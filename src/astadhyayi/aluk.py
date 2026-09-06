# -*- coding: utf-8 -*-
"""
६.३.१–२४ — अलुगुत्तरपदे: the case ending that does NOT drop.

2.4.71 सुपो धातुप्रातिपदिकयोः drops every case ending inside a
compound, because 2.4.1's समासे makes the finished compound a
प्रातिपदिक and a प्रातिपदिक carries no ending. This run is where it
stays. 6.3.2's own vṛtti says exactly that: **समासे कृते
प्रातिपदिकत्वात् सुपो लुकि प्राप्ते प्रतिषेधः क्रियते** — the
deletion is due, and the rule refuses it.

So स्तोकात् + मुक्तः stays स्तोकान्मुक्तः and not *स्तोकमुक्तः;
आत्मने + पदम् stays आत्मनेपदम्; युधि + स्थिरः stays युधिष्ठिरः.
Every ablative, instrumental, dative, locative and genitive that
survives inside a Sanskrit compound survives by one of these
twenty-three rules.

**AND THE HEADING'S TWO WORDS STOP IN DIFFERENT PLACES — FOR THE
FOURTH TIME IN TWO PĀDAS.** 6.3.1's vṛtti closes with both bounds
in one line: **अलुगधिकारः प्रागानङः। उत्तरपदाधिकारः
प्रागङ्गाधिकारात्** — अलुक् holds only to 6.3.24, since 6.3.25
आनङ् replaces it, while उत्तरपदे runs the whole pāda and stops
only at 6.4.1's अङ्गस्य. 6.2.1, 6.2.64 and 6.2.111 each did the
same, and this is the fourth.

**AND THE WORD उत्तरपदे IS THERE FOR A REASON THAT IS NOT ITS OWN
MEANING.** **अन्यार्थमिदम् उत्तरपदग्रहणम् इहाप्यलुको निवृत्तिं
करोतीत्येवमर्थं लक्षणप्रतिपदोक्तपरिभाषा नाश्रयितव्या** — without
it one would reach for the paribhāṣā that a rule stated of a
described class does not reach what another rule names outright.
Saying उत्तरपदे makes the refusal turn on POSITION instead, so
निःस्तोकः — where स्तोक is the FIRST word and nothing follows it
inside the compound — simply falls outside.

**WHAT THIS MODULE DOES NOT DO.** It reports which ending stays
and by which rule. It does not inflect: which ablative, whose
locative, and what form it then takes are the caller's, and
6.3.9's युधिष्ठिरः is a locative because the query says so.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where अलुक् governs — **अलुगधिकारः प्रागानङः**, so to 6.3.24,
#: since 6.3.25 आनङ् ऋतो द्वन्द्वे displaces it.
ALUK_RUN: Tuple[str, str] = ("6.3.1", "6.3.24")

#: And where उत्तरपदे does, which is the whole pāda:
#: **उत्तरपदाधिकारः प्रागङ्गाधिकारात्**.
UTTARAPADE_RUN: Tuple[str, str] = ("6.3.1", "6.3.139")

#: 6.3.2's स्तोकादि, and the vṛtti takes them as SENSES and not as
#: words: **स्तोकान्तिकदूरार्थकृच्छ्राणि स्तोकादीनि** — so अल्प
#: goes with स्तोक, अभ्याश with अन्तिक, विप्रकृष्ट with दूर.
STOKADI: Tuple[str, ...] = ("stoka", "antika", "dūra", "kṛcchra")

#: And what each of them covers, by the vṛtti's own examples.
STOKADI_SENSES = {
    "stoka": ("stoka", "alpa"),
    "antika": ("antika", "abhyāśa"),
    "dūra": ("dūra", "viprakṛṣṭa"),
    "kṛcchra": ("kṛcchra",),
}

#: 6.3.3's four, and the vārttika that adds a fifth.
OJASADI: Tuple[str, ...] = ("ojas", "sahas", "ambhas", "tamas")
OJASADI_VARTIKA: Tuple[str, ...] = ("añjas",)

#: The three restrictions 6.3.10 lays on a rule that had already
#: supplied the form: **एते च त्रयो नियमविकल्पा अत्रेष्यन्ते —
#: कारनाम्न्येव, प्राचामेव, हलादावेवेति**.
NIYAMA_THREE: Tuple[str, ...] = ("kāranāman", "prācām", "hal-ādi")

#: The genitive अलुक्s no sūtra states — every one a vārttika on
#: 6.3.21, and each a fixed compound rather than a class.
SASTHI_VARTIKA: Tuple[str, ...] = (
    "vāco-yukti", "diśo-daṇḍa", "paśyato-hara", "āmuṣyāyaṇa",
    "āmuṣya-putrikā", "āmuṣya-kulikā", "devānāṃ-priya",
    "śunaḥ-śepa", "śunaḥ-puccha", "śuno-lāṅgūla", "divo-dāsa")

#: The locative अलुक् 6.3.9's vārttika adds for two stems:
#: **हृद्द्युभ्यां ङेः — हृदिस्पृक्, दिविस्पृक्**.
NGI_VARTIKA: Tuple[str, ...] = ("hṛd", "div")

#: What 6.3.12 keeps out of स्वाङ्ग, and 6.3.18 out of its own
#: three second members.
NOT_SVANGA: Tuple[str, ...] = ("mūrdhan", "mastaka")


@dataclass(frozen=True)
class Aluk:
    """One rule of 6.3.1–24: which ending stays, and when."""

    sutra: str
    #: The case whose ending is kept — pañcamī, tṛtīyā, caturthī,
    #: saptamī, ṣaṣṭhī.
    keeps: str = ""
    #: The first members the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of first member instead — स्तोकादि, हलदन्त,
    #: स्वाङ्ग, कालनामन्, ऋदन्त-विद्यायोनिसम्बन्ध.
    gana: str = ""
    #: The second members the rule names outright.
    uttarapada: Tuple[str, ...] = ()
    #: A named class of second member instead — कृत्, पूरण, इन्नन्त.
    uttarapada_gana: str = ""
    samasa: str = ""
    #: The further condition — a sense (संज्ञा, आक्रोश), a register
    #: (भाषा), or a shape (कारनामन्).
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    #: बहुलम् — wider than an option, and the vṛtti gives forms
    #: both ways without pairing them.
    bahulam: bool = False
    #: A नियम: the form was already available, and the rule's work
    #: is to narrow where.
    niyama: bool = False
    heading: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ALUK_TABLE: Tuple[Aluk, ...] = (
    Aluk(
        "6.3.1", heading=True,
        why="अलुगुत्तरपदे — **अलुगिति च, उत्तरपद इति चैतदधिकृतं "
            "वेदितव्यम्। यदित ऊर्ध्वमनुक्रमिष्यामोऽलुगुत्तरपद "
            "इत्येवं तद् वेदितव्यम्** — from here a case ending "
            "that 2.4.71 would have dropped inside the compound "
            "STAYS, so long as something follows it. The vṛtti "
            "reads the next sūtra out as its example: **वक्ष्यति "
            "पञ्चम्याः स्तोकादिभ्यः — स्तोकान्मुक्तः, "
            "अल्पान्मुक्तः**.\\n\\n"
            "**AND उत्तरपदे IS SAID FOR SOMETHING OTHER THAN WHAT "
            "IT MEANS.** **उत्तरपद इति किम्? निष्क्रान्तः स्तोकाद् "
            "निःस्तोकः** — there स्तोक is the second word and "
            "nothing follows, so no ending survives. But the vṛtti "
            "says that is not why the word is there: **अन्यार्थम् "
            "इदम् उत्तरपदग्रहणम् इहाप्यलुको निवृत्तिं करोतीत्येवमर्थं "
            "लक्षणप्रतिपदोक्तपरिभाषा नाश्रयितव्या** — without it "
            "one would have to invoke the paribhāṣā that a rule "
            "framed by description does not reach what another "
            "rule names outright. Stating position instead settles "
            "it without the paribhāṣā.\\n\\n"
            "**AND THE HEADING'S TWO WORDS STOP IN DIFFERENT "
            "PLACES.** **अलुगधिकारः प्रागानङः। उत्तरपदाधिकारः "
            "प्रागङ्गाधिकारात्** — अलुक् to 6.3.24, where 6.3.25 "
            "आनङ् takes over; उत्तरपदे to the end of the pāda, "
            "stopping only at 6.4.1 अङ्गस्य. The fourth heading in "
            "two pādas built this way"),
    Aluk(
        "6.3.2", keeps="pañcamī", gana="stokādi",
        keeps_out="स्तोकाभ्यां मुक्तः, स्तोकेभ्यो मुक्तः — no "
                  "compound is formed at all",
        why="पञ्चम्याः स्तोकादिभ्यः — an ablative stays after a "
            "word meaning A LITTLE, NEAR, FAR or WITH DIFFICULTY: "
            "**स्तोकान्मुक्तः, अल्पान्मुक्तः; अन्तिकादागतः, "
            "अभ्याशादागतः; दूरादागतः, विप्रकृष्टादागतः; "
            "कृच्छ्रान्मुक्तः** — freed by a hair, come from "
            "nearby, come from far off, barely got away.\\n\\n"
            "**AND THE FOUR ARE SENSES AND NOT WORDS.** "
            "**स्तोकान्तिकदूरार्थकृच्छ्राणि स्तोकादीनि** — which "
            "is why अल्प goes with स्तोक and विप्रकृष्ट with दूर.\\n\\n"
            "**AND THE DUAL AND PLURAL ARE OUT FOR A REASON THAT "
            "IS NOT GRAMMATICAL.** **द्विवचनबहुवचनान्तानां तु "
            "स्तोकादीनाम् अनभिधानात् समास एव न भवति — स्तोकाभ्यां "
            "मुक्तः, स्तोकेभ्यो मुक्त इति। तेनात्र न कदाचिद् "
            "ऐकपद्यम् ऐकस्वर्यं च भवति** — nobody says it, so "
            "there is no compound to keep an ending in, and hence "
            "neither one word nor one accent. A vārttika adds "
            "one more: **ब्राह्मणाच्छंसिन उपसंख्यानम्**"),
    Aluk(
        "6.3.3", keeps="tṛtīyā", of=OJASADI + OJASADI_VARTIKA,
        why="ओजःसहोऽम्भस्तमसस्तृतीयायाः — an instrumental stays "
            "after these four: **ओजसाकृतम्, सहसाकृतम्, "
            "अम्भसाकृतम्, तमसाकृतम्** — done by force, done by "
            "strength, done by water, done in the dark.\\n\\n"
            "**AND TWO VĀRTTIKAS ADD TO IT.** **अञ्जस "
            "उपसंख्यानम् — अञ्जसाकृतम्**, and **पुंसानुजो "
            "जनुषान्ध इति वक्तव्यम् — पुंसानुजः, जनुषान्धः** — "
            "born after a male child, blind from birth. The second "
            "adds two whole compounds rather than a stem"),
    Aluk(
        "6.3.4", keeps="tṛtīyā", of=("manas",), result=("saṃjñā",),
        keeps_out="मनोदत्ता, मनोगुप्ता — not a name, and the "
                  "ending goes",
        why="मनसः संज्ञायाम् — an instrumental stays after मनस् "
            "where the compound is a NAME: **मनसादत्ता, "
            "मनसागुप्ता, मनसासंगता** — women's names, given by "
            "the heart, guarded by the heart"),
    Aluk(
        "6.3.5", keeps="tṛtīyā", of=("manas",),
        uttarapada=("ājñāyin",),
        why="आज्ञायिनि च — and before आज्ञायिन्, whether or not "
            "the compound is a name: **मनसा आज्ञातुं शीलमस्य "
            "मनसाज्ञायी** — one whose way it is to understand by "
            "the mind alone"),
    Aluk(
        "6.3.6", keeps="tṛtīyā", of=("ātman",),
        uttarapada_gana="pūraṇa",
        keeps_out="आत्मचतुर्थः — a बहुव्रीहि, **आत्मा चतुर्थोऽस्य**, "
                  "and no instrumental in it to keep",
        why="आत्मनश्च पूरणे — an instrumental stays after आत्मन् "
            "before an ORDINAL: **आत्मनापञ्चमः, आत्मनाषष्ठः** — "
            "himself the fifth, himself the sixth, a man counted "
            "in with four others.\\n\\n"
            "**AND BOTH THE CASE AND THE COMPOUND COME FROM "
            "SOMEWHERE ELSE.** **तृतीयाविधाने प्रकृत्यादिभ्य "
            "उपसंख्यानम् इति तृतीया। तृतीयेति योगविभागात् "
            "समासः** — the instrumental by a vārttika on 2.3.18, "
            "and the compound by splitting 2.1.30 in two. And the "
            "vṛtti answers the obvious objection: **कथं जनार्दनस् "
            "त्वात्मचतुर्थ एवेति? बहुव्रीहिरयम्**"),
    Aluk(
        "6.3.7", keeps="caturthī", of=("ātman",),
        result=("vaiyākaraṇākhyā",),
        why="वैयाकरणाख्यायां चतुर्थ्याः — a dative stays after "
            "आत्मन् in a term GRAMMARIANS use: **आत्मनेपदम्, "
            "आत्मनेभाषा**. The vṛtti glosses the condition twice "
            "over — **वैयाकरणानाम् आख्या वैयाकरणाख्या। आख्या "
            "संज्ञा। यया संज्ञया वैयाकरणा एव व्यवहरन्ति** — a "
            "name in which only grammarians deal. The dative is "
            "**तादर्थ्ये चतुर्थी** and the compound again "
            "**चतुर्थीति योगविभागात्**"),
    Aluk(
        "6.3.8", keeps="caturthī", of=("para",),
        result=("vaiyākaraṇākhyā",),
        why="परस्य च — and after पर in the same kind of term: "
            "**परस्मैपदम्, परस्मैभाषा**. Two sūtras for the two "
            "halves of one pair of names, and the pair is what "
            "1.4.99–100 then use to sort every ending in the "
            "grammar"),
    Aluk(
        "6.3.9", keeps="saptamī", gana="hal-adanta",
        result=("saṃjñā",),
        keeps_out="नदीकुक्कुटिका, भूमिपाशाः — the first member "
                  "ends in neither a consonant nor अ; अक्षशौण्डः "
                  "— no name",
        why="हलदन्तात् सप्तम्याः संज्ञायाम् — a locative stays "
            "after a stem ending in a CONSONANT or in अ, where "
            "the compound is a NAME: **युधिष्ठिरः, त्वचिसारः; "
            "अरण्येतिलकाः, अरण्येमाषकाः, वनेकिंशुकाः, "
            "वनेहरिद्रकाः, वनेबल्वजकाः, पूर्वाह्णेस्फोटकाः, "
            "कूपेपिशाचकाः** — steady in battle, and the names of "
            "plants and places.\\n\\n"
            "**AND ONE FAMOUS NAME IS NOT REACHED BY THIS RULE AT "
            "ALL.** **गविष्ठिर इत्यत्र तु गवियुधिभ्यां स्थिरः "
            "इत्यत एव वचनाद् अलुक्** — गो ends in neither, so the "
            "locative in गविष्ठिरः is kept by 8.3.95 naming it, "
            "not by this.\\n\\n"
            "**AND A VĀRTTIKA ADDS TWO STEMS OUTRIGHT.** "
            "**हृद्द्युभ्यां ङेः — हृदिस्पृक्, दिविस्पृक्** — "
            "touching the heart, touching the sky, with no "
            "condition that the compound be a name"),
    Aluk(
        "6.3.10", keeps="saptamī", gana="hal-adanta",
        result=("kāranāman",), niyama=True,
        keeps_out="अभ्यर्हितपशुः — **कारादन्यस्यैतद् देयस्य "
                  "नाम**; यूथपशुः — not an eastern usage; "
                  "अविकटोरणः — the second member opens with a "
                  "vowel",
        why="कारनाम्नि च प्राचां हलादौ — the same locative stays "
            "in an EASTERN name for a due payment, before a "
            "second member beginning with a consonant: "
            "**स्तूपेशाणः, दृषदिमाषकः, हलेद्विपदिका, "
            "हलेत्रिपदिका**.\\n\\n"
            "**AND THE RULE GRANTS NOTHING — IT NARROWS.** "
            "**कारविशेषस्य संज्ञा एताः, तत्र पूर्वेणैव सिद्धे "
            "नियमार्थम् इदम्** — 6.3.9 had already supplied every "
            "one of these, all of them being names. What 6.3.10 "
            "does is fence them: **एते च त्रयो नियमविकल्पा "
            "अत्रेष्यन्ते — कारनाम्न्येव, प्राचामेव, "
            "हलादावेवेति**, three restrictions from one sūtra, "
            "each with its own counter-example"),
    Aluk(
        "6.3.11", keeps="saptamī", of=("madhya", "anta"),
        uttarapada=("guru",),
        why="मध्याद्गुरौ — a locative stays after मध्य before "
            "गुरु: **मध्येगुरुः** — a metrical foot heavy in the "
            "middle. A vārttika adds the other end: **अन्ताच्चेति "
            "वक्तव्यम् — अन्तेगुरुः**. And the compound is again "
            "**सप्तमीति योगविभागात्**, the same split 6.3.6 and "
            "6.3.7 leaned on for their own cases"),
    Aluk(
        "6.3.12", keeps="saptamī", gana="svāṅga",
        excludes=NOT_SVANGA + ("kāma",),
        keeps_out="मूर्धशिखः, मस्तकशिखः — the two the sūtra names "
                  "out; मुखकामः — before काम; अक्षशौण्डः — अक्ष "
                  "is no part of the body; अङ्गुलित्राणः, "
                  "जङ्घावलिः — the stem ends in neither a "
                  "consonant nor अ",
        why="अमूर्धमस्तकात् स्वाङ्गादकामे — a locative stays "
            "after a word for a PART OF THE BODY, मूर्धन् and "
            "मस्तक excepted, and not before काम: **कण्ठे "
            "कालोऽस्य कण्ठेकालः; उरसिलोमा; उदरेमणिः** — "
            "blue-throated, hairy-chested, jewel-bellied. "
            "6.3.9's हलदन्तात् is still running, which is what "
            "keeps अङ्गुलित्राणः out"),
    Aluk(
        "6.3.13", keeps="saptamī", uttarapada=("bandha",),
        optional=True,
        keeps_out="गुप्तिबन्धः — गुप्ति ends in neither a "
                  "consonant nor अ",
        why="बन्धे च विभाषा — before बन्ध the locative stays "
            "OPTIONALLY: **हस्तेबन्धः / हस्तबन्धः; चक्रेबन्धः / "
            "चक्रबन्धः**. And बन्ध here is one particular "
            "formation: **बन्ध इति घञन्तो गृह्यते**.\\n\\n"
            "**AND THE OPTION WORKS IN BOTH DIRECTIONS AT "
            "ONCE.** **उभयत्रविभाषेयम्। स्वाङ्गाद्धि बहुव्रीहौ "
            "पूर्वेण नित्यम् अलुक् प्राप्नोति। तत्पुरुषे तु "
            "स्वाङ्गाद् अस्वाङ्गात् च नेन्सिद्धबध्नातिषु च इति "
            "प्रतिषेधः प्राप्नोति** — in a बहुव्रीहि from a "
            "body-part, 6.3.12 would have kept the ending always, "
            "so the option takes it away; in a तत्पुरुष, 6.3.19 "
            "would have refused it always, so the option grants "
            "it. One विभाषा facing opposite ways"),
    Aluk(
        "6.3.14", keeps="saptamī", samasa="tatpuruṣa",
        uttarapada_gana="kṛt", bahulam=True, optional=True,
        keeps_out="कुरुचरः, मद्रचरः — the ending goes, though the "
                  "conditions are met",
        why="तत्पुरुषे कृति बहुलम् — in a तत्पुरुष before a "
            "कृत्-formed second member the locative stays "
            "VARIOUSLY: **स्तम्बेरमः, कर्णेजपः** — one that "
            "sports in the thicket, one who whispers in the ear. "
            "**न च भवति — कुरुचरः, मद्रचरः**, where it does not. "
            "बहुलम् is not an option offering two forms of one "
            "word: it is the statement that both happen and the "
            "rule does not say which"),
    Aluk(
        "6.3.15", keeps="saptamī",
        of=("prāvṛṣ", "śarad", "kāla", "div"), uttarapada=("ja",),
        why="प्रावृट्शरत्कालदिवां जे — a locative stays after "
            "these four before ज: **प्रावृषिजः, शरदिजः, कालेजः, "
            "दिविजः** — born in the rains, born in autumn, born "
            "in due season, born in heaven. The vṛtti marks it as "
            "no more than a spelling-out of the rule before: "
            "**पूर्वस्यैवायं प्रपञ्चः**"),
    Aluk(
        "6.3.16", keeps="saptamī",
        of=("varṣa", "kṣara", "śara", "vara"), uttarapada=("ja",),
        optional=True,
        why="विभाषा — and after four more, optionally: "
            "**वर्षेजः / वर्षजः; क्षरेजः / क्षरजः; शरेजः / "
            "शरजः; वरेजः / वरजः**. The bare word विभाषा for a "
            "whole sūtra, with everything else carried down"),
    Aluk(
        "6.3.17", keeps="saptamī", gana="kālanāman",
        uttarapada=("kāla", "tara", "tama", "tana"), optional=True,
        keeps_out="शुक्लतरे, शुक्लतमे — शुक्ल names no time; "
                  "रात्रितरायाम् — रात्रि ends in neither a "
                  "consonant nor अ",
        why="घकालतनेषु कालनाम्नः — after a word naming a TIME, "
            "the locative stays optionally before घ, before the "
            "word काल, and before तन: **पूर्वाह्णेतरे / "
            "पूर्वाह्णतरे; पूर्वाह्णेतमे / पूर्वाह्णतमे; "
            "पूर्वाह्णेकाले / पूर्वाह्णकाले; पूर्वाह्णेतने / "
            "पूर्वाह्णतने**.\\n\\n"
            "**AND NAMING AN AFFIX HERE DOES NOT REACH WHAT ENDS "
            "IN IT.** **उत्तरपदाधिकारे प्रत्ययग्रहणे "
            "तदन्तविधिर्नेष्यते** — under the उत्तरपद heading, "
            "naming an affix names the affix and not a stem "
            "ending in it. And the vṛtti says how that is known: "
            "**हृदयस्य हृल्लेख० इति लेखग्रहणाद् लिङ्गात्** — from "
            "6.3.50 having to say लेख at all"),
    Aluk(
        "6.3.18", keeps="saptamī",
        uttarapada=("śaya", "vāsa", "vāsin"), excludes=("kāla",),
        optional=True,
        keeps_out="पूर्वाह्णशयः — a time-word, which this rule "
                  "excludes and 6.3.17 takes instead; भूमिशयः — "
                  "भूमि ends in neither a consonant nor अ",
        why="शयवासवासिष्वकालात् — before शय, वास or वासिन्, and "
            "NOT after a time-word, the locative stays "
            "optionally: **खेशयः / खशयः; ग्रामेवासः / ग्रामवासः; "
            "ग्रामेवासी / ग्रामवासी** — lying in the open, "
            "dwelling in the village.\\n\\n"
            "**AND A VĀRTTIKA ADDS A STEM WITH THREE SECOND "
            "MEMBERS OF ITS OWN.** **अपो योनियन्मतुषु सप्तम्या "
            "अलुग् वक्तव्यः — अप्सुयोनिः, अप्सव्यः, "
            "अप्सुमन्तौ** — born in the waters, of the waters, "
            "having waters. The यत् there is by 4.3.54's "
            "दिगादि"),
    Aluk(
        "6.3.19", refuses=True, keeps="saptamī",
        uttarapada=("siddha", "badhnāti"), uttarapada_gana="in-anta",
        blocks=("6.3.14",),
        why="नेन्सिद्धबध्नातिषु च — but the locative does NOT "
            "stay before a second member ending in इन्, before "
            "सिद्ध, or before a form of बध्: **स्थण्डिलवर्ती; "
            "सांकाश्यसिद्धः, काम्पिल्यसिद्धः; चक्रबद्धः, "
            "चारबद्धः** — each of them a कृदन्त that 6.3.14 "
            "would otherwise have reached.\\n\\n"
            "**AND ONE OF ITS OWN EXAMPLES IS DISPUTED.** "
            "**चक्रबन्ध इति केचिद् उदाहरन्ति तत् पचाद्यजन्तं "
            "द्रष्टव्यम्। घञन्ते हि बन्धे च विभाषा इत्युक्तम्** — "
            "some cite चक्रबन्धः here, and it can only be the "
            "अच्-formed word, since the घञ्-formed one is 6.3.13's "
            "and optional"),
    Aluk(
        "6.3.20", refuses=True, keeps="saptamī",
        uttarapada=("stha",), result=("bhāṣā",),
        blocks=("6.3.14",),
        keeps_out="कृष्णोऽस्याखरेष्ठः — in the Veda the ending "
                  "does stay, and 8.3.104 then gives the ष्",
        why="स्थे च भाषायाम् — nor before स्थ, in the SPOKEN "
            "language: **समस्थः, विषमस्थः, कूटस्थः, पर्वतस्थः** "
            "— standing level, standing on a peak. Naming the "
            "register is what leaves the Veda alone, and the "
            "Vedic form is quoted to show it: **कृष्णोऽस्य "
            "आखरेष्ठः**"),
    Aluk(
        "6.3.21", keeps="ṣaṣṭhī", result=("ākrośa",),
        keeps_out="ब्राह्मणकुलम् — no abuse meant",
        why="षष्ठ्या आक्रोशे — a genitive stays where ABUSE is "
            "meant: **चौरस्यकुलम्, वृषलस्यकुलम्** — a thief's "
            "family, a serf's family.\\n\\n"
            "**AND THE VĀRTTIKAS ON THIS ONE SŪTRA CARRY MOST OF "
            "THE GENITIVES SANSKRIT ACTUALLY KEEPS.** "
            "**षष्ठीप्रकरणे वाग्दिक्पश्यद्भ्यो युक्तिदण्डहरेषु "
            "यथासंख्यम् अलुग् वक्तव्यः — वाचोयुक्तिः, "
            "दिशोदण्डः, पश्यतोहरः**, matched one to one; "
            "**आमुष्यायणामुष्यपुत्रिकामुष्यकुलिकेति चालुग् "
            "वक्तव्यः**; **देवानांप्रिय इत्यत्र च षष्ठ्या अलुग् "
            "वक्तव्यः**; **शेपपुच्छलाङ्गूलेषु शुनः संज्ञायां "
            "षष्ठ्या अलुग् वक्तव्यः — शुनःशेपः, शुनःपुच्छः, "
            "शुनोलाङ्गूलः**; and **दिवश्च दासे षष्ठ्या अलुग् "
            "वक्तव्यः — दिवोदासाय गायति**. Śunaḥśepa and "
            "Divodāsa are named men, and neither is reachable "
            "from a sūtra"),
    Aluk(
        "6.3.22", keeps="ṣaṣṭhī", uttarapada=("putra",),
        result=("ākrośa",), optional=True,
        keeps_out="ब्राह्मणीपुत्रः — no abuse, so no option",
        why="पुत्रेऽन्यतरस्याम् — before पुत्र, still in abuse, "
            "the genitive stays OPTIONALLY: **दास्याःपुत्रः / "
            "दासीपुत्रः; वृषल्याःपुत्रः / वृषलीपुत्रः** — son of "
            "a slave woman, son of a serf woman"),
    Aluk(
        "6.3.23", keeps="ṣaṣṭhī", gana="ṛd-anta-vidyā-yoni",
        uttarapada_gana="vidyā-yoni-sambandha",
        keeps_out="आचार्यपुत्रः, मातुलपुत्रः — the first member "
                  "does not end in ऋ; होतृधनम्, पितृगृहम् — the "
                  "SECOND member names neither learning nor birth",
        why="ऋतो विद्यायोनिसम्बन्धेभ्यः — a genitive stays after "
            "an ऋ-final word naming a relation of LEARNING or of "
            "BIRTH: **होतुरन्तेवासी, होतुःपुत्रः; पितुरन्तेवासी, "
            "पितुःपुत्रः** — the Hotṛ's pupil, the father's son.\\n\\n"
            "**AND THE CONDITION HAS TO HOLD OF BOTH MEMBERS.** "
            "**विद्यायोनिसंबन्धेभ्यस्तत्पूर्वोत्तरपदग्रहणम्। "
            "विद्यायोनिसंबन्धवाचिन्येवोत्तरपदे यथा स्याद्, "
            "अन्यत्र मा भूत् — होतृधनम्, पितृधनम्, होतृगृहम्, "
            "पितृगृहम्** — a Hotṛ's money is not a relation of "
            "learning, so the ending goes"),
    Aluk(
        "6.3.24", keeps="ṣaṣṭhī", gana="ṛd-anta-vidyā-yoni",
        uttarapada=("svasṛ", "pati"), optional=True,
        why="विभाषा स्वसृपत्योः — and before स्वसृ and पति, "
            "optionally: **मातुःष्वसा / मातृष्वसा; दुहितुःपतिः / "
            "दुहितृपतिः; ननान्दुःपतिः / ननान्दृपतिः**.\\n\\n"
            "**AND WHICH WAY THE OPTION FALLS DECIDES A LATER "
            "RULE.** **यदा लुक् तदा मातृपितृभ्यां स्वसा इति "
            "नित्यं षत्वम्। यदा त्वलुक् तदा मातुःपितुर्भ्याम् "
            "अन्यतरस्याम् इति विकल्पेन षत्वम्** — drop the "
            "ending and 8.3.84 gives ष् always; keep it and "
            "8.3.85 gives ष् only optionally. So मातुःष्वसा and "
            "मातुःस्वसा both stand beside मातृष्वसा, three forms "
            "from two options meeting. This is the last rule "
            "under अलुक्; 6.3.25 आनङ् replaces the word"),
)


def _reaches(row: Aluk, purvapada: str, gana: str, uttarapada: str,
             uttarapada_gana: str, samasa: str,
             result: str) -> bool:
    """
    Whether one row is even in play.

    The first member may be named by word or by class and the
    second likewise, and inside each side those are alternatives —
    6.3.19 refuses before सिद्ध, before बध् and before anything
    ending in इन्, any one of which is enough. Between the sides
    they are requirements: 6.3.23 wants an ऋ-final word of
    learning or birth in first place AND a word of the same kind
    in second, and one without the other is a different case.
    """
    if row.heading:
        return False
    named = row.of or row.gana
    if named and not (purvapada in row.of
                      or (row.gana and gana == row.gana)):
        return False
    after = row.uttarapada or row.uttarapada_gana
    if after and not (uttarapada in row.uttarapada
                      or (row.uttarapada_gana
                          and uttarapada_gana == row.uttarapada_gana)):
        return False
    if row.samasa and samasa != row.samasa:
        return False
    if row.result and result not in row.result:
        return False
    if row.excludes and (purvapada in row.excludes
                         or uttarapada in row.excludes
                         or gana in row.excludes):
        return False
    return True


def _supplies(row: Aluk, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.keeps and not row.refuses


def _how_specific(row: Aluk, purvapada: str, gana: str,
                  uttarapada: str, uttarapada_gana: str) -> int:
    """
    A refusal beats what it refuses, and a named second member
    beats a named first one.

    The run is arranged by the ending it keeps and then by what
    follows: 6.3.4 and 6.3.5 both name मनस् and are told apart by
    आज्ञायिन् standing after it. And every column is scored on
    whether THIS query matched through it — the lesson 6.1.15 and
    6.2.117 each taught in their own section.
    """
    return (
        10 * bool(row.refuses)
        + 8 * bool(row.uttarapada and uttarapada in row.uttarapada)
        + 7 * bool(row.of and purvapada in row.of)
        + 6 * bool(row.uttarapada_gana
                   and uttarapada_gana == row.uttarapada_gana)
        + 5 * bool(row.gana and gana == row.gana)
        + 4 * bool(row.result)
        + 3 * bool(row.niyama)
        + 2 * bool(row.samasa)
    )


@dataclass(frozen=True)
class Retained:
    """What the run answers: an ending kept, and by which rule."""

    keeps: str
    sutra: str
    why: str
    optional: bool = False
    bahulam: bool = False
    blocked_by: Tuple[str, ...] = ()


def stays(purvapada: str = "", *, gana: str = "",
          uttarapada: str = "", uttarapada_gana: str = "",
          samasa: str = "", result: str = "",
          wants: str = "") -> Retained:
    """
    6.3.1–24 — whether the case ending inside the compound stays.

    Nothing answers by default: where no rule of this run is
    reached, 2.4.71 सुपो धातुप्रातिपदिकयोः stands and the ending is
    dropped, which is what makes every one of these rules worth
    stating.
    """
    matched = [
        row for row in ALUK_TABLE
        if _reaches(row, purvapada, gana, uttarapada,
                    uttarapada_gana, samasa, result)
        and _supplies(row, wants)
    ]
    if not matched:
        return Retained(
            "", "", "No rule of 6.3.1–24 is reached, so 2.4.71 "
                    "सुपो धातुप्रातिपदिकयोः stands and the case "
                    "ending is dropped inside the compound")
    row = max(matched, key=lambda one: _how_specific(
        one, purvapada, gana, uttarapada, uttarapada_gana))
    return Retained("" if row.refuses else row.keeps, row.sutra,
                    row.why, optional=row.optional,
                    bahulam=row.bahulam, blocked_by=row.blocks)


def aluk_runs() -> Retained:
    """
    Where each of 6.3.1's two words stops.

    **अलुगधिकारः प्रागानङः। उत्तरपदाधिकारः प्रागङ्गाधिकारात्** —
    read off the vṛtti and not inferred from where the rules
    happen to leave off.
    """
    return Retained(
        "", ALUK_RUN[0],
        "अलुक् governs %s–%s, stopping because %s आनङ् replaces "
        "it; उत्तरपदे governs %s–%s, the whole pāda, stopping "
        "only at 6.4.1 अङ्गस्य"
        % (ALUK_RUN[0], ALUK_RUN[1], "6.3.25",
           UTTARAPADE_RUN[0], UTTARAPADE_RUN[1]))


def provisions_for(sutra_id: str) -> Tuple[Aluk, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ALUK_TABLE if row.sutra == sutra_id)


__all__ = [
    "Aluk", "ALUK_TABLE", "ALUK_RUN", "UTTARAPADE_RUN", "STOKADI",
    "STOKADI_SENSES", "OJASADI", "OJASADI_VARTIKA", "NIYAMA_THREE",
    "SASTHI_VARTIKA", "NGI_VARTIKA", "NOT_SVANGA", "Retained",
    "stays", "aluk_runs", "provisions_for",
]
