# -*- coding: utf-8 -*-
"""
४.१.७६ and ४.१.८२–९१ — the taddhita heading, and what it presupposes.

4.1.76 तद्धिताः names everything from here to the end of अध्याय ५.
But three more headings have to be in place before a single affix can
be given, and this run puts them there:

* **4.1.82 समर्थानां प्रथमाद्वा** — from the FIRST of the words that
  are syntactically connected, OPTIONALLY. Three words, each an
  अधिकार in its own right, and together they say what a taddhita
  attaches TO. Without them a rule like तस्यापत्यम् would not say
  which of the two words in *Upagu's descendant* takes the affix.

* **4.1.83 प्राग्दीव्यतोऽण्** — and unless something else is said,
  the affix is अण्. A default running to 4.4.2, which is how the
  rules that follow can state only a SENSE and let the affix be
  understood.

* **4.1.88–91** — and where a taddhita would have come and does not
  show, it is ELIDED rather than absent. Four rules on लुक्, which is
  the machinery that lets a form be derived and then not appear.

The order matters and is the vṛtti's own: 4.1.82 says what attaches,
4.1.83 says what attaches by default, and only then does 4.1.92
तस्यापत्यम् begin to say in what senses.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: The three words of 4.1.82, each governing separately.
#: त्रयमप्यधिक्रियते समर्थानामिति च, प्रथमादिति च, वेति च.
SAMARTHA_WORDS: Tuple[str, ...] = ("samarthānām", "prathamāt", "vā")


@dataclass(frozen=True)
class Heading:
    """What a heading governs, how far, and what its words do."""

    by: str
    why: str
    #: The sūtra the heading runs to, where the vṛtti states one.
    through: str = ""
    #: The words the heading contributes, where it contributes more
    #: than one. 4.1.82 gives three and each governs alone.
    words: Tuple[str, ...] = ()
    #: The name it confers, for a संज्ञा-heading.
    names: str = ""


@dataclass(frozen=True)
class Affix:
    """A taddhita affix, and by which rule."""

    gives: str
    by: str
    why: str
    #: The rules this one excepts, where the vṛtti says अपवादः.
    excepts: Tuple[str, ...] = ()


@dataclass(frozen=True)
class Elided:
    """Whether a taddhita that would have come is dropped."""

    holds: bool
    by: str
    why: str
    optional: bool = False


def taddhita_heading() -> Heading:
    """
    4.1.76 तद्धिताः — every affix from here to the end of अध्याय ५
    bears the name.

    अधिकारोऽयम्, आ पञ्चमाध्यायपरिसमाप्तेः. It runs exactly as far as
    4.1.1's ङ्याप्प्रातिपदिकात्, which is the pair a reader needs: one
    heading says what the affixes attach TO and the other says what
    they are CALLED, over the same two chapters.

    **And the plural is doing work.** बहुवचनमनुक्ततद्धितपरिग्रहार्थम्
    — the name is given in the plural so that affixes NOT stated in
    these two chapters are taken in as well: पृथिव्या ञाञौ (वा०
    ४.१.८५) and अग्रादिपश्चाड्डिमच् (वा० ४.३.२३) come under it though
    no sūtra gives them. A grammatical number read as a scope.
    """
    return Heading(
        "4.1.76",
        "तद्धिताः — अधिकारोऽयम्. आ पञ्चमाध्यायपरिसमाप्तेर्यानित "
        "ऊर्ध्वमनुक्रमिष्यामः, तद्धितसंज्ञास्ते वेदितव्याः. The same "
        "range 4.1.1 governs, and the two make a pair: one says what "
        "the affixes attach TO and this says what they are CALLED. "
        "वक्ष्यति यूनस्तिः — युवतिः.\n\n"
        "AND THE PLURAL IS DOING WORK. "
        "बहुवचनमनुक्ततद्धितपरिग्रहार्थम् — the name is given in the "
        "plural so that affixes NOT stated in these chapters are "
        "taken in too: पृथिव्या ञाञौ (वा० ४.१.८५) and "
        "अग्रादिपश्चाड्डिमच् (वा० ४.३.२३) become तद्धित though no "
        "sūtra gives them. A grammatical number read as a scope.\n\n"
        "तद्धितप्रदेशाः — कृत्तद्धितसमासाश्च इत्येवमादयः: the "
        "vṛtti points at where the name is used, and 1.2.46 is the "
        "first, which is what makes a taddhita-formed word a "
        "प्रातिपदिक and so lets 4.1.1 govern the next affix",
        through="5.4.160", names="taddhita")


def samartha(*, position: int = 1, connected: bool = True) -> Heading:
    """
    4.1.82 समर्थानां प्रथमाद्वा — of the words that go together, the
    FIRST takes the affix, and optionally.

    त्रयमप्यधिक्रियते समर्थानामिति च, प्रथमादिति च, वेति च — **three
    words and each governs separately**, which is why this is one
    sūtra doing the work of three headings.

    **What each of them buys is shown by what goes wrong without it.**
    समर्थानामिति किम्? कम्बल उपगोः, अपत्यं देवदत्तस्य — two words in
    one sentence that do not go together, and without this the affix
    would cross between them. प्रथमादिति किम्? षष्ठ्यन्ताद् यथा
    स्यात् प्रथमान्ताद् मा भूत् — the affix comes after the word in
    the genitive, not after the one in the nominative. वेति किम्?
    वाक्यमपि हि यथा स्यात् — so that the phrase उपगोरपत्यम् may
    stand beside the word औपगवः.

    समर्थानामिति निर्धारणे षष्ठी: the genitive is one of selection —
    समर्थानां मध्ये प्रथमः प्रत्ययप्रकृतित्वेन निर्धार्यते, the first
    is picked out FROM AMONG the connected words as the base.

    The heading runs to 5.3.1 प्राग् दिशो विभक्तिः, and the vṛtti
    says why it stops there: स्वार्थिकेषु ह्यस्योपयोगो नास्ति,
    विकल्पोऽपि तत्रानवस्थितः — the affixes beyond that point add no
    meaning of their own, so there is nothing for *the first of the
    connected words* to pick out, and केचिन्नित्यमेव भवन्ति, some of
    them are not optional at all.
    """
    if not connected:
        return Heading(
            "4.1.82",
            "समर्थानाम् — the words do not go together, so no affix "
            "crosses between them: कम्बल उपगोः, अपत्यं देवदत्तस्य. "
            "समर्थानामिति निर्धारणे षष्ठी, and where there is nothing "
            "to select from there is nothing to select",
            through="5.3.1", words=SAMARTHA_WORDS)
    if position != 1:
        return Heading(
            "4.1.82",
            "प्रथमात् — the affix comes after the FIRST of the "
            "connected words, not the %d%s. षष्ठ्यन्ताद् यथा स्यात् "
            "प्रथमान्ताद् मा भूत्"
            % (position, "th" if position > 3 else
               ("nd" if position == 2 else "rd")),
            through="5.3.1", words=SAMARTHA_WORDS)
    return Heading(
        "4.1.82",
        "समर्थानां प्रथमाद्वा — त्रयमप्यधिक्रियते समर्थानामिति च, "
        "प्रथमादिति च, वेति च: THREE WORDS AND EACH GOVERNS "
        "SEPARATELY, which is one sūtra doing the work of three "
        "headings. उपगोरपत्यम् — औपगवः.\n\n"
        "AND WHAT EACH BUYS IS SHOWN BY WHAT GOES WRONG WITHOUT IT. "
        "समर्थानामिति किम्? कम्बल उपगोः, अपत्यं देवदत्तस्य — words in "
        "one sentence that do not go together, and without this the "
        "affix would cross between them. प्रथमादिति किम्? "
        "षष्ठ्यन्ताद् यथा स्यात् प्रथमान्ताद् मा भूत्. वेति किम्? "
        "वाक्यमपि हि यथा स्यात् — so that the PHRASE उपगोरपत्यम् may "
        "stand beside the single word.\n\n"
        "समर्थानामिति निर्धारणे षष्ठी — समर्थानां मध्ये प्रथमः "
        "प्रत्ययप्रकृतित्वेन निर्धार्यते: the genitive selects, and "
        "the first is picked out FROM AMONG the connected words as "
        "the base.\n\n"
        "IT RUNS TO 5.3.1, AND THE VṚTTI SAYS WHY IT STOPS THERE. "
        "स्वार्थिकप्रत्ययावधिश्चायमधिकारः — स्वार्थिकेषु "
        "ह्यस्योपयोगो नास्ति, विकल्पोऽपि तत्रानवस्थितः, "
        "केचिन्नित्यमेव भवन्ति: past that point the affixes add no "
        "meaning of their own, so there is nothing for *the first of "
        "the connected words* to select, and the option is not "
        "steady there either. A heading bounded by the point at which "
        "its own words stop meaning anything",
        through="5.3.1", words=SAMARTHA_WORDS)


def default_affix() -> Affix:
    """
    4.1.83 प्राग्दीव्यतोऽण् — until 4.4.2, the affix is अण् unless a
    rule says otherwise.

    तदेकदेशो दीव्यच्छब्दोऽवधित्वेन गृह्यते — the boundary is named by
    taking ONE WORD out of the rule it stops at, तेन दीव्यति (4.4.2),
    and using that word as the marker. The same way 3.3.140's option
    was bounded, and the same way 4.1.87 and 5.2.1 are paired.

    अधिकारः, परिभाषा, विधिर्वेति त्रिष्वपि दर्शनेष्वपवादविषयं
    परिहृत्याण् प्रवर्तते — **whether it is read as a heading, as a
    principle, or as a rule that gives an affix, the result is the
    same**: अण् comes wherever no exception takes the ground. The
    vṛtti lists three analyses and declines to choose, because
    nothing turns on it.

    This is what lets every rule from 4.1.92 onward state only a
    SENSE — तस्यापत्यम्, तेन रक्तं रागात्, तत्र भवः — and leave the
    affix to be understood.
    """
    return Affix(
        "aṇ", "4.1.83",
        "प्राग्दीव्यतोऽण् — प्राग् दीव्यत्संशब्दनाद् यानित "
        "ऊर्ध्वमनुक्रमिष्यामः, अण्प्रत्ययस्तत्र भवतीति वेदितव्यम्. "
        "औपगवः, कापटवः.\n\n"
        "THE BOUNDARY IS NAMED BY TAKING ONE WORD OUT OF THE RULE IT "
        "STOPS AT. तेन दीव्यति (4.4.2) is the rule, and तदेकदेशो "
        "दीव्यच्छब्दोऽवधित्वेन गृह्यते — a single word of it is "
        "lifted out and used as the marker.\n\n"
        "AND THE VṚTTI OFFERS THREE ANALYSES AND CHOOSES NONE. "
        "अधिकारः, परिभाषा, विधिर्वेति त्रिष्वपि दर्शनेषु "
        "अपवादविषयं परिहृत्याण् प्रवर्तते — heading, principle or "
        "rule, the result is the same: अण् comes wherever no "
        "exception has the ground. Nothing turns on which it is, and "
        "the commentary says so rather than deciding.\n\n"
        "This is what lets every rule from 4.1.92 on state only a "
        "SENSE and leave the affix to be understood")


#: 4.1.84 to 4.1.87 — the rules that except 4.1.83's अण् and, in one
#: case, restate it.
PRAG_DIVYATAH: Tuple[Tuple[str, str, str, Tuple[str, ...]], ...] = (
    ("4.1.84", "aṇ", "aśvapatyādi",
     ("4.1.85",)),
    ("4.1.85", "ṇya", "dity-adity-āditya-paty-uttarapada", ()),
    ("4.1.86", "añ", "utsādi", ("4.1.83", "4.1.85")),
    ("4.1.87", "nañ", "strī", ()),
    ("4.1.87", "snañ", "puṃs", ()),
)


def prag_divyatah_affix(of: str = "") -> Affix:
    """
    4.1.84–87 — the affixes given in the senses that run to 4.4.2.

    4.1.84 अश्वपत्यादिभ्यश्च gives 4.1.83's own अण् to a list, and
    the vṛtti says why a rule is needed to give what the default
    already gives: पत्युत्तरपदाद् ण्यं वक्ष्यति, तस्यापवादः — the
    NEXT rule would take these away, so this one holds them back
    against a rule that has not been stated yet.

    4.1.86 उत्सादिभ्योऽञ् is अणस्तदपवादानां च बाधकः: it beats the
    default AND the exceptions to the default, which is a rank above
    what an ordinary अपवाद claims.

    4.1.87 स्त्रीपुंसाभ्यां नञ्स्नञौ भवनात् pairs two stems with two
    affixes यथाक्रमम् and shows one affix serving four senses in a
    row — स्त्रैणम् for *born among women*, for *a collection of*,
    for *come from*, and for *good for*. **The affix does not change
    with the sense; the sense is supplied by the section the rule
    stands in.**
    """
    matched = [row for row in PRAG_DIVYATAH if not of or row[2] == of]
    if not matched:
        return default_affix()
    sutra, gives, ground, excepts = matched[0]
    WHY = {
        "4.1.84":
            "अश्वपत्यादिभ्यश्च — 4.1.83's own अण् given again to a "
            "list, and the vṛtti says why: पत्युत्तरपदाद् ण्यं "
            "वक्ष्यति, तस्यापवादः. The NEXT rule would take these "
            "words away, so this one holds them back **against a "
            "rule that has not been stated yet**. आश्वपतम्, शातपतम्",
        "4.1.85":
            "दित्यदित्यादित्यपत्युत्तरपदाण्ण्यः. दैत्यः, आदित्यः, "
            "प्राजापत्यम्, सैनापत्यम्.\n\n"
            "The vārttikas on this rule are the densest in the pāda, "
            "and several are cited straight to a text: वाच्यः "
            "(मा०सं० १३.५८), मात्या (मै०सं० २.७.१९), पैतृमत्यम् "
            "(मा०सं० ७.४६), पार्थिवा (ऋ० १.६४.३), दैव्यम् "
            "(ऋ० १.३१.१७), बाह्याः (शौ०सं० १९.४४.६). And one of them "
            "settles a whole class of conflicts by **पूर्वविप्रतिषेध** "
            "— ण्यादयोऽर्थविशेषलक्षणादणपवादात् पूर्वविप्रतिषेधेन: "
            "an EARLIER rule made to beat a later one, which is the "
            "same instrument 3.4.37 used",
        "4.1.86":
            "उत्सादिभ्योऽञ्, अणस्तदपवादानां च बाधकः — it beats the "
            "default AND the exceptions to the default, which is a "
            "rank above what an ordinary अपवाद claims. औत्सः, "
            "औदपानः.\n\n"
            "ग्रीष्मादच्छन्दसीति वक्तव्यम् (ग०सू० ५९), and the "
            "vṛtti stops to say which छन्दस् is meant: "
            "छन्दश्चेह वृत्तं गृह्यते न वेदः — the METRE and not the "
            "Veda. त्रिष्टुब् ग्रैष्मी (काठ०सं० १६.१९)",
        "4.1.87":
            "स्त्रीपुंसाभ्यां नञ्स्नञौ भवनात्, यथाक्रमम्. And ONE "
            "AFFIX SERVES FOUR SENSES IN A ROW: स्त्रीषु भवं "
            "स्त्रैणम्, स्त्रीणां समूहः स्त्रैणम्, स्त्रीभ्य आगतं "
            "स्त्रैणम्, स्त्रीभ्यो हितं स्त्रैणम् — born among, a "
            "collection of, come from, good for. **The affix does "
            "not change with the sense**; the sense comes from the "
            "section the rule stands in, which is what 4.1.83's "
            "default made possible.\n\n"
            "स्त्रियाः पुंवद् इति ज्ञापकाद् वत्यर्थे न भवति — one "
            "sense is kept out, and by a ज्ञापक read off a rule two "
            "chapters later",
    }
    return Affix(gives, sutra, WHY[sutra], excepts=excepts)


def elision(*, of: str = "", gotra: bool = False, before_ac: bool = False,
            apatya: bool = False, yuvan: bool = False) -> Elided:
    """
    4.1.88–91 — where a taddhita would have come and does not show.

    **This is the machinery that lets a form be derived and then not
    appear.** पञ्चकपालः is *prepared in five bowls*: the affix that
    said so is given and then elided, and the word that remains has a
    meaning no part of it carries.

    4.1.88 द्विगोर्लुगनपत्ये elides it after a numeral compound, but
    not a patronymic: द्वैदेवदत्तिः keeps its affix. The vṛtti works
    hard at what द्विगोः names — ननु च प्रत्ययादर्शनस्यैषा संज्ञा?
    उपचारेण तु लक्षणया द्विगुनिमित्तभूतः प्रत्यय एव द्विगुः — the
    affix CAUSED by a द्विगु is called द्विगु by transfer, and that
    is what is elided. And a form that looks the same is kept out by
    asking what caused what: पाञ्चकपालम् survives because न तस्य
    द्विगुत्वं निमित्तम्.

    4.1.89 गोत्रेऽलुगचि stops the elision before a vowel-initial
    affix — गार्गीयाः — and 4.1.90 यूनि लुक् elides the young-
    descendant affix **before it has been formed**: बुद्धिस्थेऽनुत्पन्न
    एव युवप्रत्ययस्य लुग् भवति, तस्मिन्निवृत्ते सति यो यतः प्राप्नोति
    स ततो भवति. An elision applied to something merely intended.

    4.1.91 फक्फिञोरन्यतरस्याम् makes that optional for two affixes,
    which is why both गार्गीयाः and गार्ग्यायणीयाः stand.
    """
    if yuvan and before_ac:
        if of in ("phak", "phiñ"):
            return Elided(
                True, "4.1.91",
                "फक्फिञोरन्यतरस्याम् — पूर्वसूत्रेण नित्ये लुकि "
                "प्राप्ते विकल्प उच्यते. Both stand: गार्गीयाः and "
                "गार्ग्यायणीयाः, वात्सीयाः and वात्स्यायनीयाः; "
                "यास्कीयाः and यास्कायनीयाः",
                optional=True)
        return Elided(
            True, "4.1.90",
            "यूनि लुक् — and the elision reaches the affix BEFORE IT "
            "IS FORMED. प्राग्दीव्यतीयेऽजादौ प्रत्यये विवक्षिते "
            "**बुद्धिस्थेऽनुत्पन्न एव** युवप्रत्ययस्य लुग् भवति, "
            "तस्मिन्निवृत्ते सति यो यतः प्राप्नोति स ततो भवति: what "
            "is elided is something merely INTENDED, and once it is "
            "gone whatever else would have applied applies. "
            "फाण्टाहृतिः, फाण्टाहृतः")
    if gotra and before_ac:
        return Elided(
            False, "4.1.89",
            "गोत्रेऽलुगचि — where a गोत्र affix was elided by 2.4.63 "
            "and the like, the elision is REFUSED before a "
            "vowel-initial affix: गार्गीयाः, वात्सीयाः, आत्रेयीयाः, "
            "खारपायणीयाः. अचीति किम्? गर्गरूप्यम्, गर्गमयम्. गोत्र "
            "इति किम्? कौवलम्, बादरम्")
    if apatya:
        return Elided(
            False, "4.1.88",
            "अनपत्ये — a patronymic keeps its affix: द्वैदेवदत्तिः, "
            "त्रैदेवदत्तिः. The one thing 4.1.88 does not reach")
    return Elided(
        True, "4.1.88",
        "द्विगोर्लुगनपत्ये — after a numeral compound the taddhita "
        "is ELIDED: पञ्चसु कपालेषु संस्कृतः पञ्चकपालः, दशकपालः; "
        "द्वौ वेदावधीते द्विवेदः.\n\n"
        "**This is the machinery that lets a form be derived and then "
        "not appear.** The word that remains means *prepared in five "
        "bowls* and no part of it carries that meaning.\n\n"
        "AND द्विगोः IS READ AS NAMING THE AFFIX, NOT THE COMPOUND. "
        "ननु च प्रत्ययादर्शनस्यैषा संज्ञा? सत्यमेतत्. उपचारेण तु "
        "लक्षणया द्विगुनिमित्तभूतः प्रत्यय एव द्विगुः, तस्य लुग् "
        "भवति — the affix CAUSED by a द्विगु is itself called द्विगु "
        "by transfer. A form that looks the same is then kept out by "
        "asking what caused what: पाञ्चकपालम् stands because "
        "न तस्य द्विगुत्वं निमित्तम्, इतरस्तु द्विगुत्वस्यैव "
        "निमित्तम्.\n\n"
        "प्राग् दीव्यत इत्येव — द्वैपारायणिकः. And वेत्यनुवर्तते, "
        "सा च व्यवस्थितविभाषा विज्ञायते: 4.1.82's option runs down "
        "here too, read as distributed, which is how पञ्चगर्गरूप्यम् "
        "keeps its affix")
