# -*- coding: utf-8 -*-
"""
2.4.58 to 2.4.71 — affixes that are added and then taken away.

A descendant-affix is put on by adhyāya 4 and this run takes it off
again, so that the son is called by the father's name. Two conditions
divide it: the first four rules elide the YUVAN affix, the next nine
elide a GOTRA or तद्राज affix in the PLURAL, and the last rule stands
apart from both.

    2.4.58 ण्यक्षत्रियार्षञितो यूनि लुगणिञोः  four stems lose अण् and इञ्
    2.4.59 पैलादिभ्यश्च                      and a gaṇa
    2.4.60 इञः प्राचाम्                       after इञ्, among easterners
    2.4.61 न तौल्वलिभ्यः                      but not after these
    2.4.62 तद्राजस्य बहुषु तेनैवास्त्रियाम्    a तद्राज, in the plural
    2.4.63 यस्कादिभ्यो गोत्रे                 a gotra affix, after a gaṇa
    2.4.64 यञञोश्च                           and these two gotra affixes
    2.4.65 अत्रिभृगुकुत्सवसिष्ठगोतमाङ्गिरोभ्यश्च  and after six ṛṣis
    2.4.66 बह्वच इञः प्राच्यभरतेषु            इञ् after a long stem
    2.4.67 न गोपवनादिभ्यः                     but not after eight words
    2.4.68 तिककितवादिभ्यो द्वन्द्वे            in a dvandva
    2.4.69 उपकादिभ्योऽन्यतरस्यामद्वन्द्वे      optionally, outside one
    2.4.70 आगस्त्यकौण्डिन्ययोरगस्तिकुण्डिनच्   and the stem changes too
    2.4.71 सुपो धातुप्रातिपदिकयोः              a सुप् goes inside a word

**Three conditions run through 2.4.62 to 2.4.70, and each is a real
one.** बहुषु — the plural; अस्त्रियाम् — not the feminine; and तेनैव —
the plurality must be MADE by that very affix. The Kāśikā gives a
counter-example for each in turn, and they are the difference between
अङ्गाः and आङ्गः, between यस्काः and यास्क्यः स्त्रियः, and between
यस्काः and प्रिययास्काः, where the plurality comes from the बहुव्रीहि
and not from the descendant-affix. Codified as three separate
conditions, because a form can fail any one of them alone.

**2.4.66 teaches something about 2.4.60 by saying a word it did not
need to.** भरत is already among the प्राच्, so naming both in 2.4.66 is
redundant — and the vṛtti reads the redundancy as deliberate: भरताः
प्राच्या एव, तेषां पुनर्ग्रहणं ज्ञापनार्थम् — अन्यत्र प्राग्ग्रहणे
भरतग्रहणं न भवति. Wherever else प्राच् is said, भरत is NOT included. So
2.4.60 does not reach the Bharatas, and आर्जुनिः पिता, आर्जुनायनः पुत्रः
keep different forms. A rule stated where it was not needed is doing
other work — the same argument the vṛtti makes at 2.4.36 about ल्यप्.

**गोपवनादि is taken from the Kāśikā and NOT from the gaṇapāṭha on
disk.** The file holds eleven entries, one of which is the bare string
``"1"`` — a parse artifact, not a word — and several others are
spelling variants. The vṛtti is explicit about the true extent:
एतावन्त एवाष्टौ गोपवनादयः, exactly eight, and it names them; then it
says what the surplus is and why it matters —
परिशिष्टानां हरितादीनां प्रमादपाठः, ते हि चतुर्थे बिदादिषु पठ्यन्ते,
तेभ्यश्च बहुषु लुग् भवत्येव. The extra words belong to बिदादि, and the
elision DOES happen for them: हरिताः, किंदासाः. Reading the file
straight would have made this rule block exactly the forms the
commentary says it must allow. The second defective gaṇa this pāda has
turned up, after the Kāśikā stored against 2.4.28.
"""

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.anga import Elided
from src.astadhyayi.samasa import _gana

# ---------------------------------------------------------------------------
# The lists
# ---------------------------------------------------------------------------

#: 2.4.59's पैलादि, from disk. आकृतिगणोऽयम् — the vṛtti marks it open,
#: so membership is a lookup and not a closed count.
PAILADI: Tuple[str, ...] = _gana("2.4.59", "pailādi")

#: 2.4.61's तौल्वल्यादि, from disk — the प्रतिषेध against 2.4.60.
TAULVALYADI: Tuple[str, ...] = _gana("2.4.61", "taulvalyādi")

#: 2.4.63's यस्कादि, from disk.
YASKADI: Tuple[str, ...] = _gana("2.4.63", "yaskādi")

#: 2.4.68's तिककितवादि, from disk — and these are finished PLURAL
#: compounds, तिककितवाः and the rest, not the members. The rule is
#: about a द्वन्द्व, so what it names is the द्वन्द्व. The same shape as
#: 2.4.11's गवाश्वादि, which also fixes शब्दरूप rather than a class.
TIKAKITAVADI: Tuple[str, ...] = _gana("2.4.68", "tikakitavādi")

#: 2.4.69's उपकादि, from disk.
UPAKADI: Tuple[str, ...] = _gana("2.4.69", "upakādi")

#: 2.4.67's गोपवनादि — the Kāśikā's eight, NOT the gaṇapāṭha's eleven.
#: See the module docstring: the file carries a parse artifact and
#: several variants, and the vṛtti both fixes the extent
#: (एतावन्त एवाष्टौ) and says the surplus words take the elision after
#: all. Held by a test that checks the disk list still disagrees, so a
#: corrected corpus turns it red.
GOPAVANADI: Tuple[str, ...] = (
    "gopavana", "śigru", "bindu", "bhājana", "aśva", "avatāna",
    "śyāmāka", "śvāparṇa",
)

#: 2.4.65's six ṛṣis, named in the sūtra itself.
ATRYADI: Tuple[str, ...] = (
    "atri", "bhṛgu", "kutsa", "vasiṣṭha", "gotama", "aṅgiras",
)

#: 2.4.58's four kinds of stem the yuvan affix is dropped after.
NYADI_STEMS: Tuple[str, ...] = ("ṇya", "kṣatriya-gotra", "ārṣa", "ñit")

#: 2.4.70's two, and what each stem becomes. आगस्त्य and कौण्डिन्य lose
#: their affix AND change shape — यथासंख्यम्, each to its own.
AGASTYA_KAUNDINYA: dict = {
    "āgastya": "agasti",
    "kauṇḍinya": "kuṇḍinac",
}


@dataclass(frozen=True)
class Renamed(Elided):
    """
    2.4.70 alone: the affix goes AND the stem is replaced.

    Every other rule of this run only takes an affix away, so the
    substitute is carried here rather than in :class:`Elided`, which is
    shared with 2.4.72 and should not grow a field only one caller uses.
    """

    stem: str = ""


def taddhita_luk(
    *,
    affix: str = "",
    descendant: str = "",
    stem: str = "",
    stem_kind: str = "",
    plural: bool = False,
    feminine: bool = False,
    by_that_affix: bool = True,
    region: str = "",
    dvandva: bool = False,
    bahvac: bool = False,
) -> Elided:
    """
    Whether a descendant-affix is elided — 2.4.58 to 2.4.70.

    The two प्रतिषेध are asked first, because a prohibition written
    against a rule cannot be reached after that rule has answered.
    """
    # --- 2.4.61 and 2.4.67, the two prohibitions -----------------------
    if stem and stem in TAULVALYADI:
        return Elided(
            False, "2.4.61",
            f"न तौल्वलिभ्यः — {stem} is one of the words 2.4.60's elision "
            f"is refused after, so father and son differ: तौल्वलिः पिता, "
            f"तौल्वलायनः पुत्रः",
            elision="",
        )
    if stem and stem in GOPAVANADI:
        return Elided(
            False, "2.4.67",
            f"न गोपवनादिभ्यः — {stem} is one of the eight, so the elision "
            f"2.4.64 would have given is refused: गौपवनाः, शैग्रवाः. "
            f"एतावन्त एवाष्टौ गोपवनादयः — the vṛtti fixes the count at "
            f"eight and says the words usually added to it are a "
            f"प्रमादपाठ belonging to बिदादि, from which the elision does "
            f"happen: हरिताः, किंदासाः",
            elision="",
        )

    # --- 2.4.58 to 2.4.60, the यूनि block ------------------------------
    if descendant == "yuvan":
        if stem_kind and stem_kind in NYADI_STEMS and affix in ("aṇ", "iñ"):
            return Elided(
                True, "2.4.58",
                f"ण्यक्षत्रियार्षञितो यूनि लुगणिञोः — after a {stem_kind} "
                f"stem the yuvan {affix} goes, so father and son are "
                f"called alike: कौरव्यः पिता, कौरव्यः पुत्रः; श्वाफल्कः "
                f"पिता, श्वाफल्कः पुत्रः",
                elision="luk",
            )
        if stem and stem in PAILADI:
            return Elided(
                True, "2.4.59",
                f"पैलादिभ्यश्च — {stem} is in the gaṇa: पैलः पिता, पैलः "
                f"पुत्रः. आकृतिगणोऽयम्, so the list is open. Several of "
                f"its members end in इञ् and would have been reached by "
                f"2.4.60 anyway — अप्रागर्थः पाठः, they are listed here "
                f"because 2.4.60 holds only among the easterners",
                elision="luk",
            )
        if affix == "iñ" and region == "prāc":
            return Elided(
                True, "2.4.60",
                "इञः प्राचाम् — after an इञ्-final gotra stem, among the "
                "easterners: पान्नागारिः पिता, पान्नागारिः पुत्रः. "
                "प्राचामिति किम्? दाक्षिः पिता, दाक्षायणः पुत्रः. And "
                "गोत्रविशेषणं प्राग्ग्रहणम्, न विकल्पार्थम् — प्राचाम् "
                "qualifies the gotra and does not make the rule optional",
                elision="luk",
            )
        if affix == "iñ" and region == "bharata":
            return Elided(
                False, "",
                "भरताः प्राच्या एव, तेषां पुनर्ग्रहणं ज्ञापनार्थम् — "
                "अन्यत्र प्राग्ग्रहणे भरतग्रहणं न भवति. By naming भरत "
                "where it did not need to, 2.4.66 teaches that प्राच् "
                "said anywhere else does NOT take the Bharatas in. So "
                "2.4.60 does not reach them: आर्जुनिः पिता, आर्जुनायनः "
                "पुत्रः",
                elision="",
            )
        return Elided(
            False, "",
            "No rule of 2.4.58 to 2.4.60 reaches this yuvan affix, so it "
            "stands and the son is named apart from the father",
            elision="",
        )

    # --- 2.4.62 to 2.4.70, the बहुषु block -----------------------------
    # The three conditions the whole run carries, each refused on its own
    # so that a reader is told WHICH one failed.
    if not plural:
        return Elided(
            False, "",
            "बहुष्विति किम्? आङ्गः, यास्कः, गार्ग्यः. Everything from "
            "2.4.62 to 2.4.70 holds in the PLURAL only",
            elision="",
        )
    if feminine:
        return Elided(
            False, "",
            "अस्त्रियामिति किम्? आङ्ग्यः स्त्रियः, यास्क्यः स्त्रियः, "
            "गार्ग्यः स्त्रियः. The feminine keeps its affix",
            elision="",
        )
    if not by_that_affix:
        return Elided(
            False, "",
            "तेनैवग्रहणं किम्? प्रियो वाङ्गो येषां ते प्रियवाङ्गाः, "
            "प्रिययास्काः, प्रियगार्ग्याः — there the plural comes from "
            "the बहुव्रीहि and not from the descendant-affix itself, so "
            "the affix is not what made the many",
            elision="",
        )

    if stem and stem in AGASTYA_KAUNDINYA:
        return Renamed(
            True, "2.4.70",
            f"आगस्त्यकौण्डिन्ययोरगस्तिकुण्डिनच् — the affix goes and the "
            f"stem changes with it, यथासंख्यम्: अगस्तयः, कुण्डिनाः. This "
            f"is the one rule of the run that replaces as well as "
            f"elides. चकारः स्वरार्थः — the च is there for the accent, "
            f"since कुण्डिनी is मध्योदात्त and its substitute would else "
            f"be so too",
            elision="luk", stem=AGASTYA_KAUNDINYA[stem],
        )
    if affix == "tadrāja":
        return Elided(
            True, "2.4.62",
            "तद्राजस्य बहुषु तेनैवास्त्रियाम् — अङ्गाः, वङ्गाः, मगधाः. "
            "तद्राजस्येति किम्? औपगवाः, where the affix is not a तद्राज",
            elision="luk",
        )
    if dvandva and stem and stem in TIKAKITAVADI:
        return Elided(
            True, "2.4.68",
            f"तिककितवादिभ्यो द्वन्द्वे — {stem}. The gaṇa holds finished "
            f"द्वन्द्व plurals and not their members, as 2.4.11's "
            f"गवाश्वादि holds finished compounds: तैकायनयश्च कैतवायनयश्च "
            f"gives तिककितवाः",
            elision="luk",
        )
    if stem and stem in UPAKADI:
        if dvandva:
            return Elided(
                True, "2.4.68",
                f"अद्वन्द्वग्रहणं द्वन्द्वाधिकारनिवृत्त्यर्थम् — 2.4.69's "
                f"option is for the NON-dvandva. Three of उपकादि are "
                f"also read in तिककितवादि, and in a द्वन्द्व those go by "
                f"2.4.68: तेषां पूर्वेण नित्यमेव लुग् भवति, उपकलमकाः",
                elision="luk",
            )
        return Elided(
            True, "2.4.69",
            f"उपकादिभ्योऽन्यतरस्यामद्वन्द्वे — outside a द्वन्द्व it is a "
            f"choice: उपकाः beside औपकायनाः, लमकाः beside लामकायनाः",
            elision="luk",
        )
    if descendant == "gotra":
        if stem and stem in YASKADI:
            return Elided(
                True, "2.4.63",
                f"यस्कादिभ्यो गोत्रे — यस्काः, लभ्याः. गोत्र इति किम्? "
                f"यास्काश्छात्राः. And the गोत्र meant is the ordinary "
                f"one and not 4.1.162's technical descendant: "
                f"प्रत्ययविधेश्चान्यत्र लौकिकस्य गोत्रस्य ग्रहणम्, so it "
                f"reaches an immediate child too",
                elision="luk",
            )
        if affix in ("yañ", "añ"):
            return Elided(
                True, "2.4.64",
                f"यञञोश्च — गर्गाः and वत्साः from यञ्, बिदाः and उर्वाः "
                f"from अञ्. गोत्र इत्येव: द्वैप्याः and औत्साश्छात्राः "
                f"keep theirs, being no gotra affix",
                elision="luk",
            )
        if stem and stem in ATRYADI:
            return Elided(
                True, "2.4.65",
                f"अत्रिभृगुकुत्सवसिष्ठगोतमाङ्गिरोभ्यश्च — {stem} is one "
                f"of the six: अत्रयः, भृगवः, कुत्साः, वसिष्ठाः, गोतमाः, "
                f"अङ्गिरसः",
                elision="luk",
            )
        if affix == "iñ" and bahvac and region in ("prācya", "bharata"):
            return Elided(
                True, "2.4.66",
                f"बह्वच इञः प्राच्यभरतेषु — पन्नागाराः, मन्थरैषणाः; and "
                f"among the Bharatas युधिष्ठिराः, अर्जुनाः. बह्वच इति "
                f"किम्? बैकयः, पौष्पयः — a two-syllable stem is not "
                f"reached. प्राच्यभरतेष्विति किम्? बालाकयः, हास्तिदासयः",
                elision="luk",
            )
    return Elided(
        False, "",
        "No rule of 2.4.62 to 2.4.70 reaches this affix, so it stands",
        elision="",
    )


def sup_luk(*, becomes: str = "") -> Elided:
    """
    2.4.71 सुपो धातुप्रातिपदिकयोः — a सुप् inside a word goes.

    सुपो विभक्तेर्धातुसंज्ञायाः प्रातिपदिकसंज्ञायाश्च लुग् भवति. The
    case-ending is put on and then taken away again wherever what
    carries it has become a root or a nominal stem: पुत्रीयति for the
    first, राजपुरुषः for the second. तदन्तर्गतास्तद्ग्रहणेन गृह्यन्ते —
    a word that has one INSIDE it is taken by the same naming.

    This is what lets a compound be built out of inflected words and
    still come out with one ending at the end, so it underwrites the
    whole of 2.1 and 2.2.
    """
    if becomes not in ("dhātu", "prātipadika"):
        return Elided(
            False, "",
            "धातुप्रातिपदिकयोरिति किम्? वृक्षः, प्लक्षः — an ordinary "
            "inflected word keeps its ending. The elision happens only "
            "where what carries the सुप् has itself become a root or a "
            "nominal stem",
            elision="",
        )
    shown = ("पुत्रीयति, घटीयति — a noun made into a verb"
             if becomes == "dhātu" else
             "कष्टश्रितः, राजपुरुषः — words joined into one stem")
    return Elided(
        True, "2.4.71",
        f"सुपो धातुप्रातिपदिकयोः — the सुप् goes where a {becomes} name "
        f"has applied: {shown}. तदन्तर्गतास्तद्ग्रहणेन गृह्यन्ते, a word "
        f"with one inside it is taken by the same naming. This is what "
        f"lets 2.1 and 2.2 build a compound out of inflected words and "
        f"still end it with one ending",
        elision="luk",
    )
