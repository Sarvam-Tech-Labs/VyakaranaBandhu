# -*- coding: utf-8 -*-
"""
कित्त्व and ङित्त्व by atideśa — 1.2.1 to 1.2.26.

An affix marked with an indicatory क् or ङ् blocks guṇa and vṛddhi, by 1.1.5
क्ङिति च. These twenty-six sūtras hand that mark to affixes that do not carry
it, and take it back from affixes that do. The corpus types the three runs, and
the typing is the structure:

    1.2.1 – 1.2.4    ङित्त्वातिदेश   behaves as if ṅit
    1.2.5 – 1.2.17   कित्त्वातिदेश   behaves as if kit
    1.2.18 – 1.2.26  अकित्त्वातिदेश  and here the kit-ness is denied

The denials matter because the affixes concerned — क्त्वा, and the निष्ठा pair
क्त and क्तवतु — are kit already, by the plain 1.3.8 लशक्वतद्धिते. So this block
does not need to be told which affixes are kit to begin with: `itsamjna` reads
the mark off the affix, exactly as it reads ङ् off a root for 1.3.12, and
1.2.18 onwards then withdraws it under conditions.

Three things are worth saying about what is computed and what is not.

**The shapes are computed.** असंयोगान्त, इगन्त, रलन्त, नोपध, व्युपध, झलादि —
every one is a pratyāhāra applied to a position, and both halves are already
codified. `formation` holds them; nothing here lists a root by its shape.

**The gaṇa is read.** कुटादि is not a list in the Aṣṭādhyāyī. The Kāśikā fixes
its ends — कुट कौटिल्ये to कुङ् शब्दे — and the dhātupāṭha has those at 06.0093
and 06.0136, so the forty-three members between them are read off the file.

**पित्त्व is an input.** 1.2.4's अपित् carries down through 1.2.5, and for a
सार्वधातुक ending the mark can be read off the affix — तिप् has प् and तस् does
not. For the लिट् endings it cannot: the Kāśikā's counter-example बिभेदिथ shows
थल् counts as पित्, and nothing in the affix's own spelling says so. 3.4.82,
which teaches those endings, is not codified, so the caller supplies it.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Dict, FrozenSet, List, Optional, Sequence, Tuple

from src.astadhyayi.formation import (
    begins_with,
    drop_aprapta,
    ends_in,
    gana_run,
    ik_before_final_consonant,
    is_asamyoganta,
    order_of,
    penult_is,
)
from src.astadhyayi.itsamjna import PRATYAYA, analyze
from src.astadhyayi.pada import root_key
from src.astadhyayi.samjna import ghu_roots


class Behaves(Enum):
    """What an affix is made to behave as."""

    KIT = "kit"
    NGIT = "ṅit"


# --- कुटादि ----------------------------------------------------------------
#
# कुटादयोऽपि «कुट कौटिल्ये» इत्येतदारभ्य यावत् «कुङ् शब्दे» — the Kāśikā names
# both ends, and the dhātupāṭha has them at 06.0093 and 06.0136.

_KUTADI_FIRST, _KUTADI_LAST = "06.0093", "06.0136"


def kutadi() -> Tuple[str, ...]:
    """कुटादि — the gaṇa 1.2.1 points at, read between its two named ends."""
    return gana_run(_KUTADI_FIRST, _KUTADI_LAST)


# --- the shapes a sūtra can ask about --------------------------------------
#
# Each is a question about sounds and nothing else. Keeping them in one table
# means a provision can only ask a question that has an answer.

SHAPES: Dict[str, Callable[[str], bool]] = {
    # 1.2.5 असंयोगात् — सस्रंसे and दध्वंसे are what it keeps out
    "asaṃyogānta": is_asamyoganta,
    # 1.2.9 इकः — चिचीषति yes, पिपासति no
    "ik-final": lambda root: ends_in(root, "iK"),
    # 1.2.10, 1.2.11 इगन्तात् इक्समीपात् हलः — बिभित्सति yes, यियक्षते no
    "ik-then-consonant": ik_before_final_consonant,
    # 1.2.12 उश्च. The sūtra says उ, and the Kāśikā reads it as ऋवर्णान्त —
    # ऋवर्णान्ताद् धातोः — because the उ of the sūtra is the उ of the ऋ-ॠ pair
    # taken by 1.1.69. कृषीष्ट and अकृत, but वरिषीष्ट is वृ and not ऋ-final.
    "ṛ-final": lambda root: root_key(root)[-1:] in ("ṛ", "ṝ"),
    # 1.2.21 उदुपधात् — द्युतितम् yes, लिखितम् no
    "u-penult": lambda root: penult_is(root, "u"),
    # 1.2.23 नोपधात् — ग्रथित्वा yes, रेफित्वा no
    "n-penult": lambda root: penult_is(root, "n"),
    # 1.2.23 थफान्तात् — ग्रन्थ् and गुम्फ् yes, स्रंस् no
    "th-or-ph-final": lambda root: (root_key(root).endswith("th")
                                    or root_key(root).endswith("ph")),
    # 1.2.26 रलः — द्युतित्वा yes, देवित्वा no
    "ral-final": lambda root: ends_in(root, "raL"),
    # 1.2.26 व्युपधात् — उ or इ as penultimate: द्युत् and लिख् yes, वृत् no
    "u-or-i-penult": lambda root: penult_is(root, "u", "i"),
    # 1.2.26 हलादेः — द्युत् yes, एष् no
    "hal-initial": lambda root: begins_with(root_key(root), "haL"),
}


# --- what is being formed --------------------------------------------------

#: The sound each affix actually begins with when it attaches, which is what
#: झलादि asks about. सन् and सिच् are plain enough; the आशीर्लिङ् of 1.2.11 is
#: सीष्ट and so begins with स्, though the affix is taught as लिङ्.
_ATTACHES_AS: Dict[str, str] = {
    "san": "sa",
    "sic": "si",
    "liṅ": "sīṣṭa",
    "ktvā": "tvā",
    "niṣṭhā": "ta",
}

CONDITIONS: FrozenSet[str] = frozenset(
    """
    pit seṭ ātmanepada
    """.split()
)

SENSES: FrozenSet[str] = frozenset(
    """
    gandhana upayamana titikṣā anas bhāva-ādikarman
    """.split()
)


@dataclass(frozen=True)
class Formation:
    """
    A root with an affix coming after it, as far as this block cares.

    `given` holds what cannot be read off either: whether the ending is पित्,
    whether the इट् augment is there, whether the endings are ātmanepada.
    """

    root: str
    affix: str
    #: The ending as actually written, where the caller knows it — तिप्, तस्,
    #: अतुस्, थल्. 1.2.1's अञ्णित् and 1.2.4's अपित् are questions about the
    #: affix's own it-letters, and given the ending they can be answered by
    #: reading it rather than by being told.
    ending: Optional[str] = None
    artha: Optional[str] = None
    sense: Optional[str] = None
    given: Tuple[str, ...] = ()

    def has(self, condition: str) -> bool:
        return condition in self.given

    @property
    def marks(self) -> Tuple[str, ...]:
        """The it-letters of the ending, where one was given."""
        if not self.ending:
            return ()
        return tuple(sorted(analyze(self.ending, PRATYAYA).it_letters))

    @property
    def pit(self) -> bool:
        """
        Is the ending पित्? 1.2.4's condition, carried down through 1.2.5.

        Read off the ending where there is one — तिप् has प् and तस् does not.
        For the लिट् endings it cannot be read: the Kāśikā's बिभेदिथ shows थल्
        counts as पित् and nothing in its spelling says so, 3.4.82 not being
        codified. There the caller states it.
        """
        if self.ending:
            return "p" in self.marks
        return self.has("pit")

    @property
    def jhaladi(self) -> bool:
        """
        Does the affix begin with a झल्?

        Only if the इट् augment is not there. That single condition is what
        separates the Kāśikā's चिचीषति from its शिशयिषते: सन् begins with स्,
        but under सेट् it begins with इ and 1.2.9 no longer reaches it.
        """
        if self.has("seṭ"):
            return False
        return begins_with(_ATTACHES_AS.get(self.affix, self.affix), "jhaL")


def already(form: Formation) -> Tuple[str, ...]:
    """
    What the affix is marked with in its own right, by 1.3.3 and 1.3.8.

    क्त्वा and the निष्ठा pair carry a क् and are kit before this block says
    anything; तिप् carries a प् and is पित्; लिङ् carries a ङ्. Read, not
    listed — the same `analyze` that finds a root's marks for 1.3.12.
    """
    written = _ATTACHES_AS.get(form.affix, form.affix)
    if form.affix == "niṣṭhā":
        written = "kta"
    elif form.affix == "ktvā":
        written = "ktvā"
    return tuple(sorted(analyze(written, PRATYAYA).it_letters))


# --- the provisions --------------------------------------------------------

K, N = Behaves.KIT, Behaves.NGIT


@dataclass(frozen=True)
class Provision:
    """One sūtra of the block, as conditions rather than as code."""

    sutra: str
    gives: Optional[Behaves] = None
    blocks: Tuple[str, ...] = ()
    roots: Tuple[str, ...] = ()
    gana: Tuple[str, ...] = ()
    affixes: Tuple[str, ...] = ()
    shapes: Tuple[str, ...] = ()
    not_shapes: Tuple[str, ...] = ()
    senses: Tuple[str, ...] = ()
    not_senses: Tuple[str, ...] = ()
    requires: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    #: 1.2.1's अञ्णित् — the affix must not carry any of these marks.
    affix_unmarked: Tuple[str, ...] = ()
    #: A prohibition that does not reach what these provisions already settled.
    #: 1.2.18's is drawn forward past 1.2.7 and 1.2.8 — तस्यायं पुरस्तादपकर्षः.
    yields_to: Tuple[str, ...] = ()
    optional: bool = False
    aprapta: bool = False
    gloss: str = ""
    example: str = ""
    counter: str = ""

    def unmet(self, form: Formation) -> Tuple[str, ...]:
        """Which of this provision's conditions the formation does not satisfy."""
        missing: List[str] = []
        key = root_key(form.root)

        allowed = {root_key(r) for r in self.roots} | set(self.gana)
        if allowed and key not in allowed:
            named = ", ".join(self.roots) if self.roots else "the gaṇa"
            missing.append(f"root is not one of {named}")
        if self.affixes and form.affix not in self.affixes:
            missing.append(f"affix is not {'/'.join(self.affixes)}")
        for shape in self.shapes:
            if shape == "jhalādi":
                if not form.jhaladi:
                    missing.append("affix is not झलादि")
            elif not SHAPES[shape](form.root):
                missing.append(f"root is not {shape}")
        for shape in self.not_shapes:
            if SHAPES[shape](form.root):
                missing.append(f"root is {shape}")
        if self.senses and form.sense not in self.senses:
            missing.append(f"sense is not {'/'.join(self.senses)}")
        if self.not_senses and form.sense in self.not_senses:
            missing.append(f"sense is {form.sense}")
        for mark in self.affix_unmarked:
            if mark in form.marks:
                missing.append(f"affix is {mark}it")
        for condition in self.requires:
            if condition == "pit":
                if not form.pit:
                    missing.append("affix is not पित्")
            elif not form.has(condition):
                missing.append(f"{condition} not stated")
        for condition in self.excludes:
            if condition == "pit":
                if form.pit:
                    missing.append("affix is पित्")
            elif form.has(condition):
                missing.append(f"{condition} is stated")
        return tuple(missing)

    def applies(self, form: Formation) -> bool:
        return not self.unmet(form)

    def describe(self) -> str:
        parts: List[str] = []
        if self.roots:
            parts.append("root ∈ {" + ", ".join(self.roots) + "}")
        if self.gana:
            parts.append(f"root ∈ कुटादि ({len(self.gana)} members)")
        if self.affixes:
            parts.append("affix ∈ {" + ", ".join(self.affixes) + "}")
        parts.extend(self.shapes)
        parts.extend(f"not {s}" for s in self.not_shapes)
        if self.senses:
            parts.append("sense ∈ {" + ", ".join(self.senses) + "}")
        parts.extend(f"sense ≠ {s}" for s in self.not_senses)
        parts.extend(f"affix not {m}it" for m in self.affix_unmarked)
        parts.extend(self.requires)
        parts.extend(f"not {c}" for c in self.excludes)
        if self.blocks:
            head = "cancels " + ", ".join(self.blocks)
        else:
            head = f"behaves as {self.gives.value}"
            if self.optional:
                head = "optionally " + head
        return f"{head} when {'; '.join(parts)}" if parts else head


def _p(*args, **kwargs) -> Provision:
    return Provision(*args, **kwargs)


PROVISIONS: Tuple[Provision, ...] = (
    # --- 1.2.1 to 1.2.4: made to behave as ṅit --------------------------
    _p("1.2.1", gives=N, roots=("gāṅ",), gana=kutadi(),
       affix_unmarked=("ñ", "ṇ"),
       gloss="गाङ्कुटादिभ्योऽञ्णिन्ङित् — after गाङ् or a कुटादि root, an affix "
             "that is neither ञित् nor णित् behaves as ṅit",
       example="adhyagīṣṭa, utkuṭitā, utpuṭitā", counter="utkoṭayati"),
    _p("1.2.1v1", gives=N, roots=("vyac",), not_senses=("anas",),
       gloss="व्यचेः कुटादित्वमनसि (vārt.) — व्यच् counts as a कुटादि root, "
             "except where अनस् is in view",
       example="vicitā, vicitum", counter="uruvyacāḥ"),
    _p("1.2.2", gives=N, roots=("vij",), requires=("seṭ",),
       gloss="विज इट् — after विज्, an affix beginning with इट्",
       example="udvijitā", counter="udvejanam"),
    _p("1.2.3", gives=N, roots=("ūrṇu",), requires=("seṭ",), optional=True,
       aprapta=True,
       gloss="विभाषोर्णोः — after ऊर्णु, optionally",
       example="prorṇuvitā / prorṇavitā", counter="prorṇavanam"),
    _p("1.2.4", gives=N, affixes=("sārvadhātuka",), excludes=("pit",),
       gloss="सार्वधातुकमपित् — a sārvadhātuka affix that is not पित्",
       example="kurutaḥ, kurvanti", counter="karoti"),

    # --- 1.2.5 to 1.2.17: made to behave as kit -------------------------
    _p("1.2.5", gives=K, affixes=("liṭ",), excludes=("pit",),
       shapes=("asaṃyogānta",),
       gloss="असंयोगाल्लिट् कित् — an apit लिट् after a root not ending in a "
             "conjunct",
       example="bibhidatuḥ, bibhiduḥ, ījatuḥ",
       counter="sasraṃse, dadhvaṃse"),
    _p("1.2.6", gives=K, affixes=("liṭ",), roots=("indh", "bhū"),
       gloss="इन्धिभवतिभ्यां च — and after इन्धि and भू, whatever their shape",
       example="samīdhe, babhūva, babhūvitha"),
    _p("1.2.6v1", gives=K, affixes=("liṭ",),
       roots=("śranth", "granth", "danbh", "svañj"), optional=True,
       gloss="श्रन्थिग्रन्थिदम्भिस्वञ्जीनां लिटः कित्त्वम् (vārt.), optionally",
       example="śrethatuḥ, grethatuḥ, debhatuḥ, pariṣasvaje"),
    _p("1.2.7", gives=K, affixes=("ktvā",),
       roots=("mṛḍ", "mṛd", "gudh", "kuṣ", "kliś", "vad", "vas"),
       gloss="मृडमृदगुधकुषक्लिशवदवसः क्त्वा — क्त्वा after these seven",
       example="mṛḍitvā, gudhitvā, uditvā, uṣitvā"),
    _p("1.2.8", gives=K, affixes=("ktvā", "san"),
       roots=("rud", "vid", "muṣ", "grah", "svap", "prach"),
       gloss="रुदविदमुषग्रहिस्वपिप्रच्छः सँश्च — क्त्वा and सन् after these six",
       example="ruditvā, gṛhītvā, suptvā; rurudiṣati, jighṛkṣati, suṣupsati"),
    _p("1.2.9", gives=K, affixes=("san",), shapes=("ik-final", "jhalādi"),
       gloss="इको झल् — a झलादि सन् after a root ending in इक्",
       example="cicīṣati, tuṣṭūṣati, cikīrṣati",
       counter="pipāsati, tiṣṭhāsati, śiśayiṣate"),
    _p("1.2.10", gives=K, affixes=("san",),
       shapes=("ik-then-consonant", "jhalādi"),
       gloss="हलन्ताच्च — and after a consonant next to an इक्, अन्त being read "
             "as समीपवचन",
       example="bibhitsati, bubhutsate",
       counter="yiyakṣate, vivartiṣate"),
    _p("1.2.11", gives=K, affixes=("liṅ", "sic"),
       shapes=("ik-then-consonant", "jhalādi"), requires=("ātmanepada",),
       gloss="लिङ्सिचावात्मनेपदेषु — लिङ् and सिच् in the middle endings",
       example="bhitsīṣṭa, bhutsīṣṭa, abhitta, abuddha",
       counter="yakṣīṣṭa, ceṣīṣṭa, asrākṣīt"),
    _p("1.2.12", gives=K, affixes=("liṅ", "sic"), shapes=("ṛ-final", "jhalādi"),
       requires=("ātmanepada",),
       gloss="उश्च — and after a root ending in ऋ or ॠ",
       example="kṛṣīṣṭa, hṛṣīṣṭa, akṛta, ahṛta", counter="variṣīṣṭa"),
    _p("1.2.13", gives=K, affixes=("liṅ", "sic"), roots=("gam",),
       shapes=("jhalādi",), requires=("ātmanepada",), optional=True,
       gloss="वा गमः — after गम्, optionally",
       example="saṃgaṃsīṣṭa / saṃgasīṣṭa, samagata / samagaṃsta"),
    _p("1.2.14", gives=K, affixes=("sic",), roots=("han",),
       requires=("ātmanepada",),
       gloss="हनः सिच् — सिच् after हन्",
       example="āhata, āhasātām"),
    _p("1.2.15", gives=K, affixes=("sic",), roots=("yam",),
       senses=("gandhana",), requires=("ātmanepada",),
       gloss="यमो गन्धने — सिच् after यम् in the sense of insinuation",
       example="udāyata", counter="udāyaṃsta pādam"),
    _p("1.2.16", gives=K, affixes=("sic",), roots=("yam",),
       senses=("upayamana",), requires=("ātmanepada",), optional=True,
       gloss="विभाषोपयमने — and in the sense of marrying, optionally",
       example="upāyata kanyām / upāyaṃsta kanyām"),
    _p("1.2.17", gives=K, affixes=("sic",),
       roots=("sthā",) + ghu_roots(), requires=("ātmanepada",),
       gloss="स्था घ्वोरिच्च — सिच् after स्था and the घु roots, which also take "
             "इ for their final",
       example="upāsthita, adita, adhita"),

    # --- 1.2.18 to 1.2.26: and here it is denied ------------------------
    _p("1.2.18", blocks=("1.3.8",), affixes=("ktvā",), requires=("seṭ",),
       yields_to=("1.2.7", "1.2.8"),
       gloss="न क्त्वा सेट् — a क्त्वा that takes इट् is not kit after all",
       example="devitvā, vartitvā", counter="kṛtvā, hṛtvā"),
    _p("1.2.19", blocks=("1.3.8",), affixes=("niṣṭhā",), requires=("seṭ",),
       roots=("śī", "svid", "mid", "kṣvid", "dhṛṣ"),
       gloss="निष्ठा शीङ्स्विदिमिदिक्ष्विदिधृषः — nor a seṭ निष्ठा after these five",
       example="śayitaḥ, prasveditaḥ, pradharṣitaḥ", counter="svinnaḥ"),
    _p("1.2.20", blocks=("1.3.8",), affixes=("niṣṭhā",), requires=("seṭ",),
       roots=("mṛṣ",), senses=("titikṣā",),
       gloss="मृषस्तितिक्षायाम् — nor after मृष् in the sense of forbearance",
       example="marṣitaḥ", counter="apamṛṣitaṃ vākyam"),
    _p("1.2.21", gives=K, affixes=("niṣṭhā",), requires=("seṭ",),
       shapes=("u-penult",), senses=("bhāva-ādikarman",), optional=True,
       gloss="उदुपधाद्भावादिकर्मणोरन्यतरस्याम् — optionally, after a root with उ "
             "as its penultimate, in the sense of the action or of its "
             "beginning",
       example="dyutitam / dyotitam, pramuditaḥ / pramoditaḥ",
       counter="likhitam anena"),
    _p("1.2.22", blocks=("1.3.8",), affixes=("niṣṭhā", "ktvā"),
       requires=("seṭ",), roots=("pū",),
       gloss="पूङः क्त्वा च — nor after पूङ्",
       example="pavitaḥ, pavitvā"),
    _p("1.2.23", gives=K, affixes=("ktvā",), requires=("seṭ",),
       shapes=("n-penult", "th-or-ph-final"), optional=True,
       gloss="नोपधात्थफान्ताद्वा — optionally, for a क्त्वा after a root with न् "
             "as penultimate ending in थ् or फ्",
       example="grathitvā / granthitvā, guphitvā / gumphitvā",
       counter="rephitvā, sraṃsitvā"),
    _p("1.2.24", gives=K, affixes=("ktvā",), requires=("seṭ",),
       roots=("vañc", "luñc", "ṛ"), optional=True,
       gloss="वञ्चिलुञ्च्यृतश्च — and after वञ्च्, लुञ्च् and ऋत्, optionally",
       example="vacitvā / vañcitvā, lucitvā / luñcitvā", counter="vaktvā"),
    _p("1.2.25", gives=K, affixes=("ktvā",), requires=("seṭ",),
       roots=("tṛṣ", "mṛṣ", "kṛś"), optional=True,
       gloss="तृषिमृषिकृशेः काश्यपस्य — after these three, optionally, and the "
             "option is Kāśyapa's",
       example="tṛṣitvā / tarṣitvā, mṛṣitvā / marṣitvā"),
    _p("1.2.26", gives=K, affixes=("ktvā", "san"), requires=("seṭ",),
       shapes=("ral-final", "u-or-i-penult", "hal-initial"), optional=True,
       gloss="रलो व्युपधाद्धलादेः संश्च — optionally, for क्त्वा and सन् after a "
             "root that begins with a consonant, ends in a रल्, and has उ or इ "
             "before that",
       example="dyutitvā / dyotitvā, likhitvā / lekhitvā",
       counter="devitvā, vartitvā, eṣitvā, bhuktvā"),
)


# --- resolving -------------------------------------------------------------


@dataclass(frozen=True)
class Verdict:
    """What the affix behaves as, by which sūtra, and on what ground."""

    behaves: Tuple[str, ...]
    by: str
    why: str
    optional: bool = False
    blocked: Tuple[str, ...] = ()
    already_marked: Tuple[str, ...] = ()


def resolve(form: Formation) -> Verdict:
    """
    What this affix behaves as after this root.

    The order is the corpus's own typing of the three runs. What the affix is
    marked with in its own right comes first, because 1.2.18 onwards can only
    deny something that was there; then the atideśas of 1.2.1–1.2.17; then the
    denials, which the Kāśikā is careful to say do not reach what 1.2.7 and
    1.2.8 have already settled — तस्यायं पुरस्तादपकर्षः.
    """
    marked = already(form)
    matched = [p for p in PROVISIONS if p.applies(form)]

    ngit = [p for p in matched if p.gives is N]
    kit = [p for p in matched if p.gives is K]
    denials = [p for p in matched if p.blocks]

    # The prohibitions of 1.2.18 onwards reach the kit-ness only, and not what
    # 1.2.7 and 1.2.8 have already settled — तस्यायं पुरस्तादपकर्षः.
    settled = {p.sutra for p in kit}
    denials = [
        p for p in denials
        if not any(earlier in settled for earlier in p.yields_to)
    ]

    behaves: List[str] = []
    reasons: List[str] = []
    by: List[str] = []
    optional = False

    if ngit:
        chosen = max(drop_aprapta(ngit), key=lambda p: order_of(p.sutra))
        behaves.append("ṅit")
        by.append(chosen.sutra)
        reasons.append(chosen.gloss)
        optional = optional or chosen.optional
    elif "ṅ" in marked:
        behaves.append("ṅit")
        by.append("1.3.3")
        reasons.append("हलन्त्यम् — the affix carries an indicatory ङ् of its own")

    # नित्यविकल्पयोर् नित्यो बलीयान् — where a grant is invariable and another
    # only optional, the invariable one stands. That is the whole point of
    # naming गुध, कुष and क्लिश in 1.2.7 and रुद्, विद् and मुष् in 1.2.8: all
    # six satisfy 1.2.26's shape conditions and would otherwise have had the
    # kit-ness by option only — नित्यार्थं वचनम्.
    if kit and any(not p.optional for p in kit):
        kit = [p for p in kit if not p.optional]

    strongest = max(kit, key=lambda p: order_of(p.sutra)) if kit else None
    denial = (max(denials, key=lambda p: order_of(p.sutra))
              if denials else None)

    # A denial reaches only what stands before it. 1.2.18 cannot touch a grant
    # made later, and the optional grants of 1.2.23–1.2.26 are all later.
    if denial and strongest and order_of(strongest.sutra) > order_of(denial.sutra):
        denial = None

    if strongest is not None:
        behaves.append("kit")
        by.append(strongest.sutra)
        reasons.append(strongest.gloss)
        optional = optional or strongest.optional
    elif denial is not None and ("k" in marked):
        by.append(denial.sutra)
        reasons.append(denial.gloss)
    elif "k" in marked:
        behaves.append("kit")
        by.append("1.3.8")
        reasons.append(
            "लशक्वतद्धिते — the affix carries an indicatory क् of its own, and "
            "nothing in 1.2.18–1.2.26 withdraws it here"
        )

    if not by:
        return Verdict(
            (), "—",
            "Neither marked nor made to behave as marked, so 1.1.5 क्ङिति च "
            "does not block guṇa here.",
            already_marked=marked,
        )
    return Verdict(
        tuple(behaves), " + ".join(dict.fromkeys(by)), "; ".join(reasons),
        optional=optional,
        blocked=tuple(sorted({p.sutra for p in denials})),
        already_marked=marked,
    )


def behaves_as(
    root: str,
    affix: str,
    *,
    ending: Optional[str] = None,
    artha: Optional[str] = None,
    sense: Optional[str] = None,
    given: Sequence[str] = (),
) -> Verdict:
    """What an affix behaves as after a root — the whole of 1.2.1–1.2.26."""
    return resolve(Formation(
        root=root, affix=affix, ending=ending, artha=artha, sense=sense,
        given=tuple(given),
    ))


def near_misses(form: Formation) -> Tuple[Tuple[str, Tuple[str, ...]], ...]:
    """Provisions that would have fired but for one condition."""
    return tuple(
        (p.sutra, unmet) for p in PROVISIONS
        if len(unmet := p.unmet(form)) == 1
    )


def provisions_for(sutra: str) -> Tuple[Provision, ...]:
    """Every provision one sūtra contributes — some contribute two."""
    return tuple(
        p for p in PROVISIONS
        if p.sutra == sutra or p.sutra.startswith(sutra + "v")
        or p.sutra.startswith(sutra + "niyama")
    )


__all__ = [
    "Behaves",
    "CONDITIONS",
    "Formation",
    "PROVISIONS",
    "Provision",
    "SENSES",
    "SHAPES",
    "Verdict",
    "already",
    "behaves_as",
    "kutadi",
    "near_misses",
    "provisions_for",
    "resolve",
]
