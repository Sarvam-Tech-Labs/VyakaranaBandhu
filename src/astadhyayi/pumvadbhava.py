# -*- coding: utf-8 -*-
"""
६.३.३४–४५ — पुंवद्भाव: a feminine stem wearing the masculine's shape.

दर्शनीया भार्या यस्य — the man whose wife is good-looking — comes
out दर्शनीयभार्यः and not *दर्शनीयाभार्यः. The feminine ending is
not deleted and not replaced: the whole word simply takes **the form
the masculine would have had**, and 6.3.34 says so in those words —
**तस्य भाषितपुंस्कादनूङः स्त्रीशब्दस्य पुंशब्दस्येव रूपं भवति**.

**WHICH FEMININE, THOUGH.** Not every one. 6.3.34's condition is one
bahuvrīhi, and the Kāśikā unpacks it twice before using it:
**भाषितः पुमान् येन समानायाम् आकृताव् एकस्मिन् प्रवृत्तिनिमित्ते स
भाषितपुंस्कः शब्दः**, and then **ऊङोऽभावोऽनूङ्, भाषितपुंस्काद् अनूङ्
यस्मिन् स्त्रीशब्दे, स भाषितपुंस्कादनूङ् स्त्रीशब्दः। बहुव्रीहिरयम्**.
So: a feminine whose masculine exists in the SAME shape and the SAME
sense, and which does not owe its femininity to ऊङ्. खट्वा has no
masculine खट्व in that sense — खट्वाभार्यः. ब्रह्मबन्धू ends in ऊङ्
— ब्रह्मबन्धूभार्यः. Neither is reached.

**AND FIVE RULES REFUSE IT AND ONE RULE UNDOES ALL FIVE.**
6.3.37–41 take it away — for a stem with क before the ending, for a
name, for an ordinal, for a taddhita that caused a vṛddhi, for an
ई after a body-part, for a class-word. Then 6.3.42 पुंवत्
कर्मधारयजातीयदेशीयेषु gives every one of them back in three
environments, and its vṛtti walks the five one at a time:
**न कोपधायाः इत्युक्तम्, तत्रापि भवति — पाचकवृन्दारिका**, and so on
through all five. A rule whose entire content is the undoing of its
five predecessors.

**AND THEN THE STEM IS SHORTENED INSTEAD.** 6.3.43–45 do something
different to the same feminine: before घ and seven named second
members, a ङी-ending stem of more than one vowel goes SHORT —
ब्राह्मणितरा, not *ब्राह्मणीतरा. Where both could apply the vṛtti
settles it: **पुंवद्भावाद् ह्रस्वत्वं खिद्घादिकेषु भवति
विप्रतिषेधेन**.

**WHAT THIS MODULE DOES NOT DO.** It reports whether the feminine
takes the masculine's shape, or is shortened, and by which rule. It
does not build the masculine: what दर्शनीया's masculine looks like
is a question for the affix that made it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where these twelve stand, between the द्वन्द्व substitutions and
#: 6.3.46's महत् → महा.
PUMVAT_RUN: Tuple[str, str] = ("6.3.34", "6.3.45")

#: 6.3.35 names its affixes by the stretch of sūtras that ordains
#: them — **पञ्चम्यास्तसिल् इत्यतः प्रभृति संख्यायाः
#: क्रियाभ्यावृत्तिगणने कृत्वसुच् इति प्राग् एतस्माद् ये
#: प्रत्ययाः** — so the bound is a pair of sūtra numbers and not a
#: list. The list is a vārttika's: **तसिलादिषु परिगणनं कर्तव्यम्**.
TASILADI_RUN: Tuple[str, str] = ("5.3.7", "5.4.17")

#: And that परिगणन, read off the vṛtti in its own order.
TASILADI: Tuple[str, ...] = (
    "tral", "tasi", "tarap", "tamap", "caraṭ", "jātīyar", "kalpap",
    "deśya", "deśīyar", "rūpap", "pāśap", "thamu", "thāl", "dā",
    "rhil", "til", "tātil")

#: The eight of 6.3.43. The first three are affixes and the rest are
#: second members: **घरूपकल्पाः प्रत्ययाश्चेलडादीन्युत्तरपदानि**.
GHADI: Tuple[str, ...] = (
    "gha", "rūpa", "kalpa", "celaṭ", "bruva", "gotra", "mata",
    "hata")

#: The प्रियादि 6.3.34 keeps out, as far as the vṛtti reads them.
PRIYADI: Tuple[str, ...] = ("priyā", "manojñā", "kalyāṇī")

#: The three environments in which 6.3.42 gives everything back.
#: The last two are affixes 6.3.35's stretch already covered —
#: 5.3.69 jātīyar and 5.3.67 deśīyar — so they are named by the
#: same strings here; what 6.3.42 adds for them is not the
#: environment but the classes of stem it lets back in.
KARMADHARAYA_THREE: Tuple[str, ...] = (
    "karmadhāraya", "jātīyar", "deśīyar")

#: And the five classes it lets back in, one per refusing rule.
REFUSED_CLASSES: Tuple[str, ...] = (
    "kopadhā", "saṃjñā", "pūraṇī", "vṛddhi-nimitta-taddhita",
    "svāṅga-īkārānta", "jāti")

#: The five refusals 6.3.42 undoes, in the order its vṛtti walks
#: them: **न कोपधायाः इत्युक्तम्, तत्रापि भवति...**
UNDONE_BY_6_3_42: Tuple[str, ...] = (
    "6.3.37", "6.3.38", "6.3.39", "6.3.40", "6.3.41")


@dataclass(frozen=True)
class Pumvat:
    """One rule of 6.3.34–45: what the feminine stem does."""

    sutra: str
    #: puṃvat — it takes the masculine's shape; hrasva — its final
    #: goes short.
    does: str = ""
    #: The kinds of feminine stem the rule is about.
    stem: Tuple[str, ...] = ()
    #: What must FOLLOW — an affix or a second member.
    before: Tuple[str, ...] = ()
    #: The further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


PUMVAT_TABLE: Tuple[Pumvat, ...] = (
    Pumvat(
        "6.3.34", does="puṃvat", stem=("bhāṣitapuṃska-anūṅ",),
        result=("samānādhikaraṇa",),
        excludes=("pūraṇī",) + PRIYADI,
        keeps_out="ग्रामणिदृष्टिः — no feminine stem at all; "
                  "खट्वाभार्यः — खट्वा has no masculine of the same "
                  "form and sense; द्रोणीभार्यः — not the same "
                  "shape; ब्रह्मबन्धूभार्यः — the femininity is "
                  "ऊङ्'s; कल्याणीमाता — a genitive and not an "
                  "apposition; कल्याणीप्रधानाः — the second member "
                  "is not feminine; कल्याणीपञ्चमाः — an ordinal; "
                  "कल्याणीप्रियः — one of the प्रियादि",
        why="स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे "
            "स्त्रियामपूरणीप्रियादिषु — a feminine stem takes the "
            "MASCULINE'S SHAPE before an appositional feminine "
            "second member: **दर्शनीयभार्यः, श्लक्ष्णचूडः, "
            "दीर्घजङ्घः** — the man whose wife is good-looking, "
            "whose crest is smooth, whose shanks are long.\\n\\n"
            "**AND THE CONDITION IS ONE COMPOUND, UNPACKED TWICE "
            "BEFORE USE.** **भाषितः पुमान् येन समानायाम् आकृताव् "
            "एकस्मिन् प्रवृत्तिनिमित्ते स भाषितपुंस्कः शब्दः** — a "
            "word whose masculine is spoken with the SAME form and "
            "the SAME ground of application. Then **ऊङोऽभावोऽनूङ्, "
            "भाषितपुंस्काद् अनूङ् यस्मिन् स्त्रीशब्दे, स "
            "भाषितपुंस्कादनूङ् स्त्रीशब्दः। बहुव्रीहिरयम्, अलुग्। "
            "निपातनात् पञ्चम्याः** — and even the ablative in the "
            "sūtra is there by निपातन.\\n\\n"
            "**AND WHAT IT DOES IS NOT A DELETION.** **तस्य "
            "भाषितपुंस्कादनूङः स्त्रीशब्दस्य पुंशब्दस्येव रूपं "
            "भवति** — the word takes the form the masculine WOULD "
            "have had. Nothing is dropped and nothing replaced; "
            "one word is told to look like another.\\n\\n"
            "**AND A VĀRTTIKA TIGHTENS TWO OF THE EXCEPTIONS.** "
            "**प्रधानपूरणीग्रहणं कर्तव्यम् — इह मा भूत् "
            "कल्याणपञ्चमीकः पक्ष इति** — the ordinal excepted is "
            "the PRINCIPAL one, and the vṛtti carries the same "
            "reading into 5.4.116"),
    Pumvat(
        "6.3.35", does="puṃvat", stem=("bhāṣitapuṃska-anūṅ",),
        before=TASILADI,
        why="तसिलादिष्वा कृत्वसुचः — and before the affixes from "
            "5.3.7 तसिल् as far as 5.4.17 कृत्वसुच्: **तस्याः "
            "शालायास्ततः; तस्यां तत्र; यस्या यतः; यस्यां यत्र** — "
            "the feminine is there in the analysis and gone from "
            "the form.\\n\\n"
            "**AND THE STRETCH HAS TO BE COUNTED OUT BY HAND.** "
            "**तसिलादिषु परिगणनं कर्तव्यम्** — a bound given as "
            "*from here to there* leaves it unclear which affixes "
            "of the stretch are meant, so a vārttika lists them: "
            "**त्रतसौ। तरप्तमपौ। चरट्जातीयरौ। कल्पब्देश्यदेशीयरः। "
            "रूपप्पाशपौ। थम्थालौ। दार्हिलौ। तिल्तातिलौ**.\\n\\n"
            "**AND FOUR MORE VĀRTTIKAS ADD FOUR MORE PLACES.** "
            "**शसि बह्वल्पार्थस्य — बहुशो देहि, अल्पशो देहि**; "
            "**त्वतलोर्गुणवचनस्य — पटुत्वम्, पटुता**, but only for "
            "a quality-word: **गुणवचनस्येति किम्? कठीत्वम्, "
            "कठीता**; **भस्याढे तद्धिते — हास्तिकम्**, and not "
            "before a ढ: **श्यैनेयः, रौहिणेयः**; and "
            "**ठक्छसोश्च — भावत्काः**"),
    Pumvat(
        "6.3.36", does="puṃvat", stem=("bhāṣitapuṃska-anūṅ",),
        before=("kyaṅ", "mānin"),
        why="क्यङ्मानिनोश्च — and before क्यङ् and मानिन्: "
            "**एनी — एतायते; श्येनी — श्येतायते**; and "
            "**दर्शनीयमानी अयमस्याः, दर्शनीयमानिनीयमस्याः**.\\n\\n"
            "**AND मानिन् IS NAMED FOR TWO CASES 6.3.34 COULD NOT "
            "REACH.** **मानिनो ग्रहणम् अस्त्र्यर्थम् "
            "असमानाधिकरणार्थं च** — where the whole word is not "
            "feminine, and where the two members are not in "
            "apposition. **इह तु दर्शनीयाम् आत्मानं मन्यते "
            "दर्शनीयमानिनीति पूर्वेणैव सिद्धम्** — the appositional "
            "feminine case 6.3.34 had already"),
    Pumvat(
        "6.3.37", refuses=True, stem=("kopadhā",),
        blocks=("6.3.34",),
        keeps_out="पाकभार्यः, भेकभार्यः — the क is part of the "
                  "stem and not a वुक्",
        why="न कोपधायाः — but not where the feminine has a क "
            "before its ending: **पाचिकाभार्यः, कारिकाभार्यः, "
            "मद्रिकाभार्यः, वृजिकाभार्यः**, and the same through "
            "every environment the earlier rules gave — "
            "**मद्रिकाकल्पा, मद्रिकायते, मद्रिकामानिनी, "
            "वैलेपिकम्**.\\n\\n"
            "**AND A VĀRTTIKA SAYS WHICH क IS MEANT.** "
            "**कोपधप्रतिषेधे तद्धितवुग्रहणं कर्तव्यम्। इह मा भूत् "
            "— पाकभार्यः, भेकभार्य इति** — the क put there by the "
            "taddhita वुक्, not any क that happens to stand before "
            "the ending"),
    Pumvat(
        "6.3.38", refuses=True, stem=("saṃjñā", "pūraṇī"),
        blocks=("6.3.34",),
        why="संज्ञापूरण्योश्च — nor where the feminine is a NAME "
            "or an ORDINAL: **दत्ताभार्यः, गुप्ताभार्यः, "
            "दत्तापाशा, दत्तायते, दत्तामानिनी**; **पञ्चमीभार्यः, "
            "दशमीभार्यः, पञ्चमीपाशा, पञ्चमीयते, पञ्चमीमानिनी**. "
            "The ordinal was already excepted by 6.3.34's own "
            "words in the appositional case; here it is refused "
            "across the rest"),
    Pumvat(
        "6.3.39", refuses=True, stem=("vṛddhi-nimitta-taddhita",),
        excludes=("rakta", "vikāra"), blocks=("6.3.34",),
        keeps_out="मध्यमभार्यः — nothing caused a वृद्धि; "
                  "काण्डलावभार्यः — no taddhita; काषायी बृहतिका — "
                  "the taddhita is laid down for a DYE, which the "
                  "sūtra excepts",
        why="वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे — nor where "
            "the feminine ends in a taddhita that CAUSED a वृद्धि, "
            "unless that taddhita was laid down for a dye or a "
            "modification: **स्रौघ्नीभार्यः, माथुरीभार्यः, "
            "स्रौघ्नीपाशा, स्रौघ्नीयते, स्रौघ्नीमानिनी**.\\n\\n"
            "**AND THE बहुव्रीहि READING IS WHAT LETS IT REACH A "
            "WHOLE WORD.** **बहुव्रीहिपरिग्रहः किमर्थम्? "
            "तावद्भार्यः, यावद्भार्यः** — read as *one whose "
            "taddhita caused a वृद्धि* the rule reaches the stem "
            "that merely ENDS in such a taddhita, which is what "
            "these two need"),
    Pumvat(
        "6.3.40", refuses=True, stem=("svāṅga-īkārānta",),
        excludes=("mānin",), blocks=("6.3.34",),
        keeps_out="पटुभार्यः — पटु is no part of the body; "
                  "अकेशभार्यः — no ई after it; दीर्घकेशमानिनी — "
                  "before मानिन्, which the sūtra excepts",
        why="स्वाङ्गाच्चेतोऽमानिनि — nor where an ई follows a word "
            "for a PART OF THE BODY, except before मानिन्: "
            "**दीर्घकेशीभार्यः, श्लक्ष्णकेशीभार्यः, "
            "दीर्घकेशीपाशा, दीर्घकेशीयते**"),
    Pumvat(
        "6.3.41", refuses=True, stem=("jāti",),
        excludes=("mānin",), blocks=("6.3.34",),
        keeps_out="कठमानिनी, बह्वृचमानिनी — before मानिन्, still "
                  "excepted",
        why="जातेश्च — nor where the feminine names a CLASS, again "
            "except before मानिन्: **कठीभार्यः, बह्वृचीभार्यः, "
            "कठीपाशा, कठीयते**.\\n\\n"
            "**AND THE REFUSAL DOES NOT REACH WHAT A VĀRTTIKA "
            "SUPPLIED.** **अयं प्रतिषेध औपसंख्यानिकस्य "
            "पुंवद्भावस्य नेष्यते। हस्तिनीनां समूहो हास्तिकम्** — "
            "हस्तिनी names a class, and the पुंवद्भाव in हास्तिकम् "
            "comes from 6.3.35's vārttika **भस्याढे तद्धिते**, not "
            "from a sūtra, so this refusal does not touch it"),
    Pumvat(
        "6.3.42", does="puṃvat", stem=REFUSED_CLASSES,
        before=KARMADHARAYA_THREE, blocks=UNDONE_BY_6_3_42,
        keeps_out="खट्वावृन्दारिका — no masculine of the same form; "
                  "ब्रह्मबन्धूवृन्दारिका — the femininity is ऊङ्'s",
        why="पुंवत् कर्मधारयजातीयदेशीयेषु — in a कर्मधारय, and "
            "before जातीय and देशीय, the feminine takes the "
            "masculine's shape after all. **प्रतिषेधार्थोऽयम् "
            "आरम्भः** — the rule exists for the refusals, and the "
            "vṛtti walks all five: **न कोपधायाः इत्युक्तम्, "
            "तत्रापि भवति — पाचकवृन्दारिका, पाचकजातीया, "
            "पाचकदेशीया; संज्ञापूरण्योश्च इत्युक्तम्, तत्रापि भवति "
            "— दत्तवृन्दारिका, पञ्चमवृन्दारिका; वृद्धिनिमित्तस्य च "
            "तद्धितस्यारक्तविकारे इत्युक्तम्, तत्रापि भवति — "
            "स्रौघ्नवृन्दारिका; स्वाङ्गाच्चेतोऽमानिनि इत्युक्तम्, "
            "तत्रापि भवति — श्लक्ष्णमुखवृन्दारिका; जातेश्च "
            "इत्युक्तम्, तत्रापि भवति — कठवृन्दारिका**.\\n\\n"
            "**BUT 6.3.34'S OWN TWO CONDITIONS STILL HOLD.** "
            "**भाषितपुंस्कादित्येव — खट्वावृन्दारिका। अनूङित्येव — "
            "ब्रह्मबन्धूवृन्दारिका** — undoing five refusals is not "
            "the same as widening the rule they refused.\\n\\n"
            "**AND WHERE THE SHORTENING COULD ALSO APPLY, IT "
            "WINS.** **पुंवद्भावाद् ह्रस्वत्वं खिद्घादिकेषु भवति "
            "विप्रतिषेधेन — कालिंमन्या; पाट्वितरा, पट्वितमा**. A "
            "vārttika adds one more class: **कुक्कुट्यादीनाम् "
            "अण्डादिषु पुंवद्भावो वक्तव्यः — कुक्कुटाण्डम्, "
            "मृगपदम्, काकशावः**"),
    Pumvat(
        "6.3.43", does="hrasva", stem=("ṅī-anta-anekāc",),
        before=GHADI,
        keeps_out="दत्तातरा, गुप्तातरा — the ending is not ङी; "
                  "आमलकीतरा, कुवलीतरा — no masculine of the same "
                  "form and sense",
        why="घरूपकल्पचेलड्ब्रुवगोत्रमतहतेषु ङ्योऽनेकाचो ह्रस्वः — "
            "before eight things, a ङी-ending feminine of more "
            "than one vowel goes SHORT: **ब्राह्मणितरा, "
            "ब्राह्मणितमा** (घ), **ब्राह्मणिरूपा, ब्राह्मणिकल्पा, "
            "ब्राह्मणिचेली, ब्राह्मणिब्रुवा, ब्राह्मणिगोत्रा, "
            "ब्राह्मणिमता, ब्राह्मणिहता**.\\n\\n"
            "**AND THE EIGHT ARE NOT ALL OF ONE KIND.** "
            "**घरूपकल्पाः प्रत्ययाश्चेलडादीन्युत्तरपदानि** — the "
            "first three are affixes and the last five are second "
            "members. And ब्रुव is explained: **ब्रुवीतीति ब्रुवः "
            "पचाद्यचि वच्यादेशो गुणश्च निपातनाद् न भवति**"),
    Pumvat(
        "6.3.44", does="hrasva", stem=("nadī-śeṣa",), before=GHADI,
        optional=True,
        keeps_out="लक्ष्मीतरा, तन्त्रीतरा — the vārttika "
                  "**कृन्नद्याः प्रतिषेधो वक्तव्यः**",
        why="नद्याः शेषस्यान्यतरस्याम् — and what 6.3.43 left of "
            "नदी goes short OPTIONALLY: **ब्रह्मबन्धूतरा / "
            "ब्रह्मबन्धुतरा; वीरबन्धूतरा / वीरबन्धुतरा; स्त्रितरा "
            "/ स्त्रीतरा**.\\n\\n"
            "**AND THE VṚTTI SAYS WHAT THE REMAINDER IS.** "
            "**कश्च शेषः? अङी च या नदी, ङ्यन्तं च यदेकाच्** — the "
            "नदी that has no ङी, and the ङी-ending word that has "
            "only one vowel. Exactly the two things 6.3.43's "
            "ङ्यः and अनेकाचः had between them left out"),
    Pumvat(
        "6.3.45", does="hrasva", stem=("ugit",), before=GHADI,
        optional=True,
        why="उगितश्च — and a नदी after a उगित् stem goes short "
            "optionally: **श्रेयसितरा / श्रेयसीतरा / श्रेयस्तरा; "
            "विदुषितरा / विदुषीतरा / विद्वत्तरा** — three forms, "
            "not two.\\n\\n"
            "**AND THE THIRD OF THE THREE IS NOT THIS RULE'S.** "
            "**पुंवद्भावोऽप्यत्र पक्षे वक्तव्यः। प्रकर्षयोगात् "
            "प्राक् स्त्रीत्वस्याविवक्षितत्वाद् वा सिद्धम्** — "
            "श्रेयस्तरा is the masculine's shape, either by a "
            "vārttika supplying पुंवद्भाव here as well, or because "
            "the femininity was never meant in the first place, "
            "the word being under comparison"),
)


def _reaches(row: Pumvat, stem: str, before: str,
             result: str) -> bool:
    if row.stem and stem not in row.stem:
        return False
    if row.before and before not in row.before:
        return False
    if row.result and result not in row.result:
        return False
    if row.excludes and (before in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Pumvat, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.does and not row.refuses


def _how_specific(row: Pumvat, stem: str, before: str) -> int:
    """
    A rule that names what it displaces outranks it, and by as many
    rules as it names.

    That is what 6.3.42 needs. By conditions alone it is no sharper
    than the five refusals it undoes — it names an environment and
    they name a kind of stem — but its whole content is that it
    beats them, and the vṛtti proves it by walking all five. So
    `blocks` is weighed, and weighed by length.
    """
    return (
        4 * len(row.blocks)
        + 10 * bool(row.refuses)
        + 8 * bool(row.before and before in row.before)
        + 5 * bool(row.stem and stem in row.stem)
        + 4 * bool(row.result)
    )


@dataclass(frozen=True)
class Behaves:
    """What the run answers: what the feminine stem does."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def behaves_as(stem: str = "", *, before: str = "",
               result: str = "", wants: str = "") -> Behaves:
    """
    6.3.34–45 — whether the feminine takes the masculine's shape.

    Nothing answers by default: where no rule is reached the
    feminine stands as a feminine, which is what दर्शनीयाभार्यः
    would have been.
    """
    matched = [
        row for row in PUMVAT_TABLE
        if _reaches(row, stem, before, result)
        and _supplies(row, wants)
    ]
    if not matched:
        return Behaves(
            "", "", "No rule of 6.3.34–45 is reached, so the "
                    "feminine stem stands as it is, with its own "
                    "ending and its own length")
    row = max(matched,
              key=lambda one: _how_specific(one, stem, before))
    return Behaves("" if row.refuses else row.does, row.sutra,
                   row.why, optional=row.optional,
                   blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Pumvat, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in PUMVAT_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Pumvat", "PUMVAT_TABLE", "PUMVAT_RUN", "TASILADI",
    "TASILADI_RUN", "GHADI", "PRIYADI", "KARMADHARAYA_THREE",
    "REFUSED_CLASSES", "UNDONE_BY_6_3_42", "Behaves",
    "behaves_as", "provisions_for",
]
