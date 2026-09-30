# -*- coding: utf-8 -*-
"""
६.१.८४–११२ — एकः पूर्वपरयोः, and the single substitutes it governs.

From 6.1.84 to 6.1.111 whatever is put in place stands for the earlier sound
and the later one **together** — not for one of them, and not for each. That is
why the substitute is built here as ONE edit over two sounds (`ekadesa`), and
why it belongs to the later word and remembers the earlier (6.1.85 अन्तादिवत्).
6.1.112 stands outside the heading (*ख्यत्यात् परस्य*: the substitute is for the
later sound alone) but closes the same stretch of अ-sandhi.

**The rules are a chain of exceptions, and the arrangement is the grammar.**
The Kāśikā states the principle at 6.1.89 in a line the engine needs whole:
*पुरस्तादपवादा अनन्तरान् विधीन् बाधन्ते नोत्तरान्* — an exception stated
earlier displaces only what stands nearest after it, never what lies beyond.

    6.1.87  आद्गुणः            guṇa — the general rule
    6.1.88  वृद्धिरेचि          vṛddhi before an एच् — excepts 6.1.87
    6.1.89  एत्येधत्यूठ्सु       vṛddhi before एति, एधति, ऊठ् — excepts 6.1.94 (6.1.87 for ऊठ्)
                              and, by that maxim, NOT 6.1.95
    6.1.90  आटश्च             vṛddhi after the augment आट् — the ca excepts 6.1.95, 6.1.96
    6.1.91  उपसर्गादृति धातौ    vṛddhi of upasarga + ṛ-dhātu — excepts 6.1.87
    6.1.92  वा सुप्यापिशलेः     the same, optional when a subanta is inside the dhātu
    6.1.93  औतोऽम्शसोः         ā for o + am/śas
    6.1.94  एङि पररूपम्         the later sound for upasarga + eṅ-dhātu — excepts 6.1.88
    6.1.95  ओमाङोश्च          the later sound before om and āṅ — excepts 6.1.88, 6.1.101
    6.1.96  उस्यपदान्तात्       the later sound before us inside a pada
    6.1.97  अतो गुणे          the later sound for a + guṇa — excepts 6.1.101, NOT 6.1.102
    6.1.98  अव्यक्तानुकरणस्यात इतौ   the later इ for the whole *at* of an imitation and इति
    6.1.99  नाम्रेडितस्यान्त्यस्य तु वा  …refused for the repeated member, optional for its t
    6.1.100 नित्यमाम्रेडिते डाचि  the later sound for the t and the first sound of the repeat
    6.1.101 अकः सवर्णे दीर्घः    the long vowel where the two are alike
    6.1.102 प्रथमयोः पूर्वसवर्णः  the earlier sound's long form before the first two cases
    6.1.103 तस्माच्छसो नः पुंसि    the s of शस् becomes n after it, in the masculine
    6.1.104–106  the refusals of 6.1.102: नादिचि, दीर्घाज्जसि च, and वा छन्दसि
    6.1.107 अमि पूर्वः          the earlier sound before अम्
    6.1.108 सम्प्रसारणाच्च       the earlier sound (a samprasāraṇa vowel) before an अच्
    6.1.109 एङः पदान्तादति      the earlier sound for a pada-final एङ् + अ
    6.1.110 ङसिङसोश्च          the same, inside a pada, before the अ of ङसि, ङस्
    6.1.111 ऋत उत्            उ (with रपर) for a ṛ-varṇa + the अ of ङसि, ङस्
    6.1.112 ख्यत्यात् परस्य      the अ of ङसि, ङस् alone becomes उ after khy, ty (no एकादेश)

Each relation is declared on the rule that wins, with the tradition's own words
as its reason, so a step in a trace can say *why* a rule lost. Where the
commentaries disagree about a relation, or leave a question open, the module
takes the reading the Kāśikā and the Kaumudī share and records the other in
`OPEN` (an OPEN or SCOPE note with its quotations) and in the rule's docstring.

**Which substitute is not chosen here.** 6.1.87's guṇa is `adesa.guna_of` (1.1.2
naming the candidates, 1.1.50 choosing, 1.1.51 adding the र् of ṛ), 6.1.88's
vṛddhi is `adesa.vrddhi_of`, 6.1.101's long vowel is
`anga.akah_savarne_dirghah` (1.1.9 asking whether the two are alike), 6.1.97 asks
`anga.ato_gune`. The pararūpa and pūrvarūpa rules put in **one of the two sounds
they are given** — that is the whole content of their names — so no sound is
written in them.

**What the letters cannot say — read from the word's flags, never guessed.**
The README's vocabulary (`upasarga`, `dhatu[:ROOT]`, `ang`, `nipata`, `stem:X`)
and the boundary kind UPASARGA are used as documented. This family also reads
the flags below (a caller sets them in braces, one group per word:
``hare~as{sup:ṅas}``), each of which says something no reading of the letters can:

    upasarga      the word is a preverb (1.4.59) — or the boundary is ``|``
    dhatu[:ROOT]  the word is (or begins with) a dhātu, and which (1.3.1)
    ang           the word is the preverb आङ्, **or begins with the substitute in
                  which आङ् has fused with the dhātu's vowel** (ehi, oḍhā). 6.1.85
                  makes that substitute the END of आङ्, and आङ् is one sound, so
                  the substitute *is* आङ् for 6.1.95 — the Bālamanoramā on 6.1.95:
                  आःइहीति स्थिते गुणे एहीति रूपम्, ततः शिव-एहि इति स्थिते वृद्धिं
                  बाधित्वा पररूपमेकारः
    nipata        the particle (1.4.56); with the text `om` it is ओम् for 6.1.95
    aat           the piece is the augment आट् (6.4.72), for 6.1.90
    uth           the word begins with the ऊठ् that replaces वाह्'s va (6.4.132); the
                  closed vocabulary's `stem:ūṭh` says the same
    subanta       the dhātu has a subanta inside it — a नामधातु (ṛṣabhīyati), 6.1.92
    sup:NAME      the piece is the case ending NAME (`jas`, `au`, `śas`, `am`, `ṅas`,
                  `ṅasi`, `ṅe` …) — its letters `as` are the same for jas and śas.
                  `stem:NAME` (the README's `stem:X`) is read the same way
    pum           the stem is masculine (6.1.103 पुंसि)
    krdanta       the word is a nominal kṛdanta, neither tiṅanta nor lyabanta
                  (the Bālamanoramā on 6.1.89: तेन तिङन्ते ल्यबन्ते च न वृद्धिः)
    trtiya        the first member of a compound stands in the instrumental
                  (6.1.89 vārttika ऋते च तृतीयासमासे)
    aniyoga       the particle एव is not restrictive (6.1.94 vārttika एवे चानियोगे)
    avyakta       the word is the imitation of an indistinct sound (6.1.98–100)
    amredita      the word is the repeated (second) member of such a doubling
    dac           the word ends in ḍāc (6.1.100)
    samprasarana  the sound is a samprasāraṇa vowel (1.1.45) — 6.1.15 ff. that make
                  it are not in the engine, so the caller says so (6.1.108); the ऊठ्
                  (`uth`) is one by 1.1.45 and needs no second flag
    keśaveśe, paśupakṣiṇoḥ
                  the sense a śakandhvādi entry is restricted to, spelled as the
                  gaṇapāṭha spells it

**Refusals.** 6.1.104 and 6.1.105 refuse 6.1.102, and the guṇa/vṛddhi/yaṇ that
the exception was shadowing must come back (*बाधके निवृत्ते गुणः पुनरुन्मिषति*,
Bālamanoramā on 6.1.104). The engine's own refusal (an Application with
`edits=()`) records that **every** rule displaced at the site is not to be
offered there again — right for शात् refusing चुत्व, wrong here, where the
general rule is the answer. So these two refusals put a MARK on the earlier vowel
(`remark`) that 6.1.102 reads. The step is still a step (kind pratiṣedha, the
sthānin unchanged), and the vowels are then open to whatever else applies. The
same reason makes 6.1.98's refusal by the vārttika एकाचो न the engine's own:
nothing revives there.

**Options.** Every विभाषा here passes ``optional="वा"``. 6.1.92, the vārttikas of
6.1.94 and 6.1.101, 6.1.106 and 6.1.108 are *prāptavibhāṣā* — what the option
displaces was already due; 6.1.99 is *aprāptavibhāṣā* (nothing was due for the t
alone). Where the optional rule is the exception, the declined course falls to
the rule it displaced: 6.1.88 for 6.1.94, 6.1.101 for its vārttikas, 6.1.105's
refusal (and then 6.1.77) for 6.1.106 — and, 6.1.91 standing aside for a subanta
dhātu where 6.1.92 replaces its nityatva, 6.1.87 for 6.1.92.
"""

from __future__ import annotations

from typing import Callable, List, Optional, Sequence, Tuple

from src.astadhyayi import corpus
from src.astadhyayi.adesa import guna_of, raparatva, ti as ti_of, vrddhi_of
from src.astadhyayi.anga import akah_savarne_dirghah, ato_gune
from src.astadhyayi.grahana import kala
from src.astadhyayi.sandhi import supports as S
from src.astadhyayi.sandhi import trace
from src.astadhyayi.sandhi.parse import tokenize
from src.astadhyayi.sandhi.rule import (
    sk,
    ADESA, EKADESA, PRATISEDHA, SUTRA, VARTTIKA, Application, Detail, NewSeg,
    Via, ekadesa, remark, replace, rule, site)
from src.astadhyayi.sandhi.segs import (
    AVAGRAHA, SAMASA, UPASARGA, Junction, Sight, View, Word)
from src.astadhyayi.sup import SUP
from src.astadhyayi.varna import savarna, savarnas_of

# ---------------------------------------------------------------------------
# What this family reads from a word — see the module docstring
# ---------------------------------------------------------------------------

F_UPASARGA = "upasarga"
F_DHATU = "dhatu"
F_ANG = "ang"
F_NIPATA = "nipata"
F_AAT = "aat"
F_UTH = "uth"
F_SUBANTA = "subanta"
F_SUP = "sup"
F_PUM = "pum"
F_KRDANTA = "krdanta"
F_TRTIYA = "trtiya"
F_ANIYOGA = "aniyoga"
F_AVYAKTA = "avyakta"
F_AMREDITA = "amredita"
F_DAC = "dac"
F_SAMPRASARANA = "samprasarana"

FAMILIES = ("ac", "ekadesa")

#: The mark 6.1.104 and 6.1.105 put on the earlier vowel of a pair, so that
#: 6.1.102 does not offer itself there again.
NO_PURVASAVARNA = "pūrvasavarṇa-niṣiddha"
#: A vowel of two mātrās that is not one of the alphabet's long vowels — the
#: single substitute the vārttikas of 6.1.101 lay down (ऋति सवर्णे ऋ वा).
DVIMATRA = "dvimātra"

#: The a-varṇa, and the ṛ-varṇa that the Kāśikā on 6.1.92 says ऋति covers
#: (ऋकारऌकारयोः सावर्ण्यविधिः इति ऋतीति ऌकारोऽपि गृह्यते) — 1.1.9 asked, not typed.
AVARNA = frozenset(savarnas_of("a"))
RVARNA = frozenset(savarnas_of("ṛ"))


# ---------------------------------------------------------------------------
# What the tradition says, checkable — quotes and vārttikas come from the disk
# ---------------------------------------------------------------------------

_WORK = {"kashika": "Kāśikā", "kaumudi": "Siddhāntakaumudī",
         "balamanorama": "Bālamanoramā", "tattvabodhini": "Tattvabodhinī",
         "bhashya": "Mahābhāṣya"}

#: Every quotation this module gives as a reason, as (work, sūtra, words) — so
#: `tests/test_sandhi_ac_ekadesa.py` can read each one back out of the
#: commentary it names. A reason that cannot be found there fails a test.
QUOTES: List[Tuple[str, str, str]] = []


def _quote(work: str, sutra: str, words: str) -> str:
    """A reason for an `overrides` entry: the tradition's own words, and where."""
    QUOTES.append((work, sutra, words))
    return f"{words} ({_WORK[work]} on {sutra})"


def _varttika(sutra: str, needle: str) -> str:
    """The vārttika on `sutra` that contains `needle`, exactly as the corpus has it."""
    for found in corpus.varttikas_on(sutra):
        if needle in found.text:
            return found.text
    raise LookupError(f"no vārttika on {sutra} contains {needle!r}")


def _name(sutra: str) -> str:
    """The sūtra's own words in Devanāgarī, from the corpus."""
    return trace.deva(trace.sutra_text(sutra))


V_AKSAT_UHINYAM = _varttika("6.1.89", "अक्षादूहिन्या")
V_SVADIRERINOH = _varttika("6.1.89", "स्वादीरे")
V_PRADUHODHODHYESAISYESU = _varttika("6.1.89", "प्रादूह")
V_RTE_TRTIYASAMASE = _varttika("6.1.89", "ऋते च तृतीयासमासे")
V_PRAVATSATARA = _varttika("6.1.89", "प्रवत्सतर")
V_SAKANDHVADISU = _varttika("6.1.94", "शकन्ध्वादिषु")
V_EVE_CANIYOGE = _varttika("6.1.94", "एवे चानियोगे")
V_OTVOSTHAYOH = _varttika("6.1.94", "ओत्वोष्ठयोः")
V_EMANNADISU = _varttika("6.1.94", "एमन्नादिषु")
V_EKACO_NA = _varttika("6.1.98", "एकाचो न")
V_RTI_SAVARNE = _varttika("6.1.101", "ऋति सवर्णे")
V_LTI_SAVARNE = _varttika("6.1.101", "ऌति सवर्णे")


# ---------------------------------------------------------------------------
# Small questions, asked once
# ---------------------------------------------------------------------------


def _sounds(text: str) -> Tuple[str, ...]:
    return tuple(sound for sound, _ in tokenize(text))


def _idx(seg) -> frozenset:
    """The words a sound belongs to: its own, and — for a single substitute —
    the earlier one it also stands in (6.1.85)."""
    return frozenset({seg.w}) if seg.lw is None else frozenset({seg.w, seg.lw})


def _begins(v: View, sight: Sight, word: int) -> bool:
    """`sight` is the first live sound of word number `word` (6.1.85 counted)."""
    if word not in _idx(sight.seg):
        return False
    return not any(word in _idx(t.seg) for t in v.live[:v.index(sight)])


def _bare(word: Word) -> str:
    """The word's letters, with the visarga the parser read as s or r taken off."""
    if word.has("final:s") or word.has("final:r"):
        return word.text[:-1]
    return word.text


def _matches(word: Word, forms: Sequence[str]) -> bool:
    return _bare(word) in forms or word.flag_value("stem") in forms


def _named(v: View, sight: Sight, *forms: str) -> bool:
    """`sight` begins a word that a rule names — by its letters or by `stem:`."""
    return v.begins_word(sight) and _matches(v.word(sight), forms)


def _ends_named(v: View, sight: Sight, *forms: str) -> bool:
    """`sight` ends a word that a rule names."""
    return v.ends_word(sight) and _matches(v.word(sight), forms)


def _dhatu(word: Word) -> bool:
    return word.has(F_DHATU) or word.flag_value(F_DHATU) is not None


def _upasarga_dhatu(v: View, j: Junction) -> bool:
    """A preverb, then its dhātu — what 6.1.91, 6.1.92 and 6.1.94 stand on.

    The letters cannot say it, so it is read: the boundary written ``|`` means a
    preverb and its dhātu (README); otherwise the left word must carry
    `upasarga` and the right `dhatu`. The preverb ends a word and the dhātu
    begins one.
    """
    if not v.ends_word(j.left) or not v.begins_word(j.right):
        return False
    if j.kind == UPASARGA:
        return True
    return v.word(j.left).has(F_UPASARGA) and _dhatu(v.word(j.right))


def _rt(sound: str) -> bool:
    """`ṛt` — a ṛ-varṇa of one mātrā (1.1.70: a sound named with a त् names only
    sounds of its own measure), ḷ included by the Kāśikā on 6.1.92."""
    return sound in RVARNA and kala(sound) == kala("a")


def _ending_of(word: Word) -> Optional[str]:
    """Which of 4.1.2's twenty-one endings a piece is, as the caller says.

    The letters cannot: `as` is जस् and शस् and ङस्, `au` औ and औट्. The caller's
    flag is `sup:NAME`, and the closed vocabulary's `stem:X` (README) is read the
    same way where X is one of the twenty-one — `stem:śas` says of the piece `as`
    what `stem:īra` says of a word: which lexical item it is.
    """
    named = word.flag_value(F_SUP)
    if named is not None:
        return named
    stem = word.flag_value("stem")
    return stem if stem in SUP else None


def _sup(v: View, sight: Sight) -> Optional[str]:
    """Which case ending the word beginning at `sight` is, or None."""
    if not v.begins_word(sight):
        return None
    return _ending_of(v.word(sight))


def _is_uth(word: Word) -> bool:
    """The word begins with the ऊठ् that replaces वाह्'s va (6.4.132): `uth`, or
    `stem:ūṭh`."""
    return word.has(F_UTH) or word.flag_value("stem") == "ūṭh"


def _samprasarana(word: Word) -> bool:
    """The piece is a samprasāraṇa vowel (1.1.45): the caller's word (`samprasarana`)
    — or the ऊठ्, which 6.4.132 puts in the place of the व of वाह्, a यण् given an इक्,
    which is what 1.1.45 calls samprasāraṇa."""
    return word.has(F_SAMPRASARANA) or _is_uth(word)


def _uth_at(v: View, right: Sight) -> bool:
    """The ū at `right` is the ऊठ्. Asked through 6.1.85 as आङ् is (`_om_or_ang`): where
    the ऊठ् has fused with the आ that follows it — the Bālamanoramā's *विश्व ऊ आह् अस्*,
    then *विश्व ऊह् अस्* — the substitute is the ऊठ् (पूर्वस्यान्तवत्, and ऊठ् is one
    sound), so the piece that carries the flag is any word the substitute stands in."""
    return right.s == "ū" and any(
        _is_uth(v.state.words[index]) and _begins(v, right, index)
        for index in sorted(_idx(right.seg)))


def _first_two_cases() -> Tuple[str, ...]:
    """The endings of the first two cases, from 4.1.2's own order — three in each
    of seven cases, so the first six are प्रथमा and द्वितीया."""
    return SUP[:6]


def _dirgha(left: str, right: str) -> Optional[str]:
    """The long vowel 6.1.101 puts for a pair, by `anga.akah_savarne_dirghah`.

    Where the vowel has no long form of its own in the alphabet (ḷ) the Kāśikā
    says what stands: दीर्घपक्षे तु समुदायान्तरतमस्य ऌवर्णस्य दीर्घस्याभावात्
    ॠकारः क्रियते — the long ṝ. It is taken from the savarṇas of the vowel that
    the codified rule can lengthen, not typed.
    """
    got = akah_savarne_dirghah(left, right).result
    if got is None or kala(got) > kala(left):
        return got
    for other in savarnas_of(left):
        if kala(other) > kala(left) and akah_savarne_dirghah(other, other).result == other:
            return other
    return got


def _step(left: Sight, right: Sight, new: Sequence, *, nimitta: str, because: str,
          via: Sequence[Via], adesa: str = "", first: Optional[Sight] = None,
          covered: Sequence[Sight] = (), optional: str = "", authority: str = SUTRA,
          varttika: str = "", sthanin: str = "") -> Application:
    """One single substitute (6.1.84) for everything from `first` (or `left`) to
    `right`, and the explanation of it. `covered` are further sounds the rule
    read without changing."""
    start = first if first is not None else left
    return Application(
        site=site(start, left, right, *covered),
        edits=(ekadesa(start, right, *new),),
        optional=optional,
        detail=Detail(
            kind=EKADESA,
            sthanin=sthanin or f"{sk(left.s)}+{sk(right.s)}",
            adesa=adesa or "".join(n if isinstance(n, str) else n.s for n in new),
            nimitta=nimitta, because=because, via=tuple(via),
            authority=authority, varttika=varttika))


def _base(extra: Sequence[Via] = ()) -> List[Via]:
    return [S.ekadesa_one_for_two(), S.antadivat(), *extra]


def _upasarga_via(v: View, j: Junction) -> Tuple[Via, Via]:
    how = ("the boundary is written for a preverb and its dhātu"
           if j.kind == UPASARGA else
           "the caller flags the left word upasarga and the right dhatu")
    return (Via("1.4.59", f"{sk(v.word(j.left).text)} is an {{upasarga}} — {how}; the "
                          f"letters cannot say it, and a word like खट्वा is not one"),
            Via("1.3.1", f"{sk(v.word(j.right).text)} is a {{dhātu}} — read from the "
                         f"caller, since only its dhātu makes the preverb a preverb"))


def _sup_via(name: str) -> Via:
    return Via("4.1.2", f"the piece is the case ending {sk(name)}, one of the twenty-one; "
                        f"its letters are the same as another ending's, so the caller "
                        f"says which")


def _raparatva_via(sthanin: str, sounds: Sequence[str]) -> Via:
    return Via("1.1.51", f"the aṇ {sk(sounds[0])} that stands in place of {sk(sthanin)} is "
                         f"followed by {sk(sounds[-1])} — उरण् रपरः, with the vārttika that "
                         f"gives ḷ its ल्")


def _vrddhi(right: Sight) -> Tuple[Tuple[str, ...], List[Via]]:
    """The vṛddhi of the later sound and the sūtras it leans on — 1.1.1, 1.1.50,
    and 1.1.51 where the sound is ṛ or ḷ."""
    sounds = _sounds(vrddhi_of(right.s))
    via = [Via("1.1.1", "वृद्धि is आ, ऐ, औ — the vṛddhi vowels"),
           S.antaratama(right.s, sounds[0], "{vṛddhi} (ā, ai, au)")]
    if len(sounds) > 1:
        via.append(_raparatva_via(right.s, sounds))
    return sounds, via


def _para(left: Sight, right: Sight) -> Tuple[NewSeg]:
    """पररूपम् — the later sound stands for both."""
    return (NewSeg(right.s, right.seg.marks),)


def _purva(left: Sight) -> Tuple[NewSeg]:
    """पूर्वरूपम् — the earlier sound stands for both."""
    return (NewSeg(left.s, left.seg.marks),)


# ---------------------------------------------------------------------------
# 6.1.87 आद्गुणः — the general rule
# ---------------------------------------------------------------------------


@rule("6.1.87", name=_name("6.1.87"), families=FAMILIES)
def ad_gunah(v: View):
    """अवर्णादचि परे पूर्वपरयोरेको गुण आदेशः — उपेन्द्रः, रमेशः, गङ्गोदकम्, तवल्कारः."""
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if left.s not in AVARNA:
            continue
        sub = guna_of(right.s)
        if sub is None:
            continue
        sounds = _sounds(sub)
        via = _base([S.saptami_purva(f"{{aC}} {sk(right.s)}"),
                     Via("1.1.2", "अदेङ् गुणः — the guṇa vowels are अ, ए, ओ"),
                     S.antaratama(right.s, sounds[0], "{guṇa} (a, e, o)")])
        if len(sounds) > 1:
            via.append(_raparatva_via(right.s, sounds))
        yield _step(
            left, right, sounds, via=via,
            nimitta=f"the vowel {sk(right.s)} follows an {{avarṇa}}",
            because=(f"{sk(left.s)} is an {{avarṇa}} and {sk(right.s)} an {{aC}}, "
                     f"so both are replaced by the single guṇa {sk(sub)}"))


# ---------------------------------------------------------------------------
# 6.1.88 वृद्धिरेचि — the exception to guṇa
# ---------------------------------------------------------------------------


@rule("6.1.88", name=_name("6.1.88"), families=FAMILIES,
      overrides=(("6.1.87", _quote("kashika", "6.1.88", "आद्गुणस्यापवादः")),))
def vrddhir_eci(v: View):
    """आदेचि परे वृद्धिरेकादेशः — कृष्णैकत्वम्, गङ्गौघः, देवैश्वर्यम्, ब्रह्मौदनः."""
    eC = S.members("eC")
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if left.s not in AVARNA or right.s not in eC:
            continue
        sounds, via = _vrddhi(right)
        yield _step(
            left, right, sounds,
            via=_base([S.pratyahara("eC", "e, o, ai, au"), *via]),
            nimitta=f"the {{eC}} {sk(right.s)} follows an {{avarṇa}}",
            because=(f"{sk(left.s)} is an {{avarṇa}} and {sk(right.s)} an {{eC}}, so both "
                     f"are replaced by the single vṛddhi {sk(''.join(sounds))}"))


# ---------------------------------------------------------------------------
# 6.1.89 एत्येधत्यूठ्सु — vṛddhi before three named things, and its vārttikas
# ---------------------------------------------------------------------------


def _eti_edhati_uth(v: View, right: Sight) -> str:
    """Which of the three 6.1.89 names begins here, or "".

    *एजादि* qualifies एति and एधति and not ऊठ् — तदेतदेज्ग्रहणम् एतेरेव
    विशेषणम्, न पुनरेधतेः, अव्यभिचारादूठश्चासंभवात् (Kāśikā) — so a form of √इ
    counts only if it begins with an एच् (एति, एषि, एमि; not the इ of इतः, which is
    the very point of *एजादियोः किम्? उपेतः*), the root एध् always does, and ऊठ् is
    the ū of a word flagged `uth`, or the ū that has fused with the आ after it
    (`_uth_at`). Which dhātu it is cannot be read from the letters: the caller's
    `dhatu:ROOT`.
    """
    if _uth_at(v, right):
        return "ūṭh"
    if not v.begins_word(right):
        return ""
    root = v.word(right).flag_value(F_DHATU)
    if right.s in S.members("eC"):
        if root in ("i", "iṇ"):
            return "eti"
        if root in ("edh", "edha"):
            return "edhati"
    return ""


@rule("6.1.89", name=_name("6.1.89"), families=FAMILIES,
      overrides=(("6.1.94", _quote("kashika", "6.1.89", "एत्येधत्योस्त्वेङिपररूपापवादः")),
                 ("6.1.87", _quote("kashika", "6.1.89",
                                   "ऊठ्याद्गुणापवादो वृद्धिर्विधीयते"))))
def etyedhatyuthsu(v: View):
    """अवर्णादेजाद्योरेत्येधत्योरूठि च परे वृद्धिरेकादेशः — उपैति, उपैधते, प्रष्ठौहः.

    It displaces 6.1.94 (for एति, एधति) and 6.1.87 (for ऊठ्), and **not**
    6.1.95, though that is a pararūpa too: *ओमाङोश्च इत्येतत् तु पररूपं न
    बाध्यते — पुरस्तादपवादा अनन्तरान् विधीन् बाधन्ते नोत्तरान्* (Kāśikā). So
    *उप आ इत* is उपेतः, and the Kaumudī's *अवैहि* is not a form: *तेनावैहीति
    वृद्धिरसाधुरेव*. Nothing here overrides 6.1.95, which stands later, so 1.4.2
    gives it the place. (Where no 6.1.94 is in the way — *iha eti* — 6.1.88 gives
    the very same vṛddhi and 1.4.2 credits the later, 6.1.89.)

    OPEN (see `OPEN`): the Bālamanoramā holds that 6.1.89 is no exception to 6.1.95
    at all and that 6.1.95 wins by paratva; the result, and here the course, is the
    same.
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if left.s not in AVARNA:
            continue
        which = _eti_edhati_uth(v, right)
        if not which:
            continue
        sounds, via = _vrddhi(right)
        name = {"eti": "एति (a form of √इ)", "edhati": "एधति (a form of √एध्)",
                "ūṭh": "ऊठ्"}[which]
        yield _step(
            left, right, sounds, via=_base(via),
            nimitta=f"{name} follows an {{avarṇa}}",
            because=(f"{sk(left.s)} is an {{avarṇa}} and {sk(right.s)} begins {name}, one "
                     f"of the three 6.1.89 names, so both are replaced by the single "
                     f"vṛddhi {sk(''.join(sounds))} — where 6.1.94 or 6.1.87 would "
                     f"otherwise have taken the place"))


def _varttika_vrddhi(text: str, *, quoted: Tuple[str, str, str],
                     also: Sequence[Tuple[str, Tuple[str, str, str]]] = (),
                     chosen: Callable[[View, Junction], bool]):
    """A vārttika of 6.1.89: vṛddhi where the words it NAMES meet.

    The vārttikas list words, and the engine reads the words it is given, as
    the vārttika does — a lexical condition, so nothing here guesses at
    meaning. Each displaces 6.1.87 (*गुणे प्राप्तेऽनेन वार्तिकेन वृद्धिः*, the
    Bālamanoramā); those that also stand before an एङ्-initial word displace
    6.1.94 — `also`.
    """
    overrides = (("6.1.87", _quote(*quoted)),) + tuple(
        (target, _quote(*words)) for target, words in also)

    def find(v: View):
        for j in v.vowel_pairs():
            left, right = j.left, j.right
            if left.s not in AVARNA or not chosen(v, j):
                continue
            sounds, via = _vrddhi(right)
            said, lw = v.word(right).text, v.word(left).text
            yield _step(
                left, right, sounds, via=_base(via),
                authority=VARTTIKA, varttika=text,
                nimitta=f"{sk(said)} follows {sk(lw)}",
                because=(f"the vārttika names this pair — {sk(lw)} before {sk(said)} — and "
                         f"gives vṛddhi, so {sk(left.s)} and {sk(right.s)} are replaced by "
                         f"the single vṛddhi {sk(''.join(sounds))}, where the general "
                         f"rules would give something else"))

    find.__doc__ = f"{text} — {quoted[2]}"
    return rule("6.1.89", name=text, families=FAMILIES, authority=VARTTIKA,
                varttika=text, overrides=overrides)(find)


#: The second members the vārttika प्रादूहोढोढ्येषैष्येषु names, and the first
#: it names them after. एष and एष्य only as nominal kṛdantas: *एषशब्दसाहचर्यादेष्यशब्दोऽपि
#: कृदन्त एव गृह्यते, तेन तिङन्ते ल्यबन्ते च न वृद्धिः* (Bālamanoramā).
_PRA_RIGHT = ("ūha", "ūḍha", "ūḍhi")
_PRA_RIGHT_KRT = ("eṣa", "eṣya")
_PRAVATSATARA_LEFT = ("pra", "vatsatara", "kambala", "vasana", "ṛṇa", "daśa")

aksad_uhinyam = _varttika_vrddhi(
    V_AKSAT_UHINYAM,
    quoted=("balamanorama", "6.1.89", "अक्ष — ऊहिनीति स्थिते गुण प्राप्तेऽनेन वार्तिकेन वृद्धिः"),
    chosen=lambda v, j: (_ends_named(v, j.left, "akṣa") and _named(v, j.right, "ūhinī")))

svadirerinoh = _varttika_vrddhi(
    V_SVADIRERINOH,
    quoted=("balamanorama", "6.1.89", "स्व — ईर इति स्थिते गुणेप्राप्तेऽनेन वार्तिकेन वृद्धिः"),
    chosen=lambda v, j: (_ends_named(v, j.left, "sva") and _named(v, j.right, "īra", "īrin")))

praduhodhodhyesaisyesu = _varttika_vrddhi(
    V_PRADUHODHODHYESAISYESU,
    quoted=("balamanorama", "6.1.89", "प्र-ऊढिरिति स्थिते गुणं बाधित्वाऽनेन"),
    also=(("6.1.94", ("balamanorama", "6.1.89",
                      "प्र एष प्र एष्य इति स्थिते एङि पररूपं बाधित्वाऽनेन वृद्धिः")),),
    chosen=lambda v, j: (_ends_named(v, j.left, "pra") and (
        _named(v, j.right, *_PRA_RIGHT)
        or (_named(v, j.right, *_PRA_RIGHT_KRT) and v.word(j.right).has(F_KRDANTA)))))

rte_ca_trtiyasamase = _varttika_vrddhi(
    V_RTE_TRTIYASAMASE,
    quoted=("balamanorama", "6.1.89", "सुख-ऋत इति स्थिते गुणे प्राप्तेऽनेन वृद्धिराकारः"),
    chosen=lambda v, j: (j.kind == SAMASA and v.word(j.left).has(F_TRTIYA)
                         and v.ends_word(j.left) and _named(v, j.right, "ṛta")))

pravatsatara_rne = _varttika_vrddhi(
    V_PRAVATSATARA,
    quoted=("balamanorama", "6.1.89",
            "प्र-ऋणिमिति स्थिते गुणं बाधित्वाऽनेन वार्तिकेन वृद्धिराकारः"),
    chosen=lambda v, j: (_ends_named(v, j.left, *_PRAVATSATARA_LEFT)
                         and _named(v, j.right, "ṛṇa")))


# ---------------------------------------------------------------------------
# 6.1.90 आटश्च — after the augment आट्
# ---------------------------------------------------------------------------


@rule("6.1.90", name=_name("6.1.90"), families=FAMILIES,
      overrides=(("6.1.95", _quote("kashika", "6.1.90", "इति पररूपबाधनार्थः")),
                 ("6.1.96", _quote("kashika", "6.1.90", "इति पररूपबाधनार्थः"))))
def atas_ca(v: View):
    """आटोऽचि परे वृद्धिरेकादेशः — ऐक्षत, औभीत्, आर्ध्नोत्, औस्रीयत्, बहुश्रेयस्यै.

    The ca is there *to displace* 6.1.95 and 6.1.96: *चकारोऽधिकविधानार्थः …
    इति पररूपबाधनार्थः* (Kāśikā) — both stand later, and without it 1.4.2 would
    give them the place. The augment is the caller's word: `aat` on the piece.
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if left.s not in AVARNA or not v.ends_word(left) or not v.word(left).has(F_AAT):
            continue
        sounds, via = _vrddhi(right)
        yield _step(
            left, right, sounds, via=_base(via),
            nimitta=f"the vowel {sk(right.s)} follows the augment {{āṭ}}",
            because=(f"{sk(left.s)} is the augment {{āṭ}} and {sk(right.s)} an {{aC}}, so "
                     f"both are replaced by the single vṛddhi {sk(''.join(sounds))}"))


# ---------------------------------------------------------------------------
# 6.1.91, 6.1.92 — a preverb and a ṛ-dhātu
# ---------------------------------------------------------------------------


def _upasarga_rt(v: View, j: Junction) -> bool:
    return j.left.s in AVARNA and _rt(j.right.s) and _upasarga_dhatu(v, j)


@rule("6.1.91", name=_name("6.1.91"), families=FAMILIES,
      overrides=(("6.1.87", _quote("kashika", "6.1.91", "आद्गुणापवादः")),))
def upasargad_rti_dhatau(v: View):
    """अवर्णान्तादुपसर्गादृकारादौ धातौ परे वृद्धिरेकादेशः — उपार्च्छति, प्रार्च्छति.

    *उपसर्गात् किम्?* खट्वर्च्छति, and प्रर्च्छको देशः where प्र goes with no verb;
    *ऋति किम्?* उपेतः; *धातौ किम्?* उपर्कारः. The तपरकरण: *उप ॠकारीयति
    उपर्कारीयति* — a long ṝ is not reached.

    **When a subanta stands inside the dhātu, 6.1.92 replaces this rule's
    nityatva**: वृद्धि there is optional, and the other course is guṇa. So it is not
    offered to such a dhātu, which is what lets the declined course of 6.1.92 fall
    to 6.1.87 and not back to here.
    """
    for j in v.vowel_pairs():
        if not _upasarga_rt(v, j) or v.word(j.right).has(F_SUBANTA):
            continue
        left, right = j.left, j.right
        sounds, via = _vrddhi(right)
        yield _step(
            left, right, sounds,
            via=_base([*_upasarga_via(v, j), S.tapara(right.s), *via]),
            nimitta=f"the ṛ-initial dhātu {sk(v.word(right).text)} follows the "
                    f"{{upasarga}} {sk(v.word(left).text)}",
            because=(f"{sk(v.word(left).text)} is an {{upasarga}} ending in an {{avarṇa}} "
                     f"and {sk(v.word(right).text)} is a dhātu beginning with the short "
                     f"{sk(right.s)}, so both sounds are replaced by the single vṛddhi "
                     f"{sk(''.join(sounds))} — where 6.1.87 would give guṇa"))


@rule("6.1.92", name=_name("6.1.92"), families=FAMILIES,
      overrides=(("6.1.91", _quote("kashika", "6.1.91", "वा सुप्यापिशलेः इति विकल्पः स्यात्")),
                 ("6.1.87", _quote("kashika", "6.1.92", "उपर्षभीयति, उपार्षभीयति"))))
def va_supy_apisaleh(v: View):
    """अवर्णान्तादुपसर्गादृकारादौ सुब्धातौ परे वृद्धिरेकादेशः वा — प्रार्षभीयति, प्रर्षभीयति; प्राल्कारीयति, प्रल्कारीयति.

    A प्राप्तविभाषा: 6.1.91's vṛddhi was already due, and the option displaces it
    in the one course. *आपिशलिग्रहणं पूजार्थम्, वेति ह्युच्यत एव* — the teacher's
    name is honour and adds no condition. ṛ and ḷ alike (*ऋकारऌकारयोः सावर्ण्यविधिः*),
    the short ones only (*तपरत्वाद्दीर्घे न*: उपऋकारीयति is उपर्कारीयति).
    """
    for j in v.vowel_pairs():
        if not _upasarga_rt(v, j) or not v.word(j.right).has(F_SUBANTA):
            continue
        left, right = j.left, j.right
        sounds, via = _vrddhi(right)
        yield _step(
            left, right, sounds, optional="वा",
            via=_base([*_upasarga_via(v, j), S.tapara(right.s), *via]),
            nimitta=f"the ṛ-initial dhātu {sk(v.word(right).text)}, with a subanta inside "
                    f"it, follows the {{upasarga}} {sk(v.word(left).text)}",
            because=(f"{sk(v.word(right).text)} is a dhātu with a {{subanta}} inside it, so "
                     f"the vṛddhi 6.1.91 would have made is here optional (a "
                     f"prāptavibhāṣā): one course takes it, {sk(left.s)} and "
                     f"{sk(right.s)} becoming the single vṛddhi {sk(''.join(sounds))}; "
                     f"the other declines it and 6.1.87's guṇa stands"))


# ---------------------------------------------------------------------------
# 6.1.93 औतोऽम्शसोः
# ---------------------------------------------------------------------------

#: The two endings 6.1.93 names — *अमिति द्वितीयैकवचनं गृह्यते, शसा साहचर्यात्*.
_AM_SAS = ("am", "śas")


@rule("6.1.93", name=_name("6.1.93"), families=FAMILIES)
def auto_mrasasoh(v: View):
    """ओकारादम्शसोरचि परे आकार एकादेशः — गाम्, गाः (Kaumudī); गां पश्य, द्यां पश्य (Kāśikā).

    *आ ओत इति छेदः* (Kaumudī, Bālamanoramā): the substitute is आ, which the sūtra
    names, and ओत is तपर — the sound o. The अम् is the case ending, not a tense
    ending: *तेनाचिनवमसुनवमित्यत्र न भवति*. Which ending a piece is cannot be
    read from its letters — the caller's `sup:am` or `sup:śas`. Nothing here
    displaces 6.1.78 by name; 6.1.93 stands later and 1.4.2 gives it the place.
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if left.s != "o" or right.s != "a":
            continue
        name = _sup(v, right)
        if name not in _AM_SAS:
            continue
        yield _step(
            left, right, ("ā",), via=_base([_sup_via(name), S.tapara("o")]),
            nimitta=f"the ending {sk(name)} follows the sound {{o}}",
            because=(f"{sk(left.s)} ends the stem and {sk(right.s)} begins the case ending "
                     f"{sk(name)}, so both are replaced by the single {sk('ā')} that the "
                     f"sūtra names"))


# ---------------------------------------------------------------------------
# 6.1.94 एङि पररूपम् — the later sound, for a preverb and an eṅ-dhātu
# ---------------------------------------------------------------------------


@rule("6.1.94", name=_name("6.1.94"), families=FAMILIES,
      overrides=(("6.1.88", _quote("kashika", "6.1.94", "वृद्धिरेचि इत्यस्यापवादः")),))
def engi_pararupam(v: View):
    """आदुपसर्गादेङादौ धातौ परे पररूपमेकादेशः — प्रेजते, उपोषति.

    For a dhātu with a subanta inside (एडकीयति), the Kaumudī and the Bālamanoramā
    read *वा सुपि* into this sūtra by वाक्यभेद: *एङादौ सुब्धातौ पररूपं पाक्षिकं भवति,
    तदितरधातौ तु नित्यम्* — उपेडकीयति, उपैडकीयति. The declined course is 6.1.88.

    OPEN (see `OPEN`): the Kāśikā gives the option only as the view of some
    (*केचिद्*); the module takes it as the Kaumudī and the Bālamanoramā do.
    """
    eng = S.members("eṄ")
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if left.s not in AVARNA or right.s not in eng or not _upasarga_dhatu(v, j):
            continue
        subanta = v.word(right).has(F_SUBANTA)
        yield _step(
            left, right, _para(left, right), optional="वा" if subanta else "",
            adesa=f"{right.s} (pararūpa)",
            via=_base([*_upasarga_via(v, j), S.pratyahara("eṄ", "e, o")]),
            nimitta=f"the eṅ-initial dhātu {sk(v.word(right).text)} follows the "
                    f"{{upasarga}} {sk(v.word(left).text)}",
            because=(f"{sk(v.word(left).text)} is an {{upasarga}} ending in an {{avarṇa}} and "
                     f"{sk(v.word(right).text)} a dhātu beginning with the {{eṅ}} "
                     f"{sk(right.s)}, so the later sound {sk(right.s)} stands for both"
                     + (" — in one course only, the dhātu having a subanta inside it "
                        "(the other course is 6.1.88's vṛddhi)" if subanta else "")))


@rule("6.1.94", name=V_EVE_CANIYOGE, families=FAMILIES, authority=VARTTIKA,
      varttika=V_EVE_CANIYOGE,
      overrides=(("6.1.88", _quote("balamanorama", "6.1.94",
                                   "बाधित्वाऽनेन वार्तिकेन पररूपमेकारः")),))
def eve_caniyoge(v: View):
    """एवे चानियोगे पररूपं वक्तव्यम् — इहेव, अद्येव, क्वेव; *इहैव भव* is the niyoga.

    *नियोगोऽवधारणम्* — restriction; where the एव restricts (इहैव भव) it is
    6.1.88's, where it does not (इह एव, क्व एव) it is this. Which it is is meaning,
    so the caller says: `aniyoga` on the particle.
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if (left.s not in AVARNA or right.s != "e" or not _named(v, right, "eva")
                or not v.word(right).has(F_ANIYOGA)):
            continue
        yield _step(
            left, right, _para(left, right), authority=VARTTIKA, varttika=V_EVE_CANIYOGE,
            adesa=f"{right.s} (pararūpa)", via=_base(),
            nimitta="the particle एव, not restrictive, follows an {avarṇa}",
            because=(f"{sk(left.s)} is an {{avarṇa}} and {sk('eva')} does not restrict "
                     f"(aniyoga), so the later sound {sk(right.s)} stands for both — "
                     f"where 6.1.88 would give vṛddhi"))


@rule("6.1.94", name=V_OTVOSTHAYOH, families=FAMILIES, authority=VARTTIKA,
      varttika=V_OTVOSTHAYOH,
      overrides=(("6.1.88", _quote("balamanorama", "6.1.94", "बाधित्वा पाक्षिकं पररूपम्")),))
def otvosthayoh_samase_va(v: View):
    """ओत्वोष्ठयोः समासे वा पररूपं वक्तव्यम् — स्थूलोतुः, स्थूलौतुः; बिम्बोष्ठी, बिम्बौष्ठी.

    A प्राप्तविभाषा — the vṛddhi was due and the pararūpa displaces it in one
    course. *समास इति किम्? तिष्ठ देवदत्तौष्ठं पश्य*: only inside a compound,
    which is the boundary the caller writes ``-``.
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if (left.s not in AVARNA or j.kind != SAMASA or right.s not in S.members("eṄ")
                or not _named(v, right, "otu", "oṣṭha")):
            continue
        yield _step(
            left, right, _para(left, right), optional="वा", authority=VARTTIKA,
            varttika=V_OTVOSTHAYOH, adesa=f"{right.s} (pararūpa)", via=_base(),
            nimitta=f"{sk(v.word(right).text)} follows the first member of a compound",
            because=(f"{sk(left.s)} ends the first member of a compound and "
                     f"{sk(v.word(right).text)} the second, so the later sound "
                     f"{sk(right.s)} may stand for both — one course lets it, the "
                     f"other declines and 6.1.88's vṛddhi stands"))


@rule("6.1.94", name=V_EMANNADISU, families=FAMILIES, authority=VARTTIKA,
      varttika=V_EMANNADISU, vedic=True,
      overrides=(("6.1.88", _quote("kashika", "6.1.94", "वृद्धिरेचि इत्यस्यापवादः")),))
def emannadisu_chandasi(v: View):
    """एमन्नादिषु छन्दसि पररूपं वक्तव्यम् — अपां त्वा एमन्, अपां त्वेमन् (Vedic only)."""
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if (left.s not in AVARNA or right.s not in S.members("eṄ")
                or not _named(v, right, "eman", "odman")):
            continue
        yield _step(
            left, right, _para(left, right), authority=VARTTIKA, varttika=V_EMANNADISU,
            adesa=f"{right.s} (pararūpa)", via=_base(),
            nimitta=f"{sk(v.word(right).text)} in the Veda follows an {{avarṇa}}",
            because=(f"in the Veda, before {sk(v.word(right).text)}, the later sound "
                     f"{sk(right.s)} stands for {sk(left.s)} and {sk(right.s)} both"))


# ---------------------------------------------------------------------------
# 6.1.95 ओमाङोश्च — the later sound, before om and āṅ
# ---------------------------------------------------------------------------

_OM = ("om", "oṃ")


def _om_or_ang(v: View, right: Sight) -> Optional[str]:
    """Which of ओम् and आङ् the sound `right` is, or None.

    ओम् is the particle whose letters are `om` (the flag `nipata` says it is the
    particle). आङ् is a word flagged `ang` — the preverb itself, or a word that
    begins with the substitute in which the preverb fused with its dhātu (ehi,
    oḍhā). 6.1.85 makes that substitute the end of आङ् (पूर्वस्यान्तवत्), आङ् is a
    single sound, so it is आङ् — asked through `Seg.lw`, the word the substitute
    also stands in.
    """
    word = v.word(right)
    if v.begins_word(right) and word.has(F_NIPATA) and _bare(word) in _OM:
        return "om"
    for index in sorted(_idx(right.seg)):
        if v.state.words[index].has(F_ANG) and _begins(v, right, index):
            return "āṅ"
    return None


@rule("6.1.95", name=_name("6.1.95"), families=FAMILIES,
      overrides=(("6.1.88", _quote("kashika", "6.1.95", "वृद्धिरेचि इत्यस्यापवादः")),
                 ("6.1.101", _quote("kashika", "6.1.95", "अकः सवर्णे दीर्घत्वं बाधते"))))
def omango_ca(v: View):
    """ओमि आङि चात्परे पररूपमेकादेशः — शिवायों नमः, शिवेहि (Kaumudī); का ओमित्यवोचत् कोमित्यवोचत्, अद्योढा (Kāśikā).

    आङ् is asked through 6.1.85: in *शिव एहि* the e is the guṇa that आङ् and इहि
    made — *आःइहीति स्थिते गुणे एहीति रूपम्, ततः शिव-एहि इति स्थिते वृद्धिं बाधित्वा
    पररूपमेकारः* (Bālamanoramā) — and it counts as आङ्, the end of the preverb.
    **6.1.95 is not displaced by 6.1.89** (the maxim of 6.1.89), so *अव एहि* is अवेहि.
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if left.s not in AVARNA:
            continue
        which = _om_or_ang(v, right)
        if which is None:
            continue
        via = _base([S.tapara("o")] if which == "om" else [
            Via("1.4.59", "आङ् is a preverb, and the letters cannot say which ā or "
                          "which fused e is the preverb — the caller's `ang`")])
        yield _step(
            left, right, _para(left, right), adesa=f"{right.s} (pararūpa)", via=via,
            nimitta=f"{sk('om' if which == 'om' else 'āṅ')} follows an {{avarṇa}}",
            because=(f"{sk(left.s)} is an {{avarṇa}} and {sk(right.s)} is "
                     + ("the particle {om}" if which == "om" else
                        "{āṅ} — the preverb, or the substitute in which it has fused with "
                        "its dhātu, which 6.1.85 makes the end of {āṅ}")
                     + f", so the later sound {sk(right.s)} stands for both — where 6.1.88 "
                       f"or 6.1.101 would have taken the place"))


# ---------------------------------------------------------------------------
# 6.1.96 उस्यपदान्तात्
# ---------------------------------------------------------------------------


@rule("6.1.96", name=_name("6.1.96"), families=FAMILIES,
      overrides=(("6.1.87", _quote("kashika", "6.1.96",
                                   "पूर्वपरयोराद्गुणापवादः पररूपमेकादेशो भवति")),))
def usy_apadantat(v: View):
    """अपदान्तादवर्णादुसि परे पररूपमेकादेशः — भिन्द्युः, छिन्द्युः, अदुः, अयुः, अपुः.

    *उसि* is read as the Kāśikā reads it, as the letters `us` beginning what
    follows (its examples of the counter-case, का उस्रा, have the u and s of
    उस्रा): the u, with an s next in the same word. *अपदान्तात् किम्? का उस्रा
    कोस्रा* — a pada-final अ is not the case, which is the boundary the caller
    writes. *आदित्येव — चक्रुः*: the earlier sound must be an अवर्ण.

    SCOPE (see `OPEN`): the optative's *यास्* + *उस्* is where 7.2.80 अतो येयः
    contends with this rule (भवेयुः, the Kaumudī's ārṣa sandhi); 7.2.80 is not in the
    engine, so the caller gives the piece as it stands.
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if left.s not in AVARNA or v.pada_final(left):
            continue
        if right.s != "u" or not v.begins_word(right):
            continue
        after = v.next(right)
        if after is None or after.s != "s" or after.w != right.w:
            continue
        yield _step(
            left, right, _para(left, right), covered=(after,),
            adesa=f"{right.s} (pararūpa)", via=_base(),
            nimitta=f"{{us}} follows an {{avarṇa}} that does not end a pada",
            because=(f"{sk(left.s)} is an {{avarṇa}} inside a pada and {sk(right.s)} begins "
                     f"{{us}}, so the later sound {sk(right.s)} stands for both — where "
                     f"6.1.87 would give guṇa"))


# ---------------------------------------------------------------------------
# 6.1.97 अतो गुणे
# ---------------------------------------------------------------------------


@rule("6.1.97", name=_name("6.1.97"), families=FAMILIES,
      overrides=(("6.1.101", _quote("kashika", "6.1.97", "अकः सवर्णे दीर्घस्य अपवादः")),
                 ("6.1.88", _quote("kashika", "6.1.97",
                                   "पचे,यज इत्यत्र वृद्धिरेचि इति वृद्धिः प्राप्नोति"))))
def ato_gune_rule(v: View):
    """अपदान्तादकाराद्गुणे परतः पररूपमेकादेशः — पचन्ति, यजन्ति, पचे, यजे.

    The pair is asked of `anga.ato_gune` (1.1.2 says what a guṇa is); the
    condition the module adds is अपदान्तात् — ANGA, not a pada boundary:
    *अपदान्तादित्येव — दण्डाग्रम्, यूपाग्रम्* keep their long ā by 6.1.101. It
    displaces 6.1.101 and **not** 6.1.102 — *पुरस्तादपवादा अनन्तरान् विधीन्
    बाधन्ते नोत्तरान्* (Kaumudī: रामाः) — which is nothing declared here:
    6.1.102 stands later and 1.4.2 gives it the place.

    OPEN (see `OPEN`): the Bālamanoramā says the pararūpa is no exception to 6.1.102
    at all, so the maxim is not needed; the answer is the same.
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if v.pada_final(left) or ato_gune(left.s, right.s).result is None:
            continue
        yield _step(
            left, right, _para(left, right), adesa=f"{right.s} (pararūpa)",
            via=_base([S.tapara("a"), Via("1.1.2", "अदेङ् गुणः — {} is a guṇa vowel".format(
                sk(right.s)))]),
            nimitta=f"the guṇa {sk(right.s)} follows a short {{a}} that does not end a pada",
            because=(f"{sk(left.s)} is a short अ inside a pada and {sk(right.s)} a guṇa "
                     f"vowel, so the later sound {sk(right.s)} stands for both — where "
                     f"6.1.101 would give the long {sk('ā')}"))


# ---------------------------------------------------------------------------
# 6.1.98–6.1.100 — the imitation of an indistinct sound
# ---------------------------------------------------------------------------


def _at_before_iti(v: View, j: Junction) -> Optional[Sight]:
    """The अ of the `at` that ends an अव्यक्तानुकरण word standing before *iti*, or None.

    *तस्य योऽच्छब्दस्तस्मादितौ* (Kāśikā): the word is the imitation (the caller's
    `avyakta`), it ends in the syllable `at` — *अत इति किम्? मरट् इति मरडिति* — and
    the next word is इति, whose first sound is the later one.
    """
    t, i = j.left, j.right
    if t.s != "t" or i.s != "i" or not v.ends_word(t) or not _named(v, i, "iti"):
        return None
    if not v.word(t).has(F_AVYAKTA):
        return None
    a = v.prev(t)
    if a is None or a.s != "a" or a.w != t.w:
        return None
    # A place a later rule (jaśtva, 8.2.39) has already worked on is one this
    # rule sees only through its past — it has had its chance there, and so has
    # the refusal below, which is not to be repeated after the t has become d.
    if a.through or t.through or i.through:
        return None
    return a


def _vowels_in(word: Word) -> int:
    return sum(1 for sound in _sounds(word.text) if S.is_member(sound, "aC"))


@rule("6.1.98", name=_name("6.1.98"), families=FAMILIES)
def avyaktanukaranasyata_itau(v: View):
    """ध्वनेरनुकरणस्य योऽच्छब्दस्तस्मादितौ पररूपमेकादेशः — पटिति, घटिति, झटिति, छमिति.

    The sthānin is the whole `at` with the इ that follows — the anukaraṇa is
    meaningless, so 1.1.52 अलोऽन्त्यस्य does not cut it down to the t: *नानर्थकेऽलोऽन्त्यविधिः*
    (Bālamanoramā) — and the later इ stands for the three sounds.

    Not offered to the repeated member (`amredita`): **6.1.99 refuses it there** —
    the Kāśikā, तस्य पररूपं न भवति. That refusal is modelled by not offering, and
    not by a step, because what 6.1.99 puts in its place is optional, and the
    declined course of an option would otherwise bring this rule back.
    """
    for j in v.junctions():
        a = _at_before_iti(v, j)
        if a is None or v.word(j.left).has(F_AMREDITA):
            continue
        t, i = j.left, j.right
        yield _step(
            t, i, _para(t, i), first=a, adesa=f"{i.s} (pararūpa)",
            sthanin=f"{sk('at')}+{sk(i.s)}", via=_base(),
            nimitta=f"{{iti}} follows the imitation {sk(v.word(t).text)}",
            because=(f"{sk(v.word(t).text)} imitates an indistinct sound and ends in "
                     f"{sk('at')}, and {{iti}} follows, so the later {sk(i.s)} stands for "
                     f"the whole {sk('at')} and the {sk(i.s)} together"))


@rule("6.1.98", name=V_EKACO_NA, families=FAMILIES, authority=VARTTIKA,
      varttika=V_EKACO_NA,
      overrides=(("6.1.98", _quote("kashika", "6.1.98", "अनेकाच इति वक्तव्यम्")),))
def ekaco_na(v: View):
    """एकाचो न — the imitation must have more than one vowel: श्रत् इति श्रदिति.

    A refusal, and the engine's own kind: nothing is revived at this place, the
    ordinary consonant rules act on the t next (*श्रदिति*).
    """
    for j in v.junctions():
        a = _at_before_iti(v, j)
        if a is None or v.word(j.left).has(F_AMREDITA) or _vowels_in(v.word(j.left)) != 1:
            continue
        t, i = j.left, j.right
        yield Application(
            site=site(a, t, i), edits=(),
            detail=Detail(
                kind=PRATISEDHA, sthanin=f"{sk('at')}+{sk(i.s)}", adesa="",
                nimitta=f"the imitation {sk(v.word(t).text)} has one vowel",
                because=(f"{sk(v.word(t).text)} has a single vowel, so the pararūpa of "
                         f"6.1.98 is refused for it (a vārttika: it must be more than "
                         f"one)"),
                via=(), authority=VARTTIKA, varttika=V_EKACO_NA))


@rule("6.1.99", name=_name("6.1.99"), families=FAMILIES)
def namreditasyantyasya_tu_va(v: View):
    """आम्रेडितस्य प्रागुक्तं न स्यादन्त्यस्य तु तकारमात्रस्य वा — पटत्पटदिति, पटत्पटेति.

    For the repeated member the pararūpa of 6.1.98 is refused for the whole `at`
    — *तस्य पररूपं न भवति, तस्य योऽन्त्यस्तकारस्तस्य वा भवति* (Kāśikā) — and the
    t alone may take it: an अप्राप्तविभाषा, nothing having been due for the t
    by itself. The declined course leaves the t to the ordinary rules (पटदिति);
    the taken one leaves ...a + i, which 6.1.87 makes ए (पटेति).
    """
    for j in v.junctions():
        a = _at_before_iti(v, j)
        if a is None or not v.word(j.left).has(F_AMREDITA):
            continue
        t, i = j.left, j.right
        yield _step(
            t, i, _para(t, i), optional="वा", adesa=f"{i.s} (pararūpa)", via=_base(),
            nimitta=f"{{iti}} follows the repeated imitation {sk(v.word(t).text)}",
            because=(f"{sk(v.word(t).text)} is the repeated member and {{iti}} follows, so "
                     f"6.1.98's replacement of the whole {sk('at')} is refused; the "
                     f"last sound {sk('t')} alone may be replaced by the later "
                     f"{sk(i.s)} (an aprāptavibhāṣā) — one course takes it, the other "
                     f"leaves the {sk('t')} to the ordinary rules"))


@rule("6.1.100", name=_name("6.1.100"), families=("ekadesa", "hal"))
def nityam_amredite_daci(v: View):
    """डाच्परं यदाम्रेडितं तस्मिन् पूर्वस्याव्यक्तानुकरणस्याच्छब्दस्य योऽन्त्यस्तकारस्तस्य पूर्वस्य परस्य चाद्यस्य वर्णस्य नित्यं पररूपमेकादेशो भवति — पटपटा करोति, दमदमा करोति.

    The t that ends the imitation and the first sound of the repeated member
    that ḍāc follows are one place, and the later of the two stands for both.
    That first sound is a consonant here, which is why the pair is not a
    vowel junction. `avyakta` on the first word, `amredita` and `dac` on the
    second.

    SCOPE (see `OPEN`): the Bhāṣya has this as a vārttika with a rival reading; it is
    done as the Vidyut sūtrapāṭha and the Kāśikā give it, a sūtra.
    """
    for j in v.junctions():
        t, p = j.left, j.right
        if t.s != "t" or not v.ends_word(t) or not v.begins_word(p):
            continue
        a = v.prev(t)
        if a is None or a.s != "a" or a.w != t.w or not v.word(t).has(F_AVYAKTA):
            continue
        word = v.word(p)
        if not (word.has(F_AMREDITA) and word.has(F_DAC)):
            continue
        yield _step(
            t, p, _para(t, p), adesa=f"{p.s} (pararūpa)", via=_base(),
            nimitta=f"the repeated member {sk(word.text)}, ending in ḍāc, follows "
                    f"{sk(v.word(t).text)}",
            because=(f"{sk(v.word(t).text)} imitates an indistinct sound and ends in "
                     f"{sk('at')}; the repeated member {sk(word.text)} is followed by "
                     f"ḍāc; so the later sound {sk(p.s)} always stands for the last "
                     f"{sk(t.s)} and itself"))


# ---------------------------------------------------------------------------
# 6.1.101 अकः सवर्णे दीर्घः — and the two vārttikas that give ṛ and ḷ a sound of their own
# ---------------------------------------------------------------------------


@rule("6.1.101", name=_name("6.1.101"), families=FAMILIES)
def akah_savarne_dirghah_rule(v: View):
    """अकः सवर्णेऽचि परे दीर्घ एकादेशः — दैत्यारिः, श्रीशः, विष्णूदयः, दण्डाग्रम्, दधीन्द्रः.

    *अक इति किम्? अग्नये* — the earlier sound is not an अक्; *सवर्ण इति किम्? दध्यत्र*
    — the two are not alike; *अचीत्येव — कुमारी शेते*. Whether they are alike is
    `varna.savarna` (1.1.9), asked through `anga.akah_savarne_dirghah`. ḷ has no
    long form of its own: its दीर्घपक्ष is ॠकार (Kāśikā), see `_dirgha`.
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        # अकः and सवर्णे are both asked of `anga.akah_savarne_dirghah`, which refuses a
        # left sound that is no अक् — not decided a second time here.
        sub = _dirgha(left.s, right.s)
        if sub is None:
            continue
        yield _step(
            left, right, (sub,),
            via=_base([S.savarna_of(left.s, right.s),
                       S.pratyahara("aK", "a, i, u, ṛ, ḷ")]),
            nimitta=f"the savarṇa vowel {sk(right.s)} follows an {{ak}}",
            because=(f"{sk(left.s)} is an {{ak}} and {sk(right.s)} is savarṇa to it, so "
                     f"both are replaced by the single long vowel {sk(sub)}"))


def _dvimatra_varttika(text: str, sound: str, quoted: Tuple[str, str, str]):
    """ऋति सवर्णे ऋ वा / ऌति सवर्णे ऌ वा — an ak before a short `sound` that is savarṇa to it
    may be replaced by ONE sound of two mātrās, which the alphabet has no letter for.

    *उभयत्रापि विधेयं वर्णद्वयं द्विमात्रम्* (Kaumudī) — it is written with the letter of
    the vārttika and marked `dvimātra`. A प्राप्तविभाषा: 6.1.101's dīrgha is due, and
    the other course is that.
    """

    def find(v: View):
        for j in v.vowel_pairs():
            left, right = j.left, j.right
            if right.s != sound or not S.is_member(left.s, "aK") \
                    or not savarna(left.s, right.s):
                continue
            # The engine keys a declined option by (sūtra, site), and this
            # vārttika shares its sūtra with 6.1.101 itself: were the two sites
            # the same, declining the vārttika would shut 6.1.101 out of the
            # place too, and the other course could not be the long vowel. So
            # the site of the vārttika names the sound beside the pair (the one
            # after the ṛ, or before the earlier sound) — it looked past it.
            beside = v.next(right) or v.prev(left)
            yield _step(
                left, right, (NewSeg(sound, frozenset({DVIMATRA})),), optional="वा",
                covered=(beside,) if beside is not None else (),
                authority=VARTTIKA, varttika=text, adesa=f"{sound} (dvimātra)",
                via=_base([S.savarna_of(left.s, right.s)]),
                nimitta=f"the short {sk(sound)} follows a savarṇa {{ak}}",
                because=(f"{sk(left.s)} and {sk(right.s)} are savarṇa and the later is the "
                         f"short {sk(sound)}, so the two may be replaced by ONE {sk(sound)} "
                         f"of two mātrās — one course takes it, the other declines and "
                         f"6.1.101's long vowel stands"))

    find.__doc__ = f"{text} — {quoted[2]}"
    return rule("6.1.101", name=text, families=FAMILIES, authority=VARTTIKA,
                varttika=text, overrides=(("6.1.101", _quote(*quoted)),))(find)


rti_savarne_r_va = _dvimatra_varttika(
    V_RTI_SAVARNE, "ṛ",
    ("kashika", "6.1.101", "ऋति सवर्णे परभूते तत्र ऋ वा भवतीति"))
lti_savarne_l_va = _dvimatra_varttika(
    V_LTI_SAVARNE, "ḷ",
    ("kashika", "6.1.101", "ऌति सवर्णे परतो ऌ वा भवतीति"))


# ---------------------------------------------------------------------------
# 6.1.102–6.1.106 — the earlier sound's long form, and its refusals
# ---------------------------------------------------------------------------


def _first_case_ac(v: View, j: Junction) -> Optional[str]:
    """The ending, if this is a place 6.1.102 reaches: an अक् before the vowel that
    begins an ending of the first or second case, and not yet refused."""
    left = j.left
    if not S.is_member(left.s, "aK") or NO_PURVASAVARNA in left.marks:
        return None
    name = _sup(v, j.right)
    return name if name in _first_two_cases() else None


@rule("6.1.102", name=_name("6.1.102"), families=FAMILIES)
def prathamayoh_purvasavarnah(v: View):
    """अकः प्रथमाद्वितीययोरचि पूर्वसवर्णदीर्घ एकादेशः — अग्नी, वायू, वृक्षाः, वृक्षान्.

    The endings of the first two cases are the first six of 4.1.2's list. The
    substitute is the long vowel savarṇa to the EARLIER sound (*पूर्वग्रहणं किम्?
    अग्नी इत्यत्र पक्षे परसवर्णो मा भूत्*). It is **not** displaced by 6.1.97 —
    *अतो गुणे … न तु पूर्वसवर्णदीर्घत्वम्* (Kāśikā) — which is why *राम अस्* is रामाः.
    """
    for j in v.vowel_pairs():
        name = _first_case_ac(v, j)
        if name is None:
            continue
        left, right = j.left, j.right
        sub = _dirgha(left.s, left.s)
        if sub is None:
            continue
        yield _step(
            left, right, (sub,), adesa=f"{sub} (pūrvasavarṇadīrgha)",
            via=_base([_sup_via(name), S.savarna_of(left.s, sub)]),
            nimitta=f"the ending {sk(name)} follows an {{ak}}",
            because=(f"{sk(left.s)} is an {{ak}} and {sk(right.s)} begins the ending "
                     f"{sk(name)} of the first or second case, so both are replaced by "
                     f"the long vowel savarṇa to the earlier sound: {sk(sub)}"))


@rule("6.1.103", name=_name("6.1.103"), families=("hal",))
def tasmac_chaso_nah_pumsi(v: View):
    """तस्माच्छसो नः पुंसि — वृक्षान्, अग्नीन्, वायून्.

    The s of शस् after the long vowel 6.1.102 has just made, in the masculine.
    *तस्मादिति किम्? एतांश्चरतो गाः पश्य* — the ā of गाः is 6.1.93's and not
    6.1.102's, so it is not this. *पुंसि किम्? धेनूः, बह्वीः, कुमारीः*. The gender is
    the caller's (`pum` on the stem), the ending's name too (`sup:śas`).
    """
    for s in v.live:
        if s.s != "s":
            continue
        before = v.prev(s)
        if before is None or before.seg.made_by != "6.1.102" or before.w != s.w:
            continue
        if _ending_of(v.word(s)) != "śas" or before.seg.lw is None:
            continue
        if not v.state.words[before.seg.lw].has(F_PUM):
            continue
        yield Application(
            site=site(before, s), edits=(replace(s, "n"),),
            detail=Detail(
                kind=ADESA, sthanin=s.s, adesa="n",
                nimitta="the long vowel 6.1.102 made stands before it, in the masculine",
                because=("the s of {śas} follows the long vowel that 6.1.102 made, and the "
                         "stem is masculine, so it becomes the {n} the sūtra names"),
                via=(S.pancami_para("{pūrvasavarṇadīrgha}"),
                     _sup_via("śas"))))


def _refuse(left: Sight, right: Sight, name: str, why: str, via: Sequence[Via]
            ) -> Application:
    """A refusal of 6.1.102 that lets the rules it shadowed come back: a mark on
    the earlier vowel (see the module docstring), the sthānin unchanged."""
    return Application(
        site=site(left, right), edits=(remark(left, NO_PURVASAVARNA),),
        detail=Detail(
            kind=PRATISEDHA, sthanin=f"{sk(left.s)}+{sk(right.s)}", adesa="",
            nimitta=f"the ending {sk(name)} follows the {sk(left.s)}", because=why,
            via=tuple(via),
            note=("the rules listed as displaced at this step lost only the place "
                  "for this step: 6.1.102 is refused, and they apply next")))


@rule("6.1.104", name=_name("6.1.104"), families=FAMILIES,
      overrides=(("6.1.102", _quote("kashika", "6.1.104",
                                    "अवर्णादिचि पूर्वसवर्णदीर्घो न भवति")),))
def nadici(v: View):
    """अवर्णादिचि परे न पूर्वसवर्णदीर्घः — वृक्षौ, खट्वे, कुण्डे, शिवोऽर्च्यः.

    *आदिति किम्? अग्नी* — the earlier sound is an अवर्ण; *इचीति किम्? वृक्षाः*. With
    the exception refused, **the general rule comes back** (*बाधके निवृत्ते गुणः
    पुनरुन्मिषति*): वृक्षौ is 6.1.88's vṛddhi.
    """
    for j in v.vowel_pairs():
        name = _first_case_ac(v, j)
        left, right = j.left, j.right
        if name is None or left.s not in AVARNA or right.s not in S.members("iC"):
            continue
        yield _refuse(
            left, right, name,
            f"{sk(left.s)} is an {{avarṇa}} and {sk(right.s)} an {{iC}}, so the "
            f"pūrvasavarṇadīrgha of 6.1.102 is refused; the rules it shadowed apply",
            (S.pratyahara("iC", "i, u, ṛ, ḷ, e, o, ai, au"), _sup_via(name)))


@rule("6.1.105", name=_name("6.1.105"), families=FAMILIES,
      overrides=(("6.1.102", _quote("kashika", "6.1.105",
                                    "दीर्घात् जसि इचि च परतः पूर्वसवर्णदीर्घो न भवति")),))
def dirghaj_jasi_ca(v: View):
    """दीर्घाज्जसि इचि च परे पूर्वसवर्णदीर्घो न स्यात् — कुमार्यौ, कुमार्यः, विश्वपौ, विश्वपाः.

    Where 6.1.104 also reaches (an अवर्ण before an इच्), 6.1.105 is the one that
    is done — *विश्वपावित्यत्र नादिचि इत्यस्य दीर्घाज्जसि च इत्यस्य च प्राप्तौ परत्वेन
    दीर्घाज्जसि च इत्यस्यैवोपन्यासौचित्यात्* (Bālamanoramā). Nothing declared: it stands
    later, and 1.4.2 says so.
    """
    for j in v.vowel_pairs():
        name = _first_case_ac(v, j)
        left, right = j.left, j.right
        if name is None or kala(left.s) != kala("ā"):
            continue
        if not (name == "jas" or right.s in S.members("iC")):
            continue
        yield _refuse(
            left, right, name,
            f"{sk(left.s)} is long and {sk(right.s)} begins "
            + ("{jas}" if name == "jas" else "an ending that begins with an {iC}")
            + ", so the pūrvasavarṇadīrgha of 6.1.102 is refused; the rules it "
              "shadowed apply",
            (_sup_via(name),))


@rule("6.1.106", name=_name("6.1.106"), families=FAMILIES, vedic=True,
      overrides=(("6.1.105", _quote("kashika", "6.1.106",
                                    "दीर्घात् छन्दसि विषये जसि च इचि च परतो वा "
                                    "पूर्वसवर्णदीर्घो न भवति")),))
def va_chandasi(v: View):
    """दीर्घाज्जसि इचि च पूर्वसवर्णदीर्घो वा — वाराही, वाराह्यौ; मारुतीश्चतस्रः, मारुत्यश्चतस्रः (Vedic only).

    In the Veda the refusal of 6.1.105 is optional (a प्राप्तविभाषा over a
    refusal): one course lets the long vowel stand, the other keeps the refusal
    and the rules it shadowed (6.1.77: मारुत्यः). Not offered where 6.1.104 also
    refuses — an अवर्ण before an इच् — for 6.1.106 takes the 'vā' of 6.1.105 alone.
    """
    for j in v.vowel_pairs():
        name = _first_case_ac(v, j)
        left, right = j.left, j.right
        if name is None or kala(left.s) != kala("ā"):
            continue
        if not (name == "jas" or right.s in S.members("iC")):
            continue
        if left.s in AVARNA and right.s in S.members("iC"):
            continue
        sub = _dirgha(left.s, left.s)
        if sub is None:
            continue
        yield _step(
            left, right, (sub,), optional="वा", adesa=f"{sub} (pūrvasavarṇadīrgha)",
            via=_base([_sup_via(name), S.savarna_of(left.s, sub)]),
            nimitta=f"the ending {sk(name)} follows a long vowel, in the Veda",
            because=(f"in the Veda 6.1.105's refusal is optional: one course lets "
                     f"6.1.102 stand, {sk(left.s)} and {sk(right.s)} becoming the long "
                     f"{sk(sub)}; the other declines that and keeps the refusal"))


# ---------------------------------------------------------------------------
# 6.1.107 अमि पूर्वः, 6.1.108 सम्प्रसारणाच्च
# ---------------------------------------------------------------------------


@rule("6.1.107", name=_name("6.1.107"), families=FAMILIES,
      overrides=(("6.1.102", _quote("tattvabodhini", "6.1.107",
                                    "पूर्वसवर्णदीर्घे प्राप्तेऽयमारम्भः")),))
def ami_purvah(v: View):
    """अकोऽम्यचि परतः पूर्वरूपमेकादेशः — वृक्षम्, अग्निम्, वायुम्, कुमारीम्.

    *पूर्वग्रहणं किम्? … कुमारीमित्यत्र हि त्रिमात्रः स्यात्* — the earlier sound stands,
    not its long form. The ending is the case ending अम्, not any अम्:
    `sup:am`. Kāśikā: *वा छन्दसीत्येव — शमीं च, शम्यं च* — the Vedic option is not
    modelled (COVERAGE).
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if not S.is_member(left.s, "aK") or right.s != "a" or _sup(v, right) != "am":
            continue
        yield _step(
            left, right, _purva(left), adesa=f"{left.s} (pūrvarūpa)",
            via=_base([_sup_via("am"), S.pratyahara("aK", "a, i, u, ṛ, ḷ")]),
            nimitta=f"the ending {{am}} follows an {{ak}}",
            because=(f"{sk(left.s)} is an {{ak}} and {sk(right.s)} begins the case ending "
                     f"{{am}}, so the earlier sound {sk(left.s)} stands for both"))


@rule("6.1.108", name=_name("6.1.108"), families=FAMILIES)
def samprasaranac_ca(v: View):
    """संप्रसारणादचि परे पूर्वरूपमेकादेशः — इष्टम्, उप्तम्, गृहीतम्, विश्वौहः.

    The vowel that stands where a यण् was (1.1.45) is asked of the caller —
    `samprasarana` on its piece, since 6.1.15 ff. are not in the engine — and the
    अ that follows it goes: *संप्रसारणविधानसामर्थ्याद् विगृहीतस्य श्रवणे प्राप्ते पूर्वत्वं
    विधीयते* (Kāśikā), i.e. the yaṇ 6.1.77 would give is what this displaces. In
    the Veda it is optional (*वा छन्दसीत्येव — मित्रावरुणौ यज्यमानः*): the declined
    course is the yaṇ. Not modelled: the antaraṅga condition, *अन्तरङ्गे चाचि कृतार्थं
    वचनमिति बाह्ये पश्चात् संनिपतिते पूर्वत्वं न भवति* (शकह्वौ).
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if (not _samprasarana(v.word(left)) or not v.ends_word(left)
                or not S.is_member(left.s, "iK")):
            continue
        yield _step(
            left, right, _purva(left), adesa=f"{left.s} (pūrvarūpa)",
            optional="वा" if v.state.veda else "",
            via=_base([Via("1.1.45", f"{sk(left.s)} stands where a {{yaṇ}} stood: a "
                                     f"{{samprasāraṇa}} — the caller's word, not the "
                                     f"letters'")]),
            nimitta=f"{sk(right.s)} follows the samprasāraṇa {sk(left.s)}",
            because=(f"{sk(left.s)} is a samprasāraṇa vowel and an {{aC}} follows, so the "
                     f"earlier sound {sk(left.s)} stands for both"
                     + (" — in the Veda only optionally (the other course is 6.1.77's "
                        "yaṇ)" if v.state.veda else "")))


# ---------------------------------------------------------------------------
# 6.1.109 एङः पदान्तादति, 6.1.110 ङसिङसोश्च
# ---------------------------------------------------------------------------


@rule("6.1.109", name=_name("6.1.109"), families=FAMILIES,
      overrides=(("6.1.78", _quote("kashika", "6.1.109", "अयवादेशयोरयमपवादः")),))
def engah_padantad_ati(v: View):
    """पदान्तादेङोऽति परे पूर्वरूपमेकादेशः — हरेऽव, विष्णोऽव, अग्नेऽत्र, वायोऽत्र.

    *एङः किम्? दध्यत्र; पदान्तात् किम्? चयनम्, लवनम्; अति किम्? वायो इति* — and
    *तपरकरणं किम्? वायवायाहि*: the later sound is a SHORT अ. It is written as the
    tradition writes it: the एङ् stays and the अ shows as an avagraha.
    """
    eng = S.members("eṄ")
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        # पदान्तात् — the एङ् ends a pada, which is a question about WORDS
        # (6.1.85 अन्तादिवत् counts), and अति — a short अ, by 1.1.70's तपर.
        if left.s not in eng or not v.pada_final(left):
            continue
        if right.s != "a":
            continue
        yield Application(
            site=site(left, right),
            # पूर्वरूपम् — the earlier sound stands for both. It is written as
            # the tradition writes it: the एङ् stays, and the अ that was
            # absorbed shows as an avagraha.
            edits=(replace(right, NewSeg("'", frozenset({AVAGRAHA}))),),
            detail=Detail(
                kind=EKADESA, sthanin=f"{sk(left.s)}+{sk(right.s)}",
                adesa=f"{sk(left.s)} (pūrvarūpa)",
                nimitta="a short a follows a pada-final {eṅ}",
                because=(f"{sk(left.s)} is an {{eṅ}} ending a pada and the short "
                         f"{sk(right.s)} follows, so the earlier sound {sk(left.s)} "
                         f"stands for both — the {sk(right.s)} is written as "
                         f"an avagraha"),
                via=(S.ekadesa_one_for_two(), S.antadivat(),
                     S.pratyahara("eṄ", "e, o"), S.tapara("a"))))


#: The two endings 6.1.110 and 6.1.111 name: ङसि and ङस्.
_NGASI_NGAS = ("ṅasi", "ṅas")


@rule("6.1.110", name=_name("6.1.110"), families=FAMILIES,
      overrides=(("6.1.78", _quote("kashika", "6.1.110", "अपदान्तार्थ आरम्भः")),))
def ngasingasos_ca(v: View):
    """एङो ङसिङसोरति पूर्वरूपमेकादेशः — हरेः, अग्नेः, वायोः, गोः; हर्योः, हरीणाम् are not.

    *अपदान्तार्थ आरम्भः* (Kāśikā): 6.1.109 covers the pada-final एङ्, this one the
    एङ् that is not, before the अ of ङसि or ङस् — the place where 6.1.78 would give
    अय् or अव्. Written without the avagraha, for it is inside one pada: हरेः.
    *न यथासङ्ख्यम्* — the two endings and the two sounds are not paired.
    """
    eng = S.members("eṄ")
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if left.s not in eng or right.s != "a" or _sup(v, right) not in _NGASI_NGAS:
            continue
        name = _sup(v, right)
        yield _step(
            left, right, _purva(left), adesa=f"{left.s} (pūrvarūpa)",
            via=_base([_sup_via(name), S.pratyahara("eṄ", "e, o")]),
            nimitta=f"the ending {sk(name)} follows an {{eṅ}}",
            because=(f"{sk(left.s)} is an {{eṅ}} and {sk(right.s)} begins the ending "
                     f"{sk(name)}, so the earlier sound {sk(left.s)} stands for both"))


# ---------------------------------------------------------------------------
# 6.1.111 ऋत उत्, 6.1.112 ख्यत्यात् परस्य
# ---------------------------------------------------------------------------


@rule("6.1.111", name=_name("6.1.111"), families=FAMILIES)
def rta_ut(v: View):
    """ऋदन्तान्ङसिङसोरति परे उकार एकादेशः — होतुः, मातुः, पितुः.

    उ is तपर (*उदिति तपरकरणं द्विमात्रनिवृत्त्यर्थम्*), and the substitute of ṛ is
    followed by र् — *द्वयोः षष्ठीनिर्दिष्टयोः स्थाने यः स लभतेऽन्यतरव्यपदेशम्, इति उरण्
    रपरः इति रपरत्वमत्र कृत्वा रात् सस्य इति सलोपः कर्तव्यः* (Kāśikā). The loss of the s
    (8.2.24) is not this family's: होतुर्स् stands here.
    """
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if left.s not in RVARNA or right.s != "a" or _sup(v, right) not in _NGASI_NGAS:
            continue
        name = _sup(v, right)
        sounds = _sounds(raparatva(left.s, "u"))
        via = _base([_sup_via(name), S.tapara("u")])
        if len(sounds) > 1:
            via.append(_raparatva_via(left.s, sounds))
        yield _step(
            left, right, sounds, via=via,
            nimitta=f"the ending {sk(name)} follows a ṛ-varṇa",
            because=(f"{sk(left.s)} ends the stem and {sk(right.s)} begins the ending "
                     f"{sk(name)}, so both are replaced by the single short {sk('u')}, "
                     f"which as the substitute of ṛ is followed by {sk(sounds[-1])}"))


def _before_y() -> Tuple[str, ...]:
    """The sounds that stand before the य् of ख्यत्यात् — खि, खी, ति, ती after their yaṇ
    (*कृतयणादेशयोः*, Kāśikā), read from the sūtra's own word and not typed."""
    word = _sounds(trace.sutra_text("6.1.112").split()[0])
    return tuple(word[i - 1] for i, sound in enumerate(word) if sound == "y" and i)


@rule("6.1.112", name=_name("6.1.112"), families=("ac",))
def khyatyat_parasya(v: View):
    """ख्यत्यात् परस्य — सख्युः, पत्युः: the अ of ङसि, ङस् becomes उ.

    *ख्य* and *त्य* are खि, खी, ति, ती after their यण् has been done (*कृतयणादेशयोः*): so
    the y must be the one 6.1.77 has just made, out of an इ, and the sound before it
    kh or t — *अतिसखेरागच्छति, सेनापतेरागच्छति* end in ए, which is 6.1.110's.
    The substitute is for the LATER sound alone (*परस्य*, 1.1.54): the एकादेश
    heading has lapsed.
    """
    for j in v.pairs():
        y, a = j.left, j.right
        if y.s != "y" or y.seg.made_by != "6.1.77" or a.s != "a":
            continue
        name = _sup(v, a)
        if name not in _NGASI_NGAS:
            continue
        before = v.prev(y)
        if before is None or before.w != y.w or before.s not in _before_y():
            continue
        yield Application(
            site=site(before, y, a), edits=(replace(a, "u"),),
            detail=Detail(
                kind=ADESA, sthanin=a.s, adesa="u",
                nimitta=f"{sk(name)} follows {sk(before.s + y.s)}, a yaṇ already done",
                because=(f"{sk(before.s + y.s)} is what खि, खी, ति, ती become when their "
                         f"yaṇ has been done, and {sk(a.s)} begins the ending {sk(name)}, "
                         f"so that अ alone becomes {sk('u')}"),
                via=(S.adeh_parasya(a.s), _sup_via(name), S.tapara("u"))))


# ---------------------------------------------------------------------------
# The śakandhvādi vārttika — the pararūpa of the ṭi
# ---------------------------------------------------------------------------


def _sakandhvadi_label(items: Sequence[str], index: int) -> Optional[str]:
    """The sense a gaṇa entry is restricted to, or None.

    The gaṇapāṭha writes the restriction as the next item, in the locative or
    genitive: *सीमन्तः केशवेशे*, *सारङ्गः पशुपक्षिणोः*. No entry of the list ends in
    ए or ओः, so an item that does is a sense and not a word.
    """
    nxt = items[index + 1] if index + 1 < len(items) else ""
    return nxt if nxt.endswith(("e", "oḥ")) else None


def _sakandhvadi_entry(joined: str) -> Optional[Tuple[Sequence[str], int]]:
    """The gaṇa and the index of the entry equal to `joined` (a visarga ignored)."""
    for gana in corpus.ganas_for("6.1.94"):
        for index, item in enumerate(gana.items):
            if item.rstrip("ḥ") == joined:
                return gana.items, index
    return None


@rule("6.1.94", name=V_SAKANDHVADISU, families=FAMILIES, authority=VARTTIKA,
      varttika=V_SAKANDHVADISU,
      overrides=(("6.1.87", _quote("balamanorama", "6.1.94", "अत्र गुणे प्राप्ते पररूपम्")),
                 ("6.1.101", _quote("balamanorama", "6.1.94",
                                    "सवर्णदीर्घे प्राप्तेऽनेन पररूपम्"))))
def sakandhvadisu_pararupam(v: View):
    """शकन्ध्वादिषु पररूपं वक्तव्यम् — तच्च टेरिति (Bālamanoramā); शकन्धुः, कर्कन्धुः, कुलटा, मनीषा, हलीषा, पतञ्जलिः.

    The pararūpa is **of the ṭi** (1.1.64: from the last vowel to the end) of the
    first member and the vowel that follows: मनस् + ईषा is मन् + ई. Which
    compounds it reaches is the gaṇapāṭha's list, read from the disk: the joined
    form must be an entry (a visarga ignored). The entries that carry a sense
    (सीमन्तः केशवेशे, सारङ्गः पशुपक्षिणोः) need the sense as the caller's flag.
    **The gaṇa is an ākṛtigaṇa** — *मार्तण्डः* is outside the list the disk gives — and
    that is not modelled (COVERAGE).
    """
    for j in v.junctions():
        left, right = j.left, j.right
        if j.kind != SAMASA or not v.ends_word(left) or not v.begins_word(right):
            continue
        first_text, second = v.word(left).text, v.word(right)
        tail = ti_of(first_text)
        if not tail:
            continue
        joined = first_text[:len(first_text) - len(tail)] + _bare(second)
        found = _sakandhvadi_entry(joined)
        if found is None:
            continue
        items, index = found
        label = _sakandhvadi_label(items, index)
        if label is not None and not v.word(left).has(label):
            continue
        cover = _sounds(tail)
        members = v.word_sights(left.w)
        if len(members) < len(cover):
            continue
        first = members[-len(cover)]
        yield _step(
            left, right, _para(left, right), first=first, adesa=f"{right.s} (pararūpa)",
            sthanin=f"{sk(tail)}+{sk(right.s)}", authority=VARTTIKA,
            varttika=V_SAKANDHVADISU,
            via=_base([Via("1.1.64", f"the ṭi of {sk(first_text)} is {sk(tail)} — from its "
                                     f"last vowel to its end")]),
            nimitta=f"{sk(second.text)} follows {sk(first_text)} in a compound of the "
                    f"śakandhvādi list",
            because=(f"{sk(first_text)} with {sk(second.text)} makes {sk(joined)}, an "
                     f"entry of the śakandhvādi list, so the ṭi {sk(tail)} and the "
                     f"vowel {sk(right.s)} are replaced by the later {sk(right.s)}"))


RULES = (
    ad_gunah, vrddhir_eci, etyedhatyuthsu,
    aksad_uhinyam, svadirerinoh, praduhodhodhyesaisyesu, rte_ca_trtiyasamase,
    pravatsatara_rne,
    atas_ca, upasargad_rti_dhatau, va_supy_apisaleh, auto_mrasasoh,
    engi_pararupam, eve_caniyoge, otvosthayoh_samase_va, emannadisu_chandasi,
    sakandhvadisu_pararupam,
    omango_ca, usy_apadantat, ato_gune_rule,
    avyaktanukaranasyata_itau, ekaco_na, namreditasyantyasya_tu_va,
    nityam_amredite_daci,
    akah_savarne_dirghah_rule, rti_savarne_r_va, lti_savarne_l_va,
    prathamayoh_purvasavarnah, tasmac_chaso_nah_pumsi, nadici, dirghaj_jasi_ca,
    va_chandasi, ami_purvah, samprasaranac_ca, engah_padantad_ati,
    ngasingasos_ca, rta_ut, khyatyat_parasya,
)

#: Where the commentaries disagree or the grammar leaves a question open: what this
#: module does, and what the other reading is — the project's own OPEN (a question
#: the sources did not settle; the module takes the reading the Kāśikā and the
#: Kaumudī share) and SCOPE (something deliberately not done). Each is said again
#: in the docstring of the rule it touches, and every quotation is read back out
#: of the commentary it names (`QUOTES`).
OPEN = (
    ("OPEN", "6.1.89",
     "Whether 6.1.89 is an exception to 6.1.95 at all. The Kāśikā keeps it out of "
     "6.1.95's reach by the maxim — "
     + _quote("kashika", "6.1.89", "ओमाङोश्च इत्येतत् तु पररूपं न बाध्यते")
     + "; the Bālamanoramā (after the Bhāṣya's first answer) says it is no exception "
       "to it — "
     + _quote("balamanorama", "6.1.89", "एत्येधतीति वृद्धिरोमाङोश्चात्यस्यापवाद एव न भवति")
     + " — and that 6.1.95 wins by paratva. Both give अवेहि, and the module declares "
       "nothing of 6.1.95, so 1.4.2 gives it the place: the same course either way."),
    ("OPEN", "6.1.89",
     "The last vārttika of 6.1.89 has three wordings. The Kāśikā lists "
     + _quote("kashika", "6.1.89", "प्रवत्सतरकम्बलवसनानामृणे")
     + " and adds ऋणदशाभ्याम्; the Kaumudī has "
     + _quote("kaumudi", "6.1.89", "प्रवत्सतरकम्बलवसनार्णदशानामृणे")
     + "; the corpus's list of vārttikas has a third order. The rule quotes the "
       "corpus's and takes the six first members from the Kāśikā."),
    ("OPEN", "6.1.94",
     "The option for a dhātu with a subanta inside it. The Kāśikā gives it as the "
     "view of some — "
     + _quote("kashika", "6.1.94", "केचिद् वा सुप्यापिशलेः इत्यनुवर्तयन्ति")
     + "; the Kaumudī and the Bālamanoramā take it as the reading — "
     + _quote("kaumudi", "6.1.94", "इह वासुपीत्यनुवर्त्य वाक्यभेदेन व्याख्येयम्")
     + ". The module follows them: pararūpa is nitya for an ordinary dhātu and "
       "optional, with 6.1.88's vṛddhi, for one with a subanta inside it."),
    ("OPEN", "6.1.97",
     "Why 6.1.97 leaves 6.1.102 alone. The Kaumudī gives the maxim — an exception "
     "stated earlier displaces only the rule next after it, 6.1.101; the Bālamanoramā "
     "says the maxim is not needed, since the pararūpa is no exception to 6.1.102 at "
     "all: "
     + _quote("balamanorama", "6.1.97", "नहि पररूपमिदं पूर्वसवर्णदीर्घस्यापवादः")
     + ". The answer is the same (रामाः): only 6.1.101 is declared displaced, and 6.1.102, "
       "standing later, is given the place by 1.4.2."),
    ("SCOPE", "6.1.96",
     "The clash with 7.2.80 अतो येयः for the optative and उस्. The Kaumudī grants that "
     "pararūpa is the fitter — "
     + _quote("kaumudi", "6.1.96", "यद्यप्यन्तरङ्गत्वात्पररूपं न्याय्यं तथापि यास् इत्येतस्य इय् इति व्याख्येयम्")
     + " — the Tattvabodhinī says why: "
     + _quote("tattvabodhini", "6.1.96", "प्रत्ययमात्रापेक्षत्वात्")
     + ". 7.2.80 is not in the engine, so भवेयुः is not derived here: 6.1.96 acts on "
       "any अवर्ण and उस् inside a pada, and the caller gives the piece as it stands."),
    ("SCOPE", "6.1.100",
     "The Bhāṣya has this as a vārttika under 6.1.99, with a rival — "
     + _quote("bhashya", "6.1.99", "नित्यमाम्रेडिते डाचि पररूपं कर्तव्यम्")
     + ", "
     + _quote("bhashya", "6.1.99", "अकारान्तानुकरणाद्वा")
     + " — where the Vidyut sūtrapāṭha and the Kāśikā have it as a sūtra. It is done as "
       "a sūtra; the Bhāṣya's rival reading is not modelled."),
    ("OPEN", "6.1.85",
     "The Tattvabodhinī calls the sūtra redundant — "
     + _quote("tattvabodhini", "6.1.85", "स्थानिवत्सूत्रेणैव गतार्थमिदम्")
     + " — and the Bālamanoramā defends it (क्षीरपेण: the substitute is the end of the "
       "earlier word for ṇatva, which 1.1.56 could not give it). The engine follows "
       "the Bālamanoramā: the earlier word is kept in `Seg.lw` and 1.1.56 is applied "
       "to nothing."),
    ("OPEN", "1.1.59",
     "The Kāśikā reads द्विर्वचनेऽचि as an atideśa — "
     + _quote("kashika", "1.1.59", "द्विर्वचननिमित्तेऽचि अजादेशः स्थानिवद् भवति द्विर्वचन एव कर्तव्ये")
     + " — the Kaumudī as a refusal — "
     + _quote("kaumudi", "1.1.59", "द्वित्वनिमित्तेऽचिपरे अच आदेशो न स्याद्द्वित्वे कर्तव्ये")
     + ". Not settled here and not needed: no rule of this family doubles a sound."),
)


#: Which sūtras of this family's scope the module implements — the honest
#: account, kept beside the code. See `rulebook.COVERAGE_STATUS`.
COVERAGE = (
    ("6.1.84", "support",
     "एकः पूर्वपरयोः is the `ekadesa` builder — ONE edit over the two sounds, put in the "
     "later word and remembering the earlier — and `supports.ekadesa_one_for_two`, cited "
     "by every rule of 6.1.87–6.1.111 in the same words; there is nothing to run"),
    ("6.1.85", "support",
     "अन्तादिवच्च is `View.ends_word` / `begins_word` (antadivat=True) with `Seg.lw`, and "
     "`supports.antadivat`, cited by each step. Not applied to a rule that rests on the "
     "sounds themselves (वर्णाश्रयविधावयमन्तादिवद्भावो नेष्यते, Kāśikā), which is every "
     "rule of sandhi; 6.1.95 uses it for आङ् (the substitute is the end of आङ्) and 6.1.89 "
     "for ऊठ्. OPEN: the Tattvabodhinī calls the sūtra redundant after 1.1.56, the "
     "Bālamanoramā defends it (see `OPEN`)"),
    ("6.1.86", "scope",
     "षत्वतुकोरसिद्धः — the single substitute is asiddha to ṣatva and tuk (Kāśikā: "
     "सिद्धकार्यं न करोतीत्यर्थः; कोऽसिचत्, अधीत्य). `asiddha.ekadesa_visible` codifies "
     "the question, but `segs.View` hides a sound's past only through `asiddha.visible` "
     "(8.2.1), which does not ask it, and the engine holds no ṣatva (8.3.55–59) or tuk "
     "(6.1.71) rule to be asked. A core matter — see core_requests"),
    ("6.1.87", "rule", ""),
    ("6.1.88", "rule", ""),
    ("6.1.89", "rule",
     "with the five vārttikas (अक्षादूहिन्याम्, स्वादीरेरिणोः, प्रादूहोढोढ्येषैष्येषु, ऋते च "
     "तृतीयासमासे, प्रवत्सतर…ऋणे); their words are read from the words the caller gives"),
    ("6.1.90", "rule", ""),
    ("6.1.91", "rule", ""),
    ("6.1.92", "rule", ""),
    ("6.1.93", "rule", ""),
    ("6.1.94", "partial",
     "the vārttikas एवे चानियोगे, ओत्वोष्ठयोः समासे वा, एमन्नादिषु छन्दसि (Vedic) and "
     "शकन्ध्वादिषु पररूपम् are done; the last only as far as the gaṇapāṭha on disk goes — "
     "the gaṇa is an ākṛtigaṇa, so मार्तण्डः and its like are not derived"),
    ("6.1.95", "rule", ""),
    ("6.1.96", "rule", ""),
    ("6.1.97", "rule", ""),
    ("6.1.98", "rule", "with the vārttika एकाचो न"),
    ("6.1.99", "rule", ""),
    ("6.1.100", "rule", ""),
    ("6.1.101", "rule",
     "with the vārttikas ऋति सवर्णे ऋ वा and ऌति सवर्णे ऌ वा (a sound of two mātrās, "
     "written with the vārttika's letter and marked dvimātra)"),
    ("6.1.102", "partial",
     "the case ending is the caller's flag, so the u that 6.1.113 makes out of the ru of a "
     "प्रथमा ending (शिवः अर्च्यः), where the Bālamanoramā finds 6.1.102 prāpta, is 6.1.102's "
     "only when the piece is written and named (`śiva~s{sup:su} arcya`, and 6.1.104 is then "
     "shown); written as the finished word śivas, शिवोऽर्च्यः comes out by 6.1.87 alone"),
    ("6.1.103", "rule", ""),
    ("6.1.104", "rule", ""),
    ("6.1.105", "rule", ""),
    ("6.1.106", "vedic", "the option of 6.1.105's refusal, in the Veda only"),
    ("6.1.107", "partial",
     "the classical rule is done; the Vedic option (शमीं च, शम्यं च) is not — the "
     "Kaumudī reads 6.1.106's वा into this sūtra by वाक्यभेद but does not say what "
     "then stands for the शम्यम् course, and the engine would give शमीम् again by 6.1.102"),
    ("6.1.108", "partial",
     "the samprasāraṇa vowel is the caller's flag (6.1.15 ff. are not in the engine), and "
     "the antaraṅga condition (अन्तरङ्गे चाचि कृतार्थं वचनम्, शकह्वौ) is not modelled; "
     "the Vedic option is"),
    ("6.1.109", "rule", ""),
    ("6.1.110", "rule", ""),
    ("6.1.111", "rule",
     "the loss of the s after the र् (8.2.24 रात् सस्य) is not this family's: होतुर्स् "
     "stands until it is done"),
    ("6.1.112", "partial",
     "the y must be the one 6.1.77 has made in this derivation, so a finished word "
     "ending in khy or ty is not enough; and the निष्ठानत्व cases (लून्युः, where 8.2.44 "
     "hides the ty) are not modelled"),
    ("1.1.1", "support",
     "वृद्धिरादैच् — `adesa.vrddhi_of` chooses the vṛddhi and each vṛddhi step cites 1.1.1"),
    ("1.1.2", "support",
     "अदेङ् गुणः — `adesa.guna_of` and `anga.ato_gune`; 6.1.87 and 6.1.97 cite 1.1.2"),
    ("1.1.3", "scope",
     "इको गुणवृद्धी supplies इकः only where no sthānin is named (7.3.84); in 6.1.87–88 the "
     "sthānin is named by 6.1.84 (पूर्वपरयोः) — Tattvabodhinī: यत्र साक्षात्स्थानी न "
     "निर्दिष्टः, तत्रैवेयं परिभाषा प्रवर्तते — so it does not arise"),
    ("1.1.53", "scope",
     "ङिच्च puts a ङित् substitute on the last sound; no substitute of 6.1.84–112 is ङित् "
     "(each replaces both sounds at once)"),
    ("1.1.54", "support",
     "आदेः परस्य — cited by 6.1.112, whose उ replaces the first sound (the अ) of the "
     "ending that follows"),
    ("1.1.55", "scope",
     "अनेकाल्शित्सर्वस्य speaks of a many-sound SUBSTITUTE; in 6.1.98 it is the sthānin "
     "that is many, and why the whole `at` goes is नानर्थकेऽलोऽन्त्यविधिः (Bālamanoramā), "
     "the paribhāṣā of 1.1.52 — which is outside this scope"),
    ("1.1.56", "scope",
     "स्थानिवदादेशोऽनल्विधौ — the engine keeps a sound's past (`Seg.prior`) for 8.2.1 only; "
     "every rule of sandhi rests on the sounds themselves, which is exactly what the "
     "sūtra excepts, and the Kāśikā on 6.1.85 says the same of the एकादेश"),
    ("1.1.57", "scope",
     "अचः परस्मिन् पूर्वविधौ — the sthānivadbhāva of a vowel substitute for a rule that "
     "stands earlier; not applied, for the reason given at 1.1.56, and 6.1.86 (which "
     "this family would need it for) is itself open"),
    ("1.1.58", "scope",
     "the ten operations it withholds sthānivadbhāva from — none arises, since it is not "
     "applied (see 1.1.56)"),
    ("1.1.59", "scope",
     "द्विर्वचनेऽचि — sthānivadbhāva for the doubling rules, which the sandhi engine does "
     "not carry (dvitva is 8.4.46–47); not applied, as at 1.1.56. OPEN: the Kāśikā reads "
     "it as an atideśa and the Kaumudī as a refusal (see `OPEN`)"),
    ("1.1.60", "scope",
     "अदर्शनं लोपः — nothing is lost in this family: what 6.1.98 and 6.1.100 remove is "
     "replaced by the later sound, an एकादेश; the `delete` builder is the visarga "
     "family's"),
    ("1.1.61", "scope",
     "प्रत्ययस्य लुक्श्लुलुपः — names the elisions of an affix (लुक्, श्लु, लुप्); no rule "
     "of sandhi elides an affix, and the एकादेश rules replace sounds, not affixes"),
    ("1.1.62", "support",
     "प्रत्ययलोपे प्रत्ययलक्षणम् with 1.4.14 is what makes the first member of a compound "
     "and a preverb a pada (`segs.PADA_LIKE`), asked by `View.pada_final` in 6.1.96, "
     "6.1.97 and 6.1.109"),
    ("1.1.63", "scope",
     "न लुमताङ्गस्य — refuses 1.1.62's pratyayalakṣaṇa after an elision made by a "
     "लुमत् word; the engine has no elision of an affix to carry it, so it has nothing "
     "to refuse"),
    ("1.1.64", "support",
     "अचोऽन्त्यादि टि — `adesa.ti`, asked by the vārttika शकन्ध्वादिषु पररूपम्, whose "
     "pararūpa is of the ṭi (तच्च टेः)"),
)
