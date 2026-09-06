# -*- coding: utf-8 -*-
"""
3.1.69 to 3.1.93 — the class-marker, and the headings that follow it.

3.1.68 कर्तरि शप् gives every root शप् in the active. This run is
almost entirely अपवाद to it: nine of the ten dhātupāṭha classes take
something else instead, and which they take is what makes the classes
classes at all.

    3.1.69 दिवादिभ्यः श्यन्            the fourth class
    3.1.70 वा भ्राशभ्लाश…              optionally, nine roots
    3.1.71 यसोऽनुपसर्गात्              यस् without a preverb
    3.1.72 संयसश्च                    and with सम्
    3.1.73 स्वादिभ्यः श्नुः            the fifth class
    3.1.74 श्रुवः शृ च                 and श्रु, which changes shape
    3.1.75 अक्षोऽन्यतरस्याम्            optionally, अक्ष्
    3.1.76 तनूकरणे तक्षः               and तक्ष्, in one sense
    3.1.77 तुदादिभ्यः शः               the sixth class
    3.1.78 रुधादिभ्यः श्नम्             the seventh — and it goes INSIDE
    3.1.79 तनादिकृञ्भ्य उः              the eighth, and कृ
    3.1.80 धिन्विकृण्व्योर अ च           two roots, with a change
    3.1.81 क्र्यादिभ्यः श्ना            the ninth class
    3.1.82 स्तन्भु…श्नुश्च              five roots take two markers
    3.1.83 हलः श्नः शानज्झौ            श्ना becomes शानच् before हि
    3.1.84 छन्दसि शायजपि               and शायच् in the Veda

    3.1.85 व्यत्ययो बहुलम्              the Veda swaps them about
    3.1.86 लिङ्याशिष्यङ्                अङ् in a Vedic benedictive
    3.1.87 कर्मवत् कर्मणा तुल्यक्रियः    an agent treated as an object
    3.1.88 तपस्तपःकर्मकस्यैव            तप्, only of तपस्
    3.1.89 न दुहस्नुनमां यक्चिणौ        but not two effects, for three roots
    3.1.90 कुषिरजोः प्राचां श्यन्…       two roots, on the easterners' view

    3.1.91 धातोः                      heading, to the end of adhyāya 3
    3.1.92 तत्रोपपदं सप्तमीस्थम्         what stands in the locative
    3.1.93 कृदतिङ्                     and what is called कृत्

**The classes are read from the dhātupāṭha, never listed.** दिवादि is
class 04, स्वादि 05, तुदादि 06, रुधादि 07, तनादि 08, क्र्यादि 09 — the
codes the corpus already carries, asked through `verbal_gana`. That
helper was written for 2.4.72's अदादि and reused for 3.1.25's चुरादि;
this run brings the count to nine of the ten. A hand-copied class list
would be a second statement of what the data says.

**3.1.79 names कृ though कृ is already in तनादि, and the vṛtti says
what the naming buys.** तनादिपाठादेव उप्रत्यये सिद्धे करोतेरुपादानं
नियमार्थम्, अन्यत् तनादिकार्यं मा भूत् — so that the OTHER things done
to तनादि roots are not done to it. The one named is 2.4.79
तनादिभ्यस्तथासोः, whose optional elision of सिच् must not reach कृ:
अकृत, अकृथाः. A rule in this pāda reaching back to restrict one
codified two pādas earlier, and held by a test.

**कर्मवद्भाव is a transfer, not an affix.** 3.1.87 says an agent whose
action is like the object's is treated AS an object — कर्माश्रयाणि
कार्याणि प्रतिपद्यते — and the vṛtti names the four things that then
follow: यक्, the middle endings, चिण्, and चिण्वद्भाव. Three of those
are rules of the run just codified, 3.1.62 to 3.1.67, so this is where
that section is put to work. वत्करणं स्वाश्रयमपि यथा स्यात्: the वत्
is there so the transfer also reaches what belongs to the agent in its
own right — भिद्यते कुसूलेन.
"""

from dataclasses import dataclass
from typing import Dict, Optional, Tuple

# ---------------------------------------------------------------------------
# The lists the sūtras name
# ---------------------------------------------------------------------------

#: 3.1.70's nine, where श्यन् is a choice. उभयत्र विभाषेयम् — the
#: vṛtti notes भ्रमु is read twice in the dhātupāṭha and both are meant.
BHRASADI: Tuple[str, ...] = (
    "bhrāś", "bhlāś", "bhramu", "kramu", "klamu", "trasi", "truṭi",
    "laṣ",
)

#: 3.1.82's five. आद्याश्चत्वारो धातवः सौत्राः — the first four are
#: roots the sūtra itself supplies, found in no dhātupāṭha.
STAMBHVADI: Tuple[str, ...] = (
    "stanbhu", "stunbhu", "skanbhu", "skunbhu", "skuñ",
)

#: 3.1.80's two, which take उ and change their final to अ.
DHINVADI: Tuple[str, ...] = ("dhinvi", "kṛṇvi")

#: 3.1.89's three, refused two of कर्मवद्भाव's effects.
DUHADI: Tuple[str, ...] = ("duh", "snu", "nam")

#: Which dhātupāṭha class each विकरण belongs to, by the code the corpus
#: uses. Nine of the ten classes are settled this way — 01 by 3.1.68
#: शप्, 02 by 2.4.72, 10 by 3.1.25, and these six here.
BY_CLASS: Tuple[Tuple[str, str, str], ...] = (
    ("04", "śyan", "3.1.69"),
    ("05", "śnu", "3.1.73"),
    ("06", "śa", "3.1.77"),
    ("07", "śnam", "3.1.78"),
    ("08", "u", "3.1.79"),
    ("09", "śnā", "3.1.81"),
)

#: The other four classes, whose markers are settled outside this run —
#: 3.1.68 for the first, 2.4.72 for the second, 2.4.75 for the third,
#: 3.1.25 for the tenth. All four are codified, and the docstring above
#: already names three of them; this states the fourth and puts the ten in
#: one place so a caller can ask *by class code* rather than by root name.
#: The distinction matters: जि (ji) is spelt the same at 01.0642 जि जये
#: and 10.0324 जि भाषायाम्, so the name answers to two markers and only
#: the code answers to one.
OUTSIDE_THE_RUN: Tuple[Tuple[str, str, str], ...] = (
    ("01", "śap", "3.1.68"),
    ("02", "luk", "2.4.72"),
    ("03", "ślu", "2.4.75"),
    ("10", "ṇic", "3.1.25"),
)

#: All ten classes, by the dhātupāṭha's own two-digit code. Built from the
#: two tables above rather than written out, so that a correction to either
#: reaches this and nothing has to be kept in step by hand.
CLASS_MARKERS: Dict[str, Tuple[str, str]] = {
    code: (gives, sutra)
    for code, gives, sutra in BY_CLASS + OUTSIDE_THE_RUN
}


def marker_of_class(code: str) -> Optional[Tuple[str, str]]:
    """
    Which मार्कर a dhātupāṭha class takes, and by which sūtra.

    Asked with the code — "01", "06" — and not with a root, because a root
    NAME may be read in several classes and a code never is. Returns None
    for a code the dhātupāṭha does not use.

        marker_of_class("01")  → ("śap", "3.1.68")     भवति (bhavati)
        marker_of_class("06")  → ("śa",  "3.1.77")     तुदति (tudati)

    2.4.72's entry says "luk" rather than an affix, and that is the rule
    itself speaking: शप् is added by 3.1.68 and then elided, so the second
    class's marker is the *absence* left behind — अत्ति (atti), with
    nothing between root and ending.
    """
    return CLASS_MARKERS.get(code)


#: What the four things are that कर्मवद्भाव carries over. यग्-आत्मनेपद-
#: चिण्-चिण्वद्भावाः प्रयोजनम् — the vṛtti names them rather than
#: leaving "treated as an object" to be worked out.
KARMAVAT_EFFECTS: Tuple[str, ...] = ("yak", "ātmanepada", "ciṇ",
                                     "ciṇvadbhāva")


@dataclass(frozen=True)
class Marker:
    """A class-marker put after the root, and by which rule."""

    gives: str
    by: str
    why: str
    optional: bool = False
    #: A further change the same rule states — 3.1.74's and 3.1.80's.
    also: str = ""


@dataclass(frozen=True)
class NoMarker:
    """That this run adds none. ``by`` names a rule only where one acted."""

    by: str
    why: str
    gives: str = ""


def vikarana(
    root: str = "",
    *,
    gana: str = "",
    sense: str = "",
    upasarga: str = "",
    chandas: bool = False,
    before_hi: bool = False,
) -> object:
    """
    Which class-marker a root takes — 3.1.69 to 3.1.84.

    Everything here is an अपवाद of 3.1.68 कर्तरि शप्, so a root this
    run does not reach keeps शप् and is told so by name.
    """
    from src.astadhyayi.pada import verbal_gana

    classes = verbal_gana(root) if root else frozenset()

    # 3.1.83 and 3.1.84 replace the marker 3.1.81 gave, so they are
    # asked before it.
    if "09" in classes and chandas:
        return Marker(
            "śāyac", "3.1.84",
            "छन्दसि शायजपि — गृभाय जिह्वया मधु. शानचपि, so both "
            "substitutes stand in the Veda: बधान देव",
            also="or शानच्",
        )
    if "09" in classes and before_hi and _ends_in_consonant(root):
        return Marker(
            "śānac", "3.1.83",
            "हलः श्नः शानज्झौ — मुषाण, पुषाण. हल इति किम्? क्रीणीहि. "
            "हाविति किम्? मुष्णाति. And श्नः is written as a "
            "स्थानिनिर्देश आदेशसंप्रत्ययार्थः — naming what is replaced, "
            "so that शानच् is understood as a SUBSTITUTE; without it "
            "इतरथा प्रत्ययान्तरम् एव सर्वविषयं विज्ञायेत, it would have "
            "been read as another affix altogether, valid everywhere",
        )

    # The rules that name roots outright, before the classes they may
    # also belong to.
    if root in STAMBHVADI:
        return Marker(
            "śnā", "3.1.82",
            f"स्तन्भुस्तुन्भुस्कन्भुस्कुन्भुस्कुञ्भ्यः श्नुश्च — "
            f"स्तभ्नाति beside स्तभ्नोति: BOTH markers, not a choice "
            f"between a marker and none. आद्याश्चत्वारो धातवः सौत्राः, "
            f"the first four supplied by the sūtra itself. And "
            f"उदित्त्वप्रतिज्ञानात् सौत्राणाम् अपि धातूनां सर्वार्थत्वं "
            f"विज्ञायते — a सौत्र root is a root for every purpose and "
            f"not only for the rule that supplies it",
            also="or श्नु",
        )
    if root in DHINVADI:
        return Marker(
            "u", "3.1.80",
            "धिन्विकृण्व्योर अ च — धिनोति, कृणोति. The उ comes and the "
            "root's final becomes अ. अतो लोपस्य स्थानिवद्भावाद् गुणो न "
            "भवति: that अ is then dropped, and being स्थानिवत् by "
            "1.1.56 it keeps guṇa away — a sound doing work after it "
            "has gone, as at 2.4.42",
            also="the final becomes अ",
        )
    if root == "śru":
        return Marker(
            "śnu", "3.1.74",
            "श्रुवः शृ च — शृणोति, शृणुतः, शृण्वन्ति. The marker comes "
            "and the root changes shape with it, तत्संनियोगेन: two "
            "operations in one rule, as at 3.1.80",
            also="श्रु becomes शृ",
        )
    if root == "akṣ":
        return Marker(
            "śnu", "3.1.75",
            "अक्षोऽन्यतरस्याम् — अक्ष्णोति beside अक्षति. भौवादिकः, a "
            "first-class root, so without this rule it would simply "
            "have taken शप्",
            optional=True,
        )
    if root == "takṣ":
        if sense != "tanūkaraṇa":
            return NoMarker(
                "",
                "तनूकरण इति किम्? संतक्षति वाग्भिः — of cutting someone "
                "with words the marker does not come. "
                "अनेकार्थत्वाद् धातूनां विशेषणोपादानम्: a root having "
                "many senses is why the rule states one",
            )
        return Marker(
            "śnu", "3.1.76",
            "तनूकरणे तक्षः — तक्ष्णोति काष्ठम् beside तक्षति काष्ठम्, "
            "of thinning wood down",
            optional=True,
        )
    if root == "yas":
        if upasarga in ("", "sam"):
            which = "3.1.72" if upasarga == "sam" else "3.1.71"
            shown = ("संयस्यति beside संयसति"
                     if upasarga == "sam" else "यस्यति beside यसति")
            return Marker(
                "śyan", which,
                f"{'संयसश्च' if upasarga else 'यसोऽनुपसर्गात्'} — "
                f"{shown}. यस् is दैवादिक, a fourth-class root, so "
                f"3.1.69 would have given it श्यन् obligatorily; these "
                f"two make it a choice. सोपसर्गार्थ आरम्भः — 3.1.72 is "
                f"written because 3.1.71 had excluded preverbs",
                optional=True,
            )
        return Marker(
            "śyan", "3.1.69",
            "अनुपसर्गादिति किम्? आयस्यति, प्रयस्यति — with any preverb "
            "but सम् the option is gone and 3.1.69's श्यन् is "
            "obligatory again",
        )
    if root in BHRASADI:
        return Marker(
            "śyan", "3.1.70",
            f"वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः — भ्राश्यते "
            f"beside भ्राशते, भ्राम्यति beside भ्रमति. उभयत्र "
            f"विभाषेयम्, and भ्रमु is read twice in the dhātupāṭha — "
            f"अनवस्थाने and चलने — द्वयोरपि ग्रहणम्, both are meant",
            optional=True,
        )

    # 3.1.79 names कृ beside the eighth class, and the naming does work
    # of its own — see the module docstring.
    if root in ("kṛ", "ḍukṛñ"):
        return Marker(
            "u", "3.1.79",
            "तनादिकृञ्भ्य उः — करोति. कृ is in तनादि already, so the "
            "naming is not for the marker: तनादिपाठादेव उप्रत्यये "
            "सिद्धे करोतेरुपादानं नियमार्थम्, अन्यत् तनादिकार्यं मा "
            "भूत् — it restricts, so that the OTHER things done to "
            "तनादि roots are not done to कृ. The one meant is 2.4.79 "
            "तनादिभ्यस्तथासोः, whose optional elision of सिच् must not "
            "reach it: अकृत, अकृथाः",
        )

    # A root name does not fix a class. रुध् is read in the fourth and
    # the seventh, दिव् in three, तन् in two — the dhātupāṭha reads one
    # spelling in several places with different senses, and the marker
    # follows whichever is meant. Where the caller has not said, the
    # ambiguity is REPORTED rather than resolved by taking the first:
    # answering रुध् with श्यन् because 04 sorts before 07 would be the
    # table choosing on Pāṇini's behalf.
    reached = [(c, g, su) for c, g, su in BY_CLASS if c in classes]
    if gana:
        if gana not in classes:
            return NoMarker(
                "",
                f"{root} is not read in class {gana} of the "
                f"dhātupāṭha. It is read in "
                f"{', '.join(sorted(classes)) or 'none'}",
            )
        reached = [row for row in reached if row[0] == gana]
        if not reached:
            # The root IS of that class; the class simply takes no
            # marker from this run. Saying "not read in it" would have
            # been false — 01 goes to 3.1.68, 02 to 2.4.72, 10 to
            # 3.1.25, and all three are codified elsewhere.
            return NoMarker(
                "",
                f"class {gana} takes no marker from 3.1.69 to 3.1.84. "
                f"The first class keeps 3.1.68 कर्तरि शप्, the second "
                f"loses it by 2.4.72 अदिप्रभृतिभ्यः शपः, and the tenth "
                f"takes णिच् by 3.1.25 — each codified in its own place",
            )
    if len(reached) > 1:
        return NoMarker(
            "",
            f"{root} is read in more than one class — "
            f"{', '.join(c for c, _g, _s in reached)} — and each takes "
            f"a different marker. Say which is meant: the dhātupāṭha "
            f"reads one spelling in several places, in different "
            f"senses, and the marker follows the reading, not the "
            f"spelling",
        )
    if reached:
        code, gives, sutra = reached[0]
        return Marker(gives, sutra, _class_why(code, gives, sutra))

    return NoMarker(
        "",
        f"No rule of 3.1.69 to 3.1.84 reaches {root or 'this root'}, so "
        f"3.1.68 कर्तरि शप् stands — भवति, पचति. Every rule of this run "
        f"is an अपवाद of that one, and what none of them takes away it "
        f"keeps",
    )


def _class_why(code: str, gives: str, sutra: str) -> str:
    shown = {
        "04": "दीव्यति, सीव्यति. नकारः स्वरार्थः, शकारः सार्वधातुकार्थः "
              "— the न for the accent, the श् so that 1.4.13's "
              "सार्वधातुक reaches what follows",
        "05": "सुनोति, चिनोति",
        "06": "तुदति, नुदति. शकारः सार्वधातुकसंज्ञार्थः",
        "07": "रुणद्धि, भिनत्ति. मकारो देशविध्यर्थः — the म् says WHERE "
              "it goes, and by 1.1.47 it goes inside the root rather "
              "than after it. शकारः 6.4.23 श्नान्नलोपः इति "
              "विशेषणार्थः",
        "08": "तनोति, सनोति, क्षणोति",
        "09": "क्रीणाति, प्रीणाति. शकारः सार्वधातुकसंज्ञार्थः",
    }[code]
    return (f"the dhātupāṭha's class {code} takes {gives}: {shown}. "
            f"शपोऽपवादः — an exception to 3.1.68, and the class is read "
            f"from the corpus rather than listed here")


def _ends_in_consonant(root: str) -> bool:
    """
    हलः — whether the root's last sound is a consonant.

    हल् is a pratyāhāra, and which sounds it denotes is settled by the
    śivasūtras, which are codified. Asked rather than answered here: a
    hand-written vowel list would be a second statement of what those
    fourteen lines already say, and would have to be corrected twice.
    """
    from src.astadhyayi.adesa import scan_phonemes
    from src.astadhyayi.sivasutra import resolve

    sounds = scan_phonemes(root)
    # `resolve` and not the `denotes` wrapper: resolve is what 1.1.71
    # आदिरन्त्येन सहेता is registered as, and calling the wrapper put
    # the real rule one level further away than the reuse guard walks.
    return bool(sounds) and sounds[-1].text in resolve("hal").sounds


# ---------------------------------------------------------------------------
# 3.1.85 to 3.1.90 — an agent treated as an object
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Karmavat:
    """That an agent is treated as an object, and what follows from it."""

    by: str
    why: str
    effects: Tuple[str, ...] = ()
    refused: Tuple[str, ...] = ()


def karmavat(
    root: str = "",
    *,
    tulyakriya: bool = True,
    object_of_tap: bool = False,
    pracam: bool = False,
    lakara: str = "",
) -> object:
    """
    3.1.87 to 3.1.90 — कर्मवद्भाव, and the two rules that qualify it.

    कर्मस्थया क्रियया तुल्यक्रियः कर्ता कर्मवद् भवति: where the agent's
    action is like the object's — the wood as good as splitting itself
    — the agent takes what belongs to an object. The four things that
    then follow are named by the vṛtti and carried in `effects`.
    """
    if root in ("kuṣ", "rañj") and pracam:
        # व्यवस्थितविभाषा: settled differently in different places, and
        # the vṛtti says which — not in लिट्, लिङ् or the स्य futures.
        if lakara in ("liṭ", "liṅ", "lṛṭ", "lṛṅ"):
            return Karmavat(
                "",
                f"प्राचांग्रहणं विकल्पार्थम्, and व्यवस्थितविभाषा चेयम् "
                f"— the option is settled by where one is, not chosen: "
                f"तेन लिट्लिङोः स्यादिविषये च न भवतः. चुकुषे पादः "
                f"स्वयमेव, कोषिषीष्ट, कोषिष्यते all keep the middle",
            )
        return Karmavat(
            "3.1.90",
            "कुषिरजोः प्राचां श्यन् परस्मैपदं च — कुष्यति पादः स्वयमेव, "
            "रज्यति वस्त्रं स्वयमेव. यगात्मनेपदयोरपवादौ: श्यन् in place "
            "of the यक् 3.1.67 would have given, and the ACTIVE in "
            "place of the middle — two of कर्मवद्भाव's four effects "
            "displaced at once, on the eastern teachers' view",
            effects=("śyan", "parasmaipada"),
        )
    if root == "tap":
        if not object_of_tap:
            return Karmavat(
                "",
                "तपःकर्मकस्यैवेति किम्? उत्तपति सुवर्णं सुवर्णकारः — "
                "where तप् has any other object the transfer does not "
                "happen",
            )
        return Karmavat(
            "3.1.88",
            "तपस्तपःकर्मकस्यैव — तप्यते तपस्तापसः, अतप्त तपस्तापसः. "
            "पूर्वेणाप्राप्तः कर्मवद्भावो विधीयते: 3.1.87 could not "
            "have reached it, so this GRANTS rather than restricts. "
            "क्रियाभेदाद् विध्यर्थम् एतत् — the two senses of तप् are "
            "different acts, and the vṛtti separates them: austerities "
            "torment the ascetic, and the ascetic performs them",
            effects=KARMAVAT_EFFECTS,
        )
    if not tulyakriya:
        return Karmavat(
            "",
            "कर्मणा तुल्यक्रियः — the agent's action must be LIKE the "
            "object's. Where it is not, nothing is transferred",
        )
    if root in DUHADI:
        return Karmavat(
            "3.1.89",
            f"न दुहस्नुनमां यक्चिणौ — {root} is refused two of the four: "
            f"दुग्धे गौः स्वयमेव, प्रस्नुते गौः स्वयमेव, नमते दण्डः "
            f"स्वयमेव. And the vṛtti notes only one is newly refused — "
            f"दुहेरनेन यक् प्रतिषिध्यते, चिण् तु 3.1.63 दुहश्च इति "
            f"पूर्वम् एव विभाषितः: दुह्'s चिण् was already a choice, so "
            f"the prohibition adds nothing there",
            effects=("ātmanepada", "ciṇvadbhāva"),
            refused=("yak", "ciṇ"),
        )
    return Karmavat(
        "3.1.87",
        "कर्मवत् कर्मणा तुल्यक्रियः — भिद्यते काष्ठं स्वयमेव, अभेदि "
        "काष्ठं स्वयमेव, कारिष्यते कटः स्वयमेव. कर्माश्रयाणि कार्याणि "
        "प्रतिपद्यते: the agent takes what belongs to an object. And "
        "वत्करणं स्वाश्रयम् अपि यथा स्यात् — the वत् is there so the "
        "transfer reaches what belongs to the agent in its own right "
        "too: भिद्यते कुसूलेन",
        effects=KARMAVAT_EFFECTS,
    )


def vedic_latitude(*, lakara: str = "") -> object:
    """
    3.1.85 and 3.1.86 — what the Veda does with all of this.

    3.1.85 व्यत्ययो बहुलम्: the class-markers are swapped about.
    व्यतिगमनं व्यत्ययो व्यतिहारः, and the vṛtti sorts the kinds —
    विषयान्तरे विधानम्, क्वचिद् द्विविकरणता, क्वचित् त्रिविकरणता: one
    marker where another was due, sometimes two at once, sometimes
    three. बहुलग्रहणं सर्वविधिव्यभिचारार्थम् — the बहुल is there so
    that EVERY rule may be departed from, and a verse the vṛtti quotes
    extends it to number, person, voice, gender, tense and more.
    """
    if lakara == "liṅ":
        return Marker(
            "aṅ", "3.1.86",
            "लिङ्याशिष्यङ् — in the Veda, before a benedictive लिङ्: "
            "उपस्थेयम्, गमेम, वोचेम, विदेयम्, शकेयम्, आरुहेयम्. "
            "शपोऽपवादः. And 3.4.117 छन्दस्युभयथा gives that लिङ् the "
            "name सार्वधातुक as well, which is what lets a विकरण stand "
            "before it at all. A vārttika adds दृश्: दृशेयम्",
        )
    return Marker(
        "", "3.1.85",
        "व्यत्ययो बहुलम् — in the Veda the class-markers are "
        "interchanged: भेदति for भिनत्ति, मरन्ति for म्रियन्ते. "
        "Sometimes two markers at once and sometimes three — "
        "क्वचिद् द्विविकरणता, क्वचित् त्रिविकरणता. "
        "बहुलग्रहणं सर्वविधिव्यभिचारार्थम्, so this is a licence and "
        "not a rule with an output: nothing here can be derived, only "
        "recognised",
    )


# ---------------------------------------------------------------------------
# 3.1.91 to 3.1.93 — the headings the कृत् section opens with
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Heading:
    """One of the three rules that set up the कृत् section."""

    name: str
    by: str
    why: str
    through: str = ""


#: 3.1.91's extent — आ तृतीयाध्यायपरिसमाप्तेः.
DHATOH_FROM, DHATOH_THROUGH = "3.1.92", "3.4.117"

#: 3.1.95's, given as a boundary rather than a span: प्राक् एतस्मात्
#: ण्वुल्संशब्दनात् — before 3.1.133 ण्वुल्तृचौ, so the last rule it
#: reaches is 3.1.132.
KRTYA_FROM, KRTYA_THROUGH = "3.1.96", "3.1.132"


def dhatoh_heading() -> Heading:
    """
    3.1.91 धातोः — everything to the end of adhyāya 3 is after a root.

    धातुग्रहणम् अनर्थकम्, यङ्विधौ धात्वधिकारात्: the vṛtti raises the
    objection that the word is redundant, 3.1.22's धातोः being still in
    force — and answers it twice. कृदुपपदसंज्ञार्थं तर्हि: the heading
    is needed so that 3.1.92's उपपद and 3.1.93's कृत् apply HERE and
    not earlier. And आर्धधातुकसंज्ञार्थं च द्वितीयं धातुग्रहणं
    कर्तव्यम् — a second धातोः is wanted so that 3.4.114's आर्धधातुक
    reaches what is prescribed after a root and not after a stem:
    इह मा भूत् — लूभ्यां लूभिः.
    """
    return Heading(
        "dhātoḥ", "3.1.91",
        "धातोः — an अधिकार to the end of adhyāya 3: आ "
        "तृतीयाध्यायपरिसमाप्तेः. Everything enumerated from here is "
        "added after a ROOT. The vṛtti asks whether the word is not "
        "redundant and gives two reasons it is not — the two names "
        "3.1.92 and 3.1.93 confer are to hold in this stretch and not "
        "before it, and 3.4.114's आर्धधातुक is to reach what is "
        "prescribed after a root: इह मा भूत् लूभ्यां लूभिः",
        through=DHATOH_THROUGH,
    )


def upapada(*, in_locative: bool = False) -> object:
    """
    3.1.92 तत्रोपपदं सप्तमीस्थम् — what a rule of this section states in
    the locative is called उपपद, a word that must stand beside.

    स्थग्रहणं सूत्रेषु सप्तमीनिर्देशप्रतिपत्त्यर्थम्: without स्थ the
    name would attach only where a locative is actually heard, and
    rules that carry one down by anuvṛtti would be left out —
    स्तम्बेरमः, कर्णेजपः. With it, सर्वत्र भवति.

    And the name is अन्वर्थ, read for what it means: गुरुसंज्ञाकरणम्
    अन्वर्थसंज्ञाविज्ञाने सति समर्थपरिभाषाव्यापारार्थम् — a heavy name
    is chosen so that 2.1.1 समर्थः पदविधिः has something to act on, and
    पश्य कुम्भम्, करोति कटम् get no affix.
    """
    if not in_locative:
        return Heading(
            "", "",
            "तत्रोपपदं सप्तमीस्थम् — only what a rule of this section "
            "states in the LOCATIVE bears the name. A word named in "
            "any other case is not an उपपद",
        )
    return Heading(
        "upapada", "3.1.92",
        "तत्रोपपदं सप्तमीस्थम् — कर्मण्यण् (3.2.1) states कर्मणि in the "
        "locative, so the object is an उपपद and कुम्भकारः is formed. "
        "स्थग्रहणं सूत्रेषु सप्तमीनिर्देशप्रतिपत्त्यर्थम्: the स्थ makes "
        "the name reach every rule that carries a locative down, not "
        "only those that state one — सर्वत्र भवति",
    )


def krt(*, affix: str = "", is_tin: bool = False) -> object:
    """
    3.1.93 कृदतिङ् — in this section, any affix but a तिङ् is a कृत्.

    कर्तव्यम्, करणीयम्. अतिङिति किम्? चीयात्, स्तूयात् — those are
    तिङ् endings and keep their own name. कृत्प्रदेशाः: where the name
    is used, beginning with 1.2.46 कृत्तद्धितसमासाश्च, which is
    codified.
    """
    if is_tin:
        return Heading(
            "", "",
            "अतिङिति किम्? चीयात्, स्तूयात् — a तिङ् ending is named by "
            "1.4.104 and keeps that name. The exception is what makes "
            "कृत् mean the non-finite affixes",
        )
    return Heading(
        "kṛt", "3.1.93",
        f"कृदतिङ् — in the धातोः section an affix that is not a तिङ् "
        f"bears the name कृत्: कर्तव्यम्, करणीयम्. The name is what "
        f"1.2.46 कृत्तद्धितसमासाश्च then uses to call the whole word a "
        f"प्रातिपदिक{', and ' + affix + ' is one' if affix else ''}",
    )


def in_the_dhatoh_section(sutra_id: str) -> bool:
    """Whether 3.1.91's heading reaches this sūtra."""
    def order(sid: str) -> Tuple[int, ...]:
        return tuple(int(p) for p in sid.split("."))

    return order(DHATOH_FROM) <= order(sutra_id) <= order(DHATOH_THROUGH)


def krtya(*, affix: str = "", sutra_id: str = "") -> object:
    """
    3.1.95 कृत्याः — the affixes named from here to 3.1.133.

    प्राक् एतस्मात् ण्वुल्संशब्दनात् — the range is given by naming the
    rule it stops before, not by naming its end, which is how this
    grammar writes most of its headings. The vṛtti gives no example
    here and says why: तत्रैवोदाहरिष्यामः, the examples belong to the
    rules that add the affixes.

    कृत्याः is PLURAL, and the Nyāsa offers two reasons — बहुत्वात्
    संज्ञिनाम्, there being many things named; or
    अनुक्तकृत्प्रत्ययसंग्रहार्थम्, to gather in कृत् affixes not
    separately listed, which is why a vārttika adding केलिमर is not
    needed.

    कृत्यप्रदेशाः: where the name is used — 2.1.33 कृत्यैरधिकार्थवचने
    and 2.3.71 कृत्यानां कर्तरि वा, both codified. So this heading is
    what those two rules of adhyāya 2 were waiting on.
    """
    if sutra_id and not in_the_krtya_section(sutra_id):
        return Heading(
            "", "",
            f"प्राक् एतस्मात् ण्वुल्संशब्दनात् — 3.1.95 reaches "
            f"{KRTYA_FROM} to {KRTYA_THROUGH}, and {sutra_id} is "
            f"outside it. 3.1.133 ण्वुल्तृचौ is where it stops",
        )
    return Heading(
        "kṛtya", "3.1.95",
        f"कृत्याः — an अधिकार over {KRTYA_FROM} to {KRTYA_THROUGH}: "
        f"प्राक् एतस्मात् ण्वुल्संशब्दनात्, the range given by naming "
        f"the rule it stops before. Every affix enumerated there bears "
        f"the name{', and ' + affix + ' is one' if affix else ''}. "
        f"कृत्यप्रदेशाः — 2.1.33 कृत्यैरधिकार्थवचने and 2.3.71 "
        f"कृत्यानां कर्तरि वा are where it is used, and both are "
        f"codified: this heading is what those two were waiting on",
        through=KRTYA_THROUGH,
    )


def in_the_krtya_section(sutra_id: str) -> bool:
    """Whether 3.1.95's heading reaches this sūtra."""
    def order(sid: str) -> Tuple[int, ...]:
        return tuple(int(p) for p in sid.split("."))

    return order(KRTYA_FROM) <= order(sutra_id) <= order(KRTYA_THROUGH)
