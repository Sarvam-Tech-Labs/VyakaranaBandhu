# -*- coding: utf-8 -*-
"""
2.4.1 to 2.4.31 — what number a compound counts as, and what gender.

2.1 and 2.2 settled which words may join and which is spoken first. This
stretch settles what the joined thing then IS. Two questions, and the
second depends on the first:

    2.4.1  द्विगुरेकवचनम्                 a समाहार-द्विगु counts as one
    2.4.2  द्वन्द्वश्च प्राणितूर्यसेनाङ्गानाम्  limbs, instruments, army
    2.4.3  अनुवादे चरणानाम्               vedic schools, in a restatement
    2.4.4  अध्वर्युक्रतुरनपुंसकम्          Yajurveda rites, not neuter
    2.4.5  अध्ययनतोऽविप्रकृष्टाख्यानाम्     names close by reason of study
    2.4.6  जातिरप्राणिनाम्                classes of non-living things
    2.4.7  विशिष्टलिङ्गो नदी देशोऽग्रामाः  rivers and regions, not villages
    2.4.8  क्षुद्रजन्तवः                  small creatures
    2.4.9  येषां च विरोधः शाश्वतिकः        those in perpetual enmity
    2.4.10 शूद्राणामनिरवसितानाम्           śūdras who are not excluded
    2.4.11 गवाश्वप्रभृतीनि च               a gaṇa of finished forms
    2.4.12 विभाषा वृक्षमृग…                ten kinds, optionally
    2.4.13 विप्रतिषिद्धं चानधिकरणवाचि      opposites, not naming a locus
    2.4.14 न दधिपयआदीनि                   but never these forms
    2.4.15 अधिकरणैतावत्त्वे च              nor where the locus is counted
    2.4.16 विभाषा समीपे                   though optionally near that count

    2.4.17 स नपुंसकम्                     whatever counted as one is neuter
    2.4.18 अव्ययीभावश्च                    and an अव्ययीभाव
    2.4.19 तत्पुरुषोऽनञ् कर्मधारयः          heading: a तत्पुरुष, two excluded
    2.4.20 संज्ञायां कन्थोशीनरेषु          a name in कन्था, among Uśīnaras
    2.4.21 उपज्ञोपक्रमं तदाद्याचिख्यासायाम्  first telling of a first thing
    2.4.22 छाया बाहुल्ये                   छाया where abundance is meant
    2.4.23 सभा राजामनुष्यपूर्वा            सभा after a king- or non-human word
    2.4.24 अशाला च                        and a सभा that is not a hall
    2.4.25 विभाषा सेनासुराच्छायाशालानिशानाम् five words, optionally
    2.4.26 परवल्लिङ्गं द्वन्द्वतत्पुरुषयोः  otherwise: the LAST member's gender
    2.4.27 पूर्ववदश्ववडवौ                  but अश्ववडवौ takes the FIRST member's
    2.4.28 हेमन्तशिशिरावहोरात्रे च च्छन्दसि and two more, in the Veda
    2.4.29 रात्राह्नाहाः पुंसि              these three finals are masculine
    2.4.30 अपथं नपुंसकम्                   अपथ is neuter
    2.4.31 अर्धर्चाः पुंसि च               and a long list is both

**2.4.17 asks, it does not restate.** स नपुंसकम् — "THAT is neuter" —
has no content of its own; स names whatever the sixteen rules before it
made count as one. So :func:`gender` runs :func:`ekavat` and reads the
answer, rather than taking "does it count as one" as something the
caller supplies. Both take the same :class:`Compound`, which is why one
question can ask the other without a second parameter list. The same
shape as 2.3.50 षष्ठी शेषे, which could not be computed before the
things it is the remainder of.

**The precedence between 2.4.2, 2.4.12 and 2.4.9 is stated, not
inferred.** 2.4.2 makes a द्वन्द्व of animal-limbs count as one always;
2.4.12 then offers पशु and शकुनि a choice, and the Kāśikā on 2.4.2 says
why it wins — हस्त्यश्वादिषु परत्वात् पशुद्वन्द्वे विभाषयैकवद् भवति, by
1.4.2 विप्रतिषेधे परं कार्यम्, the later rule. Then 2.4.9's च pulls it
back: तेन पशुशकुनिद्वन्द्वे विरोधिनामनेन नित्यमेकवद्भावो भवति — for
animals that are natural enemies it is obligatory again, अश्वमहिषम्,
काकोलूकम्. Three rules, two reversals, every step in the vṛtti.

**A corpus defect, found by reading more than one commentary.** The
Kāśikā stored against 2.4.28 in ``reference/`` is not the Kāśikā on
2.4.28: it is a vṛtti on a छ-affix rule, about अपोनप्तृ and
अपोनप्त्रीयम्, with nothing to do with हेमन्तशिशिरौ. The Nyāsa, the
Padamañjarī, the Siddhāntakaumudī and Vasu all agree on the real content
and are what the rule is codified from. This is the standing argument
for reading *every* commentary rather than the first one that answers: a
single source being wrong is invisible until a second is asked.
"""

from dataclasses import dataclass, field
from typing import Dict, Optional, Tuple

from src.astadhyayi.samasa import Samasa, _gana
from src.astadhyayi.samjna import karmadharaya

# ---------------------------------------------------------------------------
# The lists
# ---------------------------------------------------------------------------

#: 2.4.11's गवाश्वादि, from the gaṇapāṭha on disk — finished compounds,
#: not a pattern. The Mahābhāṣya fixes the forms as given:
#: गवाश्वप्रभृतिषु यथोच्चारितं द्वन्द्ववृत्तम्, and the Kāśikā adds
#: रूपान्तरे तु नायं विधिर्भवति — गोऽश्वम् is a different shape and
#: falls back to 2.4.12's option.
GAVASVADI: Tuple[str, ...] = _gana("2.4.11", "gavāśvādi")

#: 2.4.12's ten, which the sūtra states in its own body rather than
#: sending to a gaṇa — so they are read from the sūtra, not from disk.
VRKSADI: Tuple[str, ...] = (
    "vṛkṣa", "mṛga", "tṛṇa", "dhānya", "vyañjana", "paśu", "śakuni",
    "aśvavaḍava", "pūrvāpara", "adharottara",
)

#: The vārttika read at 2.4.12 — बहुप्रकृतिः फलसेनावनस्पतिमृगशकुनि-
#: क्षुद्रजन्तुधान्यतृणानाम्. एषां बहुप्रकृतिरेव द्वन्द्व एकवद् भवति, न
#: द्विप्रकृतिः: for these eight, एकवद्भाव holds only where MORE than
#: two things are joined.
#:
#: These eight are NOT a subset of 2.4.12's ten. फल, सेना, वनस्पति and
#: क्षुद्रजन्तु appear nowhere in that sūtra, and the vārttika's own
#: examples give it away: बदरामलके is 2.4.6's fruit-class, यूकालिक्षे is
#: 2.4.8's small creatures, रथिकाश्वारोहौ is 2.4.2's सेनाङ्ग. So the
#: restriction is on whichever rule would have given एकवद्भाव, not on
#: 2.4.12 alone, and it is checked before the table rather than inside
#: one row of it. Written as a condition on 2.4.12's branch it silently
#: covered four kinds and missed four others.
MANY_ONLY: Tuple[str, ...] = (
    "phala", "senā", "vanaspati", "mṛga", "śakuni", "kṣudrajantu",
    "dhānya", "tṛṇa",
)

#: 2.4.14's दधिपयःआदि. The gaṇapāṭha file on disk carries no members for
#: this one, so the list is the Kāśikā's own enumeration, given as
#: finished dual forms because the rule is about शब्दरूप — the
#: word-shapes themselves and not a class of meaning.
DADHIPAYASADI: Tuple[str, ...] = (
    "dadhipayasī", "sarpirmadhunī", "madhusarpiṣī", "brahmaprajāpatī",
    "śivavaiśravaṇau", "skandaviśākhau", "parivrāṭkauśikau",
    "pravargyopasadau", "śuklakṛṣṇau", "idhmābarhiṣī", "dīkṣātapasī",
    "śraddhātapasī", "medhātapasī", "adhyayanatapasī", "ulūkhalamusale",
    "ādyavasāne", "śraddhāmedhe", "ṛksāme", "vāṅmanase",
)

#: 2.4.2's three kinds of अङ्ग. The Kāśikā and the Nyāsa both insist the
#: word अङ्ग goes with each separately — अङ्गशब्दस्य प्रत्येकं
#: वाक्यपरिसमाप्त्या त्रीणि वाक्यानि संपद्यन्ते — so a compound mixing a
#: limb with a drum-part is caught by none of the three, and न हि चतुर्थं
#: वाक्यमस्ति, there is no fourth sentence to catch it.
ANGA_KINDS: Tuple[str, ...] = ("prāṇin", "tūrya", "senā")

#: 2.4.25's five.
SENADI: Tuple[str, ...] = ("senā", "surā", "chāyā", "śālā", "niśā")

#: 2.4.29's three, as compound-finals with their समासान्त already made —
#: कृतसमासान्तानां निर्देशः.
RATRADI: Tuple[str, ...] = ("rātra", "ahna", "aha")

#: 2.4.31's अर्धर्चादि, from disk. Both genders stand for every member.
ARDHARCADI: Tuple[str, ...] = _gana("2.4.31", "ardharcādi")

#: The vārttika on 2.4.26 — द्विगुप्राप्तापन्नालंपूर्वगतिसमासेषु
#: प्रतिषेधो वक्तव्यः. Five compounds "the gender of the last" does not
#: reach: पञ्चकपालः, प्राप्तजीविकः, आपन्नजीविकः, अलंजीविकः, निष्कौशाम्बिः.
NO_PARAVAT: Tuple[str, ...] = ("dvigu", "prāpta", "āpanna", "alam", "gati")

#: What may be asserted of a compound, and what each assertion means.
#: The same shape as :data:`samasa.FACTS`, and for the same reason: the
#: conditions of this pāda are mostly yes-or-no facts about the members,
#: and a parameter apiece would be thirty parameters that both questions
#: would then have to repeat.
FACTS: Dict[str, str] = {
    "samāhāra": "an aggregate is meant, not the members severally. 2.4.1 "
                "takes only this द्विगु: समाहारद्विगोश्चेदं ग्रहणम्, "
                "नान्यस्य (2.4.1)",
    "anuvāda": "the words merely restate what is already known otherwise "
               "— प्रमाणान्तरावगतस्य अर्थस्य शब्देन संकीर्तनमात्रम् "
               "(2.4.3)",
    "aorist-sthā-iṇ": "the verb is स्था or इण् in the aorist, which the "
                      "vārttika स्थेणोरद्यतन्यां च requires of 2.4.3",
    "anapuṃsaka": "the rite-names are not themselves neuter (2.4.4)",
    "adhyayana-āsanna": "the designations stand close by reason of what "
                        "is studied — संपाठः पदानां क्रमस्य च "
                        "प्रत्यासन्नः (2.4.5)",
    "prāṇin": "the things named are living (2.4.6)",
    "viśiṣṭaliṅga": "the words differ in gender. गङ्गायमुने and "
                    "मद्रकेकयाः share one and are untouched (2.4.7)",
    "grāma": "one of the places named is a village (2.4.7)",
    "nagara": "one of them is a town — the vārttika नगराणां प्रतिषेधो "
              "वक्तव्यः puts मथुरापाटलिपुत्रम् out too (2.4.7)",
    "kṣudra-jantu": "the creatures are small. अपचितपरिमाणः क्षुद्रः, and "
                    "the Kāśikā settles the bound at आ नकुलादपि — up to "
                    "and including the mongoose (2.4.8)",
    "śāśvatika-virodha": "a standing enmity, not a quarrel. विरोधो "
                         "वैरम्, शाश्वतिको नित्यः (2.4.9)",
    "niravasita": "excluded — those by whose eating a vessel is not made "
                  "clean again even by scouring (2.4.10)",
    "vipratiṣiddha": "the things named are opposites: शीत and उष्ण, सुख "
                     "and दुःख. कामक्रोधौ are not (2.4.13)",
    "adhikaraṇa-vācin": "the words name the SUBSTANCE that bears the "
                        "qualities rather than the qualities — शीतोष्णे "
                        "उदके (2.4.13)",
    "etāvattva": "the locus itself is counted: दश दन्तोष्ठाः. अधिकरणं "
                 "वर्त्तिपदार्थः, the thing the compound's meaning rests "
                 "on (2.4.15)",
    "samīpa": "the count is approximate — उपदशं, about ten (2.4.16)",
    "saṃjñā": "the compound is a proper name (2.4.20)",
    "uśīnara": "the कन्था so named is among the Uśīnaras (2.4.20)",
    "ācikhyāsā": "the wish is to tell of the BEGINNING of what was first "
                 "known or first undertaken. आख्यातुमिच्छा आचिख्यासा "
                 "(2.4.21)",
    "bāhulya": "abundance is meant, and it belongs to the first member: "
               "पूर्वपदार्थधर्मो बाहुल्यम् (2.4.22)",
    "rājan-pūrva": "a synonym of राजन् stands first. राजसभा itself is "
                   "untouched — पर्यायवचनस्यैवेष्यते (2.4.23)",
    "amanuṣya-pūrva": "a non-human word stands first, and अमनुष्य is "
                      "fixed to demons and spirits rather than meaning "
                      "whatever is not a man — काष्ठसभा escapes (2.4.23)",
    "aśālā": "the सभा is a GATHERING and not a hall — सङ्घातवचनोऽत्र "
             "सभाशब्दो गृह्यते (2.4.24)",
    "nañ": "the तत्पुरुष is a नञ् compound, which 2.4.19 puts outside "
           "2.4.20 to 2.4.25: असेना",
    "samānādhikaraṇa": "the members refer to one thing, which by 1.2.42 "
                       "makes it a कर्मधारय — the other compound 2.4.19 "
                       "puts outside: परमसेना",
    "chandas": "the usage is Vedic (2.4.28)",
}


@dataclass(frozen=True)
class Compound:
    """A finished compound, offered for its number and its gender."""

    #: The name 2.1 and 2.2 conferred.
    samasa: Optional[Samasa] = None
    #: Which of 2.4.2's three kinds of अङ्ग — and this is अङ्ग in the
    #: ordinary sense, a LIMB, not the अङ्ग of 6.4.1 that an affix
    #: attaches to. The two are different words wearing one spelling.
    anga_of: str = ""
    #: What sort of class 2.4.6's जाति is — द्रव्य, गुण or क्रिया. Only
    #: the first is made one: नञिवयुक्तन्यायेन द्रव्यजातीनामयमेकवद्भावः.
    jati_of: str = ""
    #: What the members NAME: rivers or regions for 2.4.7, and the
    #: Yajurvedic rites of 2.4.4. Kept apart from `ends_in`, which
    #: the gender rules 2.4.20 to 2.4.29 own.
    names: str = ""
    #: Whether they name śūdras, for 2.4.10, or vedic schools, for 2.4.3.
    people: str = ""
    #: A finished form, for the two gaṇas that fix शब्दरूप — 2.4.11's
    #: गवाश्वादि and 2.4.14's दधिपयःआदि — and for the words 2.4.27 to
    #: 2.4.31 name outright.
    form: str = ""
    #: What kind of thing is being joined. 2.4.12 names ten, and the
    #: बहुप्रकृति vārttika names eight that only partly overlap them
    #: — so this is not 2.4.12's slot alone.
    group: str = ""
    #: How many things are compounded. 2.4.12's vārttika needs more than
    #: two for some of its ten.
    member_count: int = 2
    #: What the compound ends in, for 2.4.20 to 2.4.25 and 2.4.29.
    ends_in: str = ""
    #: Which sort of तत्पुरुष, for 2.4.26's vārttika.
    kind: str = ""
    #: Facts asserted from :data:`FACTS`.
    given: Tuple[str, ...] = field(default_factory=tuple)

    def has(self, fact: str) -> bool:
        if fact not in FACTS:
            raise ValueError(
                f"{fact!r} is not a fact this pāda knows. Known: "
                f"{', '.join(sorted(FACTS))}")
        return fact in self.given


# ---------------------------------------------------------------------------
# What the two questions answer with
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Count:
    """That this compound counts as one, and by which rule."""

    by: str
    why: str
    optional: bool = False
    singular: bool = True


@dataclass(frozen=True)
class Refused:
    """
    That एकवद्भाव does not happen, and why.

    ``by`` names a rule only where a प्रतिषेध is what refused — 2.4.14
    and 2.4.15 refusing IS those rules acting, and asking either of them
    on a form it keeps out is a worked example, not a counter-example.
    Where a rule simply does not reach the input, ``by`` is empty. The
    two are different answers and must not be run together.
    """

    by: str
    why: str
    singular: bool = False


@dataclass(frozen=True)
class Gender:
    """The gender a compound takes, and by which rule."""

    name: str
    by: str
    why: str
    #: A second gender that stands equally — 2.4.31's list is both.
    also: Tuple[str, ...] = ()
    optional: bool = False


@dataclass(frozen=True)
class LikeMember:
    """
    That the gender is not stated but taken from a member.

    2.4.26, 2.4.27 and 2.4.28 name no gender at all; they say *whose*
    gender to use. Returning a name here would be inventing one, so the
    slot is returned and the caller reads it off the word.
    """

    slot: str
    by: str
    why: str


MASCULINE = "puṃliṅga"
NEUTER = "napuṃsakaliṅga"


# ---------------------------------------------------------------------------
# 2.4.1 to 2.4.16 — एकवद्भाव
# ---------------------------------------------------------------------------

def ekavat(c: Compound) -> object:
    """
    Whether this compound counts as one — 2.4.1 to 2.4.16.

    एकवद्भाव is not merely "takes a singular ending". The Nyāsa is at
    pains about it: एकवचन here is not the technical एकवचन of 1.4.102 but
    the word in its own sense, एकस्य वचनम् — *that which speaks of one*.
    Were the technical one meant, पञ्चपूलीयं शोभना could not be singular,
    since शोभना is not itself a द्विगु — अनुप्रयोगस्याद्विगुत्वात्. What
    the rule confers is oneness of MEANING; the ending follows from it.
    """
    # 2.4.16 first, then the two प्रतिषेध. 2.4.16 is the विभाषा that
    # answers 2.4.15's refusal — अधिकरणैतावत्त्वस्य समीपे विभाषा — and a
    # prohibition read before it would swallow it.
    if c.has("samīpa"):
        return Count(
            "2.4.16",
            "विभाषा समीपे — near the count 2.4.15 refuses for, the "
            "choice is open again: उपदशं दन्तोष्ठम् beside उपदशा "
            "दन्तोष्ठाः. On the एकवत् reading the उप- word is an "
            "अव्ययीभाव, on the other a बहुव्रीहि, so the two differ in "
            "more than number",
            optional=True,
        )
    if c.has("etāvattva"):
        return Refused(
            "2.4.15",
            "अधिकरणैतावत्त्वे च — where the LOCUS is counted the "
            "compound does not count as one: दश दन्तोष्ठाः, दश "
            "मार्दङ्गिकपाणविकाः. Ten of them cannot be one",
        )
    if c.form and c.form in DADHIPAYASADI:
        return Refused(
            "2.4.14",
            f"न दधिपयआदीनि — {c.form} is one of the शब्दरूप this rule "
            f"keeps out, whichever rule before would have reached it: "
            f"दधिपयसी, वाङ्मनसे, ऋक्सामे. यथायथमेकवद्भावे प्राप्ते "
            f"प्रतिषेध आरभ्यते — the prohibition is written because each "
            f"of them was otherwise caught",
        )

    # 2.4.11's gaṇa of finished forms, read before the general rules
    # because it fixes शब्दरूप and not a class.
    if c.form and c.form in GAVASVADI:
        return Count(
            "2.4.11",
            f"गवाश्वप्रभृतीनि च — {c.form} is given whole in the gaṇa "
            f"and is correct as it stands. गवाश्वप्रभृतिषु यथोच्चारितं "
            f"द्वन्द्ववृत्तम्, as uttered so read; रूपान्तरे तु नायं "
            f"विधिर्भवति, and गोऽश्वम् falls back to 2.4.12's option",
        )

    # 2.4.9 first of all the positive rows. Its च makes एकवद्भाव
    # obligatory for animals that are enemies, and काकोलूकम् — crow and
    # owl, exactly two — is the vṛtti's own example, so it stands above
    # both 2.4.12's option and the बहुप्रकृति vārttika below. शकुनि is
    # named by all three, which is what makes the order visible.
    if c.has("śāśvatika-virodha"):
        return Count(
            "2.4.9",
            "येषां च विरोधः शाश्वतिकः — मार्जारमूषकम्, अहिनकुलम्. "
            "शाश्वतिक इति किम्? गोपालिशालङ्कायनाः कलहायन्ते — men who "
            "happen to be fighting are not enemies by nature. चकारः "
            "पुनरस्यैव समुच्चयार्थः, and by that च it holds even over "
            "2.4.12's पशु and शकुनि: अश्वमहिषम्, काकोलूकम्",
        )

    # The बहुप्रकृति vārttika, before the rest of the table: it
    # restricts whichever rule would otherwise have given एकवद्भाव, and
    # three of its own examples belong to rules other than 2.4.12.
    if c.group in MANY_ONLY and c.member_count <= 2:
        return Refused(
            "",
            f"बहुप्रकृतिः फलसेनावनस्पतिमृगशकुनिक्षुद्रजन्तुधान्यतृणानाम् "
            f"— एषां बहुप्रकृतिरेव द्वन्द्व एकवद् भवति, न द्विप्रकृतिः. "
            f"With only two {c.group} things joined, no rule makes them "
            f"one: बदरामलके, यूकालिक्षे, रथिकाश्वारोहौ, प्लक्षन्यग्रोधौ "
            f"all stay dual",
        )


    # 2.4.12 and 2.4.13 — the two options.
    if c.group and c.group in VRKSADI:
        return Count(
            "2.4.12",
            f"विभाषा वृक्षमृगतृणधान्यव्यञ्जनपशुशकुन्यश्ववडवपूर्वापराधरोत्तराणाम् "
            f"— {c.group} is one of the ten and either reading stands: "
            f"प्लक्षन्यग्रोधम् beside प्लक्षन्यग्रोधाः, दधिघृतम् beside "
            f"दधिघृते. Being later than 2.4.2, it opens by परत्व what "
            f"that rule had shut",
            optional=True,
        )
    if c.has("vipratiṣiddha"):
        if c.has("adhikaraṇa-vācin"):
            return Refused(
                "",
                "अनधिकरणवाचीति किम्? शीतोष्णे उदके — where the words "
                "name the SUBSTANCE that is hot and cold rather than "
                "the qualities, they are two things and stay two",
            )
        return Count(
            "2.4.13",
            "विप्रतिषिद्धं चानधिकरणवाचि — शीतोष्णम् beside शीतोष्णे, "
            "सुखदुःखम्, जीवितमरणम्. विप्रतिषिद्धमिति किम्? कामक्रोधौ — "
            "desire and anger are not opposites. "
            "विभाषानुकर्षणार्थश्चकारः: the च drags 2.4.12's option "
            "down, so this too is a choice",
            optional=True,
        )

    # 2.4.1 to 2.4.10 — the obligatory rows, in the text's own order.
    if c.samasa is Samasa.DVIGU:
        if not c.has("samāhāra"):
            return Refused(
                "",
                "समाहारद्विगोश्चेदं ग्रहणम्, नान्यस्य — 2.4.1 takes only "
                "the द्विगु that means a COLLECTION. One that merely "
                "qualifies is not made one by it",
            )
        return Count(
            "2.4.1",
            "द्विगुरेकवचनम् — पञ्च पूलाः समाहृताः पञ्चपूली, दशपूली. And "
            "because the oneness is of meaning and not of ending, what "
            "is said of it afterwards is singular too: पञ्चपूलीयं शोभना",
        )
    if c.anga_of:
        if c.anga_of not in ANGA_KINDS:
            raise ValueError(
                f"{c.anga_of!r} is not one of 2.4.2's three: "
                f"{', '.join(ANGA_KINDS)}")
        shown = {"prāṇin": "पाणिपादम्, शिरोग्रीवम्",
                 "tūrya": "मार्दङ्गिकपाणविकम्, वीणावादकपरिवादकम्",
                 "senā": "रथिकाश्वारोहम्, रथिकपादातम्"}[c.anga_of]
        return Count(
            "2.4.2",
            f"द्वन्द्वश्च प्राणितूर्यसेनाङ्गानाम् — {shown}. अङ्गशब्दस्य "
            f"प्रत्येकं वाक्यपरिसमाप्त्या त्रीणि वाक्यानि संपद्यन्ते: the "
            f"word अङ्ग goes with each of the three separately, so a "
            f"limb compounded with a drum-part is caught by none of "
            f"them — न हि चतुर्थं वाक्यमस्ति",
        )
    if c.people == "caraṇa":
        if not c.has("anuvāda"):
            return Refused(
                "",
                "अनुवाद इति किम्? उदगुः कठकालापाः — said for the first "
                "time, the schools are many",
            )
        if not c.has("aorist-sthā-iṇ"):
            return Refused(
                "",
                "स्थेणोरद्यतन्यां चेति वक्तव्यम् — the vārttika holds "
                "2.4.3 to स्था and इण् in the aorist. अनन्दिषुः "
                "कठकालापाः is another root, उद्यन्ति कठकालापाः another "
                "tense, and neither is made one",
            )
        return Count(
            "2.4.3",
            "अनुवादे चरणानाम् — उदगात् कठकालापम्, प्रत्यष्ठात् "
            "कठकौथुमम्. चरणशब्दः शाखानिमित्तकः पुरुषेषु वर्तते: the word "
            "names the MEN, by way of the recension they follow — where "
            "it names the recension itself, 2.4.6 covers it already",
        )
    if c.names == "kratu":
        if not c.has("anapuṃsaka"):
            return Refused(
                "",
                "अनपुंसकमिति किम्? राजसूयवाजपेये — rite-names that are "
                "themselves neuter are left out",
            )
        return Count(
            "2.4.4",
            "अध्वर्युक्रतुरनपुंसकम् — अर्काश्वमेधम्, सायाह्नातिरात्रम्. "
            "अध्वर्युवेदे यस्य क्रतोर्विधानं सोऽध्वर्युक्रतुः, a rite laid "
            "down in the Yajurveda. अध्वर्युक्रतुरिति किम्? इषुवज्रौ. "
            "And दर्शपौर्णमासौ escapes because क्रतुशब्दः सोमयागेषु "
            "रूढः — the word is fixed to the soma rites",
        )
    if c.has("adhyayana-āsanna"):
        return Count(
            "2.4.5",
            "अध्ययनतोऽविप्रकृष्टाख्यानाम् — पदकक्रमकम्, "
            "क्रमकवार्त्तिकम्. अध्ययनत इति किम्? पितापुत्रौ. "
            "अविप्रकृष्टाख्यानामिति किम्? याज्ञिकवैयाकरणौ — a ritualist "
            "and a grammarian both study, but not the same thing",
        )
    if c.jati_of:
        if c.has("prāṇin"):
            return Refused(
                "",
                "अप्राणिनामिति किम्? ब्राह्मणक्षत्रियविट्शूद्राः — "
                "classes of LIVING things stay many",
            )
        if c.jati_of != "dravya":
            return Refused(
                "",
                f"नञिवयुक्तन्यायेन द्रव्यजातीनामयमेकवद्भावः, न "
                f"गुणक्रियाजातीनाम् — only classes of SUBSTANCE. A "
                f"{c.jati_of}-class is not made one: रूपरसगन्धस्पर्शाः, "
                f"गमनाकुञ्चनप्रसारणानि",
            )
        return Count(
            "2.4.6",
            "जातिरप्राणिनाम् — आराशस्त्रि, धानाशष्कुलि. And the class "
            "must be what is meant: जातिपरत्वे च … न "
            "नियतद्रव्यविवक्षायाम् — इह कुण्डे बदरामलकानि तिष्ठन्ति, "
            "where particular fruits in a particular bowl are meant and "
            "not the kinds",
        )
    if c.names in ("nadī", "deśa"):
        if not c.has("viśiṣṭaliṅga"):
            return Refused(
                "",
                "विशिष्टलिङ्ग इति किम्? गङ्गायमुने, मद्रकेकयाः — where "
                "the words share a gender the rule does not reach",
            )
        if c.has("grāma") or c.has("nagara"):
            return Refused(
                "",
                "अग्रामाः — जाम्बवशालूकिन्यौ. The vārttika adds towns, "
                "नगराणां प्रतिषेधो वक्तव्यः, so मथुरापाटलिपुत्रम् is "
                "out; and उभयतश्च ग्रामाणां प्रतिषेधो वक्तव्यः puts a "
                "town-and-village pair out too — सौर्यकेतवते",
            )
        return Count(
            "2.4.7",
            "विशिष्टलिङ्गो नदी देशोऽग्रामाः — गङ्गाशोणम्, "
            "कुरुकुरुक्षेत्रम्. नदी देश इत्यसमासनिर्देश एवायम् — the two "
            "words are NOT compounded in the sūtra, so each condition "
            "stands on its own. And जनपदो हि देशः, a देश is a settled "
            "country, which is why mountains are untouched: "
            "कैलासगन्धमादने",
        )
    if c.has("kṣudra-jantu"):
        return Count(
            "2.4.8",
            "क्षुद्रजन्तवः — दंशमशकम्, यूकालिक्षम्. क्षुद्रजन्तव इति "
            "किम्? ब्राह्मणक्षत्रियौ. The Kāśikā weighs two definitions "
            "— boneless, or simply small — and settles it by the verse "
            "ending आ नकुलादपि, इयमेव स्मृतिः प्रमाणम्",
        )
    if c.people == "śūdra":
        if c.has("niravasita"):
            return Refused(
                "",
                "अनिरवसितानामिति किम्? चण्डालमृतपाः — those who ARE "
                "excluded stay many",
            )
        return Count(
            "2.4.10",
            "शूद्राणामनिरवसितानाम् — तक्षायस्कारम्, रजकतन्तुवायम्: a "
            "carpenter and a smith, a washerman and a weaver",
        )
    return Refused(
        "",
        "None of 2.4.1 to 2.4.16 reaches this compound, so it keeps the "
        "number its members give it, and 2.4.26's परवल्लिङ्ग decides the "
        "gender rather than 2.4.17's नपुंसक",
    )


# ---------------------------------------------------------------------------
# 2.4.17 to 2.4.31 — the gender
# ---------------------------------------------------------------------------

def gender(c: Compound) -> object:
    """
    What gender this compound takes — 2.4.17 to 2.4.31.

    2.4.17 asks :func:`ekavat` rather than restating it: स नपुंसकम् has
    no content of its own, and what it names is whatever 2.4.1 to 2.4.16
    made count as one.
    """
    # 2.4.30 and 2.4.31 name words outright, so they answer first.
    if c.form == "apatha":
        return Gender(
            NEUTER, "2.4.30",
            "अपथं नपुंसकम् — अपथमिदम्, अपथानि गाहते मूढः. तत्पुरुष इति "
            "वर्तते carries down from 2.4.19, which is why अपथो देशः "
            "and अपथा नगरी are untouched: those are बहुव्रीहि",
        )
    if c.form and c.form in ARDHARCADI:
        return Gender(
            MASCULINE, "2.4.31",
            f"अर्धर्चाः पुंसि च — {c.form} is in the list and BOTH "
            f"genders stand: अर्धर्चः and अर्धर्चम्, गोमयः and गोमयम्. "
            f"शब्दरूपाश्रया चेयं द्विलिङ्गता — it attaches to the "
            f"word-shape; and क्वचिदर्थभेदेनापि व्यवतिष्ठते, sometimes "
            f"the two genders divide a meaning between them, as सार is "
            f"masculine for excellence and neuter for what is sound",
            also=(NEUTER,),
        )

    # 2.4.28 before 2.4.29: the Nyāsa reads it as overriding that rule —
    # रात्राह्नाहाः पुंसि इति पुंल्लिङ्गत्वे प्राप्ते छन्दसि लिङ्गव्यत्यय उक्तः.
    if c.has("chandas") and c.form in ("hemantaśiśirau", "ahorātre"):
        return LikeMember(
            "first", "2.4.28",
            "हेमन्तशिशिरावहोरात्रे च च्छन्दसि — in the Veda these two "
            "take the FIRST member's gender. For हेमन्तशिशिरौ that "
            "displaces the neuter शिशिर would have given through "
            "2.4.26; for अहोरात्रे it displaces the masculine 2.4.29 "
            "would have given — व्यत्ययो बहुलम्, by 3.1.85. (Codified "
            "from the Nyāsa, the Padamañjarī and the "
            "Siddhāntakaumudī: the Kāśikā stored on disk against this "
            "sūtra is another rule's text.)",
        )
    if c.form == "aśvavaḍavau":
        return LikeMember(
            "first", "2.4.27",
            "पूर्ववदश्ववडवौ — अश्वश्च वडवा च अश्ववडवौ, masculine after "
            "अश्व and not feminine after वडवा. अर्थातिदेशश्चायम् न "
            "निपातनम् — it transfers the sense, it does not fix a form, "
            "so तत्र द्विवचनमतन्त्रम्: the dual in the sūtra is not "
            "binding, and अश्ववडवान्, अश्ववडवैः go the same way",
        )
    if c.ends_in and c.ends_in in RATRADI:
        return Gender(
            MASCULINE, "2.4.29",
            f"रात्राह्नाहाः पुंसि — a compound ending in {c.ends_in} is "
            f"masculine: द्विरात्रः, पूर्वाह्णः, द्व्यहः. "
            f"कृतसमासान्तानां निर्देशः, the three are named with their "
            f"समासान्त already made. परवल्लिङ्गतया स्त्रीनपुंसकयोः "
            f"प्राप्तयोरिदं वचनम् — written because 2.4.26 would else "
            f"have given the feminine or the neuter. The vārttika adds "
            f"अनुवाकादयः पुंसि",
        )

    # 2.4.17 and 2.4.18 — the two neuters that beat 2.4.26 outright.
    if getattr(ekavat(c), "singular", False):
        return Gender(
            NEUTER, "2.4.17",
            "स नपुंसकम् — यस्यायमेकवद्भावो विहितः स नपुंसकलिङ्गो भवति: "
            "whatever 2.4.1 to 2.4.16 made count as ONE is neuter, "
            "द्विगु and द्वन्द्व alike — पञ्चगवम्, पाणिपादम्. "
            "परवल्लिङ्गतापवादो योगः, written to beat 2.4.26. The rule "
            "has no content of its own; स points back, so the answer is "
            "asked of that table and not decided here",
        )
    if c.samasa is Samasa.AVYAYIBHAVA:
        return Gender(
            NEUTER, "2.4.18",
            "अव्ययीभावश्च — अधिस्त्रि, उपकुमारि, उन्मत्तगङ्गम्. "
            "पूर्वपदार्थप्रधानस्यालिङ्गतैव प्राप्ता — a compound whose "
            "FIRST member carries the meaning would have had no gender "
            "at all, and one whose meaning lies outside would take its "
            "referent's; so the neuter has to be stated. "
            "अनुक्तसमुच्चयार्थश्चकारः, and the vārttikas add पुण्याहम्, "
            "त्रिपथम्, and adverbs — मृदु पचति",
        )

    # 2.4.19's अधिकार, and the six rules it governs.
    if c.samasa is Samasa.TATPURUSA:
        if c.has("nañ") or karmadharaya(
                tatpurusa=True,
                samanadhikarana=c.has("samānādhikaraṇa")):
            return Gender(
                "", "",
                "तत्पुरुषोऽनञ् कर्मधारयः — 2.4.19 heads 2.4.20 to 2.4.25 "
                "and puts two तत्पुरुष outside them: the नञ् compound, "
                "असेना, and the कर्मधारय, परमसेना, which 1.2.42 names. "
                "Neither is made neuter, so the gender comes from "
                "2.4.26 instead",
            )
        if c.ends_in == "kanthā":
            if not (c.has("saṃjñā") and c.has("uśīnara")):
                return Gender(
                    "", "",
                    "संज्ञायामिति किम्? वीरणकन्था. उशीनरेष्विति किम्? "
                    "दाक्षिकन्था — it must be a NAME, and the कन्था "
                    "must be among the Uśīnaras",
                )
            return Gender(
                NEUTER, "2.4.20",
                "संज्ञायां कन्थोशीनरेषु — सौशमिकन्थम्, आह्वरकन्थम्. "
                "परवल्लिङ्गतापवाद इदं प्रकरणम्: from here to 2.4.25 "
                "every rule exists to beat 2.4.26",
            )
        if c.ends_in in ("upajñā", "upakrama"):
            if not c.has("ācikhyāsā"):
                return Gender(
                    "", "",
                    "तदाद्याचिख्यासायामिति किम्? देवदत्तोपज्ञो रथः, "
                    "यज्ञदत्तोपक्रमो रथः — the neuter comes only where "
                    "the wish is to tell of the BEGINNING of the thing "
                    "first known or first undertaken",
                )
            return Gender(
                NEUTER, "2.4.21",
                "उपज्ञोपक्रमं तदाद्याचिख्यासायाम् — पाणिन्युपज्ञमकालकं "
                "व्याकरणम्, the tenseless grammar Pāṇini first knew; "
                "आढ्योपक्रमं प्रासादः, नन्दोपक्रमाणि मानानि",
            )
        if c.ends_in == "chāyā" and c.has("bāhulya"):
            return Gender(
                NEUTER, "2.4.22",
                "छाया बाहुल्ये — शलभच्छायम्, इक्षुच्छायम्, where a "
                "MULTITUDE casts the shade. 2.4.25 offers छाया a "
                "choice; नित्यार्थमिदं वचनम् — this rule is written to "
                "make it obligatory here. बाहुल्य इति किम्? कुड्यच्छाया",
            )
        if c.ends_in == "sabhā" and (c.has("rājan-pūrva")
                                     or c.has("amanuṣya-pūrva")):
            return Gender(
                NEUTER, "2.4.23",
                "सभा राजामनुष्यपूर्वा — इनसभम्, ईश्वरसभम्; रक्षःसभम्, "
                "पिशाचसभम्. राजसभा itself is untouched, because "
                "पर्यायवचनस्यैवेष्यते — only SYNONYMS of राजन् are "
                "meant, जित् पर्यायस्यैव राजाद्यर्थम्",
            )
        if c.ends_in == "sabhā" and c.has("aśālā"):
            return Gender(
                NEUTER, "2.4.24",
                "अशाला च — स्त्रीसभम्, दासीसभम्, where सभा means a "
                "GATHERING and not a hall: दासीसङ्घात इत्यर्थः. अशालेति "
                "किम्? अनाथसभा, which is अनाथकुटी, a shelter",
            )
        if c.ends_in and c.ends_in in SENADI:
            return Gender(
                NEUTER, "2.4.25",
                f"विभाषा सेनासुराच्छायाशालानिशानाम् — a compound in "
                f"{c.ends_in} is neuter or not, as one chooses: "
                f"ब्राह्मणसेनम् beside ब्राह्मणसेना, यवसुरम् beside "
                f"यवसुरा, गोशालम् beside गोशाला",
                optional=True,
            )

    # 2.4.26 — the general rule everything above was written to beat.
    if c.samasa in (Samasa.DVANDVA, Samasa.TATPURUSA):
        if c.kind and c.kind in NO_PARAVAT:
            return Gender(
                "", "",
                f"द्विगुप्राप्तापन्नालंपूर्वगतिसमासेषु प्रतिषेधो "
                f"वक्तव्यः — the vārttika keeps 2.4.26 off a {c.kind} "
                f"compound: पञ्चकपालः, प्राप्तजीविकः, आपन्नजीविकः, "
                f"अलंजीविकः, निष्कौशाम्बिः. Each keeps the gender its "
                f"referent has rather than the last member's",
            )
        return LikeMember(
            "last", "2.4.26",
            "परवल्लिङ्गं द्वन्द्वतत्पुरुषयोः — the gender of the LAST "
            "member: कुक्कुटमयूर्याविमे but मयूरीकुक्कुटाविमौ, and अर्धं "
            "पिप्पल्याः अर्धपिप्पली. समाहारद्वन्द्वे नपुंसकलिङ्गस्य "
            "विहितत्वाद् इतरेतरयोगद्वन्द्वस्येदं ग्रहणम् — 2.4.17 has "
            "taken the समाहार already, so what is left here is the "
            "इतरेतरयोग द्वन्द्व",
        )
    return Gender(
        "", "",
        "No rule of 2.4.17 to 2.4.31 reaches this, so the compound takes "
        "the gender of whatever it denotes",
    )
