# -*- coding: utf-8 -*-
"""
७.४.५८–९७ — अभ्यासस्य, the last heading of the adhyāya.

7.4.58 अत्र लोपोऽभ्यासस्य does two things at once. It drops the
copy outright in the environment just left behind — **सनि मीमा
इत्यादि मुचोऽकर्मकस्य इति यावत्**, which is 7.4.54–57 — and it
opens a heading: **अभ्यासस्य इत्येतच् च अधिकृतं वेदितव्यम् आ
अध्यायपरिसमाप्तेः**. Everything from here to 7.4.97 is about the
reduplicated copy and nothing else, and no later sūtra has to
say so.

**WHAT THE COPY LOSES.** 7.4.60 हलादिः शेषः keeps its first
consonant and drops the rest, and 7.4.61 शर्पूर्वाः खयः keeps
instead the खय् that a शर् stands before — which is why श्च्युत्
gives चुश्च्योतिषति and not *शुश्च्योतिषति.

**WHAT IT CHANGES.** A guttural or ह् becomes a palatal (7.4.62
चकार, जगाम, जहार), unless the root is कव् before यङ् (7.4.63
कोकूयते) or कृष् before यङ् in the Veda (7.4.64 करिकृष्यते).

**WHAT IT TAKES.** Before लिट्: saṃprasāraṇa for व्यथ् (7.4.68
विव्यथे), length for इण् (7.4.69 ईयतुः), length for an initial
अ (7.4.70 आट) — and then a नुट् for what follows (7.4.71
आनङ्ग). Before श्लु: guṇa for three (7.4.75 नेनेक्ति) and इ for
five (7.4.76–77 बिभर्ति, जिहीते, इयर्ति). Before सन्: इ for an
अ-final copy (7.4.79 पिपक्षति) and for a उ-final one in a named
following (7.4.80 पिपविषते). Before यङ् and यङ्लुक्: नीक् for
eight (7.4.84 वनीवच्यते), नुक् for the nasal-final (7.4.85
तन्तन्यते) and eight more (7.4.86–87 जञ्जप्यते, चञ्चूर्यते).

**AND THE COPY CAN BE MADE TO ACT AS IF सन् FOLLOWED.** 7.4.93
सन्वल्लघुनि चङ्परेऽनग्लोपे is the rule the causal aorist turns
on: with a णि that चङ् follows, and a light root-syllable, and
nothing lost, the copy does what 7.4.79 and 7.4.80 would have
made it do — **अचीकरत्, अपीपचत्, अपीपवत्** — and 7.4.94 दीर्घो
लघोः then lengthens it.

**WHAT THIS MODULE DOES NOT DO.** That there is a copy at all is
6.1.1's; which affixes are सन्, यङ्, श्लु and चङ् is अध्याय ३'s.
Seven sūtras of this stretch — 7.4.59, 7.4.60, 7.4.66, 7.4.82,
7.4.83, 7.4.90 and 7.4.91 — were codified long before the pāda
was read, inside the reduplication itself, and are named in
`CODIFIED_APART` rather than restated here.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.kiti_sani import (  # noqa: E402
    AP_JNAP_RDH,
    MI_MA_EIGHT,
)

#: This module's stretch — and the whole of the अभ्यासस्य heading.
ABHYASA_RUN: Tuple[str, str] = ("7.4.58", "7.4.97")

#: Where the heading opened by 7.4.58 stops: the adhyāya's end.
ADHIKARA_TO: str = "7.4.97"

#: Codified inside the reduplication itself, long before this
#: pāda was read. `dvirvacana.py` holds them; nothing here
#: restates them.
CODIFIED_APART: Tuple[str, ...] = (
    "7.4.59", "7.4.60", "7.4.66", "7.4.82", "7.4.83",
    "7.4.90", "7.4.91")

#: 7.4.58's अत्र — the stems 7.4.54–57 named, whose copy goes.
#: 7.4.54's eight and 7.4.55's three are imported rather than
#: written out again; दम्भ् is 7.4.56's and मुच् 7.4.57's.
ATRA: Tuple[str, ...] = MI_MA_EIGHT + AP_JNAP_RDH + ("dambh", "muc")

#: 7.4.65's eighteen Vedic forms, laid down whole.
NIPATANA_EIGHTEEN: Tuple[str, ...] = (
    "dādharti", "dardharti", "dardharṣi", "bobhūtu", "tetikte",
    "alarṣi", "āpanīphaṇat", "saṃsaniṣyadat", "karikrat",
    "kanikradat", "bharibhrat", "davidhvataḥ", "davidyutat",
    "taritrataḥ", "sarīsṛpatam", "varīvṛjat", "marmṛjya",
    "āganīganti")

#: 7.4.75's three, whose copy takes guṇa before श्लु.
NIJADI_THREE: Tuple[str, ...] = ("ṇij", "vij", "viṣlṛ")

#: 7.4.76's three, whose copy takes इ before श्लु.
BHRNADI_THREE: Tuple[str, ...] = ("bhṛñ", "māṅ", "ohāṅ")

#: 7.4.77's two, added to them.
ARTI_PIPARTI: Tuple[str, ...] = ("ṛ", "pṝ")

#: 7.4.81's six, whose copy takes इ only optionally.
SRAVATI_SIX: Tuple[str, ...] = (
    "sru", "śru", "dru", "pru", "plu", "cyu")

#: 7.4.84's eight, whose copy takes नीक्.
VANCU_EIGHT: Tuple[str, ...] = (
    "vañc", "sraṃs", "dhvaṃs", "bhraṃs", "kas", "pat", "pad",
    "skand")

#: 7.4.86's six, whose copy takes नुक्.
JAPADI_SIX: Tuple[str, ...] = (
    "jap", "jabh", "dah", "daṃś", "bhañj", "paś")

#: 7.4.87–89's two, which take नुक्, and then a उ after the copy.
CAR_PHAL: Tuple[str, ...] = ("car", "phal")

#: 7.4.95's seven, whose copy takes a short अ before चङ्.
SMRADI_SEVEN: Tuple[str, ...] = (
    "smṛ", "dṝ", "tvar", "prath", "mrad", "stṝ", "spaś")

#: 7.4.96's two, which take it only optionally.
VESTI_CESTI: Tuple[str, ...] = ("veṣṭ", "ceṣṭ")


@dataclass(frozen=True)
class Abhyasa:
    """One rule of 7.4.58–97: what the reduplicated copy does."""

    sutra: str
    #: `lopa`, `śeṣa`, `cu`, `saṃprasāraṇa`, `dīrgha`, `nuṭ`,
    #: `a`, `guṇa`, `it`, `nīk`, `nuk`, `ut`, `ruk-rik-rīk`,
    #: `sanvat`, `at`, `ī`, `nipātana`.
    does: str = ""
    #: The roots or ready-made forms named outright.
    of: Tuple[str, ...] = ()
    #: The shape of the copy, or of the stem, instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: Which piece the rule reaches. Empty is the copy itself,
    #: which the heading supplies; `para` is what stands AFTER
    #: it, which three sūtras reach instead.
    part: str = ""
    #: A further condition on the environment.
    result: Tuple[str, ...] = ()
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    #: True where the sūtra only takes a rule away.
    refuses: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ABHYASA_TABLE: Tuple[Abhyasa, ...] = (
    Abhyasa(
        "7.4.58", does="lopa", of=ATRA, before=("sa-ādi-san",),
        why="अत्र लोपोऽभ्यासस्य — in the environment just left "
            "behind the copy goes altogether: **सनि मीमाघुरभ"
            "लभशकपतपदाम् इति यावत् मुचोऽकर्मकस्य इति**, which "
            "is 7.4.54–57. मित्सति, दित्सति, आरिप्सते — the "
            "reduplication is made and then taken away, and "
            "what is left has only the इस् those rules gave."
            "\\n\\n"
            "**AND THE SŪTRA OPENS THE LAST HEADING OF THE "
            "ADHYĀYA.** **अभ्यासस्य इत्येतच् च अधिकृतं "
            "वेदितव्यम् आ अध्यायपरिसमाप्तेः। इत उत्तरं यद् "
            "वक्ष्यामः अभ्यासस्य इत्येवं तद् वेदितव्यम्** — "
            "everything from 7.4.59 to 7.4.97 is about the "
            "copy, and none of the forty sūtras has to say so "
            "again. The Kāśikā proves the heading on the very "
            "next rule: 7.4.59 ह्रस्वः is one word, and it is "
            "the copy that shortens — डुढौकिषते, तुत्रौकिषते."
            "\\n\\n"
            "**AND अत्र IS IN THE SŪTRA TO FENCE THE LOSS IN.** "
            "The loss could have been packed into 7.4.54 itself "
            "— **इत्येवं सिद्धे यद् अत्रग्रहणम् इह क्रियते, तद् "
            "विषयावधारणार्थम्** — and it is stated separately "
            "so that HERE and nowhere later is where the copy "
            "goes. Without it the heading would carry the loss "
            "down with it"),
    Abhyasa(
        "7.4.61", does="śeṣa", gana="śar-pūrva-khay",
        blocks=("7.4.60",),
        keeps_out="पपाच — the च् has no शर् before it; सस्नौ — "
                  "the न् is not a खय्",
        why="शर्पूर्वाः खयः — of the copy the खय् that a शर् "
            "stands before are what remain, and the other "
            "consonants go: **शर्पूर्वाः खयः शिष्यन्ते, अन्ये "
            "हलो लुप्यन्ते**. श्च्युत् gives **चुश्च्योतिषति**, "
            "स्था **तिष्ठासति**, स्पन्द् **पिस्पन्दिषते** — in "
            "each the copy keeps its SECOND consonant and drops "
            "the first, which is exactly what 7.4.60 would not "
            "have done.\\n\\n"
            "**AND A VĀRTTIKA WIDENS शर् TO खर्.** **खर्पूर्वाः "
            "खय इति वक्तव्यम्** — for उचिच्छिषति, where उच्छ् "
            "takes its तुक् first, being अन्तरङ्ग, and the copy "
            "is then त्छ्; त् is a खर् and not a शर्, so without "
            "the vārttika 7.4.60 would keep the त् and the form "
            "would be heard with one"),
    Abhyasa(
        "7.4.62", does="cu", gana="ku-ha",
        why="कुहोश्चुः — a guttural or ह् in the copy becomes "
            "the answering palatal: **चकार, चखान, जगाम, जघान**, "
            "and for ह् **जहार, जिहीर्षति, जहौ**. This is why a "
            "reduplicated perfect almost never begins with the "
            "sound its root begins with, and why the copy of "
            "गम् is ज and not ग"),
    Abhyasa(
        "7.4.63", of=("kav",), before=("yaṅ",), refuses=True,
        blocks=("7.4.62",),
        keeps_out="चुकुवे — the perfect and not यङ्, where the "
                  "palatal comes as usual",
        why="न कवतेर्यङि — but NOT of कव् before यङ्: "
            "**कोकूयते उष्ट्रः, कोकूयते स्वरः**, where 7.4.62 "
            "would have given *चोकूयते. The root is named by "
            "its conjugated shape — **कवतेः इति विकरणनिर्देशः "
            "कौतेः कुवतेश्च निवृत्त्यर्थः** — so that कौति and "
            "कुवति, which look the same in the root list, are "
            "left out and keep their palatal: **चोकूयते**"),
    Abhyasa(
        "7.4.64", of=("kṛṣ",), before=("yaṅ",), chandasi=True,
        refuses=True, blocks=("7.4.62",),
        keeps_out="चरीकृष्यते कृषीवलः — outside the Veda, where "
                  "the palatal stands",
        why="कृषेश्छन्दसि — and not of कृष् before यङ् IN THE "
            "VEDA: **करिकृष्यते यज्ञकुणपः**. The pair is the "
            "cleanest test of a छन्दसि refusal anywhere in the "
            "pāda — करिकृष्यते in the Veda against चरीकृष्यते "
            "in the spoken language, one and the same root, "
            "one and the same affix, and only the register "
            "telling them apart"),
    Abhyasa(
        "7.4.65", does="nipātana", of=NIPATANA_EIGHTEEN,
        chandasi=True, nipatana=True,
        why="दाधर्तिदर्धर्ति…आगनीगन्तीति च — eighteen Vedic "
            "forms laid down whole: **दाधर्ति, दर्धर्ति, "
            "दर्धर्षि, बोभूतु, तेतिक्ते, अलर्षि, आपनीफणत्, "
            "संसनिष्यदत्, करिक्रत्, कनिक्रदत्, भरिभ्रत्, "
            "दविध्वतः, दविद्युतत्, तरित्रतः, सरीसृपतम्, "
            "वरीवृजत्, मर्मृज्य, आगनीगन्ति**.\\n\\n"
            "**EACH IS TAKEN APART IN THE VṚTTI, AND THE FIRST "
            "THREE SHOW THE METHOD.** **दाधर्ति दर्धर्ति "
            "दर्धर्षि इति धारयतेः, धृङो वा श्लौ यङ्लुकि वा "
            "अभ्यासस्य दीर्घत्वं णिलोपश्च** — from धारि or from "
            "धृङ्, in the श्लु or in the यङ्लुक्, with the copy "
            "lengthened and the णि lost. Three derivations are "
            "offered and none is chosen, because a निपातन does "
            "not need one: the form is given, and the grammar "
            "is only asked to make room for it"),
    Abhyasa(
        "7.4.67", does="saṃprasāraṇa", of=("dyut", "svāpi"),
        keeps_out="स्वापकीयति — क्यच् on स्वापक, where the "
                  "affix that made the copy is no longer next "
                  "to it",
        why="द्युतिस्वाप्योः सम्प्रसारणम् — the copy of द्युत् "
            "and of स्वापि takes saṃprasāraṇa: **विदिद्युते, "
            "व्यदिद्युतत्, विदिद्योतिषते, विदेद्युत्यते**; and "
            "**सुष्वापयिषति**. The स्वापि meant is the causal "
            "— **स्वापिः ण्यन्तो गृह्यते** — and the vṛtti adds "
            "a condition the sūtra does not state: **तस्य "
            "अभ्यासनिमित्तेन प्रत्ययेन आनन्तर्ये सति "
            "सम्प्रसारणम् इष्यते**, the affix that caused the "
            "reduplication must stand next to the stem"),
    Abhyasa(
        "7.4.68", does="saṃprasāraṇa", of=("vyath",),
        before=("liṭ",), blocks=("7.4.60",),
        keeps_out="वाव्यथ्यते — यङ् and not the perfect",
        why="व्यथो लिटि — and the copy of व्यथ् in the perfect: "
            "**विव्यथे, विव्यथाते, विव्यथिरे**. The rule is "
            "stated for what it saves: 7.4.60 was about to drop "
            "the य् as a later consonant — **हलादिः शेषेण "
            "यकारस्य निवृत्तौ प्राप्तायां सम्प्रसारणं क्रियते** "
            "— and the saṃprasāraṇa turns it into इ instead. "
            "The व् is not touched, because 6.1.37 refuses a "
            "saṃprasāraṇa inside a saṃprasāraṇa"),
    Abhyasa(
        "7.4.69", does="dīrgha", of=("iṇ",), before=("liṭ-kit",),
        keeps_out="इयाय, इययिथ — the perfect endings that are "
                  "not कित्",
        why="दीर्घ इणः किति — the copy of इण् lengthens before "
            "a कित् perfect: **ईयतुः, ईयुः**. The derivation "
            "runs backwards through 6.4.81: **इणो यण् इति "
            "यणादेशे कृते स्थानिवद्भावाद् द्विर्वचनम्** — इ "
            "becomes य्, the substitute stands for what it "
            "replaced, and so there is a vowel there to copy at "
            "all. Without स्थानिवद्भाव इ + अतुस् would have no "
            "syllable to reduplicate"),
    Abhyasa(
        "7.4.70", does="dīrgha", gana="a-ādi", before=("liṭ",),
        keeps_out="पपाच, पपाठ — the अ is not the copy's FIRST "
                  "sound but its only one, and आदेः is not met",
        why="अत आदेः — an अ at the START of the copy lengthens "
            "in the perfect: **आट, आटतुः, आटुः**. It is stated "
            "against a rule that would otherwise have merged "
            "the two vowels — **अतो गुणे पररूपत्वस्य अपवादः** "
            "— for अट् + अ + अट् would give अटतुः by 6.1.97 and "
            "the copy would vanish into the root. Length keeps "
            "it visible, and every ordinary परस्मैपद perfect of "
            "an अ-initial root shows it"),
    Abhyasa(
        "7.4.71", does="nuṭ", gana="dvi-hal", before=("liṭ",),
        part="para",
        keeps_out="आट, आटतुः, आटुः — अट् has one consonant and "
                  "not two",
        why="तस्मान्नुड् द्विहलः — after that lengthened अ, a "
            "stem of TWO consonants takes नुट्: **आनङ्ग, "
            "आनङ्गतुः, आनङ्गुः; आनञ्ज, आनञ्जतुः, आनञ्जुः**. "
            "The rule reaches not the copy but what stands "
            "after it, which is why it is the one sūtra of the "
            "heading that has to name its own target. And ऋ "
            "counts as carrying a consonant — **ऋकारैकदेशो "
            "रेफो हल्ग्रहणेन गृह्यते** — so ऋध् too: "
            "**आनृधतुः, आनृधुः**"),
    Abhyasa(
        "7.4.72", does="nuṭ", of=("aśnoti",), before=("liṭ",),
        part="para",
        keeps_out="आश, आशतुः, आशुः — अश्नाति of the ninth "
                  "class, which the conjugated naming leaves "
                  "out",
        why="अश्नोतेश्च — and अश्नोति takes it too: **व्यानशे, "
            "व्यानशाते, व्यानशिरे**. The root is named by its "
            "fifth-class shape on purpose — **अश्नोतेः इति "
            "विकरणनिर्देशः अश्नातेर् मा भूत् इति** — so that "
            "the ninth-class अश् 'eat' is not reached, and it "
            "keeps the plain आश"),
    Abhyasa(
        "7.4.73", does="a", of=("bhavati",), before=("liṭ",),
        keeps_out="बुभूषति, बोभूयते — सन् and यङ्, not the "
                  "perfect; अनुबभूवे कम्बलो देवदत्तेन",
        why="भवतेरः — the copy of भू becomes अ in the perfect: "
            "**बभूव, बभूवतुः, बभूवुः**. Without it the copy "
            "would be बु and the commonest perfect in the "
            "language would read *बुभूव. The root is again "
            "named by its conjugated shape — **भवतेः इति "
            "कृतविकरणनिर्देशाद्** — which the vṛtti uses to "
            "keep out **अनुबभूवे कम्बलो देवदत्तेन**, where the "
            "sense is not the ordinary one"),
    Abhyasa(
        "7.4.74", does="nipātana", of=("sasūva",), chandasi=True,
        nipatana=True,
        keeps_out="सुषुवे इति भाषायाम् — outside the Veda the "
                  "ordinary form stands",
        why="ससूवेति निगमे — **ससूव** is laid down for the "
            "Veda: **ससूव स्थविरं विपश्चिताम्**. Three things "
            "are given at once and none of them would come "
            "otherwise — **सूतेर् लिटि परस्मैपदं वुगागमः "
            "अभ्यासस्य च अत्वं निपात्यते**: a root that takes "
            "आत्मनेपद is given a परस्मैपद ending, a वुक् is put "
            "in, and the copy becomes अ. The spoken language "
            "keeps सुषुवे, and the two forms sit side by side "
            "in the vṛtti as the measure of what a निपातन "
            "costs"),
    Abhyasa(
        "7.4.75", does="guṇa", of=NIJADI_THREE, before=("ślu",),
        keeps_out="निनेज — the perfect and not the श्लु",
        why="निजां त्रयाणां गुणः श्लौ — the copy of णिज्, विज् "
            "and विष्लृ takes guṇa when श्लु follows: "
            "**नेनेक्ति, वेवेक्ति, वेवेष्टि**. **त्रिग्रहणम् "
            "उत्तरार्थम्** — saying THREE is not needed here, "
            "since the root list marks just these three, and it "
            "is said for the next sūtra, which borrows the word "
            "and needs it"),
    Abhyasa(
        "7.4.76", does="it", of=BHRNADI_THREE, before=("ślu",),
        keeps_out="जहाति — ओहाक् and not ओहाङ्, a fourth root "
                  "the त्रयाणाम् shuts out; बभार — the perfect",
        why="भृञामित् — the copy of भृञ्, माङ् and ओहाङ् becomes "
            "इ when श्लु follows: **बिभर्ति, मिमीते, जिहीते**. "
            "The THREE carried down from the sūtra before is "
            "doing real work: भृञ् is first in the root list "
            "and भृञादि could have been read as a whole class, "
            "and the count stops it at three — which is how "
            "**जहाति** keeps its अ"),
    Abhyasa(
        "7.4.77", does="it", of=ARTI_PIPARTI, before=("ślu",),
        why="अर्तिपिपर्त्योश्च — and the copy of ऋ and of पॄ: "
            "**इयर्ति भूमम्; पिपर्ति सोमम्**. The two are named "
            "by their finished third-person forms, अर्ति and "
            "पिपर्ति, and not by their root shapes — the same "
            "device 7.4.63, 7.4.72 and 7.4.73 use, and here it "
            "settles which of the several roots written ऋ and "
            "पॄ is meant"),
    Abhyasa(
        "7.4.78", does="it", before=("ślu",), chandasi=True,
        optional=True,
        keeps_out="ददाति, जजनदिन्द्रम्, माता यद्वीरं दधनद्" +
                  "धनिष्ठा — the same Veda leaving it undone",
        why="बहुलं छन्दसि — and in the Veda the इ comes "
            "VARIOUSLY before श्लु, on roots no other rule "
            "names: **पूर्णां विवष्टि** from वश्, **जनिमा "
            "विवक्ति** from वच्, **वत्सं न माता सिषक्ति** from "
            "सच्, **जघर्ति सोमम्**. And बहुलम् cuts the other "
            "way too — **न च भवति। ददाति इत्येवं ब्रूयात्। "
            "जजनदिन्द्रम्** — so that the Veda both extends the "
            "rule past its list and declines it where the list "
            "would have given it"),
    Abhyasa(
        "7.4.79", does="it", gana="a-anta", before=("san",),
        keeps_out="पपाच — the perfect and not सन्; लुलूषति — "
                  "the copy is उ-final; पापचिषते — the तपर "
                  "keeps a long आ out",
        why="सन्यतः — before सन् a SHORT-अ-final copy becomes "
            "इ: **पिपक्षति, यियक्षति, तिष्ठासति, पिपासति**. "
            "This is the rule the whole desiderative is heard "
            "by, and the तपर in अतः is what keeps पापचिषते — "
            "the यङ् stem's long-आ copy — out of its reach"),
    Abhyasa(
        "7.4.80", does="it", gana="u-anta", before=("san",),
        result=("pa-varga-a-para", "yaṇ-a-para", "ja-a-para"),
        why="ओः पुयण्ज्यपरे — and a उ-final copy becomes इ "
            "before सन् when what follows is a प-वर्ग sound, a "
            "यण् or ज् with अ-वर्ण after it: **पिपविषते, "
            "पिपावयिषति, बिभावयिषति** for the first, "
            "**यियविषति, यियावयिषति, रिरावयिषति, लिलावयिषति** "
            "for the second, and **जिजावयिषति** for the third, "
            "from the root जु the sūtras alone attest.\\n\\n"
            "**AND THE SŪTRA IS READ AS PROOF OF SOMETHING "
            "ELSE.** **एतदेव पुयण्ज्यपरे इति वचनं ज्ञापकम्** — "
            "the three conditions would be idle unless the "
            "reduplication were already in place when this rule "
            "ran, so the order of the two is settled by the "
            "sūtra having anything to say at all"),
    Abhyasa(
        "7.4.81", does="it", of=SRAVATI_SIX, before=("san",),
        result=("yaṇ-a-para",), optional=True, blocks=("7.4.80",),
        why="स्रवतिशृणोतिद्रवतिप्रवतिप्लवतिच्यवतीनां वा — but "
            "for these six the इ comes only OPTIONALLY: "
            "**सिस्रावयिषति, सुस्रावयिषति; शिश्रावयिषति, "
            "शुश्रावयिषति; दिद्रावयिषति, दुद्रावयिषति; "
            "पिप्रावयिषति, पुप्रावयिषति; पिप्लावयिषति, "
            "पुप्लावयिषति; चिच्यावयिषति, चुच्यावयिषति**. All "
            "six are named by their conjugated forms and all "
            "six fall under 7.4.80's यण् with अ after it, so "
            "the sūtra is a विभाषा of exactly one of that "
            "rule's three cases"),
    Abhyasa(
        "7.4.84", does="nīk", of=VANCU_EIGHT,
        before=("yaṅ", "yaṅ-luk"),
        why="नीग्वञ्चुस्रंसुध्वंसुभ्रंसुकसपतपदस्कन्दाम् — the "
            "copy of these eight takes नीक् before यङ् and "
            "before the यङ्लुक्: **वनीवच्यते, वनीवञ्चीति; "
            "सनीस्रस्यते, सनीस्रंसीति; दनीध्वस्यते, "
            "दनीध्वंसीति; बनीभ्रस्यते, बनीभ्रंसीति; "
            "चनीकस्यते, चनीकसीति; पनीपत्यते, पनीपतीति; "
            "पनीपद्यते, पनीपदीति; चनीस्कद्यते**. Each pair is "
            "the same stem twice over, once with the यङ् heard "
            "and once with it dropped, and the augment is "
            "indifferent to which"),
    Abhyasa(
        "7.4.85", does="nuk", gana="anunāsika-anta",
        before=("yaṅ", "yaṅ-luk"),
        why="नुगतोऽनुनासिकान्तस्य — the अ-final copy of a "
            "nasal-final stem takes नुक् before यङ् and the "
            "यङ्लुक्: **तन्तन्यते, तन्तनीति; जङ्गम्यते, "
            "जङ्गमीति; यंयम्यते, यंयमीति; रंरम्यते, रंरमीति**."
            "\\n\\n"
            "**AND THE नुक् IS WRITTEN FOR AN ANUSVĀRA.** "
            "**नुक् इत्येतद् अनुस्वारोपलक्षणार्थं द्रष्टव्यम्। "
            "स्थानिना हि आदेशो लक्ष्यते** — the न् is named "
            "because the anusvāra that actually appears is its "
            "substitute, which is why **यंयम्यते** shows one "
            "even where no झल् follows and 8.3.23 would not "
            "have given it"),
    Abhyasa(
        "7.4.86", does="nuk", of=JAPADI_SIX,
        before=("yaṅ", "yaṅ-luk"),
        why="जपजभदहदशभञ्जपशां च — and the copy of these six: "
            "**जञ्जप्यते, जञ्जपीति; जञ्जभ्यते; दन्दह्यते, "
            "दन्दहीति; दन्दश्यते, दन्दशीति; बम्भज्यते, "
            "बम्भञ्जीति; पम्पश्यते**. Two of the six are "
            "written short on purpose: दश is the root दंश् — "
            "**दश इति दंशिः अयं नकारलोपार्थम् एव निर्दिष्टः। "
            "तेन यङ्लुक्यपि नकारलोपो भवति** — and पश is a root "
            "the sūtras alone attest, **पश इति सौत्रो धातुः**, "
            "which is why it is written with no marker at all"),
    Abhyasa(
        "7.4.87", does="nuk", of=CAR_PHAL,
        before=("yaṅ", "yaṅ-luk"),
        why="चरफलोश्च — and the copy of चर् and फल्: "
            "**चञ्चूर्यते, चञ्चूरीति; पम्फुल्यते, पम्फुलीति**. "
            "The two are taken out of the list before them "
            "because the next sūtra needs them by themselves — "
            "they alone go on to change the vowel that follows "
            "the copy as well as the copy itself"),
    Abhyasa(
        "7.4.88", does="ut", of=CAR_PHAL,
        before=("yaṅ", "yaṅ-luk"), part="para",
        keeps_out="the copy's own अ — परस्य shuts it out; and "
                  "every sound but the अ — अतः shuts out "
                  "1.1.52's last-sound rule",
        why="उत् परस्यातः — and the अ that stands AFTER the "
            "copy of चर् and फल् becomes उ: **चञ्चूर्यते, "
            "चञ्चूरीति; पम्फुल्यते, पम्फुलीति**. Both words in "
            "the sūtra are tested — **परस्य इति किम्? "
            "अभ्यासस्य मा भूत्। अतः इति किम्? अलोऽन्त्यस्य मा "
            "भूत्** — and the तपर is there for a third reason: "
            "**चञ्चूर्ति, पम्फुलीति इत्यत्र लघूपधगुणनिवृत्त्य"
            "र्थम्**, to keep the light-penult guṇa off"),
    Abhyasa(
        "7.4.89", does="ut", of=CAR_PHAL, before=("ta-ādi",),
        part="para",
        why="ति च — and the same उ before a त-initial affix: "
            "**चरणं चूर्तिः; ब्रह्मणश् चूर्तिः; प्रफुल्तिः; "
            "प्रफुल्ताः सुमनसः**. Here the heading itself is "
            "set aside — **यङ्यङ्लुकोः, अभ्यासस्य इति च "
            "अनुवर्तमानम् अपि वचनसामर्थ्याद् इह न "
            "अभिसम्बध्यते** — for there is no reduplication in "
            "चूर्तिः at all, and a sūtra that could not apply "
            "under its own heading is read without it"),
    Abhyasa(
        "7.4.92", does="ruk-rik-rīk", gana="ṛ-anta",
        before=("yaṅ-luk",), optional=True,
        keeps_out="चाकर्ति from किर् — the तपर makes ऋ short, "
                  "and a root whose ऋ is long is left out",
        why="ऋतश्च — an ऋ-FINAL stem's copy takes रुक्, रिक् or "
            "रीक् in the यङ्लुक् too: **चर्कर्ति, चरिकर्ति, "
            "चरीकर्ति; जर्हर्ति, जरिहर्ति, जरीहर्ति**. 7.4.90 "
            "and 7.4.91 had given the three to a stem with ऋ in "
            "the PENULT; this adds the stem that ends in one, "
            "and the तपर keeps किर् out — **किरतेश् चाकर्ति**. "
            "The vṛtti quotes a verse about how hard the whole "
            "चर्करीत class is to place: **किरतिं चर्करीतान्तं "
            "पचति इत्यत्र यो नयेत्, प्राप्तिज्ञं तम् अहं मन्ये**"),
    Abhyasa(
        "7.4.93", does="sanvat", before=("caṅ-para-ṇi",),
        result=("laghu-anaglopa",),
        why="सन्वल्लघुनि चङ्परेऽनग्लोपे — where a light "
            "root-syllable follows, and the णि has चङ् after "
            "it, and no vowel has been lost, the copy does "
            "whatever it would do BEFORE सन्. Three rules are "
            "borrowed at once and the vṛtti names them: 7.4.79 "
            "सन्यतः gives **अचीकरत्, अपीपचत्**; 7.4.80 ओः "
            "पुयण्ज्यपरे gives **अपीपवत्, अलीलवत्, अजीजवत्**; "
            "and 7.4.81's option carries over as well. This is "
            "the sūtra the causal aorist turns on — every "
            "अचीकरत्-shaped form in the language is made by it "
            "together with the one after"),
    Abhyasa(
        "7.4.94", does="dīrgha", gana="laghu-abhyāsa",
        before=("caṅ-para-ṇi",), result=("laghu-anaglopa",),
        keeps_out="अबिभ्रजत् — the copy is not light; अततक्षत्, "
                  "अररक्षत् — the root syllable is not; अहं "
                  "पपच — no चङ्; अचकमत — the चङ् does not "
                  "follow the णि; अचकथत् — a vowel was lost",
        why="दीर्घो लघोः — and a LIGHT copy then lengthens, "
            "under the same four conditions: **अचीकरत्, "
            "अजीहरत्, अलीलवत्, अपीपचत्**. The ई of every one of "
            "those is made twice over — इ by 7.4.93's borrowed "
            "सन्यतः and long by this — and the vṛtti tests each "
            "condition by taking it away, which is the "
            "cleanest set of counter-examples in the pāda"),
    Abhyasa(
        "7.4.95", does="at", of=SMRADI_SEVEN,
        before=("caṅ-para-ṇi",), result=("laghu-anaglopa",),
        blocks=("7.4.93", "7.4.94"),
        why="अत् स्मृदृत्वरप्रथम्रदस्तॄस्पशाम् — but the copy "
            "of these seven becomes a SHORT अ instead: "
            "**असस्मरत्, अददरत्, अतत्वरत्, अपप्रथत्, अमम्रदत्, "
            "अतस्तरत्, अपस्पशत्**. It displaces both rules "
            "before it, and the vṛtti says so of each in turn: "
            "**सन्वद्भावाद् इत्त्वं प्राप्तम् अनेन बाध्यते**, "
            "and **तपरकरणसामर्थ्याद् अति कृते दीर्घो लघोः "
            "इत्येतद् अपि न भवति** — the तपर would be idle if "
            "the length could come afterwards, so it cannot: "
            "**अददरत्**"),
    Abhyasa(
        "7.4.96", does="at", of=VESTI_CESTI,
        before=("caṅ-para-ṇi",), result=("laghu-anaglopa",),
        optional=True, blocks=("7.4.93",),
        why="विभाषा वेष्टिचेष्ट्योः — and for वेष्ट् and चेष्ट् "
            "the अ comes only OPTIONALLY: **अववेष्टत्, "
            "अविवेष्टत्; अचचेष्टत्, अचिचेष्टत्**. The second of "
            "each pair is what 7.4.93 gives on its own. The "
            "vṛtti notes the order — **अभ्यासह्रस्वत्वे कृते "
            "अत्त्वं पक्षे भवति** — the copy is shortened first "
            "and the अ then replaces what is there"),
    Abhyasa(
        "7.4.97", does="ī", of=("gaṇ",), before=("caṅ-para-ṇi",),
        result=("laghu-anaglopa",), optional=True,
        blocks=("7.4.93",),
        why="ई च गणः — and the copy of गण् becomes ई: "
            "**अजीगणत्**, with the च carrying 7.4.95's अत् down "
            "so that **अजगणत्** stands beside it. With this the "
            "अभ्यासस्य heading closes and so does the adhyāya — "
            "**इति श्रीवामनविरचितायां काशिकायां वृत्तौ "
            "सप्तमाध्यायस्य चतुर्थः पादः**"),
)


def _reaches(row: Abhyasa, root: str, gana: str, before: str,
             part: str, result: str, chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (root in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    # `part` matches BOTH ways. 7.4.87 and 7.4.88 reach the same
    # root before the same affix and differ in nothing but which
    # piece they touch — the copy or what follows it — so a row
    # that names no piece must not answer a question about one.
    if row.part != part:
        return False
    if row.result and result not in row.result:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Abhyasa, root: str, gana: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, and a
    named root outweighs a shape.

    7.4.63 and 7.4.64 are why the refusal has to weigh more:
    both take 7.4.62's palatal away from a single root, and
    both would otherwise be tied with the rule they refuse.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of and root in row.of)
        + 5 * bool(row.result)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
        + 1 * bool(row.part)
    )


@dataclass(frozen=True)
class Copied:
    """What the run answers about the reduplicated copy."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    nipatana: bool = False
    refuses: bool = False
    blocked_by: Tuple[str, ...] = ()


def in_the_copy(root: str = "", *, gana: str = "",
                before: str = "", part: str = "",
                result: str = "", chandasi: bool = False) -> Copied:
    """
    7.4.58–97 — what happens to the reduplicated copy.

    Nothing answers by default. A copy that none of these rules
    reaches goes into the form with whatever 7.4.59 and 7.4.60
    left of it.
    """
    matched = [
        row for row in ABHYASA_TABLE
        if _reaches(row, root, gana, before, part, result, chandasi)
    ]
    if not matched:
        return Copied(
            "", "", "No rule of 7.4.58-97 is reached, so the copy "
                    "stands as 7.4.59 and 7.4.60 left it")
    row = max(matched, key=lambda one: _how_specific(one, root, gana))
    return Copied(row.does, row.sutra, row.why,
                  optional=row.optional, nipatana=row.nipatana,
                  refuses=row.refuses, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Abhyasa, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ABHYASA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Abhyasa", "ABHYASA_TABLE", "ABHYASA_RUN", "ADHIKARA_TO",
    "CODIFIED_APART", "ATRA", "NIPATANA_EIGHTEEN",
    "NIJADI_THREE", "BHRNADI_THREE", "ARTI_PIPARTI",
    "SRAVATI_SIX", "VANCU_EIGHT", "JAPADI_SIX", "CAR_PHAL",
    "SMRADI_SEVEN", "VESTI_CESTI",
    "Copied", "in_the_copy", "provisions_for",
]
