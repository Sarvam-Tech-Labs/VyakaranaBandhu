# -*- coding: utf-8 -*-
"""
३.३.१०–१२ — affixes where the act is done FOR another act.

क्रियार्थोपपद: one act stands beside the root as the purpose of it —
भोक्तुं व्रजति, he goes in order to eat. Three rules divide the ground,
and the reason there are three is a principle carried over from the
pāda before.

**वासरूप is suspended here, and this is the third section to suspend
it.** 3.1.94 वाऽसरूपोऽस्त्रियाम् lets a general affix stand beside the
special one that excepts it. 3.2.146's vṛtti argued that the तच्छीलादि
section suspends that — ताच्छीलिकेषु वासरूपविधिर् नास्ति — and 3.2.177
was written because of the suspension. Here the Kāśikā says it again in
its own terms, and cites the Mahābhāṣya for it:
क्रियायामुपपदे क्रियार्थायां वासरूपेण तृजादयो न भवन्ति. Both 3.3.11 and
3.3.12 then exist ONLY because of the suspension — without it the
affixes they give would have come anyway.

So this run is not three rules that happen to sit together. It is one
rule and two repairs for what the suspension broke, and the commentary
says so at each of the three.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

from src.astadhyayi.samjna import is_ghu
from src.astadhyayi.upapada_krt import Added, NotAdded, upapada_affix

#: 3.3.10's two, given together. तुमुन् makes an indeclinable and ण्वुल्
#: an agent-noun, and the vṛtti gives one example of each: भोक्तुं
#: व्रजति, भोजको व्रजति.
KRIYARTHA_PAIR: Tuple[str, ...] = ("tumun", "ṇvul")


@dataclass(frozen=True)
class Kriyartha:
    """One rule giving an affix where a purpose-act stands beside."""

    sutra: str
    gives: str
    also: str = ""
    #: 3.3.12's कर्मणि — an object stands beside as well.
    karman: bool = False
    #: 3.3.11's भाववचनाः — the affix asked after is one of those
    #: given under 3.3.18 भावे, naming the act itself.
    bhava: bool = False
    #: Which affix is being asked after, where more than one rule
    #: reaches the same ground. The idiom three entry points of 3.2
    #: already needed.
    wants: Tuple[str, ...] = ()
    #: A rule this one RESTATES rather than adds to. 3.3.12's अण् is
    #: 3.2.1's own, said again because वासरूप being suspended it could
    #: not stand beside 3.3.10's ण्वुल्. Where a row names one, the
    #: affix is asked of that rule instead of being written here — so
    #: `gives` is left empty and filled at resolve time.
    restates: str = ""
    why: str = ""


KRIYARTHA: Tuple[Kriyartha, ...] = (
    Kriyartha(
        "3.3.10", "tumun", also="ण्वुल्", wants=KRIYARTHA_PAIR,
        why="तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम् — भोक्तुं व्रजति, "
            "भोजको व्रजति. भुजिक्रियार्थो व्रजिरत्रोपपदम्: the going "
            "is for the sake of the eating, and it is the EATING that "
            "stands beside. Both questions are asked. क्रियायामिति "
            "किम्? भिक्षिष्य इत्यस्य जटाः — where what stands beside "
            "is not an act. क्रियार्थायामिति किम्? धावतस्ते पतिष्यति "
            "दण्डः — an act stands beside, but the first is not done "
            "FOR it; the stick falls as he runs, not so that he may "
            "run. Two conditions, two counter-examples, and neither "
            "is redundant.\n\n"
            "AND THE RULE ARGUES FOR ITS OWN SECOND HALF. अथ किमर्थं "
            "ण्वुल् विधीयते, यावता ण्वुल्तृचौ इति सामान्येन विहित "
            "एव? — why give ण्वुल् when 3.1.133 gives it already? "
            "Because लृटा क्रियार्थोपपदेन बाध्यते, 3.3.13's लृट् "
            "would displace it here. Then वासरूपविधिना सोऽपि "
            "भविष्यति, could it not stand beside by 3.1.94? एवं "
            "तर्ह्येतज् ज्ञाप्यते — क्रियायामुपपदे क्रियार्थायां "
            "वासरूपेण तृजादयो न भवन्ति. The rule's own redundancy is "
            "the evidence that वासरूप is suspended over this ground, "
            "and तेन कर्ता व्रजति, विक्षिपो व्रजति are thereby ruled "
            "out. The same argument 3.2.146 made from वुञ्"),
    Kriyartha(
        "3.3.11", "ghañ-ādi", bhava=True, wants=("ghañ", "bhāvavacana"),
        why="भाववचनाश्च — पाकाय व्रजति, भूतये व्रजति, पुष्टये व्रजति. "
            "The affixes given under 3.3.18 भावे, which name the act "
            "itself, come here too.\n\n"
            "किमर्थमिदं यावता विहिता एव ते? — why state it when they "
            "are given already? क्रियार्थोपपदे विहितेनास्मिन्विषये "
            "तुमुना बाध्येरन्: 3.3.10's तुमुन्, given for this very "
            "ground, would displace them, AND वासरूपविधिश्चात्र "
            "नास्तीत्युक्तम् — the escape by 3.1.94 was shut at "
            "3.3.10. So this rule exists BECAUSE of the suspension "
            "the rule before it established.\n\n"
            "अथ वचनग्रहणं किमर्थम्? वाचका यथा स्युः — the word वचन "
            "is there so the affixes must actually NAME the act: "
            "याभ्यः प्रकृतिभ्यो येन विशेषणेन विहिताः, यदि ताभ्यस्तथैव "
            "भवन्ति, from the same roots under the same conditions "
            "they were given for, नासामञ्जस्येन, and not "
            "irregularly.\n\n"
            "DEBT — the affixes this rule reaches are given at "
            "3.3.18 and after, which are not codified yet. The rule "
            "names a class by pointing FORWARD inside its own pāda"),
    Kriyartha(
        "3.3.12", "", karman=True, wants=("aṇ",),
        restates="3.2.1",
        why="अण् कर्मणि च — काण्डलावो व्रजति, अश्वदायो व्रजति, "
            "गोदायो व्रजति, कम्बलदायो व्रजति. चकारः सन्नियोगार्थः, "
            "the च joining this condition to the running ones rather "
            "than adding a separate ground.\n\n"
            "AND IT IS 3.2.1's OWN अण्, RESTATED. कर्मण्यण् इति "
            "सामान्येन विहितो वासरूपविधेरभावाद् ण्वुला बाधितः पुनरण् "
            "विधीयते — the अण् 3.2.1 gives for an object was "
            "displaced here by 3.3.10's ण्वुल्, and could not stand "
            "beside it because वासरूप is suspended, so it has to be "
            "said again. The third rule in a row whose existence the "
            "suspension explains.\n\n"
            "Once restated it wins twice over, and by two different "
            "principles: सोऽपवादत्वाद् ण्वुलं बाधते, being the "
            "narrower it defeats ण्वुल्; परत्वात् कादीन्, being later "
            "it defeats क and the rest. तेनापवादविषयेऽपि भवत्येव — so "
            "it holds even on ground those others had taken")
)


#: 3.3.12's OWN worked example — काण्डलावो व्रजति — put to 3.2.1,
#: which is where the अण् in it comes from: काण्डानि लुनातीति
#: काण्डलावः is 3.2.1's form, and 3.3.12 is the rule that lets it keep
#: the affix on this ground. Asking that rule rather than writing the
#: answer down is what makes the restatement checkable.
_KARMANI_EXAMPLE = dict(root="lū", beside="kāṇḍa", role="karman")


def restated_affix(sutra: str) -> str:
    """
    The affix a rule of the pāda before gives, asked of that rule.

    Only 3.2.1 is reached this way so far. The point is not generality
    but that the dependence be REAL: a declared reuse whose code holds
    a copied string is a claim the guard cannot check, which is how a
    false one survived a whole block once already.
    """
    if sutra != "3.2.1":
        return ""
    answer = upapada_affix(**_KARMANI_EXAMPLE)
    return answer.gives if getattr(answer, "by", "") == sutra else ""

def kriyartha_affix(*, wants: str = "", karman: bool = False,
                    bhava: bool = False, kriya: bool = True,
                    kriyartha: bool = True) -> object:
    """
    3.3.10 to 3.3.12 — which affix comes where a purpose-act stands
    beside the root.

    Both of 3.3.10's conditions must hold: an ACT stands beside
    (`kriya`), and the root's act is done FOR it (`kriyartha`). The
    vṛtti gives a counter-example for each separately, so neither is
    inferable from the other.

    Where more than one rule reaches the ground, `wants` names the
    affix being asked after — the idiom 3.2's तच्छीलादि run needed
    when thirteen pairs of rules turned out to share roots.
    """
    if not kriya:
        return NotAdded(
            "",
            "क्रियायामिति किम्? भिक्षिष्य इत्यस्य जटाः — 3.3.10 and "
            "the two after it want an ACT standing beside, and here "
            "none does")
    if not kriyartha:
        return NotAdded(
            "",
            "क्रियार्थायामिति किम्? धावतस्ते पतिष्यति दण्डः — an act "
            "stands beside, but the root's act is not done FOR it. "
            "The stick falls as he runs, not so that he may run")

    matched = [row for row in KRIYARTHA
               if (not row.karman or karman)
               and (not row.bhava or bhava)
               and (not wants or wants in row.wants)]
    if not matched:
        return NotAdded(
            "",
            "No rule of 3.3.10 to 3.3.12 gives that affix here. What "
            "this ground has is तुमुन् and ण्वुल् by 3.3.10, the "
            "भाववचन affixes by 3.3.11, and अण् where an object "
            "stands beside by 3.3.12")
    best = max(matched, key=_how_specific)
    # 3.3.10 gives तुमुन् AND ण्वुल्. Asked after one of them by name,
    # the answer must be the affix asked after and not whichever the
    # row happens to list first — the `wants` idiom exists precisely
    # because one rule can supply more than one.
    gives = best.gives
    if best.restates:
        # 3.3.12 does not have an affix of its own: it says 3.2.1's
        # again. Ask that rule for it, so the restatement is a call.
        gives = restated_affix(best.restates)
        if not gives:
            return NotAdded(
                best.sutra,
                "3.3.12 restates the अण् of %s, and that rule does not "
                "give one here" % best.restates)
    gives = wants if wants in best.wants and wants else gives
    also = best.also if gives == best.gives else ""
    return Added(gives, best.sutra, best.why, also=also)


def _how_specific(row: Kriyartha) -> int:
    """
    How much a row states.

    3.3.12 states one condition more than 3.3.10 and the vṛtti says
    it must win — सोऽपवादत्वाद् ण्वुलं बाधते — so specificity gives
    the answer the commentary already gave.
    """
    return 2 * row.karman + 2 * row.bhava


def vasarupa_suspended() -> Tuple[str, ...]:
    """
    The sūtras whose vṛtti says वासरूप does not hold over their ground.

    Read from the rules rather than listed, so the answer cannot drift
    from what the notes actually say. Two sections now suspend the
    principle 3.1.94 states, and this run is the second.
    """
    return tuple(row.sutra for row in KRIYARTHA
                 if "वासरूप" in row.why)

# -------------------------------------------------------------------------
# 3.3.16 to 3.3.37 — घञ्.
#
# भविष्यति stops here: भविष्यतीति निवृत्तम्, and इत उत्तरं त्रिष्वपि
# कालेषु प्रत्ययाः — from 3.3.16 the affixes hold in all three times.
# What runs instead are two conditions the vṛtti names at 3.3.19:
# इत उत्तरं भावे अकर्तरि च कारक इति च द्वयमनुवर्तते. So most rules of
# this run state a preverb and a root and let भाव or अकर्तृ-कारक come
# down from above, which is why the table carries both per row.
# -------------------------------------------------------------------------


def _bhidadi() -> Tuple[str, ...]:
    """
    3.3.104's भिदादि, read from the गणपाठ.

    The corpus keys three gaṇas to this pāda — गम्यादि at 3.3.3,
    भिदादि here, संपदादि at 3.3.108 — and asking it is the standing
    remedy for the mistake 3.2.5 and 3.2.15 recorded and 3.3.3 repeated:
    a list typed out of a commentary's running text loses a member.
    """
    try:
        from src.astadhyayi.corpus import load_ganapatha

        return tuple(
            item
            for gana in load_ganapatha().get("3.3.104", ())
            for item in gana.items
        )
    except Exception:
        return ()


#: 3.3.104's भिदादि, from the corpus. The vṛtti gives more forms than
#: the gaṇa carries — जरा and त्रपा come from its षित् half, not from
#: the list — and it also fixes senses for four of them: गुहा
#: गिर्योषध्योः, भिदा विदारणे, छिदा द्वैधीकरणे, आरा शस्त्र्याम्,
#: धारा प्रपाते, with भित्तिः, छित्तिः, आर्तिः, धृतिः for the rest.
BHIDADI: Tuple[str, ...] = _bhidadi()

#: 3.3.95's — स्था, गा, पा, पच्.
STHADI: Tuple[str, ...] = ("sthā", "gā", "pā", "pac")

#: 3.3.96's, and the rule holds them to मन्त्र.
VRSADI: Tuple[str, ...] = ("vṛṣ", "iṣ", "pac", "man", "vid", "bhū",
                           "vī", "rā")

#: 3.3.99's, where a NAME is meant.
SAMAJADI: Tuple[str, ...] = ("sam-aj", "ni-sad", "ni-pat", "man",
                             "vid", "ṣuñ", "śīṅ", "bhṛñ", "iṇ")

#: 3.3.105's five, all of the चुरादि class.
CINTADI: Tuple[str, ...] = ("cint", "pūj", "kath", "kumb", "carc")

#: 3.3.90's six roots — यज, याच, यत, विच्छ, प्रच्छ, रक्ष्.
YAJADI: Tuple[str, ...] = ("yaj", "yāc", "yat", "vicch",
                          "pracch", "rakṣ")


@dataclass(frozen=True)
class BhavaKrt:
    """
    One rule of the run, as the conditions it states.

    Most give घञ्, which is why that is the default, but
    3.3.43 gives णच्, 3.3.44 इनुण्, 3.3.56 अच् and 3.3.57 and
    after अप् — all on the one ground the headings of 3.3.18
    and 3.3.19 mark out.
    """

    sutra: str
    gives: str = "ghañ"
    #: A second affix the same rule gives beside the first —
    #: 3.3.60's चकारादप् च, so both न्यादः and निघसः stand.
    #: `Added` has carried this since 3.2.44; no row of this
    #: table wanted it until now.
    also: str = ""
    #: The roots the rule names. Empty means every root — 3.3.18 and
    #: 3.3.20 both reach all of them.
    of: Tuple[str, ...] = ()
    #: The preverbs it names. Empty means it names none; `any_upasarga`
    #: is the different case of 3.3.22, which wants one without saying
    #: which.
    upasarga: Tuple[str, ...] = ()
    any_upasarga: bool = False
    #: 3.3.24 wants NO preverb — अनुपसर्गे. Tri-state against the two
    #: above, since silence is not a prohibition.
    no_upasarga: object = None
    #: यथासंख्यम् rows, where the members are bound crosswise and the
    #: lists must not be crossed. Each entry is (preverb, root, sense).
    #: 3.3.28 binds two lists; 3.3.37 binds THREE, which is why the
    #: entries carry a sense as well.
    bound: Tuple[Tuple[str, str, str], ...] = ()
    #: The senses the rule allows, ANY ONE of which satisfies it,
    #: and the senses it refuses. Tuples because 3.3.41 names four
    #: at once — निवास, चिति, शरीर, उपसमाधान — and one string
    #: cannot hold alternatives.
    sense: Tuple[str, ...] = ()
    not_sense: Tuple[str, ...] = ()
    #: What the finished word is ABOUT, where a rule refuses one.
    #: 3.3.33 needs both axes at once — the sense must be spreading
    #: AND what is spread must not be speech — and writing the
    #: second into `not_sense` cancelled the first, since one input
    #: cannot be प्रथन and शब्द together. विस्तरो वचसाम् is the form
    #: it must refuse. A field-name collision of the kind that
    #: splits, as seven of the nine before it were.
    not_about: Tuple[str, ...] = ()
    #: What the finished WORD denotes — the field 3.2.25 had to be
    #: split off from `sense`, wanted again here by 3.3.30 and 3.3.34.
    names_a: str = ""
    #: 3.3.19's अकर्तरि च कारके — the affix names a कारक other than
    #: the agent — and 3.3.18's भावे, the act itself. Both run down
    #: from where they are stated, so rows after them carry them.
    bhava: bool = False
    akartari_karake: bool = False
    #: 3.3.19 and 3.3.34 want a NAME. Tri-state: 3.3.19 requires it.
    samjna: object = None
    #: 3.3.20's परिमाणाख्यायाम् — a measure is being named.
    parimana: bool = False
    #: 3.3.41 and 3.3.42 replace the root's first sound as well as
    #: adding the affix — आदेश् च कः. The only rules of the run
    #: that change the root, so the substitute is stated per row.
    adesha: str = ""
    #: 3.3.43's स्त्रियाम् — the finished word is feminine.
    stri: bool = False
    #: Which affix is being asked after, where two rules reach one
    #: ground and give different things — 3.3.114 क्त and 3.3.115
    #: ल्युट्, हसितम् and हसनम्, both good. The idiom three entry
    #: points of 3.2 needed when thirteen pairs of rules turned
    #: out to share roots.
    wants: Tuple[str, ...] = ()
    #: The root's FINAL SOUND, where a rule divides on it rather
    #: than naming roots. 3.3.56 wants इवर्णान्त and 3.3.57 wants
    #: ॠकारान्त or उवर्णान्त — the first two rules of this run to
    #: reach by shape instead of by list.
    #:
    #: NOT `ends_in`, which asks what a COMPOUND ends in (2.4.20
    #: to 2.4.25). That was the eighth field-name collision on
    #: record and this is the same pair a second time — the name
    #: was split apart once and then reached for again. It follows
    #: the house convention besides: `a_final`, `r_final` and
    #: `y_final` ask this of one sound each, and this asks it of
    #: several at once.
    root_final: Tuple[str, ...] = ()
    #: 3.3.72 to 3.3.75 vocalise the root as well as adding to it —
    #: संप्रसारणं च, so ह्वे gives हु and the word is हवः.
    samprasarana: bool = False
    #: What part the finished word names. 3.3.82 to 3.3.84 and
    #: 3.3.93 want करण or अधिकरण in particular, where the heading
    #: running from 3.3.19 asks only for something other than the
    #: agent. A narrowing of a condition already in force.
    karaka: str = ""
    #: 3.3.92 and 3.3.93 want a root bearing the name घु, which
    #: 1.1.20 दाधा घ्वदाप् confers. The row does not list those
    #: roots: the resolver ASKS that rule, as 3.3.14 asks 3.2.127
    #: for the name सत्.
    ghu: bool = False
    #: A root's उपदेश mark, where a rule reaches by it. 3.3.88
    #: wants ड्वित् and 3.3.89 ट्वित् — डु इद् यस्य, टु इद् यस्य.
    marked: str = ""
    #: 3.3.96's मन्त्रे — the form belongs to a Vedic verse. A
    #: one-way condition, as छन्दसि was in 3.2: a rule that wants
    #: it must not answer outside, and one that says nothing about
    #: it still answers inside.
    mantra: bool = False
    #: 3.3.102's प्रत्ययात् — the stem is already made with an
    #: affix, so the rule reaches चिकीर्ष and पुत्रीय rather than
    #: a bare root. 3.2.166 and 3.2.168 wanted particular such
    #: stems; this wants any.
    pratyayanta: bool = False
    #: 3.3.103's गुरोश्च हलः — a root with a heavy vowel AND
    #: ending in a consonant. Two conditions the vṛtti tests
    #: separately: गुरोरिति किम्? भक्तिः; हल इति किम्? नीतिः.
    gurumat: bool = False
    hal_final: bool = False
    #: 3.3.114 onward want the NEUTER, where 3.3.94 to 3.3.112
    #: wanted the feminine and 3.3.118 the masculine. The three
    #: genders divide this end of the pāda between them.
    napumsaka: bool = False
    pum: bool = False
    #: 3.3.126 to 3.3.130's ईषद्, दुर्, सु — and the senses they
    #: must carry, कृच्छ्र for दुर् and अकृच्छ्र for the other two.
    isadadi: bool = False
    #: 3.3.129 and 3.3.130 hold in the Veda only. One-way, as
    #: छन्दसि was throughout 3.2: a Vedic rule must not answer
    #: outside, and a rule silent about it still answers inside.
    chandasi: bool = False
    #: 3.3.130's गत्यर्थ — the root means going.
    gati_artha: bool = False
    #: 3.3.40's अस्तेये. Tri-state, because the rule requires the
    #: ABSENCE of theft and silence elsewhere is not a demand that
    #: theft be present. फलप्रचयश्चौर्येण is the form it refuses.
    steya: object = None
    #: विभाषा — the rule offers rather than requires. It starts at
    #: 3.3.50 and runs to the end of the घञ् rules, and 3.3.49
    #: borrows it BACKWARD by सिंहावलोकितन्याय.
    optional: bool = False
    why: str = ""


BHAVA_KRT: Tuple[BhavaKrt, ...] = (
    BhavaKrt("3.3.16", of=("pad", "ruj", "viś"),
         why="पदरुजविशस्पृशो घञ्: पद्यतेऽसौ पादः, रुजत्यसौ रोगः, "
             "विशत्यसौ वेशः.\n\n"
             "भविष्यति निवृत्तम्, and the vṛtti says what replaces it: "
             "इत उत्तरं त्रिष्वपि कालेषु प्रत्ययाः — from here the "
             "affixes hold in ALL THREE times. A heading dropped and "
             "nothing put in its place, which the commentary has to "
             "state because the sūtras cannot.\n\n"
             "SCOPE — स्पृश उपताप इति वक्तव्यम् is a vārttika holding "
             "स्पृश् to AFFLICTION: स्पर्श उपतापः. ततोऽन्यत्र पचाद्यच् "
             "भवति, स्पर्शो देवदत्तः — elsewhere 3.1.134's अच् comes "
             "instead, and स्वरे विशेषः, the two differ in ACCENT "
             "alone. Two identical spellings told apart by a feature "
             "the sūtrapāṭha on disk does not carry"),
    BhavaKrt("3.3.16", of=("spṛś",), sense=("upatāpa",),
         why="पदरुजविशस्पृशो घञ्, held to one sense for one of its "
             "four roots by a vārttika: स्पृश उपताप इति वक्तव्यम् — "
             "स्पृशतीति स्पर्श उपतापः, the touch that is an "
             "affliction. ततोऽन्यत्र पचाद्यच् भवति: elsewhere "
             "3.1.134's अच् gives स्पर्शो देवदत्तः, and स्वरे "
             "विशेषः — the two forms differ in ACCENT alone.\n\n"
             "Codified as a row of its own rather than merely "
             "recorded, because it CHANGES THE OUTPUT: without it "
             "this sūtra reaches स्पर्शो देवदत्तः too and the "
             "vārttika's own counter-example cannot be tested. The "
             "rule 3.2.24 established, met again — and the two rows "
             "carry one sūtra number between them, since one sūtra "
             "is what they are"),
    BhavaKrt("3.3.17", of=("sṛ",), sense=("sthira",),
         why="सृ स्थिरे: चन्दनसारः, खदिरसारः. स्थिर इति "
             "कालान्तरस्थायी पदार्थ उच्यते — what stays on into "
             "another time, and the vṛtti reasons the root into the "
             "sense rather than asserting it: स चिरं तिष्ठन् "
             "कालान्तरं सरतीति धात्वर्थस्य कर्ता युज्यते, standing "
             "long it 'moves' into another time, so the root फits. "
             "स्थिर इति किम्? सर्ता, सारकः.\n\n"
             "SCOPE — व्याधिमत्स्यबलेष्विति वक्तव्यम्: अतीसारो "
             "व्याधिः, विसारो मत्स्यः, सारो बलम्"),
    BhavaKrt("3.3.18", bhava=True,
         why="भावे: पाकः, त्यागः, रागः. THE RULE THE WHOLE RUN "
             "STANDS ON, and 3.3.11 pointed forward to it from seven "
             "sūtras back.\n\n"
             "क्रियासामान्यवाची भवतिः — भू is used because it names "
             "action AT LARGE, तेनार्थनिर्देशः क्रियमाणः "
             "सर्वधातुविषयः कृतो भवति, so naming the sense this way "
             "reaches every root. And the vṛtti separates two things "
             "carefully: धात्वर्थश्च धातुनैवोच्यते — the root already "
             "says its own meaning — यस्तस्य सिद्धता नाम धर्मः तत्र "
             "घञादयः प्रत्यया विधीयन्ते, and what the affix adds is "
             "the act's ACCOMPLISHEDNESS, its standing as a thing.\n\n"
             "पुँल्लिङ्गमेकवचनं चात्र न तन्त्रम् — the masculine "
             "singular of भावे is not binding: पक्तिः, पचनम्, "
             "पक्वम्, पाकौ, पाकाः all come. A grammatical form in the "
             "rule read as not meaning what it would mean anywhere "
             "else"),
    BhavaKrt("3.3.19", akartari_karake=True, samjna=True,
         why="अकर्तरि च कारके संज्ञायाम्: प्रास्यन्ति तं प्रासः, "
             "प्रसीव्यन्ति तं प्रसेवः, आहरन्ति तस्माद् रसमित्याहारः, "
             "मधुराहारः, तक्षशिलाहारः.\n\n"
             "अकर्तरीति किम्? मिषत्यसौ मेषः. संज्ञायामिति किम्? "
             "कर्तव्यः कटः. And चकारः संज्ञाव्यभिचारार्थः — the च is "
             "there so the NAME-sense may be departed from: को भवता "
             "दायो दत्तः, को भवता लाभो लब्धः.\n\n"
             "AND A ज्ञापक FROM A WORD THAT NEED NOT HAVE BEEN THERE. "
             "कारकग्रहणं पर्युदासे न कर्तव्यम् — with अकर्तरि read as "
             "an exclusion the word कारक is unnecessary; तत् क्रियते "
             "प्रसज्यप्रतिषेधेऽपि समासोऽस्तीति ज्ञापनार्थम्, it is "
             "stated to show that a compound is formed even with a "
             "flat negation, which is then used at 6.1.45. A "
             "redundancy in one rule licensing a compound in "
             "another.\n\n"
             "इत उत्तरं भावे अकर्तरि च कारक इति च द्वयमनुवर्तते — "
             "both conditions run forward from here, which is why "
             "the rows after this one carry them"),
    BhavaKrt("3.3.20", parimana=True,
         why="परिमाणाख्यायां सर्वेभ्यः: एकस्तण्डुलनिश्चायः, द्वौ "
             "शूर्पनिष्पावौ, द्वौ कारौ, त्रयः काराः.\n\n"
             "सर्वग्रहणमपोऽपि बाधनार्थम्: the word 'all' is there to "
             "defeat अप् as well — पुरस्तादपवादन्यायेन ह्यचमेव "
             "बाधेत नापम्, since by the ordinary reading an अपवाद "
             "displaces only what precedes it, and अप् comes after. "
             "A rule reaching FORWARD by saying 'all'.\n\n"
             "आख्याग्रहणं रूढिनिरासार्थम् — आख्या is said to keep out "
             "mere established usage, तेन संख्यापि गृह्यते, न "
             "प्रस्थाद्येव: so NUMBER counts as a measure too and not "
             "only the named units. परिमाणाख्यायामिति किम्? निश्चयः.\n\n"
             "SCOPE — घञनुक्रमणमजपोर्विषये, स्त्रीप्रत्ययास्तु न "
             "बाध्यन्ते: एका तिलोच्छ्रितिः, द्वे प्रसृती — the "
             "feminine affixes are NOT displaced. And दारजारौ कर्तरि "
             "णिलुक् च is a vārttika: दारयन्तीति दाराः, जरयन्तीति "
             "जाराः"),
    BhavaKrt("3.3.21", of=("iṅ",),
         why="इङश्च: अध्यायः, उपेत्यास्मादधीत उपाध्यायः. "
             "अचोऽपवादः.\n\n"
             "SCOPE — अपादाने स्त्रियामुपसंख्यानं तदन्ताच्च वा ङीष्: "
             "उपाध्याया, उपाध्यायी. And शृ वायुवर्णनिवृतेषु: शारो "
             "वायुः, शारो वर्णः, शारो निवृतम् — the vṛtti quoting a "
             "verse for the last"),
    BhavaKrt("3.3.22", of=("ru",), any_upasarga=True,
         why="उपसर्गे रुवः: संरावः, उपरावः. अपोऽपवादः. उपसर्ग इति "
             "किम्? रवः.\n\n"
             "The rule wants A PREVERB WITHOUT SAYING WHICH, which is "
             "a third possibility beside naming one (3.3.23) and "
             "refusing one (3.3.24). Three rules in a row, three "
             "different things done with the same category"),
    BhavaKrt("3.3.23", of=("yu", "dru", "du"), upasarga=("sam",),
         why="समि युद्रुदुवः: संयावः, संद्रावः, संदावः. समीति किम्? "
             "प्रयवः"),
    BhavaKrt("3.3.24", of=("śri", "ṇī", "bhū"), no_upasarga=True,
         why="श्रिणीभुवोऽनुपसर्गे: श्रायः, नायः, भावः. "
             "अजपोरपवादः. अनुपसर्ग इति किम्? प्रश्रयः, प्रणयः, "
             "प्रभवः.\n\n"
             "AND THE VṚTTI ANSWERS TWO APPARENT COUNTER-EXAMPLES "
             "RATHER THAN LETTING THEM STAND. कथं प्रभावो राज्ञः? "
             "प्रकृष्टो भाव इति प्रादिसमासो भविष्यति — that form is "
             "a compound of प्र with भाव, not this affix after a "
             "preverbed root. कथं च नयो राज्ञः? कृत्यल्युटो बहुलम् "
             "इत्यज् भविष्यति — 3.3.113 supplies it. A rule defended "
             "by parsing the awkward form differently, and by "
             "sending the other to a rule ninety sūtras ahead"),
    BhavaKrt("3.3.25", of=("kṣu", "śru"), upasarga=("vi",),
         why="वौ क्षुश्रुवः: विक्षावः, विश्रावः. अपोऽपवादः. वाविति "
             "किम्? क्षवः, श्रवः"),
    BhavaKrt("3.3.26", of=("nī",), upasarga=("ava", "ud"),
         why="अवोदोर्नियः: अवनायः, उन्नायः. कथमुन्नयः पदार्थानाम्? "
             "कृत्यल्युटो बहुलम् इत्यज् भविष्यति — the second appeal "
             "to 3.3.113 in three sūtras, and by now it is the "
             "commentary's standing answer for a form this run does "
             "not give"),
    BhavaKrt("3.3.27", of=("dru", "stu", "sru"), upasarga=("pra",),
         why="प्रे द्रुस्तुस्रुवः: प्रद्रावः, प्रस्तावः, प्रस्रावः. "
             "प्र इति किम्? द्रवः, स्तवः, स्रवः"),
    BhavaKrt("3.3.28",
         bound=(("nis", "pū", ""), ("abhi", "lū", "")),
         why="निरभ्योः पूल्वोः: निष्पावः, अभिलावः. यथासंख्यमुपसर्ग"
             "संबन्धः — निस् goes with पू and अभि with लू, and the "
             "lists must not be crossed. निरभ्योरिति किम्? पवः, "
             "लवः.\n\n"
             "पू इति पूङ्पूञोः सामान्येन ग्रहणम् — पू is taken "
             "GENERALLY, covering both the roots spelt so, which is "
             "the same question 3.2.39's द्वयोरपि ग्रहणम् settled "
             "and the same answer"),
    BhavaKrt("3.3.29", of=("gṝ",), upasarga=("ud", "ni"),
         why="उन्न्योर्ग्रः: उद्गारः समुद्रस्य, निगारो देवदत्तस्य. "
             "उन्न्योरिति किम्? गरः.\n\n"
             "गृ शब्दे and गृ निगरणे — द्वयोरपि ग्रहणम्, both roots "
             "spelt alike are meant. The second time in two sūtras, "
             "and the vṛtti uses the identical formula"),
    BhavaKrt("3.3.30", of=("kṝ",), upasarga=("ud", "ni"), names_a="dhānya",
         why="कॄ धान्ये: उत्कारो धान्यस्य, निकारो धान्यस्य. "
             "उन्न्योरिति वर्तते. धान्य इति किम्? भैक्ष्योत्करः, "
             "पुष्पनिकरः.\n\n"
             "AND ONE OF TWO ROOTS IS EXCLUDED BY अनभिधानात्. "
             "विक्षेपार्थस्य किरतेर्ग्रहणम्, न हिंसार्थस्य, "
             "अनभिधानात् — the कॄ meaning to scatter is meant, not "
             "the one meaning to hurt, and the ground is that no such "
             "word exists. The same limit 3.2.1 and 3.1.108 were "
             "held by, and it is not a condition the rule states"),
    BhavaKrt("3.3.31", of=("stu",), upasarga=("sam",), sense=("yajña",),
         why="यज्ञे समि स्तुवः: संस्तावश्छन्दोगानाम्. And the vṛtti "
             "defines by the situation: समेत्य स्तुवन्ति यस्मिन् "
             "देशे छन्दोगाः, स देशः संस्ताव इत्युच्यते — the PLACE "
             "where the chanters gather and praise. यज्ञ इति किम्? "
             "संस्तवश्छात्रयोः"),
    BhavaKrt("3.3.32", of=("stṝ",), upasarga=("pra",), not_sense=("yajña",),
         why="प्रे स्त्रोऽयज्ञे: शङ्खप्रस्तारः. अयज्ञ इति किम्? "
             "बर्हिष्प्रस्तरः. The rule before wanted the sacrifice "
             "and this one refuses it — a pair divided by one sense, "
             "one sūtra apart"),
    BhavaKrt("3.3.33", of=("stṝ",), upasarga=("vi",), sense=("prathana",),
         not_about=("śabda",),
         why="प्रथने वावशब्दे: पटस्य विस्तारः. प्रथनं विस्तीर्णता, "
             "spreading out. TWO conditions and both tested: प्रथन "
             "इति किम्? तृणविस्तरः. अशब्द इति किम्? विस्तरो वचसाम् — "
             "of speech spread out the affix does not come, though "
             "the spreading is real"),
    BhavaKrt("3.3.34", of=("stṝ",), upasarga=("vi",),
         names_a="chandonāman",
         why="छन्दोनाम्नि च: विष्टारपङ्क्तिश्छन्दः, विष्टारबृहती "
             "छन्दः. वौ स्त्र इति वर्तते.\n\n"
             "AND THE VṚTTI FIXES WHICH छन्दस् IS MEANT BY THE WORD "
             "नामन् ALONE. वृत्तमत्र छन्दो गृह्यते, यस्य गायत्र्यादयो "
             "विशेषाः, न मन्त्रब्राह्मणम्, नामग्रहणात् — METRE is "
             "meant, of which गायत्री and the rest are kinds, and "
             "not sacred text, and the ground is that the rule says "
             "'name'. Metres have names; scripture is not named that "
             "way.\n\n"
             "विष्टारपङ्क्तिशब्दोऽत्र छन्दोनाम, न घञन्तं शब्दरूपम् — "
             "and the NAME is the whole word, the घञ्-form being only "
             "a part of it, तत्र त्ववयवत्वेन वर्तते. A condition on "
             "the whole, as four rules of 3.2 had. "
             "छन्दोनाम्नीत्यधिकरणसप्तम्येषा"),
    BhavaKrt("3.3.35", of=("grah",), upasarga=("ud",),
         why="उदि ग्रहः: उद्ग्राहः. अपोऽपवादः.\n\n"
             "SCOPE — छन्दसि निपूर्वादपीष्यते स्रुगुद्यमननिपातनयोः is "
             "a vārttika, with हकारस्य भकारः: उद्ग्राभं च निग्राभं च "
             "ब्रह्म देवा अवीवृधन् (मा०सं० १७.६४). A Vedic form where "
             "the root's ह becomes भ, quoted with its passage"),
    BhavaKrt("3.3.36", of=("grah",), upasarga=("sam",), sense=("muṣṭi",),
         why="समि मुष्टौ: अहो मल्लस्य संग्राहः, अहो मुष्टिकस्य "
             "संग्राहः. मुष्टिरङ्गुलिसंनिवेशः, the set of the "
             "fingers, and दृढमुष्टिताख्यायते — what is being spoken "
             "of is a firm grip. मुष्टाविति किम्? संग्रहो धान्यस्य"),
    BhavaKrt("3.3.37",
         bound=(("pari", "nī", "dyūta"), ("ni", "i", "abhreṣa")),
         why="परिन्योर्नीणोर्द्यूताभ्रेषयोः — अचोऽपवादः. "
             "यथासंख्यम् BINDING THREE LISTS AT ONCE, which no rule "
             "of the pāda before did: द्यूताभ्रेषयोः, अत्रापि "
             "यथासंख्यमेव संबन्धः. परि goes with नी and with dicing, "
             "नि with इण् and with correctness — "
             "द्यूतविषयश्चेन्नयतेरर्थः, अभ्रेषविषयश्चेदिणर्थः. "
             "3.2.5 and 3.2.13 bound two lists; 3.2.186 bound a "
             "kāraka to a kind of being; this binds preverb, root and "
             "sense in one stroke.\n\n"
             "परिणायेन शारान् हन्ति, समन्तान्नयनेन — moving the "
             "pieces about. एषोऽत्र न्यायः for the other. "
             "पदार्थानामनपचारो यथाप्राप्तकरणमभ्रेषः, doing things as "
             "they should be done. द्यूताभ्रेषयोरिति किम्? परिणयः, "
             "न्ययं गतः पापः"),
    BhavaKrt("3.3.38", of=("i",), upasarga=("pari",),
         sense=("anupātyaya",),
         why="परावनुपात्यय इणः: तव पर्यायः, मम पर्यायः. "
             "क्रमप्राप्तस्यानतिपातोऽनुपात्ययः, परिपाटी — not "
             "overstepping what comes in turn. अनुपात्यय इति किम्? "
             "कालस्य पर्ययः, अतिपात इत्यर्थः: with the overstepping "
             "the word means the opposite, and the affix does not "
             "come. One preverb and one root giving two words that "
             "differ by a single sound and mean contrary things"),
    BhavaKrt("3.3.39", of=("śī",), upasarga=("vi", "upa"),
         sense=("paryāya",),
         why="व्युपयोः शेतेः पर्याये: तव विशायः, तव राजोपशायः — "
             "तव राजानमुपशयितुं पर्याय इत्यर्थः, your turn to lie "
             "by the king. पर्याय इति किम्? विशयः, उपशयः"),
    BhavaKrt("3.3.40", of=("ci",), sense=("hastādāna",), steya=False,
         why="हस्तादाने चेरस्तेये: पुष्पप्रचायः, फलप्रचायः. "
             "हस्तादानग्रहणेन प्रत्यासत्तिरादेयस्य लक्ष्यते — what "
             "the word marks is that the thing is WITHIN REACH.\n\n"
             "TWO CONDITIONS ON DIFFERENT FOOTINGS, as 3.3.33 had. "
             "हस्तादान इति किम्? वृक्षशिखरे फलप्रचयं करोति — picking "
             "from the treetop is not within reach. अस्तेय इति किम्? "
             "फलप्रचयश्चौर्येण — picking by theft is within reach and "
             "still refused. So the second is not a kind of the "
             "first, and a tri-state carries it: the rule requires "
             "the ABSENCE of theft, and silence elsewhere is not a "
             "demand that theft be present.\n\n"
             "SCOPE — उच्चयस्य प्रतिषेधो वक्तव्यः"),
    BhavaKrt("3.3.41", of=("ci",), adesha="ka",
         sense=("nivāsa", "citi", "śarīra", "upasamādhāna"),
         why="निवासचितिशरीरोपसमाधानेष्वादेश्च कः: चिखल्लिनिकायः, "
             "आकायमग्निं चिन्वीत, अनित्यकायः, महान् गोमयनिकायः. "
             "निवसन्त्यस्मिन्निति निवासः; चीयतेऽसौ चितिः; "
             "पाण्यादिसमुदायः शरीरम्; राशीकरणमुपसमाधानम्.\n\n"
             "FOUR SENSES IN ONE RULE, which is why the field holds "
             "alternatives rather than one string. एतेष्विति किम्? "
             "चयः.\n\n"
             "AND THE RULE CHANGES THE ROOT AS WELL AS ADDING TO IT. "
             "आदेश् च कः — the first sound of चि becomes क, so the "
             "word is काय and not *चाय. The only rules of this run "
             "that touch the root, and the substitute is stated per "
             "row because nothing else in the table does it.\n\n"
             "SCAR — A FORM REFUSED BY WHAT THE SPEAKER MEANT. इह "
             "कस्माद् न भवति महान् काष्ठनिचयः? बहुत्वमत्र विवक्षितं "
             "नोपसमाधानम् — mere MUCHNESS is meant there and not "
             "heaping-up, so the sense is absent though the situation "
             "looks the same. विवक्षा is not readable from a form, "
             "and this is passed in like every other semantic "
             "condition"),
    BhavaKrt("3.3.42", of=("ci",), adesha="ka", sense=("saṅgha",),
         why="संघे चानौत्तराधर्ये: भिक्षुकनिकायः, ब्राह्मणनिकायः, "
             "वैयाकरणनिकायः.\n\n"
             "AND THE CONDITION IS CARVED OUT OF A DEFINITION. "
             "प्राणिनां समुदायः संघः — a संघ is a group of LIVING "
             "beings — स च द्वाभ्यां प्रकाराभ्यां भवति, and it comes "
             "about two ways: एकधर्मसमावेशेन, by sharing one "
             "property, or औत्तराधर्येण, by ranking above and below. "
             "तत्र औत्तराधर्यपर्युदासादितरो गृह्यते: the rule "
             "excludes the second, so the first is what is left. A "
             "condition stated by removing one half of a definition "
             "the rule does not give.\n\n"
             "अनौत्तराधर्य इति किम्? सूकरनिचयः. And two more fall "
             "outside for the OTHER half of the definition, which "
             "the rule never states: कृताकृतसमुच्चयः, "
             "प्रमाणसमुच्चयः — प्राणिविषयत्वात् संघस्येह न भवति, "
             "these are not groups of living beings at all"),
    BhavaKrt("3.3.43", gives="ṇac", sense=("karmavyatihāra",),
         stri=True,
         why="कर्मव्यतिहारे णच् स्त्रियाम्: व्यावक्रोशी, व्यावलेखी, "
             "व्यावहासी वर्तते. कर्म क्रिया, व्यतिहारः "
             "परस्परकरणम् — doing a thing to each other. तच्च भावे, "
             "so भावे runs down into it.\n\n"
             "चकारो विशेषणार्थः for 5.4.14 णचः स्त्रियामञ् — the च is "
             "spent so that a rule two adhyāyas on can pick this "
             "affix out. स्त्रियामिति किम्? व्यतिपाको वर्तते.\n\n"
             "SCOPE — बाधकविषयेऽपि क्वचिदिष्यते: व्यावचोरी, "
             "व्यावचर्ची stand even where a displacing rule reaches. "
             "इह न भवति — व्यतीक्षा, व्यतीहा वर्तते; व्यात्युक्षी "
             "भवति. तदेतद् वैचित्र्यं कथं लभ्यते? कृत्यल्युटो बहुलम् "
             "इति भवति — the third appeal to 3.3.113, and this time "
             "for the IRREGULARITY itself rather than for one form"),
    BhavaKrt("3.3.44", gives="inuṇ", sense=("abhividhi",), bhava=True,
         why="अभिविधौ भाव इनुण्: सांकूटिनम्, सांराविणम्, सान्द्राविणं "
             "वर्तते. अभिविधिरभिव्याप्तिः, क्रियागुणाभ्यां "
             "कार्त्स्न्येन संबन्धः — being bound up with an act or "
             "a quality entirely. अभिविधाविति किम्? संकोटः, संरावः, "
             "संद्रावः.\n\n"
             "AND वासरूप IS SUSPENDED HERE BY REPEATING A WORD, not "
             "by a ज्ञापक. भाव इति वर्तमाने पुनर्भावग्रहणं "
             "वासरूपनिरासार्थम्, तेन घञ् न भवति — भावे was already "
             "running from 3.3.18, and saying it AGAIN cancels "
             "3.1.94 so that घञ् cannot stand beside this affix. The "
             "fourth suspension met, and the first done this way: "
             "3.2.146, 3.2.177 and 3.3.10 all argued from a ज्ञापक.\n\n"
             "ल्युटा तु समावेश इष्यते, संकूटनं वर्तते. तत् कथम्? "
             "कृत्यल्युटो बहुलम् इति — so the suspension is not "
             "total, and 3.3.113 lets ल्युट् in beside. Fourth "
             "appeal to that rule in this run"),
    BhavaKrt("3.3.45", of=("grah",), upasarga=("ava", "ni"),
         sense=("ākrośa",),
         why="आक्रोशेऽवन्योर्ग्रहः: अवग्राहो हन्त ते वृषल भूयात्, "
             "निग्राहो हन्त ते वृषल भूयात्. आक्रोशः शपनम्, cursing. "
             "आक्रोश इति किम्? अवग्रहः पदस्य, निग्रहश्चोरस्य.\n\n"
             "AND WHICH AFFIX IS CARRIED DOWN IS NOT THE NEAREST ONE. "
             "दृष्टानुवृत्तिसामर्थ्याद् घञनुवर्तते, नानन्तर इनुण् — "
             "घञ् runs down from further back and 3.3.44's इनुण्, "
             "standing immediately before, does NOT. The ground is "
             "the strength of an अनुवृत्ति already seen at work. "
             "3.2.122's मण्डूकप्लुति showed a condition vaulting "
             "forward over rules; this shows the nearest word losing "
             "to a further one"),
    BhavaKrt("3.3.46", of=("grah",), upasarga=("pra",),
         sense=("lipsā",),
         why="प्रे लिप्सायाम्: पात्रप्रग्राहेण चरति भिक्षुः "
             "पिण्डार्थी, स्रुवप्रग्राहेण चरति द्विजो दक्षिणार्थी — "
             "a monk going about with his bowl held out, a brahmin "
             "with his ladle. लिप्सायामिति किम्? प्रग्रहो "
             "देवदत्तस्य.\n\n"
             "लिप्सा was 3.3.6's condition too, forty sūtras back "
             "and for a tense-ending rather than an affix. The same "
             "sense doing work in two quite different questions"),
    BhavaKrt("3.3.47", of=("grah",), upasarga=("pari",),
         sense=("yajña",),
         why="परौ यज्ञे: उत्तरपरिग्राहः. यज्ञविषयश्चेत् "
             "प्रत्ययान्ताभिधेयः स्यात् — the condition is on what "
             "the FINISHED WORD denotes and not on the act. "
             "यज्ञ इति किम्? परिग्रहो देवदत्तस्य"),
    BhavaKrt("3.3.48", of=("vṛ",), upasarga=("ni",), names_a="dhānya",
         why="नौ वृ धान्ये: नीवारा नाम व्रीहयो भवन्ति — a kind of "
             "wild rice. अपोऽपवादः. धान्य इति किम्? निवरा कन्या.\n\n"
             "वृ इति वृङ्वृञोः सामान्येन ग्रहणम् — the THIRD time in "
             "this run that a spelling is taken generally over two "
             "roots, after 3.3.28's पू and 3.3.29's गृ. The formula "
             "is the commentary's standing move, and it has now been "
             "used three times in twenty sūtras"),
    BhavaKrt("3.3.49", of=("śri", "yu", "pū", "dru"), upasarga=("ud",),
         optional=True,
         why="उदि श्रयतियौतिपूद्रुवः: उच्छ्रायः, उद्यावः, उत्पावः, "
             "उद्द्रावः. अजपोरपवादः.\n\n"
             "AND ITS OPTIONALITY IS BORROWED FROM THE RULE AFTER IT. "
             "कथं पतनान्ताः समुच्छ्रयाः? — how does the short form "
             "stand? वक्ष्यमाणं विभाषाग्रहणमिह सिंहावलोकितन्यायेन "
             "संबध्यते: the विभाषा about to be stated at 3.3.50 is "
             "read BACK into this rule by the LION'S BACKWARD GLANCE. "
             "A device this project has not met. अनुवृत्ति runs "
             "forward; 3.2.122's मण्डूकप्लुति vaults forward over "
             "intervening rules; this looks BACKWARD, so a word not "
             "yet uttered conditions a rule already given. Codified "
             "as `optional` on this row, with the borrowing recorded "
             "— there is no way to represent a word that has not "
             "been said yet"),
    BhavaKrt("3.3.50", of=("ru", "plu"), upasarga=("āṅ",), optional=True,
         why="विभाषाङि रुप्लुवोः: आरावः and आरवः, आप्लावः and "
             "आप्लवः — both stand, which is what विभाषा buys. And "
             "the word is spent twice over: 3.3.49 borrows it "
             "backward by सिंहावलोकित, and it runs FORWARD from here "
             "to the end of the घञ् rules"),
    BhavaKrt("3.3.51", of=("grah",), upasarga=("ava",),
         sense=("varṣapratibandha",), optional=True,
         why="अवे ग्रहो वर्षप्रतिबन्धे: अवग्राहो देवस्य, अवग्रहो "
             "देवस्य. प्राप्तकालस्य वर्षस्य कुतश्चिन्निमित्तादभावो "
             "वर्षप्रतिबन्धः — a drought, rain due and withheld. "
             "वर्षप्रतिबन्ध इति किम्? अवग्रहः पदस्य — where the same "
             "word means the pause between two parts of a compound"),
    BhavaKrt("3.3.52", of=("grah",), upasarga=("pra",), names_a="vaṇij",
         optional=True,
         why="प्रे वणिजाम्: तुलाप्रग्राहेण चरति, तुलाप्रग्रहेण चरति. "
             "वणिजामिति किम्? प्रग्रहो देवदत्तस्य.\n\n"
             "AND THE MERCHANTS ARE NOT THE POINT. वणिक्संबन्धेन च "
             "तुलासूत्रं लक्ष्यते, न तु वणिजस्तन्त्रम् — naming them "
             "MARKS OUT the scale-cord, and is not itself the "
             "condition: तुला प्रगृह्यते येन सूत्रेण स शब्दार्थः, "
             "the word means the cord by which the balance is held. "
             "So वणिगन्यो वा — a merchant or anyone else. A rule "
             "whose stated condition is a pointer to the real one"),
    BhavaKrt("3.3.53", of=("grah",), upasarga=("pra",), names_a="raśmi",
         optional=True,
         why="रश्मौ च: प्रग्राहः, प्रग्रहः. "
             "रथादियुक्तानामश्वादीनां संयमनार्था रज्जू रश्मिरिह "
             "गृह्यते — the rein by which harnessed horses are held. "
             "ग्रहो विभाषा प्र इति वर्तते, three things carried down "
             "at once from three different places"),
    BhavaKrt("3.3.54", of=("vṛ",), upasarga=("pra",),
         sense=("ācchādana",), optional=True,
         why="वृणोतेराच्छादने: प्रावारः, प्रवरः — a cloak. "
             "प्रत्ययान्तेन चेदाच्छादनविशेष उच्यते, the finished word "
             "naming a particular COVERING. आच्छादन इति किम्? "
             "प्रवरा गौः"),
    BhavaKrt("3.3.55", of=("bhū",), upasarga=("pari",),
         sense=("avajñāna",), optional=True,
         why="परौ भुवोऽवज्ञाने: परिभावः, परिभवः. अवज्ञानमसत्कारः, "
             "contempt. अवज्ञान इति किम्? सर्वतो भवनं परिभवः — where "
             "the word means being all round, the affix does not "
             "come, and the short form stands for both.\n\n"
             "SCAR — THE TWO EDITIONS OF THE MŪLA DISAGREE HERE, AND "
             "THE COMMENTARY SETTLES IT. GRETIL reads प्रौ, Vidyut "
             "reads परौ, and they are different preverbs. The Kāśikā "
             "is decisive: परिशब्द उपपदे भवतेः, and every form it "
             "gives is परिभावः, परिभवः. So परौ is right and GRETIL is "
             "wrong. The collation already flags the pair as "
             "divergent; what the commentary adds is which witness to "
             "believe"),
    BhavaKrt("3.3.56", gives="ac", root_final=("i", "ī"),
         why="एरच् — चयः, अयः, जयः, क्षयः. घञोऽपवादः, and the FIRST "
             "rule of the run to reach by the root's SHAPE rather "
             "than by naming roots.\n\n"
             "चकारो विशेषणार्थः for 6.2.143 अन्तः and 6.2.144 "
             "थाथघञ्क्ताजबित्रकाणाम् — the च is spent so that two "
             "accent rules three adhyāyas on can pick this affix "
             "out. The same use of a च as 3.3.43's.\n\n"
             "AND THE VṚTTI SAYS HOW FAR THE HEADINGS REACH. भावे, "
             "अकर्तरि च कारक इति प्रकृतमनुवर्तते यावत् कृत्यल्युटो "
             "बहुलम् इति — the two conditions run from 3.3.18 and "
             "3.3.19 all the way to 3.3.113. An extent stated "
             "outright, as 3.2.134's आ क्वेः was, and this one names "
             "the rule rather than a number.\n\n"
             "SCOPE — अज्विधौ भयादीनामुपसंख्यानम्, नपुंसके "
             "क्तादिनिवृत्त्यर्थम्: भयम्, वर्षम्. And जवसवौ छन्दसि "
             "वक्तव्यौ — ऊर्वोरस्तु मे जवः (पै०सं० २०.३६.७), "
             "पञ्चौदनस् सवः (पै०सं० ८.१९.३)"),
    BhavaKrt("3.3.57", gives="ap", root_final=("ṝ", "u", "ū"),
         why="ॠदोरप् — करः, गरः, शरः; यवः, स्तवः, लवः, पवः. "
             "घञोऽपवादः, and 3.3.20's सर्वग्रहण was spent thirty-seven "
             "sūtras back to reach forward and defeat THIS affix.\n\n"
             "TWO MARKS, NEITHER OF THEM DOING GRAMMAR. पित्करणं "
             "स्वरार्थम् — the प is for the accent; दकारो "
             "मुखसुखार्थः, मा भूत् तादपि परस्तपरः, the द is for ease "
             "of pronunciation, so that the rule does not read as "
             "तपर. A letter in a sūtra put there to keep the sūtra "
             "sayable"),
    BhavaKrt("3.3.58", gives="ap",
         of=("grah", "vṛ", "dṛ", "niści", "gam"),
         why="ग्रहवृदृनिश्चिगमश्च — ग्रहः, वरः, दरः, निश्चयः, गमः. "
             "घञोऽपवादः, निश्चिनोतेस्त्वचोऽपवादः. निश्चिग्रहणं "
             "स्वरार्थम् — that root is named for the ACCENT alone, "
             "the affix being reachable without it.\n\n"
             "SCOPE — वशिरण्योरुपसंख्यानम्: वशः, रणः. And a longer "
             "one, घञर्थे कविधानं स्थास्नापाव्यधिहनियुध्यर्थम्, "
             "giving six words with क where घञ् would be expected: "
             "प्रतिष्ठन्तेऽस्मिन्निति प्रस्थः, प्रस्नः, "
             "प्रपिबन्त्यस्यामिति प्रपा, आविधः, विहन्यन्तेऽस्मिन्निति "
             "विघ्नः, आयुध्यतेऽनेनेत्यायुधम्"),
    BhavaKrt("3.3.59", gives="ap", of=("ad",), any_upasarga=True,
         why="उपसर्गेऽदः — विघसः, प्रघसः. उपसर्ग इति किम्? घासः. "
             "The second rule to want A PREVERB without saying which, "
             "after 3.3.22"),
    BhavaKrt("3.3.60", gives="ṇa", also="अप्", of=("ad",),
         upasarga=("ni",),
         why="नौ णश्च — न्यादः by the ण, निघसः by the च, which "
             "brings अप् down as well. चकारादप् च: so the rule gives "
             "TWO affixes and the vṛtti gets both forms out of it"),
    BhavaKrt("3.3.61", gives="ap", of=("vyadh", "jap"),
         no_upasarga=True,
         why="व्यधजपोरनुपसर्गे — व्यधः, जपः. घञोऽपवादः. अनुपसर्ग "
             "इति किम्? आव्याधः, उपजापः"),
    BhavaKrt("3.3.62", gives="ap", of=("svan", "has"),
         no_upasarga=True, optional=True,
         why="स्वनहसोर्वा — स्वनः and स्वानः, हसः and हासः, both "
             "standing. अनुपसर्ग इत्येव: प्रस्वानः, प्रहासः"),
    BhavaKrt("3.3.63", gives="ap", of=("yam",),
         upasarga=("sam", "upa", "ni", "vi"), optional=True,
         why="यमः समुपनिविषु च — संयमः and संयामः, उपयमः and "
             "उपयामः, नियमः and नियामः, वियमः and वियामः. "
             "अनुपसर्गे वेति वर्तते, so अनुपसर्गात् खल्वपि — यमः, "
             "यामः: the rule adds four preverbs to a condition of "
             "NO preverb, and both grounds stand together"),
    BhavaKrt("3.3.64", gives="ap",
         of=("gad", "nad", "paṭh", "svan"), upasarga=("ni",),
         optional=True,
         why="नौ गदनदपठस्वनः — निगदः and निगादः, निनदः and निनादः, "
             "निपठः and निपाठः, निस्वनः and निस्वानः. घञोऽपवादः"),
    BhavaKrt("3.3.65", gives="ap", of=("kvaṇ",), sense=("vīṇā",),
         optional=True,
         why="क्वणो वीणायां च — निक्वणः and निक्वाणः; क्वणः and "
             "क्वाणः without a preverb; and कल्याणप्रक्वणा वीणा "
             "where a lute is meant.\n\n"
             "सोपसर्गार्थं वीणाया ग्रहणम् — the lute is named so "
             "that the rule reaches a PREVERBED root too, नौ and "
             "अनुपसर्गे having been all it would otherwise have "
             "had. एतेष्विति किम्? अतिक्वाणो वर्तते"),
    BhavaKrt("3.3.66", gives="ap", of=("paṇ",), parimana=True,
         why="नित्यं पणः परिमाणे — मूलकपणः, शाकपणः. "
             "संव्यवहाराय मूलकादीनां यः परिमितो मुष्टिर्बध्यते, "
             "तस्येदमभिधानम्: the measured bundle tied for sale.\n\n"
             "नित्यग्रहणं विकल्पनिवृत्त्यर्थम् — the word नित्यम् is "
             "there to STOP the option running down from 3.3.62, "
             "which had reached this far. A rule cancelling an "
             "अनुवृत्ति by naming its opposite, where 3.3.44 "
             "cancelled a principle by repeating a word. "
             "परिमाण इति किम्? पाणः"),
    BhavaKrt("3.3.67", gives="ap", of=("mad",), no_upasarga=True,
         why="मदोऽनुपसर्गे — विद्यामदः, धनमदः, कुलमदः. घञोऽपवादः. "
             "अनुपसर्ग इति किम्? उन्मादः, प्रमादः"),
    BhavaKrt("3.3.69", gives="ap", of=("aj",), upasarga=("sam", "ud"),
         names_a="paśu",
         why="समुदोरजः पशुषु — समजः पशूनाम्, उदजः पशूनाम्. "
             "घञोऽपवादः. पशुष्विति किम्? समाजो ब्राह्मणानाम्, "
             "उदाजः क्षत्रियाणाम् — of men the long form stands, of "
             "beasts the short.\n\n"
             "अज गतिक्षेपणयोः, and the vṛtti divides the two senses "
             "between the two preverbs without the rule saying so: "
             "स संपूर्वः समुदाये वर्तते, उत्पूर्वश्च प्रेरणे — with "
             "सम् it is gathering, with उद् driving"),
    BhavaKrt("3.3.71", gives="ap", of=("sṛ",), sense=("prajana",),
         why="प्रजने सर्तेः — गवामुपसरः, पशूनामुपसरः. घञोऽपवादः. "
             "प्रजनं प्रथमं गर्भग्रहणम्, and the vṛtti spells the "
             "situation out: स्त्रीगवीषु पुंगवानां गर्भाधानाय "
             "प्रथममुपसरणमुच्यते"),
    BhavaKrt("3.3.72", gives="ap", of=("hve",),
         upasarga=("ni", "abhi", "upa", "vi"), samprasarana=True,
         why="ह्वः संप्रसारणं च न्यभ्युपविषु — निहवः, अभिहवः, "
             "विहवः. घञोऽपवादः. एतेष्विति किम्? प्रह्वायः.\n\n"
             "THE RULE VOCALISES THE ROOT AS WELL AS ADDING TO IT. "
             "संप्रसारणं च: ह्वे gives हु, so the word is हवः and "
             "not *ह्वायः. With 3.3.41's क and 3.3.76's वध, a third "
             "kind of rule in this pāda that changes the root"),
    BhavaKrt("3.3.73", gives="ap", of=("hve",), upasarga=("āṅ",),
         sense=("yuddha",), samprasarana=True,
         why="आङि युद्धे — आहूयन्तेऽस्मिन्नित्याहवः, a battle: the "
             "place into which men are called. युद्ध इति किम्? "
             "आह्वायः"),
    BhavaKrt("3.3.75", gives="ap", of=("hve",), no_upasarga=True,
         bhava=True, samprasarana=True,
         why="भावेऽनुपसर्गस्य — हवः, and the vṛtti quotes the Ṛgveda "
             "for it: हवे हवे सुहवं शूरमिन्द्रम् (ऋ० ६.४७.११). "
             "अनुपसर्गस्येति किम्? आह्वायः.\n\n"
             "AND भाव IS SAID HERE TO SHUT OUT THE OTHER HEADING. "
             "भावग्रहणम् अकर्तरि च कारके संज्ञायाम् इत्यस्य "
             "निरासार्थम् — both 3.3.18's भावे and 3.3.19's "
             "अकर्तरि कारके have been running side by side since they "
             "were stated, and naming one CANCELS the other. The "
             "second time a word already running is repeated to take "
             "something away, after 3.3.44"),
    BhavaKrt("3.3.76", gives="ap", of=("han",), no_upasarga=True,
         bhava=True, adesha="vadha",
         why="हनश्च वधः — वधश्चोराणाम्, वधो दस्यूनाम्. The root is "
             "REPLACED as well: तत्संनियोगेन च वधादेशः, स "
             "चान्तोदात्तः, and the substitute is accented on its "
             "last syllable so that तत्रोदात्तनिवृत्तिस्वरेण the "
             "affix becomes उदात्त. भाव इत्येव — घातः; "
             "अनुपसर्गस्येत्येव — प्रघातः, विघातः.\n\n"
             "AND THE च IS READ AGAINST ITS OWN POSITION. चकारो "
             "भिन्नक्रमत्वाद् नादेशेन संबध्यते, किं तर्हि? प्रकृतेन "
             "प्रत्ययेन — standing where it does the च would join "
             "the SUBSTITUTE, and it is taken instead with the affix "
             "running down: अप् च, यश्चापरः प्राप्नोति, तेन घञपि "
             "भवति, घातो वर्तते. So घञ् stands beside after all, and "
             "the word order of the sūtra is overruled by what makes "
             "sense of it"),
    BhavaKrt("3.3.77", gives="ap", of=("han",), sense=("mūrti",),
         adesha="ghana",
         why="मूर्तौ घनः — अभ्रघनः, दधिघनः. मूर्तिः काठिन्यम्, "
             "hardness, curdling.\n\n"
             "कथं घनं दधीति? धर्मशब्देन धर्मी भण्यते — how can the "
             "curd BE the hardening? Because a word for the quality "
             "names the thing that has it. A figure of speech "
             "admitted into the grammar to save a form"),
    BhavaKrt("3.3.78", gives="ap", of=("han",), upasarga=("antar",),
         names_a="deśa", adesha="ghana",
         why="अन्तर्घनो देशे — संज्ञीभूतो वाहीकेषु देशविशेष उच्यते, "
             "a particular place among the Vāhīkas. देश इति किम्? "
             "अन्तर्घातोऽन्यः.\n\n"
             "अन्ये णकारं पठन्ति — अन्तर्घणो देश इति, तदपि "
             "ग्राह्यमेव: OTHERS READ ण, and that is acceptable too. "
             "The commentary recording a variant reading and "
             "declining to choose — where at 3.3.55 it chose"),
    BhavaKrt("3.3.82", gives="ap", of=("han",),
         upasarga=("ayas", "vi", "dru"), karaka="karaṇa",
         adesha="ghana",
         why="अयस्विद्रुहनः — अयो हन्यतेऽनेनेत्ययोघनः, विघनः, "
             "द्रुघनः. करणे कारके, and घनादेशः.\n\n"
             "SCOPE — द्रुघण इति केचिदुदाहरन्ति, कथं णत्वम्? "
             "अरीहणादिषु पाठात्, 8.4.3 पूर्वपदात् संज्ञायामगः इति वा "
             "— a variant with ण, and the vṛtti offers TWO routes to "
             "it without choosing. Neither rule is codified"),
    BhavaKrt("3.3.83", gives="ka", also="अप्", of=("han",),
         upasarga=("stamba",), karaka="karaṇa", adesha="ghana",
         why="स्तम्बे क च — स्तम्बघ्नः by the क, स्तम्बघनः by the च "
             "which brings अप् down, तत्र घनादेशः. And the feminine "
             "of both is wanted: स्त्रियां स्तम्बघ्ना स्तम्बघनेति "
             "इष्यते. करण इत्येव — स्तम्बघातः"),
    BhavaKrt("3.3.84", gives="ap", of=("han",), upasarga=("pari",),
         karaka="karaṇa", adesha="gha",
         why="परौ घः — परिहन्यतेऽनेनेति परिघः, a door-bar; and "
             "पलिघः. The substitute here is घ where 3.3.82 and "
             "3.3.83 had घन — one syllable shorter, and nothing in "
             "the rules says why beyond that each states its own"),
    BhavaKrt("3.3.86", gives="ap", of=("han",),
         upasarga=("sam", "ud"), sense=("praśaṃsā",),
         names_a="gaṇa", adesha="gha",
         why="संघोद्घौ गणप्रशंसयोः — संघः पशूनाम्, उद्घो "
             "मनुष्याणाम्. टिलोपो घत्वं च निपात्यते, and यथासंख्यं "
             "गणेऽभिधेये प्रशंसायां गम्यमानायाम् — सम् with the "
             "GROUP and उद् with the PRAISE, bound crosswise. "
             "गणप्रशंसयोरिति किम्? संघातः"),
    BhavaKrt("3.3.88", gives="ktri", marked="ḍvit",
         why="ड्वितः क्त्रिः — डु इद् यस्य, तस्माद् ड्वितो धातोः. "
             "डुपचष् पाके gives पक्त्रिमम्, डुवप बीजसंताने "
             "उप्त्रिमम्, डुकृञ् करणे कृत्रिमम्.\n\n"
             "AND THE AFFIX IS NEVER USED ALONE. क्त्रेर्मम् नित्यम् "
             "(4.4.20) इति वचनात् केवलो न प्रयुज्यते — another rule "
             "always adds मम् after it, so no word ever ends in क्त्रि "
             "and every form the vṛtti gives is क्त्रिम. A rule whose "
             "output cannot be observed on its own.\n\n"
             "The first rule of the run to reach by a root's उपदेश "
             "MARK rather than by its name, its shape or its sense. "
             "DEBT — 4.4.20 is not codified"),
    BhavaKrt("3.3.89", gives="athuc", marked="ṭvit",
         why="ट्वितोऽथुच् — टु इद् यस्य, तस्माट् ट्वितो धातोः. "
             "टुवेपृ कम्पने gives वेपथुः, टुओश्वि गतिवृद्ध्योः "
             "श्वयथुः, टुक्षु शब्दे क्षवथुः. भावादौ, so the "
             "conditions running from 3.3.18 and 3.3.19 both hold. "
             "The pair to 3.3.88: two adjacent rules dividing roots "
             "by which of two marks they carry"),
    BhavaKrt("3.3.90", gives="naṅ", of=YAJADI,
         why="यजयाचयतविच्छप्रच्छरक्षो नङ् — यज्ञः, याच्ञा, यत्नः, "
             "विश्नः, प्रश्नः, रक्ष्णः. ङकारो गुणप्रतिषेधार्थः, the "
             "ङ being there to keep the strengthening off.\n\n"
             "AND A ज्ञापक DRAWN FROM A RULE ALREADY CODIFIED. "
             "प्रच्छेरसंप्रसारणं ज्ञापकात् प्रश्ने चासन्नकाले इति — "
             "प्रच्छ् does NOT vocalise here, and the evidence is "
             "3.2.117, which writes प्रश्ने and could not have if the "
             "root vocalised. A rule of the pāda before, codified, "
             "used as evidence about a rule of this one. Recorded as "
             "a citation rather than a call: 3.2.117 answers which "
             "लकार comes, not what प्रच्छ् does"),
    BhavaKrt("3.3.91", gives="nan", of=("svap",),
         why="स्वपो नन् — स्वप्नः. नकारः स्वरार्थः, the न for the "
             "accent alone. The third mark in this pāda put in a "
             "rule for the accent, after 3.3.57's प and 3.3.58's "
             "निश्चि"),
    BhavaKrt("3.3.92", gives="ki", ghu=True, any_upasarga=True,
         why="उपसर्गे घोः किः — प्रदिः, प्रधिः, अन्तर्धिः. "
             "कित्करणमातो लोपार्थम्, the क there so the आ drops.\n\n"
             "THE RULE NAMES ITS ROOTS BY A संज्ञा AND THE RESOLVER "
             "ASKS FOR IT. घु is conferred by 1.1.20 दाधा घ्वदाप्, "
             "which is codified as `is_ghu`, so this row does not "
             "list दा and धा: it asks. The same treatment 3.3.14 "
             "gave 3.2.127's सत्"),
    BhavaKrt("3.3.93", gives="ki", ghu=True, karaka="adhikaraṇa",
         why="कर्मण्यधिकरणे च — जलं धीयतेऽस्मिन्निति जलधिः, the sea; "
             "शरधिः, a quiver. घोरित्येव, so the name is asked of "
             "1.1.20 here too.\n\n"
             "अधिकरणग्रहणमर्थान्तरनिरासार्थम् — naming the LOCUS "
             "shuts out the other senses that were running, and "
             "चकारः प्रत्ययानुकर्षणार्थः, the च drags the affix down "
             "from the rule before. Two words in one short sūtra, "
             "each undoing or carrying something from outside it"),
    BhavaKrt("3.3.94", gives="ktin", stri=True,
         why="स्त्रियां क्तिन् — कृतिः, चितिः, मतिः. "
             "घञजपामपवादः, so it defeats three affixes of this run at "
             "once.\n\n"
             "SCOPE — SIX VĀRTTIKAS, more than any rule of the pāda. "
             "क्तिन्नाबादिभ्यश्च वक्तव्यः, and आबादयः प्रयोगतोऽनुसर्तव्याः "
             "— the list is to be FOLLOWED FROM USAGE, so it is open: "
             "आप्तिः, राद्धिः, दीप्तिः, स्रस्तिः, ध्वस्तिः, लब्धिः. "
             "श्रुयजिस्तुभ्यः करणे — श्रुतिः, इष्टिः, स्तुतिः. "
             "ग्लाम्लाज्याहाभ्यो निः — ग्लानिः, म्लानिः, ज्यानिः, "
             "हानिः. ॠकारल्वादिभ्यः क्तिन्निष्ठावद् भवति — कीर्णिः, "
             "गीर्णिः, जीर्णिः, शीर्णिः, लूनिः, धूनिः. संपदादिभ्यः "
             "क्विप् — संपत्, विपत्, प्रतिपत्; and क्तिन्नपीष्यते "
             "besides, संपत्तिः, विपत्तिः, so the last two stand "
             "together"),
    BhavaKrt("3.3.95", gives="ktin", stri=True, of=STHADI, bhava=True,
         why="स्थागापापचो भावे — प्रस्थितिः, उद्गीतिः, संगीतिः, "
             "प्रपीतिः, संपीतिः, पक्तिः. अङोऽपवादस्य बाधकः — it "
             "defeats a rule that was itself an अपवाद, so the "
             "displacing runs two deep.\n\n"
             "भावग्रहणमर्थान्तरनिरासार्थम्, naming the act to shut out "
             "the other senses running.\n\n"
             "SCAR — AND TWO FORMS THE RULE SHOULD HAVE DESTROYED "
             "SURVIVE. कथमवस्था संस्थेति? व्यवस्थायामसंज्ञायाम् "
             "(1.1.34) इति ज्ञापकाद् नात्यन्ताय बाधा भवति — an "
             "अपवाद does not displace ABSOLUTELY, and the evidence is "
             "a rule three adhyāyas back that presupposes the very "
             "words. 1.1.34 is codified. A ज्ञापक used to blunt the "
             "displacement this rule performs"),
    BhavaKrt("3.3.96", gives="ktin", stri=True, of=VRSADI,
         mantra=True, bhava=True,
         why="मन्त्रे वृषेषपचमनविदभूवीरा उदात्तः, and the affix is "
             "उदात्त: वृष्टिः (ऋ० १.३.८.८), इष्टिः (ऋ० ४.४.७), "
             "पक्तिः (ऋ० १.२४.५), मतिः (ऋ० १.१४१.१), वित्तिः and "
             "भूतिः (मा०सं० १८.१४), वीतिः (शौ०सं० २०.६९.३), रातिः "
             "(ऋ० १.३४.१). Eight forms, each with its passage.\n\n"
             "AND THE RULE IS FOR THE ACCENT AND NOTHING ELSE. "
             "सर्वत्र सर्वधातुभ्यः सामान्येन विहित एव क्तिन्, "
             "उदात्तार्थं वचनम् — 3.3.94 gives the affix to every root "
             "already; this rule exists to make it उदात्त in a mantra, "
             "and मन्त्रादन्यत्रादिरुदात्तः elsewhere. The fourth "
             "accent-only statement of the pāda, and the first that is "
             "a whole SŪTRA rather than a letter.\n\n"
             "प्रकृतिप्रत्यययोर्विभक्तिविपरिणामेन संबन्धः — the cases "
             "in the rule have to be changed round to construe it, and "
             "कस्मादेवं कृतम्? वैचित्र्यार्थम्, for variety. A "
             "grammarian's answer that the wording is simply not "
             "uniform"),
    BhavaKrt("3.3.98", gives="kyap", stri=True, of=("vraj", "yaj"),
         bhava=True,
         why="व्रजयजोर्भावे क्यप् — व्रज्या, इज्या. क्तिनोऽपवादः, "
             "and उदात्त runs down from 3.3.96. पित्करणमुत्तरत्र "
             "तुगर्थम् — the प is for a तुक् in a LATER rule, so a "
             "mark is spent forward as 3.3.43's च and 3.3.56's were"),
    BhavaKrt("3.3.99", gives="kyap", stri=True, of=SAMAJADI,
         samjna=True,
         why="संज्ञायां समजनिषदनिपतमनविदषुञ्शीङ्भृञिणः — "
             "समजन्त्यस्यामिति समज्या, निषद्या, निपत्या, मन्या, "
             "विद्या, सुत्या, शय्या, भृत्या, इत्या.\n\n"
             "AND THE VṚTTI DENIES THAT भाव IS A HEADING HERE. भाव "
             "इति न स्वर्यते, पूर्व एवात्रार्थाधिकारः. Asked about the "
             "line स्त्रियां भावाधिकारोऽस्ति तेन भार्या प्रसिध्यति, it "
             "answers भावाधिकारो भावव्यापारो वाच्यत्वेन विवक्षितः, न "
             "तु शास्त्रीयोऽधिकारः — 'the heading of भाव' there means "
             "the SENSE being expressed, not a heading of the grammar. "
             "One phrase read two ways, and the commentary saying "
             "which is technical and which is not"),
    BhavaKrt("3.3.100", gives="śa", also="क्यप्", stri=True,
         of=("kṛñ",),
         why="कृञः श च — क्रिया by the श, कृत्या by the च.\n\n"
             "AND A योगविभाग IS CALLED FOR TO GET A THIRD FORM. "
             "योगविभागोऽत्र कर्तव्यः, क्तिन्नपि यथा स्यात् — split the "
             "rule in two and क्तिन् comes as well, giving कृतिः. "
             "3.2.4 needed a योगविभाग for a SENSE; this one needs it "
             "for a third affix the rule as written would have shut "
             "out"),
    BhavaKrt("3.3.102", gives="a", stri=True, pratyayanta=True,
         why="अ प्रत्ययात् — चिकीर्षा, जिहीर्षा, पुत्रीया, "
             "पुत्रकाम्या, लोलूया, कण्डूया. क्तिनोऽपवादः. The stem is "
             "already MADE with an affix, so the rule reaches "
             "चिकीर्ष and not कृ. 3.2.166 and 3.2.168 wanted "
             "particular such stems — यङन्त, सन्नन्त — and this wants "
             "any at all"),
    BhavaKrt("3.3.103", gives="a", stri=True, gurumat=True,
         hal_final=True,
         why="गुरोश्च हलः — कुण्डा, हुण्डा, ईहा, ऊहा. क्तिनोऽपवादः. "
             "TWO conditions and each tested: गुरोरिति किम्? भक्तिः; "
             "हल इति किम्? नीतिः. A root with a heavy vowel AND "
             "ending in a consonant — one about weight, one about "
             "shape, and neither follows from the other"),
    BhavaKrt("3.3.104", gives="aṅ", stri=True, of=BHIDADI,
         why="षिद्भिदादिभ्योऽङ् — भिदा, छिदा, विदा, क्षिपा, श्रद्धा, "
             "मेधा, गोधा, आरा, हारा, कारा, क्षिया, तारा, धारा, लेखा, "
             "रेखा, चूडा, पीडा, वपा, वसा, मृजा; and from the षित् "
             "half जरा (जृष्) and त्रपा (त्रपूष्). "
             "गणपरिपठितेषु भिदादिषु निष्कृष्य प्रकृतयो गृह्यन्ते.\n\n"
             "THE MEMBERS ARE READ FROM THE गणपाठ ON DISK, not typed "
             "out of the vṛtti — the remedy for a mistake made at "
             "3.2.5, recorded, and then made again at 3.3.3, where a "
             "hand-copied list came to ten members against the "
             "corpus's nine.\n\n"
             "SCOPE — five गणसूत्र fix a sense for one member each, "
             "and four of them by CONTRAST with another word: गुहा "
             "गिर्योषध्योः; भिदा विदारणे, भित्तिरन्या; छिदा "
             "द्वैधीकरणे, छित्तिरन्या; आरा शस्त्र्याम्, आर्तिरन्या; "
             "धारा प्रपाते, धृतिरन्या. And क्रपेः संप्रसारणं च gives "
             "कृपा. So the gaṇa is not a flat list: several of its "
             "members are held to one sense, with the क्तिन् form "
             "taking the rest"),
    BhavaKrt("3.3.105", gives="aṅ", also="युच्", stri=True,
         of=CINTADI,
         why="चिन्तिपूजिकथिकुम्बिचर्चश्च — चिन्ता, पूजा, कथा, "
             "कुम्बा, चर्चा; and चकाराद् युजपि भवति, चिन्तना. All "
             "five are चुरादि, so युच् would have come by 3.3.107 and "
             "this gives अङ् instead — युचि प्राप्ते"),
    BhavaKrt("3.3.106", gives="aṅ", stri=True, root_final=("ā",),
         any_upasarga=True,
         why="आतश्चोपसर्गे — प्रदा, उपदा, प्रधा, उपधा. "
             "क्तिनोऽपवादः. The fourth rule of the run to want A "
             "PREVERB without saying which.\n\n"
             "SETTLED — AND TWO WORDS THAT ARE NOT PREVERBS COUNT AS "
             "ONE. श्रदन्तरोरुपसर्गवद् वृत्तिः: श्रद् and अन्तर् "
             "BEHAVE LIKE preverbs here, giving श्रद्धा and अन्तर्धा. "
             "1.4.59 उपसर्गाः क्रियायोगे is codified and would refuse "
             "both, so this is an extension the vṛtti makes and the "
             "rule does not — recorded rather than folded into the "
             "condition"),
    BhavaKrt("3.3.107", gives="yuc", stri=True,
         of=("ṇyanta", "ās", "śranth"),
         why="ण्यासश्रन्थो युच् — कारणा, हारणा, आसना, श्रन्थना. "
             "अकारस्यापवादः.\n\n"
             "कथमास्या? ऋहलोर्ण्यत् (3.1.124) भविष्यति — the awkward "
             "form is sent to a rule that IS codified. And a "
             "principle with it: वासरूपप्रतिषेधश्च "
             "स्त्रीप्रकरणविषयस्यैवोत्सर्गापवादस्य — the suspension "
             "of 3.1.94 holds only for the general-and-special pairs "
             "WITHIN the feminine section. A fifth suspension, and the "
             "first that is explicitly BOUNDED.\n\n"
             "SETTLED — TWO ROOTS SPELT ALIKE, AND THE CHOICE IS MADE "
             "TWICE ON ONE GROUND. श्रन्थिः क्र्यादिर्गृह्यते, न "
             "चुरादिः, ण्यन्तत्वेनैव सिद्धत्वात् — the चुरादि one is "
             "not meant BECAUSE it would already be covered by "
             "ण्यन्त. And the vārttika घट्टिवन्दिविदिभ्य "
             "उपसंख्यानम् (घट्टना, वन्दना, वेदना) makes the same "
             "choice for घट्ट by the same reason. Elsewhere in this "
             "project such an ambiguity was settled from the sense; "
             "here it is settled from REDUNDANCY — the reading that "
             "would make the rule say nothing new is the wrong one.\n\n"
             "SCOPE — इषेरनिच्छार्थस्य युज्वक्तव्यः, अध्येषणा, "
             "अन्वेषणा; परेर्वा, पर्येषणा, परीष्टिः"),
    BhavaKrt("3.3.108", gives="ṇvul", names_a="roga",
         why="रोगाख्यायां ण्वुल् बहुलम् — प्रच्छर्दिका, प्रवाहिका, "
             "विचर्चिका. क्तिन्नादीनामपवादः. आख्याग्रहणं रोगस्य चेत् "
             "प्रत्ययान्तेन संज्ञा भवति, and बहुलग्रहणं व्यभिचारार्थम् "
             "— the बहुलम् is there so the rule may FAIL: न च भवति "
             "शिरोऽर्तिः, a disease named without it.\n\n"
             "SCOPE — seven vārttikas, and most of them are about "
             "NAMING GRAMMATICAL THINGS rather than making words. "
             "इक्श्तिपौ धातुनिर्देशे — भिदिः, छिदिः, पचतिः, पठतिः, "
             "how to refer to a root. वर्णात् कारः — अकारः, इकारः, "
             "how to refer to a letter. रादिफः — रेफः, the name of र. "
             "So the grammar's own vocabulary for talking about itself "
             "is supplied by vārttikas on a rule about DISEASES"),
    BhavaKrt("3.3.109", gives="ṇvul", samjna=True,
         why="संज्ञायाम् — उद्दालकपुष्पभञ्जिका, "
             "वारणपुष्पप्रचायिका, अभ्यूषखादिका, आचोषखादिका, "
             "शालभञ्जिका, तालभञ्जिका. Names of games and festivals, "
             "each a whole compound"),
    BhavaKrt("3.3.110", gives="iñ", also="ण्वुल्", optional=True,
         sense=("paripraśna", "ākhyāna"),
         why="विभाषाख्यानपरिप्रश्नयोरिञ् च — कां त्वं कारिमकार्षीः, "
             "कां कारिकामकार्षीः, कां क्रियामकार्षीः? and the answer "
             "सर्वां कारिमकार्षम्. चकाराद् ण्वुलपि, and "
             "विभाषाग्रहणात् परोऽपि यः प्राप्नोति सोऽपि भवति — the "
             "option lets even a LATER affix stand, so five forms are "
             "given for one question.\n\n"
             "पूर्वं परिप्रश्नः, पश्चादाख्यानम् — the ASKING comes "
             "first and the telling after, though the rule names them "
             "the other way round; सूत्रेऽल्पाच्तरस्य पूर्वनिपातः, "
             "the shorter word stands first by 2.2.34. The word order "
             "read as an artefact of a rule about compounds — where "
             "3.2.29 read the same fact as EVIDENCE. "
             "आख्यानपरिप्रश्नयोरिति किम्? कृतिः, हृतिः"),
    BhavaKrt("3.3.111", gives="ṇvuc", optional=True,
         sense=("paryāya", "arha", "ṛṇa", "utpatti"),
         why="पर्यायार्हर्णोत्पत्तिषु ण्वुच् — भवतः शायिका "
             "for the turn; अर्हति भवानिक्षुभक्षिकाम् for what one "
             "deserves; इक्षुभक्षिकां मे धारयसि for a debt; "
             "इक्षुभक्षिका मे उदपादि for what has arisen. Four senses "
             "in one rule, each glossed — पर्यायः परिपाटी क्रमः, "
             "अर्हणमर्हः तद्योग्यता, ऋणं तत् यत् परस्य धार्यते, "
             "उत्पत्तिर्जन्म.\n\n"
             "ण्वुलि प्रकृते प्रत्ययान्तरकरणं स्वरार्थम् — ण्वुल् was "
             "already running and a DIFFERENT affix is given for the "
             "accent alone. The fifth accent-only statement of the "
             "pāda, and the same device 3.2.12 and 3.2.16 used to "
             "reach a feminine"),
    BhavaKrt("3.3.112", gives="ani", upasarga=("nañ",),
         sense=("ākrośa",),
         why="आक्रोशे नञ्यनिः — अकरणिस्ते वृषल भूयात्. आक्रोशः "
             "शपनम्, and विभाषेति निवृत्तम्, the option having run "
             "out. BOTH conditions tested: आक्रोश इति किम्? "
             "अकृतिस्तस्य कटस्य. नञीति किम्? मृतिस्ते वृषल भूयात् — "
             "a curse without the negative particle, which does not "
             "reach.\n\n"
             "आक्रोश was 3.3.45's condition too, and there the affix "
             "was अप् after ग्रह्. The same sense reached for twice in "
             "one pāda for two different affixes"),
    BhavaKrt("3.3.114", gives="kta", wants=("kta",),
         napumsaka=True, bhava=True,
         why="नपुंसके भावे क्तः — हसितम्, सहितम्, जल्पितम्. The "
             "feminine run is over and the NEUTER begins: 3.3.94 to "
             "3.3.112 wanted स्त्रियाम्, 3.3.118 will want the "
             "masculine, and the three genders divide this end of the "
             "pāda between them"),
    BhavaKrt("3.3.115", gives="lyuṭ", wants=("lyuṭ",),
         napumsaka=True, bhava=True,
         why="ल्युट् च — हसनं छात्रस्य, शोभनम्, जल्पनम्, शयनम्, "
             "आसनम्. The affix could have been given with 3.3.114's, "
             "and योगविभाग उत्तरार्थः — the rule is split off FOR THE "
             "SAKE OF WHAT COMES AFTER, so that 3.3.116 and 3.3.117 "
             "have something to carry down. A योगविभाग made not for "
             "this rule but for the next"),
    BhavaKrt("3.3.116", gives="lyuṭ", napumsaka=True, bhava=True,
         sense=("sukha",), karaka="karman",
         why="कर्मण्यधिकरणे च — पयःपानं सुखम्, ओदनभोजनं सुखम्.\n\n"
             "AND THE RULE GIVES NOTHING NEW BUT A COMPOUND. "
             "पूर्वेणैव सिद्धे प्रत्यये नित्यसमासार्थं वचनम्, "
             "उपपदसमासो हि नित्यः समासः — 3.3.115 gives the affix "
             "already; this exists so the two words must COMPOUND, an "
             "उपपद compound being obligatory. A whole sūtra for a "
             "compound, as 3.3.96 was for an accent.\n\n"
             "FOUR CONDITIONS AND FOUR COUNTER-EXAMPLES, and the "
             "vṛtti works each one: कर्मणीति किम्? तूलिकाया "
             "उत्त्थानं सुखम्. संस्पर्शादिति किम्? "
             "अग्निकुण्डस्योपासनं सुखम्. कर्तुरिति किम्? गुरोः "
             "स्नापनं सुखम् — स्नापयतेर्न गुरुः कर्ता, किं तर्हि? "
             "कर्म, the teacher being what is bathed and not the "
             "bather. शरीरग्रहणं किम्? पुत्रस्य परिष्वञ्जनं सुखम् — "
             "सुखं मानसी प्रीतिः, that pleasure is of the mind. "
             "सुखमिति किम्? कण्टकानां मर्दनं दुःखम्.\n\n"
             "And सर्वत्रासमासः प्रत्युदाह्रियते — every "
             "counter-example is given UNCOMPOUNDED, since the affix "
             "still comes and only the compulsory compounding is "
             "lost. A counter-example that differs from its example "
             "in nothing but a space"),
    BhavaKrt("3.3.117", gives="lyuṭ", karaka="karaṇa",
         why="करणाधिकरणयोश्च — इध्मप्रव्रश्चनः, पलाशशातनः for the "
             "means; गोदोहनी, सक्तुधानी for the place. The two "
             "kārakas 3.3.19's heading had left general, now named"),
    BhavaKrt("3.3.118", gives="gha", pum=True, samjna=True,
         karaka="karaṇa",
         why="पुंसि संज्ञायां घः प्रायेण — दन्तच्छदः, उरश्छदः पटः; "
             "and for the place एत्य तस्मिन् कुर्वन्ति इत्याकरः, "
             "आलयः. समुदायेन चेत् संज्ञा गम्यते, the NAME being "
             "carried by the whole — the sixth समुदायोपाधि.\n\n"
             "प्रायग्रहणमकार्त्स्न्यार्थम् — the word प्रायेण is "
             "there to say the rule does NOT hold throughout, which "
             "is a रule admitting its own leaks in its own wording. "
             "पुंसीति किम्? प्रसाधनम्. संज्ञायामिति किम्? प्रहरणो "
             "दण्डः. And घकारः छादेर्घे इति विशेषणार्थः, the घ spent "
             "so 6.4.96 can pick this affix out"),
    BhavaKrt("3.3.120", gives="ghañ", of=("tṝ", "stṝ"),
         upasarga=("ava",), pum=True, karaka="karaṇa",
         why="अवे तॄस्त्रोर्घञ् — अवतारः, अवस्तारः. घस्यापवादः.\n\n"
             "ञकारो वृद्ध्यर्थः स्वरार्थश्च, घकार उत्तरत्र "
             "कुत्वार्थः — one mark doing two jobs at once and "
             "another spent forward on a later rule.\n\n"
             "AND THE RULE LEAKS, BY A HEDGE TWO SŪTRAS BACK. "
             "संज्ञायाम् runs down from 3.3.118 and would require a "
             "name; कथमवतारो नद्याः, न हीयं संज्ञा? — how does "
             "अवतारो नद्याः stand, a river's descent being no name? "
             "प्रायानुवृत्तेरसंज्ञायामपि भवति: 3.3.118's प्रायेण "
             "runs down too, so the rule holds where no name is "
             "meant. The row therefore does NOT require one — a hedge "
             "written into one sūtra doing work in another, and the "
             "codification has to follow the outcome rather than the "
             "condition"),
    BhavaKrt("3.3.121", gives="ghañ", pum=True, samjna=True,
         karaka="karaṇa", hal_final=True,
         why="हलश्च — लेखः, वेदः, वेष्टः, बन्धः, मार्गः, अपामार्गः, "
             "वीमार्गः. घस्यापवादः, and पुंसि संज्ञायां "
             "करणाधिकरणयोश्चेति सर्वमनुवर्तते — everything from "
             "3.3.118 runs down, so the rule states only the root's "
             "shape"),
    BhavaKrt("3.3.125", gives="gha", also="घञ्", of=("khan",),
         karaka="karaṇa",
         why="खनो घ च — आखनः by the घ, आखानः by the च bringing घञ्.\n\n"
             "SCOPE — FIVE VĀRTTIKAS, EACH GIVING ONE MORE AFFIX FOR "
             "ONE ROOT: डो वक्तव्यः, आखः; डरो वक्तव्यः, आखरः; इको "
             "वक्तव्यः, आखनिकः; इकवको वक्तव्यः, आखनिकवकः. So seven "
             "words from one root, and five of them are supplements. "
             "No rule of the pāda has been supplemented this densely "
             "for so little"),
    BhavaKrt("3.3.126", gives="khal", isadadi=True,
         why="ईषद्दुःसुषु कृच्छ्राकृच्छ्रार्थेषु खल् — ईषत्करो भवता "
             "कटः, दुष्करः, सुकरः; ईषद्भोजः, दुर्भोजः, सुभोजः.\n\n"
             "AND THE THREE COMPANIONS DIVIDE THE TWO SENSES BETWEEN "
             "THEM WITHOUT यथासंख्यम्. कृच्छ्रं दुःखम्, तद् दुरो "
             "विशेषणम्; अकृच्छ्रं सुखम्, तदितरयोर्विशेषणम्, "
             "संभवात् — HARD qualifies दुर्, EASY the other two, and "
             "the ground is संभवात्, what each can sensibly mean. A "
             "pairing settled by fit rather than by counting off, "
             "where 3.3.37 and 3.3.86 counted.\n\n"
             "ईषदादिष्विति किम्? कृच्छ्रेण कार्यः कटः. "
             "कृच्छ्राकृच्छ्रार्थेष्विति किम्? ईषत्कार्यः. And two "
             "marks: लकारः स्वरार्थः, खित्करणमुत्तरत्र मुमर्थम् — one "
             "for the accent and one for an augment in a LATER rule"),
    BhavaKrt("3.3.127", gives="khal", isadadi=True,
         of=("bhū", "kṛñ"), karaka="kartṛ",
         why="कर्तृकर्मणोश्च भूकृञोः — यथासंख्यम् binds भू to the "
             "AGENT and कृ to the OBJECT: ईषदाढ्यंभवं भवता, "
             "दुराढ्यंभवम्; ईषदाढ्यंकरः, स्वाढ्यंकरो देवदत्तो भवता. "
             "चकारादीषदादिषु च, so the three companions run down.\n\n"
             "SCOPE — कर्तृकर्मणोश्च्व्यर्थयोरिति वक्तव्यम्: the "
             "agent and object must be in the सense of च्वि, इह मा "
             "भूत् स्वाढ्येन भूयते"),
    BhavaKrt("3.3.128", gives="yuc", isadadi=True, root_final=("ā",),
         why="आतो युच् — ईषत्पानः सोमो भवता, दुष्पानः, सुपानः; "
             "ईषद्दानो गौर्भवता, दुर्दानः, सुदानः. खलोऽपवादः. "
             "ईषदादयोऽनुवर्तन्ते, कर्तृकर्मणोरिति न स्वर्यते — the "
             "three companions carry down and 3.3.127's two kārakas "
             "do NOT, which the vṛtti has to say because nothing in "
             "the wording shows it"),
    BhavaKrt("3.3.129", gives="yuc", isadadi=True, gati_artha=True,
         chandasi=True,
         why="छन्दसि गत्यर्थेभ्यः — सूपसदनोऽग्निः (तै०सं० "
             "७.५.२०.१), सूपसदनमन्तरिक्षम्. खलोऽपवादः"),
    BhavaKrt("3.3.130", gives="yuc", gati_artha=True, chandasi=True,
         why="अन्येभ्योऽपि दृश्यते — सुदोहनाम् (निरु० ११.४३) अकृणोद् "
             "ब्रह्मणे गाम्, सुवेदनामकृणोर्ब्रह्मणे गाम् (ऋ० "
             "१०.११२.८).\n\n"
             "दृश्यते A FOURTH TIME, and it takes the usage-following "
             "reading again: the rule opens the class rather than "
             "closing it, as at 3.2.75 and 3.3.2, and not 3.2.178's "
             "gathering-in of other operations.\n\n"
             "SCOPE — भाषायां शासियुधिदृशिधृषिमृषिभ्यो युज् "
             "वक्तव्यः: दुःशासनः, दुर्योधनः, दुर्दर्शनः, दुर्धर्षणः, "
             "दुर्मर्षणः — five roots given the affix OUTSIDE the "
             "Veda by a vārttika, against a rule that holds only "
             "inside it. The supplement undoes the rule's own "
             "restriction"),
)


def bhava_affix(root: str = "", *, upasarga: str = "", sense: str = "",
               about: str = "", names_a: str = "",
               bhava: bool = False, akartari_karake: bool = False,
               samjna: bool = False, parimana: bool = False,
               stri: bool = False, steya: bool = False,
               root_final: str = "", karaka: str = "",
               marked: str = "", mantra: bool = False,
               pratyayanta: bool = False, gurumat: bool = False,
               hal_final: bool = False, napumsaka: bool = False,
               pum: bool = False, isadadi: bool = False,
               chandasi: bool = False,
               gati_artha: bool = False,
               wants: str = "") -> object:
    """
    3.3.16 onward — which affix comes where the ACT itself is
    named, or a कारक other than the agent.

    Not "where घञ् comes", though घञ् is what the first rules give:
    3.3.56 gives अच् and 3.3.57 अप्, both as अपवाद on this same
    ground. What holds the run together is the pair of conditions
    running from 3.3.18 and 3.3.19, and 3.3.56 states how far they
    reach — भावे, अकर्तरि च कारक इति प्रकृतमनुवर्तते यावत्
    कृत्यल्युटो बहुलम् इति, as far as 3.3.113.

    3.3.18 भावे reaches every root and every rule after it narrows, so
    the MOST SPECIFIC row answers, as 3.2's runs did.

    Two conditions run down from 3.3.18 and 3.3.19 — भावे and
    अकर्तरि च कारके — and the vṛtti says so outright rather than
    leaving it to be inferred: इत उत्तरं भावे अकर्तरि च कारक इति च
    द्वयमनुवर्तते. The codification cannot represent a running
    condition, so each row states its own, and the rules that state a
    preverb and a root state neither.
    """
    asked = dict(
        root=root, upasarga=upasarga, sense=sense, about=about,
        names_a=names_a, any_upasarga=upasarga, no_upasarga=upasarga,
        bhava=bhava, akartari_karake=akartari_karake, samjna=samjna,
        parimana=parimana, stri=stri, steya=steya,
        root_final=root_final, karaka=karaka, marked=marked,
        ghu=is_ghu(root) if root else False,
        mantra=mantra, pratyayanta=pratyayanta,
        gurumat=gurumat, hal_final=hal_final,
        napumsaka=napumsaka, pum=pum, isadadi=isadadi,
        chandasi=chandasi, gati_artha=gati_artha,
    )
    matched = [row for row in BHAVA_KRT if _bhava_reaches(row, asked)]
    if wants:
        # Where two rules reach one ground and give different
        # affixes, the caller names the one asked after. A row that
        # claims no affix by name is not thereby excluded — it is
        # only outranked by one that does.
        named = [row for row in matched if wants in row.wants]
        if named:
            matched = named
        else:
            matched = [row for row in matched
                       if row.gives == wants or not row.wants]
    if not matched:
        return NotAdded(
            "",
            "No rule of this run reaches it. 3.3.18 भावे "
            "reaches every root where the ACT itself is named, and "
            "3.3.19 where the affix names a कārakа other than the "
            "agent and a name is meant; the rest want a particular "
            "root, mostly with a particular preverb")
    best = max(matched, key=_bhava_specific)
    return Added(best.gives, best.sutra, best.why, also=best.also)


#: The conditions, with what naming one is worth and how it is read.
#: `_bhava_reaches` and `_bhava_specific` both used to enumerate every
#: field by hand — two lists that had to be kept in step, and the run
#: is about to double. One declaration now feeds both, so a field
#: cannot be added to the filter and forgotten in the ranking.
#:
#:   "any"   the row lists alternatives; the asked value must be among
#:           them. An empty list states nothing.
#:   "none"  the row lists what it refuses.
#:   "is"    a plain flag: if the row sets it, the asker must too.
#:   "tri"   stated or not stated, and if stated must MATCH — silence
#:           and denial being different things.
#:   "tri-not"  the same, but the asked value must be the OPPOSITE.
#:           3.3.24's अनुपसर्गे states a preverb condition by REFUSING
#:           one: no_upasarga=True is satisfied exactly when no preverb
#:           was given. Read as a plain tri-state it inverts, and every
#:           अनुपसर्ग rule answers backwards.
#:   "same"  a string the asked value must equal, if the row gives one.
#:
#: A GENDER weighs more than a named root, which is not a tuning:
#: the feminine, neuter and masculine runs at this end of the pāda
#: DISPLACE the affixes given earlier — 3.3.94 is घञजपामपवादः in
#: so many words — so a rule naming one must beat a rule naming a
#: root. Without it हसितम् came back as हसः, by a rule of the
#: earlier run that happens to name हस्.
_CONDITIONS: Tuple[Tuple[str, str, int], ...] = (
    ("of", "any", 3),
    ("upasarga", "any", 2),
    ("sense", "any", 2),
    ("not_sense", "none", 2),
    ("not_about", "none", 2),
    ("names_a", "same", 2),
    ("any_upasarga", "is", 1),
    ("no_upasarga", "tri-not", 1),
    ("bhava", "is", 1),
    ("akartari_karake", "is", 1),
    ("samjna", "tri", 2),
    ("parimana", "is", 2),
    ("stri", "is", 5),
    ("root_final", "any", 2),
    ("karaka", "same", 2),
    ("ghu", "is", 2),
    ("marked", "same", 3),
    ("mantra", "is", 2),
    ("pratyayanta", "is", 2),
    ("gurumat", "is", 2),
    ("hal_final", "is", 2),
    ("napumsaka", "is", 5),
    ("pum", "is", 5),
    ("isadadi", "is", 2),
    ("chandasi", "is", 2),
    ("gati_artha", "is", 2),
    ("steya", "tri", 2),
)

#: What is asked about, per condition, where the parameter is not named
#: the same as the field. `of` is matched against the root and
#: `not_about` against what the word is about.
_ASKED_AS = {"of": "root", "not_about": "about", "not_sense": "sense"}


def _bhava_reaches(row: BhavaKrt, asked: Dict[str, object]) -> bool:
    """Whether one row covers this."""
    if row.bound:
        # यथासंख्यम्: the members are bound crosswise and the lists must
        # not be crossed, so preverb, root and sense are checked as one
        # triple rather than three conditions.
        if not any(u == asked["upasarga"] and r == asked["root"]
                   and (not sn or sn == asked["sense"])
                   for u, r, sn in row.bound):
            return False
    else:
        for field in ("of", "upasarga", "any_upasarga", "no_upasarga"):
            if not _one(row, field, asked):
                return False
    for field, kind, _ in _CONDITIONS:
        if field in ("of", "upasarga", "any_upasarga", "no_upasarga"):
            continue
        if not _one(row, field, asked):
            return False
    return True


def _one(row: BhavaKrt, field: str, asked: Dict[str, object]) -> bool:
    """Whether one condition of one row is satisfied."""
    kind = next(k for f, k, _ in _CONDITIONS if f == field)
    stated = getattr(row, field)
    value = asked[_ASKED_AS.get(field, field)]
    if kind == "any":
        return not stated or value in stated
    if kind == "none":
        return not stated or value not in stated
    if kind == "same":
        return not stated or value == stated
    if kind == "is":
        return not stated or bool(value)
    if kind == "tri-not":
        return stated is None or bool(stated) != bool(value)
    # "tri"
    return stated is None or bool(stated) == bool(value)


def _bhava_specific(row: BhavaKrt) -> int:
    """
    How much a row states. Naming a root weighs most, as in 3.2, and a
    यथासंख्यम् triple most of all — 3.3.37 names a preverb, a root and
    a sense at once and must beat any of the three separately.
    """
    score = 4 * (len(row.bound) > 0)
    for field, kind, weight in _CONDITIONS:
        stated = getattr(row, field)
        if kind in ("tri", "tri-not"):
            score += weight * (stated is not None)
        elif stated:
            score += weight
    return score

#: 3.3.68, 3.3.70, 3.3.74 and 3.3.79 to 3.3.81 — words the grammar
#: fixes outright. Six in this run, against four in the whole of 3.2.
#:
#: Each entry carries its OWN affix and what the vṛtti says is being
#: fixed in it. 3.2's निपातन table began with the affix hardcoded for
#: every entry and that was wrong within five rules; the lesson is
#: kept here from the start.
NIPATANA = {
    "pramada": (
        "3.3.68", "ap",
        "प्रमदसंमदौ हर्षे — कन्यानां प्रमदः, कोकिलानां संमदः. "
        "हर्ष इति किम्? प्रमादः, संमादः. प्रसंभ्यामिति नोक्तम्, "
        "निपातनं रूढ्यर्थम् — the rule does NOT say 'after प्र and "
        "सम्', and the fixing is for the established usage: these "
        "two words and no others formed the same way.",
    ),
    "sammada": (
        "3.3.68", "ap",
        "प्रमदसंमदौ हर्षे — कोकिलानां संमदः, the delight of "
        "cuckoos. Fixed with प्रमद by one rule, and both only where "
        "gladness is meant.",
    ),
    "glaha": (
        "3.3.70", "ap",
        "अक्षेषु ग्लहः — अक्षस्य ग्लहः, a throw at dice. "
        "अक्षेष्विति किम्? ग्रहः पादस्य.\n\n"
        "AND WHAT IS BEING FIXED IS ONE SOUND. ग्रहेरप् सिद्ध एव, "
        "लत्वार्थं निपातनम् — the affix would have come anyway by "
        "3.3.58; the निपातन is for the र becoming ल. A fixed form "
        "stated for a single letter of it.\n\n"
        "अन्ये ग्लहिं प्रकृत्यन्तरमाहुः, ते घञं प्रत्युदाहरन्ति, "
        "ग्लाहः — others take ग्लह् for a root in its own right and "
        "give घञ् as the counter-example. A second opinion recorded "
        "and not chosen between.",
    ),
    "āhāva": (
        "3.3.74", "ap",
        "निपानमाहावः — आहावः पशूनाम्, the trough at a well. "
        "निपिबन्त्यस्मिन्निति निपानमुदकाधार उच्यते, and the vṛtti "
        "explains the name: कूपोपसरेषु य उदकाधारस्तत्र हि पानाय "
        "पशव आहूयन्ते — cattle are CALLED to it, which is the root. "
        "THREE things are fixed at once: संप्रसारणम्, अप् and "
        "वृद्धि. निपानमिति किम्? आह्वायः.",
    ),
    "praghaṇa": (
        "3.3.79", "ap",
        "अगारैकदेशे प्रघणः प्रघाणश्च — द्वारप्रकोष्ठो बाह्य "
        "उच्यते, the outer porch by a door. TWO forms fixed by one "
        "rule, differing in a vowel, and both stand. "
        "अगारैकदेश इति किम्? प्रघातोऽन्यः.",
    ),
    "praghāṇa": (
        "3.3.79", "ap",
        "अगारैकदेशे प्रघणः प्रघाणश्च — the second of the two forms "
        "this rule fixes, and the च is what admits it.",
    ),
    "udghana": (
        "3.3.80", "ap",
        "उद्घनोऽत्याधाने — यस्मिन् काष्ठे स्थापयित्वा अन्यानि "
        "काष्ठानि तक्ष्यन्ते तदभिधीयते, the block other wood is "
        "laid on to be cut. उद्घातोऽन्यः.",
    ),
    "parvatopaghna": (
        "3.3.85", "ap",
        "उपघ्नमाश्रये — पर्वतोपघ्नः, ग्रामोपघ्नः, a place sheltering "
        "under a hill. अप् and the LOSS OF THE PENULTIMATE are both "
        "fixed: उपधालोपश्च निपात्यते. आश्रयशब्दः सामीप्यं "
        "प्रत्यासत्तिं लक्षयति — the word 'shelter' marks out "
        "nearness. आश्रय इति किम्? पर्वतोपघात एवान्यः.",
    ),
    "nigha": (
        "3.3.87", "ap",
        "निघो निमितम् — निघा वृक्षाः, निघाः शालयः, trees of an even "
        "growth. टिलोपो घत्वं च निपात्यते. समन्ताद् मितं निमितम्, "
        "समारोहपरिणाहम् — measured all round, in height and girth. "
        "निमितमिति किम्? निघातः.",
    ),
    "ūti": (
        "3.3.97", "ktin",
        "ऊतियूतिजूतिसातिहेतिकीर्तयश्च — ऊत्यादयः शब्दा निपात्यन्ते, "
        "and उदात्त runs down from 3.3.96. Each is fixed for a "
        "different reason, which is why they are entries and not a "
        "row: अवतेः ऊठ् by 6.4.20 and ऊतिः is स्वरार्थं वचनम्; "
        "यूतिः and जूतिः lengthen; सातिः either keeps इत्व off स्यति "
        "or is स्वरार्थ from सनोति after 6.4.42; हेतिः is from हन् "
        "or हिनोति; कीर्तिः from कीर्तयति. Six words, six grounds.",
    ),
    "icchā": (
        "3.3.101", "śa",
        "इच्छा — इषेर्धातोः शः प्रत्ययो यगभावश्च निपात्यते: the "
        "affix AND the absence of यक् are both fixed. 3.3.96 had "
        "already pointed forward to this — इषेस्तु इच्छा इति "
        "निपातनं वक्ष्यति.\n\n"
        "SCOPE — परिचर्यापरिसर्यामृगयाटाट्यानामुपसंख्यानम्: "
        "परिचर्या, परिसर्या, मृगया, अटाट्या. And जागर्तेरकारो वा — "
        "जागरा beside जागर्या.",
    ),
    "gocara": (
        "3.3.119", "gha",
        "गोचरसंचरवहव्रजव्यजापणनिगमाश्च — गावश्चरन्त्यस्मिन्निति "
        "गोचरः, संचरः, वहः, व्रजः, व्यजः, आपणः, निगमः; and "
        "चकारोऽनुक्तसमुच्चयार्थः adds कषः, निकषः.\n\n"
        "हलश्च इति घञं वक्ष्यति, तस्यायमपवादः — an exception stated "
        "BEFORE the rule it excepts, which comes at 3.3.121. And one "
        "of the words is fixed for what does NOT happen to it: "
        "निपातनाद् अजेर्व्यघञपोः इति वीभावो न भवति, so व्यज keeps "
        "its अज where 2.4.56 would have replaced it.",
    ),
    "adhyāya": (
        "3.3.122", "ghañ",
        "अध्यायन्यायोद्यावसंहारावायाश्च — अधीयतेऽस्मिन्नित्यध्यायः, "
        "नीयतेऽनेनेति न्यायः, उद्यावः, संहारः, आधारः, आवायः; and "
        "the च adds अवहारः.\n\n"
        "अहलन्तार्थ आरम्भः — the rule exists for roots NOT ending in "
        "a consonant, since 3.3.121 covers those. 3.3.118's घ would "
        "otherwise have come, and घञ् is fixed instead.",
    ),
    "udaṅka": (
        "3.3.123", "ghañ",
        "उदङ्कोऽनुदके — तैलोदङ्कः, an oil-vessel. अनुदक इति किम्? "
        "उदकोदञ्चनः.\n\n"
        "AND THE VṚTTI ASKS WHY THE WORD IS FIXED AT ALL. ननु च हलश्च "
        "इति सिद्ध एव घञ्? — 3.3.121 gives it already. "
        "उदके प्रतिषेधार्थमिदं वचनम्: the statement is for the "
        "PROHIBITION, to keep the form off where water is meant. A "
        "निपातन whose work is entirely negative.\n\n"
        "घः कस्माद् न प्रत्युदाह्रियते? विशेषाभावात् — why is घ not "
        "given as the counter-form? Because there would be no "
        "difference: घञ्यपि थाथादिस्वरेणान्तोदात्त एव, both come out "
        "accented alike.",
    ),
    "ānāya": (
        "3.3.124", "ghañ",
        "आनायोऽनहः — आनायो मत्स्यानाम्, आनायो मृगाणाम्, a net. "
        "आङ्पूर्वाद् नयतेः करणे घञ् निपात्यते, and it is fixed only "
        "where a NET is meant: जालं चेत् तद् भवति.",
    ),
    "apaghana": (
        "3.3.81", "ap",
        "अपघनोऽङ्गम् — अपघनः अङ्गम्. And the vṛtti narrows what "
        "अङ्ग means here by asking: अवयवः, एकदेशो न सर्वः; किं "
        "तर्हि? पाणिः पादश्चाभिधीयते — a LIMB and not the body, a "
        "hand or a foot. अपघातोऽन्यः.",
    ),
}


def _fixed(word: str):
    """One fixed word, read by both entry points so neither calls the
    other and the reuse walk sees no edge between them."""
    return NIPATANA.get(word)


def nipatana(word: str = "") -> object:
    """
    3.3.68, 3.3.70, 3.3.74 and 3.3.79 to 3.3.81 — words given whole.

    A table that derived these would be pretending to a derivation the
    grammar declines to give. Each entry carries its own affix, since
    what is fixed differs from word to word: 3.3.70 fixes a single
    SOUND of a form the rules already reach, and 3.3.74 fixes three
    things at once.
    """
    entry = _fixed(word)
    if entry is None:
        return NotAdded(
            "",
            "No rule of this pāda fixes that word. The ones it fixes "
            "are " + ", ".join(sorted(NIPATANA)))
    sutra, affix, why = entry
    return Added(affix, sutra, why)

#: 3.3.113's own worked examples, in the three groups the vṛtti puts
#: them in. Each group is a DIFFERENT way of going beyond where the
#: affix was prescribed, which is what बहुलम् buys.
KRTYA_LYUT_BAHULAM = {
    "kṛtya-kāraka": (
        ("snānīyaṃ cūrṇam", "स्नानीयं चूर्णम् — powder for bathing"),
        ("dānīyo brāhmaṇaḥ", "दानीयो ब्राह्मणः — a brahmin to give to"),
    ),
    "lyuṭ-kāraka": (
        ("apasecanam", "अपसेचनम् — a means of sprinkling off"),
        ("avasrāvaṇam", "अवस्रावणम् — a means of draining"),
        ("rājabhojanāḥ śālayaḥ", "राजभोजनाः शालयः — rice a king eats"),
        ("rājācchādanāni vāsāṃsi",
         "राजाच्छादनानि वासांसि — cloths a king wears"),
        ("praskandanam", "प्रस्कन्दनम् — a falling away"),
        ("prapatanam", "प्रपतनम् — a falling forward"),
    ),
    "anye-kṛtaḥ": (
        ("pādahārakaḥ", "पादाभ्यां ह्रियते पादहारकः — carried by the "
                        "feet"),
        ("galecopakaḥ", "गले चोप्यते गलेचोपकः — thrust at the throat"),
    ),
}


def krtya_lyut_bahulam(group: str = "") -> object:
    """
    3.3.113 कृत्यल्युटो बहुलम् — the rule six others have leaned on.

    कृत्यसंज्ञकाः प्रत्यया ल्युट् च बहुलमर्थेषु भवन्ति, यत्र
    विहितास्ततोऽन्यत्रापि भवन्ति: the कृत्य affixes and ल्युट् come
    बहुलम्, and OCCUR BEYOND WHERE THEY WERE PRESCRIBED. That is why
    the commentary reaches for it whenever a run does not give a form
    usage has — at 3.2.53, 3.2.153, 3.3.24, 3.3.26, 3.3.43 and 3.3.44,
    and 3.3.56 cites it for a different reason again.

    **It also closes the two headings.** भावे अकर्तरि च कारक इति
    निवृत्तम् — the conditions running since 3.3.18 and 3.3.19 stop
    here, which is exactly the extent 3.3.56 stated: यावत् कृत्यल्युटो
    बहुलम् इति. A claim made fifty-seven sūtras early and confirmed by
    the rule it named.

    Like 3.3.1's बहुलम्, this cannot be resolved into conditions and
    the codification does not pretend otherwise. What it can do is say
    WHICH KIND of going-beyond is licensed, since the vṛtti sorts its
    examples into three: कृत्य affixes given for भाव and कर्मन्
    appearing for another kāraka; ल्युट् given for करण and अधिकरण
    appearing for भाव, and the reverse; and बहुलग्रहणादन्येऽपि कृतो
    यथाप्राप्तमभिधेयं व्यभिचरन्ति — other कृत् affixes departing from
    what they should denote.
    """
    if group and group not in KRTYA_LYUT_BAHULAM:
        return NotAdded(
            "3.3.113",
            "3.3.113 licenses three kinds of going-beyond, and %s is "
            "not one of them: %s" % (group, ", ".join(
                sorted(KRTYA_LYUT_BAHULAM))))
    return Added(
        "kṛtya, lyuṭ", "3.3.113",
        "कृत्यल्युटो बहुलम् — कृत्यसंज्ञकाः प्रत्यया ल्युट् च "
        "बहुलमर्थेषु भवन्ति, यत्र विहितास्ततोऽन्यत्रापि भवन्ति. The "
        "affixes occur BEYOND where they were prescribed, which is "
        "why six rules of these two pādas send an awkward form here "
        "rather than accounting for it.\n\n"
        "भावे अकर्तरि च कारक इति निवृत्तम्: and the two headings "
        "running since 3.3.18 and 3.3.19 stop at this rule — the "
        "extent 3.3.56 stated fifty-seven sūtras early, यावत् "
        "कृत्यल्युटो बहुलम् इति.\n\n"
        "Three kinds of going-beyond, and the vṛtti keeps them apart. "
        "भावकर्मणोः कृत्या विहिताः कारकान्तरेऽपि भवन्ति — स्नानीयं "
        "चूर्णम्, दानीयो ब्राह्मणः. करणाधिकरणयोर्भावे च ल्युट्, "
        "अन्यत्रापि भवति — अपसेचनम्, राजभोजनाः शालयः, प्रस्कन्दनम्. "
        "And बहुलग्रहणादन्येऽपि कृतो यथाप्राप्तमभिधेयं व्यभिचरन्ति — "
        "पादहारकः, गलेचोपकः.\n\n"
        "Not resolved into conditions, and it cannot be: बहुलम् is "
        "the same refusal 3.3.1 made about the उणादि affixes at the "
        "other end of this pāda.")
