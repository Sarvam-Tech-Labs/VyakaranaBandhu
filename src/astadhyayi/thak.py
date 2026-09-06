# -*- coding: utf-8 -*-
"""
४.४.१–३० — प्राग्वहतेष्ठक्, and the affix named before the senses are.

4.1.83 प्राग्दीव्यतोऽण् put अण् over everything up to 4.4.2 and let
each rule state a sense. This pāda opens by doing the same thing with
a different affix and a different boundary: **प्रागेतस्माद्
वहतिसंशब्दनाद् यानर्थाननुक्रमिष्यामः, ठक् प्रत्ययस्तेष्वधिकृतो
वेदितव्यः** — ठक् is the affix for every sense named between here and
4.4.76 तद्वहति, unless a rule says otherwise.

So the two great headings of the taddhita section meet exactly at
4.4.2: अण् stops where ठक् begins, and each is bounded by lifting one
word out of the rule it stops at.

**And the senses here are ACTIONS.** 4.1 asked whose descendant a man
was, 4.2 and 4.3 where a thing came from or what it was made of; from
4.4.2 the question is what someone DOES with the thing — plays with
it, digs with it, crosses by it, lives by it, carries by it. The base
stands in the instrumental and the affix reports the means:
**क्रियाप्रधानत्वेऽपि चाख्यातस्य तद्धितः स्वभावात् साधनप्रधानः** —
though a finite verb foregrounds the action, a taddhita by its nature
foregrounds the means.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where the ठक् heading runs — and its MARKER and its LAST RULE are
#: not the same sūtra.
#:
#: 4.4.1's vṛtti names the marker: **तद्वहति रथयुगप्रासङ्गम् इति
#: वक्ष्यति, प्रागेतस्माद् वहतिसंशब्दनात्**, so the word वहति is
#: lifted out of 4.4.76 exactly as 4.1.83 lifted दीव्यति out of the
#: rule IT stops at. But 4.4.75 प्राग्घिताद् यत् is itself a heading
#: and stands inside that range, so ठक् does not reach it — and
#: 4.4.74's vṛtti closes the account: **ठकः पूर्णोऽवधिः, अतः परमन्यः
#: प्रत्ययो विधीयते**, the limit is complete and from here another
#: affix is enjoined.
#:
#: The two come apart because a second heading opens inside the
#: first's range. Held separately for that reason.
THAK_RUN: Tuple[str, str] = ("4.4.1", "4.4.74")

#: The sūtra whose word bounds the ठक् heading — one past the range,
#: and two past its last rule.
THAK_MARKER: str = "4.4.76"

#: And the third great प्राक्-heading, which reaches out of the
#: chapter. 4.4.75's vṛtti: **तस्मै हितम् इति वक्ष्यति; प्रागेतस्माद्
#: हितसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामो यत्प्रत्ययस्तेष्वधिकृतो
#: वेदितव्यः** — यत् from here to 5.1.4, bounded by lifting हित out
#: of 5.1.5, which is the same device for the third time.
#: And it closes the same way the ठक् heading did. 4.4.144's
#: vṛtti ends the pāda with **यतः पूर्णोऽवधिः, अतः परमन्यः
#: प्रत्ययोऽधिक्रियते** — word for word what 4.4.74 said of
#: ठक् — because 5.1.1 प्राक्क्रीताच्छः opens छ inside this
#: range. So the marker is 5.1.5 and the last rule is
#: 4.4.144.
#:
#: Twice in one pāda, and the second confirms the first: a
#: प्राक्-heading's marker is where its NAME points, and its
#: last rule is where the next heading starts. Not an
#: irregularity — it is how they nest.
YAT_RUN: Tuple[str, str] = ("4.4.75", "4.4.144")
YAT_MARKER: str = "5.1.5"

#: A kārikā at 4.4.7 counts the ष-initial affixes of this section:
#:
#:     आकर्षात् पर्पादेर्भस्त्रादिभ्यः कुसीदसूत्राच्च ।
#:     आवसथात् किशरादेः षितः षडेते ठगधिकारे ॥
#:
#: Six bases, and then the correction: **विधिवाक्यापेक्षं च षट्त्वम्,
#: प्रत्ययास्तु सप्त** — six as far as the rule-statements go, but
#: SEVEN affixes, because one of the rules gives two.
#:
#: Held as the bases the verse names rather than as rule-numbers,
#: since four of the six lie beyond what is codified. Each will be
#: checked against its row as it arrives.
SIT_AFFIX_BASES: Tuple[str, ...] = (
    "ākarṣa", "parpādi", "bhastrādi", "kusīda-sūtra",
    "āvasatha", "kiśarādi")


@dataclass(frozen=True)
class Thak:
    """One rule of 4.4: a means, an action, and what comes."""

    sutra: str
    #: What the affix is, or "" where the rule removes one instead.
    #: Empty also where 4.4.1's ठक् simply stands, which is most of
    #: the section — but every rule here names its own sense, so the
    #: rows carry ठक् explicitly rather than leaving it to be
    #: inferred.
    gives: str = ""
    #: The other affixes the same rule gives — 4.4.11's ष्ठन् beside
    #: its ठञ्, 4.4.14's ठञ् beside its छ.
    also_gives: Tuple[str, ...] = ()
    of: Tuple[str, ...] = ()
    gana: str = ""
    #: The ACTION the affix reports: दीव्यति, खनति, जयति, तरति,
    #: चरति, जीवति, हरति, संसृष्ट, उपसिक्त, वर्तते, प्रयच्छति.
    #: Not a sense in the way 4.2's were — these are verbs, and the
    #: derived word means *one who does that by this*.
    sense: str = ""
    #: The case the base stands in. तृतीया for the means, and
    #: द्वितीया from 4.4.28, where the thing is what one moves along
    #: rather than what one moves by.
    case: str = ""
    #: A further condition on what the result must be — 4.4.30's
    #: गर्ह्य, where only a BLAMEWORTHY giving takes the affix.
    result: str = ""
    #: A class the base belongs to: व्यञ्जन, and the stems ending in
    #: 3.3.88's क्त्रि.
    of_samjna: str = ""
    #: The PENULTIMATE sound — 4.4.4's कोपध, on the same argument
    #: that gave the two previous pādas theirs.
    upadha: str = ""
    #: How many vowels the base has. 4.4.7 wants द्व्यच्.
    vowels: str = ""
    #: Which register the rule is confined to — छन्दसि for the Veda
    #: at 4.4.106 and from 4.4.110 to the end, and "" for the rest.
    #: 4.4.110's vṛtti states the range: **आ पादपरिसमाप्तेश्
    #: छन्दोऽधिकारः**, to the end of the pāda.
    #:
    #: One column and not two flags, for the reason `kala_taddhita`
    #: gave: a rule is in one register, the other, or neither.
    usage: str = ""
    #: The last member of the compound the rule names — 4.4.37's
    #: माथ, 4.4.39's पद — or the sound the base ends in, 4.4.49's ऋ.
    stem_final: str = ""
    #: What stands in front — 4.4.28's प्रति and अनु.
    pre: str = ""
    optional: bool = False
    #: True where the rule takes the affix AWAY. 4.4.24 and 4.4.79.
    elides: bool = False
    #: An आगम the rule adds in the same act — 4.4.89's षुक्.
    augment: str = ""
    #: True where the row IS a heading rather than a rule under one.
    #: There are two in this pāda, and they do not compete: 4.4.1
    #: governs to 4.4.74 and 4.4.75 from there on.
    heading: bool = False
    excepts: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


THAK_TABLE: Tuple[Thak, ...] = (
    Thak("4.4.1", gives="ṭhak", case="tṛtīyā", heading=True,
         why="प्राग्वहतेष्ठक्. **तद्वहति रथयुगप्रासङ्गम् इति "
             "वक्ष्यति; प्रागेतस्माद् वहतिसंशब्दनाद् "
             "यानर्थाननुक्रमिष्यामः, ठक् प्रत्ययस्तेष्वधिकृतो "
             "वेदितव्यः** — ठक् is the affix for every sense named "
             "between here and 4.4.76, unless a rule says otherwise. "
             "अक्षैर्दीव्यति **आक्षिकः**.\\n\\n"
             "**AND THE TWO GREAT HEADINGS MEET AT 4.4.2.** 4.1.83 "
             "प्राग्दीव्यतोऽण् put अण् over everything up to the "
             "rule that names दीव्यति, and that rule is the next one. "
             "Each heading is bounded by lifting one word out of the "
             "sūtra it stops at, and the two boundaries are the two "
             "halves of one join.\\n\\n"
             "Four vārttikas add senses the sūtras do not name. "
             "**ठक्प्रकरणे तदाहेति माशब्दादिभ्य उपसंख्यानम्** — "
             "माशब्द इत्याह **माशब्दिकः**, one who says *no*; "
             "**आहौ प्रभूतादिभ्यः** — प्राभूतिकः; **पृच्छतौ "
             "सुस्नातादिभ्यः** — सौस्नातिकः, one who asks after "
             "another's bath; **गच्छतौ परदारादिभ्यः** — "
             "**पारदारिकः**, an adulterer, made by a supplement to a "
             "rule about affixes"),
    Thak("4.4.2", gives="ṭhak", sense="dīvyati", case="tṛtīyā",
         why="तेन दीव्यति खनति जयति जितम्, the दीव्यति member. "
             "अक्षैर्दीव्यति **आक्षिकः**, a dicer; शालाकिकः.\\n\\n"
             "**सर्वत्र करणे तृतीया समर्थविभक्तिः** — the "
             "instrumental here is always the INSTRUMENT and never "
             "the agent. देवदत्तेन जितमिति प्रत्ययो न भवति, "
             "**अनभिधानात्**: *won by Devadatta* takes nothing, "
             "because that is not how the language says it. "
             "अङ्गुल्या खनतीति च — nor *digs with a finger*.\\n\\n"
             "**प्रत्ययार्थे संख्याकालयोरविवक्षा** — number and time "
             "are not meant by the affix. And "
             "**क्रियाप्रधानत्वेऽपि चाख्यातस्य तद्धितः स्वभावात् "
             "साधनप्रधानः**: though a finite verb foregrounds the "
             "ACTION, a taddhita by its nature foregrounds the MEANS. "
             "The clearest statement in the section of what these "
             "affixes are for",
         keeps_out="देवदत्तेन जितम्, अङ्गुल्या खनति"),
    Thak("4.4.2", gives="ṭhak", sense="khanati", case="tṛtīyā",
         why="तेन दीव्यति खनति जयति जितम्, the खनति member. अभ्र्या "
             "खनति **आभ्रिकः**, one who digs with a hoe; "
             "कौद्दालिकः"),
    Thak("4.4.2", gives="ṭhak", sense="jayati", case="tṛtīyā",
         why="तेन दीव्यति खनति जयति जितम्, the जयति member. "
             "अक्षैर्जयति **आक्षिकः** — the same form as the dicer's, "
             "and the same word answers two of the four senses"),
    Thak("4.4.2", gives="ṭhak", sense="jita", case="tṛtīyā",
         why="तेन दीव्यति खनति जयति जितम्, the जित member — and this "
             "one is a PARTICIPLE where the other three are finite "
             "verbs. अक्षैर्जितम् **आक्षिकम्**; शालाकिकम्. What was "
             "won by dice, rather than one who wins by them"),
    Thak("4.4.3", gives="ṭhak", sense="saṃskṛta", case="tṛtīyā",
         why="संस्कृतम्. **सत उत्कर्षाधानं संस्कारः** — a refinement "
             "is the raising of something that already is. दध्ना "
             "संस्कृतं **दाधिकम्**; शार्ङ्गवेरिकम्, मारिचिकम्.\\n\\n"
             "**योगविभाग उत्तरार्थः** — the rule is split off from "
             "the last for the sake of the next, and the same device "
             "the pāda before used five times"),
    Thak("4.4.4", gives="aṇ", of=("kulattha",), sense="saṃskṛta",
         case="tṛtīyā", excepts=("4.4.3",),
         why="कुलत्थकोपधादण्, ठकोऽपवादः; the named-word half. "
             "कुलत्थैः संस्कृतं **कौलत्थम्**"),
    Thak("4.4.4", gives="aṇ", upadha="k", sense="saṃskṛta",
         case="tṛtīyā", excepts=("4.4.3",),
         why="कुलत्थकोपधादण्, the कोपध half. तैत्तिडीकम्, "
             "दार्दभकम् — and the penultimate again, the third pāda "
             "running to state a rule on it"),
    Thak("4.4.5", gives="ṭhak", sense="tarati", case="tṛtīyā",
         why="तरति. **तरति प्लवत इत्यर्थः** — crosses, floats. "
             "काण्डप्लवेन तरति **काण्डप्लविकः**; औडुपिकः, one who "
             "crosses by a raft"),
    Thak("4.4.6", gives="ṭhañ", of=("gopuccha",), sense="tarati",
         case="tṛtīyā", excepts=("4.4.5",),
         why="गोपुच्छाट् ठञ्, ठकोऽपवादः. **स्वरे विशेषः** — and the "
             "two affixes differ in the accent and in nothing else. "
             "**गौपुच्छिकः**, one who crosses holding a cow's tail"),
    Thak("4.4.7", gives="ṭhan", of=("nau",), sense="tarati",
         case="tṛtīyā", excepts=("4.4.5",),
         why="नौद्व्यचष्ठन्, ठकोऽपवादः; the नौ half. नावा तरति "
             "**नाविकः**, a sailor"),
    Thak("4.4.7", gives="ṭhan", vowels="dvyac", sense="tarati",
         case="tṛtīyā", excepts=("4.4.5",),
         why="नौद्व्यचष्ठन्, the द्व्यच् half. घटिकः, प्लविकः, "
             "बाहुकः — one who crosses by a pot, a float, his own "
             "arms. **षकारः सांहितिको नानुबन्धः**: the ष् in the "
             "sūtra is there by sandhi and is not a marker, so the "
             "feminine is बाहुका and not बाहुकी.\\n\\n"
             "**AND A KĀRIKĀ COUNTS THE ष-INITIAL AFFIXES OF THE "
             "WHOLE SECTION.** आकर्षात् पर्पादेर्भस्त्रादिभ्यः "
             "कुसीदसूत्राच्च / आवसथात् किशरादेः **षितः षडेते "
             "ठगधिकारे** — six of them in the ठक् section, from six "
             "named grounds. And then the correction: "
             "**विधिवाक्यापेक्षं च षट्त्वम्, प्रत्ययास्तु सप्त** — "
             "six as far as the rule-STATEMENTS go, but seven "
             "affixes, because one rule gives two. A count offered "
             "and immediately qualified by what it counts"),
    Thak("4.4.8", gives="ṭhak", sense="carati", case="tṛtīyā",
         why="चरति. **चरतिर्भक्षणे गतौ च वर्तते** — चर् is both "
             "eating and going. दध्ना चरति **दाधिकः**, one who takes "
             "his food with curds; हास्तिकः, शाकटिकः, one who travels "
             "by elephant or by cart"),
    Thak("4.4.9", gives="ṣṭhal", of=("ākarṣa",), sense="carati",
         case="tṛtīyā", excepts=("4.4.8",),
         why="आकर्षात् ष्ठल्, ठकोऽपवादः. **लकारः स्वरार्थः, षकारो "
             "ङीषर्थः** — the ल् for the accent and the ष् for the "
             "feminine. आकर्षेण चरति **आकर्षिकः**, आकर्षिकी.\\n\\n"
             "**आकर्ष इति सुवर्णपरीक्षार्थो निकषोपल उच्यते** — an "
             "आकर्ष is the touchstone one tests gold on, and the "
             "derived word is the man who goes about with one. The "
             "first of the six the kārikā counts"),
    Thak("4.4.10", gives="ṣṭhan", gana="parpādi", sense="carati",
         case="tṛtīyā", excepts=("4.4.8",),
         why="पर्पादिभ्यः ष्ठन्, ठकोऽपवादः. **नकारः स्वरार्थः, "
             "षकारो ङीषर्थः**. पर्पिकः, पर्पिकी; अश्विकः, अश्विकी. "
             "A गणसूत्र rides with the list — **पादः पच्च**, and पाद "
             "gives पदिकः. The second of the six"),
    Thak("4.4.11", gives="ṭhañ", also_gives=("ṣṭhan",),
         of=("śvagaṇa",), sense="carati", case="tṛtīyā",
         excepts=("4.4.8",),
         why="श्वगणाट् ठञ् च, ठकोऽपवादः — the च bringing ष्ठन् along. "
             "श्वगणेन चरति **श्वागणिकः**, श्वागणिकी, a man who goes "
             "about with a pack of dogs; and by the ष्ठन् श्वगणिकः, "
             "श्वगणिकी.\\n\\n"
             "**AND A VĀRTTIKA NINE HUNDRED SŪTRAS AWAY IS WRITTEN "
             "FOR THIS WORD.** श्वादेरिञि [7.3.8] इत्यत्र वक्ष्यति — "
             "**इकारादिग्रहणं च कर्तव्यं श्वागणिकाद्यर्थम्**, and "
             "**तेन ठञि द्वारादिकार्यं न भवति**: the supplement is "
             "added there so that the द्वारादि operation does not "
             "reach the form this rule makes"),
    Thak("4.4.12", gives="ṭhak", gana="vetanādi", sense="jīvati",
         case="tṛtīyā",
         why="वेतनादिभ्यो जीवति. वेतनेन जीवति **वैतनिको कर्मकरः**, a "
             "hired workman — one who lives by his wage.\\n\\n"
             "**धनुर्दण्डग्रहणमत्र संघातविगृहीतार्थम्** — धनुर्दण्ड "
             "is in the list so the rule reaches the compound AND "
             "each of its members: धानुर्दण्डिकः, **धानुष्कः**, "
             "दाण्डिकः. The bowman and the staff-bearer out of one "
             "entry"),
    Thak("4.4.13", gives="ṭhan", of=("vasna", "kraya", "vikraya"),
         sense="jīvati", case="tṛtīyā", excepts=("4.4.12",),
         why="वस्नक्रयविक्रयाट् ठन्, ठकोऽपवादः. वस्नेन जीवति "
             "**वस्निकः**, one who lives by wages.\\n\\n"
             "**क्रयविक्रयग्रहणं संघातविगृहीतार्थम्** — the same "
             "device as the last rule's, and the same three forms: "
             "क्रयविक्रयिकः, क्रयिकः, विक्रयिकः. A trader in both, a "
             "buyer, a seller"),
    Thak("4.4.14", gives="cha", also_gives=("ṭhak",), of=("āyudha",),
         sense="jīvati", case="tṛtīyā",
         why="आयुधाच्छ च — the छ, and by the च the ठक् as well, so "
             "both stand. आयुधेन जीवति **आयुधीयः**, **आयुधिकः**: one "
             "who lives by arms"),
    Thak("4.4.15", gives="ṭhak", gana="utsaṅgādi", sense="harati",
         case="tṛtīyā",
         why="हरत्युत्सङ्गादिभ्यः, तेनेत्येव. **हरतिर्देशान्तर"
             "प्रापणे वर्तते** — हृ here is carrying from one place "
             "to another. उत्सङ्गेन हरति **औत्सङ्गिकः**, one who "
             "carries in his lap; औडुपिकः"),
    Thak("4.4.16", gives="ṣṭhan", gana="bhastrādi", sense="harati",
         case="tṛtīyā", excepts=("4.4.15",),
         why="भस्त्रादिभ्यः ष्ठन्. भस्त्रया हरति **भस्त्रिकः**, "
             "भस्त्रिकी, one who carries in a leather bag; भरटिकः, "
             "भरटिकी. The third of the six the kārikā counts"),
    Thak("4.4.17", gives="ṣṭhan", of=("vivadha", "vīvadha"),
         optional=True, sense="harati", case="tṛtīyā",
         excepts=("4.4.15",),
         why="विभाषा विवधवीवधात्, हरतीत्येव. **तेन मुक्ते प्रकृतष्ठग् "
             "भवति** — where the option lets this affix go, the ठक् "
             "of the heading comes back. विवधिकः and वैवधिकः both, "
             "and the feminines विवधिकी, वैवधिकी.\\n\\n"
             "**विवधवीवधशब्दौ समानार्थौ पथि पर्याहारे च वर्तेते** — "
             "the two words mean the same and denote both a road and "
             "a carrying-pole"),
    Thak("4.4.18", gives="aṇ", of=("kuṭilikā",), sense="harati",
         case="tṛtīyā", excepts=("4.4.15",),
         why="अण् कुटिलिकायाः, हरतीत्येव. **कुटिलिका वक्रगतिः, "
             "कर्माराणामायुधकर्षणी लोहमयी यष्टिश्चोच्यते** — a "
             "कुटिलिका is a crooked movement, and also the iron rod "
             "a smith draws his work with. So one word gives two "
             "quite different men: कुटिलिकया हरति मृगो व्याधं "
             "**कौटिलिको मृगः**, the deer that leads the hunter off "
             "by its swerving, and कुटिलिकया हरत्यङ्गारान् "
             "**कौटिलिकः कर्मारः**, the smith who draws the coals "
             "with his rod"),
    Thak("4.4.19", gives="ṭhak", gana="akṣadyūtādi", sense="nirvṛtta",
         case="tṛtīyā",
         why="निर्वृत्तेऽक्षद्यूतादिभ्यः, तेनेत्येव. अक्षद्यूतेन "
             "निर्वृत्तम् **आक्षद्यूतिकं वैरम्**, a feud brought "
             "about by a game of dice; जानुप्रहृतिकम्, one caused by "
             "a blow with the knee. The list is a catalogue of "
             "quarrels and their causes"),
    Thak("4.4.20", gives="map", of_samjna="ktri-anta", sense="nirvṛtta",
         case="tṛtīyā", excepts=("4.4.19",),
         why="क्त्रेर्मम् नित्यम्, निर्वृत्त इत्येव. **ड्वितः "
             "क्त्रिः** [3.3.88] इत्ययं त्रिशब्दो गृह्यते — the "
             "त्रि meant is the affix that rule gives. डुपचष् पाके: "
             "**पक्त्रिमम्**; डुवप्: उप्त्रिमम्; डुकृञ्: "
             "**कृत्रिमम्**, artificial, and the word survives in "
             "every Indian language.\\n\\n"
             "**नित्यग्रहणं स्वातन्त्र्यनिवृत्त्यर्थम्** — *always* "
             "is said to take away the word's independence: a stem "
             "ending in that क्त्रि must ALWAYS carry this affix and "
             "may not be used without it. A rule making one affix "
             "inseparable from another"),
    Thak("4.4.21", gives="kak", of=("apamitya",), sense="nirvṛtta",
         case="tṛtīyā", excepts=("4.4.19",),
         why="अपमित्ययाचिताभ्यां कक्कनौ, यथासंख्यम्; the first of the "
             "two. **आपमित्यकम्** — what has been brought about by "
             "borrowing"),
    Thak("4.4.21", gives="kan", of=("yācita",), sense="nirvṛtta",
         case="tṛtīyā", excepts=("4.4.19",),
         why="अपमित्ययाचिताभ्यां कक्कनौ, the second. **याचितकम्** — "
             "what has been brought about by asking. Two bases and "
             "two affixes matched in order, and the affixes differ in "
             "one letter"),
    Thak("4.4.22", gives="ṭhak", sense="saṃsṛṣṭa", case="tṛtīyā",
         why="संसृष्टे, तेनेत्येव. **संसृष्टमेकीभूतमभिन्नमित्यर्थः** "
             "— mixed, become one, not separable. दध्ना संसृष्टं "
             "**दाधिकम्**; मारिचिकम्, शार्ङ्गवेरिकम्, पैप्पलिकम् — "
             "food mixed with curds, with pepper, with ginger, with "
             "long pepper"),
    Thak("4.4.23", gives="ini", of=("cūrṇa",), sense="saṃsṛṣṭa",
         case="tṛtīyā", excepts=("4.4.22",),
         why="चूर्णादिनिः, ठकोऽपवादः. चूर्णैः संसृष्टाः **चूर्णिनो "
             "ऽपूपाः**, cakes mixed with powder; चूर्णिनो धानाः"),
    Thak("4.4.24", of=("lavaṇa",), sense="saṃsṛṣṭa", case="tṛtīyā",
         elides=True, excepts=("4.4.22",),
         why="लवणाल्लुक्. **संसृष्ट इत्यनेनोत्पन्नस्य ठको लवणशब्दाद् "
             "लुग् भवति** — the ठक् given in this sense goes after "
             "लवण. **लवणः सूपः**, salted soup; लवणं शाकम्, लवणा "
             "यवागूः.\\n\\n"
             "**द्रव्यवाची लवणशब्दो लुकं प्रयोजयति, न गुणवाची** — "
             "and only where लवण names the SUBSTANCE salt, not where "
             "it names the quality of being salty. A homonym split by "
             "which of its two senses is meant"),
    Thak("4.4.25", gives="aṇ", of=("mudga",), sense="saṃsṛṣṭa",
         case="tṛtīyā", excepts=("4.4.22",),
         why="मुद्गादण्, ठकोऽपवादः. **मौद्ग ओदनः**, rice mixed with "
             "beans; मौद्गी यवागूः"),
    Thak("4.4.26", gives="ṭhak", of_samjna="vyañjana", sense="upasikta",
         case="tṛtīyā",
         why="व्यञ्जनैरुपसिक्ते, तेनेत्येव. From any word for a "
             "SEASONING, in the sense *sprinkled with it*. दध्ना "
             "उपसिक्तं **दाधिकम्**; सौपिकम्, खारिकम्.\\n\\n"
             "व्यञ्जनैरिति किम्? **उदकेनोपसिक्त ओदनः** — rice "
             "sprinkled with water takes nothing, water being no "
             "seasoning",
         keeps_out="उदकेनोपसिक्त ओदनः"),
    Thak("4.4.27", gives="ṭhak", of=("ojas", "sahas", "ambhas"),
         sense="vartate", case="tṛtīyā",
         why="ओजःसहोऽम्भसा वर्तते. ओजसा वर्तते **औजसिकः शूरः**, a "
             "hero who lives by his strength; **साहसिकश्चौरः**, a "
             "robber who lives by force; **आम्भसिको मत्स्यः**, a fish "
             "that lives by water. Three words, three creatures, and "
             "each named by what it goes on"),
    Thak("4.4.28", gives="ṭhak", pre="prati-anu",
         of=("īpa", "loman", "kūla"), sense="vartate", case="dvitīyā",
         why="तत् प्रत्यनुपूर्वमीपलोमकूलम्. **तदिति "
             "द्वितीयासमर्थविभक्तिः** — and here the case changes to "
             "the ACCUSATIVE, the first time in this pāda. प्रतीपं "
             "वर्तते **प्रातीपिकः**, one who goes against the "
             "stream; आन्वीपिकः, with it; प्रातिलोमिकः and "
             "आनुलोमिकः, against and with the grain; प्रातिकूलिकः "
             "and आनुकूलिकः, against and with the bank.\\n\\n"
             "**AND AN INTRANSITIVE VERB GIVEN AN OBJECT.** ननु च "
             "वृतिरकर्मकः, तस्य कथं कर्मणा संबन्धः? — वृत् takes no "
             "object, so how can it have one here? "
             "**क्रियाविशेषणमकर्मकाणामपि कर्म भवति**: what qualifies "
             "the action counts as an object even for a verb that "
             "has none. Which is why the case could change at all"),
    Thak("4.4.29", gives="ṭhak", of=("parimukha",), sense="vartate",
         case="dvitīyā",
         why="परिमुखं च. परिमुखं वर्तते **पारिमुखिकः**. "
             "**चकारोऽनुक्तसमुच्चयार्थः** — the च gathers what has "
             "not been said, so पारिपार्श्विकः comes in too: an "
             "attendant who stays at one's side"),
    Thak("4.4.30", gives="ṭhak", sense="prayacchati", result="garhya",
         case="dvitīyā",
         why="प्रयच्छति गर्ह्यम्, तदित्येव — and only where what is "
             "given is BLAMEWORTHY. **द्विगुणार्थं द्विगुणम्, "
             "तादर्थ्यात् ताच्छब्द्यम्**: *double* stands for *for "
             "the sake of double*, a word taking the name of what it "
             "is for. द्विगुणं प्रयच्छति **द्वैगुणिकः**, a usurer "
             "who lends at double; त्रैगुणिकः.\\n\\n"
             "A vārttika supplies another shape: **वृद्धेर्वृधुषिभावो "
             "वक्तव्यः** — **वार्धुषिकः**, and "
             "**प्रकृत्यन्तरं वा वृद्धिपर्यायो वृधुषिशब्दः**, or "
             "else वृधुषि is simply another word for interest.\\n\\n"
             "गर्ह्यमिति किम्? **द्विगुणं प्रयच्छत्यधमर्णः** — the "
             "DEBTOR who repays double is doing nothing blameworthy, "
             "and gets no affix",
         keeps_out="द्विगुणं प्रयच्छत्यधमर्णः"),
    Thak("4.4.31", gives="ṣṭhan", of=("kusīda",), sense="prayacchati",
         result="garhya", case="dvitīyā", excepts=("4.4.30",),
         why="कुसीददशैकादशात् ष्ठन्ष्ठचौ, यथासंख्यम्; ठकोऽपवादौ. "
             "**कुसीदं वृद्धिः, तदर्थं द्रव्यं कुसीदम्** — कुसीद is "
             "interest, and by transfer the capital lent for it. "
             "कुसीदं प्रयच्छति **कुसीदिकः**, कुसीदिकी.\n\n"
             "AND THIS IS THE RULE THAT MAKES 4.4.7's COUNT SEVEN. "
             "That kārikā named six grounds for the ष-initial affixes "
             "of the section and then said **विधिवाक्यापेक्षं च "
             "षट्त्वम्, प्रत्ययास्तु सप्त** — six statements, seven "
             "affixes. This is the statement that gives two"),
    Thak("4.4.31", gives="ṣṭhac", of=("daśaikādaśa",),
         sense="prayacchati", result="garhya", case="dvitīyā",
         excepts=("4.4.30",),
         why="कुसीददशैकादशात् ष्ठन्ष्ठचौ, the second of the two. "
             "**एकादशार्था दश दशैकादशशब्देनोच्यते** — ten lent for "
             "eleven, the whole transaction in one word. "
             "**दशैकादशिकः**, दशैकादशिकी: a man who lends at ten per "
             "cent, and the rule is still under 4.4.30's गर्ह्य"),
    Thak("4.4.32", gives="ṭhak", sense="uñchati", case="dvitīyā",
         why="उञ्छति, तदिति द्वितीयासमर्थात्. **भूमौ पतितस्यैकैकस्य "
             "कणस्योपादानमुञ्छः** — gleaning is taking up the fallen "
             "grains one by one. बदराण्युञ्छति **बादरिकः**; "
             "श्यामाकिकः, काणिकः"),
    Thak("4.4.33", gives="ṭhak", sense="rakṣati", case="dvitīyā",
         why="रक्षति. समाजं रक्षति **सामाजिकः**, one who keeps order "
             "at an assembly; सांनिवेशिकः"),
    Thak("4.4.34", gives="ṭhak", of=("śabda", "dardura"),
         sense="karoti", case="dvitīyā",
         why="शब्ददर्दुरं करोति. शब्दं करोति **शाब्दिको वैयाकरणः** — "
             "*one who makes words* is the grammarian, and the "
             "grammar names its own practitioner by a rule of its "
             "own. **दार्दुरिकः कुम्भकारः**, the potter who makes "
             "the drum"),
    Thak("4.4.35", gives="ṭhak", of=("pakṣin", "matsya", "mṛga"),
         sense="hanti", case="dvitīyā",
         why="पक्षिमत्स्यमृगान् हन्ति. पक्षिणो हन्ति **पाक्षिकः**; "
             "मात्स्यिकः; मार्गिकः.\n\n"
             "**AND A NAME REACHES ITS SYNONYMS AND ITS SPECIES.** "
             "**स्वरूपस्य पर्यायाणां तद्विशेषाणां च ग्रहणमिहेष्यते** "
             "— the word itself, the words that mean the same, and "
             "the words for KINDS of the thing. So from पक्षिन् come "
             "शाकुनिकः by a synonym and मायूरिकः, तैत्तिरिकः by "
             "species; from मत्स्य, मैनिकः, शाफरिकः, शाकुलिकः; from "
             "मृग, हारिणिकः, सौकरिकः, सारङ्गिकः. Three words in the "
             "rule and a whole vocabulary of hunters out of them"),
    Thak("4.4.36", gives="ṭhak", of=("paripantha",), sense="tiṣṭhati",
         case="dvitīyā",
         why="परिपन्थं च तिष्ठति. परिपन्थं तिष्ठति **पारिपन्थिकश् "
             "चौरः** — the robber who waits on the road.\n\n"
             "**चकारो भिन्नक्रमः प्रत्ययार्थं समुच्चिनोति** — the च "
             "stands out of its place and gathers a second sense: "
             "परिपन्थं हन्ति पारिपन्थिकः, one who STRIKES on the "
             "road as well as one who waits there.\n\n"
             "**समर्थविभक्तिप्रकरणे पुनर्द्वितीयोच्चारणं "
             "लौकिकवाक्यप्रदर्शनार्थम्** — the accusative is uttered "
             "again inside a section that already had it, to show the "
             "everyday sentence; and **परिपथशब्दपर्यायः "
             "परिपन्थशब्दोऽस्तीति ज्ञापयति**, which indicates that "
             "परिपन्थ is a synonym of परिपथ, **स विषयान्तरेऽपि "
             "प्रयोक्तव्यः**, to be used elsewhere too"),
    Thak("4.4.37", gives="ṭhak", stem_final="mātha", sense="dhāvati",
         case="dvitīyā",
         why="माथोत्तरपदपदव्यनुपदं धावति, the माथ-ending half. "
             "दण्डमाथं धावति **दाण्डमाथिकः**; शौल्कमाथिकः. "
             "**माथशब्दः पथिपर्यायः** — माथ is another word for a "
             "road"),
    Thak("4.4.37", gives="ṭhak", of=("padavī", "anupada"),
         sense="dhāvati", case="dvitīyā",
         why="माथोत्तरपदपदव्यनुपदं धावति, the two named words. "
             "**पादविकः**, one who runs on the track; **आनुपदिकः**, "
             "one who runs at another's heels"),
    Thak("4.4.38", gives="ṭhañ", also_gives=("ṭhak",),
         of=("ākranda",), sense="dhāvati", case="dvitīyā",
         why="आक्रन्दाट् ठञ् च — the ठञ्, and by the च the ठक् too; "
             "**स्वरे विशेषः**, and the two differ only in the "
             "accent. **आक्रन्दिकः**, आक्रन्दिकी.\n\n"
             "The base is read two ways and both are kept: "
             "**आक्रन्दन्त्येतस्मिन्नित्याक्रन्दो देशः** — a place "
             "where people cry out; **अथवाक्रन्द्यत इत्याक्रन्द "
             "आर्तायनमुच्यते**, or the cry for help itself. "
             "**विशेषाभावाद् द्वयोरपि ग्रहणम्**: nothing separates "
             "them, so both are taken"),
    Thak("4.4.39", gives="ṭhak", stem_final="pada", sense="gṛhṇāti",
         case="dvitīyā",
         why="पदोत्तरपदं गृह्णाति. पूर्वपदं गृह्णाति "
             "**पौर्वपदिकः**; औत्तरपदिकः — and both are the "
             "grammarians' own words for the first and last member "
             "of a compound.\n\n"
             "**पदान्तादिति नोक्तम् — बहुच्पूर्वान् मा भूदिति** — "
             "the rule says *last member* and not *ending in पद*, so "
             "that a पद preceded by बहुच् does not come in. The same "
             "argument 4.2.137 made with the same word"),
    Thak("4.4.40", gives="ṭhak",
         of=("pratikaṇṭha", "artha", "lalāma"), sense="gṛhṇāti",
         case="dvitīyā",
         why="प्रतिकण्ठार्थललामं च. प्रतिकण्ठं गृह्णाति "
             "**प्रातिकण्ठिकः**, one who learns by heart; "
             "**आर्थिकः**, one who takes the sense; लालामिकः"),
    Thak("4.4.41", gives="ṭhak", of=("dharma",), sense="carati",
         case="dvitīyā",
         why="धर्मं चरति. **चरतिरासेवायां नानुष्ठानमात्रे** — चर् "
             "here is PRACTISING habitually and not merely "
             "performing once. धर्मं चरति **धार्मिकः**. And a "
             "vārttika: **अधर्माच्चेति वक्तव्यम्** — आधर्मिकः, one "
             "who practises the opposite"),
    Thak("4.4.42", gives="ṭhan", also_gives=("ṭhak",),
         of=("pratipatha",), sense="eti", case="dvitīyā",
         why="प्रतिपथमेति ठंश्च — the ठन्, and by the च the ठक् too. "
             "प्रतिपथमेति **प्रतिपथिकः**, **प्रातिपथिकः**: one who "
             "goes to meet another on the road"),
    Thak("4.4.43", gives="ṭhak", of_samjna="samavāya",
         sense="samavaiti", case="dvitīyā",
         why="समवायान् समवैति. **समवायः समूह उच्यते, न "
             "संप्रधारणा** — a समवाय here is a GATHERING and not a "
             "deliberation; **समवैति आगत्य तदेकदेशीभवतीत्यर्थः**, to "
             "come and become part of it. समवायान् समवैति "
             "**सामवायिकः**; सामाजिकः, सामूहिकः. **समवायानिति "
             "बहुवचनं स्वरूपविधिनिरासार्थम्**"),
    Thak("4.4.44", gives="ṇya", of=("pariṣad",), sense="samavaiti",
         case="dvitīyā", excepts=("4.4.43",),
         why="परिषदो ण्यः, ठकोऽपवादः. परिषदं समवैति **पारिषद्यः** — "
             "one who attends an assembly"),
    Thak("4.4.45", gives="ṇya", of=("senā",), optional=True,
         sense="samavaiti", case="dvitīyā", excepts=("4.4.43",),
         why="सेनाया वा, ठकोऽपवादः; **पक्षे सोऽपि भवति**. सेनां "
             "समवैति **सैन्यः** and **सैनिकः** — and both words for "
             "a soldier survive, one by each side of the option"),
    Thak("4.4.46", gives="ṭhak", of=("lalāṭa", "kukkuṭī"),
         sense="paśyati", result="saṃjñā", case="dvitīyā",
         why="संज्ञायां ललाटकुक्कुट्यौ पश्यति. "
             "**संज्ञाग्रहणमभिधेयनियमार्थम्, न तु रूढ्यर्थम्** — the "
             "word *name* restricts what is denoted and does not make "
             "the form conventional.\n\n"
             "**AND BOTH RESULTS ARE IDIOMS THE VṚTTI HAS TO "
             "EXPLAIN.** ललाटं पश्यति **लालाटिकः सेवकः**: "
             "सर्वावयवेभ्यो ललाटं दूरे दृश्यते — of all the parts of "
             "a man the forehead is seen from farthest off, so *one "
             "who looks at the forehead* is the servant who keeps his "
             "distance, **स्वामिनः कार्येषु नोपतिष्ठते**, never at "
             "hand for his master's business.\n\n"
             "**कौक्कुटिको भिक्षुः**: कुक्कुटीशब्देनापि कुक्कुटीपातो "
             "लक्ष्यते — the hen's word stands for a hen's stride, "
             "and **देशस्याल्पतया हि भिक्षुरविक्षिप्तदृष्टिः "
             "पादविक्षेपदेशे चक्षुः संयम्य गच्छति**: the monk who "
             "walks with his eyes fixed on the little patch his foot "
             "will fall on. Two words for two kinds of downcast "
             "look, and neither is derivable without the story"),
    Thak("4.4.47", gives="ṭhak", sense="dharmya", case="ṣaṣṭhī",
         why="तस्य धर्म्यम्, षष्ठीसमर्थात्. **धर्म्यं न्याय्यम्, "
             "आचारयुक्तमित्यर्थः** — what is right, what accords with "
             "usage. शुल्कशालाया धर्म्यं **शौल्कशालिकम्**, the "
             "customs-house's due; आकरिकम्, आपणिकम्, गौल्मिकम्. And "
             "the case changes to the genitive here"),
    Thak("4.4.48", gives="aṇ", gana="mahiṣyādi", sense="dharmya",
         case="ṣaṣṭhī", excepts=("4.4.47",),
         why="अण् महिष्यादिभ्यः, ठकोऽपवादः. महिष्या धर्म्यं "
             "**माहिषम्**, what is due to the chief queen; "
             "प्राजावतम्. The list runs from the queen through the "
             "purohita to the sacrificer and the हॊतृ"),
    Thak("4.4.49", gives="añ", stem_final="ṛ", sense="dharmya",
         case="ṣaṣṭhī", excepts=("4.4.47",),
         why="ऋतोऽञ्, ठकोऽपवादः. पोतुर्धर्म्यं **पौत्रम्**; "
             "औद्गात्रम् — the dues of the Potṛ and the Udgātṛ "
             "priests.\n\n"
             "Three vārttikas add shapes. **नराच्चेति वक्तव्यम्** — "
             "नरस्य धर्म्या **नारी**, and the ordinary word for a "
             "woman is made by this rule. **विशसितुरिड्लोपश्च** — "
             "वैशस्त्रम्; **विभाजयितुर्णिलोपश्च** — वैभाजित्रम्"),
    Thak("4.4.50", gives="ṭhak", sense="avakraya", case="ṣaṣṭhī",
         why="अवक्रयः, तस्येत्येव. **अवक्रीणीतेऽनेनेत्यवक्रयः, "
             "पिण्डक उच्यते** — the rent by which a thing is farmed. "
             "शुल्कशालाया अवक्रयः **शौल्कशालिकः**; आकरिकः, आपणिकः, "
             "गौल्मिकः.\n\n"
             "**नन्ववक्रयोऽपि धर्म्यमेव? नैतदस्ति; लोकपीडया "
             "धर्मातिक्रमेणाप्यवक्रयो भवति** — is rent not also what "
             "is DUE, and so covered by the rule before? No: rent can "
             "be exacted to the people's hurt and in defiance of "
             "right, and the two senses part company there"),
    Thak("4.4.51", gives="ṭhak", sense="paṇya", case="prathamā",
         why="तदस्य पण्यम्, प्रथमासमर्थाद् अस्येति षष्ठ्यर्थे. "
             "अपूपाः पण्यमस्य **आपूपिकः**, a man whose wares are "
             "cakes; शाष्कुलिकः, मौदकिकः. The case changes again — "
             "the base in the nominative and the relation a "
             "genitive.\n\n"
             "**पण्यमिति विशेषणं तद्धितवृत्तावन्तर्भूतम्, अतः "
             "पण्यशब्दो न प्रयुज्यते** — the qualifier is taken up "
             "INTO the derived word, so the word *wares* is not used "
             "beside it. आपूपिकः already says it"),
    Thak("4.4.52", gives="ṭhañ", of=("lavaṇa",), sense="paṇya",
         case="prathamā", excepts=("4.4.51",),
         why="लवणाट् ठञ्, ठकोऽपवादः; **स्वरे विशेषः**. लवणं पण्यमस्य "
             "**लावणिकः**, a salt-merchant — and the same word whose "
             "affix 4.4.24 removed in another sense"),
    Thak("4.4.53", gives="ṣṭhan", gana="kiśarādi", sense="paṇya",
         case="prathamā", excepts=("4.4.51",),
         why="किशरादिभ्यः ष्ठन्, ठकोऽपवादः. **किशरादयो "
             "गन्धविशेषवचनाः** — the list is of particular perfumes. "
             "किशराः पण्यमस्य **किशरिकः**, किशरिकी; नरदिकः, "
             "नरदिकी. The fifth of the six the kārikā at 4.4.7 "
             "counts"),
    Thak("4.4.54", gives="ṣṭhan", of=("śalālu",), optional=True,
         sense="paṇya", case="prathamā", excepts=("4.4.51",),
         why="शलालुनोऽन्यतरस्याम्, ठकोऽपवादः; पक्षे सोऽपि भवति. "
             "**शलालुशब्दो गन्धविशेषवचनः** — another perfume. "
             "**शलालुकः**, शलालुकी; and by the option **शालालुकः**, "
             "शालालुकी"),
    Thak("4.4.55", gives="ṭhak", sense="śilpa", case="prathamā",
         why="शिल्पम्, तदस्येत्येव. **शिल्पं कौशलम्** — a craft is a "
             "skill. मृदङ्गवादनं शिल्पमस्य **मार्दङ्गिकः**, a "
             "drummer; पाणविकः, **वैणिकः**, a lutanist.\n\n"
             "**मृदङ्गवादने वर्तमानो मृदङ्गशब्दः प्रत्ययमुत्पादयति** "
             "— the word मृदङ्ग stands for the PLAYING of the drum "
             "and it is that which takes the affix; **शिल्पं "
             "तद्धितवृत्तावन्तर्भवति**, and the qualifier is absorbed "
             "as it was four sūtras back"),
    Thak("4.4.56", gives="aṇ", of=("maḍḍuka", "jharjhara"),
         optional=True, sense="śilpa", case="prathamā",
         excepts=("4.4.55",),
         why="मड्डुकझर्झरादण् अन्यतरस्याम्, ठकोऽपवादः; पक्षे सोऽपि "
             "भवति. मड्डुकवादनं शिल्पमस्य **माड्डुकः**, माड्डुकिकः; "
             "**झार्झरः**, झार्झरिकः — two more drums and two forms "
             "each"),
    Thak("4.4.57", gives="ṭhak", sense="praharaṇa", case="prathamā",
         why="प्रहरणम्, तदस्येत्येव. असिः प्रहरणमस्य **आसिकः**, a "
             "swordsman; प्रासिकः, चाक्रिकः, **धानुष्कः** — and that "
             "last is the same word 4.4.12's compound-entry produced "
             "in quite another sense"),
    Thak("4.4.58", gives="ṭhañ", also_gives=("ṭhak",),
         of=("paraśvadha",), sense="praharaṇa", case="prathamā",
         excepts=("4.4.57",),
         why="परश्वधाट् ठञ् च — the ठञ्, and by the च the ठक्; "
             "**स्वरे विशेषः**. परश्वधः प्रहरणमस्य **पारश्वधिकः**, "
             "an axeman"),
    Thak("4.4.59", gives="īkak", of=("śakti", "yaṣṭi"),
         sense="praharaṇa", case="prathamā", excepts=("4.4.57",),
         why="शक्तियष्ट्योरीकक्, ठकोऽपवादः. शक्तिः प्रहरणमस्य "
             "**शाक्तीकः**; **याष्टीकः** — the spearman and the "
             "staff-fighter"),
    Thak("4.4.60", gives="ṭhak", of=("asti", "nāsti", "diṣṭa"),
         sense="mati", case="prathamā",
         why="अस्तिनास्तिदिष्टं मतिः, तदस्येत्येव. अस्ति मतिरस्य "
             "**आस्तिकः**; नास्ति मतिरस्य **नास्तिकः**; "
             "**दैष्टिकः**.\n\n"
             "**AND THE RULE IS NOT ABOUT HAVING AN OPINION.** "
             "**न च मतिसत्तामात्रे प्रत्यय इष्यते; किं तर्हि? "
             "परलोकोऽस्तीति यस्य मतिरस्ति, स आस्तिकः** — one whose "
             "conviction is that the next world IS; **तद्विपरीतो "
             "नास्तिकः**, and one whose conviction runs the other "
             "way. **प्रमाणानुपातिनी यस्य मतिः स दैष्टिकः**, one "
             "whose conviction follows the evidence. Three words for "
             "three stances, and **तदेतदभिधानशक्तिस्वभावाल् "
             "लभ्यते**: got from the nature of what the words can "
             "denote, not from anything the rule says.\n\n"
             "**अस्तिनास्तिशब्दौ निपातौ, वचनसामर्थ्याद् वा "
             "आख्याताद् वाक्याच् च प्रत्ययः** — the first two are "
             "particles, or else the affix comes from a finite verb "
             "and from a whole sentence, as the vārttikas on 4.4.1 "
             "already allowed"),
    Thak("4.4.61", gives="ṭhak", sense="śīla", case="prathamā",
         why="शीलम्, तदस्येत्येव. **शीलं स्वभावः** — a habit is a "
             "man's nature. अपूपभक्षणं शीलमस्य **आपूपिकः**; "
             "शाष्कुलिकः, मौदकिकः. **भक्षणक्रिया तद्विशेषणं च शीलं "
             "तद्धितवृत्तावन्तर्भवति** — the eating, and the habit "
             "that qualifies it, are both taken up into the derived "
             "word: आपूपिकः already says *given to eating cakes*"),
    Thak("4.4.62", gives="ṇa", gana="chatrādi", sense="śīla",
         case="prathamā", excepts=("4.4.61",),
         why="छत्रादिभ्यो णः, ठकोऽपवादः. **छादनादावरणाच्छत्रम्** — a "
             "छत्र is from covering. And the derived word is "
             "explained at length: **गुरुकार्येष्ववहितस्तच्छिद्रा"
             "वरणप्रवृत्तश्छत्रशीलः शिष्यश्छात्रः** — the pupil who "
             "attends to his teacher's affairs and makes it his "
             "habit to COVER his faults is a **छात्रः**. The "
             "ordinary word for a student, and it means one who "
             "shelters his master.\n\n"
             "**स्थाशब्दोऽत्र पठ्यते, स चोपसर्गपूर्वोऽत्र गृह्यते** "
             "— स्था is in the list and is taken only with a "
             "preverb: आस्था, संस्था, अवस्था"),
    Thak("4.4.63", gives="ṭhak", sense="karma-adhyayane-vṛtta",
         case="prathamā",
         why="कर्माध्ययने वृत्तम्, तदस्येत्येव. एकमन्यदध्ययने कर्म "
             "वृत्तमस्य **ऐकान्यिकः**; द्वैयन्यिकः, त्रैयन्यिकः.\n\n"
             "**AND THE WORD MEANS A MISTAKE IN RECITATION.** "
             "**यस्याध्ययनप्रयुक्तस्य परीक्षाकाले पठतः स्खलितम् "
             "अपपाठरूपमेकं जातम्, स उच्यत ऐकान्यिकः** — a student "
             "who, reciting at his examination, has slipped ONCE "
             "into a wrong reading. And so द्वैयन्यिकः for twice, "
             "त्रैयन्यिकः for three times. The grammar has a word "
             "for how many errors a pupil made.\n\n"
             "The base is itself compounded first: **एकमन्यदिति "
             "विगृह्य तद्धितार्थो** [2.1.51] इति समासः, and then the "
             "affix. **अध्ययने कर्म वृत्तमित्येतत् सर्वं "
             "तद्धितवृत्तावन्तर्भवति**"),
    Thak("4.4.64", gives="ṭhac", pre="bahvac",
         sense="karma-adhyayane-vṛtta", case="prathamā",
         excepts=("4.4.63",),
         why="बह्वच्पूर्वपदाट् ठच्, ठकोऽपवादः. द्वादशान्यानि "
             "कर्माण्यध्ययने वृत्तान्यस्य **द्वादशान्यिकः**; "
             "त्रयोदशान्यिकः, **चतुर्दशान्यिकः** — *he has made "
             "fourteen wrong readings*.\n\n"
             "And the vṛtti explains what counts as one: **उदात्ते "
             "कर्तव्ये योऽनुदात्तं करोति, स उच्यतेऽन्यत् त्वं "
             "करोषीति** — where an acute was called for and he made "
             "it grave, one says *you are doing something ELSE*. "
             "That is where the अन्य of the compound comes from"),
    Thak("4.4.65", gives="ṭhak", sense="hita", result="bhakṣa",
         case="prathamā",
         why="हितं भक्षाः, तदस्येत्येव. अपूपभक्षणं हितमस्मै "
             "**आपूपिकः**; शाष्कुलिकः, मौदकिकः.\n\n"
             "**AND A CASE-RELATION SILENTLY CHANGED BY WHAT THE "
             "WORDS REQUIRE.** ननु च हितयोगे चतुर्थ्या भवितव्यम्, "
             "तत्र कथं षष्ठ्यर्थे प्रत्ययो विधीयते? — *beneficial* "
             "governs a dative, so how is the affix given in the "
             "sense of a genitive? **एवं तर्हि सामर्थ्याद् "
             "विभक्तिविपरिणामो भविष्यति**: the construction itself "
             "turns the case. The rule says षष्ठी and the sense "
             "requires चतुर्थी, and the requirement wins"),
    Thak("4.4.66", gives="ṭhak", sense="dīyate-niyukta",
         case="prathamā",
         why="तदस्मै दीयते नियुक्तम्. **नियोगेनाव्यभिचारेण दीयते "
             "इत्यर्थः; अव्यभिचारो नियोगः** — given by appointment "
             "and without fail. अग्रे भोजनमस्मै नियुक्तं दीयते "
             "**आग्रभोजनिकः**; आपूपिकः, शाष्कुलिकः.\n\n"
             "**केचित् तु नियुक्तं नित्यमाहुः** — and some say "
             "नियुक्त simply means *always*: अपूपा नित्यमस्मै "
             "दीयन्त आपूपिकः. Two readings recorded and neither "
             "chosen"),
    Thak("4.4.67", gives="ṭiṭhan", of=("śrāṇā", "māṃsaudana"),
         sense="dīyate-niyukta", case="prathamā", excepts=("4.4.66",),
         why="श्राणामांसौदनाट् टिठन्, ठकोऽपवादः. **इकार "
             "उच्चारणार्थः, टकारो ङीबर्थः** — the इ only to make the "
             "affix pronounceable and the ट् for the feminine. "
             "श्राणा नियुक्तमस्मै दीयते **श्राणिकः**, श्राणिकी; "
             "मांसौदनिकः, मांसौदनिकी.\n\n"
             "अथ ठञेव कस्माद् नोक्तः, **न ह्यत्र ठञष्टिठनो वा "
             "विशेषोऽस्ति?** — why not simply ठञ्, when nothing "
             "separates the two? **मांसौदनग्रहणं संघातविगृहीतार्थं "
             "केचिदिच्छन्ति; तत्र वृद्ध्यभावो विशेषः** — because "
             "some read मांसौदन as compound AND parts, and then the "
             "absence of the strengthening is what tells them apart: "
             "ओदनिकः, not औदनिकः"),
    Thak("4.4.68", gives="aṇ", of=("bhakta",), optional=True,
         sense="dīyate-niyukta", case="prathamā", excepts=("4.4.66",),
         why="भक्तादण् अन्यतरस्याम्, ठकोऽपवादः; पक्षे सोऽपि भवति. "
             "भक्तमस्मै दीयते नियुक्तं **भाक्तः**, **भाक्तिकः**"),
    Thak("4.4.69", gives="ṭhak", sense="niyukta", case="saptamī",
         why="तत्र नियुक्तः, सप्तमीसमर्थात्. **नियुक्तोऽधिकृतो "
             "व्यापारित इत्यर्थः** — appointed, put in charge, set "
             "to work. शुल्कशालायां नियुक्तः **शौल्कशालिकः**; "
             "आकरिकः, आपणिकः, गौल्मिकः, **दौवारिकः** — the "
             "doorkeeper. The same four bases 4.4.47 and 4.4.50 used, "
             "in a third sense"),
    Thak("4.4.70", gives="ṭhan", stem_final="agāra", sense="niyukta",
         case="saptamī", excepts=("4.4.69",),
         why="अगारान्ताट् ठन्, ठकोऽपवादः. देवागारे नियुक्तो "
             "**देवागारिकः**; कोष्ठागारिकः, **भाण्डागारिकः** — the "
             "temple-keeper, the granary-keeper, the storekeeper"),
    Thak("4.4.71", gives="ṭhak", of_samjna="adeśa-akāla",
         sense="adhyāyin", case="saptamī",
         why="अध्यायिन्यदेशकालात्, तत्रेत्येव. **अध्ययनस्य यौ "
             "देशकालौ शास्त्रेण प्रतिषिद्धौ तावदेशकालशब्देनोच्येते** "
             "— the *non-place* and *non-time* are the place and the "
             "time at which the śāstra FORBIDS study, and it is from "
             "those that the affix comes.\n\n"
             "श्मशानेऽधीते **श्माशानिकः**, one who studies in a "
             "cremation-ground; चातुष्पथिकः, at a crossroads; and "
             "from the forbidden days चतुर्दश्यामधीते "
             "**चातुर्दशिकः**, आमावास्यिकः. अदेशकालादिति किम्? "
             "स्रुघ्नेऽधीते, पूर्वाह्णेऽधीते — an ordinary place and "
             "an ordinary hour get nothing. A rule that exists only "
             "for what another text prohibits",
         keeps_out="स्रुघ्नेऽधीते, पूर्वाह्णेऽधीते"),
    Thak("4.4.72", gives="ṭhak", stem_final="kaṭhina",
         sense="vyavaharati", case="saptamī",
         why="कठिनान्तप्रस्तारसंस्थानेषु व्यवहरति, the कठिनान्त "
             "half. **व्यवहारः क्रियातत्त्वम्, यथा लौकिकव्यवहार "
             "इति** — dealing is the thing done. वंशकठिने व्यवहरति "
             "**वांशकठिनिकश्चक्रचरः**, the acrobat who works on a "
             "bamboo frame; वार्ध्रकठिनिकः"),
    Thak("4.4.72", gives="ṭhak", of=("prastāra", "saṃsthāna"),
         sense="vyavaharati", case="saptamī",
         why="कठिनान्तप्रस्तारसंस्थानेषु व्यवहरति, the two named "
             "words. **प्रास्तारिकः**, सांस्थानिकः"),
    Thak("4.4.73", gives="ṭhak", of=("nikaṭa",), sense="vasati",
         case="saptamī",
         why="निकटे वसति. **यस्य शास्त्रतो निकटवासस्तत्रायं विधिः** "
             "— the rule is for one whose dwelling-near is laid down "
             "by a text: **आरण्यकेन भिक्षुणा ग्रामात् क्रोशे "
             "वस्तव्यमिति शास्त्रम्**, a forest mendicant must live a "
             "krośa from the village. निकटे वसति **नैकटिको भिक्षुः**. "
             "A grammatical rule whose condition is a monastic one"),
    Thak("4.4.74", gives="ṣṭhal", of=("āvasatha",), sense="vasati",
         case="saptamī", excepts=("4.4.73",),
         why="आवसथात् ष्ठल्, तत्रेत्येव. **लकारः स्वरार्थः, षकारो "
             "ङीषर्थः**. आवसथे वसति **आवसथिकः**, आवसथिकी — one who "
             "lives in a rest-house.\n\n"
             "THE SIXTH AND LAST OF THE KĀRIKĀ'S SIX. 4.4.7's verse "
             "named आकर्ष, पर्पादि, भस्त्रादि, कुसीदसूत्र, आवसथ and "
             "किशरादि as the grounds of the ष-initial affixes in this "
             "section; this is the last of them to arrive.\n\n"
             "**AND IT CLOSES THE ठक् SECTION IN AS MANY WORDS.** "
             "**ठकः पूर्णोऽवधिः, अतः परमन्यः प्रत्ययो विधीयते** — "
             "the ठक्'s limit is complete, and from here another "
             "affix is enjoined. So the heading's LAST RULE is this "
             "one, though the word that MARKS its boundary was "
             "lifted out of 4.4.76"),
    Thak("4.4.75", gives="yat", heading=True, case="dvitīyā",
         why="प्राग्घिताद् यत्. **तस्मै हितम् [5.1.5] इति वक्ष्यति; "
             "प्रागेतस्माद् हितसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामो "
             "यत्प्रत्ययस्तेष्वधिकृतो वेदितव्यः** — यत् is the affix "
             "for every sense named from here to 5.1.4.\n\n"
             "**THE THIRD GREAT प्राक्-HEADING, AND THE FIRST TO "
             "CROSS A CHAPTER.** 4.1.83 bounded अण् by lifting "
             "दीव्यति out of 4.4.2; 4.4.1 bounded ठक् by lifting "
             "वहति out of 4.4.76; this bounds यत् by lifting हित out "
             "of 5.1.5. The same device three times, and this one "
             "reaches out of अध्याय ४ altogether.\n\n"
             "And the heading's own example is the rule that follows: "
             "वक्ष्यति तद्वहति रथयुगप्रासङ्गम् — **रथ्यः, युग्यः, "
             "प्रासङ्ग्यः**"),
    Thak("4.4.76", gives="yat", of=("ratha", "yuga", "prāsaṅga"),
         sense="vahati", case="dvitīyā",
         why="तद्वहति रथयुगप्रासङ्गम्. रथं वहति **रथ्यः**; "
             "**युग्यः**, **प्रासङ्ग्यः** — the horse that draws a "
             "chariot, a yoke, a training-harness.\n\n"
             "**AND THIS IS THE RULE WHOSE WORD BOUNDED THE LAST "
             "HEADING.** वहति was lifted out of it to mark where "
             "ठक् stops — and the rule itself falls under the NEW "
             "heading and gives यत्. A sūtra used as a boundary-post "
             "by one section and governed by another.\n\n"
             "**रथसीताहलेभ्यो यद्विधौ** (महाभाष्यवार्त्तिक on "
             "1.1.72) इति तदन्तविध्युपसंख्यानात् परमरथ्य इत्यपि "
             "भवति — the same vārttika 4.3.121 needed, extending the "
             "rule to compounds ending in these words"),
    Thak("4.4.77", gives="yat", also_gives=("ḍhak",), of=("dhur",),
         sense="vahati", case="dvitīyā",
         why="धुरो यड्ढकौ. धुरं वहति **धुर्यः**, **धौरेयः** — the "
             "beast that bears the yoke-pole, and both words are "
             "still the ordinary ones for a leader"),
    Thak("4.4.78", gives="kha", of=("sarvadhurā",), sense="vahati",
         case="dvitīyā", excepts=("4.4.77",),
         why="खः सर्वधुरात्. सर्वधुरां वहति **सर्वधुरीणः**. "
             "**स्त्रीलिङ्गे न्याय्ये सर्वधुरादिति प्रातिपदिकमात्रा"
             "पेक्षो निर्देशः** — the feminine would have been "
             "proper, and the rule names the bare stem instead. "
             "**ख इति योगविभागः कर्तव्य इष्टसंग्रहार्थः**: and the "
             "rule is to be split, the ख standing alone, so that "
             "उत्तरधुरीणः and दक्षिणधुरीणः come in too"),
    Thak("4.4.79", gives="kha", of=("ekadhurā",), optional=True,
         elides=True, sense="vahati", case="dvitīyā",
         excepts=("4.4.78",),
         why="एकधुराल्लुक् च. एकधुरां वहति **एकधुरीणः** and "
             "**एकधुरः** — the affix and, by the च, its removal. "
             "**वचनसामर्थ्यात् पक्षे लुग् विधीयते**: the mere fact "
             "of the rule being spoken makes the elision optional, "
             "for otherwise it would leave the affix nothing to do"),
    Thak("4.4.80", gives="aṇ", of=("śakaṭa",), sense="vahati",
         case="dvitīyā", excepts=("4.4.76",),
         why="शकटादण्. शकटं वहति **शाकटो गौः** — the ox that draws "
             "a cart"),
    Thak("4.4.81", gives="ṭhak", of=("hala", "sīra"), sense="vahati",
         case="dvitīyā", excepts=("4.4.76",),
         why="हलसीराट् ठक्. हलं वहति **हालिकः**; सैरिकः — the ox "
             "that draws a plough.\n\n"
             "**AND THE SAME RULE STOOD IN THE PĀDA BEFORE.** "
             "4.3.124 हलसीराट् ठक् gives the same affix from the "
             "same two bases, in the sense *what belongs to a "
             "plough*. One pair of words, one affix, and two "
             "senses a whole pāda apart — there the plough's "
             "own gear, here the ox that pulls it"),
    Thak("4.4.82", gives="yat", of=("janī",), result="saṃjñā",
         sense="vahati", case="dvitīyā",
         why="संज्ञायां जन्याः. **जनी वधूरुच्यते** — जनी is the "
             "bride. जनीं वहति **जन्या, जामातुर्वयस्या**: the "
             "bridegroom's friend, **सा हि विहारादिषु "
             "जामातृसमीपं प्रापयति**, because she is the one who "
             "brings the bride to him. A whole social role in one "
             "derived word"),
    Thak("4.4.83", gives="yat", sense="vidhyati", result="adhanuṣā",
         case="dvitīyā",
         why="विध्यत्यधनुषा. पादौ विध्यन्ति **पद्याः शर्कराः**, "
             "gravel that pierces the feet; **ऊरव्याः कण्टकाः**, "
             "thorns that pierce the thighs.\n\n"
             "अधनुषेति किम्? पादौ विध्यति धनुषा. But the objection "
             "goes deeper: **ननु असमर्थत्वादनभिधानाच्च प्रत्ययो न "
             "भवति, न हि धनुषा पद्य इत्युक्ते विवक्षितोऽर्थः "
             "प्रतीयते?** — the exclusion is unnecessary, since the "
             "words would not convey the meaning anyway. "
             "**एवं तर्हि धनुष्प्रतिषेधेन व्यधनक्रिया विशेष्यते — "
             "यस्यां धनुष्करणं न संभाव्यत इति**: the refusal is "
             "therefore read as qualifying the ACT, restricting it to "
             "a piercing in which a bow could not be the instrument. "
             "**तेनेह न भवति — चौरं विध्यति, शत्रुं विध्यति** — and "
             "so a man shot at gets no derived word",
         keeps_out="चौरं विध्यति, शत्रुं विध्यति"),
    Thak("4.4.84", gives="yat", of=("dhana", "gaṇa"), sense="labdhā",
         case="dvitīyā",
         why="धनगणं लब्धा. **धन्यः**, **गण्यः** — one who wins "
             "wealth, one who wins a following. **लब्धेति "
             "तृन्नन्तम्, तेन द्वितीया समर्था विभक्तिर्युज्यते**: "
             "the word is an agent-noun in तृन्, which is why an "
             "accusative can go with it"),
    Thak("4.4.85", gives="ṇa", of=("anna",), sense="labdhā",
         case="dvitīyā", excepts=("4.4.84",),
         why="अन्नाण्णः. अन्नं लब्धा **आन्नः** — one who gets food"),
    Thak("4.4.86", gives="yat", of=("vaśa",), sense="gata",
         case="dvitīyā",
         why="वशं गतः. वशं गतो **वश्यः** — **कामप्राप्तो विधेय "
             "इत्यर्थः**, one brought under another's will and so "
             "subject to him"),
    Thak("4.4.87", gives="yat", of=("pada",), sense="dṛśya",
         case="prathamā",
         why="पदमस्मिन् दृश्यम्. **निर्देशादेव प्रथमा "
             "समर्थविभक्तिः** — the case is read off the wording "
             "itself, the rule naming no case-word. पदं दृश्यमस्मिन् "
             "**पद्यः कर्दमः**; पद्याः पांसवः.\n\n"
             "**शक्यार्थे कृत्यप्रत्ययः; शक्यते** — दृश्य is a "
             "कृत्य and means *can be seen*. **यस्मिन् पदं द्रष्टुं "
             "प्रतिमुद्रोत्पादनेन, स पद्यः कर्दमः**: mud in which a "
             "footprint can be seen because it takes an impression — "
             "**कर्दमस्यावस्थोच्यते नातिद्रवो नातिशुष्क इति**, and "
             "what the word names is a STATE of mud, neither too wet "
             "nor too dry. A rule about the consistency of mud"),
    Thak("4.4.88", gives="yat", of=("mūla",), sense="ābarhi",
         case="prathamā",
         why="मूलमस्याबर्हि. **मूल्या माषाः**, मूल्या मुद्गाः. "
             "**वृहू उद्यमने** — येषां मूलमावृह्यत उत्पाट्यते, ते "
             "मूल्याः, **सुष्ठु निष्पन्नाः**: plants whose root has "
             "to be pulled up, and that means fully grown — "
             "**मूलोत्पाटनेन विना ग्रहीतुं न शक्यन्ते**, they cannot "
             "be taken without uprooting. Ripeness described by how "
             "one has to harvest it"),
    Thak("4.4.89", gives="yat", of=("dhenu",), augment="ṣuk",
         result="saṃjñā", sense="dohana-dattā", case="prathamā",
         why="संज्ञायां धेनुष्या. **धेनोः षुगागमो यश्च प्रत्ययो "
             "निपात्यते** — the षुक् and the affix are laid down "
             "together, and **अन्तोदात्तोऽपि ह्ययमिष्यते**, the "
             "final accent with them.\n\n"
             "**या धेनुरुत्तमर्णाय ऋणप्रदानाद् दोहनार्थं दीयते सा "
             "धेनुष्या** — the cow made over to a creditor, in place "
             "of interest, for him to milk; **पीतदुग्धेति यस्याः "
             "प्रसिद्धिः**, known as *the one whose milk is drunk*. "
             "धेनुष्यां भवते ददामि. A financial instrument with a "
             "word of its own"),
    Thak("4.4.90", gives="ñya", of=("gṛhapati",), sense="saṃyukta",
         result="saṃjñā", case="tṛtīyā",
         why="गृहपतिना संयुक्ते ञ्यः. **निर्देशादेव तृतीयासमर्थ"
             "विभक्तिः** — the instrumental is read off the wording. "
             "गृहपतिना संयुक्तो **गार्हपत्योऽग्निः**, the "
             "householder's fire, one of the three of the śrauta "
             "ritual.\n\n"
             "**अन्यस्यापि गृहपतिना संयोगोऽस्ति, तत्र "
             "संज्ञाधिकारादतिप्रसङ्गनिवृत्तिः** — other things are "
             "joined to a householder too, and it is the संज्ञा "
             "heading that keeps the rule from reaching them"),
    Thak("4.4.91", gives="yat", case="tṛtīyā", result="saṃjñā",
         of=("nau", "vayas", "dharma", "viṣa", "mūla", "sītā", "tulā"),
         sense="tārya-tulya-prāpya-vadhya-ānāmya-sama-samita-sammita",
         why="नौवयोधर्मविषमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्य"
             "समसमितसंमितेषु — **अष्टभ्यः शब्देभ्योऽष्टस्वेव "
             "तार्यादिष्वर्थेषु यथासंख्यम्**: eight bases against "
             "eight senses, matched in order, and मूल answers two of "
             "them.\n\n"
             "नावा तार्यं **नाव्यमुदकम्**, water one can cross by "
             "boat; वयसा तुल्यो **वयस्यः सखा**, a friend of one's own "
             "age; धर्मेण प्राप्यं **धर्म्यम्**; विषेण वध्यो "
             "**विष्यः**; मूलेनानाम्यं **मूल्यम्**; मूलेन समो "
             "**मूल्यः पटः**; सीतया समितं **सीत्यं क्षेत्रम्**; "
             "तुलया संमितं **तुल्यम्**.\n\n"
             "**AND THE NEXT RULE IS SHOWN NOT TO COVER ONE OF THEM.** "
             "ननु च धर्मादनपेते इति वक्ष्यमाणेनैव सिद्धम्? **नैतदस्ति; "
             "धर्मं यदनुवर्तते तद् धर्मादनपेतमित्युच्यते; फलं तु "
             "धर्मादपेत्यैव, कार्यविरोधित्वाद् धर्मस्य** — what "
             "*does not depart from* dharma is what conforms to it, "
             "and a FRUIT departs from it, being the opposite of the "
             "act. So *obtainable by dharma* needs its own rule"),
    Thak("4.4.92", gives="yat", case="pañcamī", result="saṃjñā",
         of=("dharma", "pathin", "artha", "nyāya"), sense="anapeta",
         why="धर्मपथ्यर्थन्यायादनपेते. **निर्देशादेव पञ्चमी "
             "समर्थविभक्तिः** — the ablative is read off the wording. "
             "धर्मादनपेतं **धर्म्यम्**; **पथ्यम्**, **अर्थ्यम्**, "
             "**न्याय्यम्** — and all four are still the ordinary "
             "words for *proper*, *wholesome*, *meaningful*, *just*"),
    Thak("4.4.93", gives="yat", of=("chandas",), sense="nirmita",
         case="tṛtīyā",
         why="छन्दसो निर्मिते. **निर्मित उत्पादितः**. छन्दसा "
             "निर्मितश् **छन्दस्यः**, **इच्छया कृत इत्यर्थः** — and "
             "**इच्छापर्यायश्छन्दःशब्द इह गृह्यते**: the छन्दस् here "
             "is not metre but WILL, a synonym of *wish*"),
    Thak("4.4.94", gives="aṇ", also_gives=("yat",), of=("uras",),
         sense="nirmita", case="tṛtīyā", result="saṃjñā",
         why="उरसोऽण् च — the अण्, and by the च the यत्. उरसा "
             "निर्मित **औरसः पुत्रः**, उरस्यः पुत्रः: a son made of "
             "one's own breast, the legitimate son"),
    Thak("4.4.95", gives="yat", of=("hṛdaya",), sense="priya",
         case="ṣaṣṭhī", result="saṃjñā",
         why="हृदयस्य प्रियः. हृदयस्य प्रियो **हृद्यो देशः**, हृद्यं "
             "वनम् — a place dear to the heart. And the संज्ञा "
             "heading narrows what may be meant: **इह न भवति — "
             "हृदयस्य प्रियः पुत्रः**, a beloved SON is not what the "
             "word names",
         keeps_out="हृदयस्य प्रियः पुत्रः"),
    Thak("4.4.96", gives="yat", of=("hṛdaya",), sense="bandhana",
         result="ṛṣi", case="ṣaṣṭhī",
         why="बन्धने चर्षौ, हृदयस्येत्येव. **बध्यते येन तद् "
             "बन्धनम्**; **ऋषिर्वेदो गृह्यते**. हृदयस्य बन्धनम् "
             "ऋषिर् **हृद्यः** — **परहृदयं येन बध्यते वशीक्रियते, स "
             "वशीकरणमन्त्रो हृद्य इत्युच्यते**: the verse by which "
             "another's heart is bound, a spell for winning someone "
             "over"),
    Thak("4.4.97", gives="yat", of=("mata", "jana", "hala"),
         sense="karaṇa-jalpa-karṣa", case="ṣaṣṭhī",
         why="मतजनहलात् करणजल्पकर्षेषु, **यथासंख्यम्**. Three bases "
             "against three senses. **मतं ज्ञानं तस्य करणं मत्यम्**; "
             "जनस्य जल्पो **जन्यः**; हलस्य कर्षो **हल्यः**, "
             "द्विहल्यः, त्रिहल्यः. **भावसाधनं वा** — or each may be "
             "read as naming the act itself"),
    Thak("4.4.98", gives="yat", sense="sādhu", case="saptamī",
         why="तत्र साधुः, सप्तमीसमर्थात्. सामसु साधुः **सामन्यः**; "
             "वेमन्यः, **कर्मण्यः**, **शरण्यः**.\n\n"
             "**साधुरिह प्रवीणो योग्यो वा गृह्यते, नोपकारकः** — "
             "साधु here is SKILLED or FIT and not *helpful*, "
             "**तत्र हि परत्वात् तस्मै हितम् इत्यनेन विधिना "
             "भवितव्यम्**: for *helpful* the later rule 5.1.5 would "
             "have the ground. A sense narrowed by pointing at the "
             "rule that would otherwise take it"),
    Thak("4.4.99", gives="khañ", gana="pratijanādi", sense="sādhu",
         case="saptamī", excepts=("4.4.98",),
         why="प्रतिजनादिभ्यः खञ्, यतोऽपवादः. प्रतिजने साधुः "
             "**प्रातिजनीनः**, **जनेजने साधुरित्यर्थः** — good with "
             "every man he meets. ऐदंयुगीनः, सांयुगीनः.\n\n"
             "**यत्र हितार्थ एव साध्वर्थस्तत्र वचनात् प्राक् "
             "क्रीतीया बाध्यन्ते** — where *fit* amounts to "
             "*helpful*, this rule's being spoken displaces the "
             "affixes of the section 5.1.1 opens"),
    Thak("4.4.100", gives="ṇa", of=("bhakta",), sense="sādhu",
         case="saptamī", excepts=("4.4.98",),
         why="भक्ताण्णः, यतोऽपवादः. भक्ते साधुर् **भाक्तः शालिः**, "
             "rice that does well as a meal; भाक्तास्तण्डुलाः"),
    Thak("4.4.101", gives="ṇya", also_gives=("ṇa",), of=("pariṣad",),
         sense="sādhu", case="saptamī", excepts=("4.4.98",),
         why="परिषदो ण्यः, यतोऽपवादः. परिषदि साधुः **पारिषद्यः**.\n\n"
             "**णप्रत्ययोऽप्यत्रेष्यते; तदर्थं योगविभागः क्रियते** — "
             "the ण too is wanted, and the rule is split for it: "
             "*from परिषद्, ण*, giving **पारिषदः**, and then *ण्य*. "
             "One rule read as two so that both affixes come"),
    Thak("4.4.102", gives="ṭhak", gana="kathādi", sense="sādhu",
         case="saptamī", excepts=("4.4.98",),
         why="कथादिभ्यष्ठक्, यतोऽपवादः. कथायां साधुः **काथिकः**, a "
             "good story-teller; वैकथिकः"),
    Thak("4.4.103", gives="ṭhañ", gana="guḍādi", sense="sādhu",
         case="saptamī", excepts=("4.4.98",),
         why="गुडादिभ्यष्ठञ्, यतोऽपवादः. गुडे साधुर् **गौडिक इक्षुः**, "
             "sugarcane that makes good molasses; **कौल्माषिको "
             "मुद्गः**, **साक्तुको यवः** — beans good for porridge, "
             "barley good for meal. A list of what each crop is best "
             "turned into"),
    Thak("4.4.104", gives="ḍhañ",
         of=("pathin", "atithi", "vasati", "svapati"), sense="sādhu",
         case="saptamī", excepts=("4.4.98",),
         why="पथ्यतिथिवसतिस्वपतेर्ढञ्, यतोऽपवादः. पथि साधु "
             "**पाथेयम्**, provision for the road; **आतिथेयम्**, "
             "what is fit for a guest; वासतेयम्, **स्वापतेयम्**"),
    Thak("4.4.105", gives="ya", of=("sabhā",), sense="sādhu",
         case="saptamī", excepts=("4.4.98",),
         why="सभाया यः, यतोऽपवादः; **स्वरे विशेषः**, and the two "
             "differ only in the accent. सभायां साधुः **सभ्यः** — "
             "one fit for an assembly, and so *civil*"),
    Thak("4.4.106", gives="ḍha", of=("sabhā",), usage="chandasi",
         sense="sādhu", case="saptamī", excepts=("4.4.105",),
         why="ढश्छन्दसि, **यस्यापवादः**. **सभेयो युवास्य यजमानस्य "
             "वीरो जायताम्** (माध्यन्दिनसंहिता २२.२२) — *let a hero "
             "be born to this sacrificer, a youth fit for the "
             "assembly*"),
    Thak("4.4.107", gives="yat", of=("samānatīrtha",), sense="vāsin",
         case="saptamī",
         why="समानतीर्थे वासी. **साधुरिति निवृत्तम्** — *fit* has "
             "lapsed. समाने तीर्थे वासीति **सतीर्थ्यः**, "
             "**समानोपाध्याय इत्यर्थः**: a fellow-student. "
             "**तीर्थशब्देनेह गुरुरुच्यते** — तीर्थ here means the "
             "TEACHER, and the word for a shared ford is the word "
             "for a shared master"),
    Thak("4.4.108", gives="yat", of=("samānodara",), sense="śayita",
         case="saptamī",
         why="समानोदरे शयित ओ चोदात्तः. **शयितः स्थित इत्यर्थः** — "
             "*lain* means *been*. समानोदरे शयितः **समानोदर्यो "
             "भ्राता**, a brother born of the same womb; and the ओ "
             "is made acute in the same act"),
    Thak("4.4.109", gives="ya", of=("sodara",), sense="śayita",
         case="saptamī", excepts=("4.4.108",),
         why="सोदराद् यः. **विभाषोदरे** [6.3.88] इति सूत्रेण "
             "यकारादौ प्रत्यये विवक्षिते **प्रागेव समानस्य सभावः** — "
             "समान becomes स before the affix is even added, by a "
             "rule of the sixth chapter. समानोदरे शयितः **सोदर्यो "
             "भ्राता**. **ओ चोदात्त इति नानुवर्तते; यकारे स्वरः**: "
             "the accent-clause does not carry, and the accent falls "
             "on the य"),
    Thak("4.4.110", gives="yat", usage="chandasi", sense="bhava",
         case="saptamī",
         why="भवे छन्दसि, तत्रेत्येव; **अणादीनां घादीनां चापवादः**. "
             "**नमो मेघ्याय च विद्युत्याय च नमः** (तैत्तिरीयसंहिता "
             "४.५.७.२).\n\n"
             "**सति दर्शने तेऽपि भवन्ति, सर्वविधीनां छन्दसि "
             "व्यभिचारात्** — and where they are actually attested "
             "the other affixes come too, since EVERY rule is "
             "irregular in the Veda. An exception stated and at once "
             "made porous.\n\n"
             "**आ पादपरिसमाप्तेश्छन्दोऽधिकारः, भवाधिकारश्च "
             "समुद्राभ्राद् घः इति यावत्** — the Vedic heading runs "
             "to the END OF THE PĀDA and the भव heading to 4.4.118. "
             "Two ranges opened by one rule and stopped at different "
             "places"),
    Thak("4.4.111", gives="ḍyaṇ", of=("pāthas", "nadī"),
         usage="chandasi", sense="bhava", case="saptamī",
         excepts=("4.4.110",),
         why="पाथोनदीभ्यां ड्यण्, यतोऽपवादः. पाथसि भवः **पाथ्यो "
             "वृषा** (ऋग्वेद ६.१६.१५); **चनो दधीत नाद्यो गिरो मे** "
             "(ऋग्वेद २.३५.१). **पाथोऽन्तरिक्षम्** — पाथस् is the "
             "middle air"),
    Thak("4.4.112", gives="aṇ", of=("veśanta", "himavat"),
         usage="chandasi", sense="bhava", case="saptamī",
         excepts=("4.4.110",),
         why="वेशन्तहिमवद्भ्यामण्, यतोऽपवादः. **वैशन्तीभ्यः स्वाहा** "
             "(तैत्तिरीयसंहिता ७.४.१३.९); **हैमवतीभ्यः स्वाहा**"),
    Thak("4.4.113", gives="ḍyat", also_gives=("ḍya",), of=("srotas",),
         optional=True, usage="chandasi", sense="bhava",
         case="saptamī", excepts=("4.4.110",),
         why="स्रोतसो विभाषा ड्यड्ड्यौ, यतोऽपवादः; पक्षे सोऽपि भवति. "
             "स्रोतसि भवः **स्रोत्यः** (ऋग्वेद १०.१०४.८), "
             "**स्रोतस्यः**. **ड्यड्ड्ययोः स्वरे विशेषः** — the two "
             "differ in the accent alone"),
    Thak("4.4.114", gives="yan",
         of=("sagarbha", "sayūtha", "sanuta"), usage="chandasi",
         sense="bhava", case="saptamī", excepts=("4.4.110",),
         why="सगर्भसयूथसनुताद् यन्, यतोऽपवादः; **स्वरे विशेषः**. "
             "**अनु भ्राता सगर्भ्यः**; **अनु सखा सयूथ्यः**; "
             "**यो नः सनुत्यः**. **सर्वत्र समानस्य छन्दसि** [6.3.84] "
             "इति सभावः — समान becomes स in all three, by a Vedic "
             "rule of the sixth chapter"),
    Thak("4.4.115", gives="ghan", of=("tugra",), usage="chandasi",
         sense="bhava", case="saptamī", excepts=("4.4.110",),
         why="तुग्राद् घन्, यतोऽपवादः. **त्वमग्ने वृषभस्तुग्रियाणाम्**. "
             "**अन्नाकाशयज्ञवरिष्ठेषु तुग्रशब्दः** — तुग्र is food, "
             "sky, sacrifice and the best of anything, four senses "
             "for one word"),
    Thak("4.4.116", gives="yat", of=("agra",), usage="chandasi",
         sense="bhava", case="saptamī",
         why="अग्राद् यत्. अग्रे भवम् **अग्र्यम्**.\n\n"
             "**किमर्थमिदं यावता सामान्येन यद् विहित एव?** — why "
             "state it, when 4.4.110 gives यत् generally already? "
             "**घच्छौ च इति वक्ष्यति, ताभ्यां बाधा मा भूदिति पुनर् "
             "विधीयते**: because the NEXT rule adds घ and छ, and "
             "without this the यत् would have been displaced by them. "
             "A rule restated so that its own successor cannot beat "
             "it"),
    Thak("4.4.117", gives="gha", also_gives=("cha", "yat", "ghan"),
         of=("agra",), usage="chandasi", sense="bhava",
         case="saptamī",
         why="घच्छौ च. **अग्र्यम्** (खिल १.३.७), **अग्रियम्** "
             "(ऋग्वेद १.१३.१०), **अग्रीयम्** (मैत्रायणीसंहिता "
             "२.७.१३). **चकारः तुग्राद् घन् इत्यस्यानुकर्षणार्थः** — "
             "the च drags in 4.4.115's घन् as well, so अग्रियम् comes "
             "by that too; **स्वरे विशेषः**, and the two अग्रिय differ "
             "only in accent"),
    Thak("4.4.118", gives="gha", of=("samudra", "abhra"),
         usage="chandasi", sense="bhava", case="saptamī",
         excepts=("4.4.110",),
         why="समुद्राभ्राद् घः, यतोऽपवादः. **समुद्रिया नदीनाम्** "
             "(ऋग्वेद ७.८७.१); **अभ्रियस्येव घोषाः** (ऋग्वेद "
             "१०.६८.१).\n\n"
             "**अभ्रशब्दस्यापूर्वनिपातः, तस्य लक्षणस्य "
             "व्यभिचारित्वात्** — अभ्र does not come first in the "
             "compound though the rule for order would put it there, "
             "because that rule is not without exception. And this "
             "rule is where the भव heading stops"),
    Thak("4.4.119", gives="yat", of=("barhis",), sense="datta",
         case="saptamī", usage="chandasi",
         why="बर्हिषि दत्तम्. **भव इति निवृत्तम्** — *being* has "
             "lapsed. **बर्हिष्येषु निधिषु प्रियेषु** (ऋग्वेद "
             "१०.१५.५) — of the dear treasures laid on the sacred "
             "grass"),
    Thak("4.4.120", gives="yat", of=("dūta",), sense="bhāga-karman",
         case="ṣaṣṭhī", usage="chandasi",
         why="दूतस्य भागकर्मणी. **भागोंऽशः; कर्म क्रिया**. "
             "**यदग्ने यासि दूत्यम्** (ऋग्वेद १.१२.४) — *when, Agni, "
             "you go on your embassy*: दूतभागः, दूतकर्म वा"),
    Thak("4.4.121", gives="yat", of=("rakṣas", "yātu"),
         sense="hananī", case="ṣaṣṭhī", usage="chandasi",
         why="रक्षोयातूनां हननी. **हन्यतेऽनयेति हननी** — that by "
             "which they are killed. **या वां मित्रावरुणौ रक्षस्या "
             "तनूः**; **यातव्या**.\n\n"
             "**बहुवचनं स्तुतिवैशिष्ट्यज्ञापनार्थम्; बहूनां रक्षसां "
             "हननेन तनूः स्तूयते** — the plural in the rule is there "
             "to mark the force of the praise: the body is praised "
             "for killing MANY demons"),
    Thak("4.4.122", gives="yat",
         of=("revatī", "jagatī", "haviṣyā"), sense="praśasya",
         case="ṣaṣṭhī", usage="chandasi",
         why="रेवतीजगतीहविष्याभ्यः प्रशस्ये. **प्रशंसनं प्रशस्यम्; "
             "भावे क्यप् प्रत्ययो भवति**. **यद्वो रेवती रेवत्यम्**, "
             "**यद्वो जगतीर्जगत्यम्**, **यद्वो हविष्या हविष्यम्** "
             "(काठकसंहिता १.८) — *what praise of you there is*, three "
             "times over"),
    Thak("4.4.123", gives="yat", of=("asura",), sense="sva",
         case="ṣaṣṭhī", usage="chandasi", excepts=("4.1.83",),
         why="असुरस्य स्वम्, अणोऽपवादः. **असुर्यं वा एतत् पात्रं यत् "
             "कुलालकृतं चक्रवृत्तम्** (मैत्रायणीसंहिता १.८.३) — "
             "*that vessel is the Asuras' own, the one the potter "
             "made and the wheel turned*"),
    Thak("4.4.124", gives="aṇ", of=("asura",), sense="sva",
         result="māyā", case="ṣaṣṭhī", usage="chandasi",
         excepts=("4.4.123",),
         why="मायायामण्, **पूर्वस्य यतोऽपवादः**. **आसुरी माया स्वधया "
             "कृतासि** (माध्यन्दिनसंहिता ११.६९) — the Asuras' own, "
             "but only where the MAGIC of them is meant"),
    Thak("4.4.125", gives="yat", of_samjna="matup-anta",
         result="upadhāna-mantra-iṣṭakā", elides=True,
         case="prathamā", usage="chandasi", sense="āsām",
         why="तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः. The "
             "longest rule of the pāda, and every word of it is "
             "conditional. A stem ending in मतुप् takes यत् where the "
             "thing named is BRICKS and the first word names the "
             "mantra by which they are laid — and the मतुप् is "
             "removed in the same act, **लुक् च मतोरिति "
             "प्रकृतिनिर्ह्रासः**.\n\n"
             "वर्चःशब्दो यस्मिन् मन्त्रेऽस्ति स वर्चस्वान्; "
             "**उपधीयते येन स उपधानः, चयनवचन इत्यर्थः**. "
             "वर्चस्वानुपधानमन्त्र आसामिष्टकानाम् इति विगृह्य — "
             "**वर्चस्या उपदधाति**, **तेजस्या**, पयस्याः, रेतस्याः.\n\n"
             "Four counter-examples, one for each word: तद्वानिति "
             "किम्? मन्त्रसमुदायादेव मा भूत्. उपधान इति किम्? "
             "**वर्चस्वानुपस्थानमन्त्रः**. मन्त्र इति किम्? "
             "**अङ्गुलिमानुपधानो हस्तः**. इष्टकास्विति किम्? "
             "**वर्चस्वानुपधानमन्त्र एषां कपालानाम्**.\n\n"
             "**इतिकरणो नियमार्थः; अनेकपदसंभवेऽपि केनचिदेव पदेन "
             "तद्वान् मन्त्रो गृह्यते, न सर्वेण** — and the इति "
             "restricts: though a mantra may have many words, it "
             "counts as *having that* by ONE of them and not by all",
         keeps_out="वर्चस्वानुपस्थानमन्त्रः, अङ्गुलिमानुपधानो हस्तः"),
    Thak("4.4.126", gives="aṇ", of=("aśvimat",),
         result="upadhāna-mantra-iṣṭakā", elides=True,
         case="prathamā", usage="chandasi", sense="āsām",
         excepts=("4.4.125",),
         why="अश्विमानण्, **पूर्वस्य यतोऽपवादः**. "
             "**अश्विनीरुपदधाति** (शतपथब्राह्मण ८.२.१.१). And when "
             "the मतुप् goes, **इनण्यनपत्ये** [6.4.164] इति "
             "प्रकृतिभावः keeps the stem whole where 4.3.108 needed "
             "a vārttika to cut it"),
    Thak("4.4.127", gives="matup", of=("mūrdhan",),
         result="vayasyā", case="prathamā", usage="chandasi",
         sense="āsām", excepts=("4.4.125",),
         why="वयस्यासु मूर्ध्नो मतुप्, **पूर्वस्य यतोऽपवादः**. "
             "**मूर्धा वयः प्रजापतिश्छन्दः** — where one mantra has "
             "BOTH words, it is वयस्वान् and मूर्धन्वान् alike, and "
             "from the second the यत् would have come; मतुप् is given "
             "instead. **मूर्धन्वतीर्भवन्ति**.\n\n"
             "**मूर्धन्वत इति वक्तव्ये मूर्ध्न इत्युक्तम्, मतुपो "
             "लुकं भाविनं चित्ते कृत्वा** — the rule names the bare "
             "stem where it should have named the मतुप्-form, with "
             "the coming elision of that मतुप् already in mind. A "
             "rule worded for a state that does not yet exist"),
    Thak("4.4.128", gives="yat", result="māsa-tanū",
         case="prathamā", usage="chandasi", sense="matvartha",
         why="मत्वर्थे मासतन्वोः. **मत्वर्थीयानामपवादः** — an "
             "exception to the whole class of possessive affixes, "
             "where the thing is a MONTH or a BODY. नभांसि विद्यन्ते "
             "यस्मिन् मासे **नभस्यः**; **सहस्यः**, **तपस्यः**, "
             "मधव्यः — the Vedic month-names. ओजोऽस्यां विद्यत "
             "**ओजस्या तनूः**.\n\n"
             "मासतन्वोरिति किम्? **मधुमता पात्रेण चरति**. And a "
             "vārttika adds four more endings for the months: "
             "**लुगकारेकाररेफाश्च** — तपश्च तपस्यश्च by the elision, "
             "**इषः** and **ऊर्जः** by अ, **शुचिः** by इ, **शुक्रः** "
             "by र. Six ways of naming a month, all from one rule "
             "and its supplement",
         keeps_out="मधुमता पात्रेण चरति"),
    Thak("4.4.129", gives="ña", also_gives=("yat",), of=("madhu",),
         case="prathamā", usage="chandasi", sense="matvartha",
         excepts=("4.4.128",),
         why="मधोर्ञ च — the ञ, and by the च the यत्; and "
             "**उपसंख्यानात् लुक् च**, the elision by a supplement. "
             "**माधवः**, **मधव्यः**, **मधुः** — three names for one "
             "month, and the first is the ordinary word for spring"),
    Thak("4.4.130", gives="yat", also_gives=("kha",), of=("ojas",),
         result="ahan", case="prathamā", usage="chandasi",
         sense="matvartha", excepts=("4.4.128",),
         why="ओजसोऽहनि यत्खौ, मत्वर्थ इत्येव. **ओजस्यमहः**, "
             "**ओजसीनमहः** — a day that has vigour in it"),
    Thak("4.4.131", gives="yal", of_samjna="veśo-yaśa-ādi-bhaga-anta",
         case="prathamā", usage="chandasi", sense="matvartha",
         why="वेशोयशआदेर्भगाद् यल्, मत्वर्थ इत्येव. **लकारः "
             "स्वरार्थः**. वेशोभगो विद्यते यस्य स **वेशोभग्यः**; "
             "यशोभग्यः.\n\n"
             "**वेश इति बलमुच्यते; श्रीकामप्रयत्नमाहात्म्यवीर्ययशस्सु "
             "भगशब्दः** — वेश is strength, and भग is fortune, desire, "
             "effort, greatness, vigour or fame: six senses in the "
             "second member alone"),
    Thak("4.4.132", gives="kha", also_gives=("yat",),
         of_samjna="veśo-yaśa-ādi-bhaga-anta", case="prathamā",
         usage="chandasi", sense="matvartha",
         why="ख च. **योगविभागो यथासंख्यनिरासार्थ उत्तरार्थश्च** — "
             "the rule is split BOTH to stop a pairing and for the "
             "sake of what follows, which is the first time in the "
             "project a split has been given two purposes at once. "
             "**वेशोभगीनः**, वेशोभग्यः; यशोभगीनः, यशोभग्यः"),
    Thak("4.4.133", gives="ina", also_gives=("ya", "kha"),
         of=("pūrva",), sense="kṛta", case="tṛtīyā",
         usage="chandasi",
         why="पूर्वैः कृतमिनयौ च. **मत्वर्थ इति निवृत्तम्**. "
             "**गम्भीरेभिः पथिभिः पूर्विणेभिः**; **पूर्व्यैः**; "
             "पूर्वीणैः.\n\n"
             "**पूर्वैरिति बहुवचनान्तेन पूर्वपुरुषा उच्यन्ते; "
             "तत्कृताः पन्थानः प्रशस्ता इति पथां प्रशंसा** — the "
             "plural names the men of old, and roads THEY made are "
             "praised roads. The rule is a compliment"),
    Thak("4.4.134", gives="yat", of=("ap",), sense="saṃskṛta",
         case="tṛtīyā", usage="chandasi",
         why="अद्भिः संस्कृतम्. **यस्येदमप्यं हविः** (ऋग्वेद "
             "१०.८६.१२) — the offering prepared with water"),
    Thak("4.4.135", gives="gha", of=("sahasra",), sense="sammita",
         case="tṛtīyā", usage="chandasi",
         why="सहस्रेण संमितौ घः. **संमितस्तुल्यः सदृशः**. "
             "**अयमग्निः सहस्रियः** (तैत्तिरीयसंहिता ४.७.१३.४), "
             "*worth a thousand*.\n\n"
             "**केचित्तु समिताविति पठन्ति; तत्रापि समित्या संमित एव "
             "लक्षयितव्यः** — some read the word without the prefix, "
             "and even then the sense has to be *measured against*. "
             "A variant reading admitted and then read back to the "
             "same meaning"),
    Thak("4.4.136", gives="gha", of=("sahasra",), case="prathamā",
         usage="chandasi", sense="matvartha", excepts=("4.4.135",),
         why="मतौ च. सहस्रमस्य विद्यते **सहस्रियः** — an exception to "
             "**तपःसहस्राभ्यां विनीनी** [5.2.102] and **अण् च** "
             "[5.2.103], two rules in the chapter after this one"),
    Thak("4.4.137", gives="ya", of=("soma",), sense="arhati",
         case="dvitīyā", usage="chandasi",
         why="सोममर्हति यः. **सोममर्हन्ति सोम्या ब्राह्मणाः** "
             "(काठकसंहिता ५.२), **यज्ञार्हा इत्यर्थः** — brahmins fit "
             "to receive the soma. **यति प्रकृते यग्रहणम्; स्वरे "
             "विशेषः**: यत् was already carrying, and य is named "
             "instead for the accent alone"),
    Thak("4.4.138", gives="ya", of=("soma",), sense="mayaṭ-artha",
         usage="chandasi", case="ṣaṣṭhī", excepts=("4.4.137",),
         why="मये च. **मय इति मयडर्थो लक्ष्यते** — the syllable "
             "stands for the sense of मयट्, and the vṛtti lists every "
             "rule that gives it: 4.3.81, 4.3.82, 4.3.143 and 5.4.21. "
             "**आगतविकारावयवप्रकृता मयडर्थाः**, four senses gathered "
             "under one name. **पिबाति सोम्यं मधु** (ऋग्वेद "
             "८.२४.१३), सोममयम्"),
    Thak("4.4.139", gives="yat", of=("madhu",), sense="mayaṭ-artha",
         usage="chandasi", case="ṣaṣṭhī", excepts=("4.4.138",),
         why="मधोः. **यशब्दो निवृत्तः** — the य of the last rule has "
             "lapsed and the heading's यत् returns. **मधव्यान् "
             "स्तोकान्** (पैप्पलादसंहिता १.८८.२), मधुमयान्"),
    Thak("4.4.140", gives="yat", of=("vasu",), sense="samūha",
         usage="chandasi", case="ṣaṣṭhī",
         why="वसोः समूहे च. **वसव्यः समूहः**, and by the च in the "
             "मयट् sense too.\n\n"
             "**अक्षरसमूहे छन्दसः स्वार्थ उपसंख्यानम्** — a vārttika "
             "gives the affix to छन्दस् in its own sense when a "
             "count of SYLLABLES is meant, and the vṛtti works the "
             "count: ओश्रावय four, अस्तु श्रौषट् four, यज two, ये "
             "यजामहे five, वषट्कार two — **एष वै सप्तदशाक्षरश् "
             "छन्दस्यः प्रजापतिर्यज्ञो मन्त्रे विहितः**. Seventeen "
             "syllables, added up in the commentary"),
    Thak("4.4.141", gives="gha", of=("nakṣatra",), sense="svārtha",
         usage="chandasi", case="prathamā",
         why="नक्षत्राद् घः, स्वार्थे. **समूह इति नानुवर्तते** — the "
             "collection-sense does not carry. **नक्षत्रियेभ्यः "
             "स्वाहा** (माध्यन्दिनसंहिता २२.२८)"),
    Thak("4.4.142", gives="tātil", of=("sarva", "deva"),
         sense="svārtha", usage="chandasi", case="prathamā",
         why="सर्वदेवात् तातिल्, छन्दसि; स्वार्थिकः. **सर्वतातिम्** "
             "(ऋग्वेद १०.३६.१४), **देवतातिम्** (ऋग्वेद ३.१९.२) — "
             "an affix that changes nothing but the shape"),
    Thak("4.4.143", gives="tātil", gana="śivādi", sense="kara",
         case="ṣaṣṭhī", usage="chandasi",
         why="शिवशमरिष्टस्य करे. **करोतीति करः प्रत्ययार्थः**. शिवं "
             "करोतीति **शिवतातिः**; **शंतातिः**, **अरिष्टतातिः** — "
             "*making blessed*, *making peace*, *making unharmed*"),
    Thak("4.4.144", gives="tātil", gana="śivādi", sense="bhāva",
         case="ṣaṣṭhī", usage="chandasi",
         why="भावे च. शिवस्य भावः **शिवतातिः** — the same three "
             "words and the same affix, now for the STATE and not the "
             "making. One form for both, and only the context "
             "divides them.\n\n"
             "**AND THE PĀDA AND THE CHAPTER END BY CLOSING THE "
             "HEADING.** **यतः पूर्णोऽवधिः, अतः परमन्यः प्रत्ययो "
             "ऽधिक्रियते** — word for word what 4.4.74 said of ठक्. "
             "So यत्'s marker is 5.1.5 and its last rule is this one, "
             "because 5.1.1 प्राक्क्रीताच्छः opens छ inside the "
             "range. Twice in one pāda, and the second time settles "
             "that the gap between a heading's MARKER and its LAST "
             "RULE is how these headings nest.\n\n"
             "इति काशिकायां वृत्तौ चतुर्थाध्यायस्य चतुर्थः पादः"),
)


@dataclass(frozen=True)
class ByMeansOf:
    """The affix given for an action, and by which rule."""

    gives: str
    by: str
    why: str
    also_gives: Tuple[str, ...] = ()
    case: str = ""
    optional: bool = False
    #: True where the answer is that the affix GOES. 4.4.24.
    elided: bool = False
    excepts: Tuple[str, ...] = ()


def _reaches(row: Thak, stem: str, gana: str, sense: str, case: str,
             result: str, samjna: str, upadha: str, vowels: str,
             pre: str, stem_final: str, usage: str,
             elided: bool) -> bool:
    if row.of and stem not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.sense and sense != row.sense:
        # Strict, where the other tables are loose. Every rule
        # of this pāda names its own action and only the
        # heading does not, so a query that names no action is
        # asking after the heading — which is the whole point
        # of प्राग्वहतेष्ठक्.
        return False
    if row.case and case and case != row.case:
        return False
    if row.result and result != row.result:
        return False
    if row.of_samjna and samjna != row.of_samjna:
        return False
    if row.upadha and upadha != row.upadha:
        return False
    if row.vowels and vowels != row.vowels:
        return False
    if row.pre and pre != row.pre:
        return False
    if row.stem_final and stem_final != row.stem_final:
        return False
    if row.usage and usage != row.usage:
        return False
    if elided and not row.elides:
        return False
    return True


def _supplies(row: Thak, wants: str) -> bool:
    """Whether the row gives the affix asked for."""
    return (not wants
            or wants == row.gives
            or wants in row.also_gives)


def _how_specific(row: Thak) -> int:
    """
    A named base is the narrowest thing these rules state; the action
    and the case are the widest, since both are carried.
    """
    return (
        6 * bool(row.of)
        + 5 * bool(row.of_samjna)
        + 4 * bool(row.gana)
        + 4 * bool(row.pre)
        + 3 * bool(row.result)
        + 3 * bool(row.upadha)
        + 3 * bool(row.vowels)
        + 2 * bool(row.stem_final)
        + 3 * bool(row.usage)
        + 2 * bool(row.sense)
        + 1 * bool(row.case)
    )


def by_means_of(stem: str = "", *, gana: str = "", sense: str = "",
                case: str = "", result: str = "", samjna: str = "",
                upadha: str = "", vowels: str = "", pre: str = "",
                stem_final: str = "", usage: str = "",
                elided: bool = False, wants: str = "") -> ByMeansOf:
    """
    4.4.1–30 — the affix for what a man DOES by means of a thing.

    `sense` is the action the derived word reports — दीव्यति, तरति,
    चरति, जीवति, हरति — and `case` the relation the base stands in:
    the instrumental for a means, and from 4.4.28 the accusative for
    what one moves along rather than by.

    Where no rule of this section is reached the answer is 4.4.1's
    ठक्, which is what the heading is for.
    """
    matched = [
        row for row in THAK_TABLE
        if _reaches(row, stem, gana, sense, case, result, samjna,
                    upadha, vowels, pre, stem_final, usage,
                    elided)
        and _supplies(row, wants)
    ]
    if not matched:
        heading = THAK_TABLE[0]
        return ByMeansOf(heading.gives, heading.sutra, heading.why,
                         case=case or heading.case)
    row = max(matched, key=_how_specific)
    if row.elides:
        return ByMeansOf("", row.sutra, row.why, case=row.case,
                         elided=True, excepts=row.excepts)
    return ByMeansOf(row.gives, row.sutra, row.why,
                     also_gives=row.also_gives, case=row.case,
                     optional=row.optional, excepts=row.excepts)


def thak_run() -> ByMeansOf:
    """
    How far ठक् is the affix — and the marker is not the last rule.

    4.4.1's vṛtti names the marker: **प्रागेतस्माद्
    वहतिसंशब्दनात्**, the word वहति lifted out of 4.4.76, exactly as
    4.1.83 lifted दीव्यति out of the rule IT stops at. But 4.4.75
    प्राग्घिताद् यत् opens a heading of its own INSIDE that range, so
    the last rule ठक् actually governs is 4.4.74 — and that rule's
    vṛtti says so: **ठकः पूर्णोऽवधिः**.
    """
    opens, closes = THAK_RUN
    return ByMeansOf(
        "ṭhak", opens,
        "ठक् is the affix from %s to %s. The marker is %s — the word "
        "वहति lifted out of तद्वहति रथयुगप्रासङ्गम् — but 4.4.75 "
        "opens यत् inside that range, so ठकः पूर्णोऽवधिः at %s"
        % (opens, closes, THAK_MARKER, closes))


def yat_run() -> ByMeansOf:
    """
    And the third great प्राक्-heading, reaching out of the chapter.

    4.4.75's vṛtti: **तस्मै हितम् इति वक्ष्यति; प्रागेतस्माद्
    हितसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामो यत्प्रत्ययस्तेष्वधिकृतो
    वेदितव्यः** — यत् from here to 5.1.4, bounded by lifting हित out
    of 5.1.5. The same device a third time, and the first of the
    three to cross a chapter boundary.
    """
    opens, closes = YAT_RUN
    return ByMeansOf(
        "yat", opens,
        "यत् is the affix from %s to %s. The marker is %s तस्मै "
        "हितम्, two pādas past the last rule — because 5.1.1 "
        "प्राक्क्रीताच्छः opens छ inside the range, and 4.4.144 says "
        "so: यतः पूर्णोऽवधिः, the same words 4.4.74 used of ठक्"
        % (opens, closes, YAT_MARKER))


def provisions_for(sutra_id: str) -> Tuple[Thak, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in THAK_TABLE if row.sutra == sutra_id)
