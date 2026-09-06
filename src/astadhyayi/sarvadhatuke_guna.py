# -*- coding: utf-8 -*-
"""
७.३.८५–१०० — guṇa and vṛddhi before a सार्वधातुक, and the ईट्.

Sixteen sūtras following on 7.3.84's guṇa. 7.3.86
पुगन्तलघूपधस्य च widens it to a stem with a light penult, which
is why भेदनम् and छेत्ता have their ए; 7.3.87 and 7.3.88 refuse
it to a reduplicated stem and to भू and सू; 7.3.89 gives vṛddhi
instead where a विकरण has been elided — यौति, स्तौति; and from
7.3.92 the rest of the run is augments: इम् for तृणह्, ईट् for
ब्रू, ईट् again for अस् and the सिच्, and finally अट् for अद्.

**AND TWO OF THEM NAME TEACHERS TO SETTLE AN AUGMENT.** 7.3.99
gives the रुदादि roots an अट् in Gārgya's and Gālava's view —
अरोदत् beside अरोदीत् — and the vṛtti says the naming is not to
mark a dissent but to honour them, **गार्ग्यगालवयोर्ग्रहणं
पूजार्थम्**. 7.3.100 then gives अद् the same augment in EVERY
teacher's view: आदत्.

**AND ONE REFUSAL IS PROVED FROM A RULE A PĀDA AWAY.** Asked why
बोभवीति keeps its guṇa when भू is refused it before a तिङ्, the
vṛtti answers **ज्ञापकात्** — 7.4.65 lays down बोभूतु expressly
without guṇa, and it would not need to if the refusal reached
there anyway.

**WHAT THIS MODULE DOES NOT DO.** It says whether the vowel is
strengthened and what augment comes. The guṇa itself is 1.1.2's
and 7.3.84's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
GUNA_RUN: Tuple[str, str] = ("7.3.85", "7.3.100")

#: Where the run stops being about strengthening.
AUGMENTS_FROM: str = "7.3.92"

#: 7.3.95's five, which take an optional ईट्.
TU_RU_FIVE: Tuple[str, ...] = ("tu", "ru", "stu", "śam", "am")

#: 7.3.98–99's five, which are 7.2.76's own list read again —
#: one set of roots, two augments, two pādas apart. Asked for
#: rather than written out twice.
from src.astadhyayi.it_agama import RUDADI_FIVE  # noqa: E402

#: The two teachers 7.3.99 names, and what the vṛtti says the
#: naming is for.
GARGYA_GALAVA: str = "gārgya-gālavayoḥ matena"
PUJARTHAM: str = "गार्ग्यगालवयोर्ग्रहणं पूजार्थम्"


@dataclass(frozen=True)
class Guna:
    """One rule of 7.3.85–100: strengthening, or an augment."""

    sutra: str
    #: `guṇa`, `vṛddhi`, or the augment's name — "" if refused.
    does: str = ""
    #: The roots named outright.
    of: Tuple[str, ...] = ()
    #: The stem class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow.
    not_before: Tuple[str, ...] = ()
    #: A further condition on the environment.
    result: Tuple[str, ...] = ()
    #: The named teachers' view this rule records.
    view: str = ""
    #: True where the rule supplies an आगम.
    augment: bool = False
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    bahulam: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


GUNA_TABLE: Tuple[Guna, ...] = (
    Guna(
        "7.3.85", does="guṇa", of=("jāgṛ",),
        not_before=("ci", "ciṇ", "ṇal", "ṅit"),
        blocks=("7.2.116",),
        keeps_out="जागृविः — the क्विन् of the Uṇādi, which is "
                  "ङित्; अजागरि — चिण्; जजागार — णल्",
        why="जाग्रोऽविचिण्णल्ङित्सु — जागृ takes guṇa except "
            "before वि, चिण्, णल् and a ङित्: **जागरयति, "
            "जागरकः, साधुजागरी, जागरो वर्तते; जागरितः, "
            "जागरितवान्**.\\n\\n"
            "**AND THE GUṆA IS STATED SO THAT THE vṛddhi SHALL "
            "NOT COME.** **वृद्धिविषये प्रतिषेधविषये च यथा "
            "स्याद् इति जागर्तेर् अयं गुण आरभ्यते** — once the "
            "guṇa is in, 7.2.116's vṛddhi has no अ in the penult "
            "to work on. **यदि हि स्याद् अनर्थक एव गुणः स्यात्** "
            "— and the exception for चिण् and णल् would be idle "
            "besides"),
    Guna(
        "7.3.86", does="guṇa", gana="pug-anta-laghu-upadha",
        before=("sārvadhātuka", "ārdhadhātuka"),
        why="पुगन्तलघूपधस्य च — a stem ending in पुक् and one "
            "with a LIGHT penult take guṇa before a सार्वधातुक "
            "or an आर्धधातुक: **व्लेपयति, ह्रेपयति, क्नोपयति** "
            "for the first; **भेदनम्, छेदनम्, भेत्ता, छेत्ता** "
            "for the second. This is why so many verbal nouns "
            "have an ए where the root has an इ.\\n\\n"
            "**AND A VERSE ASKS HOW भेत्ता IS POSSIBLE AT ALL.** "
            "**संयोगे गुरुसंज्ञायां गुणो भेत्तुर् न सिध्यति** — "
            "with the cluster of the affix after it the penult "
            "is heavy and not light. The answer is read out of "
            "3.2.140 and 1.2.10's marking the क्नु and सन् as "
            "कित्, which would be pointless unless the guṇa "
            "reached across a cluster"),
    Guna(
        "7.3.87", refuses=True, gana="abhyasta-laghu-upadha",
        before=("ac-ādi-pit-sārvadhātuka",), blocks=("7.3.86",),
        keeps_out="वेदानि — no reduplication; नेनेक्ति — the "
                  "affix does not begin with a vowel; निनेज — "
                  "an आर्धधातुक; जुहवानि — the penult is not "
                  "light",
        why="नाभ्यस्तस्याचि पिति सार्वधातुके — but a REDUPLICATED "
            "stem with a light penult does not take it before a "
            "vowel-initial पित् सार्वधातुक: **नेनिजानि, "
            "वेविजानि, परिवेविषाणि; अनेनिजम्, अवेविजम्**. A "
            "vārttika lets the Veda off — **बहुलं छन्दसीति "
            "वक्तव्यम्**, which is how जुजोषत् comes out"),
    Guna(
        "7.3.88", refuses=True, of=("bhū", "sū"), before=("tiṅ",),
        blocks=("7.3.84",),
        keeps_out="भवति — a तिङ् but not a सार्वधातुक one in the "
                  "sense wanted; व्यतिभविषीष्ट — an आर्धधातुक",
        why="भूसुवोस्तिङि — भू and सू do not take guṇa before a "
            "तिङ्: **अभूत्, अभूः, अभूवम्; सुवै, सुवावहै, "
            "सुवामहै**. The सू meant is the one whose विकरण is "
            "elided, the other being kept from the guṇa by its "
            "own ङित् विकरण anyway.\\n\\n"
            "**AND WHY बोभवीति KEEPS ITS GUṆA IS ANSWERED FROM A "
            "RULE A PĀDA AWAY.** **ज्ञापकात्, यद् अयं बोभूतु इति "
            "गुणाभावार्थं निपातनं करोति** — 7.4.65 lays down "
            "बोभूतु expressly without guṇa, and would not need "
            "to if this refusal reached there"),
    Guna(
        "7.3.89", does="vṛddhi", gana="u-anta",
        before=("hal-ādi-pit-sārvadhātuka",), result=("luk",),
        keeps_out="एति, एषि — not उ-final; सुनोति — no लुक्; "
                  "यवानि, रवाणि — the affix begins with a vowel; "
                  "युतः, रुतः — not पित्",
        why="उतो वृद्धिर्लुकि हलि — an उ-final stem takes VṚDDHI "
            "before a consonant-initial पित् सार्वधातुक where "
            "the विकरण has been elided: **यौति, यौषि, यौमि; "
            "नौति; स्तौति, स्तौषि, स्तौमि**. In अपि स्तुयाद् "
            "राजानम् the ending is ङित् and so not पित्, and no "
            "vṛddhi comes"),
    Guna(
        "7.3.90", does="vṛddhi", of=("ūrṇu",),
        before=("hal-ādi-pit-sārvadhātuka",), optional=True,
        blocks=("7.3.89",),
        keeps_out="प्रोर्णवानि — a vowel-initial affix",
        why="ऊर्णोतेर्विभाषा — and ऊर्णु takes it OPTIONALLY: "
            "**प्रोर्णौति, प्रोर्णोति; प्रोर्णौषि, प्रोर्णोषि; "
            "प्रोर्णौमि, प्रोर्णोमि**"),
    Guna(
        "7.3.91", does="guṇa", of=("ūrṇu",),
        before=("apṛkta-hal-pit-sārvadhātuka",),
        blocks=("7.3.90",),
        why="गुणोऽपृक्ते — but where that ending is a single "
            "sound the change is guṇa and not vṛddhi: "
            "**प्रौर्णोत्, प्रौर्णोः**.\\n\\n"
            "**AND THE WORD अपृक्त IS ITSELF A ज्ञापक.** हलि was "
            "already running, so naming the single-sound ending "
            "adds nothing unless a paribhāṣā is being taught: "
            "**तेनैव ज्ञाप्यते भवत्येषा परिभाषा — यस्मिन् "
            "विधिस्तदादावल्ग्रहणे इति**"),
    Guna(
        "7.3.92", does="im", of=("tṛṇah",),
        before=("hal-ādi-pit-sārvadhātuka",), augment=True,
        keeps_out="तृणहानि — a vowel-initial affix; तृण्ढः — "
                  "not पित्",
        why="तृणह इम् — तृणह् takes the augment इम् before a "
            "consonant-initial पित् सार्वधातुक: **तृणेढि, "
            "तृणेक्षि, तृणेह्मि, अतृणेट्**. The तृणह् meant is "
            "the one that HAS its श्नम् — **आगतश्नम्को "
            "गृह्यते, श्नमि कृत इमागमो यथा स्यात्** — so the "
            "two augments go in one after the other"),
    Guna(
        "7.3.93", does="īṭ", of=("brū",),
        before=("hal-ādi-pit-sārvadhātuka",), augment=True,
        keeps_out="ब्रवाणि — a vowel-initial affix; ब्रूतः — "
                  "not पित्",
        why="ब्रुव ईट् — ब्रू takes ईट् before a "
            "consonant-initial पित् सार्वधातुक: **ब्रवीति, "
            "ब्रवीषि, ब्रवीमि, अब्रवीत्**"),
    Guna(
        "7.3.94", does="īṭ", gana="yaṅ-anta",
        before=("hal-ādi-pit-sārvadhātuka",), augment=True,
        optional=True,
        keeps_out="वर्वर्ति, चर्करिति चक्रम् — the यङ् has been "
                  "elided, and the rule wants it present",
        why="यङो वा — and after यङ् it is optional: "
            "**शाकुनिको लालपीति; दुन्दुभिर्वावदीति; त्रिधा बद्धो "
            "वृषभो रोरवीति**"),
    Guna(
        "7.3.95", does="īṭ", of=TU_RU_FIVE,
        before=("hal-ādi-sārvadhātuka",), augment=True,
        optional=True,
        why="तुरुस्तुशम्यमः सार्वधातुके — five roots take it "
            "optionally: **उत्तौति, उत्तवीति; उपरौति, "
            "उपरवीति; उपस्तौति, उपस्तवीति; शाम्यध्वम्, "
            "शमीध्वम्; अभ्यमति, अभ्यमीति**. The तु is a root "
            "known only from this sūtra — **तु इति सौत्रोऽयं "
            "धातुः** — and the Āpiśalas read the whole rule as "
            "Vedic"),
    Guna(
        "7.3.96", does="īṭ", of=("as", "sic"),
        before=("apṛkta-sārvadhātuka",), augment=True,
        keeps_out="अस्ति, अकार्षम् — the ending is more than one "
                  "sound",
        why="अस्तिसिचोऽपृक्ते — अस् and a सिच्-final stem take "
            "ईट् before a single-sound सार्वधातुक: **आसीत्, "
            "आसीः; अकार्षीत्, असावीत्, अलावीत्, अपावीत्**. A "
            "vārttika refuses the ईट् to आह् and भू — "
            "**आहिभुवोर् ईटि प्रतिषेधः** — so आत्थ and अभूत् "
            "stand"),
    Guna(
        "7.3.97", does="īṭ", of=("as", "sic"),
        before=("apṛkta-sārvadhātuka",), augment=True,
        chandasi=True, bahulam=True, blocks=("7.3.96",),
        why="बहुलं छन्दसि — and in the Veda it is बहुलम्: "
            "**आप एवेदं सलिलं सर्वम् आः** for आसीत्; **गोभिर् "
            "अक्षाः; प्रत्यञ्चम् अत्साः** for the सिच्. The "
            "Vedic freedom goes further than the augment — "
            "**छान्दसत्वाद् माङ्योगेऽप्यडागमो भवति**, and the "
            "सिच् loses its इट् besides"),
    Guna(
        "7.3.98", does="īṭ", of=RUDADI_FIVE,
        before=("apṛkta-hal-sārvadhātuka",), augment=True,
        keeps_out="अजागर्भवान् — जागृ is not one of the five; "
                  "रोदिति — the ending is more than one sound",
        why="रुदश्च पञ्चभ्यः — and the five रुदादि roots: "
            "**अरोदीत्, अरोदीः; अस्वपीत्; अश्वसीत्; प्राणीत्; "
            "अजक्षीत्**. The same five 7.2.76 gave an इट् before "
            "a वल्-initial सार्वधातुक — one list, two augments, "
            "two pādas apart"),
    Guna(
        "7.3.99", does="aṭ", of=RUDADI_FIVE,
        before=("apṛkta-sārvadhātuka",), augment=True,
        view=GARGYA_GALAVA, optional=True, blocks=("7.3.98",),
        why="अड्गार्ग्यगालवयोः — and in GĀRGYA's and GĀLAVA's "
            "view they take अट् instead: **अरोदत्, अरोदः; "
            "अस्वपत्; अश्वसत्; प्राणत्; अजक्षत्**.\\n\\n"
            "**AND NAMING THE TWO IS NOT TO MARK A DISSENT.** "
            "**गार्ग्यगालवयोर्ग्रहणं पूजार्थम्** — it is done in "
            "their honour, which is a different thing from the "
            "views recorded at 7.1.74 and 7.2.63, where the "
            "naming makes the rule an option in the language"),
    Guna(
        "7.3.100", does="aṭ", of=("ad",),
        before=("apṛkta-sārvadhātuka",), augment=True,
        view="sarveṣām ācāryāṇām matena", blocks=("7.3.98",),
        keeps_out="अत्ति, अत्सि — the ending is more than one "
                  "sound",
        why="अदः सर्वेषाम् — and अद् takes it in EVERY teacher's "
            "view: **आदत्, आदः**. The contrast with the sūtra "
            "before is the whole content: there two teachers, "
            "here all of them, and the augment the same"),
)


def _reaches(row: Guna, root: str, gana: str, before: str,
             result: str, chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (root in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.not_before and before in row.not_before:
        return False
    if row.result and result not in row.result:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Guna, root: str, gana: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, a named
    root beats a class, and a named environment beats both.

    7.3.98 against 7.3.99 and 7.3.100 is what needs the last:
    all three name the same five roots before the same ending,
    and they differ only in which augment and whose view.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of and root in row.of)
        + 5 * bool(row.gana and gana == row.gana)
        + 4 * bool(row.result)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Strengthened:
    """What the run answers: a strengthening, or an augment."""

    does: str
    sutra: str
    why: str
    view: str = ""
    augment: bool = False
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def before_sarvadhatuka(root: str = "", *, gana: str = "",
                        before: str = "", result: str = "",
                        chandasi: bool = False,
                        wants: str = "") -> Strengthened:
    """
    7.3.85–100 — strengthening before a सार्वधातुक, and the ईट्.

    Nothing answers by default, and the default is not *no guṇa*:
    7.3.84 has already given it to every इक्-final stem, and this
    run is where that is widened, refused and replaced.
    """
    matched = [
        row for row in GUNA_TABLE
        if _reaches(row, root, gana, before, result, chandasi)
        and (not wants or (wants == row.does and not row.refuses))
    ]
    if not matched:
        return Strengthened(
            "", "", "No rule of 7.3.85-100 is reached, so 7.3.84 "
                    "stands as it is")
    row = max(matched, key=lambda one: _how_specific(one, root, gana))
    return Strengthened("" if row.refuses else row.does, row.sutra,
                        row.why, view=row.view,
                        augment=row.augment, optional=row.optional,
                        blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Guna, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in GUNA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Guna", "GUNA_TABLE", "GUNA_RUN", "AUGMENTS_FROM",
    "TU_RU_FIVE", "RUDADI_FIVE", "GARGYA_GALAVA", "PUJARTHAM",
    "Strengthened", "before_sarvadhatuka", "provisions_for",
]
