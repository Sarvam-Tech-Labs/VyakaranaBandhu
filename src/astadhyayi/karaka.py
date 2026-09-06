# -*- coding: utf-8 -*-
"""
The kārakas — 1.4.23 to 1.4.55.

Thirty-three sūtras giving six names to the participants in an action, and one
more to the person who sets an agent going:

    1.4.24 – 1.4.31   अपादान      what a departure is from
    1.4.32 – 1.4.41   सम्प्रदान    who a giving is to
    1.4.42 – 1.4.44   करण          what it is done with
    1.4.45 – 1.4.48   अधिकरण      where it takes place
    1.4.49 – 1.4.53   कर्मन्        what it is done to
    1.4.54 – 1.4.55   कर्तृ, हेतु   who does it, and who makes them

**The order of the six is the mechanism.** They stand under 1.4.1 आ कडारादेका
संज्ञा, where one name only may apply and the later stands; and Pāṇini has
arranged them so that the later name is always the one wanted. कर्तृ is last
and beats everything, कर्मन् beats सम्प्रदान and करण, and the two sūtras
1.4.38 and 1.4.46–48 exist only to move particular cases *later* — from
सम्प्रदान or अधिकरण to कर्मन्. So the resolution is `eka_samjna`'s, called and
not written out, and each verdict names what it displaced.

The Kāśikā makes the same point from the other side at 1.4.49, explaining why
कर्म is said twice over: पुनः कर्मग्रहणम् आधारनिवृत्त्यर्थम्, इतरथा आधारस्यैव
हि स्यात् — without the repetition गेहं प्रविशति would come out अधिकरण.

**And 1.4.55 breaks the rule deliberately.** तत्प्रयोजको हेतुश्च: the च gives
the causer *both* names, and the Kāśikā says so in as many words —
संज्ञासमावेशार्थश्चकारः — with the reason: हेतुत्वाद् णिचो निमित्तं,
कर्तृत्वाच्च कर्तृप्रत्ययेनोच्यते. Being हेतु it triggers the causative affix;
being कर्तृ it is expressed by the agent-ending. It needs both, so an explicit
च restores what 1.4.1 withdrew.

**What is given.** Every one of these is semantic. ध्रुव, ईप्सिततम, साधकतम,
स्वतन्त्र — no property of a form settles any of them, and 1.4.23's own
counter-example turns on it: वृक्षस्य पर्णं पतति has a tree and a falling and
no kāraka at all, because the tree is not a cause of the falling. So the facts
are asserted by the caller, as everywhere else in this codification, and
`near_misses` reports which assertion was wanting.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, List, Optional, Sequence, Tuple

from src.astadhyayi.formation import order_of
from src.astadhyayi.pada import root_key
from src.astadhyayi.vipratisedha import Rule, eka_samjna


class Karaka(Enum):
    """The six, and हेतु, in the order the sūtras give them."""

    APADANA = "apādāna"
    SAMPRADANA = "sampradāna"
    KARANA = "karaṇa"
    ADHIKARANA = "adhikaraṇa"
    KARMAN = "karman"
    KARTR = "kartṛ"
    HETU = "hetu"


# --- what the caller asserts ----------------------------------------------
#
# Each is a sūtra's own description of the participant. Held in one set so a
# misspelling is a test failure rather than a rule that never fires.

FACTS: FrozenSet[str] = frozenset(
    """
    dhruva-apāya bhaya-hetu asoḍha vāraṇa-īpsita antardhi-adarśana
    ākhyātā-upayoga jani-prakṛti prabhava karmaṇā-abhipreta prīyamāṇa
    jñīpsyamāna uttamarṇa spṛhā-īpsita kopa-viṣaya vipraśna pūrvasya-kartā
    sādhakatama ādhāra īpsitatama anīpsita-tathāyukta akathita aṇau-kartā
    svatantra prayojaka parikrayaṇa dyūta-paṇa
    """.split()
)

#: The verb-classes the sūtras name by sense rather than by root. Each is the
#: sūtra's own word, and where the Kāśikā glosses it the gloss is in the note.
VERB_SENSES: FrozenSet[str] = frozenset(
    """
    bhī-trā vāraṇa ruc ślāgh-hnu-sthā-śap dhṛ spṛh
    krudh-druh-īrṣyā-asūyā rādh-īkṣ jugupsā-virāma-pramāda
    gati-buddhi-pratyavasāna-śabdakarman-akarmaka
    """.split()
)


@dataclass(frozen=True)
class Participant:
    """
    One participant in an action, as far as these thirty-three sūtras care.

    `given` holds the semantic facts asserted about it — that it is the fixed
    point of a departure, that it is what the agent most wants to reach. None
    of them is readable off a form.
    """

    verb: Optional[str] = None
    verb_sense: Tuple[str, ...] = ()
    upasargas: Tuple[str, ...] = ()
    given: Tuple[str, ...] = ()
    causative: bool = False

    def has(self, fact: str) -> bool:
        return fact in self.given


@dataclass(frozen=True)
class Provision:
    """One sūtra's contribution, as conditions rather than as code."""

    sutra: str
    gives: Karaka
    #: 1.4.55's च — this name applies *beside* the other rather than instead.
    alongside: Optional[Karaka] = None
    roots: Tuple[str, ...] = ()
    senses: Tuple[str, ...] = ()
    upasargas: Tuple[str, ...] = ()
    upasarga: Optional[bool] = None
    requires: Tuple[str, ...] = ()
    causative: Optional[bool] = None
    optional: bool = False
    gloss: str = ""
    example: str = ""
    counter: str = ""

    def unmet(self, who: Participant) -> Tuple[str, ...]:
        missing: List[str] = []
        if self.roots:
            key = root_key(who.verb) if who.verb else None
            if key not in {root_key(r) for r in self.roots}:
                missing.append(f"verb is not one of {', '.join(self.roots)}")
        if self.senses and not (set(self.senses) & set(who.verb_sense)):
            missing.append(f"verb is not {'/'.join(self.senses)}-artha")
        if self.upasargas and not (set(self.upasargas) & set(who.upasargas)):
            missing.append(f"no upasarga among {', '.join(self.upasargas)}")
        if self.upasarga is True and not who.upasargas:
            missing.append("no upasarga at all")
        if self.upasarga is False and who.upasargas:
            missing.append("an upasarga is present")
        if self.causative is not None and who.causative is not self.causative:
            missing.append(
                "not a causative" if self.causative else "is a causative")
        for fact in self.requires:
            if not who.has(fact):
                missing.append(f"{fact} not stated")
        return tuple(missing)

    def applies(self, who: Participant) -> bool:
        return not self.unmet(who)

    def describe(self) -> str:
        parts: List[str] = []
        if self.roots:
            parts.append("verb ∈ {" + ", ".join(self.roots) + "}")
        if self.senses:
            parts.append("verb is " + "/".join(self.senses) + "-artha")
        if self.upasargas:
            parts.append("upasarga ∈ {" + ", ".join(self.upasargas) + "}")
        if self.upasarga is False:
            parts.append("no upasarga")
        if self.causative is not None:
            parts.append("causative" if self.causative else "not causative")
        parts.extend(self.requires)
        head = self.gives.value
        if self.alongside:
            head += f" and {self.alongside.value} together"
        if self.optional:
            head = "optionally " + head
        return f"{head} when {'; '.join(parts)}" if parts else head


def _p(*args, **kwargs) -> Provision:
    return Provision(*args, **kwargs)


A, S, KR, ADH, KM, KT, H = (
    Karaka.APADANA, Karaka.SAMPRADANA, Karaka.KARANA, Karaka.ADHIKARANA,
    Karaka.KARMAN, Karaka.KARTR, Karaka.HETU,
)


PROVISIONS: Tuple[Provision, ...] = (
    # --- अपादान, 1.4.24 to 1.4.31 --------------------------------------
    _p("1.4.24", A, requires=("dhruva-apāya",),
       gloss="ध्रुवमपायेऽपादानम् — the fixed point from which a going away is "
             "reckoned",
       example="grāmād āgacchati, parvatād avarohati, rathāt patitaḥ"),
    _p("1.4.24v1", A, requires=("dhruva-apāya",),
       senses=("jugupsā-virāma-pramāda",),
       gloss="जुगुप्साविरामप्रमादार्थानाम् (vārt.) — and with verbs of "
             "loathing, desisting and being careless",
       example="adharmāj jugupsate, adharmād viramati, dharmāt pramādyati"),
    _p("1.4.25", A, senses=("bhī-trā",), requires=("bhaya-hetu",),
       gloss="भीत्रार्थानां भयहेतुः — with verbs of fearing and protecting, "
             "what the fear is of",
       example="corād bibheti"),
    _p("1.4.26", A, roots=("ji",), upasargas=("parā",), requires=("asoḍha",),
       gloss="पराजेरसोढः — with परा-जि, what is not put up with",
       example="adhyayanāt parājayate"),
    _p("1.4.27", A, senses=("vāraṇa",), requires=("vāraṇa-īpsita",),
       gloss="वारणार्थानामीप्सितः — with verbs of warding off, the thing "
             "wanted that is kept away",
       example="yavebhyo gāṃ vārayati"),
    _p("1.4.28", A, requires=("antardhi-adarśana",),
       gloss="अन्तर्द्धौ येनादर्शनमिच्छति — in concealing, the one from whom "
             "one wishes not to be seen",
       example="upādhyāyād antardhatte"),
    _p("1.4.29", A, requires=("ākhyātā-upayoga",),
       gloss="आख्यातोपयोगे — the teacher, where the learning is regular",
       example="upādhyāyād adhīte"),
    _p("1.4.30", A, requires=("jani-prakṛti",),
       gloss="जनिकर्तुः प्रकृतिः — what the thing born is born of",
       example="brahmaṇaḥ prajāḥ prajāyante"),
    _p("1.4.31", A, roots=("bhū",), requires=("prabhava",),
       gloss="भुवः प्रभवः — with भू, where a thing takes its rise",
       example="himavato gaṅgā prabhavati"),

    # --- सम्प्रदान, 1.4.32 to 1.4.41 -------------------------------------
    _p("1.4.32", S, requires=("karmaṇā-abhipreta",),
       gloss="कर्मणा यमभिप्रैति स सम्प्रदानम् — the one the agent means to "
             "reach by means of the object",
       example="brāhmaṇāya gāṃ dadāti"),
    _p("1.4.33", S, senses=("ruc",), requires=("prīyamāṇa",),
       gloss="रुच्यर्थानां प्रीयमाणः — with verbs of pleasing, the one pleased",
       example="devadattāya rocate modakaḥ"),
    _p("1.4.34", S, senses=("ślāgh-hnu-sthā-śap",),
       requires=("jñīpsyamāna",),
       gloss="श्लाघह्नुङ्स्थाशपां ज्ञीप्स्यमानः — with these four, the one to "
             "be made to know",
       example="devadattāya ślāghate"),
    _p("1.4.35", S, senses=("dhṛ",), requires=("uttamarṇa",),
       gloss="धारेरुत्तमर्णः — with धृ, the creditor",
       example="devadattāya śataṃ dhārayati"),
    _p("1.4.36", S, senses=("spṛh",), requires=("spṛhā-īpsita",),
       gloss="स्पृहेरीप्सितः — with स्पृह्, the thing longed for",
       example="puṣpebhyaḥ spṛhayati"),
    # No upasarga condition: the sūtra has none, and 1.4.38 is what handles
    # the prefixed case. An earlier version of this provision carried
    # upasarga=False, which produced the right answer for the wrong reason —
    # 1.4.38 then won by being the only rule that matched rather than by
    # standing later, and 1.4.1 was doing nothing at all.
    _p("1.4.37", S, senses=("krudh-druh-īrṣyā-asūyā",),
       requires=("kopa-viṣaya",),
       gloss="क्रुधद्रुहेर्ष्यासूयार्थानां यं प्रति कोपः — with verbs of anger, "
             "the one it is directed at",
       example="devadattāya krudhyati"),
    _p("1.4.38", KM, roots=("krudh", "druh"), upasarga=True,
       requires=("kopa-viṣaya",),
       gloss="क्रुधद्रुहोरुपसृष्टयोः कर्म — but with an upasarga on क्रुध् or "
             "द्रुह्, the object instead",
       example="devadattam abhikrudhyati"),
    _p("1.4.39", S, senses=("rādh-īkṣ",), requires=("vipraśna",),
       gloss="राधीक्ष्योर्यस्य विप्रश्नः — with राध् and ईक्ष्, the one "
             "enquired about",
       example="devadattāya rādhyati"),
    _p("1.4.40", S, roots=("śru",), upasargas=("prati", "ā"),
       requires=("pūrvasya-kartā",),
       gloss="प्रत्याङ्भ्यां श्रुवः पूर्वस्य कर्ता — with प्रति- or आ-श्रु, the "
             "agent of the earlier act",
       example="devadattāya pratiśṛṇoti"),
    _p("1.4.41", S, roots=("gṝ",), upasargas=("anu", "prati"),
       requires=("pūrvasya-kartā",),
       gloss="अनुप्रतिगृणश्च — and with अनु- or प्रति-गॄ",
       example="devadattāya anugṛṇāti"),

    # --- करण, 1.4.42 to 1.4.44 -------------------------------------------
    _p("1.4.42", KR, requires=("sādhakatama",),
       gloss="साधकतमं करणम् — the most effective means: क्रियासिद्धौ यत् "
             "प्रकृष्टोपकारकं विवक्षितम्",
       example="dātreṇa lunāti, paraśunā chinatti",
       counter="gaṅgāyāṃ ghoṣaḥ, kūpe gargakulam"),
    _p("1.4.43", KM, roots=("div",), requires=("sādhakatama",),
       gloss="दिवः कर्म च — with दिव्, the stake is also called कर्मन्",
       example="akṣair dīvyati / akṣān dīvyati"),
    _p("1.4.44", S, requires=("parikrayaṇa", "sādhakatama"), optional=True,
       gloss="परिक्रयणे सम्प्रदानमन्यतरस्याम् — in hiring, सम्प्रदान "
             "optionally instead of करण",
       example="śatena parikrītaḥ / śatāya parikrītaḥ"),

    # --- अधिकरण, 1.4.45 to 1.4.48 ---------------------------------------
    _p("1.4.45", ADH, requires=("ādhāra",),
       gloss="आधारोऽधिकरणम् — the support: आध्रियन्तेऽस्मिन् क्रिया",
       example="kaṭe āste, sthālyāṃ pacati"),
    _p("1.4.46", KM, roots=("śī", "sthā", "ās"), upasargas=("adhi",),
       requires=("ādhāra",),
       gloss="अधिशीङ्स्थाऽऽसां कर्म — with अधि on these three, the object "
             "instead",
       example="adhiśete grāmam, adhitiṣṭhati grāmam"),
    _p("1.4.47", KM, roots=("viś",), upasargas=("abhi",),
       requires=("ādhāra",),
       gloss="अभिनिविशश्च — and with अभि-नि-विश्",
       example="abhiniviśate grāmam"),
    _p("1.4.48", KM, roots=("vas",), upasargas=("upa", "anu", "adhi", "ā"),
       requires=("ādhāra",),
       gloss="उपान्वध्याङ्वसः — and with these four on वस्",
       example="upavasati grāmam"),

    # --- कर्मन्, 1.4.49 to 1.4.53 ----------------------------------------
    _p("1.4.49", KM, requires=("īpsitatama",),
       gloss="कर्तुरीप्सिततमं कर्म — what the agent most wants to reach by the "
             "action",
       example="kaṭaṃ karoti, grāmaṃ gacchati",
       counter="māṣeṣv aśvaṃ badhnāti; payasaudanaṃ bhuṅkte"),
    _p("1.4.50", KM, requires=("anīpsita-tathāyukta",),
       gloss="तथायुक्तं चानीप्सितम् — and what is connected in the same way "
             "though not wanted",
       example="viṣaṃ bhuṅkte"),
    _p("1.4.51", KM, requires=("akathita",),
       gloss="अकथितं च — and whatever is a kāraka and has not been given "
             "another name",
       example="māṇavakaṃ panthānaṃ pṛcchati",
       counter="māṇavakasya pitaraṃ panthānaṃ pṛcchati"),
    _p("1.4.52", KM, causative=True,
       senses=("gati-buddhi-pratyavasāna-śabdakarman-akarmaka",),
       requires=("aṇau-kartā",),
       gloss="गतिबुद्धिप्रत्यवसानार्थशब्दकर्माकर्मकाणामणि कर्ता स णौ — with the "
             "causative of these five classes, what was the agent without it",
       example="māṇavakaṃ grāmaṃ gamayati"),
    _p("1.4.53", KM, causative=True, roots=("hṛ", "kṛ"),
       requires=("aṇau-kartā",), optional=True,
       gloss="हृक्रोरन्यतरस्याम् — with the causative of हृ and कृ, optionally",
       example="māṇavakena / māṇavakaṃ bhāraṃ hārayati"),

    # --- कर्तृ and हेतु, 1.4.54 and 1.4.55 ------------------------------
    _p("1.4.54", KT, requires=("svatantra",),
       gloss="स्वतन्त्रः कर्ता — the one presented as independent, "
             "प्रधानभूतः अगुणभूतः",
       example="devadattaḥ pacati, sthālī pacati"),
    _p("1.4.55", H, alongside=KT, requires=("prayojaka",),
       gloss="तत्प्रयोजको हेतुश्च — the one who sets that agent going is "
             "called हेतु, and by the च कर्तृ as well",
       example="kurvāṇaṃ prayuṅkte, kārayati, hārayati"),
)


# --- resolving -------------------------------------------------------------


@dataclass(frozen=True)
class Verdict:
    """Which name the participant takes, by which sūtra, and against what."""

    karaka: Optional[Karaka]
    by: str
    why: str
    optional: bool = False
    #: 1.4.55's case: two names standing together rather than one displacing.
    also: Optional[Karaka] = None
    instead_of: Tuple[str, ...] = ()


def resolve(who: Participant) -> Verdict:
    """
    Which kāraka name this participant takes — 1.4.23 to 1.4.55.

    The resolution is 1.4.1's: one name only, and the later stands. That is
    not a convenience here but the design of the section — 1.4.38 and
    1.4.46–1.4.48 exist precisely to move cases from an earlier name to a
    later one, and they would do nothing under any other reading.

    1.4.55 is the exception, and an explicit one: संज्ञासमावेशार्थश्चकारः.
    """
    matched = [p for p in PROVISIONS if p.applies(who)]
    if not matched:
        return Verdict(
            None, "1.4.23",
            "कारके — no name, because nothing here reaches this participant. "
            "The heading itself is a condition: कारकं हेतुरित्यनर्थान्तरम्, a "
            "kāraka is a cause of the action, and वृक्षस्य पर्णं पतति has a "
            "tree that is no cause of the falling.",
        )

    settled = eka_samjna([
        Rule(p.sutra, what=p.gives.value) for p in matched
    ])
    chosen = max(matched, key=lambda p: order_of(p.sutra))

    if chosen.alongside is not None:
        return Verdict(
            chosen.gives, chosen.sutra,
            chosen.gloss + " — and the च is there to make the two names stand "
            "together, against 1.4.1: संज्ञासमावेशार्थश्चकारः. Both are "
            "needed, हेतुत्वाद् णिचो निमित्तं कर्तृत्वाच्च "
            "कर्तृप्रत्ययेनोच्यते.",
            optional=chosen.optional,
            also=chosen.alongside,
        )

    displaced = tuple(s for s in settled.against if s != chosen.sutra)
    why = chosen.gloss
    if displaced:
        why += (f" — and 1.4.1 leaves this one of the "
                f"{len(matched)}: एका संज्ञा, the later standing.")
    return Verdict(
        chosen.gives, chosen.sutra, why,
        optional=chosen.optional, instead_of=displaced,
    )


def karaka_of(
    *,
    verb: Optional[str] = None,
    verb_sense: Sequence[str] = (),
    upasargas: Sequence[str] = (),
    given: Sequence[str] = (),
    causative: bool = False,
) -> Verdict:
    """Which kāraka name a participant takes, given what is asserted of it."""
    return resolve(Participant(
        verb=verb, verb_sense=tuple(verb_sense), upasargas=tuple(upasargas),
        given=tuple(given), causative=causative,
    ))


def near_misses(who: Participant) -> Tuple[Tuple[str, Tuple[str, ...]], ...]:
    """Provisions that would have fired but for one condition."""
    return tuple(
        (p.sutra, unmet) for p in PROVISIONS
        if len(unmet := p.unmet(who)) == 1
    )


def provisions_for(sutra: str) -> Tuple[Provision, ...]:
    """Every provision one sūtra contributes."""
    return tuple(
        p for p in PROVISIONS
        if p.sutra == sutra or p.sutra.startswith(sutra + "v")
    )


__all__ = [
    "FACTS",
    "Karaka",
    "PROVISIONS",
    "Participant",
    "Provision",
    "VERB_SENSES",
    "Verdict",
    "karaka_of",
    "near_misses",
    "provisions_for",
    "resolve",
]
