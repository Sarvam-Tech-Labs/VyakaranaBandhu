# -*- coding: utf-8 -*-
"""
2.4.73 and 2.4.75 to 2.4.85 — the affixes this pāda takes away last.

Three groups and a closing rule. The first carries on 2.4.72's elision
of शप्; the second takes away सिच् and ले; the third carries on 2.4.71's
elision of सुप्, now after an अव्यय; and the pāda ends by naming three
endings outright.

    2.4.73 बहुलं छन्दसि              शप् goes variously, in the Veda
    2.4.75 जुहोत्यादिभ्यः श्लुः       and after the third gaṇa, श्लु
    2.4.76 बहुलं छन्दसि              श्लु variously, in the Veda
    2.4.77 गातिस्थाघुपाभूभ्यः सिचः…   सिच् goes after five roots
    2.4.78 विभाषा घ्राधेट्शाच्छासः    optionally after five more
    2.4.79 तनादिभ्यस्तथासोः           optionally after the eighth gaṇa
    2.4.80 मन्त्रे घसह्वर…लेः         ले goes after ten roots, in a mantra
    2.4.81 आमः                       and after आम्
    2.4.82 अव्ययादाप्सुपः             आप् and सुप् go after an अव्यय
    2.4.83 नाव्ययीभावादतोऽम्त्वपञ्चम्याः  but not after this one — अम् instead
    2.4.84 तृतीयासप्तम्योर्बहुलम्      and variously for two of the cases
    2.4.85 लुटः प्रथमस्य डारौरसः      three endings, named outright

**श्लु rather than लुक्, and the vṛtti says why.** 2.4.75 could have
said लुक्, which was already running from 2.4.72 — instead it names a
different elision: लुकि प्रकृते श्लुविधानं द्विर्वचनार्थम्. A श्लु is
what triggers 6.1.10 श्लौ, the reduplication, and a लुक् would not
have. जुहोति, बिभर्ति, नेनेक्ति exist because of which elision was
chosen. 1.1.61 names the three apart precisely so that this kind of
choice can be made.

**2.4.77 names two roots that are already substitutes.** The vārttika
गापोः … इण्पिबत्योर्ग्रहणम् fixes which गा and which पा are meant: the
गा that इण् BECAME at 2.4.45, and the पा of पिबति. Not गायति, to sing,
and not पाति, to protect — अगासीन् नटः and अपासीन् नृपः keep their
सिच्. So a rule twenty-two sūtras earlier in this same pāda supplies
the root this one acts on, and the two have to be read together.

**2.4.83 and 2.4.84 land on the compound section.** उपकुम्भम् is an
अव्ययीभाव, made by 2.1.6 and called neuter by 2.4.18; here it is told
which ending it takes — अम्, and not the elision 2.4.82 would have
given. The fifth case is excepted by name, so उपकुम्भादानय keeps its
ending audible. One pāda builds the compound, another names its
gender, and this one gives it an ending: the same three-way division
that runs through the whole of adhyāya 2.
"""

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.anga import Elided

# ---------------------------------------------------------------------------
# The lists the sūtras name
# ---------------------------------------------------------------------------

#: 2.4.77's five. गा and पा are read narrowly, by the vārttika: the गा
#: that इण् became at 2.4.45, and the पा of पिबति. घु is the class 1.1.20
#: names — दा and धा — so the row covers अदात् and अधात् through it.
SICA_LUK_ROOTS: Tuple[str, ...] = ("gā", "sthā", "ghu", "pā", "bhū")

#: 2.4.78's five, where the elision is a choice. For धेट् the rule makes
#: an OBLIGATION optional — धेटः पूर्वेण नित्ये प्राप्ते विभाषार्थं
#: वचनम्, since धेट् is a घु and 2.4.77 had it already; for the other
#: four nothing had reached them, परिशिष्टानामप्राप्ते.
SICA_VIBHASA_ROOTS: Tuple[str, ...] = ("ghrā", "dheṭ", "śā", "chā", "sā")

#: 2.4.80's ten, in a mantra. वृ is taken for both वृङ् and वृञ्
#: सामान्येन, and आत् is read as "the ā-final one", which the vṛtti
#: identifies as प्रा in आप्रा द्यावापृथिवी.
LE_LUK_ROOTS: Tuple[str, ...] = (
    "ghas", "hvar", "ṇaś", "vṛ", "dah", "āt", "vṛc", "kṛ", "gami",
    "jani",
)

#: 2.4.85's three, यथाक्रमम् — one per number.
LUT_PRATHAMA: Tuple[Tuple[int, str], ...] = ((1, "ḍā"), (2, "rau"),
                                             (3, "ras"))


@dataclass(frozen=True)
class Replaced:
    """An ending named outright rather than elided — 2.4.83 and 2.4.85."""

    gives: str
    by: str
    why: str
    bahulam: bool = False


def verbal_luk(
    *,
    affix: str = "",
    root: str = "",
    gana: str = "",
    parasmaipada: bool = True,
    before: str = "",
    chandas: bool = False,
    mantra: bool = False,
) -> Elided:
    """
    Whether a verbal affix goes — 2.4.73 and 2.4.75 to 2.4.81.

    2.4.72 अदिप्रभृतिभ्यः शपः is codified in `anga` and is not repeated
    here; this run picks up where it stops.
    """
    # --- शप् : 2.4.75, then the Vedic latitude of 2.4.73 and 2.4.76 ---
    if affix == "śap":
        if gana == "juhotyādi" and chandas:
            # 2.4.76 overrides 2.4.75, and the vṛtti's own first
            # examples are the ones where the श्लु FAILS.
            return Elided(
                False, "2.4.76",
                "बहुलं छन्दसि — यत्रोक्तं तत्र न भवति, अन्यत्रापि भवति. "
                "The श्लु 2.4.75 gives fails for these very roots in the "
                "Veda: दाति प्रियाणि, धाति देवम्. And it happens for "
                "roots outside the gaṇa, which 2.4.75 never reached — "
                "पूर्णां विवष्टि, जनिमा विवक्ति. बहुलम् records both, so "
                "neither is a choice being offered",
                elision="",
            )
        if gana == "juhotyādi":
            return Elided(
                True, "2.4.75",
                "जुहोत्यादिभ्यः श्लुः — जुहोति, बिभर्ति, नेनेक्ति. And it "
                "is श्लु and not the लुक् already running: लुकि प्रकृते "
                "श्लुविधानं द्विर्वचनार्थम् — a श्लु is what triggers the "
                "reduplication, and a लुक् would not have. शबनुवर्तते, न "
                "यङ्: it is शप् that is replaced, not the यङ् of 2.4.74",
                elision="ślu",
            )
        if chandas:
            return Elided(
                True, "2.4.73",
                "बहुलं छन्दसि — and बहुलम् cuts both ways here, which the "
                "vṛtti spells out: अदिप्रभृतिभ्य उक्तस्ततो न भवत्यपि, "
                "अन्येभ्यश्च भवति. It fails where 2.4.72 gave it — वृत्रं "
                "हनति, अहिः शयते — and happens where that rule did not: "
                "त्राध्वं नो देवाः",
                elision="luk",
            )
        return Elided(
            False, "",
            "शप् stands. 2.4.72 अदिप्रभृतिभ्यः शपः takes it away after "
            "the second gaṇa, and that rule is codified apart from this "
            "run",
            elision="",
        )

    # --- सिच् : 2.4.77 to 2.4.79 ---------------------------------------
    if affix == "sic":
        if before in ("ta", "thās") and gana == "tanādi":
            return Elided(
                True, "2.4.79",
                "तनादिभ्यस्तथासोः — अतत beside अतनिष्ट, अतथाः beside "
                "अतनिष्ठाः. थासा साहचर्यादात्मनेपदस्य तशब्दस्य ग्रहणम्: "
                "the त meant is the MIDDLE त, kept company by थास्, so "
                "the active अतनिष्ट यूयम् is untouched",
                elision="luk",
            )
        if not parasmaipada:
            return Elided(
                False, "",
                "परस्मैपदेष्विति किम्? अगासातां ग्रामौ देवदत्तेन, "
                "अघ्रासातां सुमनसौ देवदत्तेन — 2.4.77 and 2.4.78 hold in "
                "the active only",
                elision="",
            )
        if root in SICA_VIBHASA_ROOTS:
            return Elided(
                True, "2.4.78",
                f"विभाषा घ्राधेट्शाच्छासः — अघ्रात् beside अघ्रासीत्, "
                f"अधात् beside अधासीत्. For धेट् this makes a choice of "
                f"what was obligatory, धेटः पूर्वेण नित्ये प्राप्ते "
                f"विभाषार्थं वचनम् — धेट् is a घु and 2.4.77 had it "
                f"already; for the other four nothing had reached them, "
                f"परिशिष्टानामप्राप्ते",
                elision="luk",
            )
        if root in SICA_LUK_ROOTS or _is_ghu(root):
            return Elided(
                True, "2.4.77",
                f"गातिस्थाघुपाभूभ्यः सिचः परस्मैपदेषु — अगात्, अस्थात्, "
                f"अदात्, अधात्, अपात्, अभूत्. And two of the five are "
                f"read narrowly: गापोः … इण्पिबत्योर्ग्रहणम् — the गा "
                f"that इण् BECAME at 2.4.45, and the पा of पिबति. Not "
                f"गायति and not पाति, so अगासीन् नटः and अपासीन् नृपः "
                f"keep their सिच्",
                elision="luk",
            )
        return Elided(
            False, "",
            "No rule of 2.4.77 to 2.4.79 reaches this root, so the सिच् "
            "stands: अगासीत्, अपासीत्",
            elision="",
        )

    # --- ले : 2.4.80 and 2.4.81 ----------------------------------------
    if affix == "le":
        if root == "ām":
            return Elided(
                True, "2.4.81",
                "आमः — ईहांचक्रे, ऊहांचक्रे, ईक्षांचक्रे. No mantra is "
                "needed here; 2.4.80's condition does not carry",
                elision="luk",
            )
        if root in LE_LUK_ROOTS:
            if not mantra:
                return Elided(
                    False, "",
                    f"मन्त्रे — 2.4.80 holds in a mantra only, and {root} "
                    f"keeps its ले outside one",
                    elision="",
                )
            return Elided(
                True, "2.4.80",
                f"मन्त्रे घसह्वरणशवृदहाद्वृच्कृगमिजनिभ्यो लेः — "
                f"अमीमदन्त, मा ह्वार्, प्रणक्, मा न आ धक्, अक्रन्, "
                f"अग्मन्. Two of the ten are read wide: वृ stands for "
                f"वृङ् and वृञ् both, सामान्येन, and आत् means the "
                f"आकारान्त root, which the vṛtti identifies as प्रा in "
                f"आप्रा द्यावापृथिवी",
                elision="luk",
            )
        return Elided(
            False, "",
            "No rule of 2.4.80 or 2.4.81 reaches this, so the ले stands",
            elision="",
        )

    return Elided(
        False, "",
        "This run takes away शप्, सिच् and ले. Another affix is not its "
        "business",
        elision="",
    )


def avyaya_ending(
    *,
    avyayibhava: bool = False,
    ends_in_a: bool = False,
    vibhakti: int = 0,
) -> object:
    """
    What happens to a सुप् or आप् after an indeclinable — 2.4.82 to 2.4.84.

    2.4.82 takes it away; 2.4.83 refuses that for one kind of अव्ययीभाव
    and puts अम् there instead; 2.4.84 makes the अम् a choice for two of
    the cases. Read in that order, because each answers the one before.
    """
    if avyayibhava and ends_in_a:
        if vibhakti == 5:
            return Elided(
                False, "",
                "अपञ्चम्या इति किम्? उपकुम्भादानय — the fifth case is "
                "excepted by name, so 2.4.83's अम् does not reach it and "
                "the ending stays audible. एतस्मिन् प्रतिषिद्धे पञ्चम्याः "
                "श्रवणमेव भवति",
                elision="",
            )
        if vibhakti in (3, 7):
            return Replaced(
                "am", "2.4.84",
                "तृतीयासप्तम्योर्बहुलम् — पूर्वेण नित्यमम्भावे प्राप्ते "
                "वचनमिदम्: 2.4.83 had made the अम् obligatory and this "
                "makes it various. उपकुम्भेन कृतम् beside उपकुम्भं कृतम्, "
                "उपकुम्भे निधेहि beside उपकुम्भं निधेहि. A vārttika holds "
                "it obligatory for ऋद्धि, नदी, समास and संख्यावयव — "
                "सुमद्रम्, उन्मत्तगङ्गम् — and adds बहुलवचनात् सिद्धम्, "
                "the बहुल covers it anyway",
                bahulam=True,
            )
        return Replaced(
            "am", "2.4.83",
            "नाव्ययीभावादतोऽम्त्वपञ्चम्याः — the elision 2.4.82 would "
            "have given is refused, and अम् is put there instead: "
            "उपकुम्भं तिष्ठति, उपकुम्भं पश्य, उपमणिकं तिष्ठति. अत इति "
            "किम्? अधिस्त्रि, अधिकुमारि — an अव्ययीभाव not ending in अ "
            "goes back to 2.4.82 and loses its ending outright",
        )
    return Elided(
        True, "2.4.82",
        "अव्ययादाप्सुपः — after an indeclinable both आप् and सुप् go: "
        "तत्र शालायाम्, यत्र शालायाम् for the आप्, and कृत्वा, हृत्वा "
        "for the सुप्. This is what makes an अव्यय look uninflected: the "
        "ending is added and then taken away",
        elision="luk",
    )


def lut_prathama(*, number: int = 1) -> Replaced:
    """
    2.4.85 लुटः प्रथमस्य डारौरसः — the three endings that close the pāda.

    यथाक्रमम्, one per number, and for the middle as well as the active:
    कर्ता, कर्तारौ, कर्तारः; अध्येता, अध्येतारौ, अध्येतारः. प्रथमस्येति
    किम्? श्वः कर्तासि — only the third person is replaced.
    """
    for n, ending in LUT_PRATHAMA:
        if n == number:
            shown = {1: "कर्ता, अध्येता", 2: "कर्तारौ, अध्येतारौ",
                     3: "कर्तारः, अध्येतारः"}[number]
            return Replaced(
                ending, "2.4.85",
                f"लुटः प्रथमस्य डारौरसः — {shown}. यथाक्रमम्, one "
                f"ending per number, and it reaches the middle as well "
                f"as the active. प्रथमस्येति किम्? श्वः कर्तासि, "
                f"श्वोऽध्येतासे — the other two persons keep theirs. "
                f"This is the last rule of the pāda, and of adhyāya 2",
            )
    raise ValueError(
        f"{number} is not a number: 2.4.85 gives one ending for each of "
        f"1, 2 and 3")


def _is_ghu(root: str) -> bool:
    """
    2.4.77's घु is not a root but the class 1.1.20 दाधा ध्वदाप् names —
    and that rule is codified, so it is asked. दा and धा written into
    the list here would be a second statement of it, and 1.1.20 has
    conditions of its own that a copied pair would quietly lose.
    """
    from src.astadhyayi.samjna import is_ghu

    return bool(root) and is_ghu(root)
