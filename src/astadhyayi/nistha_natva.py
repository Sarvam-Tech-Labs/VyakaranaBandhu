# -*- coding: utf-8 -*-
"""
८.२.४२–६१ — the निष्ठा's त्, and the six things it becomes instead.

Twenty sūtras on one affix. The निष्ठा — क्त and क्तवतु — is
written with a त्, and this run says where that त् is heard as
something else: as न् after a र् or a द् (आस्तीर्णम्, भिन्नः,
छिन्नः), after a cluster-initial आ-final root (म्लानः), after
the ल्वादि (लूनः, धूनः), after an ओदित् (लग्नः, सूनः); as क्
after शुष् (शुष्कः), व् after पच् (पक्वः), म् after क्षै
(क्षामः), and ल् in फुल्ल.

**AND HALF THE RUN TURNS ON A SENSE AND NOT A FORM.** श्यै gives
शीनं घृतम् of congealed ghee and शीतो वायुः of a cold wind;
अञ्च् gives समक्नौ but उदक्तम् उदकं कूपात् where an अपादान is
there; दिव् gives आद्यूनः of a wretch and द्यूतम् of gambling,
**विजिगीषया हि तत्र अक्षपातनादि क्रियते**; and निर्वाण is the
extinguished fire, the lamp and the monk, but निर्वातो वातः is
the wind that has died down.

**AND ONE SŪTRA IS THE ONLY REFUSAL IN THE WHOLE RUN.** 8.2.57
न ध्याख्यापॄमूर्छिमदाम् keeps the न् off five roots that
8.2.42, 8.2.43 and 8.2.56 between them would otherwise have
reached: ध्यातः, ख्यातः, पूर्तः, मूर्तः, मत्तः.

**AND FOUR MORE WORDS ARE LAID DOWN OUTRIGHT.** वित्त of wealth
and of renown, भित्तम् of a fragment, ऋणम् of a debt, and the
six Vedic forms of 8.2.61 — each of them a त् where the
grammar owed an न्, which is the mirror image of everything the
run has been doing.

**WHAT THIS MODULE DOES NOT DO.** It says what the निष्ठा's त्
becomes. That the affix is there at all is 3.2.102's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.nalopa_matup import Changed  # noqa: E402

#: This module's stretch.
NISTHA_RUN: Tuple[str, str] = ("8.2.42", "8.2.61")

#: The affix every rule of the run is about.
THE_AFFIX: str = "3.2.102"

#: 8.2.55's four, laid down where no preverb stands in front.
PHULLADI_FOUR: Tuple[str, ...] = (
    "phulla", "kṣība", "kṛśa", "ullāgha")

#: 8.2.56's six, whose निष्ठा takes न् only optionally.
NUDADI_SIX: Tuple[str, ...] = (
    "nud", "vid", "und", "trā", "ghrā", "hrī")

#: 8.2.57's five, which refuse it outright.
DHYADI_FIVE: Tuple[str, ...] = (
    "dhyā", "khyā", "pṝ", "mūrch", "mad")

#: 8.2.61's six Vedic forms, laid down whole.
NASATTADI_SIX: Tuple[str, ...] = (
    "nasatta", "niṣatta", "anutta", "pratūrta", "sūrta",
    "gūrta")


@dataclass(frozen=True)
class Nistha:
    """One rule of 8.2.42–61: what the निष्ठा's त् becomes."""

    sutra: str
    #: `na`, `ka`, `va`, `ma`, `la`, `nipātana`.
    does: str = ""
    #: The roots or ready-made words named outright.
    of: Tuple[str, ...] = ()
    #: The shape of the root instead.
    gana: str = ""
    sense: Tuple[str, ...] = ()
    #: The preverb the root must carry, or must not.
    upasarga: str = ""
    #: True where the sūtra only keeps the न् off.
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


NISTHA_TABLE: Tuple[Nistha, ...] = (
    Nistha(
        "8.2.42", does="na", gana="ra-da-para",
        why="रदाभ्यां निष्ठातो नः पूर्वस्य च दः — after a र् or "
            "a द्, the निष्ठा's त् becomes न् — and a preceding "
            "द् becomes न् with it. After र्: **आस्तीर्णम्, "
            "विस्तीर्णम्, विशीर्णम्, निगीर्णम्, अवगूर्णम्**. "
            "After द्: **भिन्नः, भिन्नवान्; छिन्नः, "
            "छिन्नवान्** — where भिद् and छिद् lose their own "
            "द् to a न् as well, which is what पूर्वस्य च दः "
            "adds and what makes the whole cluster न्न"),
    Nistha(
        "8.2.43", does="na", gana="saṃyoga-ādi-āt-anta-yaṇvat",
        keeps_out="यातः, यातवान् — no cluster at the start; "
                  "च्युतः, प्लुतः — the root does not end in आ",
        why="संयोगादेरातो धातोर्यण्वतः — and after a root that "
            "begins with a CLUSTER, ends in आ, and has a यण् in "
            "it: **प्रद्राणः, प्रद्राणवान्; म्लानः, "
            "म्लानवान्**. All three conditions are tested — "
            "**संयोगादेर् इति किम्? यातः। आत इति किम्? "
            "च्युतः** — and the यण् is what द्रा and म्ला have "
            "and या has not"),
    Nistha(
        "8.2.44", does="na", gana="lvādi",
        why="ल्वादिभ्यः — and after the ल्वादि roots: **लूनः, "
            "लूनवान्; धूनः, धूनवान्; जीनः, जीनवान्**. The class "
            "is bounded by the root list itself — **लूञ् छेदने "
            "इत्येतत्प्रभृति व्री वरणे इति यावत् वृत्करणेन "
            "समापिताः** — from लू to व्री, closed off by the "
            "marker वृ, so the ग्रन्थ and not the grammar says "
            "where it stops"),
    Nistha(
        "8.2.45", does="na", gana="odit",
        why="ओदितश्च — and after a root marked with ओ: from "
            "ओलस्जी **लग्नः, लग्नवान्**; from ओविजी "
            "**उद्विग्नः**; from ओप्यायी **आपीनः**; and from "
            "the ओदित् roots of the fifth class **सूनः, "
            "दूनः**. The marker is put on the root in the list "
            "for this rule and for almost nothing else, which "
            "is what makes it a cheap way of naming a set that "
            "has no shape in common"),
    Nistha(
        "8.2.46", does="na", of=("kṣi",), gana="dīrgha",
        why="क्षियो दीर्घात् — and after क्षि when its vowel is "
            "LONG: **क्षीणाः क्लेशाः; क्षीणो जाल्मः; क्षीणस् "
            "तपस्वी**. The length is given by 6.4.59–61 — "
            "क्षियः, निष्ठायाम् अण्यदर्थे, वा क्रोशदैन्ययोः — "
            "so the rule is stated for the output of three "
            "earlier sūtras and does nothing where they have "
            "not run"),
    Nistha(
        "8.2.47", does="na", of=("śyai",),
        sense=("a-sparśa",),
        keeps_out="शीतं वर्तते, शीतो वायुः — touch is meant, "
                  "and the त् stands",
        why="श्योऽस्पर्शे — and after श्यै where TOUCH is not "
            "meant: **शीनं घृतम्; शीनं मेदः; शीना वसा** — "
            "congealed ghee, fat, marrow. Where the sense is "
            "what the hand feels the त् stays: **शीतं वर्तते; "
            "शीतो वायुः**. And the vṛtti notes that in "
            "शीतम् उदकम् touch is present only as a secondary "
            "sense, which is enough to keep the न् off"),
    Nistha(
        "8.2.48", does="na", of=("añc",), sense=("an-apādāna",),
        keeps_out="उदक्तम् उदकं कूपात् — drawn FROM the well, "
                  "and the source is an अपादान",
        why="अञ्चोऽनपादाने — and after अञ्च् where there is no "
            "अपादान: **समक्नौ शकुनेः पादौ; तस्मात् पशवो "
            "न्यक्नाः**. Water drawn from a well has one — "
            "**उदक्तम् उदकं कूपात्** — and the त् stands. The "
            "vṛtti adds that व्यक्तम् is a different root "
            "altogether, अञ्ज् and not अञ्च्"),
    Nistha(
        "8.2.49", does="na", of=("div",),
        sense=("a-vijigīṣā",),
        keeps_out="द्यूतं वर्तते — gambling, where winning IS "
                  "the point",
        why="दिवोऽविजिगीषायाम् — and after दिव् where no wish "
            "to WIN is meant: **आद्यूनः, परिद्यूनः** — a "
            "wretch, one who is played out. Of gambling the त् "
            "stands, and the vṛtti says exactly why the two "
            "senses part: **विजिगीषया हि तत्र अक्षपातनादि "
            "क्रियते** — the dice are thrown in order to win, "
            "so द्यूत has the wish in it and आद्यून has not"),
    Nistha(
        "8.2.50", does="nipātana", of=("nirvāṇa",),
        sense=("a-vāta",), nipatana=True,
        keeps_out="निर्वातो वातः; निर्वातं वातेन — the wind "
                  "itself, where वात् has its own sense",
        why="निर्वाणोऽवाते — **निर्वाण** is laid down: वा with "
            "निस् in front takes न् for the निष्ठा's त्, "
            "provided the sense is not the WIND's blowing. "
            "**निर्वाणोऽग्निः; निर्वाणः प्रदीपः; निर्वाणो "
            "भिक्षुः** — the fire gone out, the lamp gone out, "
            "and the monk. **अवात इति किम्? निर्वातो वातः**"),
    Nistha(
        "8.2.51", does="ka", of=("śuṣ",),
        why="शुषः कः — after शुष् the निष्ठा's त् becomes क्: "
            "**शुष्कः, शुष्कवान्**. Three sūtras in a row now "
            "give three different sounds to three single roots, "
            "and nothing but the root distinguishes them — "
            "which is why the run reads as a list rather than "
            "as a rule"),
    Nistha(
        "8.2.52", does="va", of=("pac",),
        why="पचो वः — and after पच् it becomes व्: **पक्वः, "
            "पक्ववान्**. The क् of पक्व is 8.2.30's — पच् "
            "before a झल् — so the finished word has both this "
            "rule and that one in it, and neither is visible "
            "in the written stem"),
    Nistha(
        "8.2.53", does="ma", of=("kṣai",),
        why="क्षायो मः — and after क्षै it becomes म्: "
            "**क्षामः, क्षामवान्**. This is the third of the "
            "single-root substitutes and the one the next "
            "sūtra borrows"),
    Nistha(
        "8.2.54", does="ma", of=("styai",), upasarga="pra",
        optional=True, blocks=("8.2.43",),
        why="प्रस्त्योऽन्यतरस्याम् — and after स्त्यै with प्र "
            "in front, OPTIONALLY: **प्रस्तीमः, प्रस्तीमवान्** "
            "beside **प्रस्तीतः, प्रस्तीतवान्**. And the "
            "alternative where the म् does not come is not the "
            "plain form either — **यदा मत्वं नास्ति तदा 8.2.43 "
            "इत्यस्य पूर्वत्रासिद्धत्वात्** the न् of that "
            "rule cannot come, स्त्यै being cluster-initial and "
            "आ-final; so the त् stands and प्रस्तीतः is what is "
            "heard"),
    Nistha(
        "8.2.55", does="nipātana", of=PHULLADI_FOUR,
        upasarga="anupasarga", nipatana=True,
        keeps_out="प्रफुल्लः and the rest — with a preverb in "
                  "front, the निपातन does not hold",
        why="अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः — four words laid "
            "down where no preverb stands in front. **फुल्ल** "
            "is ञिफला with ल् for the निष्ठा's त् — "
            "**उत्वम् इडभावश् च सिद्ध एव** — and the "
            "क्तवतु-form takes it too. The other three are "
            "given whole, and the condition is one all four "
            "share: with a preverb, none of them holds"),
    Nistha(
        "8.2.56", does="na", of=NUDADI_SIX, optional=True,
        why="नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम् — and after "
            "these six the न् comes only OPTIONALLY, so each "
            "has two निष्ठा-forms: **नुन्नः, नुत्तः; विन्नः, "
            "वित्तः; समुन्नः, समुत्तः; त्राणः, त्रातः; "
            "घ्राणः, घ्रातः; ह्रीणः, ह्रीतः**. Two of the "
            "twelve are then taken up again by 8.2.58 and "
            "8.2.59, which lay down वित्त and भित्त in "
            "particular senses"),
    Nistha(
        "8.2.57", refuses=True, of=DHYADI_FIVE,
        blocks=("8.2.42", "8.2.43", "8.2.56"),
        why="न ध्याख्यापॄमूर्छिमदाम् — but for ध्या, ख्या, पॄ, "
            "मूर्छ् and मद् the न् does NOT come: **ध्यातः, "
            "ख्यातः, पूर्तः, मूर्तः, मत्तः**. It is the only "
            "refusal in the run, and it is aimed at three "
            "different rules at once — 8.2.42 would have "
            "reached पॄ and मूर्छ् through their र्, 8.2.43 "
            "ध्या and ख्या, and 8.2.56 would have made मद् "
            "optional"),
    Nistha(
        "8.2.58", does="nipātana", of=("vitta",),
        sense=("bhoga", "pratyaya"), nipatana=True,
        blocks=("8.2.56",),
        why="वित्तो भोगप्रत्यययोः — **वित्त** is laid down "
            "with its त् in two senses: of WEALTH and of "
            "RENOWN. **वित्तम् अस्य बहु** — his wealth is "
            "great, and the vṛtti explains why the word for "
            "enjoying names the thing: **धनं हि भुज्यत इति "
            "भोगोऽभिधीयते**. And **वित्तोऽयं मनुष्यः**, "
            "प्रतीत इत्यर्थः — this man is well known. In any "
            "other sense 8.2.56's option leaves both विन्नः "
            "and वित्तः standing"),
    Nistha(
        "8.2.59", does="nipātana", of=("bhitta",),
        sense=("śakala",), nipatana=True, blocks=("8.2.42",),
        why="भित्तं शकलम् — and **भित्तम्** where a FRAGMENT is "
            "meant: **भित्तं तिष्ठति; भित्तं प्रपतति**. "
            "**शकलपर्यायोऽयम्** — it is simply another word "
            "for a chip, and the vṛtti is careful that the "
            "root is only its etymology: **भिदिक्रिया "
            "शब्दव्युत्पत्तेर् एव निमित्तम्**. Where the "
            "SPLITTING is meant, भिन्नम् stands and 8.2.42 has "
            "its way"),
    Nistha(
        "8.2.60", does="nipātana", of=("ṛṇa",),
        sense=("ādhamarṇya",), nipatana=True,
        blocks=("8.2.42",),
        why="ऋणमाधमर्ण्ये — and **ऋणम्** — ऋ with the निष्ठा's "
            "त् turned न् — in the sense of DEBT: **अधम ऋणे "
            "अधमर्णः**, and the state of being one is "
            "आधमर्ण्य. The निपातन buys a compound besides — "
            "**एतस्माद् एव निपातनात् सप्तम्यन्तेन उत्तरपदेन "
            "समासः** — a locative first member compounded with "
            "what follows, which no ordinary rule allows"),
    Nistha(
        "8.2.61", does="nipātana", of=NASATTADI_SIX,
        chandasi=True, nipatana=True, blocks=("8.2.42",),
        keeps_out="नसन्नम् इति भाषायाम् — outside the Veda the "
                  "ordinary न् comes",
        why="नसत्तनिषत्तानुत्तप्रतूर्तसूर्तगूर्तानि छन्दसि — six "
            "Vedic forms laid down whole: **नसत्तम् अञ्जसा; "
            "निषत्तः; अनुत्तम्; प्रतूर्तम्; सूर्तम्; "
            "गूर्तम्**. The first two are सद् with नञ् and नि "
            "in front, and what is laid down in each is the "
            "ABSENCE of the न् — **नत्वाभावो निपात्यते** — so "
            "the whole sūtra is a list of places where the "
            "run's own rule is set aside. The spoken language "
            "keeps नसन्नम्"),
)


def _reaches(row: Nistha, root: str, gana: str, sense: str,
             upasarga: str, chandasi: bool) -> bool:
    # `of` and `gana` CONJOIN at 8.2.46, which names क्षि AND
    # wants its vowel long. Everywhere else only one of the two
    # is given, so a conjunction costs nothing and an
    # alternative would let a bare `dīrgha` answer for क्षि.
    if row.of and root not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.sense and sense not in row.sense:
        return False
    if row.upasarga and upasarga != row.upasarga:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Nistha) -> int:
    """
    A refusal outweighs the rules it refuses, a named root
    outweighs a shape, and a named sense outweighs both.

    8.2.47 through 8.2.50 are why the sense has to weigh most:
    शीनम् and शीतम्, समक्नौ and उदक्तम्, आद्यूनः and द्यूतम्,
    निर्वाणः and निर्वातः — four pairs that differ in nothing
    but what is meant.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of)
        + 6 * len(row.sense)
        + 4 * bool(row.gana)
        + 3 * bool(row.upasarga)
        + 2 * bool(row.chandasi)
    )


def the_nistha(root: str = "", *, gana: str = "", sense: str = "",
               upasarga: str = "",
               chandasi: bool = False) -> Changed:
    """
    8.2.42–61 — what the निष्ठा's त् becomes.

    Nothing answers by default, and the default is the affix as
    written: कृतः, गतः, भूतः all keep their त्.
    """
    matched = [
        row for row in NISTHA_TABLE
        if _reaches(row, root, gana, sense, upasarga, chandasi)
    ]
    if not matched:
        return Changed(
            "", "", "No rule of 8.2.42-61 is reached, so the "
                    "nistha keeps the t it is written with")
    row = max(matched, key=_how_specific)
    return Changed(row.does, row.sutra, row.why,
                   refuses=row.refuses, optional=row.optional,
                   nipatana=row.nipatana, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Nistha, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in NISTHA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Nistha", "NISTHA_TABLE", "NISTHA_RUN", "THE_AFFIX",
    "PHULLADI_FOUR", "NUDADI_SIX", "DHYADI_FIVE",
    "NASATTADI_SIX",
    "the_nistha", "provisions_for",
]
