# -*- coding: utf-8 -*-
"""
The रु of 8.2.66 and everything that becomes of it — the visarga, the य्, the उ,
the स् and the ष् — with the s/r-final padas that lead there.

    8.2.62–81   the end of a word: रु, र्, द्, न्      (8.2.66–71 done; the rest
                                                        below in COVERAGE)
    8.3.8–22    the रु from a न्; ro ri; the visarga; the य् and its fates
    8.3.34–54   what the visarga becomes before a खर्
    6.1.113–114 the रु as उ            6.3.111  the loss and the long vowel
    6.1.132–135 the loss of the सु of एतद् and तद्

**One sound, many fates, decided by what stands beside it.** A pada-final स्
becomes a रु (8.2.66) — a र् whose उ is an इत् and is lost, so what the engine
carries is a र् marked `RU`. Before a short अ, or a soft consonant, after a
short अ, that रु is an उ (6.1.113–114). Before a र् it is lost (8.3.14) and the
vowel before it lengthens (6.3.111). Before a खर् or a pause it is the visarga
(8.3.15) and the visarga is a स् (8.3.34), a ष् (8.3.39–48), a जिह्वामूलीय or an
उपध्मानीय (8.3.37) or stays (8.3.35–36). After अ or आ and before an अश् it is a
य् (8.3.17), which may be a lighter य् (8.3.18) or lost (8.3.19–22).

**The ordering is the whole point, and each ordering is asked of the tradition.**
8.2.66 stands in the tripādī, 6.1.113 in the सपादसप्ताध्यायी — so 8.2.1 hides the
रु from 6.1.113, and 6.1.113 *names* the रु and would be empty if hidden: that is
`consumes=(RU,)` (वचनप्रामाण्यात्). 8.3.14 competes with 6.1.114 for the रु of
*manoratha* and loses to it by 8.2.1 (the Laghusiddhāntakaumudī's
*पूर्वत्रासिद्धमिति रोरीत्यस्यासिद्धत्वादुत्वमेव*): the engine says so by 8.2.1 and
not by a line in this file. 6.3.111 names the loss 8.3.13–14 make (`consumes`).
8.2.66 displaces 8.2.39 (जश्त्वापवादः, Kaumudī). Where an अपवाद is stated in the
tradition the rule carries it in `overrides`, with the words quoted (`_q`), and a
test reads every quotation from the corpus.

**What the letters cannot say is a flag** (NORTH_STAR §5) — the caller's word,
never a guess. Flags this family reads, beyond the README's closed vocabulary:

    pluta          the last vowel of this word is pluta (6.1.113–114)
    stem:etad  stem:tad  stem:tyad  stem:ahan      what the word is a form of
    akac           the word carries the affix क (सकच्, 6.1.132 अकोः)
    nan_samasa     a नञ्-compound (6.1.132)         padapuranam   (6.1.134)
    sakatayana     offer Śākaṭāyana's lighter य्/व् (8.3.18) — silent otherwise
    saptamibahuvacana   the word is the locative plural सु (8.3.16)
    sup            the word is a सुप् (8.2.68–69)   amredita  a repeated word (8.3.12)
    dhatu  bha  kvasu     the word ends in a dhātu / is a भ / ends in क्वसु
    pratyaya       the word is an affix, not a पद (8.3.38–39 अपदादौ)
    gati  avyaya   (also implied by nipata, upasarga: 1.1.37, 1.4.58)  8.3.38–47
    apratyaya      the final स्/र् is not an affix (8.3.41)   isus   (8.3.44–45)
    krtvo_artha    a numeral adverb "times" (8.3.43)          samartha  (8.3.44)
    antahpada      this word and the next stand in one ṛk pāda (8.3.9)
    pancami  sasthi  adhyartha  mahavyahrti  dhatu:ROOT     (8.2.71, 8.3.50–54)

A **visarga is never where the grammar starts**: the parser reads a final visarga
as the स् it came from (8.2.66) unless the word carries `final:r`; the trace says
so as an assumption. This module therefore starts from स् or र्.

**Which sounds are chosen, and how.** Classes are `S.members` of a pratyāhāra,
never typed; the varga sounds are `varna.VARGA`; the pairing of 8.3.37 (कवर्ग with
जिह्वामूलीय, पवर्ग with उपध्मानीय) is 1.3.10 through `reading.yathasamkhya`.
The two letters of *व्योः* (8.3.18–22) and the letter of *ओतः* are read from the
sūtra's own words, not typed here; the wide इण् of 8.3.39 is the one the
Bālamanoramā names (*'इ' णिति परणकारेण प्रत्याहारः*). The word-lists of the
gaṇas and the sūtras (निर्, दुर्, …) are those `visarjaniya` and `ru_adesa` already
keep — asked, not retyped.

**Sūtras in this range left to other machinery, and why** — see `COVERAGE`.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Dict, Iterator, List, Optional, Sequence, Tuple

from src.astadhyayi import corpus
from src.astadhyayi.adesa import hrasva_of
from src.astadhyayi.anga import akah_savarne_dirghah
from src.astadhyayi.reading import yathasamkhya
from src.astadhyayi.ru_adesa import BHA_KUR_CHUR, UBHAYATHA_THREE, VASU_FOUR
from src.astadhyayi.sandhi import supports as S
from src.astadhyayi.sandhi.parse import to_iast, tokenize
from src.astadhyayi.sandhi.rule import (
    ADESA, LOPA, PRATISEDHA, VARTTIKA, Application, Detail, NewSeg, Via,
    delete, replace, rule, site, sk)
from src.astadhyayi.sandhi.segs import (
    AC, ANGA, HAL, PADA_LIKE, PLUTA, RU, SAMASA, Junction, Sight, View,
    base_of)
from src.astadhyayi.sandhi.trace import deva
from src.astadhyayi.sivasutra import resolve, resolve_all
from src.astadhyayi.svara import duration
from src.astadhyayi.varna import (
    JIHVAMULIYA, UPADHMANIYA, VARGA, VISARGA, savarna)
from src.astadhyayi.visarjaniya import (
    DVIS_THREE, KRKAMI_SEVEN, NIRADI, PATI_SEVEN)

# ---------------------------------------------------------------------------
# What the tradition says, quoted — and checkable
# ---------------------------------------------------------------------------

_WORKS = {
    "kashika": "Kāśikā", "kaumudi": "Siddhāntakaumudī",
    "balamanorama": "Bālamanoramā", "tattvabodhini": "Tattvabodhinī",
    "bhashya": "Mahābhāṣya", "nyaas": "Nyāsa", "padamanjari": "Padamañjarī",
    "varttika": "Vārttika",
}

#: Every quotation this module makes, as (sūtra, work, words). A test reads each
#: from the corpus and fails if one is not there — the reasons the rules give are
#: the tradition's own words, or they are not given.
QUOTED: List[Tuple[str, str, str]] = []


def _q(sutra: str, work: str, quote: str) -> str:
    """A verbatim quotation, registered for the test that checks it."""
    QUOTED.append((sutra, work, quote))
    return f"{quote} ({_WORKS[work]} on {sutra})"


def _bare(sutra: str, work: str, quote: str) -> str:
    """The quotation itself, registered for the same test — for a line of the
    commentary that a list of words is read from."""
    QUOTED.append((sutra, work, quote))
    return quote


@lru_cache(maxsize=None)
def _sutra(sutra_id: str) -> str:
    """The sūtra as the corpus has it, in IAST."""
    return corpus.load_vidyut_sutrapatha()[sutra_id].text


def _name(sutra_id: str) -> str:
    """The sūtra's own words in Devanāgarī, from the corpus — a rule's name is
    never typed."""
    return deva(_sutra(sutra_id))


def _vtext(sutra_id: str, index: int) -> str:
    """A vārttika as `corpus.varttikas_on` has it — never retyped."""
    return corpus.varttikas_on(sutra_id)[index].text.strip(" ।")


#: The vārttikas this family makes rules of. The first four are read from the
#: corpus's vārttika list; *saṃpuṃkānāṃ so vaktavyaḥ* is not there (it stands in
#: the Kaumudī's text, marked <!…!>) and is a checked quotation instead.
_VT_KHARPARE = _vtext("8.3.36", 0)
_VT_ANAVYAYA = _vtext("8.3.38", 1)
_VT_KAMYE = _vtext("8.3.38", 2)
_VT_MUHUS = _vtext("8.3.41", 0)
#: The word that vārttika excepts — *muhus*, the stem of *muhuṣaḥ* read off it.
_MUHUS = to_iast(_VT_MUHUS.split()[0])[:-len("aḥ")]
_VT_RUPARATRI = _vtext("8.2.68", 0)
_VT_AHARADI = _vtext("8.2.70", 0)
_VT_SAMPUM = "संपुंकानां सो वक्तव्यः"
_q("8.3.34", "kaumudi", _VT_SAMPUM)


#: Options, each under the sūtra's own word for it.
_VA = "वा"
_UBHAYATHA = "उभयथा"
_ANYATARASYAM = "अन्यतरस्याम्"
_SAKALYA = "शाकल्यस्य"
_SAKATAYANA = "शाकटायनस्य"
_CA = "च"
_BAHULAM = "बहुलम्"


def _own(sutra_id: str) -> str:
    """A family tag that only the *base* rule of a sūtra carries, so that a
    vārttika on the same sūtra can be named as displacing it (or displaced by
    it) without also matching itself: `Rule.overrides` names a sūtra by id, and
    a vārttika shares its sūtra's id."""
    return "sutra:" + sutra_id


def _ov(sutra_id: str) -> str:
    """The override target for a base rule (see `_own`)."""
    return "@" + _own(sutra_id)


#: The two marks this family writes on a sound (segs.RU is the third).
#: The loss 8.3.13–14 make, which 6.3.111 names in its own wording (ढ्रलोपे).
DHRA_LOPA = "ḍhra-lopa"
#: The lighter य्/व् of 8.3.18 — the same letter, uttered with less effort.
LAGHU = "laghuprayatnatara"

#: The visarga's substitutes in 8.3.34–54 — the tag the शर्परे prohibition
#: (8.3.35) displaces as a group: विकारनिवृत्त्यर्थम्.
VIKARA = "visarga_vikara"


# ---------------------------------------------------------------------------
# Small questions the rules keep asking
# ---------------------------------------------------------------------------


def _flag(v: View, sight: Sight, name: str) -> bool:
    return name in v.flags(sight)


def _text(v: View, sight: Sight) -> str:
    return v.word(sight).text


def _stem(v: View, sight: Sight) -> Optional[str]:
    return v.word(sight).flag_value("stem")


def _asked(v: View, *names: str) -> bool:
    """Some word of the input carries one of these flags. Every rule that
    rests on a flag passes over a form with none at once — the engine asks
    each rule at every turn."""
    return any(f in w.flags for w in v.state.words for f in names)


def _named(v: View, *texts: str) -> bool:
    return any(w.text in texts for w in v.state.words)


def _avarna(sound: str) -> bool:
    """अवर्ण — a sound savarṇa to अ (1.1.9), the short and the long."""
    return savarna("a", base_of(sound))


def _short_a(sight: Sight) -> bool:
    """A short अ — an अवर्ण of one mātrā (तपर, 1.1.70; `svara.duration`)."""
    return _avarna(sight.s) and duration(sight.s) == 1


def _ru(sight: Sight) -> bool:
    return sight.s == "r" and sight.has(RU)


def _from_ru(sight: Sight) -> bool:
    """This visarga was made out of a रु (8.3.15), not out of a plain र्."""
    return any(RU in p.marks for p in sight.seg.prior)


def _last_vowel_of_word(v: View, sight: Sight) -> bool:
    """No vowel of the same word stands after this sound."""
    nxt = v.next(sight)
    while nxt is not None and nxt.w == sight.w:
        if nxt.is_vowel:
            return False
        nxt = v.next(nxt)
    return True


def _pluta(v: View, sight: Sight) -> bool:
    """The vowel is pluta: a mark a rule of 8.2.82–107 has left, or the caller's
    flag on the word for its last vowel (the letters cannot say it)."""
    if PLUTA in sight.marks:
        return True
    return (sight.is_vowel and _flag(v, sight, "pluta")
            and _last_vowel_of_word(v, sight))


@lru_cache(maxsize=None)
def _svaradi() -> frozenset:
    """The words of the svarādi gaṇa (1.1.37), from the gaṇapāṭha on disk."""
    return frozenset(item for g in corpus.ganas_for("1.1.37")
                     for item in g.items)


def _avyaya(v: View, sight: Sight) -> bool:
    """
    The word is indeclinable: the caller's `avyaya`; a nipāta or an upasarga,
    which 1.1.37 स्वरादिनिपातमव्ययम् and 1.4.58 प्रादयः make one; or a word of the
    svarādi gaṇa (*prātar*, *punar*, *svar*, *śvas*) — both readings of a final
    स्/र् are tried, since a visarga does not say which it came from. The gaṇa
    is an ākṛtigaṇa, so a word missing from it proves nothing.
    """
    if any(_flag(v, sight, f) for f in ("avyaya", "nipata", "upasarga")):
        return True
    text = _text(v, sight)
    readings = {text, text[:-1] + "r"} if text.endswith("s") else {text}
    return bool(readings & _svaradi())


def _begins_pada(v: View, sight: Sight) -> bool:
    """The sound begins a पद — not an affix that follows a पद (`pratyaya`)."""
    return v.begins_word(sight) and not _flag(v, sight, "pratyaya")


def _uttarapada(v: View, sight: Sight) -> bool:
    """The sound's word is the last member of a compound (or of an earlier
    compound the same word stands at the end of)."""
    return sight.w > 0 and v.state.bounds[sight.w - 1] == SAMASA


@lru_cache(maxsize=None)
def _letters_of(sutra_id: str, stop: str) -> Tuple[str, ...]:
    """The sounds a sūtra's first word names — everything before `stop`, read
    from the sūtra's own text: *vyoḥ* names v and y."""
    return tuple(s for s, _ in tokenize(_sutra(sutra_id).partition(stop)[0]))


def _yv() -> Tuple[str, ...]:
    """व् and य् — the two letters of *व्योः* (8.3.18)."""
    return _letters_of("8.3.18", "or")


def _o() -> str:
    """ओ — the letter of *ओतः* (8.3.20)."""
    return _letters_of("8.3.20", "t")[0]


def _sounds(text: str) -> List[str]:
    return [s for s, _ in tokenize(text)]


def _form_of(text: str, item: str) -> bool:
    """`text` is a form of the word `item`: it begins with it, or with all of it
    but a final अ and then a vowel — *putra* + *āya* is *putrāya*, *pada* + *ī* is
    *padī* — the two ways a case-ending can stand after the stem."""
    if text.startswith(item):
        return True
    stem = _sounds(item)
    if stem[-1] != "a":
        return False
    have = _sounds(text)
    k = len(stem) - 1
    return len(have) > k and have[:k] == stem[:k] and have[k] in AC


def _shorten(text: str) -> str:
    """The word with every vowel short (`adesa.hrasva_of`, 1.1.48 and 1.2.27)
    — a list of words is compared in the shape it gives them, धूः and धुर्."""
    out = []
    for sound in _sounds(text):
        out.append((hrasva_of(sound) or sound) if sound in AC else sound)
    return "".join(out)


def _listed(quote: str) -> Tuple[str, ...]:
    """The words of a quoted line of the commentary, in IAST."""
    return tuple(to_iast(w) for w in quote.split())


@lru_cache(maxsize=None)
def _wide_in() -> frozenset:
    """इण् as the Bālamanoramā reads it on 8.3.57 — *'इ' णिति परणकारेण
    प्रत्याहारः*: to the LATER ण्, which is इ उ ऋ ऌ ए ओ ऐ औ ह य व र ल."""
    return frozenset(max(resolve_all("iṆ"), key=lambda r: len(r.sounds)).sounds)


def _khar() -> frozenset:
    return S.members("khaR")


def _junction_pairs(v: View) -> Iterator[Junction]:
    return iter(v.junctions())


# ---------------------------------------------------------------------------
# 8.2.66  ससजुषो रुः
# ---------------------------------------------------------------------------

#: The word whose final ष् the sūtra names beside स् — *sajuṣ*.
_SAJUS = "sajuṣ"


@rule("8.2.66", name=_name("8.2.66"), families=("visarga",),
      overrides=(("8.2.39", _q("8.2.66", "kaumudi", "जश्त्वापवादः")),))
def sasajuso_ruh(v: View):
    """
    सकारान्तस्य पदस्य सजुष् इत्येतस्य च रुर्भवति — अग्निरत्र, वायुरत्र, रामस् ⟶ रामरु.

    A pada-final स् becomes रु, whose उ is an इत् (1.3.2) and is lost (1.3.9), so
    the sound left is a र् marked `RU`. The word *sajuṣ* is named too: its final
    ष् is the sthānin (Bālamanoramā: सजुष्शब्दान्तं यत् पदं तदन्तस्य षकारस्य);
    *sajuṣau, sajuṣaḥ* keep their ष् — it does not end a pada.
    """
    for s in v.live:
        if not v.pada_final(s):
            continue
        if s.s == "s" or (s.s == "ṣ" and _text(v, s).endswith(_SAJUS)):
            yield Application(
                site=site(s),
                edits=(replace(s, NewSeg("r", frozenset({RU}), show="ru")),),
                detail=Detail(
                    kind=ADESA, sthanin=s.s, adesa="ru",
                    nimitta="the end of a pada",
                    because=(f"{sk(s.s)} ends a pada"
                             + (" ({sajuṣ})" if s.s == "ṣ" else "")
                             + ", so it is replaced by {ru} — a र् whose उ is "
                               "an इत् and is lost"),
                    via=(S.alo_antyasya(s.s),) + S.it_removed("u")))


# ---------------------------------------------------------------------------
# 6.1.113–114  the रु as उ
# ---------------------------------------------------------------------------


def _after_short_a(v: View, r: Sight) -> Optional[Sight]:
    """The अ before the रु — short, and not pluta (अप्लुतादतः, तपर 1.1.70)."""
    prev = v.prev(r)
    if prev is None or not _short_a(prev) or _pluta(v, prev):
        return None
    return prev


@rule("6.1.113", name=_name("6.1.113"), families=("visarga",),
      consumes=(RU,),
      overrides=(("8.3.17", _q("6.1.113", "kaumudi", "यत्वस्यापवादः")),))
def ato_ror_aplutad_aplute(v: View):
    """
    अप्लुतादतः परस्य रोरुः स्यादप्लुतेऽति — वृक्षोऽत्र, प्लक्षोऽत्र, शिवोऽर्च्यः.

    The Kāśikā's *kim*s: अग्निरत्र (the sound before is इ), वृक्षा अत्र (long आ —
    तपरकरणम्, so it goes to य्, 8.3.17), स्वरत्र and प्रातरत्र (a र् that is not
    the रु of 8.2.66 — सानुबन्धग्रहणम्), वृक्ष इह (the sound after is not अ),
    सुस्रोत३ अत्र (a pluta before) and तिष्ठतु पय अ३श्विन् (a pluta after).
    """
    for r in v.live:
        if not _ru(r):
            continue
        prev, nxt = _after_short_a(v, r), v.next(r)
        if prev is None or nxt is None or not _short_a(nxt) or _pluta(v, nxt):
            continue
        yield Application(
            site=site(prev, r, nxt), edits=(replace(r, "u"),),
            detail=Detail(
                kind=ADESA, sthanin="ru", adesa="u",
                nimitta="a short a before and a short a after",
                because=("the {ru} stands after a short {a}, neither pluta, "
                         "and before a short {a}, so it becomes {u}: this is "
                         "the exception to 8.3.17's य्"),
                via=(S.tapara("a"), S.alo_antyasya("ru"))))


@rule("6.1.114", name=_name("6.1.114"), families=("visarga",),
      consumes=(RU,))
def hasi_ca(v: View):
    """
    तथा रोरुः स्याद्धशि — शिवो वन्द्यः, पुरुषो याति, पुरुषो हसति, मनोरथः.

    The अतो रोरप्लुतादप्लुते of 6.1.113 runs on into this sūtra (Bālamanoramā:
    अतो रोरप्लुतादिति पदत्रयमनुवर्तते) — so the अ before is short and not pluta —
    and *haś* is what stands after. It leaves 6.1.113's own case alone: the
    engine gives it to whichever of the two the sound after belongs to.
    """
    has = S.members("haŚ")
    for r in v.live:
        if not _ru(r):
            continue
        prev, nxt = _after_short_a(v, r), v.next(r)
        if prev is None or nxt is None or nxt.s not in has:
            continue
        yield Application(
            site=site(prev, r, nxt), edits=(replace(r, "u"),),
            detail=Detail(
                kind=ADESA, sthanin="ru", adesa="u",
                nimitta=f"a short a before and the {{haś}} {sk(nxt.s)} after",
                because=(f"the {{ru}} stands after a short {{a}} and before "
                         f"the {{haś}} {sk(nxt.s)}, so it becomes {{u}}"),
                via=(S.tapara("a"), S.alo_antyasya("ru"))))


# ---------------------------------------------------------------------------
# 6.1.132–135  the सु of एतद् and तद्
# ---------------------------------------------------------------------------


def _etattad(v: View, s: Sight) -> bool:
    """The word is a form of एतद् or तद् (its सु is the final स्): the caller's
    `stem:etad` / `stem:tad`, or the two nominative forms *eṣas*, *sas*."""
    stem = _stem(v, s)
    return stem in ("etad", "tad") or _text(v, s) in ("eṣas", "sas")


@rule("6.1.132", name=_name("6.1.132"), families=("visarga",))
def etattadoh_sulopo(v: View):
    """
    अककारयोरेतत्तदोर्यः सुस्तस्य लोपः स्याद्धलि न तु नञ्समासे — एष विष्णुः, स शंभुः.

    The सु is the pada-final स् of *eṣas*, *sas*. Kāśikā's *kim*s: एतत्तदोः किम्?
    यो ददाति (no एतद्/तद्); अकोः किम्? एषको ददाति (the सकच् form — flag
    `akac`); अनञ्समासे किम्? असः शिवः (flag `nan_samasa`); हलि किम्? एषोऽत्र
    (a vowel follows, so the स् goes on to be a रु and an उ, 8.2.66 and 6.1.113).
    """
    for j in v.junctions():
        s, nxt = j.left, j.right
        if s.s != "s" or j.kind not in PADA_LIKE or nxt.s not in HAL:
            continue
        if not (v.pada_final(s) and _etattad(v, s)):
            continue
        if _flag(v, s, "akac") or _flag(v, s, "nan_samasa"):
            continue
        yield Application(
            site=site(s, nxt), edits=(delete(s),),
            detail=Detail(
                kind=LOPA, sthanin="s", adesa="",
                nimitta=f"the consonant {sk(nxt.s)} follows",
                because=(f"the final {{s}} of {sk(_text(v, s))} is the {{su}} of "
                         f"a form of {{etad}} or {{tad}} (neither ending in "
                         f"{{ka}} nor a {{nañ}}-compound), and the consonant "
                         f"{sk(nxt.s)} follows, so it is lost"),
                via=(S.samhita_condition(),)))


@rule("6.1.133", name=_name("6.1.133"), families=("visarga",), vedic=True)
def syas_chandasi_bahulam(v: View):
    """
    स्य इत्येतस्य छन्दसि हलि परतो बहुलं सोर्लोपो भवति — एष स्य भानुः.

    Vedic. *बहुलम्* — sometimes, and sometimes not (Kāśikā: न च भवति — यत्र स्यो
    निपतेत्); the engine offers both courses.
    """
    for j in v.junctions():
        s, nxt = j.left, j.right
        if s.s != "s" or j.kind not in PADA_LIKE or nxt.s not in HAL:
            continue
        if not (v.pada_final(s) and (_text(v, s) == "syas"
                                     or _stem(v, s) == "tyad")):
            continue
        yield Application(
            site=site(s, nxt), edits=(delete(s),), optional=_BAHULAM,
            detail=Detail(
                kind=LOPA, sthanin="s", adesa="",
                nimitta=f"the consonant {sk(nxt.s)} follows",
                because=(f"in the Veda the final {{s}} of {{sya}} may be lost "
                         f"before the consonant {sk(nxt.s)} ({{bahulam}}: it is "
                         f"also heard)"),
                via=(S.samhita_condition(),)))


@rule("6.1.134", name=_name("6.1.134"), families=("visarga",))
def so_aci_lope_cet_padapuranam(v: View):
    """
    सस् इत्यस्य सोर्लोपः स्यादचि पादश्चेल्लोपे सत्येव पूर्येत — सेमामविड्ढि प्रभृतिम्,
    सैष दाशरथी रामः.

    *पादपूरणम्* — that the pāda is filled up only if the loss takes place — is
    metre, and no reading of the letters says it: it is the flag `padapuranam`
    on the word (NORTH_STAR §5). Without it the स् goes on to be a रु
    (Kāśikā: लोपे चेत् पादपूरणमिति किम्? स इव व्याघ्रो भवेत्).
    """
    for j in v.junctions():
        s, nxt = j.left, j.right
        if s.s != "s" or j.kind not in PADA_LIKE or not nxt.is_vowel:
            continue
        if not (v.pada_final(s) and _text(v, s) == "sas"
                and _flag(v, s, "padapuranam")):
            continue
        yield Application(
            site=site(s, nxt), edits=(delete(s),),
            detail=Detail(
                kind=LOPA, sthanin="s", adesa="",
                nimitta=f"the vowel {sk(nxt.s)} follows",
                because=(f"the final {{s}} of {{sa}} is the {{su}}, a vowel "
                         f"follows, and the caller says the pāda is filled "
                         f"only if it is lost, so it is lost"),
                via=(S.samhita_condition(),)))


# ---------------------------------------------------------------------------
# 8.3.13–14  ḍho ḍhe lopaḥ, ro ri — and 6.3.111 which names the loss
# ---------------------------------------------------------------------------


@rule("8.3.13", name=_name("8.3.13"), families=("visarga",))
def dho_dhe_lopah(v: View):
    """
    ढकारस्य ढकारे लोपो भवति — लीढम्, मीढम्, उपगूढम्, तृढः.

    The sūtra stands under पदस्य, but a ढ् cannot end a pada and stay one before
    another ढ् (the Kāśikā reads it of a ढ् *not* at the end of a pada:
    सत्यपि पदाधिकारे तस्यासंभवादपदान्तस्य ढकारस्यायं लोपो विज्ञायते); *śvaliḍ
    ḍhaukate* has lost its first ढ् to 8.2.39 before this rule is reached.
    """
    for j in v.pairs():
        if j.left.s != "ḍh" or j.right.s != "ḍh" or v.pada_final(j.left):
            continue
        yield Application(
            site=site(j.left, j.right), edits=(delete(j.left, DHRA_LOPA),),
            detail=Detail(
                kind=LOPA, sthanin="ḍh", adesa="",
                nimitta="a {ḍh} follows",
                because=("a {ḍh} that does not end a pada is lost before "
                         "another {ḍh}; the loss is what 6.3.111 names"),
                via=()))


@rule("8.3.14", name=_name("8.3.14"), families=("visarga",))
def ro_ri(v: View):
    """
    रेफस्य रेफे परतो लोपो भवति — पुना रक्तं वासः, हरी रम्यः, नीरक्तम्, दूरक्तम्.

    पदस्येत्यत्र विशेषणे षष्ठी (Kāśikā): any र् of the pada, so the र् of an aṅga
    before a र् too, not only a pada-final one. It is the रु of 8.2.66 or a
    plain र् (*punar*). **It competes with 6.1.114 for the रु of *manoratha* and
    loses**: 8.3.14 is asiddha to 6.1.114 (8.2.1) — the engine settles it and the
    trace says so.
    """
    for j in v.junctions():
        if j.left.s != "r" or j.right.s != "r":
            continue
        yield Application(
            site=site(j.left, j.right), edits=(delete(j.left, DHRA_LOPA),),
            detail=Detail(
                kind=LOPA, sthanin="r", adesa="",
                nimitta="a {r} follows",
                because=("a {r} of the pada before another {r} is lost; the "
                         "loss is what 6.3.111 names"),
                via=()))


@rule("6.3.111", name=_name("6.3.111"), families=("visarga",),
      consumes=(DHRA_LOPA,))
def dhralope_purvasya_dirgho_nah(v: View):
    """
    ढ्रेफयोर्लोपनिमित्तयोः पूर्वस्याणो दीर्घः — पुना रमते, हरी रम्यः, शम्भू राजते, लीढम्.

    **The sūtra names the loss** (ढ्रलोपे), so it sees what 8.3.13–14 made though
    8.2.1 would hide it — `consumes`. *Aṇaḥ kim?* तृढः, वृढः — the ऋ before the
    lost ढ् is no अण् (Bālamanoramā: ऋकारश्चात्र अण्ग्रहणे न गृह्यते, so the अण्
    is the narrow अ इ उ). Only the sound immediately before is lengthened
    (1.1.66), by the same rule that lengthens the 'alike' pair of 6.1.101.
    """
    sights = list(v.sights)
    for index, lost in enumerate(sights):
        if not lost.seg.elided or DHRA_LOPA not in lost.marks or index == 0:
            continue
        before = sights[index - 1]
        if before.seg.elided or not S.is_member(before.s, "aṆ"):
            continue
        got = akah_savarne_dirghah(before.s, before.s)
        if got.result is None or got.result == before.s:
            continue
        yield Application(
            site=site(before, lost), edits=(replace(before, got.result),),
            detail=Detail(
                kind=ADESA, sthanin=before.s, adesa=got.result,
                nimitta="a {ḍh} or {r} has just been lost after it",
                because=(f"{sk(before.s)} is an {{aṇ}} and the ढ् or र् after "
                         f"it has been lost, so it is lengthened to "
                         f"{sk(got.result)}"),
                via=(S.pratyahara("aṆ", "a, i, u"),
                     S.saptami_purva("{ḍhra}-lopa"))))


# ---------------------------------------------------------------------------
# 8.3.15–16  the visarga, and the restriction before सु
# ---------------------------------------------------------------------------


def _su_follows(v: View, nxt: Optional[Sight]) -> bool:
    """The sound after is the स् of the locative plural सु (8.3.16)."""
    return (nxt is not None and nxt.s == "s" and v.begins_word(nxt)
            and _flag(v, nxt, "saptamibahuvacana"))


@rule("8.3.15", name=_name("8.3.15"), families=("visarga",))
def kharavasanayor_visarjaniyah(v: View):
    """
    रेफान्तस्य पदस्य खरि परतोऽवसाने च विसर्जनीयादेशो भवति — वृक्षश्छादयति,
    वृक्षस्तरति, वृक्षः, प्लक्षः.

    *Kharavasānayoriti kim?* अग्निर्नयति, वायुर्नयति — the sound after is neither
    a खर् nor a pause. The र् is the रु of 8.2.66 or a plain र् (*punar*). A र् that
    is only the middle of a longer sound (*महर्षि*, 6.1.85) is not pada-final for
    a rule that rests on the sounds. Before सु the niyama of 8.3.16 lets only the
    रु be a visarga — and the step says so.
    """
    khar = _khar()
    for r in v.live:
        if r.s != "r" or not v.pada_final(r):
            continue
        nxt = v.next(r)
        if not (v.at_pause(r) or (nxt is not None and nxt.s in khar)):
            continue
        via = [S.alo_antyasya("r")]
        if nxt is None:
            via.append(S.avasana_condition())
        elif _su_follows(v, nxt) and _ru(r):
            via.append(Via("8.3.16", "the रु is the one र् that is a visarga "
                                     "before the locative plural {su}"))
        yield Application(
            site=site(r, nxt) if nxt is not None else site(r),
            edits=(replace(r, VISARGA),),
            detail=Detail(
                kind=ADESA, sthanin="r", adesa=VISARGA,
                nimitta=("a pause follows" if nxt is None
                         else f"the {{khar}} {sk(nxt.s)} follows"),
                because=("the pada ends in {r} and " + (
                    "a pause follows" if nxt is None
                    else f"{sk(nxt.s)} is a {{khar}}") + ", so it becomes "
                    "the visarga"),
                via=tuple(via)))


@rule("8.3.16", name=_name("8.3.16"), families=("visarga",),
      overrides=(("8.3.15", _q("8.3.16", "kashika",
                               "रोरेव सुपि विसर्जनीयादेशः, नान्यस्य")),))
def ro_supi(v: View):
    """
    सप्तमीबहुवचने परे रोरेव विसर्जनीयो नान्यरेफस्य — पयःसु, यशःसु; गीर्षु, धूर्षु.

    A niyama: 8.3.15 would make any pada-final र् before the स् of सु a visarga,
    and this sūtra says only the रु — so a plain र् (*gir*) before सु is refused.
    It is a refusal, an application with no edit at the very place of 8.3.15's.
    *Supi* is the locative plural ending (Kāśikā: सुपीति सप्तमीबहुवचनं गृह्यते),
    which the letters do not say — the flag `saptamibahuvacana`.
    """
    for r in v.live:
        if r.s != "r" or _ru(r) or not v.pada_final(r):
            continue
        nxt = v.next(r)
        if not _su_follows(v, nxt):
            continue
        yield Application(
            site=site(r, nxt), edits=(),
            detail=Detail(
                kind=PRATISEDHA, sthanin="r", adesa="",
                nimitta="the locative plural {su} follows",
                because=("this {r} is not the {ru} of 8.2.66, and before the "
                         "locative plural {su} only the {ru} becomes a "
                         "visarga — so the visarga of 8.3.15 is refused"),
                via=()))


# ---------------------------------------------------------------------------
# 8.3.17–22  the य् and its fates
# ---------------------------------------------------------------------------

#: The three words 8.3.17 names before the रु — भोस्, भगोस्, अघोस् (Kaumudī:
#: भोस् भगोस् अघोस् इति सकारान्ता निपाताः).
_BHOBHAGOAGHO = _listed(_bare("8.3.17", "kaumudi", "भोस् भगोस् अघोस्"))


def _bho_word(v: View, sight: Sight) -> bool:
    return _text(v, sight) in _BHOBHAGOAGHO


def _yv_after_a_or_bho(v: View, y: Sight) -> Optional[Sight]:
    """The sound before a pada-final य्/व् that 8.3.18–22 speak of: an अवर्ण, or
    the ओ of भो, भगो, अघो. Returns it, else None."""
    if y.s not in _yv() or not v.pada_final(y):
        return None
    prev = v.prev(y)
    if prev is None:
        return None
    if _avarna(prev.s) or (prev.s == _o() and _bho_word(v, y)):
        return prev
    return None


@rule("8.3.17", name=_name("8.3.17"), families=("visarga",))
def bhobhago_yo_si(v: View):
    """
    एतत्पूर्वस्य रोर्यादेशोऽशि — देवा इह ⟶ देवायिह, भो अत्र, भगो ददाति, ब्राह्मणा ददति.

    The रु is preceded by the ओ of *bhos, bhagos, aghos* (Kaumudī: भोस् भगोस्
    अघोस् इति सकारान्ता निपाताः) or by an अवर्ण; an अश् follows. *Kim*s: अग्निरत्र
    (इ before), *ro ity eva* प्रातरत्र (a plain र्), *aśi kim?* देवाः सन्ति (a खर् —
    the visarga of 8.3.15, not a य्). An अ before and an अ after is 6.1.113's
    (that sūtra displaces this one); a short अ before a हश् is 6.1.114's.
    """
    ash = S.members("aŚ")
    for r in v.live:
        if not _ru(r):
            continue
        prev, nxt = v.prev(r), v.next(r)
        if prev is None or nxt is None or nxt.s not in ash:
            continue
        bho = prev.s == _o() and _bho_word(v, r)
        if not (bho or _avarna(prev.s)):
            continue
        via: List[Via] = []
        if not bho and prev.s != "a":
            via.append(S.savarna_of("a", prev.s))
        yield Application(
            site=site(prev, r, nxt), edits=(replace(r, "y"),),
            detail=Detail(
                kind=ADESA, sthanin="ru", adesa="y",
                nimitta=(f"{sk(prev.s)} before"
                         + (" (of a word named in the sūtra)" if bho else "")
                         + f" and the {{aś}} {sk(nxt.s)} after"),
                because=(f"the {{ru}} follows "
                         + ("the {o} of " + sk(_text(v, r)) if bho
                            else f"{sk(prev.s)}, an {{avarṇa}},")
                         + f" and the {{aś}} {sk(nxt.s)} comes after it, so it "
                         f"becomes {{y}}"),
                via=tuple(via) + (S.alo_antyasya("ru"),)))


def _lighter(v: View, y: Sight) -> bool:
    return LAGHU in y.marks


@rule("8.3.18", name=_name("8.3.18"), families=("visarga",))
def vyor_laghuprayatnatarah(v: View):
    """
    वकारयकारयोः पदान्तयोर्लघुप्रयत्नतर आदेशो भवत्यशि परतः शाकटायनस्य मतेन — भोयत्र,
    कयास्ते, अस्मायुद्धर, द्वावत्र.

    The substitute is the same letter, uttered with less effort (Kāśikā:
    लघुप्रयत्नतरत्वमुच्चारणे स्थानकरणशैथिल्यम्); *āntaratamya* gives य् for य् and
    व् for व् (Nyāsa: उदाहरणेष्वान्तरतम्याद्वकारस्य वकार एव भवति, यकारस्य यकार
    एव). **Written it is the very letter it replaces**, so it changes no spelling
    and doubles every derivation of every अवर्ण + रु + अश् meeting: the engine offers
    it only where the caller asks for Śākaṭāyana's reading, `{sakatayana}` on
    any word — the same decision the prakṛtibhāva family takes for Śākalya's
    options. It is an option (Nyāsa on 8.3.19: three courses — the lighter
    sound, the loss, neither); the lighter sound is not then lost by 8.3.19.
    """
    if not _asked(v, "sakatayana"):
        return
    ash = S.members("aŚ")
    for y in v.live:
        prev = _yv_after_a_or_bho(v, y)
        if prev is None or _lighter(v, y):
            continue
        nxt = v.next(y)
        if nxt is None or nxt.s not in ash:
            continue
        yield Application(
            site=site(prev, y, nxt),
            edits=(replace(y, NewSeg(y.s, frozenset({LAGHU}),
                                     show=y.s + "̆")),),
            optional=_SAKATAYANA,
            detail=Detail(
                kind=ADESA, sthanin=y.s, adesa=y.s + " (laghuprayatnatara)",
                nimitta=f"{sk(prev.s)} before and the {{aś}} {sk(nxt.s)} after",
                because=(f"{sk(y.s)} ends the pada after {sk(prev.s)} and the "
                         f"{{aś}} {sk(nxt.s)} follows, so by Śākaṭāyana's "
                         f"opinion it is uttered with less effort — the same "
                         f"letter, lighter"),
                via=(S.antaratama(y.s, y.s, "the lighter sounds"),)))


@rule("8.3.19", name=_name("8.3.19"), families=("visarga",))
def lopah_sakalyasya(v: View):
    """
    अवर्णपूर्वयोः पदान्तयोर्यवयोर्लोपो वाशि परे — हर इह, हरयिह; क आस्ते, कयास्ते;
    द्वा अत्र, द्वावत्र.

    An option (शाकल्यग्रहणं विभाषार्थम् — Kāśikā): the loss, or the letter heard.
    It is not otherwise got, so the nitya sūtras that follow displace it
    (8.3.21 विकल्पनिवृत्त्यर्थम्; 8.3.22). **The loss is asiddha to the sandhi of
    vowels** (8.2.1): after *hara iha* has lost its य्, 6.1.87 still sees it —
    the two vowels are not joined. *Avarṇapūrvayoḥ kim?* दध्यत्र, मध्वत्र (इ, उ
    before). *Aśi kim?* वृक्षव् करोति (a खर्).
    """
    ash = S.members("aŚ")
    for y in v.live:
        if y.s not in _yv() or not v.pada_final(y) or _lighter(v, y):
            continue
        prev = v.prev(y)
        if prev is None or v.word(prev) != v.word(y) or not _avarna(prev.s):
            continue
        nxt = v.next(y)
        if nxt is None or nxt.s not in ash:
            continue
        yield Application(
            site=site(prev, y, nxt), edits=(delete(y),),
            optional=_SAKALYA,
            detail=Detail(
                kind=LOPA, sthanin=y.s, adesa="",
                nimitta=f"{sk(prev.s)} before and the {{aś}} {sk(nxt.s)} after",
                because=(f"a pada-final {sk(y.s)} after {sk(prev.s)}, an "
                         f"{{avarṇa}}, and before the {{aś}} {sk(nxt.s)} may "
                         f"be lost, by Śākalya's opinion"),
                via=()))


@rule("8.3.20", name=_name("8.3.20"), families=("visarga",))
def oto_gargyasya(v: View):
    """
    ओकारादुत्तरस्य यकारस्य लोपो भवति गार्ग्यस्य मतेनाशि परतः — भो अत्र, भगो अत्र.

    Nitya (नित्यार्थोऽयमारम्भः; गार्ग्यग्रहणं पूजार्थम् — an honour, not a dissent).
    It removes the *loss-option* of 8.3.19 for such a य्, **but not the lighter य्**:
    Kāśikā — लघुप्रयत्नतरस्तु भवत्येव यकारः, भो अत्र, भोयत्र. Only य् can stand after
    ओ (a व् cannot). *Padāntasya kim?* तोयम् (the य् is inside the word).
    """
    ash = S.members("aŚ")
    y_letter = _yv()[1]
    for y in v.live:
        if y.s != y_letter or not v.pada_final(y) or _lighter(v, y):
            continue
        prev = v.prev(y)
        if prev is None or v.word(prev) != v.word(y) or prev.s != _o():
            continue
        nxt = v.next(y)
        if nxt is None or nxt.s not in ash:
            continue
        yield Application(
            site=site(prev, y, nxt), edits=(delete(y),),
            detail=Detail(
                kind=LOPA, sthanin=y.s, adesa="",
                nimitta=f"{sk(prev.s)} before and the {{aś}} {sk(nxt.s)} after",
                because=(f"the pada-final {sk(y.s)} stands after the {{o}} and "
                         f"before the {{aś}} {sk(nxt.s)}, so by Gārgya's "
                         f"opinion — always — it is lost"),
                via=()))


def _un(v: View, sight: Sight) -> bool:
    """The word is the particle उञ् — the letter उ said to be a particle (the
    letters alone do not say it)."""
    return (v.begins_word(sight) and _text(v, sight) == "u"
            and (_flag(v, sight, "nipata") or _stem(v, sight) == "uñ"))


@rule("8.3.21", name=_name("8.3.21"), families=("visarga",),
      overrides=(("8.3.19", _q("8.3.21", "balamanorama",
                               "लोपश्शाकल्यस्येति विकल्पनिवृत्त्यर्थमिदम्")),))
def unci_ca_pade(v: View):
    """
    अवर्णपूर्वयोर्व्योः पदान्तयोर्लोपो भवत्युञि च पदे परतः — स उ एकाग्निः.

    Nitya: it is there to take away the option of 8.3.19 (Bālamanoramā:
    लोपश्शाकल्यस्येति विकल्पनिवृत्त्यर्थमिदम्). The particle उञ् is the caller's
    word (`nipata`), the letter alone is not enough. *Pade kim?* तन्त्रयुतम् — the
    उ there is not a पद. OPEN: whether the lighter sound of 8.3.18 survives before
    उञ् as it does before अश् after ओ (8.3.20) — the sources are silent; taken so.
    """
    y_or_v = _yv()
    for y in v.live:
        if y.s not in y_or_v or not v.pada_final(y) or _lighter(v, y):
            continue
        prev = v.prev(y)
        if prev is None or not _avarna(prev.s):
            continue
        nxt = v.next(y)
        if nxt is None or not _un(v, nxt):
            continue
        yield Application(
            site=site(prev, y, nxt), edits=(delete(y),),
            detail=Detail(
                kind=LOPA, sthanin=y.s, adesa="",
                nimitta=f"{sk(prev.s)} before and the particle {{uñ}} after",
                because=(f"the pada-final {sk(y.s)} stands after "
                         f"{sk(prev.s)}, an {{avarṇa}}, and the particle "
                         f"{{uñ}} follows, so it is lost, always"),
                via=()))


@rule("8.3.22", name=_name("8.3.22"), families=("visarga",),
      overrides=(
          ("8.3.18", _q("8.3.22", "kashika",
                        "सर्वेषांग्रहणं शाकटायनस्यापि लोपो यथा स्यात्, "
                        "लघुप्रयत्नतरो मा भूदिति")),
          ("8.3.19", _q("8.3.22", "kaumudi",
                        "भोभगोअघोअपूर्वस्य लघ्वलघूच्चारणस्य यकारस्य लोपः "
                        "स्याद्धलि सर्वेषां मतेन")),
          ("8.3.20", _q("8.3.22", "kaumudi",
                        "भोभगोअघोअपूर्वस्य लघ्वलघूच्चारणस्य यकारस्य लोपः "
                        "स्याद्धलि सर्वेषां मतेन"))))
def hali_sarvesam(v: View):
    """
    भोभगोअघोअपूर्वस्य लघ्वलघूच्चारणस्य यकारस्य लोपः स्याद्धलि सर्वेषां मतेन — भो देवाः,
    भगो नमस्ते, अघो याहि, देवा नम्याः, ब्राह्मणा ददति.

    Before a consonant that is an अश् — a हश् (*aśi* runs on: Bālamanoramā,
    अशात्मके हलीति भाष्ये) — the loss is agreed by all, the lighter य् too, and
    it is always. Only the य्: Bālamanoramā — वकारस्त्वत्र नानुवर्तते. *Hali kim?*
    देवायिह (a vowel — 8.3.19's option). *Vṛkṣav karoti* keeps its व् (a खर्).
    """
    has = S.members("haŚ")
    y_letter = _yv()[1]
    for y in v.live:
        if y.s != y_letter or not v.pada_final(y):
            continue
        prev = _yv_after_a_or_bho(v, y)
        if prev is None:
            continue
        nxt = v.next(y)
        if nxt is None or nxt.s not in has:
            continue
        yield Application(
            site=site(prev, y, nxt), edits=(delete(y),),
            detail=Detail(
                kind=LOPA, sthanin=y.s, adesa="",
                nimitta=f"{sk(prev.s)} before and the {{haś}} {sk(nxt.s)} after",
                because=(f"the pada-final {sk(y.s)} stands after "
                         f"{sk(prev.s)} and before the consonant "
                         f"{sk(nxt.s)}, so every teacher agrees it is lost — "
                         f"whether or not it is the lighter sound"),
                via=()))




# ---------------------------------------------------------------------------
# 8.3.34–37  what the visarga becomes before a खर्
# ---------------------------------------------------------------------------


def _ku_pu() -> frozenset:
    """कवर्ग and पवर्ग — the sounds 8.3.37 names, from `varna.VARGA`."""
    return frozenset(VARGA["ku"]) | frozenset(VARGA["pu"])


def _visarga_before(v: View, sounds) -> Iterator[Junction]:
    """The junctions whose left sound is a visarga and whose right sound is one
    of `sounds`. A visarga *inside* a word is not offered (README: interiors)."""
    if not any(s.s == VISARGA for s in v.live):
        return
    for j in v.junctions():
        if j.left.s == VISARGA and j.right.s in sounds:
            yield j


def _to(j: Junction, sound: str, nimitta: str, because: str, *,
        via: Tuple[Via, ...] = (), optional: str = "",
        authority: str = "sūtra", varttika: str = "") -> Application:
    """The visarga replaced by `sound` — one shape for the many rules of
    8.3.34–54 that do it."""
    return Application(
        site=site(j.left, j.right), edits=(replace(j.left, sound),),
        optional=optional,
        detail=Detail(kind=ADESA, sthanin=VISARGA, adesa=sound,
                      nimitta=nimitta, because=because, via=via,
                      authority=authority, varttika=varttika))


def _keep(j: Junction, nimitta: str, because: str, *, optional: str = "",
          authority: str = "sūtra", varttika: str = "") -> Application:
    """A refusal: the visarga is left as it is. It has NO edit and the SAME
    site as the rule it refuses (README, *A refusal is an application with no
    edits*)."""
    return Application(
        site=site(j.left, j.right), edits=(), optional=optional,
        detail=Detail(kind=PRATISEDHA, sthanin=VISARGA, adesa="",
                      nimitta=nimitta, because=because, via=(),
                      authority=authority, varttika=varttika))


def _before_khar(j: Junction) -> str:
    return f"the {{khar}} {sk(j.right.s)} follows"


@rule("8.3.34", name=_name("8.3.34"),
      families=("visarga", VIKARA, _own("8.3.34")))
def visarjaniyasya_sah(v: View):
    """
    खरि परे विसर्जनीयस्य सः — वृक्षश्छादयति, वृक्षस्तरति, विष्णुस्त्राता.

    *Khari* runs down from 8.3.15 by *maṇḍūkaplutyā* (Bālamanoramā), so a pause
    does not qualify — वृक्षः, प्लक्षः (Bhāṣya: संहितायामिति वर्तते, and the
    visarga of a pause has nothing after it). **Before a कवर्ग or पवर्ग sound
    this sūtra is not the rule at all**: 8.3.37 is its अपवाद (Kaumudī: येन
    नाप्राप्त इति न्यायेन), and what 8.3.37 brings back with its *ca* is the
    visarga, never the स् — so the field is left to it entirely (नाप्राप्ते यो
    विधिरारभ्यते स तस्यापवादः: the utsarga does not return when the apavāda's
    own option is declined).
    """
    kupu = _ku_pu()
    for j in _visarga_before(v, _khar()):
        if j.right.s in kupu:
            continue
        yield _to(j, "s", _before_khar(j),
                  f"the visarga stands before the {{khar}} {sk(j.right.s)}, "
                  f"so it becomes {{s}}")


@rule("8.3.34", name=_VT_SAMPUM, authority=VARTTIKA,
      varttika=_VT_SAMPUM, families=("visarga", VIKARA),
      overrides=(
          (_ov("8.3.36"), _q("8.3.34", "balamanorama",
                             "पाक्षिकविसर्गबाधनार्थमिति भावः")),
          ("8.3.37", _q("8.3.12", "balamanorama",
                        "संपुंकाना॑मिति सत्वमित्यर्थः"))))
def sampumkanam_so_vaktavyah(v: View):
    """
    संपुंकानां सो वक्तव्यः — संस्स्कर्ता, पुंस्कोकिलः, कांस्कान्.

    Vārttika. Of *sam*, *pum* and *kān* the visarga is always स्: it takes away
    the optional visarga of 8.3.36 (Bālamanoramā: पाक्षिकविसर्गबाधनार्थम्) and the
    कवर्ग/पवर्ग substitutes of 8.3.37 (*8.3.34 का बाधित्वा कुप्वोः प्राप्तौ
    संपुंकानाम् इति सत्वम्*). The three words are those the Bālamanoramā lists:
    सम् पुम्-कान्-एतेषां विसर्गस्य सकारो वक्तव्य इत्यर्थः.
    """
    words = tuple(w.replace("ṃ", "m") for w in _listed(_bare(
        "8.3.34", "balamanorama",
        "सम् पुम्-कान्-एतेषां विसर्गस्य सकारो वक्तव्य इत्यर्थः").split(
            "एतेषां")[0].replace("-", " ")))
    for j in _visarga_before(v, _khar()):
        if _text(v, j.left).replace("ṃ", "m") not in words:
            continue
        yield _to(j, "s", _before_khar(j),
                  f"the visarga belongs to {sk(_text(v, j.left))}, one of "
                  f"{{sam}}, {{pum}}, {{kān}}, whose visarga is always "
                  f"{{s}} before a {{khar}}",
                  authority=VARTTIKA, varttika=_VT_SAMPUM)


def _sar() -> frozenset:
    return S.members("śaR")


@rule("8.3.35", name=_name("8.3.35"), families=("visarga",),
      overrides=(
          ("8.3.37", _q("8.3.37", "kashika",
                        "पूर्वत्रासिद्धे नास्ति विप्रतिषेधोऽभावादुत्तरस्येति")),
          (_ov("8.3.34"), _q("8.3.35", "tattvabodhini", "सत्वादेरयमपवादः")),
          ("@" + VIKARA, _q("8.3.35", "kashika",
                            "नेति वक्तव्ये विसर्जनीयस्य "
                            "विसर्जनीयादेशविधानं विकारनिवृत्त्यर्थम्"))))
def sarpare_visarjaniyah(v: View):
    """
    शर्परे खरि परतो विसर्जनीयस्य विसर्जनीयादेशो भवति — शशः क्षुरम्, पुरुषः क्षुरम्,
    अद्भिः प्सातम्, वासः क्षौमम्, पुरुषः त्सरुः.

    The visarga is 'replaced by the visarga', which is a prohibition that takes
    away *every* change of it (Kāśikā: विकारनिवृत्त्यर्थम्; so no जिह्वामूलीय or
    उपध्मानीय either). It displaces 8.3.34 (सत्वादेरयमपवादः), and **it also
    wins over 8.3.37**, which stands later in the tripādī: पूर्वत्रासिद्धे नास्ति
    विप्रतिषेधोऽभावादुत्तरस्य — the engine records the refusal at the very place
    of the rules it refuses, so neither is offered there again.
    """
    khar, sar = _khar(), _sar()
    for j in _visarga_before(v, khar):
        after = v.next(j.right)
        if after is None or after.s not in sar:
            continue
        yield _keep(j, f"the {{khar}} {sk(j.right.s)} is followed by the "
                       f"{{śar}} {sk(after.s)}",
                    f"a {{śar}} ({sk(after.s)}) comes after the {{khar}} "
                    f"{sk(j.right.s)}, so the visarga is 'replaced' by "
                    f"itself: it stays, and no other substitute is made")


@rule("8.3.36", name=_name("8.3.36"), families=("visarga", _own("8.3.36")),
      overrides=((_ov("8.3.34"), _q("8.3.34", "kaumudi",
                                   "पाक्षिके विसर्गे प्राप्ते")),))
def va_sari(v: View):
    """
    शरि परे विसर्जनीयस्य विसर्जनीय एव वा स्यात् — हरिः शेते, हरिश्शेते.

    Optional (*vā*): the visarga stays, or 8.3.34 makes it a स् — a course the
    engine also returns, since declining an option leaves the general rule
    free (a विभाषा displacing a rule already got).
    """
    for j in _visarga_before(v, _sar()):
        yield _keep(j, f"the {{śar}} {sk(j.right.s)} follows",
                    f"the {{śar}} {sk(j.right.s)} follows, so the visarga may "
                    f"stay as it is instead of becoming {{s}}",
                    optional=_VA)


@rule("8.3.36", name=_VT_KHARPARE,
      authority=VARTTIKA, varttika=_VT_KHARPARE,
      families=("visarga",),
      overrides=(
          (_ov("8.3.36"), _q("8.3.36", "kaumudi",
                             "पक्षे विसर्गे सत्वे च त्रैरूप्यम्")),
          (_ov("8.3.34"), _q("8.3.36", "kaumudi",
                             "पक्षे विसर्गे सत्वे च त्रैरूप्यम्"))))
def kharpare_sari_va_visargalopah(v: View):
    """
    खर्परे शरि वा विसर्गलोपो वक्तव्यः — वृक्षा स्थातारः, वृक्षाः स्थातारः,
    वृक्षास्स्थातारः.

    Vārttika. Where the शर् is itself followed by a खर् the visarga may also be
    lost — three courses (Kaumudī: पक्षे विसर्गे सत्वे च त्रैरूप्यम्).
    """
    khar = _khar()
    for j in _visarga_before(v, _sar()):
        after = v.next(j.right)
        if after is None or after.s not in khar:
            continue
        # The site takes in the खर् after the शर् — which this vārttika reads
        # and 8.3.36 does not — so that declining the vārttika's option is not
        # also declining 8.3.36's (the engine keys a declined option by sūtra
        # and site, and a vārttika has its sūtra's number).
        yield Application(
            site=site(j.left, j.right, after), edits=(delete(j.left),),
            optional=_VA,
            detail=Detail(
                kind=LOPA, sthanin=VISARGA, adesa="",
                nimitta=f"the {{śar}} {sk(j.right.s)} with the {{khar}} "
                        f"{sk(after.s)} after it",
                because=f"the {{śar}} {sk(j.right.s)} is followed by the "
                        f"{{khar}} {sk(after.s)}, so the visarga may be lost",
                via=(), authority=VARTTIKA, varttika=_VT_KHARPARE))


@rule("8.3.37", name=_name("8.3.37"),
      families=("visarga", VIKARA, _own("8.3.37")),
      overrides=((_ov("8.3.34"), _q("8.3.37", "kaumudi",
                                   "येन नाप्राप्त इति न्यायेन")),))
def kupvoh_kah_pau_ca(v: View):
    """
    कवर्गे पवर्गे च परे विसर्जनीयस्य क्रमाज्जिह्वामूलीयोपध्मानीयौ स्तः; चाद्विसर्गः —
    वृक्ष≍ करोति, वृक्षः करोति; वृक्ष≍ पचति, वृक्षः पचति.

    *Yathāsaṅkhyam* (1.3.10): the कवर्ग takes the जिह्वामूलीय, the पवर्ग the
    उपध्मानीय — the two lists are of equal length and `reading.yathasamkhya`
    pairs them. The *ca* brings back the visarga (चाद्विसर्गः), so this is an
    option between the special sound and the visarga — never the स् of 8.3.34,
    of which it is the अपवाद. (The letters ᳵक, ᳶप of the sūtra are only for
    saying the two sounds: कपावुच्चारणार्थौ.) Before a कवर्ग/पवर्ग sound that
    is followed by a शर्, 8.3.35 wins (*vāsaḥ kṣaumam*).
    """
    pairing = dict(yathasamkhya(("ku", "pu"), (JIHVAMULIYA, UPADHMANIYA)))
    for j in _visarga_before(v, _ku_pu() & _khar()):
        which = "ku" if j.right.s in VARGA["ku"] else "pu"
        sound = pairing[which]
        yield _to(j, sound, f"the {{{which}}} sound {sk(j.right.s)} follows",
                  f"the visarga stands before the {{{which}}} sound "
                  f"{sk(j.right.s)}, so it becomes {sk(sound)} — or, by the "
                  f"{{ca}}, stays a visarga",
                  via=(S.yathasamkhya("ku, pu", "ẖ, ḫ"),), optional=_CA)


# ---------------------------------------------------------------------------
# 8.3.38–48  the visarga as स् or ष् before a कवर्ग or पवर्ग sound
# ---------------------------------------------------------------------------

#: What every one of 8.3.38–48 and the Vedic 8.3.50–53 says of 8.3.37: they are
#: its exceptions. The Kāśikā (8.3.39): the *sa* of 8.3.38 and *iṇaḥ ṣaḥ* run on
#: from here; the Nyāsa (8.3.38): पूर्वस्यायमपवादः.
_APAVADA37 = (_q("8.3.39", "kashika", "इत उत्तरं स इति, इणः ष इति च वर्तते")
              + "; " + _q("8.3.38", "padamanjari", "पूर्वस्यायमपवादः"))


def _apadadau(v: View, nxt: Sight) -> bool:
    """The कु/पु sound does not begin a पद: it begins an affix (`pratyaya`)."""
    return v.begins_word(nxt) and _flag(v, nxt, "pratyaya")


@rule("8.3.38", name=_name("8.3.38"),
      families=("visarga", VIKARA, _own("8.3.38")),
      overrides=(("8.3.37", _q("8.3.38", "padamanjari",
                               "पूर्वस्यायमपवादः")),))
def so_apadadau(v: View):
    """
    सकार आदेशो भवति विसर्जनीयस्य कुप्वोरपदाद्योः परतः — पयस्पाशम्, पयस्कल्पम्,
    यशस्कल्पम्, पयस्कम्, यशस्काम्यति.

    The कु/पु sound must not begin a पद — it begins an affix (पाशप्, कल्पप्, क,
    काम्यच्: *sambhavadarśana, not parigaṇana*, Tattvabodhinī). The stem is a
    पद by 1.4.17 before those affixes, so it is written as a word of its own
    and the affix carries the flag `pratyaya`. *Apadādāviti kim?* पय कामयते,
    पय पिबति (a पद begins). The two vārttikas that restrict it — अनव्ययस्य and
    काम्ये रोरेव — are refusals below (they are not Pāṇini's).
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        if not _apadadau(v, j.right):
            continue
        yield _to(j, "s", f"the {sk(j.right.s)} begins an affix, not a pada",
                  f"the visarga stands before {sk(j.right.s)}, which does not "
                  f"begin a pada but an affix ({{pratyaya}}), so it becomes "
                  f"{{s}}")


@rule("8.3.38", name=_VT_ANAVYAYA, authority=VARTTIKA,
      varttika=_VT_ANAVYAYA, families=("visarga",),
      overrides=(
          ("8.3.37", _q("8.3.38", "kashika",
                        "इह मा भूत् — प्रातःकल्पम्, पुनःकल्पमिति")),
          (_ov("8.3.38"), _q("8.3.38", "kashika",
                             "सोऽपदादावित्यनव्ययस्येति वक्तव्यम्")),
          ("8.3.39", _q("8.3.38", "kashika",
                        "इह मा भूत् — प्रातःकल्पम्, पुनःकल्पमिति"))))
def so_apadadav_anavyayasya(v: View):
    """
    सोऽपदादावनव्ययस्य — प्रातःकल्पम्, पुनःकल्पम्.

    Vārttika: an indeclinable's visarga is left alone. *Punaḥkalpam* has an उ
    before the visarga, so 8.3.39 would give ष् — the vārttika holds it off too,
    which is why the Kāśikā gives that example. An avyaya is what the caller
    marks so, or a nipāta or upasarga (1.1.37, 1.4.58).
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        if not _apadadau(v, j.right) or not _avyaya(v, j.left):
            continue
        yield _keep(j, "the word is indeclinable",
                    f"{sk(_text(v, j.left))} is an {{avyaya}}, so the visarga "
                    f"is not made {{s}} (or {{ṣ}}) before the affix — "
                    f"'{_text(v, j.left)} kalpam' keeps it",
                    authority=VARTTIKA, varttika=_VT_ANAVYAYA)


@rule("8.3.38", name=_VT_KAMYE, authority=VARTTIKA,
      varttika=_VT_KAMYE, families=("visarga",),
      overrides=(
          ("8.3.37", _q("8.3.38", "kashika", "इह मा भूत् — गीःकाम्यति। "
                                            "धूःकाम्यति")),
          (_ov("8.3.38"), _q("8.3.38", "kashika", "रोरेव काम्ये नान्यस्येति "
                                                 "नियमार्थं वक्तव्यम्")),
          ("8.3.39", _q("8.3.38", "kashika", "इह मा भूत् — गीःकाम्यति। "
                                            "धूःकाम्यति"))))
def kamye_roreva(v: View):
    """
    रोः काम्ये नियमार्थम् — रोरेव काम्ये नान्यस्य; पयस्काम्यति, गीःकाम्यति.

    Vārttika, a niyama: before the affix काम्यच् only a रु's visarga becomes
    स्/ष्; the visarga of a plain र् (*gīr*) stays (Kāśikā: गीःकाम्यति,
    धूःकाम्यति — with इ/उ before, 8.3.39 is held off as well).
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        if not (_apadadau(v, j.right) and _text(v, j.right).startswith("kāmy")
                and not _from_ru(j.left)):
            continue
        yield _keep(j, "the affix is {kāmyac} and the visarga is not a रु's",
                    "before {kāmyac} only the visarga of a रु is a स्/ष्, and "
                    "this one comes from a plain र्, so it stays",
                    authority=VARTTIKA, varttika=_VT_KAMYE)


@rule("8.3.39", name=_name("8.3.39"),
      families=("visarga", VIKARA, _own("8.3.39")),
      overrides=(
          (_ov("8.3.38"), _q("8.3.39", "tattvabodhini",
                             "सोऽपदादावित्यस्यापवादः")),
          ("8.3.37", _APAVADA37)))
def inah_sah(v: View):
    """
    इण उत्तरस्य विसर्जनीयस्य षकारादेशो भवति कुप्वोरपदाद्योः परतः — सर्पिष्पाशम्,
    यजुष्पाशम्, सर्पिष्कल्पम्, सर्पिष्कम्, सर्पिष्काम्यति.

    The अपवाद of 8.3.38. इण् is the wide one, to the *later* ण् (Bālamanoramā on
    8.3.57: *'इ' णिति परणकारेण प्रत्याहारः*): इ उ ऋ ऌ ए ओ ऐ औ ह य व र ल. *Apadādāveva*:
    अग्निः करोति, वायुः करोति (a पद begins) — and *kupvoreva*: सर्पिस्ते.
    """
    wide = _wide_in()
    for j in _visarga_before(v, _ku_pu() & _khar()):
        prev = v.prev(j.left)
        if prev is None or prev.s not in wide or not _apadadau(v, j.right):
            continue
        yield _to(j, "ṣ", f"{sk(prev.s)} (an {{iṇ}}) before and the affix "
                          f"{sk(j.right.s)} after",
                  f"the visarga stands after {sk(prev.s)}, an {{iṇ}}, and "
                  f"before {sk(j.right.s)} beginning an affix, so it becomes "
                  f"{{ṣ}} and not {{s}}")


def _gati_word(v: View, sight: Sight, words: Tuple[str, ...]) -> bool:
    return _text(v, sight) in words and _flag(v, sight, "gati")


@rule("8.3.40", name=_name("8.3.40"),
      families=("visarga", VIKARA, _own("8.3.40")),
      overrides=(("8.3.37", _APAVADA37),))
def namaspurasor_gatyoh(v: View):
    """
    गतिसंज्ञयोरनयोर्विसर्गस्य सः कुप्वोः परयोः — नमस्करोति, नमस्कर्ता, पुरस्करोति.

    The two words are *namas* and *puras* (Kāśikā: नमस् पुरस्). *Gatyoḥ* — being
    a गति (1.4.60) is what the letters cannot say: the flag `gati`. *Gatyoriti
    kim?* पूः, पुरौ, पुरः करोति — the word is not a गति there — and *namaḥ
    karoti* when 'namas' is not one (Kaumudī: तदभावे नमः करोति).
    """
    words = tuple(to_iast(w) for w in _bare(
        "8.3.40", "kashika", "नमस् पुरस्").split())
    for j in _visarga_before(v, _ku_pu() & _khar()):
        if _gati_word(v, j.left, words):
            yield _to(j, "s", f"the {sk(j.right.s)} follows a gati",
                      f"{sk(_text(v, j.left))} is a {{gati}} and "
                      f"{sk(j.right.s)} is a {{ku}} or {{pu}} sound, so the "
                      f"visarga becomes {{s}}")


@lru_cache(maxsize=None)
def _iu() -> Tuple[str, ...]:
    """इ and उ — the vowels of *idud-upadhasya*, each written with a त्-marked
    consonant (इत्, उत्, 1.1.70), so short: read off the sūtra's own word."""
    sounds = tokenize(_sutra("8.3.41").split()[0])
    return tuple(s for s, _ in sounds[:4] if s in AC)


def _idudupadha(v: View, h: Sight) -> Optional[Sight]:
    """The sound before the visarga, if it is a short इ or उ (इदुदुपधस्य: तपर,
    1.1.70)."""
    prev = v.prev(h)
    if prev is None or prev.w != h.w or prev.s not in _iu():
        return None
    return prev


@rule("8.3.41", name=_name("8.3.41"),
      families=("visarga", VIKARA, _own("8.3.41")),
      overrides=(("8.3.37", _APAVADA37),))
def idudupadhasya_capratyayasya(v: View):
    """
    इकारोपधस्य उकारोपधस्य चाप्रत्ययस्य विसर्जनीयस्य षकार आदेशो भवति कुप्वोः परतः —
    निष्कृतम्, दुष्कृतम्, बहिष्कृतम्, आविष्कृतम्, चतुष्कपालम्, प्रादुष्कृतम्.

    *Apratyayasya*: the visarga must not be an affix's — अग्निः करोति, वायुः
    करोति. The letters cannot say which; the Kāśikā lists the words the shape
    picks out (निर्दुर्बहिराविश्चतुर्प्रादुस्, which `visarjaniya.NIRADI` keeps)
    and any other word is the caller's — `apratyaya`. *Idudupadhasya kim?* गीः
    करोति, पूः करोति (ई, ऊ). A द्विस्/त्रिस्/चतुर् in the sense of 'times' is
    8.3.43's, which gives an option and not this nitya ष्: as with 8.3.34 and
    8.3.37, the utsarga does not return when the option of the sūtra that names
    the case is declined, so it leaves that field alone. **The vārttika मुहुसः
    प्रतिषेधः** (Kāśikā: मुहु≍ कामा; Kaumudī: मुहुः कामा) is applied here as an
    exclusion: it changes no sound, so there is nothing for a rule of its own
    to do, and the visarga is left to 8.3.37's courses.
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        h = j.left
        word = _text(v, h)
        if not (word in NIRADI or _flag(v, h, "apratyaya")):
            continue
        if _idudupadha(v, h) is None:
            continue
        if word in DVIS_THREE and _flag(v, h, "krtvo_artha"):
            continue
        if word == _MUHUS:
            continue
        up = _idudupadha(v, h)
        yield _to(j, "ṣ", f"{sk(up.s)} in the penult and the visarga is no "
                          f"affix's",
                  f"{sk(word)} has {sk(up.s)} before its last sound, that "
                  f"sound is not an affix, and {sk(j.right.s)} is a {{ku}} or "
                  f"{{pu}} sound, so the visarga becomes {{ṣ}}")


@rule("8.3.42", name=_name("8.3.42"),
      families=("visarga", VIKARA, _own("8.3.42")),
      overrides=(("8.3.37", _APAVADA37),))
def tiraso_nyatarasyam(v: View):
    """
    तिरसो विसर्गस्य सो वा स्यात् कुप्वोः — तिरस्कर्ता, तिरः कर्ता.

    Only *tiras* as a गति (गतेरित्येव — तिरः कृत्वा काण्डं गतः: no गति, no option).
    An option: declining it leaves 8.3.37's own courses.
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        if _gati_word(v, j.left, ("tiras",)):
            yield _to(j, "s", f"the {sk(j.right.s)} follows a gati",
                      f"{{tiras}} is a {{gati}} and {sk(j.right.s)} is a "
                      f"{{ku}} or {{pu}} sound, so the visarga may become "
                      f"{{s}}", optional=_ANYATARASYAM)


@rule("8.3.43", name=_name("8.3.43"),
      families=("visarga", VIKARA, _own("8.3.43")),
      overrides=(
          ("8.3.41", _q("8.3.43", "kashika",
                        "कृत्वोऽर्थ इति किम्? चतुष्कपालम्। चतुष्कण्टकम्। "
                        "पूर्वेण नित्यं षत्वं भवति")),
          ("8.3.37", _APAVADA37)))
def dvistriscatur_krtvo_rthe(v: View):
    """
    कृत्वोऽर्थे वर्तमानानामेषां विसर्गस्य षकारो वा स्यात् कुप्वोः — द्विष्करोति, द्विः
    करोति, त्रिष्पचति, चतुष्करोति, चतुःकरोति.

    The three words are those `visarjaniya.DVIS_THREE` keeps; *kṛtvo 'rthe* — used
    for 'times' — is the caller's flag `krtvo_artha`. *Kṛtvo 'rtha iti kim?*
    चतुष्कपालम् — there 8.3.41's ष् is nitya (Kāśikā: पूर्वेण नित्यं षत्वं भवति),
    and 8.3.41 does not act on a चतुर् in the 'times' sense either: this sūtra
    names it so that it should not.
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        if _text(v, j.left) in DVIS_THREE and _flag(v, j.left, "krtvo_artha"):
            yield _to(j, "ṣ", f"the {sk(j.right.s)} follows a numeral "
                              f"adverb of 'times'",
                      f"{sk(_text(v, j.left))} is used in the sense of "
                      f"'times' ({{kṛtvas}}) before the {{ku}} or {{pu}} "
                      f"sound {sk(j.right.s)}, so the visarga may become "
                      f"{{ṣ}}", optional=_ANYATARASYAM)


@rule("8.3.44", name=_name("8.3.44"),
      families=("visarga", VIKARA, _own("8.3.44")),
      overrides=(("8.3.37", _APAVADA37),))
def isusoh_samarthye(v: View):
    """
    एतयोर्विसर्गस्य षः स्याद्वा कुप्वोः — सर्पिष्करोति, सर्पिः करोति, धनुष्करोति.

    इस्/उस् are the affixes (flag `isus`); *sāmarthya* is *vyapekṣā* — that the two
    words are construed together (Kaumudī: सामर्थ्यमिह व्यपेक्षा) — the caller's
    flag `samartha`. *Sāmarthye kim?* तिष्ठतु सर्पिः, पिब त्वमुदकम्. In a compound
    there is no vyapekṣā (Kāśikā on 8.3.45: व्यपेक्षा च तत्र सामर्थ्यमाश्रितमिति
    समासे न भवति) — 8.3.45 has it there.
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        if (j.kind not in PADA_LIKE or j.kind == SAMASA
                or not _flag(v, j.left, "isus")
                or not _flag(v, j.left, "samartha")):
            continue
        yield _to(j, "ṣ", "the two words are construed together",
                  f"the word ends in the affix {{is}} or {{us}} and is "
                  f"construed with the word after it, before the {{ku}} or "
                  f"{{pu}} sound {sk(j.right.s)}, so the visarga may become "
                  f"{{ṣ}}", optional=_ANYATARASYAM)


@rule("8.3.45", name=_name("8.3.45"),
      families=("visarga", VIKARA, _own("8.3.45")),
      overrides=(
          (_ov("8.3.44"), _q("8.3.45", "kashika",
                             "पूर्वसूत्रेण विकल्पोऽप्यत्र न भवति")),
          ("8.3.37", _APAVADA37)))
def nityam_samase_nuttarapadasthasya(v: View):
    """
    इसुसोर्विसर्गस्यानुत्तरपदस्थस्य समासे नित्यं षः स्यात् कुप्वोः — सर्पिष्कुण्डिका,
    धनुष्कपालम्, सर्पिष्पानम्, धनुष्फलम्.

    *Anuttarapadasthasya kim?* परमसर्पिःकुण्डिका — the visarga stands in the last
    member of a compound, and then not even 8.3.44's option applies (Kāśikā).
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        if (j.kind != SAMASA or not _flag(v, j.left, "isus")
                or _uttarapada(v, j.left)):
            continue
        yield _to(j, "ṣ", "a compound whose first member ends in इस्/उस्",
                  f"the word ends in {{is}} or {{us}}, is the first member "
                  f"of a compound, and {sk(j.right.s)} is a {{ku}} or {{pu}} "
                  f"sound, so the visarga becomes {{ṣ}}, always")


def _krkami(v: View, nxt: Sight) -> bool:
    """The word after is one of कृ कमि कंस कुम्भ पात्र कुशा कर्णी — a form of the
    roots कृ and कम् (the caller's `dhatu:kṛ`, `dhatu:kam`), or a word that
    begins with the others."""
    if not v.begins_word(nxt):
        return False
    text, root = _text(v, nxt), v.word(nxt).flag_value("dhatu")
    for item in KRKAMI_SEVEN:
        if root == item or (item == "kami" and root == "kam"):
            return True
        if item not in ("kṛ", "kami") and _form_of(text, item):
            return True
    return False


@rule("8.3.46", name=_name("8.3.46"),
      families=("visarga", VIKARA, _own("8.3.46")),
      overrides=(("8.3.37", _APAVADA37),))
def atah_krkami(v: View):
    """
    अकारादुत्तरस्यानव्ययविसर्जनीयस्य समासेऽनुत्तरपदस्थस्य नित्यं सकारादेशो भवति कृ कमि
    कंस कुम्भ पात्र कुशा कर्णी इत्येतेषु परतः — अयस्कारः, पयस्कामः, अयस्कंसः, अयस्कुम्भः,
    अयस्पात्रम्, अयस्कुशा, अयस्कर्णी.

    The seven are those `visarjaniya.KRKAMI_SEVEN` keeps (and the Kāśikā lists).
    *Ataḥ kim?* गीःकारः, धूःकारः; *tapara kim?* भाःकरणम् (a long आ); *anavyayasya
    kim?* श्वःकारः, पुनःकारः; *samāse kim?* यशः करोति; *anuttarapadasthasya kim?*
    परमपयःकारः.
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        h = j.left
        prev = v.prev(h)
        if (j.kind != SAMASA or prev is None or prev.w != h.w
                or not _short_a(prev) or _avyaya(v, h) or _uttarapada(v, h)
                or not _krkami(v, j.right)):
            continue
        yield _to(j, "s", "a compound of an a-final word before one of the "
                          "seven",
                  f"the visarga stands after a short {{a}} in the first "
                  f"member of a compound (not an {{avyaya}}) and before "
                  f"{sk(_text(v, j.right))}, so it becomes {{s}}, always")


#: The word 8.3.47 names — *pade*, the locative of *pada*.
_PADA = _sutra("8.3.47").split()[-1][:-1] + "a"


@rule("8.3.47", name=_name("8.3.47"),
      families=("visarga", VIKARA, _own("8.3.47")),
      overrides=(("8.3.37", _APAVADA37),))
def adhah_sirasi_pade(v: View):
    """
    एतयोर्विसर्गस्य सादेशः स्यात्पदशब्दे परे — अधस्पदम्, शिरस्पदम्.

    Only in a compound and not in its last member (*samāsa* and *anuttarapadastha*
    run on from the sūtras before). *Samāsa ity eva* — अधः पदम्; *anuttarapadastha
    ity eva* — परमशिरःपदम्. The two words are *adhas* and *śiras* (Kāśikā:
    अधस् शिरस्); *pada* may stand with an ending that
    merges with its अ (*padī*, अधस्पदी).
    """
    words = tuple(to_iast(w) for w in _bare(
        "8.3.47", "kashika", "अधस् शिरस्").split())
    for j in _visarga_before(v, _ku_pu() & _khar()):
        h = j.left
        if (j.kind != SAMASA or _text(v, h) not in words or _uttarapada(v, h)
                or not _form_of(_text(v, j.right), _PADA)):
            continue
        yield _to(j, "s", "a compound before {pada}",
                  f"{sk(_text(v, h))} is the first member of a compound and "
                  f"{{pada}} follows, so the visarga becomes {{s}}")


@lru_cache(maxsize=None)
def _kaskadi_items() -> Tuple[str, ...]:
    return tuple(item for g in corpus.ganas_for("8.3.48") for item in g.items)


def _kaskadi_match(v: View, j: Junction, sound: str) -> Optional[str]:
    """The kaskādi word whose beginning is the two words as they would stand
    joined with `sound`, if there is one."""
    left, right = _text(v, j.left), _text(v, j.right)
    stem = left[:-1] if left[-1:] in ("s", "r") else left
    tail = right[:-1] if right.endswith("s") else right
    joined = stem + sound + tail
    for item in _kaskadi_items():
        if item.startswith(joined):
            return item
    return None


@rule("8.3.48", name=_name("8.3.48"),
      families=("visarga", VIKARA, _own("8.3.48")),
      overrides=(("8.3.37", _q("8.3.48", "kaumudi", "≍क≍पयोरपवादः")),))
def kaskadisu_ca(v: View):
    """
    कस्कादिषु च विसर्जनीयस्य सकारः षकारो वा यथायोगमादेशो भवति कुप्वोः परतः — कस्कः,
    कौतस्कुतः, भ्रातुष्पुत्रः, शुनस्कर्णः, सद्यस्कालः, सर्पिष्कुण्डिका, भास्करः.

    Kaumudī: एष्विण उत्तरस्य विसर्गस्य षः स्यादन्यत्र तु सः — ष् after an इण्, else
    स्. The gaṇa is a list of *finished words* (an ākṛtigaṇa: अविहितलक्षण उपचारः
    कस्कादिषु द्रष्टव्यः), read from the gaṇapāṭha on disk; the two words meet in it
    if the spelling of the one joined to the other is the beginning of an item.
    PARTIAL for that reason: a word the list does not spell is not seen. The
    visarga's word must begin the compound it stands in: the Kāśikā's own
    counter-example is परमसर्पिःकुण्डिका (भाष्ये वृत्तौ च …). **OPEN**: the
    Pārāyaṇikas read the paṭha of सर्पिष्कुण्डिका as making the ष् in a last
    member too (their counter-example is परमसर्पिः फलम्); they are not followed.
    """
    wide = _wide_in()
    for j in _visarga_before(v, _ku_pu() & _khar()):
        prev = v.prev(j.left)
        if prev is None or _uttarapada(v, j.left):
            continue
        sound = "ṣ" if prev.s in wide else "s"
        item = _kaskadi_match(v, j, sound)
        if item is None:
            continue
        yield _to(j, sound, f"the pair is spelt in the kaskādi gaṇa "
                            f"({sk(item)})",
                  f"the two words join as {sk(item)}, a word of the "
                  f"{{kaskādi}} gaṇa, so the visarga becomes "
                  f"{sk(sound)} — ṣ after an {{iṇ}}, s otherwise")


# ---------------------------------------------------------------------------
# 8.3.49–54  the same, in the Veda
# ---------------------------------------------------------------------------


def _amredita(v: View, sight: Sight) -> bool:
    """The word is the second of a repeated pair (8.1.2 तस्य परमाम्रेडितम् —
    दिरुक्तस्य परम्): the caller's `amredita`, or plainly the same word again."""
    if not v.begins_word(sight):
        return False
    word = v.word(sight)
    return word.has("amredita") or (
        sight.w > 0 and v.state.words[sight.w - 1].text == word.text)


@rule("8.3.49", name=_name("8.3.49"),
      families=("visarga", VIKARA, _own("8.3.49")), vedic=True,
      overrides=(("8.3.37", _APAVADA37),))
def chandasi_va_apramreditayoh(v: View):
    """
    छन्दसि विषये विसर्जनीयस्य वा सकारादेशो भवति कुप्वोः परतः प्रशब्दमाम्रेडितं च वर्जयित्वा —
    अयःपात्रम्, अयस्पात्रम्; विश्वतस्पात्रम्; उरु णस्कारः.

    Vedic. Not before *pra* (अग्निः प्रविद्वान्) and not before an āmreḍita (परुषः
    परुषः) — where the s is not made at all. A second option on top of 8.3.37's.
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        if _text(v, j.right) == "pra" or _amredita(v, j.right):
            continue
        yield _to(j, "s", f"the {sk(j.right.s)} follows, in the Veda",
                  f"in the Veda the visarga may become {{s}} before the "
                  f"{{ku}} or {{pu}} sound {sk(j.right.s)}, which begins "
                  f"neither {{pra}} nor a repeated word", optional=_VA)


def _matches(text: str, item: str) -> bool:
    return text == item or text.startswith(item + "m")


_KAH_KARAT = tuple(_listed(_bare("8.3.50", "kashika", "कः करत् करति कृधि कृत")))


@rule("8.3.50", name=_name("8.3.50"),
      families=("visarga", VIKARA, _own("8.3.50")), vedic=True,
      overrides=(("8.3.37", _APAVADA37),
                 ("8.3.49", _q("8.3.50", "kaumudi", "विसर्गस्य सः स्यात्"))))
def kah_karat_karati_krdhi_krte(v: View):
    """
    कः करत् करति कृधि कृत इत्येतेषु परतोऽनदितेर्विसर्जनीयस्य सकारादेशो भवति छन्दसि —
    विश्वतस्कः, विश्वतस्करत्, पयस्करति, उरु णस्कृधि, सदस्कृतम्.

    Vedic. *Anaditeḥ kim?* यथा नो अदितिः करत् — the visarga of *aditi*.
    """
    words = tuple(w.replace("ḥ", "s") for w in _KAH_KARAT)
    for j in _visarga_before(v, _ku_pu() & _khar()):
        text = _text(v, j.right)
        if _text(v, j.left) == "aditis" or not v.begins_word(j.right):
            continue
        if not any(_matches(text, w) for w in words):
            continue
        yield _to(j, "s", f"{sk(text)} follows, in the Veda",
                  f"in the Veda the visarga (not that of {{aditi}}) becomes "
                  f"{{s}} before {sk(text)}, one of कः, करत्, करति, कृधि, कृत")


@rule("8.3.51", name=_name("8.3.51"),
      families=("visarga", VIKARA, _own("8.3.51")), vedic=True,
      overrides=(("8.3.37", _APAVADA37),
                 ("8.3.49", _q("8.3.51", "kaumudi",
                               "पञ्चमीविसर्गस्य सः स्यादुपरिभवार्थे "
                               "परिशब्दे परतः"))))
def pancamyah_paravadhyarthe(v: View):
    """
    पञ्चमीविसर्गस्य सः स्यादुपरिभवार्थे परिशब्दे परतः — दिवस्परि प्रथमं जज्ञे.

    Vedic. The ablative is `pancami` and *pari* in the sense of *adhi* (upari-
    bhāva) is `adhyartha` — the caller's words, the letters do not say them.
    *Adhyarthe kim?* दिवस्पृथिव्याः पर्योजः (*pari* = all round).
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        if (_flag(v, j.left, "pancami") and _text(v, j.right) == "pari"
                and _flag(v, j.right, "adhyartha")):
            yield _to(j, "s", "an ablative before pari in the sense of adhi",
                      "the visarga is an ablative's and {pari} means "
                      "'above', so it becomes {s}")


@rule("8.3.52", name=_name("8.3.52"),
      families=("visarga", VIKARA, _own("8.3.52")), vedic=True,
      overrides=(("8.3.37", _APAVADA37),))
def patau_ca_bahulam(v: View):
    """
    पातौ च धातौ परतः पञ्चमीविसर्जनीयस्य बहुलं सकार आदेशो भवति छन्दसि — दिवस्पातु,
    राज्ञस्पातु; न च भवति — परिषदः पातु.

    Vedic and *bahulam*: often and not always — the engine returns both. The
    dhātu is `dhatu:pā` on the word after.
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        if (_flag(v, j.left, "pancami")
                and v.word(j.right).flag_value("dhatu") == "pā"):
            yield _to(j, "s", "an ablative before the root pā",
                      "the visarga is an ablative's and the root {pā} "
                      "follows, so it may become {s}", optional=_BAHULAM)


@rule("8.3.53", name=_name("8.3.53"),
      families=("visarga", VIKARA, _own("8.3.53")), vedic=True,
      overrides=(("8.3.37", _APAVADA37),
                 ("8.3.49", _q("8.3.49", "kaumudi",
                               "नेह । वसुनः पूर्व्यस्पतिः"))))
def sasthyah_patiputra(v: View):
    """
    षष्ठीविसर्जनीयस्य सकारादेशो भवति पति पुत्र पृष्ठ पार पद पयस् पोष इत्येतेषु परतः
    छन्दसि — वाचस्पतिम्, दिवस्पुत्राय, दिवस्पृष्ठे, तमसस्पारम्, इडस्पदे, दिवस्पयः, रायस्पोषम्.

    Vedic. The genitive is the caller's `sasthi`; the seven are those
    `visarjaniya.PATI_SEVEN` keeps. *Ṣaṣṭhyā iti kim?* मनुः पुत्रेभ्यः. The word
    *iḍāyāḥ* is 8.3.54's, an option.
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        text = _text(v, j.right)
        if (not _flag(v, j.left, "sasthi") or not v.begins_word(j.right)
                or _text(v, j.left) == "iḍāyās"
                or not any(_form_of(text, w) for w in PATI_SEVEN)):
            continue
        yield _to(j, "s", "a genitive before one of the seven",
                  f"the visarga is a genitive's and {sk(text)} follows, one "
                  f"of pati, putra, pṛṣṭha, pāra, pada, payas, poṣa, so it "
                  f"becomes {{s}}")


@rule("8.3.54", name=_name("8.3.54"),
      families=("visarga", VIKARA, _own("8.3.54")), vedic=True,
      overrides=(("8.3.37", _APAVADA37),))
def idayah_va(v: View):
    """
    इडायाः षष्ठीविसर्जनीयस्य वा सकार आदेशो भवति पत्यादिषु परतश्छन्दसि — इडायास्पतिः,
    इडायाः पतिः; इडायास्पुत्रः, इडायास्पदम्.

    Vedic. The one word taken out of 8.3.53 and given an option.
    """
    for j in _visarga_before(v, _ku_pu() & _khar()):
        text = _text(v, j.right)
        if (_text(v, j.left) == "iḍāyās" and v.begins_word(j.right)
                and any(_form_of(text, w) for w in PATI_SEVEN)):
            yield _to(j, "s", "iḍāyāḥ before one of the seven",
                      f"the visarga is that of {{iḍāyā}} and {sk(text)} "
                      f"follows, so it may become {{s}}", optional=_VA)


# ---------------------------------------------------------------------------
# 8.3.8–12  the रु out of a न्
# ---------------------------------------------------------------------------


def _make_ru(sight: Sight):
    """The रु of these sūtras — the same र् marked `RU` that 8.2.66 makes, so
    everything that acts on the रु of a स् acts on this one."""
    return replace(sight, NewSeg("r", frozenset({RU}), show="ru"))


def _n_to_ru(j: Junction, *, why: str, nimitta: str, optional: str = "",
             via: Tuple[Via, ...] = ()) -> Application:
    return Application(
        site=site(j.left, j.right), edits=(_make_ru(j.left),),
        optional=optional,
        detail=Detail(kind=ADESA, sthanin="n", adesa="ru", nimitta=nimitta,
                      because=why, via=(S.alo_antyasya("n"),) + via))


@rule("8.3.8", name=_name("8.3.8"), families=("visarga",), vedic=True)
def ubhayatharksu(v: View):
    """
    नकारान्तस्य पदस्य छवि परतोऽम्पर उभयथा ऋक्षु भवति, रुर्वा नकारो वा — तस्मिँस्त्वा
    दधाति, तस्मिन्त्वा दधाति; पशून्तांश्चक्रे.

    Vedic (in ṛk verses). *Ṛkṣviti kim?* ताँस्त्वं खाद सुखादितान्. **OPEN**: in the
    full rulebook 8.3.7 (the nasal family) gives this रु as a rule of the
    language; this sūtra is the Ṛk verses' option on it (Kāśikā: पूर्वेण नित्ये
    प्राप्ते विकल्पः क्रियते). The option is offered here as a रु made or not
    made; whether the *not-made* course stays न् depends on 8.3.7 standing aside
    for Ṛk verses at the same place — see the report's core_requests.
    """
    chav, am = S.members("chaV"), S.members("aM")
    for j in v.junctions():
        n, nxt = j.left, j.right
        if n.s != "n" or not v.pada_final(n) or nxt.s not in chav:
            continue
        after = v.next(nxt)
        if after is None or after.s not in am:
            continue
        yield _n_to_ru(j, optional=_UBHAYATHA,
                       nimitta=f"the {{chav}} {sk(nxt.s)} follows, with an "
                               f"{{am}} after it",
                       why=f"the pada ends in {{n}}, the {{chav}} "
                           f"{sk(nxt.s)} follows with the {{am}} "
                           f"{sk(after.s)} after it, in a ṛk verse: {{ru}} or "
                           f"{{n}}, both stand")


@rule("8.3.9", name=_name("8.3.9"), families=("visarga",), vedic=True)
def dirghad_ati_samanapade(v: View):
    """
    दीर्घादुत्तरस्य पदान्तस्य नकारस्य रुर्भवत्यटि परतः तौ चेद् निमित्तनिमित्तिनौ समानपादे
    भवतः — परिधीँरति, देवाँ अच्छा, महाँ इन्द्रो य ओजसा.

    Vedic. Optional (उभयथेत्यनुवृत्तेः — Kaumudī: उभयथेत्यनुवृत्तेर्नेह, आदित्यान्
    याचिषामहे: no option-less form is meant). The two sounds must stand in one ṛk
    pāda — the caller's `antahpada`; the long vowel is asked of `svara.duration`
    (1.2.27). *Dīrghāditi kim?* अहन्नहिम्. *Aṭīti kim?* इभ्यान् क्षत्रियान्.
    """
    at = S.members("aṬ")
    for j in v.junctions():
        n, nxt = j.left, j.right
        if n.s != "n" or not v.pada_final(n) or nxt.s not in at:
            continue
        prev = v.prev(n)
        if (prev is None or prev.w != n.w or duration(prev.s) != 2
                or not _flag(v, n, "antahpada")):
            continue
        yield _n_to_ru(j, optional=_UBHAYATHA,
                       nimitta=f"the long {sk(prev.s)} before and the {{aṭ}} "
                               f"{sk(nxt.s)} after, in one pāda",
                       why=f"the pada-final {{n}} follows the long "
                           f"{sk(prev.s)}, the {{aṭ}} {sk(nxt.s)} comes after "
                           f"it in the same ṛk pāda: {{ru}} or {{n}}")


def _sutra_word(sutra_id: str, index: int) -> str:
    return _sutra(sutra_id).split()[index]


@rule("8.3.10", name=_name("8.3.10"), families=("visarga",))
def nrn_pe(v: View):
    """
    नॄनित्यस्य रुः स्याद्वा पकारे परे — नॄँः पाहि, नॄंः पाहि; नॄन् पाहि.

    The word is *nṝn* (the sūtra's own first word), and *pe* is the letter प्. An
    option, as the Kaumudī and the Laghusiddhāntakaumudī read it (रुर्वा पे —
    उभयथेत्यपि केचिदनुवर्तयन्ति, the Kāśikā allows *nṝn pāhi* too, though it
    states the रु as its rule). **OPEN**: the Kāśikā's own reading is the nitya
    रु, the option of the *kecit*; the shared ground is that the रु is there and
    *nṝn pāhi* is admitted, which is what the two courses give. The nasal
    sounds of *nṝ̐ḥ*, *nṝṃḥ* are 8.3.2 and 8.3.4's (the nasal family); the
    visarga is then 8.3.15, the उपध्मानीय or the visarga 8.3.37.
    """
    word = _sutra_word("8.3.10", 0)
    p = tokenize(_sutra_word("8.3.10", 1))[0][0]
    for j in v.junctions():
        n, nxt = j.left, j.right
        if (n.s == "n" and v.pada_final(n) and _text(v, n) == word
                and nxt.s == p):
            yield _n_to_ru(j, optional=_UBHAYATHA,
                           nimitta=f"{{pa}} follows the word {sk(word)}",
                           why=f"the word {sk(word)} ends in {{n}} and "
                               f"{sk(p)} follows, so the {{n}} may be a "
                               f"{{ru}} — or stay")


_PAYU = to_iast(_bare("8.3.11", "kashika", "पायुशब्दे").replace("शब्दे", ""))


@rule("8.3.11", name=_name("8.3.11"), families=("visarga",))
def svatavan_payau(v: View):
    """
    स्वतवानित्येतस्य नकारस्य रुर्भवति पायुशब्दे परतः — स्वतवाँः पायुरग्ने.

    Of the word *svatavān* (the sūtra's first word) before *pāyu*. Option or
    nitya as with 8.3.10 (Kaumudī: रुर्वा; Kāśikā: रुर्भवति) — **OPEN**, the same
    reading is taken: the रु, and the न् admitted.
    """
    word = _sutra_word("8.3.11", 0)
    for j in v.junctions():
        n, nxt = j.left, j.right
        if (n.s == "n" and v.pada_final(n) and _text(v, n) == word
                and v.begins_word(nxt) and _text(v, nxt).startswith(_PAYU)):
            yield _n_to_ru(j, optional=_UBHAYATHA,
                           nimitta=f"the word {sk(_text(v, nxt))} follows",
                           why=f"the word {sk(word)} ends in {{n}} and "
                               f"{sk(_PAYU)} follows, so the {{n}} may be a "
                               f"{{ru}}")


@rule("8.3.12", name=_name("8.3.12"), families=("visarga",))
def kan_amredite(v: View):
    """
    कान्नकारस्य रुः स्यादाम्रेडिते परे — कांस्कानामन्त्रयते, कांस्कान् भोजयति.

    The word is *kān* and the second *kān* is the āmreḍita (8.1.2 तस्य
    परमाम्रेडितम्: the repeated word). *Āmreḍita iti kim?* कान् कान् पश्यसि — two
    different words (the caller says so by *not* repeating one, or by giving
    `amredita` for the second). The स् of *kāṃskān* is the vārttika of 8.3.34
    (संपुंकानां सो वक्तव्यः) and the kaskādi gaṇa (8.3.48). **OPEN**: the Kāśikā
    reads the स् as enjoined directly here (समः सुटि इत्यतो वा सकारोऽनुवर्तते) and
    gives no रु-route; the Kaumudī and the Laghu (कान्नकारस्य रुः) take the रु, and
    that is the course implemented.
    """
    word = _sutra("8.3.12").partition("āmreḍite")[0]
    for j in v.junctions():
        n, nxt = j.left, j.right
        if (n.s == "n" and v.pada_final(n) and _text(v, n) == word
                and _amredita(v, nxt)):
            yield _n_to_ru(j, nimitta="the repeated word follows",
                           why=f"the word {sk(word)} is followed by its own "
                               f"repetition, an {{āmreḍita}}, so its {{n}} is "
                               f"a {{ru}}",
                           via=(Via("8.1.2", "the second of two identical "
                                             "words is the āmreḍita"),))


# ---------------------------------------------------------------------------
# 8.2.64–65  म् of a dhātu
# ---------------------------------------------------------------------------


@rule("8.2.64", name=_name("8.2.64"), families=("hal",))
def mo_no_dhatoh(v: View):
    """
    मकारान्तस्य धातोः पदस्य नकारादेशो भवति — प्रशान्, प्रतान्, प्रदान्.

    *Dhātoriti kim?* इदम्, किम्. The word is one that ends in a dhātu — a dhātu
    whose affix (क्विप्) has been lost (the caller's `dhatu`); the letters cannot
    say it. *Padasyeti eva* — प्रतामौ, प्रतामः (the म् is inside the word). The
    न् this rule makes is invisible to the rule that would drop it (8.2.7), and
    stays: 8.2.1.
    """
    for m in v.live:
        if m.s != "m" or not v.pada_final(m) or not _flag(v, m, "dhatu"):
            continue
        yield Application(
            site=site(m), edits=(replace(m, "n"),),
            detail=Detail(
                kind=ADESA, sthanin="m", adesa="n",
                nimitta="the end of a pada that ends in a dhātu",
                because=f"the pada {sk(_text(v, m))} ends in the {{dhātu}}'s "
                        f"{{m}}, so it becomes {{n}}",
                via=(S.alo_antyasya("m"),)))


@rule("8.2.65", name=_name("8.2.65"), families=("hal",))
def mvos_ca(v: View):
    """
    मकारवकारयोश्च परतो मकारान्तस्य धातोर्नकारादेशो भवति — अगन्म, अगन्व, जगन्वान्.

    Only where the म् does not end a pada (Kāśikā: अपदान्तार्थ आरम्भः — at a pada's
    end 8.2.64 has it): the dhātu and its affix are two pieces of one pada,
    `agam~ma`. The two letters are those of *म्वोः* (the sūtra's first word).
    """
    m_letter, v_letter = _letters_of("8.2.65", "o")
    for j in v.junctions():
        m, nxt = j.left, j.right
        if (m.s != m_letter or v.pada_final(m) or not _flag(v, m, "dhatu")
                or nxt.s not in (m_letter, v_letter)):
            continue
        yield Application(
            site=site(m, nxt), edits=(replace(m, "n"),),
            detail=Detail(
                kind=ADESA, sthanin="m", adesa="n",
                nimitta=f"{sk(nxt.s)} follows",
                because=f"the {{dhātu}} ends in {{m}} and {sk(nxt.s)} "
                        f"follows, so the {{m}} becomes {{n}}",
                via=(S.alo_antyasya("m"),)))


# ---------------------------------------------------------------------------
# 8.2.68–72  अहन्, and the Veda's two roads
# ---------------------------------------------------------------------------

_AHAN = _sutra("8.2.68")
_RUPA3 = ("rūpa", "rātri", "rathantara")
# the vārttika's word is those three, the last joined to *eṣu* (a + e = e)
assert "".join(_RUPA3)[:-1] + "eṣu" == to_iast(_VT_RUPARATRI.split()[0]), \
    "8.2.68's vārttika names rūpa, rātri, rathantara"


def _ahan(v: View, sight: Sight) -> bool:
    return _text(v, sight) == _AHAN or _stem(v, sight) == _AHAN


def _sup_follows(v: View, sight: Sight) -> bool:
    nxt = v.next(sight)
    return nxt is not None and v.begins_word(nxt) and _flag(v, nxt, "sup")


@rule("8.2.68", name=_name("8.2.68"),
      families=("visarga", _own("8.2.68")))
def ahan(v: View):
    """
    अहन्नित्येतस्य पदस्य रुर्भवति — अहोभ्याम्, अहोभिः; दीर्घाहा निदाघः; हे दीर्घाहोऽत्र.

    The pada *ahan* (or a word ending in it — the caller's `stem:ahan`). Its न् is
    the sthānin, and it is not dropped first (Kāśikā: नलोपमकृत्वा निर्देशो
    ज्ञापकः — नलोपाभावो यथा स्यादिति). Where no सुप् follows, 8.2.69 takes it
    instead; a सुप् is the caller's `sup` on the ending's word.
    """
    for n in v.live:
        if n.s != "n" or not v.pada_final(n) or not _ahan(v, n):
            continue
        yield Application(
            site=site(n), edits=(_make_ru(n),),
            detail=Detail(
                kind=ADESA, sthanin="n", adesa="ru",
                nimitta="the end of the pada ahan",
                because="the pada {ahan} ends in {n}, so it is replaced by "
                        "{ru} (a सुप् follows, else 8.2.69 would make it "
                        "{r})",
                via=(S.alo_antyasya("n"),)))


@rule("8.2.69", name=_name("8.2.69"),
      families=("visarga", _own("8.2.69")),
      overrides=((_ov("8.2.68"), _q("8.2.69", "kaumudi", "रोरपवादः")),))
def ro_asupi(v: View):
    """
    अह्नो रेफादेशः स्यान्न तु सुपि — अहर्ददाति, अहरहः, अहर्गणः; अहोभ्याम् (a सुप्).

    Not a रु but a plain र् — the र् that stays a र् before a vowel and is a visarga
    only before a खर् or at a pause (8.3.15): *aharahaḥ*, *ahargaṇaḥ*, *ahaḥ*. *Asupi*
    is a negation, not a 'like a सुप्' (Bālamanoramā: प्रसज्यप्रतिषेध): no सुप्
    follows. A pada's सुप् that was elided (*dīrghāhan* + सु, 6.1.68) does not
    count (Kāśikā: अह्नो रविधौ लुमता लुप्ते प्रत्ययलक्षणं न भवति) — the flag is on
    the ending's *word*, and an elided one is no word.
    """
    for n in v.live:
        if (n.s != "n" or not v.pada_final(n) or not _ahan(v, n)
                or _sup_follows(v, n)):
            continue
        yield Application(
            site=site(n), edits=(replace(n, "r"),),
            detail=Detail(
                kind=ADESA, sthanin="n", adesa="r",
                nimitta="the end of the pada ahan, no सुप् after",
                because="the pada {ahan} ends in {n} and no सुप् follows, so "
                        "it is replaced by a plain {r} — not a {ru}",
                via=(S.alo_antyasya("n"),)))


@rule("8.2.68", name=_VT_RUPARATRI, authority=VARTTIKA,
      varttika=_VT_RUPARATRI, families=("visarga",),
      overrides=((_ov("8.2.69"), _q("8.2.68", "kashika",
                                    "इत्यस्यापवादो रुत्वमुपसंख्यायते")),))
def ruparatrirathantaresu(v: View):
    """
    अह्नो रुविधौ रूपरात्रिरथन्तरेषूपसंख्यानं कर्तव्यम् — अहोरूपम्, अहोरात्रः, अहोरथन्तरम्.

    Vārttika: before *rūpa*, *rātri* and *rathantara* it is the रु and not 8.2.69's
    र् (Kāśikā: रोऽसुपि इत्यस्यापवादो रुत्वमुपसंख्यायते). OPEN: another opinion
    (अपर आह) has the रु before any र् — अहोरम्यम्, अहोरत्नानि; not taken.
    """
    for n in v.live:
        if n.s != "n" or not v.pada_final(n) or not _ahan(v, n):
            continue
        nxt = v.next(n)
        if nxt is None or not v.begins_word(nxt) or not any(
                _text(v, nxt).startswith(w) for w in _RUPA3):
            continue
        yield Application(
            site=site(n), edits=(_make_ru(n),),
            detail=Detail(
                kind=ADESA, sthanin="n", adesa="ru",
                nimitta=f"{sk(_text(v, nxt))} follows",
                because="the pada {ahan} is followed by {rūpa}, {rātri} or "
                        "{rathantara}, so its {n} is a {ru} and not a plain "
                        "{r}",
                via=(S.alo_antyasya("n"),), authority=VARTTIKA,
                varttika=_VT_RUPARATRI))


def _gana_words(sutra_id: str) -> Tuple[Tuple[str, ...], ...]:
    return tuple(tuple(g.items) for g in corpus.ganas_for(sutra_id))


@rule("8.2.70", name=_name("8.2.70"), families=("visarga",), vedic=True,
      overrides=(("8.2.66", _q("8.2.70", "kashika",
                               "रुर्वा रेफो वा")),))
def amnarudharavar_ityubhayatha(v: View):
    """
    अम्नस् ऊधस् अवस् इत्येतेषां छन्दसि विषय उभयथा भवति, रुर्वा रेफो वा — अम्न एव,
    अम्नरेव; ऊध एव, ऊधरेव; अव एव, अवरेव.

    Vedic. The three words are those `ru_adesa.UBHAYATHA_THREE` keeps. The plain
    र् is the course that displaces 8.2.66; the other is 8.2.66's own रु (which
    then goes to य् before a vowel, 8.3.17: अम्न एव).
    """
    for s in v.live:
        if s.s == "s" and v.pada_final(s) and _text(v, s) in UBHAYATHA_THREE:
            yield Application(
                site=site(s), edits=(replace(s, "r"),), optional=_UBHAYATHA,
                detail=Detail(
                    kind=ADESA, sthanin="s", adesa="r",
                    nimitta="the end of the pada, in the Veda",
                    because=f"{sk(_text(v, s))} is one of amnas, ūdhas, avas: "
                            f"in the Veda its final is a {{ru}} or a plain "
                            f"{{r}}, and this course takes the {{r}}",
                    via=(S.alo_antyasya("s"),)))


@rule("8.2.70", name=_VT_AHARADI, authority=VARTTIKA, varttika=_VT_AHARADI,
      families=("visarga",),
      overrides=(("8.3.15", _q("8.2.70", "kashika",
                               "विसर्जनीयबाधनार्थमत्र पक्षे रेफस्यैव रेफो "
                               "विधीयते")),))
def aharadinam_patyadisu_va_repha(v: View):
    """
    अहरादीनां पत्यादिषूपसंख्यानं कर्तव्यम् — अहर्पतिः, अहःपतिः; गीर्पतिः, गीःपतिः;
    धूर्पतिः, धूःपतिः.

    Vārttika, from the gaṇapāṭha: the words are the *aharādi* gaṇa (ahar, gīr,
    dhur), the following ones the *patyādi* gaṇa (pati, gaṇa, putra). Where 8.3.15
    would make the र् a visarga before a खर्, the र् may stay a र् (विसर्जनीयबाधनार्थम्)
    — a refusal of 8.3.15, at its very place.
    """
    aharadi, patyadi = _gana_words("8.2.70")
    khar = _khar()
    for r in v.live:
        if r.s != "r" or not v.pada_final(r):
            continue
        nxt = v.next(r)
        if nxt is None or nxt.s not in khar or not v.begins_word(nxt):
            continue
        word = _text(v, r)
        if not (_shorten(word) in {_shorten(w) for w in aharadi}
                or word == _AHAN or _stem(v, r) == _AHAN):
            continue
        if not any(_form_of(_text(v, nxt), w) for w in patyadi):
            continue
        yield Application(
            site=site(r, nxt), edits=(), optional=_VA,
            detail=Detail(
                kind=PRATISEDHA, sthanin="r", adesa="",
                nimitta=f"{sk(_text(v, nxt))} follows",
                because=f"{sk(word)} is of the aharādi gaṇa and "
                        f"{sk(_text(v, nxt))} of the patyādi: the {{r}} may "
                        f"stay a {{r}} and not become the visarga",
                via=(), authority=VARTTIKA, varttika=_VT_AHARADI))


#: The word 8.2.71 names — *bhuvas* — read off the sūtra's first word, *bhuvaśca*
#: (the visarga of *bhuvaḥ* joined to *ca*), with the स् this module reads a
#: visarga as (8.2.66).
_BHUVAS = _sutra("8.2.71").split()[0][:-len("śca")] + "s"


@rule("8.2.71", name=_name("8.2.71"), families=("visarga",), vedic=True,
      overrides=(("8.2.66", _q("8.2.71", "kashika", "रुर्वा रेफो वा")),))
def bhuvas_ca_mahavyahrteh(v: View):
    """
    भुवस् इत्येतस्य महाव्याहृतेश्छन्दसि विषय उभयथा भवति, रुर्वा रेफो वा — भुव इत्यन्तरिक्षम्,
    भुवरित्यन्तरिक्षम्.

    Vedic. *Mahāvyāhṛteriti kim?* भुवो विश्वेषु सवनेषु यज्ञियः — the word is not the
    mahāvyāhṛti: the caller's flag `mahavyahrti`.
    """
    word = _BHUVAS
    for s in v.live:
        if (s.s == "s" and v.pada_final(s) and _text(v, s) == word
                and _flag(v, s, "mahavyahrti")):
            yield Application(
                site=site(s), edits=(replace(s, "r"),), optional=_UBHAYATHA,
                detail=Detail(
                    kind=ADESA, sthanin="s", adesa="r",
                    nimitta="the end of the pada bhuvas, the mahāvyāhṛti",
                    because="{bhuvas} as the mahāvyāhṛti has, in the Veda, a "
                            "{ru} or a plain {r}; this course takes the {r}",
                    via=(S.alo_antyasya("s"),)))


_VASU, _SRAMS, _DHVAMS, _ANADUH = VASU_FOUR


@rule("8.2.72", name=_name("8.2.72"), families=("visarga",),
      overrides=(
          ("8.2.66", _q("8.2.72", "kashika",
                        "रुत्वे नाप्राप्त इदमारभ्यत इति तद् बाध्यते")),
          ("8.2.31", _q("8.2.72", "kashika",
                        "अनडुहोऽपि ढत्वमनेन बाध्यते"))))
def vasu_sramsu_dhvamsu_anaduham_dah(v: View):
    """
    वस्वन्तस्य पदस्य सकारान्तस्य, स्रंसु, ध्वंसु, अनडुह् इत्येतेषां च दकारादेशो भवति —
    विद्वद्भ्याम्, पपिवद्भिः, उखास्रद्भ्याम्, पर्णध्वद्भ्याम्, अनडुद्भ्याम्.

    PARTIAL. The पद ends in क्वसु (the caller's flag `kvasu`) or in *sraṃs*,
    *dhvaṃs*, *anaḍuh* (which `ru_adesa.VASU_FOUR` keeps, and whose spelling is
    read off the end of the word). *Sa iti eva* — विद्वान् (an न् ends the word, so
    there is no स् to change). It displaces the रु of 8.2.66 (रुत्वे नाप्राप्त
    इदमारभ्यते) and, for अनडुह्, the ढ् of 8.2.31 (अनडुहोऽपि ढत्वमनेन बाध्यते).
    """
    for s in v.live:
        if not v.pada_final(s):
            continue
        text = _text(v, s)
        bare = text.replace("ṃ", "")
        if s.s == "s" and (_flag(v, s, "kvasu")
                           or bare.endswith(_SRAMS.replace("ṃ", ""))
                           or bare.endswith(_DHVAMS.replace("ṃ", ""))):
            pass
        elif s.s == "h" and text.endswith(_ANADUH):
            pass
        else:
            continue
        yield Application(
            site=site(s), edits=(replace(s, "d"),),
            detail=Detail(
                kind=ADESA, sthanin=s.s, adesa="d",
                nimitta="the end of a pada of vasu, sraṃs, dhvaṃs or anaḍuh",
                because=f"the pada {sk(text)} is of {{vasu}}, {{sraṃs}}, "
                        f"{{dhvaṃs}} or {{anaḍuh}}, so its final {sk(s.s)} "
                        f"becomes {{d}}",
                via=(S.alo_antyasya(s.s),)))


# ---------------------------------------------------------------------------
# 8.2.76–79  the penult before र् and व् of a dhātu
# ---------------------------------------------------------------------------


def _rv() -> Tuple[str, ...]:
    """र् and व् — the two letters of *र्वोः*."""
    return _letters_of("8.2.76", "or")


def _lengthened_upadha(v: View, x: Sight) -> Optional[Tuple[Sight, str]]:
    """The penult of the piece ending in `x`, and its long — if it is
    a short इक् (6.3.111's method: `akah_savarne_dirghah`, the nearest long)."""
    prev = v.prev(x)
    if prev is None or prev.w != x.w or not S.is_member(prev.s, "iK"):
        return None
    if duration(prev.s) != 1:
        return None
    got = akah_savarne_dirghah(prev.s, prev.s)
    if got.result is None or got.result == prev.s:
        return None
    return prev, got.result


@rule("8.2.76", name=_name("8.2.76"), families=("visarga",))
def rvor_upadhaya_dirgha_ikah(v: View):
    """
    रेफवकारान्तस्य धातोः पदस्योपधाया इको दीर्घो भवति — गीः, धूः, पूः, आशीः.

    The पद ends in a dhātu (the caller's `dhatu`) whose last sound is र् or व्.
    *Upadhāgrahaṇaṃ kim?* अबिभर्भवान् (the इ of the reduplication is not the
    penult). *Dhātoriti eva* — अग्निः, वायुः. *Padasyeti eva* — गिरौ, गिरः (the र्
    is not at the end). The word arrives with its penult short; a word that
    arrives already long is left alone.
    """
    for x in v.live:
        if x.s not in _rv() or not v.pada_final(x) or not _flag(v, x, "dhatu"):
            continue
        found = _lengthened_upadha(v, x)
        if found is None:
            continue
        prev, long = found
        yield Application(
            site=site(prev, x), edits=(replace(prev, long),),
            detail=Detail(
                kind=ADESA, sthanin=prev.s, adesa=long,
                nimitta=f"the pada ends in the dhātu's {sk(x.s)}",
                because=f"{sk(prev.s)} is the penult of a pada that ends in "
                        f"{sk(x.s)} of a {{dhātu}}, so it is lengthened to "
                        f"{sk(long)}",
                via=(S.pratyahara("iK", "i, u, ṛ, ḷ"),)))


@rule("8.2.77", name=_name("8.2.77"), families=("visarga",))
def hali_ca_dirgha(v: View):
    """
    हलि च परतो रेफवकारान्तस्य धातोरुपधाया इको दीर्घो भवति — आस्तीर्णम्, विशीर्णम्,
    दीव्यति, सीव्यति.

    Where the र्/व् does not end the पद — 8.2.76 has that (अपदान्तार्थोऽयमारम्भः).
    The dhātu and the affix are two pieces of one पद (`div~yati`). *Dhātoriti
    eva* — दिवमिच्छति दिव्यति (denominative). *Ika iti eva* — स्मर्यते, भव्यम्.
    """
    hal = HAL
    for j in v.junctions():
        x, nxt = j.left, j.right
        if (x.s not in _rv() or v.pada_final(x) or nxt.s not in hal
                or not _flag(v, x, "dhatu")):
            continue
        found = _lengthened_upadha(v, x)
        if found is None:
            continue
        prev, long = found
        yield Application(
            site=site(prev, x), edits=(replace(prev, long),),
            detail=Detail(
                kind=ADESA, sthanin=prev.s, adesa=long,
                nimitta=f"the consonant {sk(nxt.s)} follows the dhātu",
                because=f"{sk(prev.s)} is the penult of a {{dhātu}} ending in "
                        f"{sk(x.s)}, and the consonant {sk(nxt.s)} follows, "
                        f"so it is lengthened to {sk(long)}",
                via=(S.pratyahara("iK", "i, u, ṛ, ḷ"),)))


@rule("8.2.79", name=_name("8.2.79"), families=("visarga",),
      overrides=(
          ("8.2.76", _q("8.2.79", "kashika",
                        "रेफवकारान्तस्य भस्य कुर् छुर् इत्येतयोश्च दीर्घो न भवति")),
          ("8.2.77", _q("8.2.79", "kashika",
                        "रेफवकारान्तस्य भस्य कुर् छुर् इत्येतयोश्च दीर्घो न भवति"))))
def na_bhakurchuram(v: View):
    """
    रेफवकारान्तस्य भस्य कुर् छुर् इत्येतयोश्च दीर्घो न भवति — धुर्यः, दिव्यम्, कुर्यात्,
    छुर्यात्.

    A refusal, at the very place of 8.2.76 and 8.2.77. *Bha* (1.4.18) is the
    caller's flag `bha`; *kur* and *chur* are the words `ru_adesa.BHA_KUR_CHUR`
    keeps. *Reph-vakārābhyāṃ bha-viśeṣaṇaṃ kim?* प्रतिदीव्ना — a भ whose व् is not
    final is lengthened all the same.
    """
    _bha, kur, chur = BHA_KUR_CHUR
    for x in v.live:
        if x.s not in _rv() or not _flag(v, x, "dhatu"):
            continue
        if not (_flag(v, x, "bha") or _text(v, x) in (kur, chur)):
            continue
        if _lengthened_upadha(v, x) is None:
            continue
        prev = v.prev(x)
        yield Application(
            site=site(prev, x), edits=(),
            detail=Detail(
                kind=PRATISEDHA, sthanin=prev.s, adesa="",
                nimitta=f"the word is a {{bha}} or {{kur}}/{{chur}}",
                because=f"{sk(_text(v, x))} is a {{bha}} or is {{kur}} or "
                        f"{{chur}}, so the penult {sk(prev.s)} is not "
                        f"lengthened",
                via=()))


RULES = (sasajuso_ruh, ato_ror_aplutad_aplute, hasi_ca, etattadoh_sulopo,
         syas_chandasi_bahulam, so_aci_lope_cet_padapuranam, dho_dhe_lopah,
         ro_ri, dhralope_purvasya_dirgho_nah, kharavasanayor_visarjaniyah,
         ro_supi, bhobhago_yo_si, vyor_laghuprayatnatarah, lopah_sakalyasya,
         oto_gargyasya, unci_ca_pade, hali_sarvesam,
         visarjaniyasya_sah, sampumkanam_so_vaktavyah, sarpare_visarjaniyah,
         va_sari, kharpare_sari_va_visargalopah, kupvoh_kah_pau_ca,
         so_apadadau, so_apadadav_anavyayasya, kamye_roreva, inah_sah,
         namaspurasor_gatyoh, idudupadhasya_capratyayasya,
         tiraso_nyatarasyam, dvistriscatur_krtvo_rthe, isusoh_samarthye,
         nityam_samase_nuttarapadasthasya, atah_krkami, adhah_sirasi_pade,
         kaskadisu_ca, chandasi_va_apramreditayoh, kah_karat_karati_krdhi_krte,
         pancamyah_paravadhyarthe, patau_ca_bahulam, sasthyah_patiputra,
         idayah_va,
         ubhayatharksu, dirghad_ati_samanapade, nrn_pe, svatavan_payau,
         kan_amredite, mo_no_dhatoh, mvos_ca, ahan, ro_asupi,
         ruparatrirathantaresu, amnarudharavar_ityubhayatha,
         aharadinam_patyadisu_va_repha, bhuvas_ca_mahavyahrteh,
         vasu_sramsu_dhvamsu_anaduham_dah, rvor_upadhaya_dirgha_ikah,
         hali_ca_dirgha, na_bhakurchuram)

#: Which sūtras of this family's scope the module implements — the honest
#: account, kept beside the code. See `rulebook.COVERAGE_STATUS`. Every sūtra of
#: 8.2.62–81, 8.3.8–22, 8.3.34–54, 6.1.113–114, 6.3.111 and 6.1.132–135 is here.
COVERAGE = (
    ("8.2.62", "scope",
     "क्विन्प्रत्ययस्य कुः gives a guttural to the last sound of a word whose ROOT "
     "took क्विन् (घृतस्पृक्): a fact about how the stem was built, which no "
     "letter of the finished word says; the words arrive already formed"),
    ("8.2.63", "scope",
     "नशेर्वा — the same for the root नश् with क्विप् (जीवनक्, जीवनट्): a "
     "root-and-affix derivation whose result arrives as a finished word, and "
     "its ट्/क् alternative is 8.2.36's contest, not a junction"),
    ("8.2.64", "rule",
     "for a word that ends in a dhātu — the caller's flag `dhatu`"),
    ("8.2.65", "rule",
     "for the म् of a dhātu that does not end a pada — flag `dhatu`, boundary ~"),
    ("8.2.66", "rule", ""),
    ("8.2.67", "scope",
     "अवयाः, श्वेतवाः, पुरोडाः are laid down whole by निपातन (with the दीर्घ of "
     "the vocative): a finished word is the input, and 8.2.66 works on its स् "
     "like any other"),
    ("8.2.68", "rule",
     "with the two vārttikas' word rūpa/rātri/rathantara; the alternative "
     "opinion (a रु before any र्) is not taken — OPEN"),
    ("8.2.69", "rule",
     "a सुप् is the caller's flag `sup` on the ending's word"),
    ("8.2.70", "vedic",
     "also carries the vārttika अहरादीनां पत्यादिषु वा रेफः, which is not Vedic"),
    ("8.2.71", "vedic", "the mahāvyāhṛti is the caller's flag"),
    ("8.2.72", "partial",
     "the word is known by the caller's `kvasu`, or by ending in स्रंस्, "
     "ध्वंस्, अनडुह्; another word of those roots is not seen; अनडुह्'s ह् is "
     "first the hal family's (8.2.31), which this rule displaces by name"),
    ("8.2.73", "scope",
     "conditioned on the affix तिप्, which has been lost (6.1.66) before the "
     "word reaches a junction — no sound of it records that; it would need a "
     "flag naming the lost affix"),
    ("8.2.74", "scope",
     "conditioned on the affix सिप्, lost before the junction (6.1.66) — same "
     "reason as 8.2.73"),
    ("8.2.75", "scope",
     "conditioned on the affix सिप्, lost before the junction (6.1.66) — same "
     "reason as 8.2.73"),
    ("8.2.76", "rule",
     "for a word ending in a dhātu's र्/व् — flag `dhatu`; a penult that "
     "arrives long is left alone"),
    ("8.2.77", "rule",
     "at the junction of a dhātu and an affix beginning with a consonant — "
     "flag `dhatu`, boundary ~"),
    ("8.2.78", "scope",
     "the र्/व् is the penult INSIDE a dhātu (हूर्छिता, ऊर्विता) and its trigger "
     "is another consonant of the same dhātu: there is no junction, and the "
     "engine does not rewrite the inside of a word"),
    ("8.2.79", "partial",
     "a भ (1.4.18) is the caller's flag `bha`; कुर् and छुर् are known by the "
     "word; it refuses 8.2.76–77 (8.2.78 is not implemented)"),
    ("8.2.80", "scope",
     "rebuilds the STEM अदस् (अमु-, अमी) before any junction: the finished "
     "stem arrives, with the flag `adas` for 1.1.12"),
    ("8.2.81", "scope",
     "rebuilds the stem अदस् in the plural (अमी) — as 8.2.80, a stem-building "
     "rule whose result is the input of a junction"),
    ("8.3.8", "vedic",
     "an option on the रु 8.3.7 (nasal family) gives; the न्-stays course "
     "needs 8.3.7 to stand aside in ṛk verses — OPEN, see the report"),
    ("8.3.9", "vedic", "one pāda is the caller's flag `antahpada`"),
    ("8.3.10", "rule",
     "optional as the Kaumudī and Laghu read it; the Kāśikā's nitya reading "
     "is OPEN"),
    ("8.3.11", "rule",
     "optional as the Kaumudī reads it; the Kāśikā's nitya reading is OPEN"),
    ("8.3.12", "rule",
     "the रु-route of the Kaumudī and Laghu; the Kāśikā's direct स् is OPEN"),
    ("8.3.13", "rule", ""),
    ("8.3.14", "rule", ""),
    ("8.3.15", "rule", ""),
    ("8.3.16", "rule", "the locative plural is the caller's flag"),
    ("8.3.17", "rule", ""),
    ("8.3.18", "partial",
     "offered only where the caller asks (`sakatayana`): its product is spelt "
     "exactly as the sound it replaces, so offering it at every meeting "
     "would double every derivation and change no letter"),
    ("8.3.19", "rule", ""),
    ("8.3.20", "rule", ""),
    ("8.3.21", "rule",
     "whether the lighter य् survives before उञ् is OPEN (taken as after ओ)"),
    ("8.3.22", "rule", ""),
    ("8.3.34", "rule",
     "with the vārttika संपुंकानां सो वक्तव्यः; in the कवर्ग/पवर्ग field it "
     "yields to 8.3.37"),
    ("8.3.35", "rule", ""),
    ("8.3.36", "rule", "with the vārttika खर्परे शरि वा विसर्गलोपः"),
    ("8.3.37", "rule", ""),
    ("8.3.38", "rule",
     "an affix's कु/पु is the caller's flag `pratyaya`; the vārttikas "
     "अनव्ययस्य and काम्ये रोरेव are refusals; पाशकल्पककाम्येषु is a "
     "sambhavadarśana and is not a rule of its own"),
    ("8.3.39", "rule", ""),
    ("8.3.40", "rule", "a गति is the caller's flag `gati`"),
    ("8.3.41", "partial",
     "an affix's visarga is known by the closed list (निर्, दुर्, बहिर्, "
     "आविस्, चतुर्, प्रादुस्) or by the caller's `apratyaya`; the vārttika "
     "एकादेशशास्त्रनिमित्तकस्य न षत्वम् (मातुः कृपा) is not implemented — the "
     "ऋ→उ ekādeśa leaves no trace at the junction; मुहुसः प्रतिषेधः is"),
    ("8.3.42", "rule", "a गति is the caller's flag `gati`"),
    ("8.3.43", "rule", "the sense 'times' is the caller's flag `krtvo_artha`"),
    ("8.3.44", "rule",
     "इस्/उस् and सामर्थ्य are the caller's flags `isus`, `samartha`"),
    ("8.3.45", "rule", "इस्/उस् is the caller's flag `isus`"),
    ("8.3.46", "rule",
     "the seven are known by their spelling; कृ and कमि by the caller's "
     "`dhatu:kṛ`, `dhatu:kam`"),
    ("8.3.47", "rule", ""),
    ("8.3.48", "partial",
     "a gaṇa of FINISHED words (an ākṛtigaṇa): a pair is recognised if its "
     "spelling begins an item of the list on disk; a word the list does not "
     "spell is not seen"),
    ("8.3.49", "vedic", ""),
    ("8.3.50", "vedic", ""),
    ("8.3.51", "vedic", "the case and the sense are the caller's flags"),
    ("8.3.52", "vedic", "बहुलम् — both courses are returned"),
    ("8.3.53", "vedic", "the case is the caller's flag `sasthi`"),
    ("8.3.54", "vedic", ""),
    ("6.1.113", "rule", ""),
    ("6.1.114", "rule", ""),
    ("6.3.111", "rule", ""),
    ("6.1.132", "rule",
     "the सु is the final स् of eṣas / sas or of a word given `stem:etad` or "
     "`stem:tad`; the sākac form and the नञ्-compound are flags"),
    ("6.1.133", "vedic", "बहुलम् — both courses are returned"),
    ("6.1.134", "rule",
     "पादपूरणम् is metre and is the caller's flag `padapuranam`"),
    ("6.1.135", "scope",
     "an अधिकार, the heading of the सुट्-āgama sūtras 6.1.136–157 "
     "(सम्पर्युपेभ्यः करोतौ भूषणे …): it governs affixes, not a junction "
     "of words, and nothing in this family reads it"),
)
