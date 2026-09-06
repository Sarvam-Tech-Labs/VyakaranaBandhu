# -*- coding: utf-8 -*-
"""
3.2.134 to 3.2.186 — habit and duty, and the last affixes of the
pāda.

3.2.134 आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु is a heading and adds
nothing. It puts every rule as far as 3.2.177 under three senses at
once, and the vṛtti separates them:

    तच्छील     yaḥ svabhāvataḥ phalanirapekṣas tatra pravartate
               — one who does the thing by nature, with no eye to
               what comes of it
    तद्धर्म    yaḥ svadharme mamāyam iti pravartate vināpi śīlena
               — one who does it as his OFFICE, whether or not it
               is his bent
    तत्साधुकारी yo dhātvarthaṃ sādhu karoti
               — one who does it well

The distinction between the first two is the interesting one: habit
against duty, and a man may have the office without the inclination.

**The heading's extent is stated by naming a rule, not a number.**
आ क्वेः — as far as the क्विप् of 3.2.177 — and अभिविधौ चायम् आङ्,
the आ is inclusive, so that rule is covered too. तेन क्विपोऽप्ययम्
अर्थनिर्देशः.

**वासरूप IS SUSPENDED INSIDE THIS HEADING.** Three rules cite the
same ज्ञāpaka — ताच्छीलिकेषु वासरूपविधिर् नास्ति — and 3.2.146 argues
it out: ण्वुल् would have given the same form as वुञ्, so stating वुञ्
must be telling us something, and what it tells us is that 3.1.94 does
not let the other affixes stand alongside here. 3.1.94 IS codified, and
its own notes record that it suspends the अपवाद principle for the कृत्
section at large; this heading then suspends the suspension.

The resolver already gives ONE answer, so nothing had to change for it.
What changes is why: the single answer is right here for a reason the
text supplies, and not merely because a table picks a winner.

**And the suspension is general, not absolute.** प्रायिकं चैतद्
ज्ञापकम्, क्वचित् समावेश इष्यत एव — कम्रा युवतिः beside कमना युवतिः.
Recorded as a scar, since the code cannot offer both.

**DEBT — 3.2.177 is not codified**, so the far end of the heading
cannot be checked against a real rule. Recorded, and a test asserts it
so that paying it is noticed.
"""

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.upapada_krt import Added, NotAdded

#: 3.2.134's three senses, in the vṛtti's own order.
TACCHILA_SENSES: Tuple[str, ...] = (
    "tacchīla", "taddharma", "tatsādhukārin",
)

#: The heading runs from 3.2.134 to 3.2.177, inclusive at both ends.
TACCHILA_FROM, TACCHILA_THROUGH = 134, 177

#: 3.2.136's roots. The sūtra names them in one long compound and the
#: vṛtti works each: अलंकरिष्णुः, निराकरिष्णुः, प्रजनिष्णुः,
#: उत्पचिष्णुः, उत्पतिष्णुः, उन्मदिष्णुः, रोचिष्णुः, अपत्रपिष्णुः,
#: वर्तिष्णुः, वर्धिष्णुः, सहिष्णुः, चरिष्णुः.
ALAMKRNADI: Tuple[str, ...] = (
    "alaṃkṛñ", "nirākṛñ", "prajan", "utpac", "utpat", "unmad", "ruc",
    "apatrap", "vṛt", "vṛdh", "sah", "car",
)

#: 3.2.139's three, and भू joins them by the च — ग्लास्नुः, जिष्णुः,
#: स्थास्नुः, भूष्णुः.
GLADI: Tuple[str, ...] = ("glā", "ji", "sthā", "bhū")

#: 3.2.140's four.
TRASADI: Tuple[str, ...] = ("tras", "gṛdh", "dhṛṣ", "kṣip")


#: 3.2.141's eight. शमु उपशमे इत्यतः प्रभृति मदी हर्षे इत्येवमन्तः —
#: a stretch of the दिवादि class named by both its ends, as 3.1.140's
#: ज्वलादि was. The vṛtti works nine forms because प्रमादी and
#: उन्मादी both come from the last.
SAMADI: Tuple[str, ...] = (
    "śam", "tam", "dam", "śram", "bhram", "kṣam", "klam", "mad",
)

#: 3.2.142's roots, and the vṛtti settles four ambiguities among them
#: before listing the forms: पृची is the रुधादि root and not the
#: तुदादि, लुग्विकरणत्वात्; परिदेवि is भ्वादि; क्षिप् is taken in both
#: its classes; युज् likewise in both.
SAMPRCADI: Tuple[str, ...] = (
    "pṛc", "anurudh", "yam", "yas", "sṛ", "sṛj", "div", "jvar",
    "kṣip", "raṭ", "vad", "dah", "muh", "duṣ", "dviṣ", "druh", "duh",
    "yuj", "krīḍ", "vic", "tyaj", "raj", "bhaj", "car", "muṣ", "han",
)

#: 3.2.143's four, with वि before them.
KASADI: Tuple[str, ...] = ("kaṣ", "las", "katth", "srambh")

#: 3.2.145's six, with प्र before them.
LAPADI: Tuple[str, ...] = ("lap", "sṛ", "dru", "math", "vad", "vas")

#: 3.2.146's roots, which take वुञ् and not घिनुण्.
NINDADI: Tuple[str, ...] = (
    "nind", "hiṃs", "kliś", "khād", "vināś", "parikṣip", "pariraṭ",
    "parivād", "vyābhāṣ", "asūy",
)

#: 3.2.150's, beginning with a root the sūtra supplies itself —
#: जु इति सौत्रो धातुः.
JVADI: Tuple[str, ...] = (
    "ju", "caṅkramya", "dandramya", "sṛ", "gṛdh", "jval", "śuc",
    "laṣ", "pat", "pad",
)

#: 3.2.153's three, where युच् is refused.
SUDADI: Tuple[str, ...] = ("sūd", "dīp", "dīkṣ")

#: 3.2.154's, taking उकञ्.
LASADI: Tuple[str, ...] = (
    "laṣ", "pat", "pad", "sthā", "bhū", "vṛṣ", "han", "kam", "gam",
    "śṝ",
)

#: 3.2.155's, taking षाकन् — and षकारो ङीषर्थः, the ष written for the
#: feminine: जल्पाकः, वराकः, वराकी.
JALPADI: Tuple[str, ...] = (
    "jalp", "bhikṣ", "kuṭṭ", "luṇṭ", "vṛ",
)


#: 3.2.157's roots, and the vṛtti settles two before listing forms:
#: क्षि is taken in both its senses, and प्रसू is षू प्रेरणे.
JYADI: Tuple[str, ...] = (
    "ji", "dṛ", "kṣi", "viśri", "ṇu", "vam", "avyath", "abhyam",
    "paribhū", "prasū",
)

#: 3.2.158's. निद्रा and तन्द्रा are द्रा with नि, and श्रद्धा is धा
#: with श्रत् — compounds fixed by the sūtra, not roots of the list.
SPRHADI: Tuple[str, ...] = (
    "spṛh", "gṛh", "pat", "day", "nidrā", "tandrā", "śraddhā", "śī",
)

DADHETADI: Tuple[str, ...] = ("dā", "dheṭ", "si", "śad", "sad")
SRGHASADI: Tuple[str, ...] = ("sṛ", "ghas", "ad")
BHANJADI: Tuple[str, ...] = ("bhañj", "bhās", "mid")
VIDADI_KURAC: Tuple[str, ...] = ("vid", "bhid", "chid", "vyadh")
INADI: Tuple[str, ...] = ("iṇ", "naś", "ji", "sṛ")
YAJADI_UKA: Tuple[str, ...] = ("yaj", "jap", "daṃś")

#: 3.2.167's — and this is the rule 3.2.153 named when asking whether
#: its own refusal was needed at all.
NAMYADI: Tuple[str, ...] = (
    "nam", "kamp", "smi", "jas", "kam", "hiṃs", "dīp",
)

#: 3.2.171's three named roots; ā-final and ṛ-final roots come by the
#: shape conditions rather than by name.
GAMADI_KIKIN: Tuple[str, ...] = ("gam", "han", "jan")

STHESADI: Tuple[str, ...] = ("sthā", "īś", "bhās", "pis", "kas")

#: 3.2.177's, the rule 3.2.134's आ क्वेः names as its far end.
BHRAJADI: Tuple[str, ...] = (
    "bhrāj", "bhās", "dhur", "vidyut", "ūrj", "pṝ", "ju", "grāvastu",
)


def tacchila_heading(sutra_id: str = "") -> object:
    """
    3.2.134 — the heading, which adds nothing.

    It puts every rule as far as 3.2.177 under तच्छील, तद्धर्म and
    तत्साधुकारिन् at once. यानित ऊर्ध्वम् अनुक्रमिष्यामः
    तच्छीलादिषु कर्तृषु ते वेदितव्याः — whatever is enumerated from
    here on is to be understood of a doer of those kinds.

    Its extent is given by naming a RULE rather than a number, and the
    आ is inclusive: अभिविधौ चायम् आङ्, so 3.2.177 is covered too.
    """
    span = "3.2.%d to 3.2.%d" % (TACCHILA_FROM, TACCHILA_THROUGH)
    if not sutra_id:
        return Added(
            "", "3.2.134",
            "आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु — a heading over %s, "
            "its extent named by the क्विप् of 3.2.177 rather than by "
            "a count, and inclusive of it. It gives no affix; it puts "
            "the rules after it under three senses at once — habit, "
            "office, and doing well." % span)
    try:
        number = int(str(sutra_id).rsplit(".", 1)[1])
    except (ValueError, IndexError):
        number = -1
    inside = (str(sutra_id).startswith("3.2.")
              and TACCHILA_FROM <= number <= TACCHILA_THROUGH)
    if inside:
        return Added(
            "", "3.2.134",
            "%s falls under तच्छीलादिषु, so its affix comes of a doer "
            "who acts by habit, by office, or well — though the rule "
            "does not say so." % sutra_id)
    return NotAdded(
        "", "The heading reaches %s only. %s falls outside it."
        % (span, sutra_id))


#: 3.2.182's thirteen roots, each giving an instrument-word.
DAMNADI: Tuple[str, ...] = (
    "dāp", "nī", "śas", "yu", "yuj", "stu", "tud", "si", "sic",
    "mih", "pat", "daṃś", "nah",
)

#: 3.2.184's seven.
ARTYADI: Tuple[str, ...] = ("ṛ", "lū", "dhū", "sū", "khan", "sah", "car")


@dataclass(frozen=True)
class Tacchila:
    """One rule of the run, as the conditions it states."""

    sutra: str
    gives: str
    #: A second affix the same rule gives beside the first — 3.2.171's
    #: लिट् and 3.2.174's क्लुकन्.
    also: str = ""
    of: Tuple[str, ...] = ()
    causative: bool = False
    chandasi: bool = False
    #: A preverb the rule names — 3.2.143's वि, 3.2.145's प्र.
    which_upasarga: Tuple[str, ...] = ()
    #: 3.2.147 wants A preverb without saying which.
    any_upasarga: bool = False
    #: 3.2.148 and 3.2.149 want an INTRANSITIVE root.
    akarmaka: bool = False
    #: 3.2.149's अनुदात्तेत् and हलादि.
    anudattet: bool = False
    hal_adi: bool = False
    #: 3.2.148's चलनार्थ and शब्दार्थ, 3.2.151's क्रुध् and मण्ड्.
    sense: str = ""
    #: 3.2.152's यकारान्त.
    y_final: bool = False
    #: 3.2.166 and 3.2.176 want a यङन्त stem, 3.2.168 a सन्नन्त,
    #: 3.2.170 a क्यन्त. Each is a stem built before this affix comes.
    yan_anta: bool = False
    san_anta: bool = False
    kya_anta: bool = False
    #: 3.2.171 reaches roots by SHAPE as well as by name.
    a_final: bool = False
    r_final: bool = False
    #: 3.2.179 and 3.2.185 want the finished word to be a NAME;
    #: 3.2.180 wants it not to be. Tri-state for that reason.
    samjna: object = None
    #: 3.2.181 to 3.2.186 divide by which kāraka the word names.
    karaka: str = ""
    #: 3.2.183's हलसूकरयोः — the instrument is part of a plough or a
    #: boar, which is a condition on what the thing IS.
    part_of: Tuple[str, ...] = ()
    #: 3.2.186's ऋषि and देवता, bound crosswise to the kāraka.
    rsi_devata: str = ""
    #: 3.2.178 is the pāda's fourth open rule.
    attested: bool = False
    #: 3.2.152 and 3.2.153 REFUSE युच् rather than giving anything.
    refuses: bool = False
    why: str = ""


TACCHILA: Tuple[Tacchila, ...] = (
    Tacchila("3.2.135", "tṛn",
             why="तृन् — सर्वधातुभ्यः, after EVERY root, so this is the "
                 "widest of the run and the others cut into it. "
                 "नकारः स्वरार्थः, the न written for the accent. "
                 "तच्छीले कर्ता कटान्, वदिता जनापवादान्; तद्धर्मणि "
                 "मुण्डयितारः श्राविष्ठायना भवन्ति; तत्साधुकारिणि "
                 "कर्ता कटम्, गन्ता खेटम् — and the vṛtti gives an "
                 "example under each of the heading's three senses, so "
                 "the heading is seen to be doing work. SCOPE: five "
                 "vārttikas, तृन्विधावृत्विक्षु चानुपसर्गस्य (होता, "
                 "पोता — and अनुपसर्गस्येति किम्? उद्गातā, "
                 "प्रतिहर्ता, तृजेव भवति, स्वरे विशेषः), नयतेः षुक् "
                 "(नेष्टा), त्विषेर्देवतायाम् (त्वष्टा), क्षदेश्च "
                 "नियुक्ते (क्षत्ता), and छन्दसि तृच्"),
    Tacchila("3.2.136", "iṣṇuc", of=ALAMKRNADI,
             why="अलंकृञ्निराकृञ्… इष्णुच् — अलंकरिष्णुः, निराकरिष्णुः, "
                 "सहिष्णुः, चरिष्णुः. SCOPE: अलंकृञो मण्डनार्थाद् "
                 "युचः पूर्वविप्रतिषेधेनेष्णुज् वक्तव्यः — where अलम्+कृ "
                 "means adorning, this affix wins over युच् by "
                 "पूर्वविप्रतिषेध, a prior rule beating a later one, "
                 "which is the reverse of the usual order"),
    Tacchila("3.2.137", "iṣṇuc", causative=True, chandasi=True,
             why="णेश्छन्दसि — दृषदं धारयिष्णवः, वीरुधः पारयिष्णवः. "
                 "From the CAUSATIVE stem, and in the Veda"),
    Tacchila("3.2.138", "iṣṇuc", of=("bhū",), chandasi=True,
             why="भुवश्च — भविष्णुः, and छन्दसि विषये: 3.2.137's Vedic "
                 "condition runs on into this rule and stops only at "
                 "3.2.139, which says so itself. Without it this row "
                 "tied with 3.2.139 — both name भू — and won on table "
                 "order, so भूष्णुः was lost. योगविभाग उत्तरार्थः, split from "
                 "3.2.137 for the rule after. And चकारोऽनुक्त"
                 "समुच्चयार्थः: the च gathers in what is not named — "
                 "भ्राजिष्णुना लोहितचन्दनेन"),
    Tacchila("3.2.139", "ksnu", of=GLADI,
             why="ग्लाजिस्थश्च क्स्नुः — ग्लास्नुः, जिष्णुः, स्थास्नुः, "
                 "and भूष्णुः by the च. छन्दसीति निवृत्तम्, so it is "
                 "not held to the Veda. AND THE MARKER IS ग् AND NOT "
                 "क्: गिच् चायं प्रत्ययः, न कित्, and the vṛtti draws "
                 "out three consequences and then puts them in a "
                 "VERSE — क्स्नोर्गित्त्वान्न स्थ ईकारः "
                 "क्ङितोरीत्वशासनात्, गुणाभावस्त्रिषु स्मार्यः "
                 "श्र्युकोऽनिट्त्वं गकोरितोः. So स्था does not become "
                 "स्थी, no guṇa comes, and भू takes no augment. A "
                 "mnemonic verse standing in for three separate "
                 "arguments. SCOPE: दंशेश्छन्दस्युपसंख्यानम्, "
                 "दङ्क्ष्णवः पशवः"),
    Tacchila("3.2.140", "knu", of=TRASADI,
             why="त्रसिगृधिधृषिक्षिपेः क्नुः — त्रस्नुः, गृध्नुः, "
                 "धृष्णुः, क्षिप्णुः"),
    Tacchila("3.2.141", "ghinuṇ", of=SAMADI,
             why="शमित्यष्टाभ्यो घिनुण् — शमी, तमी, दमी, श्रमी, भ्रमी, "
                 "क्षमी, क्लमी, प्रमादी, उन्मादी. इतिशब्द आद्यर्थः, "
                 "and the group is a stretch of the दिवादि class named "
                 "by both its ends — शमु उपशमे इत्यतः प्रभृति मदी "
                 "हर्षे इत्येवमन्तः — as 3.1.140's ज्वलादि was. "
                 "अष्टाभ्य इति किम्? असिता, the ninth. AND THREE "
                 "MARKERS EACH DOING A DIFFERENT JOB: घकार उत्तरत्र "
                 "कुत्वार्थः, for a sound-change later; उकार "
                 "उच्चारणार्थः, merely to make the ghost pronounceable; "
                 "णकारो वृद्ध्यर्थः, for the strengthening. One affix, "
                 "three marks, three unrelated purposes"),
    Tacchila("3.2.142", "ghinuṇ", of=SAMPRCADI,
             why="संपृचानुरुधाङ्यमाङ्यस… — संपर्की, अनुरोधी, आयामी, "
                 "परिसारी, संसर्गी, परिदेवी, परिक्षेपी, परिवादी, "
                 "दोषी, द्वेषी, द्रोही, दोही, योगी, विवेकी, त्यागी, "
                 "रागी, भागी. AND FOUR ROOT AMBIGUITIES SETTLED BEFORE "
                 "ANY FORM IS GIVEN: पृची is the रुधादि root and not "
                 "the तुदादि, लुग्विकरणत्वात् — because the तुदादि one "
                 "loses its class-marker and so could not be told "
                 "apart; परिदेवि is भ्वादि; क्षिप् is taken in both "
                 "its classes सामान्येन; युज् likewise, द्वयोरपि "
                 "ग्रहणम्. And रञ्ज loses its nasal by निपातन"),
    Tacchila("3.2.143", "ghinuṇ", of=KASADI,
             which_upasarga=("vi",),
             why="वौ कषलसकत्थस्रम्भः — विकाषी, विलासी, विकत्थी, "
                 "विस्रम्भी"),
    Tacchila("3.2.144", "ghinuṇ", of=("laṣ",),
             which_upasarga=("apa", "vi"),
             why="अपे च लषः — अपलाषी, and विलाषी by the च, चकाराद् वौ "
                 "च: the च carries वि down from 3.2.143, so one rule "
                 "borrows the preverb of the rule before"),
    Tacchila("3.2.145", "ghinuṇ", of=LAPADI,
             which_upasarga=("pra",),
             why="प्रे लपसृद्रुमथवदवसः — प्रलापी, प्रसारी, प्रद्रावी, "
                 "प्रमाथी, प्रवादी, प्रवासी. And वस् is वस निवासे and "
                 "not the one meaning to clothe, लुग्विकरणत्वात् — the "
                 "same ground as 3.2.142's पृची, twice in four rules"),
    Tacchila("3.2.146", "vuñ", of=NINDADI,
             why="निन्दहिंसक्लिशखादविनाश… वुञ् — निन्दकः, हिंसकः, "
                 "क्लेशकः, खादकः, विनाशकः, परिवादकः, असूयकः. "
                 "पञ्चम्यर्थे प्रथमा, the nominative standing for an "
                 "ablative. AND A ज्ञापक THAT BEARS ON THE WHOLE "
                 "HEADING: ण्वुलैव सिद्धे वुञ्विधानं ज्ञापनार्थम् — "
                 "ण्वुल् would have given the same form, so stating "
                 "वुञ् must be telling us something, and what it tells "
                 "us is ताच्छीलिकेषु वासरूपन्यायेन तृजादयो न भवन्ति: "
                 "inside this heading 3.1.94's वासरूप does NOT let the "
                 "other affixes stand alongside"),
    Tacchila("3.2.147", "vuñ", of=("dev", "kruś"), any_upasarga=True,
             why="देविक्रुशोश्चोपसर्गे — आदेवकः, परिदेवकः, आक्रोशकः, "
                 "परिक्रोशकः. उपसर्ग इति किम्? देवयिता, क्रोष्टा — "
                 "with no preverb the ordinary affixes stand. The rule "
                 "wants A preverb without naming which, where 3.2.143 "
                 "to 3.2.145 each named one"),
    Tacchila("3.2.148", "yuc", akarmaka=True, sense="calana-śabda",
             why="चलनशब्दार्थादकर्मकाद् युच् — चलनः, चोपनः; and of "
                 "sound, शब्दनः, रवणः. अकर्मकादिति किम्? पठिता "
                 "विद्याम् — with an object the rule does not reach"),
    Tacchila("3.2.149", "yuc", anudattet=True, hal_adi=True,
             akarmaka=True,
             why="अनुदात्तेतश्च हलादेः — वर्तनः, वर्धनः. THREE "
                 "CONDITIONS AND THE VṚTTI ASKS AFTER EACH: "
                 "अनुदात्तेत इति किम्? भविता; हलादेरिति किम्? एधिता; "
                 "and आदिग्रहणं किम्? जुगुप्सनः, मीमांसनः — the word "
                 "आदि is there so that a root beginning with a "
                 "consonant counts even where a reduplication or a "
                 "सन् stands before it. अकर्मकादित्येव, carried down: "
                 "वसिता वस्त्रम्"),
    Tacchila("3.2.150", "yuc", of=JVADI,
             why="जुचङ्क्रम्यदन्द्रम्यसृगृधिज्वलशुचलषपतपदः — जवनः, "
                 "चङ्क्रमणः, दन्द्रमणः, सरणः, गर्धनः, ज्वलनः, शोचनः, "
                 "लषणः, पतनः, पदनः. जु इति सौत्रो धातुः, a root the "
                 "sūtra supplies itself. AND THE SAME ज्ञापक AGAIN, "
                 "with an addition: चलनार्थानां पदेश्च ग्रहणं "
                 "सकर्मकार्थम् — naming पद् is for the transitive "
                 "case; ज्ञापकार्थं च पदिग्रहणम् अन्ये वर्णयन्ति, "
                 "ताच्छीलिकेषु मिथो वासरूपविधिर् नास्ति, तेन अलंकृञस् "
                 "तृन् न भवति. And then the caveat: प्रायिकं चैतद् "
                 "ज्ञापकम्, क्वचित् समावेश इष्यत एव — गन्ता खेटं "
                 "विकत्थनः. So the suspension is general and not "
                 "absolute"),
    Tacchila("3.2.151", "yuc", of=("krudh", "maṇḍ"),
             sense="krodha-bhūṣā",
             why="क्रुधमण्डार्थेभ्यश्च — क्रोधनः, रोषणः, मण्डनः, "
                 "भूषणः. The rule names two roots and reaches whatever "
                 "MEANS what they mean, which is why रोषण and भूषण "
                 "stand beside the two named"),
    Tacchila("3.2.152", "yuc", y_final=True, refuses=True,
             why="न यः — क्नूयिता, क्ष्मायिता. पूर्वेण प्राप्तः "
                 "प्रतिषिध्यते: what 3.2.149 would have given a "
                 "य-final root is refused"),
    Tacchila("3.2.153", "yuc", of=SUDADI, refuses=True,
             why="सूददीपदीक्षश्च — सूदिता, दीपिता, दीक्षिता. "
                 "अनुदात्तेत्त्वात् प्राप्तः प्रतिषिध्यते. AND THE "
                 "VṚTTI ASKS WHY THE REFUSAL IS NEEDED AT ALL, since "
                 "3.2.167 gives दीप् a र of its own and that would "
                 "have displaced the युच् anyway — स एव बाधको "
                 "भविष्यति, किं प्रतिषेधेन? The answer is वासरूपेण "
                 "युजपि प्राप्नोति: by 3.1.94 the युच् could still "
                 "have stood beside it. And then the caveat again — "
                 "ताच्छीलिकेषु च वासरूपविधिर् नास्तीति प्रायिकम् एतद् "
                 "इत्युक्तम्, तथा च समावेशो दृश्यते: कम्रा युवतिः "
                 "beside कमना युवतिः, कम्प्रा शाखा beside कम्पना "
                 "शाखा. SCAR: सूदेर् युचि प्रतिषिद्धे कथं मधुसूदनो "
                 "रिपुसूदन इति? — three answers are offered and none "
                 "settled: अनित्योऽयं प्रतिषेधः by योगविभाग, or the "
                 "words are नन्द्यादि, or they are ल्युडन्त by "
                 "3.3.113, which is not codified"),
    Tacchila("3.2.154", "ukañ", of=LASADI,
             why="लषपतपदस्थाभूवृषहनकमगमशॄभ्य उकञ् — अपलाषुकं "
                 "वृषलसंगतम्, प्रपातुका गर्भा भवन्ति, उपपादुकं "
                 "सत्त्वम्, उपस्थायुका एनं पशवो भवन्ति, प्रभावुकम् "
                 "अन्नम्, प्रवर्षुकाः पर्जन्याः, कामुका एनं स्त्रियो "
                 "भवन्ति, आगामुकं वाराणसीं रक्ष आहुः, किंशारुकं "
                 "तीक्ष्णम् आहुः. Every example the vṛtti gives is a "
                 "whole sentence rather than a bare word, which is "
                 "unusual and worth noticing: these forms are quoted "
                 "from usage rather than built"),
    Tacchila("3.2.155", "ṣākan", of=JALPADI,
             why="जल्पभिक्षकुट्टलुण्टवृङः षाकन् — जल्पाकः, भिक्षाकः, "
                 "कुट्टाकः, लुण्टाकः, वराकः. षकारो ङीषर्थः — the ष is "
                 "written for the FEMININE, वराकी, so a marker here "
                 "does its work two adhyāyas away, as 3.2.16's ट did"),
    Tacchila("3.2.156", "ini", of=("ju",), which_upasarga=("pra",),
             why="प्रजोरिनिः — प्रजवी, प्रजविनौ"),
    Tacchila("3.2.157", "ini", of=JYADI,
             why="जिदृक्षिविश्रीण्वमाव्यथाभ्यमपरिभूप्रसूभ्यश्च — जयी, "
                 "दरी, क्षयी, विश्रयी, अत्ययी, वमी, अव्यथी, परिभवी, "
                 "प्रसवी. Two roots settled first, as the long lists "
                 "of this pāda always are: क्षि is taken in both its "
                 "senses, द्वयोरपि ग्रहणम्; and प्रसू is षू प्रेरणे"),
    Tacchila("3.2.158", "āluc", of=SPRHADI,
             why="स्पृहिगृहिपतिदयिनिद्रातन्द्राश्रद्धाभ्य आलुच् — "
                 "स्पृहयालुः, गृहयालुः, पतयालुः, दयालुः, निद्रालुः, "
                 "तन्द्रालुः, श्रद्धालुः. Three of the seven are not "
                 "roots of a list at all but compounds the sūtra "
                 "fixes: निद्रा and तन्द्रा are द्रा with नि, and "
                 "श्रद्धा is धा with श्रत्, तदो नकारान्तता च "
                 "निपात्यते. SCOPE: आलुचि शीङो ग्रहणं कर्तव्यम्, "
                 "शयालुः"),
    Tacchila("3.2.159", "ru", of=DADHETADI,
             why="दाधेट्सिशदसदो रुः — दारुः, धारुर्वत्सो मातरम्, "
                 "सेरुः, शद्रुः, सद्रुः. And 2.3.69's ban on the "
                 "genitive does not reach these, उकारप्रश्लेषात् — "
                 "the rule's own wording admits a उ that these affixes "
                 "do not answer to"),
    Tacchila("3.2.160", "kmarac", of=SRGHASADI,
             why="सृघस्यदः क्मरच् — सृमरः, घस्मरः, अद्मरः"),
    Tacchila("3.2.161", "ghurac", of=BHANJADI,
             why="भञ्जभासमिदो घुरच् — भङ्गुरं काष्ठम्, भासुरं "
                 "ज्योतिः, मेदुरः पशुः. घित्त्वात् कुत्वम्, the ghost "
                 "घ giving the क. AND भञ्जेः कर्मकर्तरि प्रत्ययः, "
                 "स्वभावात्: for that root the affix falls in the "
                 "कर्मकर्तृ sense — not because the rule says so but "
                 "BY THE NATURE OF THE THING, wood being broken rather "
                 "than breaking"),
    Tacchila("3.2.162", "kurac", of=VIDADI_KURAC,
             why="विदिभिदिच्छिदेः कुरच् — विदुरः पण्डितः, भिदुरं "
                 "काष्ठम्, छिदुरा रज्जुः. विद् is the one meaning to "
                 "KNOW and not the one meaning to get — again "
                 "स्वभावात्, from the nature of the case rather than "
                 "from anything stated, which is the second time in "
                 "two rules the vṛtti settles a question that way. "
                 "भिदिच्छिद्योः कर्मकर्तरि प्रयोगः. SCOPE: व्यधेः "
                 "संप्रसारणं कुरच् च, विधुरः"),
    Tacchila("3.2.163", "kvarap", of=INADI,
             why="इण्नश्जिसर्तिभ्यः क्वरप् — इत्वरः and इत्वरी, "
                 "नश्वरः, जित्वरः, सृत्वरः. पकारस्तुगर्थः, the प for "
                 "an augment; and 7.2.8 नेड् वशि कृति keeps the इट् "
                 "out"),
    Tacchila("3.2.164", "kvarap", of=("gam",),
             why="गत्वरश्च — गत्वरः, गत्वरी. A निपातन within the "
                 "table rather than outside it: what is fixed is the "
                 "loss of the nasal, गमेर् अनुनासिकलोपः, while the "
                 "affix itself is prescribed as everywhere else"),
    Tacchila("3.2.165", "ūka", of=("jāgṛ",),
             why="जागुरूकः — जागरूकः"),
    Tacchila("3.2.166", "ūka", of=YAJADI_UKA, yan_anta=True,
             why="यजजपदशां यङः — यायजूकः, जञ्जपूकः, दन्दशूकः. The "
                 "affix comes after the यङन्त stem and not the bare "
                 "root, so the stem must be built before this rule "
                 "can reach it"),
    Tacchila("3.2.167", "ra", of=NAMYADI,
             why="नमिकम्पिस्म्यजसकमहिंसदीपो रः — नम्रं काष्ठम्, "
                 "कम्प्रा शाखा, स्मेरं मुखम्, अजस्रं जुहोति, कम्रा "
                 "युवतिः, हिंस्रं रक्षः, दीप्रं काष्ठम्. THIS IS THE "
                 "RULE 3.2.153 NAMED when asking whether its own "
                 "refusal was needed — and कम्रा and कम्प्रा are the "
                 "very forms cited there as standing beside कमना and "
                 "कम्पना, which is how the suspension of वासरूप was "
                 "shown to be only general. अजस्र is जसु with नञ् "
                 "before it, in the sense of an act going on without "
                 "cease"),
    Tacchila("3.2.168", "u", of=("āśaṃs", "bhikṣ"), san_anta=True,
             why="सनाशंसभिक्ष उः — चिकीर्षुः, जिहीर्षुः, आशंसुः, "
                 "भिक्षुः. AND सन् IS THE AFFIX, NOT THE ROOT षण्: "
                 "अनभिधानाद् व्याप्तिन्यायाद् वा — either because no "
                 "usage would result, or by the principle that the "
                 "wider reading is taken. Two grounds offered for one "
                 "reading, and the vṛtti does not choose. आङः शसि "
                 "इच्छायाम् is meant and not शंस् in the sense of "
                 "praising"),
    Tacchila("3.2.169", "u", of=("vid", "iṣ"),
             why="विन्दुरिच्छुः — वेदनशीलो विन्दुः, एषणशील इच्छुः. "
                 "Both are fixed: विदेर् नुमागमः for the first, "
                 "इषेश् छत्वम् for the second, and the उ for both"),
    Tacchila("3.2.170", "u", kya_anta=True, chandasi=True,
             why="क्याच्छन्दसि — मित्रयुः, स्वेदयुः, सुम्नयुः. क्य is "
                 "क्यच्, क्यङ् and क्यष् taken together, सामान्येन "
                 "निर्देशः — one syllable standing for three affixes. "
                 "छन्दसीति किम्? मित्रीयिता. And 7.4.35 keeps the "
                 "vowel short"),
    Tacchila("3.2.171", "kikin", of=GAMADI_KIKIN, chandasi=True,
             also="लिट्",
             why="आदृगमहनजनः किकिनौ लिट् च — पपिः सोमं ददिर्गाः, "
                 "ततुरिम्, जगुरिः, जग्मिर्युवा, जघ्निर्वृत्रम्. "
                 "लिड्वच्च तौ भवतः, they behave as लिट् does. AND THE "
                 "VṚTTI ASKS WHY THEY ARE MARKED कित् AT ALL, since "
                 "1.2.5 असंयोगाल्लिट् कित् gives that already: "
                 "ऋच्छत्यृताम् (7.4.11) prescribes a guṇa in the "
                 "perfect precisely where a prohibition would "
                 "otherwise reach, तस्यापि बाधनार्थं कित्त्वम् — the "
                 "marking is there to defeat THAT. SCOPE: three "
                 "vārttikas widen it — किकिनावुत्सर्गः (सेदिः, "
                 "नेमिः), भाषायां धाञ्कृञ्सृजनिगमिनमिभ्यः (दधिः, "
                 "चक्रिः, जग्मिः), and सहिवहिचलिपतिभ्यो यङन्तेभ्यः "
                 "(सासहिः, वावहिः)"),
    Tacchila("3.2.172", "najiṅ", of=("svap", "tṛṣ"),
             why="स्वपितृषोर्नजिङ् — स्वप्नक्, तृष्णक्. छन्दसीति "
                 "निवृत्तम्, so the Vedic condition that ran through "
                 "3.2.170 and 3.2.171 stops here. SCOPE: धृषेश्च, "
                 "धृष्णक्"),
    Tacchila("3.2.173", "āru", of=("śṝ", "vand"),
             why="शॄवन्द्योरारुः — शरारुः, वन्दारुः"),
    Tacchila("3.2.174", "kru", of=("bhī",), also="क्लुकन्",
             why="भियः क्रुक्लुकनौ — भीरुः, भीलुकः, both affixes "
                 "standing. SCOPE: क्रुकन्नपि वक्तव्यः gives a third, "
                 "भीरुकः"),
    Tacchila("3.2.175", "varac", of=STHESADI,
             why="स्थेशभासपिसकसो वरच् — स्थावरः, ईश्वरः, भास्वरः, "
                 "पेस्वरः, विकस्वरः"),
    Tacchila("3.2.176", "varac", of=("yā",), yan_anta=True,
             why="यश्च यङः — यायावरः. The second rule of the run to "
                 "want a यङन्त stem, after 3.2.166"),
    Tacchila("3.2.177", "kvip", of=BHRAJADI,
             why="भ्राजभासधुर्विद्युतोर्जिपॄजुग्रावस्तुवः क्विप् — "
                 "विभ्राट्, भाः, धूः, विद्युत्, ऊर्क्, पूः, जूः, "
                 "ग्रावस्तुत्. जवतेर् दीर्घश्च निपात्यते.\n\n"
                 "AND IT CLOSES AN ARGUMENT BEGUN THIRTY-ONE RULES "
                 "EARLIER. किमर्थमिदमुच्यते, यावता अन्येभ्योऽपि "
                 "दृश्यन्ते, क्विप् च इति क्विप् सिद्ध एव? — 3.2.75 "
                 "and 3.2.76 give क्विप् already, so why say it again? "
                 "ताच्छीलिकैर् बाध्यते, वासरूपविधिर् नास्तीत्युक्तम्: "
                 "the affixes of this heading would DISPLACE that "
                 "general क्विप्, and since वासरूप is suspended here "
                 "it could not have stood beside them. So the rule "
                 "exists because of the ज्ञापक at 3.2.146. And the "
                 "vṛtti adds the qualification once more — अथ तु "
                 "प्रायिकम् एतत्, ततस् तस्यैवायं प्रपञ्चः: if the "
                 "suspension is only general, then this is simply that "
                 "rule worked out.\n\n"
                 "This is also the rule 3.2.134's आ क्वेः names as the "
                 "far end of the heading, so codifying it closes the "
                 "span from both sides"),
    Tacchila("3.2.178", "kvip", attested=True,
             why="अन्येभ्योऽपि दृश्यते — युक्, छित्, भित्. The pāda's "
                 "FOURTH open rule, after 3.2.75, 3.2.76 and 3.2.101, "
                 "and held to attested forms as they are.\n\n"
                 "AND ITS दृश्यते DOES A DIFFERENT JOB FROM THEIRS. At "
                 "3.2.75 the word was read प्रयोगानुसरणार्थम्, so that "
                 "the rule follows usage. Here it is "
                 "विध्यन्तरोपसंग्रहार्थम् — to GATHER IN OTHER "
                 "OPERATIONS: क्वचिद् दीर्घः, क्वचिद् द्विर्वचनम्, "
                 "क्वचित् संप्रसारणम्, क्वचिद् असंप्रसारणम्. One word, "
                 "two purposes, a hundred rules apart.\n\n"
                 "SCOPE — the vṛtti then gives the operations in a "
                 "verse and its own remarks: वचि, प्रच्छि, आयतस्तु, "
                 "कटप्रु and श्री take the long vowel and no "
                 "संप्रसारण — वाक्, शब्दप्राट्, आयतस्तूः, कटप्रूः, "
                 "श्रीः; द्युति, गमि and जुहोति reduplicate — "
                 "दिद्युत्, जगत्, जुहूः; दृ takes a short vowel and "
                 "reduplication, ददृत्; ध्यै takes संप्रसारण, धीः. "
                 "And the vṛtti notices its own verse is redundant in "
                 "one place: जुग्रहणेनात्र नार्थः, भ्राजादिसूत्र एव "
                 "गृहीतत्वात् — जु was already named at 3.2.177"),
    Tacchila("3.2.179", "kvip", of=("bhū",), samjna=True,
             why="भुवः संज्ञान्तरयोः — विभूर्नाम कश्चित्, a name; and "
                 "प्रतिभूः in the sense of BETWEEN, which the vṛtti "
                 "glosses concretely: धनिकाधमर्णयोरन्तरे यस्तिष्ठति स "
                 "प्रतिभूः — one who stands between creditor and "
                 "debtor, a surety. Two senses in one rule, and the "
                 "second explained by the situation rather than by a "
                 "synonym"),
    Tacchila("3.2.180", "ḍu", of=("bhū",), samjna=False,
             which_upasarga=("vi", "pra", "sam"),
             why="विप्रसम्भ्यो ड्वसंज्ञायाम् — विभुः सर्वगतः, प्रभुः "
                 "स्वामी, संभुर्जनिता. असंज्ञायामिति किम्? विभूर्नाम "
                 "कश्चित् — and that is 3.2.179's own example, so the "
                 "two rules divide one word between them by whether it "
                 "is a name. SCOPE: मितद्र्वादिभ्य उपसंख्यानम्, "
                 "मितद्रुः, शंभुः"),
    Tacchila("3.2.181", "ṣṭran", of=("dhe", "dhā"), karaka="karman",
             why="धः कर्मणि ष्ट्रन् — धयन्ति तां दधति वा भैषज्यार्थम् "
                 "इति धात्री, said both of a wet-nurse and of the "
                 "myrobalan. षकारो ङीषर्थः, the ष for the feminine — "
                 "the fourth marker in this pāda written for what "
                 "another rule will do with it"),
    Tacchila("3.2.182", "ṣṭran", of=DAMNADI, karaka="karaṇa",
             why="दाम्नीशसयुयुजस्तुतुदसिसिचमिहपतदशनहः करणे — दात्रम्, "
                 "नेत्रम्, शस्त्रम्, योत्रम्, योक्त्रम्, स्तोत्रम्, "
                 "तोत्त्रम्, सेत्रम्, सेक्त्रम्, मेढ्रम्, पत्त्रम्, "
                 "दंष्ट्रा, नद्ध्री. Thirteen roots, each naming the "
                 "thing an act is done WITH.\n\n"
                 "AND A ज्ञापक FROM HOW ONE ROOT IS SPELT: "
                 "दंशेरनुनासिकलोपेन निर्देशो ज्ञापनार्थः — the sūtra "
                 "writes दश and not दंश, and that tells us "
                 "क्ङितोऽन्यस्मिन्नपि प्रत्यये नलोपः क्वचिद् भवति, "
                 "the nasal may drop before affixes other than कित् "
                 "and ङित् ones. तेन ल्युट्यपि भवति, दशनम्. A "
                 "spelling in one rule licensing an operation in "
                 "another"),
    Tacchila("3.2.183", "ṣṭran", of=("pū",), karaka="karaṇa",
             part_of=("hala", "sūkara"),
             why="हलसूकरयोः पुवः — हलस्य पोत्रम्, सूकरस्य पोत्रम्, "
                 "मुखम् उच्यते: the ploughshare and the boar's snout, "
                 "one word for both. The condition is on what the "
                 "instrument is PART OF, which no rule of the pāda had "
                 "asked before"),
    Tacchila("3.2.184", "itra", of=ARTYADI, karaka="karaṇa",
             why="अर्तिलूधूसूखनसहचर इत्रः — अरित्रम् an oar, लवित्रम् "
                 "a sickle, धवित्रम् a fan, सवित्रम्, खनित्रम् a "
                 "spade, सहित्रम्, चरित्रम्"),
    Tacchila("3.2.185", "itra", of=("pū",), karaka="karaṇa",
             samjna=True,
             why="पुवः संज्ञायाम् — दर्भः पवित्रम्, बर्हिष्पवित्रम्. "
                 "समुदायेन चेत् संज्ञा गम्यते: the NAME is carried by "
                 "the whole, the fourth समुदायोपाधि of this pāda after "
                 "3.2.80, 3.2.92 and 3.2.99"),
    Tacchila("3.2.186", "itra", of=("pū",), rsi_devata="ṛṣi",
             karaka="karaṇa",
             why="कर्तरि चर्षिदेवतयोः, यथासंख्यम् — and the pairing is "
                 "crosswise between a kāraka and a kind of being: "
                 "ऋषौ करणे, देवतायां कर्तरि. Of a seer the word names "
                 "the MEANS — पूयतेऽनेनेति पवित्रोऽयमृषिः; of a deity "
                 "the DOER — अग्निः पवित्रं स मा पुनातु. One form, two "
                 "readings, chosen by what it is said of"),
)


def tacchila_affix(root: str = "", *, wants: str = "",
                   causative: bool = False,
                   chandasi: bool = False, upasarga: str = "",
                   akarmaka: bool = False, anudattet: bool = False,
                   hal_adi: bool = False, sense: str = "",
                   y_final: bool = False, yan_anta: bool = False,
                   san_anta: bool = False, kya_anta: bool = False,
                   a_final: bool = False, r_final: bool = False,
                   samjna: bool = False, karaka: str = "",
                   part_of: str = "", rsi_devata: str = "",
                   attested: bool = False) -> object:
    """
    Which affix a root takes of one who acts by habit, by office or
    well — 3.2.135 to 3.2.140.

    3.2.135 reaches every root and the rest cut into it, so the MOST
    SPECIFIC rule answers. Where two rules name one root — which is
    common here, and the vṛtti gives forms from each — `wants`
    names the affix asked after, as it does in the उपपद table. The three senses of 3.2.134's heading are
    not inputs: every rule of the run wants them together, and none
    divides on which, so there is nothing for a caller to choose.
    """
    matched = [row for row in TACCHILA
               if _reaches(row, root, causative, chandasi, upasarga,
                           akarmaka, anudattet, hal_adi, sense,
                           y_final, yan_anta, san_anta, kya_anta,
                           a_final, r_final, samjna, karaka,
                           part_of, rsi_devata, attested)]
    if wants:
        matched = [row for row in matched
                   if row.refuses or row.gives == wants
                   or (row.also and wants in row.also)]
    refusals = [row for row in matched if row.refuses]
    giving = [row for row in matched if not row.refuses]
    # 3.2.152 and 3.2.153 refuse युच्. What those roots then take is
    # whatever else reaches them — 3.2.135's तृन् — so that is the
    # rule reported and the प्रतिषेध rides alongside. The decision
    # 2.3.72 settled and 3.2.23 and 3.2.113 followed.
    for refusal in refusals:
        giving = [row for row in giving if row.gives != refusal.gives]
    if not giving:
        if refusals:
            best = max(refusals, key=_how_specific)
            return NotAdded(best.sutra, best.why, best.gives)
        return NotAdded(
            "",
            "No rule of this run reaches it — though 3.2.135 reaches "
            "every root, so this can only happen where a condition it "
            "does not state was asserted")
    best = max(giving, key=_how_specific)
    return Added(best.gives, best.sutra, best.why,
                 also=best.also,
                 blocked_by=refusals[0].sutra if refusals else "")


def _how_specific(row: Tacchila) -> int:
    return (3 * (len(row.of) > 0) + 2 * row.causative
            + 2 * row.chandasi
            + 2 * (len(row.which_upasarga) > 0) + row.any_upasarga
            + row.akarmaka + 2 * row.anudattet + row.hal_adi
            + 2 * bool(row.sense) + 2 * row.y_final
            + 2 * row.yan_anta + 2 * row.san_anta
            + 2 * row.kya_anta + row.a_final + row.r_final
            + (row.samjna is not None) + 2 * bool(row.karaka)
            + 2 * (len(row.part_of) > 0)
            + 2 * bool(row.rsi_devata) + 2 * row.attested)


def _reaches(row: Tacchila, root: str, causative: bool,
             chandasi: bool, upasarga: str = "",
             akarmaka: bool = False, anudattet: bool = False,
             hal_adi: bool = False, sense: str = "",
             y_final: bool = False, yan_anta: bool = False,
             san_anta: bool = False, kya_anta: bool = False,
             a_final: bool = False, r_final: bool = False,
             samjna: bool = False, karaka: str = "",
             part_of: str = "", rsi_devata: str = "",
             attested: bool = False) -> bool:
    if row.of and root not in row.of:
        return False
    if row.which_upasarga and upasarga not in row.which_upasarga:
        return False
    # 3.2.147 wants A preverb without naming which.
    if row.any_upasarga and not upasarga:
        return False
    if row.akarmaka and not akarmaka:
        return False
    if row.anudattet and not anudattet:
        return False
    if row.hal_adi and not hal_adi:
        return False
    if row.sense and row.sense != sense:
        return False
    if row.y_final and not y_final:
        return False
    # A stem built BEFORE this affix comes — यङन्त, सन्नन्त, क्यन्त.
    # Each is one-way: requiring it excludes what lacks it.
    if row.yan_anta and not yan_anta:
        return False
    if row.san_anta and not san_anta:
        return False
    if row.kya_anta and not kya_anta:
        return False
    if row.a_final and not a_final:
        return False
    if row.r_final and not r_final:
        return False
    if row.samjna is not None and bool(row.samjna) != samjna:
        return False
    if row.karaka and row.karaka != karaka:
        return False
    if row.part_of and part_of not in row.part_of:
        return False
    if row.rsi_devata and row.rsi_devata != rsi_devata:
        return False
    if row.attested and not attested:
        return False
    # One-way, as everywhere else: requiring a condition excludes what
    # lacks it, and saying nothing about it excludes nothing.
    if row.causative and not causative:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def provisions_for(sutra_id: str) -> Tuple[Tacchila, ...]:
    """Every row a sūtra of this run states."""
    return tuple(r for r in TACCHILA if r.sutra == sutra_id)
