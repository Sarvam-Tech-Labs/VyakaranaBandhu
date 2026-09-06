# -*- coding: utf-8 -*-
"""
सनादि — the affixes that make a new root, 3.1.5 to 3.1.31.

The module opened on यङ् alone, because यङ् is what 1.1.4 turns on, and
that narrative is kept below. The table came later and holds the whole
run: twenty-six rules adding eleven affixes, some to a root and some to
a finished word, each in a sense the rule names. 3.1.32 सनाद्यन्ता
धातवः then calls whatever they make a root, which is what lets the
grammar start over on it.

**यङ् is in the table once and implemented once.** 3.1.22 has its own
function below, `yan`, because its conditions are phonological — one
vowel, consonant-initial — and no other row needs them. 3.1.23 and
3.1.24 add the same affix on quite different grounds, कौटिल्य and
भावगर्हा, and नित्यम् in both: they are rows, not callers. The affix
being the same does not make the rules the same.

    3.1.22   धातोरेकाचो हलादेः क्रियासमभिहारे यङ्   the affix is added
    3.1.32   सनाद्यन्ता धातवः                        and the result is a root
    3.1.134  नन्दिग्रहिपचादिभ्यो ल्युणिन्यचः          अच् comes after it
    2.4.74   यङोऽचि च                                and the यङ् then drops

Read in that order the four tell one story, and it is the story 1.1.4
exists for. यङ् is added to लू and the stem लोलूय is a *root* by 3.1.32 —
which is what makes the यङ् inside it a धात्वेकदेश. अच् is then added, and
that same अच् elides the यङ् by 2.4.74. So the affix which would have
strengthened the vowel is the affix that ate part of the root, and 1.1.4
takes its strengthening away: लोलुवः, not लोलवः.

The Kāśikā on 1.1.4 sets it out in one sentence — लोलूयादिभ्यो यङन्तेभ्यः
पचाद्यचि विहिते यङो लुकि कृते तमेवाचम् आश्रित्य ये गुणवृद्धी प्राप्ते तयोः
प्रतिषेधः — and तम् एव अचम् आश्रित्य is the whole of it: it is *that very*
aC the prohibition is about, not some other affix.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple, Union

from src.astadhyayi.dvirvacana import (
    Change, is_ekac, is_haladi, reduplicated)

#: यङ् as it stands after its ṅ is dropped. The ङ् is an it by 1.3.3
#: हलन्त्यम् and goes by 1.3.9 तस्य लोपः, both codified, leaving य.
YAN = "ya"

#: The vārttika on 3.1.22 admits seven roots that fail एकाच् or हलादि:
#: सूचिसूत्रिमूत्र्यट्यर्त्यशूर्णोतीनां ग्रहणं यङ्विधावनेकाजहलाद्यर्थम्.
#: Named as the Kāśikā names them. Only अटि reaches a stem here — the rest
#: want changes to the root before the doubling that are not codified, and
#: `dvirvacana` says which.
VARTTIKA_ROOTS: Tuple[str, ...] = (
    "sūci", "sūtri", "mūtri", "aṭi", "arti", "aśū", "ūrṇoti",
)

#: The roots those names stand for, where this module can reach them.
_VARTTIKA_STEMS = {"aṭi": "aṭ"}


@dataclass(frozen=True)
class Yananta:
    """A stem made with यङ्, and how it was made."""

    stem: str
    root: str
    by: str
    why: str
    changes: Tuple[Change, ...] = ()


@dataclass(frozen=True)
class Refused:
    """Why 3.1.22 does not reach this root."""

    root: str
    by: str
    why: str


def yan(
    root: str, *, kriyasamabhihara: bool = True, sopasarga: bool = False,
) -> Union[Yananta, Refused]:
    """
    3.1.22 — यङ् after a one-vowelled consonant-initial root, in the sense
    of क्रियासमभिहार.

    पौनःपुन्यं भृशार्थो वा क्रियासमभिहारः: doing a thing again and again, or
    doing it hard. पुनःपुनः पचति gives पापच्यते; भृशं ज्वलति gives
    जाज्वल्यते. The sense is a parameter because no form carries it — भृशं
    शोभते and भृशं रोचते are refused अनभिधानात्, on usage alone, and that is
    not something a rule can be asked to see.

    The three counter-examples are the three conditions:
    धातोरिति किम्? भृशं प्राटति — सोपसर्गाद् उत्पत्तिर्मा भूत्.
    एकाच इति किम्? भृशं जागर्ति.
    हलादेरिति किम्? भृशम् ईक्षते.
    """
    if not kriyasamabhihara:
        return Refused(
            root, "3.1.22",
            "क्रियासमभिहारे — the affix is for repeated or intense action "
            "and for nothing else",
        )
    if sopasarga:
        return Refused(
            root, "3.1.22",
            "धातोरिति किम्? भृशं प्राटति — सोपसर्गाद् उत्पत्तिर्मा भूत्, "
            "the affix does not come after a root with a preverb on it",
        )

    admitted = root in _VARTTIKA_STEMS.values()
    if not admitted:
        if not is_ekac(root):
            return Refused(
                root, "3.1.22",
                f"एकाच इति किम्? भृशं जागर्ति — {root} has more than one "
                f"vowel and is not among the seven the vārttika adds",
            )
        if not is_haladi(root):
            return Refused(
                root, "3.1.22",
                f"हलादेरिति किम्? भृशम् ईक्षते — {root} does not begin with "
                f"a consonant and is not among the seven the vārttika adds",
            )

    doubled = reduplicated(root, affix=YAN, after="yaṅ")
    return Yananta(
        stem=doubled.text,
        root=root,
        by="3.1.22",
        why=(
            "धातोरेकाचो हलादेः क्रियासमभिहारे यङ् — पुनःपुनः or भृशम्: "
            "पापच्यते, यायज्यते, जाज्वल्यते, देदीप्यते. The doubling that "
            "follows is 6.1.9's"
            + (", and this root is one of the seven the vārttika admits "
               "though it fails एकाच् or हलादि" if admitted else "")
        ),
        changes=doubled.changes,
    )


@dataclass(frozen=True)
class Named:
    """That a stem bears the name धातु, and which rule gave it."""

    name: str
    by: str
    why: str


def dhatu_by(stem: str, *, sanadyanta: bool = False) -> Optional[Named]:
    """
    3.1.32 सनाद्यन्ता धातवः — a stem ending in one of the सनादि affixes is
    itself called धातु. चिकीर्षति, पुत्रीयति, पुत्रकाम्यति.

    Two rules confer this one name and they are asked in the order a form
    meets them: 1.3.1 भूवादयो धातवः for what the dhātupāṭha lists, and this
    for what the grammar builds. लू is a root by the first; लोलूय is a root
    by the second, and only by the second — it is in no list.

    That second reading is what 1.1.4 turns on. If लोलूय is a धातु then the
    यङ् inside it is a धात्वेकदेश, and the Kāśikā's first line there —
    धात्वेकदेशो धातुः — makes eliding the यङ् an eliding of the root.
    """
    from src.astadhyayi.samjna import is_dhatu as listed

    if listed(stem):
        return Named(
            "dhātu", "1.3.1",
            "भूवादयो धातवः — the dhātupāṭha lists it",
        )
    if sanadyanta:
        return Named(
            "dhātu", "3.1.32",
            "सनाद्यन्ता धातवः — सनादयोऽन्ते येषां ते सनाद्यन्ताः: the whole "
            "stem, यङ् and all, bears the name. It is in no list and needs "
            "none; the grammar built it",
        )
    return None


def pacadi(stem: str, *, yananta: bool = False) -> Optional[Named]:
    """
    3.1.134 नन्दिग्रहिपचादिभ्यो ल्युणिन्यचः, for its third gaṇa only.

    त्रिभ्यो गणेभ्यस्त्रयः प्रत्यया यथासंख्यं भवन्ति — three classes, three
    affixes, paired in order: नन्द्यादि takes ल्यु, ग्रहादि takes णिनि,
    पचादि takes अच्. Only the third is wanted here.

    The gaṇa is read off the gaṇapāṭha on disk, and the reason a यङन्त stem
    is admitted to it is recorded there too: पचादि is marked open-ended, an
    आकृतिगण, and the Kāśikā on 1.1.4 says outright that the अच् of this
    sūtra is what लोलूय takes — लोलूयादिभ्यो यङन्तेभ्यः पचाद्यचि विहिते.

    The Kāśikā also warns what the gaṇa is not: नन्दिग्रहिपचादयश्च न
    धातुपाठतः संनिविष्टा गृह्यन्ते — these are not dhātupāṭha entries but
    stems drawn out of prātipadika lists, which is why membership is a
    lookup and not a computation.
    """
    from src.astadhyayi.corpus import load_ganapatha

    gana = next(
        (g for g in load_ganapatha().get("3.1.134", ())
         if g.name.startswith("pacādi")), None)
    if gana is None:
        return None

    if stem in gana.items:
        return Named(
            "ac", "3.1.134",
            f"पचादिभ्योऽच् — {stem} is in the gaṇa as it stands",
        )
    if yananta and gana.open_ended:
        return Named(
            "ac", "3.1.134",
            "पचादिभ्योऽच् — पचादि is an आकृतिगण, and the Kāśikā puts the "
            "यङन्त stems in it by name: लोलूयादिभ्यो यङन्तेभ्यः पचाद्यचि "
            "विहिते",
        )
    return None


@dataclass(frozen=True)
class Elided:
    """What is left of a यङन्त stem once the यङ् has gone."""

    stem: str
    was: str
    by: str
    why: str


def yan_luk(stem: str, *, before_ac: bool = True) -> Optional[Elided]:
    """
    2.4.74 यङोऽचि च — the यङ् disappears before an अच् affix.

    यङो लुग् भवत्यचि प्रत्यये परतः: लोलुवः, पोपुवः, सनीस्रंसः, दनीध्वंसः.
    And the च draws बहुल down, so it happens outside अच् as well —
    शाकुनिको लालपीति, दुन्दुभिर्वावदीति — which is not modelled, since the
    forms that need it are finite and this module makes stems.

    A लुक् takes the affix away and leaves everything it did standing:
    the doubling stays, and so does everything 7.4 did to the copy. That is
    the whole reason there is anything left to call लोलू.
    """
    if not before_ac or not stem.endswith(YAN):
        return None
    return Elided(
        stem=stem[: -len(YAN)],
        was=stem,
        by="2.4.74",
        why=(
            "यङोऽचि च — यङो लुग् भवत्यचि प्रत्यये परतः. The affix goes and "
            "its work remains: लोलूय becomes लोलू with the doubling intact"
        ),
    )


@dataclass(frozen=True)
class Step:
    """One rule's turn in the derivation, and the form after it."""

    by: str
    form: str
    why: str


@dataclass(frozen=True)
class Derivation:
    """A finished stem and every rule that made it."""

    form: str
    root: str
    steps: Tuple[Step, ...]

    @property
    def rules(self) -> Tuple[str, ...]:
        return tuple(step.by for step in self.steps)


def intensive_stem(root: str) -> Union["Derivation", Refused]:
    """
    लू to लोलुव, मृज् to मरीमृज — the whole run, rule by rule.

    This is the derivation 1.1.4 is written for, and it is the first one in
    this codebase where a prohibition is reached because of what an earlier
    rule in the same derivation did, rather than because a caller said so.
    """
    from src.astadhyayi.anga import iyan_uvan

    made = yan(root)
    if isinstance(made, Refused):
        return made

    steps = [Step("3.1.22", made.stem, made.why)]
    steps.extend(Step(c.by, c.now, c.why) for c in made.changes)

    named = dhatu_by(made.stem, sanadyanta=True)
    if named is not None:
        steps.append(Step(named.by, made.stem, named.why))

    affix = pacadi(made.stem, yananta=True)
    if affix is None:
        return Derivation(made.stem, root, tuple(steps))
    steps.append(Step(affix.by, made.stem + " + a", affix.why))

    dropped = yan_luk(made.stem)
    if dropped is None:
        return Derivation(made.stem + "a", root, tuple(steps))
    steps.append(Step(dropped.by, dropped.stem + " + a", dropped.why))

    # The same aC prescribed the strengthening and elided the यङ्, which is
    # the whole of 1.1.4's condition. It is asked here rather than asserted:
    # `dhatu_lopa` is True because 2.4.74 just ran, on this stem, at the
    # instance of this affix.
    stopped = _strengthening_stopped(root, dropped.stem)
    if stopped is not None:
        steps.append(Step(stopped[0], dropped.stem + " + a", stopped[1]))

    turned = iyan_uvan(dropped.stem, ardhadhatuka=True, dhatu_lopa=True)
    if turned is not None and turned.applied:
        steps.append(Step(turned.by, turned.form + "a", turned.why))
        return Derivation(turned.form + "a", root, tuple(steps))
    return Derivation(dropped.stem + "a", root, tuple(steps))


def _strengthening_stopped(root: str, stem: str) -> Optional[Tuple[str, str]]:
    """
    Which strengthening was in line here, and whether 1.1.4 took it away.

    Asked of the rule that would have done it rather than worked out again:
    7.2.114 मृजेर्वृद्धिः for मृज्, whose target is the ऋ inside the aṅga
    and not its final sound — testing the final would find a consonant and
    conclude, wrongly, that nothing was ever in danger. For the rest it is
    the guṇa of 7.3.84, whose target is the aṅga's final इक्.
    """
    from src.astadhyayi.adesa import antya
    from src.astadhyayi.anga import mrjer_vrddhi
    from src.astadhyayi.rules.adhyaya_1_pada_1 import guna_vrddhi_blocked

    if root in ("mṛj", "mṛjū"):
        verdict = mrjer_vrddhi(root, ardhadhatuka=True, dhatu_lopa=True)
        if verdict.result is None and verdict.by == "1.1.4":
            return verdict.by, verdict.why
        return None

    blocked = guna_vrddhi_blocked(
        antya(stem), ardhadhatuka=True, dhatu_lopa=True)
    return (blocked.by, blocked.why) if blocked is not None else None


__all__ = [
    "Derivation", "Elided", "Named", "Refused", "Step", "VARTTIKA_ROOTS",
    "YAN", "Yananta", "dhatu_by", "intensive_stem", "pacadi", "yan",
    "yan_luk",
]

# ---------------------------------------------------------------------------
# 3.1.5 to 3.1.31 — the affixes that make a new root
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Sanadi:
    """One rule adding one सनादि affix, as its conditions."""

    sutra: str
    gives: str
    #: What it is added to: a धातु or a finished word, a प्रातिपदिक.
    base: str = "dhātu"
    #: The roots or stems the sūtra names. Empty means any of that base.
    of: Tuple[str, ...] = ()
    #: A gaṇapāṭha list read from disk, by its name there.
    gana: str = ""
    #: A class of the dhātupāṭha, by its code — "10" for चुरादि.
    verbal_gana: str = ""
    #: The sense the rule requires, in the vṛtti's own term.
    sense: str = ""
    #: वा or विभाषा in the sūtra itself.
    optional: bool = False
    #: नित्यम् said outright — 3.1.23 and 3.1.24, where it narrows the
    #: SCOPE rather than removing an option: विषयनियमार्थम्.
    nitya: bool = False
    #: A further change the same rule makes, where it states one.
    also: str = ""
    why: str = ""


#: 3.1.21's ten, named in the sūtra itself.
MUNDADI: Tuple[str, ...] = (
    "muṇḍa", "miśra", "ślakṣṇa", "lavaṇa", "vrata", "vastra", "hala",
    "kala", "kṛta", "tūsta",
)

#: 3.1.25's thirteen, likewise named in the sūtra, before it sends the
#: rest to चुरादि.
SATYADI: Tuple[str, ...] = (
    "satya", "apa", "pāśa", "rūpa", "vīṇā", "tūla", "śloka", "senā",
    "loman", "tvaca", "varman", "varṇa", "cūrṇa",
)

#: 3.1.24's eight.
LUPADI: Tuple[str, ...] = (
    "lup", "sad", "car", "jap", "jabh", "dah", "daś", "gṝ",
)

#: 3.1.28's five.
GUPADI: Tuple[str, ...] = ("gupū", "dhūp", "vicch", "paṇ", "pan")

#: The three affixes 3.1.31 makes optional before an आर्धधातुक —
#: आयादयः, "आय and what follows it", which the vṛtti reads as the
#: affixes of 3.1.28, 3.1.29 and 3.1.30.
AYADI: Tuple[str, ...] = ("āya", "īyaṅ", "ṇiṅ")

SANADI: Tuple[Sanadi, ...] = (
    Sanadi("3.1.5", "san", of=("gup", "tij", "kit"),
           sense="nindā-kṣamā-vyādhipratīkāra",
           why="गुप्तिज्किद्भ्यः सन् — जुगुप्सते, तितिक्षते, चिकित्सति. "
               "The vārttika holds it to three senses — "
               "निन्दाक्षमाव्याधिप्रतीकारेषु सन्निष्यते, अन्यत्र यथाप्राप्तं "
               "प्रत्यया भवन्ति — so गोपयति, तेजयति stand outside it. "
               "गुपादिष्वनुबन्धकरणमात्मनेपदार्थम्: the marks on the roots "
               "are there for the middle endings"),
    Sanadi("3.1.6", "san", of=("mān", "badh", "dān", "śān"),
           also="the abhyāsa's इ is lengthened",
           why="मान्बधदान्शान्भ्यो दीर्घश्चाभ्यासस्य — मीमांसते, बीभत्सते, "
               "दीदांसते, शीशांसते. Here too a sense is wanted: "
               "अत्रापि सन्नर्थविशेष इष्यते — मानेर्जिज्ञासायाम्, बधेर्वैरूप्ये, "
               "दानेरार्जवे, शानेर्निशाने. Without it मानयति, बाधयति"),
    Sanadi("3.1.7", "san", sense="icchā", optional=True,
           why="धातोः कर्मणः समानकर्तृकादिच्छायां वा — कर्तुमिच्छति, "
               "चिकीर्षति; जिहीर्षति. Four conditions and a counter for "
               "each: धातोरिति किम्? प्राचिकीर्षत् — the affix goes on the "
               "root, not on root-with-preverb. कर्मण इति किम्? गमनेनेच्छति. "
               "समानकर्तृकादिति किम्? देवदत्तस्य भोजनमिच्छति यज्ञदत्तः. "
               "इच्छायामिति किम्? कर्तुं जानाति. And वावचनाद् वाक्यमपि "
               "भवति — the phrase stands beside the derived verb"),
    Sanadi("3.1.8", "kyac", base="prātipadika", sense="icchā",
           optional=True,
           why="सुप आत्मनः क्यच् — आत्मनः पुत्रमिच्छति, पुत्रीयति. "
               "सुब्ग्रहणं किम्? महान्तं पुत्रमिच्छति — a phrase, not a "
               "word. आत्मन इति किम्? राज्ञः पुत्रमिच्छति: the wish must "
               "be for what is one's OWN. ककारो नः क्ये इति "
               "सामान्यग्रहणार्थः, the क् is marked so 1.4.15 can name "
               "all three क्य affixes together"),
    Sanadi("3.1.9", "kāmyac", base="prātipadika", sense="icchā",
           optional=True,
           why="काम्यच्च — आत्मनः पुत्रमिच्छति, पुत्रकाम्यति; वस्त्रकाम्यति. "
               "योगविभाग उत्तरत्र क्यचोऽनुवृत्त्यर्थः: the rule is split "
               "off so that क्यच् and not काम्यच् carries down to 3.1.10"),
    Sanadi("3.1.10", "kyac", base="prātipadika", sense="ācāra",
           optional=True,
           why="उपमानादाचारे — पुत्रमिवाचरति, पुत्रीयति छात्रम्; "
               "प्रावारीयति कम्बलम्. आचारक्रियायाः प्रत्ययार्थत्वात् "
               "तदपेक्षयैवोपमानस्य कर्मता — the thing compared is the "
               "object only in relation to the behaving, which is what "
               "the affix means. A vārttika adds the locative: "
               "प्रासादीयति कुट्याम्"),
    Sanadi("3.1.11", "kyaṅ", base="prātipadika", sense="ācāra",
           optional=True, also="a final स is dropped",
           why="कर्तुः क्यङ् सलोपश्च — श्येन इवाचरति काकः, श्येनायते; "
               "कुमुदं पुष्करायते. Here the comparison is with the AGENT, "
               "where 3.1.10 took the object. अन्वाचयशिष्टः सलोपः — the "
               "स-elision is added on and is not a condition, so the "
               "affix comes whether or not there is a स to drop. And it "
               "is a व्यवस्थितविभाषा: ओजसोऽप्सरसो नित्यं पयसस्तु "
               "विभाषया. Being a स्थानषष्ठी it reaches the last sound "
               "only, so हंसायते and सारसायते keep theirs"),
    Sanadi("3.1.12", "kyaṅ", base="prātipadika", gana="bhṛśādi",
           sense="bhū", also="a final consonant is dropped",
           why="भृशादिभ्यो भुव्यच्वेर्लोपश्च हलः — अभृशो भृशो भवति, "
               "भृशायते; शीघ्रायते. The sense is अभूततद्भाव, becoming "
               "what one was not. अच्वेः keeps it off a stem already "
               "made with च्वि, and the vṛtti says the prohibition is "
               "there तत्सदृशप्रतिपत्त्यर्थम्, to fix the pattern by "
               "showing its edge"),
    Sanadi("3.1.13", "kyaṣ", base="prātipadika", gana="lohitādi",
           sense="bhū",
           why="लोहितादिडाज्भ्यः क्यष् — लोहितायति, लोहितायते; and after "
               "a डाच्-final, पटपटायति. The vārttika divides the two "
               "affixes by the list: लोहितडाज्भ्यः क्यष्वचनम्, भृशादिषु "
               "इतराणि — what is READ in लोहितादि takes क्यङ्, what is "
               "not takes क्यष्. आकृतिगणश्चायम्, so the list is open"),
    Sanadi("3.1.14", "kyaṅ", base="prātipadika", of=("kaṣṭa",),
           sense="kramaṇa",
           why="कष्टाय क्रमणे — कष्टाय कर्मणे क्रामति, कष्टायते: striving "
               "after what is harsh, and अनार्जवे, not straightforwardly. "
               "अत्यल्पमिदमुच्यते, says the vṛtti — too little is stated "
               "— and a vārttika widens it to six words in the sense "
               "कण्वचिकीर्षा: सत्रायते, कक्षायते, कृच्छ्रायते, गहनायते"),
    Sanadi("3.1.15", "kyaṅ", base="prātipadika",
           of=("romantha", "tapas"), sense="varti-cara",
           why="कर्मणो रोमन्थतपोभ्यां वर्तिचरोः — यथाक्रमम्, each word to "
               "its own sense: रोमन्थं वर्तयति, रोमन्थायते गौः; तपश्चरति, "
               "तपस्यति. A vārttika narrows the first to हनुचलन, the "
               "moving of the jaw, so कीटो रोमन्थं वर्तयति is out; "
               "another gives तपस् the active endings"),
    Sanadi("3.1.16", "kyaṅ", base="prātipadika", of=("bāṣpa", "ūṣman"),
           sense="udvamana",
           why="बाष्पोष्मभ्यामुद्वमने — बाष्पमुद्वमति, बाष्पायते; "
               "ऊष्मायते. A vārttika adds फेन: फेनायते"),
    Sanadi("3.1.17", "kyaṅ", base="prātipadika",
           of=("śabda", "vaira", "kalaha", "abhra", "kaṇva", "megha"),
           sense="karaṇa",
           why="शब्दवैरकलहाभ्रकण्वमेघेभ्यः करणे — शब्दं करोति, शब्दायते; "
               "वैरायते, कलहायते, अभ्रायते, मेघायते. Two vārttikas add "
               "more: सुदिनायते, दुर्दिनायते, नीहारायते, and a further "
               "eight beginning अटायते"),
    Sanadi("3.1.18", "kyaṅ", base="prātipadika", gana="sukhādi",
           sense="kartṛvedanā",
           why="सुखादिभ्यः कर्तृवेदनायाम् — सुखं वेदयते, सुखायते; "
               "दुःखायते. वेदना is अनुभव, feeling it oneself, and the "
               "feeling must belong to the one who feels: कर्तृग्रहणं "
               "किम्? सुखं वेदयते प्रसाधको देवदत्तस्य"),
    Sanadi("3.1.19", "kyac", base="prātipadika",
           of=("namas", "varivas", "citraṅ"), sense="karaṇa",
           optional=True,
           why="नमोवरिवश्चित्रङः क्यच् — and each of the three in its own "
               "sense: नमसः पूजायाम्, नमस्यति देवान्; वरिवसः परिचर्यायाम्, "
               "वरिवस्यति गुरून्; चित्रङ आश्चर्ये, चित्रीयते. ङकार "
               "आत्मनेपदार्थः on the third alone, which is why only it "
               "takes the middle"),
    Sanadi("3.1.20", "ṇiṅ", base="prātipadika",
           of=("puccha", "bhāṇḍa", "cīvara"), sense="karaṇa",
           why="पुच्छभाण्डचीवरात् णिङ् — and the vārttikas give each a "
               "sense: पुच्छाद् उदसने पर्यसने वा, उत्पुच्छयते; भाण्डात् "
               "समाचयने, संभाण्डयते; चीवरादर्जने परिधाने वा, संचीवरयते "
               "भिक्षुः. णकारः सामान्यग्रहणार्थः, marked so 6.4.51 can "
               "name every णि together; ङकार आत्मनेपदार्थः"),
    Sanadi("3.1.21", "ṇic", base="prātipadika", of=MUNDADI,
           sense="karaṇa",
           why="मुण्डमिश्रश्लक्ष्णलवणव्रतवस्त्रहलकलकृततूस्तेभ्यो णिच् — "
               "मुण्डं करोति, मुण्डयति; मिश्रयति, लवणयति. "
               "हलिकल्योरदन्तत्वनिपातनं सन्वद्भावप्रतिषेधार्थम्: हलि and "
               "कलि are given as a-final on purpose, to keep 7.4.93's "
               "सन्वद्भाव away — अजहलत्, अचकलत्"),
    Sanadi("3.1.23", "yaṅ", sense="kauṭilya", nitya=True,
           why="नित्यं कौटिल्ये गतौ — कुटिलं क्रामति, चङ्क्रम्यते; "
               "दन्द्रम्यते. Only of a root that MEANS going. "
               "नित्यग्रहणं विषयनियमार्थम्: the नित्यम् fixes the scope "
               "rather than removing an option — from a going-root the "
               "affix comes for crookedness ONLY, and not for 3.1.22's "
               "repetition, so भृशं क्रामति has none"),
    Sanadi("3.1.24", "yaṅ", of=LUPADI, sense="bhāvagarhā", nitya=True,
           why="लुपसदचरजपजभदहदशगॄभ्यो भावगर्हायाम् — गर्हितं लुम्पति, "
               "लोलुप्यते; जञ्जप्यते, दन्दह्यते. भावग्रहणं किम्? "
               "साधनगर्हायां मा भूत् — मन्त्रं जपति वृषलः: it is the ACT "
               "that is blamed and not who does it. The नित्यम् carries "
               "down and fixes the scope the same way"),
    # 3.1.25 states two bases, not one: thirteen STEMS named in the
    # sūtra, and चुरादि, which is a class of ROOTS. Written as a single
    # row with both conditions, the named list shut the gaṇa out and
    # चुर् reached nothing.
    Sanadi("3.1.25", "ṇic", base="prātipadika", of=SATYADI,
           why="सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो "
               "णिच् — सत्यमाचष्टे, सत्यापयति; विपाशयति, निरूपयति, "
               "उपवीणयति, अभिषेणयति. चुरादि is the tenth class of the "
               "dhātupāṭha and is read from the corpus, not copied. A "
               "vārttika gives three of them an आपुक्: अर्थापयति, "
               "वेदापयति, and आपुग्वचनसामर्थ्यात् the टि is not dropped"),
    Sanadi("3.1.25", "ṇic", verbal_gana="10",
           why="…चुरादिभ्यो णिच् — the second half of the same sūtra, and "
               "a different base: चुरादि is the TENTH class of the "
               "dhātupāṭha, so these are roots where the thirteen before "
               "them are stems. चोरयति, चिन्तयति. Read from the corpus "
               "by its class code rather than copied, as 2.4.72 reads "
               "the second class"),
    Sanadi("3.1.26", "ṇic", sense="hetumat",
           why="हेतुमति च — कटं कारयति, ओदनं पाचयति. हेतुः स्वतन्त्रस्य "
               "कर्तुः प्रयोजकः: the cause is what sets the independent "
               "agent going, and तदीयो व्यापारः प्रेषणादिलक्षणो हेतुमान् "
               "— what the affix means is that prompting. Vārttikas add "
               "तत्करोति (सूत्रयति) and the आख्यान construction, where a "
               "कृत् is dropped and the case-roles stay as they were: "
               "कंसवधमाचष्टे, कंसं घातयति"),
    Sanadi("3.1.27", "yak", gana="kaṇḍvādi",
           why="कण्ड्वादिभ्यो यक् — कण्डूयति, कण्डूयते. द्विविधाः "
               "कण्ड्वादयः, धातवः प्रातिपदिकानि च — the list holds both "
               "roots and stems, and the vṛtti settles which is meant by "
               "where the rule stands: धात्वधिकाराद् धातुभ्य एव प्रत्ययो "
               "विधीयते. The क् is marked to keep guṇa off"),
    Sanadi("3.1.28", "āya", of=GUPADI,
           why="गुपूधूपविच्छिपणिपनिभ्य आयः — गोपायति, धूपायति, विच्छायति, "
               "पणायति, पनायति. पण् is taken in the sense of praising "
               "only, स्तुत्यर्थेन पनिना साहचर्यात् — known by the company "
               "पन् keeps it in — so शतस्य पणते is untouched. And "
               "अनुबन्धश्च केवले चरितार्थः: the marks did their work on "
               "the bare roots, so the आय-stem takes no middle endings"),
    Sanadi("3.1.29", "īyaṅ", of=("ṛti",),
           why="ऋतेरीयङ् — ऋतीयते, ऋतीयेते, ऋतीयन्ते. ऋति is a सौत्र "
               "root, one the sūtra itself supplies, in the sense of "
               "loathing. ङकार आत्मनेपदार्थः. And the rule is written "
               "though the form was already obtainable — ऋतेश्छङिति "
               "सिद्धे ईयङ्वचनं ज्ञापनार्थम् — which TEACHES that आयादि "
               "affixes do not come after affixes prescribed to a root"),
    Sanadi("3.1.30", "ṇiṅ", of=("kam",),
           why="कमेर्णिङ् — कामयते, कामयेते, कामयन्ते. णकारो वृद्ध्यर्थः, "
               "the ण् for the strengthening; ङकार आत्मनेपदार्थः, the ङ् "
               "for the middle endings. Two marks, two jobs"),
)


def provisions_for(sutra_id: str) -> Tuple[Sanadi, ...]:
    """Every row a sūtra of this run states."""
    return tuple(r for r in SANADI if r.sutra == sutra_id)


@dataclass(frozen=True)
class Added:
    """That an affix is added, and by which rule."""

    gives: str
    by: str
    why: str
    optional: bool = False
    nitya: bool = False
    also: str = ""


@dataclass(frozen=True)
class NotAdded:
    """That no rule of 3.1.5 to 3.1.30 reaches this."""

    by: str
    why: str
    gives: str = ""


def _in_gana(word: str, sutra: str, name: str) -> bool:
    from src.astadhyayi.formation import gana_items

    try:
        return word in gana_items(sutra, name)
    except Exception:                       # noqa: BLE001 — corpus absent
        return False


def sanadi_affix(
    base: str,
    *,
    is_root: bool = True,
    sense: str = "",
    upamana: str = "",
    affix: str = "",
) -> object:
    """
    Which सनादि affix this base takes — 3.1.5 to 3.1.30.

    3.1.22 यङ् is not in this walk. Its conditions are phonological and
    `yan` above already asks them; asking twice would be two statements
    of one rule. 3.1.23 and 3.1.24 add the same affix on quite different
    grounds and are rows here, because a shared affix is not a shared
    rule.
    """
    # More than one rule can reach the same base in the same sense, and
    # both answers are right: पुत्रीयति by 3.1.8 and पुत्रकाम्यति by
    # 3.1.9 are alternatives, not rivals. Naming the affix picks which
    # is being asked about; leaving it unnamed answers with the first,
    # which is the reading the text gives first.
    # Where more than one row reaches the same base, the MORE SPECIFIC
    # rule answers — विशेष over सामान्य. Two collisions made this
    # necessary and neither produced a wrong form, only an unreachable
    # rule: पच् is read in the tenth class, so 3.1.25 answered before
    # 3.1.26 हेतुमति च; and धूप likewise, so it answered before 3.1.28,
    # which names धूप outright. A rule that names the sense, or names
    # the base, is saying more than one that names a class.
    matched = [row for row in SANADI
               if _reaches(row, base, is_root, sense, upamana, affix)]
    if not matched:
        return NotAdded(
            "",
            f"No rule of 3.1.5 to 3.1.30 adds an affix to {base} here. "
            f"3.1.22 यङ् is asked separately, through `yan`, and 3.1.31 "
            f"speaks about three of these affixes rather than adding one",
        )
    best = max(matched, key=_how_specific)
    return Added(best.gives, best.sutra, best.why,
                 optional=best.optional, nitya=best.nitya,
                 also=best.also)


def _how_specific(row: Sanadi) -> int:
    """
    How much a row says. Naming the sense counts for more than naming
    the base, a sense being the harder condition to meet; naming a
    class counts for nothing, since that is what every other row
    narrows. Ties keep the text's own order, `max` being stable.
    """
    return (2 if row.sense else 0) + (1 if row.of else 0)


def _reaches(row: Sanadi, base: str, is_root: bool, sense: str,
             upamana: str, affix: str) -> bool:
    """Whether one row of the table covers this base at all."""
    from src.astadhyayi.pada import verbal_gana

    if (row.base == "dhātu") != is_root:
        return False
    if affix and row.gives != affix:
        return False
    if row.sense and row.sense != sense:
        return False
    if row.of and base not in row.of:
        return False
    if row.gana and not _in_gana(base, row.sutra, row.gana):
        return False
    if row.verbal_gana and row.verbal_gana not in verbal_gana(base):
        return False
    # 3.1.10 and 3.1.11 both mean behaving LIKE something and are told
    # apart only by which role the thing compared plays.
    if row.sutra == "3.1.10" and upamana != "karman":
        return False
    if row.sutra == "3.1.11" and upamana != "kartṛ":
        return False
    return True


def ayadi_optional(affix: str, *, ardhadhatuka: bool = False) -> object:
    """
    3.1.31 आयादय आर्धधातुके वा — a rule about three affixes, not a fourth.

    आयादयः is आय and what follows it, which the vṛtti takes as the
    affixes of 3.1.28, 3.1.29 and 3.1.30. Before an आर्धधातुक they
    become optional, so both the plain root and the derived stem carry
    on: गोप्ता beside गोपायिता, अर्तिता beside ऋतीयिता, कमिता beside
    कामयिता.

    नित्यं प्रत्ययप्रसङ्गे तदुत्पत्तिः आर्धधातुकविषये विकल्प्यते — the
    affix was obligatory, and it is the ADDING of it that is made
    optional here, not something about the affix itself. Whether an
    affix is आर्धधातुक is 3.4.114's question and is passed in, as it is
    at 2.4.35.
    """
    if affix not in AYADI:
        return NotAdded(
            "",
            f"आयादयः is आय and the two after it — {', '.join(AYADI)} — so "
            f"3.1.31 does not speak about {affix}",
        )
    if not ardhadhatuka:
        return Added(
            affix, "",
            f"3.1.31 holds before an आर्धधातुक only. Elsewhere {affix} "
            f"stands as its own rule gave it, obligatorily",
        )
    return Added(
        affix, "3.1.31",
        f"आयादय आर्धधातुके वा — before an आर्धधातुक the {affix} is "
        f"optional, so both forms stand: गोप्ता beside गोपायिता, "
        f"अर्तिता beside ऋतीयिता, कमिता beside कामयिता. And it reaches "
        f"the nominal derivatives too — गुप्तिः beside गोपाया",
        optional=True,
    )
