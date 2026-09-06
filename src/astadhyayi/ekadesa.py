# -*- coding: utf-8 -*-
"""
६.१.८४–११४ — एकः पूर्वपरयोः, one substitute standing for two sounds.

**एकः पूर्वपरयोः.** From 6.1.84 to 6.1.111, whatever is substituted
stands in the room of the EARLIER sound and the LATER one together.
Not of one of them, and not of each separately: खट्वा + इन्द्रः gives
खट्वेन्द्रः, and the ए is the single replacement of the आ and the इ
at once.

**AND BOTH WORDS IN THE HEADING ARE DOING WORK.** The vṛtti says what
each buys. **पूर्वपरग्रहणं द्वयोरपि युगपदादेशप्रतिपत्त्यर्थम्, एकस्यैव
हि स्यात्, नोभे सप्तमीपञ्चम्यौ युगपत् प्रकल्पिके भवत इति** — without
पूर्वपर, आद् गुणः has आत् in the ablative and अचि in the locative, and
1.1.67 and 1.1.66 would send the substitution to opposite sides. And
**एकग्रहणं पृथगादेशनिवृत्त्यर्थम्, स्थानिभेदाद्धि भिन्नादिषु नत्ववद्
द्वावादेशौ स्याताम्** — without एक, two different substitutes would
answer to two different स्थानिन्, as the न् of नत्व does.

**WHAT THE SECTION IS ARRANGED AS.** A chain of exceptions, each
displacing the one before it. 6.1.87 gives guṇa; 6.1.88 gives vṛddhi
instead where the second sound is an एच्; 6.1.94 gives the LATER
FORM instead of that vṛddhi; and 6.1.89 gives the vṛddhi back for
three cases — but against 6.1.94 and not against 6.1.95, on the
maxim **पुरस्तादपवादा अनन्तरान् विधीन् बाधन्ते नोत्तरान्**, that an
exception stated earlier displaces only what stands nearest.

**WHAT THIS MODULE DOES NOT DO.** It names the rule and the KIND of
substitute — guṇa, vṛddhi, the earlier form, the later form, the long
homogeneous vowel. Which actual sound results is 1.1.50's
स्थानेऽन्तरतमः and the guṇa/vṛddhi tables, and `adesa` holds those.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where एकः पूर्वपरयोः governs, on the vṛtti's own bound at 6.1.84:
#: **ख्यत्यात् परस्य इति प्रागेतस्मात् सूत्रात्** — everything up to
#: but not including 6.1.112.
EKADESA_RUN: Tuple[str, str] = ("6.1.84", "6.1.111")
EKADESA_MARKER: str = "6.1.112"

#: What each of the heading's two words buys, read off its vṛtti.
#: Neither is decoration: drop either and the section says something
#: different.
WHY_BOTH_WORDS: Tuple[str, str] = (
    "पूर्वपरग्रहणं द्वयोरपि युगपदादेशप्रतिपत्त्यर्थम्",
    "एकग्रहणं पृथगादेशनिवृत्त्यर्थम्",
)

#: The maxim that settles which rule an exception displaces, cited at
#: 6.1.89 and again at 6.1.102. An exception stated EARLIER reaches
#: only what stands nearest to it, never past that to a later rule.
PURASTAT: str = (
    "पुरस्तादपवादा अनन्तरान् विधीन् बाधन्ते नोत्तरान्"
)


@dataclass(frozen=True)
class Ekadesa:
    """One rule of 6.1.84–114: two sounds, and what stands for both."""

    sutra: str
    #: What kind of single substitute: guṇa, vṛddhi, pararūpa,
    #: pūrvarūpa, pūrvasavarṇa, or a named sound.
    does: str = ""
    #: The words the rule names outright.
    of: Tuple[str, ...] = ()
    #: What the EARLIER sound must be.
    after: str = ""
    #: What the LATER sound or affix must be.
    before: str = ""
    #: A second `before` the same rule reaches.
    also_before: str = ""
    #: What the derived form must mean or be — पुंस् at 6.1.103.
    result: str = ""
    #: The sound put in, where the rule names one rather than a kind.
    gives: str = ""
    #: The ācārya whose opinion the rule reports. Four are named in
    #: this pāda and only one of them is what makes his rule
    #: optional; for the rest the vṛtti says **पूजार्थम्**.
    teacher: str = ""
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    #: True where the row IS the heading.
    heading: bool = False
    #: The rule this one displaces, by ITS own number.
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


EKADESA_TABLE: Tuple[Ekadesa, ...] = (
    Ekadesa(
        "6.1.84", heading=True,
        why="एकः पूर्वपरयोः — **अधिकारोऽयम्। ख्यत्यात् परस्य इति "
            "प्रागेतस्मात् सूत्रादित उत्तरं यद् वक्ष्यामस्तत्र "
            "पूर्वस्य परस्य द्वयोरपि स्थान एकादेशो भवति** — from "
            "here to 6.1.111, one substitute stands in the room of "
            "the earlier sound and the later one together. "
            "**खट्वेन्द्रः**: the ए replaces the आ and the इ at "
            "once.\\n\\n"
            "**AND पूर्वपर IS SAID SO THAT THE SUBSTITUTION HAS ONE "
            "PLACE AND NOT TWO.** **पूर्वपरग्रहणं द्वयोरपि "
            "युगपदादेशप्रतिपत्त्यर्थम्, एकस्यैव हि स्यात्, नोभे "
            "सप्तमीपञ्चम्यौ युगपत् प्रकल्पिके भवत इति** — 6.1.87 has "
            "आत् in the ablative and अचि in the locative; 1.1.67 "
            "would send the substitution to what FOLLOWS the आ and "
            "1.1.66 to what PRECEDES the vowel, and the two cases "
            "cannot both take effect. The word makes them one "
            "place.\\n\\n"
            "**AND एक IS SAID SO THAT THERE IS ONE SUBSTITUTE AND "
            "NOT TWO.** **एकग्रहणं पृथगादेशनिवृत्त्यर्थम्, "
            "स्थानिभेदाद्धि भिन्नादिषु नत्ववद् द्वावादेशौ स्याताम्** "
            "— two different स्थानिन् would otherwise take two "
            "different substitutes, as they do under the न् rules. "
            "Two words, two failures they prevent, and the "
            "commentary states each"),
    Ekadesa(
        "6.1.87", does="guṇa", after="a-ā", before="ac",
        keeps_out="वृक्षः — 6.1.97's पररूप takes it, being the "
                  "nearer exception",
        why="आद् गुणः — where अ or आ stands before a vowel, one guṇa "
            "replaces both: **तवेदम्, खट्वेन्द्रः, मालेन्द्रः; "
            "तवोदकम्, खट्वोदकम्; तवर्श्यः, खट्वर्श्यः; तवल्कारः, "
            "खट्वल्कारः**.\\n\\n"
            "**AND THE ऌ CASE NEEDS 1.1.51 TO FINISH IT.** "
            "**ऌकारस्य स्थाने योऽण् तस्य लपरत्वमिष्यते** — the guṇa "
            "of ऌ is अ, and 1.1.51's उरण् रपरः is read as putting a "
            "ल् after it, exactly as it puts a र् after the अ that "
            "replaces ऋ. **तवल्कारः**, and not *तवकारः.\\n\\n"
            "**AND THIS IS THE RULE THE WHOLE SECTION IS AN "
            "EXCEPTION CHAIN AGAINST.** 6.1.88, 6.1.91, 6.1.94, "
            "6.1.96, 6.1.97 and 6.1.102 each displace it in their "
            "own case, and 6.1.89 displaces one of THOSE"),
    Ekadesa(
        "6.1.88", does="vṛddhi", after="a-ā", before="ec",
        blocks=("6.1.87",),
        why="वृद्धिरेचि — where the later sound is an एच्, vṛddhi "
            "instead of guṇa: **ब्रह्मैडका, खट्वैडका; ब्रह्मौदनः, "
            "खट्वौदनः; ब्रह्मौपगवः, खट्वौपगवः**. The vṛtti names "
            "the relation rather than leaving it to be worked out — "
            "**आद्गुणस्यापवादः**"),
    Ekadesa(
        "6.1.89", does="vṛddhi", after="a-ā", before="eti-edhati-ūṭh",
        blocks=("6.1.94",),
        keeps_out="उपेतः — the root has not become ए there, and एचि "
                  "qualifies एति alone",
        why="एत्येधत्यूठ्सु — vṛddhi before the ए of एति, the एध् of "
            "एधति, and the ऊठ्: **उपैति, उपैषि, उपैमि; उपैधते, "
            "प्रैधते; प्रष्ठौहः, प्रष्ठौहा**.\\n\\n"
            "**AND THE एच् OF THE RULE BEFORE QUALIFIES ONE OF THE "
            "THREE ONLY.** **तदेतदेज्ग्रहणम् एतेरेव विशेषणम्, न "
            "पुनरेधतेः, अव्यभिचारादूठश्चासंभवात्** — एधति always has "
            "its diphthong and ऊठ् can never have one, so only एति "
            "needs saying that its ए is one.\\n\\n"
            "**AND WHICH RULE IT IS AN EXCEPTION TO IS SETTLED BY A "
            "MAXIM.** For the ऊठ् it displaces 6.1.87; for the other "
            "two it displaces 6.1.94's पररूप — but NOT 6.1.95's, "
            "though that is a पररूप too: **येन नाप्राप्ते यो "
            "विधिरारभ्यते स तस्य बाधको भवति**, or "
            "**पुरस्तादपवादा अनन्तरान् विधीन् बाधन्ते नोत्तरान्**. "
            "An exception stated earlier reaches only what stands "
            "nearest. So **उप आ इत** is **उपेतः** and not *उपैतः*, "
            "the later rule standing"),
    Ekadesa(
        "6.1.90", does="vṛddhi", after="āṭ", before="ac",
        blocks=("6.1.95", "6.1.96"),
        why="आटश्च — after the augment आट्, vṛddhi before any vowel: "
            "**ऐक्षिष्ट, ऐक्षत, ऐक्षिष्यत; औभीत्, औब्जीत्**. "
            "**एचीति निवृत्तम्** — the एच् of 6.1.88 has "
            "lapsed.\\n\\n"
            "**AND THE च IS WHAT MAKES IT REACH FURTHER.** "
            "**चकारोऽधिकविधानार्थः, उसि, ओमाङोश्च इति पररूपबाधनार्थः** "
            "— the word is there to displace the पररूप of 6.1.95 and "
            "6.1.96 as well as the guṇa: **औस्रीयत्, औङ्कारीयत्, "
            "औढीयत्**"),
    Ekadesa(
        "6.1.91", does="vṛddhi", after="upasarga-a", before="ṛ-dhātu",
        blocks=("6.1.87",),
        keeps_out="खट्वर्च्छति, प्रर्च्छको देशः — प्र there is not a "
                  "उपसर्ग but a गति; उपेतः — the root does not begin "
                  "on ऋ",
        why="उपसर्गादृति धातौ — after a preverb ending in अ or आ and "
            "before a root beginning with ऋ, vṛddhi: **उपार्च्छति, "
            "प्रार्च्छति, उपार्ध्नोति**. **आद्गुणापवादः**.\\n\\n"
            "**AND उपसर्ग IS A RELATIVE NAME, NOT A LIST.** "
            "**यत्क्रियायुक्ताः प्रादयस्तं प्रति गत्युपसर्गसंज्ञकाः** "
            "— प्र is a preverb only with respect to the action it "
            "is joined to. In **प्रर्च्छको देशः** it is not, and the "
            "rule does not reach.\\n\\n"
            "**AND धातु IS SAID THOUGH उपसर्ग IMPLIES IT.** "
            "**उपसर्गग्रहणादेव धातुग्रहणे सिद्धे धातुग्रहणं "
            "शाकलनिवृत्त्यर्थम्** — the word is put in to keep "
            "6.1.128's ऋत्यकः from offering Śākalya's non-junction "
            "here.\\n\\n"
            "**AND THE त् IN ऋति IS FOR THE RULE AFTER.** "
            "**तपरकरणं किम्? उप ॠकारीयति उपर्कारीयति** — only a "
            "SHORT ऋ, and no ordinary root begins with a long one, "
            "so the restriction only bites on the denominatives "
            "6.1.92 will take"),
    Ekadesa(
        "6.1.92", does="vṛddhi", after="upasarga-a",
        before="ṛ-sup-dhātu", teacher="Āpiśali", optional=True,
        why="वा सुप्यापिशलेः — where the ऋ-initial root is a "
            "denominative made from a सुबन्त, the vṛddhi is a "
            "choice, **आपिशलेराचार्यस्य मतेन**: **उपार्षभीयति, "
            "उपर्षभीयति; उपाल्कारीयति, उपल्कारीयति**.\\n\\n"
            "**AND THE NAME IS FOR HONOUR AND NOTHING ELSE.** "
            "**आपिशलिग्रहणं पूजार्थम्। वेति ह्युच्यत एव** — the वा "
            "already makes it optional, and naming the teacher adds "
            "no force. The first of four ācāryas named in this pāda, "
            "and three of the four are named for this reason.\\n\\n"
            "**AND ऌ IS READ IN WITH ऋ.** "
            "**ऋकारऌकारयोः सावर्ण्यविधिः इति ऋतीति ऌकारोऽपि "
            "गृह्यते** — which is what reaches उपल्कारीयति"),
    Ekadesa(
        "6.1.93", does="ā", after="o", before="am-śas", gives="ā",
        blocks=("7.1.90",),
        keeps_out="अचिनवम्, असुनवम् — that अम् is a tense-ending and "
                  "not the accusative",
        why="ओतोऽम्शसोः — where a stem ending in ओ meets the "
            "accusative अम् or शस्, आ stands for both: **गां पश्य, "
            "गाः पश्य; द्यां पश्य, द्याः पश्य**.\\n\\n"
            "**AND IT DISPLACES A VṚDDHI THAT HAS NOT BEEN STATED "
            "YET.** 7.1.90 makes the सर्वनामस्थान endings णित् after "
            "these stems, which would give vṛddhi. **तेन नाप्राप्तायां "
            "वृद्धौ अयमाकारो विधीयमानस्तां बाधते** — the substitute "
            "is laid down against a vṛddhi that would otherwise "
            "reach, and so displaces it.\\n\\n"
            "**AND WHICH अम् IS MEANT IS SETTLED BY ITS COMPANY.** "
            "**अमिति द्वितीयैकवचनं गृह्यते, शसा साहचर्यात्, सुपीति "
            "चाधिकारात्** — it keeps company with शस् and the सुप् "
            "heading is carrying, so the tense-ending अम् is not "
            "reached"),
    Ekadesa(
        "6.1.94", does="pararūpa", after="upasarga-a",
        before="eṅ-dhātu", blocks=("6.1.88",),
        why="एङि पररूपम् — after a preverb in अ or आ and before a "
            "root beginning with ए or ओ, the LATER form stands for "
            "both: **उपेलयति, प्रेलयति; उपोषति, प्रोषति**. "
            "**वृद्धिरेचि इत्यस्यापवादः**.\\n\\n"
            "**AND FOUR SUPPLEMENTS EXTEND IT WELL BEYOND ROOTS.** "
            "**शकन्ध्वादिषु पररूपं वक्तव्यम्** — **शकन्धुः, कुलटा**; "
            "**सीमन्तः केशेषु**, and where the sense is not hair, "
            "**सीमान्तः**. **एवे चानियोगे** — **इहेव, अद्येव**, but "
            "**इहैव भव** where the sense IS command. "
            "**ओत्वोष्ठयोः समासे वा** — **स्थूलोतुः, स्थूलौतुः; "
            "बिम्बोष्ठी, बिम्बौष्ठी**, and outside a compound the "
            "vṛddhi is fixed: **देवदत्तौष्ठं पश्य**. And "
            "**एमन्नादिषु छन्दसि** — **अपां त्वेमन्, अपां "
            "त्वोद्मन्**"),
    Ekadesa(
        "6.1.95", does="pararūpa", after="a-ā", before="om-āṅ",
        blocks=("6.1.88", "6.1.101"),
        why="ओमाङोश्च — before ओम् and before the preverb आङ्, the "
            "later form again: **कोमित्यवोचत्, योमित्यवोचत्; "
            "अद्योढा, कदोढा, तदोढा**.\\n\\n"
            "**AND IT DISPLACES TWO DIFFERENT RULES.** Against the "
            "vṛddhi of 6.1.88, and against the lengthening of 6.1.101 "
            "where the two are savarṇa: **आ ऋश्यात् अर्श्यात्, अद्य "
            "अर्श्यात् अद्यर्श्यात्** — one substitute, two "
            "उत्सर्ग.\\n\\n"
            "**AND IT IS THE RULE 6.1.89 CANNOT REACH.** The maxim "
            "about a forward-stated exception is stated at 6.1.89 "
            "precisely so that this rule stands, and उपेतः is not "
            "*उपैतः*"),
    Ekadesa(
        "6.1.96", does="pararūpa", after="a-apadānta", before="us",
        blocks=("6.1.87",),
        keeps_out="कोस्रा, कोषिता — the अ ends a पद there; चक्रुः, "
                  "अबिभयुः — the earlier sound is not अ",
        why="उस्यपदान्तात् — before the ending उस्, where the अ does "
            "not end a पद, the later form: **भिन्द्युः, छिन्द्युः; "
            "अदुः, अयुः**. **आद्गुणापवादः**.\\n\\n"
            "**AND अपदान्तात् IS ARGUED TO BE IDLE, AND THEN "
            "SAVED.** The affix उस् can never follow a पद at "
            "all — it is added to a stem that has not yet become "
            "one — so the word looks empty. Read उस् as the SOUNDS "
            "उस् rather than the affix and it earns its place: "
            "**का उस्रा कोस्रा, का उषिता कोषिता**, where the "
            "पदान्त अ takes the guṇa instead"),
    Ekadesa(
        "6.1.98", does="pararūpa", after="avyakta-at", before="iti",
        keeps_out="जगदिति — जगत् imitates no sound; मरडिति — the "
                  "final is not अत्; पटदत्र — इति does not follow",
        why="अव्यक्तानुकरणस्यात इतौ — where a word imitating an "
            "inarticulate sound ends in अत् and इति follows, the "
            "later form stands: **पटिति, घटिति, झटिति, "
            "छमिति**.\\n\\n"
            "**AND THE VṚTTI DEFINES THE TWO HALVES OF THE TERM.** "
            "**अव्यक्तम् अपरिस्फुटवर्णम्, तदनुकरणं परिस्फुटवर्णमेव। "
            "केनचित् सादृश्येन तदव्यक्तमनुकरोति** — the sound "
            "imitated has no distinct letters and the imitation has "
            "nothing else. The word is articulate speech standing "
            "for what is not.\\n\\n"
            "**AND A SUPPLEMENT KEEPS THE ONE-SYLLABLE CASES OUT.** "
            "**अनेकाच इति वक्तव्यम्** — **श्रदिति** stays, and "
            "**घटदिति** in the verse is read as a द-final imitation "
            "rather than as this rule failing"),
    Ekadesa(
        "6.1.99", after="āmreḍita-at", before="iti", refuses=True,
        optional=True, blocks=("6.1.98",),
        keeps_out="पटत्पटिति करोति — there the whole doubled thing "
                  "imitates the sound, and 6.1.98 holds",
        why="नाम्रेडितस्यान्त्यस्य तु वा — where the imitation has "
            "been doubled by 8.1.4, the later form does NOT stand "
            "for its अत् — and for the final त् alone it stands "
            "optionally: **पटत्पटदिति** beside **पटत्पटेति "
            "करोति**.\\n\\n"
            "**AND WHAT THE DOUBLED WORD IS TAKEN TO IMITATE DECIDES "
            "IT.** **यदा तु समुदायानुकरणं तदा भवत्येव पूर्वेण "
            "पररूपम् — पटत्पटिति करोति** — read the pair as one "
            "imitation and the rule before applies untouched. One "
            "form, two analyses, and both are attested"),
    Ekadesa(
        "6.1.100", does="pararūpa", after="āmreḍita", before="ḍāc",
        blocks=("6.1.99",),
        why="नित्यमाम्रेडिते डाचि — with the affix डाच् after the "
            "doubled imitation, the later form is FIXED, and now for "
            "the final त् and the following consonant: "
            "**पटपटा करोति, दमदमा करोति**.\\n\\n"
            "**AND THE DOUBLING HAPPENS BEFORE THE ELISION.** "
            "5.4.57 gives डाच्; a vārttika on 8.1.12 doubles the "
            "word; **तच्च टिलोपात् पूर्वमेवेष्यते** — and that "
            "doubling is wanted BEFORE the टि is dropped, or there "
            "would be nothing left to double"),
    Ekadesa(
        "6.1.102", does="pūrvasavarṇa", after="ak",
        before="prathamā-dvitīyā", blocks=("6.1.101",),
        keeps_out="वृक्षः — no vowel follows; नावौ — the earlier "
                  "sound is not an अक्",
        why="प्रथमयोः पूर्वसवर्णः — before the endings of the first "
            "and second cases, the long vowel HOMOGENEOUS WITH THE "
            "EARLIER sound stands for both: **अग्नी, वायू; वृक्षाः, "
            "प्लक्षाः; वृक्षान्, प्लक्षान्**.\\n\\n"
            "**AND प्रथमा IS READ AS COVERING TWO CASES.** "
            "**प्रथमाशब्दो विभक्तिविशेषे रूढः, तत्साहचर्याद् "
            "द्वितीयापि प्रथमेत्युक्ता** — the accusative is called "
            "*first* by keeping company with the nominative.\\n\\n"
            "**AND THE EXCEPTION CHAIN IS WORKED OUT HERE IN FULL.** "
            "6.1.97's पररूप would give वृक्षः for वृक्ष + अस्, and "
            "it does displace 6.1.101's lengthening — but not THIS "
            "rule, **पुरस्तादपवादा अनन्तरान् विधीन् बाधन्ते** — "
            "because an exception stated earlier reaches only what "
            "stands nearest to it.\\n\\n"
            "**AND EACH WORD OF THE RULE ANSWERS A QUESTION.** "
            "**पूर्वसवर्णग्रहणं किम्? अग्नी इत्यत्र पक्षे परसवर्णो "
            "मा भूत्** — so that the LATER sound's homogeneous "
            "vowel is not an option. **दीर्घग्रहणं किम्? त्रिमात्रे "
            "स्थानिनि त्रिमात्रादेशनिवृत्त्यर्थम्** — so that a "
            "three-mora स्थानिन् does not give a three-mora "
            "substitute"),
    Ekadesa(
        "6.1.103", does="n", after="pūrvasavarṇa-dīrgha", before="śas",
        result="puṃs", gives="n",
        keeps_out="गाः पश्य — the long vowel there is 6.1.93's आ and "
                  "not a पूर्वसवर्ण; वृक्षाः — that is जस् and not "
                  "शस्; धेनूः, कुमारीः — not masculine",
        why="तस्माच्छसो नः पुंसि — after the long vowel THAT rule "
            "gave, the स् of शस् becomes न् in the masculine: "
            "**वृक्षान्, अग्नीन्, वायून्, कर्तॄन्**.\\n\\n"
            "**AND तस्मात् IS WHAT KEEPS गाः OUT.** The long vowel "
            "of गाः comes from 6.1.93 and not from the rule before, "
            "so the न् does not follow: **एतांश्चरतो गाः "
            "पश्य**.\\n\\n"
            "**AND A WORD THAT IS MASCULINE IN SENSE BUT FEMININE IN "
            "FORM IS NOT REACHED.** चञ्चा for a man keeps its "
            "feminine shape by 1.2.51's लुपि युक्तवद् व्यक्तिवचने, "
            "**तेन नत्वं न भवति — चञ्चाः पश्य, वध्रिकाः पश्य**. The "
            "rule turns on the शब्द's gender, not the thing's"),
    Ekadesa(
        "6.1.104", after="a-ā", before="ic", refuses=True,
        blocks=("6.1.102",),
        keeps_out="अग्नी — the earlier sound is not अ; वृक्षाः — the "
                  "ending does not begin with an इच्",
        why="नादिचि — after अ or आ, and before a first- or "
            "second-case ending beginning with a vowel other than अ, "
            "the homogeneous long vowel does NOT stand: **वृक्षौ, "
            "प्लक्षौ; खट्वे, कुण्डे**. What answers instead is "
            "6.1.87 and 6.1.88, whose ordinary work the refusal "
            "leaves untouched"),
    Ekadesa(
        "6.1.105", after="dīrgha", before="jas-ic", refuses=True,
        blocks=("6.1.102",),
        why="दीर्घाज्जसि च — and after a long vowel the same refusal, "
            "before जस् as well as before an इच्: **कुमार्यौ, "
            "कुमार्यः; ब्रह्मबन्ध्वौ, ब्रह्मबन्ध्वः**. What stands "
            "instead is 6.1.77's semivowel"),
    Ekadesa(
        "6.1.106", after="dīrgha", before="jas-ic", optional=True,
        chandasi=True, does="pūrvasavarṇa", blocks=("6.1.105",),
        why="वा छन्दसि — in the Vedic corpus the refusal of the rule "
            "before is itself a choice, so the long vowel comes "
            "back: **मारुतीश्चतस्रः पिण्डीः** beside "
            "**मारुत्यश्चतस्रः पिण्ड्यः**; **वाराही उपानहा** beside "
            "**वाराह्यौ उपानह्यौ**"),
    Ekadesa(
        "6.1.107", does="pūrvarūpa", after="ak", before="am",
        blocks=("6.1.87",),
        why="अमि पूर्वः — before the ending अम्, the EARLIER form "
            "stands for both: **वृक्षम्, प्लक्षम्; अग्निम्, "
            "वायुम्**.\\n\\n"
            "**AND पूर्व IS SAID SO THAT THE VOWEL DOES NOT GROW.** "
            "**पूर्वग्रहणं किम्? पूर्व एव यथा स्यात्, पूर्वसवर्णोऽ"
            "न्तरतमो मा भूदिति, कुमारीमित्यत्र हि त्रिमात्रः स्यात्** "
            "— the earlier form ITSELF, not the homogeneous vowel "
            "nearest to it; otherwise the ई of कुमारीम् would come "
            "out three morae long, being substituted for ई and अ "
            "together"),
    Ekadesa(
        "6.1.108", does="pūrvarūpa", after="samprasāraṇa", before="ac",
        why="संप्रसारणाच्च — after a vocalised semivowel the earlier "
            "form again: **इष्टम्, उप्तम्, गृहीतम्**. And this is "
            "the rule whose words bound the अचि heading opened at "
            "6.1.77.\\n\\n"
            "**AND THE RULE IS WHAT MAKES संप्रसारण WORTH DOING AT "
            "ALL.** **संप्रसारणविधानसामर्थ्याद् विगृहीतस्य श्रवणे "
            "प्राप्ते पूर्वत्वं विधीयते** — without it, वप् + त "
            "would be उ · अप् · त, and 6.1.77 would turn the उ back "
            "into व् and undo the whole operation. **परपूर्वत्व"
            "विधाने सत्यर्थवत् संप्रसारणविधानम्.**\\n\\n"
            "**AND IT DOES NOT REACH A JUNCTION MADE LATER.** "
            "**अन्तरङ्गे चाचि कृतार्थं वचनमिति बाह्ये पश्चात् "
            "संनिपतिते पूर्वत्वं न भवति** — शकह्वौ, शकह्वर्थम्"),
    Ekadesa(
        "6.1.109", does="pūrvarūpa", after="eṅ-padānta", before="at",
        blocks=("6.1.78",),
        keeps_out="दध्यत्र — the earlier sound is not ए or ओ; "
                  "चयनम्, लवनम् — it does not end a पद; वायविति — "
                  "what follows is not a short अ",
        why="एङः पदान्तादति — where ए or ओ ends a पद and a short अ "
            "follows, the earlier form stands: **अग्नेऽत्र, "
            "वायोऽत्र**. **अयवादेशयोरयमपवादः** — an exception to "
            "6.1.78's अय् and अव्.\\n\\n"
            "**AND THE त् OF अति IS WHAT KEEPS वायवायाहि OUT.** "
            "**तपरकरणं किम्? वायवायाहि** — a long आ following is "
            "not reached, and 6.1.78 takes it"),
    Ekadesa(
        "6.1.110", does="pūrvarūpa", after="eṅ", before="ṅasi-ṅas",
        why="ङसिङसोश्च — and before the ablative and genitive "
            "singular, whether or not the ए or ओ ends a पद: "
            "**अग्नेरागच्छति, वायोरागच्छति; अग्नेः स्वम्, वायोः "
            "स्वम्**. **अपदान्तार्थ आरम्भः** — the rule exists for "
            "exactly the case the one before it could not reach"),
    Ekadesa(
        "6.1.111", does="ut", after="ṛ", before="ṅasi-ṅas", gives="u",
        why="ऋत उत् — after a ऋ-final stem and before the same two "
            "endings, उ stands for both: **होतुरागच्छति, होतुः "
            "स्वम्**. The last rule the एकादेश heading "
            "reaches.\\n\\n"
            "**AND THE उ TAKES A र् AFTER IT THOUGH IT REPLACES TWO "
            "SOUNDS.** **द्वयोः षष्ठीनिर्दिष्टयोः स्थाने यः स "
            "लभतेऽन्यतरव्यपदेशम्** — a substitute standing for two "
            "things named in the genitive may be called the "
            "substitute of either. So 1.1.51's उरण् रपरः reaches "
            "it, the र् is put in, and 8.2.24's रात् सस्य then "
            "drops the स्"),
    Ekadesa(
        "6.1.112", does="ut", of=("sakhi", "pati"), after="khy-ty",
        before="ṅasi-ṅas", gives="u",
        keeps_out="अतिसखेरागच्छति, सेनापतेरागच्छति — the rule names "
                  "the SHAPES ख्य and त्य, which those do not show",
        why="ख्यत्यात् परस्य — after सखि and पति with their इ already "
            "turned into य्, the same उ for the अ of the ending: "
            "**सख्युरागच्छति, सख्युः स्वम्; पत्युरागच्छति, पत्युः "
            "स्वम्**. And this rule's words are what bound the "
            "एकादेश heading.\\n\\n"
            "**AND THE ODD SHAPE IN THE RULE REACHES TWO MORE "
            "WORDS.** ख्य covers खी and त्य covers ती, so the "
            "denominatives reach it too: सखीयति gives **सख्युः**, "
            "लूनीयति gives **लून्युः** — and the न् of लूनी counts "
            "as the त् it replaced, 8.2.44's substitution being "
            "असिद्ध by 8.2.1.\\n\\n"
            "**AND NAMING SHAPES RATHER THAN WORDS IS WHAT KEEPS "
            "COMPOUNDS OUT.** **विकृतनिर्देशादेवेह न भवति — "
            "अतिसखेरागच्छति** — 1.4.13's घि is refused to सखि alone "
            "and not to what ends in it, so the compound never "
            "shows the ख्य the rule names"),
    Ekadesa(
        "6.1.113", does="ut", of=("ru",), after="a-apluta",
        before="at-apluta", gives="u", blocks=("8.3.17",),
        keeps_out="अग्निरत्र — the earlier sound is not अ; स्वरत्र, "
                  "प्रातरत्र — that र् is the word's own and no रु; "
                  "वृक्ष इह — what follows is not a short अ",
        why="अतो रोरप्लुतादप्लुते — where रु stands between a short "
            "अ and a short अ, उ replaces it: **वृक्षोऽत्र, "
            "प्लक्षोऽत्र**.\\n\\n"
            "**AND IT DISPLACES A RULE OF THE त्रिपादी WITHOUT BEING "
            "BLOCKED BY IT.** 8.3.17 would give य् instead. "
            "**रुत्वमप्याश्रयत्वात् पूर्वत्रासिद्धम् इत्यसिद्धं न "
            "भवति** — the रु this rule leans on comes from 8.2.66, "
            "which is itself in the त्रिपादी; being what the rule "
            "RESTS ON rather than what it is stated against, it is "
            "not held back by 8.2.1.\\n\\n"
            "**AND अप्लुत IS SAID TWICE FOR TWO REASONS.** "
            "**अप्लुतादिति किम्? सुस्रोत३ अत्र न्वसि। अप्लुत इति "
            "किम्? तिष्ठतु पय अ३श्विन्** — a prolated vowel on "
            "either side takes the rule away, and there **प्लुतस्य "
            "असिद्धत्वाद् उत्वं प्राप्नोति** unless both are said"),
    Ekadesa(
        "6.1.114", does="ut", of=("ru",), after="a", before="haś",
        gives="u",
        why="हशि च — and before a soft consonant the same उ for रु: "
            "**पुरुषो याति, पुरुषो हसति, पुरुषो ददाति**. The one "
            "rule of the pāda that acts before a consonant rather "
            "than a vowel"),
)


@dataclass(frozen=True)
class Single:
    """What the resolver answers with."""

    does: str
    sutra: str
    why: str
    gives: str = ""
    teacher: str = ""
    optional: bool = False
    chandasi: bool = False
    #: Where a rule displaces or refuses another, that rule's number.
    blocked_by: Tuple[str, ...] = ()


def _reaches(row: Ekadesa, stem: str, after: str, before: str,
             result: str, teacher: str, chandasi: bool) -> bool:
    # 6.1.84 states no operation of its own and would otherwise be
    # the answer to every question ever asked.
    if row.heading:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.teacher and teacher != row.teacher:
        return False
    if row.of and stem not in row.of:
        return False
    if row.after and after != row.after:
        return False
    allowed = tuple(one for one in (row.before, row.also_before) if one)
    if allowed and before not in allowed:
        return False
    if row.result and result != row.result:
        return False
    return True


def _supplies(row: Ekadesa, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.does and not row.refuses


#: The rules of this section that refuse rather than give. A rule
#: that displaces one of THESE has to outrank it, or the refusal
#: stands and the rule undoing it is never reached — which is
#: exactly what 6.1.106 वा छन्दसि exists to do to 6.1.105.
_REFUSING = frozenset(row.sutra for row in EKADESA_TABLE if row.refuses)


def _how_specific(row: Ekadesa) -> int:
    """
    A refusal beats what it refuses — and a rule that undoes a
    refusal beats the refusal, on the same weight.

    An ācārya's name counts, because a rule reported as one teacher's
    opinion is narrower than the rule it stands beside: 6.1.91 and
    6.1.92 differ in nothing else that a query can see.

    And the corpus counts, because 6.1.105 and 6.1.106 are otherwise
    scored alike: the second says only that the first is a choice
    छन्दसि, and without that term it would never be reached.
    """
    undoes_a_refusal = any(one in _REFUSING for one in row.blocks)
    return (
        9 * (row.refuses or undoes_a_refusal)
        + 8 * bool(row.of)
        + 6 * bool(row.teacher)
        + 5 * bool(row.result)
        + 4 * bool(row.after)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


def one_for_both(stem: str = "", *, after: str = "", before: str = "",
                 result: str = "", teacher: str = "",
                 chandasi: bool = False, wants: str = "") -> Single:
    """
    6.1.84–114 — one substitute in the room of two sounds.

    The answer names the KIND of substitute and the rule that gives
    it. Where a rule refuses, it answers by its own number with
    nothing given, and reports on `blocked_by` the rule the form is
    taken away FROM.

    6.1.84 supplies nothing: it says how a substitute in this section
    is to be READ, not what it is, so what escapes the rules escapes
    the section.
    """
    matched = [
        row for row in EKADESA_TABLE
        if _reaches(row, stem, after, before, result, teacher, chandasi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Single(
            "", "", "No rule of 6.1.84–114 is reached. 6.1.84 is a "
                    "heading that says how a substitute is READ — "
                    "for the earlier and later sounds together — and "
                    "supplies none of its own")
    row = max(matched, key=_how_specific)
    return Single("" if row.refuses else row.does, row.sutra, row.why,
                  gives=row.gives, teacher=row.teacher,
                  optional=row.optional, chandasi=row.chandasi,
                  blocked_by=row.blocks)


def ekadesa_run() -> Single:
    """
    How far एकः पूर्वपरयोः governs, and what each of its two words
    is doing.

    **ख्यत्यात् परस्य इति प्रागेतस्मात् सूत्रात्.**
    """
    opens, closes = EKADESA_RUN
    return Single(
        "", opens,
        "एकः पूर्वपरयोः governs from %s to %s, bounded by the words "
        "of %s. Both of its words earn their place: %s, and %s"
        % (opens, closes, EKADESA_MARKER, WHY_BOTH_WORDS[0],
           WHY_BOTH_WORDS[1]))


def provisions_for(sutra_id: str) -> Tuple[Ekadesa, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in EKADESA_TABLE if row.sutra == sutra_id)
