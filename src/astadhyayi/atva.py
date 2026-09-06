# -*- coding: utf-8 -*-
"""
६.१.४५–५७ — आ for a diphthong, and a heading that ends on itself.

**आदेच उपदेशेऽशिति.** A root whose final in the धातुपाठ is an एच् —
ए, ऐ, ओ, औ — has आ put in its place, except before an affix marked
श्. ग्लै is ग्लाता, ग्लातुम्, ग्लातव्यम्; शो is निशाता. Before a शित्
affix it stays: ग्लायति, म्लायति.

**THE HEADING IS DECLARED BY THE VṚTTI AND ENDS ON ITS OWN LAST
RULE.** **आकाराधिकारस्त्वयं नित्यं स्मयतेः इति यावत्** — the आकार
governs from 6.1.45 to 6.1.57 and stops there. Every प्राक्-heading in
adhyāyas 4 and 5 was bounded by a word lifted out of the rule AFTER
its last; this one names its last rule outright. Thirteen sūtras, and
the thirteenth is both the marker and a member.

**AND THE PROHIBITION IN IT IS A प्रसज्यप्रतिषेध.** **अशितीति
प्रसज्यप्रतिषेधोऽयम्. तेन एतद् आत्वम् अनैमित्तिकं प्रागेव
प्रत्ययोत्पत्तेर्भवति** — the substitution is not CAUSED by the affix
that follows, so it has already happened when the affix arrives. That
is why 3.1.136's क reaches सुग्लः and 3.3.128's युच् reaches सुग्लानः:
both rules want a root ending in आ, and by then ग्लै is one.

**AND शित् IS READ AS शिदादि.** एश्, the perfect ending, has its श् at
the END and would be a शित् on the plain reading, so जग्ले and मम्ले
would be unreachable. **न एवं विज्ञायते — शकार इद् यस्य सोऽयं शिदिति।
किं तर्हि? श एव इत् शित्** — and then **यस्मिन् विधिस्तदादाव्
अल्ग्रहणे** confines the refusal to affixes BEGINNING with श्.

**AND THE LAST RULE DROPS AN OPTION BY SAYING नित्यम्.** 6.1.51's
विभाषा carries down through six rules; 6.1.57 says नित्यम् and
**नित्यग्रहणाद् विभाषेति निवृत्तम्**. The same device 6.1.32 used by
repeating संप्रसारणम् — a word that adds nothing to the sense and
everything to the force.

**WHAT THIS MODULE DOES NOT DO.** It reports which rule substitutes,
not the finished form. Getting from ग्लै to ग्लाता needs 7.2.35's इट्
and the तृच् rules; getting from क्री to क्रापयति needs 7.3.36's प्.
Neither is codified, and the forms in the notes are the Kāśikā's own.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.varna import _SANDHYAKSARA

#: Where the आकार governs, on the vṛtti's own statement at 6.1.45:
#: **आकाराधिकारस्त्वयं नित्यं स्मयतेः इति यावत्**. The far end is
#: named by the rule's own words, and that rule is INSIDE the run —
#: which no heading of adhyāya 4 or 5 was.
ATVA_RUN: Tuple[str, str] = ("6.1.45", "6.1.57")

#: And the sūtra whose words bound it, which is the run's own last
#: member rather than the one after it.
ATVA_MARKER: str = "6.1.57"

#: Where the option runs, and what ends it. 6.1.51 opens it and
#: 6.1.57's नित्यम् closes it: **नित्यग्रहणाद् विभाषेति निवृत्तम्**.
VIBHASA_RUN: Tuple[str, str] = ("6.1.51", "6.1.56")

#: The maxim that keeps the perfect ending एश् out of the refusal,
#: read together with श एव इत् शित्.
SHIDADI: str = "यस्मिन् विधिस्तदादावल्ग्रहणे"

#: The four the general rule reaches, and only where the धातुपाठ
#: taught them: एच्. चेता and स्तोता have an ए and an ओ standing
#: here and are still out of reach, the vowel there being guṇa
#: arrived at later.
#:
#: Asked of `varna` rather than written out again. The four are the
#: सन्ध्यक्षर — the vowels that are not simple — and that module
#: already holds them for 1.1.9's savarṇa test. Two lists would be
#: two answers to one question, and the day one gained a member the
#: other would not.
EC: Tuple[str, ...] = tuple(sorted(_SANDHYAKSARA))


@dataclass(frozen=True)
class Atva:
    """One rule of 6.1.45–57: a root, a condition, and आ put in."""

    sutra: str
    #: The roots the rule names. Empty on 6.1.45, which names none
    #: and reaches every एजन्त root there is.
    of: Tuple[str, ...] = ()
    #: The affix that must follow — घञ्, णि, ल्यप्, णमुल्, लिट्.
    before: str = ""
    #: A second affix condition the same rule carries. 6.1.50's च
    #: pulls एच् down beside ल्यप्.
    also_before: str = ""
    #: The sense the form must carry — अपारलौकिक at 6.1.49, प्रजन at
    #: 6.1.55, हेतुभय at 6.1.56 and 6.1.57.
    result: str = ""
    #: What must stand in front — अप at 6.1.53.
    pre: str = ""
    #: What is put in. आ everywhere here; the column exists so that a
    #: refusal can hold nothing and be told apart from a rule that
    #: gives.
    gives: str = "ā"
    #: The affix the rule refuses to act before — शित् at 6.1.45,
    #: carried as a condition on the giving rule itself.
    not_before: str = ""
    #: True where the rule reaches a root only because the धातुपाठ
    #: gave it an एच् final. 6.1.45 alone, and it is what keeps
    #: the general rule off सिध्, खिद्, भी and स्मि — whose ए is
    #: guṇa arrived at later, and which the rules after 6.1.48
    #: therefore have to name one by one.
    final_ec: bool = False
    refuses: bool = False
    optional: bool = False
    #: True where the option is व्यवस्थितविभाषा — 6.1.51, settled by
    #: the sense the root carries.
    vyavasthita: bool = False
    chandasi: bool = False
    #: True where the row IS the heading. 6.1.45 is both: it declares
    #: the run and states a rule.
    heading: bool = False
    #: The rule this one refuses, by ITS own number.
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ATVA_TABLE: Tuple[Atva, ...] = (
    Atva(
        "6.1.45", heading=True, not_before="śit", final_ec=True,
        keeps_out="कर्ता, हर्ता — no एच् to replace; चेता, स्तोता — "
                  "the ए is not what the धातुपाठ taught; ग्लायति — "
                  "a शित् affix follows",
        why="आदेच उपदेशेऽशिति — a root whose final in the धातुपाठ is "
            "an एच् has आ put in its place, and धातोः carries down "
            "from 6.1.8. **ग्लाता, ग्लातुम्, ग्लातव्यम्; निशाता, "
            "निशातुम्, निशातव्यम्**.\\n\\n"
            "**AND THE HEADING IS DECLARED HERE, ENDING ON ITS OWN "
            "LAST RULE.** **आकाराधिकारस्त्वयं नित्यं स्मयतेः इति "
            "यावत्** — the आकार governs to 6.1.57. Every प्राक् "
            "heading of adhyāyas 4 and 5 was bounded by a word "
            "lifted out of the rule AFTER its last; this one names "
            "its last rule, and that rule is a member of the run "
            "rather than its neighbour.\\n\\n"
            "**AND उपदेशे IS WHAT KEEPS चेता OUT.** The condition is "
            "on the shape the धातुपाठ taught, not on the shape "
            "standing here: चि and स्तु end in इ and उ there, and "
            "the ए and ओ of चेता and स्तोता are guṇa arrived at "
            "later.\\n\\n"
            "**AND अशिति IS A प्रसज्यप्रतिषेध, WHICH MOVES THE "
            "SUBSTITUTION EARLIER.** **अशितीति प्रसज्यप्रतिषेधोऽयम्। "
            "तेनैतदात्वमनैमित्तिकं प्रागेव प्रत्ययोत्पत्तेर्भवति** — "
            "the आ is not caused by what follows, so it is already "
            "there when an affix arrives. 3.1.136's क wants a root "
            "in आ and finds one: **सुग्लः, सुम्लः**; so does "
            "3.3.128's युच्: **सुग्लानः, सुम्लानः**.\\n\\n"
            "**AND शित् IS READ AS शिदादि, OR THE PERFECT IS "
            "LOST.** एश् has its श् at the end and would block the "
            "substitution on the plain reading, leaving जग्ले and "
            "मम्ले unreachable. **नैवं विज्ञायते — शकार इद् यस्य "
            "सोऽयं शिदिति। किं तर्हि? श एव इत् शित्**, and then "
            "**यस्मिन् विधिस्तदादावल्ग्रहणे** confines the refusal "
            "to affixes that BEGIN with श्"),
    Atva(
        "6.1.46", of=("vyeñ",), before="liṭ", gives="", refuses=True,
        blocks=("6.1.45",),
        why="न व्यो लिटि — व्येञ् keeps its diphthong in the "
            "perfect: **संविव्याय, संविव्ययिथ**.\\n\\n"
            "**AND THE FORM IT LEAVES STANDING IS BUILT BY TWO OTHER "
            "RULES.** The copy is vocalised by 6.1.17 "
            "लिट्यभ्यासस्योभयेषाम्, and the vṛddhi in संविव्याय is "
            "7.2.115's अचो ञ्णिति before the णित् णल्. The refusal "
            "removes one operation and leaves the rest of the "
            "derivation where it was"),
    Atva(
        "6.1.47", of=("sphur", "sphul"), before="ghañ",
        why="स्फुरतिस्फुलत्योर्घञि — before घञ् these two give आ "
            "where guṇa would have given ओ: **विस्फारः, विस्फालः**, "
            "not विस्फोरः and विस्फोलः. And 8.3.76 makes the स् "
            "optionally ष् after वि, so **विष्फारः, विष्फालः** "
            "stand beside them"),
    Atva(
        "6.1.48", of=("krī", "iṅ", "ji"), before="ṇi",
        why="क्रीङ्जीनां णौ — three roots before णि: **क्रापयति, "
            "अध्यापयति, जापयति**.\\n\\n"
            "**AND THE प् THAT APPEARS IS A CONSEQUENCE OF THE आ, "
            "NOT OF THIS RULE.** 7.3.36 gives the augment पुक् to a "
            "root ending in आ before णि; the substitution here is "
            "what makes these roots end in आ. Three rules deep, and "
            "none of the three mentions the प्"),
    Atva(
        "6.1.49", of=("sidh",), before="ṇi", result="apāralaukika",
        keeps_out="तपस्तापसं सेधयति — the ascetic's attainment bears "
                  "its fruit in another world",
        why="सिध्यतेरपारलौकिके — before णि, and only where what is "
            "brought about is NOT for the next world: **अन्नं "
            "साधयति, ग्रामं साधयति**.\\n\\n"
            "**AND THE COUNTER-EXAMPLE IS ARGUED, NOT ASSERTED.** In "
            "तपस्तापसं सेधयति the root means a particular knowledge, "
            "**स च ज्ञानविशेष उत्पन्नः परलोके जन्मान्तरे फलम् "
            "अभ्युदयलक्षणम् उपसंहरन् परलोकप्रयोजनो भवति** — the "
            "knowledge gathers its fruit in another birth, so its "
            "purpose is of that world and the substitution is "
            "withheld.\\n\\n"
            "**AND THE REFUSAL DOES NOT REACH ONE STEP FURTHER.** "
            "Why then is **अन्नं साधयति ब्राह्मणेभ्यो दास्यामीति** "
            "not caught, the food being cooked for a gift whose "
            "fruit is in the next world? **सिध्यतेरत्रार्थो "
            "निष्पत्तिः... तस्य यद् दानं तत् पारलौकिकम्, न पुनः "
            "सिद्धिरेवेति न आत्वं पर्युदस्यते** — the root means "
            "only the getting-ready; it is the GIVING that is for "
            "the next world, and the rule reaches only what the root "
            "itself does. **साक्षात् परलोकप्रयोजने च सिध्यर्थे "
            "कृतावकाशं वचनम् एवंविषयं नावगाहते.**\\n\\n"
            "**AND THE SHAPE OF THE WORD IN THE RULE PICKS THE "
            "ROOT.** सिध्यतेः is written with श्यन्, which is the "
            "दिवादि root; **षिधु गत्याम् इत्यस्य भौवादिकस्य "
            "निवृत्त्यर्थः**, and the भ्वादि root of the same shape "
            "is left out"),
    Atva(
        "6.1.50", of=("mī", "mi", "dī"), before="lyap", also_before="ec",
        why="मीनातिमिनोतिदीङां ल्यपि च — before ल्यप्, and by the च "
            "before whatever else the आकार section reaches: "
            "**प्रमाता, प्रमातव्यम्, प्रमातुम्, प्रमाय; निमाता, "
            "निमाय; उपदाता, उपदाय**.\\n\\n"
            "**AND उपदेशे CARRIES DOWN, WHICH DECIDES WHICH AFFIXES "
            "THE ROOTS CAN TAKE AT ALL.** **उपदेश एवात्वविधानाद् "
            "इवर्णान्तलक्षणः प्रत्ययो न भवति, आकारान्तलक्षणश्च "
            "भवति** — since the आ is there in the धातुपाठ itself, a "
            "rule that wants a root ending in इ or ई never finds "
            "one, and a rule that wants आ always does. So घञ् and "
            "युच् give **उपदायो वर्तते, ईषदुपदानम्**, and the affixes "
            "for इ-final roots do not apply"),
    Atva(
        "6.1.51", of=("lī",), before="lyap", also_before="ec",
        optional=True, vyavasthita=True,
        why="विभाषा लीयतेः — **विलाता, विलातुम्, विलातव्यम्, विलाय** "
            "beside **विलेता, विलेतुम्, विलेतव्यम्, विलीय**. Both "
            "लीङ् of the दिवादि and ली of the क्र्यादि are "
            "meant.\\n\\n"
            "**AND THE OPTION IS SETTLED BY THE SENSE.** "
            "**लियो व्यवस्थितविभाषाविज्ञानात् सिद्धम्** — in the "
            "senses of coaxing, cheating and putting to shame the "
            "substitution is fixed before णि: **कस्त्वामुल्लापयते, "
            "श्येनो वर्तिकामुल्लापयते**.\\n\\n"
            "**AND A SUPPLEMENT KEEPS TWO AFFIXES OUT.** "
            "**निमिमीलियां खलचोः प्रतिषेधो वक्तव्यः** — before खल् "
            "and अच् the substitution fails for नि, मि, मी and ली: "
            "**ईषन्निमयः, ईषत्प्रमयः, ईषद्विलयः**"),
    Atva(
        "6.1.52", of=("khid",), optional=True, chandasi=True,
        keeps_out="चित्तं खेदयति, in ordinary speech",
        why="खिदेश्छन्दसि — in the Vedic corpus the option reaches "
            "खिद् as well: **चित्तं चखाद** beside **चित्तं "
            "चिखेद**. Outside it there is no choice and no "
            "substitution"),
    Atva(
        "6.1.53", of=("gur",), before="ṇamul", pre="apa",
        optional=True,
        why="अपगुरो णमुलि — after अप and before णमुल्: "
            "**अपगारमपगारम्** beside **अपगोरमपगोरम्**. The णमुल् is "
            "3.4.22's, given for repeated action, and the word is "
            "doubled with it. 3.4.53 gives the same affix in "
            "**अस्यपगारं युध्यन्ते**"),
    Atva(
        "6.1.54", of=("ci", "sphur"), before="ṇi", optional=True,
        why="चिस्फुरोर्णौ — before णि, optionally: **चापयति, "
            "चाययति; स्फारयति, स्फोरयति**. स्फुर् is here for the "
            "second time in the section — 6.1.47 took it before "
            "घञ् and made it fixed, and this rule takes it before "
            "णि and makes it a choice"),
    Atva(
        "6.1.55", of=("vī",), before="ṇi", result="prajana",
        optional=True,
        why="प्रजने वीयतेः — before णि, in the sense of conceiving: "
            "**पुरोवातो गाः प्रवापयति** beside **प्रवाययति**, which "
            "the vṛtti glosses **गर्भं ग्राहयति**. And it says what "
            "the sense-word covers: **प्रजनो हि जन्मन उपक्रमो "
            "गर्भग्रहणम्** — the beginning of a birth, the taking of "
            "an embryo. वी has five senses in the धातुपाठ and only "
            "this one is reached"),
    Atva(
        "6.1.56", of=("bhī",), before="ṇi", result="hetubhaya",
        optional=True,
        keeps_out="कुञ्चिकयैनं भाययति — the fear comes from the key, "
                  "which is an instrument and not the हेतु",
        why="बिभेतेर्हेतुभये — before णि, where the fear comes "
            "STRAIGHT from the causative agent: **मुण्डो भापयते, "
            "जटिलो भापयते** beside भीषयते.\\n\\n"
            "**AND हेतु IS THE TECHNICAL WORD, NOT THE ORDINARY "
            "ONE.** **हेतुरिह पारिभाषिकः स्वतन्त्रस्य प्रयोजकः** — "
            "1.4.55's हेतु, the one who sets the independent agent "
            "going. Where the fear is caused by an instrument "
            "instead, the rule does not reach it.\\n\\n"
            "**AND THE TWO SIDES OF THE OPTION TAKE DIFFERENT "
            "AUGMENTS.** 7.3.40 gives षुक् to भी before णि, and "
            "**स चात्वपक्षे न भवति** — not on the side where the आ "
            "was put in. The rule there names भी with its ई "
            "written in, and there is no ई left"),
    Atva(
        "6.1.57", of=("smi",), before="ṇi", result="hetubhaya",
        keeps_out="कुञ्चिकयैनं विस्माययति",
        why="नित्यं स्मयतेः — the same condition as the rule before, "
            "the same affix, the same sense — and no choice: "
            "**मुण्डो विस्मापयते, जटिलो विस्मापयते**.\\n\\n"
            "**AND THE WORD नित्यम् IS WHAT DROPS THE OPTION.** "
            "**नित्यग्रहणाद् विभाषेति निवृत्तम्** — the विभाषा that "
            "has carried since 6.1.51 stops here, and it stops "
            "because one word says so. The same device 6.1.32 used "
            "by repeating संप्रसारणम्.\\n\\n"
            "**AND THE SENSE-WORD IS STRETCHED TO FIT.** भय carries "
            "down, but smiling is not fear. **भयशब्देन "
            "धात्वर्थसामान्याद् इह स्मयतेरर्थोऽभिधीयते। न हि "
            "मुख्ये भये स्मयतेर्वृत्तिरस्ति** — the word stands for "
            "*whatever this root means*, since it plainly cannot "
            "mean fear here.\\n\\n"
            "**AND THIS RULE IS THE HEADING'S OWN BOUND.** "
            "**आकाराधिकारस्त्वयं नित्यं स्मयतेः इति यावत्** — 6.1.45 "
            "names this sūtra as where the आकार stops, and the rule "
            "is inside the run it bounds"),
)


@dataclass(frozen=True)
class PutIn:
    """What the resolver answers with."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    vyavasthita: bool = False
    chandasi: bool = False
    #: Where a refusal answers, the rule the substitution is taken
    #: away from — with THAT rule's number, never this one's.
    blocked_by: Tuple[str, ...] = ()


def _reaches(row: Atva, root: str, before: str, result: str,
             pre: str, final: str, chandasi: bool) -> bool:
    if row.chandasi and not chandasi:
        return False
    if row.final_ec and final not in EC:
        return False
    if row.of and root not in row.of:
        return False
    allowed = tuple(one for one in (row.before, row.also_before) if one)
    if allowed and before not in allowed:
        return False
    if row.not_before and before == row.not_before:
        return False
    if row.result and result != row.result:
        return False
    if row.pre and pre != row.pre:
        return False
    return True


def _how_specific(row: Atva) -> int:
    """
    A refusal beats what it refuses, and a named root beats the
    heading, which names none at all.

    The sense counts above the affix because 6.1.56 and 6.1.57 share
    both the affix and the sense and are told apart by the root — but
    6.1.48 and 6.1.49 share the affix alone, and there the one with a
    sense is the narrower.
    """
    return (
        9 * bool(row.refuses)
        + 8 * bool(row.of)
        + 5 * bool(row.pre)
        + 4 * bool(row.result)
        + 3 * bool(row.before)
    )


def becomes_a(root: str = "", *, before: str = "", result: str = "",
              pre: str = "", final: str = "",
              chandasi: bool = False) -> PutIn:
    """
    6.1.45–57 — whether आ is put in for a root's final diphthong.

    6.1.45 is both the heading and a rule, so unlike every section
    this project has met since adhyāya 4, the fallback here DOES
    supply — but only where `final` says the धातुपाठ gave the root
    an एच्. सिध्, खिद्, भी and स्मि do not have one, which is
    why the rules after 6.1.48 name them by hand: the ए they work on
    is guṇa arrived at later, and उपदेशे keeps the general rule
    off it.
    """
    matched = [
        row for row in ATVA_TABLE
        if _reaches(row, root, before, result, pre, final, chandasi)
    ]
    if not matched:
        return PutIn(
            "", "", "No rule of 6.1.45–57 is reached. 6.1.45 is the "
                    "heading and a rule at once, so what escapes it "
                    "escapes the section")
    row = max(matched, key=_how_specific)
    return PutIn(row.gives, row.sutra, row.why, optional=row.optional,
                 vyavasthita=row.vyavasthita, chandasi=row.chandasi,
                 blocked_by=row.blocks)


def atva_run() -> PutIn:
    """
    How far the आकार governs, and where the vṛtti says it stops.

    **आकाराधिकारस्त्वयं नित्यं स्मयतेः इति यावत्** — and what is
    named is the run's own LAST RULE, not the one after it. Every
    प्राक् heading of adhyāyas 4 and 5 was bounded the other way.
    """
    opens, closes = ATVA_RUN
    return PutIn(
        "", opens,
        "आकार governs from %s to %s, and %s names %s by its own "
        "words नित्यं स्मयतेः. The marker is a MEMBER of the run "
        "here, where every प्राक् heading before this one was "
        "bounded by the rule that comes after its last"
        % (opens, closes, opens, ATVA_MARKER))


def provisions_for(sutra_id: str) -> Tuple[Atva, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ATVA_TABLE if row.sutra == sutra_id)
