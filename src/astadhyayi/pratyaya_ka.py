# -*- coding: utf-8 -*-
"""
७.३.४४–५१ — the क of a feminine, and the ठ of a taddhita.

Eight sūtras about two letters. Before आप् the अ that stands
before an affix's क becomes इ — जटिलिका, कारिका, मुण्डिका — and
four sūtras then refuse that, three of them **उदीचां** and
**आचार्याणाम्**, in the northern teachers' view. Then the ठ of
every taddhita becomes इक (आक्षिकः, लावणिकः), or क after certain
stem-endings (सार्पिष्कः, धानुष्कः, मातृकम्).

**THE FOUR REFUSALS ARE OPINIONS AND ARE MARKED AS SUCH.**
**उदीचांग्रहणं विकल्पार्थम्** — naming the northerners is what
makes the refusal an option, so इभ्यका and इभ्यिका both stand.
7.3.49 then gives a fifth teacher's view, in which the vowel
becomes आ instead: खट्वाका.

**AND ONE SŪTRA IS FOUR CONDITIONS DEEP.** 7.3.44 wants the क to
belong to an AFFIX, the अ to stand BEFORE it, that अ to be short,
and the आप् not to follow a सुप्. The vṛtti tests each with its
own counter-example — शका, पटुका, गोका, राका — and there is a
fifth thing it will not do, which is let the क be an affix all
by itself.

**WHAT THIS MODULE DOES NOT DO.** It says what the sounds become.
Which affix the क belongs to, and where the ठ came from, is
अध्याय ४ and ५'s.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
KA_RUN: Tuple[str, str] = ("7.3.44", "7.3.51")

#: The two views the run records without adopting: the northern
#: teachers', and the teachers' at large.
UDICAM: str = "udīcām ācāryāṇām matena"
ACARYANAM: str = "ācāryāṇām matena"

#: 7.3.47's seven, named out of the इ-substitution.
BHASTRADI: Tuple[str, ...] = (
    "bhastrā", "eṣā", "ajā", "jñā", "dvā", "svā")

#: 7.3.51's stem-endings, before which the ठ becomes क and not
#: इक: सार्पिष्कः, धानुष्कः, मातृकम्, औदश्वित्कः.
ISUS_UK_TA: Tuple[str, ...] = ("is-anta", "us-anta", "uk-anta",
                               "ta-anta")


@dataclass(frozen=True)
class Ka:
    """One rule of 7.3.44–51: what the क or the ठ becomes."""

    sutra: str
    #: `it`, `āt`, `ika`, `ka` — or "" where the rule refuses.
    does: str = ""
    #: What the rule acts on.
    of: Tuple[str, ...] = ()
    #: The stem class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow.
    not_before: Tuple[str, ...] = ()
    #: The named teacher's view this rule records.
    view: str = ""
    refuses: bool = False
    optional: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


KA_TABLE: Tuple[Ka, ...] = (
    Ka(
        "7.3.44", does="it", of=("a-before-pratyaya-ka",),
        before=("āp",), not_before=("sup-para",),
        keeps_out="शका — the क is no affix; मण्डना, रमणा — no क "
                  "at all; पटुका, मृदका — the अ FOLLOWS the क; "
                  "गोका, नौका — no अ; राका, धाका — the आ is "
                  "long, and the तपर shuts it out",
        why="प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः — the अ "
            "before an AFFIX's क becomes इ before आप्, unless "
            "that आप् follows a सुप्: **जटिलिका, मुण्डिका, "
            "कारिका, हारिका; एतिकाश्चरन्ति**.\\n\\n"
            "**AND THE WORD प्रत्ययस्थ IS ARGUED TO BE "
            "DERIVABLE.** **ककारमात्रं प्रत्ययो नास्तीति "
            "सामर्थ्यात् प्रत्ययस्थस्य ग्रहणं शक्यते विज्ञातुम्** "
            "— no affix is a bare क, so the qualification could "
            "have been read out of the rule's own working. It "
            "is written all the same, **स्थग्रहणं "
            "विस्पष्टार्थम्**"),
    Ka(
        "7.3.45", refuses=True, of=("yā", "sā"), before=("āp",),
        blocks=("7.3.44",),
        why="न यासयोः — but not for या and सा: **यका, सका**. And "
            "the two are named as a specimen and not a list — "
            "**या सा इति निर्देशोऽतन्त्रम्, यत्तदोर् "
            "उपलक्षणार्थम् एतत्** — so यकांयकाम् and तकांतकाम् "
            "are refused too. Three vārttikas add more: "
            "**यासयोरित्त्वप्रतिषेधे त्यकन उपसंख्यानम्** giving "
            "उपत्यका; **पावकादीनां छन्दसि** giving पावकाः; and "
            "**आशिषि च** giving जीवका, नन्दका, भवका"),
    Ka(
        "7.3.46", refuses=True, gana="ya-ka-pūrva-ā",
        before=("āp",), view=UDICAM, optional=True,
        blocks=("7.3.44",),
        keeps_out="सांकाश्यिका — the अ does not stand for a long "
                  "आ; अश्विका — no य before it",
        why="उदीचामातः स्थाने यकपूर्वायाः — and in the NORTHERN "
            "teachers' view, an अ that stands in place of a long "
            "आ and has a य or a क before it: **इभ्यका, इभ्यिका; "
            "क्षत्रियका, क्षत्रियिका; चटकका, चटकिका; मूषिकका, "
            "मूषिकिका**.\\n\\n"
            "**AND NAMING THE TEACHERS IS WHAT MAKES IT AN "
            "OPTION.** **उदीचांग्रहणं विकल्पार्थम्** — both "
            "forms stand, and the sūtra records a view rather "
            "than settling one"),
    Ka(
        "7.3.47", refuses=True, of=BHASTRADI, before=("āp",),
        view=UDICAM, optional=True, blocks=("7.3.44",),
        why="भस्त्रैषाऽजाज्ञाद्वास्वानञ्पूर्वाणामपि — and six "
            "stems, with or without a नञ् before them: "
            "**भस्त्रका, भस्त्रिका; एषका, एषिका; अजका, अजिका; "
            "ज्ञका, ज्ञिका; द्वके, द्विके; स्वका, स्विका**. Two "
            "of the six can take no नञ् — **एषाद्वे नञ्पूर्वे न "
            "प्रयोजयतः** — and the vṛtti works out why, from "
            "which ending the compound would take on either "
            "order of operations"),
    Ka(
        "7.3.48", refuses=True, gana="a-bhāṣitapuṃska",
        before=("āp",), view=UDICAM, optional=True,
        blocks=("7.3.44",),
        keeps_out="अखट्विका — the अखट्वा here is *she who has no "
                  "cot*, not a small one, and the अ is not the "
                  "one the rule wants",
        why="अभाषितपुंस्काच्च — and an अ supplied after a stem "
            "with no masculine of its own: **खट्वका, खट्विका; "
            "अखट्वका, अखट्विका; परमखट्वका, परमखट्विका**. In a "
            "बहुव्रीहि it applies only where the कप् has "
            "shortened the vowel, and the vṛtti separates the "
            "two readings of अखट्वा carefully"),
    Ka(
        "7.3.49", does="āt", gana="a-bhāṣitapuṃska",
        before=("āp",), view=ACARYANAM, blocks=("7.3.44",),
        why="आदाचार्याणाम् — and in the TEACHERS' view that same "
            "अ becomes आ: **खट्वाका, अखट्वाका, परमखट्वाका**. A "
            "fifth form beside the four the sūtras before "
            "allow, and again a view recorded rather than "
            "adopted"),
    Ka(
        "7.3.50", does="ika", of=("ṭha",), before=("taddhita",),
        why="ठस्येकः — a taddhita's ठ becomes इक: **आक्षिकः, "
            "शालाकिकः** from 4.4.1's ठक्; **लावणिकः** from "
            "4.4.52's ठञ्.\\n\\n"
            "**AND THE ठ REPLACED IS THE WHOLE AFFIX OR JUST "
            "ITS SOUND, ACCORDING TO HOW AFFIXES ARE READ.** "
            "**ठगादिषु यदि वर्णमात्रं प्रत्ययः, उच्चारणार्थोऽकारः, "
            "तदेहाप्यकार उच्चारणार्थः... संघातग्रहणे तु प्रत्यये "
            "अत्रापि संघातग्रहणम् एव** — the rule works either "
            "way, and the vṛtti sets out both. The Uṇādi कण्ठ "
            "keeps its ठ, **उणादयो बहुलम्**"),
    Ka(
        "7.3.51", does="ka", of=("ṭha",), gana="is-us-uk-ta-anta",
        blocks=("7.3.50",),
        keeps_out="आशिषिकः, औषिकः — the इस् and उस् meant are "
                  "the ones a rule supplies by name, and these "
                  "are not those",
        why="इसुसुक्तान्तात् कः — but after a stem ending in "
            "इस्, उस्, an उक् vowel or त्, the ठ becomes क: "
            "**सार्पिष्कः; धानुष्कः, याजुष्कः; नैषादकर्षुकः, "
            "मातृकम्, पैतृकम्; औदश्वित्कः, शाकृत्कः, "
            "याकृत्कः**. A vārttika adds one more: **दोष "
            "उपसंख्यानम्। दौष्कः**"),
)


def _reaches(row: Ka, what: str, gana: str, before: str,
             view: str) -> bool:
    # `of` names the sound acted on and `gana` the class of the
    # stem it stands in — different dimensions, so a row carrying
    # both is a conjunction. 7.3.50 and 7.3.51 are why: both name
    # the ठ, and only the stem's ending tells them apart.
    if row.of and what not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.before and before not in row.before:
        return False
    if row.not_before and before in row.not_before:
        return False
    # A view is asked for by name or not at all: 7.3.48 and
    # 7.3.49 differ in nothing else, one being the northerners'
    # refusal and one the teachers' आ.
    if view and row.view != view:
        return False
    if not view and row.view == ACARYANAM:
        return False
    return True


def _how_specific(row: Ka, what: str, gana: str) -> int:
    """
    A rule that names what it displaces beats it, and a named
    thing beats a named class.

    7.3.44 against the four that refuse it is what needs the
    first; 7.3.50 against 7.3.51 the second.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.of and what in row.of)
        + 5 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.before)
        + 2 * bool(row.view)
    )


@dataclass(frozen=True)
class Became:
    """What the run answers: the new sound, or the refusal."""

    does: str
    sutra: str
    why: str
    view: str = ""
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def the_ka(what: str = "", *, gana: str = "",
           before: str = "", view: str = "") -> Became:
    """
    7.3.44–51 — what the affix's क and the taddhita's ठ become.

    Nothing answers by default. A stem with no क before its आप्
    and no ठ in its taddhita is untouched by all eight.

    `view` asks for a named teacher's opinion. Left empty, the
    northerners' refusals still answer — they are options in the
    language — but the teachers' आ of 7.3.49 does not, being a
    fifth form that only a reader asking for it wants.
    """
    matched = [row for row in KA_TABLE
               if _reaches(row, what, gana, before, view)]
    if not matched:
        return Became(
            "", "", "No rule of 7.3.44-51 is reached, so the "
                    "sounds stand as they are")
    row = max(matched, key=lambda one: _how_specific(one, what, gana))
    return Became("" if row.refuses else row.does, row.sutra,
                  row.why, view=row.view, optional=row.optional,
                  blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Ka, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in KA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Ka", "KA_TABLE", "KA_RUN", "UDICAM", "ACARYANAM",
    "BHASTRADI", "ISUS_UK_TA", "Became", "the_ka",
    "provisions_for",
]
