# -*- coding: utf-8 -*-
"""
७.२.३५–७८ — the इट् itself: given, made optional, refused again.

7.2.35 आर्धधातुकस्येड् वलादेः is the rule the whole of 7.2.8–34
was stated before. Every ārdhadhātuka affix beginning with a वल्
sound takes the augment: लविता, लवितुम्, लवितव्यम्. And then
forty-three sūtras argue about it — lengthening it (ग्रहीता),
making it optional for one root at a time (वरिता, वरीता), taking
it away again in the perfect's थल् (पपक्थ), and finally giving it
to five roots before a सार्वधातुक, which is a different affix
class altogether (रोदिति, स्वपिति).

**THE RUN LENGTHENS THE AUGMENT BEFORE IT ARGUES ABOUT IT.**
7.2.37–43 are about the ई of ग्रहीता and तरीता, not about whether
the इ is there: ग्रह् always lengthens outside the perfect, वृ
and the ॠ-final roots do so optionally, and 7.2.39, 7.2.40 then
refuse the lengthening in the optative and the परस्मैपद aorist.
Four rules to place one long vowel.

**AND ONE OF THEM NAMES A TEACHER TO MAKE A RESTRICTION.**
7.2.63 ऋतो भारद्वाजस्य — the थल् refuses its इट् for an ऋ-final
root **in Bhāradvāja's view**, and **सिद्धे सत्यारम्भो
नियमार्थः**, so what the two sūtras before had made compulsory
becomes optional everywhere else: ययिथ, पेचिथ, शेकिथ.

**AND THE LAST THREE ARE ABOUT A DIFFERENT AFFIX CLASS.**
7.2.76–78 give the इट् before a सार्वधातुक, which 7.2.35's
आर्धधातुक had shut out by name. रोदिति, स्वपिति, ईशिषे,
ईडिध्वे — and the vṛtti notes that 7.2.35 says आर्धधातुक rather
than leaving 7.2.76 to restrict it, because reading a restriction
there would cost the reader more.

**WHAT THIS MODULE DOES NOT DO.** It says whether the इट् comes
and how long it is. What the root then does — the guṇa, the
संप्रसारण, the reduplication — is 7.3's and 6.4's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
IT_RUN: Tuple[str, str] = ("7.2.35", "7.2.78")

#: The rule the whole of 7.2.8–34 was stated before.
THE_RULE: str = "7.2.35"

#: Where the run stops being about the ārdhadhātuka.
SARVADHATUKA_FROM: str = "7.2.76"

#: 7.2.45's eight, which take the इट् optionally.
RADHADI: Tuple[str, ...] = (
    "radh", "naś", "tṛp", "dṛp", "druh", "muh", "snuh", "snih")

#: 7.2.48's five, likewise, before a त-initial affix.
TISAHADI: Tuple[str, ...] = ("iṣ", "sah", "lubh", "ruṣ", "riṣ")

#: 7.2.49's eleven named beside the इ-final roots.
SANI_ELEVEN: Tuple[str, ...] = (
    "ṛdh", "bhrasj", "dambh", "śri", "svṛ", "yu", "ūrṇu", "bhṛ",
    "jñap", "san")

#: 7.2.57's five, before a स-initial affix that is not सिच्.
KRTADI_FIVE: Tuple[str, ...] = (
    "kṛt", "cṛt", "chṛd", "tṛd", "nṛt")

#: 7.2.59's four, which refuse it in the परस्मैपद.
VRDADI_FOUR: Tuple[str, ...] = ("vṛt", "vṛdh", "śṛdh", "syand")

#: 7.2.64's four Vedic perfects, laid down whole.
NIGAMA_FOUR: Tuple[str, ...] = (
    "babhūtha", "ātatantha", "jagṛbhma", "vavartha")

#: 7.2.68's four, optional before वसु.
GAMA_FOUR: Tuple[str, ...] = ("gam", "han", "vid", "viś")

#: 7.2.75's five, which take it before सन्.
KIRADI_FIVE: Tuple[str, ...] = ("kṛ", "gṛ", "dṛṅ", "dhṛṅ", "prach")

#: 7.2.76's five, the सार्वधातुक roots: रोदिति, स्वपिति,
#: श्वसिति, प्राणिति, जक्षिति.
RUDADI_FIVE: Tuple[str, ...] = ("rud", "svap", "śvas", "an", "jakṣ")

#: The teacher 7.2.63 names, which is how a view is recorded as a
#: restriction rather than adopted outright.
BHARADVAJA: str = "bhāradvājasya ācāryasya matena"


@dataclass(frozen=True)
class It:
    """One rule of 7.2.35–78: the इट्, its length, or its refusal."""

    sutra: str
    #: `iṭ` where the augment is given, `dīrgha` where the vowel
    #: is lengthened, `sak` where another augment comes with it.
    does: str = "iṭ"
    #: The roots named outright.
    of: Tuple[str, ...] = ()
    #: The root class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow.
    not_before: Tuple[str, ...] = ()
    #: The preverb the root must carry.
    upasarga: str = ""
    #: परस्मैपद or आत्मनेपद.
    pada: str = ""
    #: The sense that licenses it.
    sense: str = ""
    refuses: bool = False
    optional: bool = False
    nipatana: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


IT_TABLE: Tuple[It, ...] = (
    It(
        "7.2.35", before=("val-ādi-ārdhadhātuka",),
        keeps_out="आस्ते, शेते, वस्ते — a सार्वधातुक and not an "
                  "आर्धधातुक; लव्यम्, लवनीयम् — the affix does "
                  "not begin with a वल् sound",
        why="आर्धधातुकस्येड् वलादेः — an ārdhadhātuka affix "
            "beginning with a वल् sound takes the इट्: **लविता, "
            "लवितुम्, लवितव्यम्; पविता, पवितुम्, "
            "पवितव्यम्**.\\n\\n"
            "**THIS IS THE RULE THE WHOLE OF 7.2.8–34 WAS STATED "
            "BEFORE.** Twenty-seven sūtras refuse an augment that "
            "only now exists. And the छन्दस् heading has "
            "lapsed — **छन्दसीति निवृत्तम्**.\\n\\n"
            "**AND IT SAYS आर्धधातुक RATHER THAN LEAVING 7.2.76 "
            "TO RESTRICT IT.** **रुदादिभ्यः सार्वधातुके "
            "इत्येतस्मिन् नियमार्थे विज्ञायमाने प्रतिपत्तिगौरवं "
            "भवति** — a restriction there would have done the "
            "same work and cost the reader more. And इट् is "
            "said twice over, **प्रतिषेधनिवृत्त्यर्थम्**, to end "
            "the refusals that have been running"),
    It(
        "7.2.36", of=("snu", "kram"),
        before=("val-ādi-ārdhadhātuka",),
        not_before=("ātmanepada-nimitta",),
        keeps_out="प्रस्नोषीष्ट, प्रक्रंसीष्ट, प्रस्नोष्यते — the "
                  "root IS the आत्मनेपद's occasion, and the इट् "
                  "does not come",
        why="स्नुक्रमोरनात्मनेपदनिमित्ते — स्नु and क्रम् take "
            "the इट् where they are NOT what occasions an "
            "आत्मनेपद ending: **प्रस्नविता, प्रक्रमिता**.\\n\\n"
            "**AND IT IS A RESTRICTION WHOSE WHOLE POINT IS THE "
            "REFUSAL.** **नियमार्थम् इदम्... प्रतिषेधफलं चेदं "
            "सूत्रम्। स्नुक्रमोर् उदात्तत्वाद् इट् सिद्ध एव** — "
            "both roots are उदात्त and 7.2.35 gives them the "
            "इट् anyway, so stating it again can only be to take "
            "it away in the other case"),
    It(
        "7.2.37", does="dīrgha", of=("grah",),
        not_before=("liṭ",),
        keeps_out="जगृहिव, जगृहिम — the perfect; ग्राहिता, "
                  "ग्राहिष्यते — a चिण्वद् इट्, which is not the "
                  "one running here",
        why="ग्रहोऽलिटि दीर्घः — after ग्रह् the इट् is LONG, "
            "except in the perfect: **ग्रहीता, ग्रहीतुम्, "
            "ग्रहीतव्यम्**. The next seven sūtras are about this "
            "ई and not about whether the इ is there at all"),
    It(
        "7.2.38", does="dīrgha", of=("vṛ",), gana="ṝ-anta",
        not_before=("liṭ",), optional=True,
        keeps_out="करिष्यति, हरिष्यति — neither वृ nor ॠ-final; "
                  "ववरिथ, तेरिथ — the perfect, where अलिटि still "
                  "runs",
        why="वॄतो वा — and after वृ and a ॠ-final root the इट् is "
            "long OPTIONALLY: **वरिता, वरीता; प्रावरिता, "
            "प्रावरीता; तरिता, तरीता; आस्तरिता, आस्तरीता**. "
            "**वृ इति वृङ्वृञोः सामान्येन ग्रहणम्** — one "
            "syllable naming both roots"),
    It(
        "7.2.39", refuses=True, of=("vṛ",), gana="ṝ-anta",
        before=("liṅ",), blocks=("7.2.38",),
        why="न लिङि — but not in the optative: **विवरिषीष्ट, "
            "प्रावरिषीष्ट, आस्तरिषीष्ट, विस्तरिषीष्ट** — the "
            "short इ only"),
    It(
        "7.2.40", refuses=True, of=("vṛ",), gana="ṝ-anta",
        before=("sic",), pada="parasmaipada", blocks=("7.2.38",),
        keeps_out="प्रावरिष्ट, प्रावरीष्ट — आत्मनेपद, where the "
                  "option stands",
        why="सिचि च परस्मैपदेषु — nor before a सिच् followed by a "
            "परस्मैपद ending: **प्रावारिष्टाम्, प्रावारिषुः; "
            "अतारिष्टाम्, अतारिषुः; आस्तारिष्टाम्, "
            "आस्तारिषुः**"),
    It(
        "7.2.41", of=("vṛ",), gana="ṝ-anta", before=("san",),
        optional=True, blocks=("7.2.12",),
        why="इट् सनि वा — and before सन् the इट् itself is "
            "optional: **वुवूर्षते, विवरिषते, विवरीषते; "
            "तितीर्षति, तितरिषति, तितरीषति**. 7.2.12 had refused "
            "it outright for an उक्-final root; this gives the "
            "option back, and 7.2.38's lengthening then applies "
            "on the side where the इट् is there. चिकीर्षति has "
            "none, its ॠ being one a rule made and not one the "
            "उपदेश has"),
    It(
        "7.2.42", of=("vṛ",), before=("liṅ", "sic"),
        pada="ātmanepada", optional=True,
        keeps_out="प्रावारिष्टाम्, प्रावारिषुः — परस्मैपद, where "
                  "7.2.40 refuses the length outright",
        why="लिङ्सिचोरात्मनेपदेषु — and in the आत्मनेपद optative "
            "and aorist the इट् is optional: **वृषीष्ट, "
            "वरिषीष्ट; आस्तरिषीष्ट, आस्तीर्षीष्ट; अवृत, "
            "अवरिष्ट, अवरीष्ट**. The vṛtti gives no "
            "counter-example for the optative — **असंभवाद् "
            "यासुटोऽवलादित्वात्**, its यासुट् does not begin "
            "with a वल् at all"),
    It(
        "7.2.43", gana="ṛ-anta-saṃyoga-ādi", before=("liṅ", "sic"),
        pada="ātmanepada", optional=True,
        keeps_out="च्योषीष्ट, अप्लोष्ट — not ऋ-final; कृषीष्ट, "
                  "आकृत — no cluster at the head",
        why="ऋतश्च संयोगादेः — and for an ऋ-final root that "
            "BEGINS with a cluster: **ध्वृषीष्ट, ध्वरिषीष्ट; "
            "स्मृषीष्ट, स्मरिषीष्ट; अध्वृषाताम्, "
            "अध्वरिषाताम्**. संस्कृषीष्ट has none — its सुट् is "
            "no part of the root as taught"),
    It(
        "7.2.44", of=("svṛ", "sū", "sūya", "dhūñ"), gana="ūdit",
        before=("val-ādi-ārdhadhātuka",), optional=True,
        why="स्वरतिसूतिसूयतिधूञूदितो वा — four roots and every "
            "ऊदित् root take it optionally: **स्वर्ता, स्वरिता; "
            "प्रसोता, प्रसविता; सोता, सविता; धोता, धविता; "
            "विगाढा, विगाहिता; गोप्ता, गोपिता**.\\n\\n"
            "**AND EVERY NAME IN THE LIST IS SHAPED TO EXCLUDE "
            "SOMETHING.** **सूतिसूयत्योर् विकरणनिर्देशः षू "
            "प्रेरणे इत्यस्य निवृत्त्यर्थः** — the roots are "
            "named with their conjugation-signs so that a third "
            "root of the same shape is left out; **धूञिति "
            "सानुबन्धकस्य निर्देशो धू विधूनने इत्यस्य "
            "निवृत्त्यर्थः**, and that one keeps its इट् always. "
            "And वा is said again although वा was running, "
            "**लिङ्सिचोर् निवृत्त्यर्थम्**"),
    It(
        "7.2.45", of=RADHADI, before=("val-ādi-ārdhadhātuka",),
        optional=True,
        why="रधादिभ्यश्च — and eight roots from रध् on: **रद्धा, "
            "रधिता; नंष्टा, नशिता; त्रप्ता, तर्प्ता, तर्पिता; "
            "द्रोग्धा, द्रोढा, द्रोहिता; मोग्धा, मोढा, मोहिता; "
            "स्नेग्धा, स्नेढा, स्नेहिता**.\\n\\n"
            "**AND WHETHER THE OPTION REACHES THE PERFECT IS "
            "DISPUTED.** 7.2.13's restriction makes them सेट् "
            "there; this rule is later and would make it "
            "optional. **केचिद् इच्छन्ति** the option; "
            "**अपरे पुनराहुः — पूर्वविधेर् इण्निषेधविधानसामर्थ्याद् "
            "बलीयस्त्वं प्रतिषेधनियमस्य**, and on that reading "
            "ररन्धिव keeps its इट् without fail"),
    It(
        "7.2.46", of=("kuṣ",), upasarga="nir",
        before=("val-ādi-ārdhadhātuka",), optional=True,
        keeps_out="कोषिता, कोषितुम् — no निर्",
        why="निरः कुषः — and कुष् after निर्: **निष्कोष्टा, "
            "निष्कोषिता; निष्कोष्टव्यम्, निष्कोषितव्यम्**.\\n\\n"
            "**AND THE FORM निरः IS ITSELF A ज्ञापक.** निसः was "
            "what the grammar owed; निरः is written instead, "
            "**रेफान्तम् उपसर्गान्तरम् अस्तीति ज्ञाप्यते** — "
            "there IS a separate र्-final preverb. Which is what "
            "lets 8.2.19's ल् reach निलयनम्: from निस् the "
            "र्-substitution would be असिद्ध and the ल् could "
            "not come"),
    It(
        "7.2.47", of=("kuṣ",), upasarga="nir", before=("niṣṭhā",),
        blocks=("7.2.15", "7.2.46"),
        why="इण्निष्ठायाम् — but in the निष्ठा it is COMPULSORY: "
            "**निष्कुषितः, निष्कुषितवान्**. **इड्ग्रहणं "
            "नित्यार्थम्** — the word इट् is said again to make "
            "it so, and the sūtra exists to beat 7.2.15, which "
            "would otherwise have turned the option before it "
            "into a refusal"),
    It(
        "7.2.48", of=TISAHADI, before=("ta-ādi-ārdhadhātuka",),
        optional=True,
        keeps_out="एषिष्यति — the affix does not begin with त्",
        why="तीषसहलुभरुषरिषः — five roots take it optionally "
            "before a त-initial ārdhadhātuka: **एष्टा, एषिता; "
            "सोढा, सहिता; लोब्धा, लोभिता; रोष्टा, रोषिता; "
            "रेष्टा, रेषिता**. And the इष् meant is **इषु "
            "इच्छायाम्** alone: the दैवादिक and क्र्यादि roots of "
            "that shape keep the इट् always, **प्रेषिता, "
            "प्रेषितुम्**"),
    It(
        "7.2.49", of=SANI_ELEVEN, gana="i-anta", before=("san",),
        optional=True,
        why="सनीवन्तर्धभ्रस्जदम्भुश्रिस्वृयूर्णुभरज्ञपिसनाम् — "
            "इ-final roots and eleven named ones take it "
            "optionally before सन्: **दिदेविषति, दुद्यूषति; "
            "अर्दिधिषति, ईर्त्सति; बिभ्रज्जिषति, बिभ्रक्षति; "
            "दिदम्भिषति, धिप्सति; उच्छिश्रयिषति, उच्छिश्रीषति; "
            "प्रोर्णुनविषति, प्रोर्णुनूषति**. भर is the भ्वादि "
            "भृञ्, and the vṛtti knows it from the conjugation "
            "sign — **शपा निर्देशात्**"),
    It(
        "7.2.50", of=("kliś",), before=("ktvā", "niṣṭhā"),
        optional=True, blocks=("7.2.15",),
        why="क्लिशः क्त्वानिष्ठयोः — क्लिश् takes it optionally "
            "before क्त्वा and the निष्ठा: **क्लिष्ट्वा, "
            "क्लिशित्वा; क्लिष्टः, क्लिशितः**. Two roots of the "
            "shape and two reasons: for **क्लिशू विबाधने** the "
            "option in क्त्वा was already there and 7.2.15 would "
            "have refused the निष्ठा outright; for **क्लिश "
            "उपतापे** the इट् would have been compulsory in "
            "both, **तदर्थं क्त्वाग्रहणं क्रियते**"),
    It(
        "7.2.51", of=("pūṅ",), before=("ktvā", "niṣṭhā"),
        optional=True, blocks=("7.2.11",),
        why="पूङश्च — and पूङ्: **पूत्वा, पवित्वा; सोमोऽतिपूतः, "
            "सोमोऽतिपवितः; पूतवान्, पवितवान्**. 7.2.11 had "
            "refused it for an उक्-final root before a कित्, and "
            "this gives the option back"),
    It(
        "7.2.52", of=("vas", "kṣudh"), before=("ktvā", "niṣṭhā"),
        why="वसतिक्षुधोरिट् — वस् and क्षुध् take it without fail: "
            "**उषित्वा, उषितः, उषितवान्; क्षुधित्वा, क्षुधितः, "
            "क्षुधितवान्**. वस् is named with its conjugation "
            "sign only to be identified — **वसतीति विकरणो "
            "निर्देशार्थ एव** — since being उदात्त it would have "
            "had the इट् anyway; and **पुनरिड्ग्रहणं "
            "नित्यार्थम्**"),
    It(
        "7.2.53", of=("añc",), before=("ktvā", "niṣṭhā"),
        sense="pūjā", blocks=("7.2.15",),
        keeps_out="उदक्तमुदकं कूपात् — water drawn from a well, "
                  "and no honouring meant",
        why="अञ्चेः पूजायाम् — and अञ्च् where HONOURING is "
            "meant: **अञ्चित्वा जानु जुहोति; अञ्चिता अस्य "
            "गुरवः**. 7.2.56 would have made the क्त्वा optional "
            "and 7.2.15 would have refused the निष्ठा; the "
            "sūtra is begun for both, **तदर्थम् इदम् "
            "प्रारब्धम्**"),
    It(
        "7.2.54", of=("lubh",), before=("ktvā", "niṣṭhā"),
        sense="vimohana", blocks=("7.2.15", "7.2.48"),
        keeps_out="लुब्धो वृषलः — pained with cold; and in "
                  "greed the ordinary rules stand, "
                  "**गार्ध्ये यथाप्राप्तम् एव भवति**",
        why="लुभो विमोचने — and लुभ् where CONFUSING is meant: "
            "**लुभित्वा, लोभित्वा; विलुभिताः केशाः; विलुभितः "
            "सीमन्तः**. **विमोहनम् आकुलीकरणम्** — the sense is "
            "hair in disarray and not desire"),
    It(
        "7.2.55", of=("jṝ", "vraśc"), before=("ktvā",),
        blocks=("7.2.11",),
        why="जॄव्रश्च्योः क्त्वि — जॄ and व्रश्च् take it before "
            "क्त्वा: **जरित्वा, जरीत्वा; व्रश्चित्वा**. For जॄ "
            "7.2.11 had refused it and for व्रश्च्, being ऊदित्, "
            "it was an option. **क्त्वाग्रहणं "
            "निष्ठानिवृत्त्यर्थम्** — the निष्ठा running down "
            "from 7.2.50 is cut off here"),
    It(
        "7.2.56", gana="udit", before=("ktvā",), optional=True,
        why="उदितो वा — and an उदित् root takes it optionally "
            "before क्त्वा: **शमित्वा, शान्त्वा; तमित्वा, "
            "तान्त्वा; दमित्वा, दान्त्वा**"),
    It(
        "7.2.57", of=KRTADI_FIVE,
        before=("sa-ādi-ārdhadhātuka",), not_before=("sic",),
        optional=True,
        why="सेऽसिचि कृतचृतच्छृदतृदनृतः — five roots take it "
            "optionally before a स-initial ārdhadhātuka that is "
            "not सिच्: **कर्त्स्यति, कर्तिष्यति; चिकृत्सति, "
            "चिकर्तिषति; छर्त्स्यति, छर्दिष्यति; तर्त्स्यति, "
            "तर्दिष्यति; नर्त्स्यति, नर्तिष्यति**"),
    It(
        "7.2.58", of=("gam",), before=("sa-ādi-ārdhadhātuka",),
        pada="parasmaipada",
        keeps_out="संगंसीष्ट, संगंस्यते, संजिगंसते — आत्मनेपद; "
                  "गन्तास्मि — the affix does not begin with स्",
        why="गमेरिट् परस्मैपदेषु — गम् takes it without fail "
            "before a स-initial ārdhadhātuka in the परस्मैपद: "
            "**गमिष्यति, अगमिष्यत्, जिगमिषति**. **इड्ग्रहणं "
            "नित्यार्थम्**. And the refusal is only where the "
            "root and the आत्मनेपद ending stand in one word — "
            "**आत्मनेपदेन समानपदस्थस्य गमेर् अयम् इडागमो "
            "नेष्यते। अन्यत्र सर्वत्रैवेष्यते**, so संजिगमिषिता "
            "and जिगमिष त्वम् both keep it"),
    It(
        "7.2.59", refuses=True, of=VRDADI_FOUR,
        before=("sa-ādi-ārdhadhātuka",), pada="parasmaipada",
        blocks=("7.2.58",),
        why="न वृद्भ्यश्चतुर्भ्यः — but four roots refuse it "
            "there: **वर्त्स्यति, विवृत्सति; शर्त्स्यति; "
            "स्यन्त्स्यति, सिस्यन्त्सति**.\\n\\n"
            "**AND THE WORD चतुर्भ्यः IS ARGUED TO BE "
            "UNNECESSARY AND KEPT.** The धातुपाठ's own वृत् "
            "already marks where the द्युतादि end; if it marks "
            "the वृतादि too, nothing goes wrong. It is kept so "
            "that स्यन्द्'s ऊदित् option — which is अन्तरङ्ग — "
            "should be beaten by this refusal all the same"),
    It(
        "7.2.60", refuses=True, of=("kḷp",),
        before=("tāsi", "sa-ādi-ārdhadhātuka"),
        pada="parasmaipada", blocks=("7.2.58",),
        keeps_out="कल्पितासे, कल्पिष्यते, चिकल्पिषते — "
                  "आत्मनेपद, where the इट् stands",
        why="तासि च कॢपः — and कॢप् refuses it before तासि too: "
            "**श्वः कल्प्ता; कल्प्स्यति, अकल्प्स्यत्, "
            "चिक्ऌप्सति**. The same rule about one word holds "
            "here — **क्ऌपेरप्य् आत्मनेपदेन समानपदस्थस्य इडागम "
            "इष्यते। अन्यत्र प्रतिषेधः**"),
    It(
        "7.2.61", refuses=True, gana="ac-anta-tāsi-anit",
        before=("thal",),
        keeps_out="बिभेदिथ — the root is not vowel-final; "
                  "लुलविथ — it is not अनिट् before तासि; ययिव, "
                  "ययिम — not the थल्; विदुधविथ — its इट् before "
                  "तासि is optional and not refused",
        why="अचस्तास्वत् थल्यनिटो नित्यम् — a vowel-final root "
            "that is ALWAYS अनिट् before तासि refuses the इट् in "
            "the थल् as well: **ययाथ, चिचेथ, निनेथ, जुहोथ**. "
            "**नित्यग्रहणं** is what shuts out विधोता's "
            "optional case.\\n\\n"
            "**AND तास्वत् IS SAID AS A COMPARISON FOR A "
            "REASON.** **तासौ सतस्थलि प्रतिषेधार्थः। यो हि "
            "तासाव् असन्, असत्त्वात् च नित्यानिट्, तस्य थलि "
            "प्रतिषेधो न भवति** — a root that has no तासि form "
            "at all is not अनिट् there in the required sense, so "
            "जघसिथ and उवयिथ keep their इट्"),
    It(
        "7.2.62", refuses=True, gana="a-vat-upadeśa-tāsi-anit",
        before=("thal",),
        keeps_out="चकर्षिथ — its अ is not there in the उपदेश; "
                  "बिभेदिथ — the root has no अ; रराधिथ — the "
                  "अ is long, and the तपर shuts that out; "
                  "जग्रहिथ — not अनिट् before तासि",
        why="उपदेशेऽत्वतः — and a root that HAS an अ as it is "
            "taught and is अनिट् before तासि: **पपक्थ, इयष्ठ, "
            "शशक्थ**"),
    It(
        "7.2.63", refuses=True, gana="ṛ-anta", before=("thal",),
        blocks=("7.2.61", "7.2.62"),
        why="ऋतो भारद्वाजस्य — an ऋ-final root refuses it in the "
            "थल्, IN BHĀRADVĀJA'S VIEW: **सस्मर्थ, दध्वर्थ**. "
            "**सिद्धे सत्यारम्भो नियमार्थः। ऋत एव भारद्वाजस्य, "
            "नान्येषां धातूनाम्** — a restriction, and what the "
            "two sūtras before had made compulsory becomes "
            "optional everywhere else: **ययिथ, वविथ, पेचिथ, "
            "शेकिथ**. Naming the teacher is Pāṇini's way of "
            "recording a view rather than adopting it"),
    It(
        "7.2.64", of=NIGAMA_FOUR, nipatana=True, chandasi=True,
        blocks=("7.2.13",),
        why="बभूथाततन्थजगृम्भववर्थेति निगमे — four Vedic perfects "
            "laid down whole: **त्वं हि होता प्रथमो बभूथ**, "
            "where the language has बभूविथ; **येनान्तरिक्षम् "
            "उर्वाततन्थ** for आतेनिथ; **जगृभ्मा ते दक्षिणम् "
            "इन्द्र हस्तम्** for जगृहिम; **ववर्थ त्वं हि "
            "ज्योतिषा** for ववरिथ. And it is a restriction and "
            "not a fresh refusal — **निगम एव न भाषायाम् इति**"),
    It(
        "7.2.65", refuses=True, of=("sṛj", "dṛś"), before=("thal",),
        optional=True,
        why="विभाषा सृजिदृशोः — सृज् and दृश् refuse it in the "
            "थल् optionally: **सस्रष्ठ, ससर्जिथ; दद्रष्ठ, "
            "ददर्शिथ**"),
    It(
        "7.2.66", of=("ad", "ṛ", "vye"), before=("thal",),
        blocks=("7.2.63",),
        why="इडत्त्यर्तिव्ययतीनाम् — but अद्, ऋ and व्ये take it "
            "in the थल् without fail: **आदिथ, आरिथ, "
            "विव्ययिथ**. For अद् and व्ये 7.2.63's restriction "
            "had made it optional, for ऋ it was refused "
            "outright; **अत्रेड्ग्रहणं विस्पष्टार्थम्**, the "
            "word इट् being there only to make the rule read "
            "plainly"),
    It(
        "7.2.67", gana="eka-ac-ā-anta-ghas", before=("vasu",),
        why="वस्वेकाजाद्घसाम् — before वसु the इट् comes for a "
            "reduplicated root of ONE syllable, for an आ-final "
            "root, and for घस्: **आदिवान्, आशिवान्, पेचिवान्, "
            "शेकिवान्; ययिवान्, तस्थिवान्; जक्षिवान्**.\\n\\n"
            "**AND *ONE SYLLABLE* IS COUNTED AFTER THE "
            "REDUPLICATION IS DONE.** **धात्वभ्यासयोर् एकादेशे "
            "कृत एत्वाभ्यासलोपयोश्च कृतयोः कृतद्विर्वचना एत "
            "एकाचो भवन्ति** — पच् is two syllables until the "
            "perfect makes it पेच्. And it is a restriction: "
            "**एकाजाद्घसाम् एव वसाव् इडागमो भवति नान्येषाम्**, "
            "so बिभिद्वान् and शिश्रिवान् have none"),
    It(
        "7.2.68", of=GAMA_FOUR, before=("vasu",), optional=True,
        blocks=("7.2.67",),
        why="विभाषा गमहनविदविशाम् — and four roots take it "
            "optionally: **जग्मिवान्, जगन्वान्; जघ्निवान्, "
            "जघन्वान्; विविदिवान्, विविद्वान्; विविशिवान्, "
            "विविश्वान्**. The विद् meant is the तौदादिक one "
            "*to get* — **विशिना साहचर्यात्** — and the one "
            "meaning *to know* keeps विविद्वान् always. A "
            "vārttika adds दृश्: **ददृशिवान्, ददृश्वान्**"),
    It(
        "7.2.69", of=("san",), nipatana=True, chandasi=True,
        why="सनिंससनिवांसम् — ससनिवांसम् is laid down after "
            "सनिम्, with the इट् and with no ए and no "
            "reduplication-loss: **आजिं त्वाग्ने... सनिं "
            "ससनिवांसम्**. Elsewhere it is सेनिवांसम्, and "
            "**भाषायां सेनिवांसम् इति भवति**"),
    It(
        "7.2.70", gana="ṛ-anta", of=("han",), before=("sya",),
        why="ऋद्धनोः स्ये — an ऋ-final root and हन् take it "
            "before स्य: **करिष्यति, हरिष्यति, हनिष्यति**. And "
            "it beats 7.2.44's option for स्वृ by prior "
            "contradiction — **स्वरतेर् वेट्त्वाद् ऋद्धनोः स्य "
            "इत्येतद् भवति विप्रतिषेधेन। स्वरिष्यति**"),
    It(
        "7.2.71", of=("añj",), before=("sic",), blocks=("7.2.44",),
        keeps_out="अङ्क्ता, अञ्जिता — no सिच्, and the ऊदित् "
                  "option stands",
        why="अञ्जेः सिचि — अञ्ज् takes it before सिच्: "
            "**आञ्जीत्, आञ्जिष्टाम्, आञ्जिषुः**. Being ऊदित् it "
            "would only have had the option"),
    It(
        "7.2.72", of=("stu", "su", "dhūñ"), before=("sic",),
        pada="parasmaipada",
        keeps_out="अस्तोष्ट, असोष्ट, अधोष्ट — आत्मनेपद",
        why="स्तुसुधूञ्भ्यः परस्मैपदेषु — स्तु, सु and धूञ् take "
            "it before a सिच् in the परस्मैपद: **अस्तावीत्, "
            "असावीत्, अधावीत्**"),
    It(
        "7.2.73", does="sak-iṭ", of=("yam", "ram", "nam"),
        gana="ā-anta", before=("sic",), pada="parasmaipada",
        keeps_out="आयंस्त, अरंस्त, अनंस्त — आत्मनेपद",
        why="यमरमनमातां सक् च — यम्, रम्, नम् and every आ-final "
            "stem take the augment सक् AND the इट् before a "
            "सिच् in the परस्मैपद: **अयंसीत्, व्यरंसीत्, "
            "अनंसीत्; आयासीत्, अयासिष्टाम्**. 7.2.3 would have "
            "given the four consonant-final ones vṛddhi, and "
            "7.2.4 refuses it once the इट् is there"),
    It(
        "7.2.74", of=("smiṅ", "pūṅ", "ṛ", "añjū", "aśū"),
        before=("san",),
        keeps_out="पुपूषति — पूञ्, which the ङ् of पूङ् shuts out",
        why="स्मिपूङ्रञ्ज्वशां सनि — five roots take it before "
            "सन्: **सिस्मयिषते, पिपविषते, अरिरिषति, "
            "अञ्जिजिषति, अशिशिषते**. **ङकारग्रहणं पूञो मा "
            "भूत्** — the marker is there to keep the other पू "
            "out, and अश् is named as the ऊदित् one so that "
            "अश्नाति keeps its इट् always"),
    It(
        "7.2.75", of=KIRADI_FIVE, before=("san",),
        blocks=("7.2.41",),
        keeps_out="सिसृक्षति — not one of the five",
        why="किरश्च पञ्चभ्यः — and five more: **चिकरिषति, "
            "जिगरिषति, दिदरिषते, दिधरिषते, पिपृच्छिषति**. "
            "7.2.41 had made it optional for कॄ and गॄ; this "
            "makes it compulsory, and the lengthening of 7.2.38 "
            "is not wanted here — **वृतो वा इति चास्येटो "
            "दीर्घत्वं नेच्छन्ति**"),
    It(
        "7.2.76", of=RUDADI_FIVE,
        before=("val-ādi-sārvadhātuka",),
        keeps_out="जागर्ति — not one of the five; स्वप्ता — an "
                  "ārdhadhātuka; रुदन्ति — the affix does not "
                  "begin with a वल्",
        why="रुदादिभ्यः सार्वधातुके — five roots take the इट् "
            "before a वल्-initial सार्वधातुक: **रोदिति, "
            "स्वपिति, श्वसिति, प्राणिति, जक्षिति**. This is the "
            "affix class 7.2.35 shut out by name, and the last "
            "three sūtras of the run are all about it"),
    It(
        "7.2.77", of=("īś",), before=("se",),
        why="ईशः से — and ईश् before से: **ईशिषे, ईशिष्व**. One "
            "root and one ending, and the sūtra says no more "
            "than that — but the next one is read by some so as "
            "to catch ईशिध्वे as well, which would make this "
            "rule's से the smaller half of a pair"),
    It(
        "7.2.78", of=("īḍ", "jan"), before=("dhve", "se"),
        why="ईडजनोर्ध्वे च — and ईड् and जन् before ध्वे and से: "
            "**ईडिध्वे, ईडिध्वम्, ईडिषे, ईडिष्व; जनिध्वे, "
            "जनिषे, जनिष्व**.\\n\\n"
            "**AND SOME READ THE SŪTRA DIFFERENTLY TO CATCH ONE "
            "MORE FORM.** **ध्वेशब्द ईशेरपि इडागम इष्यते — "
            "ईशिध्वे, ईशिध्वम् इति। तदर्थं केचिद् ईडिजनोः "
            "स्ध्वे च इति सूत्रं पठन्ति** — a variant reading "
            "recorded rather than settled"),
)


def _reaches(row: It, root: str, gana: str, before: str,
             upasarga: str, pada: str, sense: str,
             chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (root in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.not_before and before in row.not_before:
        return False
    if row.upasarga and upasarga != row.upasarga:
        return False
    if row.pada and pada != row.pada:
        return False
    if row.sense and sense != row.sense:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: It, root: str, gana: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, a named
    root beats a named class, and a named sense beats both.

    7.2.58, 7.2.59 and 7.2.60 are the stretch that needs the
    first: गम् takes the इट् before a स-initial affix, and four
    roots and कॢप् take it back again.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of and root in row.of)
        + 6 * bool(row.sense)
        + 5 * bool(row.gana and gana == row.gana)
        + 4 * bool(row.upasarga)
        + 3 * bool(row.before)
        + 2 * bool(row.pada)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Given:
    """What the run answers: the इट्, its length, or its refusal."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def the_it(root: str = "", *, gana: str = "", before: str = "",
           upasarga: str = "", pada: str = "", sense: str = "",
           chandasi: bool = False, wants: str = "") -> Given:
    """
    7.2.35–78 — the इट् given, lengthened, made optional, refused.

    Nothing answers by default, and the default here is not the
    augment: it is that no rule of this run has been reached, and
    whether the इट् comes then depends on 7.2.8–34, which was
    stated first.
    """
    matched = [
        row for row in IT_TABLE
        if _reaches(row, root, gana, before, upasarga, pada, sense,
                    chandasi)
        and (not wants or (wants == row.does and not row.refuses))
    ]
    if not matched:
        return Given(
            "", "", "No rule of 7.2.35-78 is reached, so whether "
                    "the it comes is left to 7.2.8-34")
    row = max(matched, key=lambda one: _how_specific(one, root, gana))
    return Given("" if row.refuses else row.does, row.sutra,
                 row.why, optional=row.optional,
                 nipatana=row.nipatana, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[It, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in IT_TABLE if row.sutra == sutra_id)


__all__ = [
    "It", "IT_TABLE", "IT_RUN", "THE_RULE", "SARVADHATUKA_FROM",
    "RADHADI", "TISAHADI", "SANI_ELEVEN", "KRTADI_FIVE",
    "VRDADI_FOUR", "NIGAMA_FOUR", "GAMA_FOUR", "KIRADI_FIVE",
    "RUDADI_FIVE", "BHARADVAJA", "Given", "the_it",
    "provisions_for",
]
