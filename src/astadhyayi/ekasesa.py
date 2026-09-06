# -*- coding: utf-8 -*-
"""
वचन and एकशेष — 1.2.58 to 1.2.73.

Two questions, and the pāda ends on them. First, when may a number be used
that does not match what is being counted: a plural for one thing, a plural
for two. Then the larger one — when several words are coordinated, which of
them survives and which drop away.

    1.2.58 – 1.2.63   बहुवचनम्, द्विवचनम्, एकवचनम् where they do not fit
    1.2.64 – 1.2.73   एकशेष: एकः शिष्यते, इतरे निवर्तन्ते

The Mahābhāṣya's reason for एकशेष is worth having, because it explains why the
rule is needed rather than merely what it does: प्रत्यर्थं शब्दनिवेशाद्
नैकेनानेकस्याभिधानम् — a word is deployed once per thing meant, so one word
cannot denote several. Two trees would call for two utterances of वृक्ष, and
this is what licenses saying it once.

Two things here are read rather than listed.

**त्यदादि.** 1.2.72 names a gaṇa, and the gaṇa is the tail of सर्वादि: the
corpus has all thirty-five members of 1.1.27's list, and त्यद् is the
twenty-fourth. So the twelve are taken from there. That also gives the
vārttika something to be checked against — त्यदादीनां मिथो यद् यत् परं तत्
तच्छिष्यते, of two tyadādi words the later one survives, and 'later' means
later *in that list*, which is why स च यश्च gives यौ and यश्च कश्च gives कौ.

**यथासंख्यम्.** 1.2.68 pairs two words against two others respectively, and
that is 1.3.10's rule, already codified. It is called rather than repeated.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Optional, Sequence, Tuple

from src.astadhyayi.corpus import load_ganapatha
from src.astadhyayi.reading import yathasamkhya

#: The three genders 1.2.66, 1.2.67 and 1.2.69 turn on, and a fourth value for
#: a word that has none — प्राक् is an avyaya, and 1.2.67's counter-example
#: प्राक्प्राच्यौ turns on exactly that: प्रागित्यव्ययमलिङ्गम्.
PUMS, STRI, NAPUMSAKA, ALINGA = "puṃs", "strī", "napuṃsaka", "aliṅga"


# --- त्यदादि, read off 1.1.27's gaṇa ---------------------------------------


@lru_cache(maxsize=None)
def sarvadi() -> Tuple[str, ...]:
    """1.1.27's सर्वादि, in the order the gaṇapāṭha reads it."""
    for gana in load_ganapatha().get("1.1.27", ()):
        if gana.name.startswith("sarvādi"):
            return tuple(gana.items)
    return ()


@lru_cache(maxsize=None)
def tyadadi() -> Tuple[str, ...]:
    """
    त्यदादि — 1.2.72's group, the tail of सर्वादि from त्यद् onwards.

    Not a separate list anywhere: the name means 'त्यद् and what follows', and
    what follows is fixed by the gaṇa the corpus already holds. Twelve words,
    ending at किम्.
    """
    members = sarvadi()
    if "tyad" not in members:
        return ()
    return members[members.index("tyad"):]


def is_tyadadi(stem: str) -> bool:
    return stem in tyadadi()


def _tyadadi_order(stem: str) -> int:
    return tyadadi().index(stem) if stem in tyadadi() else -1


# --- a word, as far as these ten sūtras care ------------------------------


@dataclass(frozen=True)
class Word:
    """
    One member of a coordination.

    `stem` is what 1.2.64's सरूपाणाम् compares and what 1.2.65's तल्लक्षणश्चेदेव
    विशेषः asks after: whether the only difference between two words is the one
    the sūtra names. Two words with different stems are simply two words.
    """

    stem: str
    form: str = ""
    gender: str = PUMS
    case: int = 1
    #: 1.2.65 — वृद्ध is the gotra proper and युवन् its descendant. The Kāśikā
    #: notes वृद्धशब्दः पूर्वाचार्यसंज्ञा गोत्रस्य, an earlier teachers' term.
    gotra: Optional[str] = None
    #: 1.2.68, 1.2.70, 1.2.71 — the eight kinship words those three name.
    kinship: Optional[str] = None
    #: तल्लक्षणश्चेदेव विशेषः. Where the two differ in something *besides* what
    #: the sūtra names, neither drops: इन्द्र and इन्द्राणी differ by 4.1.48 as
    #: well as by gender, so इन्द्रेन्द्राण्यौ stands.
    other_difference: bool = False
    #: 1.2.73's four conditions.
    gramya: bool = False
    pasu: bool = False
    sangha: bool = False
    taruna: bool = False
    #: The vārttika अनेकशफेषु — cloven-hoofed. अश्वाः is what it keeps out.
    aneka_shapha: bool = True

    def __post_init__(self):
        if not self.form:
            object.__setattr__(self, "form", self.stem)


@dataclass(frozen=True)
class Verdict:
    """Which word remains, in what number, and by which sūtra."""

    remaining: Optional[Word]
    number: Optional[int]
    by: str
    why: str
    optional: bool = False
    #: What the surviving word behaves as, where a sūtra says. 1.2.66's पुंवत्
    #: is the case: a feminine survives but takes the masculine's forms.
    behaves_as: Optional[str] = None


# --- the retention rules ---------------------------------------------------


def _same_but_for(words: Sequence[Word], field_name: str) -> bool:
    """
    तल्लक्षणश्चेदेव विशेषः — is the named property the *only* thing differing?

    The Kāśikā tests it three ways at 1.2.65 and gives a counter-example for
    each: a different stem (गार्ग्यवात्स्यायनौ), a difference of some other
    kind (भागवित्तिभागवित्तिकौ, where कुत्सा and सौवीरत्व divide them besides),
    and the property itself failing to differ.
    """
    if len({w.stem for w in words}) != 1:
        return False
    if any(w.other_difference for w in words):
        return False
    return len({getattr(w, field_name) for w in words}) == len(words)


def _herd_of_animals(words: Sequence[Word]) -> bool:
    """1.2.73's four conditions, each with a counter-example in the Kāśikā."""
    return all(
        w.gramya and w.pasu and w.sangha and not w.taruna and w.aneka_shapha
        for w in words
    )


def ekasesa(words: Sequence[Word]) -> Verdict:
    """
    Which of these coordinated words remains — 1.2.64 to 1.2.73.

    The specific rules are tried before the general one, since 1.2.65 onwards
    are all apavādas to 1.2.64: that sūtra reaches words of the same form, and
    each of the others names a pair that differ. 1.2.72 comes first because it
    is नित्यम् and displaces the options.
    """
    words = tuple(words)
    if len(words) < 2:
        return Verdict(words[0] if words else None, len(words), "—",
                       "एकशेष needs more than one word to have anything to do.")

    if len({w.case for w in words}) != 1:
        return Verdict(
            None, None, "1.2.64",
            "एकविभक्तौ — the words must stand in one and the same case, and "
            "these do not: पयः पयो जरयति, ब्राह्मणाभ्यां च कृतं ब्राह्मणाभ्यां "
            "च देहि.",
        )

    total = len(words)

    # 1.2.72 — त्यदादीनि सर्वैर्नित्यम्, invariably and against everything.
    tyad = [w for w in words if is_tyadadi(w.stem)]
    if tyad:
        chosen = max(tyad, key=lambda w: _tyadadi_order(w.stem))
        why = ("त्यदादीनि सर्वैर्नित्यम् — a त्यदादि word survives against any "
               "other, and नित्यग्रहणं विकल्पनिवृत्त्यर्थम्, the नित्यम् is "
               "there to shut out the options: स च देवदत्तश्च तौ")
        if len(tyad) > 1:
            why = ("त्यदादीनां मिथो यद् यत् परं तत् तच्छिष्यते (vārt.) — of two "
                   "त्यदादि words the one later in the gaṇa survives: "
                   "स च यश्च यौ, यश्च कश्च कौ")
        return Verdict(chosen, total, "1.2.72", why)

    # 1.2.73 — an apavāda to 1.2.67, and the Kāśikā says so outright.
    if _herd_of_animals(words) and any(w.gender is STRI for w in words):
        female = next(w for w in words if w.gender == STRI)
        return Verdict(
            female, total, "1.2.73",
            "ग्राम्यपशुसंघेष्वतरुणेषु स्त्री — पुमान् स्त्रिया इति पुंसः शेषे "
            "प्राप्ते स्त्रीशेषो विधीयते: for a herd of grown domestic animals "
            "the feminine survives instead: गाव इमाः, अजा इमाः",
        )

    # 1.2.68 — and the pairing is 1.3.10's, called rather than repeated.
    paired = yathasamkhya(("bhrātṛ", "putra"), ("svasṛ", "duhitṛ"))
    kinships = {w.kinship for w in words if w.kinship}
    for keeps, drops in paired or ():
        if kinships == {keeps, drops}:
            kept = next(w for w in words if w.kinship == keeps)
            return Verdict(
                kept, total, "1.2.68",
                f"भ्रातृपुत्रौ स्वसृदुहितृभ्याम् — यथासंख्यम् by 1.3.10, so "
                f"{keeps} survives against {drops}: भ्राता च स्वसा च भ्रातरौ, "
                f"पुत्रश्च दुहिता च पुत्रौ",
            )

    # 1.2.70, 1.2.71 — the two optional pairs.
    for keeps, drops, sutra, worked in (
        ("pitṛ", "mātṛ", "1.2.70", "माता च पिता च पितरौ, or मातापितरौ"),
        ("śvaśura", "śvaśrū", "1.2.71",
         "श्वशुरश्च श्वश्रूश्च श्वशुरौ, or श्वश्रूश्वशुरौ"),
    ):
        if kinships == {keeps, drops}:
            kept = next(w for w in words if w.kinship == keeps)
            return Verdict(
                kept, total, sutra,
                f"अन्यतरस्याम् carries down from 1.2.69, so the retention is "
                f"optional and the compound stands beside it: {worked}",
                optional=True,
            )

    # 1.2.69 — the neuter, and optionally in the singular.
    genders = {w.gender for w in words}
    if NAPUMSAKA in genders and genders != {NAPUMSAKA}:
        neuter = next(w for w in words if w.gender == NAPUMSAKA)
        return Verdict(
            neuter, 1, "1.2.69",
            "नपुंसकमनपुंसकेनैकवच्चास्यान्यतरस्याम् — the neuter survives "
            "against a non-neuter, and optionally goes into the singular: "
            "शुक्लश्च कम्बलः शुक्ला च बृहतिका शुक्लं च वस्त्रं तदिदं शुक्लम्, "
            "or तानीमानि शुक्लानि",
            optional=True,
        )

    # 1.2.66, 1.2.67 — gender, and 1.2.66 where the gotra divides them too.
    if genders == {PUMS, STRI} and _same_but_for(words, "gender"):
        female = next(w for w in words if w.gender == STRI)
        male = next(w for w in words if w.gender == PUMS)
        if female.gotra == "vṛddha" and male.gotra == "yuvan":
            return Verdict(
                female, total, "1.2.66",
                "स्त्री पुंवच्च — the elder survives though she is feminine, "
                "and takes the masculine's forms: पुंस इवास्याः कार्यं भवति. "
                "गार्गी च गार्ग्यायणश्च गार्ग्यौ",
                behaves_as=PUMS,
            )
        return Verdict(
            male, total, "1.2.67",
            "पुमान् स्त्रिया — the masculine survives: ब्राह्मणश्च ब्राह्मणी च "
            "ब्राह्मणौ. तल्लक्षणश्चेदेव विशेषः, so इन्द्रेन्द्राण्यौ stands, the "
            "two differing by 4.1.48 as well as by gender",
        )

    # 1.2.65 — the gotra proper against its descendant.
    if _same_but_for(words, "gotra") and {w.gotra for w in words} == {
        "vṛddha", "yuvan"
    }:
        elder = next(w for w in words if w.gotra == "vṛddha")
        return Verdict(
            elder, total, "1.2.65",
            "वृद्धो यूना तल्लक्षणश्चेदेव विशेषः — the gotra name survives "
            "against the descendant's, if that is the only thing dividing "
            "them: गार्ग्यश्च गार्ग्यायणश्च गार्ग्यौ",
        )

    # 1.2.64 — the general case.
    if len({w.form for w in words}) == 1:
        return Verdict(
            words[0], total, "1.2.64",
            "सरूपाणामेकशेष एकविभक्तौ — of words of one form standing in one "
            "case, one remains: वृक्षश्च वृक्षश्च वृक्षौ. रूपग्रहणं is there so "
            "that it holds though the meanings differ — अक्षाः, पादाः, माषाः",
        )

    return Verdict(
        None, None, "—",
        "Nothing retains: the words differ in form and in no way any of "
        "1.2.65–1.2.73 names, so both stand — प्लक्षन्यग्रोधाः.",
    )


# --- 1.2.58 to 1.2.63, the numbers that do not match ----------------------


@dataclass(frozen=True)
class NumberVerdict:
    """Which number may be used, by which sūtra."""

    numbers: Tuple[int, ...]
    by: str
    why: str
    optional: bool = False


#: Each of these four sūtras names its stars, and naming them is most of what
#: it does — 1.2.60's counter-example फल्गुन्यौ माणविके turns on the word being
#: used of stars at all, and 1.2.61's पुनर्वसू माणवकौ on the same. So the
#: codification asks which star, not merely whether one is meant.
_PAIRED_STARS = ("phalgunī", "proṣṭhapadā")        # 1.2.60, plural for dual
_VEDIC_SINGULAR = ("punarvasū", "viśākhā")         # 1.2.61 and 1.2.62
_TISYA_PAIR = ("tiṣya", "punarvasū")               # 1.2.63, dual for plural


def number_for(
    *,
    counted: int,
    jati: bool = False,
    asmad: bool = False,
    star: Optional[str] = None,
    nakshatra: bool = False,
    dvandva_of: Sequence[str] = (),
    chandas: bool = False,
    with_numeral: bool = False,
) -> NumberVerdict:
    """
    Which number may stand — 1.2.58 to 1.2.63.

    Each of these lets a number be used that does not match the count, and
    each is an option except the last. The conditions are all semantic —
    whether a word names a class, whether a star or a boy is meant — so they
    are given rather than computed, as everywhere else in this pāda.
    """
    if dvandva_of and tuple(dvandva_of) == _TISYA_PAIR and nakshatra:
        return NumberVerdict(
            (2,), "1.2.63",
            "तिष्यपुनर्वस्वोर्नक्षत्रद्वन्द्वे बहुवचनस्य द्विवचनं नित्यम् — one "
            "star and two make three, and the dvandva would be plural; this "
            "makes it dual, and नित्यग्रहणं विकल्पनिवृत्त्यर्थम्: "
            "उदितौ तिष्यपुनर्वसू दृश्येते",
        )

    if star in _VEDIC_SINGULAR and nakshatra and chandas and counted == 2:
        return NumberVerdict(
            (1, 2), "1.2.61" if star == "punarvasū" else "1.2.62",
            "छन्दसि पुनर्वस्वोरेकवचनम् and 1.2.62 विशाखयोश्च — in the Veda, "
            "these two pairs may stand in the singular: पुनर्वसुर्नक्षत्रम् "
            "beside पुनर्वसू नक्षत्रम्, विशाखा नक्षत्रम् beside विशाखे नक्षत्रम्. "
            "छन्दसि is the condition, and outside it पुनर्वसू stands dual",
            optional=True,
        )

    if star in _PAIRED_STARS and nakshatra and counted == 2:
        return NumberVerdict(
            (2, 3), "1.2.60",
            "फल्गुनीप्रोष्ठपदानां च नक्षत्रे — of these two pairs of stars, the "
            "plural may stand for the dual: कदा पूर्वे फल्गुन्यौ, कदा पूर्वाः "
            "फल्गुन्यः. नक्षत्रे is the condition — फल्गुन्यौ माणविके is out",
            optional=True,
        )

    if asmad and counted in (1, 2):
        return NumberVerdict(
            (counted, 3), "1.2.59",
            "अस्मदो द्वयोश्च — for अस्मद्, the plural may stand for one or two: "
            "अहं ब्रवीमि / वयं ब्रूमः, आवां ब्रूवः / वयं ब्रूमः",
            optional=True,
        )

    if jati and counted == 1:
        if with_numeral:
            return NumberVerdict(
                (1,), "1.2.58",
                "संख्याप्रयोगे प्रतिषेधः (vārt.) — not where a numeral is used: "
                "एको व्रीहिः संपन्नः सुभिक्षं करोति",
            )
        return NumberVerdict(
            (1, 3), "1.2.58",
            "जात्याख्यायामेकस्मिन् बहुवचनमन्यतरस्याम् — a class-name for one "
            "thing may take the plural: संपन्नो व्रीहिः / संपन्ना व्रीहयः. "
            "आख्यायाम् is a condition — काश्यपः meaning a portrait of Kāśyapa "
            "does not name a class, and is out",
            optional=True,
        )

    return NumberVerdict(
        (counted,), "—",
        "Nothing in 1.2.58–1.2.63 reaches this, so the number matches what is "
        "counted.",
    )


#: The words a coordination member may be tagged with, after its stem.
#: Everything here is a fact the sūtras ask about and a bare string cannot
#: carry — गार्ग्य alone does not say whether it is the gotra name or the
#: descendant's, and 1.2.65 turns on nothing else.
TAGS = {
    "puṃs": ("gender", PUMS), "strī": ("gender", STRI),
    "napuṃsaka": ("gender", NAPUMSAKA), "aliṅga": ("gender", ALINGA),
    "vṛddha": ("gotra", "vṛddha"), "yuvan": ("gotra", "yuvan"),
    "herd": ("_herd", True), "young": ("taruna", True),
    "wild": ("_wild", True), "one-hoofed": ("aneka_shapha", False),
    "other": ("other_difference", True),
}

#: The eight kinship words 1.2.68, 1.2.70 and 1.2.71 name. Tagging is
#: unnecessary for these — the stem *is* the kinship.
_KINSHIP = ("bhrātṛ", "svasṛ", "putra", "duhitṛ",
            "pitṛ", "mātṛ", "śvaśura", "śvaśrū")

#: And the feminine of the four that have one, so a caller need not say it.
_FEMININE = ("svasṛ", "duhitṛ", "mātṛ", "śvaśrū")


def parse(text: str) -> Word:
    """
    One coordination member, written as `stem` with optional `:tag`s.

    A form on a web page can hand back strings and nothing else, so the
    facts these sūtras turn on need a way in. `gārgya:vṛddha` against
    `gārgya:yuvan` is 1.2.65's pair; `go:strī:herd` against `go:herd` is
    1.2.73's. Unknown tags are ignored rather than raising, since a reader
    experimenting in the playground should get an answer and not a stack
    trace.
    """
    stem, *tags = [part.strip() for part in text.split(":") if part.strip()]
    fields = {"stem": stem}
    if stem in _KINSHIP:
        fields["kinship"] = stem
    if stem in _FEMININE:
        fields["gender"] = STRI
    for tag in tags:
        if tag not in TAGS:
            continue
        name, value = TAGS[tag]
        if name == "_herd":
            fields.update(gramya=True, pasu=True, sangha=True)
        elif name == "_wild":
            fields.update(pasu=True, sangha=True, gramya=False)
        else:
            fields[name] = value
    return Word(**fields)


def ekasesa_of(words: Sequence[str]) -> Verdict:
    """
    1.2.64 to 1.2.73, from a list of written members — what the form offers.

    Each member is a stem with optional tags: `gārgya:vṛddha`,
    `śukla:napuṃsaka`, `go:strī:herd`. See `parse` for the vocabulary.
    """
    return ekasesa([parse(w) for w in words])


__all__ = [
    "ALINGA",
    "TAGS",
    "ekasesa_of",
    "parse",
    "NAPUMSAKA",
    "NumberVerdict",
    "PUMS",
    "STRI",
    "Verdict",
    "Word",
    "ekasesa",
    "is_tyadadi",
    "number_for",
    "sarvadi",
    "tyadadi",
]
