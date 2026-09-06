# -*- coding: utf-8 -*-
"""
3.2.1 to 3.2.28 — the affix a root takes when a word stands beside it.

3.1.92 named the उपपद and this is where the name earns its keep: from
here the affix depends not on the root alone but on what stands next
to it. 3.2.1 gives अण् wherever the object is that companion, and the
rules after it cut into that ground with six other affixes:

    3.2.1  कर्मण्यण्                  अण्, with the object beside
    3.2.2  ह्वावामश्च                 and after three roots
    3.2.3  आतोऽनुपसर्गे कः            क, after आ with no preverb
    3.2.4  सुपि स्थः                  and after स्था, with any word
    3.2.5  तुन्दशोकयोः परिमृजापनुदोः   and two roots with two words
    3.2.6  प्रे दाज्ञः                and two more, after प्र
    3.2.7  समि ख्यः                   and ख्या after सम्
    3.2.8  गापोष्टक्                  टक्, after two roots
    3.2.9  हरतेरनुद्यमनेऽच्           अच्, after हृ, not of lifting
    3.2.10 वयसि च                     and where an age is meant
    3.2.11 आङि ताच्छील्ये             and after आ, of a disposition
    3.2.12 अर्हः                      and after अर्ह्
    3.2.13 स्तम्बकर्णयो रमिजपोः        and two roots with two words
    3.2.14 शमि धातोः संज्ञायाम्        and any root with शम्, as a name
    3.2.15 अधिकरणे शेतेः               and शी, with a place beside
    3.2.16 चरेष्टः                    ट, and चर् with a place
    3.2.17 भिक्षासेनादायेषु च          and with three words
    3.2.18 पुरोऽग्रतोऽग्रेषु सर्तेः     and सृ with three more
    3.2.19 पूर्वे कर्तरि               and with पूर्व as the doer
    3.2.20 कृञो हेतुताच्छील्यानुलोम्येषु  and कृ, in three senses
    3.2.21 दिवाविभानिशा…              and कृ, after twenty-seven words
    3.2.22 कर्मणि भृतौ                and कृ with कर्मन्, of wages
    3.2.23 न शब्दश्लोक…               but NOT after nine words
    3.2.24 स्तम्बशकृतोरिन्             इन्, कृ after two words
    3.2.25 हरतेर्दृतिनाथयोः पशौ        and हृ, of an animal
    3.2.26 फलेग्रहिरात्मम्भरिश्च        — two words simply fixed
    3.2.27 छन्दसि वनसनरक्षिमथाम्       and four roots, in the Veda
    3.2.28 एजेः खश्                   खश्, after causative एज्

**Which kāraka the companion is cannot be read off it.** 3.2.1 wants
the object, and 1.4.49 कर्तुरीप्सिततमं कर्म is codified — but that
rule takes the semantic facts asserted of a participant, not a word,
because deciding a kāraka needs the whole clause. So the role is
passed in, exactly as 2.3.1 passes it, and the debt is the same one.

**What IS asked is 1.4.59, and only that.** 3.2.3 and 3.2.8 turn on
whether a preverb stands, which that rule decides. 3.2.3's आत् looks
like a second call and is not: आ is a plain sound, so no pratyāhāra is
formed and 1.1.71 — which the कृत्य and agent runs both ask, for हल्
and अच् and इक् — is never reached here. It was declared anyway, out
of habit, and the reuse guard refused it.

**One rule refuses instead of giving, and does not thereby govern.**
3.2.23 is the only प्रतिषेध here: it keeps 3.2.20's ट off nine words.
What those words then take is 3.2.1's अण् — शब्दकारः — so that is the
rule reported, with 3.2.23 carried in `blocked_by`. The standing
decision is the one 2.3.72 and 2.3.50 settled: the rule that SUPPLIES
the case answers, not the rule that excepted it. But where a refusal
leaves nothing at all, refusing IS the rule acting, and then it names
itself.

**3.2.26 is a निपातन and has its own entry point.** यदिह
लक्षणेनानुपपन्नं तत् सर्वं निपातनात् सिद्धम्. फलेग्रहि fixes both the
ए-final shape of its companion and its affix; आत्मम्भरि fixes an
augment. Neither is reachable by a condition, so `nipatana` gives them
as they stand rather than the table pretending to derive them.

**अनभिधानात् is a limit the rules do not state.** 3.2.1 looks as
though it should give a form for every object whatever, and the vṛtti
stops it by hand: ग्रामं गच्छति, आदित्यं पश्यति, हिमवन्तं शृणोति —
these take no affix, अनभिधानात्, because usage has no such word. A
ground of the same kind as 3.1.108's, and recorded rather than turned
into a condition, since there is no condition to turn it into.
"""

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.krt_conditions import ends_in_a, has_upasarga

# ---------------------------------------------------------------------------
# The roots and words the sūtras name
# ---------------------------------------------------------------------------

#: 3.2.2's three.
HVADI: Tuple[str, ...] = ("hveñ", "veñ", "māṅ")

#: 3.2.5's two roots, with the two words they pair with यथासंख्यम्.
TUNDA_SOKA: Tuple[Tuple[str, str], ...] = (
    ("tunda", "parimṛj"), ("śoka", "apanud"),
)

#: 3.2.13's two, likewise paired.
STAMBA_KARNA: Tuple[Tuple[str, str], ...] = (
    ("stamba", "ram"), ("karṇa", "jap"),
)

#: 3.2.17's three companions for चर्.
BHIKSADI: Tuple[str, ...] = ("bhikṣā", "senā", "ādāya")

#: 3.2.18's three for सृ.
PURASADI: Tuple[str, ...] = ("puras", "agratas", "agre")

#: 3.2.20's three senses.
KRN_SENSES: Tuple[str, ...] = ("hetu", "tācchīlya", "ānulomya")

#: 3.2.21's twenty-seven companions for कृ. The vṛtti reads BOTH
#: कर्मणि and सुपि down into it — कर्मणि सुपीति च द्वयमप्यनुवर्तते,
#: तत्र यथायोगं सम्बन्धः — each member taking whichever fits, and it
#: names दिवा as the one that is a place: दिवाशब्दोऽधिकरणवचनः.
DIVADI: Tuple[str, ...] = (
    "divā", "vibhā", "niśā", "prabhā", "bhās", "kāra", "anta",
    "ananta", "ādi", "bahu", "nāndī", "kim", "lipi", "libi", "bali",
    "bhakti", "kartṛ", "citra", "kṣetra", "saṃkhyā", "jaṅghā", "bāhu",
    "ahar", "yat", "tad", "dhanus", "arus",
)

#: 3.2.21's vārttika gives four of them अच् instead —
#: किंयत्तद्बहुषु कृञोऽज्विधानम्, for the feminines किंकरा, यत्करा.
KIMYATTADBAHU: Tuple[str, ...] = ("kim", "yat", "tad", "bahu")

#: 3.2.23's nine, where the ट is REFUSED.
SABDADI: Tuple[str, ...] = (
    "śabda", "śloka", "kalaha", "gāthā", "vaira", "cāṭu", "sūtra",
    "mantra", "pada",
)

#: 3.2.27's four roots, in the Veda only.
VANADI: Tuple[str, ...] = ("van", "san", "rakṣ", "math")

#: 3.2.29's licensed combinations, and the point of the rule is that
#: they are NOT one-to-one. यथासंख्यमत्र नेष्यते: स्तने धेटः —
#: स्तनन्धयः — but नासिकायां तु ध्मश्च धेटश्च, both. The vṛtti reads
#: that off the WORDING rather than the sense: लक्षणव्यभिचारचिह्नाद्
#: अल्पाच्तरस्यापूर्वनिपातनाल्लभ्यते — the shorter word should have
#: been placed first by 2.2.34 अल्पाच्तरम्, and its not being placed
#: first is the sign that the usual reading is departed from.
NASIKA_STANA: Tuple[Tuple[str, str], ...] = (
    ("nāsikā", "dhmā"), ("nāsikā", "dheṭ"), ("stana", "dheṭ"),
)

#: 3.2.30's two, and the च gathers in four more the vṛtti supplies —
#: अनुक्तसमुच्चयार्थश्चकारः: घटिन्धमः, खारिन्धमः, वातन्धमः.
NADI_MUSTI: Tuple[str, ...] = (
    "nāḍī", "muṣṭi", "ghaṭi", "khāri", "vāta",
)

#: 3.2.33's परिमाणम्, glossed प्रस्थादि — an आकृतिगण, so the three
#: named are examples and not the whole of it.
PARIMANA: Tuple[str, ...] = ("prastha", "droṇa", "khārī")

#: 3.2.36's two, यथासंख्यम् — असूर्यम्पश्या with दृश्, ललाटन्तपः
#: with तप्.
ASURYA_LALATA: Tuple[Tuple[str, str], ...] = (
    ("asūrya", "dṛś"), ("lalāṭa", "tap"),
)

#: 3.2.41's two, likewise — पुरंदरः with दॄ, सर्वंसहः with सह्.
PUR_SARVA: Tuple[Tuple[str, str], ...] = (
    ("pur", "dṝ"), ("sarva", "sah"),
)

#: 3.2.42's four companions for कष्.
SARVAKULADI: Tuple[str, ...] = ("sarva", "kūla", "abhra", "karīṣa")

#: 3.2.43's three for कृ. भय is the one the vṛtti singles out for
#: तदन्तविधि — उपपदविधौ भयादिग्रहणं तदन्तविधिं प्रयोजयति, अभयंकरः.
MEGHADI: Tuple[str, ...] = ("megha", "ṛti", "bhaya")

#: 3.2.44's three, which take BOTH अण् and खच्.
KSEMADI: Tuple[str, ...] = ("kṣema", "priya", "madra")

#: 3.2.46's eight roots, in a NAME.
BHRADI: Tuple[str, ...] = (
    "bhṛ", "tṝ", "vṛ", "ji", "dhṛ", "sah", "tap", "dam",
)


def _gana_members(sutra_id: str) -> Tuple[str, ...]:
    """
    The members of a gaṇa, from the गणपाठ on disk.

    Read rather than retyped. The two gaṇas this pāda needs were both
    in the corpus before they were in the code, and the only reason
    they were missing is that nobody had asked. A hand-copied list
    would also have had to be corrected here when the corpus was.
    """
    from src.astadhyayi.corpus import load_ganapatha

    return tuple(item for entry in load_ganapatha().get(sutra_id, ())
                 for item in entry.items)


#: 3.2.5's vārttika gaṇa — कप्रकरणे मूलविभुजादिभ्य उपसंख्यानम्. The
#: members are FINISHED words and not companions: मूलानि विभुजतीति
#: मूलविभुजो रथः, नखमुचानि धनूंषि, काकगुहास्तिलाः, कौ मोदते कुमुदम्.
#: So they are looked up whole, as निपातन are, rather than resolved —
#: what the vārttika supplies is the word, not a rule for making it.
#: The गणपाठ marks it आकृतिगण, so the list is open.
MULAVIBHUJADI: Tuple[str, ...] = _gana_members("3.2.5")

#: 3.2.15's — पार्श्वादिषूपसंख्यानम्, and these ARE companions:
#: पार्श्वाभ्यां शेते पार्श्वशयः. The corpus holds five, of which the
#: vṛtti works three under this vārttika and two under the next,
#: उत्तानादिषु कर्तृषु.
PARSVADI: Tuple[str, ...] = _gana_members("3.2.15")


#: 3.2.48's seven companions for गम्.
ANTADI: Tuple[str, ...] = (
    "anta", "atyanta", "adhvan", "dūra", "pāra", "sarva", "ananta",
)

#: 3.2.48's vārttikas add five more, and then decline to close the
#: list: डप्रकरणेऽन्येष्वपि दृश्यत इति — स्त्र्यगारगः, ग्रामगः,
#: गुरुतल्पगः. So the members are held with the sūtra's own seven and
#: the rule is marked open rather than pretending to completeness.
ANTADI_VARTTIKA: Tuple[str, ...] = (
    "sarvatra", "panna", "uras", "su", "dur", "nis",
)

#: 3.2.56 and 3.2.57's आढ्यादि. The गणपाठ on disk keys no gaṇa to
#: either sūtra, so the members are the seven the vṛtti works through
#: in its own examples — आढ्यंकरणम्, सुभगंकरणम्, and so on for each.
ADHYADI: Tuple[str, ...] = (
    "āḍhya", "subhaga", "sthūla", "palita", "nagna", "andha", "priya",
)

#: 3.2.60's त्यदादि, likewise taken from the vṛtti's worked forms —
#: त्यादृशः, तादृशः, यादृशः — with समान and अन्य added by a vārttika,
#: समानान्ययोश्चेति वक्तव्यम्, सदृशः, अन्यादृशः.
TYADADI: Tuple[str, ...] = (
    "tyad", "tad", "yad", "etad", "idam", "kim", "samāna", "anya",
)

#: 3.2.59's three roots that take क्विन् BY RULE, as against the five
#: words it fixes outright.
ANCADI: Tuple[str, ...] = ("añc", "yuj", "kruñc")


#: 3.2.61's twelve roots. The vṛtti settles three ambiguities among
#: them by hand: सू is सूतेः आदादिकस्य and not सुवतेः तौदादिकस्य, द्विषा
#: साहचर्यात् — read off the company it keeps; युज् is BOTH युजिर् योगे
#: and युज समाधौ; विद् is three of the four — ज्ञाने, सत्तायाम्,
#: विचारणे — but न लाभार्थस्य विदेः, अकारस्य विवक्षितत्वात्.
SADADI: Tuple[str, ...] = (
    "sad", "sū", "dviṣ", "druh", "duh", "yuj", "vid", "bhid", "chid",
    "ji", "nī", "rāj",
)

#: 3.2.67's five, and two of them are likewise doubled: जन जनने and
#: जनी प्रादुर्भावे, षणु दाने and वन षण संभक्तौ, द्वयोरपि ग्रहणम्.
JANADI: Tuple[str, ...] = ("jan", "san", "khan", "kram", "gam")

#: 3.2.74 and 3.2.75 give the same four affixes — and the fourth comes
#: from the च: चकाराद् विज् भवति.
ATO_AFFIXES: Tuple[str, ...] = ("manin", "kvanip", "vanip", "vic")


#: 3.2.87's three objects for हन्, and 3.2.89's four for कृ (सु is
#: excluded from the कर्म reading — तदसंभवात् सुशब्दं वर्जयित्वा).
BRAHMADI: Tuple[str, ...] = ("brahman", "bhrūṇa", "vṛtra")
SUKARMADI: Tuple[str, ...] = ("su", "karman", "pāpa", "mantra", "puṇya")


@dataclass(frozen=True)
class Upapada:
    """One rule adding an affix where a word stands beside, as conditions."""

    sutra: str
    gives: str
    of: Tuple[str, ...] = ()
    #: The companion word the rule names, where it names one.
    beside: Tuple[str, ...] = ()
    #: Which (companion, root) combinations actually hold, where
    #: the rule does not license every pairing of its two lists.
    #: यथासंख्यम् is the usual reason — 3.2.5 binds तुन्द to
    #: परिमृज् and not to अपनुद् — but 3.2.29 needs it for the
    #: opposite case, where the vṛtti REFUSES the one-to-one
    #: reading and the licensed set is neither paired nor the
    #: full product.
    pairs: Tuple[Tuple[str, str], ...] = ()
    #: What that companion must be — कर्मन्, अधिकरण, कर्तृ, or any सुबन्त.
    role: str = ""
    a_final: bool = False
    #: True where a preverb is wanted, False where refused, None where
    #: the rule says nothing.
    upasarga: object = None
    which_upasarga: Tuple[str, ...] = ()
    sense: str = ""
    not_sense: str = ""
    #: What the FINISHED WORD denotes, which is a different
    #: question from the sense of the act — 3.2.25 needs both at
    #: once, since पशौ is its own condition while उद्यमन is what
    #: keeps 3.2.9 off दृतिहारः.
    names_a: str = ""
    #: True where the rule REFUSES the affix rather than giving it.
    #: 3.2.23 is the only प्रतिषेध of the run.
    refuses: bool = False
    #: 3.2.27 holds in the Veda only.
    chandasi: bool = False
    #: 3.2.28 wants the causative stem, not the bare root. A rule
    #: that leaves this False is SILENT about the causative, not
    #: opposed to it — 3.2.39 takes both readings of तप्.
    causative: bool = False
    #: 3.2.43 — where naming a word in an उपपद rule reaches what
    #: ENDS in it, by 1.1.72 येन विधिस्तदन्तस्य. The vṛtti flags
    #: this rule for it specifically, so it is not applied to the
    #: run at large.
    tadanta: bool = False
    #: 3.2.53 wants a NON-human agent, and says so — अमनुष्यकर्तृके.
    #: 3.2.54 exists for the human case but does not state it, so it
    #: carries a sense and not this: मनुष्यकर्तृकार्थ आरम्भः is the
    #: vṛtti's reason for the rule, not a condition in it.
    agent: str = ""
    #: 3.2.58's अनुदके — a companion the rule REFUSES, as against the
    #: companions it requires.
    not_beside: Tuple[str, ...] = ()
    #: 3.2.56 and 3.2.57 want the companion in the च्वि SENSE —
    #: अनाढ्यमाढ्यं करोति, making what was not so — while NOT actually
    #: carrying the च्वि affix. Two conditions, and the vṛtti asks
    #: after each separately, so they are two fields.
    cvi_sense: bool = False
    refuses_cvi_ending: bool = False
    #: 3.2.59's युज् and क्रुञ्च् take क्विन् केवलात्, with no
    #: companion at all — सोपपदात् तु 3.2.61 इत्यादिना क्विब् भवति.
    no_upapada: bool = False
    #: 3.2.71 and 3.2.72 hold मन्त्रे विषये — a narrower register than
    #: छन्दसि, which the vṛtti keeps distinct, so it is its own field.
    mantra: bool = False
    #: 3.2.66's अनन्तः पादम् — the root must NOT stand at the end of a
    #: metrical quarter. The only prosodic condition in the pāda, and
    #: the only one anywhere in the project so far that turns on where
    #: a word sits in a VERSE rather than on grammar.
    refuses_pada_final: bool = False
    #: 3.2.75's अन्येभ्यः — after roots that do NOT end in आ, which is
    #: the complement of 3.2.74 and not silence about it.
    not_a_final: bool = False
    #: 3.2.75's दृश्यन्ते. दृशिग्रहणं प्रयोगानुसरणार्थम् — 'are seen'
    #: is written so that one FOLLOWS USAGE, so the rule licenses
    #: attested forms and does not manufacture them. Without this the
    #: rule would give four affixes to every root in the language.
    attested: bool = False
    #: 3.2.78's अजातौ — the companion must NOT name a class. None is
    #: silence; False is the refusal the rule states.
    jati: object = None
    #: What role the thing likened to plays — the SAME question
    #: 3.1.10 and 3.1.11 divide on, and the same field they use.
    #: 3.2.79 कर्तर्युपमाने wants it as the agent, so the row
    #: carries 'kartṛ' rather than a bool of its own.
    upamana: str = ""
    #: भूते, the अधिकāra 3.2.84 opens and 3.2.123 closes. Every rule
    #: under it wants the act to be PAST, and none of them says so.
    past: bool = False
    #: A नियम: the rule does not provide but RESTRICTS one that
    #: already did. Four run together at 3.2.87–91 because 3.2.76 has
    #: already given क्विप् to every root there is. Carried for the
    #: record and for tests; it narrows nothing by itself, since what
    #: a नियम restricts to is exactly what its conditions state.
    niyama: bool = False
    #: A second affix the same rule gives beside the first.
    also: str = ""
    #: Extra weight a rule carries because the vṛtti says it is
    #: written to DEFEAT another — वेति वक्तव्ये पुनरण्ग्रहणं
    #: हेत्वादिषु टप्रतिषेधार्थम् at 3.2.44. Its stated conditions
    #: tie with 3.2.20's, and a tie would lose क्षेमकारः. The same
    #: device 3.1.109 and 3.1.141 needed.
    badhaka: bool = False
    why: str = ""


UPAPADA: Tuple[Upapada, ...] = (
    Upapada("3.2.1", "aṇ", role="karman",
            why="कर्मण्यण् — कुम्भकारः, नगरकारः; काण्डलावः; वेदाध्यायः. "
                "त्रिविधं कर्म: the vṛtti sorts the object into three "
                "kinds — what is brought into being, what is altered, "
                "what is reached — and gives an example of each, so "
                "that the rule is seen to cover all three. And it stops "
                "the rule by hand where usage has no word: ग्रामं "
                "गच्छति, आदित्यं पश्यति, हिमवन्तं शृणोति — न भवति, "
                "अनभिधानात्"),
    Upapada("3.2.2", "aṇ", of=HVADI, role="karman",
            why="ह्वावामश्च — स्वर्गह्वायः, तन्तुवायः, धान्यमायः. "
                "कप्रत्ययस्यापवादः: these three are आ-final and 3.2.3 "
                "would have given them क, so अण् is restored to them by "
                "name"),
    Upapada("3.2.3", "ka", a_final=True, upasarga=False, role="karman",
            why="आतोऽनुपसर्गे कः — गोदः, कम्बलदः, पार्ष्णित्रम्. "
                "अणोऽपवादः. अनुपसर्ग इति किम्? गोसंदायः, वडवासंदायः — "
                "with a preverb the अण् comes back"),
    Upapada("3.2.4", "ka", of=("sthā",), role="sup",
            why="सुपि स्थः — समस्थः, विषमस्थः. And the vṛtti wants the "
                "rule split — अत्र योगविभागः कर्तव्यः: सुपि alone gives "
                "क to आ-final roots after any word, द्विपः, पादपः, "
                "कच्छपः; and स्थः then adds स्था. What the second half "
                "buys is the भाव sense — अनेन भावेऽपि यथा स्यात्, "
                "आखूत्थः, शलभोत्थः — since the first would have given "
                "the agent only"),
    Upapada("3.2.5", "ka", of=("parimṛj", "apanud"),
            beside=("tunda", "śoka"), pairs=TUNDA_SOKA,
            role="karman",
            why="तुन्दशोकयोः परिमृजापनुदोः, यथासंख्यम् — तुन्दपरिमृज "
                "आस्ते, शोकापनुदः पुत्रो जातः. A vārttika fixes the "
                "senses: आलस्य for the first and सुखाहरण for the "
                "second, so अलसः तुन्दपरिमृज उच्यते but तुन्दपरिमार्ज "
                "एव अन्यः — the affix marks the idler, not the wiper"),
    Upapada("3.2.6", "ka", of=("dā", "jñā"), which_upasarga=("pra",),
            role="karman",
            why="प्रे दाज्ञः — सर्वप्रदः, पथिप्रज्ञः. अणोऽपवादः, and "
                "सोपसर्गार्थ आरम्भः: the rule exists only because 3.2.3 "
                "had shut preverbs out, so this lets one back in — the "
                "same shape as 3.1.72 against 3.1.71. प्र इति किम्? "
                "गोसंदायः"),
    Upapada("3.2.7", "ka", of=("khyā",), which_upasarga=("sam",),
            role="karman",
            why="समि ख्यः — गां संचष्टे गोसंख्यः. अणोऽपवादः, and "
                "सोपसर्गार्थ आरम्भः again. ख्या is itself what चक्षिङ् "
                "became by 2.4.54, which is codified"),
    Upapada("3.2.8", "ṭak", of=("gai", "pā"), upasarga=False,
            role="karman",
            why="गापोष्टक् — शक्रं गायति शक्रगः, सामगः, and the "
                "feminines शक्रगी, सामगी. कस्यापवादः. अनुपसर्ग इत्येव: "
                "शक्रसंगायः. A vārttika holds पा to two drinks — "
                "सुरापः, शीधुपः — and asks सुराशीध्वोरिति किम्? "
                "क्षीरपा ब्राह्मणी; पिबतेरिति किम्? सुरां पातीति "
                "सुरापा, where the root is 'protect' and not 'drink'"),
    Upapada("3.2.9", "ac", of=("hṛ",), role="karman",
            not_sense="udyamana",
            why="हरतेरनुद्यमनेऽच् — अंशं हरतीति अंशहरः, रिक्थहरः. "
                "अणोऽपवादः. उद्यमनम् उत्क्षेपणम्, the lifting up. "
                "अनुद्यमन इति किम्? भारहारः — of carrying a load the "
                "अण् stands"),
    Upapada("3.2.10", "ac", of=("hṛ",), role="karman", sense="vayas",
            why="वयसि च — अस्थिहरः श्वा, कवचहरः क्षत्रियकुमारः. "
                "उद्यमनार्थोऽयम् आरम्भः: this rule exists FOR the "
                "lifting sense 3.2.9 refused, where an age is meant. "
                "कालकृता शरीरावस्था यौवनादिर्वयः — the body's state as "
                "time makes it"),
    Upapada("3.2.11", "ac", of=("hṛ",), which_upasarga=("āṅ",),
            role="karman", sense="tācchīlya",
            why="आङि ताच्छील्ये — पुष्पाहरः, फलाहरः. ताच्छील्यं "
                "तत्स्वभावता, being that by nature: the vṛtti glosses "
                "it as picking flowers without an eye to the fruit of "
                "it. ताच्छील्य इति किम्? भाराहारः"),
    Upapada("3.2.12", "ac", of=("arh",), role="karman",
            why="अर्हः — पूजार्हा, गन्धार्हा, मालार्हा. अणोऽपवादः, and "
                "स्त्रीलिङ्गे विशेषः: the difference between the two "
                "affixes shows in the feminine"),
    Upapada("3.2.13", "ac", of=("ram", "jap"),
            beside=("stamba", "karṇa"), pairs=STAMBA_KARNA,
            role="sup",
            why="स्तम्बकर्णयो रमिजपोः, यथासंख्यम् — स्तम्बे रमत इति "
                "स्तम्बेरमो हस्ती, कर्णे जपतीति कर्णेजपः सूचकः. And "
                "the companion is a सुबन्त and NOT an object, which the "
                "vṛtti reasons out: रमेरकर्मकत्वात्, जपेः "
                "शब्दकर्मकत्वात् कर्म न संभवति — रम् takes no object at "
                "all and जप्'s object is a sound, so कर्मणि could not "
                "have been meant and सुपि is read instead. A condition "
                "settled by what the roots can do"),
    Upapada("3.2.14", "ac", beside=("śam",), role="sup", sense="saṃjñā",
            why="शमि धातोः संज्ञायाम् — शंकरः, शंभवः, शंवदः. And the "
                "vṛtti asks why धातोः is said when it is running "
                "already: धातुग्रहणं कृञो हेत्वादिषु टप्रतिषेधार्थम् — "
                "to keep 3.2.20's ट off कृ here, so शंकरा नाम "
                "परिव्राजिका is formed with अच् and not with ट"),
    Upapada("3.2.15", "ac", of=("śī",), role="adhikaraṇa",
            why="अधिकरणे शेतेः — खे शेत इति खशयः, गर्तशयः. सुपीति "
                "संबध्यते, so the companion is a finished word and "
                "the rule adds that it be the place"),
    Upapada("3.2.15", "ac", of=("śī",), beside=PARSVADI, role="sup",
            why="पार्श्वादिषूपसंख्यानम् — पार्श्वाभ्यां शेते "
                "पार्श्वशयः, उदरशयः, पृष्ठशयः. A vārttika, and what "
                "it buys is precisely that the companion NEED NOT be "
                "the place: पार्श्वाभ्याम् is instrumental. The "
                "members come from the गणपाठ on disk, which keys this "
                "gaṇa to this sūtra"),
    Upapada("3.2.15", "ac", of=("śī",), beside=PARSVADI, role="kartṛ",
            why="उत्तानादिषु कर्तृषु — उत्तानः शेत इति उत्तानशयः, "
                "अवमूर्धा शेते अवमूर्धशयः. A second vārttika over the "
                "same gaṇa, taking the companion as the AGENT. The "
                "corpus holds all five members together and the vṛtti "
                "divides them by which vārttika works them, so the "
                "rows share the list and differ by role"),
    Upapada("3.2.15", "ac", of=("śī",), beside=("digdhasaha",),
            role="sup",
            why="दिग्धसहपूर्वाच्च — दिग्धेन सह शेते दिग्धसहशयः"),
    Upapada("3.2.15", "ḍa", of=("śī",), beside=("giri",),
            role="adhikaraṇa", chandasi=True,
            why="गिरौ डश्छन्दसि — गिरौ शेते गिरिशः, in the Veda and "
                "with a DIFFERENT affix. The one vārttika of the four "
                "that changes what is added rather than what it is "
                "added after"),
    Upapada("3.2.16", "ṭa", of=("car",), role="adhikaraṇa",
            why="चरेष्टः — कुरुषु चरतीति कुरुचरः, मद्रचरः. And why a "
                "DIFFERENT affix from 3.2.15's: प्रत्ययान्तरकरणं "
                "ङीबर्थम् — so that the feminine takes ङीप्, कुरुचरी, "
                "मद्रचरी. An affix chosen for what it does two rules "
                "away"),
    Upapada("3.2.17", "ṭa", of=("car",), beside=BHIKSADI,
            why="भिक्षासेनादायेषु च — भिक्षाचरः, सेनाचरः, आदायचरः. "
                "अनधिकरणार्थ आरम्भः: the rule exists because none of "
                "the three is a place, which is what 3.2.16 wanted"),
    Upapada("3.2.18", "ṭa", of=("sṛ",), beside=PURASADI,
            why="पुरोऽग्रतोऽग्रेषु सर्तेः — पुरःसरः, अग्रतःसरः, "
                "अग्रेसरः"),
    Upapada("3.2.19", "ṭa", of=("sṛ",), beside=("pūrva",), role="kartṛ",
            why="पूर्वे कर्तरि — पूर्वः सरतीति पूर्वसरः. कर्तरीति "
                "किम्? पूर्वं देशं सरतीति पूर्वसारः — as an object the "
                "same word gives the other affix, so the role is the "
                "whole of the difference"),
    Upapada("3.2.20", "ṭa", of=("kṛ",), role="karman",
            sense="hetu-tācchīlya-ānulomya",
            why="कृञो हेतुताच्छील्यानुलोम्येषु — and the vṛtti glosses "
                "all three: हेतुरैकान्तिकं कारणम्, ताच्छील्यं "
                "तत्स्वभावता, आनुलोम्यम् अनुकूलता. शोककरी कन्या, "
                "यशस्करी विद्या; श्राद्धकरः; प्रैषकरः, वचनकरः. "
                "एतेष्विति किम्? कुम्भकारः, नगरकारः — outside the three "
                "senses 3.2.1's अण् stands"),
    Upapada("3.2.21", "ṭa", of=("kṛ",), beside=DIVADI, role="sup",
            why="दिवाविभानिशा… — दिवाकरः, विभाकरः, निशाकरः, प्रभाकरः, "
                "भास्करः, अन्तकरः, किंकरः, अहस्करः, धनुष्करः. "
                "अहेत्वाद्यर्थ आरम्भः: the rule exists for the senses "
                "3.2.20 did NOT cover, which is why it names its "
                "companions instead of a sense. And the vṛtti reads "
                "both कर्मणि and सुपि down into it — कर्मणि सुपीति च "
                "द्वयमप्यनुवर्तते, तत्र यथायोगं सम्बन्धः, each member "
                "taking whichever fits: दिवाशब्दोऽधिकरणवचनः"),
    Upapada("3.2.22", "ṭa", of=("kṛ",), beside=("karman",),
            role="karman", sense="bhṛti",
            why="कर्मणि भृतौ — कर्म करोतीति कर्मकरः, भृतक इत्यर्थः, a "
                "hired labourer. भृतिर्वेतनम्, कर्मनिर्वेशः — wages. "
                "कर्मणीति स्वरूपग्रहणम्: HERE कर्मन् is the word "
                "itself standing beside, not the kāraka 3.2.1 meant by "
                "the same word twenty-one rules back. भृताविति किम्? "
                "कर्मकारः"),
    Upapada("3.2.23", "ṭa", of=("kṛ",), beside=SABDADI, refuses=True,
            why="न शब्दश्लोककलहगाथावैरचाटुसूत्रमन्त्रपदेषु — शब्दकारः, "
                "श्लोककारः, सूत्रकारः, मन्त्रकारः. हेत्वादिषु "
                "प्राप्तः प्रतिषिध्यते: what is refused is the ट "
                "3.2.20 would have given in the three senses. The only "
                "प्रतिषेध of the run, and so the only rule here that "
                "may name itself in a refusal — but what these words "
                "actually GET is 3.2.1's अण्, and that is the rule "
                "reported, with the प्रतिषेध recorded beside it"),
    Upapada("3.2.24", "in", of=("kṛ",), beside=("stamba", "śakṛt"),
            role="karman", names_a="vrīhi-vatsa",
            why="स्तम्बशकृतोरिन् — स्तम्बकरिर्व्रीहिः, शकृत्करिर्वत्सः. "
                "SCOPE: व्रीहिवत्सयोरिति वक्तव्यम् is a vārttika, and "
                "it is codified as a condition rather than merely "
                "noted because the vṛtti's own counter turns on it — "
                "व्रीहिवत्सयोरिति किम्? स्तम्बकारः, शकृत्कारः"),
    Upapada("3.2.25", "in", of=("hṛ",), beside=("dṛti", "nātha"),
            role="karman", names_a="paśu",
            why="हरतेर्दृतिनाथयोः पशौ — दृतिं हरतीति दृतिहरिः पशुः, "
                "नाथहरिः पशुः. पशाविति किम्? दृतिहारः, नाथहारः. The "
                "condition is on what the finished word DENOTES, as "
                "3.2.10's वयस् was"),
    Upapada("3.2.27", "in", of=VANADI, role="karman", chandasi=True,
            why="छन्दसि वनसनरक्षिमथाम् — ब्रह्मवनिम्, गोसनिम्, "
                "पथिरक्षी, हविर्मथीनाम्, each with the Vedic passage "
                "the vṛtti cites for it. छन्दसि विषये: the rule holds "
                "in the Veda and not outside it"),
    Upapada("3.2.28", "khaś", of=("ej",), role="karman",
            causative=True,
            why="एजेः खश् — अङ्गमेजयति अङ्गमेजयः, जनमेजयः. ण्यन्तात्, "
                "from the CAUSATIVE stem and not the bare root. And "
                "the two markers do two different jobs: खकारो "
                "मुमर्थः, the ख is there for the मुम् augment that "
                "gives अङ्गम्-; शकारः सार्वधातुकसंज्ञार्थः, the श "
                "makes it सार्वधातुक by 3.4.113 तिङ्शित्सार्वधातुकम्, "
                "which is codified and so is asked"),
    Upapada("3.2.29", "khaś", of=("dhmā", "dheṭ"),
            beside=("nāsikā", "stana"), pairs=NASIKA_STANA,
            role="karman",
            why="नासिकास्तनयोर्ध्माधेटोः — नासिकन्धमः, नासिकन्धयः, "
                "स्तनन्धयः. AND यथासंख्यमत्र नेष्यते, the vṛtti "
                "refusing the pairing 3.2.5 and 3.2.13 required: स्तने "
                "धेटः, but नासिकायां तु ध्मश्च धेटश्च. What licenses "
                "the refusal is the WORDING — लक्षणव्यभिचारचिह्नाद् "
                "अल्पाच्तरस्यापूर्वनिपातनाल्लभ्यते: the shorter word "
                "would stand first by 2.2.34 अल्पाच्तरम्, and its not "
                "standing first is the sign the usual reading is off. "
                "धेटष्टित्त्वात् स्त्रियां ङीप्: स्तनन्धयी"),
    Upapada("3.2.30", "khaś", of=("dhmā", "dheṭ"), beside=NADI_MUSTI,
            role="karman",
            why="नाडीमुष्ट्योश्च — नाडिन्धमः, मुष्टिन्धयः, and every "
                "combination stands, both roots with both words. Here "
                "too the sign is in the wording: घ्यन्तस्यापूर्वनिपातो "
                "लक्षणव्यभिचारचिह्नम्, तेन संख्यातानुदेशो न भवति — "
                "the घि-final word not standing first, by 2.2.34's "
                "companion rules. अनुक्तसमुच्चयार्थश्चकारः gathers in "
                "घटि, खारि and वात besides: वातन्धमः पर्वतः"),
    Upapada("3.2.31", "khaś", of=("ruj", "vah"), beside=("kūla",),
            which_upasarga=("ud",), role="karman",
            why="उदि कूले रुजिवहोः — कूलमुद्रुजो रथः, कूलमुद्वहः"),
    Upapada("3.2.32", "khaś", of=("lih",), beside=("vaha", "abhra"),
            role="karman",
            why="वहाभ्रे लिहः — वहंलिहो गौः, अभ्रंलिहो वायुः"),
    Upapada("3.2.33", "khaś", of=("pac",), beside=PARIMANA,
            role="karman",
            why="परिमाणे पचः — प्रस्थंपचा स्थाली, द्रोणम्पचः, "
                "खारिम्पचः कटाहः. परिमाणं प्रस्थादि, an आकृतिगण, so "
                "the three named are examples and not the whole"),
    Upapada("3.2.34", "khaś", of=("pac",), beside=("mita", "nakha"),
            role="karman",
            why="मितनखे च — मितम्पचा ब्राह्मणी, नखम्पचा यवागूः. "
                "अपरिमाणार्थ आरम्भः: the rule exists because neither "
                "word is a measure, which is what 3.2.33 required — "
                "the same shape as 3.2.17 against 3.2.16"),
    Upapada("3.2.35", "khaś", of=("tud",), beside=("vidhu", "arus"),
            role="karman",
            why="विध्वरुषोस्तुदः — विधुन्तुदो राहुः, अरुन्तुदः"),
    Upapada("3.2.36", "khaś", of=("dṛś", "tap"),
            beside=("asūrya", "lalāṭa"), pairs=ASURYA_LALATA,
            role="karman",
            why="असूर्यललाटयोर्दृशितपोः, यथासंख्यम् — असूर्यम्पश्या "
                "राजदाराः, ललाटन्तप आदित्यः. And असूर्य is an "
                "असमर्थसमास, the vṛtti says, because the न belongs "
                "with दृश् and not with सूर्य: सूर्यं न पश्यन्तीति. "
                "गुप्तिपरं चैतत् — the word is about seclusion, एवं "
                "नाम गुप्ता यदपरिहार्यदर्शनं सूर्यमपि न पश्यन्तीति"),
    Upapada("3.2.38", "khac", of=("vad",), beside=("priya", "vaśa"),
            role="karman",
            why="प्रियवशे वदः खच् — प्रियंवदः, वशंवदः. खकारो मुमर्थः; "
                "चकारः खचि ह्रस्वः (6.4.94) इति विशेषणार्थः, the च "
                "written so a rule four adhyāyas on can name this "
                "affix. प्रत्ययान्तरकरणमुत्तरार्थम् — a DIFFERENT "
                "affix from the खश् before, for the sake of the rules "
                "after: the third time this pāda chooses an affix for "
                "what a later rule does with it, after 3.2.12 and "
                "3.2.16"),
    Upapada("3.2.39", "khac", of=("tap",), beside=("dviṣat", "para"),
            role="karman",
            why="द्विषत्परयोस्तापेः — द्विषन्तपः, परन्तपः. तप दाहे "
                "चुरादिः and तप संतापे भ्वादिः, द्वयोरपि ग्रहणम् — "
                "both roots written alike are meant, so this rule "
                "unlike 3.2.28 does not turn on the causative. "
                "द्विषत्परयोरिति द्वितकारको निर्देशः, तेन स्त्रियां न "
                "भवति: the spelling with two त् keeps the feminine "
                "out, द्विषतीतापः"),
    Upapada("3.2.40", "khac", of=("yam",), beside=("vāc",),
            role="karman", sense="vrata",
            why="वाचि यमो व्रते — वाचंयम आस्ते, one under a vow of "
                "silence. व्रत इति शास्त्रितो नियम उच्यते, a restraint "
                "laid down by rule. व्रत इति किम्? वाग्यामः"),
    Upapada("3.2.41", "khac", of=("dṝ", "sah"), beside=("pur", "sarva"),
            pairs=PUR_SARVA, role="karman",
            why="पूःसर्वयोर्दारिसहोः, यथासंख्यम् — पुरं दारयति "
                "पुरंदरः; सर्वंसहो राजा. SCOPE: भगे च दारेरिति "
                "वक्तव्यम्, भगन्दरः"),
    Upapada("3.2.42", "khac", of=("kaṣ",), beside=SARVAKULADI,
            role="karman",
            why="सर्वकूलाभ्रकरीषेषु कषः — सर्वंकषः खलः, कूलंकषा नदी, "
                "अभ्रंकषो गिरिः, करीषंकषा वात्या"),
    Upapada("3.2.43", "khac", of=("kṛ",), beside=MEGHADI,
            role="karman", tadanta=True,
            why="मेघर्तिभयेषु कृञः — मेघंकरः, ऋतिंकरः, भयंकरः. AND "
                "उपपदविधौ भयादिग्रहणं तदन्तविधिं प्रयोजयति: naming "
                "भय in an उपपद rule brings 1.1.72 येन विधिस्तदन्तस्य "
                "into play, so a word ENDING in भय is reached too — "
                "अभयंकरः. 1.1.72 is codified, so it is asked"),
    Upapada("3.2.44", "aṇ", of=("kṛ",), beside=KSEMADI, role="karman",
            also="खच्", badhaka=True,
            why="क्षेमप्रियमद्रेऽण् च — क्षेमकारः and क्षेमंकरः, "
                "प्रियकारः and प्रियंकरः, मद्रकारः and मद्रंकरः: "
                "चकारात् खच्च, so BOTH affixes stand and the rule "
                "gives two forms for each word. And the vṛtti asks why "
                "अण् is stated when वा would have done — वेति वक्तव्ये "
                "पुनरण्ग्रहणं हेत्वादिषु टप्रतिषेधार्थम्: to keep "
                "3.2.20's ट out. The second rule of this pāda to "
                "repeat a word for that purpose, after 3.2.14"),
    Upapada("3.2.45", "khac", of=("bhū",), beside=("āśita",),
            role="sup", sense="karaṇa-bhāva",
            why="आशिते भुवः करणभावयोः — अत्र सुपीत्युपतिष्ठते, सुपि "
                "and not कर्मणि stands here. आशितो भवत्यनेन "
                "आशितंभव ओदनः, the rice by WHICH one is fed — the "
                "instrument; and आशितस्य भवनम् आशितंभवं वर्तते — the "
                "act itself. One rule, two senses, both named"),
    Upapada("3.2.46", "khac", of=BHRADI, role="sup", sense="saṃjñā",
            why="संज्ञायां भृतॄवृजिधारिसहितनिषु — विश्वम्भरा, "
                "वसुन्धरा, रथंतरं साम, पतिंवरा कन्या, शत्रुंजयो "
                "हस्ती, युगंधरः पर्वतः, शत्रुंसहः, शत्रुंतपः, "
                "अरिंदमः. कर्मणीति सुपीति च प्रकृतं संज्ञावशाद् "
                "यथासंभवं संबध्यते — both run down and the संज्ञा "
                "settles which applies to which. संज्ञायामिति किम्? "
                "कुटुम्बभारः"),
    Upapada("3.2.47", "khac", of=("gam",), role="sup", sense="saṃjñā",
            why="गमश्च — सुतंगमो नाम, यस्य पुत्रः सौतंगमिः. "
                "योगविभाग उत्तरार्थः: split from 3.2.46 for the sake "
                "of the rule after, the same device as 3.1.147"),
    Upapada("3.2.48", "ḍa", of=("gam",),
            beside=ANTADI + ANTADI_VARTTIKA, role="karman",
            why="अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः — अन्तगः, "
                "अध्वगः, दूरगः, पारगः, सर्वगः. डकारः टिलोपार्थः, the "
                "ड marked so the टि is dropped. AND संज्ञायामिति "
                "नानुवर्तते: the संज्ञा condition running through "
                "3.2.46 and 3.2.47 STOPS here — an अनुवृत्ति ended by "
                "the commentary rather than by the text. SCOPE: five "
                "vārttikas add सर्वत्रगः, पन्नगः, उरगः (उरसो लोपश्च), "
                "सुगः and दुर्गः (सुदुरोरधिकरणे), निर्गो देशः (निरो "
                "देशे) — and then decline to close the list: "
                "डप्रकरणेऽन्येष्वपि दृश्यत इति, स्त्र्यगारगः, "
                "ग्रामगः"),
    Upapada("3.2.49", "ḍa", of=("han",), role="karman", sense="āśis",
            why="आशिषि हनः — तिमिं वध्यात् तिमिहः, शत्रुहः. आशिषीति "
                "किम्? शत्रुघातः. SCOPE: three vārttikas give अण् "
                "instead with आ+हन् and सम्+हन्, and a ट for the "
                "root's final — दार्वाघाटः, चार्वाघाटः beside "
                "चार्वाघातः, वर्णसंघाटः beside वर्णसंघातः"),
    Upapada("3.2.50", "ḍa", of=("han",), which_upasarga=("apa",),
            beside=("kleśa", "tamas"), role="karman",
            why="अपे क्लेशतमसोः — क्लेशापहः पुत्रः, तमोऽपहः सूर्यः. "
                "अनाशीरर्थ आरम्भः: the rule exists for the sense "
                "3.2.49 did NOT cover — not a blessing — which is the "
                "third time this pāda writes a rule to reach past the "
                "condition of the rule before it, after 3.2.10 and "
                "3.2.34"),
    Upapada("3.2.51", "ṇini", of=("han",),
            beside=("kumāra", "śīrṣa"), role="karman",
            why="कुमारशीर्षयोर्णिनिः — कुमारघाती, शीर्षघाती. "
                "निपातनाच्छिरसः शीर्षभावः: शिरस् becomes शीर्ष by the "
                "fixing in this sūtra and by no rule"),
    Upapada("3.2.52", "ṭak", of=("han",), beside=("jāyā", "pati"),
            role="karman", sense="lakṣaṇa",
            why="लक्षणे जायापत्योष्टक् — जायाघ्नो ब्राह्मणः, पतिघ्नी "
                "वृषली, of one who bears the MARK of it. The vṛtti "
                "offers two readings and settles neither: लक्षणवति "
                "कर्तरि, the agent having the mark; अथ वा लक्षणे "
                "द्योत्ये, the mark being what the word conveys"),
    Upapada("3.2.53", "ṭak", of=("han",), role="karman",
            agent="amanuṣya",
            why="अमनुष्यकर्तृके च — जायाघ्नस्तिलकालकः, पतिघ्नी "
                "पाणिरेखा, श्लेष्मघ्नं मधु, पित्तघ्नं घृतम्. "
                "अमनुष्यकर्तृक इति किम्? आखुघातः शूद्रः. DEBT: the "
                "vṛtti then asks why चौरघातो हस्ती is not formed here "
                "though an elephant is no man, and answers by 3.3.113 "
                "कृत्यल्युटो बहुलम् — बहुलवचनाद् अण् भवति. 3.3.113 is "
                "NOT codified, so that answer cannot be reached from "
                "here and is recorded rather than run"),
    Upapada("3.2.54", "ṭak", of=("han",),
            beside=("hastin", "kapāṭa"), role="karman", sense="śakti",
            why="शक्तौ हस्तिकपाटयोः — हस्तिनं हन्तुं शक्तो हस्तिघ्नो "
                "मनुष्यः; कं पाटयति प्रविशतीति कपाटघ्नश्चौरः. "
                "मनुष्यकर्तृकार्थ आरम्भः is the vṛtti's REASON for the "
                "rule — it reaches the human agent 3.2.53 excluded — "
                "but the rule states शक्तौ and not that, so the "
                "condition codified is the one written. शक्ताविति "
                "किम्? विषेण हस्तिनं हन्ति हस्तिघातः"),
    Upapada("3.2.56", "khyun", of=("kṛ",), beside=ADHYADI,
            role="karman", sense="karaṇa", cvi_sense=True,
            refuses_cvi_ending=True,
            why="आढ्यसुभगस्थूलपलितनग्नान्धप्रियेषु च्व्यर्थेष्वच्वौ "
                "कृञः करणे ख्युन् — अनाढ्यमाढ्यं कुर्वन्त्यनेन "
                "आढ्यंकरणम्, सुभगंकरणम्. TWO conditions on the "
                "companion and the vṛtti asks after each: च्व्यर्थेष्व "
                "इति किम्? आढ्यं तैलेन कुर्वन्ति, merely anointing, "
                "where nothing BECOMES what it was not; अच्वाविति "
                "किम्? आढ्यीकुर्वन्त्यनेन, where the च्वि is actually "
                "there. And a fine argument on the प्रतिषेध: ननु च "
                "ख्युना मुक्ते ल्युटा भवितव्यम् — if ख्युन् is "
                "refused, ल्युट् should come, and the two are "
                "indistinguishable, so what has the refusal bought? "
                "प्रतिषेधसामर्थ्यात् ख्युन्यसति ल्युडपि न भवति: the "
                "very force of refusing keeps ल्युट् out too"),
    Upapada("3.2.57", "khiṣṇuc", of=("bhū",), beside=ADHYADI,
            role="sup", cvi_sense=True, refuses_cvi_ending=True,
            also="खुकञ्",
            why="कर्तरि भुवः खिष्णुच्खुकञौ — TWO affixes, both "
                "standing: अनाढ्य आढ्यो भवति आढ्यंभविष्णुः and "
                "आढ्यंभावुकः, सुभगंभविष्णुः and सुभगंभावुकः. "
                "कर्तरीति किम्? करणे मा भूत् — the agent here, where "
                "3.2.56 wanted the instrument, which is the whole "
                "difference between the two rules. च्व्यर्थेष्वित्येव "
                "and अच्वावित्येव, both carried down"),
    Upapada("3.2.58", "kvin", of=("spṛś",), role="sup",
            not_beside=("udaka",),
            why="स्पृशोऽनुदके क्विन् — घृतस्पृक्, मन्त्रस्पृक्, "
                "जलस्पृक्. अनुदक इति किम्? उदकस्पर्शः. AND the vṛtti "
                "reasons out why the companion is any सुबन्त and not "
                "the object: सकर्मकत्वात् स्पृशेः कर्मैवोपपदं "
                "प्राप्नोति? — स्पृश् takes an object, so surely that "
                "is meant. नैष दोषः: कर्तरि runs down from 3.2.57 and "
                "is read as कर्तृप्रचय, which lets any सुबन्त stand — "
                "hence मन्त्रेण स्पृशन्ति मन्त्रस्पृक्, an "
                "instrument. नकारः क्विन्प्रत्ययस्य कुः (8.2.62) इति "
                "विशेषणार्थः, the न written so a rule five adhyāyas "
                "on can name this affix"),
    Upapada("3.2.59", "kvin", of=("añc",), role="sup",
            why="अञ्चेः सुबन्तमात्र उपपदे — प्राङ्, प्रत्यङ्, उदङ्. "
                "One of the three roots this sūtra gives क्विन् BY "
                "RULE, as against the five words it fixes outright"),
    Upapada("3.2.59", "kvin", of=("yuj", "kruñc"), no_upapada=True,
            why="युजेः क्रुञ्चेश्च केवलादेव — युङ्, युञ्जौ, युञ्जः; "
                "क्रुङ्, क्रुञ्चौ, क्रुञ्चः. केवलात्, from the BARE "
                "root with no companion at all: सोपपदात् तु "
                "सत्सूद्विष० इत्यादिना क्विब् भवति, अश्वयुक् — with a "
                "companion it is 3.2.61's क्विप् and not this. "
                "नलोपः कस्माद् न भवति? निपातनसाहचर्यात् — the न is not "
                "dropped, by the company these roots keep with the "
                "fixed words in the same sūtra"),
    Upapada("3.2.60", "kañ", of=("dṛś",), beside=TYADADI, role="sup",
            not_sense="ālocana", also="क्विन्",
            why="त्यदादिषु दृशोऽनालोचने कञ् च — त्यादृशः and त्यादृक्, "
                "तादृशः and तादृक्, यादृशः and यादृक्: चकारात् क्विन् "
                "च, so both affixes stand. अनालोचन इति किम्? तं "
                "पश्यति तद्दर्शः — and the vṛtti explains that these "
                "are रूढिशब्द, settled words, नैवात्र दर्शनक्रिया "
                "विद्यते, no act of seeing in them at all. कञो ञकारो "
                "विशेषणार्थः, for 4.1.15 ठक्ठञ्कञ्. SCOPE: "
                "समानान्ययोश्चेति वक्तव्यम् gives सदृशः, अन्यादृशः; "
                "दृशेः क्सश्च वक्तव्यः gives तादृक्षः, कीदृक्षः"),
    Upapada("3.2.61", "kvip", of=SADADI, role="sup",
            why="सत्सूद्विषद्रुहदुहयुजविदभिदच्छिदजिनीराजामुपसर्गेऽपि "
                "क्विप् — शुचिषत्, अण्डसूः, मित्रद्विट्, मित्रध्रुक्, "
                "गोधुक्, अश्वयुक्, वेदवित्, काष्ठभित्, रज्जुच्छिद्, "
                "शत्रुजित्, सेनानीः, सम्राट्. उपसर्गेऽपि, so both "
                "प्रद्विट् and मित्रद्विट् stand. AND कर्मग्रहणं तु "
                "न व्याप्रियते: the कर्म of the earlier rules has "
                "stopped running by 3.2.58, and only सुपि comes down. "
                "उपसर्गग्रहणं ज्ञापनार्थम् — the mention of the preverb "
                "is a ज्ञापक, telling us that ELSEWHERE, where सुप् is "
                "mentioned, a preverb is not, as at 3.1.106. And the "
                "vṛtti closes by making the rule redundant: "
                "अन्येभ्योऽपि दृश्यते, क्विप् च इति सामान्येन वक्ष्यति, "
                "तस्यैवायं प्रपञ्चः — 3.2.75 and 3.2.76 say this in "
                "general, and this rule is only their expansion"),
    Upapada("3.2.62", "ṇvi", of=("bhaj",), role="sup",
            why="भजो ण्विः — अर्धं भजते अर्धभाक्; उपसर्गेऽपि, प्रभाक्"),
    Upapada("3.2.63", "ṇvi", of=("sah",), role="sup", chandasi=True,
            why="छन्दसि सहः — तुराषाट्. सहेः साडः सः (8.3.56) gives the "
                "ष, and अन्येषामपि दृश्यते (6.3.137) the long vowel"),
    Upapada("3.2.64", "ṇvi", of=("vah",), role="sup", chandasi=True,
            why="वहश्च — प्रष्ठवाट्, दित्यवाट्. योगविभाग उत्तरार्थः: "
                "split from 3.2.63 for the sake of the rules after, "
                "which want वह् and not सह्"),
    Upapada("3.2.65", "ñyuṭ", of=("vah",),
            beside=("kavya", "purīṣa", "purīṣya"), chandasi=True,
            why="कव्यपुरीषपुरीष्येषु ञ्युट् — कव्यवाहनः पितॄणाम्, "
                "पुरीषवाहणः, पुरीष्यवाहनः, each from a Vedic passage "
                "the vṛtti cites"),
    Upapada("3.2.66", "ñyuṭ", of=("vah",), beside=("havya",),
            chandasi=True, refuses_pada_final=True,
            why="हव्येऽनन्तः पादम् — अग्निश्च हव्यवाहनः. THE CONDITION "
                "IS PROSODIC AND NOT GRAMMATICAL: the root must not "
                "stand at the end of a पाद, a metrical quarter. "
                "अनन्तः पादमिति किम्? हव्यवाडग्निरजरः पिता नः — at the "
                "quarter's end the other form stands. The only rule in "
                "this pāda, and the first in the project, whose "
                "condition is where a word sits in a VERSE"),
    Upapada("3.2.67", "viṭ", of=JANADI, role="sup", chandasi=True,
            why="जनसनखनक्रमगमो विट् — अब्जाः, गोजाः, गोषाः, नृषाः, "
                "बिसखाः, दधिक्राः, अग्रेगा नेतॄणाम्. टकारः "
                "सामान्यग्रहणाविघातार्थः for 6.1.67 वेरपृक्तस्य and "
                "विशेषणार्थः for 6.4.41 विड्वनोरनुनासिकस्यात् — one "
                "marker doing two jobs in two later rules"),
    Upapada("3.2.68", "viṭ", of=("ad",), role="sup",
            not_beside=("anna",),
            why="अदोऽनन्ने — आममत्ति आमात्, सस्यात्. अनन्न इति किम्? "
                "अन्नादः. AND छन्दसीति निवृत्तम्: the Vedic condition "
                "that ran through 3.2.63–67 STOPS here, so this rule "
                "holds in ordinary speech too. The second अनुवृत्ति in "
                "this pāda ended by the commentary rather than the "
                "text, after 3.2.48"),
    Upapada("3.2.69", "viṭ", of=("ad",), beside=("kravya",),
            badhaka=True,
            why="क्रव्ये च — क्रव्यमत्ति क्रव्यात्. AND पूर्वेणैव सिद्धे "
                "वचनम् असरूपबाधनार्थम्, तेन अण् न भवति: 3.2.68 gives "
                "it already, and this is stated to keep out the "
                "असरूप अण् that 3.1.94 would otherwise let stand "
                "beside it. A third rule repeated to defeat another, "
                "after 3.1.109 and 3.2.44 — and the vṛtti then "
                "explains the form that DOES have अण्: कथं तर्हि "
                "क्रव्यादः? कृत्तविकृत्तशब्द उपपदेऽण्, तस्य च "
                "पृषोदरादिपाठात् क्रव्यभावः — so the two words differ "
                "in sense, क्रव्यादः eating cut and cooked flesh, "
                "क्रव्यात् eating it raw"),
    Upapada("3.2.70", "kap", of=("duh",), role="sup",
            why="दुहः कब् घश्च — कामदुघा धेनुः, अर्घदुघा, घर्मदुघा. "
                "घकारश्चान्तादेशः, the घ replacing the root's final"),
    Upapada("3.2.71", "ṇvin", of=("vah",), beside=("śveta",),
            role="karman", mantra=True,
            why="मन्त्रे श्वेतवहोक्थशस्पुरोडाशो ण्विन् — श्वेता एनं "
                "वहन्ति श्वेतवा इन्द्रः. AND THE SŪTRA IS PART FIXING "
                "AND PART RULE, which the vṛtti separates precisely: "
                "धातूपपदसमुदाया निपात्यन्ते अलाक्षणिककार्यसिद्ध्यर्थम्, "
                "प्रत्ययस्तु विधीयत एव — the whole root-and-companion "
                "compounds are fixed so that their irregular "
                "operations come out, but the AFFIX is genuinely "
                "prescribed. So the rows give the affix and the notes "
                "carry what is fixed. SCOPE: श्वेतवहादीनां डस्पदस्य "
                "gives श्वेतवोभ्याम्; पदस्येति किम्? श्वेतवाहौ"),
    Upapada("3.2.71", "ṇvin", of=("śaṃs",), beside=("uktha",),
            role="karman", mantra=True,
            why="उक्थानि शंसति उक्थैर्वा शंसति उक्थशा यजमानः — the "
                "companion may be the object or the instrument, "
                "कर्मणि करणे वा, and नलोपश्च निपात्यते, the loss of "
                "the न being fixed here"),
    Upapada("3.2.71", "ṇvin", of=("dāś",), beside=("puras",),
            role="karman", mantra=True,
            why="पुरो दाशन्त एनं पुरोडाः — दाशृ दाने with पुरस् before, "
                "and इत्येतस्य पुरःपूर्वस्य डत्वम्, the ड fixed"),
    Upapada("3.2.72", "ṇvin", of=("yaj",), which_upasarga=("ava",),
            mantra=True,
            why="अवे यजः — त्वं यज्ञे वरुणस्यावया असि. योगविभाग "
                "उत्तरार्थः, split from 3.2.71 for the rule after"),
    Upapada("3.2.73", "vic", of=("yaj",), which_upasarga=("upa",),
            chandasi=True,
            why="विजुपे छन्दसि — उपयड्भिरूर्ध्वं वहन्ति, उपयट्त्वम्. "
                "छन्दोग्रहणं ब्राह्मणार्थम्, the mention of छन्दस् "
                "being for the Brāhmaṇa texts. विचः चित्करणं "
                "सामान्यग्रहणाविघातार्थम् for 6.1.67. AND THE RULE IS "
                "A नियम AND NOT A PROVISION, which the vṛtti argues "
                "out: किमर्थमिदमुच्यते, यावता अन्येभ्योऽपि दृश्यन्ते "
                "इति यजेरपि विच् सिद्ध एव? — why say this at all, when "
                "3.2.75 gives यज् its विच् already? यजेर्नियमार्थमेतत्: "
                "it exists to RESTRICT — उपयजेश्छन्दस्येव, न भाषायाम्, "
                "only in the Veda and not in speech. A rule whose "
                "whole work is to narrow another"),
    Upapada("3.2.74", "manin", a_final=True, role="sup", chandasi=True,
            also="क्वनिप्, वनिप्, विच्",
            why="आतो मनिन्क्वनिब्वनिपश्च — सुदामा, अश्वत्थामा; क्वनिप् "
                "सुधीवा, सुपीवा; वनिप् भूरिदावा, घृतपावा; and चकाराद् "
                "विज् भवति, a FOURTH affix from the च — कीलालपाः, "
                "शुभंयाः, रामस्योपदाः. सुप्युपसर्गेऽपि, so a preverb "
                "does not stop it"),
    Upapada("3.2.75", "manin", not_a_final=True, attested=True,
            also="क्वनिप्, वनिप्, विच्",
            why="अन्येभ्योऽपि दृश्यन्ते — सुशर्मा; क्वनिप् प्रातरित्वा; "
                "वनिप् विजावा, अग्रेगावा; विच् रेडसि. छन्दसीति "
                "निवृत्तम्, so it is not held to the Veda. AND THE "
                "RULE IS DELIBERATELY OPEN AT EVERY JOINT: "
                "अपिशब्दः सर्वोपाधिव्यभिचारार्थः — the अपि is there so "
                "that EVERY condition may be departed from — and "
                "निरुपपदादपि भवति, it works with no companion at all, "
                "धीवा, पीवा. What holds it back from swallowing the "
                "language is दृशिग्रहणं प्रयोगानुसरणार्थम्: 'are SEEN' "
                "is written so that one follows USAGE, so the rule "
                "licenses attested forms rather than manufacturing "
                "them — which is why it is codified with a condition "
                "the caller must assert"),
    Upapada("3.2.76", "kvip", attested=True,
            why="क्विप् च — सर्वधातुभ्यः सोपपदेभ्यो निरुपपदेभ्यश्च, "
                "छन्दसि भाषायां च: उखायाः स्रंसते उखास्रत्, पर्णध्वत्, "
                "वाहाभ्रट्. The widest rule in the pāda — every root, "
                "with a companion or without, in the Veda and in "
                "speech — and it is what makes the four नियम rules at "
                "3.2.87 to 3.2.91 necessary, since after this there is "
                "nothing left to provide. Held to attested forms for "
                "the reason 3.2.75 is: read as a bare provision it "
                "would put क्विप् after everything"),
    Upapada("3.2.77", "ka", of=("sthā",), beside=("śam",),
            role="sup", badhaka=True, also="क्विप्",
            why="स्थः क च — and the vṛtti asks why it is said at all: "
                "किमर्थमिदमुच्यते, यावता सुपि स्थः इति कः सिद्ध एव, "
                "अन्येभ्योऽपि दृश्यते इति क्विप्? 3.2.4 gives the क "
                "and 3.2.178 the क्विप् already. बाधकबाधनार्थं "
                "पुनर्वचनम् — it is repeated to DEFEAT: शमि धातोः "
                "संज्ञायाम् (3.2.14) would give अच्, and this beats it, "
                "शंस्थः, शंस्थाः. The fourth बाधकबाधन of the project, "
                "after 3.1.109, 3.2.44 and 3.2.69 — and the row is "
                "held to शम्, which is the whole of where the "
                "repetition does work: everywhere else 3.2.4 gives "
                "the same क already, and left general the weight "
                "displaced that rule for its own समस्थः"),
    Upapada("3.2.78", "ṇini", role="sup", jati=False,
            sense="tācchīlya",
            why="सुप्यजातौ णिनिस्ताच्छील्ये — उष्णभोजी, शीतभोजी. "
                "अजाताविति किम्? ब्राह्मणानामन्त्रयिता — a class-word "
                "beside, and the affix does not come. ताच्छील्य इति "
                "किम्? उष्णं भुङ्क्ते कदाचित्, once and not by habit. "
                "AND सुपीति वर्तमाने पुनः सुब्ग्रहणम् "
                "उपसर्गनिवृत्त्यर्थम्: सुप् is already running, and "
                "saying it again is how the PREVERB is stopped — a "
                "word repeated not to add but to end something else. "
                "SCOPE: three vārttikas, उत्प्रतिभ्यामाङि सर्तेः "
                "(उदासारिण्यः), साधुकारिणि च (साधुकारी), ब्रह्मणि वदः "
                "(ब्रह्मवादिनो वदन्ति)"),
    Upapada("3.2.79", "ṇini", role="sup", upamana="kartṛ",
            why="कर्तर्युपमाने — उष्ट्र इव क्रोशति उष्ट्रक्रोशी, "
                "ध्वाङ्क्षरावी. उपपदकर्ता प्रत्ययार्थस्य कर्तुरुपमानम्: "
                "the companion is the agent of ITS own act and what "
                "the rule's agent is likened TO. कर्तरीति किम्? "
                "अपूपानिव भक्षयति माषान् — likened as object, and the "
                "affix does not come. उपमान इति किम्? उष्ट्रः क्रोशति. "
                "अताच्छील्यार्थ आरम्भः — written to reach past 3.2.78's "
                "condition, the fourth time this pāda does that"),
    Upapada("3.2.80", "ṇini", role="sup", sense="vrata",
            why="व्रते — स्थण्डिलशायी, अश्राद्धभोजी. व्रत इति शास्त्रतो "
                "नियम उच्यते, a restraint laid down by rule, and "
                "कामचारप्राप्तौ नियमः, a restriction where freedom "
                "would otherwise hold: सति शयने स्थण्डिल एव शेते "
                "नान्यत्र. AND समुदायोपाधिश्चायम्, "
                "धातूपपदप्रत्ययसमुदायेन व्रतं गम्यते — the condition "
                "attaches to the WHOLE, root and companion and affix "
                "together, not to any part of it. व्रत इति किम्? "
                "स्थण्डिले शेते देवदत्तः"),
    Upapada("3.2.81", "ṇini", role="sup", sense="ābhīkṣṇya",
            why="बहुलमाभीक्ष्ण्ये — कषायपायिणो गान्धाराः, क्षीरपायिण "
                "उशीनराः. आभीक्ष्ण्यं पौनःपुन्यम्, तात्पर्यमासेवैव, "
                "ताच्छील्यादन्यत् — again and again, an intentness, "
                "and expressly NOT 3.2.78's ताच्छील्य. The second "
                "time this project has had to keep two senses of one "
                "region apart, after 3.1.149's समभिहार against "
                "3.1.22's. बहुलग्रहणात् the rule is not everywhere: "
                "कुल्माषखाद इत्यत्र न भवति"),
    Upapada("3.2.82", "ṇini", of=("man",), role="sup",
            why="मनः — दर्शनीयमानी, शोभनमानी. AND THE ROOT IS PINNED "
                "BY WHAT A LATER RULE WOULD DO: बहुलग्रहणानुवृत्तेर् "
                "मन्यतेर्ग्रहणम्, न मनुतेः — मन्यते of class four and "
                "not मनुते of class eight, उत्तरसूत्रे हि खश्प्रत्यये "
                "विकरणकृतो विशेषः स्यात्, because with 3.2.83's खश् "
                "the class-marker would show a difference. A root "
                "disambiguated by a consequence one rule downstream"),
    Upapada("3.2.83", "khaś", of=("man",), role="sup",
            sense="ātmamāna", also="णिनि",
            why="आत्ममाने खश् च — आत्मनो मननम् आत्ममानः, thinking it "
                "of ONESELF: दर्शनीयमात्मानं मन्यते दर्शनीयंमन्यः, and "
                "चकाराद् णिनिश्च, दर्शनीयमानी. पण्डितंमन्यः, "
                "पण्डितमानी. आत्ममान इति किम्? दर्शनीयमानी "
                "देवदत्तस्य यज्ञदत्तः — thought of another, and this "
                "rule does not reach it"),
    Upapada("3.2.85", "ṇini", of=("yaj",), role="karaṇa", past=True,
            why="करणे यजः — अग्निष्टोमेनेष्टवान् अग्निष्टोमयाजी. "
                "अग्निष्टोमः फलभावनायां करणं भवति. णिनिरनुवर्तते, न "
                "खश् — only the one affix comes down from 3.2.83, not "
                "both. And 3.2.84's भूते is running: भूत इति किम्? "
                "अग्निष्टोमेन यजते"),
    Upapada("3.2.86", "ṇini", of=("han",), role="karman", past=True,
            sense="kutsā",
            why="कर्मणि हनः — पितृव्यघाती, मातुलघाती. SCOPE made a "
                "condition: कुत्सितग्रहणं कर्तव्यम्, a vārttika adding "
                "that the killing be blameworthy — इह मा भूत् चौरं "
                "हतवान्. Codified rather than merely recorded, since "
                "the counter-example turns on it"),
    Upapada("3.2.87", "kvip", of=("han",), beside=BRAHMADI,
            role="karman", past=True, niyama=True,
            why="ब्रह्मभ्रूणवृत्रेषु क्विप् — ब्रह्महा, भ्रूणहा, "
                "वृत्रहा. AND IT PROVIDES NOTHING: किमर्थमिदमुच्यते, "
                "यावता सर्वधातुभ्यः क्विब् विहित एव? — 3.2.76 has given "
                "क्विप् to every root already. ब्रह्मादिषु हन्तेः "
                "क्विब्वचनं नियमार्थम्, and the vṛtti counts the "
                "restriction FOURFOLD: only after these companions and "
                "no other; only from हन् and no other root; only "
                "क्विप् and no other affix; only in the past. "
                "तदेतद् वक्ष्यमाणबहुलग्रहणस्य पुरस्तादपकर्षणाद् "
                "लभ्यते — and that reading is got by dragging 3.2.88's "
                "बहुल BACKWARD over this rule"),
    Upapada("3.2.88", "kvip", of=("han",), chandasi=True, past=True,
            why="बहुलं छन्दसि — मातृहा, पितृहा, with companions 3.2.87 "
                "does not name. पूर्वेण नियमाद् अप्राप्तः क्विप् "
                "प्रत्ययो विधीयते: what the नियम before shut out is "
                "given back here, for the Veda. न च भवति मातृघातः — "
                "and बहुलम् is why the other form still stands"),
    Upapada("3.2.89", "kvip", of=("kṛ",), beside=SUKARMADI,
            role="karman", past=True, niyama=True,
            why="सुकर्मपापमन्त्रपुण्येषु कृञः — सुकृत्, कर्मकृत्, "
                "पापकृत्, मन्त्रकृत्, पुण्यकृत्. कर्मणीति वर्तते, "
                "तदसंभवात् सुशब्दं वर्जयित्वा — सु cannot be an object, "
                "so the कर्म qualifies the other four only. "
                "अयमपि नियमार्थ आरम्भः, and here the restriction is "
                "THREEFOLD and not fourfold: धातुनियमं वर्जयित्वा "
                "कालोपपदप्रत्ययनियमः — the root is NOT restricted, so "
                "other companions do work, शास्त्रकृत्, भाष्यकृत्. The "
                "vṛtti counting the kinds of restriction rule by rule "
                "is what makes the difference visible"),
    Upapada("3.2.90", "kvip", of=("su",), beside=("soma",),
            role="karman", past=True, niyama=True,
            why="सोमे सुञः — सोमसुत्, सोमसुतौ, सोमसुतः. अयमपि "
                "नियमार्थ आरम्भः, चतुर्विधश्चात्र नियम इष्यते, "
                "धातुकालोपपदप्रत्ययविषयः — fourfold again, the root "
                "restricted here where 3.2.89 left it free"),
    Upapada("3.2.91", "kvip", of=("ci",), beside=("agni",),
            role="karman", past=True, niyama=True,
            why="अग्नौ चेः — अग्निचित्, अग्निचितौ, अग्निचितः. "
                "अत्रापि पूर्ववच्चतुर्विधो नियम इष्यते"),
    Upapada("3.2.92", "kvip", of=("ci",), role="karman", past=True,
            names_a="agni",
            why="कर्मण्यग्न्याख्यायाम् — श्येन इव चीयते श्येनचित्, "
                "कङ्कचित्. धातूपपदप्रत्ययसमुदायेन चेद् अग्न्याख्या "
                "गम्यते: the whole must NAME a fire, and the condition "
                "is on the समुदाय as 3.2.80's was. आख्याग्रहणं "
                "रूढिसंप्रत्ययार्थम् — आख्या is said so that a SETTLED "
                "name is meant: अग्न्यर्थो हीष्टकाचय उच्यते "
                "श्येनचिदिति, a hawk-shaped altar of bricks"),
    Upapada("3.2.93", "ini", of=("krī",), which_upasarga=("vi",),
            role="karman", past=True, sense="kutsā",
            why="कर्मणीनिविक्रयः — सोमविक्रयी, रसविक्रयी. AND कर्मन् "
                "IS SAID AGAIN THOUGH IT IS ALREADY RUNNING: कर्मणीति "
                "वर्तमाने पुनः कर्मग्रहणं कर्तुः कुत्सानिमित्ते कर्मणि "
                "यथा स्यात्, कर्ममात्रे मा भूत् — the object must be "
                "one that makes the AGENT blameworthy, and not any "
                "object whatever. इह न भवति धान्यविक्रायः: selling "
                "grain is no reproach, selling soma is. A repetition "
                "that narrows, where 3.2.78's repetition ended an "
                "अनुवृत्ति and 3.2.44's defeated another rule"),
    Upapada("3.2.94", "kvanip", of=("dṛś",), role="karman", past=True,
            why="दृशेः क्वनिप् — मेरुदृश्वा, परलोकदृश्वा. AND A FIFTH "
                "USE OF REPETITION: अन्येभ्योऽपि दृश्यन्ते इति क्वनिपि "
                "सिद्धे पुनर्वचनं प्रत्ययान्तरनिवृत्त्यर्थम् — 3.2.75 "
                "gives क्वनिप् already, and this is said to SHUT OUT "
                "the other affixes that rule would give beside it. Not "
                "to defeat a rule, not to end an अनुवृत्ति, not to "
                "narrow a condition, but to keep the rest of one "
                "rule's own list away"),
    Upapada("3.2.95", "kvanip", of=("yudh", "kṛ"), beside=("rājan",),
            role="karman", past=True,
            why="राजनि युधिकृञः — राजयुध्वा, राजकृत्वा. AND THE VṚTTI "
                "MEETS AN OBJECTION ABOUT THE ROOT: ननु च युधिरकर्मकः? "
                "— युध् takes no object, so how can कर्मणि hold? "
                "अन्तर्भावितण्यर्थः सकर्मको भवति: it absorbs a "
                "causative sense and so becomes transitive, राजानं "
                "योधितवान् इत्यर्थः. A root made to satisfy a "
                "condition by being read as containing another affix"),
    Upapada("3.2.96", "kvanip", of=("yudh", "kṛ"), beside=("saha",),
            past=True,
            why="सहे च — सहयुध्वा, सहकृत्वा. And the companion is NOT "
                "the object here, for a reason about what the word "
                "denotes: असत्त्ववाचित्वाद् नोपपदं कर्मणा विशेष्यते — "
                "सह names no substance, so कर्मन् cannot qualify it. "
                "The same shape of argument as 3.2.13's, where what "
                "the roots could do settled the condition"),
    Upapada("3.2.97", "ḍa", of=("jan",), role="adhikaraṇa", past=True,
            why="सप्तम्यां जनेर्डः — उपसरे जातः उपसरजः, मन्दुरजः. The "
                "companion is a locative, which is why the role is the "
                "place"),
    Upapada("3.2.98", "ḍa", of=("jan",), role="apādāna", past=True,
            jati=False,
            why="पञ्चम्यामजातौ — बुद्धिजः, संस्कारजः, दुःखजः. "
                "अजाताविति किम्? हस्तिनो जातः, अश्वाज् जातः — of a "
                "class the affix does not come, as at 3.2.78"),
    Upapada("3.2.99", "ḍa", of=("jan",), past=True, sense="saṃjñā",
            upasarga=True,
            why="उपसर्गे च संज्ञायाम् — and समुदायोपाधिः संज्ञा: the "
                "NAME is conveyed by the whole, not by any part. The "
                "third समुदायोपाधि of this pāda, after 3.2.80's व्रत "
                "and 3.2.92's अग्न्याख्या"),
    Upapada("3.2.100", "ḍa", of=("jan",), which_upasarga=("anu",),
            role="karman", past=True,
            why="अनौ कर्मणि — पुमांसमनुजातः पुमनुजः, स्त्र्यनुजः"),
    Upapada("3.2.101", "ḍa", of=("jan",), attested=True, past=True,
            why="अन्येष्वपि दृश्यते — and the vṛtti walks through EVERY "
                "ONE of the four rules before it and shows the "
                "condition departed from: सप्तम्याम् इत्युक्तम्, "
                "असप्तम्याम् अपि दृश्यते (अजः); पञ्चम्यामजातौ "
                "इत्युक्तम्, जातावपि दृश्यते (ब्राह्मणजो धर्मः); "
                "उपसर्गे च संज्ञायाम् इत्युक्तम्, असंज्ञायामपि दृश्यते "
                "(परिजाः केशाः); अनौ कर्मणि इत्युक्तम्, अकर्मण्यपि "
                "दृश्यते (अनुजः). अपिशब्दः सर्वोपाधिव्यभिचारार्थः, and "
                "तेन धात्वन्तरादपि भवति, कारकान्तरेऽपि — even from "
                "another root, परिखा. The third open rule of the pāda, "
                "after 3.2.75 and 3.2.76, and held to attested forms "
                "for the same reason"),
    Upapada("3.2.103", "ṅvanip", of=("su", "yaj"), past=True,
            why="सुयजोर्ङ्वनिप् — सुत्वा, यज्वा. No companion is "
                "wanted: the rule names two roots and nothing else"),
    Upapada("3.2.104", "atṛn", of=("jṝ",), past=True,
            also="निष्ठा",
            why="जीर्यतेरतृन् — जरन्, जरन्तौ, जरन्तः. वासरूपेण निष्ठा: "
                "by 3.1.94 the निष्ठा stands beside it too, जीर्णः, "
                "जीर्णवान् — so the rule does not shut the other out"),
)


@dataclass(frozen=True)
class Added:
    """An affix put after the root, and by which rule."""

    gives: str
    by: str
    why: str
    #: A second affix the same rule gives beside the first — 3.2.44's
    #: चकारात् खच्च, so क्षेमकारः and क्षेमंकरः both stand.
    also: str = ""
    #: Where a प्रतिषेध kept a nearer rule out, the sūtra that did it.
    #: The affix is still reported by the rule that SUPPLIES it —
    #: 3.2.23 refuses ट and 3.2.1 gives अण्, so `by` is 3.2.1 and
    #: `blocked_by` is 3.2.23. A rule that excepts a word by name does
    #: not thereby govern it.
    blocked_by: str = ""


@dataclass(frozen=True)
class NotAdded:
    """That no rule of this run reaches it."""

    by: str
    why: str
    gives: str = ""


def upapada_affix(
    root: str = "",
    *,
    word: str = "",
    wants: str = "",
    beside: str = "",
    role: str = "",
    upasarga: str = "",
    sense: str = "",
    names_a: str = "",
    chandasi: bool = False,
    causative: bool = False,
    agent: str = "",
    cvi_sense: bool = False,
    cvi_ending: bool = False,
    mantra: bool = False,
    pada_final: bool = False,
    attested: bool = False,
    jati: bool = False,
    upamana: str = "",
    past: bool = False,
) -> object:
    """
    Which affix a root takes when a word stands beside it — 3.2.1 to
    3.2.28, less the निपātana of 3.2.26, which has its own entry point.

    3.2.1 reaches every root whose companion is the object, and every
    rule after it is an अपवाद to it, so the MORE SPECIFIC rule answers.
    `role` is what 1.4.23–55 call the companion, and it is passed in
    rather than worked out: deciding a kāraka needs the whole clause,
    which is the debt 2.3.1 records.

    `wants` names the affix being asked after, where more than one
    rule reaches the same root and they differ in what they give —
    3.2.75 and 3.2.76 are both open and both reach स्रंस्. Left
    out, the most specific rule answers as before.

    `word` asks after a form the grammar FIXES rather than derives,
    and is how 3.2.5's मूलविभुजः and 3.2.59's ऋत्विक् are reached:
    both sūtras have a regular provision as well, so both answer
    from here.

    One rule of the run REFUSES rather than gives — 3.2.23. What it
    refuses is 3.2.20's ट; what the word then gets is 3.2.1's अण्. So
    the answer names 3.2.1 and carries 3.2.23 in `blocked_by`, since a
    rule that excepts a word by name does not thereby govern it.
    """
    # Two sūtras of this pāda are of BOTH kinds — 3.2.5 has its own
    # regular provision and a vārttika supplying whole words, and
    # 3.2.59 names three roots beside the five words it fixes. Each
    # registers this function, so a fixed word has to be able to reach
    # its own sūtra through it. `nipatana` remains the dedicated entry
    # point for the sūtras that ONLY fix words.
    if word:
        return _fixed(word)
    with_preverb = has_upasarga(upasarga)
    a_final = ends_in_a(root)
    matched = [row for row in UPAPADA
               if _reaches(row, root, beside, role, upasarga,
                           with_preverb, a_final, sense, names_a,
                           chandasi, causative, agent, cvi_sense,
                           cvi_ending, mantra, pada_final,
                           attested, jati, upamana, past)]
    if wants:
        matched = [row for row in matched
                   if row.refuses or _gives(row, wants)]
    refusals = [row for row in matched if row.refuses]
    giving = [row for row in matched if not row.refuses]
    for refusal in refusals:
        giving = [row for row in giving if row.gives != refusal.gives]
    if not giving:
        if refusals:
            # Here the refusal IS the rule acting, so it names itself.
            best = max(refusals, key=_ranking)
            return NotAdded(best.sutra, best.why, best.gives)
        return NotAdded(
            "",
            "No rule of 3.2.1 to 3.2.28 reaches this. 3.2.1 wants the "
            "companion to be the object, and every rule after it "
            "narrows that further",
        )
    best = max(giving, key=_ranking)
    return Added(best.gives, best.sutra, best.why, also=best.also,
                 blocked_by=refusals[0].sutra if refusals else "")


def _gives(row: Upapada, affix: str) -> bool:
    """
    Whether a row supplies the affix asked after, counting the ones it
    carries on `also`. A rule that gives two affixes gives both, and
    asking after either should reach it.
    """
    if row.gives == affix:
        return True
    return bool(row.also) and affix in row.also


def _ranking(row: Upapada):
    """
    How the resolver picks between rows, most specific first.

    The first term is how much the row states. The second breaks a tie
    by NARROWNESS: a rule naming one root is more specific than one
    naming twelve, though both merely 'name roots'. 3.2.70 दुहः कब्
    against 3.2.61's twelve is why — दुह् is in both, they tie on
    stated conditions, and without this कामदुघा came out with
    3.2.61's क्विप्.

    Kept apart from `_how_specific` on purpose: that answers what a
    rule says, which is a fact about the rule, while this answers
    which of two rules wins, which is a fact about the pair.
    """
    return (_how_specific(row), -len(row.of))


def _how_specific(row: Upapada) -> int:
    """
    How much a row says. Naming a ROOT outweighs naming a shape, as the
    कृत्य and agent runs both established: 3.2.2 names three roots that
    are आ-final precisely because 3.2.3 would otherwise have reached
    them — कप्रत्ययस्यापवादः.
    """
    return (
        3 * (len(row.of) > 0) + 2 * (len(row.beside) > 0)
        + row.a_final + (row.upasarga is not None)
        + 2 * (len(row.which_upasarga) > 0) + bool(row.role)
        + 2 * bool(row.sense) + bool(row.not_sense) + 2 * bool(row.names_a)
        + 2 * row.chandasi + 2 * row.causative + 3 * row.badhaka
        + 2 * bool(row.agent) + 2 * bool(row.not_beside)
        + 2 * row.cvi_sense + row.refuses_cvi_ending
        + 2 * row.no_upapada + 2 * row.mantra
        + 2 * row.refuses_pada_final + row.not_a_final
        + 2 * row.attested + (row.jati is not None)
        + 2 * bool(row.upamana) + row.past
    )


def _reaches(row: Upapada, root: str, beside: str, role: str,
             upasarga: str, with_preverb: bool, a_final: bool,
             sense: str, names_a: str = "", chandasi: bool = False,
             causative: bool = False, agent: str = "",
             cvi_sense: bool = False, cvi_ending: bool = False,
             mantra: bool = False, pada_final: bool = False,
             attested: bool = False, jati: bool = False,
             upamana: str = "", past: bool = False) -> bool:
    """Whether one row covers this root and companion."""
    # 3.2.27 holds in the Veda only; 3.2.28 wants the causative stem.
    # Both are one-way: requiring the condition excludes what lacks
    # it, but saying nothing about it excludes nothing. 3.2.39 is why
    # the second half matters — द्वयोरपि ग्रहणम्, both roots spelt
    # alike are meant, so silence there admits the causative too.
    if row.chandasi and not chandasi:
        return False
    # 3.2.59's युज् and क्रुञ्च् take क्विन् केवलात् — from the bare
    # root. With a companion the affix is 3.2.61's क्विप् instead, so
    # this is the one row shape that WANTS the companion absent.
    if row.no_upapada and beside:
        return False
    if row.not_beside and beside in row.not_beside:
        return False
    if row.agent and row.agent != agent:
        return False
    # 3.2.56 and 3.2.57 want the च्वि meaning WITHOUT the च्वि affix.
    # The vṛtti asks after the two separately, so they are checked
    # separately.
    if row.cvi_sense and not cvi_sense:
        return False
    if row.refuses_cvi_ending and cvi_ending:
        return False
    # मन्त्रे is narrower than छन्दसि and the vṛtti keeps them apart,
    # so a mantra rule wants the mantra register specifically.
    if row.mantra and not mantra:
        return False
    # 3.2.66's अनन्तः पादम् — the one prosodic condition of the pāda.
    if row.refuses_pada_final and pada_final:
        return False
    if row.not_a_final and a_final:
        return False
    # 3.2.75's दृश्यन्ते. The rule licenses what usage SHOWS rather
    # than manufacturing forms, so it answers only where the caller
    # says the form is attested. Without this it would hand four
    # affixes to every root there is.
    if row.attested and not attested:
        return False
    # 3.2.78's अजातौ — the companion must not name a class. Tri-state,
    # like the preverb: None says nothing, False refuses.
    if row.jati is not None and bool(row.jati) != jati:
        return False
    if row.upamana and row.upamana != upamana:
        return False
    # भूते, the अधिकāra 3.2.84 opens. One-way: the rules under it want
    # the act past, and the rules before it say nothing either way.
    if row.past and not past:
        return False
    if row.causative and not causative:
        return False
    if row.of and root not in row.of:
        return False
    if row.beside and beside not in row.beside:
        # 3.2.43 alone reaches what ENDS in one of its words —
        # उपपदविधौ भयादिग्रहणं तदन्तविधिं प्रयोजयति, अभयंकरः. That is
        # 1.1.72 येन विधिस्तदन्तस्य, which is codified, so it is asked
        # rather than approximated with a suffix test here.
        if not row.tadanta:
            return False
        from src.astadhyayi.grahana import tadantavidhi

        if not any(tadantavidhi(named, beside) for named in row.beside):
            return False
    if row.pairs and (beside, root) not in row.pairs:
        return False
    if row.role:
        # सुप् is the widest: any finished word standing beside.
        if row.role != "sup" and row.role != role:
            return False
        if row.role == "sup" and role not in ("sup", "karman",
                                              "adhikaraṇa", "kartṛ"):
            return False
    if row.a_final and not a_final:
        return False
    if row.upasarga is not None and bool(row.upasarga) != with_preverb:
        return False
    if row.which_upasarga and upasarga not in row.which_upasarga:
        return False
    if row.sense and row.sense != sense:
        return False
    if row.names_a and row.names_a != names_a:
        return False
    if row.not_sense and row.not_sense == sense:
        return False
    return True


def provisions_for(sutra_id: str) -> Tuple[Upapada, ...]:
    """Every row a sūtra of this run states."""
    return tuple(r for r in UPAPADA if r.sutra == sutra_id)


# ---------------------------------------------------------------------------
# 3.2.26 — निपातन, kept out of the table on purpose
# ---------------------------------------------------------------------------

#: फलेग्रहिरात्मम्भरिश्च. Two words FIXED rather than derived, and the
#: vṛtti says what is being fixed in each: for the first, that the
#: companion फल ends in ए and that the affix is इन्; for the second,
#: that आत्म takes the मुम् augment and the affix is इन् again. Neither
#: is something a condition could produce, which is what a निपातन is —
#: so they are recorded as given and not run through the table.
#: word -> (sūtra, affix, what the vṛtti says is being fixed).
#: The affix belongs to the ENTRY, not to the entry point: 3.2.26
#: fixes इन् forms, 3.2.37 खश् forms, 3.2.5's vārttika क forms.
#: A single hardcoded इन् reported 3.2.37's three wrongly, and
#: nothing caught it until a third affix arrived.
NIPATANA = {
    'pāṇigha': (
        "3.2.55", "ṭak",
        'पाणिघः — one who strikes with the hand, as a trade. पाणि इत्येतस्मिन् कर्मण्युपपदे हन्तेष्टक्, तस्मिंश्च परतो हन्तेष्टिलोपो घत्वं च निपात्यते: the affix, the dropping of the टि and the घ are all three fixed here. शिल्पिनीति किम्? पाणिघातः.',
    ),
    'tāḍagha': (
        "3.2.55", "ṭak",
        'ताडघः — a striker of drums, likewise.',
    ),
    'rājagha': (
        "3.2.55", "ṭak",
        'राजानं हन्ति राजघः — added by a vārttika, राजघ उपसंख्यानम्, and not held to a craftsman.',
    ),
    'ṛtvij': (
        "3.2.59", "kvin",
        'ऋतौ यजति, ऋतुं वा यजति, ऋतुप्रयुक्तो वा यजति ऋत्विक् — a priest. The vṛtti gives three derivations and settles none: रूढिरेषा यथाकथंचिदनुगन्तव्या, the word is SETTLED and the derivation is to be taken however one may. A commentary declining to derive what usage has already fixed.',
    ),
    'dadhṛṣ': (
        "3.2.59", "kvin",
        'धृष्णोतीति दधृक् — the bold one. धृषेः क्विन् द्विर्वचनम् अन्तोदात्तत्वं च निपात्यते: the affix, the reduplication and the final accent, all three fixed.',
    ),
    'sraj': (
        "3.2.59", "kvin",
        'सृजन्ति तामिति स्रक् — a garland. सृजेः कर्मणि क्विन् अमागमश्च निपात्यते, the affix and the अम् augment both.',
    ),
    'diś': (
        "3.2.59", "kvin",
        'दिशन्ति तामिति दिक् — a direction. दिशेः कर्मणि क्विन् निपात्यते.',
    ),
    'uṣṇih': (
        "3.2.59", "kvin",
        "उष्णिक् — the Uṣṇih metre. उत्पूर्वात् स्निहः क्विन् उपसर्गान्तलोपः षत्वं च निपात्यते: the affix, the loss of the preverb's end and the ष, all fixed.",
    ),
    'upeyivān': (
        "3.2.109", "kvasu",
        'उपेयिवान् — one who has approached. उपपूर्वाद् इणः क्वसुः, द्विर्वचनम् अभ्यासदीर्घत्वम्, and the vṛtti works out a chain of consequences: तत्सामर्थ्याद् एकादेशप्रतिबन्धः, and 7.2.67 वस्वेकाजाद्घसाम् would have refused the augment for being more than one vowel, स निपात्यते. न चात्रोपसर्गस्तन्त्रम् — the preverb is not essential: समीयिवान्, ईयिवान् stand too.',
    ),
    'anāśvān': (
        "3.2.109", "kvasu",
        'अनाश्वान् — one who has not eaten. अश्नातेः नञ्पूर्वात् क्वसुर् निपात्यते, इडभावश्च: the affix and the absence of the augment both fixed.',
    ),
    'anūcāna': (
        "3.2.109", "kānac",
        'अनूचानः — one who has recited, a learned man. वचेर् अनुपूर्वात् कर्तरि कानज् निपात्यते — and this one fixes कानच् where the other two fix क्वसु, so the sūtra gives two different affixes among its three words.',
    ),
    "phalegrahi": (
        "3.2.26", "in",
        "फलेग्रहिर्वृक्षः — a tree that bears fruit. फलशब्दस्य "
        "उपपदस्यैकारान्तत्वम् इन्प्रत्ययश्च ग्रहेर्निपात्यते: the "
        "ए-final shape of फल and the इन् after ग्रह् are BOTH fixed "
        "here, neither being reachable by rule.",
    ),
    "ātmambhari": (
        "3.2.26", "in",
        "आत्मानं बिभर्तीति आत्मम्भरिः — one who feeds only himself. "
        "आत्मशब्दस्योपपदस्य मुमागम इन्प्रत्ययश्च भृञो निपात्यते: the "
        "मुम् augment on आत्म and the इन् after भृ, both fixed.",
    ),
    "kukṣimbhari": (
        "3.2.26", "in",
        "कुक्षिम्भरिः — and अनुक्तसमुच्चयार्थश्चकारः, the च is there "
        "to gather in what the rule did not name. So the two words the "
        "sūtra states are not the whole of it, and the vṛtti adds "
        "these by that च rather than by any rule.",
    ),
    'mūlavibhuja': (
        "3.2.5", "ka",
        "मूलानि विभुजतीति मूलविभुजो रथः — a chariot that bends the roots. कप्रकरणे मूलविभुजादिभ्य उपसंख्यानम्: a vārttika supplying whole WORDS in the क section, not a rule for making them. The गणपाठ marks the list आकृतिगण, so it is open and these are its examples.",
    ),
    'nakhamuca': (
        "3.2.5", "ka",
        "नखमुचानि धनूंषि — bows that slip the nail.",
    ),
    'kākaguha': (
        "3.2.5", "ka",
        "काकगुहास्तिलाः — sesame that hides the crow.",
    ),
    'kumuda': (
        "3.2.5", "ka",
        "कौ मोदते कुमुदम् — the lotus, which rejoices on the earth.",
    ),
    "ugrampaśya": (
        "3.2.37", "khaś",
        "उग्रं पश्यतीत्युग्रम्पश्यः — one of fierce gaze. निपात्यन्ते: "
        "the three words of this sūtra are given outright, the खश् "
        "run having stopped short of them.",
    ),
    "irammada": (
        "3.2.37", "khaś",
        "इरया माद्यतीतीरम्मदः — one who delights in food or drink.",
    ),
    "pāṇindhama": (
        "3.2.37", "khaś",
        "पाणयो ध्मायन्त एष्विति पाणिन्धमाः पन्थानः — roads so hard "
        "going that hands are blown on. The companion is not the "
        "object here at all, which is part of what makes the word "
        "unreachable by the rules and so a निपातन.",
    ),
    "udarambhari": (
        "3.2.26", "in",
        "उदरम्भरिः — a belly-filler, added by the same च.",
    ),
}


def nipatana(word: str) -> object:
    """
    3.2.26 — a form the rules do not reach, given as it stands.

    Separate from `upapada_affix` for the reason the कृत्य run
    established: यदिह लक्षणेनानुपपन्नं तत् सर्वं निपातनात् सिद्धम् —
    whatever the rules do not reach, the fixing supplies. A table that
    tried to derive these would be pretending to a derivation the
    grammar itself declines to give.
    """
    return _fixed(word)


def _fixed(word: str) -> object:
    """
    The fixed-word lookup itself, read by both entry points.

    Deliberately names no sūtra: a private helper that cites one is
    read as implementing it, and this implements none. `nipatana` is
    what the fixed-only rules register, and the table resolver reads
    the same lookup because two rules have a regular provision AND
    supply whole words. Neither function calls the other — a table
    rule does not consult a fixing, and a delegation would say it did.
    """
    found = NIPATANA.get(word)
    if found is None:
        return NotAdded(
            "",
            "3.2.26 fixes फलेग्रहि and आत्मम्भरि, and its च gathers in "
            "कुक्षिम्भरि and उदरम्भरि besides. It reaches nothing else",
        )
    sutra, affix, why = found
    return Added(affix, sutra, why)

# ---------------------------------------------------------------------------
# 3.2.84 — an अधिकार, which confers nothing itself
# ---------------------------------------------------------------------------

#: भूते runs from 3.2.84 to 3.2.122, stopping where 3.2.123
#: वर्तमाने लट् takes over. यदित ऊर्ध्वम् अनुक्रमिष्यामो भूत इत्येवं
#: तद् वेदितव्यम् — whatever is said from here on is to be understood
#: as of the past.
BHUTE_FROM, BHUTE_THROUGH = 84, 122


def bhute_heading(sutra_id: str = "") -> object:
    """
    3.2.84 भूते — the heading, not a provision.

    It adds no affix. What it does is put every rule after it, as far
    as 3.2.123, under a condition none of them states: the act is
    PAST. So the rows carry `past` and this reports the extent, as the
    कृत् and कृत्य headings of 3.1 do.

    धात्वधिकाराच्च धात्वर्थे भूत इति विज्ञायते — and it is the ROOT's
    meaning that is past, not the word's, since the root section is
    what is running.
    """
    span = "3.2.%d to 3.2.%d" % (BHUTE_FROM, BHUTE_THROUGH)
    if not sutra_id:
        return Added(
            "", "3.2.84",
            "भूते — a heading over %s, stopping where 3.2.123 "
            "वर्तमाने लट् begins. It gives no affix; it puts the rules "
            "after it under a condition none of them states." % span)
    try:
        number = int(str(sutra_id).rsplit(".", 1)[1])
    except (ValueError, IndexError):
        number = -1
    inside = (str(sutra_id).startswith("3.2.")
              and BHUTE_FROM <= number <= BHUTE_THROUGH)
    if inside:
        return Added(
            "", "3.2.84",
            "%s falls under भूते, so its act is past though the rule "
            "does not say so." % sutra_id)
    return NotAdded(
        "", "भूते reaches %s only. %s falls outside it." % (span, sutra_id))

# ---------------------------------------------------------------------------
# 3.2.102 — a संज्ञा rule, which names an affix rather than adding one
# ---------------------------------------------------------------------------


def nistha(affix: str = "", *, past: bool = True) -> object:
    """
    3.2.102 निष्ठा — the affix so named comes where the act is PAST.

    It adds nothing of its own. WHICH affixes bear the name is 1.1.26
    क्तक्तवतू निष्ठा's business, and that rule is codified, so it is
    asked rather than the two being retyped here.

    The vṛtti raises a circularity against itself and answers it:
    निष्ठायाम् इतरेतराश्रयत्वाद् अप्रसिद्धिः — the name is being
    conferred on affixes that do not yet exist, and the affixes are
    being introduced by the name, so neither can start. नैष दोषः,
    भाविनी संज्ञा विज्ञायते: the name is understood as FORTHCOMING —
    it applies to what will bear it once produced. सामर्थ्यात्
    क्तक्तवत्वोर् विधानम् एतत्, and the force of the statement is that
    this rule INTRODUCES those two.
    """
    from src.astadhyayi.samjna import is_nistha

    if not affix:
        return NotAdded(
            "",
            "3.2.102 निष्ठा names no affix of its own. Ask it with an "
            "affix and it says whether that affix bears the name and "
            "so comes in the past")
    if not is_nistha(affix):
        return NotAdded(
            "",
            "%s does not bear the name निष्ठा. 1.1.26 क्तक्तवतू "
            "निष्ठा gives it to two affixes only, and this is not one "
            "of them" % affix)
    if not past:
        return NotAdded(
            "3.2.102",
            "%s bears the name निष्ठा by 1.1.26, but this rule gives "
            "it only where the act is PAST — भूते. Here the rule "
            "refuses, which is the whole of what it does" % affix)
    return Added(
        affix, "3.2.102",
        "निष्ठा — कृतम्, कृतवान्, भुक्तम्, भुक्तवान्. Which affixes "
        "bear the name is 1.1.26's, asked and not restated. And the "
        "vṛtti answers a circularity — भाविनी संज्ञा विज्ञायते, the "
        "name is understood as forthcoming. SCOPE: आदिकर्मणि निष्ठा "
        "वक्तव्या, a vārttika giving it for the START of an act too, "
        "प्रकृतः कटं देवदत्तः")


# ---------------------------------------------------------------------------
# 3.2.105 to 3.2.108 — what stands in place of लिट्
# ---------------------------------------------------------------------------

#: 3.2.108's three roots, where क्वसु is optional in ordinary speech.
SADADI_LIT: Tuple[str, ...] = ("sad", "vas", "śru")


def lit_substitute(root: str = "", *, chandasi: bool = False,
                   wants: str = "") -> object:
    """
    3.2.105 to 3.2.108 — लिट् in the Veda, and what replaces it.

    These do not add an affix to a root as the rest of the pāda does;
    they put लिट् where the past is meant and then substitute for it,
    so they answer here rather than from the table.

    3.2.105 छन्दसि लिट्, and the vṛtti asks why, since 3.4.6 gives
    लिट् in the Veda already: धातुसंबन्धे स विधिः, अयं त्वविशेषेण —
    that rule is about the root's connection, this one is unqualified.
    """
    if chandasi and wants in ("kānac", "कानच्"):
        return Added(
            "kānac", "3.2.106",
            "लिटः कानज् वा — अग्निं चिक्यानः, सोमं सुषुवाणः. Optional, "
            "so the ordinary perfect still stands beside it: न च भवति "
            "अहं सूर्यमुभयतो ददर्श. AND लिड्ग्रहणं किम्? The vṛtti "
            "asks why लिट् is named again when it is running, and "
            "answers लिण्मात्रस्य यथा स्यात् — naming it makes the "
            "substitution reach EVERY लिट्, योऽपि परोक्षे विहितः. A "
            "repetition that WIDENS, which is a use the pāda had not "
            "shown before",
            also="लिट् itself, where the option is not taken")
    if chandasi and wants in ("kvasu", "क्वसु"):
        return Added(
            "kvasu", "3.2.107",
            "क्वसुश्च — जक्षिवान्, पपिवान्. न च भवति अहं सूर्यमुभयतो "
            "ददर्श. योगविभाग उत्तरार्थः: split from 3.2.106 for the "
            "rule after, which wants क्वसु and not कानच्",
            also="लिट् itself, and 3.2.106's कानच्")
    if chandasi:
        return Added(
            "liṭ", "3.2.105",
            "छन्दसि लिट् — the perfect where the past is meant, in the "
            "Veda. And it may be replaced: 3.2.106 gives कानच् वा and "
            "3.2.107 gives क्वसु, so three forms stand. ननु च छन्दसि "
            "लुङ्लङ्लिटः इति सामान्येन लिड् विहित एव? धातुसंबन्धे स "
            "विधिः, अयं त्वविशेषेण",
            also="कानच् (3.2.106, optional), क्वसु (3.2.107)")
    if root in SADADI_LIT:
        return Added(
            "kvasu", "3.2.108",
            "भाषायां सदवसश्रुवः — क्वसु for लिट् in ORDINARY SPEECH "
            "too, after these three roots and optionally: उपसेदिवान् "
            "कौत्सः पाणिनिम्, अनूषिवान्, उपशुश्रुवान्. आदेशविधानाद् "
            "एव लिडपि तद्विषयोऽनुमीयते — prescribing a substitute is "
            "how we know लिट् itself is available here. तेन मुक्ते "
            "यथाप्राप्तं प्रत्यया भवन्ति: where the option is not "
            "taken the ordinary forms stand, उपासदत्, उपससाद",
            also="लिट् itself, and लुङ् and लङ् besides")
    return NotAdded(
        "",
        "3.2.105 to 3.2.107 hold in the Veda; 3.2.108 reaches सद्, "
        "वस् and श्रु in ordinary speech. Nothing here reaches this")

#: 3.2.188's three senses — मतिरिच्छा, बुद्धिर्ज्ञानम्, पूजा सत्कारः.
PRESENT_KTA_SENSES: Tuple[str, ...] = ("mati", "buddhi", "pūjā")

#: The two rules that give क्त in the present, against 3.2.102.
PRESENT_KTA = {
    "ñit": (
        "3.2.187",
        "ञीतः क्तः — मिन्नः, क्ष्विण्णः, धृष्टः, of roots marked ञि "
        "in उपदेश. भूते निष्ठा विहिता वर्तमाने न प्राप्नोतीति "
        "विधीयते: the निष्ठा having been given for the PAST at "
        "3.2.102, it would not have reached the present, so this rule "
        "is stated. An exception to a rule of this same pāda, "
        "eighty-five sūtras back.",
    ),
    "mati": (
        "3.2.188",
        "मतिबुद्धिपूजार्थेभ्यश्च — राज्ञां मतः, राज्ञामिष्टः, "
        "राज्ञां बुद्धः, राज्ञां ज्ञातः, राज्ञां पूजितः, "
        "राज्ञामर्चितः. मतिरिच्छा, बुद्धिर्ज्ञानम्, पूजा सत्कारः — "
        "the rule reaches by MEANING and not by naming roots. "
        "अनुक्तसमुच्चयार्थश्चकारः, and the vṛtti then adds a long "
        "list in two verses, closing with सुप्तः, शयितः, आशितः, "
        "लिप्तः, तृप्तः and the like — all to be understood of the "
        "present. It also notes that कष्टः belongs to the FUTURE and "
        "अमृतः to the present as before, so the list is not uniform.",
    ),
}


def kta_in_present(*, nit: bool = False, sense: str = "") -> object:
    """
    3.2.187 and 3.2.188 — where क्त comes of a PRESENT act.

    3.2.102 gave the affix named निष्ठा for the past. These two are
    its exceptions, and they answer from beside it rather than from
    the affix table: the question is when क्त comes, which is the same
    question 3.2.102 answers differently.
    """
    if nit:
        sutra, why = PRESENT_KTA["ñit"]
        return Added("kta", sutra, why)
    if sense in PRESENT_KTA_SENSES:
        sutra, why = PRESENT_KTA["mati"]
        return Added("kta", sutra, why)
    return NotAdded(
        "",
        "क्त comes in the PRESENT only after a root marked ञि, or "
        "after one meaning thought, knowledge or honour. Otherwise "
        "3.2.102 holds and the affix is of the past")
