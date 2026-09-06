# -*- coding: utf-8 -*-
"""
४.२.१–२१ — a case-relation and a sense, and the affix understood.

4.1 spent 178 sūtras on ONE sense — *his descendant* — and named the
affix in almost every rule. 4.2 changes the shape entirely. Each rule
here states **a case-relation and a sense**, and leaves the affix to
4.1.83's default unless it has reason to say otherwise:

    तेन रक्तं रागात्      by that, dyed          — instrumental
    तेन युक्तं कालः       joined with that       — instrumental
    तेन दृष्टं साम        seen by that           — instrumental
    तेन परिवृतो रथः       wrapped in that        — instrumental
    तत्रोद्धृतममत्रेभ्यः  taken up in that       — locative
    तत्र संस्कृतं भक्षाः  prepared in that       — locative
    सास्मिन् पौर्णमासी    that being in it       — nominative

**And the case-relation is carried by anuvṛtti like any other word.**
4.2.1's vṛtti says how far its own runs — द्वैपवैयाघ्रादञ् इति यावत्
तृतीयासमर्थविभक्तिरनुवर्तते, to 4.2.12 — and 4.2.14's says the same
of the locative, क्षीराड् ढञ् इति यावत्. So each of the two blocks is
bounded by a rule NAMED IN THE VṚTTI, and the boundaries can be
checked rather than guessed.

That is what 4.1.82 समर्थानां प्रथमाद्वा was for. It said the affix
attaches to the FIRST of the syntactically connected words; these
rules say WHICH connection, in which case, and in what sense. The
heading and the section fit together exactly, and neither works
alone.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: The case in which the base stands, named as the vṛtti names it.
#: तृतीयासमर्थ, सप्तमीसमर्थ, प्रथमासमर्थ.
CASES: Tuple[str, ...] = ("tṛtīyā", "saptamī", "prathamā", "dvitīyā")


@dataclass(frozen=True)
class SenseRule:
    """One rule of 4.2: a case, a sense, and what comes."""

    sutra: str
    #: The case the base stands in. Carried by anuvṛtti, and each
    #: run's end is named in the vṛtti of the rule that opens it.
    case: str = ""
    #: The sense the affix is given in — रक्त, युक्त, दृष्ट, परिवृत,
    #: उद्धृत, संस्कृत.
    sense: str = ""
    #: What the affix is given, or "" where 4.1.83's default stands.
    gives: str = ""
    #: Particular bases the rule names.
    of: Tuple[str, ...] = ()
    gana: str = ""
    #: A further condition on WHAT the result is: a time, a chant, a
    #: chariot, a vessel, food. Several rules of this run turn on it,
    #: and it is stated in the sūtra rather than left to the sense.
    result: str = ""
    #: What the base ends in. 4.2.71 wants a उ-final stem, and it is
    #: the only rule of this pāda stated on a SOUND rather than on a
    #: meaning, a list, or a named word.
    stem_final: str = ""
    #: Two vowels — 4.2.73's बह्वचः is stated the other way, of MANY,
    #: so the field carries the rule's own condition and not its
    #: complement.
    dvyac: bool = False
    #: A condition on the whole compound rather than on either part.
    of_samjna: str = ""
    optional: bool = False
    #: 4.2.4's अविशेषे — where no PARTICULAR part of the day-and-night
    #: is meant. It is the only thing separating that rule from
    #: 4.2.3, and without it the two are indistinguishable: the same
    #: base, the same case, the same sense, and one gives an affix
    #: while the other takes it away.
    unspecified: bool = False
    #: What stands in front — 4.2.107's दिक्पूर्वपद.
    pre: str = ""
    #: The accent the base must carry. 4.2.109 wants अन्तोदात्त, and
    #: its counter-example turns on an accent placed by a mark on a
    #: quite different affix.
    accent: str = ""
    #: The affix the base already carries, where the rule points at
    #: another rule's output rather than at a shape: 4.2.111 and
    #: 4.2.112 both do.
    marked: str = ""
    #: The PENULTIMATE sound of the base — कोपध, योपध, रोपध, खोपध.
    #: Not `stem_final`: उपधा is defined at 1.1.65 as the sound before
    #: the last, and six rules of 4.2.119–145 are stated on it. A base
    #: whose उपधा is क does not end in क, and saying so would let
    #: 4.2.132 reach words it never reaches.
    upadha: str = ""
    #: The last member of the compound the rule names, where it names
    #: several. 4.2.126 names four and 4.2.142 five, which is why this
    #: is a tuple where `stem_final` is a string.
    ends_with: Tuple[str, ...] = ()
    #: True where देश carries — the base must name a COUNTRY. The
    #: word enters at 4.2.119 and the vṛtti says देश इत्येव down to
    #: the last rule of the pāda.
    desa: bool = False
    #: The rule whose affix this one leaves standing, where the rule
    #: enjoins only a substitute. 4.2.140 is the one:
    #: **आदेशमात्रमिह विधेयम्, प्रत्ययस्तु वृद्धाच्छ इत्येव सिद्धः**.
    affix_from: str = ""
    #: The rule whose affixes this one BORROWS, where an अतिदेश takes
    #: over what another stretch of the grammar gives. 4.2.34
    #: कालेभ्यो भववत् is the one, and it reaches forward: the rules
    #: it borrows from are stated a pāda later. Not `affix_from`,
    #: which names a rule in this table whose affix is simply left
    #: standing; this fetches from another resolver entirely, and
    #: **वत्करणं सर्वसादृश्यपरिग्रहार्थम्** is why it takes whatever
    #: it finds rather than one named affix.
    borrows_from: str = ""
    #: True where the rule REFUSES. 4.2.113 is the only one here.
    refuses: bool = False
    #: A second thing the rule does in the same act — 4.2.91's कुक्.
    along_with: str = ""
    #: True where the rule ELIDES the affix rather than giving one.
    elides: bool = False
    excepts: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


#: Where each case-relation stops, as the vṛtti of the rule that
#: opens it says. Held as data because both ends are stated and both
#: can be checked: the opening rule and the rule it names.
CASE_RUNS: Tuple[Tuple[str, str, str], ...] = (
    ("tṛtīyā", "4.2.1", "4.2.12"),
    ("saptamī", "4.2.14", "4.2.20"),
)

#: And the SENSES are bounded the same way. Each of these is an
#: अधिकार whose closing rule the vṛtti of the opening rule names —
#: सास्य देवता runs महाराजप्रोष्ठपदाट् ठञ् इति यावत्, and तस्य समूहः
#: runs इनित्रकट्यचश्च इति यावत्. Three stated ranges in one pāda,
#: where most anuvṛtti has to be inferred.
SENSE_RUNS: Tuple[Tuple[str, str, str], ...] = (
    ("devatā", "4.2.24", "4.2.35"),
    ("samūha", "4.2.37", "4.2.51"),
    ("adhīte-veda", "4.2.59", "4.2.65"),
    ("cāturarthika", "4.2.67", "4.2.91"),
)

#: And देश is the third kind of stated range in this pāda. It enters
#: at 4.2.119 ओर्देशे and the vṛtti of nine rules after it opens with
#: देश इत्येव — 4.2.120, 122, 123, 124, 126, 132, 133, 137, 139, 141,
#: 142 and 145 among them — so the last of those, 4.2.145, is where
#: the commentary still has it running. SEVEN bounded ranges in one
#: pāda — two case-runs, four sense-runs and this — where most
#: anuvṛtti in this project has had to be inferred from where a
#: rule stops making sense.
DESA_RUN: Tuple[str, str] = ("4.2.119", "4.2.145")

#: 4.2.67 to 4.2.70 state FOUR senses, and 4.2.70's च is what gathers
#: them: **चकारः पूर्वेषां त्रयाणामर्थानामिह सन्निधानार्थः, तेन
#: उत्तरेषु चत्वारोऽप्यर्थाः संबध्यन्ते** — the conjunction brings
#: the first three alongside the fourth, and from there all four
#: carry together. Every rule from 4.2.71 to 4.2.91 gives an affix in
#: whichever of the four fits, यथासंभवम्, and the tradition calls
#: those affixes चातुरर्थिक, *of-the-four-senses*.
#:
#: A name for a group of rules taken from the NUMBER of senses they
#: serve, and the number is produced by a single conjunction.
CATURARTHIKA: Tuple[str, ...] = (
    "asti-deśe",      # 4.2.67 तदस्मिन्नस्तीति देशे तन्नाम्नि
    "nirvṛtta",       # 4.2.68 तेन निर्वृत्तम्
    "nivāsa",         # 4.2.69 तस्य निवासः
    "adūrabhava",     # 4.2.70 अदूरभवश्च
)


SENSE_TABLE: Tuple[SenseRule, ...] = (
    SenseRule("4.2.1", case="tṛtīyā", sense="rakta", of_samjna="rāga",
              why="तेन रक्तं रागात्. शुक्लस्य वर्णान्तरापादनम् इह "
                  "रञ्जेरर्थः, रज्यतेऽनेनेति रागः — the sense of the "
                  "root is bringing a white thing to another colour, "
                  "and a dye is what it is done with. कषायेण रक्तं "
                  "वस्त्रं काषायम्; माञ्जिष्ठम्, कौसुम्भम्.\\n\\n"
                  "रागादिति किम्? देवदत्तेन रक्तं वस्त्रम् — the "
                  "base must name a DYE and not whoever did the "
                  "dyeing.\\n\\n"
                  "कथं काषायौ गर्दभस्य कर्णौ, हारिद्रौ कुक्कुटस्य "
                  "पादौ? **उपमानाद् भविष्यति** — काषायाविव काषायौ: "
                  "an ass's ears and a cock's feet are not dyed, and "
                  "the forms stand by LIKENESS. The same instrument "
                  "4.1.103 and 4.1.105 used for three famous names.\\n\\n"
                  "AND THE VṚTTI NAMES WHERE THE CASE STOPS: "
                  "**द्वैपवैयाघ्रादञ् इति यावत् तृतीयासमर्थविभक्तिर् "
                  "अनुवर्तते** — the instrumental runs to 4.2.12, "
                  "and no further",
              keeps_out="देवदत्तेन रक्तं वस्त्रम्"),
    SenseRule("4.2.2", case="tṛtīyā", sense="rakta", gives="ṭhak",
              gana="lākṣādi", excepts=("4.1.83",),
              why="लाक्षारोचनाशकलकर्दमाट् ठक्, अणोऽपवादः. लाक्षिकम्, "
                  "रौचनिकम्, शाकलिकम्, कार्दमिकम् — and "
                  "शकलकर्दमाभ्यामणपीष्यते, so शाकलम् and कार्दमम् "
                  "stand too.\\n\\n"
                  "Four vārttikas give four more dyes four more "
                  "affixes: नील्या अन् — नीलं वस्त्रम्; पीतात् कन् "
                  "— पीतकम्; हरिद्रामहारजनाभ्यामञ् — हारिद्रम्, "
                  "माहारजनम्. **A colour-word for each colour**"),
    SenseRule("4.2.3", case="tṛtīyā", sense="yukta", result="kāla",
              of_samjna="nakṣatra",
              why="नक्षत्रेण युक्तः कालः. पौषी रात्रिः, पौषमहः; "
                  "माघी रात्रिः.\\n\\n"
                  "**AND THE VṚTTI HAS TO EXPLAIN HOW A TIME CAN BE "
                  "JOINED WITH A STAR AT ALL.** कथं पुनर्नक्षत्रेण "
                  "पुष्यादिना कालो युज्यते? — पुष्यादिसमीपस्थे "
                  "चन्द्रमसि वर्तमानाः पुष्यादिशब्दाः प्रत्ययम् "
                  "उत्पादयन्ति: the star-names are used of the MOON "
                  "standing near those stars, and it is the moon the "
                  "time is joined with. A grammatical rule needing an "
                  "astronomical gloss before it can be applied.\\n\\n"
                  "नक्षत्रेणेति किम्? चन्द्रमसा युक्ता रात्रिः. काल "
                  "इति किम्? पुष्येण युक्तश्चन्द्रमाः",
              keeps_out="पुष्येण युक्तश्चन्द्रमाः"),
    SenseRule("4.2.4", case="tṛtīyā", sense="yukta", result="kāla",
              of_samjna="nakṣatra", unspecified=True, elides=True,
              why="लुबविशेषे. Where no PARTICULAR part of the "
                  "day-and-night is meant, the affix is dropped: "
                  "अद्य पुष्यः, अद्य कृत्तिकाः. यावान् कालो "
                  "नक्षत्रेण युज्यतेऽहोरात्रः, तस्याविशेषे लुब् "
                  "भवति. अविशेष इति किम्? पौषी रात्रिः, पौषमहः.\\n\\n"
                  "The elision is what makes a star-name serve as a "
                  "day-name — the affix is given and removed, and "
                  "4.1.88's machinery is what allows it",
              keeps_out="पौषी रात्रिः"),
    SenseRule("4.2.5", case="tṛtīyā", sense="yukta", result="kāla",
              of=("śravaṇa", "aśvattha"), of_samjna="saṃjñā",
              elides=True,
              why="संज्ञायां श्रवणाश्वत्थाभ्याम्. अविशेषे लुब् विहितः "
                  "पूर्वेण, **विशेषार्थोऽयमारम्भः** — begun for the "
                  "particular case the rule before excluded: श्रवणा "
                  "रात्रिः, अश्वत्थो मुहूर्तः. संज्ञायामिति किम्? "
                  "श्रावणी, आश्वत्थी रात्रिः.\\n\\n"
                  "लुपि युक्तवद्भावः कस्माद् न भवति? **निपातनात्** "
                  "विभाषा फाल्गुनीश्रवणाकार्तिकी इति — the gender "
                  "and number of the elided affix's base would "
                  "normally carry over, and they do not, and the "
                  "evidence is a form fixed eighteen sūtras ahead",
              keeps_out="श्रावणी रात्रिः"),
    SenseRule("4.2.6", case="tṛtīyā", sense="yukta", result="kāla",
              gives="cha", of_samjna="nakṣatra-dvandva",
              why="द्वन्द्वाच्छः. From a DVANDVA of star-names, and "
                  "विशेषे चाविशेषे च — in both cases: "
                  "राधानुराधीया रात्रिः, and अद्य राधानुराधीयम्. "
                  "**लुपं परत्वाद् बाधते** — it beats the elision by "
                  "being later, which is परत्व doing in one word "
                  "what 4.1.85's vārttika needed पूर्वविप्रतिषेध to "
                  "do in reverse"),
    SenseRule("4.2.7", case="tṛtīyā", sense="dṛṣṭa", result="sāman",
              why="तेन दृष्टम्. क्रुञ्चेन दृष्टं क्रौञ्चं साम; "
                  "वासिष्ठम्, वैश्वामित्रम्. The sense is a CHANT "
                  "SEEN by a seer, which is how the tradition speaks "
                  "of composition"),
    SenseRule("4.2.8", case="tṛtīyā", sense="dṛṣṭa", result="sāman",
              gives="ḍhak", of=("kali",), excepts=("4.1.83",),
              why="कलेर्ढक्, अणोऽपवादः. कालेयम्.\\n\\n"
                  "**THE DENSEST VĀRTTIKA-SET SINCE 4.1.85, AND IT "
                  "ENDS IN A VERSE.** सर्वत्राग्निकलिभ्यां ढग् "
                  "वक्तव्यः — आग्नेयम्, and एवमग्नौ भवम्, "
                  "अग्नेरागतम्, अग्नेः स्वम् इति **सर्वत्र ढगेव "
                  "भवति**: one affix for one word in every sense, "
                  "which is a rule about a WORD rather than about a "
                  "sense. दृष्टे सामनि अण् वा डिद् भवति — औशनसम्, "
                  "औशनम्. तीयादीकक् स्वार्थे वा — द्वैतीयीकम्, but "
                  "**न विद्यायाः**, not of a branch of learning. "
                  "गोत्रादङ्कवदिष्यते — औपगवकम्.\\n\\n"
                  "दृष्टे सामनि जाते च द्विरण् डिद् वा विधीयते / "
                  "तीयादीकक् न विद्याया गोत्रादङ्कवदिष्यते — five "
                  "vārttikas gathered into one verse, which is how "
                  "the tradition remembers a set"),
    SenseRule("4.2.9", case="tṛtīyā", sense="dṛṣṭa", result="sāman",
              gives="ḍyat", of=("vāmadeva",), excepts=("4.1.83",),
              why="वामदेवाड् ड्यड्ड्यौ, अणोऽपवादः. वामदेव्यं साम. "
                  "तित्करणं स्वरार्थम्.\\n\\n"
                  "**AND THE ड् IS THERE TO KEEP THE AFFIX OUT OF A "
                  "RULE FOUR CHAPTERS AWAY.** डित्करणं किमर्थम्? "
                  "ययतोश्चातदर्थे इति नञ उत्तरस्यान्तोदात्तत्वे "
                  "विधीयमाने **अनयोर्ग्रहणं मा भूत्** — 6.2.156 "
                  "names य and यत्, and without the ड् these two "
                  "would be caught by it: अवामदेव्यम् would take the "
                  "wrong accent. The exclusion works through "
                  "अननुबन्धकग्रहणपरिभाषा and एकानुबन्धकग्रहण"
                  "परिभाषा — a name with no mark, or one mark, does "
                  "not reach a two-marked affix.\\n\\n"
                  "And a verse states the whole argument: सिद्धे "
                  "यस्येतिलोपेन किमर्थं ययतौ डितौ / ग्रहणं मातदर्थे "
                  "भूद् वामदेव्यस्य नञ्स्वरे"),
    SenseRule("4.2.10", case="tṛtīyā", sense="parivṛta", result="ratha",
              why="तेन परिवृतो रथः. वस्त्रेण परिवृतो रथो वास्त्रो "
                  "रथः; काम्बलः, चार्मणः. रथ इति किम्? वस्त्रेण "
                  "परिवृतः कायः.\\n\\n"
                  "AND परिवृत IS DEFINED TIGHTLY. समन्ताद् वेष्टितः "
                  "परिवृत उच्यते, **यस्य न कश्चिदवयवो वस्त्रादिभिर् "
                  "अवेष्टितः** — wrapped on every side, with no part "
                  "left uncovered. तेनेह न भवति — छात्रैः परिवृतो "
                  "रथः: a chariot surrounded by students is not "
                  "wrapped in them",
              keeps_out="छात्रैः परिवृतो रथः"),
    SenseRule("4.2.11", case="tṛtīyā", sense="parivṛta", result="ratha",
              gives="ini", of=("pāṇḍukambala",), excepts=("4.1.83",),
              why="पाण्डुकम्बलादिनिः, अणोऽपवादः. पाण्डुकम्बली, "
                  "पाण्डुकम्बलिनौ. पाण्डुकम्बलशब्दो राजास्तरणस्य "
                  "वर्णकम्बलस्य वाचकः.\\n\\n"
                  "**मत्वर्थीयेनैव सिद्धे वचनमणो निवृत्त्यर्थम्** — "
                  "the affix इनि was available anyway as a "
                  "possessive, so the rule exists only to keep the "
                  "default OUT. A rule stated for what it prevents "
                  "rather than for what it gives, which 4.1.84 also "
                  "was"),
    SenseRule("4.2.12", case="tṛtīyā", sense="parivṛta", result="ratha",
              gives="añ", of=("dvaipa", "vaiyāghra"),
              excepts=("4.1.83",),
              why="द्वैपवैयाघ्रादञ्, अणोऽपवादः, **स्वरे विशेषः** — "
                  "the two affixes differ only in accent, for the "
                  "fourth time since 4.1.25. द्वैपेन परिवृतो रथो "
                  "द्वैपः; वैयाघ्रः. द्वीपिव्याघ्रयोर्विकारभूते "
                  "चर्मणी द्वैपवैयाघ्रे — the bases are already "
                  "derived, naming the HIDES of those animals.\\n\\n"
                  "And this is the rule 4.2.1's vṛtti named as where "
                  "the instrumental stops"),
    SenseRule("4.2.13", case="dvitīyā", of=("kumārī",),
              of_samjna="apūrva",
              why="कौमारापूर्ववचने. निपात्यते — कौमारः पतिः, a "
                  "husband who is a girl's FIRST, and "
                  "पाणिग्रहणस्यापूर्ववचनम्. **उभयतः स्त्रिया "
                  "अपूर्वत्वे निपातनमेतत्** — the fixing covers the "
                  "firstness on both sides.\\n\\n"
                  "And the vṛtti gives two derivations rather than "
                  "one, in a verse: कौमारापूर्ववचने कुमार्या अण् "
                  "विधीयते / **अपूर्वत्वं यदा तस्याः कुमार्यां भवति "
                  "इति वा** — either from the girl in the "
                  "second case, or simply *what happens in "
                  "girlhood*, कुमार्यां भवः कौमारः पतिः, तस्य स्त्री "
                  "कौमारी भार्या. The second needs no fixing at all"),
    SenseRule("4.2.14", case="saptamī", sense="uddhṛta",
              of_samjna="amatra",
              why="तत्रोद्धृतममत्रेभ्यः. शरावेषूद्धृतः शाराव ओदनः; "
                  "माल्लिकः, कार्परः. **भुक्तोच्छिष्टमुद्धृतमुच्यते, "
                  "यस्योद्धरणमिति प्रसिद्धिः** — what is taken up "
                  "means the leavings of a meal, and अमत्रं भाजनं "
                  "पात्रम्, a vessel. अमत्रेभ्य इति किम्? पाणावुद्धृत "
                  "ओदनः.\\n\\n"
                  "AND THE VṚTTI NAMES WHERE THIS CASE STOPS: "
                  "**क्षीराड् ढञ् इति यावत्** — the locative runs to "
                  "4.2.20, exactly as 4.2.1 said of the instrumental. "
                  "Two runs, two boundaries, both stated",
              keeps_out="पाणावुद्धृत ओदनः"),
    SenseRule("4.2.15", case="saptamī", sense="śayita",
              of=("sthaṇḍila",), of_samjna="vrata",
              why="स्थण्डिलाच्छयितरि व्रते. स्थण्डिले शयितुं व्रतमस्य "
                  "**स्थाण्डिलो भिक्षुः**, a mendicant vowed to "
                  "sleep on bare ground. व्रतमिति शास्त्रितो नियम "
                  "उच्यते — a restraint laid down by a text.\\n\\n"
                  "व्रत इति किम्? स्थण्डिले शेते ब्रह्मदत्तः — "
                  "sleeping there is not enough; it has to be a VOW, "
                  "and the affix carries that and nothing else",
              keeps_out="स्थण्डिले शेते ब्रह्मदत्तः"),
    SenseRule("4.2.16", case="saptamī", sense="saṃskṛta",
              result="bhakṣa",
              why="संस्कृतं भक्षाः. भ्राष्ट्रे संस्कृता भक्षा "
                  "भ्राष्ट्रा अपूपाः; कालशाः, कौम्भाः.\\n\\n"
                  "Two definitions the rule does not give. "
                  "**खरविशदमभ्यवहार्यं भक्षम्** — a hard, dry thing "
                  "eaten; and **सत उत्कर्षाधानं संस्कारः**, "
                  "preparation is the improving of what already is. "
                  "भक्षा इति किम्? पुष्पपुटे संस्कृतो मालागुणः",
              keeps_out="पुष्पपुटे संस्कृतो मालागुणः"),
    SenseRule("4.2.17", case="saptamī", sense="saṃskṛta",
              result="bhakṣa", gives="yat", of=("śūla", "ukhā"),
              excepts=("4.1.83",),
              why="शूलोखाद् यत्, अणोऽपवादः. शूल्यं मांसम्; उख्यम्"),
    SenseRule("4.2.18", case="saptamī", sense="saṃskṛta",
              result="bhakṣa", gives="ṭhak", of=("dadhi",),
              why="दध्नष्ठक्. दाधिकम्.\\n\\n"
                  "**AND THE VṚTTI ASKS WHY THE RULE IS NEEDED AT "
                  "ALL, AND ANSWERS BY A DISTINCTION IN THE "
                  "SITUATION.** ननु च संस्कृतार्थे प्राग् वहतेष्ठकं "
                  "वक्ष्यति, तेनैव सिद्धम्? — 4.4.1 will give the "
                  "same affix in the same sense. न सिध्यति: दध्ना हि "
                  "तत् संस्कृतं यस्य **दधिकृतमेवोत्कर्षाधानम्**, इह "
                  "तु दधि **केवलमाधारभूतम्**, द्रव्यान्तरेण लवणादिना "
                  "संस्कारः क्रियते. There the curds do the "
                  "improving; here they are only what the thing "
                  "stands in, and salt does the work. The two rules "
                  "give one affix in one sense and differ in **who "
                  "is acting**"),
    SenseRule("4.2.19", case="saptamī", sense="saṃskṛta",
              result="bhakṣa", gives="ṭhak", of=("udaśvit",),
              optional=True,
              why="उदश्वितोऽन्यतरस्याम्. औदश्वित्कम् — and पक्षे "
                  "यथाप्राप्तमण्, औदश्वितम्"),
    SenseRule("4.2.20", case="saptamī", sense="saṃskṛta",
              result="bhakṣa", gives="ḍhañ", of=("kṣīra",),
              excepts=("4.1.83",),
              why="क्षीराड् ढञ्, अणोऽपवादः. क्षीरे संस्कृता क्षैरेयी "
                  "यवागूः. The rule 4.2.14's vṛtti named as where "
                  "the locative stops"),
    SenseRule("4.2.21", case="prathamā", sense="asmin",
              of_samjna="paurṇamāsī-saṃjñā",
              why="सास्मिन् पौर्णमासीति संज्ञायाम्. पौषी पौर्णमासी "
                  "अस्मिन् **पौषो मासः**, पौषोऽर्धमासः, पौषः "
                  "संवत्सरः — मासार्धमाससंवत्सराणामेषा संज्ञा, the "
                  "name of a month, a fortnight or a year. इह न "
                  "भवति — पौषी पौर्णमासी अस्मिन् दशरात्रे.\\n\\n"
                  "**AND THE VṚTTI ASKS WHY TWO WORDS ARE SPENT ON "
                  "ONE JOB.** इतिकरणस्य संज्ञाशब्दस्य च तुल्यमेव फलं "
                  "प्रयोगानुसरणम्, तत्र किमर्थं द्वयमुपादीयते? — "
                  "both इति and संज्ञायाम् do the same thing, hold "
                  "the rule to established usage. **संज्ञाशब्देन "
                  "तुल्यताम् इतिकरणस्य ज्ञापयितुम्, न ह्ययं लोके "
                  "तथा प्रसिद्धः**: the pair is there to TEACH that "
                  "इति does that job, since it is not commonly known "
                  "to. One word explained by being placed beside "
                  "another that is understood.\\n\\n"
                  "अथ पौर्णमासीति कोऽयं शब्दः? Two derivations again "
                  "— पूर्णमासादण्, or पूर्णो माः पूर्णमाः, मा इति "
                  "चन्द्र उच्यते: *the moon being full*",
              keeps_out="पौषी पौर्णमासी अस्मिन् दशरात्रे"),
    # --- the पौर्णमासी run closes -------------------------------------
    SenseRule("4.2.22", case="prathamā", sense="asmin", gives="ṭhak",
         of=("āgrahāyaṇī", "aśvattha"),
         of_samjna="paurṇamāsī-saṃjñā", excepts=("4.1.83",),
         why="आग्रहायण्यश्वत्थाट् ठक्, अणोऽपवादः. आग्रहायणिको मासः, "
             "अर्धमासः, संवत्सरः; आश्वत्थिकः. सास्मिन् पौर्णमासीति "
             "सर्वमनुवर्तते — the whole of 4.2.21 carries down"),
    SenseRule("4.2.23", case="prathamā", sense="asmin", gives="ṭhak",
         gana="phālgunyādi", of_samjna="paurṇamāsī-saṃjñā",
         optional=True,
         why="विभाषा फाल्गुनीश्रवणाकार्तिकीचैत्रीभ्यः. "
             "नित्यमणि प्राप्ते पक्षे ठग् विधीयते — the default was "
             "obligatory and this makes room beside it: फाल्गुनो "
             "मासः beside फाल्गुनिकः, श्रावणः beside श्रावणिकः, "
             "कार्तिकः beside कार्तिकिकः, चैत्रः beside चैत्रिकः.\n\n"
             "This is the rule 4.2.5's vṛtti reached forward to, "
             "eighteen sūtras earlier, to settle how an elided "
             "affix's base behaves — **निपातनात्**, from a form fixed "
             "here"),
    # --- सास्य देवता --------------------------------------------------
    SenseRule("4.2.24", case="prathamā", sense="devatā",
         why="सास्य देवता. इन्द्रो देवतास्य **ऐन्द्रं हविः**; "
             "आदित्यम्, बार्हस्पत्यम्, प्राजापत्यम्.\n\n"
             "**यागसंप्रदानं देवता, देयस्य पुरोडाशादेः स्वामिनी** — a "
             "deity is what a sacrifice is given TO, the owner of "
             "the cake that is offered. The sense is a relation "
             "between an offering and a god, and the affix is on the "
             "offering. देवतेति किम्? कन्या देवदत्तस्य.\n\n"
             "Two attested forms are then accounted for and neither "
             "licensed: कथमैन्द्रो मन्त्रः? **मन्त्रस्तुत्यमपि "
             "देवतेत्युपचरन्ति** — what a verse praises is called its "
             "deity by transfer. कथमाग्नेयो वै ब्राह्मणो देवतया? "
             "उपमानाद् भविष्यति.\n\n"
             "AND THE VṚTTI NAMES WHERE THIS SENSE STOPS: "
             "**महाराजप्रोष्ठपदाट् ठञ् इति यावत् सास्य देवतेत्य् "
             "अधिकारः** — to 4.2.35. The third range in this pāda "
             "with both ends stated.\n\n"
             "सेति प्रकृते **पुनः समर्थविभक्तिनिर्देशः "
             "संज्ञानिवृत्त्यर्थः** — the case is named again though "
             "it is already running, and the repetition is what "
             "stops 4.2.21's संज्ञायाम् carrying down with it. A word "
             "restated to break a bundle, which is 4.1.65's move",
         keeps_out="कन्या देवदत्तस्य"),
    SenseRule("4.2.25", case="prathamā", sense="devatā", of=("ka",),
         why="कस्येत्. **ततः पूर्वेणैवाण्प्रत्ययः सिद्धः, "
             "इकारादेशार्थं वचनम्** — the affix came from 4.2.24 "
             "already and the whole rule is the इ: कायं हविः, "
             "कायमेककपालं निर्वपेत् (मै०सं० ३.१५.१०). The fifth rule "
             "in two pādas whose stated affix is not what it is for. "
             "कशब्दो देवतायां प्रजापतेर्वाचकः"),
    SenseRule("4.2.26", case="prathamā", sense="devatā", gives="ghan",
         of=("śukra",), excepts=("4.1.83",),
         why="शुक्राद् घन्, अणोऽपवादः. शुक्रियं हविः; शुक्रियोऽध्यायः"),
    SenseRule("4.2.27", case="prathamā", sense="devatā", gives="gha",
         of=("aponaptṛ", "apāṃnaptṛ"), excepts=("4.1.83",),
         why="अपोनप्तृ अपांनप्तृभ्यां घः, अणोऽपवादः. अपोनप्त्रियं हविः "
             "(का०श्रौ० २३.४.१४); अपांनप्त्रियम्. अपोनपाद्, अपांनपाद् "
             "इति देवताया नामधेये एते — the bases are the god's own "
             "names, and **तयोस्तु प्रत्ययसन्नियोगेन रूपमिदं "
             "निपात्यते**, the shapes given here are fixed and hold "
             "only when the affix comes"),
    SenseRule("4.2.28", case="prathamā", sense="devatā", gives="cha",
         of=("aponaptṛ", "apāṃnaptṛ"), excepts=("4.1.83",),
         why="छ च. अपोनप्त्रीयं हविः, अपांनप्त्रीयम्.\n\n"
             "**A RULE SPLIT SO THAT यथासंख्यम् MAY NOT APPLY.** "
             "**योगविभागः सङ्ख्यातानुदेशपरिहारार्थः** — had the two "
             "affixes been given in one sūtra with the two bases, "
             "1.3.10 would have paired them off one to one. Dividing "
             "the rule is what lets BOTH affixes reach BOTH words.\n\n"
             "4.1.150 did the same job by BREAKING a compounding "
             "rule and letting the breach be the signal; this does it "
             "by splitting the sūtra. Two instruments for one "
             "purpose, a pāda apart.\n\n"
             "छप्रकरणे पैङ्गाक्षीपुत्रादिभ्य उपसंख्यानम् — "
             "पैङ्गाक्षीपुत्रीयम्, तार्णबिन्दवीयम्; and "
             "शतरुद्राच्छश्च घश्च gives both to one word: "
             "शतरुद्रीयम्, शतरुद्रियम्"),
    SenseRule("4.2.29", case="prathamā", sense="devatā", gives="gha",
         of=("mahendra",), excepts=("4.1.83",),
         why="महेन्द्राद् घाणौ च. THREE AFFIXES FOR ONE WORD, and the "
             "third by a च: महेन्द्रियं हविः, माहेन्द्रम् "
             "(तै०सं० ६.५.५.४), महेन्द्रीयम् (काठ०सं० १५.१). Each "
             "cited to a different text — the three forms are not a "
             "grammarian's construction but three attested usages"),
    SenseRule("4.2.30", case="prathamā", sense="devatā", gives="ṭyaṇ",
         of=("soma",), excepts=("4.1.83",),
         why="सोमाट् ट्यण्, अणोऽपवादः. सौम्यं हविः, सौम्यं सूक्तम्, "
             "सौमी ऋक् (मै०सं० १.७.४).\n\n"
             "**ण्कारो वृद्ध्यर्थः, टकारो ङीबर्थः** — the ण् for the "
             "strengthening and the ट् so that 4.1.15's ङीप् reaches "
             "it in the feminine. Two marks, two jobs, and neither is "
             "heard: the same shape as 3.4.81's शकार and चकार"),
    SenseRule("4.2.31", case="prathamā", sense="devatā", gives="yat",
         gana="vāyvādi", excepts=("4.1.83",),
         why="वायुऋतुपित्रुषसो यत्, अणोऽपवादः. वायव्यम्, ऋतव्यम्, "
             "पित्र्यम् (ऋ० ८.२०.१३), उषस्यम्"),
    SenseRule("4.2.32", case="prathamā", sense="devatā", gives="cha",
         gana="dyāvāpṛthivyādi", excepts=("4.1.83", "4.2.30"),
         why="द्यावापृथिवीशुनासीरमरुत्वदग्नीषोमवास्तोष्पतिगृहमेधाच् "
             "छः, and चकाराद् यत् च — **so every one of the six has "
             "two forms, and both are cited**: द्यावापृथिवीयम् "
             "(मै०सं० १.८.१०) beside द्यावापृथिव्यम् (तै०सं० "
             "१.८.२.१); शुनासीरीयम् (मा०सं० २४.१९) beside शुनासीर्यम् "
             "(मै०सं० ४.३.३); मरुत्वतीयम्, अग्नीषोमीयम्, "
             "वास्तोष्पतीयम्, गृहमेधीयम् each beside its शorter "
             "form.\n\n"
             "शुनो वायुः, सीर आदित्यः — the vṛtti glosses which gods "
             "the compound names, because the words are not "
             "otherwise transparent"),
    SenseRule("4.2.33", case="prathamā", sense="devatā", gives="ḍhak",
         of=("agni",), excepts=("4.1.83",),
         why="अग्नेर्ढक्, अणोऽपवादः. आग्नेयोऽष्टाकपालः (तै०सं० "
             "१.८.२.१). And the vārttika on 4.2.8 is repeated here: "
             "**प्राग्दीव्यतीयेषु तद्धितार्थेषु सर्वत्राग्निकलिभ्यां "
             "ढग्** — one affix for these two words in EVERY sense of "
             "the section, which is a rule about words rather than "
             "about senses"),
    SenseRule("4.2.34", case="prathamā", sense="devatā",
         of_samjna="kāla", borrows_from="4.3.11",
         why="कालेभ्यो भववत्. **AN अतिदेश REACHING FORWARD TO RULES "
             "NOT YET STATED.** कालाट् ठञ् इति प्रकरणे भवे प्रत्यया "
             "विधास्यन्ते, ते सास्य देवतेत्यस्मिन्नर्थे तथैवेष्यन्ते "
             "— the affixes 4.3.11 onward will give in the sense "
             "*born in*, come here too. मासे भवं मासिकम्, and मासो "
             "देवतास्य मासिकम्; आर्धमासिकम्, सांवत्सरिकम्, वासन्तम्, "
             "प्रावृषेण्यम्.\n\n"
             "**वत्करणं सर्वसादृश्यपरिग्रहार्थम्** — the वत् takes "
             "in EVERY likeness and not merely the affix: whatever "
             "those rules do there, they do here. 3.4.85's लोटो "
             "लङ्वत् had its borrowing bounded by an option; this one "
             "is stated to be total"),
    SenseRule("4.2.35", case="prathamā", sense="devatā", gives="ṭhañ",
         of=("mahārāja", "proṣṭhapada"), excepts=("4.1.83",),
         why="महाराजप्रोष्ठपदाट् ठञ्. माहाराजिकम्, प्रौष्ठपदिकम् — "
             "and this is the rule 4.2.24's vṛtti named as where the "
             "deity-sense stops.\n\n"
             "ठञ्प्रकरणे **तदस्मिन् वर्तत** इति नवयज्ञादिभ्य "
             "उपसंख्यानम् — नावयज्ञिकः कालः, पाकयज्ञिकः: a vārttika "
             "adding not words but a whole further SENSE. And "
             "पूर्णमासादण् gives पौर्णमासी तिथिः (मै०सं० १.६.९), "
             "which is the word 4.2.21's vṛtti had to derive"),
    SenseRule("4.2.36", of=("pitṛ", "mātṛ"), of_samjna="nipātana",
         why="पितृव्यमातुलमातामहपितामहाः. निपात्यन्ते: पितुर्भ्राता "
             "पितृव्यः, मातुर्भ्राता मातुलः; पितुः पिता पितामहः, "
             "मातुः पिता मातामहः, and मातरि षित् — पितामही, "
             "मातामही.\n\n"
             "**THE MOST COMPLETE निपातन IN THE PROJECT.** "
             "**समर्थविभक्तिः प्रत्ययः प्रत्ययार्थोऽनुबन्ध इति "
             "सर्वं निपातनाद् विज्ञेयम्** — the case-relation, the "
             "affix, the sense of the affix and its marks are ALL to "
             "be known from the fixing. Nothing in the rule is "
             "derived from anything; the forms are simply given, and "
             "everything a rule normally supplies is read off them.\n\n"
             "Three vārttikas then fix three more sets on the same "
             "footing: अवेर्दुग्धे — अविसोढम्, अविदूसम्, अविमरीसम्; "
             "तिलान्निष्फलात् — तिलपिञ्जः, तिलपेजः; and पिञ्जश्छन्दसि "
             "डिच्च, तिल्पिञ्जं दण्डनं नडम् (शौ०सं० १२.२.५४)"),
    # --- तस्य समूहः ---------------------------------------------------
    SenseRule("4.2.37", case="ṣaṣṭhī", sense="samūha",
         why="तस्य समूहः. काकानां समूहः **काकम्**; बाकम्.\n\n"
             "**AND THE VṚTTI HAS TO COMPUTE AN EXAMPLE BY "
             "SUBTRACTION.** किमिहोदाहरणम्? — every ordinary base is "
             "taken by some later rule, so the answer is given as a "
             "list of what the example must NOT be: **चित्तवद् "
             "आद्युदात्तम् अगोत्रम् यस्य च नान्यत् प्रतिपदं ग्रहणम्** "
             "— animate, because 4.2.47 takes the inanimate; "
             "first-accented, because 4.2.44 takes the rest; not a "
             "lineage-name, because 4.2.39 takes those; and not named "
             "in any rule of its own, because 4.2.40 and its like "
             "name words directly. तत्परिहारेणात्रोदाहरणं द्रष्टव्यम्. "
             "**A rule whose example exists only in the gap its own "
             "section leaves.**\n\n"
             "AND THE VṚTTI NAMES WHERE THIS SENSE STOPS: "
             "**इनित्रकट्यचश्च इति यावत् समूहाधिकारः** — to 4.2.51.\n\n"
             "गुणादिभ्यो ग्रामज् वक्तव्यः — गुणग्रामः, करणग्रामः, and "
             "the list is आकृतिगणः"),
    SenseRule("4.2.38", case="ṣaṣṭhī", sense="samūha", gives="aṇ",
              gana="bhikṣādi",
         why="भिक्षादिभ्योऽण्. भैक्षम्, गार्भिणम्. **अण्ग्रहणं "
             "बाधकबाधनार्थम्** — the default is named again in order "
             "to beat what would have beaten it, which is 4.1.84's "
             "move and 4.2.11's.\n\n"
             "युवतिशब्दोऽत्र पठ्यते, **तस्य ग्रहणसामर्थ्यात् "
             "पुंवद्भावो न भवति** — being named in the list is itself "
             "the reason the feminine is not replaced by the "
             "masculine: यौवतम्. A membership doing the work of a "
             "प्रतिषेध"),
    SenseRule("4.2.39", case="ṣaṣṭhī", sense="samūha", gives="vuñ",
         gana="gotrādi",
         why="गोत्रोक्षोष्ट्रोरभ्रराजराजन्यराजपुत्रवत्समनुष्याजाद् "
             "वुञ्. औपगवकम्, औक्षकम्, औष्ट्रकम्, औरभ्रकम्, राजकम्, "
             "राजन्यकम्, राजपुत्रकम्, वात्सकम्, मानुष्यकम्, "
             "आजकम्.\n\n"
             "**AND गोत्र IS READ IN ITS ORDINARY SENSE HERE, NOT ITS "
             "TECHNICAL ONE.** अपत्याधिकारादन्यत्र **लौकिकं गोत्रं "
             "गृह्यते** अपत्यमात्रम्, न तु पौत्रप्रभृत्येव — outside "
             "the descendant section the word means any descendant "
             "and not 4.1.162's grandson-onward. The same word, "
             "technical inside one section and ordinary outside it, "
             "and the boundary is the section itself"),
    SenseRule("4.2.40", case="ṣaṣṭhī", sense="samūha", gives="yañ",
         of=("kedāra",), excepts=("4.2.47",),
         why="केदाराद् यञ् च, अचित्तलक्षणस्य ठकोऽपवादः. कैदार्यम्, "
             "and by the च also कैदारकम्. गणिकायाश्च यञ् वक्तव्यः — "
             "गाणिक्यम्"),
    SenseRule("4.2.41", case="ṣaṣṭhī", sense="samūha", gives="ṭhañ",
         of=("kavacin", "kedāra"),
         why="ठञ् कवचिनश्च. कावचिकम् — and **चकारः केदारादित्यस्य "
             "अनुकर्षणार्थः**, the च pulls the last rule's word down "
             "so that कैदारिकम् stands as well. A third form for one "
             "word, made by a conjunction"),
    SenseRule("4.2.42", case="ṣaṣṭhī", sense="samūha", gives="yan",
         gana="brāhmaṇādi",
         why="ब्राह्मणमाणववाडवाद् यन्. ब्राह्मण्यम्, माणव्यम्, "
             "वाडव्यम्. नकारः स्वरार्थः.\n\n"
             "Five vārttikas add five more, and each names a "
             "different affix: पृष्ठादुपसंख्यानम् — पृष्ठ्यः षडहः; "
             "**अह्नः खः क्रतौ** — अहीनः क्रतुः, and क्रताविति "
             "किम्? आह्नः; पर्श्वा णस् — पार्श्वम्, "
             "पदसंज्ञकत्वाद् गुणो न भवति; and वातादूलः — वातूलः"),
    SenseRule("4.2.43", case="ṣaṣṭhī", sense="samūha", gives="tal",
         gana="grāmādi",
         why="ग्रामजनबन्धुसहायेभ्यस्तल्. ग्रामता, जनता, बन्धुता, "
             "सहायता — **the affix that gives Sanskrit its abstract "
             "collectives**, and here it is a rule about crowds. "
             "गजाच्चेति वक्तव्यम् — गजता"),
    SenseRule("4.2.44", case="ṣaṣṭhī", sense="samūha", gives="añ",
         of_samjna="anudāttādi",
         why="अनुदात्तादेरञ्. कापोतम्, मायूरम्, तैत्तिरम्. This is "
             "one of the four rules 4.2.37's vṛtti had to subtract "
             "before it could name an example of its own"),
    SenseRule("4.2.45", case="ṣaṣṭhī", sense="samūha", gives="añ",
         gana="khaṇḍikādi",
         why="खण्डिकादिभ्यश्च. खाण्डिकम्, वाडवम्. **आद्युदात्तार्थम् "
             "अचित्तार्थं च वचनम्** — stated for the first-accented "
             "and the inanimate, the two grounds 4.2.44 and 4.2.47 "
             "would otherwise have taken.\n\n"
             "**AND ONE MEMBER OF THE LIST TEACHES TWO THINGS AT "
             "ONCE.** क्षुद्रकमालव is in it though 4.2.44 already "
             "reaches it, and the vṛtti works out why: ननु च "
             "परत्वादञा वुञ् बाधिष्यते? **एवं तर्ह्येतज् ज्ञापयति — "
             "वुञि पूर्वविप्रतिषेधः, सामूहिकेषु च तदन्तविधिरस्तीति**. "
             "Its presence teaches (i) that 4.2.39's वुञ् wins by "
             "पूर्वविप्रतिषेध and (ii) that these rules DO reach a "
             "compound through its last member — औपगवकम् for the "
             "first, वानहस्तिकम् for the second.\n\n"
             "And then the same member is restated with a condition "
             "to narrow it: क्षुद्रकमालवात् **सेनासंज्ञायाम्** एवाञ् "
             "भवति — क्षौद्रकमालवी सेना, क्षौद्रकमालवकमन्यत्. Two "
             "kārikās set the whole argument out"),
    SenseRule("4.2.46", case="ṣaṣṭhī", sense="samūha",
         of_samjna="caraṇa",
         why="चरणेभ्यो धर्मवत्. **AN अतिदेश BORROWING FROM A "
             "VĀRTTIKA, NOT FROM A SŪTRA.** गोत्रचरणाद् वुञ् "
             "इत्यारभ्य प्रत्यया वक्ष्यन्ते, तत्रेदमुच्यते "
             "**चरणाद् धर्माम्नाययोः** (वा० ४.३.१२६) इति, तेन "
             "धर्मवद् इत्यतिदेशः क्रियते — what is borrowed is what "
             "a vārttika on 4.3.126 will give, and the sūtra here "
             "points at it. **वतिः सर्वसादृश्यार्थः**, the borrowing "
             "is total, as at 4.2.34.\n\n"
             "कठानां धर्मः काठकम्, and तथा समूहेऽपि काठकम् — the "
             "same five forms in both senses: कालापकम्, छान्दोग्यम्, "
             "औक्थिक्यम्, आथर्वणम्"),
    SenseRule("4.2.47", case="ṣaṣṭhī", sense="samūha", gives="ṭhak",
         of_samjna="acitta", excepts=("4.1.83", "4.2.44"),
         why="अचित्तहस्तिधेनोष्ठक्, अणञोरपवादः. आपूपिकम्, "
             "शाष्कुलिकम्; हास्तिकम्, धैनुकम्. धेनोरनञ इति वक्तव्यम् "
             "— आधेनवम्. The second of the four rules 4.2.37 had to "
             "subtract"),
    SenseRule("4.2.48", case="ṣaṣṭhī", sense="samūha", gives="yañ",
         of=("keśa",), optional=True,
         why="केशाश्वाभ्यां यञ्छावन्यतरस्याम्, यथासंख्यम्. कैश्यम् "
             "beside कैशिकम्; अश्वीयम् beside आश्वम्"),
    SenseRule("4.2.48", case="ṣaṣṭhī", sense="samūha", gives="cha",
         of=("aśva",), optional=True,
         why="केशाश्वाभ्यां यञ्छावन्यतरस्याम् — अश्वीयम् beside "
             "आश्वम्"),
    SenseRule("4.2.49", case="ṣaṣṭhī", sense="samūha", gives="ya",
         gana="pāśādi",
         why="पाशादिभ्यो यः. पाश्या, तृण्या"),
    SenseRule("4.2.50", case="ṣaṣṭhī", sense="samūha", gives="ya",
         of=("khala", "go", "ratha"),
         why="खलगोरथात्. खल्या, गव्या, रथ्या. **पाशादिष्वपाठ "
             "उत्तरार्थः** — the three are kept OUT of 4.2.49's list, "
             "though the affix is the same, so that the NEXT rule may "
             "name them. A membership withheld for a later rule's "
             "sake, which is 4.1.45's move in reverse"),
    SenseRule("4.2.51", case="ṣaṣṭhī", sense="samūha", gives="ini",
         of=("khala",),
         why="इनित्रकट्यचश्च, यथासंख्यम्. खलिनी, गोत्रा, रथकट्या — "
             "and this is the rule 4.2.37's vṛtti named as where the "
             "collection-sense stops.\n\n"
             "Four vārttikas then add four more affixes, and the "
             "last two are of a kind the section has not used: "
             "**कमलादिभ्यः खण्डच्** — कमलखण्डम्, an आकृतिगण; "
             "**नरकरितुरङ्गाणां स्कन्धच्** — नरस्कन्धः; and "
             "**पूर्वादिभ्यः काण्डः** — पूर्वकाण्डम्, कर्मकाण्डम्. "
             "Affixes that are whole words, and the last of them "
             "names the divisions of a book"),
    # --- तस्य विषयो देशः ---------------------------------------------
    SenseRule("4.2.52", case="ṣaṣṭhī", sense="viṣaya", result="deśa",
         why="तस्य निवासः ... no: **तस्य विषयो देशः**. शिबीनां "
             "विषयो देशः शैबः; औष्ट्रः. देश इति किम्? देवदत्तस्य "
             "विषयोऽनुवाकः.\n\n"
             "**AND THE VṚTTI ENUMERATES FOUR SENSES OF ONE WORD "
             "BEFORE SAYING WHICH IS MEANT.** विषयशब्दोऽयं बह्वर्थः: "
             "क्वचिद् ग्रामसमुदाये — विषयो लब्धः; क्वचिद् "
             "इन्द्रियग्राह्ये — चक्षुर्विषयो रूपम्; क्वचिद् "
             "अत्यन्तशीलिते ज्ञेये — देवदत्तस्य विषयोऽनुवाकः; "
             "क्वचिद् अन्यत्राभावे — मत्स्यानां विषयो जलम्. "
             "**तत्र देशग्रहणं ग्रामसमुदायप्रतिपत्त्यर्थम्**: the "
             "word देश in the sūtra is what picks the first of the "
             "four. A word disambiguated by a second word, and the "
             "other three senses set out so the reader can see the "
             "work being done",
         keeps_out="देवदत्तस्य विषयोऽनुवाकः"),
    SenseRule("4.2.53", case="ṣaṣṭhī", sense="viṣaya", result="deśa",
         gives="vuñ", gana="rājanyādi", excepts=("4.1.83",),
         why="राजन्यादिभ्यो वुञ्, अणोऽपवादः. राजन्यकः, दैवयानकः — "
             "and **आकृतिगणश्चायम्**, so मालवकः, वैराटकः, "
             "त्रैगर्तकः come too. The fourth open list of the "
             "project"),
    SenseRule("4.2.54", case="ṣaṣṭhī", sense="viṣaya", result="deśa",
         gives="vidhal", gana="bhaurikyādi", excepts=("4.1.83",),
         why="भौरिक्याद्यैषुकार्यादिभ्यो विधल्भक्तलौ, यथासंख्यम्, "
             "अणोऽपवादः. भौरिकिविधः, वैपेयविधः; ऐषुकारिभक्तः, "
             "सारस्यायनभक्तः. **Two affixes that are whole words** — "
             "विध and भक्त, *portion* and *share* — matched to two "
             "lists"),
    # --- three senses of one sūtra each ------------------------------
    SenseRule("4.2.55", case="prathamā", sense="ādi", result="pragātha",
         of_samjna="chandas",
         why="सोऽस्यादिरिति छन्दसः प्रगाथेषु. पाङ्क्तः प्रगाथः; "
             "आनुष्टुभः, जागतः.\n\n"
             "**FIVE WORDS AND THE VṚTTI ASSIGNS A JOB TO EACH.** "
             "स इति समर्थविभक्तिः; अस्येति प्रत्ययार्थः; आदिरिति "
             "प्रकृतिविशेषणम्; इतिकरणो विवक्षार्थः; छन्दस इति "
             "प्रकृतिनिर्देशः; प्रगाथेष्विति प्रत्ययार्थविशेषणम्. Six "
             "jobs for six words, laid out before a single example.\n\n"
             "आदिरिति किम्? अनुष्टुब् मध्यमस्य. छन्दस इति किम्? "
             "उदुत्यशब्द आदिरस्य. प्रगाथेष्विति किम्? पङ्क्तिरादिर् "
             "अस्यानुवाकस्य. And प्रगाथ is defined: यत्र द्वे ऋचौ "
             "प्रग्रथनेन तिस्रः क्रियन्ते — where two verses are made "
             "three by being woven together",
         keeps_out="पङ्क्तिरादिरस्यानुवाकस्य"),
    SenseRule("4.2.56", case="prathamā", sense="asya", result="saṃgrāma",
         of_samjna="prayojana-yoddhṛ",
         why="संग्रामे प्रयोजनयोद्धृभ्यः. भाद्रः संग्रामः, "
             "सौभद्रः, गौरिमित्रः; and from the fighters — आहिमालः, "
             "स्यान्दनाश्वः, भारतः.\n\n"
             "संग्राम इति किम्? सुभद्रा प्रयोजनमस्य दानस्य. "
             "प्रयोजनयोद्धृभ्य इति किम्? सुभद्रा प्रेक्षिकास्य "
             "संग्रामस्य — a battle someone merely WATCHES is not a "
             "battle she is the cause of",
         keeps_out="सुभद्रा प्रेक्षिकास्य संग्रामस्य"),
    SenseRule("4.2.57", case="prathamā", sense="asyām", result="krīḍā",
         gives="ṇa", of_samjna="praharaṇa",
         why="तदस्मिन् प्रहरणमिति क्रीडायाम्. दण्डः प्रहरणमस्यां "
             "क्रीडायां **दाण्डा**; मौष्टा. प्रहरणमिति किम्? माला "
             "भूषणमस्यां क्रीडायाम्. क्रीडायामिति किम्? खङ्गः "
             "प्रहरणमस्यां सेनायाम् — the same weapon in an army "
             "rather than a game",
         keeps_out="खङ्गः प्रहरणमस्यां सेनायाम्"),
    SenseRule("4.2.58", case="prathamā", sense="asyām", gives="ña",
         of_samjna="ghañ-kriyā",
         why="घञः स्त्रियाम्. श्यैनंपाता, तैलंपाता. घञ इति "
             "कृद्ग्रहणम्, तत्र गतिकारकपूर्वमपि गृह्यते.\n\n"
             "**AND THE VṚTTI ASKS WHY THE CASE AND THE SENSE ARE "
             "STATED AGAIN WHEN BOTH ARE ALREADY RUNNING.** अथ "
             "समर्थविभक्तिः प्रत्ययार्थश्च कस्मात् पुनरुपादीयते, "
             "यावता द्वयमपि प्रकृतमेव? **क्रीडायामित्यनेन तत् "
             "संबद्धम्, अतस्तदनुवृत्तौ क्रीडानुवृत्तिरपि "
             "संभाव्येत** — because they came bundled with *in a "
             "game*, and carrying them would have carried that too. "
             "Restating them is how the bundle is broken, which is "
             "4.2.24's move and 4.1.65's.\n\n"
             "सामान्येन चेदं विधानम् — दाण्डपाता तिथिः, "
             "मौसलपाता तिथिः: a DAY, not a game",
         keeps_out="प्राकारोऽस्यां वर्तते"),
    # --- तदधीते तद्वेद -----------------------------------------------
    SenseRule("4.2.59", case="dvitīyā", sense="adhīte-veda",
         why="तदधीते तद्वेद. छान्दसः, वैयाकरणः, नैरुक्तः; and for "
             "the knower — नैमित्तः, मौहूर्तः, औत्पातः.\n\n"
             "**द्विस्तद्ग्रहणम् अध्ीयानविदुषोः पृथग्विधानार्थम्** — "
             "the word *that* is said TWICE so the two are given "
             "separately: one who studies it and one who knows it are "
             "not the same person, and a single statement would have "
             "required both at once"),
    SenseRule("4.2.60", case="dvitīyā", sense="adhīte-veda", gives="ṭhak",
         gana="ukthādi", excepts=("4.1.83",),
         why="क्रतूक्थादिसूत्रान्ताट् ठक्, अणोऽपवादः. आग्निष्टोमिकः, "
             "वाजपेयिकः; औक्थिकः, लौकायतिकः; वार्तिकसूत्रिकः.\n\n"
             "**THE LONGEST VĀRTTIKA-SET IN THE PĀDA**, and it is "
             "about what people study. विद्यालक्षणकल्पान्तात् — "
             "वायसविद्यिकः, गौलक्षणिकः, मातृकल्पिकः; and "
             "**विद्या च नाङ्गक्षत्रधर्मसंसर्गत्रिपूर्वा**, five "
             "compounds excluded by name. "
             "आख्यानाख्यायिकेतिहासपुराणेभ्यष्ठक् — यावक्रीतिकः, "
             "वासवदत्तिकः, ऐतिहासिकः, पौराणिकः, and the vṛtti says "
             "**आख्यानाख्यायिकयोरर्थग्रहणम्, इतिहासपुराणयोः "
             "स्वरूपग्रहणम्**: two of the four are taken by their "
             "MEANING and two by their FORM.\n\n"
             "And a word is refused for a reason outside grammar: "
             "औक्थिक्यशब्दाच्च प्रत्ययो न भवत्येव, **अनभिधानात्** — "
             "because no one says it"),
    SenseRule("4.2.61", case="dvitīyā", sense="adhīte-veda", gives="vun",
         gana="kramādi", excepts=("4.1.83",),
         why="क्रमादिभ्यो वुन्, अणोऽपवादः. क्रमकः, पदकः"),
    SenseRule("4.2.62", case="dvitīyā", sense="adhīte-veda", gives="ini",
         of=("anubrāhmaṇa",), excepts=("4.1.83",),
         why="अनुब्राह्मणादिनिः, अणोऽपवादः. अनुब्राह्मणी. "
             "ब्राह्मणसदृशोऽयं ग्रन्थोऽनुब्राह्मणम्.\n\n"
             "मत्वर्थेन **अत इनिठनौ** इतीनिना सिद्धम्? तत्रैतस्माट् "
             "ठन्नपि प्राप्नोति. अनभिधानान्न भविष्यति? "
             "**अणो निवृत्त्यर्थं तर्हि वचनम्** — the vṛtti tries "
             "three answers and settles on the last: the rule is "
             "there to keep the default out. The fourth time in two "
             "pādas a rule has been read that way"),
    SenseRule("4.2.63", case="dvitīyā", sense="adhīte-veda", gives="ṭhak",
         gana="vasantādi", excepts=("4.1.83",),
         why="वसन्तादिभ्यष्ठक्, अणोऽपवादः. वासन्तिकः, वार्षिकः. "
             "**वसन्तसहचरितोऽयं ग्रन्थो वसन्तः** — the text is "
             "called by the season it goes with, and the affix is "
             "given to the text"),
    SenseRule("4.2.64", case="dvitīyā", sense="adhīte-veda",
         of_samjna="prokta", elides=True,
         why="प्रोक्ताल्लुक्. **प्रोक्तसहचरितः प्रत्ययः प्रोक्तः** — "
             "an affix given in the sense *declared by* is itself "
             "called *declared*, by association. पाणिनिना प्रोक्तं "
             "पाणिनीयम्, तदधीते **पाणिनीयः** — and the second affix "
             "is elided, so the student and the work are one word. "
             "आपिशलः. स्त्रियां स्वरे च विशेषः — पाणिनीया ब्राह्मणी"),
    SenseRule("4.2.65", case="dvitīyā", sense="adhīte-veda",
         of_samjna="sūtra-ka-upadha", elides=True,
         why="सूत्राच्च कोपधात्. **अप्रोक्तार्थ आरम्भः** — begun for "
             "the case the rule before could not reach, the text not "
             "being *declared by* anyone. पाणिनीयमष्टकं सूत्रम्, "
             "तदधीयते **अष्टकाः पाणिनीयाः**; दशका वैयाघ्रपदीयाः; "
             "त्रिकाः काशकृत्स्नाः — students named by how many "
             "sections their book has.\n\n"
             "संख्याप्रकृतेरिति वक्तव्यम्: इह मा भूत् — माहावार्तिकः, "
             "कालापकः. कोपधादिति किम्? चातुष्टयः. And this is where "
             "the studying-sense stops",
         keeps_out="माहावार्तिकः, चातुष्टयः"),
    SenseRule("4.2.66", of_samjna="prokta-chandas-brāhmaṇa",
         why="छन्दोब्राह्मणानि च तद्विषयाणि. **A RULE THAT RESTRICTS "
             "RATHER THAN GIVES, AND WHAT IT RESTRICTS IS A WHOLE "
             "CLASS OF WORDS.** छन्दांसि ब्राह्मणानि च "
             "प्रोक्तप्रत्ययान्तानि **तद्विषयाण्येव भवन्ति** — a "
             "Vedic text or a Brāhmaṇa named by *declared by* is used "
             "of THAT SUBJECT ONLY. कठाः, मौदाः, पैप्पलादाः, "
             "वाजसनेयिनः; ताण्डिनः, भाल्लविनः, ऐतरेयिणः.\n\n"
             "**अनन्यभावो विषयार्थः, तेन स्वातन्त्र्यम् "
             "उपाध्यन्तरयोगो वाक्यं च निवर्तते** — the word "
             "*subject* means having no other being, and three things "
             "fall away with it: the word standing on its own, its "
             "joining another qualifier, and the phrase in place of "
             "the word. One restriction doing three refusals.\n\n"
             "ब्राह्मणग्रहणं किम्, यावता छन्द एव तद्? "
             "ब्राह्मणविशेषप्रतिपत्त्यर्थम् — याज्ञवल्कानि, "
             "सौलभानि stay outside. And चकारोऽनुक्तसमुच्चयार्थः "
             "brings in the ritual manuals and the aphorisms: "
             "काश्यपिनः, पाराशरिणो भिक्षवः, **शैलालिनो नटाः** — "
             "actors, in a grammar of the Veda. छन्दोब्राह्मणानीति "
             "किम्? पाणिनीयं व्याकरणम्",
         keeps_out="पाणिनीयं व्याकरणम्"),
    # --- the four senses ---------------------------------------------
    SenseRule("4.2.67", case="prathamā", sense="cāturarthika",
         result="asti-deśe",
         why="तदस्मिन्नस्तीति देशे तन्नाम्नि. उदुम्बरा अस्मिन् देशे "
             "सन्ति **औदुम्बरः**; बाल्बजः, पार्वतः.\n\n"
             "Five words and a job for each again: तदिति "
             "प्रथमासमर्थविभक्तिः, अस्मिन्निति प्रत्ययार्थः, अस्तीति "
             "प्रकृत्यर्थविशेषणम्, इतिकरणो विवक्षार्थः, देशे "
             "तन्नाम्नीति प्रत्ययार्थविशेषणम्.\n\n"
             "**तन्नाम्नि — the country must be NAMED by the derived "
             "word**, प्रत्ययान्तनामा. That clause is what 4.2.81 "
             "will lean on to keep the elision off. "
             "मत्वर्थीयापवादो योगः"),
    SenseRule("4.2.68", case="tṛtīyā", sense="cāturarthika",
         result="nirvṛtta",
         why="तेन निर्वृत्तम्. सहस्रेण निर्वृत्ता **साहस्री परिखा**; "
             "कुशाम्बेन निर्वृत्ता **कौशाम्बी नगरी** — a moat made at "
             "the cost of a thousand, and a city founded by Kuśāmba. "
             "**हेतौ कर्तरि च यथायोगं तृतीया समर्थविभक्तिः**: the "
             "instrumental is read as the CAUSE in one and as the "
             "DOER in the other, whichever fits.\n\n"
             "देशे तन्नाम्नीति **चतुर्ष्वपि योगेषु संबध्यते** — the "
             "clause from the rule before holds in all four"),
    SenseRule("4.2.69", case="ṣaṣṭhī", sense="cāturarthika",
         result="nivāsa",
         why="तस्य निवासः. **निवसन्त्यस्मिन्निति निवासः** — that in "
             "which people dwell. ऋजुनावां निवासो देश आर्जुनावः; "
             "शैबः, औदिष्ठः"),
    SenseRule("4.2.70", case="ṣaṣṭhī", sense="cāturarthika",
         result="adūrabhava",
         why="अदूरभवश्च. विदिशाया अदूरभवं नगरं **वैदिशम्**; "
             "हैमवतम्.\n\n"
             "**AND THE च IS WHAT MAKES FOUR SENSES OUT OF FOUR "
             "RULES.** चकारः **पूर्वेषां त्रयाणामर्थानामिह "
             "सन्निधानार्थः, तेनोत्तरेषु चत्वारोऽप्यर्थाः "
             "संबध्यन्ते** — the conjunction brings the previous "
             "three alongside this one, and from here all four carry "
             "together into every rule that follows. The affixes of "
             "that whole run are called चातुरर्थिक, "
             "*of-the-four-senses*: **a name for a body of rules "
             "taken from a NUMBER, and the number produced by a "
             "single syllable**"),
    # --- and the affixes for them ------------------------------------
    SenseRule("4.2.71", sense="cāturarthika", gives="añ", stem_final="u",
         excepts=("4.1.83",),
         why="ओरञ्, अणोऽपवादः. आरडवम्, काक्षतवम्, कार्कटेलवम्. "
             "नद्यां तु परत्वाद् मतुब् भवति — इक्षुमती, 4.2.85 "
             "winning by परत्व.\n\n"
             "**अञधिकारः प्राक् सुवास्त्वादिभ्योऽणः** — this affix "
             "governs as far as 4.2.77, which is the sixth stated "
             "range in the pāda and the first stated of an AFFIX "
             "rather than of a case or a sense"),
    SenseRule("4.2.72", sense="cāturarthika", gives="añ",
         of_samjna="matup-bahvac-aṅga", excepts=("4.1.83",),
         why="मतोश्च बह्वजङ्गात्, अणोऽपवादः. ऐषुकावतम्, "
             "सैध्रकावतम्. बह्वजङ्गादिति किम्? आहिमतम्, यावमतम्.\n\n"
             "**अङ्गग्रहणं किम्? बह्वजिति तद्विशेषणं यथा विज्ञायेत, "
             "मत्वन्तविशेषणं मा विज्ञायि** — the word अङ्ग is there "
             "so that *many-voweled* qualifies what the मतुप् is "
             "ADDED TO and not the whole word: मालावतां निवासो "
             "मालावतम्. A word inserted to fix which of two things "
             "an adjective attaches to"),
    SenseRule("4.2.73", sense="cāturarthika", gives="añ", dvyac=True,
         result="kūpa", excepts=("4.1.83",),
         why="बह्वचः कूपेषु, अणोऽपवादः. दीर्घवरत्रेण निर्वृत्तः कूपो "
             "दैर्घवरत्रः; कापिलवरत्रः. **यथासंभवमर्थाः "
             "संबध्यन्ते** — whichever of the four senses fits, and "
             "the vṛtti says so at nearly every rule of this run"),
    SenseRule("4.2.74", sense="cāturarthika", gives="añ", result="kūpa",
         of_samjna="udak-vipāś", excepts=("4.1.83",),
         why="उदक् च विपाशः. Wells on the NORTH bank of the Vipāś: "
             "दात्तः, गौप्तः. **अबह्वजर्थ आरम्भः** — begun for wells "
             "whose names have few vowels, which the rule before "
             "could not reach.\n\n"
             "उदगिति किम्? दक्षिणतो विपाशः कूपेष्वणेव — south of the "
             "river the DEFAULT affix comes, and **स्वरे विशेषः**, "
             "the two differ only in accent. The vṛtti's own comment "
             "on a rule that turns on which bank of a river a well "
             "stands: **महती सूक्ष्मेक्षिका वर्तते सूत्रकारस्य** — "
             "*the sūtra-maker's eye for fine distinctions is "
             "great*",
         keeps_out="दक्षिणतो विपाशः"),
    SenseRule("4.2.75", sense="cāturarthika", gives="añ", gana="saṃkalādi",
         excepts=("4.1.83",),
         why="संकलादिभ्यश्च, अणोऽपवादः. **कूपेष्विति निवृत्तम्** — "
             "the wells stop here. सांकलः, पौष्कलः"),
    SenseRule("4.2.76", sense="cāturarthika", gives="añ",
         of_samjna="strī-sauvīra-sālva-prāc", excepts=("4.1.83",),
         why="स्त्रीषु सौवीरसाल्वप्राक्षु. दात्तामित्री; वैधूमाग्नी; "
             "काकन्दी, माकन्दी, माणिचरी, जारुषी — FEMININE "
             "place-names in three regions, and the condition is "
             "the gender of the country's name"),
    SenseRule("4.2.77", sense="cāturarthika", gives="aṇ", gana="suvāstvādi",
         excepts=("4.2.71", "4.2.73"),
         why="सुवास्त्वादिभ्योऽण्, अञ उवर्णान्तलक्षणस्य "
             "कूपलक्षणस्य चापवादः. सौवास्तवम्, वार्णवम् — and this "
             "is the rule 4.2.71's vṛtti named as where its affix "
             "stops. **अण्ग्रहणं नद्यां मतुपो बाधनार्थम्**: the "
             "default is named expressly to beat 4.2.85, सौवास्तवी "
             "नदी. 4.1.84's move for the fifth time"),
    SenseRule("4.2.78", sense="cāturarthika", gives="aṇ", of=("roṇī",),
         excepts=("4.2.73",),
         why="रोणी. **रोणीति कोऽयं निर्देशः, यावता प्रत्ययविधौ "
             "पञ्चमी युक्ता?** — a rule that gives an affix should "
             "name its base in the ablative, and this names it in "
             "the nominative. **सर्वावस्थप्रतिपत्त्यर्थमेवमुच्यते**: "
             "so that the word is taken in EVERY state, alone and as "
             "a final member — रौणः, आजकरोणः, सैंहिकरोणः. A case "
             "deliberately wrong so that a restriction may not "
             "follow from it"),
    SenseRule("4.2.79", sense="cāturarthika", gives="aṇ",
         of_samjna="ka-upadha", excepts=("4.2.71", "4.2.73"),
         why="कोपधाच्च. कार्णच्छिद्रिकः कूपः, कार्णवेष्टकः; "
             "कार्कवाकवम्, त्रैशङ्कवम्"),
    SenseRule("4.2.80", sense="cāturarthika", gives="vuñ",
         gana="arīhaṇādi", excepts=("4.1.83",),
         why="वुञ्छण्कठजिलसेनिरढञ्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्व"
             "र्श्यकुमुदकाशतृणप्रेक्षाश्मसखिसंकाशबलपक्षकर्ण"
             "सुतङ्गमप्रगदिन्वराहकुमुदादिभ्यः.\n\n"
             "**SEVENTEEN AFFIXES AND SEVENTEEN LISTS, MATCHED IN "
             "ORDER.** वुञादयः सप्तदश प्रत्ययाः, अरीहणादयोऽपि "
             "सप्तदशैव प्रातिपदिकगणाः, **आदिशब्दः प्रत्येकम् "
             "अभिसंबध्यते** — and the word *and-the-rest* attaches to "
             "each of the seventeen separately. The longest "
             "यथासंख्य correspondence in the grammar, five times the "
             "length of 4.1.42's eleven.\n\n"
             "आरीहणकम्, कार्शाश्वीयः, ऋश्यकः, कुमुदिकम्, काशिलम्, "
             "तृणसः, प्रेक्षी, अश्मरः, साखेयम्, सांकाश्यम्, बल्यः, "
             "पाक्षायणः, कार्णायनिः, सौतङ्गमिः, प्रागद्यम्, "
             "वाराहकम्, कौमुदिकम् — seventeen forms, one from each.\n\n"
             "And one word is in THREE of the seventeen lists: "
             "शिरीषशब्दोऽरीहणादिषु, कुमुदादिषु, वराहादिषु च पठ्यते, "
             "**औत्सर्गिकोऽपि तत इष्यते** — and the default is "
             "wanted from it as well, so it has four affixes, and "
             "then 4.2.82's list elides one of them"),
    # --- and where the affix vanishes --------------------------------
    SenseRule("4.2.81", sense="cāturarthika", of_samjna="janapada",
         elides=True,
         why="जनपदे लुप्. **ग्रामसमुदायो जनपदः** — where the country "
             "is a group of villages the affix is DROPPED: "
             "पञ्चालानां निवासो जनपदः **पञ्चालाः**; कुरवः, मत्स्याः, "
             "अङ्गाः, वङ्गाः, मगधाः. The affix is given and removed, "
             "and what remains is the name of a people used as the "
             "name of their country.\n\n"
             "इह कस्माद् न भवति — औदुम्बरो जनपदः, वैदिशो जनपदः? "
             "**तन्नाम्नीति वर्तते, न चात्र लुबन्तं तन्नामधेयं "
             "भवति** — 4.2.67's clause carries down, and the elided "
             "form is not what those countries are called. A "
             "condition stated fourteen sūtras earlier deciding "
             "where an elision may bite",
         keeps_out="औदुम्बरो जनपदः"),
    SenseRule("4.2.82", sense="cāturarthika", gana="varaṇādi", elides=True,
         why="वरणादिभ्यश्च. **अजनपदार्थ आरम्भः** — begun for what is "
             "not a country: वरणानामदूरभवं नगरं **वरणाः**; शृङ्गी, "
             "शाल्मलयः. चकारोऽनुक्तसमुच्चयार्थ आकृतिगणतामस्य "
             "बोधयति — कटुकबदरी, शिरीषाः, काञ्ची"),
    SenseRule("4.2.83", sense="cāturarthika", of=("śarkarā",), elides=True,
         optional=True,
         why="शर्करायां वा. शर्करा beside शार्करम्.\n\n"
             "**AND THE वा IS READ AS A ज्ञापक.** वाग्रहणं किम्, "
             "यावता शर्कराशब्दः कुमुदादिषु वराहादिषु च पठ्यते, तत्र "
             "पाठसामर्थ्यात् प्रत्ययस्य पक्षे श्रवणं भविष्यति? — "
             "being in two of 4.2.80's lists would already have given "
             "the alternative. **एवं तर्ह्येतज् ज्ञापयति — "
             "शर्कराशब्दादौत्सर्गिको भवति, तस्यायं विकल्पितो लुब्** "
             "iti: so the word teaches that the DEFAULT affix comes "
             "from this word too, and it is that one being optionally "
             "elided.\n\n"
             "**तदेवं षड् रूपाणि भवन्ति** — शर्करा, शार्करम्, "
             "शर्करिकम्, शार्करकम्, शार्करिकम्, शर्करीयम्. Six forms "
             "for one word, counted out"),
    SenseRule("4.2.84", sense="cāturarthika", gives="ṭhak",
         of=("śarkarā",),
         why="ठक्छौ च. शार्करिकम्, शर्करीयम् — the two that bring "
             "the count to six"),
    SenseRule("4.2.85", sense="cāturarthika", gives="matup", result="nadī",
         why="नद्यां मतुप्. उदुम्बरा यस्यां सन्ति **उदुम्बरावती**; "
             "मशकावती, वीरणावती, पुष्करावती, इक्षुमती, द्रुमती. "
             "**तन्नाम्नो देशस्य विशेषणं नदी** — the river qualifies "
             "the named country.\n\n"
             "इह कस्माद् न भवति — भागीरथी, भैमरथी? "
             "**मतुबन्तस्यातन्नामधेयत्वात्** — those rivers are not "
             "called by a मतुप्-form, and 4.2.67's clause is again "
             "what decides",
         keeps_out="भागीरथी"),
    SenseRule("4.2.86", sense="cāturarthika", gives="matup",
         gana="madhvādi",
         why="मध्वादिभ्यश्च. **अनद्यर्थ आरम्भः** — begun for what is "
             "not a river. मधुमान्, बिसवान्"),
    SenseRule("4.2.87", sense="cāturarthika", gives="ḍmatup",
         of=("kumuda", "naḍa", "vetasa"),
         why="कुमुदनडवेतसेभ्यो ड्मतुप्. कुमुद्वान्, नड्वान्, "
             "वेतस्वान्. महिषाच्चेति वक्तव्यम् — महिष्मान् नाम देशः"),
    SenseRule("4.2.88", sense="cāturarthika", gives="ḍvalac",
         of=("naḍa", "śāda"),
         why="नडशादाड् ड्वलच्. नड्वलम्, शाद्वलम्"),
    SenseRule("4.2.89", sense="cāturarthika", gives="valac",
         of=("śikhā",),
         why="शिखाया वलच्. शिखावलं नाम नगरम्. "
             "मतुप्प्रकरणेऽपि शिखाया वलचं वक्ष्यति, "
             "**तददेशार्थं वचनम्** — 5.2.113 will give the same "
             "affix to the same word, and that one is for what is "
             "NOT a place. Two rules, one affix, one base, told apart "
             "by what the result is — 4.2.18's shape again"),
    SenseRule("4.2.90", sense="cāturarthika", gives="cha", gana="utkarādi",
         why="उत्करादिभ्यश्छः. उत्करीयम्, शफरीयम्"),
    SenseRule("4.2.91", sense="cāturarthika", gives="cha", gana="naḍādi",
         along_with="kuk",
         why="नडादीनां कुक् च. नडकीयम्, प्लक्षकीयम् — the affix and "
             "an augment together, and this is where the "
             "four-senses run stops"),
    SenseRule("4.2.92", sense="śeṣa",
         why="शेषे. **अधिकारोऽयम्** — यानित ऊर्ध्वं प्रत्ययान् "
             "अनुक्रमिष्यामः, शेषेऽर्थे ते वेदितव्याः.\n\n"
             "**A HEADING WHOSE CONTENT IS *EVERYTHING NOT ALREADY "
             "PROVIDED FOR*.** उपयुक्तादन्यः शेषः — "
             "अपत्यादिभ्यश्चतुरर्थपर्यन्तेभ्योऽन्योऽर्थः शेषः: "
             "whatever is left over from the descendant-sense through "
             "the four. Not a sense at all but the complement of all "
             "the senses so far, which is what 3.4.114's "
             "आर्धधातुकं शेषः was for names.\n\n"
             "AND THE VṚTTI GIVES TWO REASONS FOR STATING IT. "
             "तस्येदंविशेषा ह्यपत्यसमूहादयः, **तेषु घादयो मा "
             "भूवन्निति शेषाधिकारः क्रियते** — the earlier senses are "
             "special cases of *this belongs to that*, and without "
             "the heading the affixes from here would reach them. "
             "किं च, सर्वेषु जातादिषु घादयो यथा स्युः, अनन्तरेणैव "
             "अर्थादेशेन संबन्धित्वेन कृतार्थता मा विज्ञायि इति "
             "**साकल्यार्थं शेषवचनम्**: and so that they reach ALL "
             "of what remains rather than only the nearest sense. "
             "One word doing an exclusion and an inclusion at "
             "once.\n\n"
             "**शेष इति लक्षणं चाधिकारश्च** — it is both a statement "
             "of the ground and a heading. चाक्षुषं रूपम्, श्रावणः "
             "शब्दः, दार्षदाः सक्तवः, औलूखलो यावकः, आश्वो रथः, "
             "चातुरं शकटम्, चातुर्दशं रक्षः"),
    SenseRule("4.2.93", sense="śeṣa", gives="gha", of=("rāṣṭra",),
         why="राष्ट्रावारपाराद् घखौ, यथासंख्यम्. राष्ट्रियः; "
             "अवारपारीणः. विगृहीतादपीष्यते — अवारीणः, पारीणः; and "
             "विपरीताच्च — पारावारीणः.\n\n"
             "**AND THE AFFIX COMES FIRST, THE SENSE AFTERWARDS.** "
             "**प्रकृतिविशेषोपादानमात्रेण तावत् प्रत्यया विधीयन्ते; "
             "तेषां तु जातादयोऽर्थाः समर्थविभक्तयश्च पुरस्ताद् "
             "वक्ष्यन्ते** — these rules give affixes by naming their "
             "BASES only, and the senses they carry and the cases "
             "they attach in will be stated further on, at 4.3.53 and "
             "after. The exact reverse of everything from 4.2.1 to "
             "4.2.91, where a rule named a case and a sense and left "
             "the affix to be understood.\n\n"
             "That is what 4.2.92's शेषे makes possible: with the "
             "sense given as *whatever is left*, an affix can be "
             "supplied before anyone has said what it will mean"),
    SenseRule("4.2.93", sense="śeṣa", gives="kha", of=("avārapāra",),
         why="राष्ट्रावारपाराद् घखौ — अवारपारीणः, and the vārttikas "
             "take the compound apart and reverse it: अवारीणः, "
             "पारीणः, पारावारीणः"),
    SenseRule("4.2.94", sense="śeṣa", gives="ya", of=("grāma",),
         why="ग्रामाद् यखञौ. ग्राम्यः, ग्रामीणः — two affixes and no "
             "option stated, so both stand"),
    SenseRule("4.2.95", sense="śeṣa", gives="ḍhakañ", gana="katryādi",
         why="कत्र्यादिभ्यो ढकञ्. कात्रेयकः, औम्भेयकः"),
    SenseRule("4.2.96", sense="śeṣa", gives="ḍhakañ", of=("kula",),
         result="śvan",
         why="कुलकुक्षिग्रीवाभ्यः श्वास्यलंकारेषु, यथासंख्यम्. "
             "**कौलेयको भवति श्वा चेत्, कौलोऽन्यः** — a DOG of the "
             "family takes one affix and anything else the other; "
             "कौक्षेयको भवत्यसिश्चेत् for a sword, ग्रैवेयको "
             "भवत्यलंकारश्चेत् for an ornament. Three bases, three "
             "things the result must BE, matched in order — and each "
             "with the form that stands when it is something else"),
    SenseRule("4.2.97", sense="śeṣa", gives="ḍhak", gana="nadyādi",
         why="नद्यादिभ्यो ढक्. नादेयम्, माहेयम्.\n\n"
             "**TWO READINGS OF ONE LIST-ENTRY, AND BOTH ARE "
             "AUTHORITATIVE.** पूर्वनगरीशब्दोऽत्र पठ्यते — "
             "पौर्वनगरेयम्. **केचित् तु पूर्वनगिरीति पठन्ति, "
             "विच्छिद्य च प्रत्ययं कुर्वन्ति** — पौरेयम्, वानेयम्, "
             "गैरेयम्: others read the entry as three words and give "
             "the affix to each. **तदुभयमपि दर्शनं प्रमाणम्**. The "
             "same verdict 4.1.117 gave about two readings of a "
             "sūtra, here about two readings of a गण"),
    SenseRule("4.2.98", sense="śeṣa", gives="tyak",
         of=("dakṣiṇā", "paścāt", "puras"),
         why="दक्षिणापश्चात्पुरसस्त्यक्. दाक्षिणात्यः, पाश्चात्त्यः, "
             "पौरस्त्यः"),
    SenseRule("4.2.99", sense="śeṣa", gives="ṣphak", of=("kāpiśī",),
         why="कापिश्याः ष्फक्. **षकारो ङीषर्थः** — the ष् so that "
             "4.1.41's ङीष् comes in the feminine: कापिशायनं मधु, "
             "कापिशायनी द्राक्षा. A letter placed a hundred and "
             "fifty-eight sūtras from the rule that spends it. "
             "बाह्ल्युर्दिपर्दिभ्यश्चेति वक्तव्यम्"),
    SenseRule("4.2.100", sense="śeṣa", gives="aṇ", of=("raṅku",),
         of_samjna="amanuṣya",
         why="रङ्कोरमनुष्येऽण् च. राङ्कवो गौः; and by the च also "
             "राङ्कवायणो गौः. अमनुष्य इति किम्? राङ्कवको मनुष्यः.\n\n"
             "**A NEGATIVE READ AS *LIKE-BUT-NOT* RATHER THAN AS "
             "*NOT*.** The vṛtti objects that the exclusion is "
             "already had from elsewhere, and answers: **नैवायं "
             "मनुष्यप्रतिषेधः; किं तर्हि? नञिवयुक्तन्यायेन "
             "मनुष्यसदृशे प्राणिनि प्रतिपत्तिः क्रियते** — अमनुष्य "
             "does not mean *not a man* but *a living thing RESEMBLING "
             "a man*, by the principle that a नञ् is joined with an "
             "*iva*. तेन **राङ्कवः कम्बल** इति ष्फग् न भवति: a "
             "blanket is not a man and not like one either, so the "
             "second affix stays off it.\n\n"
             "A whole class of things excluded by reading a negative "
             "as a comparison",
         keeps_out="राङ्कवको मनुष्यः, राङ्कवः कम्बलः"),
    SenseRule("4.2.101", sense="śeṣa", gives="yat",
         of=("div", "prāc", "apāc", "udac", "pratyac"),
         why="दिक्प्रागपागुदक्प्रतीचो यत्. दिव्यम्, प्राच्यम्, "
             "अपाच्यम्, उदीच्यम्, प्रतीच्यम्. अव्ययात् तु "
             "कालवाचिनः परत्वात् ट्युट्युलौ भवतः — प्राक्तनम्"),
    SenseRule("4.2.102", sense="śeṣa", gives="ṭhak", of=("kanthā",),
         why="कन्थायाष्ठक्. कान्थिकः"),
    SenseRule("4.2.103", sense="śeṣa", gives="vuk", of=("kanthā",),
         of_samjna="varṇu", excepts=("4.2.102",),
         why="वर्णौ वुक्, ठकोऽपवादः. **वर्णुर्नाम नदः, तत्समीपो "
             "देशो वर्णुः** — a river, and then the country beside "
             "it by the same name, and the rule is about the word "
             "कन्था used of THAT country. जातं हिमवत्सु कान्थकम्"),
    SenseRule("4.2.104", sense="śeṣa", gives="tyap", of_samjna="avyaya",
         why="अव्ययात् त्यप्. अमात्यः, इहत्यः, क्वत्यः, इतस्त्यः, "
             "तत्रत्यः, यत्रत्यः.\n\n"
             "**AND A VERSE ENUMERATES WHICH INDECLINABLES, BECAUSE "
             "THE RULE SAYS ONLY *AN INDECLINABLE*.** "
             "अमेहक्वतसित्रेभ्यस्त्यब्विधिर्योऽव्ययात् स्मृतः / "
             "निनिर्भ्यां ध्रुवगत्योश्च प्रवेशो नियमे तथा — six "
             "endings named, and two prefixes with the senses they "
             "must carry. **परिगणनं किम्?** औपरिष्टः, पौरस्तः, "
             "पारस्तः: without the count those would take it too. A "
             "kārikā doing the work of a गण.\n\n"
             "त्यब् नेर्ध्रुवे — नित्यम्; निसो गते — **निष्ट्यश्चण्डालादिः**, "
             "one gone out from the orders of life; आविसश्छन्दसि — "
             "आविष्ट्यो वर्धते (ऋ० १.९५.५); अरण्याण् णः — आरण्याः "
             "सुमनसः; दूरादेत्यः; उत्तरादाहञ् — औत्तराहम्",
         keeps_out="औपरिष्टः, पौरस्तः"),
    SenseRule("4.2.105", sense="śeṣa", gives="tyap",
         of=("aiṣamas", "hyas", "śvas"), optional=True,
         why="ऐषमोह्यःश्वसोऽन्यतरस्याम्. ऐषमस्त्यम् beside "
             "ऐषमस्तनम्; ह्यस्त्यम् beside ह्यस्तनम्; श्वस्त्यम् "
             "beside श्वस्तनम् — and **श्वसस्तुट् च इति ठञपि तृतीयो "
             "भवति**, शौवस्तिकम्: a third form for one of the three, "
             "from a rule in the next pāda"),
    SenseRule("4.2.106", sense="śeṣa", gives="añ", stem_final="tīra",
         excepts=("4.1.83",),
         why="तीररूप्योत्तरपदादञ्ञौ, यथासंख्यम्, अणोऽपवादौ. "
             "काकतीरम्, पाल्वलतीरम्; वार्करूप्यम्, शैवरूप्यम्.\n\n"
             "**तीररूप्यान्तादिति नोक्तम्, बहुच्प्रत्ययपूर्वाद् मा "
             "भूदिति** — the rule says *having तीर as its LAST "
             "MEMBER* and not *ending in तीर*, so that a word merely "
             "ending in those sounds is kept out: बाहुतीरम्, "
             "अणेव भवति. Two ways of saying almost the same thing, "
             "and the difference is a whole class of words",
         keeps_out="बाहुतीरम्"),
    SenseRule("4.2.107", sense="śeṣa", gives="ña", pre="dik",
         of_samjna="asaṃjñā", excepts=("4.1.83",),
         why="दिक्पूर्वपदादसंज्ञायां ञः, अणोऽपवादः. पौर्वशालः, "
             "दाक्षिणशालः, आपरशालः. असंज्ञायामिति किम्? "
             "पूर्वैषुकामशमः. **पदग्रहणं स्वरूपविधिनिरासार्थम्** — "
             "the word *member* is there so the rule is not read of "
             "the bare word दिश् itself"),
    SenseRule("4.2.108", sense="śeṣa", gives="añ", of=("madra",),
         pre="dik", excepts=("4.1.83",),
         why="मद्रेभ्योऽञ्. पौर्वमद्रः, आपरमद्रः. "
             "दिशोऽमद्राणाम् इति पर्युदासाद् आदिवृद्धिरेव — a rule "
             "of the seventh chapter excepts this very word by name, "
             "and the exception is what fixes which member is "
             "strengthened"),
    SenseRule("4.2.109", sense="śeṣa", gives="añ",
         of_samjna="udīcya-grāma", dvyac=True, accent="antodātta",
         excepts=("4.1.83",),
         why="उदीच्यग्रामाच्च बह्वचोऽन्तोदात्तात्, अणोऽपवादः. "
             "शैवपुरम्, माण्डवपुरम्. **दिग्ग्रहणं निवृत्तम्** — the "
             "direction stops carrying here.\n\n"
             "Three words and a counter-example each: "
             "उदीच्यग्रामादिति किम्? माथुरम्. बह्वच इति किम्? "
             "ध्वाजम्. अन्तोदात्तादिति किम्? शार्करीधानम्, where "
             "**लित्स्वरेण धाशब्द उदात्तः** — the accent falls "
             "elsewhere by a mark on a different affix entirely",
         keeps_out="माथुरम्, ध्वाजम्, शार्करीधानम्"),
    SenseRule("4.2.110", sense="śeṣa", gives="aṇ", stem_final="prastha",
         excepts=("4.2.109",),
         why="प्रस्थोत्तरपदपलद्यादिकोपधादण्, उदीच्यग्रामलक्षणस्य "
             "अञोऽपवादः. माद्रीप्रस्थः; पालदः, पारिषदः; नैलीनकः, "
             "चैयातकः.\n\n"
             "**अण्ग्रहणं बाधकबाधनार्थम्** — the default named to "
             "beat what would have beaten it, the sixth time in two "
             "pādas. And the list carries three separate purposes: "
             "one member is there to beat 4.2.117, one to beat "
             "4.2.123, and वाहीक is in it **कोपधोऽपि पुनः पठ्यते "
             "परं छं बाधितुम्** — read again though it already "
             "qualifies, in order to beat a later rule"),
    SenseRule("4.2.111", sense="śeṣa", gives="aṇ", marked="kaṇvādi-gotra",
         excepts=("4.2.114",),
         why="कण्वादिभ्यो गोत्रे, छस्यापवादः. काण्वाश्छात्राः, "
             "गौकक्षाः.\n\n"
             "**गोत्रमिह न प्रत्ययार्थो न च प्रकृतिविशेषणम्** — the "
             "word गोत्र here is neither the sense of the affix nor "
             "a qualifier of the base. तर्ह्येवं संबध्यते: "
             "कण्वादिभ्यो गोत्रे यः प्रत्ययो विहितः, **तदन्तेभ्य "
             "एवाण्** — it points at the affix 4.1.111 gave in that "
             "sense, and this rule is stated of stems ending in "
             "THAT. A word in a rule naming neither ground nor sense "
             "but a rule"),
    SenseRule("4.2.112", sense="śeṣa", gives="aṇ", marked="iñ-gotra",
         excepts=("4.2.114",),
         why="इञश्च, छस्यापवादः. दाक्षाः, प्लाक्षाः, माहकाः. "
             "गोत्र इत्येव — सौतङ्गमेरिदं सौतङ्गमीयम्, where the "
             "इञ् is 4.2.80's and not a lineage-affix at all"),
    SenseRule("4.2.113", sense="śeṣa", gives="aṇ", dvyac=True,
         of_samjna="prācya-bharata-gotra", refuses=True,
         why="न द्व्यचः प्राच्यभरतेषु. पैङ्गीयाः, प्रौष्ठीयाः, "
             "चैदीयाः, काशीयाः. द्व्यच इति किम्? पान्नागाराः. "
             "प्राच्यभरतेष्विति किम्? दाक्षाः.\n\n"
             "**AND भरत IS NAMED SEPARATELY BECAUSE OF A ज्ञापक "
             "ELSEWHERE.** ज्ञापकाद् **अन्यत्र प्राच्यग्रहणेन "
             "भरतग्रहणं न भवतीति** स्वशब्देन भरतानामुपादानं कृतम् — "
             "2.4.66 teaches that *eastern* does not take in the "
             "Bharatas anywhere else, so this rule has to name them "
             "in their own word.\n\n"
             "काशीया इति कथमुदाहृतम्, यावता काश्यादिभ्यष्ठञ्ञिठाभ्यां "
             "भवितव्यम्? **देशवाचिनः काशिशब्दस्य तत्र ग्रहणम्, "
             "चेदिशब्देन साहचर्यात्** — the काशि of 4.2.116 is the "
             "COUNTRY, known by the company it keeps in that list",
         keeps_out="पान्नागाराः, दाक्षाः"),
    SenseRule("4.2.114", sense="śeṣa", gives="cha", of_samjna="vṛddha",
         excepts=("4.1.83",),
         why="वृद्धाच्छः, अणोऽपवादः. गार्गीयः, वात्सीयः, शालीयः, "
             "मालीयः. **गोत्र इति नानुवर्तते, सामान्येन विधानम्** — "
             "the lineage stops carrying and the rule is general.\n\n"
             "अव्ययतीररूप्योत्तरपदोदीच्यग्रामकोपधविधींस्तु "
             "**परत्वाद् बाधते** — it beats four earlier rules by "
             "standing later, and the vṛtti names all four"),
    SenseRule("4.2.115", sense="śeṣa", gives="ṭhak", of=("bhavat",),
         of_samjna="vṛddha", excepts=("4.2.114",),
         why="भवतष्ठक्छसौ, छस्यापवादौ. भावत्कः, भवदीयः. "
             "**सकारः पदसंज्ञार्थः**, and भवतस्त्यदादित्वाद् "
             "वृद्धसंज्ञा — the word is वृद्ध not by its own first "
             "vowel but by being one of the त्यदादि. "
             "अवृद्धात् तु भवतः शतुरणेव भवति — भावतः, where the same "
             "shape is a present participle and takes the default"),
    SenseRule("4.2.116", sense="śeṣa", gives="ṭhañ", gana="kāśyādi",
         of_samjna="vṛddha",
         why="काश्यादिभ्यष्ठञ्ञिठौ. काशिकी beside काशिका; चैदिकी "
             "beside चैदिका — **स्त्रीप्रत्यये विशेषः**, the two "
             "differ only in the feminine. ञकार एवोभयत्र "
             "विपर्यस्तदेशोऽनुबन्धः: the same mark, on opposite ends "
             "of the two affixes.\n\n"
             "**AND A STATEMENT OF THE MAHĀBHĀṢYA IS READ AS A "
             "व्यवस्थितविभाषा.** कथं भाष्य उदाहृतम् — वा नामधेयस्य "
             "वृद्धसंज्ञा वेदितव्या, देवदत्तीयाः, दैवदत्ताः? "
             "**तत्रैवं वर्णयन्ति — वा नामधेयस्येति "
             "व्यवस्थितविभाषेयम्, सा छे कर्तव्ये भवति, ठञ्ञिठयोर्न "
             "भवति**: the option holds where छ is to be given and "
             "not for these two. The instrument this project met "
             "first at 3.4.85, applied to a sentence of the "
             "Mahābhāṣya rather than to a word of a sūtra"),
    SenseRule("4.2.117", sense="śeṣa", gives="ṭhañ",
         of_samjna="vāhīka-grāma-vṛddha", excepts=("4.2.114",),
         why="वाहीकग्रामेभ्यश्च, छस्यापवादौ. शाकलिकी beside "
             "शाकलिका; मान्थविकी beside मान्थविका"),
    SenseRule("4.2.118", sense="śeṣa", gives="ṭhañ", optional=True,
         of_samjna="uśīnara-vāhīka-grāma-vṛddha",
         why="विभाषोशीनरेषु. उशीनरेषु ये वाहीकग्रामाः, "
             "तद्वाचिभ्यो वृद्धेभ्यः विभाषा ठञ्ञिठौ. आह्वजालिकी, "
             "आह्वजालिका, आह्वजालीय; सौदर्शनिकी, सौदर्शनिका, "
             "सौदर्शनीय — three forms where 4.2.117 gave two, "
             "because the option lets 4.2.114's छ back in"),
    SenseRule("4.2.119", sense="śeṣa", gives="ṭhañ", stem_final="u",
         desa=True,
         why="ओर्देशे ठञ्. नैषादकर्षुकः, शाबरजम्बुकः.\n\n"
             "**वृद्धादिति नानुवर्तते, उत्तरसूत्रे पुनर्वृद्धग्रहणात्** "
             "— वृद्ध stops carrying here, and the proof is that the "
             "NEXT rule names it again. A word read twice is a word "
             "that had lapsed.\n\n"
             "देश इति किम्? पटोश्छात्राः पाटवाः. And the affix is "
             "named though ठञ् was already in the air: "
             "**ठञ्ञिठयोः प्रकरणे ठञः केवलस्यानुवृत्तिर्न लभ्यत इति "
             "ठञ्ग्रहणं कृतम्** — where a rule gave TWO affixes "
             "together, neither can be carried on alone",
         keeps_out="पाटवाः"),
    SenseRule("4.2.120", sense="śeṣa", gives="ṭhañ", stem_final="u",
         desa=True, of_samjna="prāc-vṛddha",
         why="वृद्धात् प्राचाम्, ओर्दश इत्येव. आढकजम्बुकः, "
             "शाकजम्बुकः, नापितवास्तुकः.\n\n"
             "**पूर्वेणैव ठञि सिद्धे नियमार्थं वचनम्** — the "
             "preceding rule already gave ठञ् here, so this one is "
             "spoken to RESTRICT: वृद्धादेव प्राचाम्, among the "
             "eastern countries only from a वृद्ध base. मल्लवास्तु "
             "is not वृद्ध, and gives माल्लवास्तवः",
         keeps_out="माल्लवास्तवः"),
    SenseRule("4.2.121", sense="śeṣa", gives="vuñ", desa=True,
         of_samjna="vṛddha", ends_with=("dhanvan",),
         why="धन्वयोपधाद्वुञ्, the धन्व half. **धन्वशब्दो "
             "मरुदेशवचनः** — धन्व names a desert, so the rule is "
             "about compounds whose last member is one. पारेधन्वकः, "
             "ऐरावतकः"),
    SenseRule("4.2.121", sense="śeṣa", gives="vuñ", desa=True,
         of_samjna="vṛddha", upadha="y",
         why="धन्वयोपधाद्वुञ्, the योपध half. सांकाश्यकः, "
             "काम्पिल्यकः.\n\n"
             "**AND THE PENULTIMATE IS NOT THE FINAL.** This is the "
             "first rule of the pāda stated on उपधा, the sound "
             "1.1.65 defines as the one before the last. सांकाश्य "
             "does not END in य — it ends in अ — and a table that "
             "stored this in `stem_final` would answer for words "
             "the rule never reaches"),
    SenseRule("4.2.122", sense="śeṣa", gives="vuñ", desa=True,
         of_samjna="vṛddha", excepts=("4.2.114",),
         ends_with=("prastha", "pura", "vaha"),
         why="प्रस्थपुरवहान्ताच्च, छस्यापवादः. **अन्तशब्दः "
             "प्रत्येकमभिसंबध्यते** — the word *ending* attaches to "
             "each of the three separately, not to the three taken "
             "as one compound. मालाप्रस्थकः, नान्दीपुरकः, "
             "कान्तीपुरकः, पैलुवहकः, फाल्गुनीवहकः.\n\n"
             "पुरान्तो रोपधः — a word ending in पुर already has र "
             "for its penultimate, so 4.2.123 would have covered it; "
             "**अप्रागर्थमिह ग्रहणम्**, it is named here for the "
             "countries that are NOT eastern"),
    SenseRule("4.2.123", sense="śeṣa", gives="vuñ", desa=True,
         of_samjna="prāc-vṛddha", upadha="r", excepts=("4.2.114",),
         why="रोपधेतोः प्राचाम्, the रोपध half; छस्यापवादः. "
             "पाटलिपुत्रकाः, ऐकचक्रकाः. प्राचामिति किम्? "
             "दात्तामित्रीयः",
         keeps_out="दात्तामित्रीयः"),
    SenseRule("4.2.123", sense="śeṣa", gives="vuñ", desa=True,
         of_samjna="prāc-vṛddha", stem_final="ī", excepts=("4.2.114",),
         why="रोपधेतोः प्राचाम्, the ईत् half. काकन्दी — काकन्दकः; "
             "माकन्दी — माकन्दकः. **तपरकरणं विस्पष्टार्थम्** — the "
             "त appended to the ई is there only to make the reading "
             "plain, and takes nothing out that would otherwise be in"),
    SenseRule("4.2.124", sense="śeṣa", gives="vuñ", desa=True,
         of_samjna="janapada-vṛddha", excepts=("4.2.114",),
         why="जनपदतदवध्योश्च, the जनपद half; छस्यापवादः. "
             "आभिसारकः, आदर्शकः"),
    SenseRule("4.2.124", sense="śeṣa", gives="vuñ", desa=True,
         of_samjna="janapada-avadhi-vṛddha", excepts=("4.2.137",),
         why="जनपदतदवध्योश्च, the तदवधि half — a district's "
             "BOUNDARY. औपुष्टकः, श्यामायनकः. **तदवधिरपि जनपद एव "
             "गृह्यते न ग्रामः**: what the boundary bounds is a "
             "district and not a village.\n\n"
             "किमर्थं तर्हि अवधिग्रहणम्? **बाधकबाधनार्थम्** — the "
             "boundary is named to beat what would have beaten this "
             "rule. गर्तोत्तरपदाच्छं बाधित्वा वुञेव जनपदावधेर्भवति: "
             "4.2.137 would have given छ to त्रिगर्त, and this rule "
             "names the boundary so that त्रैगर्तकः stands instead"),
    SenseRule("4.2.125", sense="śeṣa", gives="vuñ", desa=True,
         of_samjna="janapada-bahuvacana",
         why="अवृद्धादपि बहुवचनविषयात्, जनपदतदवध्योरित्येव; "
             "अण्छयोरपवादः. अङ्गाः — आङ्गकः; वङ्गाः — वाङ्गकः; "
             "कलिङ्गाः — कालिङ्गकः. And from वृद्ध districts too: "
             "दार्वाः — दार्वकः; जाम्ब्वाः — जाम्ब्वकः.\n\n"
             "**विषयग्रहणमनन्यत्रभावार्थम्** — the word *domain* is "
             "there so the rule holds only where the plural is the "
             "word's own: जनपदैकशेषबहुत्वे मा भूत्, not where the "
             "plural comes from 1.2.64's एकशेष. वर्तन्यः — वार्तनः",
         keeps_out="वार्तनः"),
    SenseRule("4.2.125", sense="śeṣa", gives="vuñ", desa=True,
         of_samjna="janapada-avadhi-bahuvacana",
         why="अवृद्धादपि बहुवचनविषयात्, the boundary half. "
             "अजमीढाः — आजमीढकः; अजक्रन्दाः — आजक्रन्दकः; and from "
             "वृद्ध boundaries कालञ्जराः — कालञ्जरकः, वैकुलिशाः — "
             "वैकुलिशकः.\n\n"
             "**अपिग्रहणं किम्, यावता वृद्धात् पूर्वेणैव सिद्धम्?** "
             "If 4.2.124 already gave वुञ् from a वृद्ध district, "
             "why say *also*? **तक्रकौण्डिन्यन्यायेन बाधा मा "
             "विज्ञायीति समुच्चीयते** — so that no one reads this "
             "rule as REPLACING the last one. The maxim of "
             "*buttermilk to Kauṇḍinya*: telling the servants to "
             "give buttermilk to Kauṇḍinya does not cancel the milk "
             "everyone else was already getting. च here gathers "
             "rather than displaces"),
    SenseRule("4.2.126", sense="śeṣa", gives="vuñ", desa=True,
         excepts=("4.2.114", "4.2.132"),
         ends_with=("kaccha", "agni", "vaktra", "vartta"),
         why="कच्छाग्निवक्त्रवर्त्तोत्तरपदात्, छाणोरपवादः. "
             "**उत्तरपदशब्दः प्रत्येकमभिसंबध्यते** — *last member* "
             "attaches to each of the four. दारुकच्छकः, "
             "पैप्पलीकच्छकः; काण्डाग्नकः, वैभुजाग्नकः; "
             "ऐन्द्रवक्त्रकः, सैन्धुवक्त्रकः; बाहुगर्त्तकः, "
             "चाक्रगर्त्तकः.\n\n"
             "वृद्ध does not carry: the rule takes **चावृद्धाद् "
             "वृद्धात् च**, from a base with the first vowel "
             "lengthened and from one without"),
    SenseRule("4.2.127", sense="śeṣa", gives="vuñ", desa=True,
         gana="dhūmādi",
         why="धूमादिभ्यश्च, अणादेरपवादः. धौमकः, खाण्डकः.\n\n"
             "**AND THREE MEMBERS OF THE LIST ARE THERE FOR "
             "SOMETHING ELSE.** पाथेय has य for its penultimate and "
             "4.2.121 would have given वुञ् already, so "
             "**सामर्थ्याददेशार्थं ग्रहणम्** — it is read here to "
             "make the word a COUNTRY-word, which 4.2.121 needs it "
             "to be. विदेह and आनर्त likewise: the district-rule "
             "gave वुञ् already, and **अदेशार्थः पाठः**, they are "
             "read for the sense that is not a country — विदेहानां "
             "क्षत्रियाणां स्वं वैदेहकम्, आनर्तकम्.\n\n"
             "समुद्र is read for a narrower thing still: "
             "**तस्य नावि मनुष्ये च वुञिष्यते**. सामुद्रिका नौः, "
             "सामुद्रको मनुष्यः — but सामुद्रं जलम्, the water of "
             "the sea takes the default",
         keeps_out="सामुद्रं जलम्"),
    SenseRule("4.2.128", sense="śeṣa", gives="vuñ", of=("nagara",),
         result="kutsana-prāvīṇya",
         why="नगरात् कुत्सनप्रावीण्ययोः. कुत्सनं निन्दनम्, "
             "प्रावीण्यं नैपुण्यम् — blame and skill.\n\n"
             "**प्रत्ययार्थविशेषणं चैतत्** — the two qualify the "
             "SENSE OF THE AFFIX and not the base: born-in-a-city "
             "where blame or skill is meant. The vṛtti puts a verse "
             "on each side. केनायं मुषितः पन्था "
             "गात्रे पक्ष्मालिधूसरः — who robbed this traveller? "
             "इह नगरे मनुष्येण संभाव्यत एतन्नागरकेण, **चोरा हि "
             "नागरका भवन्ति**. And केनेदं लिखितं चित्रं "
             "मनोनेत्रविकाशि यत् — who painted this? "
             "**प्रवीणा हि नागरका भवन्ति**. Same affix, opposite "
             "compliment.\n\n"
             "कुत्सनप्रावीण्ययोरिति किम्? नागरा ब्राह्मणाः",
         keeps_out="नागरा ब्राह्मणाः"),
    SenseRule("4.2.129", sense="śeṣa", gives="vuñ", of=("araṇya",),
         result="manuṣya",
         why="अरण्यान्मनुष्ये, औपसंख्यानिकस्य णस्यापवादः. "
             "आरण्यको मनुष्यः — a man of the forest.\n\n"
             "A vārttika widens it to six things: "
             "**पथ्यध्यायन्यायविहारमनुष्यहस्तिष्विति वक्तव्यम्** — "
             "आरण्यकः पन्थाः, आरण्यकोऽध्यायः, आरण्यको न्यायः, "
             "आरण्यको विहारः, आरण्यको हस्ती. A forest ROAD, a "
             "forest LESSON, a forest RULE, a forest pleasure-ground, "
             "a forest elephant — and the आरण्यक books of the Veda "
             "are the second of those.\n\n"
             "**वा गोमयेषु** — and optionally of cow-dung: आरण्याः, "
             "आरण्यका गोमयाः. एतेष्विति किम्? आरण्याः पशवः",
         keeps_out="आरण्याः पशवः"),
    SenseRule("4.2.130", sense="śeṣa", gives="vuñ", optional=True,
         of=("kuru", "yugandhara"), excepts=("4.2.125",),
         why="विभाषा कुरुयुगन्धराभ्याम्. कौरवकः beside कौरवः; "
             "यौगन्धरकः beside यौगन्धरः.\n\n"
             "**जनपदशब्दावेतौ** — both are district-words, so "
             "4.2.125 would have given वुञ् without an option; the "
             "option is spoken against that. And कुरु is in the "
             "कच्छादि list of 4.2.133 as well, **तत्र वचनादणपि "
             "भविष्यति**, so अण् comes by that rule anyway — which "
             "leaves the option doing work for युगन्धर alone: "
             "**सैषा युगन्धरार्था विभाषा**.\n\n"
             "4.2.134 is not touched: from कुरु the वुञ् is fixed "
             "when a man is meant. कौरवको मनुष्यः, कौरवकमस्य हसितम्"),
    SenseRule("4.2.131", sense="śeṣa", gives="kan", of=("madra", "vṛji"),
         excepts=("4.2.125",),
         why="मद्रवृज्योः कन्, जनपदवुञोऽपवादः. मद्रेषु जातो मद्रकः; "
             "वृजिकः. कन् rather than वुञ्, and the difference "
             "shows only in the accent and in what 7.3.44 can reach"),
    SenseRule("4.2.132", sense="śeṣa", gives="aṇ", desa=True, upadha="k",
         excepts=("4.2.124", "4.2.125"),
         why="कोपधादण्, जनपदवुञोऽपवादः. ऋषिकेषु जातः — आर्षिकः; "
             "माहिषिकः.\n\n"
             "**अन्यत्र जनपदं मुक्त्वा पूर्वेणैव कोपधादणि सिद्धम्** "
             "— outside the districts 4.2.110 gave अण् from a "
             "क-penultimate base already, so this rule exists for "
             "the districts alone. And **अण्ग्रहणमुवर्णान्तादपि "
             "यथा स्यात्**: the affix is named so that it beats "
             "4.2.119's ठञ् on a उ-final base too — इक्ष्वाकुषु "
             "जात ऐक्ष्वाकः, where both conditions are met at once"),
    SenseRule("4.2.133", sense="śeṣa", gives="aṇ", desa=True,
         gana="kacchādi", excepts=("4.2.121", "4.2.126"),
         why="कच्छादिभ्यश्च, वुञादेरपवादः. काच्छः, सैन्धवः, "
             "वार्णवः.\n\n"
             "**कच्छशब्दो न बहुवचनविषयः** — कच्छ is not a "
             "plural-domain word, so 4.2.125 never reached it; "
             "**तस्य मनुष्यतत्स्थयोर्वुञर्थः पाठः**, it is in this "
             "list for the sake of the next rule. विजापक has क for "
             "its penultimate and 4.2.132 gave अण् already: "
             "**इह ग्रहणमुत्तरार्थम्**, read here for what follows"),
    SenseRule("4.2.134", sense="śeṣa", gives="vuñ", gana="kacchādi",
         result="manuṣya-tatstha", excepts=("4.2.133",),
         why="मनुष्यतत्स्थयोर्वुञ्, अणोऽपवादः. काच्छको मनुष्यः; "
             "काच्छकमस्य हसितम्, जल्पितम्; काच्छिका चूडा. "
             "सैन्धवको मनुष्यः, सैन्धविका चूडा.\n\n"
             "तत्स्थ is **what stands in the man** — his laughter, "
             "his talk, the lock of hair on his head. "
             "मनुष्यतत्स्थयोरिति किम्? काच्छो गौः, सैन्धवः, वार्णवः: "
             "the ox of Kaccha keeps the अण्",
         keeps_out="काच्छो गौः"),
    SenseRule("4.2.135", sense="śeṣa", gives="vuñ", of=("sālva",),
         result="apadāti-manuṣya-tatstha",
         why="अपदातौ साल्वात्. साल्व is in the कच्छादि list, "
             "**ततः पूर्वेणैव मनुष्यतत्स्थयोर्वुञि सिद्धे "
             "नियमार्थं वचनम्** — 4.2.134 gave the वुञ् already, so "
             "this rule is spoken to RESTRICT it: from साल्व the "
             "वुञ् comes for a man who is not a FOOT-SOLDIER. "
             "साल्वको मनुष्यः, साल्वकमस्य हसितम्. अपदाताविति किम्? "
             "साल्वः पदातिर्व्रजति",
         keeps_out="साल्वः पदातिः"),
    SenseRule("4.2.136", sense="śeṣa", gives="vuñ", of=("sālva",),
         result="go-yavāgū", excepts=("4.2.133",),
         why="गोयवाग्वोश्च, कच्छाद्यणोऽपवादः. साल्वको गौः; "
             "साल्विका यवागूः — the ox of Sālva and the gruel of "
             "Sālva. **साल्वमन्यत्**: everything else keeps the अण्, "
             "and 4.2.134 could not have given these two, because "
             "neither an ox nor a gruel stands in a man",
         keeps_out="साल्वम्"),
    SenseRule("4.2.137", sense="śeṣa", gives="cha", desa=True,
         ends_with=("garta",), excepts=("4.2.114", "4.2.117"),
         why="गर्तोत्तरपदाच्छः, अणोऽपवादः. वृकगर्तीयम्, "
             "शृगालगर्तीयम्, श्वाविद्गर्तीयम्. And "
             "**वाहीकग्रामलक्षणं च प्रत्ययं परत्वाद् बाधते** — it "
             "beats 4.2.117 by standing later.\n\n"
             "**उत्तरपदग्रहणं बहुच्पूर्वनिरासार्थम्** — the word "
             "*last member* is there to keep out a गर्त preceded by "
             "बहुच्, which is a prefix and not a first member at "
             "all. बाहुगर्तम्.\n\n"
             "4.2.124 beats this rule the other way for a district's "
             "boundary, and names the boundary in order to do it",
         keeps_out="बाहुगर्तम्"),
    SenseRule("4.2.138", sense="śeṣa", gives="cha", gana="gahādi",
         why="गहादिभ्यश्च, अणादेरपवादः. गहीयः, अन्तःस्थीयः.\n\n"
             "**देशाधिकारेऽपि संभवापेक्षं विशेषणम्, न सर्वेषाम्** — "
             "the country-heading is over this rule too, but it "
             "qualifies only the members that COULD be countries. "
             "अङ्ग and वङ्ग and मगध are in the list; so are "
             "पूर्वपक्ष and उत्तमशाख, which are not places.\n\n"
             "Four गणसूत्र ride with the list. मध्य मध्यमं चाण् "
             "चरणे: मध्य becomes मध्यम when the affix comes — "
             "मध्यमीयाः — but in the sense of a school it takes अण्, "
             "माध्यमाः. मुखपार्श्वतसोर्लोपः drops the तस् — "
             "मुखतीयम्, पार्श्वतीयम्. जनपरयोः कुक् च inserts क — "
             "जनकीयम्, परकीयम्, and देवस्य च adds देवकीयम्. "
             "वेणुकादिभ्यश्छण् gives छण् — वैणुकीयम्, वैत्रकीयम्. "
             "**आकृतिगणोऽयम्**, and the list is open"),
    SenseRule("4.2.139", sense="śeṣa", gives="cha", desa=True,
         gana="kaṭādi", of_samjna="prāc",
         why="प्राचां कटादेः, अणोऽपवादः. कटनगरीयम्, कटघोषीयम्, "
             "कटपल्वलीयम् — the कट-towns of the east"),
    SenseRule("4.2.140", sense="śeṣa", of=("rājan",), of_samjna="vṛddha",
         affix_from="4.2.114", along_with="क for the final of राजन्",
         why="राज्ञः क च. राजकीयम्.\n\n"
             "**AND THE RULE GIVES NO AFFIX AT ALL.** आदेशमात्रमिह "
             "विधेयम्, **प्रत्ययस्तु वृद्धाच्छ इत्येव सिद्धः** — "
             "only the substitute is enjoined here; the छ was "
             "already 4.2.114's, since राजन् has आ for its first "
             "vowel and is वृद्ध by 1.1.73. The च gathers this rule "
             "onto that one instead of replacing it, and the code "
             "says so by fetching 4.2.114's own answer rather than "
             "naming छ a second time.\n\n"
             "**असंभवाद् देशाधिकारो न विशेषणम्** — the country-"
             "heading cannot qualify this base, because a king is "
             "not a place"),
    SenseRule("4.2.141", sense="śeṣa", gives="cha", desa=True,
         of_samjna="vṛddha", ends_with=("aka", "ika"),
         excepts=("4.2.132", "4.2.117", "4.2.123"),
         why="वृद्धादकेकान्तखोपधात्, the अकान्त and इकान्त halves. "
             "आरीहणकीयम्, द्रौघणकीयम्; आश्वपथिकीयम्, शाल्मलिकीयम्. "
             "It beats three rules at once — the कोपध अण् of "
             "4.2.132, the वाहीकग्राम affix of 4.2.117, and "
             "रोपधेतोः प्राचाम्"),
    SenseRule("4.2.141", sense="śeṣa", gives="cha", desa=True,
         of_samjna="vṛddha", upadha="kha", excepts=("4.2.132",),
         why="वृद्धादकेकान्तखोपधात्, the खोपध half. कौटिशिखीयम्, "
             "आयोमुखीयम्.\n\n"
             "**अकेकान्तग्रहणे कोपधग्रहणं सौसुकाद्यर्थम्** — a "
             "vārttika reads क for the penultimate BESIDE the two "
             "endings, for words like सौसुक that have neither: "
             "सौसुकीयम्, मौसुकीयम्, ऐन्द्रवेणुकीयम्"),
    SenseRule("4.2.142", sense="śeṣa", gives="cha", desa=True,
         of_samjna="vṛddha", excepts=("4.2.117",),
         ends_with=("kanthā", "palada", "nagara", "grāma", "hrada"),
         why="कन्थापलदनगरग्रामह्रदोत्तरपदात्, "
             "वाहीकग्रामादिलक्षणस्य प्रत्ययस्यापवादः. दाक्षिकन्थीयम्, "
             "माहिकिकन्थीयम्; दाक्षिपलदीयम्; दाक्षिनगरीयम्; "
             "दाक्षिग्रामीयम्; दाक्षिह्रदीयम् — five last members, "
             "each with the same two first members to show that the "
             "ending is what the rule is about"),
    SenseRule("4.2.143", sense="śeṣa", gives="cha", of=("parvata",),
         excepts=("4.1.83",),
         why="पर्वताच्च, अणोऽपवादः. पर्वतीयो राजा, पर्वतीयः पुरुषः "
             "— the king of the mountain and the man of the mountain"),
    SenseRule("4.2.144", sense="śeṣa", gives="cha", of=("parvata",),
         result="amanuṣya", optional=True,
         why="विभाषाऽमनुष्ये. **पूर्वेण नित्ये प्राप्ते विकल्प "
             "उच्यते** — the last rule gave छ without an option, so "
             "the option is spoken here: पर्वतीयानि फलानि beside "
             "पार्वतानि फलानि; पर्वतीयमुदकम् beside पार्वतमुदकम्. "
             "अमनुष्य इति किम्? पर्वतीयो मनुष्यः, where the छ is "
             "fixed again",
         keeps_out="पर्वतीयो मनुष्यः"),
    SenseRule("4.2.145", sense="śeṣa", gives="cha", desa=True,
         of=("kṛkaṇa", "parṇa"), of_samjna="bhāradvāja-deśa",
         why="कृकणपर्णाद्भारद्वाजे. कृकणीयम्, पर्णीयम्. "
             "**भारद्वाजशब्दोऽपि देशवचन एव, न गोत्रशब्दः** — "
             "भारद्वाज here is the COUNTRY and not the lineage, "
             "though the same word is a famous gotra; and "
             "**प्रकृतिविशेषणं चैतत्, न प्रत्ययार्थः**, it qualifies "
             "the base rather than being what the affix means. "
             "भारद्वाज इति किम्? कार्कणम्, पार्णम्.\n\n"
             "The pāda ends here: इति काशिकायां वृत्तौ "
             "चतुर्थाध्यायस्य द्वितीयः पादः",
         keeps_out="कार्कणम्, पार्णम्"),
)


@dataclass(frozen=True)
class InSense:
    """The affix given in a sense, and by which rule."""

    gives: str
    by: str
    why: str
    case: str = ""
    optional: bool = False
    elided: bool = False
    excepts: Tuple[str, ...] = ()
    #: A substitution or augment the same rule makes in one act.
    along_with: str = ""


def _reaches(row: SenseRule, stem: str, gana: str, case: str,
             sense: str, result: str, samjna: str,
             unspecified: bool, stem_final: str,
             dvyac: bool, pre: str, accent: str,
             marked: str, upadha: str, ends_with: str,
             desa: bool) -> bool:
    if row.of and stem not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.case and case and case != row.case:
        return False
    if row.sense and sense != row.sense:
        return False
    if row.result and result != row.result:
        return False
    if row.of_samjna and samjna != row.of_samjna:
        return False
    if row.unspecified and not unspecified:
        return False
    if row.stem_final and stem_final != row.stem_final:
        return False
    if row.dvyac and not dvyac:
        return False
    if row.pre and pre != row.pre:
        return False
    if row.accent and accent != row.accent:
        return False
    if row.marked and marked != row.marked:
        return False
    if row.upadha and upadha != row.upadha:
        return False
    if row.ends_with and ends_with not in row.ends_with:
        return False
    if row.desa and not desa:
        return False
    return True


def _how_specific(row: SenseRule) -> int:
    """
    A named base is the narrowest thing these rules state; a case
    alone the widest, since the case is carried by anuvṛtti and
    qualifies whole runs.
    """
    return (
        6 * bool(row.of)
        + 5 * bool(row.of_samjna)
        + 4 * bool(row.gana)
        + 3 * bool(row.result)
        + 2 * bool(row.sense)
        + 1 * bool(row.case)
        + 4 * bool(row.unspecified)
        + 2 * bool(row.stem_final)
        + 2 * bool(row.dvyac)
        + 4 * bool(row.pre)
        + 3 * bool(row.accent)
        + 3 * bool(row.marked)
        + 3 * bool(row.upadha)
        + 4 * bool(row.ends_with)
        + 1 * bool(row.desa)
    )


def in_sense(stem: str = "", *, gana: str = "", case: str = "",
             sense: str = "", result: str = "", samjna: str = "",
             unspecified: bool = False, stem_final: str = "",
             dvyac: bool = False, pre: str = "",
             accent: str = "", marked: str = "",
             upadha: str = "", ends_with: str = "",
             desa: bool = False, wants: str = "") -> object:
    """
    4.2.1–21 — the affix given in a sense, from a base in a case.

    `case` is the relation the base stands in — तृतीया, सप्तमी,
    प्रथमा — and `sense` what the affix means: रक्त, युक्त, दृष्ट,
    परिवृत, उद्धृत, संस्कृत. `result` is the further condition
    several rules state on WHAT the thing is: a time, a chant, a
    chariot, a food.

    Where no rule names an affix, 4.1.83's default answers — which is
    the whole point of the section, and why so many of these rules
    name a sense and nothing else.
    """
    matched = [
        row for row in SENSE_TABLE
        if _reaches(row, stem, gana, case, sense, result, samjna,
                    unspecified, stem_final, dvyac, pre, accent,
                    marked, upadha, ends_with, desa)
        and (not wants or row.gives == wants)
    ]
    if not matched:
        from src.astadhyayi.taddhita import default_affix

        fallen = default_affix()
        return InSense(fallen.gives, fallen.by, fallen.why, case=case)
    row = max(matched, key=_how_specific)
    if row.refuses:
        # A प्रतिषेध does not govern what it excepts. 4.2.113 refuses
        # what 4.2.112 gives, so the answer comes back by that rule.
        supplying = [other for other in matched
                     if not other.refuses and other.gives == row.gives]
        if supplying:
            beaten = max(supplying, key=_how_specific)
            return InSense("", beaten.sutra, row.why, case=row.case,
                           excepts=(row.sutra,))
        return InSense("", row.sutra, row.why, case=row.case)
    if row.elides:
        return InSense("", row.sutra, row.why, case=row.case,
                       elided=True, optional=row.optional)
    if not row.gives:
        if row.borrows_from:
            # An अतिदेश takes over what another stretch of the
            # grammar gives, so the answer is fetched from there and
            # not named here. वत्करणं सर्वसादृश्यपरिग्रहार्थम्.
            from src.astadhyayi.kala_taddhita import born_in

            borrowed = born_in(stem, gana=gana, sense="śeṣa",
                               samjna=samjna, wants=wants)
            return InSense(
                borrowed.gives, row.sutra,
                row.why + "\n\nThe affix is borrowed from %s: %s"
                % (borrowed.by, borrowed.why),
                case=row.case, optional=row.optional)
        if row.affix_from:
            # The rule enjoins a SUBSTITUTE and no affix, and names
            # the rule whose affix it leaves standing. Fetching that
            # rule's own answer is how the code says what the vṛtti
            # says: आदेशमात्रमिह विधेयम्.
            standing = provisions_for(row.affix_from)[0]
            return InSense(
                standing.gives, row.sutra,
                row.why + "\n\nThe affix is %s's, left standing: %s"
                % (row.affix_from, standing.why),
                case=row.case, optional=row.optional,
                along_with=row.along_with)
        from src.astadhyayi.taddhita import default_affix

        fallen = default_affix()
        return InSense(
            fallen.gives, row.sutra,
            row.why + "\n\nThe affix is 4.1.83's default: " + fallen.why,
            case=row.case, optional=row.optional)
    return InSense(row.gives, row.sutra, row.why, case=row.case,
                   optional=row.optional, excepts=row.excepts,
                   along_with=row.along_with)


def sense_run(sense: str = "devatā") -> object:
    """
    How far a SENSE is carried, as the vṛtti of the rule that opens
    it says. सास्य देवता runs to 4.2.35 — महाराजप्रोष्ठपदाट् ठञ् इति
    यावत् — and तस्य समूहः to 4.2.51, इनित्रकट्यचश्च इति यावत्.

    Two more ranges with both ends stated, beside the two case-runs.
    **Four in one pāda**, where most anuvṛtti in this project has had
    to be inferred from where a rule stops making sense.
    """
    for named, opens, closes in SENSE_RUNS:
        if named == sense:
            return InSense(
                "", opens,
                "the sense %s runs from %s to %s, and the vṛtti of "
                "the opening rule names the closing one"
                % (named, opens, closes),
                case=named)
    return InSense(
        "", "4.2.24",
        "%s is not one of the senses whose range this pāda states. "
        "It states two: देवता from 4.2.24 to 4.2.35, and समूह from "
        "4.2.37 to 4.2.51" % (sense or "that"))


def case_run(case: str = "tṛtīyā") -> object:
    """
    How far a case-relation is carried, as the vṛtti of the rule that
    opens it says.

    4.2.1's: द्वैपवैयाघ्रादञ् इति यावत् तृतीयासमर्थविभक्तिर्
    अनुवर्तते. 4.2.14's: क्षीराड् ढञ् इति यावत्.

    **Both ends are stated, so both can be checked** — which is not
    true of most anuvṛtti. This project has recorded ranges read off a
    name before (3.3.141's मर्यादायामयमाङ्, 4.1.83's प्राग् दीव्यतः),
    and this is the first place where two of them sit side by side and
    divide one pāda between them.
    """
    for named, opens, closes in CASE_RUNS:
        if named == case:
            return InSense(
                "", opens,
                "%s runs from %s to %s, and the vṛtti of the opening "
                "rule names the closing one: %s"
                % (named, opens, closes,
                   "द्वैपवैयाघ्रादञ् इति यावत् "
                   "तृतीयासमर्थविभक्तिरनुवर्तते"
                   if named == "tṛtīyā" else
                   "तत्रेति सप्तमी समर्थविभक्तिः क्षीराड् ढञ् इति "
                   "यावदनुवर्तते"),
                case=named)
    return InSense(
        "", "4.2.1",
        "%s is not one of the case-relations this run carries. It "
        "carries two, and each names where it stops: तृतीया from "
        "4.2.1 to 4.2.12, सप्तमी from 4.2.14 to 4.2.20" % (case or "that"))


def desa_run() -> object:
    """
    How far देश carries, as the vṛttis themselves say. It enters at
    4.2.119 ओर्देशे — the first rule of this pāda to name a COUNTRY —
    and twelve later vṛttis open with **देश इत्येव**, the last of
    them on 4.2.145, the closing rule of the pāda.

    The seventh stated range in this pāda, after two case-runs and
    four sense-runs. Seven is more than the whole of अध्याय ३
    offered.
    """
    opens, closes = DESA_RUN
    return InSense(
        "", opens,
        "देश carries from %s to %s. ओर्देशे names it, and the vṛtti "
        "of every rule that keeps it opens **देश इत्येव** — twelve "
        "times, the last of them on %s" % (opens, closes, closes))


def provisions_for(sutra_id: str) -> Tuple[SenseRule, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in SENSE_TABLE if row.sutra == sutra_id)
