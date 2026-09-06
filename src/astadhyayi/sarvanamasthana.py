# -*- coding: utf-8 -*-
"""
७.१.८४–१०३ — the strong cases, and the ॠ that closes the pāda.

Twenty sūtras, and sixteen of them are about what a stem does
before a सर्वनामस्थान — the five endings 1.1.43 calls strong.
दिव् becomes द्यौः, पथिन् becomes पन्थाः, पुंस् becomes पुमान्,
सखि becomes सखा, कर्तृ becomes कर्ता, and गो and चतुर् and
अनडुह् each get a rule of their own.

**THREE OF THEM WORK ON पथिन् AT ONCE.** 7.1.85 gives it आ in
the nominative singular, 7.1.86 turns its इ into अ in every
strong case, and 7.1.87 turns its थ् into न्थ् — and only all
three together make पन्थाः, पन्थानौ, पन्थानः. Then 7.1.88 takes
the whole टि away again where the stem is भ: पथः, पथा, पथे. Four
rules, one word, and the declension falls out.

**AND ONE OF THEM IS A रूपातिदेश AND NOT A SUBSTITUTION.** 7.1.95
तृज्वत् क्रोष्टुः does not replace anything: it says that क्रोष्टु
takes the SHAPE a तृच्-final stem would have had — क्रोष्टा,
क्रोष्टारौ — and the vṛtti has to say which तृच्-final stem is
meant, **प्रत्यासत्तेश्च क्रुशेरेव**, the nearest one.

**AND THE PĀDA ENDS ON SOMETHING ELSE ENTIRELY.** 7.1.100–103
give a ॠ-final root इ or उ: किरति, गिरति, पूर्ताः, मुमूर्षति.
No सर्वनामस्थान in sight, and 7.1.103 closes the pāda with a
बहुलं छन्दसि that lets the उ reach where the rule did not and
fail where it did.

**WHAT THIS MODULE DOES NOT DO.** It says what the stem becomes.
What the ending then does is 7.2's and 7.3's, and the sandhi at
the join is अध्याय ८'s.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch, closing पाद ७.१.
STRONG_RUN: Tuple[str, str] = ("7.1.84", "7.1.103")

#: Where the सर्वनामस्थान rules give way to the ॠ rules.
RTA_FROM: str = "7.1.100"

#: 7.1.85–88's three stems, which four rules between them decline.
PATHI_THREE: Tuple[str, ...] = ("pathin", "mathin", "ṛbhukṣin")

#: 7.1.94's three named beside the ऋ-final stems.
USANAS_THREE: Tuple[str, ...] = ("uśanas", "purudaṃsas", "anehas")

#: And the three shapes उशनस् has in the vocative, which the
#: vṛtti gives in a verse and does not choose between.
USANAS_VOCATIVE: Tuple[str, ...] = ("he uśanaḥ", "he uśanan",
                                    "he uśana")

#: 7.1.95–97's one word, given three sūtras.
KROSTU: str = "kroṣṭu"

#: 7.1.98–99's two, which take आम् and then अम्.
CATUR_ANADUH: Tuple[str, ...] = ("catur", "anaḍuh")


@dataclass(frozen=True)
class Strong:
    """One rule of 7.1.84–103: what the stem becomes."""

    sutra: str
    #: The substitute, the augment, or `ṇit` / `tṛjvat` where the
    #: rule confers a property rather than a shape.
    does: str = ""
    #: The stems named outright.
    of: Tuple[str, ...] = ()
    #: The stem class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow.
    not_before: Tuple[str, ...] = ()
    #: What part of the stem is affected.
    part: str = ""
    #: A further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    augment: bool = False
    udatta: bool = False
    optional: bool = False
    chandasi: bool = False
    bahulam: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


STRONG_TABLE: Tuple[Strong, ...] = (
    Strong(
        "7.1.84", does="aut", of=("div",), before=("su",),
        keeps_out="अक्षद्यूः — the ROOT दिव्, which is taught "
                  "with a marker and so is not this word",
        why="दिव औत् — दिव् becomes द्यौ before सु: **द्यौः**. "
            "And the दिव् meant is the noun — **दिविति "
            "प्रातिपदिकम् अस्ति निरनुबन्धकम्। धातुस्तु "
            "सानुबन्धकः, स इह न गृह्यते**"),
    Strong(
        "7.1.85", does="āt", of=PATHI_THREE, before=("su",),
        why="पथिमथ्यृभुक्षामात् — पथिन्, मथिन् and ऋभुक्षिन् take "
            "आ before सु: **पन्थाः, मन्थाः, ऋभुक्षाः**. The "
            "इन् they end in is nasal and the आ that replaces it "
            "is not — **भाव्यमानेन सवर्णानां ग्रहणं न भवति इति "
            "शुद्धो ह्ययम् उच्चार्यते**, a substitute being "
            "brought into existence cannot be qualified by what "
            "it replaced"),
    Strong(
        "7.1.86", does="at", of=PATHI_THREE, part="i",
        before=("sarvanāmasthāna",),
        why="इतोऽत् सर्वनामस्थाने — and their इ becomes अ in every "
            "strong case: **पन्थाः, पन्थानौ, पन्थानः, "
            "पन्थानम्; मन्थानौ; ऋभुक्षाणौ, ऋभुक्षाणम्**. The "
            "sūtra says अत् again although आत् was already "
            "running — **आदिति वर्तमाने पुनरद्वचनं "
            "षपूर्वार्थम्** — so that 6.4.9's optional "
            "lengthening after a ष् may have something short to "
            "work on: **ऋभुक्षणम्**"),
    Strong(
        "7.1.87", does="nth", of=("pathin", "mathin"), part="th",
        before=("sarvanāmasthāna",),
        why="थो न्थः — and the थ् of पथिन् and मथिन् becomes न्थ् "
            "in the strong cases: **पन्थाः, पन्थानौ, पन्थानः; "
            "मन्थाः, मन्थानौ, मन्थानः**. Three rules acting on "
            "one word, and only all three together give the "
            "form"),
    Strong(
        "7.1.88", does="ṭi-lopa", of=PATHI_THREE, part="ṭi",
        result=("bha",), blocks=("7.1.86",),
        why="भस्य टेर्लोपः — but where the stem is भ they lose "
            "their टि altogether: **पथः, पथा, पथे; मथः, मथा; "
            "ऋभुक्षः, ऋभुक्षा**. The सर्वनामस्थान that has been "
            "governing cannot come here — **सर्वनामस्थान "
            "इत्यनुवर्तमानम् अपि विरोधाद् इह न सम्बध्यते** — "
            "since a stem cannot be भ and strong at once, and "
            "the anuvṛtti is dropped for contradiction"),
    Strong(
        "7.1.89", does="asuṅ", of=("puṃs",),
        before=("sarvanāmasthāna",),
        why="पुंसोऽसुङ् — पुंस् becomes पुमांस् in the strong "
            "cases: **पुमान्, पुमांसौ, पुमांसः**.\\n\\n"
            "**AND A VĀRTTIKA IS NEEDED FOR THE ACCENT OF A "
            "COMPOUND.** In परमपुमान् the समासान्त accent falls "
            "before the ending is even added; the असुङ् then "
            "comes and would move it. **तदर्थम् असुङ्युपदेशिवद्"
            "वचनं कर्तव्यम्** — treat the substitute as though "
            "it had been there from the start, and परमपुमान् is "
            "अन्तोदात्त while पुमान् alone stays आद्युदात्त"),
    Strong(
        "7.1.90", does="ṇit", of=("go",),
        before=("sarvanāmasthāna",),
        keeps_out="चित्रगुः, शबलगुः — the ending belongs to "
                  "another word's number and not to गो's",
        why="गोतो णित् — a सर्वनामस्थान after गो is treated as "
            "ङित्, so its vṛddhi comes: **गौः, गावौ, गावः**.\\n\\n"
            "**AND THE vṛtti OFFERS TWO WAYS TO SAVE हे चित्रगो.** "
            "Either **अङ्गवृत्ते पुनर्वृत्ताव् अविधिर् "
            "निष्ठितस्य** — the guṇa is already done and the "
            "णित् does not come back; or गोतः is a genitive of "
            "relation, and only an ending that expresses गो's "
            "own number is गो's. Some read ओतो णित् instead, to "
            "catch द्यौः, द्यावौ as well"),
    Strong(
        "7.1.91", does="ṇit", of=("ṇal",), result=("uttama",),
        optional=True,
        why="णलुत्तमो वा — and the first-person णल् is optionally "
            "ङित्: **अहं चकर, अहं चकार; अहं पपच, अहं पपाच**"),
    Strong(
        "7.1.92", does="ṇit", of=("sakhi",),
        before=("sarvanāmasthāna",), excludes=("sambuddhi",),
        keeps_out="हे सखे — the vocative singular, named out",
        why="सख्युरसम्बुद्धौ — a सर्वनामस्थान after सखि is ङित्, "
            "the vocative singular excepted: **सखायौ, सखायः**"),
    Strong(
        "7.1.93", does="anaṅ", of=("sakhi",), before=("su",),
        excludes=("sambuddhi",),
        keeps_out="हे सखे — again the vocative",
        why="अनङ् सौ — and सखि becomes सखान् before सु, unless "
            "that सु is the vocative: **सखा**. Two sūtras in a "
            "row for one word, and they do different things: "
            "7.1.92 makes the ending ङित् so that the vṛddhi "
            "comes, and this one replaces the stem's own last "
            "part. Both spare the vocative, and the vṛtti gives "
            "the same counter-example twice — **असंबुद्धाविति "
            "किम्? हे सखे**"),
    Strong(
        "7.1.94", does="anaṅ", gana="ṛ-anta", of=USANAS_THREE,
        before=("su",), excludes=("sambuddhi",),
        keeps_out="हे कर्तः, हे मातः, हे पितः — the vocative, "
                  "where the stem stays short",
        why="ऋदुशनस्पुरुदंसोऽनेहसां च — an ऋ-final stem, and "
            "उशनस्, पुरुदंसस् and अनेहस्, take अनङ् before सु "
            "outside the vocative: **कर्ता, हर्ता, माता, पिता, "
            "भ्राता; उशना, पुरुदंसा, अनेहा**.\\n\\n"
            "**AND उशनस् HAS THREE VOCATIVES AND THE VṚTTI "
            "CHOOSES NONE.** **उशनसः संबुद्धावपि पक्षेऽनङ् "
            "इष्यते। हे उशनन्** — and 8.2.8's न-loss may be "
            "refused or not, giving **हे उशन** beside **हे "
            "उशनः**. A verse records all three and adds a "
            "fourth teacher's view: **संबोधने तूशनसस्त्रिरूपं "
            "सान्तं तथा नान्तमथाप्यदन्तम्। माध्यंदिनिर्वष्टि "
            "गुणं त्विगन्ते**"),
    Strong(
        "7.1.95", does="tṛjvat", of=(KROSTU,),
        before=("sarvanāmasthāna",), excludes=("sambuddhi",),
        keeps_out="क्रोष्टून् — no सर्वनामस्थान; हे क्रोष्टो — "
                  "the vocative",
        why="तृज्वत् क्रोष्टुः — क्रोष्टु takes the SHAPE a "
            "तृच्-final stem would have had: **क्रोष्टा, "
            "क्रोष्टारौ, क्रोष्टारः, क्रोष्टारम्**.\\n\\n"
            "**AND WHICH तृच्-FINAL STEM IS A QUESTION THE "
            "VṚTTI HAS TO ANSWER.** **रूपातिदेशोऽयम्। "
            "प्रत्यासत्तेश्च क्रुशेरेव तृजन्तस्य यद् रूपं तद् "
            "अतिदिश्यते** — the nearest one, क्रोष्टृ from क्रुश्, "
            "**तच्च अन्तोदात्तम्**. A shape is conferred and not "
            "a substitute supplied, which is why the accent "
            "comes with it"),
    Strong(
        "7.1.96", does="tṛjvat", of=(KROSTU,), result=("strī",),
        why="स्त्रियां च — and in the feminine: **क्रोष्ट्री, "
            "क्रोष्ट्रीभ्याम्, क्रोष्ट्रीभिः**. "
            "**असर्वनामस्थानार्थम् आरम्भः** — the sūtra exists "
            "for the cases the one before could not reach. "
            "Whether क्रोष्टु is in the गौरादि list is disputed, "
            "and the vṛtti says what goes wrong on that reading: "
            "**पञ्चभिः क्रोष्ट्रीभिः क्रीतैः पञ्चक्रोष्टृभी "
            "रथैः इति न सिध्यति। तत्र प्रतिविधेयम्**"),
    Strong(
        "7.1.97", does="tṛjvat", of=(KROSTU,),
        before=("tṛtīyā-ādi-ac",), optional=True,
        keeps_out="क्रोष्टून् — not तृतीयादि; क्रोष्टुभ्याम्, "
                  "क्रोष्टुभिः — a consonant-initial ending",
        why="विभाषा तृतीयाऽऽदिष्वचि — and in the oblique cases "
            "before a vowel it is OPTIONAL: **क्रोष्ट्रा, "
            "क्रोष्टुना; क्रोष्ट्रे, क्रोष्टवे; क्रोष्टरि, "
            "क्रोष्टौ**. And where the shape is conferred the "
            "नुम् and नुट् still come, by "
            "पूर्वविप्रतिषेध — **तृज्वद्भावात् पूर्वविप्रतिषेधेन "
            "नुम्नुटौ भवतः। प्रियक्रोष्टुनेऽरण्याय; "
            "क्रोष्टूनाम्**"),
    Strong(
        "7.1.98", does="ām", of=CATUR_ANADUH,
        before=("sarvanāmasthāna",), augment=True, udatta=True,
        why="चतुरनडुहोरामुदात्तः — चतुर् and अनडुह् take the "
            "augment आम्, and it is udātta: **चत्वारः; "
            "अनड्वान्, अनड्वाहौ, अनड्वाहः**. It reaches a "
            "compound ending in one — **तदन्तविधिरत्रेष्यते। "
            "प्रियचत्वाः, प्रियानड्वान्** — and a vārttika makes "
            "the feminine optional: **अनडुहः स्त्रियां वेति "
            "वक्तव्यम्। अनडुही, अनड्वाही**"),
    Strong(
        "7.1.99", does="am", of=CATUR_ANADUH,
        before=("sambuddhi",), augment=True, blocks=("7.1.98",),
        why="अम् सम्बुद्धौ — but in the vocative singular the "
            "augment is अम् instead: **हे प्रियचत्वः; हे "
            "प्रियानड्वन्**. **पूर्वस्यायम् अपवादः** — an "
            "exception to the sūtra before, and the vṛtti says "
            "so in three words"),
    Strong(
        "7.1.100", does="it", gana="ṝ-anta-dhātu", part="ṝ",
        keeps_out="पितृणाम्, मातृणाम् — nouns and not roots",
        why="ॠत इद्धातोः — a ॠ-final ROOT takes इ for it: "
            "**किरति, गिरति, आस्तीर्णम्, विशीर्णम्**. And a root "
            "that is one only by a rule's reckoning counts too — "
            "**लाक्षणिकस्याप्यत्र ग्रहणम् इष्यते। चिकीर्षति** — "
            "which is what the word धातोः is doing in the sūtra"),
    Strong(
        "7.1.101", does="it", gana="ṝ-upadha-dhātu", part="ṝ-upadhā",
        why="उपधायाश्च — and a ॠ in the PENULT: **कीर्तयति, "
            "कीर्तयतः, कीर्तयन्ति**. Two words, and the whole "
            "of the rule before is carried over: the इ, the "
            "root, and the ॠ it replaces. What is new is only "
            "where in the stem it stands — last in 7.1.100, "
            "second-last here"),
    Strong(
        "7.1.102", does="ut", gana="oṣṭhya-pūrva-ṝ-anta",
        part="ṝ", blocks=("7.1.100",),
        why="उदोष्ठ्यपूर्वस्य — but where a LABIAL stands before "
            "the ॠ the substitute is उ: **पूर्ताः पिण्डाः; "
            "पुपूर्षति; मुमूर्षति**. A dental-labial counts as a "
            "labial — **वुवूर्षति ऋत्विजम्** — and the labial "
            "must be part of the stem itself, "
            "**अङ्गावयव एव गृह्यते**, so संपूर्वस्य ऋ gives "
            "समीर्णम्.\\n\\n"
            "**AND A VĀRTTIKA ORDERS THESE AGAINST THE "
            "STRENGTHENINGS.** **इत्त्वोत्त्वाभ्यां गुणवृद्धी "
            "भवतो विप्रतिषेधेन** — guṇa and vṛddhi win: "
            "**आस्तरणम्, आस्तारकः; निगरणम्, निगारकः**"),
    Strong(
        "7.1.103", does="ut", gana="ṝ-anta-dhātu", chandasi=True,
        bahulam=True, blocks=("7.1.102",),
        why="बहुलं छन्दसि — and in the Veda the उ is बहुलम्, "
            "reaching where no labial stands and failing where "
            "one does: **मित्रावरुणा ततुरिम्; दूरे ह्यध्वा "
            "जगुरिः** with no labial, and **पप्रितमम्, "
            "वव्रितमम्** with one and no उ. Sometimes both — "
            "**क्वचिद् भवति। पपुरिः**.\\n\\n"
            "**AND THIS CLOSES पाद ७.१.** The Kāśikā's colophon "
            "follows it: **इति श्रीवामनविरचितायां काशिकायां "
            "वृत्तौ सप्तमाध्यायस्य प्रथमः पादः**"),
)


def _reaches(row: Strong, stem: str, gana: str, before: str,
             part: str, result: str, chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.not_before and before in row.not_before:
        return False
    if row.part and part and part != row.part:
        return False
    if row.result and result not in row.result:
        return False
    if row.excludes and (before in row.excludes
                         or result in row.excludes):
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Strong, stem: str, gana: str) -> int:
    """
    A rule that names what it displaces beats it, a named stem
    beats a named class, and a named part beats a bare stem.

    7.1.85 to 7.1.88 are the four that need it: three of them
    build पन्थाः out of पथिन् and the fourth takes the टि away
    again where the stem is भ.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.of and stem in row.of)
        + 5 * bool(row.gana and gana == row.gana)
        + 4 * bool(row.part)
        + 4 * bool(row.result)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Made:
    """What the run answers: a substitute, an augment, a property."""

    does: str
    sutra: str
    why: str
    augment: bool = False
    udatta: bool = False
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def strong_stem(stem: str = "", *, gana: str = "",
                before: str = "", part: str = "",
                result: str = "", chandasi: bool = False,
                wants: str = "") -> Made:
    """
    7.1.84–103 — what the stem becomes before a strong ending.

    Nothing answers by default. Most stems go into the strong
    cases unchanged, and the ones here are the handful that do
    not — which is why each of them is named.
    """
    matched = [
        row for row in STRONG_TABLE
        if _reaches(row, stem, gana, before, part, result, chandasi)
        and (not wants or wants == row.does)
    ]
    if not matched:
        return Made(
            "", "", "No rule of 7.1.84-103 is reached, so the "
                    "stem goes in as it is")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Made(row.does, row.sutra, row.why, augment=row.augment,
                udatta=row.udatta, optional=row.optional,
                blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Strong, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in STRONG_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Strong", "STRONG_TABLE", "STRONG_RUN", "RTA_FROM",
    "PATHI_THREE", "USANAS_THREE", "USANAS_VOCATIVE", "KROSTU",
    "CATUR_ANADUH", "Made", "strong_stem", "provisions_for",
]
