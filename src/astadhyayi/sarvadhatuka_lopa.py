# -*- coding: utf-8 -*-
"""
६.४.९६–११४ — the losses that make a Sanskrit present tense.

Nineteen rules, and most of them are why the finite verb looks the
way it does. रुन्धः has lost the अ of श्न; लुनते has lost the आ of
श्ना; कुर्वः has lost the उ of उ; पच has lost its हि altogether;
अकारि has lost everything after the चिण्.

**AND THE हि GOES THREE DIFFERENT WAYS IN FIVE SŪTRAS, WHICH
ARE NOT FIVE IN A ROW.** 6.4.101
makes it धि after हु and a झल्; 6.4.102 and 6.4.103 widen that for
the Veda; 6.4.105 drops it after an अ; 6.4.106 drops it after a
उ-affix with no cluster before. जुहुधि, भिन्द्धि, श्रुधी, पच,
चिनु — five shapes of one affix.

**AND ONE PAIR OF RULES IS TOLD APART ONLY BY BEING COMPULSORY.**
6.4.107 drops the उ of a उ-affix OPTIONALLY before व् and म् —
सुन्वः beside सुनुवः — and 6.4.108 makes it compulsory for कृ:
कुर्वः, and no second form. **नित्यं करोतेः**, and the word
नित्यम् is the whole of the difference.

**WHAT THIS MODULE DOES NOT DO.** It reports what is lost or
substituted and by which rule. It does not conjugate: that कुर्वः
then escapes 8.2.77's lengthening by 8.2.79 is another rule's
business, and the note says so rather than the code doing it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where these nineteen stand, closing before 6.4.115's भी.
SARVA_RUN: Tuple[str, str] = ("6.4.96", "6.4.114")

#: The five roots of 6.4.98, whose penult goes before a
#: vowel-initial कित् or ङित् that is not अङ्.
GAMA_FIVE: Tuple[str, ...] = ("gam", "han", "jan", "khan", "ghas")

#: 6.4.102's five, for which the Veda makes हि into धि.
DHI_CHANDASI: Tuple[str, ...] = ("śru", "śṛṇu", "pṝ", "kṛ", "vṛ")

#: The three shapes हि takes across 6.4.101–106 — dhi, lopa, and
#: standing as it is.
HI_SHAPES: Tuple[str, ...] = ("dhi", "lopa")


@dataclass(frozen=True)
class Sarva:
    """One rule of 6.4.96–114: a loss or a substitute."""

    sutra: str
    #: hrasva, lopa, luk, dhi, ut, īt, it.
    does: str = ""
    #: The stems the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of stem. Ordinarily an ALTERNATIVE to `of` —
    #: 6.4.101's हुझल्भ्यः is a dvandva, so हु OR a झल्-final stem
    #: reaches it. Where the two are a conjunction instead, the
    #: class coming down by anuvṛtti and the stem being named in
    #: the sūtra, `and_gana` says so.
    gana: str = ""
    and_gana: bool = False
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    #: What part of the stem is affected.
    part: str = ""
    #: The further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    optional: bool = False
    #: True where the sūtra says नित्यम् against an option just
    #: given.
    nitya: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


SARVA_TABLE: Tuple[Sarva, ...] = (
    Sarva(
        "6.4.96", does="hrasva", of=("chad",), part="upadhā",
        before=("gha",), excludes=("dvi-upasarga",),
        keeps_out="समुपच्छादः — two preverbs, and a vārttika "
                  "widens that to **अद्विप्रभृत्युपसर्गस्य**",
        why="छादेर्घेऽद्व्युपसर्गस्य — छाद् shortens its penult "
            "before घ, if it has no two preverbs: **उरश्छदः, "
            "प्रच्छदः, दन्तच्छदः**.\\n\\n"
            "**AND THE MERE FACT OF THE RULE STOPS TWO OTHER "
            "THINGS.** **णिलोपस्यासिद्धत्वं स्थानिवद्भावो वा "
            "वचनसामर्थ्याद् अत्र न भवतीति ह्रस्वभाविन्युपधा "
            "भवति** — 6.4.22 would have hidden the णि's loss and "
            "1.1.56 would have kept it standing in its place; "
            "either way there would be no vowel to shorten, so "
            "the rule's existence sets both aside"),
    Sarva(
        "6.4.97", does="hrasva", of=("chad",), part="upadhā",
        before=("is", "man", "tran", "kvi"),
        why="इस्मन्त्रन्क्विषु च — and छाद् shortens before four "
            "more: **छदिः** (इस्), **छद्म** (मन्), **छत्त्रम्** "
            "(त्रन्), **धामच्छत्, उपच्छत्** (क्वि)"),
    Sarva(
        "6.4.98", does="lopa", of=GAMA_FIVE, part="upadhā",
        before=("ac",), result=("kṅit",), excludes=("aṅ",),
        keeps_out="गमनम्, हननम् — the affix is neither कित् nor "
                  "ङित्; अगमत् — an अङ्, which the sūtra shuts out",
        why="गमहनजनखनघसां लोपः क्ङित्यनङि — five roots lose the "
            "vowel of their penult before a vowel-initial कित् or "
            "ङित् that is not अङ्: **जग्मतुः, जग्मुः; जघ्नतुः, "
            "जघ्नुः; जज्ञे, जज्ञाते, जज्ञिरे; चख्नतुः, चख्नुः; "
            "जक्षतुः, जक्षुः; अक्षन् पितरोऽमीमदन्त पितरः**"),
    Sarva(
        "6.4.99", does="lopa", of=("tan", "pat"), part="upadhā",
        before=("ac",), result=("kṅit",), chandasi=True,
        keeps_out="वितेनिरे, पेतिम — outside the Veda",
        why="तनिपत्योश्छन्दसि — and तन् and पत् in the Veda: "
            "**वितत्निरे कवयः; शकुना इव पप्तिम**"),
    Sarva(
        "6.4.100", does="lopa", of=("ghas", "bhas"), part="upadhā",
        before=("hal", "ac"), result=("kṅit",), chandasi=True,
        why="घसिभसोर्हलि च — and घस् and भस् in the Veda, before "
            "a CONSONANT-initial कित् or ङित् as well as a "
            "vowel-initial one: **सग्धिश्च मे सपीतिश्च मे; "
            "बब्धां ते हरी धानाः**. The vṛtti walks सग्धि through "
            "three rules — **अदेः क्तिनि बहुलं छन्दसि इति "
            "घस्लादेश उपधाया लोपे च कृते झलो झलि इति सकारलोपः**"),
    Sarva(
        "6.4.101", does="dhi", of=("hu",), gana="jhal-anta",
        before=("hi",), result=("hal-ādi",),
        keeps_out="क्रीणीहि, प्रीणीहि — neither हु nor झल्-final; "
                  "जुहुताम् — no हि; रुदिहि, स्वपिहि — the हि does "
                  "not begin with a consonant there",
        why="हुझल्भ्यो हेर्धिः — after हु and after a झल्-final "
            "stem, a consonant-initial हि becomes धि: **जुहुधि; "
            "भिन्द्धि, छिन्द्धि**.\\n\\n"
            "**AND THE FORMS WITH तातङ् ARE SETTLED BY A "
            "PARIBHĀṢĀ.** **इह जुहुतात्, भिन्तात् त्वम् इति "
            "परत्वात् तातङि कृते सकृद्गतौ विप्रतिषेधे...** — once "
            "the later rule has put the तातङ् in, the conflict is "
            "spent and this rule does not come back"),
    Sarva(
        "6.4.102", does="dhi", of=DHI_CHANDASI, before=("hi",),
        chandasi=True, blocks=("6.4.101",),
        why="श्रुशृणुपॄकृवृभ्यश्छन्दसि — and after five roots in "
            "the Veda, consonant or no: **श्रुधी हवमिन्द्र; गिरः "
            "शृणुधी; पूर्धि; उरु णस्कृधि; अपा वृधि**.\\n\\n"
            "**AND ONE OF THE FIVE TEACHES THAT ANOTHER RULE DOES "
            "NOT REACH IT.** **शृणुधीत्यत्र धिभावविधानसामर्थ्याद् "
            "उतश्च प्रत्ययाद्० न भवति** — 6.4.106 would have "
            "dropped the हि after शृणु altogether, and the mere "
            "fact that this rule gives it a shape shows it does "
            "not"),
    Sarva(
        "6.4.103", does="dhi", before=("hi",), result=("aṅit",),
        chandasi=True,
        keeps_out="हव्यं प्रीणीहि — the हि is ङित् there",
        why="अङितश्च — and where the हि is NOT ङित्, which in the "
            "Veda it may not be: **सोम रारन्धि; अस्मभ्यं तद्धर्यश्व "
            "प्रयन्धि; युयोध्यस्मज्जुहुराणमेनः**. **वा छन्दसि इति "
            "पित्त्वेनास्याङित्त्वम्** — 3.4.88 makes it पित् in "
            "the Veda, and 1.2.4 then does not make it ङित्"),
    Sarva(
        "6.4.104", does="luk", before=("ciṇ",),
        why="चिणो लुक् — the affix after चिण् is dropped "
            "altogether: **अकारि, अहारि, अलावि, अपाचि** — it was "
            "done, it was taken, it was cut, it was cooked. The "
            "whole of the Sanskrit aorist passive third singular "
            "is this one rule.\\n\\n"
            "**AND THE लुक् DOES NOT REACH A तरप् AFTER IT.** "
            "**अकारितराम् अहारितमाम् इत्यत्र तलोपस्यासिद्धत्वात् "
            "तरप्तमपोर् न लुग् भवति। चिणो लुग् इत्येतद् "
            "विषयभेदाद् भिद्यते** — the तिप् is gone and 6.4.22 "
            "hides that, so the तरप् is no longer *after चिण्*"),
    Sarva(
        "6.4.105", does="lopa", gana="a-anta", before=("hi",),
        keeps_out="युहि, रुहि — not अ-final; लुनीहि, पुनीहि — the "
                  "tapara shuts the long आ out, **ईत्वस्यासिद्धत्वाद् "
                  "आकार एव भवति**",
        why="अतो हेः — after an अ-final stem the हि is dropped "
            "outright: **पच, पठ, गच्छ, धाव**. Every Sanskrit "
            "imperative of the first class that looks like a bare "
            "stem is this rule"),
    Sarva(
        "6.4.106", does="lopa", gana="u-pratyaya-anta",
        before=("hi",), excludes=("saṃyoga-pūrva",),
        keeps_out="लुनीहि, पुनीहि — no उ; युहि, रुहि — the उ is "
                  "the root's and no affix; प्राप्नुहि, राध्नुहि, "
                  "तक्ष्णुहि — a cluster before the उ",
        why="उतश्च प्रत्ययादसंयोगपूर्वात् — and after a उ that is "
            "an AFFIX and has no cluster before it: **चिनु, सुनु, "
            "कुरु**. A vārttika makes it optional in the Veda: "
            "**उतश्च प्रत्ययाच्छन्दसि वेति वक्तव्यम्**"),
    Sarva(
        "6.4.107", does="lopa", gana="u-pratyaya-anta",
        before=("va", "ma"), excludes=("saṃyoga-pūrva",),
        optional=True,
        keeps_out="युवः, युमः — the उ is the root's; शक्नुवः, "
                  "शक्नुमः — a cluster before it",
        why="लोपश्चास्यान्यतरस्यां म्वोः — and that same उ is "
            "dropped OPTIONALLY before an affix beginning with व् "
            "or म्: **सुन्वः / सुनुवः; सुन्मः / सुनुमः; तन्वः / "
            "तनुवः; तन्मः / तनुमः**.\\n\\n"
            "**AND THE WORD लोप IS SAID THOUGH लुक् WAS RUNNING.** "
            "**लुगिति वर्तमाने लोपग्रहणम् अन्त्यलोपार्थम्** — a "
            "लुक् takes the whole affix and a लोप only its last "
            "sound, and here only the उ goes"),
    Sarva(
        "6.4.108", does="lopa", of=("kṛ",), gana="u-pratyaya-anta", and_gana=True,
        before=("va", "ma"), nitya=True, blocks=("6.4.107",),
        why="नित्यं करोतेः — but after कृ the loss is COMPULSORY: "
            "**कुर्वः, कुर्मः**, and no second form. The word "
            "नित्यम् is the whole of the difference from the "
            "sūtra before.\\n\\n"
            "**AND THE FORM THEN ESCAPES A LENGTHENING BY A "
            "NAMED EXCEPTION.** **उकारलोपस्य दीर्घविधाव् "
            "अस्थानिवद्भावाद् हलि च इति दीर्घत्वं प्राप्तं न "
            "भकुर्छुराम् इति प्रतिषिध्यते** — 1.1.58 does not "
            "hide the loss from a lengthening rule, so 8.2.77 "
            "reaches कुर्वः, and 8.2.79 names कुर् out"),
    Sarva(
        "6.4.109", does="lopa", of=("kṛ",), gana="u-pratyaya-anta", and_gana=True,
        before=("ya",), nitya=True,
        why="ये च — and before a य्-initial affix, also "
            "compulsory: **कुर्यात्, कुर्याताम्, कुर्युः** — the "
            "optative of कृ, and the commonest verb-form in "
            "Sanskrit prose"),
    Sarva(
        "6.4.110", does="ut", of=("kṛ",), gana="u-pratyaya-anta", and_gana=True,
        part="a", before=("sārvadhātuka",), result=("kṅit",),
        keeps_out="करोति, करोषि, करोमि — the affix is neither "
                  "कित् nor ङित्",
        why="अत उत् सार्वधातुके — the अ of कृ with its उ-affix "
            "becomes उ before a कित् or ङित् सार्वधातुक: "
            "**कुरुतः, कुर्वन्ति**.\\n\\n"
            "**AND सार्वधातुक IS SAID FOR AN AFFIX THAT IS NO "
            "LONGER THERE.** **सार्वधातुकग्रहणं किम्? "
            "भूतपूर्वेऽपि सार्वधातुके यथा स्यात् — कुरु** — the "
            "हि has been dropped by 6.4.106, and the rule still "
            "has to reach what once stood before one"),
    Sarva(
        "6.4.111", does="lopa", of=("as",), gana="śna",
        part="a", before=("sārvadhātuka",), result=("kṅit",),
        keeps_out="भिनत्ति, अस्ति — the affix is neither कित् nor "
                  "ङित्",
        why="श्नसोरल्लोपः — the अ of श्न and of अस् is dropped "
            "before a कित् or ङित् सार्वधातुक: **रुन्धः, "
            "रुन्धन्ति; भिन्तः, भिन्दन्ति; स्तः, सन्ति**. This is "
            "the rule that makes the seventh class conjugate as "
            "it does, and the one that makes सन्ति out of अस्"),
    Sarva(
        "6.4.112", does="lopa", of=("śnā",), gana="abhyasta",
        part="ā", before=("sārvadhātuka",), result=("kṅit",),
        keeps_out="यान्ति, वान्ति — neither श्ना nor reduplicated; "
                  "बिभ्रति — no आ to drop; अलुनात्, अजहात् — the "
                  "affix is neither कित् nor ङित्",
        why="श्नाभ्यस्तयोरातः — the आ of श्ना and of a "
            "REDUPLICATED stem is dropped before a कित् or ङित् "
            "सार्वधातुक: **लुनते, लुनताम्, अलुनत**; **मिमते, "
            "मिमताम्, अमिमत; संजिहते, संजिहताम्, समजिहत**"),
    Sarva(
        "6.4.113", does="īt", gana="śnā-abhyasta", part="ā",
        before=("sārvadhātuka",), result=("kṅit", "hal-ādi"),
        excludes=("ghu",),
        keeps_out="लुनन्ति, मिमते — the affix begins with a vowel; "
                  "दत्तः, धत्तः — the घु class, which the sūtra "
                  "shuts out",
        why="ई हल्यघोः — and that same आ becomes ई before a "
            "CONSONANT-initial कित् or ङित् सार्वधातुक, the घु "
            "class excepted: **लुनीतः, पुनीतः, लुनीथः, लुनीते**; "
            "**मिमीते, मिमीषे, मिमीध्वे; संजिहीते, संजिहीषे, "
            "संजिहीध्वे**. So the ninth class's ना becomes नी "
            "before a consonant and goes altogether before a "
            "vowel, by two sūtras standing side by side"),
    Sarva(
        "6.4.114", does="it", of=("daridrā",),
        before=("sārvadhātuka",), result=("kṅit", "hal-ādi"),
        keeps_out="दरिद्रति — the affix begins with a vowel; "
                  "दरिद्राति — neither कित् nor ङित्",
        why="इद् दरिद्रस्य — and दरिद्रा takes इ before a "
            "consonant-initial कित् or ङित् सार्वधातुक: "
            "**दरिद्रितः, दरिद्रिथः, दरिद्रिवः, दरिद्रिमः**.\\n\\n"
            "**AND TWO VĀRTTIKAS SETTLE WHAT THE SŪTRA LEAVES.** "
            "**दरिद्रातेर् आर्धधातुके लोपो वक्तव्यः**, and "
            "**सिद्धश्च प्रत्ययविधौ भवतीति वक्तव्यम्** — the loss "
            "before an ārdhadhātuka, and that loss counting as "
            "already done when an affix is being prescribed, so "
            "that **दरिद्रातीति दरिद्रः** comes out"),
)


def _reaches(row: Sarva, stem: str, gana: str, before: str,
             part: str, result: str, chandasi: bool) -> bool:
    if row.and_gana:
        if row.of and stem not in row.of:
            return False
        if row.gana and gana != row.gana:
            return False
    else:
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


def _supplies(row: Sarva, wants: str) -> bool:
    return not wants or wants == row.does


def _how_specific(row: Sarva, stem: str, gana: str) -> int:
    """
    A rule that says नित्यम् against an option outranks it, and a
    named stem beats a named class.

    6.4.107 and 6.4.108 are the pair: both drop the उ of a उ-affix
    before व् and म्, and the only difference is that the second
    names कृ and says नित्यम्.
    """
    return (
        12 * (0 if not row.nitya else len(row.blocks))
        + 6 * bool(row.of and stem in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.result)
        + 2 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Shed:
    """What the run answers: a loss or a substitute."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    nitya: bool = False
    blocked_by: Tuple[str, ...] = ()


def before_sarvadhatuka(stem: str = "", *, gana: str = "",
                        before: str = "", part: str = "",
                        result: str = "", chandasi: bool = False,
                        wants: str = "") -> Shed:
    """
    6.4.96–114 — what the stem loses before the ending.

    Nothing answers by default: where no rule is reached the stem
    stands as it is, which is what करोति and अस्ति are.
    """
    matched = [
        row for row in SARVA_TABLE
        if _reaches(row, stem, gana, before, part, result, chandasi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Shed(
            "", "", "No rule of 6.4.96–114 is reached, so the "
                    "stem stands as it is")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Shed(row.does, row.sutra, row.why, optional=row.optional,
                nitya=row.nitya, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Sarva, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in SARVA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Sarva", "SARVA_TABLE", "SARVA_RUN", "GAMA_FIVE",
    "DHI_CHANDASI", "HI_SHAPES", "Shed", "before_sarvadhatuka",
    "provisions_for",
]
