# -*- coding: utf-8 -*-
"""
आदेश — substitution: who is replaced, by what, and where.

Four paribhāṣās govern every replacement in the grammar, and they answer four
different questions about one operation:

    1.1.49  षष्ठी स्थानेयोगा     a genitive in a rule marks what is replaced
    1.1.50  स्थानेऽन्तरतमः       of the candidates, the nearest is chosen
    1.1.51  उरण् रपरः            an aṆ replacing ṛ is followed by r
    1.1.52  अलोऽन्त्यस्य         the substitute takes the last sound, not all

1.1.50 is the one with real content, and the Kāśikā supplies both the criteria
and the arithmetic. It asks कुतश्च शब्दस्यान्तर्यम्? and answers
स्थानार्थगुणप्रमाणतः — nearness is reckoned from place, meaning, quality and
measure — then ranks them: यत्रानेकमान्तर्यं संभवति तत्र स्थानत एवान्तर्यं
बलीयो, where several kinds of nearness are available, nearness by place is the
strongest.

Three of the four dimensions are implemented. अर्थतः, nearness of meaning, is
not: its example is पुंवद्भाव in वातण्ड्ययुवतिः, which needs a semantics this
project does not have. It is left out rather than faked, and `Nearness` says so.

The features all come from src/astadhyayi/varna.py — place from the Śikṣā's own
compounds, quality from the bāhya prayatnas, measure from the prosody engine's
vowel tables through grahana.kala. Nothing phonetic is restated here.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, Optional, Sequence, Tuple

from src.chandas.core import scan_phonemes
from src.astadhyayi.grahana import AN, kala
from src.astadhyayi.sources import facts
from src.astadhyayi.varna import VOWEL_VARNA, varna


# ---------------------------------------------------------------------------
# 1.1.49 षष्ठी स्थानेयोगा — reading a rule's case marking
# ---------------------------------------------------------------------------

SASTHI = 6
PANCAMI = 5


def sthanin_padas(sutra_id: str) -> Tuple[str, ...]:
    """
    1.1.49: the words of a sūtra that stand in the sixth case, which is to say
    the words naming what a substitution replaces.

    परिभाषेयं योगनियमार्था — the paribhāṣā restricts, it does not add. The
    genitive has many senses (बहवो हि षष्ठ्यर्थाः स्वस्वाम्यनन्तरसमीपसमूह-
    विकारावयवाद्याः, the Kāśikā lists ownership, proximity, aggregate, part and
    more); this rule says that in the śāstra an otherwise unassigned genitive is
    always the स्थाने sense, "in the room of".

    The case marking is read from the corpus, which records vibhakti and vacana
    for every pada of every sūtra. That is the whole codification: the rule is a
    convention about how to read the text, so applying it is reading the text.
    """
    return tuple(
        pada.word for pada in facts(sutra_id).padas if pada.vibhakti == SASTHI
    )


def pancami_padas(sutra_id: str) -> Tuple[str, ...]:
    """
    The words of a sūtra standing in the fifth case.

    1.1.54 turns on this: क्व च परस्य कार्यं शिष्यते? यत्र पञ्चमीनिर्देशः —
    "where is an operation taught on what follows? where there is a statement in
    the fifth case." So the trigger is a fact about the text, and is read from
    the text rather than supplied by a caller.
    """
    return tuple(
        pada.word for pada in facts(sutra_id).padas if pada.vibhakti == PANCAMI
    )


# ---------------------------------------------------------------------------
# 1.1.50 स्थानेऽन्तरतमः — the nearest candidate
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Nearness:
    """
    How near one candidate stands to the sthānin, dimension by dimension.

    Each dimension counts what is shared and what is not. Counting matters
    rather than merely matching, because the sūtra says अन्तरतम and not अन्तर:
    the Kāśikā draws the superlative out at तमब्ग्रहणं किम्? — for h after a
    jhaY, being सोष्मन् suggests the aspirate and being नादवत् suggests the
    voiced, and it is the fourth of the varga that wins by being both.
    """

    candidate: str
    #: Articulators shared with the sthānin, and articulators not shared.
    sthana_shared: int
    sthana_apart: int
    #: External qualities shared and not shared — the Kāśikā's गुणतः.
    guna_shared: int
    guna_apart: int
    #: Same duration — प्रमाणतः.
    pramana: bool

    #: अर्थतः is not represented. See the module docstring.
    artha: None = None

    @property
    def key(self) -> Tuple[int, int, int, int, int]:
        """
        The ranking. Place first and by itself, because स्थानत एवान्तर्यं
        बलीयः; then quality; then measure.
        """
        return (
            self.sthana_shared,
            -self.sthana_apart,
            self.guna_shared,
            -self.guna_apart,
            int(self.pramana),
        )


def nearness(sthanin: str, candidate: str) -> Optional[Nearness]:
    """How near `candidate` is to `sthanin`, or None if either is unknown."""
    a, b = varna(sthanin), varna(candidate)
    if a is None or b is None:
        return None
    places_a, places_b = a.places, b.places
    guna_a, guna_b = a.bahya, b.bahya
    return Nearness(
        candidate=candidate,
        sthana_shared=len(places_a & places_b),
        sthana_apart=len(places_a ^ places_b),
        guna_shared=len(guna_a & guna_b),
        guna_apart=len(guna_a ^ guna_b),
        pramana=kala(sthanin) == kala(candidate),
    )


def antaratama(sthanin: str, candidates: Sequence[str]) -> Tuple[str, ...]:
    """
    1.1.50: of the substitutes a rule makes available, the nearest.

    Returns every candidate tied at the top rather than picking one, because a
    genuine tie is a fact about the grammar and silently breaking it would hide
    a place where some further provision is needed. 1.1.51 exists for exactly
    such a case: ṛ shares no articulator with any of a, e, o.
    """
    scored = [
        (score.key, score.candidate)
        for score in (nearness(sthanin, c) for c in candidates)
        if score is not None
    ]
    if not scored:
        return ()
    best = max(key for key, _ in scored)
    return tuple(name for key, name in scored if key == best)


def ranked(sthanin: str, candidates: Sequence[str]) -> Tuple[Nearness, ...]:
    """The same comparison, kept in full so a choice can be explained."""
    scores = [
        score
        for score in (nearness(sthanin, c) for c in candidates)
        if score is not None
    ]
    return tuple(sorted(scores, key=lambda s: s.key, reverse=True))


# ---------------------------------------------------------------------------
# 1.1.51 उरण् रपरः — the r that follows a substitute for ṛ
# ---------------------------------------------------------------------------

RVARNA: frozenset = frozenset(VOWEL_VARNA["ṛ"])

#: The ḷ-varṇa, which the vārttika लपर इति वक्तव्यम् brings under this sūtra
#: with l in place of r. See `raparatva`.
LVARNA: frozenset = frozenset(VOWEL_VARNA["ḷ"])


def raparatva(sthanin: str, substitute: str, *, varttika: bool = True) -> str:
    """
    1.1.51: उः स्थानेऽण् प्रसज्यमान एव रपरो वेदितव्यः — an aṆ arising in the
    room of ṛ is to be understood as having r after it.

    Both conditions of the sūtra are tested, because the Kāśikā tests both.
    उरिति किम्? खेयम्। गेयम् — the rule wants ṛ specifically, not any vowel.
    अण्ग्रहणं किम्? सुधातुरकङ् च (4.1.97) सौधातकिः — the substitute must be an
    aṆ, and where a whole affix replaces ṛ no r is added.

    ḷ is handled by Kātyāyana rather than by Pāṇini here. The sūtra says उः,
    which the Kāśikā glosses as ṛ alone, and the vārttika on this sūtra reads
    लपर इति वक्तव्यम् — "it should be stated: l-para". So the ḷ-varṇa takes l
    where the ṛ-varṇa takes r, giving अल् and आल् beside अर् and आर्.
    `varttika=False` drops that, so a test can show the addition changes an
    answer rather than restating one.
    """
    if substitute not in AN:
        return substitute
    if sthanin in RVARNA:
        return substitute + "r"
    if varttika and sthanin in LVARNA:
        return substitute + "l"
    return substitute


# ---------------------------------------------------------------------------
# 1.1.52 अलोऽन्त्यस्य — where the substitute lands
# ---------------------------------------------------------------------------


def antya(text: str) -> Optional[str]:
    """The last sound of a form. Segmentation is the prosody engine's."""
    phonemes = scan_phonemes(text)
    return phonemes[-1].text if phonemes else None


def replace_antya(text: str, substitute: str) -> str:
    """
    1.1.52: षष्ठीनिर्दिष्टस्य य उच्यत आदेशः, सोऽन्त्यस्यालः स्थाने वेदितव्यः —
    a substitute stated for something named in the genitive takes the place of
    its last sound, not of the whole.

    The Kāśikā's example is 1.2.50 इद् गोण्याः: गोणी with i gives पञ्चगोणिः, the
    i replacing only the final ī. Without this rule the whole stem would go.

    This is the default, and it has three companions. Call
    `substitution_site` or `apply_adesa` to have the four weighed together;
    this function is the 1.1.52 branch on its own.
    """
    phonemes = scan_phonemes(text)
    if not phonemes:
        return substitute
    last = phonemes[-1]
    return text[: last.start] + substitute


# ---------------------------------------------------------------------------
# Where a substitute lands — 1.1.52 to 1.1.55 as one decision
# ---------------------------------------------------------------------------


class Site(Enum):
    """The three places a substitute can take."""

    ANTYA = "antyasya"          # the last sound
    ADI = "ādeḥ parasya"        # the first sound of what follows
    SARVA = "sarvasya"          # the whole


@dataclass(frozen=True)
class Adesa:
    """
    A substitute, with its it-letters kept apart from its sounds.

    The it-letters are kept apart from the sounds because they behave
    differently: they condition rules and then vanish, and counting them as
    sounds would make शि anekāl.

    They can be supplied directly or derived. `Adesa.from_upadesa` runs
    1.3.2–1.3.9 over an enunciated form and fills the field, which is what
    those sūtras are for; the explicit constructor stays because a caller who
    already knows the analysis should not have to round-trip through a string.
    """

    form: str
    its: FrozenSet[str] = frozenset()

    @classmethod
    def from_upadesa(cls, text: str, context=None) -> "Adesa":
        """
        Read the it-letters off an enunciated substitute, by 1.3.2–1.3.9.

        This is what the docstring above used to say could not be done. It can
        now: `itsamjna.analyze` decides which letters are indicatory and which
        are not, so शि is śit and शस् is not without anyone having to say so.

        One caveat survives, and it is about the form rather than the marks.
        The it-rules do not remove the vowel that makes a consonant-final
        anubandha pronounceable, so आनङ् yields आन and not आन्. That vowel is
        उच्चारणार्थ and belongs to no sūtra codified here. Where it matters,
        construct the Adesa directly with the form you mean.
        """
        from src.astadhyayi.itsamjna import PLAIN, analyze

        parsed = analyze(text, context or PLAIN)
        return cls(form=parsed.stem, its=parsed.it_letters)

    @property
    def anekal(self) -> bool:
        """अनेकाल् — more than one sound. Counted by the prosody scanner."""
        return len(scan_phonemes(self.form)) > 1

    @property
    def ngit(self) -> bool:
        return "ṅ" in self.its

    @property
    def sit(self) -> bool:
        return "ś" in self.its


@dataclass(frozen=True)
class SiteDecision:
    """Where the substitute lands, and which sūtra put it there."""

    site: Site
    by: str
    why: str


def substitution_site(adesa: Adesa, *, pancami: bool = False) -> SiteDecision:
    """
    Which of the four rules governs this substitution.

    The order is the order of the exceptions, and 1.1.53 has to be tested
    before 1.1.55 or it would never fire — its whole purpose is to rescue
    substitutes that are anekāl and would otherwise be swept up by 1.1.55.
    आनङ् is both, and the Kāśikā says so outright: ङिच्च य आदेशः, सोऽनेकालपि
    अलोऽन्त्यस्य स्थाने भवति — "a ṅit substitute, though it be anekāl, takes
    the place of the last sound."
    """
    if pancami:
        return SiteDecision(
            Site.ADI, "1.1.54",
            "पञ्चमीनिर्देश — the rule speaks of what follows, so the first "
            "sound of it is affected",
        )
    if adesa.ngit:
        return SiteDecision(
            Site.ANTYA, "1.1.53",
            "ङित् — the last sound only, अनेकालपि, even though it is more "
            "than one sound",
        )
    if adesa.anekal or adesa.sit:
        reason = "अनेकाल्" if adesa.anekal else "शित्"
        return SiteDecision(
            Site.SARVA, "1.1.55", f"{reason} — the whole is replaced"
        )
    return SiteDecision(
        Site.ANTYA, "1.1.52", "अलोऽन्त्यस्य — the default, the last sound"
    )


def site_for(sutra_id: str, adesa: Adesa) -> SiteDecision:
    """The same decision, taking the pañcamī from the sūtra's own wording."""
    return substitution_site(adesa, pancami=bool(pancami_padas(sutra_id)))


def replace_adi(text: str, substitute: str) -> str:
    """1.1.54: the substitute takes the place of the first sound."""
    phonemes = scan_phonemes(text)
    if not phonemes:
        return substitute
    first = phonemes[0]
    return substitute + text[first.start + len(first.text):]


def apply_adesa(
    text: str, adesa: Adesa, decision: Optional[SiteDecision] = None
) -> str:
    """Carry out the substitution at the site the paribhāṣās choose."""
    decision = decision or substitution_site(adesa)
    if decision.site is Site.SARVA:
        return adesa.form
    if decision.site is Site.ADI:
        return replace_adi(text, adesa.form)
    return replace_antya(text, adesa.form)


# ---------------------------------------------------------------------------
# The payoff: guṇa and vṛddhi substitution, composed
# ---------------------------------------------------------------------------


def _substitute_for(sthanin: str, candidates: Sequence[str]) -> Optional[str]:
    chosen = antaratama(sthanin, candidates)
    if len(chosen) != 1:
        # A tie. For ṛ this is expected and 1.1.51 resolves it; the caller
        # decides, and gets None rather than an arbitrary pick.
        return None
    return chosen[0]


def _guna_vrddhi(vowel: str, candidates: Sequence[str]) -> Optional[str]:
    """
    1.1.50 picks, then 1.1.51 finishes. ṛ is not special-cased: it shares no
    articulator with a, e or o, but it stands two articulators away from a and
    three from each of e and o, so अन्तरतम selects a on its own. 1.1.51 then
    supplies the r, which is exactly the division of labour the two sūtras
    describe — उः स्थानेऽण् प्रसज्यमान एव रपरो, "an aṆ *arising* in the room of
    ṛ", takes as given that something else produced it.
    """
    chosen = _substitute_for(vowel, candidates)
    if chosen is None:
        return None
    return raparatva(vowel, chosen)


def guna_of(vowel: str) -> Optional[str]:
    """
    The guṇa substitute for an iK vowel — 1.1.3 naming the target, 1.1.2 the
    candidates, 1.1.50 choosing among them, 1.1.51 finishing the ṛ case.

    This is what the note on 1.1.3 deferred. The Kāśikā on 1.1.50 gives the
    working: चेता। स्तोता। प्रमाणतोऽकारो गुणः प्राप्तः, तत्र स्थानत
    आन्तर्यादेकारौकारौ भवतः — by measure `a` would have been the guṇa of i, but
    place is stronger and yields e.

    ḷ comes out a and ā, without the l the tradition gives it (अल्, आल्). The
    vowel is right and is reached the same way ṛ's is; the l is supplied by a
    vārttika on 1.1.51 that is not codified here, since 1.1.51 as it stands says
    उः and the Kāśikā glosses only ṛ. Recorded rather than patched in.
    """
    from src.astadhyayi.rules.adhyaya_1_pada_1 import GUNA

    return _guna_vrddhi(vowel, GUNA)


def vrddhi_of(vowel: str) -> Optional[str]:
    """The vṛddhi substitute, by the same composition."""
    from src.astadhyayi.rules.adhyaya_1_pada_1 import VRDDHI

    return _guna_vrddhi(vowel, VRDDHI)


def sthanin_is_rvarna(sound: str) -> bool:
    return sound in RVARNA


# ---------------------------------------------------------------------------
# Parts of a form — 1.1.64 ṭi, 1.1.65 upadhā
# ---------------------------------------------------------------------------
#
# Two saṃjñās naming stretches of a form by position. They belong here because
# they exist to be operated on: 3.4.79 टित आत्मनेपदानां टेरे replaces the ṭi,
# 7.2.116 अत उपधायाः lengthens the upadhā.


def ti(text: str) -> str:
    """
    1.1.64 अचोऽन्त्यादि टि — from the last vowel to the end.

    अचां संनिविष्टानां योऽन्त्योऽच्, तदादि शब्दरूपं टिसंज्ञं भवति: of the vowels
    present, the last one, and what begins with it. The Kāśikā's examples are
    अग्निचित् giving इत्, सोमसुत् giving उत्, and आताम्/आथाम् giving आम्.

    Returns "" for a form with no vowel, which is not a ṭi but the absence of
    one.
    """
    phonemes = scan_phonemes(text)
    for phoneme in reversed(phonemes):
        if phoneme.kind == "vowel":
            return text[phoneme.start:]
    return ""


def upadha(text: str) -> Optional[str]:
    """
    1.1.65 अलोऽन्त्यात् पूर्व उपधा — the sound before the last.

    अन्त्यादलः पूर्वो यो वर्णः, सोऽलेवोपधासंज्ञो भवति. A single sound, and the
    Kāśikā is explicit that it is a sound and not everything preceding:
    अल इति किम्? शिष्टः। शिष्टवान्। समुदायात् पूर्वस्य मा भूत् — "so that it
    should not be of the whole aggregate before it."

    Its examples are the penultimate of a root: पच्, पठ् give a; भिद्, छिद्
    give i; बुध्, युध् give u; वृत्, वृध् give ṛ. Returns None where there is
    no sound before the last.
    """
    phonemes = scan_phonemes(text)
    if len(phonemes) < 2:
        return None
    return phonemes[-2].text


# ---------------------------------------------------------------------------
# Which side a case-marked rule operates on — 1.1.49, 1.1.66, 1.1.67
# ---------------------------------------------------------------------------

PRATHAMA = 1
SAPTAMI = 7


class Side(Enum):
    """What a rule's case marking says its operation falls on."""

    IN_PLACE_OF = "sthāne"      # 1.1.49, the sixth
    PRECEDING = "pūrvasya"      # 1.1.66, the seventh
    FOLLOWING = "uttarasya"     # 1.1.67, the fifth
    UPASARJANA = "upasarjana"   # 1.2.43, the first — in a compound rule only


@dataclass(frozen=True)
class Nirdesa:
    """One case-marked word, and what it therefore points at."""

    word: str
    vibhakti: int
    side: Side
    by: str


def prathama_padas(sutra_id: str) -> Tuple[str, ...]:
    """
    The words of a sūtra standing in the first case.

    1.2.43 प्रथमानिर्दिष्टं समास उपसर्जनम् reads them, but only in a rule that
    makes a compound — समास इति समासविधायि शास्त्रं गृह्यते — so unlike the
    other three case-paribhāṣās this one cannot be applied to a sūtra without
    knowing what kind of sūtra it is.
    """
    return tuple(
        pada.word for pada in facts(sutra_id).padas if pada.vibhakti == PRATHAMA
    )


def saptami_padas(sutra_id: str) -> Tuple[str, ...]:
    """The words of a sūtra standing in the seventh case."""
    return tuple(
        pada.word for pada in facts(sutra_id).padas if pada.vibhakti == SAPTAMI
    )


def nirdesa(
    sutra_id: str, *, samasa_vidhi: bool = False
) -> Tuple[Nirdesa, ...]:
    """
    How to read each case-marked word of a sūtra — the three paribhāṣās at once.

    Pāṇini fixes a reading for each of four cases, and between them they say
    where an operation lands relative to the thing named:

        1.1.49  षष्ठी स्थानेयोगा            sixth   — in the room of it
        1.1.66  तस्मिन्निति निर्दिष्टे पूर्वस्य  seventh — on what precedes it
        1.1.67  तस्मादित्युत्तरस्य          fifth   — on what follows it
        1.2.43  प्रथमानिर्दिष्टं समास उपसर्जनम्  first — the upasarjana, but
                                              only in a rule making a compound

    The fourth is conditioned and the other three are not, which is why
    `samasa_vidhi` has to be passed: समास इति समासविधायि शास्त्रं गृह्यते, the
    word समास means a rule that MAKES a compound, so a first-case word in any
    other sūtra is not an upasarjana.

    The corpus records vibhakti for every pada of all 3,983 sūtras, so this
    reads the grammar's own marking rather than being told. 1.1.66's example is
    6.1.77 इको यणचि, where अचि is seventh and the substitution falls on the
    preceding iK: दधि + उदकम् gives दध्युदकम्. 1.1.67's is 8.1.28 तिङ्ङतिङः,
    where अतिङः is fifth and the accent falls on the tiṅ that follows:
    ओदनं पचति, and not on पचति in पचत्योदनम्.
    """
    out = []
    for pada in facts(sutra_id).padas:
        if samasa_vidhi and pada.vibhakti == PRATHAMA:
            out.append(
                Nirdesa(pada.word, PRATHAMA, Side.UPASARJANA, "1.2.43")
            )
        elif pada.vibhakti == SASTHI:
            out.append(Nirdesa(pada.word, SASTHI, Side.IN_PLACE_OF, "1.1.49"))
        elif pada.vibhakti == SAPTAMI:
            out.append(Nirdesa(pada.word, SAPTAMI, Side.PRECEDING, "1.1.66"))
        elif pada.vibhakti == PANCAMI:
            out.append(Nirdesa(pada.word, PANCAMI, Side.FOLLOWING, "1.1.67"))
    return tuple(out)


def operates_on(sutra_id: str) -> Tuple[Side, ...]:
    """The sides a sūtra's case marking points to, in order of its words."""
    return tuple(item.side for item in nirdesa(sutra_id))


# ---------------------------------------------------------------------------
# 1.1.45 सम्प्रसारण, 1.1.46–1.1.47 where an āgama goes, 1.1.48 the short of eC
# ---------------------------------------------------------------------------


def samprasarana(before: str, after: str) -> bool:
    """
    1.1.45 इग्यणः सम्प्रसारणम् — an iK standing in the room of a yaṆ.

    इग्यो यणः स्थाने भूतो भावी वा — an iK that has come to stand there or is
    about to. The Kāśikā's examples are the three commonest: यज् gives इष्टम्,
    वप् gives उप्तम्, ग्रह् gives गृहीतम्, where y, v and r have given way to
    i, u and ṛ.

    The name is of the relation and not of the sound alone. The Kāśikā records
    a difference over that — केचिदुभयथा सूत्रमिदं व्याचक्षते, some explain it
    both ways, as naming the whole substitution or naming the vowel — and the
    two arguments are taken here, which is the first reading.
    """
    from src.astadhyayi.sivasutra import resolve

    return before in resolve("yaṆ").sounds and after in resolve("iK").sounds


class AgamaSite(Enum):
    """Where an augment attaches."""

    ADI = "ādi"                  # before — 1.1.46, ṭit
    ANTA = "anta"                # after — 1.1.46, kit
    AFTER_LAST_VOWEL = "mit"     # 1.1.47


def agama_site(its) -> "Optional[AgamaSite]":
    """
    1.1.46 आद्यन्तौ टकितौ and 1.1.47 मिदचोऽन्त्यात्परः — where an augment goes.

    आदिष्टिद् भवति अन्तःकिद् भवति षष्ठीनिर्दिष्टस्य: a ṭit augment is the
    beginning of what the genitive named, a kit augment its end. A mit augment
    goes after the last vowel instead — अचां संनिविष्टानामन्त्यादचः परो मिद्
    भवति, and the Kāśikā notes that this overrides the default that an affix
    follows: स्थानेयोगप्रत्ययपरत्वस्य अयमपवादः.

    The marks are read off the augment by 1.3.2–1.3.9, so इट् at 7.2.35 is ṭit
    and सुक् at 7.3.40 is kit without either being declared.
    """
    if "m" in its:
        return AgamaSite.AFTER_LAST_VOWEL     # 1.1.47
    if "ṭ" in its:
        return AgamaSite.ADI                  # 1.1.46
    if "k" in its:
        return AgamaSite.ANTA                 # 1.1.46
    return None


def insert_agama(text: str, agama: str, site: "AgamaSite") -> str:
    """Place an augment at the site the paribhāṣās choose."""
    if site is AgamaSite.ADI:
        return agama + text
    if site is AgamaSite.ANTA:
        return text + agama
    phonemes = scan_phonemes(text)
    for phoneme in reversed(phonemes):
        if phoneme.kind == "vowel":
            cut = phoneme.start + len(phoneme.text)
            return text[:cut] + agama + text[cut:]
    return text + agama


def hrasva_of_ec(vowel: str) -> Optional[str]:
    """
    1.1.48 एच इग्घ्रस्वादेशे — where a short substitute is wanted for an eC,
    it is an iK and nothing else.

    इगेव ह्रस्वो भवति नान्यः. Which iK is not stated, and does not need to be:
    1.1.50 settles it, and the answers are the Kāśikā's own — रै gives अतिरि,
    नौ gives अतिनु, गो gives उपगु. So this is 1.1.50 restricted to a class,
    and is computed rather than tabulated.

    एच इति किम्? अतिखट्वः, अतिमालः — the rule is for the diphthongs only.
    ह्रस्वादेशे इति किम्? देवदत्त — where no short substitute is called for,
    nothing happens.
    """
    from src.astadhyayi.sivasutra import resolve

    if vowel not in resolve("eC").sounds:
        return None
    chosen = antaratama(vowel, list(resolve("iK").sounds))
    return chosen[0] if len(chosen) == 1 else None


# ---------------------------------------------------------------------------
# When guṇa and vṛddhi do NOT happen — 1.1.4 to 1.1.6
# ---------------------------------------------------------------------------
#
# Three prohibitions, all reading इकः and गुणवृद्धी down from 1.1.3 and न down
# from 1.1.4, so all three are about the same operation the last section
# computes. Their conditions are of three different kinds — one about what the
# affix does to the root, one about how the affix is marked, one about which
# item is in hand — which is why they are three sūtras and not one.


@dataclass(frozen=True)
class Blocked:
    """A prohibition that fired, and the sūtra it came from."""

    by: str
    why: str


#: 1.1.5 क्ङिति च. The Kāśikā adds g to the two: गकारोऽप्यत्र चर्त्वभूतो
#: निर्दिश्यते, the g too is indicated here as a cartva-form — so a git affix
#: is caught along with kit and ṅit.
KNIT: FrozenSet[str] = frozenset({"k", "ṅ", "g"})

#: 1.1.6 दीधीवेवीटाम्. Three named items, not a class: the roots दीधी and वेवी
#: and the augment इट्.
DIDHI_VEVI_IT: Tuple[str, ...] = ("dīdhī", "vevī", "iṭ")


def hrasva_of(vowel: str) -> Optional[str]:
    """
    The short counterpart of a vowel, or None where there is none.

    Not a table. The diphthongs go to 1.1.48 एच इग्घ्रस्वादेशे, which reads
    इक् through 1.1.50 and gives रै → रि, नौ → नु, गो → गु. Everything else
    is the savarṇa (1.1.9) that measures one mātrā (1.2.27) — the same two
    rules `grahana` already leans on for 1.1.70's tapara. And where that
    leaves a choice, 1.1.50 आन्तर्यतः breaks it: ṝ is savarṇa with both ṛ
    and ḷ, and the nearest is ṛ.

    A vowel already short is returned unchanged, so a caller can ask
    without first testing.
    """
    from src.astadhyayi.svara import duration
    from src.astadhyayi.varna import savarnas_of

    if duration(vowel) is None:
        return None
    if duration(vowel) == 1:
        return vowel

    by_ec = hrasva_of_ec(vowel)
    if by_ec is not None:
        return by_ec

    short = [s for s in savarnas_of(vowel) if duration(s) == 1]
    if not short:
        return None
    if len(short) == 1:
        return short[0]
    nearest = antaratama(vowel, short)
    return nearest[0] if len(nearest) == 1 else None


def guna_vrddhi_blocked(
    target: str,
    *,
    affix: Optional["Adesa"] = None,
    ardhadhatuka: bool = False,
    dhatu_lopa: bool = False,
    item: str = "",
) -> Optional[Blocked]:
    """
    Whether 1.1.4, 1.1.5 or 1.1.6 stops guṇa or vṛddhi here.

    All three inherit इकः from 1.1.3, and the Kāśikā insists on it under each —
    इक इत्येव: अभाजि, रागः under 1.1.4, कामयते under 1.1.5. So a target outside
    iK is not blocked, because there was nothing to block.

    Returns the prohibition that fired, or None if the operation proceeds.
    """
    from src.astadhyayi.rules.adhyaya_1_pada_1 import is_ik

    if not is_ik(target):
        return None

    # 1.1.4 न धातुलोप आर्धधातुके
    if dhatu_lopa and ardhadhatuka:
        return Blocked(
            "1.1.4",
            "धातुलोपे आर्धधातुके — the ārdhadhātuka has elided part of the "
            "root, so the guṇa or vṛddhi it would have caused does not "
            "happen: लोलुवः, पोपुवः, मरीमृजः",
        )

    # 1.1.5 क्ङिति च
    if affix is not None and (affix.its & KNIT):
        marks = ", ".join(sorted(affix.its & KNIT))
        return Blocked(
            "1.1.5",
            f"क्ङिति च — the affix is marked with {marks}, and this is a "
            f"निमित्तसप्तमी, a locative of cause: चितः, स्तुतः, भिन्नः",
        )

    # 1.1.6 दीधीवेवीटाम्
    if item in DIDHI_VEVI_IT:
        return Blocked(
            "1.1.6",
            f"दीधीवेवीटाम् — {item} is one of the three named: आदीध्यनम्, "
            f"आवेव्यनम्, कणिता श्वः",
        )
    return None


def guna_or_none(target: str, **conditions) -> Optional[str]:
    """
    The guṇa of a vowel in a stated environment, or None if a sūtra forbids it.

    The whole chain in one call: 1.1.3 fixes the class, 1.1.2 the candidates,
    1.1.50 the choice, 1.1.51 the r, and 1.1.4–1.1.6 the veto.
    """
    if guna_vrddhi_blocked(target, **conditions):
        return None
    return guna_of(target)


def vrddhi_or_none(target: str, **conditions) -> Optional[str]:
    """The same for vṛddhi."""
    if guna_vrddhi_blocked(target, **conditions):
        return None
    return vrddhi_of(target)


__all__ = [
    "Adesa",
    "AgamaSite",
    "Nirdesa",
    "SAPTAMI",
    "Side",
    "Blocked",
    "DIDHI_VEVI_IT",
    "KNIT",
    "Nearness",
    "PANCAMI",
    "PRATHAMA",
    "Site",
    "SiteDecision",
    "LVARNA",
    "RVARNA",
    "SASTHI",
    "antaratama",
    "agama_site",
    "antya",
    "apply_adesa",
    "guna_of",
    "hrasva_of", "hrasva_of_ec",
    "insert_agama",
    "guna_or_none",
    "guna_vrddhi_blocked",
    "nearness",
    "nirdesa",
    "operates_on",
    "pancami_padas",
    "prathama_padas",
    "ranked",
    "samprasarana",
    "saptami_padas",
    "replace_adi",
    "raparatva",
    "replace_antya",
    "site_for",
    "sthanin_is_rvarna",
    "sthanin_padas",
    "ti",
    "substitution_site",
    "upadha",
    "vrddhi_of",
    "vrddhi_or_none",
]
