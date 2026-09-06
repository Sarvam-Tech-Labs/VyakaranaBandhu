# -*- coding: utf-8 -*-
"""
३.४.८०–११२ — what stands in place of the eighteen, and what is added.

3.4.77 named the ten लकाराः and 3.4.78 gave the eighteen endings that
replace one. From here to the end of the pāda the rules work on THOSE
EIGHTEEN: this ending becomes that one, this letter of an ending goes,
this augment comes in front. It is the mechanical floor under every
finite verb form the project has so far written as a bare string.

The run is held as one table because the rules are one question asked
over and over — *given a लकार and one of its eighteen substitutes,
what happens to it* — and the answer turns on a small, repeating set
of conditions: which लकार (or which CLASS of लकार, टित् or ङित्),
which voice, which person, which root, what precedes.

**Two things are worth watching as it goes.**

The first is an option that will not die. 3.4.83 विदो लटो वा states a
वा; the vṛtti carries it down to 3.4.85, to 3.4.86 and as far as
3.4.98, each time reading it as a व्यवस्थितविभाषा — an option
DISTRIBUTED over cases rather than free in any one of them. Then
3.4.99 says नित्यम् for no other reason than to stop it:
नित्यग्रहणं विकल्पनिवृत्त्यर्थम्. A word carried sixteen sūtras by
inference and cut by one syllable.

The second is a word placed in one rule for the use of another.
3.4.111's एवकार उत्तरार्थः — the एव in शाकटायनस्यैव is there *for what
follows*, and what follows five sūtras later is 3.4.115 लिट् च, where
the vṛtti says the एव carried down is what makes the आर्धधातुक name
REPLACE the सार्वधातुक one instead of joining it. A syllable spent in
one rule and collected in another.

**Two field names here are not the ones the grammar would choose, and
the reason is worth keeping.** The voice of an ending is पद, but this
codebase already asks `pada` for something else — 1.4.14's finished
word, which `sasajuso_ruh` and `kharavasanayoh` take — so it is
`ending_pada` here. And what a rule requires in FRONT would naturally
be `after`, since सिच् comes after the root; but `after` is already
asked in `samprasarana(before, after)` for the sound that FOLLOWS, so
it is `preceded_by`. Both are the same scar this project keeps
reopening: **one name, two questions**. The remedy each time has been
to rename rather than to overload, and each time the cost of not doing
so would have been a silent wrong answer rather than an error.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

from src.astadhyayi.lakara import LAKARA_LIST, TIN

#: The nine परस्मैपद endings of 3.4.78 and the nine आत्मनेपद, split at
#: the point the rule itself divides them — three persons by three
#: numbers, then the same again in the other voice. Read off TIN
#: rather than retyped, so 3.4.82's नव and 3.4.84's पञ्चानाम् are
#: counted from the enumeration and not from a second copy of it.
PARASMAIPADA: Tuple[str, ...] = TIN[:9]
ATMANEPADA: Tuple[str, ...] = TIN[9:]

#: 3.4.82's nine, in the rule's own order. णल् stands twice — third
#: person singular and first person singular — which is why पपाच is
#: both *he cooked* and *I cooked*.
LIT_PARASMAIPADA: Tuple[str, ...] = (
    "ṇal", "atus", "us", "thal", "athus", "a", "ṇal", "va", "ma",
)

#: Which class of लकार a rule holds itself to, read off 3.4.77's own
#: enumeration rather than listed again.
TIT: Tuple[str, ...] = tuple(n for n, m in LAKARA_LIST if m == "ṭit")
NGIT: Tuple[str, ...] = tuple(n for n, m in LAKARA_LIST if m == "ṅit")


@dataclass(frozen=True)
class TinAdesa:
    """One rule about the eighteen: a substitution or an augment."""

    sutra: str
    #: What the rule operates on — an ending of 3.4.78, or a sound
    #: within one (the इ of पचति, the स् of करवावः). Several together
    #: are read यथासंख्यम् against `gives`.
    of: Tuple[str, ...] = ()
    #: What stands in its place, position for position. The empty
    #: string is elision, which is what 3.4.97 to 3.4.100 give.
    gives: Tuple[str, ...] = ()
    #: आदेश or आगम. The distinction is not cosmetic: an आगम attaches
    #: to something and an आदेश replaces it, which is exactly the
    #: ground on which 3.4.107 is allowed to stand beside 3.4.102.
    kind: str = "ādeśa"
    #: The लकार the rule names. Empty means it holds by class instead.
    lakara: Tuple[str, ...] = ()
    #: टित् or ङित् — a rule may reach six लकाराः or four without
    #: naming any of them.
    mark: str = ""
    ending_pada: str = ""
    person: str = ""
    #: A root the rule names: विद्, ब्रू, द्विष्.
    of_root: str = ""
    #: What must precede — सिच्, an अभ्यस्त stem, a long आ, or the
    #: स/व that 3.4.91 wants.
    preceded_by: str = ""
    #: A property conferred on the result rather than a shape given
    #: to it: पित्, अपित्, ङित्, कित्, उदात्त.
    confers: Tuple[str, ...] = ()
    optional: bool = False
    chandasi: bool = False
    sense: str = ""
    #: An आचार्य the rule cites. 3.4.111 and 3.4.112 give a NAMED
    #: INDIVIDUAL where 3.4.18 and 3.4.19 gave schools.
    authority: str = ""
    #: 3.4.84 reaches only the FIRST FIVE of the nine, so the sixth
    #: stands: ब्रूथ, beside आत्थ.
    limit: int = 0
    #: A second thing the same rule does. 3.4.84 gives the endings AND
    #: replaces the root, तत्सन्नियोगेन — the two are one act.
    along_with: str = ""
    why: str = ""


#: Where the vṛtti itself says अपवादः, and of what. Held apart from
#: the rows because it is a relation between rules and not a property
#: of one, and because it can then be tested as a relation: every
#: rule the commentary calls an exception must name what it excepts,
#: and what it excepts must be a rule that could otherwise reach the
#: same ground.
EXCEPTS: Dict[str, Tuple[str, ...]] = {
    "3.4.89": ("3.4.86", "3.4.97"),   # उत्वलोपयोरपवादः
    "3.4.91": ("3.4.90",),            # आमोऽपवादः
    "3.4.93": ("3.4.90",),            # आमोऽपवादः
    "3.4.103": ("3.4.102",),          # सीयुटोऽपवादः
    "3.4.105": ("7.1.3",),            # झोऽन्तापवादः
    "3.4.108": ("7.1.3",),            # झोऽन्तापवादः
}

#: What a rule's own words are there to KEEP OUT, in the vṛtti's
#: कस्माद् न भवति / इति किम् form. Each is a word doing negative
#: work, and the form beside it is what would go wrong.
#:
#: The word is stored AS THE COMMENTARY WRITES IT, not as the
#: sūtra spells it, because those are rarely the same string: a
#: word raised for questioning is joined to इति — पञ्चानामिति —
#: and one carried down by anuvṛtti is joined to इत्येव, which
#: takes परस्मैपदेषु to परस्मैपदेष्वित्येव. 3.4.100 is the second
#: kind: the word it spends is not in its own sūtra at all but
#: borrowed from 3.4.97, three rules back.
KEEPS_OUT: Dict[str, Tuple[str, str]] = {
    "3.4.84": ("पञ्चानामिति", "ब्रूथ — the sixth of the nine, which the "
                            "count leaves standing beside आत्थ"),
    "3.4.97": ("परस्मैपदग्रहण", "इट्, वहि, महिङ् — the three ātmanepada "
                              "endings that also carry an इ"),
    "3.4.98": ("उत्तमग्रहणं", "the other two persons, whose स् stays"),
    "3.4.100": ("परस्मैपदेष्वित्येव", "अपचावहि, अपचामहि"),
    "3.4.104": ("आशिषीति", "वच्यात्, जागृयात् — the same forms without "
                         "the benediction"),
    "3.4.111": ("लङ्ग्रहणेन", "यान्तु, वान्तु — a लोट् behaving as a लङ् by "
                       "3.4.85 is not thereby a लङ्"),
}


TIN_ADESA: Tuple[TinAdesa, ...] = (
    # --- टित इत्येव, carried from 3.4.79 ------------------------------
    TinAdesa(
        "3.4.80", of=("thās",), gives=("se",), mark="ṭit",
        why="थासः से. टित इत्येव — the rule says nothing of which "
            "लकार, and takes six of the ten from 3.4.79's word. "
            "टितो लकारस्य यस्थास् तस्य सेशब्द आदेशो भवति: पचसे, "
            "पेचिषे, पक्तासे, पक्ष्यसे — one substitution shown in "
            "four tenses, which is the vṛtti demonstrating the reach "
            "of a class-word rather than a list"),
    # --- लिट्, and two rules that borrow its endings -------------------
    TinAdesa(
        "3.4.81", of=("ta", "jha"), gives=("eś", "irec"),
        lakara=("liṭ",), ending_pada="ātmanepada",
        why="लिटस्तझयोरेशिरेच्. यथासंख्यम् — त takes एश् and झ takes "
            "इरेच्, position for position by 1.3.10. पेचे, पेचाते, "
            "पेचिरे; लेभे, लेभाते, लेभिरे.\n\n"
            "TWO MARKS, TWO DIFFERENT JOBS, IN ONE RULE. शकारः "
            "सर्वादेशार्थः — the श् so that 1.1.55 अनेकाल्शित् "
            "सर्वस्य makes it replace the WHOLE ending and not just "
            "its last sound; चकारः स्वरार्थः — the च् for the "
            "accent. Neither is part of what is spoken"),
    TinAdesa(
        "3.4.82", of=PARASMAIPADA, gives=LIT_PARASMAIPADA,
        lakara=("liṭ",), ending_pada="parasmaipada",
        why="परस्मैपदानां णलतुसुस्थलथुसणल्वमाः — the nine "
            "परस्मैपद endings of 3.4.78 give way to nine others, "
            "यथासंख्यम्. पपाच, पेचतुः, पेचुः; पेचिथ, पेचथुः, पेच; "
            "पपाच, पेचिव, पेचिम.\n\n"
            "AND ONE OF THE NINE IS GIVEN TWICE. णल् stands at the "
            "third person singular and again at the first, which is "
            "why पपाच is both *he cooked* and *I cooked*, and why "
            "the enumeration has nine members and eight shapes.\n\n"
            "लकारः स्वरार्थः, णकारो वृद्ध्यर्थः — the ल् for the "
            "accent, the ण् so that 7.2.115 अचो ञ्णिति gives वृद्धि: "
            "पच् becomes पाच् because of a letter that is never "
            "heard"),
    TinAdesa(
        "3.4.83", of=PARASMAIPADA, gives=LIT_PARASMAIPADA,
        lakara=("laṭ",), ending_pada="parasmaipada", of_root="vid",
        optional=True,
        why="विदो लटो वा. After विद ज्ञाने the PRESENT endings may "
            "be replaced by the nine 3.4.82 gave the perfect: वेद, "
            "विदतुः, विदुः — a present sense wearing a perfect "
            "shape. न च भवति — वेत्ति, वित्तः, विदन्ति stand "
            "equally.\n\n"
            "AND THE वा OF THIS RULE OUTLIVES IT. The vṛtti carries "
            "it to 3.4.85, to 3.4.86 and as far as 3.4.98, each time "
            "reading it as व्यवस्थितविभाषा — an option distributed "
            "over cases rather than free within one. 3.4.99 then "
            "says नित्यम् for no other purpose than to stop it"),
    TinAdesa(
        "3.4.84", of=PARASMAIPADA[:5], gives=LIT_PARASMAIPADA[:5],
        lakara=("laṭ",), ending_pada="parasmaipada", of_root="brū",
        limit=5, along_with="āh",
        why="ब्रुवः पञ्चानामादित आहो ब्रुवः. After ब्रू the first "
            "FIVE of the nine take the perfect endings, and "
            "तत्सन्नियोगेन the root itself becomes आह्: आह, आहतुः, "
            "आहुः, आत्थ, आहथुः. Not ब्रवीति, ब्रूतः, ब्रुवन्ति.\n\n"
            "पञ्चानामिति किम्? ब्रूथ — the sixth is outside the "
            "count and keeps its own shape, so the paradigm breaks "
            "in the middle. आदित इति किम्? परेषां मा भूत्.\n\n"
            "AND THE ROOT IS NAMED TWICE IN ONE SHORT RULE. ब्रुव "
            "इति पुनर्वचनं स्थान्यर्थम्, परस्मैपदानामेव हि स्यात् — "
            "the first ब्रुवः marks the domain, the second is the "
            "thing REPLACED by आह्. Without the repetition the "
            "substitution would fall on परस्मैपदानाम्, the nearest "
            "genitive to hand"),
    # --- लोट् ---------------------------------------------------------
    TinAdesa(
        "3.4.86", of=("i",), gives=("u",), lakara=("loṭ",),
        why="एरुः. The इ of a लोट् ending becomes उ: पचतु, पचन्तु — "
            "which is the whole difference between *he cooks* and "
            "*let him cook*.\n\n"
            "हिन्योरुत्वप्रतिषेधो वक्तव्यः (म०भा० वा० १): the "
            "vārttika asks that हि and नि be excepted, and the "
            "vṛtti answers twice over — न वोच्चारणसामर्थ्यात्, "
            "those two were given AS हि and नि and the very act of "
            "giving them so protects them; or else the वा of 3.4.83 "
            "still runs, व्यवस्थितविभाषा"),
    TinAdesa(
        "3.4.87", of=("sip",), gives=("hi",), lakara=("loṭ",),
        confers=("apit",),
        why="सेर्ह्यपिच्च. The लोट् सि becomes हि, AND is अपित्: "
            "लुनीहि, पुनीहि, राध्नुहि, तक्ष्णुहि.\n\n"
            "THE SECOND HALF IS A DENIAL, AND OF SOMETHING THE CODE "
            "WOULD OTHERWISE HAVE INHERITED. स्थानिवद्भावात् "
            "पित्त्वं प्राप्तं प्रतिषिध्यते — सिप् carries a प्, so "
            "1.1.56 would hand that mark to हि along with the "
            "position. The rule takes it back, and the fruit is "
            "that लू gives लुनीहि: a पित् substitute would have "
            "blocked the weakening"),
    TinAdesa(
        "3.4.88", of=("hi",), confers=("pit",), optional=True,
        chandasi=True, lakara=("loṭ",),
        why="वा छन्दसि. In the Veda the हि of 3.4.87 is OPTIONALLY "
            "पित् again — अपित्त्वं विकल्प्यते. युयोध्यस्मज्जुहुराणमेनः "
            "(ऋ० १.१८९.१) beside प्रीणाहि, and प्रीणीहि "
            "(काठ०सं० ४०.१२) shows both readings standing in the "
            "transmitted texts. A rule whose whole content is to "
            "loosen the rule before it"),
    TinAdesa(
        "3.4.89", of=("mip",), gives=("ni",), lakara=("loṭ",),
        why="मेर्निः. The लोट् मि becomes नि: पचानि, पठानि. "
            "उत्वलोपयोरपवादः — an exception at once to 3.4.86, "
            "which would have given उ, and to the elision of इ. One "
            "rule excepting two, and the two are three sūtras apart"),
    TinAdesa(
        "3.4.90", of=("e",), gives=("ām",), lakara=("loṭ",),
        why="आमेतः. The ए of a लोट् ending becomes आम्: पचताम्, "
            "पचेताम्, पचन्ताम्. The ए is 3.4.79's — टित आत्मनेपदानां "
            "टेरे put it there — so this rule works on the output of "
            "a rule two pādas' worth of reading earlier and eleven "
            "sūtras back"),
    TinAdesa(
        "3.4.91", of=("e",), gives=("va", "am"), lakara=("loṭ",),
        preceded_by="sa/va",
        why="सवाभ्यां वामौ. After a स and preceded_by a व the लोट् ए "
            "becomes व and अम् respectively, यथासंख्यम्: पचस्व, "
            "पचध्वम्. आमोऽपवादः — 3.4.90 would have given आम् to "
            "both.\n\n"
            "The condition is not a category but a SOUND: what "
            "precedes. थास् had already become से by 3.4.80 and "
            "ध्वम् is the other, so the rule reaches its two cases "
            "through the letters an earlier substitution left"),
    TinAdesa(
        "3.4.92", kind="āgama", gives=("āṭ",), lakara=("loṭ",),
        person="uttama", confers=("pit",),
        why="आडुत्तमस्य पिच्च. The first-person लोट् takes आट् in "
            "front and becomes पित्: करवाणि, करवाव, करवाम; करवै, "
            "करवावहै, करवामहै. The आ is what makes an imperative "
            "*let me* audibly longer than an indicative"),
    TinAdesa(
        "3.4.93", of=("e",), gives=("ai",), lakara=("loṭ",),
        person="uttama",
        why="एत ऐ. In the first person the लोट् ए becomes ऐ: करवै, "
            "करवावहै, करवामहै. आमोऽपवादः, the second rule of this "
            "pāda to except 3.4.90 and the third sūtra away from "
            "the first.\n\n"
            "इह कस्माद् न भवति — पचावेदम्, यजावेदम्? "
            "बहिरङ्गलक्षणत्वाद् गुणस्य: the ए there is made by a "
            "guṇa that depends on the following word, so it is "
            "बहिरङ्ग and 'not yet there' for this rule to work on. "
            "A form saved by the ORDER in which two operations "
            "become available"),
    # --- लेट् ---------------------------------------------------------
    TinAdesa(
        "3.4.94", kind="āgama", gives=("aṭ", "āṭ"), lakara=("leṭ",),
        optional=True,
        why="लेटोऽडाटौ. The Vedic subjunctive takes अट् or आट् in "
            "front, पर्यायेण — by turns, one or the other. "
            "जोषिषत् (ऋ० २.३५.१), तारिषत् (ऋ० १.२५.१२), मन्दिषत् "
            "for the short; पताति दिद्युत् (ऋ० ७.२५.१), उदधिं "
            "च्यावयाति (तै०सं० ३.५.५.२) for the long"),
    TinAdesa(
        "3.4.95", of=("ā",), gives=("ai",), lakara=("leṭ",),
        ending_pada="ātmanepada",
        why="आत ऐ. The आ of a लेट् ending becomes ऐ — "
            "प्रथमपुरुषमध्यमपुरुषात्मनेपदद्विवचनयोः, in the third "
            "and second person ātmanepada DUAL alone: मन्त्रयैते, "
            "मन्त्रयैथे, करवैते, करवैथे.\n\n"
            "आटः कस्माद् न भवति? विधानसामर्थ्यात् — 3.4.94's आट् "
            "would give the same आ, and then this rule would have "
            "nothing of its own to do; the fact that it was stated "
            "at all is the argument that it is not about that आ"),
    TinAdesa(
        "3.4.96", of=("e",), gives=("ai",), lakara=("leṭ",),
        optional=True,
        why="वैतोऽन्यत्र. The लेट् ए optionally becomes ऐ, "
            "ELSEWHERE — सप्ताहानि शासै, अहमेव पशूनामीशै "
            "(काठ०सं० २५.१), मदग्रा एव वो ग्रहा गृह्यान्तै and "
            "मद्देवत्यान्येव वः पात्राण्युच्यान्तै "
            "(तै०सं० ६.४.७.२). And न च भवति — यत्र क्व च ते मनो "
            "दक्षं दधस उत्तरम् (ऋ० ६.१६.१७) keeps the ए.\n\n"
            "AND अन्यत्र LOOKS EXACTLY ONE RULE BACK. "
            "अन्यत्रेत्यनन्तरो विधिरपेक्ष्यते, आत ऐ इत्येतद्विषयं "
            "वर्जयित्वा — 'elsewhere' is not 'anywhere else in the "
            "grammar' but 'outside what the sūtra immediately "
            "before covers'. अन्यत्रेति किम्? मन्त्रयैते, "
            "मन्त्रयैथे — 3.4.95's own examples, which this rule "
            "would otherwise make optional and so undo"),
    TinAdesa(
        "3.4.97", of=("i",), gives=("",), lakara=("leṭ",),
        ending_pada="parasmaipada", optional=True,
        why="इतश्च लोपः परस्मैपदेषु. The इ of a लेट् परस्मैपद ending "
            "is dropped: जोषिषत्, तारिषत्, मन्दिषत्. वानुवृत्तेः "
            "पक्षे श्रवणमपि भवति — 3.4.83's option is still running "
            "sixteen sūtras later, so the इ is also HEARD: पताति "
            "दिद्युत्, उदधिं च्यावयाति.\n\n"
            "परस्मैपदग्रहणमिड्वहिमहिङां मा भूत् — the word "
            "परस्मैपदेषु is there to keep the elision off इट्, "
            "वहि and महिङ्, the three ātmanepada endings that also "
            "carry an इ. A condition stated to protect three items "
            "of an eighteen-item list from a rule about a letter"),
    TinAdesa(
        "3.4.98", of=("s",), gives=("",), lakara=("leṭ",),
        person="uttama", optional=True,
        why="स उत्तमस्य. The स् of a लेट् first-person ending is "
            "OPTIONALLY dropped: करवाव, करवाम beside करवावः, "
            "करवामः. उत्तमग्रहणं पुरुषान्तरे मा भूत्.\n\n"
            "This is the last rule the वा of 3.4.83 reaches. It has "
            "been carried by inference through fifteen sūtras, read "
            "each time as व्यवस्थितविभाषा, and the very next rule "
            "spends a word to end it"),
    # --- ङितः ---------------------------------------------------------
    TinAdesa(
        "3.4.99", of=("s",), gives=("",), mark="ṅit", person="uttama",
        why="नित्यं ङितः. After a ङित् लकार the first-person स् is "
            "ALWAYS dropped: अपचाव, अपचाम.\n\n"
            "नित्यग्रहणं विकल्पनिवृत्त्यर्थम् — the word नित्यम् is "
            "in the rule for one purpose only: TO KILL THE OPTION. "
            "3.4.83's वा has been running by anuvṛtti since fifteen "
            "sūtras back, picking up 3.4.85, 3.4.86, 3.4.97 and "
            "3.4.98 on the way, and one syllable here stops it. An "
            "option carried by inference has to be cancelled "
            "expressly, because nothing else would show that it had "
            "ended.\n\n"
            "Where 3.4.85 turned that same वा into a "
            "व्यवस्थितविभाषा — an option DISTRIBUTED over cases — "
            "this rule refuses even that"),
    TinAdesa(
        "3.4.100", of=("i",), gives=("",), mark="ṅit",
        ending_pada="parasmaipada",
        why="इतश्च. And preceded_by a ङित् लकार the इ goes too, always: "
            "अपचत्, अपाक्षीत्. This is what makes an imperfect "
            "audibly an imperfect — अपचत् against पचति is the "
            "augment at one end and this elision at the other.\n\n"
            "परस्मैपदेष्वित्येव, carried from 3.4.97: अपचावहि, "
            "अपचामहि keep their इ. The same word doing the same "
            "protective work three sūtras on"),
    TinAdesa(
        "3.4.101", of=("tas", "thas", "tha", "mip"),
        gives=("tām", "tam", "ta", "am"), mark="ṅit",
        why="तस्थस्थमिपां तांतंतामः. Four of the eighteen give way "
            "to four others preceded_by a ङित् लकार, यथासंख्यम्: "
            "अपचताम्, अपचतम्, अपचत, अपचम्; अपाक्ताम्, अपाक्तम्, "
            "अपाक्त, अपाक्षम्.\n\n"
            "Note what the four are — the two duals, the second "
            "plural and the first singular. Not a natural class in "
            "the paradigm, and the rule makes no attempt to call "
            "them one: it simply lists them and lists what they "
            "become"),
    # --- लिङ् ---------------------------------------------------------
    TinAdesa(
        "3.4.102", kind="āgama", gives=("sīyuṭ",), lakara=("liṅ",),
        why="लिङः सीयुट्. Every लिङ् ending takes सीयुट् in front: "
            "पचेत, पचेयाताम्, पचेरन्; पक्षीष्ट, पक्षीयास्ताम्, "
            "पक्षीरन्.\n\n"
            "टकारो देशविध्यर्थः, उकार उच्चारणार्थः — the ट् so that "
            "1.1.46 आद्यन्तौ टकितौ puts it at the FRONT, the उ only "
            "to make the augment sayable. Two letters of a "
            "four-letter augment doing no work in the word"),
    TinAdesa(
        "3.4.103", kind="āgama", gives=("yāsuṭ",), lakara=("liṅ",),
        ending_pada="parasmaipada", confers=("udātta", "ṅit"),
        why="यासुट् परस्मैपदेषूदात्तो ङिच्च. In the active a लिङ् "
            "takes यासुट् instead, and it is उदात्त and ङित्: "
            "कुर्यात्, कुर्याताम्, कुर्युः. सीयुटोऽपवादः, and the "
            "accent is stated because आगमानुदात्तत्वे प्राप्ते — an "
            "augment would otherwise be unaccented.\n\n"
            "AND THE ङित् IS SAID REDUNDANTLY, ON PURPOSE. "
            "स्थानिवद्भावादेव लिङादेशस्य ङित्त्वे सिद्धे यासुटो "
            "ङिद्वचनं ज्ञापनार्थम् — the substitute is already ङित् "
            "by standing in a ङित् लकार's place, so saying it again "
            "here TEACHES something else: लकाराश्रयङित्त्वमादेशानां "
            "न भवति, a substitute does not inherit ङित्त्व from the "
            "लकार it replaces. The fruit is अचिनवम्, अकरवम्, which "
            "keep a guṇa that inherited ङित्त्व would have "
            "forbidden.\n\n"
            "ङित्त्वं तु लिङ एव विधीयते, नागमस्य, तत्र "
            "तत्कार्याणां संभवात् — the mark lands on the ENDING "
            "and not on the augment, because only there is there "
            "anything for it to do"),
    TinAdesa(
        "3.4.104", of=("yāsuṭ",), confers=("kit",), lakara=("liṅ",),
        sense="āśis",
        why="किदाशिषि. Where the लिङ् is a benediction, यासुट् is "
            "कित् instead: उच्यात्, उच्यास्ताम्, उच्यासुः; "
            "जागर्यात्, जागर्यास्ताम्, जागर्यासुः. आशिषीति किम्? "
            "वच्यात्, जागृयात् — the same roots without the "
            "blessing.\n\n"
            "प्रत्ययस्यैवेदं कित्त्वम्, नागमस्य, प्रयोजनाभावात् — "
            "again the mark is put on the ending and not on the "
            "augment, and for the same reason: there is nothing for "
            "it to do on an augment.\n\n"
            "ङित्त्वे प्राप्ते कित्त्वं विधीयते. The two marks "
            "mostly agree — गुणवृद्धिप्रतिषेधस्तुल्यः — and the "
            "difference is narrow and real: संप्रसारणं जागर्तेर्गुणे "
            "च विशेषः, which is why वच् gives उच्यात् here and "
            "वच्यात् otherwise"),
    TinAdesa(
        "3.4.105", of=("jha",), gives=("ran",), lakara=("liṅ",),
        why="झस्य रन्. The लिङ् झ becomes रन्: पचेरन्, यजेरन्, "
            "कृषीरन्. झोऽन्तापवादः — 7.1.3 would have made it अन्त, "
            "and this rule reaches it first"),
    TinAdesa(
        "3.4.106", of=("iṭ",), gives=("at",), lakara=("liṅ",),
        why="इटोऽत्. The लिङ् इट् becomes अत्: पचेय, यजेय, कृषीय, "
            "हृषीय.\n\n"
            "TWO SMALL QUESTIONS, BOTH ABOUT WHAT A LETTER IS. "
            "तकारस्येत्संज्ञाप्रतिषेधः प्राप्नोति — 1.3.4 न विभक्तौ "
            "तुस्माः would deny the त् its it-hood, so is the त् "
            "part of the word? नैवायमादेशावयवस्तकारः, मुखसुखार्थ "
            "उच्चार्यते: it is neither, spoken only to make the "
            "substitute pronounceable, so the question does not "
            "arise. And WHICH इट्? आगमस्येटो ग्रहणं न भवति, "
            "अर्थवद्ग्रहणे नानर्थकस्य (परि० १४) — the ENDING इट् of "
            "3.4.78 and not the augment of the same name, because a "
            "term names what has meaning"),
    TinAdesa(
        "3.4.107", kind="āgama", of=("ta", "tha"), gives=("suṭ",),
        lakara=("liṅ",),
        why="सुट् तिथोः. The त and थ of a लिङ् take सुट्: कृषीष्ट, "
            "कृषीयास्ताम्; कृषीष्ठाः, कृषीयास्थाम्. तकार इकार "
            "उच्चारणार्थः.\n\n"
            "AND IT DOES NOT COLLIDE WITH 3.4.102, FOR A REASON "
            "WORTH KEEPING. तकारथकारावागमिनौ, लिङ् तद्विशेषणम्; "
            "सीयुटस्तु लिङेवागमी — the two augments attach to "
            "DIFFERENT THINGS. सुट् attaches to the ending, with "
            "लिङ् only qualifying it; सीयुट् attaches to the लिङ् "
            "itself. तेन भिन्नविषयत्वात् सुटा बाधनं न भवति: two "
            "rules that appear to compete for one word are not "
            "competing at all, because their grounds are different. "
            "Which is exactly the distinction the `kind` field on "
            "these rows is for"),
    TinAdesa(
        "3.4.108", of=("jhi",), gives=("jus",), lakara=("liṅ",),
        why="झेर्जुस्. The लिङ् झि becomes जुस्: पचेयुः, यजेयुः. "
            "झोऽन्तापवादः, the second rule three sūtras apart to "
            "except the same 7.1.3"),
    # --- जुस् beyond the लिङ् ------------------------------------------
    TinAdesa(
        "3.4.109", of=("jhi",), gives=("jus",), mark="ṅit",
        preceded_by="sic/abhyasta/vid",
        why="सिजभ्यस्तविदिभ्यश्च. अलिङर्थ आरम्भः — the rule is "
            "begun for what is NOT a लिङ्. झि becomes जुस् preceded_by "
            "सिच्, preceded_by a reduplicated stem, and preceded_by विद्: "
            "अकार्षुः, अहार्षुः; अबिभयुः, अजिह्रयुः, अजागरुः; "
            "अविदुः.\n\n"
            "अभ्यस्तविदिग्रहणमसिजर्थम् — the second and third items "
            "are named because they are the cases WITHOUT a सिच्, "
            "so the list is not three parallel conditions but one "
            "condition and two exemptions from it"),
    TinAdesa(
        "3.4.110", of=("jhi",), gives=("jus",), mark="ṅit", preceded_by="ā",
        why="आतः. And preceded_by a long आ, with सिच् still carried down: "
            "अदुः, अधुः, अस्थुः. तकारो मुखसुखार्थः.\n\n"
            "पूर्वेणैव सिद्धे नियमार्थं वचनम् — 3.4.109 would "
            "already have covered these, so the rule is stated to "
            "RESTRICT rather than to provide: आत एव सिज्लुगन्ताद्, "
            "नान्यस्मात्. The proof is अभूवन्, where प्रत्ययलक्षणेन "
            "जुस् प्राप्तः प्रतिषिध्यते. And the restriction bites "
            "only on its own kind — तुल्यजातीयापेक्षत्वाद् "
            "नियमस्य — so a सिच् still audible gives जुस् as "
            "before: अकार्षुः, अहार्षुः.\n\n"
            "कथमाभ्यामानन्तर्यम्? सिचो लुकि कृते प्रत्ययलक्षणेन "
            "सिचोऽनन्तरः, श्रुत्या चाकारान्तादिति — the ending "
            "counts as standing next to BOTH, to the सिच् by the "
            "rule that keeps an elided affix's effect and to the आ "
            "by what is actually heard"),
    TinAdesa(
        "3.4.111", of=("jhi",), gives=("jus",), lakara=("laṅ",),
        preceded_by="ā", authority="śākaṭāyana", optional=True,
        why="लङः शाकटायनस्यैव. After a long आ the imperfect झि "
            "becomes जुस् — in the view of the आचार्य Śākaṭāyana: "
            "अयुः, अवुः. अन्येषां मते — अयान्, अवान्.\n\n"
            "A NAMED INDIVIDUAL, where 3.4.18 and 3.4.19 named "
            "SCHOOLS. प्राचाम् and उदीचाम् were the grammarians of "
            "east and north; this is one man, cited by name, twice "
            "in two adjacent rules.\n\n"
            "AND लङ् IS SAID THOUGH ङितः IS ALREADY RUNNING. ननु "
            "ङित इत्यनुवर्तते, अत्र लङेवाकारान्तादनन्तरो ङित् "
            "संभवति नान्यः — no other ङित् can stand there anyway, "
            "so why name it? एवं तर्हि लङेव यो लङ् विहितस्तस्य यथा "
            "स्यात्, लङ्वद्भावेन यस्तस्य मा भूत्: so that only a "
            "लङ् GIVEN as a लङ् is meant, and not a लोट् behaving "
            "as one by 3.4.85. यान्तु, वान्तु — and by the same "
            "argument 3.4.109 does not reach a लोट् either: बिभ्यतु, "
            "जाग्रतु, विदन्तु. A word spent to say that an "
            "अतिदेश does not carry this far.\n\n"
            "एवकार उत्तरार्थः — and the एव is not for this rule at "
            "all but FOR WHAT FOLLOWS. It is collected at 3.4.115, "
            "four sūtras on, where it turns an added name into a "
            "replacing one"),
    TinAdesa(
        "3.4.112", of=("jhi",), gives=("jus",), lakara=("laṅ",),
        of_root="dviṣ", authority="śākaṭāyana", optional=True,
        why="द्विषश्च. And preceded_by द्विष्, on the same authority: "
            "अद्विषुः. अन्येषां मते — अद्विषन्. The named teacher "
            "carries into a second rule, which is how a citation "
            "becomes a section"),
)


@dataclass(frozen=True)
class Substituted:
    """What stands in place of an ending, or what is added to it."""

    gives: str
    by: str
    why: str
    #: आदेश or आगम — see the field of the same name on the row.
    kind: str = "ādeśa"
    #: A property put on the result rather than a shape given to it.
    confers: Tuple[str, ...] = ()
    #: Rules this one excepts, where the vṛtti says अपवादः.
    excepts: Tuple[str, ...] = ()
    optional: bool = False
    #: A second thing the same rule does in one act — 3.4.84's आह्.
    along_with: str = ""
    #: True when the answer differs from what was asked about.
    changed: bool = False


@dataclass(frozen=True)
class NotSubstituted:
    """That no rule of this run touches it."""

    by: str
    why: str
    gives: str = ""


def _mark_of(lakara: str) -> str:
    """टित् or ङित्, read off 3.4.77's enumeration."""
    return dict(LAKARA_LIST).get(lakara, "")


def _reaches(row: TinAdesa, of: str, lakara: str, ending_pada: str,
             person: str, root: str, preceded_by: str, chandasi: bool,
             sense: str) -> bool:
    """Whether one row's stated conditions are all met."""
    if row.of and of not in row.of:
        return False
    if row.lakara and lakara not in row.lakara:
        return False
    if row.mark and _mark_of(lakara) != row.mark:
        return False
    if row.ending_pada and ending_pada and ending_pada != row.ending_pada:
        return False
    if row.ending_pada and not ending_pada:
        return False
    if row.person and person != row.person:
        return False
    if row.of_root and root != row.of_root:
        return False
    if row.preceded_by and preceded_by != row.preceded_by:
        return False
    if row.sense and sense != row.sense:
        return False
    # छन्दसि is a condition and not a default: a rule stated for the
    # Veda does not reach ordinary speech, and one stated without it
    # reaches both.
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: TinAdesa) -> int:
    """
    How narrowly a row states its ground. A named root is the
    narrowest thing any of these rules says — 3.4.83, 3.4.84 and
    3.4.112 each single out one — and a class of लकार the widest.
    """
    return (
        6 * bool(row.of_root)
        + 5 * bool(row.preceded_by)
        + 4 * bool(row.sense)
        + 3 * bool(row.lakara)
        + 3 * bool(row.person)
        + 2 * bool(row.ending_pada)
        + 2 * bool(row.chandasi)
        + 1 * bool(row.mark)
        # A rule that NAMES what it works on states more than
        # one that speaks of the whole class. 3.4.92 gives the
        # first-person लोट् an augment and so names no ending;
        # 3.4.93 names the ए of that same ending. Without this
        # the two tie and the table order decides, which is not
        # a decision. It is 3.4.107's own distinction read as a
        # ranking: तकारथकारावागमिनौ, लिङ् तद्विशेषणम् — one rule
        # is ABOUT the endings and the other only qualified by
        # them.
        + 2 * bool(row.of)
        # And a rule naming whole endings is narrower than one
        # naming a sound within them: 3.4.89 मेर्निः over
        # 3.4.86 एरुः.
        + 1 * (len(row.of) > 0 and all(len(item) > 1 for item in row.of))
    )


def tin_adesha(of: str = "", *, lakara: str = "", ending_pada: str = "",
               person: str = "", root: str = "", preceded_by: str = "",
               chandasi: bool = False, sense: str = "",
               wants: str = "") -> object:
    """
    3.4.80–112 — what stands in place of one of the eighteen endings,
    and what is put in front of it.

    `of` is the ending, or the sound within it the rule works on: the
    इ of पचति, the स् of करवावः. `lakara` is which of the ten, and
    `ending_pada`, `person`, `root` and `preceded_by` are the conditions
    the rules themselves state.

    `wants` picks between two rules that reach one ending — ask for
    "āgama" where both an augment and a substitution are available.
    """
    matched = [
        row for row in TIN_ADESA
        if _reaches(row, of, lakara, ending_pada, person, root, preceded_by,
                    chandasi, sense)
        and (not wants or row.kind == wants)
    ]
    if not matched:
        return NotSubstituted(
            "3.4.80–112",
            "no rule of this run reaches %s%s — the eighteen are "
            "touched only where a sūtra names them, and what is not "
            "named stands as 3.4.78 gave it"
            % (of or "that", " in the %s" % lakara if lakara else ""))
    row = max(matched, key=_how_specific)
    if row.of and row.gives and len(row.gives) == len(row.of):
        gives = row.gives[row.of.index(of)]
    else:
        gives = row.gives[0] if row.gives else ""
    return Substituted(
        gives, row.sutra, row.why,
        kind=row.kind,
        confers=row.confers,
        excepts=EXCEPTS.get(row.sutra, ()),
        optional=row.optional,
        along_with=row.along_with,
        changed=bool(gives) and gives != of,
    )


def behaves_as(lakara: str = "loṭ") -> object:
    """
    3.4.85 लोटो लङ्वत् — the imperative is treated AS an imperfect.

    अतिदेशोयम्. One word borrows a whole rule-set: तामादयस्सलोपश्च,
    3.4.101's four substitutes and 3.4.99's elision come to the लोट्
    because of it. पचताम्, पचतम्, पचत, पचाव, पचाम.

    **And an अतिदेश does not carry everything.** अडाटौ कस्माद् न
    भवतः, तथा झेर्जुसादेशः लङः शाकटायनस्यैव इति — वान्तु, यान्तु?
    The augment अट् and Śākaṭāyana's जुस् do not come, though a real
    लङ् would take them. The vṛtti's answer is that 3.4.83's वा is
    still running: विदो लटो वा इत्यतो वाग्रहणमनुवर्तते, सा च
    व्यवस्थितविभाषा भविष्यति — an option DISTRIBUTED over cases,
    holding in some and not in others.

    3.4.111 then settles the same question from the other end, and by
    a different argument: it says लङ् expressly so that only a लङ्
    given AS a लङ् is meant. Two rules, twenty-six apart, guarding one
    boundary — and the code answers from here, because this is where
    the borrowing is made.
    """
    if lakara != "loṭ":
        return NotSubstituted(
            "3.4.85",
            "%s is not made to behave as another लकार by this rule; "
            "it is stated of the लोट् alone" % (lakara or "that"))
    return Substituted(
        "laṅ", "3.4.85",
        "लोटो लङ्वत् — अतिदेशोयम्, लोटो लङ्वत् कार्यं भवति. "
        "तामादयस्सलोपश्च: the four substitutes of 3.4.101 and the "
        "elision of 3.4.99 reach the imperative because it is made to "
        "count as an imperfect. पचताम्, पचतम्, पचत; पचाव, पचाम.\n\n"
        "AND WHAT DOES NOT CARRY IS THE INTERESTING PART. अडाटौ "
        "कस्माद् न भवतः, तथा झेर्जुसादेशः — the augment and "
        "Śākaṭāyana's जुस् stay behind, or यान्तु and वान्तु would be "
        "*अयुः-shaped. विदो लटो वा इत्यतो वाग्रहणमनुवर्तते, सा च "
        "व्यवस्थितविभाषा भविष्यति: 3.4.83's option, two sūtras back, "
        "is read as DISTRIBUTED — holding for some of the borrowed "
        "operations and not for others.\n\n"
        "3.4.111 comes at the same boundary from the other side, "
        "twenty-six sūtras on, and fences it with a word instead: "
        "लङेव यो लङ् विहितस्तस्य यथा स्यात्, लङ्वद्भावेन यस्तस्य मा "
        "भूत्. The same fact held down twice, by two different kinds "
        "of argument",
        kind="atideśa")


def provisions_for(sutra_id: str) -> Tuple[TinAdesa, ...]:
    """Every row one sūtra states — several, where it gives a list."""
    return tuple(row for row in TIN_ADESA if row.sutra == sutra_id)
