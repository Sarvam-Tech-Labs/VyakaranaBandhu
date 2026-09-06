# -*- coding: utf-8 -*-
"""
३.३.१५८, १६३, १६७, १६९–१७२, १७४ — the affixes of enjoining, deserving,
necessity and blessing.

The close of the pāda divides between two questions. Most of its rules
choose a लकार on a sense, and answer from the table 3.2.110 onward
already holds. These eight give a कृत् affix instead — तुमुन्, the
कृत्य affixes, तृच्, णिनि, क्तिच् — on the same senses, and several of
them exist ONLY because a लकार rule would otherwise have displaced
what a general rule gives.

**And that is where the sixth वासरूप suspension is established.**
3.3.163 asks why the कृत्य affixes are stated when they are given
generally already, and answers: विशेषविहितेनानेन लोटा बाध्यन्ते,
वासरूपविधिना भविष्यन्ति? एवं तर्हि ज्ञापयति — स्त्र्यधिकारात् परेण
वासरूपविधिर्नावश्यं भवति. The principle of 3.1.94 is **not obligatory
after the feminine section**. 3.3.167 and 3.3.169 both lean on that
same ज्ञापक, and 3.3.107 had already bounded the suspension from the
other side — holding it WITHIN the feminine section. Between them the
two rules fence the principle off at both ends.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.upapada_krt import Added, NotAdded

#: 3.3.161's six senses, each glossed by the vṛtti — विधिः प्रेरणम्,
#: निमन्त्रणं नियोगकरणम्, आमन्त्रणं कामचारकरणम्, अधीष्टः
#: सत्कारपूर्वको व्यापारः, संप्रश्नः संप्रधारणम्, प्रार्थनं याच्ञा.
#: They run down into 3.3.162 and are narrowed at 3.3.163.
VIDHYADI: Tuple[str, ...] = (
    "vidhi", "nimantraṇa", "āmantraṇa", "adhīṣṭa", "sampraśna",
    "prārthana",
)

#: 3.3.163's three — प्रेषणं प्रैषः, कामचाराभ्यनुज्ञानमतिसर्गः,
#: निमित्तभूतस्य कालस्यावसरः प्राप्तकालता.
PRAISADI: Tuple[str, ...] = ("praiṣa", "atisarga", "prāptakāla")

#: 3.3.167's companions — कालो भोक्तुम्, समयो भोक्तुम्, वेला भोक्तुम्.
KALADI: Tuple[str, ...] = ("kāla", "samaya", "velā")


@dataclass(frozen=True)
class VidhiKrt:
    """One rule giving a कृत् affix in a sense of enjoining or the like."""

    sutra: str
    gives: str
    also: str = ""
    #: Any ONE of these senses satisfies it.
    sense: Tuple[str, ...] = ()
    #: 3.3.167's कालादि — the companion word.
    beside: Tuple[str, ...] = ()
    #: 3.3.158's समानकर्तृक — one doer for both acts.
    samana_kartrka: bool = False
    #: 3.3.174's संज्ञायाम्, and the name is carried by the WHOLE.
    samjna: bool = False
    #: Whether the rule exists because a लकार rule would otherwise
    #: have displaced what a general rule gives. Four of the eight do,
    #: and each says so.
    against_lakara: str = ""
    why: str = ""


VIDHI_KRT: Tuple[VidhiKrt, ...] = (
    VidhiKrt(
        "3.3.158", "tumun", sense=("icchā",), samana_kartrka=True,
        why="समानकर्तृकेषु तुमुन् — इच्छति भोक्तुम्, कामयते भोक्तुम्, "
            "वष्टि भोक्तुम्, वाञ्छति भोक्तुम्. "
            "तुमुन्प्रकृत्यपेक्षमेव समानकर्तृकत्वम् — the sameness of "
            "doer is judged from the root the affix goes on, not from "
            "the other. समानकर्तृकेष्विति किम्? देवदत्तं भुञ्जानमिच्छति "
            "यज्ञदत्तः.\n\n"
            "इह कस्माद् न भवति इच्छन् करोति? अनभिधानात् — the limit "
            "that is not a condition, met at 3.2.1, 3.1.108 and "
            "3.3.30. The check is against usage and there is nothing "
            "to codify"),
    VidhiKrt(
        "3.3.163", "kṛtya", also="लोट्", sense=PRAISADI,
        against_lakara="3.3.162",
        why="प्रैषातिसर्गप्राप्तकालेषु कृत्याश्च — भवता कटः करणीयः, "
            "कर्तव्यः, कृत्यः, कार्यः; and by the च, करोतु कटं भवान् "
            "इह प्रेषितः. प्रेषणं प्रैषः, कामचाराभ्यनुज्ञानमतिसर्गः, "
            "निमित्तभूतस्य कालस्यावसरः प्राप्तकालता.\n\n"
            "AND HERE THE SIXTH वासरूप SUSPENSION IS ESTABLISHED, IN "
            "ITS GENERAL FORM. किमर्थं प्रैषादिषु कृत्या विधीयन्ते, न "
            "सामान्येन भावकर्मणोर्विहिता एव? — why state them when "
            "they are given generally? विशेषविहितेनानेन लोटा "
            "बाध्यन्ते: 3.3.162's लोट्, given for this very ground, "
            "would displace them. वासरूपविधिना भविष्यन्ति? — could "
            "3.1.94 not let them stand beside? एवं तर्हि ज्ञापयति — "
            "स्त्र्यधिकारात् परेण वासरूपविधिर्नावश्यं भवति: the "
            "principle is NOT OBLIGATORY after the feminine section. "
            "3.3.107 had bounded it from the other side, holding it "
            "WITHIN that section; between them the two rules fence it "
            "off at both ends.\n\n"
            "SCOPE — विधिप्रैषयोः को विशेषः? केचिदाहुः — "
            "अज्ञातज्ञापनं विधिः, प्रेषणं प्रैष इति: some say "
            "enjoining is making known what was not known, and "
            "prompting is sending. Attributed and not adopted"),
    VidhiKrt(
        "3.3.167", "tumun", beside=KALADI,
        against_lakara="",
        why="कालसमयवेलासु तुमुन् — कालो भोक्तुम्, समयो भोक्तुम्, "
            "वेला भोक्तुम्.\n\n"
            "TWO QUESTIONS ANSWERED BY BORROWING FROM ELSEWHERE. "
            "इह कस्माद् न भवति कालः पचति भूतानि? "
            "प्रैषादिग्रहणमिहाभिसंबध्यते — 3.3.163's senses are read "
            "in, so the rule wants an enjoining and not a statement. "
            "And इह कस्माद् न भवति कालो भोजनस्य? वासरूपेण ल्युडपि "
            "भवति, उक्तमिदम् — स्त्र्यधिकारात् परत्र वासरूपविधिरनित्यः: "
            "ल्युट् stands beside by 3.1.94, the suspension after the "
            "feminine section being only optional. The ज्ञापक of "
            "3.3.163 used four sūtras later, and cited as already "
            "settled"),
    VidhiKrt(
        "3.3.169", "kṛtya", also="तृच्, लिङ्", sense=("arha",),
        against_lakara="3.3.169",
        why="अर्हे कृत्यतृचश्च — भवता खलु कन्या वोढव्या, वाह्या, "
            "वहनीया; भवान् खलु कन्याया वोढा; and by the च, भवान् खलु "
            "कन्यां वहेत्. अर्हतीत्यर्हः, तद्योग्यः.\n\n"
            "अथ कस्मादर्हे कृत्यतृचो विधीयन्ते, यावता सामान्येन "
            "विहितत्वादर्हेऽपि भविष्यन्ति? योऽयमिह लिङ् विधीयते, तेन "
            "बाधा मा भूदिति — they are stated so that the लिङ् THIS "
            "SAME RULE gives shall not displace them. A rule "
            "protecting half of itself from the other half. "
            "वासरूपविधिश्चानित्यः, the third citation of 3.3.163's "
            "ज्ञापक"),
    VidhiKrt(
        "3.3.170", "ṇini", sense=("āvaśyaka", "ādhamarṇya"),
        why="आवश्यकाधमर्ण्ययोर्णिनिः — अवश्यंकारी; and for the debt, "
            "शतं दायी, सहस्रं दायी, निष्कं दायी. "
            "अवश्यंभाव आवश्यकम्.\n\n"
            "उपाधिरयम्, नोपपदम् — these are QUALIFICATIONS of the "
            "sense and not companion words, which the rule's form "
            "does not show and the vṛtti has to say. "
            "मयूरव्यंसकादित्वात् समासः accounts for the compound"),
    VidhiKrt(
        "3.3.171", "kṛtya", sense=("āvaśyaka", "ādhamarṇya"),
        against_lakara="3.3.170",
        why="कृत्याश्च — भवता खल्ववश्यं कटः कर्तव्यः, करणीयः, "
            "कार्यः, कृत्यः; and for the debt, भवता शतं दातव्यम्, "
            "सहस्रं देयम्.\n\n"
            "किमर्थमिदम्, यावता सामान्येन विहिता अस्मिन्नपि विषये "
            "भविष्यन्ति? विशेषविहितेन णिनिना बाध्येरन् — the rule "
            "before, given for this very ground, would displace them. "
            "The same shape as 3.3.163 and 3.3.169.\n\n"
            "AND AN OBJECTION THE VṚTTI DOES NOT FULLY ANSWER. "
            "कर्तरि णिनिः, भावकर्मणोः कृत्याः, तत्र कुतो "
            "बाधप्रसङ्गः? — णिनि names the doer and the कृत्य affixes "
            "the act or the object, so how could one displace the "
            "other at all? तत्र केचिदाहुः — भव्यगेयादयः कर्तृवाचिनः "
            "कृत्याः, त इहोदाहरणमिति: SOME say certain कृत्य affixes "
            "do name the doer, and those are the examples. Attributed "
            "to others and left there"),
    VidhiKrt(
        "3.3.174", "ktic", also="क्त", sense=("āśis",), samjna=True,
        against_lakara="",
        why="क्तिच्क्तौ च संज्ञायाम् — तनुतात् तन्तिः, सनुतात् सातिः, "
            "भवतात् भूतिः; and for the क्त, देवा एनं देयासुर्देवदत्तः. "
            "समुदायेन चेत् संज्ञा गम्यते — the name carried by the "
            "WHOLE, the seventh समुदायोपाधि.\n\n"
            "सामान्येन विहितः क्तः पुनरुच्यते, क्तिचा बाधा मा भूदिति "
            "— क्त is stated again so that the क्तिच् of this rule "
            "shall not displace it. The same self-protection as "
            "3.3.169's, and by the same means. "
            "चकारो विशेषणार्थः न क्तिचि दीर्घश्च इति, the च spent so "
            "6.4.39 can pick the affix out"),
    VidhiKrt(
        "3.4.65", "tumun",
        beside=("śak", "dhṛṣ", "glai", "ghaṭ", "rabh", "labh",
                "kram", "sah", "arh", "as", "bhū", "vid"),
        why="शकधृषज्ञाग्लाघटरभलभक्रमसहार्हास्त्यर्थेषु तुमुन् — "
            "शक्नोति भोक्तुम्, धृष्णोति भोक्तुम्, ग्लायति भोक्तुम्, "
            "अर्हति भोक्तुम्; and for the words meaning 'is', अस्ति "
            "भोक्तुम्, भवति भोक्तुम्, विद्यते भोक्तुम्.\n\n"
            "अक्रियार्थोपपदार्थोऽयमारम्भः — the rule exists for a "
            "companion that is NOT an act done for the sake of "
            "another, which is what 3.3.10 had wanted. A rule defined "
            "by the condition it drops"),
    VidhiKrt(
        "3.4.66", "tumun", sense=("paryāpti",),
        beside=("alam", "paryāpta", "pāray"),
        why="पर्याप्तिवचनेष्वलमर्थेषु — पर्याप्तो भोक्तुम्, अलं "
            "भोक्तुम्, भोक्तुं पारयति. पर्याप्तिरन्यूनता, sufficiency.\n\n"
            "TWO CONDITIONS AND TWO COUNTERS THAT CROSS. "
            "पर्याप्तिवचनेष्विति किम्? अलं कृत्वा — a word meaning "
            "'enough' but not of sufficiency. अलमर्थेष्विति किम्? "
            "पर्याप्तं भुङ्क्ते — sufficiency, but not a word of that "
            "family. Each counter fails the condition the other "
            "satisfies.\n\n"
            "पूर्वसूत्रे शकिग्रहणमनलमर्थम्, शक्यमेवं कर्तुमिति — and "
            "3.4.65 names शक् for a sense OUTSIDE this one, so the two "
            "rules divide that root between them"),
)


def vidhi_affix(*, sense: str = "", beside: str = "",
                samana_kartrka: bool = False, samjna: bool = False,
                wants: str = "") -> object:
    """
    3.3.158 and after — which कृत् affix comes in a sense of
    enjoining, deserving, necessity or blessing.

    Separate from the लकार rules of the same stretch because the
    question is different: these give a कृत् affix where those choose
    a tense-ending, and four of them exist precisely BECAUSE a लकार
    rule would otherwise have displaced what a general rule gives.
    """
    matched = [row for row in VIDHI_KRT
               if (not row.sense or sense in row.sense)
               and (not row.beside or beside in row.beside)
               and (not row.samana_kartrka or samana_kartrka)
               and (not row.samjna or samjna)
               and (not wants or wants == row.gives
                    or wants in row.also)]
    if not matched:
        return NotAdded(
            "",
            "No rule of this run gives that. What it gives is तुमुन् "
            "where one doer wishes and where a time-word stands, the "
            "कृत्य affixes in enjoining, deserving and necessity, "
            "णिनि in necessity and debt, and क्तिच् in a blessing")
    best = max(matched, key=_how_specific)
    return Added(best.gives, best.sutra, best.why, also=best.also)


def _how_specific(row: VidhiKrt) -> int:
    """How much a row states."""
    return (2 * (len(row.sense) > 0) + 3 * (len(row.beside) > 0)
            + 2 * row.samana_kartrka + 2 * row.samjna)


def stated_against_a_lakara() -> Tuple[str, ...]:
    """
    The rules of this run that exist because a लकार rule would
    otherwise have displaced what a general rule gives.

    Read from the table rather than listed, so the answer cannot drift
    from what the rows say. This is the shape the सिद्ध-and-restated
    argument takes at the close of the pāda, and 3.3.163's answer to
    it is where the sixth वासरूप suspension is established.
    """
    return tuple(row.sutra for row in VIDHI_KRT if row.against_lakara)
