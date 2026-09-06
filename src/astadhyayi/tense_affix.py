# -*- coding: utf-8 -*-
"""
3.1.33 to 3.1.67 — the affix a lakāra brings with it.

A lakāra is replaced by endings in 3.4, but between the root and those
endings something else usually stands, and this run says what. Two
groups:

    3.1.33 स्यतासी लृलुटोः            स्य for लृ, तासि for लुट्
    3.1.34 सिब्बहुलं लेटि              सिप्, variously, in लेट्
    3.1.35 कास्प्रत्ययादाममन्त्रे लिटि  आम् in the perfect
    3.1.36 इजादेश्च गुरुमतोऽनृच्छः      and after these stems
    3.1.37 दयायासश्च                  and after three roots
    3.1.38 उषविदजागृभ्योऽन्यतरस्याम्    optionally after three more
    3.1.39 भीह्रीभृहुवां श्लुवच्च        and after four, doubling as under श्लु
    3.1.40 कृञ् चानुप्रयुज्यते लिटि      and a second verb follows it
    3.1.41 विदाङ्कुर्वन्त्वित्यन्यतरस्याम् one form fixed whole
    3.1.42 अभ्युत्सादयाम्…              and more, in the Veda

    3.1.43 च्लि लुङि                   च्लि in the aorist
    3.1.44 च्लेः सिच्                   and it becomes सिच्
    3.1.45 शल इगुपधादनिटः क्सः          or क्स
    3.1.46 श्लिष आलिङ्गने               क्स, for one root in one sense
    3.1.47 न दृशः                      but not after दृश्
    3.1.48 णिश्रिद्रुस्रुभ्यः कर्तरि चङ्  or चङ्
    3.1.49 विभाषा धेट्श्व्योः            optionally, after two more
    3.1.50 गुपेश्छन्दसि                 and after गुप्, in the Veda
    3.1.51 नोनयति…                     but not after these four, there
    3.1.52 अस्यतिवक्तिख्यातिभ्योऽङ्      or अङ्
    3.1.53 लिपिसिचिह्वश्च               and after three more
    3.1.54 आत्मनेपदेष्वन्यतरस्याम्       optionally, in the middle
    3.1.55 पुषादिद्युताद्यॢदितः…         and after three classes of root
    3.1.56 सर्तिशास्त्यर्तिभ्यश्च        and after three more
    3.1.57 इरितो वा                    optionally after an इरित् root
    3.1.58 जॄस्तम्भु…च                  and optionally after eight more
    3.1.59 कृमृदृरुहिभ्यश्छन्दसि         and after four, in the Veda
    3.1.60 चिण् ते पदः                  or चिण्, for पद् before त
    3.1.61 दीपजनबुध…अन्यतरस्याम्         optionally after six
    3.1.62 अचः कर्मकर्तरि               after a vowel, where the object acts
    3.1.63 दुहश्च                      and after दुह्
    3.1.64 न रुधः                      but not after रुध्
    3.1.65 तपोऽनुतापे च                 nor after तप्, of remorse
    3.1.66 चिण् भावकर्मणोः               and चिण् for the act or the object
    3.1.67 सार्वधातुके यक्               यक् before a सार्वधातुक

**च्लि exists to be replaced.** 3.1.43 puts it there and says nothing
about what it looks like; the Kāśikā admits as much — अस्य सिजादीन्
आदेशान् वक्ष्यति, तत्रैवोदाहरिष्यामः, we shall give the examples under
those. It is a placeholder whose whole purpose is to give the next
twenty-three rules something to name. So `cli_becomes` returns a
substitute always, and 3.1.43 is codified as the rule that creates the
slot rather than as one that produces a form.

**3.1.40 reaches back into 2.4.** कृञ् is a प्रत्याहार and takes कृ, भू
and अस् together; the vṛtti then draws a consequence — तत्सामर्थ्याद्
अस्तेर्भूभावो न भवति. 2.4.52 अस्तेर्भूः would have turned अस् into भू
and पाचयामास could never be formed, so the very fact that this rule
names अस् through a प्रत्याहार keeps that rule off. Codified as a
condition on 2.4.52's side of the question and held by a test, since
the claim is about a rule in another adhyāya.

**पुषादि is the दिवादि one.** 3.1.55 names a गण that is read in more
than one place, and the vṛtti says which is meant: पुषादिर्
दिवाद्यन्तर्गणो गृह्यते, न भ्वादिक्र्याद्यन्तर्गणः — the sub-gaṇa
inside the fourth class, not the ones inside the first and ninth. Same
shape as 2.4.58's कौरव्य, where one spelling was two words.
"""

from dataclasses import dataclass
from typing import Optional, Tuple

# ---------------------------------------------------------------------------
# The lists the sūtras name
# ---------------------------------------------------------------------------

#: 3.1.37's three.
DAYADI: Tuple[str, ...] = ("day", "ay", "ās")

#: 3.1.38's three, where आम् is a choice.
USADI: Tuple[str, ...] = ("uṣ", "vid", "jāgṛ")

#: 3.1.39's four, which also double as they would under श्लु — and the
#: vṛtti says what that means: किं पुनस्तत्? द्वित्वम् इत्त्वं च.
BHIYADI: Tuple[str, ...] = ("bhī", "hrī", "bhṛ", "hu")

#: 3.1.48's three named roots, beside any stem in णि.
SRIYADI: Tuple[str, ...] = ("śri", "dru", "sru")

#: 3.1.51's four, where the Veda refuses चङ्.
UNAYADI: Tuple[str, ...] = ("ūna", "dhvan", "ila", "arda")

#: 3.1.52's three.
ASYADI: Tuple[str, ...] = ("as", "vac", "khyā")

#: 3.1.53's three, where 3.1.54 then makes the middle a choice. The
#: vṛtti notes the split is for that: पृथग्योग उत्तरार्थः.
LIPYADI: Tuple[str, ...] = ("lip", "sic", "hve")

#: 3.1.56's three. पृथग्योगकरणम् आत्मनेपदार्थम् — split off so the
#: middle is reached too, समरन्त.
SARTYADI: Tuple[str, ...] = ("sṛ", "śās", "ṛ")

#: 3.1.58's eight, where अङ् is a choice.
JRYADI: Tuple[str, ...] = (
    "jṝ", "stambhu", "mrucu", "mlucu", "grucu", "glucu", "gluñcu", "śvi",
)

#: 3.1.59's four, in the Veda.
KRMRADI: Tuple[str, ...] = ("kṛ", "mṛ", "dṛ", "ruh")

#: 3.1.61's six, where चिण् before त is a choice.
DIPADI: Tuple[str, ...] = ("dīp", "jan", "budh", "pūr", "tāy", "pyāy")

#: 3.1.40's प्रत्याहार. कृञिति प्रत्याहारेण कृभ्वस्तयो गृह्यन्ते — the
#: three auxiliaries the perfect is built with.
KRBHVASTI: Tuple[str, ...] = ("kṛ", "bhū", "as")


@dataclass(frozen=True)
class Added:
    """An affix put after the root, and by which rule."""

    gives: str
    by: str
    why: str
    optional: bool = False
    bahulam: bool = False
    #: A further operation the same rule states — 3.1.39's doubling.
    also: str = ""


@dataclass(frozen=True)
class NotAdded:
    """That no rule of the run reaches this. ``by`` names a प्रतिषेध."""

    by: str
    why: str
    gives: str = ""


def tense_affix(
    *,
    lakara: str = "",
    root: str = "",
    affix_final: bool = False,
    ijadi_guru: bool = False,
    mantra: bool = False,
) -> object:
    """
    What stands between root and endings — 3.1.33 to 3.1.42.

    The aorist is not here: लुङ् takes च्लि by 3.1.43, and everything
    that happens to it is :func:`cli_becomes`.
    """
    if lakara in ("lṛṭ", "lṛṅ"):
        return Added(
            "sya", "3.1.33",
            "स्यतासी लृलुटोः, यथासंख्यम् — करिष्यति, अकरिष्यत्. लृ is "
            "given without its marks and stands for both लृट् and लृङ्: "
            "लृरूपम् उत्सृष्टानुबन्धं सामान्यम् एकमेव",
        )
    if lakara == "luṭ":
        return Added(
            "tāsi", "3.1.33",
            "स्यतासी लृलुटोः — श्वः कर्ता. The इ of तासि is marked "
            "अनुनासिकलोपप्रतिबन्धार्थम्, to stop 6.4.37's elision of a "
            "nasal: मन्ता, संगन्ता keep theirs",
        )
    if lakara == "leṭ":
        return Added(
            "sip", "3.1.34",
            "सिब्बहुलं लेटि — जोषिषत्, तारिषत्, मन्दिषत्; and न च भवति "
            "पताति दिद्युत्. बहुलम् and not an option: both are attested "
            "and neither is offered as a choice",
            bahulam=True,
        )
    if lakara != "liṭ":
        return NotAdded(
            "",
            "No rule of 3.1.33 to 3.1.42 reaches this. The aorist takes "
            "च्लि by 3.1.43 and is asked through `cli_becomes`",
        )

    # 3.1.35 to 3.1.39 — आम् in the perfect.
    if mantra:
        return NotAdded(
            "",
            "अमन्त्र इति किम्? कृष्णो नोनाव — in a mantra the आम् does "
            "not come, though the stem is affix-final",
        )
    if root in BHIYADI:
        return Added(
            "ām", "3.1.39",
            f"भीह्रीभृहुवां श्लुवच्च — बिभयाञ्चकार beside बिभाय, "
            f"जुहवाञ्चकार beside जुहाव. श्लुवत् means what it means "
            f"under 2.4.75, and the vṛtti spells it out: किं पुनस्तत्? "
            f"द्वित्वम् इत्त्वं च — the doubling and the इ",
            optional=True, also="doubled as under श्लु, with इ",
        )
    if root in USADI:
        return Added(
            "ām", "3.1.38",
            "उषविदजागृभ्योऽन्यतरस्याम् — ओषाञ्चकार beside उवोष, "
            "विदाञ्चकार beside विवेद, जागराञ्चकार beside जजागार. "
            "विदेरदन्तत्वप्रतिज्ञानाद् आमि गुणो न भवति",
            optional=True,
        )
    if root in DAYADI:
        return Added(
            "ām", "3.1.37",
            "दयायासश्च — दयाञ्चक्रे, पलायाञ्चक्रे, आसाञ्चक्रे",
        )
    if root == "kās" or affix_final:
        return Added(
            "ām", "3.1.35",
            "कास्प्रत्ययादाममन्त्रे लिटि — कासाञ्चक्रे, and after any "
            "affix-final stem लोलूयाञ्चके. That second half is what "
            "carries the whole सनादि run of 3.1.5 to 3.1.31 into the "
            "perfect: those rules made stems, 3.1.32 called them roots, "
            "and this gives them a perfect",
        )
    if ijadi_guru:
        if root == "ṛcch":
            return NotAdded(
                "",
                "अनृच्छ इति किम्? आनर्च्छ, आनर्च्छतुः, आनर्च्छुः — ऋच्छ् "
                "is इच्-initial and heavy and is still excepted by name",
            )
        return Added(
            "ām", "3.1.36",
            "इजादेश्च गुरुमतोऽनृच्छः — ईहाञ्चक्रे, ऊहाञ्चक्रे. "
            "इजादेरिति किम्? ततक्ष, ररक्ष. गुरुमत इति किम्? इयज, उवप",
        )
    return NotAdded(
        "",
        "No rule of 3.1.35 to 3.1.39 gives this root आम्, so the perfect "
        "is formed without it",
    )


def anuprayoga(*, after_am: bool = True) -> object:
    """
    3.1.40 कृञ् चानुप्रयुज्यते लिटि — a second verb follows the आम्.

    पाचयाञ्चकार, पाचयाम्बभूव, पाचयामास: कृ, भू and अस् all serve, and
    the vṛtti says why all three — कृञिति प्रत्याहारेण कृभ्वस्तयो
    गृह्यन्ते.

    **And that naming keeps 2.4.52 away.** तत्सामर्थ्यादस्तेर्भूभावो
    न भवति: अस्तेर्भूः would have turned अस् into भू, and पाचयामास
    could never be formed. A rule is kept off not by a prohibition but
    by the fact that another rule would be pointless if it applied.
    """
    if not after_am:
        return NotAdded(
            "",
            "3.1.40 follows the आम् of 3.1.35 to 3.1.39. Without one "
            "there is nothing for the second verb to follow",
        )
    return Added(
        "kṛ/bhū/as", "3.1.40",
        "कृञ् चानुप्रयुज्यते लिटि — पाचयाञ्चकार, पाचयाम्बभूव, "
        "पाचयामास. कृञिति प्रत्याहारेण कृभ्वस्तयो गृह्यन्ते, and "
        "तत्सामर्थ्यादस्तेर्भूभावो न भवति — 2.4.52 अस्तेर्भूः is "
        "kept off because this rule would be pointless if it applied",
    )


# ---------------------------------------------------------------------------
# 3.1.43 to 3.1.66 — च्लि and what it becomes
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Cli:
    """One rule replacing च्लि, as its conditions."""

    sutra: str
    gives: str
    of: Tuple[str, ...] = ()
    gana: str = ""
    #: कर्तरि, भावकर्मणोः, कर्मकर्तरि — whose action the form is about.
    voice: str = ""
    #: परस्मैपद or आत्मनेपद, where a rule confines itself to one.
    #: The row keeps the Sanskrit name; the caller passes a bool,
    #: under the name 2.4.44 already settled on for this notion.
    pada: str = ""
    #: An ending the rule names — 3.1.60's त.
    before: str = ""
    sense: str = ""
    chandas: bool = False
    optional: bool = False
    #: Whether the row REFUSES rather than substitutes.
    refuses: bool = False
    #: Phonological conditions 3.1.45 alone states.
    shal_igupadha_anit: bool = False
    ac_final: bool = False
    irit: bool = False
    #: ऌदित् — read off the root's upadeśa, not asserted.
    ldit: bool = False
    nyanta: bool = False
    why: str = ""


CLI: Tuple[Cli, ...] = (
    Cli("3.1.44", "sic",
        why="च्लेः सिच् — अकार्षीत्, अहार्षीत्. The default, and every "
            "rule after it is an अपवाद. A vārttika makes it a choice "
            "for six roots: अस्प्राक्षीत्, अस्पार्क्षीत्, अस्पृक्षत्"),
    Cli("3.1.45", "ksa", shal_igupadha_anit=True,
        why="शल इगुपधादनिटः क्सः — अधुक्षत्, अलिक्षत्. Three conditions "
            "and a counter for each: शल इति किम्? अभैत्सीत्. इगुपधादिति "
            "किम्? अधाक्षीत्. अनिट इति किम्? अकोषीत्, अमोषीत्"),
    Cli("3.1.46", "ksa", of=("śliṣ",), sense="āliṅgana",
        why="श्लिष आलिङ्गने — आश्लिक्षत् कन्यां देवदत्तः. "
            "अत्र नियमार्थमेतत्: श्लिष् already met 3.1.45's conditions, "
            "so this RESTRICTS rather than grants — क्स only where "
            "embracing is meant. आलिङ्गन इति किम्? समाश्लिषज्जतु काष्ठम्"),
    Cli("3.1.47", "", of=("dṛś",), refuses=True,
        why="न दृशः — the क्स 3.1.45 would have given is refused. "
            "अस्मिन् प्रतिषिद्धे इरितो वा इत्यङ्सिचौ भवतः: with it out "
            "of the way 3.1.57 answers instead, and BOTH forms stand — "
            "अदर्शत् and अद्राक्षीत्"),
    # 3.1.48 names two ways in — any ण्यन्त stem, OR three roots — so
    # it is two rows. Written as one, the named list shut the
    # causatives out and अचीकरत् reached nothing. The third sūtra in
    # this adhyāya to need splitting for the same reason, after 3.1.25
    # and 3.1.55.
    Cli("3.1.48", "caṅ", nyanta=True, voice="kartari",
        why="णिश्रिद्रुस्रुभ्यः कर्तरि चङ् — ण्यन्तेभ्यो धातुभ्यः, any "
            "stem in णि: अचीकरत्. सिजपवादश्चङ् विधीयते, an अपवाद of "
            "3.1.44. ङकारो गुणवृद्धिप्रतिषेधार्थः, चकारः 6.1.11 चङि "
            "इति विशेषणार्थः — two marks, two later rules. कर्तरीति "
            "किम्? अकारयिषातां कटौ देवदत्तेन"),
    Cli("3.1.48", "caṅ", of=SRIYADI, voice="kartari",
        why="…श्रिद्रुस्रुभ्यः कर्तरि चङ् — the three roots the same "
            "sūtra names beside the causatives: अशिश्रियत्, "
            "अदुद्रुवत्, असुस्रुवत्. These take चङ् without being "
            "ण्यन्त, which is why they had to be named at all"),
    Cli("3.1.49", "caṅ", of=("dheṭ", "śvi"), optional=True,
        why="विभाषा धेट्श्व्योः — अदधत्; and on the सिच् side 2.4.78 "
            "elides it, अधात् beside अधासीत्. अशिश्वियत्, and the vṛtti "
            "wants अङ् in the mix too: अश्वत्, अश्वयीत्"),
    Cli("3.1.50", "caṅ", of=("gup",), chandas=True, optional=True,
        why="गुपेश्छन्दसि — अजूगुपतम्, where the आय of 3.1.28 is not "
            "there: यत्र आयप्रत्ययो नास्ति, तत्रायं विधिः. In ordinary "
            "speech the चङ् form is the one that does NOT stand — "
            "भाषायां तु चङन्तं वर्जयित्वा शिष्टं रूपत्रयं भवति"),
    Cli("3.1.51", "", of=UNAYADI, nyanta=True, chandas=True, refuses=True,
        why="नोनयतिध्वनयत्येलयत्यर्दयतिभ्यः — in the Veda the चङ् "
            "3.1.48 would have given these four is refused: काममूनयीः, "
            "मा त्वाग्निर्ध्वनयीत्. In ordinary speech it comes — "
            "औनिनत्, अदिध्वनत्"),
    Cli("3.1.52", "aṅ", of=ASYADI, voice="kartari",
        why="अस्यतिवक्तिख्यातिभ्योऽङ् — पर्यास्थत्, अवोचत्, आख्यत्. "
            "अस्यतेः पुषादिपाठादेव अङि सिद्धे पुनर्ग्रहणम् "
            "आत्मनेपदार्थम्: अस् is already in 3.1.55's गण, so naming it "
            "again is for the middle — पर्यास्थत, पर्यास्थेताम्"),
    Cli("3.1.53", "aṅ", of=LIPYADI,
        why="लिपिसिचिह्वश्च — अलिपत्, असिचत्, आह्वत्. पृथग्योग "
            "उत्तरार्थः, split off so 3.1.54 can reach these three "
            "alone"),
    Cli("3.1.54", "aṅ", of=LIPYADI, pada="ātmanepada", optional=True,
        why="आत्मनेपदेष्वन्यतरस्याम् — पूर्वेण प्राप्ते विभाषारभ्यते: "
            "3.1.53 had made it obligatory and this makes it a choice "
            "in the middle. अलिपत beside अलिप्त, असिचत beside असिक्त"),
    # 3.1.55 names three groups and they are not found the same way.
    # पुषादि and द्युतादि are sub-gaṇas the gaṇapāṭha on disk holds no
    # members for, so they are asserted; ऌदित् is written on the root
    # in the dhātupāṭha and is read from there.
    Cli("3.1.55", "aṅ", gana="puṣādi", pada="parasmaipada",
        why="पुषादिद्युताद्यॢदितः परस्मैपदेषु — अपुषत्, अद्युतत्, "
            "अश्वितत्. And WHICH पुषादि is stated, because the name is "
            "read in more than one place: पुषादिर् दिवाद्यन्तर्गणो "
            "गृह्यते, न भ्वादिक्र्याद्यन्तर्गणः — the sub-gaṇa inside "
            "the FOURTH class. परस्मैपदेष्विति किम्? व्यद्योतिष्ट, "
            "अलोटिष्ट"),
    Cli("3.1.55", "aṅ", ldit=True, pada="parasmaipada",
        why="…ॢदितः परस्मैपदेषु — the third group of the same sūtra, "
            "and the only one that can be read from the corpus: a root "
            "marked with ऌ. गम्ऌ gives अगमत्, शक्ऌ gives अशकत्. Which "
            "marks a root carries is 1.3.2 उपदेशेऽजनुनासिक इत्'s "
            "question, so it is asked rather than restated"),
    Cli("3.1.56", "aṅ", of=SARTYADI, pada="parasmaipada",
        why="सर्तिशास्त्यर्तिभ्यश्च — असरत्, अशिषत्, आरत्. "
            "पृथग्योगकरणम् आत्मनेपदार्थम्, split so the middle is "
            "reached too: समरन्त. चकारः परस्मैपदेष्वित्यनुकर्षणार्थः, "
            "and the vṛtti notes the च's work is felt further on"),
    Cli("3.1.57", "aṅ", irit=True, pada="parasmaipada", optional=True,
        why="इरितो वा — अभिदत् beside अभैत्सीत्, अच्छिदत् beside "
            "अच्छैत्सीत्. परस्मैपदेष्वित्येव: अभित्त, अच्छित्त keep the "
            "सिच्. This is also what answers दृश् once 3.1.47 has "
            "refused it the क्स"),
    Cli("3.1.58", "aṅ", of=JRYADI, optional=True,
        why="जॄस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च — वेति "
            "वर्तते, the option carried down: अजरत् beside अजारीत्, "
            "अस्तभत् beside अस्तम्भीत्. स्तम्भु is a सौत्र root, one the "
            "sūtra itself supplies"),
    Cli("3.1.59", "aṅ", of=KRMRADI, chandas=True,
        why="कृमृदृरुहिभ्यश्छन्दसि — अकरत्, अमरत्, अदरत्, आरुहत्. "
            "छन्दसीति किम्? अकार्षीत्, अमृत, अदारीत्, अरुक्षत् — in "
            "ordinary speech each takes something else"),
    Cli("3.1.60", "ciṇ", of=("pad",), before="ta",
        why="चिण् ते पदः — उदपादि सस्यम्, समपादि भैक्षम्. And the त "
            "meant is one particular ending: सामर्थ्यात् "
            "आत्मनेपदैकवचनं गृह्यते. त इति किम्? उदपत्साताम्, उदपत्सत"),
    Cli("3.1.61", "ciṇ", of=DIPADI, before="ta", optional=True,
        why="दीपजनबुधपूरितायिप्यायिभ्योऽन्यतरस्याम् — अदीपि beside "
            "अदीपिष्ट, अजनि beside अजनिष्ट, अबोधि beside अबुद्ध. "
            "चिण् त इति वर्तते, both carried down"),
    Cli("3.1.62", "ciṇ", ac_final=True, voice="karmakartari", before="ta",
        optional=True,
        why="अचः कर्मकर्तरि — अकारि कटः स्वयमेव beside अकृत कटः "
            "स्वयमेव. प्राप्तविभाषेयम्: an option over what was already "
            "optional. अच इति किम्? अभेदि काष्ठं स्वयमेव. "
            "कर्मकर्तरीति किम्? अकारि कटो देवदत्तेन"),
    Cli("3.1.63", "ciṇ", of=("duh",), voice="karmakartari", before="ta",
        optional=True,
        why="दुहश्च — अदोहि गौः स्वयमेव beside अदुग्ध गौः स्वयमेव. "
            "दुह् is consonant-final, so 3.1.62 could not have reached "
            "it. कर्मकर्तरीत्येव: अदोहि गौर्गोपालकेन is another matter"),
    Cli("3.1.64", "", of=("rudh",), voice="karmakartari", refuses=True,
        why="न रुधः — the चिण् is refused where the object acts: "
            "अन्ववारुद्ध गौः स्वयमेव"),
    Cli("3.1.65", "", of=("tap",), sense="anutāpa", refuses=True,
        why="तपोऽनुतापे च — नेति वर्तते, the prohibition carried down. "
            "अनुतापः पश्चात्तापः, remorse. तस्य ग्रहणम् "
            "अकर्मकर्त्रर्थम्: naming the sense EXTENDS the refusal past "
            "कर्मकर्तृ to भाव and कर्मन् as well — अतप्त तपस्तापसः, "
            "अन्ववातप्त पापेन कर्मणा"),
    Cli("3.1.66", "ciṇ", voice="bhāvakarmaṇoḥ", before="ta",
        why="चिण् भावकर्मणोः — अशायि भवता for the act, अकारि कटो "
            "देवदत्तेन and अहारि भारो यज्ञदत्तेन for the object. "
            "चिण्ग्रहणं विस्पष्टार्थम्, the affix named again only for "
            "clarity"),
)


def cli_becomes(
    root: str = "",
    *,
    voice: str = "kartari",
    atmanepada: bool = False,
    before: str = "",
    sense: str = "",
    chandas: bool = False,
    shal_igupadha_anit: bool = False,
    ac_final: bool = False,
    nyanta: bool = False,
    gana: str = "",
) -> object:
    """
    What च्लि becomes in the aorist — 3.1.44 to 3.1.66.

    3.1.43 च्लि लुङि puts it there and describes nothing; every form
    comes from one of the rules that replace it, which is why this
    function always answers with a substitute or with the प्रतिषेध that
    refused one.

    The LAST matching row wins, as it did in 2.4: 3.1.54 is written to
    make optional what 3.1.53 made obligatory, and 3.1.47, 3.1.51,
    3.1.64 and 3.1.65 are प्रतिषेध against rules before them. Taking the
    first would make every one of those unreachable.
    """
    # इरित् and ऌदित् are written on the root in the dhātupāṭha, and
    # 1.3.2 is what makes those marks its — so they are asked, not
    # taken from the caller. A rule's condition that the corpus can
    # answer should never be something the reader has to assert.
    from src.astadhyayi.pada import root_its

    marks = root_its(root) if root else frozenset()
    irit = {"i", "r"} <= set(marks)
    ldit = "ḷ" in marks

    matched: list = []
    for row in CLI:
        if row.ldit and not ldit:
            continue
        if row.gana and gana != row.gana:
            continue
        if row.of and root not in row.of:
            continue
        if row.voice and row.voice != voice:
            continue
        if row.pada == "ātmanepada" and not atmanepada:
            continue
        if row.pada == "parasmaipada" and atmanepada:
            continue
        if row.before and row.before != before:
            continue
        if row.sense and row.sense != sense:
            continue
        if row.chandas and not chandas:
            continue
        if row.shal_igupadha_anit and not shal_igupadha_anit:
            continue
        if row.ac_final and not ac_final:
            continue
        if row.irit and not irit:
            continue
        if row.nyanta and not nyanta:
            continue
        matched.append(row)
    if not matched:                         # 3.1.44 always matches
        raise AssertionError("3.1.44 is unconditional and must match")
    found = max(matched, key=_weight)
    if found.refuses:
        return NotAdded(found.sutra, found.why)
    return Added(found.gives, found.sutra, found.why,
                 optional=found.optional)


def _weight(row: Cli) -> Tuple[int, int]:
    """
    Which of several reaching rows answers.

    A प्रतिषेध always wins: it exists to stop the rule that would
    otherwise have applied, so a refusal read after that rule could
    never fire. Among the rest the MORE SPECIFIC answers — विशेष over
    सामान्य — and the text's own order breaks a tie, `max` being
    stable.

    दुह् is why this is needed. It is दुहिँर् in the dhātupāṭha, so
    3.1.57 इरितो वा genuinely reaches it, and taking simply the last
    match gave अङ् where the vṛtti gives अधुक्षत् by 3.1.45. Both rules
    are right about दुह्; the question is which answers, and three
    stated conditions say more than one mark.
    """
    stated = (
        # Parenthesised on purpose: `>` binds looser than `+`, so
        # `len(row.of) > 0 + 3 * ...` reads the whole sum as the right
        # side of one comparison and every row scores False.
        (len(row.of) > 0)
        # 3.1.45 states three conditions in one word — शल्, इगुपध and
        # अनिट् — so it counts for the three it is, not for one.
        + 3 * row.shal_igupadha_anit
        + bool(row.gana) + bool(row.voice) + bool(row.pada)
        + bool(row.before) + bool(row.sense) + row.chandas
        + row.ac_final + row.irit + row.ldit + row.nyanta
    )
    return (1 if row.refuses else 0), stated


def _in_gana(word: str, sutra: str, name: str) -> bool:
    from src.astadhyayi.formation import gana_items

    try:
        return word in gana_items(sutra, name)
    except Exception:                       # noqa: BLE001 — corpus absent
        return False


def cli_slot() -> Added:
    """
    3.1.43 च्लि लुङि — the slot every later rule fills.

    इकार उच्चारणार्थः, चकारः स्वरार्थः: the इ is there to make it
    sayable and the च for the accent, so nothing of the affix survives
    into a form. अस्य सिजादीन् आदेशान् वक्ष्यति — the vṛtti gives no
    example here and says the examples belong to the rules that replace
    it.
    """
    return Added(
        "cli", "3.1.43",
        "च्लि लुङि — a placeholder in the aorist, put there so that "
        "3.1.44 to 3.1.66 have something to replace. इकार उच्चारणार्थः, "
        "चकारः स्वरार्थः, and अस्य सिजादीन् आदेशान् वक्ष्यति: the vṛtti "
        "offers no example, because no form ever shows it",
    )


def sarvadhatuke_yak(*, voice: str = "bhāvakarmaṇoḥ") -> object:
    """
    3.1.67 सार्वधातुके यक् — the passive and impersonal stem-former.

    आस्यते भवता for the act, क्रियते कटः and गम्यते ग्रामः for the
    object. ककारो गुणवृद्धिप्रतिषेधार्थः, the क् marked to keep
    strengthening off.

    A vārttika adds कर्मकर्तृ and gives the reason as a conflict
    settled by strength: यग्निवधाने कर्मकर्तर्युपसंख्यानम्,
    विप्रतिषेधाद्धि यकः शपो बलीयस्त्वम् — where both यक् and शप् could
    come, यक् is the stronger. क्रियते कटः स्वयमेव, पच्यत ओदनः स्वयमेव.
    """
    if voice not in ("bhāvakarmaṇoḥ", "karmakartari"):
        return NotAdded(
            "",
            "भावकर्मवाचिनि सार्वधातुके परतः — 3.1.67 holds where the "
            "form is about the act or the object. For the agent 3.1.68 "
            "कर्तरि शप् answers instead",
        )
    extra = ("" if voice == "bhāvakarmaṇoḥ" else
             " And the vārttika reaches कर्मकर्तृ too, where यक् beats "
             "शप् — विप्रतिषेधाद्धि यकः शपो बलीयस्त्वम्: क्रियते कटः "
             "स्वयमेव")
    return Added(
        "yak", "3.1.67",
        "सार्वधातुके यक् — आस्यते भवता, शय्यते भवता; क्रियते कटः, "
        "गम्यते ग्रामः. ककारो गुणवृद्धिप्रतिषेधार्थः." + extra,
    )

#: 3.1.41 and 3.1.42 fix forms whole. A निपātana is by definition what
#: the rules do not reach, so these are recorded as the sūtras give
#: them and are not derived — and they answer through their own entry
#: point rather than through a table that would have to pretend.
NIPATANA = {
    "3.1.41": (
        ("vidāṅkurvantu",),
        "विदाङ्कुर्वन्त्वित्यन्यतरस्याम् — विदाङ्कुर्वन्तु beside "
        "विदन्तु. Four things are fixed at once, and the vṛtti lists "
        "them: विदेर्लोटि आम्प्रत्ययः, गुणाभावः, लोटो लुक्, कृञश्च "
        "लोट्परस्यानुप्रयोगः. And इतिकरणः प्रदर्शनार्थः, न केवलं "
        "प्रथमपुरुषबहुवचनम् — the इति marks a specimen, so विदाङ्करोतु, "
        "विदाङ्कुरुतात्, विदाङ्कुरु and the rest all follow",
    ),
    "3.1.42": (
        ("abhyutsādayāmakaḥ", "prajanayāmakaḥ", "cikayāmakaḥ",
         "ramayāmakaḥ", "pāvayāṅkriyāt", "vidāmakran"),
        "अभ्युत्सादयाम्प्रजनयाञ्चिकयाम्रमयामकः "
        "पावयाङ्क्रियाद्विदामक्रन्निति च्छन्दसि — several forms fixed "
        "at once, each suspending something different: आम् in the "
        "aorist for three ण्यन्त roots, आम् with doubling and कुत्व for "
        "चि, आम् in the benedictive for पू, and आम् with गुणाभाव for "
        "विद्. अकः, क्रियात् and अक्रन् are the auxiliaries each takes",
    ),
}


def nipatana(sutra_id: str) -> object:
    """
    3.1.41 and 3.1.42 — forms the sūtra fixes rather than derives.

    Asked of anything else this answers with nothing, because a
    निपātana rule speaks about the forms it names and no others.
    """
    if sutra_id not in NIPATANA:
        return NotAdded(
            "",
            f"{sutra_id} is not one of this run's two निपातन rules. Only "
            f"3.1.41 and 3.1.42 fix forms whole",
        )
    forms, why = NIPATANA[sutra_id]
    return Added(", ".join(forms), sutra_id, why, optional=True)
