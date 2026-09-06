# -*- coding: utf-8 -*-
"""
The pada-assignment section: 1.3.12 to 1.3.93.

1.3.12 and 1.3.13 are in `pada`, because they answer for a root on its own.
Everything from 1.3.14 answers for a root **in use** — with its upasargas, in
a sense, transitive or not, under an affix — and that is what this module
adds. The Kāśikā on 1.3.78 states the architecture of the whole block, and it
is worth quoting because the resolver is built to it:

    पूर्वेण प्रकरणेनात्मनेपदनियमः कृतः, न परस्मैपदनियमः। तत् सर्वतः प्राप्नोति,
    तदर्थमिदमुच्यते। येभ्यो धातुभ्यो येन विशेषणेनात्मनेपदमुक्तं ततो यदन्यत् स शेषः।

The preceding section restricted the ātmanepada and said nothing about the
parasmaipada, which would therefore apply everywhere. 1.3.78 fixes that: from
the *remainder* — शेषादेव नान्यस्मात्. So the block is not eighty independent
rules but one system with three layers:

    1.3.12          the marks a root carries, and 1.3.13 over them
    1.3.14 – 1.3.77 sixty-four provisions granting ātmanepada in a use
    1.3.78          parasmaipada for whatever is left
    1.3.79 – 1.3.93 fifteen provisions taking some of it back

Two things about the codification are worth stating plainly rather than
hiding. First, **sense and transitivity are given, not computed.** A rule such
as 1.3.25 उपान्मन्त्रकरणे turns on whether the speaker means मन्त्रकरण, and no
amount of reading the form will settle that. So `VerbContext` takes them as
inputs, and a provision whose semantic condition is unstated does not fire —
it is reported as a near miss instead, which is the honest answer.

Second, wherever the dhātupāṭha does record something, it is read rather than
retyped. 1.3.15 न गतिहिंसार्थेभ्यः names its roots by sense, and the file gives
the sense of every root: 321 are गत्यर्थ and 157 हिंसार्थ. 1.3.72's two marks are
the svarita and the ñ, both written there. 1.3.91's द्युत्-gaṇa is a contiguous
run in the file. Not one of those is a list in this module.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, FrozenSet, List, Optional, Sequence, Tuple

from src.astadhyayi.corpus import load_dhatupatha
from src.astadhyayi.pada import (
    Pada,
    is_anudattet,
    is_ngit,
    is_nyit,
    is_svaritet,
    marks_of,
    root_key,
)

# --- the senses a rule can turn on ----------------------------------------
#
# Each is a sūtra's own word. Keeping them in one frozen set means a typo in a
# provision is a test failure rather than a rule that silently never fires.

SENSES: FrozenSet[str] = frozenset(
    """
    āsyavihāraṇa prakāśana stheyākhyā ūrdhvakarman mantrakaraṇa spardhā
    gandhana avakṣepaṇa sevana sāhasikya pratiyatna prakathana upayoga
    prasahana sammānana utsañjana ācāryakaraṇa jñāna bhṛti vigaṇana vyaya
    vṛtti sarga tāyana udgamana pādaviharaṇa apahnava ādhyāna bhāsana
    upasambhāṣā yatna vimati upamantraṇa samuccāraṇa vipralāpa pratijñāna
    svakaraṇa avana hetubhaya pralambhana śālīnīkaraṇa abhyāsa grantha
    yajñapātra
    """.split()
)

# --- the conditions an analyst asserts ------------------------------------
#
# Anything a rule needs that the form cannot supply. The caller states which
# hold; a rule needing one that was not stated does not fire.

CONDITIONS: FrozenSet[str] = frozenset(
    """
    karmavyatihāra sakarmaka akarmaka kartrabhiprāya-kriyāphala
    upapadena-pratīyamāna śabdakarman kartṛstha-aśarīra-karman samartha
    vyaktavāc samuccāraṇa tṛtīyāyukta caturthyartha śit aṇau-karma-ṇau-kartā
    cittavat-kartṛka aṇau-akarmaka svāṅgakarmaka
    """.split()
)

#: 1.3.72's two marks, and 1.3.12's two. Read from the dhātupāṭha, never typed.
_MARK_TESTS = {
    "svaritet": is_svaritet,
    "ñit": is_nyit,
    "anudāttet": is_anudattet,
    "ṅit": is_ngit,
}


# --- a root's own sense, read out of the dhātupāṭha -----------------------
#
# 1.3.15 and 1.3.87 name their roots by what the roots mean, and the file
# writes what each root means. The patterns below are the whole of the
# derivation; the tests check them against the examples and counter-examples
# the Kāśikā gives, which is the only way to know a pattern is not too wide.

_ARTHA_PATTERNS: Dict[str, str] = {
    # गत्यर्थ — गतौ, गत्योः, गतिषु
    "gati": r"gat(i|y|O|A)",
    # हिंसार्थ — हिंसायाम्, हिंसागत्योः
    "hiṃsā": r"hiMs",
    # निगरण = अभ्यवहार, swallowing: the Kāśikā glosses it so, and adds भोजन
    # पालन + अभ्यवहार comes out `pAlanAByavahArayoH`, so the leading a of
    # अभ्यवहार is swallowed by the compound and cannot be required.
    "nigaraṇa": r"(nigaraR|ByavahAr|BakzaR|pAne\b)",
    # चलन = कम्पन, the Kāśikā's own gloss
    "calana": r"(calan|kampan)",
}


@lru_cache(maxsize=None)
def _sense_index() -> Dict[str, FrozenSet[str]]:
    """Every root that falls under each artha-class, gathered once."""
    found: Dict[str, set] = {name: set() for name in _ARTHA_PATTERNS}
    for entry in load_dhatupatha().values():
        artha = entry.artha or ""
        key = root_key(entry.upadesa)
        for name, pattern in _ARTHA_PATTERNS.items():
            if re.search(pattern, artha):
                found[name].add(key)
    return {name: frozenset(members) for name, members in found.items()}


def root_senses(root: str) -> FrozenSet[str]:
    """
    Which artha-classes this root belongs to, by the dhātupāṭha's own gloss.

    हन् is `hiMsAgatyoH` and so counts as both गत्यर्थ and हिंसार्थ; लू is
    `Cedane` and counts as neither, which is why व्यतिलुनते keeps its
    ātmanepada while व्यतिघ्नन्ति loses it.
    """
    key = root_key(root)
    return frozenset(
        name for name, members in _sense_index().items() if key in members
    )


# --- the two gaṇas 1.3.91 and 1.3.92 point at ------------------------------
#
# द्युतादि and वृतादि are not lists in the Aṣṭādhyāyī: they are runs in the
# dhātupāṭha, named by their first member. The Kāśikā fixes both ends — द्युत
# (धा.पा. ७४१) through कृपू (७६२) for the first, वृतु (७५८) through कृपू for the
# second — so the run is read off the file between those two entries.

_DYUT_FIRST, _DYUT_LAST = "01.0842", "01.0866"
_VRT_FIRST, _VRT_LAST = "01.0862", "01.0866"


@lru_cache(maxsize=None)
def _run(first: str, last: str) -> Tuple[str, ...]:
    """The roots the dhātupāṭha reads between two of its entries, inclusive."""
    entries = load_dhatupatha()
    codes = sorted(code for code in entries if first <= code <= last)
    return tuple(dict.fromkeys(root_key(entries[code].upadesa) for code in codes))


def dyutadi() -> Tuple[str, ...]:
    """द्युतादि — 1.3.91's gaṇa, द्युत् to कृपू."""
    return _run(_DYUT_FIRST, _DYUT_LAST)


def vrtadi() -> Tuple[str, ...]:
    """वृतादि — 1.3.92's gaṇa, a tail of the same run."""
    return _run(_VRT_FIRST, _VRT_LAST)


# --- what a usage looks like ----------------------------------------------

A = Pada.ATMANEPADA
P = Pada.PARASMAIPADA


@dataclass(frozen=True)
class VerbContext:
    """
    A root as actually used: what is attached to it and what is meant by it.

    Everything but `root` is optional, and an unstated condition is treated as
    unstated rather than false. A rule that needs it does not fire, and
    `near_misses` will say which condition was wanting.
    """

    root: str
    upasargas: Tuple[str, ...] = ()
    #: Which reading of the root, where the name is read more than once. The
    #: commentaries disambiguate in exactly this way — «वह प्रापणे»,
    #: «युजिर् योगे», «भुज पालनाभ्यवहारयोः» — and 174 of the 1,590 names need
    #: it, because they carry different marks in different entries. Matched
    #: against the dhātupāṭha's own gloss. Left unset, the resolver follows
    #: the reading that grants the most and says so in `Verdict.ambiguous`.
    artha: Optional[str] = None
    sense: Optional[str] = None
    given: Tuple[str, ...] = ()
    upapada: Optional[str] = None
    affixes: Tuple[str, ...] = ()
    lakara: Optional[str] = None

    def has(self, condition: str) -> bool:
        return condition in self.given


@dataclass(frozen=True)
class Provision:
    """
    One sūtra's contribution, as conditions rather than as code.

    `gives` names the pada it assigns. A provision with `blocks` instead is a
    प्रतिषेध: it assigns nothing and cancels the sūtras it names.
    """

    sutra: str
    gives: Optional[Pada] = None
    blocks: Tuple[str, ...] = ()
    roots: Tuple[str, ...] = ()
    #: Where the sūtra's own wording picks one reading — 1.3.51's गॄ निगरणे
    #: against गॄ शब्दे, 1.3.66's रौधादिक भुज् against the तौदादिक.
    root_artha: Optional[str] = None
    root_senses: Tuple[str, ...] = ()
    marks: Tuple[str, ...] = ()
    upasargas: Tuple[str, ...] = ()
    upasarga: Optional[bool] = None
    senses: Tuple[str, ...] = ()
    not_senses: Tuple[str, ...] = ()
    upapadas: Tuple[str, ...] = ()
    affixes: Tuple[str, ...] = ()
    lakaras: Tuple[str, ...] = ()
    not_lakaras: Tuple[str, ...] = ()
    requires: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    optional: bool = False
    #: For an option, whether the Kāśikā calls it अप्राप्तविभाषा — granting
    #: what was not otherwise had — or प्राप्तविभाषा, withdrawing what was.
    #: It settles what happens when an option and an invariable rule both
    #: apply: 1.3.43 is अप्राप्त and yields to 1.3.38, while 1.3.85 is प्राप्त
    #: and displaces 1.3.84. Both readings are the commentary's own words.
    aprapta: bool = False
    gloss: str = ""
    example: str = ""
    counter: str = ""

    # -- matching ----------------------------------------------------------

    def unmet(self, ctx: VerbContext) -> Tuple[str, ...]:
        """
        Which of this provision's conditions the usage does not satisfy.

        Empty means it applies. The strings are meant to be read: they are
        what the playground shows when a rule nearly fired.
        """
        missing: List[str] = []
        key = root_key(ctx.root)

        if self.roots and key not in {root_key(r) for r in self.roots}:
            missing.append(f"root is not one of {', '.join(self.roots)}")
        if (self.root_artha and ctx.artha is not None
                and self.root_artha != ctx.artha):
            missing.append(f"root is not the one glossed {self.root_artha}")
        if self.root_senses and not (set(self.root_senses) & root_senses(ctx.root)):
            missing.append(f"root is not {'/'.join(self.root_senses)}-artha")
        for mark in self.marks:
            if not _MARK_TESTS[mark](ctx.root, artha=ctx.artha):
                missing.append(f"root is not {mark}")
        if self.upasargas and not (set(self.upasargas) & set(ctx.upasargas)):
            missing.append(f"no upasarga among {', '.join(self.upasargas)}")
        if self.upasarga is True and not ctx.upasargas:
            missing.append("no upasarga at all")
        if self.upasarga is False and ctx.upasargas:
            missing.append("an upasarga is present")
        if self.senses and ctx.sense not in self.senses:
            missing.append(f"sense is not {'/'.join(self.senses)}")
        if self.not_senses and ctx.sense in self.not_senses:
            missing.append(f"sense is {ctx.sense}")
        if self.upapadas and ctx.upapada not in self.upapadas:
            missing.append(f"upapada is not {'/'.join(self.upapadas)}")
        if self.affixes and not (set(self.affixes) & set(ctx.affixes)):
            missing.append(f"no affix among {', '.join(self.affixes)}")
        if self.lakaras and ctx.lakara not in self.lakaras:
            missing.append(f"lakāra is not {'/'.join(self.lakaras)}")
        if self.not_lakaras and ctx.lakara in self.not_lakaras:
            missing.append(f"lakāra is {ctx.lakara}")
        for condition in self.requires:
            if not ctx.has(condition):
                missing.append(f"{condition} not stated")
        for condition in self.excludes:
            if ctx.has(condition):
                missing.append(f"{condition} is stated")
        return tuple(missing)

    def applies(self, ctx: VerbContext) -> bool:
        return not self.unmet(ctx)

    def describe(self) -> str:
        """
        This provision's conditions, spelled out.

        What the record shows for the sūtra, so a reader can see exactly what
        the codification tests without opening the table.
        """
        parts: List[str] = []
        if self.roots:
            shown = self.roots if len(self.roots) <= 9 else self.roots[:8] + ("…",)
            parts.append("root ∈ {" + ", ".join(shown) + "}")
        if self.root_senses:
            parts.append("root is " + "/".join(self.root_senses) + "-artha")
        for mark in self.marks:
            parts.append(f"root is {mark}")
        if self.upasargas:
            parts.append("upasarga ∈ {" + ", ".join(self.upasargas) + "}")
        if self.upasarga is True:
            parts.append("some upasarga")
        if self.upasarga is False:
            parts.append("no upasarga")
        if self.senses:
            parts.append("sense ∈ {" + ", ".join(self.senses) + "}")
        for sense in self.not_senses:
            parts.append(f"sense ≠ {sense}")
        if self.upapadas:
            parts.append("upapada ∈ {" + ", ".join(self.upapadas) + "}")
        if self.affixes:
            parts.append("affix ∈ {" + ", ".join(self.affixes) + "}")
        if self.lakaras:
            parts.append("lakāra ∈ {" + ", ".join(self.lakaras) + "}")
        for lakara in self.not_lakaras:
            parts.append(f"lakāra ≠ {lakara}")
        parts.extend(self.requires)
        parts.extend(f"not {c}" for c in self.excludes)

        if self.blocks:
            head = "cancels " + ", ".join(self.blocks)
        else:
            head = (self.gives.value if self.gives else "no assignment")
            if self.optional:
                head = "optionally " + head
        return f"{head} when {'; '.join(parts)}" if parts else head


def _p(*args, **kwargs) -> Provision:
    return Provision(*args, **kwargs)


# --- the block, in the order Pāṇini reads it -------------------------------
#
# Each entry carries the Kāśikā's own worked form and, where it gives one, its
# counter-example. Those are what the tests run.

PROVISIONS: Tuple[Provision, ...] = (
    # 1.3.12, restated here so the resolver has one table rather than two.
    _p("1.3.12", gives=A, marks=("anudāttet",),
       gloss="अनुदात्तेत् — the root carries the accent 1.2.30 names",
       example="āste"),
    _p("1.3.12", gives=A, marks=("ṅit",),
       gloss="ङित् — the root carries an indicatory ङ् by 1.3.3",
       example="śete"),

    # -- the reciprocal, and the two prohibitions on it --------------------
    _p("1.3.14", gives=A, requires=("karmavyatihāra",),
       gloss="कर्मव्यतिहारे — each does to the other what the other does to him",
       example="vyatilunate", counter="lunanti"),
    _p("1.3.15", blocks=("1.3.14",), root_senses=("gati", "hiṃsā"),
       gloss="न गतिहिंसार्थेभ्यः — not from roots meaning motion or injury",
       example="vyatigacchanti, vyatighnanti"),
    _p("1.3.15v1", blocks=("1.3.14",), roots=("has", "jalp", "paṭh"),
       gloss="हसादीनामुपसंख्यानम् (vārt.) — the prohibition reaches these too",
       example="vyatihasanti, vyatijalpanti, vyatipaṭhanti"),
    _p("1.3.16", blocks=("1.3.14",),
       upapadas=("itaretara", "anyonya", "paraspara"),
       gloss="इतरेतरान्योन्योपपदात् — nor where the reciprocity is already said",
       example="itaretarasya vyatilunanti"),

    # -- root-and-upasarga provisions --------------------------------------
    _p("1.3.17", gives=A, roots=("viś",), upasargas=("ni",),
       gloss="नेर्विशः", example="niviśate", counter="praviśati"),
    _p("1.3.18", gives=A, roots=("krī",), upasargas=("pari", "vi", "ava"),
       gloss="परिव्यवेभ्यः क्रियः", example="parikrīṇīte, vikrīṇīte"),
    _p("1.3.19", gives=A, roots=("ji",), upasargas=("vi", "parā"),
       gloss="विपराभ्यां जेः", example="vijayate, parājayate"),
    _p("1.3.20", gives=A, roots=("dā",), upasargas=("ā",),
       not_senses=("āsyavihāraṇa",),
       gloss="आङो दोऽनास्यविहरणे", example="vidyām ādatte",
       counter="āsyaṃ vyādadāti"),
    _p("1.3.21", gives=A, roots=("krīḍ",), upasargas=("ā", "anu", "sam", "pari"),
       gloss="क्रीडोऽनुसम्परिभ्यश्च", example="anukrīḍate, ākrīḍate"),
    _p("1.3.22", gives=A, roots=("sthā",), upasargas=("sam", "ava", "pra", "vi"),
       gloss="समवप्रविभ्यः स्थः", example="saṃtiṣṭhate, pratiṣṭhate"),
    _p("1.3.23", gives=A, roots=("sthā",), senses=("prakāśana", "stheyākhyā"),
       gloss="प्रकाशनस्थेयाख्ययोश्च", example="tiṣṭhate kanyā chātrebhyaḥ"),
    _p("1.3.24", gives=A, roots=("sthā",), upasargas=("ud",),
       not_senses=("ūrdhvakarman",),
       gloss="उदोऽनूर्ध्वकर्मणि", example="gehe uttiṣṭhate",
       counter="āsanād uttiṣṭhati"),
    _p("1.3.25", gives=A, roots=("sthā",), upasargas=("upa",),
       senses=("mantrakaraṇa",),
       gloss="उपान्मन्त्रकरणे", example="aindryā gārhapatyam upatiṣṭhate",
       counter="bhartāram upatiṣṭhati yauvanena"),
    _p("1.3.26", gives=A, roots=("sthā",), upasargas=("upa",),
       requires=("akarmaka",),
       gloss="अकर्मकाच्च", example="yāvadbhuktam upatiṣṭhate",
       counter="rājānam upatiṣṭhati"),
    _p("1.3.27", gives=A, roots=("tap",), upasargas=("ud", "vi"),
       requires=("akarmaka",),
       gloss="उद्विभ्यां तपः", example="uttapate, vitapate",
       counter="uttapati suvarṇaṃ suvarṇakāraḥ"),
    _p("1.3.28", gives=A, roots=("yam", "han"), upasargas=("ā",),
       requires=("akarmaka",),
       gloss="आङो यमहनः", example="āyacchate, āhate",
       counter="āyacchati kūpād rajjum"),
    _p("1.3.29", gives=A, upasargas=("sam",), requires=("akarmaka",),
       roots=("gam", "ṛch", "prach", "svṛ", "ṛ", "śru", "vid", "dṛś"),
       gloss="समो गम्यृच्छिप्रच्छिस्वरत्यर्तिश्रुविदिभ्यः — and with दृश् by a वार्त्तिक vārttika",
       example="saṃgacchate, saṃśṛṇute, saṃvitte",
       counter="grāmaṃ saṃpaśyati"),
    _p("1.3.30", gives=A, roots=("hve",), upasargas=("ni", "sam", "upa", "vi"),
       gloss="निसमुपविभ्यो ह्वः", example="nihvayate, saṃhvayate"),
    _p("1.3.31", gives=A, roots=("hve",), upasargas=("ā",), senses=("spardhā",),
       gloss="स्पर्धायामाङः", example="mallo mallam āhvayate",
       counter="gām āhvayati gopālaḥ"),

    # -- कृ ----------------------------------------------------------------
    _p("1.3.32", gives=A, roots=("kṛ",),
       senses=("gandhana", "avakṣepaṇa", "sevana", "sāhasikya", "pratiyatna",
               "prakathana", "upayoga"),
       gloss="गन्धनावक्षेपणसेवनसाहसिक्यप्रतियत्नप्रकथनोपयोगेषु कृञः",
       example="utkurute, gaṇakān upakurute", counter="kaṭaṃ karoti"),
    _p("1.3.33", gives=A, roots=("kṛ",), upasargas=("adhi",),
       senses=("prasahana",),
       gloss="अधेः प्रसहने", example="tam adhicakre", counter="artham adhikaroti"),
    _p("1.3.34", gives=A, roots=("kṛ",), upasargas=("vi",),
       requires=("śabdakarman",),
       gloss="वेः शब्दकर्मणः", example="kroṣṭā vikurute svarān",
       counter="vikaroti payaḥ"),
    _p("1.3.35", gives=A, roots=("kṛ",), upasargas=("vi",), requires=("akarmaka",),
       gloss="अकर्मकाच्च", example="vikurvate saindhavāḥ",
       counter="kaṭaṃ vikaroti"),

    # -- नी ----------------------------------------------------------------
    _p("1.3.36", gives=A, roots=("nī",),
       senses=("sammānana", "utsañjana", "ācāryakaraṇa", "jñāna", "bhṛti",
               "vigaṇana", "vyaya"),
       gloss="सम्माननोत्सञ्जनाचार्यकरणज्ञानभृतिविगणनव्ययेषु नियः",
       example="māṇavakam upanayate, śataṃ vinayate",
       counter="ajāṃ nayati grāmam"),
    _p("1.3.37", gives=A, roots=("nī",), requires=("kartṛstha-aśarīra-karman",),
       gloss="कर्तृस्थे चाशरीरे कर्मणि", example="krodhaṃ vinayate",
       counter="gaḍuṃ vinayati"),

    # -- क्रम् --------------------------------------------------------------
    _p("1.3.38", gives=A, roots=("kram",), upasarga=False,
       senses=("vṛtti", "sarga", "tāyana"),
       gloss="वृत्तिसर्गतायनेषु क्रमः", example="ṛkṣv asya kramate buddhiḥ",
       counter="apakrāmati"),
    _p("1.3.39", gives=A, roots=("kram",), upasargas=("upa", "parā"),
       senses=("vṛtti", "sarga", "tāyana"),
       gloss="उपपराभ्याम् — and with an upasarga, only these two",
       example="upakramate, parākramate", counter="saṃkrāmati"),
    _p("1.3.40", gives=A, roots=("kram",), upasargas=("ā",),
       senses=("udgamana",),
       gloss="आङ उद्गमने", example="ākramate ādityaḥ",
       counter="ākrāmati māṇavakaḥ kutupam"),
    _p("1.3.41", gives=A, roots=("kram",), upasargas=("vi",),
       senses=("pādaviharaṇa",),
       gloss="वेः पादविहरणे", example="suṣṭhu vikramate",
       counter="vikrāmaty ajinasandhiḥ"),
    _p("1.3.42", gives=A, roots=("kram",), upasargas=("pra", "upa"),
       requires=("samartha",),
       gloss="प्रोपाभ्यां समर्थाभ्याम् — where the two are equivalent, i.e. आदिकर्मणि",
       example="prakramate bhoktum", counter="pūrvedyuḥ prakrāmati"),
    _p("1.3.43", gives=A, roots=("kram",), upasarga=False, optional=True,
       aprapta=True,
       gloss="अनुपसर्गाद्वा", example="kramate / krāmati", counter="saṃkrāmati"),

    # -- ज्ञा ---------------------------------------------------------------
    _p("1.3.44", gives=A, roots=("jñā",), senses=("apahnava",), upasarga=True,
       gloss="अपह्नवे ज्ञः — and the Kāśikā adds सोपसर्गश्चायम्, न केवलः",
       example="śatam apajānīte", counter="na tvaṃ kiṃcid api jānāsi"),
    _p("1.3.45", gives=A, roots=("jñā",), requires=("akarmaka",),
       gloss="अकर्मकाच्च", example="sarpiṣo jānīte",
       counter="svareṇa putraṃ jānāti"),
    _p("1.3.46", gives=A, roots=("jñā",), upasargas=("sam", "prati"),
       not_senses=("ādhyāna",),
       gloss="सम्प्रतिभ्यामनाध्याने", example="śataṃ saṃjānīte",
       counter="mātuḥ saṃjānāti"),

    # -- वद् ----------------------------------------------------------------
    _p("1.3.47", gives=A, roots=("vad",),
       senses=("bhāsana", "upasambhāṣā", "jñāna", "yatna", "vimati",
               "upamantraṇa"),
       gloss="भासनोपसम्भाषाज्ञानयत्नविमत्युपमन्त्रणेषु वदः",
       example="kṣetre vadate, kulabhāryām upavadate",
       counter="yat kiṃcid vadati"),
    _p("1.3.48", gives=A, roots=("vad",), senses=("samuccāraṇa",),
       requires=("vyaktavāc",),
       gloss="व्यक्तवाचां समुच्चारणे", example="saṃpravadante brāhmaṇāḥ",
       counter="saṃpravadanti kukkuṭāḥ"),
    _p("1.3.49", gives=A, roots=("vad",), upasargas=("anu",),
       requires=("akarmaka", "vyaktavāc"),
       gloss="अनोरकर्मकात्", example="anuvadate kaṭhaḥ kalāpasya",
       counter="anuvadati vīṇā"),
    _p("1.3.50", gives=A, roots=("vad",), senses=("vipralāpa",),
       requires=("vyaktavāc", "samuccāraṇa"),
       gloss="विभाषा विप्रलापे", example="vipravadante / vipravadanti sāṃvatsarāḥ",
       optional=True),

    # -- गॄ, चर्, दा, यम् ---------------------------------------------------
    _p("1.3.51", gives=A, roots=("gṝ",), root_artha="nigaraRe",
       upasargas=("ava",),
       gloss="अवाद्ग्रः — the निगरण root of the tudādi, not the शब्द one",
       example="avagirate", counter="girati"),
    _p("1.3.52", gives=A, roots=("gṝ",), upasargas=("sam",),
       senses=("pratijñāna",),
       gloss="समः प्रतिज्ञाने", example="śataṃ saṃgirate",
       counter="saṃgirati grāsam"),
    _p("1.3.53", gives=A, roots=("car",), upasargas=("ud",),
       requires=("sakarmaka",),
       gloss="उदश्चरः सकर्मकात्", example="geham uccarate",
       counter="bāṣpam uccarati"),
    _p("1.3.54", gives=A, roots=("car",), upasargas=("sam",),
       requires=("tṛtīyāyukta",),
       gloss="समस्तृतीयायुक्तात्", example="aśvena saṃcarate"),
    _p("1.3.55", gives=A, roots=("dā",), upasargas=("sam",),
       requires=("tṛtīyāyukta", "caturthyartha"),
       gloss="दाणश्च सा चेच्चतुर्थ्यर्थे", example="dāsyā saṃprayacchate",
       counter="pāṇinā saṃprayacchati"),
    _p("1.3.56", gives=A, roots=("yam",), upasargas=("upa",),
       senses=("svakaraṇa",),
       gloss="उपाद्यमः स्वकरणे — स्वकरण here is marriage, not appropriation",
       example="bhāryām upayacchate",
       counter="devadatto yajñadattasya bhāryām upayacchati"),

    # -- the desiderative --------------------------------------------------
    _p("1.3.57", gives=A, roots=("jñā", "śru", "smṛ", "dṛś"), affixes=("san",),
       gloss="ज्ञाश्रुस्मृदृशां सनः", example="dharmaṃ jijñāsate, naṣṭaṃ susmūrṣate",
       counter="jānāti, smarati"),
    _p("1.3.58", blocks=("1.3.57",), roots=("jñā",), upasargas=("anu",),
       affixes=("san",),
       gloss="नानोर्ज्ञः", example="putram anujijñāsati",
       counter="dharmaṃ jijñāsate"),
    _p("1.3.59", blocks=("1.3.57",), roots=("śru",), upasargas=("prati", "ā"),
       affixes=("san",),
       gloss="प्रत्याङ्भ्यां श्रुवः", example="pratiśuśrūṣati, āśuśrūṣati"),

    # -- शद् and मृ --------------------------------------------------------
    _p("1.3.60", gives=A, roots=("śad",), requires=("śit",),
       gloss="शदेः शितः", example="śīyate", counter="śatsyati, śiśatsati"),
    _p("1.3.61", gives=A, roots=("mṛ",), lakaras=("luṅ", "liṅ"),
       gloss="म्रियतेर्लुङ्लिङोश्च", example="amṛta, mṛṣīṣṭa"),
    _p("1.3.61", gives=A, roots=("mṛ",), requires=("śit",),
       gloss="म्रियतेर् … शितश्च", example="mriyate"),
    _p("1.3.61niyama", blocks=("1.3.12",), roots=("mṛ",),
       not_lakaras=("luṅ", "liṅ"), excludes=("śit",),
       gloss="म्रियतेः … नियमार्थमिदम् — मृङ् is ṅit, so 1.3.61 restricts rather "
             "than grants: ङित्त्वादात्मनेपदमत्र सिद्धमेव. Outside luṅ, liṅ and a "
             "śit the ātmanepada lapses, and an unstated lakāra is not one of "
             "the three either",
       example="mariṣyati, amariṣyat"),

    # -- युज्, क्ष्णु, भुज् -------------------------------------------------
    _p("1.3.64", gives=A, roots=("yuj",), upasargas=("pra", "upa"),
       not_senses=("yajñapātra",),
       gloss="प्रोपाभ्यां युजेरयज्ञपात्रेषु", example="prayuṅkte, upayuṅkte",
       counter="pātrāṇi prayunakti"),
    _p("1.3.65", gives=A, roots=("kṣṇu",), upasargas=("sam",),
       gloss="समः क्ष्णुवः — kept out of 1.3.29 because अकर्मकात् carries there",
       example="saṃkṣṇute śastram"),
    _p("1.3.66", gives=A, roots=("bhuj",),
       root_artha="pAlanAByavahArayoH", not_senses=("avana",),
       gloss="भुजोऽनवने — the रुधादि root, not the तुदादि one",
       example="bhuṅkte", counter="bhunakty enam agnir āhitaḥ"),

    # -- the causative ------------------------------------------------------
    _p("1.3.67", gives=A, affixes=("ṇic",), requires=("aṇau-karma-ṇau-kartā",),
       not_senses=("ādhyāna",),
       gloss="णेरणौ यत्कर्म णौ चेत् स कर्ताऽनाध्याने",
       example="ārohayate hastī svayam eva",
       counter="smarayaty enaṃ vanagulmaḥ svayam eva"),
    _p("1.3.68", gives=A, roots=("bhī", "smi"), affixes=("ṇic",),
       senses=("hetubhaya",),
       gloss="भीस्म्योर्हेतुभये", example="jaṭilo bhīṣayate",
       counter="kuñcikayainaṃ bhāyayati"),
    _p("1.3.69", gives=A, roots=("gṛdh", "vañc"), affixes=("ṇic",),
       senses=("pralambhana",),
       gloss="गृधिवञ्च्योः प्रलम्भने", example="māṇavakaṃ vañcayate",
       counter="ahiṃ vañcayati"),
    _p("1.3.70", gives=A, roots=("lī",), affixes=("ṇic",),
       senses=("sammānana", "śālīnīkaraṇa", "pralambhana"),
       gloss="लियः सम्माननशालीनीकरणयोश्च — and प्रलम्भन by the च",
       example="jaṭābhir ālāpayate", counter="bālakam ullāpayati"),
    _p("1.3.71", gives=A, roots=("kṛ",), affixes=("ṇic",), upapadas=("mithyā",),
       senses=("abhyāsa",),
       gloss="मिथ्योपपदात् कृञोऽभ्यासे", example="padaṃ mithyā kārayate",
       counter="padaṃ suṣṭhu kārayati"),

    # -- 1.3.72 and the four that extend it --------------------------------
    _p("1.3.72", gives=A, marks=("svaritet",),
       requires=("kartrabhiprāya-kriyāphala",),
       gloss="स्वरितञितः कर्त्रभिप्राये क्रियाफले — the svarita half",
       example="yajate, pacate", counter="yajanti yājakāḥ"),
    _p("1.3.72", gives=A, marks=("ñit",),
       requires=("kartrabhiprāya-kriyāphala",),
       gloss="स्वरितञितः … — the ñit half",
       example="sunute, kurute", counter="kurvanti karmakarāḥ"),
    _p("1.3.73", gives=A, roots=("vad",), upasargas=("apa",),
       requires=("kartrabhiprāya-kriyāphala",),
       gloss="अपाद्वदः", example="dhanakāmo nyāyam apavadate",
       counter="apavadati"),
    _p("1.3.74", gives=A, affixes=("ṇic",),
       requires=("kartrabhiprāya-kriyāphala",),
       gloss="णिचश्च", example="kaṭaṃ kārayate",
       counter="kaṭaṃ kārayati parasya"),
    _p("1.3.75", gives=A, roots=("yam",), upasargas=("sam", "ud", "ā"),
       not_senses=("grantha",), requires=("kartrabhiprāya-kriyāphala",),
       gloss="समुदाङ्भ्यो यमोऽग्रन्थे", example="bhāram udyacchate",
       counter="udyacchati cikitsāṃ vaidyaḥ"),
    _p("1.3.76", gives=A, roots=("jñā",), upasarga=False,
       requires=("kartrabhiprāya-kriyāphala",),
       gloss="अनुपसर्गाज्ज्ञः", example="gāṃ jānīte",
       counter="svargaṃ lokaṃ na prajānāti mūḍhaḥ"),
    _p("1.3.77", gives=A, optional=True, aprapta=True,
       requires=("upapadena-pratīyamāna",),
       excludes=("kartrabhiprāya-kriyāphala",),
       gloss="विभाषोपपदेन प्रतीयमाने — where an adjacent word, not the "
             "construction, conveys that the fruit reaches the agent",
       example="svaṃ yajñaṃ yajati / yajate"),

    # -- 1.3.79 to 1.3.93: parasmaipada taken back -------------------------
    _p("1.3.79", gives=P, roots=("kṛ",), upasargas=("anu", "parā"),
       gloss="अनुपराभ्यां कृञः", example="anukaroti, parākaroti"),
    _p("1.3.80", gives=P, roots=("kṣip",), upasargas=("abhi", "prati", "ati"),
       gloss="अभिप्रत्यतिभ्यः क्षिपः", example="abhikṣipati",
       counter="ākṣipate"),
    _p("1.3.81", gives=P, roots=("vah",), upasargas=("pra",),
       gloss="प्राद्वहः", example="pravahati", counter="āvahate"),
    _p("1.3.82", gives=P, roots=("mṛṣ",), upasargas=("pari",),
       gloss="परेर्मृषः", example="parimṛṣyati", counter="āmṛṣyate"),
    _p("1.3.83", gives=P, roots=("ram",), upasargas=("vi", "ā", "pari"),
       gloss="व्याङ्परिभ्यो रमः", example="viramati", counter="abhiramate"),
    _p("1.3.84", gives=P, roots=("ram",), upasargas=("upa",),
       gloss="उपाच्च", example="devadattam uparamati"),
    _p("1.3.85", gives=P, roots=("ram",), upasargas=("upa",),
       requires=("akarmaka",), optional=True,
       gloss="विभाषाकर्मकात्", example="uparamati / uparamate"),
    _p("1.3.86", gives=P, affixes=("ṇic",),
       roots=("budh", "yudh", "naś", "jan", "i", "pru", "dru", "sru"),
       gloss="बुधयुधनशजनेङ्प्रुद्रुस्रुभ्यो णेः",
       example="bodhayati, jhanayati, drāvayati"),
    _p("1.3.87", gives=P, affixes=("ṇic",), root_senses=("nigaraṇa", "calana"),
       gloss="निगरणचलनार्थेभ्यश्च", example="bhojayati, calayati"),
    _p("1.3.88", gives=P, affixes=("ṇic",),
       requires=("aṇau-akarmaka", "cittavat-kartṛka"),
       gloss="अणावकर्मकाच्चित्तवत्कर्तृकात्", example="āsayati devadattam",
       counter="śoṣayate vrīhīn ātapaḥ"),
    _p("1.3.89", blocks=("1.3.86", "1.3.87", "1.3.88"), affixes=("ṇic",),
       roots=("pā", "dam", "yam", "yas", "muh", "ruc", "nṛt", "vad", "vas",
              "dhe"),
       gloss="न पादम्याङ्यमाङ्यसपरिमुहरुचिनृतिवदवसः — and with धे by a वार्त्तिक vārttika",
       example="pāyayate, damayate, rocayate, nartayate"),
    _p("1.3.90", gives=P, affixes=("kyaṣ",), optional=True,
       gloss="वा क्यषः", example="lohitāyati / lohitāyate"),
    _p("1.3.91", gives=P, roots=dyutadi(), lakaras=("luṅ",), optional=True,
       gloss="द्युद्भ्यो लुङि", example="vyadyutat / vyadyotiṣṭa",
       counter="dyotate"),
    _p("1.3.92", gives=P, roots=vrtadi(), affixes=("sya", "san"), optional=True,
       gloss="वृद्भ्यः स्यसनोः", example="vartsyati / vartiṣyate",
       counter="vartate"),
    _p("1.3.93", gives=P, roots=("kḷp",), lakaras=("luṭ",), optional=True,
       gloss="लुटि च कॢपः", example="kalptā / kalpitā"),
    _p("1.3.93", gives=P, roots=("kḷp",), affixes=("sya", "san"), optional=True,
       gloss="लुटि च कॢपः — the च draws स्य and सन् down from 1.3.92",
       example="kalpsyati / kalpiṣyate"),
)


# --- the resolution --------------------------------------------------------


@dataclass(frozen=True)
class Verdict:
    """
    Which endings, by which sūtra, and on what ground.

    `optional` means both sets stand: a वा or विभाषा fired. `blocked` names the
    prohibitions that fired, so a suppressed rule is visible rather than
    silently absent.
    """

    pada: Pada
    by: str
    why: str
    optional: bool = False
    also_by: Tuple[str, ...] = ()
    blocked: Tuple[str, ...] = ()
    #: Set when the root name is read more than once with different marks and
    #: the caller did not say which was meant. The answer then follows the
    #: reading that grants the most, and this says so rather than hiding it.
    ambiguous: Tuple[str, ...] = ()


def _drop_aprapta(candidates: List[Provision]) -> List[Provision]:
    """
    अप्राप्तविभाषा — an option over what was not otherwise obtained.

    Where such an option and an invariable rule both reach the same use, the
    option has nothing to do and the invariable rule stands. 1.3.43 is the
    case: क्रमते/क्रामति is offered for क्रम् without an upasarga, but in the
    senses 1.3.38 names the ātmanepada is already had, so ऋक्ष्वस्य क्रमते
    बुद्धिः is not optional. The Kāśikā marks the two kinds apart in so many
    words — अप्राप्तविभाषेयम् on 1.3.43, प्राप्तविभाषेयम् on 1.3.50 — and only
    the first yields.
    """
    if any(not p.optional for p in candidates):
        return [p for p in candidates if not p.aprapta]
    return candidates


def _live(ctx: VerbContext) -> Tuple[List[Provision], Tuple[str, ...]]:
    """The provisions that apply, after the prohibitions have run."""
    matched = [p for p in PROVISIONS if p.applies(ctx)]
    prohibitions = [p for p in matched if p.blocks]
    killed = {sutra for p in prohibitions for sutra in p.blocks}
    live = [
        p for p in matched
        if not p.blocks and p.sutra.split("niyama")[0] not in killed
    ]
    return live, tuple(sorted({p.sutra for p in prohibitions}))


def resolve(ctx: VerbContext) -> Verdict:
    """
    Which set of endings this use of the root takes.

    The order is the Kāśikā's on 1.3.78. The ātmanepada provisions run first;
    1.3.79–1.3.93 are apavādas to them and win where they apply; and what is
    left over falls to 1.3.78, which is why that sūtra says शेषात् and not
    simply कर्तरि परस्मैपदम्.
    """
    live, blocked = _live(ctx)
    unsettled = _ambiguity(ctx)

    para = [p for p in live if p.gives is P]
    atma = [p for p in live if p.gives is A]

    para = _drop_aprapta(para)
    atma = _drop_aprapta(atma)

    if para:
        chosen = max(para, key=lambda p: _order(p.sutra))
        return Verdict(
            P, chosen.sutra, chosen.gloss, optional=chosen.optional,
            also_by=tuple(p.sutra for p in para if p is not chosen),
            blocked=blocked, ambiguous=unsettled,
        )
    if atma:
        chosen = max(atma, key=lambda p: _order(p.sutra))
        return Verdict(
            A, chosen.sutra, chosen.gloss, optional=chosen.optional,
            also_by=tuple(dict.fromkeys(
                p.sutra for p in atma if p.sutra != chosen.sutra)),
            blocked=blocked, ambiguous=unsettled,
        )
    return Verdict(
        P, "1.3.78",
        "शेषात् कर्तरि परस्मैपदम् — nothing in 1.3.12–1.3.77 reaches this use, "
        "and what is left over takes the other set: शेषादेव नान्यस्मात्",
        blocked=blocked, ambiguous=unsettled,
    )


def purvavat(ctx: VerbContext) -> Optional[Verdict]:
    """
    1.3.62 पूर्ववत् सनः — a desiderative takes what its own root took.

    सनः पूर्वो यो धातुरात्मनेपदी, तद्वत् सन्नन्तादात्मनेपदं भवति, and the
    Kāśikā adds the clause that does the real work: येन निमित्तेन पूर्वस्माद्
    आत्मनेपदं विधीयते, तेनैव सन्नन्तादपि भवति — by the same cause, not merely
    the same outcome. So the atideśa is performed by resolving the root again
    with सन् set aside; a cause that is absent there is absent here too, which
    is exactly why शिशत्सति and मुमूर्षति keep the other set.
    """
    without = VerbContext(
        root=ctx.root,
        upasargas=ctx.upasargas,
        artha=ctx.artha,
        sense=ctx.sense,
        given=ctx.given,
        upapada=ctx.upapada,
        affixes=tuple(a for a in ctx.affixes if a != "san"),
        lakara=ctx.lakara,
    )
    verdict = resolve(without)
    if verdict.pada is not A:
        return None
    return Verdict(
        A, "1.3.62",
        "पूर्ववत् सनः — the desiderative takes what the root took, by the same "
        f"cause: here {verdict.by}, {verdict.why}",
        optional=verdict.optional,
        also_by=(verdict.by,),
        blocked=verdict.blocked,
    )


def _ambiguity(ctx: VerbContext) -> Tuple[str, ...]:
    """The readings of this root name that differ in their marks, if unsettled."""
    if ctx.artha is not None:
        return ()
    readings = marks_of(ctx.root)
    if len({marks for _, _, marks in readings}) < 2:
        return ()
    return tuple(
        f"{code} {artha} [{'/'.join(marks) or 'unmarked'}]"
        for code, artha, marks in readings
    )


def _order(sutra: str) -> Tuple[int, ...]:
    """Sūtra order, so a later provision can be recognised as later."""
    digits = re.findall(r"\d+", sutra)
    return tuple(int(d) for d in digits)


def near_misses(ctx: VerbContext) -> Tuple[Tuple[str, Tuple[str, ...]], ...]:
    """
    Provisions that would have fired but for one condition.

    The point is transparency: when a rule does not apply because a semantic
    condition was never stated, the answer should say so rather than leave the
    reader to guess whether the rule was considered at all.
    """
    out = []
    for provision in PROVISIONS:
        unmet = provision.unmet(ctx)
        if len(unmet) == 1:
            out.append((provision.sutra, unmet))
    return tuple(out)


def pada_of_usage(
    root: str,
    *,
    upasargas: Sequence[str] = (),
    artha: Optional[str] = None,
    sense: Optional[str] = None,
    given: Sequence[str] = (),
    upapada: Optional[str] = None,
    affixes: Sequence[str] = (),
    lakara: Optional[str] = None,
    bhava_or_karman: bool = False,
    karmakartari: bool = False,
) -> Verdict:
    """
    The whole of 1.3.12–1.3.93 for one use of a root.

    1.3.13 is tried first: in the impersonal and the passive the endings are
    ātmanepada whatever else holds. The one wrinkle is कर्मकर्तरि — the Kāśikā
    on 1.3.78 points out that 1.3.14's second कर्तृग्रहण carries all the way
    down, so पच्यत ओदनः स्वयमेव keeps the middle endings and 1.3.78 does not
    reach it.
    """
    if bhava_or_karman or karmakartari:
        return Verdict(
            A, "1.3.13",
            "भावकर्मणोः — in the impersonal or the passive the endings are "
            "ātmanepada whatever the root: ग्लायते भवता, क्रियते कटः"
            + (". कर्मकर्तरि — पच्यत ओदनः स्वयमेव: 1.3.14's second कर्तृग्रहण "
               "carries down to 1.3.78, so parasmaipada is withheld here too"
               if karmakartari else ""),
        )
    ctx = VerbContext(
        root=root,
        upasargas=tuple(upasargas),
        artha=artha,
        sense=sense,
        given=tuple(given),
        upapada=upapada,
        affixes=tuple(affixes),
        lakara=lakara,
    )
    direct = resolve(ctx)
    if "san" in ctx.affixes and direct.pada is not A:
        carried = purvavat(ctx)
        if carried is not None:
            return carried
    return direct


def provisions_for(sutra: str) -> Tuple[Provision, ...]:
    """Every provision one sūtra contributes — some contribute two."""
    return tuple(
        p for p in PROVISIONS
        if p.sutra == sutra or p.sutra.startswith(sutra + "v")
        or p.sutra.startswith(sutra + "niyama")
    )


__all__ = [
    "CONDITIONS",
    "PROVISIONS",
    "Provision",
    "SENSES",
    "VerbContext",
    "Verdict",
    "dyutadi",
    "purvavat",
    "near_misses",
    "pada_of_usage",
    "provisions_for",
    "resolve",
    "root_senses",
    "vrtadi",
]
