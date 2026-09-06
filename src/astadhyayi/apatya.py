# -*- coding: utf-8 -*-
"""
४.१.९२–११२ — *his descendant*, and the twenty rules that answer it.

4.1.92 तस्यापत्यम् is three syllables and names no affix. It can be
that short because 4.1.82 has said which word the affix attaches to
and 4.1.83 has said which affix comes when nothing else is said, so
this rule has only to supply a SENSE — अर्थनिर्देशोऽयम्.

**And it faces both ways.** पूर्वैरुत्तरैश्च प्रत्ययैरभिसंबध्यते —
it is connected with the affixes BEFORE it as well as those after,
which is why 4.1.85's दैत्यः and 4.1.86's औत्सः are patronymics
though their rules were stated six sūtras earlier. A heading that
reaches backward as well as forward, where every heading met so far
ran one way only.

Then two rules of RESTRICTION rather than provision — 4.1.93 एको
गोत्रे and 4.1.94 गोत्राद् यून्यस्त्रियाम् — settle how many affixes
a lineage may take and what the young-descendant affix is added to.
Only after that do the affixes come: इञ्, च्फञ्, फक्, अञ्, यञ्, फञ्,
अण्, each on its own list.

**What the lists are for changes at 4.1.112.** Until there they carve
exceptions out of one another; at 4.1.112 गोत्र इति निवृत्तम्, and
one word — गङ्गा — is put in THREE lists at once so that three
affixes may all apply: गाङ्गः, गाङ्गायनिः, गाङ्गेयः. A gaṇa used for
CO-APPLICATION rather than for exception, and the first of its kind
in this project.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: 4.1.92's three readings of what an अपत्य is, in the order the
#: vṛtti gives them. अपतनादपत्यम् — that which does not fall away.
APATYA_KINDS: Tuple[str, ...] = ("anantara", "gotra", "yuvan")


@dataclass(frozen=True)
class Apatya:
    """One rule about which affix names a descendant."""

    sutra: str
    gives: str = ""
    #: Particular stems the rule names.
    of: Tuple[str, ...] = ()
    #: A गण it cites by its first member.
    gana: str = ""
    #: What the stem ends in — 4.1.95's अकारान्त.
    stem_final: str = ""
    #: The affix the stem already carries: यञ्, इञ्, अञ्.
    marked: str = ""
    #: Which kind of descendant: गोत्र, युवन्, or the immediate one.
    kind: str = ""
    #: A further condition on WHO the descendant is — भार्गव,
    #: ब्राह्मण, कौशिक, आङ्गिरस, त्रैगर्त. Several rules of this run
    #: turn on a lineage the grammar does not otherwise mention.
    among: str = ""
    optional: bool = False
    #: A substitution the same rule makes: 4.1.97's अकङ्.
    along_with: str = ""
    #: What stands in front: a numeral, सम्, भद्र — 4.1.115's three.
    pre: str = ""
    #: An affix the stem must NOT carry. 4.1.122 wants इकारान्त but
    #: अनिञन्त, which is a condition stated against another rule's
    #: output rather than against anything in the word.
    not_marked: str = ""
    #: Two vowels. 4.1.121 and 4.1.122 both state it, and it is the
    #: only condition of sheer length in the run.
    dvyac: bool = False
    #: Whether the stem ends in one of the feminine affixes. 4.1.120's
    #: स्त्री names the AFFIX and not the sense —
    #: स्त्रीप्रत्ययविज्ञापनाद् असत्यर्थग्रहणे — which is why इडबिड
    #: and दरद are outside it.
    stri_pratyaya: bool = False
    #: A class the grammar or the vṛtti names rather than lists:
    #: 4.1.113's अवृद्ध-नदी-मानुषी, 4.1.131's क्षुद्रा, 4.1.135's
    #: चतुष्पाद्. Three of them are properties of what the base
    #: MEANS — अर्थधर्म in 4.1.113's own words — and not of its shape.
    of_samjna: str = ""
    #: The attitude the rule requires. कुत्सन, contempt, conditions
    #: 4.1.147 to 4.1.149; पूजा, respect, conditions 4.1.166. Two of
    #: the strangest conditions in the grammar, and both are stated.
    attitude: str = ""
    #: Whether the base names a country whose people are kṣatriyas —
    #: 4.1.168's जनपदशब्दात् क्षत्रियात्, the ground of the whole
    #: तद्राज section.
    janapada: bool = False
    #: A named आचार्य. 4.1.130 cites the northern teachers.
    authority: str = ""
    #: Rules the vṛtti says this one excepts.
    excepts: Tuple[str, ...] = ()
    #: The form the rule's own words leave standing — what the vṛtti
    #: gives after इति किम्. A rule stated of one family does not
    #: refuse the others; it simply does not reach them.
    keeps_out: str = ""
    why: str = ""


APATYA: Tuple[Apatya, ...] = (
    Apatya("4.1.95", "iñ", stem_final="a", excepts=("4.1.83",),
           why="अत इञ्, अणोऽपवादः. From any stem in short अ: "
               "दक्षस्यापत्यं दाक्षिः. तपरकरणं किम्? शुभंयाः, "
               "कीलालपा इत्यतो मा भूत् — the त holds it to the "
               "short vowel, the same job it did at 4.1.4.\n\n"
               "कथं प्रदीयतां दाशरथाय मैथिली (वा०रा० युद्ध० ९.२२)? "
               "शेषविवक्षया भविष्यति — that form comes by the "
               "residual sense and not by this rule, which is how "
               "the vṛtti keeps a famous line inside the grammar"),
    Apatya("4.1.96", "iñ", gana="bāhvādi",
           why="बाह्वादिभ्यश्च. बाहविः, औपबाहविः. अनकारार्थ "
               "आरम्भः — begun for stems NOT in अ, which the rule "
               "before could not reach, and क्वचिद् बाधकबाधनार्थः, "
               "in places to beat what would have beaten it.\n\n"
               "चकारोऽनुक्तसमुच्चयार्थ आकृतिगणतामस्य बोधयति — the "
               "च makes it an आकृतिगण, a list recognised by shape "
               "rather than closed: जाम्बिः, ऐन्द्रशर्मिः, "
               "आजधेनविः. The second such list in the pāda, after "
               "4.1.56's क्रोडादि.\n\n"
               "And two vārttikas narrow it by USE rather than by "
               "form: बाह्वादिप्रभृतिषु येषां दर्शनं गोत्रभावे "
               "लौकिके ततोऽन्यत्र तेषां प्रतिषेधः — a member seen "
               "in ordinary speech as a lineage-name is refused "
               "elsewhere, बाहुर्नाम कश्चित्, तस्यापत्यं बाहवः"),
    Apatya("4.1.97", "iñ", of=("sudhātṛ",), along_with="akaṅ",
           why="सुधातुरकङ् च. सुधातुरपत्यं सौधातकिः — the affix and "
               "a substitution in the stem, तत्सन्नियोगेन, in one "
               "act. The same shape as 4.1.7's र and 3.4.84's आह्.\n\n"
               "व्यासवरुडनिषादचण्डालबिम्बानामिति वक्तव्यम् extends "
               "the substitution to five more: वैयासकिः, वारुडकिः, "
               "नैषादकिः, चाण्डालकिः, बैम्बकिः"),
    Apatya("4.1.98", "cphañ", gana="kuñjādi", kind="gotra",
           excepts=("4.1.95",),
           why="कुञ्जादिभ्यश्च्फञ्, इञोऽपवादः. कौञ्जायन्यः, "
               "ब्राध्नायन्यः. ञकारो वृद्ध्यर्थः, and चकारो "
               "विशेषणार्थः — the च is there for 5.3.113 to pick "
               "this affix out by, five sūtras' worth of chapters "
               "away.\n\n"
               "गोत्र इति किम्? कुञ्जस्यापत्यमनन्तरं कौञ्जिः — the "
               "immediate descendant takes the other affix.\n\n"
               "AND THE ACCENT CHANGES WITH THE NUMBER. "
               "एकवचनद्विवचनयोः सतिशिष्टत्वाद् ञित्स्वरेणैव "
               "भवितव्यम्; बहुवचने तु कौञ्जायना इति परमपि "
               "ञित्स्वरं त्यक्त्वा चित्स्वर एवेष्यते — singular "
               "and dual take one accent and the plural another, "
               "though the affix is the same. गोत्राधिकारश्च "
               "शिवादिभ्योऽण् इति यावत्"),
    Apatya("4.1.99", "phak", gana="naḍādi", kind="gotra",
           why="नडादिभ्यः फक्. नाडायनः, चारायणः. गोत्र इत्येव — "
               "नाडिः.\n\n"
               "One member is in two lists and the vṛtti works out "
               "what that means: शालङ्किः पिता, शालङ्किः पुत्रः — "
               "गोत्रविशेषे कौशिके फकं स्मरन्ति, इञेवान्यत्र; "
               "अथवा पैलादिपाठ एव ज्ञापक इञो भावस्य. A membership "
               "in one gaṇa read as teaching what happens in "
               "another"),
    Apatya("4.1.100", "phak", gana="haritādi", marked="añ",
           kind="yuvan",
           excepts=("4.1.95",),
           why="हरितादिभ्योऽञः, इञोऽपवादः. हारितायनः, "
               "कैन्दासायनः.\n\n"
               "**A HEADING PRESENT AND OVERRIDDEN BY CAPACITY.** "
               "ननु च गोत्र इति वर्तते, न च गोत्रादपरो "
               "गोत्रप्रत्ययो भवति, एको गोत्रे इति वचनात्? "
               "सत्यमेतत् — 4.1.93 allows a lineage only ONE affix, "
               "and here a second would come. इह तु "
               "गोत्राधिकारेऽपि **सामर्थ्याद् यूनि प्रत्ययो "
               "विज्ञायते**: the heading says गोत्र and the rule "
               "is read as being about the YOUNG descendant "
               "instead, because it could not otherwise do "
               "anything. गोत्राधिकारस्तूत्तरार्थः, the heading is "
               "carried for the rules after"),
    Apatya("4.1.101", "phak", marked="yañ", kind="yuvan",
           why="यञिञोश्च. गार्ग्यायणः, वात्स्यायनः; and from इञ् — "
               "दाक्षायणः, प्लाक्षायणः.\n\n"
               "गोत्रग्रहणेन यञिञौ विशेष्येते, तदन्तात् तु "
               "यून्येवायं प्रत्ययः, गोत्राद् यूनीति वचनात् — the "
               "heading qualifies the two AFFIXES named, and what "
               "the rule gives is the young-descendant affix, by "
               "4.1.94. So a word carried down qualifies the "
               "condition and a rule seven sūtras back supplies the "
               "sense. द्वीपादनुसमुद्रं यञ् and सुतङ्गमादिभ्य इञ् "
               "are kept out, being neither patronymic"),
    Apatya("4.1.101", "phak", marked="iñ", kind="yuvan",
           why="यञिञोश्च — and from an इञ्-final stem: दाक्षायणः, "
               "प्लाक्षायणः"),
    Apatya("4.1.102", "phak", of=("śaradvat",), among="bhārgava",
           kind="gotra", excepts=("4.1.104",),
           why="शरद्वच्छुनकदर्भाद् भृगुवत्साग्रायणेषु, "
               "यथासंख्यम् — THREE WORDS AND THREE LINEAGES, and "
               "each word takes the affix only inside its own: "
               "शारद्वतायनो भवति भार्गवश्चेत्, शारद्वतोऽन्यः. "
               "**A condition that is not about the word at all but "
               "about whose family is meant**"),
    Apatya("4.1.102", "phak", of=("śunaka",), among="vātsya",
           kind="gotra", excepts=("4.1.104",),
           why="शरद्वच्छुनकदर्भाद् भृगुवत्साग्रायणेषु — शौनकायनो "
               "भवति वात्स्यश्चेत्, शौनकोऽन्यः"),
    Apatya("4.1.102", "phak", of=("darbha",), among="āgrāyaṇa",
           kind="gotra",
           why="शरद्वच्छुनकदर्भाद् भृगुवत्साग्रायणेषु — दार्भायणो "
               "भवत्याग्रायणश्चेत्, दार्भिरन्यः"),
    Apatya("4.1.103", "phak", gana="droṇādi", kind="gotra",
           optional=True, excepts=("4.1.95",),
           why="द्रोणपर्वतजीवन्तादन्यतरस्याम्, इञोऽपवादः. "
               "द्रौणायनः beside द्रौणिः, पार्वतायनः beside "
               "पार्वतिः, जैवन्तायनः beside जैवन्तिः.\n\n"
               "कथमनन्तरोऽश्वत्थामा द्रौणायन इत्युच्यते? "
               "नैवात्र महाभारतद्रोणो गृह्यते, किं तर्हि? अनादिः. "
               "**इदानीन्तनात् तु श्रुतिसामान्यादध्यारोपेण "
               "तथाभिधानं भवति** — a present-day man is called by a "
               "lineage-form through mere likeness of sound, "
               "transferred. The grammar declines to own the usage "
               "and explains it anyway"),
    Apatya("4.1.104", "añ", gana="bidādi", kind="gotra",
           why="अनृष्यानन्तर्ये बिदादिभ्योऽञ्. बैदः, और्वः.\n\n"
               "**A NEGATIVE COMPOUND READ ONE WAY BECAUSE THE "
               "OTHER WAY SPOILS A NAME.** अनृष्यानन्तर्य is read "
               "as *immediate descendant of a non-sage* — "
               "अनृषिभ्योऽनन्तरे भवतीति — and not as *not being the "
               "immediate descendant of a sage*. ये पुनरत्र "
               "अनृषिशब्दाः पुत्रादयः, तेभ्योऽनन्तरापत्य एव भवति: "
               "पौत्रः, दौहित्रः.\n\n"
               "The second reading would forbid the affix right "
               "after a sage, and then कौशिको विश्वामित्रः — "
               "Viśvāmitra called a Kauśika — would be wrong: "
               "ऋष्यपत्यनैरन्तर्यविषये प्रतिषेधे विज्ञायमाने "
               "कौशिको विश्वामित्र इति दुष्यति. **A grammatical "
               "reading settled by a proper name it would "
               "otherwise break**, and the vṛtti says अवश्यं "
               "चैतदेवं विज्ञेयम्, it MUST be read so"),
    Apatya("4.1.105", "yañ", gana="gargādi", kind="gotra",
           why="गर्गादिभ्यो यञ्. गार्ग्यः, वात्स्यः.\n\n"
               "कथमनन्तरो रामो जामदग्न्यः, व्यासः पाराशर्य इति? "
               "गोत्ररूपाध्यारोपेण भविष्यति — the same transfer "
               "4.1.103 used, and for the same reason: the forms "
               "are attested and the rule does not license them. "
               "अनन्तरापत्यविवक्षायां तु ऋष्यणैव भवितव्यं जामदग्नः, "
               "पाराशर इति — what the grammar WOULD give is stated "
               "beside what people say"),
    Apatya("4.1.106", "yañ", of=("madhu",), among="brāhmaṇa",
           kind="gotra",
           why="मधुबभ्र्वोर्ब्राह्मणकौशिकयोः, यथासंख्यम्. "
               "माधव्यो भवति ब्राह्मणश्चेत्, माधव एवान्यः"),
    Apatya("4.1.106", "yañ", of=("babhru",), among="kauśika",
           kind="gotra",
           why="मधुबभ्र्वोर्ब्राह्मणकौशिकयोः — बाभ्रव्यो भवति "
               "कौशिकश्चेत्, बाभ्रव एवान्यः.\n\n"
               "AND THE WORD IS ALREADY IN 4.1.105's LIST, WHICH IS "
               "WHY THIS RULE IS A RESTRICTION AND NOT A GIFT. "
               "बभ्रुशब्दो गर्गादिषु पठ्यते, ततः सिद्धे यञि कौशिके "
               "नियमार्थं वचनम् — the affix came already and this "
               "confines it. गर्गादिषु पाठोऽप्यन्तर्गणकार्यार्थः, "
               "and the membership still earns its keep: 4.1.18's "
               "सर्वत्र लोहितादिकतन्तेभ्यः reaches it, बाभ्रव्यायणी"),
    Apatya("4.1.107", "yañ", of=("kapi", "bodha"), among="āṅgirasa",
           kind="gotra",
           why="कपिबोधादाङ्गिरसे. काप्यः, बौध्यः. आङ्गिरस इति "
               "किम्? कापेयः, बौधिः. Again a restriction on a word "
               "already in गर्गादि — कपिशब्दो गर्गादिषु पठ्यते, "
               "तस्य नियमार्थं वचनम्, आङ्गिरसे यथा स्यात् — and "
               "again the membership keeps a second job: "
               "लोहितादिकार्यार्थश्च गणे पाठः, काप्यायनी"),
    Apatya("4.1.108", "yañ", of=("vataṇḍa",), among="āṅgirasa",
           kind="gotra",
           why="वतण्डाच्च. वातण्ड्यः. आङ्गिरस इति किम्? वातण्डः.\n\n"
               "**A WORD IN TWO LISTS, AND BOTH AFFIXES STAND WHERE "
               "THE RULE DOES NOT REACH.** किमर्थमिदं यावता "
               "गर्गादिष्वयं पठ्यते? शिवादिष्वप्ययं पठ्यते — it is "
               "in गर्गादि and in शिवादि both, so this rule is "
               "stated शिवाद्यणोऽपवादार्थम्, to except that other "
               "list within the Āṅgirasa lineage. And outside it, "
               "अनाङ्गिरसे तूभयत्र पाठसामर्थ्यात् प्रत्ययद्वयमपि "
               "भवति: वातण्ड्यः AND वातण्डः, both, on the strength "
               "of being in two lists"),
    Apatya("4.1.110", "phañ", gana="aśvādi", kind="gotra",
           why="अश्वादिभ्यः फञ्. आश्वायनः, आश्मायनः. "
               "ये त्वत्र प्रत्ययान्ताः पठ्यन्ते, तेभ्यः "
               "सामर्थ्याद् यूनि प्रत्ययो विज्ञायते — the members "
               "that already end in an affix are read as taking the "
               "YOUNG-descendant one, by capacity, which is 4.1.100's "
               "argument again ten sūtras later"),
    Apatya("4.1.111", "phañ", of=("bharga",), among="traigarta",
           kind="gotra",
           why="भर्गात्त्रैगर्ते. भार्गायणो भवति त्रैगर्तश्चेत्, "
               "भार्गिरन्यः. The fifth rule of this run to turn on "
               "WHOSE FAMILY is meant rather than on anything in the "
               "word"),
    Apatya("4.1.112", "aṇ", gana="śivādi",
           why="शिवादिभ्योऽण्, यथायथमिञादीनामपवादः. शैवः, "
               "प्रौष्ठः.\n\n"
               "**AND THE गोत्र SECTION ENDS HERE.** गोत्र इति "
               "निवृत्तम्, अतः प्रभृति सामान्येन प्रत्यया "
               "विज्ञायन्ते — from this rule on the affixes are "
               "understood generally, of a descendant of any degree. "
               "4.1.98's vṛtti had already named this rule as where "
               "the section would stop: गोत्राधिकारश्च "
               "शिवादिभ्योऽण् इति यावत्, said fourteen sūtras "
               "earlier.\n\n"
               "**A LIST USED FOR CO-APPLICATION RATHER THAN FOR "
               "EXCEPTION.** गङ्गाशब्दः पठ्यते तिकादिफिञा "
               "शुभ्रादिढका च समावेशार्थम्, तेन त्रैरूप्यं भवति — "
               "गङ्गा is in THREE lists at once so that three "
               "affixes may ALL apply: गाङ्गः, गाङ्गायनिः, "
               "गाङ्गेयः. Every gaṇa in this pāda so far carved "
               "exceptions; this one is a membership that adds. "
               "विपाश is there for the same reason — वैपाशः, "
               "वैपाशायन्यः — and तक्षन् for the opposite one, "
               "कारिलक्षणमुदीचामिञं बाधितुम्, though ण्य is left "
               "standing: ताक्ष्णः, ताक्षण्यः"),
    # --- ढक् and its kin, mostly from feminine stems ------------------
    Apatya("4.1.113", "aṇ", of_samjna="avṛddha-nadī-mānuṣī",
         excepts=("4.1.120",),
         why="अवृद्धान्नपुंसकात् ... न, but here: "
             "**अवृद्धाभ्यो नदीमानुषीभ्यस्तन्नामिकाभ्यः**, ढकोऽपवादः. "
             "यमुनाया अपत्यं यामुनः; इरावत्या अपत्यम् ऐरावतः; "
             "वैतस्तः, नार्मदः. मानुषीभ्यः — शैक्षितः, चैन्तितः.\n\n"
             "**TWO KINDS OF CONDITION IN ONE RULE, AND THE VṚTTI "
             "NAMES THE DIFFERENCE.** अवृद्धाभ्य इति **शब्दधर्मः**, "
             "नदीमानुषीभ्य इति **अर्थधर्मः** — the first is a "
             "property of the WORD, whether its first vowel is a "
             "vṛddhi by 1.1.73; the second is a property of what the "
             "word MEANS, a river or a woman. तेनाभेदात् प्रकृतयो "
             "निर्दिश्यन्ते: they are stated as one because there is "
             "no difference in what they pick out. And तन्नामिकाभ्य "
             "इति सर्वनाम्ना प्रत्ययप्रकृतेः परामर्शः — a pronoun "
             "pointing back at the base.\n\n"
             "Three counter-examples, one per word. अवृद्धाभ्य इति "
             "किम्? चान्द्रभागेयः, वासवदत्तेयः. नदीमानुषीभ्य इति "
             "किम्? सौपर्णेयः, वैनतेयः. तन्नामिकाभ्य इति किम्? "
             "शोभनायाः शौभनेयः",
         keeps_out="चान्द्रभागेयः, सौपर्णेयः, शौभनेयः"),
    Apatya("4.1.114", "aṇ", gana="ṛṣyandhakavṛṣṇikuru",
         excepts=("4.1.95",),
         why="ऋष्यन्धकवृष्णिकुरुभ्यश्च, इञोऽपवादः. ऋषयः प्रसिद्धा "
             "वसिष्ठादयः; अन्धका वृष्णयः कुरव इति वंशाख्याः. "
             "वासिष्ठः, वैश्वामित्रः; श्वाफल्कः, रान्धसः; "
             "वासुदेवः, आनिरुद्धः; नाकुलः, साहदेवः.\n\n"
             "**AND HERE THE VṚTTI DEFENDS THE GRAMMAR AGAINST ITS "
             "OWN EXAMPLES.** कथं पुनर्नित्यानां शब्दानाम् "
             "अन्धकादिवंशसमाश्रयणेनान्वाख्यानं युज्यते? — if words "
             "are eternal, how can a rule be framed by reference to "
             "particular royal houses? Two answers, and the vṛtti "
             "keeps both. केचिदाहुः — **काकतालीयन्यायेन** "
             "कुर्वादिवंशेष्वसंकरेणैव नकुलसहदेवादयः शब्दास्सुबहवः "
             "संकलिताः, तानुपादाय पाणिनिना स्मृतिरुपनिबद्धेति: by "
             "the crow-and-palm-fruit coincidence a great many such "
             "words happened to gather in those houses without "
             "mixing, and Pāṇini recorded what he found. अथवा — "
             "अन्धकवृष्णिकुरुवंशा अपि नित्या एव, तेषु ये शब्दाः "
             "प्रयुज्यन्ते, तत्रेदं प्रत्ययविधानम्: or the houses "
             "are eternal too, and the rule is about the words used "
             "in them"),
    Apatya("4.1.115", "aṇ", of=("mātṛ",), pre="saṃkhyā-sam-bhadra",
         along_with="u",
         why="मातुरुत्संख्यासंभद्रपूर्वायाः. द्वयोर्मात्रोरपत्यं "
             "द्वैमातुरः; षाण्मातुरः, सांमातुरः, भाद्रमातुरः.\n\n"
             "**उकारादेशार्थं वचनम्, प्रत्ययः पुनरुत्सर्गेणैव "
             "सिद्धः** — the affix came already from 4.1.83's "
             "default, so the whole rule is the उ. The fourth rule "
             "in this pāda whose stated affix is not what it is for, "
             "after 4.1.7, 4.1.97 and 4.1.116.\n\n"
             "स्त्रीलिङ्गनिर्देशोऽर्थापेक्षः, तेन धान्यमातुर्ग्रहणं "
             "न भवति — the feminine of the rule's own word is read "
             "as being about the SENSE, which keeps धान्यमातृ out. "
             "संख्यासंभद्रपूर्वाया इति किम्? सौमात्रः",
         keeps_out="सौमात्रः"),
    Apatya("4.1.116", "aṇ", of=("kanyā",), along_with="kanīna",
         excepts=("4.1.120",),
         why="कन्यायाः कनीन च, ढकोऽपवादः. तत्सन्नियोगेन कनीनशब्द "
             "आदेशो भवति — कानीनः कर्णः, कानीनो व्यासः. Karṇa and "
             "Vyāsa in one line, and the affix and the substitution "
             "come together as at 4.1.97"),
    Apatya("4.1.117", "aṇ", of=("vikarṇa",), among="vātsya",
         why="विकर्णशुङ्गच्छगलाद् वत्सभरद्वाजात्रिषु, यथासंख्यम्. "
             "वैकर्णो भवति वात्स्यश्चेत्, वैकर्णिरन्यः — the sixth "
             "rule of the pāda to turn on whose family is meant"),
    Apatya("4.1.117", "aṇ", of=("śuṅga",), among="bhāradvāja",
         why="विकर्णशुङ्गच्छगलाद् वत्सभरद्वाजात्रिषु — शौङ्गो भवति "
             "भारद्वाजश्चेत्, शौङ्गिरन्यः.\n\n"
             "**TWO READINGS OF THE SŪTRA ITSELF, AND BOTH ARE "
             "AUTHORITATIVE.** शुङ्गाशब्दं स्त्रीलिङ्गमन्ये पठन्ति, "
             "ततो ढकं प्रत्युदाहरन्ति शौङ्गेय इति — others read the "
             "word as feminine and give a different form as the "
             "counter-example. **द्वयमपि चैतत् प्रमाणम् उभयथा "
             "सूत्रप्रणयनात्**: both are valid, because the sūtra "
             "was composed both ways. Not two views of one text but "
             "two texts, and the vṛtti accepts both"),
    Apatya("4.1.117", "aṇ", of=("chagala",), among="ātreya",
         why="विकर्णशुङ्गच्छगलाद् वत्सभरद्वाजात्रिषु — छागलो "
             "भवत्यात्रेयश्चेत्, छागलिरन्यः"),
    Apatya("4.1.118", "aṇ", of=("pīlā",), optional=True,
         excepts=("4.1.121",),
         why="पीलाया वा. पैलः beside पैलेयः — an option where "
             "4.1.121's ढक् would have come outright, and stated "
             "because that rule beats 4.1.113's अण्"),
    Apatya("4.1.119", "ḍhak", of=("maṇḍūka",), optional=True,
         why="ढक् च मण्डूकात्. माण्डूकेयः — and चकारादण् च वा, "
             "**तेन त्रैरूप्यं भवति**: माण्डूकेयः, माण्डूकः, "
             "माण्डूकिः. One च making three forms, which is 4.1.38's "
             "मनोरौ वा eighty-one sūtras later and by a different "
             "instrument"),
    Apatya("4.1.120", "ḍhak", stri_pratyaya=True,
         why="स्त्रीभ्यो ढक्. सौपर्णेयः, वैनतेयः.\n\n"
             "**स्त्री HERE NAMES THE AFFIX AND NOT THE SENSE.** इह "
             "स्त्रीग्रहणेन टाबादिप्रत्ययान्ताः शब्दा गृह्यन्ते, and "
             "**स्त्रीप्रत्ययविज्ञापनाद् असत्यर्थग्रहणे** इह न "
             "भवति — इडबिडोऽपत्यम्, दरदोऽपत्यम् give ऐडबिडः and "
             "दारदः, being feminine in sense and carrying no "
             "feminine affix. The reverse of 4.1.115, where the "
             "feminine of the rule's own word WAS read as being "
             "about the sense.\n\n"
             "वडवाया वृषे वाच्ये — वाडवेयो वृषः स्मृतः, and "
             "अपत्ये प्राप्तस्ततोऽपकृष्य विधीयते, तेनापत्ये वाडव इति "
             "भवति: the affix is pulled out of the descendant-sense "
             "and given to another, so the descendant takes a "
             "different one. अण् क्रुञ्चाकोकिलात् स्मृतः — क्रौञ्चः, "
             "कौकिलः",
         keeps_out="ऐडबिडः, दारदः"),
    Apatya("4.1.121", "ḍhak", stri_pratyaya=True, dvyac=True,
         excepts=("4.1.113",),
         why="द्व्यचः, तन्नामिकाणोऽपवादः. दत्ताया अपत्यं दात्तेयः, "
             "गौपेयः. द्व्यच इति किम्? यामुनः — three vowels, and "
             "4.1.113's अण् stands"),
    Apatya("4.1.122", "ḍhak", stem_final="i", not_marked="iñ",
         dvyac=True,
         why="इतश्चानिञः. आत्रेयः, नैधेयः. स्त्रीग्रहणं निवृत्तम्, "
             "चकारो द्व्यच इत्यस्यानुकर्षणार्थः — one word stops and "
             "a च pulls another down, in the same rule.\n\n"
             "**अनिञः IS A CONDITION ON ANOTHER RULE'S OUTPUT.** इत "
             "इति किम्? दाक्षिः, प्लाक्षिः — those end in इ too, and "
             "the difference is that their इ is 4.1.95's इञ्. "
             "अनिञ इति किम्? दाक्षायणः, प्लाक्षायणः. द्व्यच इत्येव — "
             "मारीचः",
         keeps_out="दाक्षिः, दाक्षायणः, मारीचः"),
    Apatya("4.1.123", "ḍhak", gana="śubhrādi",
         why="शुभ्रादिभ्यश्च, यथायोगमिञादीनामपवादः. शौभ्रेयः, "
             "वैष्टपुरेयः. चकारोऽनुक्तसमुच्चयार्थ आकृतिगणताम् अस्य "
             "बोधयति — the third open list of the pāda, after "
             "4.1.56's क्रोडादि and 4.1.96's बाह्वादि, and this one "
             "is what accounts for गाङ्गेयः and पाण्डवेयः"),
    Apatya("4.1.124", "ḍhak", of=("vikarṇa", "kuṣītaka"),
         among="kāśyapa",
         why="विकर्णकुषीतकात् काश्यपे. वैकर्णेयः, कौषीतकेयः. "
             "काश्यप इति किम्? वैकर्णिः, कौषीतकिः.\n\n"
             "विकर्ण appears here AND at 4.1.117, with a different "
             "affix in a different family: वैकर्णः among the "
             "Vātsyas, वैकर्णेयः among the Kāśyapas, वैकर्णिः "
             "elsewhere. **One word, three families, three affixes**"),
    Apatya("4.1.125", "ḍhak", of=("bhrū",), along_with="vuk",
         why="भ्रुवो वुक् च. भ्रौवेयः — the affix and an augment "
             "together, तत्सन्नियोगेन, for the fourth time in this "
             "run"),
    Apatya("4.1.126", "ḍhak", gana="kalyāṇyādi", along_with="inaṅ",
         why="कल्याण्यादीनामिनङ्. काल्याणिनेयः, सौभागिनेयः, "
             "दौर्भागिनेयः — with उभयपदवृद्धि by 7.3.19, both "
             "members strengthened.\n\n"
             "**AND THE LIST IS THERE FOR TWO DIFFERENT REASONS AT "
             "ONCE.** स्त्रीप्रत्ययान्तानाम् **आदेशार्थं** ग्रहणम्, "
             "प्रत्ययस्य सिद्धत्वाद्; अन्येषाम् **उभयार्थम्** — for "
             "the members that already end in a feminine affix the "
             "ढक् came from 4.1.120 and only the substitution is "
             "new; for the rest both are given. The same split "
             "4.1.49's twelve words had, and stated in the same "
             "words"),
    Apatya("4.1.127", "ḍhak", of=("kulaṭā",), along_with="inaṅ",
         optional=True,
         why="कुलटाया वा. कौलटिनेयः beside कौलटेयः. आदेशार्थं वचनम्, "
             "प्रत्ययश्च पूर्वेणैव सिद्धः — again the affix was "
             "there already and the rule is for the substitution.\n\n"
             "कुलान्यटतीति कुलटा, पररूपं निपातनात्. And the vṛtti "
             "splits the word by what it means: या तु कुलान्यटन्ती "
             "**शीलं भिनत्ति**, ततः क्षुद्राभ्यो वा इति परत्वाड् "
             "ढ्रका भवितव्यम् — कौलटेरः. The same form takes a "
             "different affix according to whether the woman is "
             "merely one who goes about the houses or one who is "
             "thereby disgraced"),
    Apatya("4.1.128", "airak", of=("caṭakā",),
         why="चटकाया ऐरक्. चाटकैरः. चटकाच्चेति वक्तव्यम् adds the "
             "masculine — चटकस्यापत्यं चाटकैरः — and स्त्रियामपत्ये "
             "लुग् वक्तव्यः takes the affix away again in the "
             "feminine: चटकाया अपत्यं स्त्री चटका. Three vārttikas "
             "on a one-word rule, and the last undoes it"),
    Apatya("4.1.129", "ḍhrak", of=("godhā",),
         why="गोधाया ढ्रक्. गौधेरः. **शुभ्रादिष्वयं पठ्यते, तेन "
             "गौधेयोऽपि भवति** — the word is in 4.1.123's list as "
             "well, so both forms stand. A double membership "
             "licensing two forms, as at 4.1.108, and here the two "
             "rules are six apart"),
    Apatya("4.1.130", "ārak", of=("godhā",), authority="udīcām",
         why="आरगुदीचाम्. गौधारः — in the view of the NORTHERN "
             "teachers, and the seventh attribution in the project.\n\n"
             "**आचार्यग्रहणं पूजार्थम्** — the word *teachers* is "
             "there FOR HONOUR, which is the same thing 3.4.18's "
             "vṛtti said of प्राचामाचार्याणां मतेन. And "
             "वचनसामर्थ्यादेव पूर्वेण समावेशो भविष्यति: the two "
             "affixes co-apply on the strength of the rule being "
             "stated at all.\n\n"
             "AND THE RULE IS READ AS A ज्ञापक BECAUSE IT IS "
             "OTHERWISE EMPTY. आरग्वचनमनर्थकम्, रका सिद्धत्वात्? "
             "**ज्ञापकं त्वयमन्येभ्योऽपि भवतीति** — the ढ्रक् of "
             "4.1.129 would already have given the form, so the "
             "point of stating आरक् is to teach that it comes after "
             "OTHER words too: जाडारः, पाण्डारः"),
    Apatya("4.1.131", "ḍhrak", of_samjna="kṣudrā", optional=True,
         excepts=("4.1.120",),
         why="क्षुद्राभ्यो वा, ढकोऽपवादः. क्षुद्रा अङ्गहीनाः "
             "शीलहीनाश्च — the maimed and the disgraced. काणेरः "
             "beside काणेयः, दासेरः beside दासेयः.\n\n"
             "ढ्रगनुवर्तते, न आरक् — one of the two affixes of the "
             "last two rules carries down and the other does not, "
             "though they were given side by side. And "
             "अर्थधर्मेण तदभिधायिन्यः स्त्रीलिङ्गाः प्रकृतयो "
             "निर्दिश्यन्ते: the bases are named by a property of "
             "their MEANING, which is 4.1.113's अर्थधर्म again"),
    Apatya("4.1.132", "chaṇ", of=("pitṛṣvasṛ",), excepts=("4.1.113",),
         why="पितृष्वसुश्छण्, अणोऽपवादः. पैतृष्वस्रीयः"),
    Apatya("4.1.133", "ḍhak", of=("pitṛṣvasṛ",), along_with="lopa",
         why="ढकि लोपः. पैतृष्वसेयः — the स् of the stem goes before "
             "ढक्.\n\n"
             "**A RULE THAT IS ITS OWN ज्ञापक.** कथं पुनरिह ढक् "
             "प्रत्ययः? — the rule before gave छण् and nothing gives "
             "ढक् here at all, so what is this elision stated "
             "before? **एतदेव ज्ञापकं ढको भावस्य**: the rule's own "
             "existence is the evidence that the affix comes. A "
             "sūtra whose only support is that it was written"),
    Apatya("4.1.134", "chaṇ", of=("mātṛṣvasṛ",), along_with="lopa",
         why="मातुश्च. पितृष्वसुरित्येतदपेक्षते, "
             "**पितृष्वसुर्यदुक्तं तद् मातृष्वसुरपि भवति** — "
             "whatever was said of the father's sister holds of the "
             "mother's: छण्प्रत्ययो ढकि लोपश्च. मातृष्वस्रीयः, "
             "मातृष्वसेयः. An अतिदेश carrying TWO rules at once, "
             "where 3.4.85's carried one"),
    Apatya("4.1.135", "ḍhañ", of_samjna="catuṣpād",
         excepts=("4.1.83",),
         why="चतुष्पाद्भ्यो ढञ्, अणादीनामपवादः. कामण्डलेयः, "
             "शौन्तिबाहेयः, जाम्बेयः. चतुष्पादभिधायिनीभ्यः "
             "प्रकृतिभ्यः — again a condition on what the base "
             "MEANS and not on its shape"),
    Apatya("4.1.136", "ḍhañ", gana="gṛṣṭyādi", excepts=("4.1.83",),
         why="गृष्ट्यादिभ्यश्च, अणादीनामपवादः. गार्ष्टेयः, "
             "हार्ष्टेयः. गृष्टिशब्दो यश्चतुष्पाद्वचनः, ततः "
             "पूर्वेणैव सिद्धः; **अचतुष्पादर्थं वचनम्** — the first "
             "member is already covered by the rule before when it "
             "names a four-footed thing, so the list exists for when "
             "it does not"),
    # --- more affixes, and two whose sense is not a descendant -------
    Apatya("4.1.137", "yat", of=("rājan",), of_samjna="jāti",
         excepts=("4.1.83",),
         why="राजश्वशुरयोर्यत्, यथाक्रममणिञोरपवादः. राजन्यः. "
             "राज्ञोऽपत्ये जातिग्रहणम् — राजन्यो भवति क्षत्रियजातिश् "
             "चेत्, राजनोऽन्यः: only where the KṢATRIYA CLASS is "
             "meant, so the word for a king gives one form for the "
             "caste and another for a man"),
    Apatya("4.1.137", "yat", of=("śvaśura",),
         why="राजश्वशुरयोर्यत् — श्वशुर्यः, and here no class-sense "
             "is required"),
    Apatya("4.1.138", "gha", of=("kṣatra",), of_samjna="jāti",
         why="क्षत्राद् घः. क्षत्रियः — **अयमपि जातिशब्द एव**, this "
             "too is a class-word and not a patronymic: क्षात्रिरन्यः "
             "is the descendant. Two rules running, and both give a "
             "CASTE where the section gives descendants"),
    Apatya("4.1.139", "kha", stem_final="kula",
         why="कुलात् खः. आढ्यकुलीनः, श्रोत्रियकुलीनः, and कुलीनः "
             "alone — उत्तरसूत्रे पूर्वपदप्रतिषेधाद् इह तदन्तः "
             "केवलश्च दृश्यते: the NEXT rule refuses a first member, "
             "and that refusal is what shows this rule takes both the "
             "compound and the bare word. A rule's scope read off its "
             "neighbour's exclusion"),
    Apatya("4.1.140", "yat", stem_final="kula", pre="none", optional=True,
         why="अपूर्वपदाद् यत् ढकञौ बहुलम्. Where NO first member "
             "stands: कुल्यः, कौलेयकः — and ताभ्यां मुक्ते खोऽपि "
             "भवति, where those two are declined 4.1.139's ख comes: "
             "कुलीनः. Three forms from two rules.\n\n"
             "पदग्रहणं किम्? बहुच्पूर्वादपि यथा स्यात् — the word "
             "पद is there so that बहु in front does not count as a "
             "first member: बहुकुल्यः, बाहुकुलेयकः, बहुकुलीनः"),
    Apatya("4.1.141", "añ", of=("mahākula",), optional=True,
         why="महाकुलाद् अञ्खञौ. माहाकुलः, माहाकुलीनः — and "
             "अन्यतरस्यामित्यनुवर्तते, so पक्षे खः gives महाकुलीनः "
             "as well"),
    Apatya("4.1.142", "ḍhak", of=("duṣkula",), optional=True,
         why="दुष्कुलाड् ढक्. दौष्कुलेयः, and "
             "अन्यतरस्यामित्यनुवृत्तेः खश्च — दुष्कुलीनः"),
    Apatya("4.1.143", "cha", of=("svasṛ",), excepts=("4.1.83",),
         why="स्वसुश्छः, अणोऽपवादः. स्वस्रीयः"),
    Apatya("4.1.144", "vyat", of=("bhrātṛ",), excepts=("4.1.83",),
         why="भ्रातुर्व्यच्च, अणोऽपवादः. भ्रातृव्यः — and चकाराच् "
             "छश्च, भ्रात्रीयः. तकारः स्वरार्थः"),
    Apatya("4.1.145", "vyan", of=("bhrātṛ",), of_samjna="amitra",
         why="व्यन् सपत्ने. भ्रातृव्यः, and **अपत्यार्थोऽत्र "
             "नास्त्येव** — there is no descendant-sense here at "
             "all. समुदायेन चेदमित्रः सपत्न उच्यते: the whole word "
             "means an ENEMY. पाप्मना भ्रातृव्येण (तै०सं० "
             "२.२.१.२), भ्रातृव्यः कण्टकः.\n\n"
             "A rule inside the descendant section whose affix does "
             "not make a descendant, and the vṛtti says so outright. "
             "4.1.161 does the same sixteen sūtras later"),
    Apatya("4.1.146", "ṭhak", gana="revatyādi",
         why="रेवत्यादिभ्यष्ठक्, यथायोगं ढगादीनामपवादः. रैवतिकः, "
             "आश्वपालिकः"),
    # --- and three rules conditioned on CONTEMPT ----------------------
    Apatya("4.1.147", "ṇa", of_samjna="gotra-strī", attitude="kutsana",
         why="गोत्रस्त्रियाः कुत्सने ण च. गार्ग्या अपत्यं गार्गो "
             "जाल्मः; ग्लौचुकायनः — and चकारात् ठक् च, गार्गिकः, "
             "ग्लौचुकायनिकः.\n\n"
             "**AND THE VṚTTI SAYS WHAT THE CONTEMPT CONSISTS IN.** "
             "पितुरसंविज्ञाने मात्रा व्यपदेशोऽपत्यस्य कुत्सा — being "
             "named by the MOTHER, where the father is not known, is "
             "the disparagement. A social fact stated as a "
             "grammatical condition, and the affix is what carries "
             "it.\n\n"
             "गोत्रमिति किम्? कारिकेयो जाल्मः. स्त्रिया इति किम्? "
             "औपगविर्जाल्मः. कुत्सन इति किम्? गार्गेयो माणवकः — "
             "three words and a counter-example each, and the "
             "contempt is one of the three",
         keeps_out="गार्गेयो माणवकः"),
    Apatya("4.1.148", "ṭhak", of_samjna="sauvīra-gotra",
         attitude="kutsana", optional=True,
         why="वृद्धाट् ठक् सौवीरेषु बहुलम्. भागवित्तिकः, "
             "तार्णबिन्दविकः, आकशापेयिकः — and पक्षे यथाप्राप्तं "
             "फक्: भागवित्तायनः.\n\n"
             "**बहुलग्रहणम् उपाधिवैचित्र्यार्थम्**, and the vṛtti "
             "spells out what the variety is: गोत्रस्त्रिया इत्यारभ्य "
             "चत्वारो योगाः — तेषु **प्रथमः कुत्सन एव, अन्त्यः "
             "सौवीरगोत्र एव, मध्यमौ द्वयोरपि**. Four rules and two "
             "conditions, and the word बहुलम् is what tells you which "
             "rule carries which. A table stated in one word.\n\n"
             "वृद्धग्रहणं स्त्रीनिवृत्त्यर्थम्. सौवीरेष्विति किम्? "
             "औपगविर्जाल्मः",
         keeps_out="औपगविर्जाल्मः"),
    Apatya("4.1.149", "cha", marked="phiñ", of_samjna="sauvīra-gotra",
         attitude="kutsana",
         why="फेश्छ च. यामुन्दायनीयः, and चकाराट् ठक् — "
             "यामुन्दायनिकः. फेरिति फिञो ग्रहणं न फिनः, "
             "वृद्धाधिकारात् — the short form names one of two "
             "affixes and not the other, and which one is settled by "
             "a heading. कुत्सन इत्येव — यामुन्दायनिः",
         keeps_out="यामुन्दायनिः"),
    Apatya("4.1.150", "ṇa", of=("phāṇṭāhṛti",), of_samjna="sauvīra",
         excepts=("4.1.101",),
         why="फाण्टाहृतिमिमताभ्यां णफिञौ, फकोऽपवादः. फाण्टाहृतः, "
             "फाण्टाहृतायनिः; मैमतः, मैमतायनिः.\n\n"
             "**A COMPOUNDING RULE BROKEN ON PURPOSE, AS A SIGNAL.** "
             "**अल्पाच्तरस्यापूर्वनिपातो लक्षणव्यभिचारचिह्नम्, तेन "
             "यथासंख्यमिह न भवति** — 2.2.34 puts the word with fewer "
             "vowels first in a dvandva, and here it is NOT first; "
             "the violation is a MARK that 1.3.10's *taken in order* "
             "does not apply. A rule deliberately broken so that its "
             "breach may carry information"),
    Apatya("4.1.151", "ṇya", gana="kurvādi",
         why="कुर्वादिभ्यो ण्यः. कौरव्यः, गार्ग्यः.\n\n"
             "The vṛtti works hard at telling this ण्य from 4.1.172's: "
             "स तु क्षत्रियात् तद्राजसंज्ञकः, तस्य बहुषु लुका "
             "भवितव्यम्, अयं तु श्रूयत एव — कौरव्याः. The two "
             "affixes are identical in shape and differ in whether "
             "they vanish in the plural.\n\n"
             "कथं भाषायां वैन्यो राजेति? **छान्दस एवायं प्रमादात् "
             "कविभिः प्रयुक्तः** — a Vedic form used in ordinary "
             "speech BY THE CARELESSNESS OF POETS. The bluntest thing "
             "the vṛtti has said about attested usage anywhere in "
             "this pāda"),
    Apatya("4.1.152", "ṇya", stem_final="senā",
         why="सेनान्तलक्षणकारिभ्यश्च. कारिषेण्यः, हारिषेण्यः; "
             "लाक्षण्यः; and from the कारि words — कारिशब्दः कारूणां "
             "तन्तुवायादीनां वाचकः — तान्तुवाय्यः, कौम्भकार्यः, "
             "नापित्यः"),
    Apatya("4.1.153", "iñ", stem_final="senā", authority="udīcām",
         why="उदीचामिञ्. कारिषेणिः, हारिषेणिः, लाक्षणिः. **ण्ये "
             "प्राप्त इञपरो विधीयते** — the rule before had already "
             "given ण्य and this gives इञ् after it.\n\n"
             "वचनसामर्थ्यादेव प्रत्ययसमावेशे लब्धे **आचार्यग्रहणं "
             "वैचित्र्यार्थम्** — the two co-apply on the strength of "
             "the rule being stated, so naming the teachers is for "
             "VARIETY. 4.1.130's vṛtti said the same naming was for "
             "HONOUR and 3.4.18's said it was too; this is the third "
             "reading of the same move and the only one that is not.\n\n"
             "तक्षन्शब्दः शिवादिः, तेनाणायमिञ् बाध्यते, न तु ण्यः — "
             "which is exactly what 4.1.112's note said from the "
             "other end: ताक्ष्णः and ताक्षण्यः both stand"),
    Apatya("4.1.154", "phiñ", gana="tikādi",
         why="तिकादिभ्यः फिञ्. तैकायनिः, कैतवायनिः. वृषशब्दोऽत्र "
             "पठ्यते, तस्य प्रत्ययसन्नियोगेन यकारान्तत्वमिष्यते — "
             "वार्ष्यायणिः, a member whose shape changes only when "
             "the affix comes"),
    Apatya("4.1.155", "phiñ", of=("kosala", "karmāra"),
         excepts=("4.1.95",),
         why="कौसल्यकार्मार्याभ्यां च, इञोऽपवादः. कौसल्यायनिः, "
             "कार्मार्यायणिः. **परमप्रकृतेरेवायं प्रत्यय इष्यते** — "
             "कोसलस्यापत्यं, कर्मारस्यापत्यमिति: the affix is wanted "
             "after the ULTIMATE base, though the rule names the "
             "derived form, प्रत्ययसन्नियोगेन तु प्रकृतिरूपं "
             "निपात्यते. A rule that names one thing and is stated "
             "of another"),
    Apatya("4.1.156", "phiñ", marked="aṇ", dvyac=True,
         excepts=("4.1.95",),
         why="अणो द्व्यचः, इञोऽपवादः. कार्त्रायणिः, हार्त्रायणिः. "
             "अण इति किम्? दाक्षायणः. द्व्यच इति किम्? औपगविः",
         keeps_out="दाक्षायणः, औपगविः"),
    Apatya("4.1.157", "phiñ", of_samjna="vṛddha-agotra",
         authority="udīcām",
         why="उदीचां वृद्धादगोत्रात्. आम्रगुप्तायनिः, "
             "ग्रामरक्षायणिः. उदीचामिति किम्? आम्रगुप्तिः. "
             "वृद्धादिति किम्? याज्ञदत्तिः. अगोत्रादिति किम्? "
             "औपगविः — three words and a counter-example each",
         keeps_out="आम्रगुप्तिः, याज्ञदत्तिः, औपगविः"),
    Apatya("4.1.158", "phiñ", gana="vākinādi", along_with="kuk",
         why="वाकिनादीनां कुक् च. वाकिनकायनिः, गारेधकायनिः.\n\n"
             "**यदिह वृद्धमगोत्रं शब्दरूपं तस्य आगमार्थमेव ग्रहणम्, "
             "अन्येषाम् उभयार्थम्** — for the members the rule before "
             "already reaches only the augment is new; for the rest "
             "both are given. The same split as 4.1.49 and 4.1.126, "
             "third time in the pāda and stated in the same words. "
             "उदीचामित्यधिकारात् पक्षे तेऽपि भवन्ति — वाकिनिः, "
             "गारेधिः"),
    Apatya("4.1.159", "phiñ", stem_final="putra", along_with="kuk",
         optional=True, authority="udīcām",
         why="पुत्रान्तादन्यतरस्याम्. **तेन त्रैरूप्यं संपद्यते** — "
             "गार्गीपुत्रकायणिः, गार्गीपुत्रायणिः, गार्गीपुत्रिः. "
             "Three forms again, and here the option is only on the "
             "AUGMENT: पुत्रान्तमगोत्रमिति पूर्वेणैव प्रत्ययः "
             "सिद्धः, तस्मिन्ननेन कुगागमोऽन्यतरस्यां विधीयते"),
    Apatya("4.1.160", "phin", authority="prācām", optional=True,
         why="प्राचामवृद्धात् फिन् बहुलम्. ग्लुचुकायनिः, "
             "अहिचुम्बकायनिः. प्राचामिति किम्? ग्लौचुकिः. "
             "अवृद्धादिति किम्? राजदन्तिः.\n\n"
             "**FIVE WAYS OF SAYING *OPTIONALLY*, AND ONE WOULD HAVE "
             "DONE.** उदीचां, प्राचाम्, अन्यतरस्याम्, बहुलम् इति "
             "**सर्व एते विकल्पार्थाः, तेषामेकेनैव सिध्यति** — all "
             "of these are for the option and any ONE of them would "
             "have sufficed. तत्राचार्यग्रहणं **पूजार्थम्**, "
             "बहुलग्रहणं **वैचित्र्यार्थम्**: so the surplus is read "
             "as honour and as variety. क्वचिन्न भवत्येव — दाक्षिः, "
             "प्लाक्षिः",
         keeps_out="ग्लौचुकिः, राजदन्तिः"),
    Apatya("4.1.161", "añ", of=("manu",), of_samjna="jāti",
         along_with="ṣuk",
         why="मनोर्जातावञ्यतौ षुक् च. मानुषः, मनुष्यः — and "
             "**अपत्यार्थोऽत्र नास्त्येव**, no descendant-sense at "
             "all: जातिशब्दावेतौ, both are class-words. The second "
             "such rule in the section, after 4.1.145.\n\n"
             "तथा च मानुषा इति बहुषु न लुग् भवति — the plural keeps "
             "the affix, which a descendant-affix would not. "
             "अपत्यविवक्षायां त्वणैव भवितव्यम्: मानवी प्रजा. And the "
             "kārikā gives a third form for a third sense — अपत्ये "
             "कुत्सिते मूढे मनोरौत्सर्गिकः स्मृतः, नकारस्य च "
             "मूर्धन्यः — माणवः, of a descendant, contemptible or "
             "foolish"),
    # --- and the तद्राज affixes, after country-names ------------------
    Apatya("4.1.168", "añ", janapada=True, excepts=("4.1.83",),
         why="जनपदशब्दात् क्षत्रियादञ्. पाञ्चालः, ऐक्ष्वाकः, "
             "वैदेहः. जनपदशब्दादिति किम्? द्रौह्यवः, पौरवः. "
             "क्षत्रियादिति किम्? ब्राह्मणस्य पञ्चालस्यापत्यं "
             "पाञ्चालिः.\n\n"
             "**AND THE SAME AFFIX NAMES THE KING.** "
             "क्षत्रियसमानशब्दाज्जनपदशब्दात् **तस्य राजन्यपत्यवत्** "
             "— what is said of a descendant holds of the RULER: "
             "पञ्चालानां राजा पाञ्चालः. An अतिदेश carried through "
             "the next eight rules and repeated in each of their "
             "vṛttis",
         keeps_out="द्रौह्यवः, पाञ्चालिः"),
    Apatya("4.1.169", "añ", of=("sālveya", "gāndhāri"), janapada=True,
         why="साल्वेयगान्धारिभ्यां च. साल्वेयः, गान्धारः — stated "
             "because 4.1.171's ञ्यङ् would have come: "
             "अञपवादे वृद्धादिति ञ्यङि प्राप्ते पुनरञ् विधीयते. A "
             "rule restating an affix to hold off a rule two ahead"),
    Apatya("4.1.170", "aṇ", janapada=True, dvyac=True,
         excepts=("4.1.168",),
         why="द्व्यञ्मगधकलिङ्गसूरमसादण्, अञोऽपवादः. आङ्गः, वाङ्गः, "
             "पौण्ड्रः, सौह्मः; मागधः, कालिङ्गः, सौरमसः. तस्य "
             "राजनीत्येव — आङ्गो राजा"),
    Apatya("4.1.171", "ñyaṅ", janapada=True, of_samjna="vṛddha",
         excepts=("4.1.168",),
         why="वृद्धेत्कोसलाजादाञ् ञ्यङ्, अञोऽपवादः. आम्बष्ठ्यः, "
             "सौवीर्यः; इकारान्तात् — आवन्त्यः, कौन्त्यः; and "
             "कोसलाजादयोरवृद्धार्थं वचनम् — कौसल्यः, आजाद्यः.\n\n"
             "तपरकरणं किम्? कौमारः — the त holds it to the short इ, "
             "which is the same letter doing the same job at 4.1.4, "
             "4.1.44 and 4.1.95. पाण्डोर्जनपदशब्दात् क्षत्रियाड् "
             "ड्यण् वक्तव्यः: पाण्ड्यः, and अन्यस्मात् पाण्डव एव",
         keeps_out="कौमारः, पाण्डवः"),
    Apatya("4.1.172", "ṇya", of=("kuru",), janapada=True,
         excepts=("4.1.168", "4.1.170"),
         why="कुरुनादिभ्यो ण्यः, अणञोरपवादः. कौरव्यः; and from the "
             "न-initial words — नैषध्यः, नैपथ्यः.\n\n"
             "This affix and 4.1.151's are the same shape and "
             "different things: **this one is a तद्राज and vanishes "
             "in the plural, and that one does not** — कौरव्याः "
             "against कौरवाः. The vṛtti at 4.1.151 tells them apart "
             "by exactly that"),
    Apatya("4.1.173", "iñ", of_samjna="sālva-avayava", janapada=True,
         excepts=("4.1.168",),
         why="साल्वावयवप्रत्यग्रथकलकूटाश्मकादिञ्, अञोऽपवादः. "
             "औदुम्बरिः, तैलखलिः, माद्रकारिः, यौगन्धरिः, भौलिङ्गिः, "
             "शारदण्डिः; प्रात्यग्रथिः, कालकूटिः, आश्मकिः.\n\n"
             "साल्वा नाम क्षत्रिया ... तस्य निवासः साल्वो जनपदः, "
             "तदवयवा उदुम्बरादयः — the country is named from the "
             "people and the districts are parts of the country, so "
             "the rule reaches a place through two steps of naming. "
             "And a kārikā lists the six districts"),
    Apatya("4.1.175", "añ", of=("kamboja",), janapada=True,
         along_with="luk",
         why="कम्बोजाल्लुक्. The affix 4.1.168 gives is ELIDED: "
             "कम्बोजः, and by कम्बोजादिभ्यो लुग्वचनं चोलाद्यर्थम् "
             "also चोलः, केरलः, शकः, यवनः — country-names that are "
             "the same word as the people. तस्य राजनीत्येव — "
             "कम्बोजो राजा"),
)


@dataclass(frozen=True)
class Named:
    """The affix that names a descendant, and by which rule."""

    gives: str
    by: str
    why: str
    along_with: str = ""
    optional: bool = False
    excepts: Tuple[str, ...] = ()


@dataclass(frozen=True)
class NotNamed:
    """That no rule of this run reaches it."""

    by: str
    why: str
    gives: str = ""


def _reaches(row: Apatya, stem: str, gana: str, stem_final: str,
             marked: str, kind: str, among: str, pre: str,
             dvyac: bool, stri_pratyaya: bool,
             samjna: str, authority: str, attitude: str,
             janapada: bool) -> bool:
    if row.of and stem not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.stem_final and stem_final != row.stem_final:
        return False
    if row.marked and marked != row.marked:
        return False
    if row.kind and kind != row.kind:
        return False
    # A rule stated of one lineage does not reach another, and one
    # stated of none reaches all: भार्गिरन्यः is what the rule leaves
    # behind, not what it refuses.
    if row.among and among != row.among:
        return False
    if row.pre and pre != row.pre:
        return False
    if row.not_marked and marked == row.not_marked:
        return False
    if row.dvyac and not dvyac:
        return False
    if row.stri_pratyaya and not stri_pratyaya:
        return False
    if row.of_samjna and samjna != row.of_samjna:
        return False
    # A rule given on a teacher's authority does not apply unless
    # that view is being asked for. 4.1.130 आरगुदीचाम् stands beside
    # 4.1.129 rather than over it — वचनसामर्थ्यादेव पूर्वेण समावेशो
    # भविष्यति, the two co-apply — so the citation is a condition on
    # the question and not a claim to rank.
    if row.authority and authority != row.authority:
        return False
    if row.attitude and attitude != row.attitude:
        return False
    if row.janapada and not janapada:
        return False
    return True


def _how_specific(row: Apatya) -> int:
    """
    A lineage is the narrowest thing these rules state — five of them
    turn on whose family is meant, which is nothing in the word at
    all — and a stem's last sound the widest.
    """
    return (
        6 * bool(row.among)
        + 5 * bool(row.of)
        + 4 * bool(row.gana)
        + 3 * bool(row.marked)
        + 2 * bool(row.kind)
        + 1 * bool(row.stem_final)
        + 5 * bool(row.pre)
        + 2 * bool(row.not_marked)
        + 2 * bool(row.dvyac)
        + 2 * bool(row.stri_pratyaya)
        + 4 * bool(row.of_samjna)
        # An attributed rule only matches when its view is asked
        # for, so once it matches it is the narrower answer.
        + 3 * bool(row.authority)
        + 5 * bool(row.attitude)
        + 3 * bool(row.janapada)
    )


def apatya_affix(stem: str = "", *, gana: str = "", stem_final: str = "",
                 marked: str = "", kind: str = "", among: str = "",
                 pre: str = "", dvyac: bool = False,
                 stri_pratyaya: bool = False, samjna: str = "",
                 authority: str = "", attitude: str = "",
                 janapada: bool = False,
                 wants: str = "") -> object:
    """
    4.1.95–112 — which affix names a descendant.

    `kind` is गोत्र, युवन् or the immediate descendant; `among` is the
    lineage a rule holds itself to, which five rules of this run state
    and which is nothing in the word at all.
    """
    matched = [
        row for row in APATYA
        if _reaches(row, stem, gana, stem_final, marked, kind, among,
                    pre, dvyac, stri_pratyaya, samjna, authority,
                    attitude, janapada)
        and (not wants or row.gives == wants)
    ]
    if not matched:
        from src.astadhyayi.taddhita import default_affix

        fallen = default_affix()
        return Named(fallen.gives, fallen.by, fallen.why)
    row = max(matched, key=_how_specific)
    return Named(row.gives, row.sutra, row.why,
                 along_with=row.along_with, optional=row.optional,
                 excepts=row.excepts)


def apatya_sense(*, kind: str = "") -> object:
    """
    4.1.92 तस्यापत्यम् — the sense, and nothing else.

    अर्थनिर्देशोऽयम्. The rule gives no affix because 4.1.83 has
    already given one, and states no base because 4.1.82 has already
    said which word it is: तस्येति षष्ठीसमर्थादपत्यमित्येतस्मिन्नर्थे
    **यथाविहितं** प्रत्ययो भवति — *the affix as it has been provided*.

    **And it faces both ways.** पूर्वैरुत्तरैश्च प्रत्ययैर्
    अभिसंबध्यते — connected with the affixes BEFORE it as well as
    after, which is why 4.1.85's दैत्यः and 4.1.86's औत्सः are
    patronymics though their rules came earlier. Every heading met so
    far ran one way only.

    प्रकृत्यर्थविशिष्टः षष्ठ्यर्थोऽपत्यमात्रञ्चेह गृह्यते,
    लिङ्गवचनादिकमन्यत् सर्वमविवक्षितम् — what is taken is the
    genitive's sense as qualified by the base, and *descendant*
    simply; gender and number are not in question.
    """
    return Named(
        "", "4.1.92",
        "तस्यापत्यम् — अर्थनिर्देशोऽयम्, and three syllables naming "
        "no affix at all. तस्येति षष्ठीसमर्थादपत्यमित्येतस्मिन्नर्थे "
        "**यथाविहितं** प्रत्ययो भवति: the affix *as it has been "
        "provided*, which is 4.1.83's. उपगोरपत्यमौपगवः; आश्वपतः; "
        "दैत्यः; औत्सः; स्त्रैणः; पौंस्नः.\n\n"
        "AND IT FACES BOTH WAYS. पूर्वैरुत्तरैश्च प्रत्ययैर् "
        "अभिसंबध्यते — connected with the affixes BEFORE it as well "
        "as those after, which is how दैत्यः and औत्सः are "
        "patronymics though 4.1.85 and 4.1.86 were stated first. "
        "Every heading met so far governed forward only.\n\n"
        "प्रकृत्यर्थविशिष्टः षष्ठ्यर्थोऽपत्यमात्रञ्चेह गृह्यते, "
        "लिङ्गवचनादिकमन्यत् सर्वमविवक्षितम् — the genitive's sense "
        "as qualified by the base, and *descendant* simply. Gender "
        "and number are not in question.\n\n"
        "And the kārikā puts this rule against 4.3.120: "
        "तस्येदमित्यपत्येऽपि बाधनार्थं कृतं भवेत् / उत्सर्गः शेष "
        "एवासौ वृद्धान्यस्य प्रयोजनम् — *this belongs to him* would "
        "have covered a descendant too, and would then have had to "
        "be beaten; this rule is what does the beating, and the "
        "other stands as the residue")


def only_one(*, kind: str = "gotra", feminine: bool = False) -> object:
    """
    4.1.93 एको गोत्रे and 4.1.94 गोत्राद् यून्यस्त्रियाम् — two rules
    that provide nothing and restrict everything after them.

    **4.1.93 is a नियम against the obvious reading.** A lineage runs
    through generations, and भेदेन प्रत्यपत्यं प्रत्ययोत्पत्तिप्रसङ्गे
    — an affix would come at each. गोत्र एक एव प्रत्ययो भवति,
    सर्वेऽपत्येन युज्यन्ते: ONE affix, and everyone in the line is
    reached by it. गर्गस्यापत्यं गार्गिः, गार्गेरपत्यं गार्ग्यः,
    तत्पुत्रोऽपि गार्ग्यः — and his son too. योऽपि व्यवहितेन जनितः,
    सोऽपि प्रथमप्रकृतेरपत्यं भवत्येव: a descendant born at any remove
    is still the descendant OF THE FIRST BASE.

    **4.1.94 says what the young-descendant affix is added to**, and
    the vṛtti finds the rule as stated will not do. गोत्राद् एव
    प्रत्ययो भवति, न परमप्रकृत्यनन्तरयुवभ्यः — from the lineage-form
    and not from the ultimate base. अस्त्रियामिति किम्? दाक्षी,
    प्लाक्षी.

    Then: किं पुनरत्र प्रतिषिध्यते? यदि नियमः, स्त्रियामनियमः
    प्राप्नोति; अथ युवप्रत्ययः, स्त्रियां गोत्रप्रत्ययेन अभिधानं न
    प्राप्नोति — read as a restriction it leaves the feminine
    unrestricted, and read as giving an affix it leaves the feminine
    with no affix at all, गोत्रसंज्ञाया युवसंज्ञया बाधितत्वात्.
    **तस्माद् योगविभागः कर्तव्यः** — so the rule must be SPLIT IN
    TWO: गोत्राद् यूनि प्रत्ययो भवति, and then ततोऽस्त्रियाम्. A
    sūtra divided because neither reading of it whole would work.
    """
    if feminine:
        return Named(
            "", "4.1.94",
            "अस्त्रियाम् — दाक्षी, प्लाक्षी. The vṛtti splits the "
            "rule to make this come out: **तस्माद् योगविभागः "
            "कर्तव्यः**, गोत्राद् यूनि प्रत्ययो भवति, ततोऽस्त्रियाम्. "
            "Read whole it fails twice over — किं पुनरत्र "
            "प्रतिषिध्यते? यदि नियमः, स्त्रियामनियमः प्राप्नोति; अथ "
            "युवप्रत्ययः, स्त्रियां गोत्रप्रत्ययेनाभिधानं न "
            "प्राप्नोति, गोत्रसंज्ञाया युवसंज्ञया बाधितत्वात्. "
            "युवसंज्ञैव प्रतिषिध्यते, तेन स्त्री गोत्रप्रत्ययेन "
            "अभिधास्यते: what the second half refuses is the NAME, "
            "and the feminine is then named by the lineage-affix")
    if kind == "yuvan":
        return Named(
            "", "4.1.94",
            "गोत्राद् यूनि — the young-descendant affix is added to "
            "the LINEAGE-FORM and not to the ultimate base: "
            "गार्ग्यस्यापत्यं युवा गार्ग्यायणः, वात्स्यायनः, "
            "दाक्षायणः, प्लाक्षायणः, औपगविः, नाडायनिः. "
            "न परमप्रकृत्यनन्तरयुवभ्यः")
    return Named(
        "", "4.1.93",
        "एको गोत्रे — ONE affix for a whole lineage. "
        "अपत्यं पौत्रप्रभृति गोत्रम् (4.1.162), and भेदेन "
        "प्रत्यपत्यं प्रत्ययोत्पत्तिप्रसङ्गे नियमः क्रियते: an "
        "affix would otherwise come at every generation, and this "
        "says गोत्र एक एव प्रत्ययो भवति, सर्वेऽपत्येन युज्यन्ते.\n\n"
        "गर्गस्यापत्यं गार्गिः, गार्गेरपत्यं गार्ग्यः, तत्पुत्रोऽपि "
        "गार्ग्यः — and his son too, and his. योऽपि व्यवहितेन "
        "जनितः, सोऽपि प्रथमप्रकृतेरपत्यं भवत्येव: a descendant born "
        "at ANY remove is still the descendant of the first base, "
        "which is what stops the affix accumulating.\n\n"
        "अपतनादपत्यम् — *that which does not fall away*, and the "
        "vṛtti offers the restriction two ways: प्रत्ययो नियम्यते or "
        "प्रकृतिर्नियम्यते, the affix restricted or the base, "
        "without choosing")


def feminine_luk(*, among: str = "") -> object:
    """
    4.1.109 लुक् स्त्रियाम् — and in the feminine the affix goes.

    वतण्डशब्दादाङ्गिरस्यां स्त्रियां यञ्प्रत्ययस्य लुग् भवति, and
    **what the elision buys is a different affix**: लुकि कृते
    शार्ङ्गरवादिपाठाद् ङीन् भवति — once it is gone, 4.1.73 reaches
    the bare word and gives ङीन्. वतण्डी.

    आङ्गिरस इति किम्? वातण्ड्यायनी. शिवाद्यणि तु वातण्डी — and by
    the OTHER list the same form comes anyway, which is what 4.1.108
    said about that word being in two gaṇas.
    """
    if among and among != "āṅgirasa":
        return NotNamed(
            "4.1.109",
            "आङ्गिरस इति किम्? वातण्ड्यायनी — outside that lineage "
            "the affix stands. शिवाद्यणि तु वातण्डी, and by the "
            "other list the same form comes anyway")
    return Named(
        "", "4.1.109",
        "लुक् स्त्रियाम् — वतण्डशब्दादाङ्गिरस्यां स्त्रियां "
        "यञ्प्रत्ययस्य लुग् भवति. **And what the elision buys is a "
        "different affix**: लुकि कृते शार्ङ्गरवादिपाठाद् ङीन् भवति "
        "— once the यञ् is gone, 4.1.73 reaches the bare word and "
        "supplies ङीन्. वतण्डी.\n\n"
        "A rule that removes an affix in order that another may "
        "come, which is what 4.1.90's elision-before-formation did "
        "from the other end: तस्मिन्निवृत्ते सति यो यतः प्राप्नोति स "
        "ततो भवति")


def provisions_for(sutra_id: str) -> Tuple[Apatya, ...]:
    """Every row one sūtra states — several, where it gives a list."""
    return tuple(row for row in APATYA if row.sutra == sutra_id)


@dataclass(frozen=True)
class Called:
    """A name conferred on a descendant, and by which rule."""

    name: str
    by: str
    why: str
    optional: bool = False


def descendant_name(*, generation: int = 3, elder_alive: bool = False,
                    elder: str = "", attitude: str = "") -> Called:
    """
    4.1.162–167 — गोत्र and युवन्, and when each holds.

    **4.1.162 अपत्यं पौत्रप्रभृति गोत्रम्** — a descendant from the
    grandson onward. संबन्धिशब्दत्वादपत्यशब्दस्य यस्य यदपत्यं
    तदपेक्षया पौत्रप्रभृतेर्गोत्रसंज्ञा विधीयते: *descendant* is a
    relative term, so the count starts from whoever is in question.
    पौत्रप्रभृतीति किम्? कौञ्जिः, गार्गिः — the son is outside it.

    **4.1.163 जीवति तु वंश्ये युवा**, and the vṛtti has to change the
    case of a word to make it come out. पौत्रप्रभृतीति च न
    सामानाधिकरण्येनापत्यं विशेषयति; किं तर्हि? **षष्ठ्या
    विपरिणम्यते** पौत्रप्रभृतेर्यदपत्यमिति — read not as *the
    descendant from the grandson on* but as *the descendant OF one
    from the grandson on*, तेन चतुर्थादारभ्य युवसंज्ञा विधीयते: so
    the name starts from the FOURTH generation. A word's case altered
    in reading to move a boundary by one.

    Then three rules widen the condition and two more make the name
    optional for reasons that are not grammatical at all:

    * **4.1.164** — an elder brother alive, though a brother is not
      an ancestor: भ्राता तु न वंश्यः, **अकारणत्वात्**, not being a
      cause of the person.
    * **4.1.165** — any older सपिण्ड alive, optionally. And the
      vṛtti defines सपिण्ड by RITUAL: सप्तमपुरुषावधयः सपिण्डाः, and
      those for whom उभयत्र दशाहानि कुलस्यान्नं न भुज्यते (मनु०
      ५.६१) — kinship measured by whose food may not be eaten.
    * **4.1.166 वृद्धस्य च पूजायाम्** — the young-name used of an
      elder OUT OF RESPECT.
    * **4.1.167 यूनश्च कुत्सायाम्** — and the lineage-name used of a
      young man OUT OF CONTEMPT. निवृत्तिप्रधानो विकल्पः: the option
      is really a refusal, युवसंज्ञायां प्रतिषिद्धायां पक्षे
      गोत्रसंज्ञैव भवति, प्रतिपक्षाभावात्.

    **Two adjacent rules, one for honour and one for scorn**, both
    making the same pair of names optional and in opposite
    directions.
    """
    if attitude == "pūjā":
        return Called(
            "yuvan", "4.1.166",
            "वृद्धस्य च पूजायाम् — the YOUNG-name used of an elder, "
            "out of respect: तत्र भवान् गार्ग्यायणः, गार्ग्यो वा. "
            "संज्ञासामर्थ्याद् गोत्रं युवप्रत्ययेन पुनरुच्यते, and "
            "वृद्धस्येति षष्ठीनिर्देशो **विचित्रा सूत्रस्य कृतिः** — "
            "the genitive is odd and the vṛtti says so rather than "
            "explaining it away. पूजायामिति किम्? गार्ग्यः",
            optional=True)
    if attitude == "kutsā":
        return Called(
            "gotra", "4.1.167",
            "यूनश्च कुत्सायाम् — and the LINEAGE-name used of a "
            "young man, out of contempt: गार्ग्यो जाल्मः, "
            "गार्ग्यायणो वा. **निवृत्तिप्रधानो विकल्पः**: the option "
            "is really a refusal — युवसंज्ञायां प्रतिषिद्धायां पक्षे "
            "गोत्रसंज्ञैव भवति, प्रतिपक्षाभावात्, since with the "
            "young-name refused nothing else is left. "
            "कुत्सायामिति किम्? गार्ग्यायणः",
            optional=True)
    if generation < 3:
        return Called(
            "", "4.1.162",
            "पौत्रप्रभृतीति किम्? अन्यस्य मा भूत् — कौञ्जिः, "
            "गार्गिः. The son is outside the name, and the count is "
            "relative: संबन्धिशब्दत्वादपत्यशब्दस्य यस्य यदपत्यं "
            "तदपेक्षया पौत्रप्रभृतेर्गोत्रसंज्ञा विधीयते")
    if elder_alive and elder == "sapiṇḍa":
        return Called(
            "yuvan", "4.1.165",
            "भ्रातरि च ज्यायसि — ... अन्यस्मिन् सपिण्डे स्थविरतरे "
            "जीवति, वा: गार्ग्यायणो गार्ग्यो वा. **तरब्निर्देश "
            "उभयोत्कर्षार्थः** — the comparative is used so that BOTH "
            "standing and age must be greater: पितृव्ये पितामहे "
            "भ्रातरि च वयसाधिके जीवति.\n\n"
            "AND सपिण्ड IS DEFINED BY RITUAL, NOT BY DESCENT. "
            "सप्तमपुरुषावधयः सपिण्डाः स्मर्यन्ते, येषाम् **उभयत्र "
            "दशाहानि कुलस्यान्नं न भुज्यते** (मनु० ५.६१) इत्येवमादिकायां "
            "क्रियायामनधिकारः — kinship measured by whose food may "
            "not be eaten. स्थविरतर इति किम्? स्थानवयोन्यूने गार्ग्य "
            "एव. जीवतीति किम्? मृते गार्ग्य एव",
            optional=True)
    if elder_alive and elder == "bhrātṛ":
        return Called(
            "yuvan", "4.1.164",
            "भ्रातरि च ज्यायसि — an elder BROTHER alive, and the "
            "rule is needed because a brother is not an ancestor: "
            "**अवंश्यार्थोऽयमारम्भः**. पूर्वजाः पित्रादयो वंश्या "
            "इत्युच्यन्ते; भ्राता तु न वंश्यः, **अकारणत्वात्** — "
            "not being a cause of the person. गार्ग्ये जीवति "
            "गार्ग्यायणोऽस्य कनीयान् भ्राता")
    if elder_alive:
        return Called(
            "yuvan", "4.1.163",
            "जीवति तु वंश्ये युवा. अभिजनप्रबन्धो वंशः, तत्र भवो "
            "वंश्यः पित्रादिः — a father or forefather still living, "
            "and the descendant is called YOUNG: गार्ग्यायणः, "
            "वात्स्यायनः.\n\n"
            "**AND A WORD'S CASE IS CHANGED IN READING TO MOVE THE "
            "BOUNDARY BY ONE.** पौत्रप्रभृतीति च न "
            "सामानाधिकरण्येनापत्यं विशेषयति; किं तर्हि? **षष्ठ्या "
            "विपरिणम्यते** पौत्रप्रभृतेर्यदपत्यमिति — not *the "
            "descendant from the grandson on* but *the descendant OF "
            "one from the grandson on*, तेन **चतुर्थादारभ्य** "
            "युवसंज्ञा विधीयते. तुशब्दोऽवधारणार्थः — युवैव न "
            "गोत्रम्")
    return Called(
        "gotra", "4.1.162",
        "अपत्यं पौत्रप्रभृति गोत्रम् — a descendant from the grandson "
        "onward. गर्गस्यापत्यं पौत्रप्रभृति गार्ग्यः, वात्स्यः.\n\n"
        "संबन्धिशब्दत्वादपत्यशब्दस्य यस्य यदपत्यं तदपेक्षया "
        "पौत्रप्रभृतेर्गोत्रसंज्ञा विधीयते — *descendant* is a "
        "RELATIVE term, so the count starts from whoever is in "
        "question rather than from a fixed ancestor.\n\n"
        "गोत्रप्रदेशाः — एको गोत्रे इत्येवमादयः: the vṛtti points at "
        "4.1.93, which used this name sixty-nine sūtras before it was "
        "conferred")


def tadraja() -> Called:
    """
    4.1.174 ते तद्राजाः — the affixes just given bear the name.

    **And the pronoun reaches back only so far, because a section
    stops it.** जनपदशब्दात् क्षत्रियादञ् इत्येवमादयः प्रत्ययाः
    सर्वनाम्ना प्रत्यवमृश्यन्ते **न तु पूर्वे, गोत्रयुवसंज्ञाकाण्डेन
    व्यवहितत्वात्** — *those* reaches the affixes from 4.1.168 and no
    further, because the section on the गोत्र and युवन् names stands
    between and separates them.

    A block of rules acting as a BARRIER. Anuvṛtti in this project has
    been stopped by a word (3.4.99's नित्यम्), read backward (4.1.18's
    सर्वत्र), and carried half-way (4.1.27); this is the first time a
    whole section has stopped a reference by standing in its path.
    """
    return Called(
        "tadrāja", "4.1.174",
        "ते तद्राजाः — the affixes given after a country-name for a "
        "kṣatriya bear the name तद्राज. तद्राजप्रदेशाः — तद्राजस्य "
        "बहुषु तेनैवास्त्रियाम् इत्येवमादयः, and 2.4.62 is where the "
        "name is spent.\n\n"
        "**AND THE PRONOUN REACHES BACK ONLY SO FAR, BECAUSE A "
        "SECTION STOPS IT.** जनपदशब्दात् क्षत्रियादञ् इत्येवमादयः "
        "प्रत्ययाः सर्वनाम्ना प्रत्यवमृश्यन्ते **न तु पूर्वे, "
        "गोत्रयुवसंज्ञाकाण्डेन व्यवहितत्वात्** — *those* takes in the "
        "affixes from 4.1.168 and no earlier ones, because 4.1.162 to "
        "4.1.167 stand between and separate them.\n\n"
        "A block of rules acting as a BARRIER. Anuvṛtti has been "
        "stopped by a word at 3.4.99, read backward at 4.1.18 and "
        "carried half-way at 4.1.27; this is the first time a whole "
        "section has blocked a reference by standing in its path")


@dataclass(frozen=True)
class Dropped:
    """Whether a तद्राज affix vanishes, and by which rule."""

    holds: bool
    by: str
    why: str


def tadraja_luk(*, feminine: bool = False, of: str = "",
                affix: str = "", gana: str = "") -> Dropped:
    """
    4.1.176–178 — when a तद्राज affix vanishes in the feminine.

    4.1.176 names three words, 4.1.177 generalises to any अ-affix,
    and 4.1.178 refuses both for the eastern kṣatriyas and two lists.

    **And 4.1.178's refusal is read as a ज्ञापक about a rule in
    another chapter.** कस्य पुनरकारस्य प्रत्ययस्य यौधेयादिभ्यो लुक्
    प्राप्तः प्रतिषिध्यते? पाञ्चमिकस्य अञः — 5.3.117's. कथं पुनस्
    तस्य भिन्नप्रकरणस्थस्य अनेन लुक् प्राप्नोति? **एतदेव
    विज्ञापयति** पाञ्चमिकस्यापि तद्राजस्य अतश्च इत्यनेन लुग् भवतीति:
    the refusal is evidence that 4.1.177 reaches an affix given two
    chapters later. And the fruit is a third rule entirely —
    पर्श्वाद्यणः स्त्रियां लुक् सिद्धो भवति, यौधेयादिप्रतिषेधो
    ज्ञापकः पर्श्वाद्यणो लुगिति.
    """
    if not feminine:
        return Dropped(
            False, "4.1.176",
            "स्त्रियामित्येव — the affix stands where no woman is "
            "meant: आवन्त्यः, कौन्त्यः, कौरव्यः")
    if gana in ("bhargādi", "yaudheyādi") or of == "prācya":
        return Dropped(
            False, "4.1.178",
            "न प्राच्यभर्गादियौधेयादिभ्यः — the elision is REFUSED: "
            "पाञ्चाली, वैदेही, आङ्गी, मागधी; भार्गी, कारूषी, "
            "कैकेयी; यौधेयी, शौभ्रेयी, शौक्रेयी.\n\n"
            "**AND THE REFUSAL IS READ AS EVIDENCE ABOUT A RULE TWO "
            "CHAPTERS AWAY.** कस्य पुनरकारस्य प्रत्ययस्य "
            "यौधेयादिभ्यो लुक् प्राप्तः प्रतिषिध्यते? पाञ्चमिकस्याञः "
            "— 5.3.117's. कथं पुनस्तस्य भिन्नप्रकरणस्थस्यानेन लुक् "
            "प्राप्नोति? **एतदेव विज्ञापयति** पाञ्चमिकस्यापि "
            "तद्राजस्य अतश्च इत्यनेन लुग् भवतीति: a refusal here is "
            "the proof that 4.1.177 reaches an affix given in "
            "अध्याय ५.\n\n"
            "And the point of the proof is a third rule: "
            "पर्श्वाद्यणः स्त्रियां लुक् सिद्धो भवति — पर्शुः, "
            "रक्षाः, असुरी. यौधेयादिप्रतिषेधो ज्ञापकः पर्श्वाद्यणो "
            "लुगिति")
    if of in ("avanti", "kunti", "kuru"):
        return Dropped(
            True, "4.1.176",
            "अवन्तिकुन्तिकुरुभ्यश्च — the तद्राज affix goes in the "
            "feminine: अवन्ती, कुन्ती, कुरूः. अवन्तिकुन्तिभ्यां "
            "ञ्यङः, कुरोर्ण्यस्य — three words and two affixes. "
            "स्त्रियामिति किम्? आवन्त्यः, कौन्त्यः, कौरव्यः")
    if affix in ("", "a", "añ", "aṇ"):
        return Dropped(
            True, "4.1.177",
            "अतश्च — and any तद्राज affix in अ goes: शूरसेनी, "
            "मद्री, दरत्. तकारो विस्पष्टार्थः, the त only for "
            "clarity.\n\n"
            "अवन्त्यादिभ्यो लुग्वचनात् **तदन्तविधिरत्र नास्ति** — "
            "because the rule before named particular words, this "
            "one does not reach a compound through its last member: "
            "आम्बष्ठ्या, सौवीर्या keep their affixes. A neighbour's "
            "form deciding this rule's reach, which is what 4.1.139 "
            "did from the other direction")
    return Dropped(
        False, "4.1.177",
        "अतश्च — the affix is not one in अ, so it stands")
