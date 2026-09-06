# -*- coding: utf-8 -*-
"""
६.१.३–१२ — the copy gets a name, and four places call for one.

`src/astadhyayi/dvirvacana.py` already runs the reduplication itself
and holds 6.1.1, 6.1.2 and 6.1.9. What it never states in words is
what the two halves are CALLED, which roots are treated as doubled
without ever having doubled, and where the doubling is ordered from.
Those are these ten sūtras, and this module is the table of them.

**THE TWO NAMES.** 6.1.4 पूर्वोऽभ्यासः names the first half alone;
6.1.5 उभे अभ्यस्तम् names the two together. Everything from 7.4.58
onward is addressed to the अभ्यास — and 6.1.189, 7.1.4 and 6.4.112 to
the अभ्यस्त. The Kāśikā at 6.1.5 says exactly why both are needed:
**उभेग्रहणं किम्? नेनिजतीत्यत्र अभ्यस्तानामादिः इति समुदाय
उदात्तत्वं यथा स्यात् प्रत्येकं पर्यायेण वा मा भूत्** — with one name
for the pair, the accent falls once, on the first vowel of the whole;
name each half separately and it could fall in either half or in both
by turns.

**THE FOUR PLACES.** लिट् (6.1.8), सन् and यङ् (6.1.9), श्लु (6.1.10),
चङ् (6.1.11) — and each is stated with **अनभ्यासस्य** carried down from
6.1.8, so nothing doubles twice. जुगुप्सिषते and लोलूयिषते are already
doubled when the desiderative arrives, and stay as they are.

**AND ONE NAME IS GIVEN WITHOUT ANY DOUBLING AT ALL.** 6.1.6 calls
seven roots अभ्यस्त outright. They look reduplicated — जक्ष्, जागृ,
दरिद्रा, चकास् — and the name is what gets them the accent and the
न-less participle, not any rule of this section.

**WHAT THIS MODULE DOES NOT DO.** It does not reduplicate: that is
`dvirvacana.for_sutra`, and the two are kept apart on purpose. This
one answers what a rule of 6.1.3–12 states; that one runs the copy
through 7.4.59 and the rest.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: 6.1.6's roots. The sūtra says **षट्**, six; the vṛtti names the run
#: by its two ends — **जक्ष भक्षहसनयोः इत्यतः प्रभृति वेवीङ् वेतिना
#: तुल्ये इति यावत्** — and that run holds SEVEN. The Kāśikā states
#: the count it actually gives, **सेयं सप्तानां धातूनाम्
#: अभ्यस्तसंज्ञा विधीयते**, without smoothing the number in the sūtra
#: away. A boundary named by its ends beats a boundary named by a
#: count, and the commentary lets the two disagree in the open.
JAKSHITYADI: Tuple[str, ...] = (
    "jakṣ", "jāgṛ", "daridrā", "cakās", "śās", "dīdhī", "vevī",
)

#: The consonants 6.1.3 keeps out of the copy, when they open a
#: cluster. A vārttika adds ब् to the three.
NDRA: Tuple[str, ...] = ("n", "d", "r")

#: Where the doubling is called for, in the order the sūtras give
#: them. 6.1.9 is `dvirvacana`'s and is named here for completeness of
#: the section, not re-stated.
TRIGGERS: Tuple[str, ...] = ("liṭ", "san", "yaṅ", "ślu", "caṅ")


@dataclass(frozen=True)
class Abhyasta:
    """One rule of 6.1.3–12: what it names, orders, or refuses."""

    sutra: str
    #: The saṃjñā the rule gives, where it gives one.
    names: str = ""
    #: Which part of the doubled form the name lands on — पूर्व at
    #: 6.1.4, उभे at 6.1.5.
    part: str = ""
    #: The roots the rule names outright.
    of: Tuple[str, ...] = ()
    #: A run named by its first member instead — तुजादि at 6.1.7,
    #: जक्षित्यादि at 6.1.6.
    gana: str = ""
    #: The affix whose presence calls for the doubling.
    before: str = ""
    #: What the rule orders: dvirvacana, dīrgha, or nothing where the
    #: rule only names.
    does: str = ""
    #: What the operation lands on.
    on: str = ""
    #: The sounds a refusal keeps out of the copy — 6.1.3's three.
    sounds: Tuple[str, ...] = ()
    #: Where in the portion those sounds must stand for the refusal to
    #: bite. 6.1.3 wants them at the head of a cluster and nowhere
    #: else: प्राणिणिषति doubles its ण् because no cluster opens on it.
    at: str = ""
    refuses: bool = False
    chandasi: bool = False
    #: True where the forms are laid down whole — 6.1.12.
    nipatana: bool = False
    #: The rule a refusal takes the form away from, by ITS number.
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ABHYASTA_TABLE: Tuple[Abhyasta, ...] = (
    Abhyasta(
        "6.1.3", sounds=NDRA, at="saṃyogādi", refuses=True,
        blocks=("6.1.2",),
        keeps_out="ईचिक्षिषते — the copy opens on क्, not one of the "
                  "three; प्राणिणिषति — a ण् with no cluster behind "
                  "it",
        why="न न्द्राः संयोगादयः — and the rule needs 6.1.2's "
            "द्वितीयस्य carried down: **द्वितीयस्येति वर्तते**. Of a "
            "vowel-initial root it is the SECOND one-vowelled portion "
            "that doubles, and where that portion opens on a cluster "
            "beginning न्, द् or र्, that consonant is left out of "
            "the copy. **उन्दिदिषति, अड्डिडिषति, "
            "अर्चिचिषति**.\\n\\n"
            "**AND BOTH CONDITIONS ARE SHOWN BY WHAT FAILS THEM.** "
            "**न्द्रा इति किम्? ईचिक्षिषते** — the cluster there "
            "opens on क् and the copy keeps it. **संयोगादय इति "
            "किम्? प्राणिणिषति** — the ण् of अन् is no cluster's "
            "head, so it doubles, and 8.4.21's उभौ साभ्यासस्य then "
            "makes both ण्.\\n\\n"
            "**AND WHY अजादेः IS READ IN A SECOND WAY.** The plain "
            "reading gives दिद्रासति. **केचिदजादेरित्यपि "
            "पञ्चम्यन्तं कर्मधारयमनुवर्तयन्ति। तस्य प्रयोजनम् — "
            "इन्दिद्रीयिषति** — read अजादेः as *from what the "
            "initial vowel is*, and the refusal reaches only the "
            "consonant immediately after that vowel. In इन्द्रीय the "
            "न् is that consonant and is dropped; the द् and र् are "
            "not, and double.\\n\\n"
            "**AND FOUR SUPPLEMENTS EXTEND IT.** ब् is added to the "
            "three — **उब्जिजिषति** — but only if उब्जि is taught "
            "with a penultimate ब् in the first place. A र् followed "
            "by य् is exempt: **अरार्यते**. ईर्ष्यति doubles its "
            "third, and the vārttika's own commentators cannot agree "
            "whether *third* counts consonants (ईर्ष्यियिषति) or "
            "one-vowelled portions (ईर्ष्यिषिषति). And for "
            "denominatives the last word is **यथेष्टं "
            "नामधातुषु** — पुपुत्रीयिषति, पुतित्रीयिषति, "
            "पुत्रीयियिषति, all of them"),
    Abhyasta(
        "6.1.4", names="abhyāsa", part="pūrva",
        why="पूर्वोऽभ्यासः — the first of the two is the अभ्यास, and "
            "this is the term every rule from 7.4.58 onward is "
            "addressed to. **पपाच, पिपक्षति, पापच्यते, जुहोति, "
            "अपीपचत्**.\\n\\n"
            "**AND A NOMINATIVE IS READ AS A GENITIVE TO GET IT.** "
            "6.1.1 supplied द्वे in the nominative. "
            "**द्वे इति प्रथमान्तं यदनुवर्तते, तदर्थादिह षष्ठ्यन्तं "
            "जायते** — the sense of THIS rule turns it into *of the "
            "two*, since पूर्व is first only with respect to "
            "something. The case a word carries down is not always "
            "the case it is read in"),
    Abhyasta(
        "6.1.5", names="abhyasta", part="ubhe",
        why="उभे अभ्यस्तम् — the two together are the अभ्यस्त. "
            "**ददति, ददत्, दधतु**.\\n\\n"
            "**AND उभे IS SAID SO THAT ONE ACCENT FALLS ONCE.** द्वे "
            "was already carrying. **उभेग्रहणं समुदायसंज्ञाप्रति"
            "पत्त्यर्थम्** — it makes the name belong to the whole "
            "and not to each half. **उभेग्रहणं किम्? नेनिजतीत्यत्र "
            "अभ्यस्तानामादिः इति समुदाय उदात्तत्वं यथा स्यात् "
            "प्रत्येकं पर्यायेण वा मा भूत्**: with the name on the "
            "pair, 6.1.189 puts the उदात्त on the first vowel of the "
            "pair, once. Name each half and the accent could land in "
            "either half, or in both by turns.\\n\\n"
            "**AND THE NAME EARNS TWO MORE RULES.** 7.1.4 puts अत् "
            "for झ after an अभ्यस्त — दद + झि gives ददति — and "
            "6.4.112 gives ददत्. Neither would reach a form whose "
            "halves were named separately"),
    Abhyasta(
        "6.1.6", names="abhyasta", gana="jakṣityādi", of=JAKSHITYADI,
        why="जक्षित्यादयः षट् — seven roots are CALLED अभ्यस्त "
            "without any rule having doubled them. **जक्षति, "
            "जाग्रति, दरिद्रति, चकासति, शासति, दीध्यते, "
            "वेव्यते**.\\n\\n"
            "**AND THE SŪTRA'S COUNT AND THE VṚTTI'S DISAGREE.** The "
            "rule says षट्, six. The vṛtti names the run by its two "
            "ends — **जक्ष भक्षहसनयोः इत्यतः प्रभृति वेवीङ् वेतिना "
            "तुल्ये इति यावत्** — and then states the count that run "
            "actually gives: **सेयं सप्तानां धातूनाम् अभ्यस्तसंज्ञा "
            "विधीयते**, of SEVEN roots. It does not reconcile them. A "
            "boundary named by its ends is the harder evidence, and "
            "the commentary leaves the number in the sūtra "
            "standing.\\n\\n"
            "**AND THE NAME IS WHAT THESE ROOTS ARE FOR.** Being "
            "अभ्यस्त gets them 6.1.189's accent on the first "
            "syllable; and दीध्यत्, the शतृ participle, is refused "
            "the नुम् augment by 7.1.78 नाभ्यस्ताच्छतुः for the same "
            "reason. A saṃjñā doing work no operation of this section "
            "does"),
    Abhyasta(
        "6.1.7", of=("tuj",), gana="tujādi", does="dīrgha",
        on="abhyāsa",
        chandasi=True,
        keeps_out="तुतोज शबलान् हरीन् — ordinary speech, and the "
                  "vowel stays short",
        why="तुजादीनां दीर्घोऽभ्यासस्य — the copy's vowel comes out "
            "long: **तूतुजानः, मामहानः, दाधान, मीमाय, दाधार, "
            "तूताव**.\\n\\n"
            "**AND आदि HERE MEANS *AND THE LIKE*, NOT *AND WHAT "
            "FOLLOWS*.** There is no तुजादि list anywhere. "
            "**तुजादीनामिति प्रकार आदिशब्दः। कश्च प्रकारः? "
            "तुजेर्दीर्घोऽभ्यासस्य न विहितः, दृश्यते च** — the kind "
            "is: *forms whose copy is long where no rule made it "
            "so, and which are nevertheless attested*. The rule is "
            "written to admit what the corpus shows rather than to "
            "generate it.\\n\\n"
            "**AND IT IS BOUNDED BY WHERE IT IS FOUND.** **दीर्घश्च "
            "एषां छन्दसि प्रत्ययविशेष एव दृश्यते, ततोऽन्यत्र न "
            "भवति** — only in the Vedic corpus and only before "
            "certain affixes. तुतोज, in ordinary speech, keeps its "
            "short vowel"),
    Abhyasta(
        "6.1.8", before="liṭ", does="dvirvacana", on="dhātu",
        keeps_out="कर्ता, हर्ता — no लिट्; शृण्विरे — the base is no "
                  "longer a धातु; नोनाव — already doubled",
        why="लिटि धातोरनभ्यासस्य — before लिट्, a root that is not "
            "already a copy doubles, first portion or second "
            "according to 6.1.1 and 6.1.2. **पपाच, पपाठ, "
            "प्रोर्णुनाव**.\\n\\n"
            "**AND धातोः IS IN THE RULE FOR ONE CASE ONLY.** Nothing "
            "stands between root and perfect ending, so the word "
            "looks idle. **लिट् सार्वधातुकम्** by 3.4.117 in some "
            "places, and then a विकरण does intervene: श्रु with श्नु "
            "is शृणु, and शृणु is not a धातु. **सस्वांसो विशृण्विरे, "
            "इम इन्द्राय सुन्विरे** — no doubling there.\\n\\n"
            "**AND अनभ्यासस्य KEEPS THE INTENSIVE OUT.** नोनूयते has "
            "doubled already under यङ्, so its perfect **नोनाव** "
            "does not double again; likewise **संमिमिक्षुः**. The "
            "word carries down through 6.1.9, 6.1.10 and 6.1.11, and "
            "is why जुगुप्सिषते and लोलूयिषते stand as they "
            "are.\\n\\n"
            "**AND IN THE छन्दस् THE WHOLE THING IS OPTIONAL.** "
            "**द्विर्वचनप्रकरणे छन्दसि वेति वक्तव्यम्** — याचिषामहे "
            "beside यियाचिषामहे, दाति beside ददाति, धातु beside "
            "दधातु. And जागृ specifically: **यो जागार** beside "
            "जजागार"),
    Abhyasta(
        "6.1.10", before="ślu", does="dvirvacana", on="dhātu",
        why="श्लौ — where श्लु has taken the शप् away, the root "
            "doubles: **जुहोति, बिभेति, जिह्रेति**. श्लु is the mark "
            "of the third class, and the doubling is what the class "
            "sounds like. **अनभ्यासस्य** carries down from 6.1.8 "
            "here as everywhere in the run"),
    Abhyasta(
        "6.1.11", before="caṅ", does="dvirvacana", on="dhātu",
        why="चङि — before the चङ् of the reduplicated aorist: "
            "**अपीपचत्, अपीपठत्, आटिटत्, आशिशत्, आर्दिदत्**.\\n\\n"
            "**AND THE ORDER OF FOUR OPERATIONS IS FORCED.** "
            "**पचादीनां ण्यन्तानां चङि कृते णिलोप उपधाह्रस्वत्वं "
            "द्विर्वचनमित्येषां कार्याणां प्रवृत्तिक्रमः** — drop the "
            "णि by 6.4.51, shorten the penult by 7.4.1, THEN double. "
            "Double first and the shortening comes after the copy is "
            "made; the short vowel is then स्थानिवत् to the long one, "
            "counts as heavy, and 7.4.93's सन्वद्भाव — which wants a "
            "LIGHT vowel after the copy — never fires.\\n\\n"
            "**AND THE SHORTENING IS NOT स्थानिवत् HERE.** 1.1.57 "
            "holds the substitute to be like the original only for an "
            "operation on what stands BEFORE it. **यो ह्यनादिष्टादचः "
            "पूर्वस्तस्य विधिं प्रति स्थानिवद्भावो भवति। न चास्मिन् "
            "कार्याणां क्रमेण अनादिष्टादचः पूर्वोऽभ्यासो भवति** — "
            "with this order the copy is not before an unsubstituted "
            "vowel at all, so the shortened vowel counts as short and "
            "सन्वद्भाव applies. आशीशमत् is the form that decides "
            "it.\\n\\n"
            "**AND आटिटत् GOES THE OTHER WAY BY THE SAME MAXIM.** "
            "There 1.1.59 द्विर्वचनेऽचि makes the substitution "
            "स्थानिवत् so that the SECOND one-vowelled portion, टि, "
            "is what doubles"),
    Abhyasta(
        "6.1.12", of=("dāś", "sah", "mih"), before="kvasu",
        refuses=True, nipatana=True, blocks=("6.1.8",),
        keeps_out="the इट् augment, refused along with the doubling",
        why="दाश्वान् साह्वान् मीढ्वांश्च — three forms laid down "
            "whole, in the Vedic corpus and in ordinary speech alike: "
            "**छन्दसि भाषायां च अविशेषेण निपात्यन्ते**. Each is "
            "क्वसु on a root that ought to have doubled, and does "
            "not.\\n\\n"
            "**दाश्वान्** from दाशृ: no doubling and no इट् — "
            "**दाश्वांसो दाशुषः सुतम्**. **साह्वान्** from षह्: "
            "parasmaipada, a lengthened penult, no doubling, no इट् "
            "— **साह्वान् बलाहकः**. **मीढ्वान्** from मिह्: no "
            "doubling, no इट्, a lengthened penult, and ह् → ढ् — "
            "**मीढ्वस्तोकाय तनयाय मृड**.\\n\\n"
            "**AND THE SINGULAR IN THE RULE IS NOT MEANT.** "
            "**एकवचनमतन्त्रम्** — the plural forms do not double "
            "either.\\n\\n"
            "**AND FOUR SUPPLEMENTS ADD DOUBLINGS THIS SECTION "
            "OTHERWISE HAS NO PLACE FOR.** क before कृञ् and क्लिद् "
            "— **चक्रम्, चिक्लिदम्**. चर्, चल्, पत् and वद् before "
            "अच्, with आक् added to the copy — **चराचरः, चलाचलः, "
            "पतापतः, वदावदः** — and that augment is itself the proof "
            "that 7.4.60's हलादिः शेषः does not run here, since "
            "**हलादिशेषे हि सति आगमस्य आदेशस्य च विशेषो नास्ति**. "
            "The same optionally, so चरः पुरुषः and चलो रथः stand "
            "too. हन् before अच् takes आक् and turns its ह् into घ् "
            "— **घनाघनः**. And पाटि before अच् drops the णि, takes "
            "उक्, and lengthens — **पाटूपटः**"),
)


@dataclass(frozen=True)
class Stated:
    """What the resolver answers with."""

    does: str
    sutra: str
    why: str
    #: The saṃjñā the rule gives, where it gives one.
    names: str = ""
    on: str = ""
    refuses: bool = False
    chandasi: bool = False
    nipatana: bool = False
    #: Where a refusal answers, the rules it takes the form away
    #: from — each with ITS own number, never this one's.
    blocked_by: Tuple[str, ...] = ()


def _reaches(row: Abhyasta, root: str, before: str, part: str,
             sound: str, at: str, chandasi: bool) -> bool:
    if row.chandasi and not chandasi:
        return False
    if (row.of or row.gana) and root not in row.of:
        return False
    if row.before and before != row.before:
        return False
    if row.part and part != row.part:
        return False
    if row.sounds and sound not in row.sounds:
        return False
    if row.at and at != row.at:
        return False
    return True


def _supplies(row: Abhyasta, wants: str) -> bool:
    """
    A refusal is never the answer to a question that asked for the
    thing refused, and a naming rule is never the answer to a question
    about an operation.
    """
    if not wants:
        return True
    if wants in ("dvirvacana", "dīrgha"):
        return row.does == wants and not row.refuses
    return wants == row.names


def _how_specific(row: Abhyasta, root: str) -> int:
    """
    A refusal beats what it refuses, and a named root beats a trigger.

    6.1.7's तुजादि is scored as a gaṇa and not as a list even though
    the column holds no members: the vṛtti says outright that there
    is no list — **तुजादीनामिति प्रकार आदिशब्दः** — so nothing can
    match it by name.
    """
    return (
        9 * bool(row.refuses)
        + 8 * (root in row.of)
        + 5 * bool(row.before)
        + 4 * bool(row.part)
        + 4 * bool(row.sounds)
        + 2 * bool(row.at)
        + 1 * bool(row.gana)
    )


def stated(root: str = "", *, before: str = "", part: str = "",
           sound: str = "", at: str = "", chandasi: bool = False,
           wants: str = "") -> Stated:
    """
    6.1.3–12 — what these rules name, order, or refuse.

    A refusal reports on `blocked_by` the rule the form is taken away
    FROM, with that rule's own number: 6.1.3 names 6.1.2, and 6.1.12
    names 6.1.8. Neither governs what it excepts.

    Nothing answers by default. 6.1.1 is an अधिकार and lives in
    `dvirvacana`, and it supplies three words rather than an
    operation, so a question this table does not reach reaches
    nothing.
    """
    matched = [
        row for row in ABHYASTA_TABLE
        if _reaches(row, root, before, part, sound, at, chandasi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Stated(
            "", "", "No rule of 6.1.3–12 is reached. The section has "
                    "no heading of its own that supplies — 6.1.1 "
                    "carries एकाचः, द्वे and प्रथमस्य, and those are "
                    "words, not an operation")
    row = max(matched, key=lambda one: _how_specific(one, root))
    return Stated(
        "" if row.refuses else row.does, row.sutra, row.why,
        names=row.names, on=("" if row.refuses else row.on),
        refuses=row.refuses, chandasi=row.chandasi,
        nipatana=row.nipatana, blocked_by=row.blocks)


def triggers() -> Tuple[str, ...]:
    """
    Every place 6.1.8–11 calls for a doubling, in the order stated.

    सन् and यङ् are 6.1.9's and are run by `dvirvacana`; they are
    named here because the section is not describable without them —
    **अनभ्यासस्य** carries from 6.1.8 through all four rules, and it
    is that one word which keeps जुगुप्सिषते from doubling twice.
    """
    return TRIGGERS


def provisions_for(sutra_id: str) -> Tuple[Abhyasta, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ABHYASTA_TABLE
                 if row.sutra == sutra_id)
