# -*- coding: utf-8 -*-
"""
६.१.७७–८३ — इको यणचि, एचोऽयवायावः, वान्तो यि प्रत्यये and what goes with them;
and the consonant adjustments the yaṇ brings on: 8.2.23, 8.2.29, 8.4.46–54, 8.4.64.

**The vowel side (6.1.77–83).** Where a vowel meets a vowel and neither the
एकादेश rules of 6.1.84–111 nor a prakṛtibhāva rule gives the result, the first
vowel becomes a consonant (6.1.77) or, if it is an एच्, a vowel and a consonant
(6.1.78). 6.1.79 makes ओ and औ into अव् and आव् before a y-initial *affix* —
where no vowel follows for 6.1.78 to read — 6.1.80 narrows that for a dhātu's
own एच्, and 6.1.81–83 fix four (and, in the Veda, more) forms outright by
निपातन. Each rule is written from the sūtra and not from a table: 6.1.77 names
*iK* and *yaṆ*, and 1.1.50 स्थानेऽन्तरतमः chooses; 6.1.78 names *eC* and four
substitutes that pair off by 1.3.10 (`anga.ayadi` asks it), and 6.1.79's
*vānta* is those of the four that end in व्.

**What the letters cannot say is read from the word's flags** (NORTH_STAR §5),
and said here rather than guessed.

* **The affix.** 6.1.79–83 speak of a *pratyaya*. The parser already says what
  a `~` is — *two pieces of ONE pada, stem | affix* — so the piece after a `~`
  IS the affix, and `go~yam` is गव्यम् while `go-yānam` (a compound, `-`) is
  गोयानम्, the Kāśikā's counter-example *प्रत्यय इति किम्?*. Nothing else is asked
  of the piece but that it begin with य् (6.1.79: यकारादौ, by the vārttika
  यस्मिन्विधिस्तदादावल्ग्रहणे).
* `dhatu[:ROOT]` — the piece is a dhātu (6.1.80–83), and *which* root where a
  sūtra names roots (6.1.81 क्षि, जि; 6.1.82 क्री; 6.1.83 भी, वी).
* `tannimitta` — this एच् is the very one the y-initial affix has caused
  (6.1.80). A fact of the derivation that made the dhātu, given by the caller.
* `shakyartha`, `krayartha`, `adhvaparimana`, `stri` — the sense the nipātanas
  and the vārttika of 6.1.79 name; the letters of *kṣe + ya* do not say whether
  the word means *able to be destroyed* or *fit to be destroyed*.
* `pluta` — the word ends in a pluta vowel (the Kāśikā's vārttika on 6.1.77).
* `abhyasa` — the piece is the reduplicate 8.4.54 works on; the engine builds no
  reduplicate, so the caller gives it as the piece before a `~`.
* the engine's `veda` flag opens the Vedic rules (6.1.83 and the vārttikas).

Of these, `tannimitta`, `shakyartha`, `krayartha`, `adhvaparimana`, `stri` and
`abhyasa` are new words for the flag vocabulary the README lists (listed in
`core_requests`); `pluta`, `nipata` and `dhatu:ROOT` are there already.

**The consonant side (8.2.23, 8.2.29, 8.4.46–54, 8.4.64)** is what the Laghu
sets out for सुधी + उपास्य:

    सुध्य् उपास्य — 6.1.77;   8.2.23 would now take off the य्, ‘इति यलोपे
    प्राप्ते’ — यणः प्रतिषेधो वाच्यः;   8.4.47 doubles the ध्;   8.4.53 makes the
    first ध् a द् —  सुद्ध्युपास्य.

*How each is modelled, and why.*

1. **The vārttika यणः प्रतिषेधो वाच्यः is a refusal**: a rule of its own, with
   `authority=VARTTIKA`, that stands at the *same site* as 8.2.23 and wins it by
   `overrides` (as 8.4.44 refuses 8.4.40). It names the loss it forbids in its own
   step (`Via` 1.1.52: the y is the last sound of the cluster, and it is that
   which 8.2.23 would have taken). Take the rule away and the य् goes, and the ध्,
   now a pada's last sound, is voiced by 8.2.39 — सुदुपास्य; there is a test. **OPEN:** the Bālamanoramā says this vārttika was rejected in the
   Bhāṣya (*इदं वार्तिकमाकरे प्रत्याख्यातम्*) and the Kāśikā reaches the same result
   by another road — *यणादेशस्य बहिरङ्गलक्षणस्यासिद्धत्वात्* (the yaṇ, caused by what
   follows the word, is asiddha to the cluster-rule, which rests on the word alone).
   The Tattvabodhinī gives both. The Laghu and the Kaumudī use the vārttika, so
   the engine does; the result is the same. The vārttika is read as it is worded
   — a yaṇ ending a pada-final cluster is not lost — and it does not need a
   repha before (8.2.24 रात्सस्य keeps 8.2.23 off a cluster with a र् before its
   last sound unless that sound is स्, so *hary* and *gaur* never reach it).
   8.2.29 (the same cluster's *first* sound, स् or क्) has no vārttika and only the
   Kāśikā's road (*वास्यर्थम्, काक्यर्थम्*), so its refusal is 8.2.29's own
   application and says so. Both are made for any yaṇ that ends the cluster —
   one 6.1.77 has just put in, or one the caller gave as the end of a pada: a
   finished pada has no other way to end in a cluster with a yaṇ in it.
2. **Which clusters 8.2.23 and 8.2.29 read.** Both act at the END of a piece: the
   last cluster of a word is where a pada's end lives, exactly as 8.2.39 reads
   the last sound. So they read the final cluster of any word the engine is
   given — *gomānt* → गोमान् — and never the inside of a word (*gacchati* keeps its
   च्छ्). The two contend for that cluster, and 8.2.29 wins: the Bālamanoramā
   says *न्याय्यत्वादिह संयोगादिलोप एव भवति* (it is the loss of the first sound that
   happens, though the loss of the last would give the same form for भृस्ज्).
   8.2.29's second place — *before a झल्* — is the cluster that ends a piece
   whose next piece begins with one (*takṣ~ta*). A cluster with a र् before its
   last sound is left to 8.2.24, which is not in this family: the niyama is read
   here as a condition of 8.2.23 (ऊर्ज्, not *ऊर्*).
3. **Doubling (8.4.46, 8.4.47, the vārttika यणो मयो द्वे वाच्ये).** The words the
   engine is given are finished, so the doubled sound is offered only where the
   yaṇ that 6.1.77 has just put in *made the condition true*: the sound before
   it, which stood before a vowel (so 8.4.47's *na tu aci* was false) and now
   stands before a consonant, and the yaṇ itself, which stands after a र् or ह्
   (8.4.46) or after a मय् (the vārttika). दद्ध्यत्र, मद्ध्वत्र, हर्य्यनुभवः, गौर्य्यौ
   are all of that shape. The interior doubling of finished words (अर्क्कः,
   ब्रह्म्मा, पुत्त्रादिनी, कर्षति), the doubling across a plain junction (दुर्ल्लभः,
   कुर्म्मः) and the head of a longer cluster (*bhakty*'s क्) are not opened,
   and 8.4.48–49, which refuse exactly those, are marked SCOPE for that reason.
   The र् and ह् of 8.4.46 are never doubled themselves: the sūtra names them as
   the *cause*, and *श्रुतानुमितयोः श्रुतं बलीयः* (Bālamanoramā on 8.4.46, quoted
   by the Tattvabodhinī on 8.2.23: *रेफस्य कार्यित्वबाधनात्*) keeps them from being
   the doubled *sthānin* too — हर्य् य्, धात् र्, and not *हर्र्य्*.
4. **Doubling is optional, and the option is the teachers'.** The Kāśikā words
   8.4.46 and 8.4.47 unconditionally (*द्वे भवतः*) and then gives three
   sūtras of *opinion* — 8.4.50 (Śākaṭāyana: none in a cluster of three or more),
   8.4.51 (Śākalya: none anywhere) and 8.4.52 (the ācāryas: none after a long
   vowel). The Kaumudī and the Tattvabodhinī read *vā* down into 8.4.46–47 and call
   the three sūtras idle (*नारम्भणीयम्*). Both readings yield the same forms, and the
   engine takes the Kāśikā's structure: **the doubling is unconditional, and 8.4.51
   is an optional refusal that displaces it** — so the derivation that follows the
   option (Śākalya, no doubling) comes first, and *ityādi* stays the first form of
   *iti ādi*, as the README has it, with *ittyādi* the second. The union of what any
   teacher allows is *both forms everywhere*: Śākalya's "everywhere" already
   contains the other two teachers' domains, so 8.4.50 and 8.4.52 are not separate
   forks (each would only repeat the same undoubled form under another name);
   where their own domain also holds, they are cited in the step of 8.4.51
   (`Via`) and marked *partial*. The three-consonant count is of the conjunct the
   word HAS: a sound the doubling itself added is not counted towards it. It is an
   option of *opinion* (मतभेद), not a विभाषा of either the 1.3.43 or the 1.3.50 kind
   (the Kaumudī's *vā* read down into 8.4.46–47 would be an अप्राप्तविभाषा — nothing
   else gives the doubling — and gives the same two courses).
   The vārttika *यणो मयो द्वे* lets the yaṇ itself be doubled after a may — both
   readings of *यणो मयः* are in the Kāśikā, and the engine takes the one that
   gives दध्य्यत्र, मध्व्वत्र, which is the one the Kaumudī counts (*तदिह
   धकारयकारयोर्द्वित्वविकल्पाच्चत्वारि रूपाणि*). Its option is offered only once
   8.4.47's own is settled at that place, so the two are independent and all four
   forms result. 8.4.64 then lets the first of two yams after a hal be lost
   (*अन्यतरस्याम्* — an अप्राप्तविभाषा, since nothing else gives that loss), each
   yam before the yam of its own kind (यथासंख्यम्, 1.3.10: *माहात्म्य* keeps its म्).
   **OPEN:** how many forms *sudhy upāsya* has. The Kaumudī counts four (the ध् and
   the य् each doubled or not); the Tattvabodhinī defends more, since the द् that
   8.4.53 makes of the first ध् is a new sound that could be doubled again
   (*पूर्वत्रासिद्धीयमद्वित्वे*), and the Prauḍhamanoramā rejects that. The engine
   gives the Kaumudī's four: a doubling needs a vowel before the sound doubled,
   and after 8.4.53 there is a consonant.
5. **8.4.54 अभ्यासे चर्च** acts on a reduplicate, which the engine does not build:
   the caller gives the piece that is the अभ्यास, flagged `abhyasa`, before a `~`
   (*bhu~bhūṣati*), and what its aspirate becomes is asked of `anga.abhyase_car`,
   not of 1.1.50 (whose nearest of चर् and जश् to थ् is स्). Without the flag
   *bha~bhūva* is a stem and a stem, and nothing happens.
6. **The Laghu as it stands on disk drops letters** — *maddhariḥ* for
   *मद्ध्वरिः* and *dhātraśaḥ* for *धात्रंशः* (the Kaumudī on 8.2.23 has both
   whole). The tests use the Kaumudī's forms.
   The same Laghu prints *(न समासे) वाप्यश्वः* beside 8.4.46. The Kaumudī has
   that vārttika under 6.1.127 (there it forbids Śākalya's shortening in a
   compound, and the Bālamanoramā on 8.2.23 uses it so: *इकोऽसवर्ण इत्यपि न, न
   समासे इति तन्निषेधात्*), and no source on disk says it forbids a doubling. So
   it is NOT a rule here, and *vāpī-aśva* is derived like any other yaṇ. Listed
   as OPEN.

**What this module does not do** is in `COVERAGE`, sūtra by sūtra, with a reason.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, Iterator, List, Optional, Tuple

from src.astadhyayi.adesa import raparatva, LVARNA, RVARNA
from src.astadhyayi.anga import (
    AYAV, abhyase_car, ayadi, ec, jhalam_jas_jhasi as _jhalam_jas_jhasi)
from src.astadhyayi.reading import yathasamkhya
from src.astadhyayi.sandhi import supports as S
from src.astadhyayi.sandhi.parse import tokenize
from src.astadhyayi.sandhi.rule import (
    sk,
    ADESA, DVITVA, LOPA, PRATISEDHA, VARTTIKA, Application, Detail, NewSeg,
    Via, delete, replace, rule, site)
from src.astadhyayi.sandhi.segs import ANGA, PRAKRTYA, WITHIN, Sight, View
from src.astadhyayi.sivasutra import resolve
from src.astadhyayi.svara import is_dirgha
from src.astadhyayi.varna import savarna

# ---------------------------------------------------------------------------
# Words the sūtras name, and vārttikas, verbatim from the corpus or a commentary
# ---------------------------------------------------------------------------

#: The step whose product the doubling rules stand beside.
YAN = "6.1.77"

#: The nipātana rules' and the vārttikas' own step, as `Seg.made_by` records it.
VANTA_STEP = "6.1.79"

#: The two steps that say a sound twice.
DOUBLING = ("8.4.46", "8.4.47")

#: 8.4.46's own cause — *र* and *ह*, named in the sūtra (रहाभ्याम्) — which are
#: never themselves the doubled sound.
RAHA = ("r", "h")

#: 8.2.29's two — *स्* and *क्*, named in the sūtra (स्कोः).
SA_KA = ("s", "k")

#: The roots the nipātanas name (Kāśikā on 6.1.81–83).
ROOTS_6_1_81 = ("kṣi", "ji")
ROOT_6_1_82 = "krī"
ROOTS_6_1_83 = ("bhī", "vī")
ROOT_PRA_VI = "vī"
#: The two stems the vārttikas of 6.1.83 name (Bhāṣya: *शरस्य च ह्रदस्य च अतः
#: अव् वक्तव्यः*), and the two spellings the Kāśikā and Kaumudī give of the other.
STEMS_AV = ("śara", "hrada")
FORMS_HRADAYYA = ("hrade", "hṛde")
#: 6.1.79's vārttikas name the word *yūti*.
WORD_YUTI = "yūti"

VT_PLUTA = "इकः प्लुतपूर्वस्य सवर्णदीर्घबाधनार्थं यणादेशो वक्तव्यः"
VT_GOR_YUTAU = "गोर्यूतौ च्छन्दस्युपसंख्यानम् ।"
VT_ADHVA = "अध्वपरिमाणे च ।"
VT_HRADAYYA = "हृदय्या उपसंख्यानम् ।"
VT_ARSA = "शरस्य च अवादेशो भवतीति वक्तव्यम् ।"
VT_YANAH = "यणः प्रतिषेधो वाच्यः ।"
VT_MAYO = "यणो मयो द्वे वाच्ये ।"

#: Not a vārttika: the Kaumudī's reading of 6.1.79's word *vānta* — the ādeśa
#: has a v that is heard. It names the rule below, which is 6.1.79's own.
GLOSS_V_NOT_LOST = ("श्रूयमाणवकारान्त आदेशः स्यात् । वकारो न लुप्यत इति यावत्")

# ---------------------------------------------------------------------------
# The tradition's words, each checked against the corpus by the tests. A reason
# in `overrides` is built from these and from nothing else.
# ---------------------------------------------------------------------------

#: name -> (sūtra, work, quote): every quote must be a substring of that
#: commentary (the work is a key of `corpus.COMMENTARIES`).
SOURCES: Dict[str, Tuple[str, str, str]] = {
    "pluta": ("6.1.77", "kashika", VT_PLUTA),
    "pluta_hold": ("6.1.77", "padamanjari",
                   "तस्य प्रकृतिभावे प्राप्ते यण्विधीयते"),
    "gor_yutau": ("6.1.79", "kashika", "गोर्यूतौ छन्दसि"),
    "gor_yutau_sk": ("6.1.79", "kaumudi", "गोर्यूतौ छन्दस्युपसङ्ख्यानम्"),
    "v_heard": ("6.1.79", "kaumudi", GLOSS_V_NOT_LOST),
    "tannimitta": ("6.1.80", "kaumudi",
                   "यादौ प्रत्यये परे धातोरेचश्चेद्वान्तादेशस्तर्हि "
                   "तन्निमित्तस्यैव नान्यस्य"),
    "tannimitta_k": ("6.1.80", "kashika",
                     "तन्निमित्तस्य हि धातोश्चाधातोश्च भवति"),
    "dhatoriti": ("6.1.80", "kashika",
                  "धातोरिति किम् ? प्रातिपदिकस्य नियमो मा भूत्"),
    "yalope": ("8.2.23", "kaumudi", "इति यलोपे प्राप्ते"),
    "yanah": ("8.2.23", "kaumudi", "यणः प्रतिषेधो वाच्यः"),
    "bahiranga_23": ("8.2.23", "kashika",
                     "दध्यत्र, मध्वत्रेत्यत्र तु यणादेशस्य बहिरङ्गलक्षणस्यासिद्धत्वात् "
                     "संयोगान्तलोपो न भवति"),
    "four_forms": ("8.2.23", "kaumudi",
                   "तदिह धकारयकारयोर्द्वित्वविकल्पाच्चत्वारि रूपाणि"),
    "rutva_later": ("8.2.23", "kashika",
                    "इह श्रेयान्, भूयानिति रुत्वं परमप्यसिद्धत्वात् "
                    "संयोगान्तस्य लोपं न बाधते"),
    "ratsasya": ("8.2.24", "kashika", "रात् सस्यैव लोपो भवति, नान्यस्येति"),
    "skoh": ("8.2.29", "kashika",
             "पदस्यान्ते यः संयोगः, झलि परतो वा यः संयोगः, "
             "तदाद्योः सकारककारयोर्लोपो भवति"),
    "bahiranga_29": ("8.2.29", "kashika",
                     "वास्यर्थम्, काक्यर्थम् इत्यत्रापि बहिरङ्गलक्षणस्य "
                     "यणादेशस्यासिद्धत्वात् संयोगादिलोपो न भवति"),
    "nyayya": ("8.2.29", "balamanorama",
               "तथापि न्याय्यत्वादिह संयोगादिलोप एव भवति"),
    "raha_cause": ("8.4.46", "balamanorama",
                   "द्वित्वप्रकरणे रहाभ्यामिति रेफत्वेन हकारत्वेन च साक्षाच्छतेन "
                   "निमित्तभावेन तयोर्यर्शब्दबोधितकार्यभाक्त्वबाधात्"),
    "anaci": ("8.4.47", "kashika", "अनच्परस्य अच उत्तरस्य यरो द्वे भवतः"),
    "mayo": ("8.4.47", "kashika", "यणो मयो द्वे भवत इति वक्तव्यम्"),
    "mayo_reading": ("8.4.47", "kashika",
                     "अपरे तु यण इति षष्ठी मय इति पञ्चमीति। तेषां दध्य्यत्र, "
                     "मध्व्वत्रेत्युदाहरणम्"),
    "sakatayana": ("8.4.50", "kashika",
                   "त्रिप्रभृतिषु वर्णेषु संयुक्तेषु शाकटायनस्याचार्यस्य मतेन "
                   "द्वित्वं न भवति"),
    "sakalya": ("8.4.51", "kashika",
                "शाकल्यस्याचार्यस्य मतेन सर्वत्र द्विर्वचनं न भवति"),
    "acaryas": ("8.4.52", "kashika",
                "दीर्घादुत्तरस्याचार्याणां मतेन न द्वित्वं भवति"),
    "yamam": ("8.4.64", "kashika",
              "हल उत्तरेषां यमां यमि परतो लोपो भवत्यन्यतरस्याम्"),
    "yamam_yathasamkhya": ("8.4.64", "kaumudi",
                           "यमां यमीति यथासङ्ख्यविज्ञानान्नेह । माहात्म्यम्"),
}


def _quote(name: str) -> str:
    """The verbatim quotation this module holds under `name`."""
    return SOURCES[name][2]


# ---------------------------------------------------------------------------
# Vias the core does not yet carry — added here, as the task allows
# ---------------------------------------------------------------------------


def uran_raparah(sthanin: str, substitute: str) -> Via:
    """
    1.1.51 उरण् रपरः, cited for what it does NOT do here: an aṇ put in the
    place of ṛ is followed by r (guṇa अर्, vṛddhi आर्), and by the vārttika an
    aṇ for ḷ by l — but the substitute of 6.1.77 is a *yaṇ*, not an aṇ, so
    nothing is added: धातृ + अंशः is धात्रंशः, not *धात्र्रंशः*.
    """
    added = raparatva(sthanin, "a")[1:]
    return Via(
        "1.1.51",
        f"{sk(sthanin)} is put right, so this would add {sk(added)} after an "
        f"{{aṇ}} substituted for it (guṇa {{ar}}) — but the substitute here is "
        f"the {{yaṇ}} {sk(substitute)}, not an {{aṇ}}, so nothing is added")


# ---------------------------------------------------------------------------
# Small readers
# ---------------------------------------------------------------------------


def _sounds(text: str) -> Tuple[str, ...]:
    return tuple(sound for sound, _ in tokenize(text))


@lru_cache(maxsize=None)
def _pairing() -> Dict[str, str]:
    """Each एच् with the substitute 6.1.78 gives it — 1.3.10 pairs the lists."""
    return dict(yathasamkhya(ec(), AYAV) or ())


@lru_cache(maxsize=None)
def _vanta() -> Dict[str, str]:
    """The substitutes 6.1.78 names that END IN व् (*वान्त*), each with the एच्
    it goes with — ओ → अव्, औ → आव्. Nothing is listed: they are the
    pairing 1.3.10 makes, cut by the sūtra's own word."""
    return {sthanin: sub for sthanin, sub in _pairing().items()
            if sub.endswith("v")}


@lru_cache(maxsize=None)
def _ay_sthanin() -> Tuple[str, str]:
    """The एच् that 1.3.10 pairs with अय् — the एकार the nipātanas name — and
    the substitute."""
    sub = AYAV[0]
    return next(e for e, s in _pairing().items() if s == sub), sub


@lru_cache(maxsize=None)
def _yam_pairing() -> Dict[str, str]:
    """8.4.64's *यमां यमि*, read यथासंख्यम् (1.3.10): each यम् is lost before the
    यम् in its own place in the list — the sound of its own kind."""
    yams = resolve("yaM").sounds
    return dict(yathasamkhya(yams, yams) or ())


def _root(v: View, sight: Sight) -> Optional[str]:
    """The root a word is flagged as, `dhatu:ROOT`, or None."""
    return v.word(sight).flag_value("dhatu")


def _is_dhatu(v: View, sight: Sight) -> bool:
    return v.word(sight).has("dhatu") or _root(v, sight) is not None


def _has_flag(v: View, sights: Tuple[Sight, ...], flag: str) -> bool:
    return any(v.word(s).has(flag) for s in sights)


def _refused(v: View, sutra: str, where: Tuple[int, ...]) -> bool:
    """
    Whether the engine has recorded `sutra` as refused at `where`.

    The one place this module reads the engine's own bookkeeping rather than a
    sound: the vārttika यणो मयो द्वे is offered only once 8.4.47's doubling of
    the same sounds is settled, and a refusal leaves no trace in the sounds.
    (Listed in `core_requests`: a View method would be cleaner.)
    """
    return (sutra, where) in v.state.declined


# ---------------------------------------------------------------------------
# 6.1.77 इको यणचि
# ---------------------------------------------------------------------------


def _yan_application(left: Sight, right: Sight, *, extra_via=(), because="",
                     authority: str = "sūtra", varttika: str = ""
                     ) -> Optional[Application]:
    sub = S.nearest(left.s, resolve("yaṆ").sounds)
    if sub is None:
        return None
    marks = frozenset({"anunāsika"}) if left.seg.nasal else frozenset()
    via = [S.saptami_purva(f"{{aC}} {sk(right.s)}"),
           S.antaratama(left.s, sub, "{yaṇ} (y, v, r, l)")]
    if S.long_form_used(left.s, "iK"):
        via.insert(0, S.varna_grahana(left.s, "iK"))
    if left.s in RVARNA or left.s in LVARNA:
        via.append(uran_raparah(left.s, sub))
    via.extend(extra_via)
    return Application(
        site=site(left, right),
        edits=(replace(left, NewSeg(sub, marks)),),
        detail=Detail(
            kind=ADESA, sthanin=left.s, adesa=sub,
            nimitta=f"the vowel {sk(right.s)} follows",
            because=(f"{sk(left.s)} is an {{ik}} and {sk(right.s)} is an {{aC}}, "
                     f"so {{ik}} {sk(left.s)} is replaced by {{yaṇ}} {sk(sub)}"
                     + because),
            via=tuple(via), authority=authority, varttika=varttika))


@rule("6.1.77", name="इको यणचि", families=("ac", "yan"))
def iko_yanaci(v: View):
    """इकः स्थाने यण् स्यादचि संहितायाम् — दध्यत्र, मध्वत्र, कर्त्रर्थम्, लाकृतिः."""
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        if not S.is_member(left.s, "iK"):
            continue
        app = _yan_application(left, right)
        if app is not None:
            yield app


@rule("6.1.77", name="इको यणचि (प्लुतपूर्वस्येकः)", families=("ac", "yan"),
      authority=VARTTIKA, varttika=VT_PLUTA,
      overrides=(
          ("6.1.101", "सवर्णदीर्घस्यापवादः — the Kāśikā gives this vārttika "
                      "to keep the two alike vowels from joining: "
                      + _quote("pluta")),
          ("6.1.77", "the same substitution, stated once more for this case: "
                     + _quote("pluta"))))
def plutapurvasya(v: View):
    """
    इकः प्लुतपूर्वस्य सवर्णदीर्घबाधनार्थं यणादेशो वक्तव्यः — भो३ इ इन्द्रम् ⟶ भो३यिन्द्रम्.

    An इक् standing after a *pluta* vowel takes the yaṇ where 6.1.101 would
    otherwise join it to an alike vowel, and where its own hold from sandhi
    (it is a pragṛhya nipāta; 6.1.125, the prakṛtibhāva family's) would otherwise
    keep it as it is — *तस्य प्रकृतिभावे प्राप्ते यण्विधीयते* (Padamañjarī). The
    vārttika is why this rule may take up a vowel another rule has marked as
    held (`PRAKRTYA`) and put the yaṇ in its place; the hold is not put back on
    the consonant. It does NOT declare 6.1.125 among what it overrides: that
    would displace the hold of the pluta vowel too, which stands in the same
    group of sounds and which nothing else protects from 6.1.78. The hold, made
    first (it stands later than 6.1.77 and 1.4.2 gives it the place), is what
    this rule then lifts. Whether the vowel before is pluta is a fact about the word
    (`pluta`, given by the caller); the letters cannot say it
    (`bho{pluta} i indra`). The pluta vowel itself is held by 6.1.125, which is
    the prakṛtibhāva family's, and takes no part here.

    Where the इक् is neither held nor alike to the vowel after it, the ordinary
    6.1.77 does the whole work and the vārttika adds nothing, so it is not cited.
    """
    for j in v.pairs():
        left, right = j.left, j.right
        if not (left.is_vowel and right.is_vowel) or PRAKRTYA in right.marks:
            continue
        if not S.is_member(left.s, "iK"):
            continue
        prev = v.prev(left)
        if prev is None or not prev.is_vowel or not v.ends_word(prev) \
                or not v.word(prev).has("pluta"):
            continue
        held = PRAKRTYA in left.marks
        alike = savarna(left.s, right.s)
        if not (held or alike):
            continue
        extra = []
        why = []
        if alike:
            extra.append(S.savarna_of(left.s, right.s))
            why.append(f"{sk(right.s)} is savarṇa to it, which would give "
                       f"6.1.101's long vowel")
        if held:
            extra.append(Via(
                "6.1.125",
                f"the {{ik}} {sk(left.s)} is a pragṛhya vowel, held from sandhi "
                f"before a vowel; the vārttika lifts that hold and the yaṇ "
                f"stands in its place ({_quote('pluta_hold')}, Padamañjarī)"))
            why.append(f"{sk(left.s)} is held as a pragṛhya vowel")
        app = _yan_application(
            left, right, authority=VARTTIKA, varttika=VT_PLUTA,
            extra_via=tuple(extra),
            because=(f" — although {' and '.join(why)}, because the {{ik}} stands "
                     f"after the pluta vowel {sk(prev.s)}"))
        if app is not None:
            yield app


# ---------------------------------------------------------------------------
# 6.1.78 एचोऽयवायावः
# ---------------------------------------------------------------------------


@rule("6.1.78", name="एचोऽयवायावः", families=("ac", "ayavayav"))
def eco_yavayavah(v: View):
    """एचोऽयवायावः — ए, ओ, ऐ, औ become अय्, अव्, आय्, आव् before a vowel."""
    for j in v.vowel_pairs():
        left, right = j.left, j.right
        got = ayadi(left.s)
        if got.result is None:
            continue
        sub = got.result
        yield Application(
            site=site(left, right),
            edits=(replace(left, *_sounds(sub)),),
            detail=Detail(
                kind=ADESA, sthanin=left.s, adesa=sub,
                nimitta=f"the vowel {sk(right.s)} follows",
                because=(f"{sk(left.s)} is an {{eC}} and {sk(right.s)} is an {{aC}}, "
                         f"so {sk(left.s)} becomes {sk(sub)}"),
                via=(S.saptami_purva(f"{{aC}} {sk(right.s)}"),
                     S.pratyahara("eC", "e, o, ai, au"),
                     S.yathasamkhya("e, o, ai, au", "ay, av, āy, āv"))))


# ---------------------------------------------------------------------------
# 6.1.79–83 — the एच् before a y-initial affix, where there is no vowel to read
# ---------------------------------------------------------------------------


def _ec_before_y(v: View) -> Iterator[Tuple[Sight, Sight, str]]:
    """(the एच्, the य् after it, the boundary) where an एच् ends a piece and
    the next piece begins with य् — 6.1.79's *यि*, read as *यकारादौ* by the
    vārttika यस्मिन्विधिस्तदादावल्ग्रहणे."""
    for j in v.pairs():
        left, right = j.left, j.right
        if right.s != "y" or j.kind == WITHIN:
            continue
        if not v.ends_word(left) or not v.begins_word(right):
            continue
        yield left, right, j.kind


def _vanta_application(left: Sight, right: Sight, sub: str, *,
                       because: str, extra_via=(), authority: str = "sūtra",
                       varttika: str = "", nimitta: str = "",
                       note: str = "") -> Application:
    return Application(
        site=site(left, right),
        edits=(replace(left, *_sounds(sub)),),
        detail=Detail(
            kind=ADESA, sthanin=left.s, adesa=sub,
            nimitta=nimitta or f"the y-initial {{pratyaya}} follows",
            because=because,
            via=(S.saptami_purva(f"{sk(right.s)}, first sound of the affix"),
                 S.pratyahara("eC", "e, o, ai, au"),
                 S.yathasamkhya("o, au", "av, āv")) + tuple(extra_via),
            authority=authority, varttika=varttika, note=note))


def _vanta_candidates(v: View) -> Iterator[Tuple[Sight, Sight, str]]:
    """Where 6.1.79 reaches, before 6.1.80 has narrowed it: an ओ or औ ending a
    piece, and an affix beginning with य् next. **The affix is what a `~`
    says** (the module docstring): गोयानम्, with a `-`, has the same letters and
    no affix."""
    vanta = _vanta()
    for left, right, kind in _ec_before_y(v):
        if left.s in vanta and kind == ANGA:
            yield left, right, vanta[left.s]


@rule("6.1.79", name="वान्तो यि प्रत्यये", families=("ac", "ayavayav"))
def vanto_yi_pratyaye(v: View):
    """
    यकारादौ प्रत्यये परे ओदौतोरव् आव् एतौ स्तः — गव्यम्, नाव्यम्, बाभ्रव्यः, शङ्कव्यम्.

    The affix is the piece after a `~` (a pratyaya is a piece of one pada, not a
    word of its own). गोभ्याम् (no य्), रयति/रैयति (an ऐ, not ओ or औ) and
    गोयानम् (a compound, no affix) are left alone. A dhātu's own एच् is
    narrowed by 6.1.80, which stands at this same place; where the dhātu's एच्
    is the very one the affix caused the step says so.
    """
    for left, right, sub in _vanta_candidates(v):
        via = ()
        if _is_dhatu(v, left):
            via = (Via("6.1.80",
                       f"{sk(left.s)} ends a dhātu and is the very {{eC}} the affix "
                       f"has caused ({{tannimitta}}), the one case of a dhātu's "
                       f"that the niyama leaves to 6.1.79"),)
        yield _vanta_application(
            left, right, sub, extra_via=via,
            because=(f"{sk(left.s)} is the {{eC}} ending its piece and the "
                     f"{{pratyaya}} beginning with {sk('y')} follows, so it "
                     f"becomes the {{vānta}} {sk(sub)}"))


def _is_go(v: View, sight: Sight) -> bool:
    word = v.word(sight)
    return word.text == "go" or word.flag_value("stem") == "go"


def _is_yuti(v: View, sight: Sight) -> bool:
    word = v.word(sight)
    return word.text.startswith(WORD_YUTI) or \
        word.flag_value("stem") == WORD_YUTI


def _go_yuti(v: View) -> Iterator[Tuple[Sight, Sight, str]]:
    """The place both vārttikas of 6.1.79 name: the ओ of *go* before the word
    *yūti*, which is no pratyaya (यूतिशब्दस्य प्रत्ययत्वाभावात्, Bālamanoramā), so
    the sūtra cannot reach it."""
    vanta = _vanta()
    for left, right, kind in _ec_before_y(v):
        if left.s in vanta and kind != WITHIN and _is_go(v, left) \
                and _is_yuti(v, right):
            yield left, right, vanta[left.s]


@rule("6.1.79", name="वान्तो यि प्रत्यये (गोर्यूतौ छन्दसि)",
      families=("ac", "ayavayav"), vedic=True, authority=VARTTIKA,
      varttika=VT_GOR_YUTAU)
def gor_yutau_chandasi(v: View):
    """
    गोर्यूतौ छन्दस्युपसङ्ख्यानम् — आ नो मित्रावरुणा घृतैर्गव्यूतिमुक्षतम्.

    The ओ of *go* takes 6.1.79's substitute before the word *yūti* — which is no
    pratyaya (यूतिशब्दस्य प्रत्ययत्वाभावात्, Bālamanoramā), so the sūtra cannot
    reach it — in the Veda. The word is the vārttika's own, and read from the
    letters of the piece; the wider vārttika below (*अध्वपरिमाणे च*) gives the
    same form in the language too, and takes the place of this one where its
    sense is given.
    """
    for left, right, sub in _go_yuti(v):
        if _has_flag(v, (left, right), "adhvaparimana"):
            continue                    # the laukika vārttika covers it
        yield _vanta_application(
            left, right, sub, authority=VARTTIKA, varttika=VT_GOR_YUTAU,
            nimitta="the word yūti follows, in the Veda",
            because=(f"{sk(left.s)} ends {sk('go')} and the word {sk('yūti')} "
                     f"follows in the Veda, so it becomes {sk(sub)} — gavyūti"),
            note=(_quote("gor_yutau_sk") + " (Kaumudī); "
                  + _quote("gor_yutau") + " (Kāśikā)"))


@rule("6.1.79", name="वान्तो यि प्रत्यये (अध्वपरिमाणे च)",
      families=("ac", "ayavayav"), authority=VARTTIKA, varttika=VT_ADHVA)
def adhvaparimane_ca(v: View):
    """
    अध्वपरिमाणे च — गव्यूतिः, a measure of road; in the language as well as
    the Veda (लोकेऽपि प्राप्त्यर्थमिदम्, Bālamanoramā).

    The sense is a semantic condition, given as the flag `adhvaparimana` on
    either piece; the letters cannot say it.
    """
    for left, right, sub in _go_yuti(v):
        if not _has_flag(v, (left, right), "adhvaparimana"):
            continue
        yield _vanta_application(
            left, right, sub, authority=VARTTIKA, varttika=VT_ADHVA,
            nimitta="the word yūti follows, in the sense of a measure of road",
            because=(f"{sk(left.s)} ends {sk('go')} and the word {sk('yūti')} "
                     f"follows in the sense of a measure of road, so it becomes "
                     f"{sk(sub)} — gavyūti"))


@rule("6.1.79", name="वान्तो यि प्रत्यये (श्रूयमाणवकारान्तः)",
      families=("ac", "ayavayav"), varttika=GLOSS_V_NOT_LOST,
      overrides=(("8.3.19", "the ādeśa has a v that is heard, and "
                            + _quote("v_heard")),))
def sruyamana_vakaranta(v: View):
    """
    श्रूयमाणवकारान्त आदेशः स्यात् । वकारो न लुप्यत इति यावत् (Kaumudī on 6.1.79).

    The v that 6.1.79 puts in is not lost. Where it ends a pada — the first
    member of a compound, *go-yūti* — 8.3.19 लोपः शाकल्यस्य would otherwise
    offer to drop it (गयूतिः) since a य् follows; the Kaumudī reads the sūtra's
    word *vānta* (read with a v standing before it, a prasleṣa) so that the
    ādeśa is one whose v is *heard*, and says what that comes to: the v is not
    lost. It is a reading of 6.1.79's own word, not a vārttika — so the rule
    stays a sūtra's, and `varttika` here only keeps its key apart from the
    sūtra's.

    A refusal: no edits, the same site as the rule it refuses (8.3.19 reads the
    a before, the v and the sound after), and it wins by `overrides`. Made only
    where 8.3.19 would be offered — a pada-final v the ādeśa made, after an
    अ or आ and before an अश्. The Bālamanoramā names 8.3.22 हलि सर्वेषाम् too
    (*लोपः शाकल्यस्येति हलि सर्वेषामिति च वकारस्य लोपो न भवति*); the rulebook
    has no such rule yet, and the day it has, this refusal must name it.
    """
    ash = S.members("aŚ")
    parts = [_sounds(sub) for sub in _vanta().values()]
    firsts, lasts = {p[0] for p in parts}, {p[-1] for p in parts}
    for y in v.live:
        if y.seg.made_by != VANTA_STEP or y.s not in lasts \
                or not v.pada_final(y):
            continue
        prev, nxt = v.prev(y), v.next(y)
        if prev is None or nxt is None:
            continue
        if prev.s not in firsts or nxt.s not in ash:
            continue
        yield Application(
            site=site(prev, y, nxt), edits=(),
            detail=Detail(
                kind=PRATISEDHA, sthanin=y.s, adesa="",
                nimitta="the ādeśa of 6.1.79 is one whose v is heard",
                because=(f"{sk(y.s)} was put in by 6.1.79 and now ends a pada, "
                         f"with {sk(nxt.s)}, an {{aś}}, after it — 8.3.19 would "
                         f"offer to drop it, but the ādeśa is a {{vānta}} whose "
                         f"v is heard, so the {sk(y.s)} is not lost"),
                via=(Via(VANTA_STEP, "the substitute of 6.1.79 is what has the "
                                     "v that is heard"),),
                note=(_quote("v_heard") + " — Kaumudī on 6.1.79; a reading of "
                      "the sūtra's word, not a vārttika")))


@rule("6.1.80", name="धातोस्तन्निमित्तस्यैव", families=("ac", "ayavayav"),
      overrides=(("6.1.79", "नियमः — " + _quote("tannimitta")),))
def dhatos_tannimittasyaiva(v: View):
    """
    धातोर्य एच् तन्निमित्तः — of a dhātu's एच्, 6.1.79's substitute is done only if
    the affix itself caused it: लव्यम्, अवश्यलाव्यम्; not ओयते, औयत.

    A niyama, so it refuses: an application with no edits at the same site as
    6.1.79, which it displaces. It leaves a prātipadika alone (*धातोरिति किम्?
    प्रातिपदिकस्य नियमो मा भूत्* — गव्यम्, बाभ्रव्यः). Whether the एच् is the one
    the affix caused is a fact of the derivation, given as `tannimitta`.
    """
    for left, right, sub in _vanta_candidates(v):
        if not _is_dhatu(v, left) or v.word(left).has("tannimitta"):
            continue
        yield Application(
            site=site(left, right), edits=(),
            detail=Detail(
                kind=PRATISEDHA, sthanin=left.s, adesa="",
                nimitta="the {eC} belongs to a dhātu and is not the one the "
                        "affix caused",
                because=(f"{sk(left.s)} ends a dhātu ({sk(_root(v, left) or 'dhātu')}) "
                         f"but was not made by the affix that follows, so "
                         f"6.1.79's {sk(sub)} is not done: it stays "
                         f"({_quote('tannimitta_k')})"),
                via=(Via("6.1.79", "this is the substitution it holds back"),),
                note=(_quote("dhatoriti") + " — a stem that is no dhātu is "
                      "not held back, so this step is made only for a "
                      "dhātu's own एच्")))


def _yat_follows(v: View, right: Sight) -> bool:
    """The affix is *yat* (3.1.97): the piece after the `~` is *ya*, with
    whatever ending it has taken — *yaḥ*, *yam*, *yā*."""
    return v.word(right).text[:2] in ("ya", "yā")


def _nipatana(v: View, roots: Tuple[str, ...], sense: Optional[str],
              extra=None) -> Iterator[Tuple[Sight, Sight, str]]:
    """The place a nipātana of 6.1.81–83 names: the एच् of a named dhātu
    before the affix *यत्*, in the sense the sūtra names. Both the root and the
    sense are the caller's to give."""
    sthanin, ay = _ay_sthanin()
    for left, right, kind in _ec_before_y(v):
        if left.s != sthanin or kind != ANGA or not _yat_follows(v, right):
            continue
        if _root(v, left) not in roots:
            continue
        if sense is not None and not _has_flag(v, (left, right), sense):
            continue
        if extra is not None and not extra(v, left, right):
            continue
        yield left, right, ay


def _nipatana_application(left: Sight, right: Sight, sub: str, *, what: str,
                          sense_text: str) -> Application:
    return Application(
        site=site(left, right), edits=(replace(left, *_sounds(sub)),),
        detail=Detail(
            kind=ADESA, sthanin=left.s, adesa=sub,
            nimitta=f"the affix yat follows, in the sense {sense_text}",
            because=(f"{sk(left.s)} ends the dhātu {what} and yat follows in the "
                     f"sense {sense_text}, so it is replaced by {sk(sub)} — a "
                     f"{{nipātana}}: the form is fixed and not derived"),
            via=(S.saptami_purva(f"{sk(right.s)}, first sound of the affix"),
                 S.yathasamkhya("e, o, ai, au", "ay, av, āy, āv")),
            note="nipātana: the rules do not reach this form, the sūtra states it"))


@rule("6.1.81", name="क्षय्यजय्यौ शक्यार्थे", families=("ac", "ayavayav"))
def ksayya_jayyau(v: View):
    """
    क्षि जि इत्येतयोर्धात्वोर्यति परतः शक्यार्थे एकारस्यायादेशो निपात्यते — क्षय्यः, जय्यः;
    not क्षेयं पापम्, जेयो वृषलः. The roots and the sense (`shakyartha`) are given.
    """
    for left, right, sub in _nipatana(v, ROOTS_6_1_81, "shakyartha"):
        yield _nipatana_application(left, right, sub, what=sk(_root(v, left)),
                                    sense_text="'able to be so done'")


@rule("6.1.82", name="क्रय्यस्तदर्थे", families=("ac", "ayavayav"))
def krayyas_tadarthe(v: View):
    """
    क्रीणातेर्धातोस्तदर्थे यति परतोऽयादेशो निपात्यते — क्रय्यो गौः; not क्रेयं नो धान्यम्.
    The sense — spread out for the purpose of buying — is `krayartha`.
    """
    for left, right, sub in _nipatana(v, (ROOT_6_1_82,), "krayartha"):
        yield _nipatana_application(left, right, sub, what=sk(_root(v, left)),
                                    sense_text="'for the purpose of buying'")


def _pra_vi(v: View, left: Sight, right: Sight) -> bool:
    """The second of 6.1.83's two: vī, and only after pra, and only in the
    feminine (*प्रवय्या इति स्त्रियामेव निपातनम्*). bhī needs neither."""
    if _root(v, left) != ROOT_PRA_VI:
        return True
    return v.word(left).text.startswith("pra") \
        and _has_flag(v, (left, right), "stri")


@rule("6.1.83", name="भय्यप्रवय्ये च च्छन्दसि", families=("ac", "ayavayav"),
      vedic=True)
def bhayyapravayye_ca_chandasi(v: View):
    """
    बिभेतेर्धातोः प्रपूर्वस्य च वी इत्येतस्य यति परतश्छन्दसि विषयेऽयादेशो निपात्यते —
    भय्यम्, प्रवय्या (only in the feminine); not भेयम्, प्रवेयम्.
    """
    for left, right, sub in _nipatana(v, ROOTS_6_1_83, None, extra=_pra_vi):
        yield _nipatana_application(left, right, sub, what=sk(_root(v, left)),
                                    sense_text="in the Veda")


@rule("6.1.83", name="भय्यप्रवय्ये च च्छन्दसि (हृदय्या)",
      families=("ac", "ayavayav"), vedic=True, authority=VARTTIKA,
      varttika=VT_HRADAYYA)
def hradayya(v: View):
    """हृदय्या उपसंख्यानम् — ह्रदय्या आपः (*ह्रदे भवाः*, यत्, in the Veda)."""
    sthanin, ay = _ay_sthanin()
    for left, right, kind in _ec_before_y(v):
        if left.s != sthanin or kind != ANGA or not _yat_follows(v, right) \
                or v.word(left).text not in FORMS_HRADAYYA:
            continue
        yield Application(
            site=site(left, right), edits=(replace(left, *_sounds(ay)),),
            detail=Detail(
                kind=ADESA, sthanin=left.s, adesa=ay,
                nimitta="the affix yat follows, in the Veda",
                because=(f"{sk(left.s)} ends {sk(v.word(left).text)} and yat "
                         f"follows in the Veda, so it becomes {sk(ay)} — "
                         f"hradayyā, by the vārttika"),
                via=(S.saptami_purva(f"{sk(right.s)}, first sound of the affix"),),
                authority=VARTTIKA, varttika=VT_HRADAYYA))


@rule("6.1.83", name="भय्यप्रवय्ये च च्छन्दसि (शरस्य च)",
      families=("ac", "ayavayav"), vedic=True, authority=VARTTIKA,
      varttika=VT_ARSA)
def sarasya_ca(v: View):
    """
    शरस्य च अवादेशो भवतीति वक्तव्यम् — the Bhāṣya adds ह्रदस्य: शरव्या, ह्रदव्या आपः.
    The *अ* at the end of śara and hrada becomes अव् before yat.
    """
    av = AYAV[1]
    for j in v.pairs():
        left, right = j.left, j.right
        if left.s != "a" or right.s != "y" or j.kind != ANGA \
                or not v.ends_word(left) or not v.begins_word(right) \
                or not _yat_follows(v, right) \
                or v.word(left).text not in STEMS_AV:
            continue
        yield Application(
            site=site(left, right), edits=(replace(left, *_sounds(av)),),
            detail=Detail(
                kind=ADESA, sthanin=left.s, adesa=av,
                nimitta="the affix yat follows, in the Veda",
                because=(f"{sk(left.s)} ends {sk(v.word(left).text)} and yat "
                         f"follows in the Veda, so it becomes {sk(av)}, by the "
                         f"vārttika"),
                via=(S.saptami_purva(f"{sk(right.s)}, first sound of the affix"),),
                authority=VARTTIKA, varttika=VT_ARSA))


# ---------------------------------------------------------------------------
# What the yaṇ brings on — first, the two rules that would take a sound away
# ---------------------------------------------------------------------------


def _final_clusters(v: View) -> Iterator[Tuple[List[Sight], Optional[Sight]]]:
    """
    Each cluster of two or more consonants that ENDS a piece, with the sound
    after it. 8.2.23 and 8.2.29 read the end of a pada, exactly as 8.2.39 reads
    its last sound; the insides of words are not offered.

    A cluster in which a sound is seen only through its past is not offered
    either: a rule of the tripādī later than these has already worked there,
    and these have had their chance (8.2.1).
    """
    for last in v.live:
        if not last.is_consonant or not v.ends_word(last):
            continue
        run = v.final_cluster(last)
        if len(run) < 2 or any(s.through for s in run):
            continue
        yield run, v.next(last)


def _text_of(run: List[Sight]) -> str:
    return "".join(s.s for s in run)


def _is_yan(sight: Sight) -> bool:
    return S.is_member(sight.s, "yaṆ")


def _rat_sasya(run: List[Sight]) -> Optional[str]:
    """
    8.2.24 रात्सस्य, read as a condition of 8.2.23: where a र् stands before the
    last sound only a स् is lost (*रात् सस्यैव लोपो भवति, नान्यस्येति*). Returns
    None where there is no र् before, "kept" where 8.2.23 must leave the cluster
    (ऊर्ज्), and "lost" where the last sound is the स् 8.2.24 lets go.
    """
    if len(run) < 2 or run[-2].s != "r":
        return None
    return "lost" if run[-1].s == "s" else "kept"


@rule("8.2.23", name="संयोगान्तस्य लोपः", families=("hal", "samyoganta"))
def samyogantasya_lopah(v: View):
    """
    संयोगान्तं यत्पदं तदन्तस्य लोपः स्यात् — गोमान्, कृतवान्.

    By 1.1.52 it is the last sound of the cluster that goes. It is offered for
    the cluster that ends a pada (*gomānt*), not for one in a word's inside; it
    is not offered where a र् stands before the last sound unless that is स्
    (8.2.24, read as a condition: ऊर्ज् keeps its ज्); and for a yaṇ the
    vārttika below refuses it. 8.2.66's रु, later in the tripādī, does not
    displace it (*रुत्वं परमप्यसिद्धत्वात् संयोगान्तस्य लोपं न बाधते*), so
    श्रेयान्स् loses its स् and does not become श्रेयान्रु.
    """
    for run, _ in _final_clusters(v):
        last = run[-1]
        if not v.pada_final(last):
            continue
        niyama = _rat_sasya(run)
        if niyama == "kept":
            continue
        via = [S.alo_antyasya(last.s)]
        if niyama == "lost":
            via.append(Via(
                "8.2.24",
                f"a {sk('r')} stands before the last sound, so only "
                f"an {sk('s')} may be lost ({_quote('ratsasya')}) — and the "
                f"last sound here is {sk(last.s)}"))
        yield Application(
            site=site(last), edits=(delete(last),),
            detail=Detail(
                kind=LOPA, sthanin=last.s, adesa="",
                nimitta="the pada ends in a cluster",
                because=(f"the pada ends in the cluster "
                         f"{sk(_text_of(run))}, so its last sound "
                         f"{sk(last.s)} is lost"),
                via=tuple(via),
                note=(_quote("rutva_later") if last.s == "s" else "")))


@rule("8.2.23", name="संयोगान्तस्य लोपः (यणः प्रतिषेधः)",
      families=("hal", "samyoganta"), authority=VARTTIKA, varttika=VT_YANAH,
      overrides=(("8.2.23",
                  "the vārttika refuses the loss of a yaṇ — Kaumudī: "
                  + _quote("yalope") + " ... " + _quote("yanah")),))
def yanah_pratisedhah(v: View):
    """
    यणः प्रतिषेधो वाच्यः — सुद्ध्युपास्यः, मद्ध्वरिः, धात्रंशः, लाकृतिः.

    The loss of a yaṇ by 8.2.23 is forbidden. A refusal: no edits, the same site
    as the rule it refuses, and it wins by `overrides`. Read as worded: any yaṇ
    that ends a pada-final cluster is kept, whether 6.1.77 has just put it there
    or the caller gave it so — and only where 8.2.23 would have reached the
    cluster at all (not after a repha, 8.2.24).
    """
    for run, _ in _final_clusters(v):
        last = run[-1]
        if not v.pada_final(last) or not _is_yan(last) \
                or _rat_sasya(run) == "kept":
            continue
        yield Application(
            site=site(last), edits=(),
            detail=Detail(
                kind=PRATISEDHA, sthanin=last.s, adesa="",
                nimitta="the last sound of the cluster is a yaṇ",
                because=(f"the pada now ends in the cluster "
                         f"{sk(_text_of(run))} and 8.2.23 would take "
                         f"its last sound, the {{yaṇ}} {sk(last.s)} (1.1.52) — "
                         f"iti yalope prāpte — but the loss of a {{yaṇ}} is "
                         f"forbidden, so it stays"),
                via=(S.alo_antyasya(last.s),),
                authority=VARTTIKA, varttika=VT_YANAH,
                note=("the Kāśikā reaches the same result by another road: "
                      + _quote("bahiranga_23"))))


@rule("8.2.29", name="स्कोः संयोगाद्योरन्ते च", families=("hal", "samyoganta"),
      overrides=(("8.2.23", "the same cluster, the first sound and not the "
                            "last — " + _quote("nyayya")),))
def skoh_samyogadyor_ante_ca(v: View):
    """
    पदान्ते झलि च परे यः संयोगस्तदाद्योः सकारककारयोर्लोपः — लग्नः, तष्टः, तट्.

    The स् or क् at the head of a cluster goes, where the cluster ends a pada
    or a झल् follows it (*takṣ*, *takṣ~ta*). It is 8.2.23's exception and wins
    the cluster (*न्याय्यत्वादिह संयोगादिलोप एव भवति*): तक्ष् is तट्, and not
    *तक्* — which the engine would give if the two only stood at different
    sounds and the leftmost went first.

    But where the last sound of the cluster is a yaṇ (the one 6.1.77 has just
    put in; a finished pada has no other way to end in a cluster with a yaṇ),
    the Kāśikā refuses it — *वास्यर्थम्, काक्यर्थम् इत्यत्रापि बहिरङ्गलक्षणस्य
    यणादेशस्यासिद्धत्वात्*: the yaṇ is caused by what follows the word, so the rule,
    which rests on the word, does not see it. That refusal is this rule's own
    application, with no edits (the road is the Kāśikā's, not a vārttika).
    """
    for run, nxt in _final_clusters(v):
        first, last = run[0], run[-1]
        if first.s not in SA_KA:
            continue
        at_end = v.pada_final(last)
        before_jhal = nxt is not None and S.is_member(nxt.s, "jhaL")
        if not (at_end or before_jhal):
            continue
        place = site(first, last) if at_end else site(first, last, nxt)
        where = ("ends a pada" if at_end
                 else f"is followed by the {{jhal}} {sk(nxt.s)}")
        if _is_yan(last):
            yield Application(
                site=place, edits=(),
                detail=Detail(
                    kind=PRATISEDHA, sthanin=first.s, adesa="",
                    nimitta="the cluster ends in a yaṇ",
                    because=(f"{sk(first.s)} heads the cluster "
                             f"{sk(_text_of(run))}, which {where}, and 8.2.29 "
                             f"would take it — but the {{yaṇ}} "
                             f"{sk(last.s)} is {{bahiraṅga}} and asiddha to it, so "
                             f"there is no cluster here to lose "
                             f"({_quote('bahiranga_29')})"),
                    via=(S.alo_antyasya(first.s),),
                    note="the road is the Kāśikā's, not a vārttika: "
                         "बहिरङ्गलक्षणत्वात् (OPEN: the Bhāṣya rejects the "
                         "vārttika of 8.2.23 for this reason too)"))
        else:
            yield Application(
                site=place, edits=(delete(first),),
                detail=Detail(
                    kind=LOPA, sthanin=first.s, adesa="",
                    nimitta=("a cluster ends the pada" if at_end
                             else f"the {{jhal}} {sk(nxt.s)} follows the cluster"),
                    because=(f"{sk(first.s)} heads the cluster "
                             f"{sk(_text_of(run))}, which {where}, so "
                             f"it is lost"),
                    via=(S.alo_antyasya(first.s),),
                    note=_quote("skoh")))


# ---------------------------------------------------------------------------
# Doubling — 8.4.46, 8.4.47, the vārttika यणो मयो द्वे, and who may decline it
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class _Dvitva:
    """One sound that may be said twice, and everything that place is."""

    kind: str                  # "rahabhyam" (8.4.46), "anaci" (8.4.47), "mayo"
    doubled: Sight
    context: Tuple[Sight, ...]
    site: Tuple[int, ...]
    #: the yaṇ 6.1.77 made, which is what brought the doubling on
    yan: Sight


def _dvitva_candidates(v: View) -> List[_Dvitva]:
    """
    Every place where a sound beside the yaṇ of 6.1.77 may be doubled. All the
    doubling rules, and the refusals that stand at the same sites, read THIS,
    so that two of them can never differ about what a place is.
    """
    yar, may, yan = S.members("yaR"), S.members("maY"), S.members("yaṆ")
    found: List[_Dvitva] = []
    for j in v.pairs():
        x, y = j.left, j.right
        if not (x.is_consonant and y.is_consonant) or x.through or y.through:
            continue
        if y.seg.made_by != YAN or y.s not in yar:
            continue
        p = v.prev(x)
        after_ac = p is not None and p.is_vowel
        if x.s in RAHA:
            # 8.4.46: the yar after a र् or ह् that follows a vowel. The र् and ह्
            # are the cause and are never the doubled sound: (r, y) gives yy.
            if after_ac and y.s not in RAHA:
                found.append(_Dvitva("rahabhyam", y, (p, x),
                                     site(p, x, y), y))
            continue
        if after_ac and x.s in yar:
            found.append(_Dvitva("anaci", x, (p, y), site(p, x, y), y))
        if x.s in may and y.s in yan and y.s not in RAHA:
            open_b = after_ac and not _refused(v, "8.4.47", site(p, x, y))
            if not open_b:
                found.append(_Dvitva("mayo", y, (x,), site(x, y), y))
    return found


def _where_doubled(c: _Dvitva) -> str:
    """Where the doubled sound stands, in this form's own sounds. One branch
    is built, the one that is true: the others name sounds that may not
    exist."""
    if c.kind == "rahabhyam":
        return (f"after {sk(c.context[1].s)}, which follows the vowel "
                f"{sk(c.context[0].s)}")
    if c.kind == "anaci":
        return (f"after the vowel {sk(c.context[0].s)}, and no vowel follows "
                f"it ({sk(c.context[1].s)} is the yaṇ)")
    return f"after the {{may}} {sk(c.context[0].s)}"


def _dvitva_note(c: _Dvitva) -> str:
    """What the tradition says of this kind of place, verbatim."""
    if c.kind == "rahabhyam":
        return (_quote("raha_cause") + " — the र् or ह् is the cause, and is "
                "not what is said twice")
    if c.kind == "anaci":
        return _quote("anaci")
    return (_quote("mayo") + "; " + _quote("mayo_reading") + "; "
            + _quote("four_forms"))


def _doubling(v: View, c: _Dvitva, sutra_via: Via, *, authority: str = "sūtra",
              varttika: str = "") -> Application:
    d = c.doubled
    return Application(
        site=c.site, edits=(replace(d, d.s, d.s),),
        detail=Detail(
            kind=DVITVA, sthanin=d.s, adesa=f"{d.s}+{d.s}",
            nimitta=f"beside the yaṇ {sk(c.yan.s)}",
            because=(f"{sk(d.s)} is a {{yar}} {_where_doubled(c)}, so it is "
                     f"said twice: {sk(d.s)} {sk(d.s)}"),
            via=(sutra_via,), authority=authority, varttika=varttika,
            note=_dvitva_note(c)))


@rule("8.4.46", name="अचो रहाभ्यां द्वे", families=("hal", "dvitva"))
def aco_rahabhyam_dve(v: View):
    """
    अचः पराभ्यां रेफहकाराभ्यां परस्य यरो द्वे स्तः — हर्य्यनुभवः, नह्य्यस्ति, गौर्य्यौ.

    The यर् after a र् or ह् that itself follows a vowel; here the y that 6.1.77
    has just put in. Unconditional as the Kāśikā words it; 8.4.51 declines it.
    """
    for c in _dvitva_candidates(v):
        if c.kind == "rahabhyam":
            yield _doubling(v, c, S.pancami_para(
                f"{{aC}} {sk(c.context[0].s)} and {sk(c.context[1].s)}"))


@rule("8.4.47", name="अनचि च", families=("hal", "dvitva"))
def anaci_ca(v: View):
    """
    अचः परस्य यरो द्वे स्तो न त्वचि — दद्ध्यत्र, मद्ध्वत्र, धात्तंशः.

    The यर् after a vowel with no vowel after it — the ध् of सुध्य् — said twice.
    The र् and ह् are not doubled (they are 8.4.46's cause). Unconditional; 8.4.51
    declines it.
    """
    for c in _dvitva_candidates(v):
        if c.kind == "anaci":
            yield _doubling(v, c, S.pancami_para(
                f"{{aC}} {sk(c.context[0].s)}"))


@rule("8.4.47", name="अनचि च (यणो मयो द्वे)", families=("hal", "dvitva"),
      authority=VARTTIKA, varttika=VT_MAYO)
def yano_mayo_dve(v: View):
    """
    यणो मयो द्वे वाच्ये — दध्य्यत्र, मध्व्वत्र (Kāśikā, second reading).

    A yaṇ after a मय् is said twice: the य् of सुध्य् after the ध्. Offered only
    once 8.4.47's own doubling of the ध् is settled at that place, so that each of
    the two is its own option — which is what makes the Kaumudī's four forms.
    """
    for c in _dvitva_candidates(v):
        if c.kind == "mayo":
            yield _doubling(
                v, c, S.pancami_para(f"{{may}} {sk(c.context[0].s)}"),
                authority=VARTTIKA, varttika=VT_MAYO)


def _second_of_a_double(sight: Sight) -> bool:
    """The sound a doubling of this family added — not the one it said twice."""
    return sight.seg.made_by in DOUBLING and not sight.seg.prior


def _cluster_size(v: View, sight: Sight) -> int:
    """
    How many consonants stand together with `sight`, as the WORD has them: a
    sound a doubling has just added is not counted (Śākaṭāyana's three are the
    conjunct the word has, not one the doubling would make).
    """
    index = v.index(sight)
    lo = hi = index
    while lo > 0 and v.live[lo - 1].is_consonant:
        lo -= 1
    while hi + 1 < len(v.live) and v.live[hi + 1].is_consonant:
        hi += 1
    return sum(1 for s in v.live[lo:hi + 1] if not _second_of_a_double(s))


@rule("8.4.51", name="सर्वत्र शाकल्यस्य", families=("hal", "dvitva"),
      overrides=(("8.4.46", _quote("sakalya")),
                 ("8.4.47", _quote("sakalya"))))
def sarvatra_sakalyasya(v: View):
    """
    शाकल्यस्याचार्यस्य मतेन सर्वत्र द्विर्वचनं न भवति — अर्कः, ब्रह्मा.

    The doubling of 8.4.46–47 declined. It is the teachers' option, and the union
    of what any of them allows is *both forms*: Śākalya's 'everywhere' already
    holds the domains of Śākaṭāyana (8.4.50: a cluster of three or more) and of
    the ācāryas (8.4.52: after a long vowel), so those two are not separate forks —
    where their own domain also holds they are cited here, as a `Via`.

    A refusal, at the same site as the doubling it declines (both read
    `_dvitva_candidates`), and optional: the course that takes it comes first.
    """
    for c in _dvitva_candidates(v):
        vias: List[Via] = []
        size = _cluster_size(v, c.doubled)
        if size >= 3:
            vias.append(Via(
                "8.4.50",
                f"{sk(c.doubled.s)} stands in a cluster of {size} consonants, and "
                f"Śākaṭāyana too has no doubling there "
                f"({_quote('sakatayana')})"))
        if c.kind == "anaci" and is_dirgha(c.context[0].s):
            vias.append(Via(
                "8.4.52",
                f"{sk(c.doubled.s)} follows the long vowel {sk(c.context[0].s)}, "
                f"and the ācāryas too have no doubling there "
                f"({_quote('acaryas')})"))
        yield Application(
            site=c.site, edits=(), optional="शाकल्यस्य",
            detail=Detail(
                kind=PRATISEDHA, sthanin=c.doubled.s, adesa="",
                nimitta="the opinion of Śākalya",
                because=(f"in the opinion of {{śākalya}} there is no doubling "
                         f"anywhere, so this course leaves {sk(c.doubled.s)} single; "
                         f"the other keeps the doubling of 8.4.46–47 (an option "
                         f"of opinion, not a {{vibhāṣā}} of the 1.3.43 or the 1.3.50 kind)"),
                via=tuple(vias)))


# ---------------------------------------------------------------------------
# 8.4.53 झलां जश् झशि, 8.4.64 हलो यमां यमि लोपः
# ---------------------------------------------------------------------------


@rule("8.4.53", name="झलां जश् झशि", families=("hal",))
def jhalam_jas_jhasi(v: View):
    """
    झलां स्थाने जशादेशो भवति झशि परतः — लब्धा, दोग्धा, बोद्धा, सुद्ध्युपास्य.

    Asked of `anga.jhalam_jas_jhasi`, which is the same sūtra as a question, and
    which agrees with 1.1.50's nearest on every झल् and झश् there is (a test says
    so). The first ध् of a doubled ध् is the case the Laghu names.
    """
    for j in v.pairs():
        left, right = j.left, j.right
        got = _jhalam_jas_jhasi(left.s + right.s)
        if got.result is None:
            continue
        sub = got.now
        yield Application(
            site=site(left, right), edits=(replace(left, sub),),
            detail=Detail(
                kind=ADESA, sthanin=left.s, adesa=sub,
                nimitta=f"the {{jhaś}} {sk(right.s)} follows",
                because=(f"{sk(left.s)} is a {{jhal}} and {sk(right.s)} a {{jhaś}}, "
                         f"so {sk(left.s)} becomes its {{jaś}} {sk(sub)}"),
                via=(S.saptami_purva(f"{{jhaś}} {sk(right.s)}"),
                     S.antaratama(left.s, sub, "{jaś} (j, b, g, ḍ, d)"))))


@rule("8.4.54", name="अभ्यासे चर्च", families=("hal",))
def abhyase_carca(v: View):
    """
    अभ्यासे वर्तमानानां झलां चरादेशो भवति, चकाराद् जश् च — बुभूषति, चिखनिषति,
    तिष्ठासति, डुढौकिषते.

    The engine does not build a reduplicate, so the piece that IS the अभ्यास
    is the caller's to name (the flag `abhyasa`, on the piece in front of the
    `~`): *bhu~bhūṣati*, *chi~khaniṣati*. What it becomes is asked of
    `anga.abhyase_car`, the same sūtra as a question: a voiceless aspirate takes
    the voiceless unaspirated of its own varga and a voiced one the voiced
    (*प्रकृतिचरां प्रकृतिचरो भवन्ति, प्रकृतिजशां प्रकृतिजशः* — a sound that is
    already one stays). 1.1.50 is not what chooses: asked for the nearest of चर्
    and जश् to थ्, it answers स्, both being dental, and तितनिषति is the vṛtti's own
    form. The sound changed is the first of the piece, the only consonant an
    अभ्यास has once 7.4.60 has left it one.
    """
    for s in v.live:
        if not v.word(s).has("abhyasa") or not v.begins_word(s):
            continue
        piece = "".join(t.s for t in v.word_sights(s.w))
        got = abhyase_car(piece)
        if got.result is None:
            continue
        new = tokenize(got.result)[0][0]
        if new == s.s:
            continue
        yield Application(
            site=site(s), edits=(replace(s, new),),
            detail=Detail(
                kind=ADESA, sthanin=s.s, adesa=new,
                nimitta="the sound stands in the abhyāsa",
                because=(f"{sk(s.s)} is a {{jhal}} in the {{abhyāsa}} "
                         f"{sk(piece)}, so it is replaced by its {{car}} — or "
                         f"its {{jaś}}, the {{ca}} of the sūtra: {sk(new)}, the "
                         f"unaspirated of its own varga"),
                via=(),
                note=got.why))


@rule("8.4.64", name="हलो यमां यमि लोपः", families=("hal", "dvitva"))
def halo_yamam_yami_lopah(v: View):
    """
    हलः परस्य यमो लोपः स्याद्वा यमि — शय्या, शय्य्या; and after the doubling of
    8.4.46–47 the first of the two.

    A yam that stands after a हल् and before a yam may be lost
    (*अन्यतरस्यामिति वर्तते*), each before the yam of its own kind — यमां यमीति
    यथासंख्यम् (1.3.10), which is why माहात्म्य keeps its म् (*यमां यमीति
    यथासङ्ख्यविज्ञानान्नेह । माहात्म्यम्*). An अप्राप्तविभाषा — nothing else gives
    the loss — so the course that takes it comes first. Offered only where the two
    yams are the doubled sounds this family has made; the yams of two finished
    words are not doubled by anything the engine did.
    """
    pairing = _yam_pairing()
    for j in v.pairs():
        x, y = j.left, j.right
        if x.through or y.through or pairing.get(x.s) != y.s:
            continue
        if x.seg.made_by not in DOUBLING and y.seg.made_by not in DOUBLING:
            continue
        p = v.prev(x)
        if p is None or not p.is_consonant:
            continue
        yield Application(
            site=site(p, x, y), edits=(delete(x),), optional="अन्यतरस्याम्",
            detail=Detail(
                kind=LOPA, sthanin=x.s, adesa="",
                nimitta=f"the yam {sk(y.s)} follows",
                because=(f"{sk(x.s)} is a {{yam}} after the {{hal}} {sk(p.s)} and "
                         f"before the {{yam}} {sk(y.s)}, so it may be lost — an "
                         f"{{aprāptavibhāṣā}} ({_quote('yamam')})"),
                via=(S.saptami_purva(f"{{yam}} {sk(y.s)}"),
                     Via("1.3.10",
                         f"the list of yams lost and the list of yams before "
                         f"which they are lost are the same length, so they "
                         f"correspond in order: {sk(x.s)} is lost before "
                         f"{sk(y.s)}, and not before a yam of another kind "
                         f"({_quote('yamam_yathasamkhya')}, Kaumudī)"))))


RULES = (
    iko_yanaci, plutapurvasya, eco_yavayavah,
    vanto_yi_pratyaye, gor_yutau_chandasi, adhvaparimane_ca,
    sruyamana_vakaranta, dhatos_tannimittasyaiva, ksayya_jayyau,
    krayyas_tadarthe, bhayyapravayye_ca_chandasi, hradayya, sarasya_ca,
    samyogantasya_lopah, yanah_pratisedhah, skoh_samyogadyor_ante_ca,
    aco_rahabhyam_dve, anaci_ca, yano_mayo_dve,
    sarvatra_sakalyasya, jhalam_jas_jhasi, abhyase_carca,
    halo_yamam_yami_lopah,
)

#: Which sūtras of this family's scope the module implements — the honest
#: account, kept beside the code. See `rulebook.COVERAGE_STATUS`.
COVERAGE = (
    ("6.1.77", "rule", "with the vārttika of the pluta-preceded इक्, which "
                       "also lifts a pragṛhya hold"),
    ("6.1.78", "rule", ""),
    ("6.1.79", "rule", "with the vārttikas गोर्यूतौ छन्दसि and अध्वपरिमाणे च, "
                       "and the Kaumudī's श्रूयमाणवकारान्त reading (the v is "
                       "not lost by 8.3.19); the affix is what a `~` says"),
    ("6.1.80", "rule", "as a niyama that refuses 6.1.79; `tannimitta` is the "
                       "caller's"),
    ("6.1.81", "rule", "a nipātana; root and sense are the caller's"),
    ("6.1.82", "rule", "a nipātana; root and sense are the caller's"),
    ("6.1.83", "vedic", "with the vārttikas हृदय्या and शरस्य च; Vedic only"),
    ("8.2.23", "partial", "the cluster that ends a pada, not the inside of a "
                          "word; a र् before the last sound keeps the cluster "
                          "unless the last is स् (8.2.24, read as a condition, "
                          "not a rule here); the vārttika यणः प्रतिषेधो "
                          "वाच्यः refuses a yaṇ"),
    ("8.2.29", "partial", "the cluster that ends a pada, and the one that ends "
                          "a piece before a झल्; not the inside of a word; the "
                          "vārttika झलि सङि (rejected in the Bhāṣya) is not "
                          "modelled; the Kāśikā refuses it for the yaṇ of 6.1.77"),
    ("8.4.46", "partial", "offered only beside the yaṇ of 6.1.77; the "
                          "interior doubling of finished words (अर्क्कः, "
                          "ब्रह्म्मा) and at a plain junction (दुर्ल्लभः) is "
                          "not opened"),
    ("8.4.47", "partial", "offered only beside the yaṇ of 6.1.77, with the "
                          "vārttika यणो मयो द्वे (its second reading only); "
                          "the interior doubling of finished words, the "
                          "vārttikas शरः खयो द्वे and अवसाने च and the head "
                          "of a longer cluster are not opened"),
    ("8.4.48", "scope", "refuses the doubling of the त् inside the finished "
                        "word पुत्र (पुत्रादिनी), which is neither at a "
                        "junction nor beside a sound this derivation made; "
                        "आक्रोश is a sense no flag carries; the vārttikas "
                        "on it (तत्परे च, वा हतजग्धयोः, चयो द्वितीयाः शरि) "
                        "are for the same finished words"),
    ("8.4.49", "scope", "refuses the doubling of a शर् before a vowel (कर्षति, "
                        "वर्षति) inside a finished root; no step of this "
                        "family makes a शर्, so the place never arises"),
    ("8.4.50", "partial", "Śākaṭāyana's opinion: cited as a Via of 8.4.51 where "
                          "its cluster of three or more holds; not a separate "
                          "fork, since the union of the teachers is 8.4.51's "
                          "'everywhere'"),
    ("8.4.51", "rule", "the optional refusal of the doubling; the union of the "
                       "teachers' allowances is both forms"),
    ("8.4.52", "partial", "the ācāryas' opinion: cited as a Via of 8.4.51 where "
                          "the yar follows a long vowel; not a separate fork"),
    ("8.4.53", "rule", "asked of anga.jhalam_jas_jhasi"),
    ("8.4.54", "partial", "only for a piece the caller flags `abhyasa`: the "
                          "engine builds no reduplicate, so the abhyāsa and "
                          "the base are given as two pieces of one pada; what "
                          "the aspirate becomes is asked of anga.abhyase_car"),
    ("8.4.64", "partial", "offered only for the yams a doubling of this "
                          "family has made, each before the yam of its own "
                          "kind"),
    ("1.1.9", "support", "cited by the vārttika of 6.1.77 (savarṇa, "
                         "varna.savarna)"),
    ("1.1.10", "support", "asked inside varna.savarna (an अच् and a हल् are "
                          "never savarṇa), which is why दधि हरति, दधि शीतम् "
                          "get no yaṇ: a consonant is no अच् for 6.1.77 "
                          "however alike; no step is made for what no rule "
                          "could apply to, so no step cites it"),
    ("1.1.50", "support", "cited by 6.1.77 and 8.4.53 (supports.antaratama)"),
    ("1.1.51", "support", "cited by 6.1.77 for ṛ and ḷ — the yaṇ is not an aṇ, "
                          "so no repha is added (`uran_raparah`)"),
    ("1.1.52", "support", "cited by 8.2.23, 8.2.29: the last (or first) sound "
                          "goes, not the cluster"),
    ("1.1.66", "support", "cited by 6.1.77–79, 8.4.53, 8.4.64 "
                          "(supports.saptami_purva)"),
    ("1.1.67", "support", "cited by 8.4.46–47 (supports.pancami_para)"),
    ("1.1.69", "support", "cited by 6.1.77 for the long इक् "
                          "(supports.varna_grahana)"),
    ("1.1.70", "support", "none of this family's sūtras names a त्-marked "
                          "sound, so no step cites it"),
    ("1.3.10", "support", "cited by 6.1.78–79, 8.4.64 (supports.yathasamkhya)"),
)
