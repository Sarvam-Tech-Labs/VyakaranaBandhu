# -*- coding: utf-8 -*-
"""
3.1.133 to 3.1.150 — the agent affixes, and the close of the pāda.

3.1.95's कृत्य heading stopped at 3.1.133, and this is the rule it
stopped before. From here the affixes name a DOER rather than a thing
to be done:

    3.1.133 ण्वुल्तृचौ                ण्वुल् and तृच्, after any root
    3.1.135 इगुपधज्ञाप्रीकिरः कः      क, after an इक् penult and three
    3.1.136 आतश्चोपसर्गे              and after आ, with a preverb
    3.1.137 पाघ्राध्माधेट्दृशः शः      श, after five roots with a preverb
    3.1.138 अनुपसर्गाल्लिम्प…श्च       and after nine, without one
    3.1.139 ददातिदधात्योर्विभाषा      optionally after two more
    3.1.140 ज्वलितिकसन्तेभ्यो णः      ण, after a span of the first class
    3.1.141 श्यादव्यधास्रु…श्च         and after आ-final and nine roots
    3.1.142 दुन्योरनुपसर्गे            and after two, without a preverb
    3.1.143 विभाषा ग्रहः              optionally after ग्रह्
    3.1.144 गेहे कः                   क, where a house is meant
    3.1.145 शिल्पिनि ष्वुन्            ष्वुन्, of a craftsman
    3.1.146 गस्थकन्                   थकन्, of one who sings
    3.1.147 ण्युट् च                  and ण्युट्, likewise
    3.1.148 हश्च व्रीहिकालयोः          and after हा, of rice and of time
    3.1.149 प्रुसृल्वः समभिहारे वुन्    वुन्, of doing a thing well
    3.1.150 आशिषि च                   and in a blessing

3.1.134 stands inside this run and was codified long ago, for the
अच् that 1.1.4 turns on.

**Three conditions here are decided by rules already codified, so they
are asked.** इगुपध at 3.1.135 is 1.1.65 अलोऽन्त्यात्पूर्व उपधा and the
pratyāhāra इक् together — the penultimate sound, and whether it falls
in that span. Whether a preverb is present, which five rules turn on,
is 1.4.59 उपसर्गाः क्रियायोगे. And 3.1.140's गण is not a list at all
but a STRETCH of the dhātupāṭha — ज्वल इत्येवमादिभ्यः कस इत्येवमन्तेभ्यः
— so it is read off the corpus by its codes.

**समभिहार does not mean here what it meant at 3.1.22.** There it was
पौनःपुन्यं भृशार्थो वा, doing a thing again and again or intensely.
Here the vṛtti reads it as doing a thing WELL —
समभिहारग्रहणेनात्र साधुकारित्वं लक्ष्यते — and draws the consequence:
सकृदपि यः सुष्ठु करोति तत्र भवति, बहुशो यो दुष्टं करोति तत्र न भवति.
Once done well is enough, and often done badly is not. One word, two
senses, and the two rules must not share a field.
"""

from dataclasses import dataclass
from typing import Tuple

# One copy, in `krt_conditions`: 3.2 asks the same three questions
# from its first sūtra, and two answers to one question drift.
from src.astadhyayi.krt_conditions import (
    ends_in_a as _ends_in_a,
    has_upasarga as _has_upasarga,
    in_dhatupatha_span,
    is_igupadha as _is_igupadha,
)

# ---------------------------------------------------------------------------
# The lists the sūtras name
# ---------------------------------------------------------------------------

#: 3.1.135's three named roots, beside any इगुपध.
JNADI: Tuple[str, ...] = ("jñā", "prī", "kṝ")

#: 3.1.137's five, which take श with a preverb.
PADI: Tuple[str, ...] = ("pā", "ghrā", "dhmā", "dheṭ", "dṛś")

#: 3.1.138's nine, which take श without one.
LIMPADI: Tuple[str, ...] = (
    "limp", "vind", "dhāri", "pāri", "vedi", "udeji", "ceti", "sāti",
    "sāhi",
)

#: 3.1.141's nine, beside श्यै and the आ-final roots.
VYADHADI: Tuple[str, ...] = (
    "vyadh", "āsru", "saṃsru", "atīṇ", "avasā", "avahṛ", "lih", "śliṣ",
    "śvas",
)

#: 3.1.149's three.
PRUSRLU: Tuple[str, ...] = ("pru", "sṛ", "lū")

#: 3.1.140's गण, as the dhātupāṭha's own codes. The vṛtti gives it as a
#: stretch and not a list — ज्वल इत्येवमादिभ्यः कस इत्येवमन्तेभ्यः — and
#: the corpus reads ज्वल at 01.0916 and कस् at 01.0996, with the
#: vṛtti's own चल at 01.0924 between them. So the bound is read, not
#: copied: a hand-written list would be a second statement of a span
#: the data already has.
JVALADI_FROM, JVALADI_THROUGH = "01.0916", "01.0996"


@dataclass(frozen=True)
class Added:
    """An agent affix put after the root, and by which rule."""

    gives: str
    by: str
    why: str
    optional: bool = False
    also: str = ""


@dataclass(frozen=True)
class NotAdded:
    """That no rule of this run reaches it."""

    by: str
    why: str
    gives: str = ""




def _in_jvaladi(root: str) -> bool:
    """
    Whether the root falls in 3.1.140's stretch of the first class —
    ज्वल इत्येवमादिभ्यः कस इत्येवमन्तेभ्यः, read off the corpus.
    """
    return in_dhatupatha_span(root, JVALADI_FROM, JVALADI_THROUGH)


@dataclass(frozen=True)
class Agent:
    """One rule adding an agent affix, as its conditions."""

    sutra: str
    gives: str
    of: Tuple[str, ...] = ()
    igupadha: bool = False
    a_final: bool = False
    jvaladi: bool = False
    #: True where a preverb is wanted, False where it is refused, None
    #: where the rule says nothing about one.
    upasarga: object = None
    sense: str = ""
    craftsman: bool = False
    optional: bool = False
    also: str = ""
    #: Extra weight where the vṛtti says a rule is written to defeat
    #: another that would otherwise win — 3.1.141's श्यै.
    badhaka: int = 0
    why: str = ""


AGENT: Tuple[Agent, ...] = (
    Agent("3.1.133", "ṇvul", also="तृच्",
          why="ण्वुल्तृचौ — कारकः and कर्ता, हारकः and हर्ता. "
              "सर्वधातुभ्यः, after every root, and everything after it "
              "in the pāda is an अपवाद. चकारः सामान्यग्रहणार्थः, the च "
              "so that तृ can be named in general at 5.3.59 and "
              "6.4.154"),
    Agent("3.1.135", "ka", igupadha=True,
          why="इगुपधज्ञाप्रीकिरः कः — विक्षिपः, विलिखः, बुधः, कृशः. "
              "इगुपध is two codified rules together, 1.1.65 for which "
              "sound is the penult and the pratyāhāra इक् for whether "
              "it falls there, so it is asked rather than restated"),
    Agent("3.1.135", "ka", of=JNADI,
          why="…ज्ञाप्रीकिरः कः — ज्ञः, प्रियः, किरः, the three named "
              "beside the इगुपध roots. They have to be named because "
              "none of them IS one: ज्ञा's penult is ञ् and no इक् at "
              "all, which is exactly what asking 1.1.65 shows"),
    Agent("3.1.136", "ka", a_final=True, upasarga=True,
          why="आतश्चोपसर्गे — प्रस्थः, सुग्लः, सुम्लः. णस्यापवादः, an "
              "exception to the ण 3.1.141 gives every आ-final root"),
    Agent("3.1.137", "śa", of=PADI, upasarga=True,
          why="पाघ्राध्माधेट्दृशः शः — उत्पिबः, उज्जिघ्रः, उद्धमः, "
              "उद्धयः, उत्पश्यः. उपसर्ग इति केचिन् नानुवर्तयन्ति — "
              "some do not carry the preverb down and read पश्यः "
              "alone. A vārttika keeps a name out: व्याघ्रः"),
    Agent("3.1.138", "śa", of=LIMPADI, upasarga=False,
          why="अनुपसर्गाल्लिम्प… — लिम्पः, विन्दः, धारयः, पारयः. "
              "सातिः सौत्रो धातुः, one the sūtra supplies. "
              "अनुपसर्गाद् इति किम्? प्रलिपः. Two vārttikas keep "
              "names: निलिम्पा नाम देवाः, गोविन्दः, अरविन्दः"),
    Agent("3.1.139", "śa", of=("dā", "dhā"), optional=True,
          why="ददातिदधात्योर्विभाषा — ददः beside दायः, दधः beside "
              "धायः. णस्यापवादः. अनुपसर्गाद् इत्येव: प्रदः, प्रधः"),
    Agent("3.1.140", "ṇa", jvaladi=True, upasarga=False, optional=True,
          why="ज्वलितिकसन्तेभ्यो णः — ज्वालः beside ज्वलः, चालः beside "
              "चलः. अचोऽपवादः. इतिशब्द आद्यर्थः, and the गण is a "
              "STRETCH of the dhātupāṭha rather than a list — ज्वल "
              "इत्येवमादिभ्यः कस इत्येवमन्तेभ्यः — so it is read off "
              "the corpus by its codes. A vārttika adds तन्: अवतानः"),
    Agent("3.1.141", "ṇa", a_final=True,
          why="श्यादव्यधास्रु…श्च — दायः, धायः, अत्यायः, अवसायः. "
              "अनुपसर्गाद् इति विभाषेति च निवृत्तम्, both conditions "
              "from the rules before are dropped here"),
    Agent("3.1.141", "ṇa", of=VYADHADI,
          why="…व्यधास्रुसंस्र्वतीणवसाऽवहृलिहश्लिषश्वसश्च — व्याधः, "
              "आस्रावः, संस्रावः, अवहारः, लेहः, श्लेषः, श्वासः"),
    Agent("3.1.141", "ṇa", of=("śyai",), badhaka=4,
          why="श्यै is named though it is आ-final and 3.1.141 already "
              "reaches it, and the vṛtti says what the naming buys: "
              "आकारान्तत्वादेव श्यायतेः प्रत्यये सिद्धे पुनर्वचनं "
              "बाधकबाधनार्थम् — to defeat 3.1.136's क where a preverb "
              "stands. अवश्यायः, प्रतिश्यायः. The second rule in this "
              "pāda repeated to survive another, after 3.1.109"),
    Agent("3.1.142", "ṇa", of=("du", "nī"), upasarga=False,
          why="दुन्योरनुपसर्गे — दुनोतीति दावः, नयतीति नायः. "
              "अनुपसर्ग इति किम्? प्रदवः, प्रणयः"),
    Agent("3.1.143", "ṇa", of=("grah",), optional=True,
          why="विभाषा ग्रहः — ग्राहः beside ग्रहः, अचोऽपवादः. And a "
              "व्यवस्थितविभाषा, settled by what is meant rather than "
              "chosen: जलचरे नित्यं ग्राहः, ज्योतिषि नेष्यते तत्र ग्रह "
              "एव. A vārttika adds भू: भावः beside भवः"),
    Agent("3.1.144", "ka", of=("grah",), sense="geha",
          why="गेहे कः — गृहं वेश्म. And तात्स्थ्याद् दाराश्च: by the "
              "thing standing in it the word reaches a household too, "
              "गृह्णन्तीति गृहा दाराः"),
    Agent("3.1.145", "ṣvun", craftsman=True,
          why="शिल्पिनि ष्वुन् — of a craftsman. A vārttika holds it "
              "to three roots by counting them, नृतिखनिरञ्जिभ्यः "
              "परिगणनं कर्तव्यम्: नर्तकः, खनकः, रजकः, and their "
              "feminines नर्तकी, खनकी, रजकी"),
    Agent("3.1.147", "ṇyuṭ", of=("gā",), craftsman=True,
          why="ण्युट् च — गायनः, गायनी. चकारेण ग इत्यनुकृष्यते: the च "
              "drags गै down from 3.1.146, so one root takes two "
              "affixes and both forms stand. योगविभाग उत्तरार्थः — the "
              "split is for 3.1.148, which needs the ण्युट् and not "
              "the थकन्"),
    Agent("3.1.146", "thakan", of=("gai",), craftsman=True,
          also="or ण्युट् by 3.1.147",
          why="गस्थकन् — गाथकः, गाथिका. And 3.1.147 ण्युट् च gives the "
              "same root a second affix beside it, गायनः, गायनी. "
              "योगविभाग उत्तरार्थः: the split is for the rule after, "
              "since 3.1.148 needs the ण्युट् and not the थकन्"),
    Agent("3.1.148", "ṇyuṭ", of=("hā",), sense="vrīhi",
          why="हश्च व्रीहिकालयोः — हायना नाम व्रीहयः, जहत्युदकम् इति "
              "कृत्वा, the rice that leaves the water behind. जहाति "
              "and जिहीते are both meant, two roots written alike"),
    Agent("3.1.148", "ṇyuṭ", of=("hā",), sense="kāla",
          why="…व्रीहिकालयोः — हायनः संवत्सरः, जिहीते भावान् इति "
              "कृत्वा, the year that goes"),
    Agent("3.1.149", "vun", of=PRUSRLU, sense="samabhihāra",
          why="प्रुसृल्वः समभिहारे वुन् — प्रवकः, सरकः, लवकः. And "
              "समभिहार is NOT what it was at 3.1.22: "
              "समभिहारग्रहणेनात्र साधुकारित्वं लक्ष्यते, doing a thing "
              "WELL. सकृदपि यः सुष्ठु करोति तत्र भवति, बहुशो यो दुष्टं "
              "करोति तत्र न भवति — once done well is enough, and often "
              "done badly is not"),
    Agent("3.1.150", "vun", sense="āśis",
          why="आशिषि च — जीवतात् जीवकः, नन्दतात् नन्दकः. आशीः "
              "प्रार्थनाविशेषः, and स चेह क्रियाविषयः: the wish is "
              "about the ACT — अमुष्याः क्रियायाः कर्ता भवेद् इति एवम् "
              "आशास्यते. The last rule of the pāda"),
)


def agent_affix(
    root: str = "",
    *,
    upasarga: str = "",
    sense: str = "",
    craftsman: bool = False,
) -> object:
    """
    Which agent affix a root takes — 3.1.133 to 3.1.150.

    3.1.133 reaches every root and everything after it is an अपवाद, so
    the MORE SPECIFIC rule answers. The chain is stated rather than
    inferred: 3.1.136 and 3.1.139 are both णस्यापवादः, 3.1.140 and
    3.1.143 are अचोऽपवादः, and 3.1.141's श्यै is written
    बाधकबाधनार्थम् to defeat 3.1.136 in turn.
    """
    # Both conditions are worked out HERE rather than deep inside the
    # row test, so that the rules they ask stay one call away: the
    # reuse guard walks two deep, and a declaration it cannot see is
    # refused however true it is.
    with_preverb = _has_upasarga(upasarga)
    igupadha = _is_igupadha(root)
    matched = [row for row in AGENT
               if _reaches(row, root, with_preverb, igupadha, sense,
                           craftsman)]
    best = max(matched, key=_how_specific)
    return Added(best.gives, best.sutra, best.why,
                 optional=best.optional, also=best.also)


def _how_specific(row: Agent) -> int:
    """
    How much a row says. Naming a ROOT outweighs naming a shape, for
    the reason the कृत्य run established: a rule that names what a
    shape rule already reached is there to qualify it. ज्ञा is the
    plainest case here — it is आ-final, so 3.1.141 reaches it, and
    3.1.135 names it anyway.
    """
    return (
        3 * (len(row.of) > 0) + row.igupadha + row.a_final + row.jvaladi
        + (row.upasarga is not None) + 2 * bool(row.sense)
        + 2 * row.craftsman + row.badhaka
    )


def _reaches(row: Agent, root: str, with_preverb: bool,
             igupadha: bool, sense: str, craftsman: bool) -> bool:
    """Whether one row covers this root at all."""
    if row.of and root not in row.of:
        return False
    if row.igupadha and not igupadha:
        return False
    if row.a_final and not _ends_in_a(root):
        return False
    if row.jvaladi and not _in_jvaladi(root):
        return False
    if row.upasarga is not None and bool(row.upasarga) != with_preverb:
        return False
    if row.sense and row.sense != sense:
        return False
    if row.craftsman != craftsman:
        return False
    return True


def provisions_for(sutra_id: str) -> Tuple[Agent, ...]:
    """Every row a sūtra of this run states."""
    return tuple(r for r in AGENT if r.sutra == sutra_id)


