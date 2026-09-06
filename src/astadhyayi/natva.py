# -*- coding: utf-8 -*-
"""
८.४.१–३९ — रषाभ्यां नो णः, and the thirty-eight rules about it.

The last pāda of the work opens on a rule that says almost
everything the whole run has to say: **रषाभ्यां नो णः समानपदे**
— a न् after a र् or a ष् becomes ण्, provided the two stand in
the SAME WORD. आस्तीर्णम्, विशीर्णम्, कुष्णाति, पुष्णाति.

**AND THE VERY NEXT SŪTRA LETS IT REACH ACROSS FIVE THINGS.**
8.4.2 अट्कुप्वाङ्नुम्व्यवायेऽपि — across a vowel (करणम्,
गिरिणा), across a guttural (अर्केण, मूर्खेण), across a labial,
across आङ्, and across a नुम्. Without it not one of the
commonest words in the language would come out right, and with
it the ण् of करणम् is separated from its र् by two sounds.

**AND THEN THE PĀDA SPENDS TWENTY-SEVEN SŪTRAS ON WHERE ELSE.**
Across a compound seam in a NAME (8.4.3 शूर्पणखा), for वन after
ten named first members (8.4.5 प्रवणे), for अह्न after an
अ-final (8.4.7 पूर्वाह्णः), for पान in the name of a country
(8.4.9 क्षीरपाणा उशीनराः), for a णोपदेश root after any preverb
whether compounded or not (8.4.14 प्रणमति, परिणमति), for नि
before seventeen roots (8.4.17 प्रणिगदति), and for the न् of a
कृत् affix after a vowel (8.4.29 प्रयाणम्, प्रमाणम्).

**AND SIX SŪTRAS AT THE END TAKE IT ALL BACK AGAIN.** Not for
eight named roots (8.4.34 प्रभानम्, प्रभवनम्), not after a
WORD-FINAL ष् (8.4.35 निष्पानम्), not of a word-final न् (8.4.37
वृक्षान्, गिरीन्), and not where a whole word stands between
(8.4.38 प्र गां नयामः) — which is 8.4.1's समानपदे said over
again from the other side.

**WHAT THIS MODULE DOES NOT DO.** 8.4.40 onwards — the ष्टुत्व,
the doubling, the जश्त्व and the अ that closes the work — belong
to the next module.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.ru_anunasika import Joined  # noqa: E402

#: This module's stretch, which opens the last pāda.
NATVA_RUN: Tuple[str, str] = ("8.4.1", "8.4.39")

#: 8.4.1's own condition, which 8.4.38 states again as a refusal.
SAMANAPADE: str = "समानपदे"

#: 8.4.2's five, across which the cerebral still reaches.
VYAVAYA_FIVE: Tuple[str, ...] = ("aṭ", "ku", "pu", "āṅ", "num")

#: 8.4.4's six first members, before वन in a name.
PURAGA_SIX: Tuple[str, ...] = (
    "puragā", "miśrakā", "sidhrakā", "śārikā", "koṭarā", "agra")

#: 8.4.5's ten, before which वन takes it name or no name.
PRANIRADI_TEN: Tuple[str, ...] = (
    "pra", "nir", "antar", "śara", "ikṣu", "plakṣa", "āmra",
    "kārṣya", "khadira", "piyūkṣā")

#: 8.4.34's seven, which refuse the cerebral outright. The
#: sūtra's compound names seven and not eight — the first draft
#: of this module called the constant EIGHT and the table said
#: otherwise, which is the second miscount अध्याय ८ has caught.
BHA_BHU_SEVEN: Tuple[str, ...] = (
    "bhā", "bhū", "pū", "kami", "gami", "pyāyī", "vepa")


@dataclass(frozen=True)
class Natva:
    """One rule of 8.4.1–39: a न् made ण्, or kept as न्."""

    sutra: str
    #: `ṇa`. A refusing row leaves it empty.
    does: str = ""
    #: The roots or words named outright.
    of: Tuple[str, ...] = ()
    #: The shape of what the rule reaches.
    gana: str = ""
    #: Where the र् or ष् stands — a preverb, a first member,
    #: or the root itself.
    after: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    sense: Tuple[str, ...] = ()
    #: True where the sūtra only keeps the cerebral off.
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


NATVA_TABLE: Tuple[Natva, ...] = (
    Natva(
        "8.4.1", does="ṇa", gana="ra-ṣa-para-na",
        after="samāna-pada",
        why="रषाभ्यां नो णः समानपदे — a न् after a र् or a ष् "
            "becomes ण्, provided the two stand in the SAME "
            "WORD: **आस्तीर्णम्, विशीर्णम्, अवगूर्णम्** after "
            "the र्, and **कुष्णाति, पुष्णाति, मुष्णाति** after "
            "the ष्. **षग्रहणम् उत्तरार्थम्** — the ष् is named "
            "for the sūtras that follow, since 8.4.41's ष्टुत्व "
            "would have given the cerebral here anyway. This is "
            "the rule the whole pāda opens on and the last "
            "seven sūtras of the run take back"),
    Natva(
        "8.4.2", does="ṇa", gana="ra-ṣa-para-na",
        after="vyavāya", blocks=("8.4.1",),
        why="अट्कुप्वाङ्नुम्व्यवायेऽपि — and it reaches ACROSS "
            "five things: a vowel, a guttural, a labial, आङ् "
            "and a नुम्. Across the vowel — **करणम्, हरणम्, "
            "किरिणा, गिरिणा, कुरुणा, गुरुणा**; across the "
            "guttural — **अर्केण, मूर्खेण, गर्गेण, अर्घेण**. "
            "Without it करणम् would have a plain न्, the र् and "
            "the न् being two sounds apart, and so would half "
            "the instrumentals in the language"),
    Natva(
        "8.4.3", does="ṇa", after="pūrvapada", sense=("saṃjñā",),
        keeps_out="चर्मनासिकः — no name; ऋगयनम् — the sound "
                  "between is a ग, which the sūtra excepts",
        why="पूर्वपदात् संज्ञायामगः — and across a COMPOUND SEAM "
            "where a NAME is being made, unless a ग stands "
            "between: **द्रुणसः, वार्ध्रीणसः, खरणसः, "
            "शूर्पणखा**. 8.4.1's समानपदे would have stopped it "
            "at the seam, so the rule is what lets a compound "
            "count as one word for this purpose — and only for "
            "a name. **केचिद् एतद् नियमार्थं वर्णयन्ति**, some "
            "read it as a restriction instead"),
    Natva(
        "8.4.4", does="ṇa", of=("vana",), after="puragādi",
        sense=("saṃjñā",),
        why="वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः — and "
            "the न् of वन after six named first members, in a "
            "name: **पुरगावणम्, मिश्रकावणम्, सिध्रकावणम्, "
            "शारिकावणम्, कोटरावणम्, अग्रेवणम्**. The condition "
            "of the sūtra before is carried down — "
            "**पूर्वपदात् संज्ञायाम् इति वर्तते** — and what is "
            "new is only the list and the one word it acts on"),
    Natva(
        "8.4.5", does="ṇa", of=("vana",), after="pranirādi",
        why="प्रनिरन्तःशरेक्षुप्लक्षाम्रकार्ष्यखदिरपियूक्षाभ्यो"
            "ऽसंज्ञायामपि — and after ten more, whether a name "
            "is being made or not: **प्रवणे यष्टव्यम्; "
            "निर्वणे प्रतिधीयते; अन्तर्वणे; शरवणम्; इक्षुवणम्; "
            "प्लक्षवणम्; आम्रवणम्**. The असंज्ञायाम् अपि is "
            "what takes the sūtra out of 8.4.3's condition, and "
            "it is the only place in the run where the name is "
            "not wanted"),
    Natva(
        "8.4.6", does="ṇa", of=("vana",),
        after="oṣadhi-vanaspati", optional=True,
        why="विभाषौषधिवनस्पतिभ्यः — and after a word for a HERB "
            "or a TREE, optionally: **दूर्वावणम्, दूर्वावनम्; "
            "मूर्वावणम्; शिरीषवणम्, शिरीषवनम्**. Three sūtras "
            "in a row on one word, each with its own list, and "
            "this the only one of the three that leaves a choice"),
    Natva(
        "8.4.7", does="ṇa", of=("ahna",), after="a-anta-pūrvapada",
        keeps_out="निरह्नः, दुरह्नः — the first member does not "
                  "end in अ",
        why="अह्नोऽदन्तात् — the न् of अह्न after an अ-final "
            "first member: **पूर्वाह्णः, अपराह्णः**. The word "
            "itself is 5.4.88's substitute for अहन्, and the "
            "अदन्तात् is what keeps निरह्नः and दुरह्नः out — "
            "which is why the two halves of a day have a "
            "cerebral and a day counted from something has not"),
    Natva(
        "8.4.8", does="ṇa", of=("vāhana",), after="āhita",
        keeps_out="दाक्षिवाहनम् — the cart belongs to Dākṣi and "
                  "is not loaded with him",
        why="वाहनमाहितात् — and the न् of वाहन after a word for "
            "WHAT IS LOADED on it: **इक्षुवाहणम्, शरवाहणम्, "
            "दर्भवाहणम्**. **वाहने यद् आरोपितम् उह्यते तद् "
            "आहितम् उच्यते**. A cart carrying sugar-cane takes "
            "the cerebral and a cart belonging to someone does "
            "not, which is a distinction of relation and not of "
            "form"),
    Natva(
        "8.4.9", does="ṇa", of=("pāna",), after="pūrvapada",
        sense=("deśa",),
        why="पानं देशे — and the न् of पान where a COUNTRY is "
            "named: **क्षीरं पानं येषां ते क्षीरपाणा "
            "उशीनराः** — the Uśīnaras, whose drink is milk. "
            "**पीयत इति पानम्**, by 3.3.113's कृत्यल्युटो "
            "बहुलम् in the sense of the object. And the vṛtti "
            "notes it is seen of PEOPLE as well as of places"),
    Natva(
        "8.4.10", does="ṇa", of=("pāna",), after="pūrvapada",
        sense=("bhāva", "karaṇa"), optional=True,
        blocks=("8.4.9",),
        why="वा भावकरणयोः — and where पान names the ACT or the "
            "INSTRUMENT, optionally: **क्षीरपाणं वर्तते, "
            "क्षीरपानम्; सुरापाणम्, सुरापानम्; क्षीरपाणः कंसः, "
            "क्षीरपानः**. One word, three senses, three "
            "sūtras — the country compulsorily, the act and the "
            "vessel by choice"),
    Natva(
        "8.4.11", does="ṇa", gana="prātipadika-anta-num-vibhakti",
        after="pūrvapada", optional=True,
        why="प्रातिपदिकान्तनुम्विभक्तिषु च — and a न् that ends "
            "a STEM, or belongs to a नुम्, or belongs to an "
            "ENDING, takes it optionally: **माषवापिणौ, "
            "माषवापिनौ** at a stem's end; **माषवापाणि, "
            "माषवापानि** in a नुम्; and in an ending likewise. "
            "Three quite different places for the same sound, "
            "and one option over all of them"),
    Natva(
        "8.4.12", does="ṇa", gana="prātipadika-anta-num-vibhakti",
        after="ekāc-uttarapada", blocks=("8.4.11",),
        why="एकाजुत्तरपदे णः — but where the SECOND MEMBER has "
            "only one vowel it is compulsory: **वृत्रहणौ, "
            "वृत्रहणः; क्षीरपाणि; सुरापाणि**. What was a choice "
            "one sūtra back is fixed here, and the condition is "
            "as mechanical as any in the work — count the "
            "vowels of the second member"),
    Natva(
        "8.4.13", does="ṇa", gana="prātipadika-anta-num-vibhakti",
        after="kumat-uttarapada", blocks=("8.4.11",),
        why="कुमति च — and where the second member HAS A "
            "GUTTURAL in it: **वस्त्रयुगिणौ, वस्त्रयुगिणः; "
            "स्वर्गकामिणौ; वृषगामिणौ; वस्त्रयुगाणि**. The "
            "guttural is what 8.4.2 had already said the "
            "cerebral reaches across, so the two rules read "
            "each other: one lets it cross a guttural inside a "
            "word and this makes it compulsory across a seam"),
    Natva(
        "8.4.14", does="ṇa", gana="ṇopadeśa", after="upasarga",
        keeps_out="प्रगता नायका अस्माद् देशात् प्रनायकः — the "
                  "प्र is not a preverb but a first member",
        why="उपसर्गादसमासेऽपि णोपदेशस्य — the न् of a root "
            "TAUGHT WITH A ण् becomes ण् after a preverb, "
            "**असमासेऽपि समासेऽपि** — compounded or not: "
            "**प्रणमति, परिणमति; प्रणायकः, परिणायकः**. "
            "**ण उपदेशे यस्य असौ णोपदेशः** — नम् is written णम् "
            "in the root list, and this is what that spelling "
            "is for. Every प्रणाम and परिणाम in the language "
            "comes from here"),
    Natva(
        "8.4.15", does="ṇa", of=("hinu", "mīnā"),
        after="upasarga",
        why="हिनुमीना — and the न् of हिनु and मीना: "
            "**प्रहिणोति, प्रहिणुतः; प्रमीणाति, प्रमीणीतः**. "
            "The two are named in their conjugated shapes and "
            "the rule still reaches them where those shapes "
            "have been altered — **विकृतस्य अपि भवति, "
            "अजादेशस्य स्थानिवत्त्वात्**"),
    Natva(
        "8.4.16", does="ṇa", of=("āni",), before=("loṭ",),
        after="upasarga",
        keeps_out="प्रवपानि मांसानि — आनि is the plural ending "
                  "and not the imperative's",
        why="आनि लोट् — and the न् of आनि where it is the "
            "IMPERATIVE'S ending: **प्रवपाणि, परिवपाणि; "
            "प्रयाणि, परियाणि**. The counter-example is the "
            "same four syllables meaning something else — "
            "प्रवपानि मांसानि, the cut meats — where आनि is a "
            "case ending and no cerebral comes"),
    Natva(
        "8.4.17", does="ṇa", of=("ni",), gana="gadādi",
        after="upasarga",
        why="नेर्गदनदपतपदघुमास्यतिहन्तियातिवातिद्रातिप्साति"
            "वपतिवहतिशाम्यतिचिनोतिदेग्धिषु च — and the न् of "
            "नि before seventeen named roots: **प्रणिगदति, "
            "परिणिगदति; प्रणिनदति; प्रणिपतति; प्रणिपद्यते**. "
            "The preverb whose न् is changed is itself the "
            "second of two, प्र or परि standing in front — "
            "which is why the sūtra needs उपसर्गात् carried "
            "down as well as its own नेः"),
    Natva(
        "8.4.18", does="ṇa", of=("ni",), gana="śeṣa-dhātu",
        after="upasarga", optional=True, blocks=("8.4.17",),
        why="शेषे विभाषाऽकखादावषान्त उपदेशे — and before any "
            "OTHER root, optionally, provided it does not begin "
            "with क् or ख् and does not end in ष् as it is "
            "taught: **प्रणिपचति, प्रनिपचति; प्रणिभिनत्ति, "
            "प्रनिभिनत्ति**. Three conditions on the following "
            "root and one option over them, which is as close "
            "as the pāda comes to a general rule about नि"),
    Natva(
        "8.4.19", does="ṇa", of=("ani",), after="upasarga",
        why="अनितेः — and the न् of अन्: **प्राणिति, "
            "पराणिति**. The root is अन् 'to breathe', and this "
            "is where प्राण and every word made from it gets "
            "its cerebral"),
    Natva(
        "8.4.20", does="ṇa", of=("ani",), after="upasarga",
        gana="pada-anta", blocks=("8.4.37",),
        why="अन्तः — and even at a WORD'S END: **हे प्राण्, हे "
            "पराण्**. **पदान्तस्य इति प्रतिषेधस्य अपवादोऽयम्** "
            "— 8.4.37 will refuse the cerebral to every "
            "word-final न्, and this one word is taken out of "
            "that refusal seventeen sūtras before it is stated"),
    Natva(
        "8.4.21", does="ṇa", of=("ani",), after="upasarga",
        gana="sābhyāsa", blocks=("8.4.19",),
        why="उभौ साभ्यासस्य — and where अन् has been "
            "reduplicated, BOTH of its न् sounds become ण्: "
            "**प्राणिणिषति, प्राणिणत्; पराणिणिषति, "
            "पराणिणत्**. The vṛtti works out why the sūtra is "
            "needed at all — with **पूर्वत्रासिद्धीयम् "
            "अद्विर्वचने** in force, a cerebral already made "
            "would not be copied, so the second ण् has to be "
            "given outright"),
    Natva(
        "8.4.22", does="ṇa", of=("hanti",), gana="at-pūrva",
        after="upasarga",
        keeps_out="प्रघ्नन्ति, परिघ्नन्ति — no अ before the "
                  "न्; प्राघानि — the vowel is long, and the "
                  "तपर shuts it out",
        why="हन्तेरत्पूर्वस्य — and the न् of हन् when a SHORT अ "
            "stands before it: **प्रहण्यते, परिहण्यते; "
            "प्रहणनम्, परिहणनम्**. Both conditions are tested — "
            "प्रघ्नन्ति has lost the अ altogether, and प्राघानि "
            "has a long one, which the तपर keeps out"),
    Natva(
        "8.4.23", does="ṇa", of=("hanti",), after="upasarga",
        before=("va", "ma"), optional=True, blocks=("8.4.22",),
        why="वमोर्वा — and before a व् or a म् it is optional: "
            "**प्रहण्वः, प्रहन्वः; परिहण्वः, परिहन्वः; "
            "प्रहण्मः, प्रहन्मः**. The forms are the dual and "
            "plural of the first person, so one paradigm has "
            "the cerebral fixed in some cells and optional in "
            "two"),
    Natva(
        "8.4.24", does="ṇa", of=("hanti",), gana="at-pūrva",
        after="antar", sense=("a-deśa",),
        keeps_out="अन्तर्हननो देशः — a PLACE, which the sūtra "
                  "excepts",
        why="अन्तरदेशे — and after अन्तर्, provided no PLACE is "
            "meant: **अन्तर्हण्यते; अन्तर्हणनं वर्तते**. A "
            "place called अन्तर्हनन keeps its plain न्. अन्तर् "
            "is not a preverb, which is why हन् needs a rule of "
            "its own here after having had one at 8.4.22"),
    Natva(
        "8.4.25", does="ṇa", of=("ayana",), after="antar",
        sense=("a-deśa",),
        keeps_out="अन्तरयनो देशः — a place again",
        why="अयनं च — and the न् of अयन after अन्तर्, again not "
            "of a place: **अन्तरयणं वर्तते; अन्तरयणं "
            "शोभनम्**. The sense-condition is carried down from "
            "the sūtra before and does the same work on a "
            "different word"),
    Natva(
        "8.4.26", does="ṇa", after="ṛ-anta-avagraha",
        chandasi=True,
        why="छन्दस्यृदवग्रहात् — and in the VEDA after an "
            "ऋ-final first member that the pada text separates: "
            "**नृमणाः, पितृयाणम्** — **अत्र हि नृऽमनाः, "
            "पितृऽयानम् इति ऋकारोऽवगृह्यते**. The condition is "
            "about how the word is RECITED, not about how it is "
            "made, which is a kind of condition found nowhere "
            "else in the work"),
    Natva(
        "8.4.27", does="ṇa", of=("nas",), after="dhātustha-uru-ṣu",
        chandasi=True,
        why="नश्च धातुस्थोरुषुभ्यः — and the न् of नस् after a "
            "cause standing IN THE ROOT, and after उरु and षु, "
            "in the Veda: **अग्ने रक्षा णः; शिक्षा णो अस्मिन्**. "
            "The enclitic नस् is a word of its own, so 8.4.1's "
            "समानपदे could not have reached it — the whole "
            "sūtra is a way round that condition"),
    Natva(
        "8.4.28", does="ṇa", of=("nas",), after="upasarga",
        optional=True,
        keeps_out="प्र नो मुञ्चतम् — where बहुलम् lets it fail",
        why="उपसर्गाद् बहुलम् — and after a preverb, VARIOUSLY: "
            "**प्रणः शूद्रः; प्रणो राजा** — and **न च भवति — "
            "प्र नो मुञ्चतम्**. **बहुलग्रहणाद् भाषायाम् अपि "
            "भवति** — बहुलम् here does something the Vedic "
            "rules around it do not: it carries the rule into "
            "the spoken language, **प्रणसं मुखम्**"),
    Natva(
        "8.4.29", does="ṇa", gana="kṛt-ac-para-na",
        after="upasarga",
        why="कृत्यचः — and a न् inside a कृत् AFFIX, standing "
            "after a vowel: **प्रयाणम्, परियाणम्; प्रमाणम्, "
            "परिमाणम्**. The vṛtti lists the affixes that can "
            "bring one — **अन, मान, अनीय, अनि, इनि** and the "
            "निष्ठा's substitute — which is a way of saying "
            "that कृत् here is a much smaller class than it "
            "sounds. Every प्रमाण and परिमाण comes from this"),
    Natva(
        "8.4.30", does="ṇa", gana="ṇi-kṛt", after="upasarga",
        optional=True, blocks=("8.4.29",),
        why="णेर्विभाषा — but where the कृत् has been added to "
            "a CAUSAL stem it is optional: **प्रयापणम्, "
            "प्रयापनम्; परियापणम्, परियापनम्; प्रयाप्यमाणम्, "
            "प्रयाप्यमानम्**. The णि itself is a ण् and might "
            "have been thought to make the cerebral certain; "
            "the sūtra says the opposite"),
    Natva(
        "8.4.31", does="ṇa", gana="hal-ādi-ik-upadha-kṛt",
        after="upasarga", optional=True, blocks=("8.4.29",),
        why="हलश्चेजुपधात् — and where the root begins with a "
            "consonant and has an इच् in its penult, optionally: "
            "**प्रकोपणम्, प्रकोपनम्; परिकोपणम्, परिकोपनम्**. "
            "Two conditions on the root, and between this sūtra "
            "and the one before, most of what 8.4.29 gave "
            "compulsorily is turned back into a choice"),
    Natva(
        "8.4.32", does="ṇa", gana="ic-ādi-sanum-kṛt",
        after="upasarga", blocks=("8.4.31",),
        why="इजादेः सनुमः — but where the root begins with an "
            "इच् and has a नुम् in it, the cerebral is "
            "compulsory again: **प्रेङ्खणम्, परेङ्खणम्; "
            "प्रेङ्गणम्, परेङ्गणम्; प्रोम्भणम्**. **हल इति "
            "वर्तते। तेन इह सामर्थ्यात् तदन्तविधिः** — the "
            "consonant-final condition is carried down and read "
            "of the root's END"),
    Natva(
        "8.4.33", does="ṇa", of=("niṃs", "nikṣ", "nind"),
        after="upasarga", optional=True,
        why="वा निंसनिक्षनिन्दाम् — and the न् of निंस्, निक्ष् "
            "and निन्द् optionally: **प्रणिंसनम्, प्रनिंसनम्; "
            "प्रणिक्षणम्, प्रनिक्षणम्; प्रणिन्दनम्, "
            "प्रनिन्दनम्**. All three are णोपदेश roots, so "
            "8.4.14 would have made the cerebral compulsory — "
            "and this is what makes it a choice"),
    Natva(
        "8.4.34", refuses=True, of=BHA_BHU_SEVEN,
        after="upasarga", blocks=("8.4.29",),
        why="न भाभूपूकमिगमिप्यायीवेपाम् — and here the refusals "
            "begin: the कृत्'s न् does NOT become ण् after "
            "these seven: **प्रभानम्, परिभानम्; प्रभवनम्, "
            "परिभवनम्; प्रपवनम्, परिपवनम्**. Six sūtras of "
            "refusal close the run, and this is the only one of "
            "them that names roots"),
    Natva(
        "8.4.35", refuses=True, gana="ṣa-pada-anta-para",
        blocks=("8.4.1",),
        keeps_out="निर्णयः — the cause is a र् and not a ष्; "
                  "कुष्णाति — the ष् does not end a word",
        why="षात् पदान्तात् — nor after a ष् that ENDS A WORD: "
            "**निष्पानम्, दुष्पानम्, सर्पिष्पानम्, "
            "यजुष्पानम्**. Both words are tested, and the "
            "compound is read as a locative — **पदे अन्तः "
            "पदान्त इति सप्तमीसमासोऽयम्** — so what is refused "
            "is the ष् standing at the end of a word and not a "
            "word ending in ष्"),
    Natva(
        "8.4.36", refuses=True, of=("naś",), gana="ṣa-anta",
        blocks=("8.4.14",),
        keeps_out="प्रणश्यति, परिणश्यति — the root is not in "
                  "its ष्-final shape there",
        why="नशेः षान्तस्य — nor of नश् IN ITS ष्-FINAL SHAPE: "
            "**प्रनष्टः, परिनष्टः**. And अन्तग्रहण widens it to "
            "what was once ष्-final and no longer is — "
            "**षान्तभूतपूर्वमात्रस्य अपि यथा स्यात्** — for "
            "प्रनङ्क्ष्यति, where the ष् has already become "
            "something else"),
    Natva(
        "8.4.37", refuses=True, gana="pada-anta-na",
        blocks=("8.4.1", "8.4.2"),
        why="पदान्तस्य — nor of a न् that ENDS a word: "
            "**वृक्षान्, प्लक्षान्, अरीन्, गिरीन्**. This is "
            "the widest of the six refusals and the one that "
            "keeps every accusative plural in the language from "
            "coming out with a cerebral. 8.4.20 had taken one "
            "word out of it seventeen sūtras earlier"),
    Natva(
        "8.4.38", refuses=True, gana="pada-vyavāya",
        blocks=("8.4.1", "8.4.2"),
        why="पदव्यवायेऽपि — nor where a WHOLE WORD stands "
            "between the र् and the न्: **माषकुम्भवापेन; "
            "चतुरङ्गयोगेन; प्रावनद्धम्; प्र गां नयामः; परि गां "
            "नयामः**. This is 8.4.1's समानपदे said again from "
            "the other side — the first sūtra of the pāda "
            "wanted one word and the thirty-eighth refuses "
            "where there are two"),
    Natva(
        "8.4.39", refuses=True, gana="kṣubhnādi",
        blocks=("8.4.1", "8.4.3"),
        why="क्षुभ्नादिषु च — nor in the क्षुभ्नादि class: "
            "**क्षुभ्नाति; नृनमनः**. The refusal reaches the "
            "altered shapes too — **अजादेशस्य स्थानिवद्भावाद् "
            "इह अपि प्रतिषेधो भवति — क्षुभ्नीतः, क्षुभ्नन्ति** "
            "— and the second example is one 8.4.3 would have "
            "reached across a compound seam. With it the "
            "cerebral न् is finished and the pāda turns to the "
            "cerebral of everything else"),
)


def _reaches(row: Natva, root: str, gana: str, after: str,
             before: str, sense: str, chandasi: bool) -> bool:
    # `of` and `gana` CONJOIN: 8.4.22 names हन् AND wants a
    # short अ before its न्; 8.4.36 names नश् AND wants its
    # ष्-final shape.
    if row.of and root not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.after and after != row.after:
        return False
    if row.before and before not in row.before:
        return False
    if row.sense and sense not in row.sense:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Natva) -> int:
    """
    A refusal outweighs the rules it refuses, a named word
    outweighs a shape, and a named sense outweighs both.

    8.4.9 against 8.4.10 is why the sense has to weigh: पान
    takes the cerebral compulsorily of a country and optionally
    of the act, and the two rules differ in nothing else.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of)
        + 6 * len(row.sense)
        + 4 * bool(row.gana)
        + 4 * bool(row.after)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


def the_cerebral_n(root: str = "", *, gana: str = "",
                   after: str = "", before: str = "",
                   sense: str = "",
                   chandasi: bool = False) -> Joined:
    """
    8.4.1–39 — the न् that becomes ण्, and where it does not.

    Nothing answers by default, and the answer is the same
    `Joined` the pāda before gives, since 8.3 and 8.4 settle
    one question between them: what two sounds do side by side.
    """
    matched = [
        row for row in NATVA_TABLE
        if _reaches(row, root, gana, after, before, sense, chandasi)
    ]
    if not matched:
        return Joined(
            "", "", "No rule of 8.4.1-39 is reached, so the n "
                    "stands as it is")
    row = max(matched, key=_how_specific)
    return Joined(row.does, row.sutra, row.why,
                  refuses=row.refuses,
                  optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Natva, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in NATVA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Natva", "NATVA_TABLE", "NATVA_RUN", "SAMANAPADE",
    "VYAVAYA_FIVE", "PURAGA_SIX", "PRANIRADI_TEN",
    "BHA_BHU_SEVEN",
    "the_cerebral_n", "provisions_for",
]
