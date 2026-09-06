# -*- coding: utf-8 -*-
"""
निपात, उपसर्ग, गति, कर्मप्रवचनीय — 1.4.56 to 1.4.98.

    1.4.56 – 1.4.58   निपात             the particles
    1.4.59 – 1.4.82   उपसर्ग, गति       and what they are when a verb is there
    1.4.83 – 1.4.98   कर्मप्रवचनीय      and what they are when it is not

**These names co-apply, and that is deliberate.** Everything else in this pāda
stands under 1.4.1 आ कडारादेका संज्ञा, where one name only may hold; this
section is written to get round it, twice, and the Kāśikā names the device
both times:

  1.4.56  प्राग्वचनं संज्ञासमावेशार्थम्। गत्युपसर्गकर्मप्रवचनीयसंज्ञाभिः
          सह निपातसंज्ञा समाविशति.
          The sūtra is cast as a *range* — 'up to ईश्वर' — rather than as a
          list, precisely so that निपात may stand alongside the other three.

  1.4.60  चकारः संज्ञासमावेशार्थः.
          And the च of गतिश्च is there so that गति may stand alongside
          उपसर्ग, which the sūtra before has just given.

So `classify` returns a *set* of names, not one. That is the third and fourth
place in the pāda where संज्ञासमावेश is explicitly restored — 1.4.55's च being
the second — and it settles what was left open at 1.4.20: co-application
inside 1.4.1's scope is a routine move with a standard device, and the only
question there is whether a vārttika may make it.

**And the yogavibhāga at 1.4.60 does the opposite.** The Kāśikā asks why गति
was not simply added to 1.4.59 and answers योगविभाग उत्तरार्थः — उत्तरत्र
गतिसंज्ञैव यथा स्यात्, उपसर्गसंज्ञा मा भूत्. The split is so that everything
from 1.4.61 on gets गति *only*, and not उपसर्ग; otherwise ऊरीस्यात् would take
8.3.87's ṣatva. The codification carries that: the ūryādi provisions give one
name where the prādi ones give two.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, List, Optional, Tuple

from src.astadhyayi.formation import gana_items


class Name(Enum):
    """The four saṃjñās this section gives."""

    NIPATA = "nipāta"
    UPASARGA = "upasarga"
    GATI = "gati"
    KARMAPRAVACANIYA = "karmapravacanīya"


N, U, G, K = Name.NIPATA, Name.UPASARGA, Name.GATI, Name.KARMAPRAVACANIYA

#: 1.4.56's range and 1.4.83's, both stated as प्राक् … from here to there.
NIPATA_FROM, NIPATA_TO = "1.4.56", "1.4.96"
KARMAPRAVACANIYA_FROM, KARMAPRAVACANIYA_TO = "1.4.83", "1.4.98"


#: The gaṇa reader lives in formation.py with the other shared corpus
#: readers — 2.1.17 wants it too, and one of these is enough.
_gana = gana_items


def cadi() -> Tuple[str, ...]:
    """चादि — 1.4.57's group, 155 members and an ākṛtigaṇa."""
    return _gana("1.4.57", "cādi")


def pradi() -> Tuple[str, ...]:
    """प्रादि — 1.4.58's group. Exactly the twenty-two upasargas."""
    return _gana("1.4.58", "prādi")


def uryadi() -> Tuple[str, ...]:
    """ऊर्यादि — 1.4.61's group."""
    return _gana("1.4.61", "ūryādi")


def sakshatprabhrti() -> Tuple[str, ...]:
    """साक्षात्प्रभृति — 1.4.74's group."""
    return _gana("1.4.74", "sākṣātprabhṛti")


# --- what is being classified ---------------------------------------------

SENSES: FrozenSet[str] = frozenset(
    """
    ādara anādara bhūṣaṇa aparigraha śraddhāpratighāta gatyarthavat
    anupadeśa antardhi upāja anvāja anatyādhāna upayamana bandhana aupamya
    lakṣaṇa tṛtīyārtha hīna adhika varjana maryādā itthaṃbhūtākhyāna bhāga
    vīpsā abhāga pratinidhi pratidāna anarthaka pūjā atikramaṇa
    padārtha saṃbhāvanā anvavasarga garhā samuccaya īśvara
    """.split()
)


@dataclass(frozen=True)
class Particle:
    """A word as far as these forty-three sūtras care."""

    form: str
    #: 1.4.59's क्रियायोगे — construed with a verb. The single condition that
    #: divides उपसर्ग/गति from कर्मप्रवचनीय.
    kriya_yoga: bool = False
    #: 1.4.57's असत्त्वे. सत्त्वम् इति द्रव्यम् उच्यते — a substance.
    sattva: bool = False
    sense: Optional[str] = None
    with_kr: bool = False
    chandas: bool = False
    #: 1.4.62's अनुकरणम् — an imitative word, and not followed by इति.
    anukarana: bool = False
    followed_by_iti: bool = False
    #: 1.4.80's ते प्राग्धातोः, and 1.4.81/1.4.82's licence to break it.
    after_dhatu: bool = False
    separated: bool = False


@dataclass(frozen=True)
class Provision:
    """One sūtra's contribution. `gives` is a set, because these co-apply."""

    sutra: str
    gives: FrozenSet[Name]
    words: Tuple[str, ...] = ()
    gana: Tuple[str, ...] = ()
    senses: Tuple[str, ...] = ()
    not_senses: Tuple[str, ...] = ()
    kriya_yoga: Optional[bool] = None
    sattva: Optional[bool] = None
    with_kr: Optional[bool] = None
    anukarana: Optional[bool] = None
    followed_by_iti: Optional[bool] = None
    optional: bool = False
    gloss: str = ""
    example: str = ""
    counter: str = ""

    def unmet(self, who: Particle) -> Tuple[str, ...]:
        missing: List[str] = []
        allowed = set(self.words) | set(self.gana)
        if allowed and who.form not in allowed:
            named = ", ".join(self.words) if self.words else "the gaṇa"
            missing.append(f"word is not one of {named}")
        if self.senses and who.sense not in self.senses:
            missing.append(f"sense is not {'/'.join(self.senses)}")
        if self.not_senses and who.sense in self.not_senses:
            missing.append(f"sense is {who.sense}")
        if self.kriya_yoga is True and not who.kriya_yoga:
            missing.append("not construed with a verb")
        if self.kriya_yoga is False and who.kriya_yoga:
            missing.append("construed with a verb")
        if self.sattva is False and who.sattva:
            missing.append("denotes a substance")
        if self.with_kr is True and not who.with_kr:
            missing.append("not with कृ")
        if self.anukarana is True and not who.anukarana:
            missing.append("not an imitative word")
        if self.followed_by_iti is False and who.followed_by_iti:
            missing.append("followed by इति")
        return tuple(missing)

    def applies(self, who: Particle) -> bool:
        return not self.unmet(who)

    def describe(self) -> str:
        parts: List[str] = []
        if self.words:
            parts.append("word ∈ {" + ", ".join(self.words) + "}")
        if self.gana:
            parts.append(f"word ∈ the gaṇa ({len(self.gana)} members)")
        if self.senses:
            parts.append("sense ∈ {" + ", ".join(self.senses) + "}")
        parts.extend(f"sense ≠ {s}" for s in self.not_senses)
        if self.kriya_yoga is True:
            parts.append("construed with a verb")
        if self.kriya_yoga is False:
            parts.append("not construed with a verb")
        if self.sattva is False:
            parts.append("not denoting a substance")
        if self.with_kr:
            parts.append("with कृ")
        if self.anukarana:
            parts.append("an imitative word")
        if self.followed_by_iti is False:
            parts.append("not followed by इति")
        head = " + ".join(sorted(n.value for n in self.gives))
        if self.optional:
            head = "optionally " + head
        return f"{head} when {'; '.join(parts)}" if parts else head


def _p(sutra, gives, **kwargs) -> Provision:
    return Provision(sutra, frozenset(gives), **kwargs)


#: गति alone, never उपसर्ग — the point of 1.4.60's yogavibhāga.
_GATI_ONLY = (G, N)
#: Both, since 1.4.59 gives one and 1.4.60's च adds the other.
_BOTH = (U, G, N)


PROVISIONS: Tuple[Provision, ...] = (
    # --- निपात, 1.4.57 and 1.4.58 ---------------------------------------
    _p("1.4.57", (N,), gana=cadi(), sattva=False,
       gloss="चादयोऽसत्त्वे — the चादि words, when they do not denote a "
             "substance. प्रसज्यप्रतिषेधोऽयम्, सत्त्वमिति द्रव्यमुच्यते",
       example="ca, vā, ha, aha, eva", counter="paśur vai puruṣaḥ"),
    _p("1.4.58", (N,), gana=pradi(), sattva=False,
       gloss="प्रादयः — and the twenty-two प्रादि words, असत्त्वे carrying down",
       example="pra, parā, apa, sam, anu"),

    # --- उपसर्ग and गति, 1.4.59 to 1.4.79 -------------------------------
    _p("1.4.59", _BOTH, gana=pradi(), kriya_yoga=True,
       gloss="उपसर्गाः क्रियायोगे — a प्रादि word construed with a verb is an "
             "उपसर्ग, and by 1.4.60's च a गति as well",
       example="praṇayati, pariṇayati", counter="pranāyako deśaḥ"),
    _p("1.4.61", _GATI_ONLY, gana=uryadi() + ("cvi", "ḍāc"), kriya_yoga=True,
       gloss="ऊर्यादिच्विडाचश्च — गति only, not उपसर्ग: that is what the "
             "yogavibhāga at 1.4.60 was for",
       example="ūrīkṛtya, śuklīkṛtya"),
    _p("1.4.62", _GATI_ONLY, kriya_yoga=True, anukarana=True,
       followed_by_iti=False,
       gloss="अनुकरणं चानितिपरम् — an imitative word, and not one followed by "
             "इति",
       example="khāṭkṛtya", counter="khāṭ iti kṛtvā"),
    _p("1.4.63", _GATI_ONLY, words=("sat", "asat"),
       senses=("ādara", "anādara"), kriya_yoga=True,
       gloss="आदरानादरयोः सदसती — सत् and असत्, in respect and disrespect",
       example="satkṛtya, asatkṛtya"),
    _p("1.4.64", _GATI_ONLY, words=("alam",), senses=("bhūṣaṇa",),
       kriya_yoga=True,
       gloss="भूषणेऽलम् — अलम् in the sense of adorning",
       example="alaṃkṛtya"),
    _p("1.4.65", _GATI_ONLY, words=("antar",), senses=("aparigraha",),
       kriya_yoga=True,
       gloss="अन्तरपरिग्रहे — अन्तर् in the sense of not accepting",
       example="antarhatya"),
    _p("1.4.66", _GATI_ONLY, words=("kaṇe", "manas"),
       senses=("śraddhāpratighāta",), kriya_yoga=True,
       gloss="कणेमनसी श्रद्धाप्रतीघाते — in the sense of appetite frustrated",
       example="kaṇehatya, manaskṛtya"),
    _p("1.4.67", _GATI_ONLY, words=("puras",), kriya_yoga=True,
       gloss="पुरोऽव्ययम् — पुरस्, being an indeclinable",
       example="puraskṛtya"),
    _p("1.4.68", _GATI_ONLY, words=("astam",), kriya_yoga=True,
       gloss="अस्तं च — and अस्तम्", example="astaṃgatya"),
    _p("1.4.69", _GATI_ONLY, words=("accha",), senses=("gatyarthavat",),
       kriya_yoga=True,
       gloss="अच्छ गत्यर्थवदेषु — अच्छ before verbs of going and वद्",
       example="acchagatya"),
    _p("1.4.70", _GATI_ONLY, words=("adas",), not_senses=("anupadeśa",),
       kriya_yoga=True,
       gloss="अदोऽनुपदेशे — अदस्, where no instruction is meant",
       example="adaḥkṛtya"),
    _p("1.4.71", _GATI_ONLY, words=("tiras",), senses=("antardhi",),
       kriya_yoga=True,
       gloss="तिरोऽन्तर्द्धौ — तिरस् in the sense of concealment",
       example="tirobhūya"),
    _p("1.4.72", _GATI_ONLY, words=("tiras",), with_kr=True, kriya_yoga=True,
       optional=True,
       gloss="विभाषा कृञि — and with कृ, optionally, whatever the sense",
       example="tiraskṛtya / tiraḥ kṛtvā"),
    _p("1.4.73", _GATI_ONLY, words=("upāje", "anvāje"), with_kr=True,
       kriya_yoga=True, optional=True,
       gloss="उपाजेऽन्वाजे — उपाजे and अन्वाजे with कृ, optionally",
       example="upājekṛtya / upāje kṛtvā"),
    _p("1.4.74", _GATI_ONLY, gana=sakshatprabhrti(), with_kr=True,
       kriya_yoga=True, optional=True,
       gloss="साक्षात्प्रभृतीनि च — and the साक्षात् group with कृ, optionally",
       example="sākṣātkṛtya / sākṣāt kṛtvā"),
    _p("1.4.75", _GATI_ONLY, words=("urasi", "manasi"),
       not_senses=("anatyādhāna",), with_kr=True, kriya_yoga=True,
       optional=True,
       gloss="अनत्याधान उरसिमनसी — उरसि and मनसि with कृ, where no placing "
             "upon is meant, optionally",
       example="urasikṛtya / urasi kṛtvā"),
    _p("1.4.76", _GATI_ONLY, words=("madhye", "pade", "nivacane"),
       with_kr=True, kriya_yoga=True, optional=True,
       gloss="मध्ये पदे निवचने च — and these three, optionally",
       example="madhyekṛtya / madhye kṛtvā"),
    _p("1.4.77", _GATI_ONLY, words=("haste", "pāṇau"),
       senses=("upayamana",), with_kr=True, kriya_yoga=True,
       gloss="नित्यं हस्ते पाणावुपयमने — हस्ते and पाणौ with कृ in the sense "
             "of marrying, and invariably: नित्यम् shuts out 1.4.72's option",
       example="hastekṛtya, pāṇikṛtya"),
    _p("1.4.78", _GATI_ONLY, words=("prādhvam",), senses=("bandhana",),
       with_kr=True, kriya_yoga=True,
       gloss="प्राध्वं बन्धने — प्राध्वम् with कृ in the sense of binding",
       example="prādhvaṃkṛtya"),
    _p("1.4.79", _GATI_ONLY, words=("jīvikā", "upaniṣad"),
       senses=("aupamya",), with_kr=True, kriya_yoga=True,
       gloss="जीविकोपनिषदावौपम्ये — these two with कृ, in comparison",
       example="jīvikākṛtya"),

    # --- कर्मप्रवचनीय, 1.4.84 to 1.4.98 ---------------------------------
    _p("1.4.84", (K, N), words=("anu",), senses=("lakṣaṇa",),
       kriya_yoga=False,
       gloss="अनुर्लक्षणे — अनु where it marks a sign",
       example="japam anu prāvarṣat"),
    _p("1.4.85", (K, N), words=("anu",), senses=("tṛtīyārtha",),
       kriya_yoga=False,
       gloss="तृतीयार्थे — and where it has the sense of the instrumental",
       example="nadīm anv avasitā senā"),
    _p("1.4.86", (K, N), words=("anu",), senses=("hīna",), kriya_yoga=False,
       gloss="हीने — and where inferiority is meant",
       example="anu hariṃ surāḥ"),
    _p("1.4.87", (K, N), words=("upa",), senses=("hīna", "adhika"),
       kriya_yoga=False,
       gloss="उपोऽधिके च — उप, where superiority is meant and inferiority too",
       example="upa khāryāṃ droṇaḥ"),
    _p("1.4.88", (K, N), words=("apa", "pari"), senses=("varjana",),
       kriya_yoga=False,
       gloss="अपपरी वर्जने — अप and परि in the sense of excluding",
       example="apa trigartebhyo vṛṣṭo devaḥ"),
    _p("1.4.89", (K, N), words=("āṅ",), senses=("maryādā",),
       kriya_yoga=False,
       gloss="आङ् मर्यादावचने — आङ् where a limit is stated. The vārttika "
             "आङ्मर्यादाभिविध्योः adds inclusion",
       example="ā pāṭaliputrād vṛṣṭo devaḥ"),
    _p("1.4.90", (K, N), words=("prati", "pari", "anu"),
       senses=("lakṣaṇa", "itthaṃbhūtākhyāna", "bhāga", "vīpsā"),
       kriya_yoga=False,
       gloss="लक्षणेत्थम्भूताख्यानभागवीप्सासु प्रतिपर्यनवः — three words "
             "against five senses, which is why 1.3.10 does *not* pair them "
             "off: समानामिति किम्?",
       example="vṛkṣaṃ prati vidyotate vidyut"),
    _p("1.4.91", (K, N), words=("abhi",), senses=("abhāga",),
       kriya_yoga=False,
       gloss="अभिरभागे — अभि, in those senses but not that of a share",
       example="abhy agniṃ śalabhāḥ patanti"),
    _p("1.4.92", (K, N), words=("prati",),
       senses=("pratinidhi", "pratidāna"), kriya_yoga=False,
       gloss="प्रतिः प्रतिनिधिप्रतिदानयोः — प्रति in substitution and requital",
       example="prati viṣṇum surāḥ"),
    _p("1.4.93", (K, N), words=("adhi", "pari"), senses=("anarthaka",),
       kriya_yoga=False,
       gloss="अधिपरी अनर्थकौ — अधि and परि, where they add no meaning",
       example="adhi hariḥ"),
    _p("1.4.94", (K, N), words=("su",), senses=("pūjā",), kriya_yoga=False,
       gloss="सुः पूजायाम् — सु in the sense of honouring",
       example="su madrān"),
    _p("1.4.95", (K, N), words=("ati",), senses=("pūjā", "atikramaṇa"),
       kriya_yoga=False,
       gloss="अतिरतिक्रमणे च — अति, in honouring and in overstepping",
       example="ati devān"),
    _p("1.4.96", (K, N), words=("api",),
       senses=("padārtha", "saṃbhāvanā", "anvavasarga", "garhā",
               "samuccaya"),
       kriya_yoga=False,
       gloss="अपिः पदार्थसम्भावनान्ववसर्गगर्हासमुच्चयेषु — अपि in these five",
       example="api siñcet sarasvatīm"),
    # 1.4.97 stands outside 1.4.56's range, which is what the range is for.
    _p("1.4.97", (K,), words=("adhi",), senses=("īśvara",),
       kriya_yoga=False,
       gloss="अधिरीश्वरे — अधि in the sense of a master. This is the sūtra "
             "1.4.56's प्राक् stops short of, so the निपात name does not come "
             "from that heading here — though अधि is प्रादि and so a निपात by "
             "1.4.58 in any case",
       example="adhi brahmadatte senāpatyam"),
    _p("1.4.98", (K,), words=("adhi",), with_kr=True, kriya_yoga=False,
       optional=True,
       gloss="विभाषा कृञि — and with कृ, optionally",
       example="adhi kṛtvā / adhikṛtya"),
)


# --- resolving -------------------------------------------------------------


@dataclass(frozen=True)
class Verdict:
    """Which names the word takes — a set, because they co-apply."""

    names: FrozenSet[Name]
    by: Tuple[str, ...]
    why: str
    optional: bool = False

    def has(self, name: Name) -> bool:
        return name in self.names


def _order(sutra: str) -> Tuple[int, ...]:
    return tuple(int(p) for p in sutra.split(".") if p.isdigit())


def in_nipata_range(sutra: str) -> bool:
    """Does 1.4.56's प्राग्रीश्वरात् reach this sūtra? To 1.4.96."""
    return _order(NIPATA_FROM) <= _order(sutra) <= _order(NIPATA_TO)


def classify(who: Particle) -> Verdict:
    """
    Which of the four names this word takes — 1.4.56 to 1.4.98.

    A set and not one name. These saṃjñās co-apply by design, and the pāda
    says so twice: 1.4.56 is cast as a range प्राग्वचनं संज्ञासमावेशार्थम्, and
    1.4.60's च is चकारः संज्ञासमावेशार्थः. So the results are unioned rather
    than resolved against each other.
    """
    matched = [p for p in PROVISIONS if p.applies(who)]
    if not matched:
        return Verdict(
            frozenset(), (),
            "Nothing in 1.4.56–1.4.98 reaches this word.",
        )

    names: set = set()
    cited_range = False
    for provision in matched:
        names |= set(provision.gives)
        # 1.4.56's range: whatever is named between 1.4.56 and 1.4.96 is also
        # a निपात, by the प्राक् formulation and not by any separate rule.
        if in_nipata_range(provision.sutra):
            names.add(N)
            cited_range = True

    latest = max(matched, key=lambda p: _order(p.sutra))
    # 1.4.56 and 1.4.83 give their names by *being ranges* and contribute no
    # provision of their own, so they would go uncited — leaving a reader
    # looking at three names and two sūtras and no way to see where the third
    # came from.
    sutras = {p.sutra for p in matched}
    if cited_range:
        sutras.add(NIPATA_FROM)
    if K in names:
        sutras.add(KARMAPRAVACANIYA_FROM)
    cited = tuple(sorted(sutras, key=_order))
    why = "; ".join(dict.fromkeys(p.gloss for p in matched))
    if len(names) > 1:
        why += (
            "\n\nThese stand together rather than one displacing the other. "
            "1.4.1 आ कडारादेका संज्ञा would allow one only, and the section "
            "is written to get round it: प्राग्वचनं संज्ञासमावेशार्थम् at "
            "1.4.56, चकारः संज्ञासमावेशार्थः at 1.4.60."
        )
    return Verdict(
        frozenset(names), cited, why,
        optional=any(p.optional for p in matched) and latest.optional,
    )


def names_of(
    form: str,
    *,
    kriya_yoga: bool = False,
    sattva: bool = False,
    sense: Optional[str] = None,
    with_kr: bool = False,
    chandas: bool = False,
    anukarana: bool = False,
    followed_by_iti: bool = False,
) -> Verdict:
    """Which names a word takes, given how it is being used."""
    return classify(Particle(
        form=form, kriya_yoga=kriya_yoga, sattva=sattva, sense=sense,
        with_kr=with_kr, chandas=chandas, anukarana=anukarana,
        followed_by_iti=followed_by_iti,
    ))


def placement(who: Particle) -> Tuple[str, str]:
    """
    1.4.80 to 1.4.82 — where an उपसर्ग or गति stands.

    ते प्राग्धातोः, before the root; and in the Veda it may follow (1.4.81
    छन्दसि परेऽपि) or stand apart from it (1.4.82 व्यवहिताश्च). The Kāśikā
    notes that ते is there for the उपसर्गs alone — तेग्रहणम् उपसर्गार्थम्,
    गतयो ह्यनन्तराः — since a गति is adjacent anyway.
    """
    if who.after_dhatu and not who.chandas:
        return ("1.4.80",
                "ते प्राग्धातोः — they stand before the root, and this one "
                "does not.")
    if who.after_dhatu:
        return ("1.4.81",
                "छन्दसि परेऽपि — in the Veda it may follow the root.")
    if who.separated and who.chandas:
        return ("1.4.82",
                "व्यवहिताश्च — and in the Veda it may stand apart from it.")
    return ("1.4.80", "ते प्राग्धातोः — before the root, as it should be.")


def provisions_for(sutra: str) -> Tuple[Provision, ...]:
    return tuple(p for p in PROVISIONS if p.sutra == sutra)


__all__ = [
    "KARMAPRAVACANIYA_FROM",
    "KARMAPRAVACANIYA_TO",
    "NIPATA_FROM",
    "NIPATA_TO",
    "Name",
    "PROVISIONS",
    "Particle",
    "Provision",
    "SENSES",
    "Verdict",
    "cadi",
    "classify",
    "in_nipata_range",
    "names_of",
    "placement",
    "pradi",
    "provisions_for",
    "sakshatprabhrti",
    "uryadi",
]
