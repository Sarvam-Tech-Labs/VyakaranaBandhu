# -*- coding: utf-8 -*-
"""
3.1.96 to 3.1.132 — the कृत्य affixes, and the forms fixed among them.

3.1.95 named the section; these are its members. Four affixes do the
work — तव्यत् with तव्य and अनीयर्, then यत्, क्यप् and ण्यत् — and
they stand in a chain of अपवाद, each cutting into the one before:

    3.1.96  तव्यत्तव्यानीयरः      three affixes, after any root
    3.1.97  अचो यत्              यत्, after a vowel
    3.1.98  पोरदुपधात्           and after a labial with अ before it
    3.1.99  शकिसहोश्च            and after two roots
    3.1.100 गदमदचरयमश्चानुपसर्गे  and four more, without a preverb
    3.1.106 वदः सुपि क्यप् च      क्यप् — and यत् too
    3.1.107 भुवो भावे            क्यप्, of the act
    3.1.108 हनस्त च              and with a त
    3.1.109 एतिस्तुशास्वृदृजुषः क्यप्  क्यप् generally, after six roots
    3.1.110 ऋदुपधाच्चाकॢपिचृतेः    and after an ऋ penult, less two
    3.1.111 ई च खनः              and with an ई
    3.1.112 भृञोऽसंज्ञायाम्       and after भृ, not as a name
    3.1.113 मृजेर्विभाषा          optionally after मृज्
    3.1.118 प्रत्यपिभ्यां ग्रहेश्छन्दसि  ग्रह् after two preverbs
    3.1.119 पदास्वैरिबाह्यापक्ष्येषु च  and in four senses
    3.1.120 विभाषा कृवृषोः        optionally after two roots
    3.1.122 अमावस्यदन्यतरस्याम्    ण्यत्, and a vṛddhi left off
    3.1.124 ऋहलोर्ण्यत्           ण्यत्, after ऋ or a consonant
    3.1.125 ओरावश्यके            and after उ, where a thing must be
    3.1.126 आसुयुवपि…श्च          and after seven more

Seventeen other rules of the run fix forms whole rather than adding an
affix, and they are kept apart from the table for that reason — see
:data:`NIPATANA`.

**The chain is stated, not inferred.** 3.1.98 is ण्यतोऽपवादः and
3.1.125 is यतोऽपवादः, so the three affixes cut across each other in
both directions: यत् takes ground from ण्यत् at 3.1.98, and ण्यत्
takes it back from यत् at 3.1.125. The vṛtti says which each time, and
the table follows the text rather than a general ordering.

**3.1.109 repeats क्यप् in order to block a blocker.** क्यबिति
वर्तमाने पुनः क्यब्ग्रहणं बाधकबाधनार्थम् — the word was already
running, and saying it again defeats 3.1.125's ण्यत् where the two
would meet: अवश्यस्तुत्यः, not *अवश्यस्तव्यम्. A rule stated a second
time so that a LATER rule cannot displace it, which is the reverse of
the usual reason for repetition.
"""

from dataclasses import dataclass
from typing import Tuple

# ---------------------------------------------------------------------------
# The lists the sūtras name
# ---------------------------------------------------------------------------

#: 3.1.100's four, which take यत् only without a preverb.
GADADI: Tuple[str, ...] = ("gad", "mad", "car", "yam")

#: 3.1.109's six, which take क्यप् generally.
ETYADI: Tuple[str, ...] = ("i", "stu", "śās", "vṛ", "dṛ", "juṣ")

#: 3.1.110's two exceptions — the rule reaches an ऋ penult EXCEPT these.
NOT_RDUPADHA: Tuple[str, ...] = ("kḷp", "cṛt")

#: 3.1.119's four senses, in which ग्रह् takes क्यप्.
GRAH_SENSES: Tuple[str, ...] = ("pada", "asvairin", "bāhyā", "pakṣya")

#: 3.1.126's seven, beside आ + सु.
YUVADI: Tuple[str, ...] = ("yu", "vap", "rap", "lap", "trap", "cam")

#: What a निपातन rule fixes: the forms, the sense they hold in, and what
#: the vṛtti says is being suspended. यदिह लक्षणेनानुपपन्नं तत् सर्वं
#: निपातनात् सिद्धम् — whatever the rules do not reach, the fixing
#: supplies.
NIPATANA = {
    "3.1.101": (("avadya", "paṇya", "varyā"),
                "गर्ह्य, पणितव्य, अनिरोध — यथासंख्यम्, one sense each: "
                "अवद्यं पापम् but अनुद्यम् अन्यत्; पण्यः कम्बलः but "
                "पाण्यम् अन्यत्; शतेन वर्या but वृत्या अन्या"),
    "3.1.102": (("vahya",),
                "करणे — वहत्यनेनेति वह्यं शकटम्, the cart one carries "
                "by. करण इति किम्? वाह्यम् अन्यत्"),
    "3.1.103": (("arya",),
                "स्वामिन् and वैश्य — अर्यः स्वामी, अर्यो वैश्यः, "
                "where ण्यत् was due. And a vārttika gives the first "
                "sense a final accent. स्वामिवैश्ययोरिति किम्? आर्यो "
                "ब्राह्मणः"),
    "3.1.104": (("upasaryā",),
                "काल्या प्रजने — प्राप्तकाला काल्या, ready in season: "
                "उपसर्या गौः. काल्या प्रजन इति किम्? उपसार्या शरदि "
                "मधुरा"),
    "3.1.105": (("ajarya",),
                "संगत — न जीर्यतीत्यजर्यम्, a friendship that does not "
                "wear out: अजर्यं नोऽस्तु संगतम्. संगतमिति किम्? "
                "अजरिता कम्बलः"),
    "3.1.114": (("rājasūya", "sūrya", "mṛṣodya", "rucya", "kupya",
                 "kṛṣṭapacya", "avyathya"),
                "seven forms fixed under क्यप्, each suspending "
                "something different — a उत्व here, a रुट् augment "
                "there, a कुत्व in a third"),
    "3.1.115": (("bhidya", "uddhya"),
                "नदे — of a river: भिनत्ति कूलं भिद्यः, उज्झत्युदकम् "
                "उद्ध्यः, with a धत्व on the second. नद इति किम्? "
                "भेत्ता, उज्झिता"),
    "3.1.116": (("puṣya", "siddhya"),
                "नक्षत्रे — of a lunar mansion, and in the locative "
                "sense: पुष्यन्त्यस्मिन्नर्थाः. नक्षत्र इति किम्? "
                "पोषणम्, सेधनम्"),
    "3.1.117": (("vipūya", "vinīya", "jitya"),
                "मुञ्ज, कल्क, हलि — यथासंख्यम्, and in the OBJECT "
                "sense where यत् was due: विपूयो मुञ्जः but विपव्यम् "
                "अन्यत्"),
    "3.1.121": (("yugya",),
                "पत्रे — पतत्यनेनेति पत्रम्, a draught animal: युग्यो "
                "गौः, with a कुत्व. पत्र इति किम्? योग्यम् अन्यत्"),
    "3.1.123": (("niṣṭarkya", "devahūya", "praṇīya", "unnīya",
                 "ucchiṣya", "marya", "starya", "adhvarya", "khanya",
                 "khānya", "devayajyā", "āpṛcchya", "pratiṣīvya",
                 "brahmavādya", "bhāvya", "stāvya", "upacāyya", "pṛḍa"),
                "छन्दसि — eighteen Vedic forms at once, and the vṛtti "
                "states the principle rather than deriving them: "
                "यदिह लक्षणेनानुपपन्नं तत् सर्वं निपातनात् सिद्धम्"),
    "3.1.127": (("ānāyya",),
                "अनित्ये — the southern fire, आनाय्यो दक्षिणाग्निः, "
                "with ण्यत् and an आय substitute. रूढिरेषा: the form "
                "is fixed to one fire and not to the kind"),
    "3.1.128": (("praṇāyya",),
                "असंमतौ — प्रणाय्यश्चोरः, one held in no regard. "
                "असंमताविति किम्? प्रणेयोऽन्यः"),
    "3.1.129": (("pāyya", "sānnāyya", "nikāyya", "dhāyya"),
                "मान, हविस्, निवास, सामिधेनी — यथासंख्यम्, four forms "
                "and four senses: पाय्यं मानम् but मेयम् अन्यत्"),
    "3.1.130": (("kuṇḍapāyya", "saṃcāyya"),
                "क्रतौ — of a rite: कुण्डेन पीयतेऽस्मिन् सोम इति "
                "कुण्डपाय्यः, in the locative sense, with a युक्"),
    "3.1.131": (("paricāyya", "upacāyya", "samūhya"),
                "अग्नौ — of a fire, the first two with ण्यत् and an "
                "आय substitute, the third with संप्रसारण and a long "
                "vowel. अग्नाविति किम्? परिचेयम्, उपचेयम्, संवाह्यम्"),
    "3.1.132": (("citya", "agnicityā"),
                "and of a fire likewise — चीयतेऽसौ चित्योऽग्निः, the "
                "second in the भाव sense with a य and a तुक्, which "
                "is what gives it a final accent"),
}


@dataclass(frozen=True)
class Krtya:
    """One rule adding a कृत्य affix, as its conditions."""

    sutra: str
    gives: str
    of: Tuple[str, ...] = ()
    #: A phonological shape the root must have.
    root_ends_in: str = ""
    penult: str = ""
    #: Roots the rule expressly excludes — 3.1.110's two.
    not_of: Tuple[str, ...] = ()
    sense: str = ""
    #: Whether a सुबन्त must stand beside, and a preverb must not.
    upapada: bool = False
    no_upasarga: bool = False
    upasarga: Tuple[str, ...] = ()
    chandas: bool = False
    optional: bool = False
    #: A second affix the same rule gives — 3.1.106's च.
    also: str = ""
    why: str = ""


KRTYA: Tuple[Krtya, ...] = (
    Krtya("3.1.96", "tavyat",
          also="तव्य and अनीयर्",
          why="तव्यत्तव्यानीयरः — कर्तव्यम्, करणीयम्. Three affixes "
              "after any root at all, and every rule after this one "
              "cuts into its ground. तकाररेफौ स्वरार्थौ, the त् and "
              "र् for the accent. A vārttika adds केलिमर: पचेलिमा "
              "माषाः, भिदेलिमानि काष्ठानि"),
    Krtya("3.1.97", "yat", root_ends_in="ac",
          why="अचो यत् — गेयम्, पेयम्, चेयम्, जेयम्. And the vṛtti "
              "asks why अच् is said when 3.1.124 will give ण्यत् to "
              "consonant-final roots anyway, and answers: "
              "अजन्तभूतपूर्वादपि यथा स्यात् — so that a root which "
              "USED to end in a vowel is reached too, दित्स्यम्, "
              "धित्स्यम्"),
    Krtya("3.1.98", "yat", root_ends_in="pu", penult="a",
          why="पोरदुपधात् — शप्यम्, लभ्यम्. ण्यतोऽपवादः: यत् taking "
              "ground back from 3.1.124. पोरिति किम्? पाक्यम्, "
              "वाक्यम्. अदुपधादिति किम्? कोप्यम्, गोप्यम्. And "
              "तपरकरणं तत्कालार्थम् — the अ is short and only a short "
              "one counts: आप्यम्"),
    Krtya("3.1.99", "yat", of=("śak", "sah"),
          why="शकिसहोश्च — शक्यम्, सह्यम्. Both end in consonants and "
              "would have taken ण्यत्, so this is the same अपवाद "
              "again, by name rather than by shape"),
    Krtya("3.1.100", "yat", of=GADADI, no_upasarga=True,
          why="गदमदचरयमश्चानुपसर्गे — गद्यम्, मद्यम्, चर्यम्, यम्यम्. "
              "अनुपसर्ग इति किम्? प्रगाद्यम्, प्रमाद्यम्. And यम् was "
              "reachable already — यमेः पूर्वेणैव सिद्धे "
              "अनुपसर्गनियमार्थं वचनम्: it is named to be RESTRICTED, "
              "not to be given. A vārttika adds चर् with आ, of a "
              "place but not a teacher: आचर्यो देशः, but आचार्य "
              "उपनेता"),
    Krtya("3.1.106", "kyap", of=("vad",), upapada=True,
          no_upasarga=True, also="यत्",
          why="वदः सुपि क्यप् च — ब्रह्मोद्यम् beside ब्रह्मवद्यम्, "
              "सत्योद्यम् beside सत्यवद्यम्. The च gives यत् as well, "
              "so both forms stand. सुपीति किम्? वाद्यम्. "
              "अनुपसर्ग इत्येव: प्रवाद्यम्"),
    Krtya("3.1.107", "kyap", of=("bhū",), upapada=True,
          no_upasarga=True, sense="bhāva",
          why="भुवो भावे — ब्रह्मभूयं गतः, देवभूयं गतः. यत् तु "
              "नानुवर्तते: the यत् 3.1.106 added does NOT carry down, "
              "so only क्यप् here. भावग्रहणम् उत्तरार्थम् — the word "
              "भावे is stated for the rule after this one"),
    Krtya("3.1.108", "kyap", of=("han",), upapada=True,
          no_upasarga=True, sense="bhāva", also="a त is put at the end",
          why="हनस्त च — ब्रह्महत्या, अश्वहत्या. सुपीत्येव: घातः. And "
              "the vṛtti notes why ण्यत् does not step in — ण्यत् तु "
              "भावे न भवति अनभिधानात्, because usage does not have it, "
              "which is a reason of a different kind from the rest"),
    Krtya("3.1.109", "kyap", of=ETYADI,
          why="एतिस्तुशास्वृदृजुषः क्यप् — इत्यः, स्तुत्यः, शिष्यः, "
              "वृत्यः, आदृत्यः, जुष्यः. सुप्यनुपसर्गे भावे इति "
              "निवृत्तम्: those three conditions stop here, "
              "सामान्येन विधानम् एतत्. And क्यप् is said AGAIN though "
              "it was running — क्यबिति वर्तमाने पुनः क्यब्ग्रहणं "
              "बाधकबाधनार्थम्, to defeat 3.1.125's ण्यत् where the two "
              "meet: अवश्यस्तुत्यः. वृग्रहणे वृञो ग्रहणम् इष्यते, न "
              "वृङः"),
    Krtya("3.1.110", "kyap", penult="ṛ", not_of=NOT_RDUPADHA,
          why="ऋदुपधाच्चाकॢपिचृतेः — वृत्यम्, वृध्यम्. "
              "अक्ऌपिचृतेरिति किम्? कल्प्यम्, चर्त्यम्. And "
              "तपरकरणम् keeps it to the SHORT ऋ: कीर्त्यम् from कृत् "
              "takes ण्यत् instead"),
    Krtya("3.1.111", "kyap", of=("khan",), also="an ई is put at the end",
          why="ई च खनः — खेयम्. दीर्घनिर्देशः प्रश्लेषार्थः: the ई is "
              "written long so that two are read in it, and the second "
              "blocks 6.4.43's आ — a long vowel in a sūtra standing "
              "for two, in order to stop a later rule"),
    Krtya("3.1.112", "kyap", of=("bhṛ",), sense="not-a-name",
          why="भृञोऽसंज्ञायाम् — भृत्याः कर्मकराः, those to be "
              "maintained. असंज्ञायामिति किम्? भार्यो नाम क्षत्रियः. "
              "A vārttika makes it optional with सम्: संभृत्याः beside "
              "संभार्याः"),
    Krtya("3.1.113", "kyap", of=("mṛj",), optional=True,
          why="मृजेर्विभाषा — परिमृज्यः beside परिमार्ग्यः. "
              "ऋदुपधत्वात् प्राप्तविभाषेयम्: 3.1.110 had already "
              "reached it by its ऋ penult, so this is an option laid "
              "over something already available"),
    Krtya("3.1.118", "kyap", of=("grah",), upasarga=("prati", "api"),
          chandas=True,
          why="प्रत्यपिभ्यां ग्रहेश्छन्दसि — प्रतिगृह्यम्, अपिगृह्यम्. "
              "छन्दसीति किम्? प्रतिग्राह्यम्, अपिग्राह्यम्"),
    Krtya("3.1.119", "kyap", of=("grah",), sense="grah-four",
          why="पदास्वैरिबाह्यापक्ष्येषु च — प्रगृह्यं पदम्, गृह्यका "
              "इमे, ग्रामगृह्या सेना. Four senses, and the vṛtti "
              "glosses each: अस्वैरी परतन्त्रः, बाह्या is what lies "
              "outside a village or town. स्त्रीलिङ्गनिर्देशाद् "
              "अन्यत्र न भवति — the feminine wording confines one of "
              "them"),
    Krtya("3.1.120", "kyap", of=("kṛ", "vṛṣ"), optional=True,
          why="विभाषा कृवृषोः — कृत्यम् beside कार्यम्, वृष्यम् beside "
              "वर्ष्यम्. And the two are reached from opposite sides: "
              "करोतेर्ण्यति प्राप्ते, वर्षतेर् ऋदुपधत्वाद् नित्ये "
              "क्यपि प्राप्ते — for कृ the option opens against ण्यत्, "
              "for वृष् against an obligatory क्यप्"),
    Krtya("3.1.122", "ṇyat", of=("vas",), upapada=True, optional=True,
          also="the vṛddhi is optionally left off",
          why="अमावस्यदन्यतरस्याम् — सह वसतोऽस्मिन् काले "
              "सूर्यचन्द्रमसौ: अमावास्या beside अमावस्या, the new-moon "
              "day. अमा means 'together'. The option is not about the "
              "affix but about the STRENGTHENING, which is what "
              "अन्यतरस्याम् reaches"),
    Krtya("3.1.124", "ṇyat", root_ends_in="ṛ-or-hal",
          why="ऋहलोर्ण्यत् — कार्यम्, हार्यम्, धार्यम्; वाक्यम्, "
              "पाक्यम्. पञ्चम्यर्थे षष्ठी, the genitive read as an "
              "ablative: after a root ending in ऋ or in a consonant"),
    Krtya("3.1.125", "ṇyat", root_ends_in="u", sense="āvaśyaka",
          why="ओरावश्यके — लाव्यम्, पाव्यम्. यतोऽपवादः, ण्यत् taking "
              "ground back from 3.1.97. आवश्यक इति किम्? लव्यम्. "
              "अवश्यंभाव आवश्यकम् — what must be done. The vṛtti "
              "raises an objection about the accent of अवश्यलाव्यम् "
              "and answers it from 2.1.72's मयूरव्यंसकादि"),
    Krtya("3.1.126", "ṇyat", of=YUVADI,
          why="आसुयुवपिरपिलपित्रपिचमश्च — आसाव्यम् from आ + सु, then "
              "याव्यम्, वाप्यम्, राप्यम्, लाप्यम्, त्राप्यम्, "
              "आचाम्यम्. यतोऽपवादः again. अनुक्तसमुच्चयार्थश्चकारः, "
              "and the vṛtti adds दभ् on that च: दाभ्यम्"),
)


@dataclass(frozen=True)
class Added:
    """A कृत्य affix put after the root, and by which rule."""

    gives: str
    by: str
    why: str
    optional: bool = False
    also: str = ""


@dataclass(frozen=True)
class NotAdded:
    """That no rule of this run reaches it."""

    by: str
    why: str
    gives: str = ""


def krtya_affix(
    root: str = "",
    *,
    root_ends_in: str = "",
    penult: str = "",
    sense: str = "",
    upapada: bool = False,
    upasarga: str = "",
    chandas: bool = False,
) -> object:
    """
    Which कृत्य affix a root takes — 3.1.96 to 3.1.126.

    The MORE SPECIFIC rule answers, and the text's own order breaks a
    tie. The three affixes cut into each other in both directions —
    3.1.98 is ण्यतोऽपवादः and 3.1.125 is यतोऽपवादः — so neither a
    first-match nor a last-match walk gives the text's own answers.
    """
    # Both of these can be READ off the root, and both are decided by
    # rules already codified — the śivasūtras for which pratyāhāra a
    # final belongs to, and 1.1.65 अलोऽन्त्यात्पूर्व उपधा for the
    # penultimate. Where a root is given they are asked; the bare
    # tokens stay accepted so a rule can still be tried in the
    # abstract, without a root in hand.
    root_ends_in = root_ends_in or _final_of(root)
    penult = penult or _penult_of(root)
    matched = [row for row in KRTYA
               if _reaches(row, root, root_ends_in, penult, sense, upapada,
                           upasarga, chandas)]
    if not matched:
        return NotAdded(
            "",
            f"No rule of 3.1.96 to 3.1.126 reaches {root or 'this root'} "
            f"here. 3.1.96 तव्यत्तव्यानीयरः is the one that holds for "
            f"any root at all, and it wants nothing said of the root",
        )
    best = max(matched, key=_how_specific)
    return Added(best.gives, best.sutra, best.why,
                 optional=best.optional, also=best.also)


def _how_specific(row: Krtya) -> int:
    """
    How much a row says. 3.1.109's repeated क्यप् counts for more than
    its conditions warrant, because the repetition is there precisely
    to beat a rule that would otherwise win — बाधकबाधनार्थम्.
    """
    # Naming a ROOT outweighs naming a shape, and the vṛtti says why
    # twice over: यम् is named at 3.1.100 अनुपसर्गनियमार्थम् and मृज्
    # at 3.1.113 प्राप्तविभाषेयम् — in both cases BECAUSE a shape rule
    # had already reached them. A rule written to qualify what another
    # already gave has to answer over it, or the qualification is lost.
    stated = (
        3 * (len(row.of) > 0) + bool(row.root_ends_in) + bool(row.penult)
        + bool(row.sense) + row.upapada + row.no_upasarga
        + (len(row.upasarga) > 0) + row.chandas
    )
    return stated + (2 if row.sutra == "3.1.109" else 0)


def _reaches(row: Krtya, root: str, root_ends_in: str, penult: str,
             sense: str, upapada: bool, upasarga: str,
             chandas: bool) -> bool:
    """Whether one row covers this root at all."""
    if row.of and root not in row.of:
        return False
    if row.not_of and root in row.not_of:
        return False
    if row.root_ends_in and row.root_ends_in != root_ends_in:
        return False
    if row.penult and row.penult != penult:
        return False
    if row.sense and row.sense != sense:
        return False
    if row.upapada and not upapada:
        return False
    if row.no_upasarga and upasarga:
        return False
    if row.upasarga and upasarga not in row.upasarga:
        return False
    if row.chandas and not chandas:
        return False
    return True


def nipatana(sutra_id: str) -> object:
    """
    The seventeen rules of this run that fix forms rather than add an
    affix — 3.1.101 to 3.1.105, 3.1.114 to 3.1.117, and the rest.

    यदिह लक्षणेनानुपपन्नं तत् सर्वं निपातनात् सिद्धम्: whatever the
    rules do not reach, the fixing supplies. So these are recorded as
    the sūtras give them, with the sense each holds in, and nothing is
    derived.
    """
    if sutra_id not in NIPATANA:
        return NotAdded(
            "",
            f"{sutra_id} is not one of this run's निपातन rules. Those "
            f"are {', '.join(sorted(NIPATANA))}",
        )
    forms, why = NIPATANA[sutra_id]
    return Added(", ".join(forms), sutra_id, why)


def provisions_for(sutra_id: str) -> Tuple[Krtya, ...]:
    """Every row a sūtra of this run states."""
    return tuple(r for r in KRTYA if r.sutra == sutra_id)


def _final_of(root: str) -> str:
    """
    Which of this run's four shapes the root's last sound falls in.

    Three different mechanisms, and each is asked of the rule that owns
    it rather than answered here:

    अच् and हल् ARE pratyāhāras, and the śivasūtras settle them.

    **पु is not.** It is प् with the it-letter उ, which by 1.1.69
    अणुदित्सवर्णस्य चाप्रत्ययः stands for the whole वर्ग — a savarṇa
    class, not a span of the śivasūtras. Reading it as a pratyāhāra
    raises PratyaharaError, which is how the mistake was found; it is
    now asked of `udit_of` and `savarnas_of`, which is where 1.1.69
    lives.

    3.1.125's उ is a single vowel and names itself. And 3.1.124 pairs
    ऋ with हल्, so a root ending in either answers to one row.
    """
    if not root:
        return ""
    from src.astadhyayi.adesa import scan_phonemes
    from src.astadhyayi.sivasutra import resolve

    sounds = scan_phonemes(root)
    if not sounds:
        return ""
    last = sounds[-1].text
    if last in ("u", "ū"):
        return "u"
    if last in ("ṛ", "ṝ") or last in resolve("hal").sounds:
        # 3.1.98 wants a labial specifically — the narrower reading of
        # the same final — so it is reported where it holds.
        if _in_varga(last, "pu"):
            return "pu"
        return "ṛ-or-hal"
    if last in resolve("ac").sounds:
        return "ac"
    return ""


def _penult_of(root: str) -> str:
    """
    The sound before the last — 1.1.65 अलोऽन्त्यात्पूर्व उपधा, which is
    codified, so it is asked rather than sliced off here.
    """
    if not root:
        return ""
    from src.astadhyayi.adesa import upadha

    return upadha(root) or ""


def _in_varga(sound: str, udit: str) -> bool:
    """
    Whether a sound falls in the वर्ग an udit term names — 1.1.69
    अणुदित्सवर्णस्य चाप्रत्ययः, which is codified.

    पु is प् marked with उ, and 1.1.69 delivers its वर्ग through
    savarṇatva. Both halves are asked: `udit_of` for which consonant
    the term is about, `savarnas_of` for the class it then stands for.
    """
    from src.astadhyayi.grahana import udit_of
    from src.astadhyayi.varna import savarnas_of

    base = udit_of(udit)
    if base is None:
        return False
    return sound in savarnas_of(base)
