# -*- coding: utf-8 -*-
"""
८.४.४०–६८ — ष्टुत्व, the doubling, जश्त्व, and the अ that ends the work.

Twenty-nine sūtras, and the last of them is two syllables long.
The run begins with the two assimilation rules every student
learns first — 8.4.40 **स्तोः श्चुना श्चुः** and 8.4.41
**ष्टुना ष्टुः**, a स् or त-वर्ग taking the class of a श् or
ष् it meets — and the Kāśikā at once says what one might expect
and is not so: **स्तोः श्चुना इति यथासंख्यम् अत्र न इष्यते**,
the pairs are NOT matched one to one, so either cause gives
either effect.

**THEN THE DOUBLING.** 8.4.46 अचो रहाभ्यां द्वे doubles a यर्
after a र् or ह् that follows a vowel — अर्क्कः, ब्रह्म्मा,
अपह्न्नुते — and 8.4.47 अनचि च doubles one after any vowel with
no vowel following: दद्ध्यत्र. And then THREE TEACHERS refuse
it in three different measures: Śākaṭāyana not in a cluster of
three (8.4.50 इन्द्रः), Śākalya not at all (8.4.51 अर्कः), and
the आचार्याः not after a long vowel (8.4.52 दात्रम्, सूत्रम्).
Of all the doubling the grammar prescribes, almost none is
written.

**THEN THE VOICING AND THE UNVOICING.** 8.4.53 झलां जश् झशि
gives लब्धा and बोद्धा; 8.4.54 अभ्यासे चर्च unvoices the
reduplication — चिखनिषति, बुभूषति, जिघत्सति; and 8.4.56
वाऽवसाने leaves वाक् and वाग् both standing at a pause, which
is why a Sanskrit word can be quoted two ways.

**AND THE WORK ENDS ON A SOUND THAT WAS NEVER REALLY THERE.**
8.4.68 **अ अ इति** — **एकोऽत्र विवृतः, अपरः संवृतः। तत्र
विवृतस्य संवृतः क्रियते**. The अ of the Śivasūtras was declared
OPEN for the grammar's own purposes, so that it could be
matched with आ; the last rule of the Aṣṭādhyāyī closes it again
so that nothing is ever spoken that way. वृक्षः, प्लक्षः.

**WHAT THIS MODULE DOES NOT DO.** 8.4.55 खरि च was codified
apart long before the pāda was read, and is named in
`CODIFIED_APART`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.ru_anunasika import Joined  # noqa: E402

#: This module's stretch, which closes the work.
STUTVA_RUN: Tuple[str, str] = ("8.4.40", "8.4.68")

#: Codified apart long before the pāda was read: 8.4.55 खरि च.
CODIFIED_APART: Tuple[str, ...] = ("8.4.55",)

#: The last sūtra of the Aṣṭādhyāyī.
THE_LAST: str = "8.4.68"

#: What the Kāśikā says of 8.4.40 and 8.4.41 both: the two pairs
#: are NOT matched one to one.
NOT_YATHASAMKHYAM: str = (
    "स्तोःश्चुना इति यथासंख्यम् अत्र न इष्यते")

#: The three teachers who refuse the doubling, and how far.
DOUBLING_REFUSED: Tuple[str, ...] = (
    "śākaṭāyana", "śākalya", "ācārya")


@dataclass(frozen=True)
class Stutva:
    """One rule of 8.4.40–68: an assimilation, a doubling, a close."""

    sutra: str
    #: `ścu`, `ṣṭu`, `anunāsika`, `dve`, `jaś`, `car`,
    #: `parasavarṇa`, `pūrvasavarṇa`, `la`, `cha`, `lopa`,
    #: `svarita`, `saṃvṛta`.
    does: str = ""
    #: The words named outright.
    of: Tuple[str, ...] = ()
    #: The shape of what the rule reaches.
    gana: str = ""
    #: What must stand before.
    after: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    sense: Tuple[str, ...] = ()
    #: A named teacher's opinion.
    view: str = ""
    #: True where the sūtra only keeps another rule off.
    refuses: bool = False
    optional: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


STUTVA_TABLE: Tuple[Stutva, ...] = (
    Stutva(
        "8.4.40", does="ścu", gana="stu", before=("ścu",),
        why="स्तोः श्चुना श्चुः — a स् or a त-वर्ग meeting a श् "
            "or a च-वर्ग takes their class. And the Kāśikā at "
            "once says what one might expect and is not so — "
            "**स्तोःश्चुना इति यथासंख्यम् अत्र न इष्यते** — the "
            "two pairs are NOT matched one to one: a स् becomes "
            "श् whether the cause is a श् or a palatal stop, "
            "and a त-वर्ग becomes a palatal either way. This is "
            "the rule तच्छिवः and रामश्च are made by"),
    Stutva(
        "8.4.41", does="ṣṭu", gana="stu", before=("ṣṭu",),
        why="ष्टुना ष्टुः — and meeting a ष् or a ट-वर्ग they "
            "take THAT class: **वृक्षष्षण्डे, प्लक्षष्षण्डे** "
            "for the ष्, **वृक्षष्टीकते** for the cerebral "
            "stop. **अत्र अपि तथैव संख्यातानुदेशाभावः** — the "
            "same refusal to match the pairs one to one, said "
            "again in one clause. स्तोः is carried down from "
            "the sūtra before"),
    Stutva(
        "8.4.42", refuses=True, gana="stu",
        after="pada-anta-ṭu", blocks=("8.4.41",),
        keeps_out="षण्णाम् — नाम् is excepted by name; ईट्टे — "
                  "the ट् does not end a word; सर्पिष्टमम् — "
                  "the cause is not a ट-वर्ग",
        why="न पदान्ताट्टोरनाम् — but NOT after a ट-वर्ग that "
            "ends a word, except before नाम्: **श्वलिट् साये; "
            "मधुलिट् तरति**. All three of its words are tested, "
            "and the exception for नाम् is what makes षण्णाम् "
            "come out as it does. The Kāśikā thinks the "
            "exception too narrow — **अत्यल्पम् इदम् उच्यते**"),
    Stutva(
        "8.4.43", refuses=True, gana="tu", before=("ṣa",),
        blocks=("8.4.41",),
        why="तोः षि — nor of a त-वर्ग before a ष्: "
            "**अग्निचित् षण्डे; भवान् षण्डे; महान् षण्डे**. "
            "8.4.41 would have made the त् a ट्, and this keeps "
            "it out — which is why a त्-final word before a "
            "ष्-initial one is heard unchanged where before a "
            "ट्-initial one it is not"),
    Stutva(
        "8.4.44", refuses=True, gana="tu", after="śa",
        blocks=("8.4.40",),
        why="शात् — nor of a त-वर्ग AFTER a श्: **प्रश्नः, "
            "विश्नः**. तोः is carried down from the sūtra "
            "before, and what is new is that the cause stands "
            "in front rather than behind — so 8.4.40's palatal "
            "does not come and प्रश्नः keeps its न्"),
    Stutva(
        "8.4.45", does="anunāsika", gana="yar-pada-anta",
        before=("anunāsika",), optional=True,
        why="यरोऽनुनासिकेऽनुनासिको वा — a word-final यर् "
            "OPTIONALLY becomes the answering nasal before a "
            "nasal: **वाङ् नयति, वाग् नयति; श्वलिण् नयति, "
            "श्वलिड् नयति; अग्निचिन् नयति, अग्निचिद् नयति; "
            "त्रिष्टुम् नयति, त्रिष्टुब् नयति**. Four pairs, "
            "one for each class of stop, and the option is what "
            "makes both readings of every such junction correct"),
    Stutva(
        "8.4.46", does="dve", gana="yar", after="ac-ra-ha",
        keeps_out="किन् ह्नुते, किम् ह्मलयति — no vowel stands "
                  "before the ह्",
        why="अचो रहाभ्यां द्वे — a यर् after a र् or a ह् that "
            "itself follows a VOWEL is doubled: **अर्क्कः, "
            "मर्क्कः; ब्रह्म्मा; अपह्न्नुते**. This and the "
            "next are the two doubling rules the manuscripts "
            "almost never write out, and the three sūtras after "
            "them are three teachers saying so"),
    Stutva(
        "8.4.47", does="dve", gana="yar", after="ac",
        before=("an-ac",), blocks=("8.4.46",),
        keeps_out="स्मितम्, ध्मातम् — no vowel before the यर्",
        why="अनचि च — and a यर् after ANY vowel, provided no "
            "vowel follows it: **दद्ध्यत्र, मद्ध्वत्र**. A "
            "vārttika restates it with two pratyāhāras — "
            "**यणो मयो द्वे भवतः** — and the Kāśikā records a "
            "disagreement about which of the two cases is "
            "ablative and which genitive, which changes what "
            "the rule reaches"),
    Stutva(
        "8.4.48", refuses=True, of=("putra",), before=("ādinī",),
        sense=("ākrośa",), blocks=("8.4.47",),
        keeps_out="पुत्त्रादिनी of plain description, where the "
                  "doubling does come",
        why="नादिन्याक्रोशे पुत्रस्य — but पुत्र is not doubled "
            "before आदिनी where ABUSE is meant: **पुत्रादिनी "
            "त्वम् असि पापे** — you child-eater, you wretch. "
            "**आक्रोश इति किम्? तत्त्वकथने द्विर्वचनं भवत्य् "
            "एव** — said as a plain statement of fact the "
            "doubling comes, and the word is then पुत्त्रादिनी"),
    Stutva(
        "8.4.49", refuses=True, gana="śar", before=("ac",),
        blocks=("8.4.46",),
        keeps_out="दर्श्श्यते — no vowel follows the शर्",
        why="शरोऽचि — nor is a शर् doubled before a vowel: "
            "**कर्षति, वर्षति; आदर्शः, अक्षदर्शः**. 8.4.46 "
            "would have doubled the ष् of कर्षति, the र् "
            "standing in front of it after a vowel, and this "
            "keeps it out"),
    Stutva(
        "8.4.50", refuses=True, gana="tri-prabhṛti",
        view="śākaṭāyana", blocks=("8.4.46", "8.4.47"),
        why="त्रिप्रभृतिषु शाकटायनस्य — and in ŚĀKAṬĀYANA'S "
            "view there is no doubling where three or more "
            "consonants already stand together: **इन्द्रः, "
            "चन्द्रः, मन्द्रः, राष्ट्रम्, भ्राष्ट्रम्**. The "
            "first of three teachers, and the narrowest of the "
            "three refusals"),
    Stutva(
        "8.4.51", refuses=True, view="śākalya",
        blocks=("8.4.46", "8.4.47"),
        why="सर्वत्र शाकल्यस्य — and in ŚĀKALYA'S view there is "
            "none ANYWHERE: **अर्कः, मर्कः, ब्रह्मा, "
            "अपह्नुते**. This is the reading the manuscripts "
            "in fact follow, and the four words are 8.4.46's "
            "own examples given back without their doubling — "
            "which is as plain a way as the Kāśikā has of "
            "saying which teacher won"),
    Stutva(
        "8.4.52", refuses=True, after="dīrgha", view="ācārya",
        blocks=("8.4.46", "8.4.47"),
        why="दीर्घादाचार्याणाम् — and in the TEACHERS' view "
            "there is none after a long vowel: **दात्रम्, "
            "पात्रम्, मूत्रम्, सूत्रम्**. Three sūtras, three "
            "namings, three different measures of the same "
            "refusal — and the grammar's own rule stands "
            "between them without ever being withdrawn"),
    Stutva(
        "8.4.53", does="jaś", gana="jhal", before=("jhaś",),
        keeps_out="दत्तः, दत्थः, दध्मः — no झश् follows",
        why="झलां जश् झशि — a झल् becomes the answering जश् "
            "before a झश्: **लब्धा, लब्धुम्, लब्धव्यम्; "
            "दोग्धा, दोग्धुम्; बोद्धा, बोद्धुम्**. This is what "
            "voices the first half of every such cluster, and "
            "8.2.40 had already made the second half aspirate — "
            "so लभ् plus त becomes लब्ध through two pādas' "
            "worth of rules"),
    Stutva(
        "8.4.54", does="car", gana="abhyāsa-jhal",
        why="अभ्यासे चर्च — in the REDUPLICATION a झल् becomes "
            "the answering चर्, and by the च a जश् as well: "
            "**चिखनिषति, चिच्छित्सति, टिठकारयिषति, तिष्ठासति, "
            "बुभूषति, जिघत्सति, डुढौकिषते**. And where the copy "
            "already has a चर् it keeps it — **प्रकृतिचरां "
            "प्रकृतिचरो भवन्ति — चिचीषति, टिटीकिषते**. Every "
            "reduplicated stem in the language passes through "
            "this rule and through 7.4.60 together"),
    Stutva(
        "8.4.56", does="car", gana="jhal", after="avasāna",
        optional=True,
        why="वाऽवसाने — and at a PAUSE a झल् becomes चर् "
            "OPTIONALLY: **वाक्, वाग्; त्वक्, त्वग्; श्वलिट्, "
            "श्वलिड्; त्रिष्टुप्, त्रिष्टुब्**. **झलां चर् इति "
            "वर्तते**. This is why a Sanskrit word quoted alone "
            "may be heard two ways, and why the lexica differ "
            "with themselves about which form to print"),
    Stutva(
        "8.4.57", does="anunāsika", gana="aṇ-a-pragṛhya",
        after="avasāna", optional=True,
        keeps_out="कर्तृ, हर्तृ — the vowel is not an अण्; "
                  "अग्नी, वायू — प्रगृह्य, which the sūtra "
                  "excepts",
        why="अणोऽप्रगृह्यस्यानुनासिकः — and an अण् that is not "
            "प्रगृह्य optionally goes NASAL at a pause: "
            "**दधिँ, दधि; मधुँ, मधु; कुमारीँ, कुमारी**. The "
            "nasalised vowel at the end of an isolated word is "
            "a feature of recitation the written language has "
            "almost no way to show, and this is the sūtra that "
            "prescribes it"),
    Stutva(
        "8.4.58", does="parasavarṇa", gana="anusvāra",
        before=("yay",),
        why="अनुस्वारस्य ययि परसवर्णः — an anusvāra before a "
            "यय् becomes the nasal OF THAT SOUND'S OWN CLASS: "
            "**शङ्किता, उञ्छिता, कुण्डिता, नन्दिता, कम्पिता**. "
            "Five words for five classes, and this is why a "
            "nasal inside a Sanskrit word always agrees with "
            "what follows it — which the writing system then "
            "records with five different letters"),
    Stutva(
        "8.4.59", does="parasavarṇa", gana="anusvāra-pada-anta",
        before=("yay",), optional=True, blocks=("8.4.58",),
        why="वा पदान्तस्य — but a word-final anusvāra does it "
            "only OPTIONALLY: **तङ् कथञ् चित्रपक्षण् डयमानन् "
            "नभःस्थम् पुरुषोऽवधीत्** beside **तं कथं "
            "चित्रपक्षं डयमानं नभःस्थं पुरुषोऽवधीत्**. One "
            "line given twice over, every nasal in it assimi"
            "lated in the first and left as an anusvāra in the "
            "second — the clearest illustration in the pāda"),
    Stutva(
        "8.4.60", does="la", gana="tu", before=("la",),
        why="तोर्लि — a त-वर्ग before a ल् becomes ल्: "
            "**अग्निचिल् लुनाति; सोमसुल् लुनाति; भवाँल् "
            "लुनाति; महाँल् लुनाति**. The last two show the "
            "nasalised ल् that a न् becomes, which no other "
            "rule of the work provides and which the writing "
            "shows with a candrabindu"),
    Stutva(
        "8.4.61", does="pūrvasavarṇa", of=("sthā", "stambh"),
        after="ud",
        keeps_out="उत्स्यति — the root is neither of the two",
        why="उदः स्थास्तम्भोः पूर्वस्य — after उद्, the स् of "
            "स्था and स्तम्भ् takes the class of what stands "
            "BEFORE it: **उत्त्थाता, उत्त्थातुम्, "
            "उत्त्थातव्यम्; उत्तम्भिता, उत्तम्भितुम्**. "
            "Everywhere else in the pāda a sound takes the "
            "class of what FOLLOWS, and this is the one rule "
            "that reverses the direction"),
    Stutva(
        "8.4.62", does="pūrvasavarṇa", gana="ha", after="jhay",
        optional=True,
        why="झयो होऽन्यतरस्याम् — and a ह् after a झय् "
            "optionally takes the class of what precedes: "
            "**वाग्घसति, वाग् हसति; श्वलिड् ढसति; "
            "अग्निचिद्धसति; सोमसुद्धसति; त्रिष्टुब्भसति**. It "
            "is the same backward direction as the sūtra "
            "before, and this time over a whole class of sounds"),
    Stutva(
        "8.4.63", does="cha", gana="śa", after="jhay",
        before=("aṭ",), optional=True,
        why="शश्छोऽटि — and a श् after a झय् with an अट् after "
            "it optionally becomes छ्: **वाक्छेते, वाक् शेते; "
            "अग्निचिच्छेते; सोमसुच्छेते; श्वलिट् छेते**. "
            "अन्यतरस्याम् is carried down from the sūtra "
            "before, which is how three optional rules in a row "
            "are stated with one word between them"),
    Stutva(
        "8.4.64", does="lopa", gana="yam", after="hal",
        before=("yam",), optional=True,
        why="हलो यमां यमि लोपः — a यम् after a consonant is "
            "optionally DROPPED before another यम्: in शय्या "
            "there are two य् and a third made by the doubling, "
            "**तत्र मध्यमस्य वा लोपो भवति** — the middle one "
            "goes, or does not: **शय्या, शय्य्या**. The rule is "
            "about what the doubling of 8.4.46–47 has just "
            "produced, and about nothing else"),
    Stutva(
        "8.4.65", does="lopa", gana="jhar", after="hal",
        before=("jhar-savarṇa",), optional=True,
        why="झरो झरि सवर्णे — and a झर् after a consonant "
            "before a HOMOGENEOUS झर्: in प्रत्तम् there are "
            "three त् and a fourth from the doubling, **तत्र "
            "मध्यमस्य मध्यमयोर् वा लोपो भवति** — one may go or "
            "two. This and the sūtra before are what keep the "
            "written language from having to show clusters four "
            "and five sounds deep"),
    Stutva(
        "8.4.66", does="svarita", gana="anudātta", after="udātta",
        why="उदात्तादनुदात्तस्य स्वरितः — an अनुदात्त after an "
            "उदात्त becomes स्वरित: **गार्ग्यः, वात्स्यः; पचति, "
            "पठति**. And the vṛtti points out what the "
            "asiddhatva of the tripādī does here — **अस्य "
            "स्वरितस्य असिद्धत्वाद् 6.1.158 अनुदात्तं पदम् "
            "एकवर्जम् इत्येतद् न प्रवर्तते** — the स्वरित this "
            "rule makes is invisible to the rule that would "
            "have made everything else toneless, so both "
            "accents are heard"),
    Stutva(
        "8.4.67", refuses=True, gana="anudātta", after="udātta",
        before=("udātta-svarita-udaya",),
        view="a-gārgya-kāśyapa-gālava", blocks=("8.4.66",),
        why="नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम् — but not "
            "where an उदात्त or a स्वरित FOLLOWS, in the view "
            "of everyone EXCEPT Gārgya, Kāśyapa and Gālava: "
            "**पूर्वेण प्राप्तः प्रतिषिध्यते**. The sūtra is "
            "the only place in the work where teachers are "
            "named to be excluded rather than followed, and the "
            "three named are the ones who would have let the "
            "स्वरित come"),
    Stutva(
        "8.4.68", does="saṃvṛta", of=("a",),
        why="अ अ इति — and the Aṣṭādhyāyī ends on two syllables. "
            "**एकोऽत्र विवृतः, अपरः संवृतः। तत्र विवृतस्य "
            "संवृतः क्रियते** — of the two अ written here the "
            "first is OPEN and the second CLOSED, and the open "
            "one is replaced by the closed. **वृक्षः, "
            "प्लक्षः**.\\n\\n"
            "**AND WHAT IT UNDOES IS SOMETHING THE GRAMMAR "
            "ITSELF PUT THERE.** **इह शास्त्रे कार्यार्थम् "
            "अकारो विवृतः प्रतिज्ञातः, तस्य तथाभूतस्य एव "
            "प्रयोगो मा भूद् इति संवृतप्रतिज्ञानम्** — the अ of "
            "अइउण् was declared open so that it could count as "
            "homogeneous with आ and the whole machinery of "
            "सवर्ण could work; and the last rule of the work "
            "closes it again so that nothing is ever actually "
            "SPOKEN that way. The book begins by making a sound "
            "up and ends by taking it back"),
)


def _reaches(row: Stutva, word: str, gana: str, after: str,
             before: str, sense: str, view: str) -> bool:
    # `of` and `gana` CONJOIN, as everywhere in अध्याय ८.
    if row.of and word not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.after and after != row.after:
        return False
    if row.before and before not in row.before:
        return False
    if row.sense and sense not in row.sense:
        return False
    if row.view and view != row.view:
        return False
    return True


def _how_specific(row: Stutva) -> int:
    """
    A refusal outweighs the rules it refuses, a named word
    outweighs a shape, and a named teacher weighs least — since
    asking for one is what makes his rule reachable at all.

    8.4.46 against 8.4.50, 8.4.51 and 8.4.52 is why the view
    column is here: one rule doubles and three teachers refuse
    it in three different measures.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of)
        + 6 * len(row.sense)
        + 4 * bool(row.gana)
        + 4 * bool(row.after)
        + 3 * bool(row.before)
        + 1 * bool(row.view)
    )


def at_the_junction(word: str = "", *, gana: str = "",
                    after: str = "", before: str = "",
                    sense: str = "", view: str = "") -> Joined:
    """
    8.4.40–68 — the assimilations, the doubling, and the close.

    Nothing answers by default, and a teacher's rule answers
    only a reader who asks for that teacher.
    """
    matched = [
        row for row in STUTVA_TABLE
        if _reaches(row, word, gana, after, before, sense, view)
    ]
    if not matched:
        return Joined(
            "", "", "No rule of 8.4.40-68 is reached, so the two "
                    "sounds stand as they are")
    row = max(matched, key=_how_specific)
    return Joined(row.does, row.sutra, row.why,
                  refuses=row.refuses,
                  optional=row.optional, view=row.view,
                  blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Stutva, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in STUTVA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Stutva", "STUTVA_TABLE", "STUTVA_RUN", "CODIFIED_APART",
    "THE_LAST", "NOT_YATHASAMKHYAM", "DOUBLING_REFUSED",
    "at_the_junction", "provisions_for",
]
