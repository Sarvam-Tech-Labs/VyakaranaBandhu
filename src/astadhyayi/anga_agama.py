# -*- coding: utf-8 -*-
"""
६.४.७१–९५ — the augment अट्, and the semivowel for a final vowel.

Two blocks under 6.4.1's अङ्गस्य.

**The augment that makes a past tense.** 6.4.71 puts an अट् before
the stem in the लुङ्, लङ् and लृङ् and says it is उदात्त —
अकार्षीत्, अकरोत्, अकरिष्यत् — and 6.4.72 makes it आट् for a
vowel-initial stem: ऐक्षिष्ट, औब्जीत्. Then 6.4.74 takes both away
after मा, and 6.4.75 puts them back VARIOUSLY in the Veda, with or
without मा.

**And the semivowel.** 6.4.77's इयङ् and उवङ् — codified apart, in
`anga.iyan_uvan`, because it has to ask 1.1.4 whether the
strengthening was stopped — and then 6.4.78 to 6.4.87 work through
where the plain यण् goes instead: निन्युः, खलप्वौ, जुह्वति,
स्त्रियौ.

**AND ONE SŪTRA'S EXISTENCE TEACHES SOMETHING ABOUT ANOTHER
SECTION ENTIRELY.** 6.4.87 names हु and श्नु, and **इदम् एव
हुश्नुग्रहणं ज्ञापकं भाषायाम् अपि यङ्लुग् अस्तीति** — if the
यङ्लुक् were Vedic only, योयुवति and रोरुवति would not have needed
keeping out, and naming the two shows it is not.

**WHAT THIS MODULE DOES NOT DO.** It reports which augment or
substitute the rule gives, and which rule. 6.4.77 itself is
answered by `anga.iyan_uvan`, which builds the form; this table
records the run around it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where these stand, from the augment run to the shortening
#: before णि.
AGAMA_RUN: Tuple[str, str] = ("6.4.71", "6.4.95")

#: The one sūtra of the run codified apart, because it has to ask
#: 1.1.4 whether the strengthening was stopped before it can act.
CODIFIED_APART: Tuple[str, ...] = ("6.4.77",)

#: The three लकारs 6.4.71 names.
PAST_LAKARAS: Tuple[str, ...] = ("luṅ", "laṅ", "lṛṅ")

#: What 6.4.85 keeps out of the यण्, and 6.4.86 then lets in for
#: the Veda both ways.
BHU_SUDHI: Tuple[str, ...] = ("bhū", "sudhī")

#: 6.4.92's class — **घटादयो मितः** — whose penult shortens
#: before णि.
MIT_ROOTS: Tuple[str, ...] = (
    "ghaṭ", "vyath", "jan", "raj", "śam", "jñap")


@dataclass(frozen=True)
class Agama:
    """One rule of 6.4.71–95: an augment or a substitute."""

    sutra: str
    #: aṭ, āṭ, re, iyaṅ, yaṇ, vuk, ūt, hrasva, dīrgha.
    does: str = ""
    #: The stems the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of stem instead.
    gana: str = ""
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    #: What part of the stem is affected.
    part: str = ""
    #: The further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    bahulam: bool = False
    chandasi: bool = False
    #: True where the augment is laid down as उदात्त as well.
    udatta: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


AGAMA_TABLE: Tuple[Agama, ...] = (
    Agama(
        "6.4.71", does="aṭ", before=PAST_LAKARAS, udatta=True,
        why="लुङ्लङ्लृङ्क्ष्वडुदात्तः — before the लुङ्, the लङ् "
            "and the लृङ् the stem takes the augment अट्, and the "
            "augment is उदात्त: **अकार्षीत्, अहार्षीत्** (लुङ्); "
            "**अकरोत्, अहरत्** (लङ्); **अकरिष्यत्, अहरिष्यत्** "
            "(लृङ्). The augment that makes a Sanskrit past tense "
            "look like one, and the accent is part of the rule "
            "rather than a consequence of it"),
    Agama(
        "6.4.72", does="āṭ", gana="ac-ādi", before=PAST_LAKARAS,
        udatta=True, blocks=("6.4.71",),
        why="आडजादीनाम् — and a VOWEL-INITIAL stem takes आट् "
            "instead, also उदात्त: **ऐक्षिष्ट, ऐहिष्ट, औब्जीत्, "
            "औम्भीत्; ऐक्षत, ऐहत; ऐक्षिष्यत, औब्जिष्यत्**.\\n\\n"
            "**AND ONE SET OF FORMS NEEDS AN ORDER ARGUMENT.** "
            "**इह ऐज्यत औप्यत औह्यतेति लङि कृते लावस्थायाम् "
            "अडागमाद् अन्तरङ्गत्वाद् लादेशः क्रियते। तत्र कृते "
            "विकरणो नित्यत्वाद् अडागमं बाधते** — the ending is "
            "substituted first, being inner, and the class-marker "
            "then beats the augment by being compulsory"),
    Agama(
        "6.4.73", does="āṭ", chandasi=True,
        why="छन्दस्यपि दृश्यते — and in the Veda the आट् is SEEN "
            "where no rule puts it: **यत्र हि विहितस् ततोऽन्यत्रापि "
            "दृश्यते। आडजादीनाम् इत्युक्तम् अनजादीनाम् अपि "
            "दृश्यते** — 6.4.72 gave it to vowel-initial stems and "
            "the Veda has it on others: **सुरुचो वेन आवः; आनक्; "
            "आयुनक्**"),
    Agama(
        "6.4.74", refuses=True, before=PAST_LAKARAS,
        result=("māṅ-yoga",), blocks=("6.4.71", "6.4.72"),
        why="न माङ्योगे — but with मा neither augment: **मा भवान् "
            "कार्षीत्, मा भवान् हार्षीत्; मा स्म करोत्, मा स्म "
            "हरत्; मा भवानीहिष्ट, मा भवानीक्षिष्ट; मा स्म "
            "भवानीहत** — the prohibitive, and the one place where "
            "a Sanskrit past-tense stem carries no augment at all"),
    Agama(
        "6.4.75", does="aṭ", before=PAST_LAKARAS, chandasi=True,
        bahulam=True, blocks=("6.4.74",),
        why="बहुलं छन्दस्यमाङ्योगेऽपि — in the Veda both augments "
            "come and go VARIOUSLY, with मा and without it: "
            "without — **जनिष्ठा उग्रः; काममूनयीः; काममर्दयीत्** "
            "(and the augment absent); with — **मा वः क्षेत्रे "
            "परबीजान्यवाप्सुः; मा अभित्थाः; मा आवः** (and the "
            "augment there). So 6.4.74's refusal is lifted and "
            "6.4.71's grant is suspended, both in the same sūtra "
            "and both **बहुलम्**"),
    Agama(
        "6.4.76", does="re", of=("ira",), chandasi=True,
        bahulam=True,
        keeps_out="चक्रिरे — **अत्र रेशब्दस्य सेटां धातूनाम् इटि "
                  "कृते पुना रेभावः क्रियते**",
        why="इरयो रे — इर becomes रे in the Veda, variously: "
            "**गर्भं प्रथमं दध्र आपः; याश्च परिददृश्रे**.\\n\\n"
            "**AND THE SUBSTITUTION IS NOT SEEN BY THE RULE THAT "
            "FOLLOWS IT.** **धाञो रेभावस्यासिद्धत्वाद् आतो लोपः "
            "भवति** — 6.4.22's असिद्धवत् hides the रे from 6.4.64, "
            "so the आ of धा is still there to be dropped"),
    Agama(
        "6.4.78", does="iyaṅ-uvaṅ", part="abhyāsa", before=("ac",),
        excludes=("savarṇa",),
        keeps_out="ईषतुः, ईषुः, ऊषतुः, ऊषुः — the vowel that "
                  "follows is of the same class; इयाज, उवाप — "
                  "**अचीत्येव**",
        why="अभ्यासस्यासवर्णे — the REDUPLICATED syllable's final "
            "इ or उ becomes इयङ् or उवङ् before a vowel NOT of "
            "its own class: **इयेष, उवोष, इयर्ति**. The same pair "
            "of substitutes 6.4.77 gives the stem, now given to "
            "the copy of it"),
    Agama(
        "6.4.79", does="iyaṅ", of=("strī",), before=("ac",),
        why="स्त्रियाः — स्त्री takes इयङ् before a vowel affix: "
            "**स्त्री, स्त्रियौ, स्त्रियः**. And **स्त्रीणाम् "
            "इत्यत्र परत्वाद् नुडागमः** — the नुट् wins there by "
            "being later. Stated apart for the next rule's sake: "
            "**पृथग्योगकरणम् उत्तरार्थम्**"),
    Agama(
        "6.4.80", does="iyaṅ", of=("strī",), before=("am", "śas"),
        optional=True, blocks=("6.4.79",),
        why="वाऽंशसोः — and before अम् and शस्, optionally: "
            "**स्त्रीं पश्य / स्त्रियं पश्य; स्त्रीः पश्य / "
            "स्त्रियः पश्य**. This is what 6.4.79 was split off "
            "for"),
    Agama(
        "6.4.81", does="yaṇ", of=("iṇ",), before=("ac",),
        blocks=("6.4.77",),
        keeps_out="अयनम्, आयकः — the strengthening wins there by "
                  "being later",
        why="इणो यण् — इण् takes a plain यण् before a vowel: "
            "**यन्ति, यन्तु, आयन्**.\\n\\n"
            "**AND IT IS AN अपवाद THAT IS ITSELF OVERRULED.** "
            "**इयङादेशापवादोऽयम्। मध्येऽपवादाः पूर्वान् विधीन् "
            "बाधन्ते इति गुणवृद्धिभ्यां परत्वाद् अयं बाध्यते** — "
            "an exception standing in the middle displaces the "
            "rules BEFORE it, so this beats 6.4.77 and loses to "
            "the strengthening that comes after"),
    Agama(
        "6.4.82", does="yaṇ", gana="i-anta-anekāc", before=("ac",),
        excludes=("saṃyoga-pūrva",),
        keeps_out="the one-vowelled stems, and any इ with a "
                  "cluster of the ROOT before it",
        why="एरनेकाचोऽसंयोगपूर्वस्य — an इ-final stem of MORE THAN "
            "ONE VOWEL, with no cluster of the root before the इ, "
            "takes यण् before a vowel: **निन्यतुः, निन्युः; "
            "उन्न्यौ, उन्न्यः; ग्रामण्यौ, ग्रामण्यः**.\\n\\n"
            "**AND WHOSE CLUSTER IS MEANT IS SAID IN SO MANY "
            "WORDS.** **धातोरिति वर्तते, तेन संयोगो विशेष्यते। "
            "धातोरवयवः संयोगः पूर्वो यस्माद् इवर्णाद् न भवति** — "
            "the cluster has to belong to the ROOT, and "
            "**असंयोगपूर्वग्रहणम् इवर्णविशेषणं यथा स्याद्, "
            "अङ्गविशेषणं मा भूदिति** — it qualifies the इ and not "
            "the stem"),
    Agama(
        "6.4.83", does="yaṇ", gana="u-anta-anekāc", before=("sup",),
        excludes=("saṃyoga-pūrva",),
        keeps_out="लुलुवतुः, लुलुवुः — no सुप्; लुवौ, लुवः — one "
                  "vowel only; कटप्रुवौ, कटप्रुवः — a cluster of "
                  "the root before the उ",
        why="ओः सुपि — and a उ-final stem of more than one vowel, "
            "with no cluster of the root before the उ, takes यण् "
            "before a vowel-initial सुप्: **खलप्वौ, खलप्वः; "
            "शतस्वौ, शतस्वः; सकृल्ल्वौ, सकृल्ल्वः**. The condition "
            "is narrower than 6.4.82's — a सुप् and not any vowel "
            "affix — and the vṛtti adds **गतिकारकाभ्याम् "
            "अन्यपूर्वस्य** as a further limit"),
    Agama(
        "6.4.84", does="yaṇ", of=("varṣābhū",), before=("sup",),
        why="वर्षाभ्वश्च — and वर्षाभू before a vowel-initial "
            "सुप्: **वर्षाभ्वौ, वर्षाभ्वः**. Two vārttikas add "
            "more: **पुनर्भ्वश्चेति वक्तव्यम् — पुनर्भ्वौ, "
            "पुनर्भ्वः**, and **कारापूर्वस्यापीष्यते — काराभ्वौ, "
            "काराभ्वः**"),
    Agama(
        "6.4.85", refuses=True, of=BHU_SUDHI, before=("sup",),
        blocks=("6.4.83", "6.4.84"),
        why="न भूसुधियोः — but भू and सुधी do not take it: "
            "**प्रतिभुवौ, प्रतिभुवः; सुधियौ, सुधियः**. Two stems "
            "named against the two rules just before, and the "
            "second of those two had just named a compound of भू "
            "itself. **सुपि** is still running from 6.4.83, which "
            "is why the refusal does not touch भू's वुक् at "
            "6.4.88"),
    Agama(
        "6.4.86", does="yaṇ", of=BHU_SUDHI, before=("sup",),
        chandasi=True, optional=True, blocks=("6.4.85",),
        why="छन्दस्युभयथा — and in the Veda both are seen: "
            "**वनेषु चित्रं विभ्वं विशे** beside **विभुवं विशे**; "
            "**सुध्यो नव्यमग्ने** beside **सुधियो नव्यमग्ने**. "
            "The same shape 6.4.5 had — a refusal lifted for the "
            "Veda and lifted both ways at once"),
    Agama(
        "6.4.87", does="yaṇ", of=("hu",), gana="śnu-anta",
        before=("sārvadhātuka",), excludes=("saṃyoga-pūrva",),
        keeps_out="योयुवति, रोरुवति — a यङ्लुक् and neither हु nor "
                  "श्नु",
        why="हुश्नुवोः सार्वधातुके — हु and a श्नु-ending stem of "
            "more than one vowel, with no cluster before, take "
            "यण् before a vowel-initial सार्वधातुक: **जुह्वति, "
            "जुह्वतु, जुह्वत्; सुन्वन्ति, सुन्वन्तु, असुन्वन्**.\\n\\n"
            "**AND NAMING THE TWO TEACHES SOMETHING ABOUT ANOTHER "
            "SECTION ENTIRELY.** **इदम् एव हुश्नुग्रहणं ज्ञापकं "
            "भाषायाम् अपि यङ्लुग् अस्तीति** — if the यङ्लुक् were "
            "Vedic only, योयुवति and रोरुवति would never arise "
            "outside the Veda and there would have been nothing "
            "to keep out. The two names show the यङ्लुक् is "
            "ordinary Sanskrit"),
    Agama(
        "6.4.88", does="vuk", of=("bhū",), before=("luṅ", "liṭ"),
        why="भुवो वुग्लुङ्लिटोः — भू takes the augment वुक् before "
            "a vowel in the लुङ् and the लिट्: **अभूवन्, अभूवम्** "
            "for the लुङ्; **बभूव, बभूवतुः, बभूवुः** for the लिट्. "
            "The rule that gives बभूव its second व्"),
    Agama(
        "6.4.89", does="ūt", of=("gūh",), part="upadhā",
        before=("ac",),
        keeps_out="निजुगुहतुः, निजुगुहुः — **गोह इति विकृतग्रहणं "
                  "विषयार्थम्। यत्रास्यैतद्रूपं तत्रैव यथा "
                  "स्यात्**",
        why="ऊदुपधाया गोहः — गूह् lengthens its penult to ऊ before "
            "a vowel affix: **निगूहयति, निगूहकः, साधुनिगूही, "
            "निगूहंनिगूहम्, निगूहन्ति**.\\n\\n"
            "**AND उपधायाः IS SAID TO STOP A PARIBHĀṢĀ.** "
            "**उपधाया इति किम्? अलोऽन्त्यस्य मा भूत्** — without "
            "it 1.1.52 would have put the substitute at the end. "
            "And the root is named in its ALTERED shape on "
            "purpose: **गोह इति विकृतग्रहणं विषयार्थम्**"),
    Agama(
        "6.4.90", does="ūt", of=("doṣ",), part="upadhā",
        before=("ṇi",),
        keeps_out="दोषो वर्तते — no णि",
        why="दोषो णौ — दोष् lengthens its penult to ऊ before णि: "
            "**दूषयति, दूषयतः, दूषयन्ति**. Named in its altered "
            "shape again, and the vṛtti says why: **विकृतग्रहणं "
            "प्रक्रमाभेदार्थम्। पूर्वत्र हि गोह इत्युक्तम्** — to "
            "keep the two sūtras' manner of naming the same"),
    Agama(
        "6.4.91", does="ūt", of=("doṣ",), part="upadhā",
        before=("ṇi",), result=("cittavirāga",), optional=True,
        blocks=("6.4.90",),
        why="वा चित्तविरागे — but where a change of MIND is meant, "
            "optionally: **चित्तं दूषयति / चित्तं दोषयति; "
            "प्रज्ञां दूषयति / प्रज्ञां दोषयति**"),
    Agama(
        "6.4.92", does="hrasva", gana="mit", part="upadhā",
        before=("ṇi",),
        why="मितां ह्रस्वः — the मित् roots, **घटादयो मितः**, "
            "shorten their penult before णि: **घटयति, व्यथयति, "
            "जनयति, रजयति, शमयति, ज्ञपयति**.\\n\\n"
            "**AND SOME READ AN OPTION INTO IT.** **केचिद् अत्र "
            "वेत्यनुवर्तयन्ति। सा च व्यवस्थितविभाषा। तेन "
            "उत्क्रामयति, संक्रामयतीत्येवमादि सिद्धं भवति** — "
            "carrying वा down from 6.4.91, and settled rather "
            "than free, so that the क्रम् forms come out"),
    Agama(
        "6.4.93", does="dīrgha", gana="mit", part="upadhā",
        before=("ciṇ", "ṇamul"), optional=True, blocks=("6.4.92",),
        why="चिण्णमुलोर्दीर्घोऽन्यतरस्याम् — and before णि with "
            "चिण् or णमुल् after it, the penult is optionally "
            "LONG instead: **अशमि / अशामि; अतमि / अतामि; "
            "शमंशमम् / शामंशामम्; तमंतमम् / तामंतामम्**.\\n\\n"
            "**AND SAYING दीर्घ RATHER THAN MAKING 6.4.92 OPTIONAL "
            "IS DELIBERATE.** **दीर्घग्रहणं किम्, न ह्रस्वविकल्प "
            "एव विधीयते? नैवं शक्यम्, शमयन्तं प्रयुङ्क्त इति "
            "द्वितीये णिचि ह्रस्वविकल्पो न स्यात्, णिलोपस्य "
            "स्थानिवद्भावात्** — with a second णि the shortening "
            "is compulsory, so an option on it would not have "
            "reached these forms"),
    Agama(
        "6.4.94", does="hrasva", part="upadhā", before=("khac",),
        why="खचि ह्रस्वः — and before णि with खच् after it, the "
            "penult shortens, मित् or not: **द्विषंतपः, परंतपः, "
            "पुरंदरः** — one who scorches his foes, one who "
            "breaks forts"),
    Agama(
        "6.4.95", does="hrasva", of=("hlād",), part="upadhā",
        before=("niṣṭhā",),
        keeps_out="प्रह्लादयति — not a निष्ठा",
        why="ह्लादो निष्ठायाम् — ह्लाद् shortens its penult before "
            "a निष्ठा: **प्रह्लन्नः, प्रह्लन्नवान्**.\\n\\n"
            "**AND IT IS SPLIT FROM THE RULE BEFORE FOR ONE MORE "
            "FORM.** **ह्लाद इति योगविभागः क्रियते, क्तिन्यपि यथा "
            "स्यात् प्रह्लत्तिरिति** — dividing the sūtra lets the "
            "shortening reach a क्तिन् as well as a निष्ठा"),
)


def _reaches(row: Agama, stem: str, gana: str, before: str,
             part: str, result: str, chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.part and part and part != row.part:
        return False
    if row.result and result not in row.result:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.excludes and (stem in row.excludes
                         or gana in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Agama, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.does and not row.refuses


def _how_specific(row: Agama, stem: str, gana: str) -> int:
    """
    A rule that undoes a refusal beats it, a refusal beats what it
    refuses, and a named stem beats a named class.

    6.4.85, 6.4.86 need the first: the refusal names भू and सुधी
    and the Vedic option names the same two, so nothing but
    `blocks` can order them.
    """
    return (
        12 * (0 if row.refuses else len(row.blocks))
        + 10 * bool(row.refuses)
        + 6 * bool(row.of and stem in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.result)
        + 2 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Given:
    """What the run answers: an augment or a substitute."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    bahulam: bool = False
    udatta: bool = False
    blocked_by: Tuple[str, ...] = ()


def augment_or_yan(stem: str = "", *, gana: str = "",
                   before: str = "", part: str = "",
                   result: str = "", chandasi: bool = False,
                   wants: str = "") -> Given:
    """
    6.4.71–95 — the augment before a past tense, and the semivowel
    for a final vowel.

    Nothing answers by default: where no rule is reached the stem
    takes no augment and keeps its vowel.

    6.4.77 is not in this table. It is answered by
    `anga.iyan_uvan`, which builds the form rather than naming the
    operation, because it has to ask 1.1.4 whether the
    strengthening that would displace it was stopped.
    """
    matched = [
        row for row in AGAMA_TABLE
        if _reaches(row, stem, gana, before, part, result, chandasi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Given(
            "", "", "No rule of 6.4.71–95 is reached, so the stem "
                    "takes no augment and keeps its vowel")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Given("" if row.refuses else row.does, row.sutra,
                 row.why, optional=row.optional,
                 bahulam=row.bahulam, udatta=row.udatta,
                 blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Agama, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in AGAMA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Agama", "AGAMA_TABLE", "AGAMA_RUN", "CODIFIED_APART",
    "PAST_LAKARAS", "BHU_SUDHI", "MIT_ROOTS", "Given",
    "augment_or_yan", "provisions_for",
]
