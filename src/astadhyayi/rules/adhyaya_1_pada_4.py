# -*- coding: utf-8 -*-
"""
अध्याय १, पाद ४ — the saṃjñās the rest of the grammar is written in.

The pāda opens with two rules about rules and then gives the names: नदी and
घि for the nominal stems, लघु and गुरु for syllables, अङ्ग, पद and भ, the
three numbers, then the कारकs, the particles, and the endings.

1.4.1 आ कडारादेका संज्ञा governs the whole of it and beyond — as far as 2.2.38
— and it is doing work here rather than sitting overhead. Three of the eight
saṃjñās codified so far are in direct competition with another, and each time
it is 1.4.1 that settles which name stands. So `vipratisedha.eka_samjna` is
called from `nominal` rather than the outcome being written into each rule.
"""

from __future__ import annotations

from src.astadhyayi.nominal import (
    anga,
    ghi,
    nadi,
    pada_or_bha,
    vacana,
    weight,
)
from src.astadhyayi.karaka import PROVISIONS as KARAKA_PROVISIONS
from src.astadhyayi.karaka import karaka_of
from src.astadhyayi.nipata import PROVISIONS as NIPATA_PROVISIONS
from src.astadhyayi.nipata import (
    in_nipata_range,
    names_of,
    placement,
)
from src.astadhyayi.sources import register
from src.astadhyayi.vibhakti import (
    ending_facts,
    juncture,
    person_for,
)
from src.astadhyayi.vipratisedha import (
    eka_samjna,
    eka_samjna_of,
    vipratisedha,
    vipratisedha_of,
)

_RULES = {
    "1.4.1": (
        eka_samjna_of,
        "eka_samjna(candidates) -> the single name that stands, and what it "
        "displaced. Called from `nominal` wherever two saṃjñās meet.",
        "SETTLED — an adhikāra, and its scope is stated in its own words: "
        "आ एतस्मात् सूत्रावधेर् यद् इत ऊर्ध्वम् अनुक्रमिष्यामः, from here to "
        "2.2.38 कडाराः कर्मधारये. 1,163 sūtras stand under it.\n\n"
        "SETTLED — it is a नियम and not a grant, and that is the whole of it: "
        "अन्यत्र संज्ञासमावेशान् नियमार्थं वचनम्, एकैव संज्ञा भवति. Names "
        "ordinarily co-apply; this stretch is where they may not.\n\n"
        "SETTLED — which one stands? या परा, अनवकाशा च — the later, or the "
        "one with no other field at all. Both readings are codified, and the "
        "अनवकाश one is tried first, since a rule with nowhere else to go "
        "would otherwise be lost entirely.\n\n"
        "SETTLED — the Kāśikā works its own example and draws the "
        "consequence to the end. 1.4.10 ह्रस्वं लघु and 1.4.11 संयोगे गुरु "
        "both reach the short vowel of शिक्षा and भिक्षा; एका संज्ञा leaves "
        "गुरु; and so अततक्षत् and अररक्षत् do not get 7.4.93's सन्वद्भाव, "
        "which wants a लघु. The first two steps are codified. The third is "
        "not — 7.4.93 is not reached yet.\n\n"
        "SCOPE — one thing in the pāda contradicts it. The vārttika on 1.4.20 "
        "reads उभयसंज्ञान्यपि, giving the अयस्मय group *both* names. Recorded "
        "at 1.4.20 rather than modelled."
    ),
    "1.4.2": (
        vipratisedha_of,
        "vipratisedha(candidates) -> which rule prevails, and whether by "
        "1.4.2 or because the two were never of equal strength.",
        "SETTLED — the most cited paribhāṣā in the grammar, and the most "
        "often cited without its qualification. विप्रतिषेध is defined by a "
        "vārttika as तुल्यबलविरोध: यत्र द्वौ प्रसङ्गौ अन्यार्थौ एकस्मिन् युगपत् "
        "प्राप्नुतः स तुल्यबलविरोधो विप्रतिषेधः — two rules, each with a field "
        "of its own, both reaching one place at once.\n\n"
        "SETTLED — and where that equality is absent the sūtra says nothing. "
        "उत्सर्गापवादनित्यानित्यान्तरङ्गबहिरङ्गेषु तुल्यबलता नास्तीति नायम् अस्य "
        "योगस्य विषयः। बलवतैव तत्र भवितव्यम्. An exception beats the rule it "
        "excepts, an invariable rule beats a contingent one, an inner rule "
        "beats an outer — and any of the three may stand earlier. Codified as "
        "four relations rather than as one comparison of numbers, because "
        "'the later wins' read flat gets three families of case backwards.\n\n"
        "SETTLED — the worked example is 7.3.101/7.3.102 against 7.3.103, "
        "each with a scope of its own — वृक्षाभ्याम् for the first, वृक्षेषु "
        "for the second — and both reaching वृक्षेभ्यः. There the later is "
        "done.\n\n"
        "SETTLED — अप्रवृत्तौ पर्यायेण वा प्रवृत्तौ प्राप्तायां वचनम् आरभ्यते: "
        "without this sūtra the two would either both fail or alternate. "
        "That is what it is for.\n\n"
        "SCOPE — the four relations are given, not computed. Which of two "
        "rules is the apavāda, or the नित्य, or the अन्तरङ्ग, is a judgement "
        "about the pair that no property of either settles, and the "
        "commentaries argue about particular cases. The caller states it."
    ),
    "1.4.3": (
        nadi,
        "nadi(word, ...) -> the नदी saṃjñā, or the sūtra that withheld it.",
        "SETTLED — यू is ई and ऊ, and the निर्देश is अविभक्तिक: the sūtra's "
        "word carries no case ending, so it is the two sounds and not a form "
        "of them.\n\n"
        "SETTLED — स्त्र्याख्य is read with care, and the आख्या is what does "
        "it: आख्याग्रहणं किम्? शब्दार्थे स्त्रीत्व एव यथा स्यात्, पदान्तराख्ये "
        "मा भूत्. The femininity must be the word's own meaning, not something "
        "a neighbouring word supplies — ग्रामण्ये स्त्रियै has स्त्री beside it "
        "and ग्रामणी is still not a नदी.\n\n"
        "SETTLED — two counter-examples, one per condition. यू इति किम्? "
        "मात्रे, दुहित्रे. स्त्र्याख्याविति किम्? ग्रामणीः, सेनानीः, खलपूः.\n\n"
        "SCOPE — the vārttika प्रथमलिङ्गग्रहणं च is not codified."
    ),
    "1.4.4": (
        nadi,
        "The prohibition, and the exception for स्त्री itself.",
        "SETTLED — पूर्वेणातिप्रसक्ता नदीसंज्ञा प्रतिषिध्यते: 1.4.3 reached too "
        "far and this pulls it back. Where the ī or ū is the place an इयङ् or "
        "उवङ् substitute will occupy, no नदी — हे श्रीः, हे भ्रूः.\n\n"
        "SETTLED — अस्त्रीति किम्? हे स्त्रि. स्त्री is itself an इयङ्-place "
        "and is excepted by name, so it keeps the saṃjñā.\n\n"
        "SCOPE — 6.4.77's इयङ् and उवङ् are not codified, so whether a given "
        "word is an इयङ्-place is given rather than derived."
    ),
    "1.4.5": (
        nadi,
        "And before आम्, optionally.",
        "SETTLED — the prohibition of 1.4.4 lapses before आम् and the name is "
        "available again, but only as an option: वा. So both readings stand."
    ),
    "1.4.6": (
        nadi,
        "And a short ि or ु before a ṅit affix, optionally.",
        "SETTLED — the reach widens twice over: ह्रस्व rather than the long "
        "vowels of 1.4.3, and the condition is the following affix rather "
        "than the word itself.\n\n"
        "SETTLED — and this is where 1.4.7's शेष gets its second clause. A "
        "short ि-final feminine is ordinarily घि; before a ṅit it is नदी by "
        "this sūtra; and 1.4.1 allows one name only. The Kāśikā's definition "
        "of the remainder says exactly that — स्त्र्याख्यं च यन् न नदीसंज्ञकं "
        "स शेषः — and the codification performs the exclusion rather than "
        "assuming it."
    ),
    "1.4.7": (
        ghi,
        "ghi(word, ...) -> the घि saṃjñā, or the sūtra that withheld it.",
        "SETTLED — शेष is defined by the Kāśikā and not by the sūtra: "
        "ह्रस्वम् इवर्णोवर्णान्तं यन् न स्त्र्याख्यम्, स्त्र्याख्यं च यन् न "
        "नदीसंज्ञकं स शेषः. Two clauses, and the codification tests both. "
        "अग्नये, वायवे, कृतये, धेनवे.\n\n"
        "SETTLED — ह्रस्वः carries down from 1.4.6, which is what makes the "
        "final short rather than long. असखीति किम्? सख्या, सख्ये, सख्युः."
    ),
    "1.4.8": (
        ghi,
        "पति takes the name only inside a compound.",
        "SETTLED — एव is restrictive and the whole of the sūtra: outside a "
        "compound पति does not take it."
    ),
    "1.4.9": (
        ghi,
        "And in the Veda, construed with a genitive, optionally.",
        "SETTLED — three conditions at once — षष्ठीयुक्त, छन्दसि, वा — and the "
        "option is over 1.4.8's refusal rather than over 1.4.7's grant."
    ),
    "1.4.10": (
        weight,
        "weight(vowel) -> लघु or गुरु.",
        "SETTLED — मात्रिकस्य ह्रस्वसंज्ञा कृता, तस्यानेन लघुसंज्ञा विधीयते: "
        "1.2.27 already named the one-mātrā vowel ह्रस्व, and this names what "
        "carries that. So the two blocks join, and nothing is redefined.\n\n"
        "SETTLED — the saṃjñā is of the syllable and not the vowel alone — "
        "ह्रस्वम् अक्षरं लघुसंज्ञं भवति — which is why 1.4.11 can make it heavy "
        "on the strength of what follows. भेत्ता, छेत्ता, अचीकरत्."
    ),
    "1.4.11": (
        weight,
        "A short vowel before a conjunct is गुरु — 1.4.1 deciding between them.",
        "SETTLED — पूर्वेण लघुसंज्ञायां प्राप्तायां गुरुसंज्ञा विधीयते. Both "
        "names reach the same syllable, and 1.4.1 leaves the later: कुण्डा, "
        "हुण्डा, शिक्षा, भिक्षा. The codification calls `eka_samjna` rather "
        "than writing the outcome in, so the record shows which sūtra it beat."
    ),
    "1.4.12": (
        weight,
        "And a long vowel is गुरु, with no condition at all.",
        "SETTLED — संयोग इति नानुवर्तते, सामान्येन संज्ञाविधानम्: the condition "
        "of 1.4.11 does not carry down, so length alone is enough. "
        "ईहांचक्रे, ईक्षांचक्रे."
    ),
    "1.4.13": (
        anga,
        "anga(base, affix, prescribed_from=...) -> the अङ्ग, or why not.",
        "SETTLED — the saṃjñā 613 sūtras depend on, since 6.4.1 अङ्गस्य "
        "governs from there to 7.4.97. What it names is तदादि — whatever a "
        "suffix is prescribed after, together with everything following it.\n\n"
        "SETTLED — three words, three counter-examples, and each names what "
        "would go wrong. प्रत्यय: न्यविशत, व्यक्रीणीत — 1.3.17 prescribes after "
        "an *upasarga*, not after a suffix, so नि does not begin an aṅga. "
        "विधि: स्त्री इयती — merely standing before a suffix is not being "
        "prescribed after one. प्रत्यय again, and the Kāśikā asks why it is "
        "repeated: लुप्तप्रत्यये मा भूत् — श्र्यर्थम्, भ्र्वर्थम्, where the "
        "suffix has gone.\n\n"
        "SETTLED — तदादिवचनं स्यादिनुमर्थम् (vārt.): the तदादि is there for "
        "the स्य and the नुम् — करिष्यावः, कुण्डानि — which would fall outside "
        "an aṅga read as the base alone. Not codified; the reading is."
    ),
    "1.4.14": (
        pada_or_bha,
        "pada_or_bha(word, ...) -> पद or भ, and which sūtra gave it.",
        "SETTLED — सुप् and तिङ् are pratyāhāras, so the sūtra says 'whatever "
        "ends in a nominal or a verbal ending'. ब्राह्मणाः पठन्ति.\n\n"
        "SETTLED — the अन्त of अन्तम् is doing more than it looks. A vārttika "
        "reads it as barring tadantavidhi in saṃjñā rules generally — "
        "पदसंज्ञायाम् अन्तग्रहणम् अन्यत्र संज्ञाविधौ प्रत्ययग्रहणे तदन्तविधेः "
        "प्रतिषेधार्थम् — so गौरी ब्राह्मणितरा is not a pada. That is a "
        "restriction on 1.1.72, which is codified; the restriction is not."
    ),
    "1.4.15": (
        pada_or_bha,
        "A न-final before क्य is a pada.",
        "SETTLED — one of three extensions of 1.4.14 to things that do not "
        "end in सुप् or तिङ् at all."
    ),
    "1.4.16": (
        pada_or_bha,
        "And before a सित् affix.",
        "SETTLED — सित् is an affix marked with an indicatory स्, found by "
        "1.3.3, already codified."
    ),
    "1.4.17": (
        pada_or_bha,
        "And before the सुप् affixes other than सर्वनामस्थान.",
        "SETTLED — स्वादिषु is read as a range and the Kāśikā fixes both ends: "
        "सुशब्दाद् एकवचनाद् आरभ्य आ कपः, from 4.1.2's सु to 5.4.151's कप्. "
        "राजभ्याम्, राजभिः, राजत्वम्, राजतरः.\n\n"
        "SETTLED — असर्वनामस्थान इति किम्? राजानौ, राजानः."
    ),
    "1.4.18": (
        pada_or_bha,
        "But before a य- or vowel-initial one of those, भ instead.",
        "SETTLED — पूर्वेण पदसंज्ञायां प्राप्तायां तदपवादो भसंज्ञा विधीयते, so "
        "this is an apavāda and not a विप्रतिषेध. Both names reach the same "
        "place and 1.4.1 leaves one. गार्ग्यः, वात्स्यः; दाक्षिः, प्लाक्षिः.\n\n"
        "SETTLED — the name matters because 6.4.129 भस्य governs from there "
        "to 6.4.175, which is 47 sūtras waiting on this one.\n\n"
        "SCOPE — two vārttikas extend it: नभोऽङ्गिरोमनुषां वति (नभस्वत्, "
        "अङ्गिरस्वत्, मनुष्वत्) and वृषण्वस्वश्वयोः (वृषण्वसुः, वृषणश्वस्य). "
        "Neither codified."
    ),
    "1.4.19": (
        pada_or_bha,
        "And a त- or स-final before a matvartha suffix.",
        "SETTLED — उदश्वित्वान् घोषः, विद्युत्वान् बलाहकः; यशस्वी, पयस्वी. "
        "तसाविति किम्? तक्षवान् ग्रामः, where the final is neither."
    ),
    "1.4.20": (
        pada_or_bha,
        "And the अयस्मय group, in the Veda.",
        "SETTLED — an option in the Veda.\n\n"
        "OPEN — the vārttika reads उभयसंज्ञान्यपीति वक्तव्यम्, that these take "
        "*both* names. Under 1.4.1 आ कडारादेका संज्ञा that should be "
        "impossible, and 1.4.20 stands squarely inside 1.4.1's scope. Whether "
        "the vārttika is overriding the adhikāra, or reading the option as "
        "covering both names in turn, is not settled here. Recorded, not "
        "modelled — `pada_or_bha` returns भ."
    ),
    "1.4.21": (
        vacana,
        "vacana(count) -> which of the three numbers.",
        "SETTLED — these two do not prescribe the endings. 4.1.2 and 3.4.78 "
        "already did that सामान्येन; what these add is the meaning — "
        "तस्यानेन बहुत्वसंख्या वाच्यत्वेन विधीयते, बहुत्वम् अस्य वाच्यं भवति.\n\n"
        "SETTLED — and the number is the कारक's, not the word's: कर्मादयोऽप्य् "
        "अपरे विभक्तीनाम् अर्था वाच्याः, तदीये बहुत्वे बहुवचनम्. So the plural "
        "of a verb answers to the plurality of its agent, which is what makes "
        "1.4.21 a bridge to the kāraka section beginning at 1.4.23.\n\n"
        "SETTLED — यत्र च संख्या संभवति तत्रायम् उपदेशः. An indeclinable has no "
        "number, and takes its endings by the general rule regardless."
    ),
    "1.4.22": (
        vacana,
        "Two and one, dual and singular.",
        "SETTLED — ब्राह्मणौ पठतः, ब्राह्मणः पठति. यथासंख्यम् by 1.3.10: two "
        "senses against two endings, equal in number, so they pair off in "
        "order."
    ),
}

#: Verified by reading the branch. Declared on the first sūtra of a block
#: where one resolver serves several: it is one function and one fact, and
#: repeating it down the block would say the same thing nine times.
#:
#:   1.4.7  `ghi` calls `nadi` before deciding, because शेष means the
#:          remainder and 1.4.6 has already taken the ṅit-affix case away.
#:          The exclusion is performed, not assumed.
#:   1.4.10 `weight` and
#:   1.4.14 `pada_or_bha` both settle competing names through 1.4.1's
#:          `eka_samjna` rather than ordering their own branches.
_RULES_REUSES = {
    "1.4.7": ("1.4.6",),
    "1.4.10": ("1.4.1",),
    "1.4.14": ("1.4.1",),
}

for _sutra, (_fn, _codification, _notes) in _RULES.items():
    register(_sutra, apply=_fn, codification=_codification, notes=_notes,
             reuses=_RULES_REUSES.get(_sutra, ()))


# --- 1.4.23 to 1.4.55: the kārakas ----------------------------------------
#
# Registered from `karaka.PROVISIONS`, like the other two provision blocks.
# The notes are hand-written where there is interpretation to record and
# derived from the table otherwise; the codification line is always the
# table's own rendering, so it cannot say something the resolver does not do.

_KARAKA_NOTES = {
    "1.4.23": (
        "SETTLED — an adhikāra over everything to 1.4.55, and a condition and "
        "not a heading: कारक इति विशेषणम् अपादानादिसंज्ञाविषयम् अधिक्रियते. "
        "So it must be satisfied before any of the six names is even in "
        "question.\n\n"
        "SETTLED — and what it means is stated flatly: कारकशब्दश्च "
        "निमित्तपर्यायः, कारकं हेतुरित्यनर्थान्तरम् — कारक is a synonym for "
        "'cause', and कारक and हेतु are not two things. Cause of what? "
        "क्रियायाः, of the action.\n\n"
        "SETTLED — two counter-examples, and both are the same shape: a "
        "genuine relation that is not a causal one. वृक्षस्य पर्णं पतति, "
        "कुड्यस्य पिण्डः पतति — the tree and the wall are there, and neither "
        "is a cause of the falling. माणवकस्य पितरं पन्थानं पृच्छति likewise, "
        "against 1.4.51's माणवकं पन्थानं पृच्छति. The codification returns no "
        "name at all where nothing is asserted, and cites this sūtra for it."
    ),
    "1.4.24": (
        "SETTLED — ध्रुवं यद् अपाययुक्तम्, अपाये साध्ये यद् अवधिभूतम्: the "
        "fixed point, where a going away is what is being brought about. "
        "ग्रामाद् आगच्छति, पर्वताद् अवरोहति, रथात् पतितः. The fixity is "
        "relative to the movement and not absolute — the village does not "
        "move, but neither need it be still in any other sense.\n\n"
        "SETTLED — the vārttika जुगुप्साविरामप्रमादार्थानाम् adds three verb "
        "classes where the 'departure' is figurative: अधर्माज् जुगुप्सते "
        "(loathing), अधर्माद् विरमति (desisting), धर्मात् प्रमाद्यति (being "
        "careless of). Codified as a separate provision so the extension is "
        "visible as one."
    ),
    "1.4.38": (
        "SETTLED — this sūtra exists only to move a case later. 1.4.37 gave "
        "क्रुध् and द्रुह् सम्प्रदान; with an upasarga this gives them कर्मन्, "
        "which is later, and 1.4.1 एका संज्ञा then leaves कर्मन् standing. "
        "देवदत्ताय क्रुध्यति against देवदत्तम् अभिक्रुध्यति.\n\n"
        "SETTLED — and the pair is the clearest demonstration in the section "
        "that the *order* of the six names is the mechanism. Read without "
        "1.4.1 this sūtra would merely add a second name and change nothing."
    ),
    "1.4.42": (
        "SETTLED — the तमप् is the whole of it. क्रियासिद्धौ यत् "
        "प्रकृष्टोपकारकं विवक्षितम् — the *most* effective, not merely an "
        "effective one. दात्रेण लुनाति, परशुना छिनत्ति.\n\n"
        "SETTLED — तमब्ग्रहणं किम्? गङ्गायां घोषः, कूपे गर्गकुलम्. Both are "
        "means of a sort and neither is the most effective, so both fall to "
        "1.4.45's अधिकरण instead."
    ),
    "1.4.45": (
        "SETTLED — आध्रियन्तेऽस्मिन् क्रिया इत्याधारः, and the Kāśikā is "
        "precise about whose action: कर्तृकर्मणोः क्रियाश्रयभूतयोः "
        "धारणक्रियां प्रति य आधारः — the support of the agent or the object, "
        "which are themselves the seat of the action. कटे आस्ते, स्थाल्यां "
        "पचति."
    ),
    "1.4.49": (
        "SETTLED — कर्तुः क्रियया यद् आप्तुम् इष्टतमम्. Two words earn "
        "counter-examples. कर्तुः: माषेष्व् अश्वं बध्नाति — कर्मण ईप्सिता "
        "माषा न कर्तुः, the beans are wanted by the horse and not by the man, "
        "so they are no कर्मन्. तमप्: पयसौदनं भुङ्क्ते, where the milk is "
        "wanted but not most wanted.\n\n"
        "SETTLED — and कर्म is said a second time though it was already "
        "carried down, for a reason the Kāśikā states: पुनः कर्मग्रहणम् "
        "आधारनिवृत्त्यर्थम्, इतरथा आधारस्यैव हि स्यात्. Without it गेहं "
        "प्रविशति would come out अधिकरण, and ओदनं पचति and सक्तून् पिबति "
        "would fail. That is 1.4.1 again, from the other side: the repetition "
        "is what keeps कर्मन् in contention at all."
    ),
    "1.4.51": (
        "SETTLED — the residue clause of the kāraka section, and it works "
        "like 1.3.78's शेषात्: whatever is a kāraka and has been given no "
        "other name is कर्मन्. माणवकं पन्थानं पृच्छति — the boy is not the "
        "thing asked for, so no other name reaches him.\n\n"
        "SETTLED — कारक carries down from 1.4.23 and does real work here, "
        "because this rule would otherwise reach anything at all. माणवकस्य "
        "पितरं पन्थानं पृच्छति: the boy in the genitive is related to the "
        "father, not a cause of the asking, so अकथित does not make him a "
        "कर्मन्.\n\n"
        "SCOPE — the vārttika अकर्मकधातुभिर्योगे देशः कालो भावो गन्तव्योऽध्वा "
        "च कर्मसंज्ञकः extends it to place, time, state and distance with "
        "intransitive verbs. Not codified."
    ),
    "1.4.52": (
        "SETTLED — five classes of verb, and with the causative of any of "
        "them what was the agent of the simple verb becomes the object: "
        "माणवकं ग्रामं गमयति. The condition अणि — 'when not causative' — is "
        "about the earlier state of the same participant, which is why the "
        "codification carries it as an assertion (अणौ-कर्ता) and not as a "
        "property of the form in hand.\n\n"
        "SCOPE — seven vārttikas hang on this sūtra, four of them "
        "restricting it: जल्पतिप्रभृतीनाम् and दृशेश्च extend, while "
        "अदिखाद्योर्न, नीवह्योर्न, भक्षेरहिंसार्थस्य न and शब्दायतेर्न cut "
        "back, and नियन्तृकर्तृकस्य वहेरनिषेधः cuts back the cutting back. "
        "None codified — the codification takes the five classes as the sūtra "
        "gives them."
    ),
    "1.4.54": (
        "SETTLED — स्वतन्त्र is glossed प्रधानभूतः अगुणभूतः: the one presented "
        "as principal rather than subordinate. And presented is the word — यः "
        "क्रियासिद्धौ स्वातन्त्र्येण विवक्ष्यते, the one *intended* as "
        "independent. So it is a fact about how the speaker frames the event "
        "and not about the world, which is why स्थाली पचति stands beside "
        "देवदत्तः पचति: a pot may be the agent if it is put forward as one.\n\n"
        "SETTLED — being last of the six, it displaces every other name under "
        "1.4.1. That is not incidental to the arrangement; it is why the "
        "agent, which could be described as a means or a locus too, always "
        "comes out कर्तृ."
    ),
    "1.4.55": (
        "SETTLED — and here the section breaks its own governing rule, "
        "deliberately and with the reason given. तत्प्रयोजको हेतुश्च: the च "
        "makes both names apply at once, and the Kāśikā says so outright — "
        "संज्ञासमावेशार्थश्चकारः. Under 1.4.1 that should be impossible.\n\n"
        "SETTLED — why both are needed: हेतुत्वाद् णिचो निमित्तं, "
        "कर्तृत्वाच्च कर्तृप्रत्ययेनोच्यते. As हेतु the causer is what "
        "3.1.26's णिच् answers to; as कर्तृ it is what the personal ending "
        "expresses. Drop either name and one of the two fails. "
        "कुर्वाणं प्रयुङ्क्ते, कारयति, हारयति.\n\n"
        "SETTLED — this bears directly on the OPEN note at 1.4.20, where a "
        "vārttika gives the अयस्मय group both पद and भ against the same "
        "adhikāra. Here the same move is made in a sūtra, with a च and an "
        "explicit statement of purpose. So संज्ञासमावेश is evidently "
        "restorable within 1.4.1's scope; what is unsettled at 1.4.20 is "
        "whether a vārttika alone can do it."
    ),
}


def _register_karaka() -> None:
    grouped = {}
    for provision in KARAKA_PROVISIONS:
        grouped.setdefault(provision.sutra.split("v")[0], []).append(provision)

    register(
        "1.4.23",
    reuses=('1.4.1',),
        apply=karaka_of,
        codification=(
            "The condition every one of the six waits on. `karaka_of` returns "
            "no name and cites this sūtra where nothing is asserted."
        ),
        notes=_KARAKA_NOTES["1.4.23"],
    )

    for sutra in sorted(grouped, key=lambda s: int(s.rsplit(".", 1)[1])):
        provisions = grouped[sutra]
        codification = " · ".join(
            dict.fromkeys(p.describe() for p in provisions))
        note = _KARAKA_NOTES.get(sutra)
        if note is None:
            first = provisions[0]
            note = "SETTLED — " + first.gloss + "."
            worked = [p.example for p in provisions if p.example]
            against = [p.counter for p in provisions if p.counter]
            if worked:
                note += " Worked as " + "; ".join(dict.fromkeys(worked)) + "."
            if against:
                note += (" Its counter-example is "
                         + "; ".join(dict.fromkeys(against)) + ".")
        register(sutra, apply=karaka_of, codification=codification, notes=note)


_register_karaka()


# --- 1.4.56 to 1.4.110: the particles, the endings, and the close ---------

_TAIL_NOTES = {
    "1.4.56": (
        "SETTLED — an adhikāra stated as a range: from here to 1.4.97\n"
        "  अधिरीश्वरे, whatever is taught is a निपात. प्रागेतस्माद् अवधेर् यान्\n"
        "  इत ऊर्ध्वम् अनुक्रमिष्यामः निपातसंज्ञास्ते वेदितव्याः.\n"
        "\n"
        "SETTLED — and the reason it is a range rather than a list is the\n"
        "  important part: प्राग्वचनं संज्ञासमावेशार्थम्।\n"
        "  गत्युपसर्गकर्मप्रवचनीयसंज्ञाभिः सह निपातसंज्ञा समाविशति. The form of\n"
        "  the statement is chosen so that निपात may stand *alongside* गति,\n"
        "  उपसर्ग and कर्मप्रवचनीय, which 1.4.1 आ कडारादेका संज्ञा would\n"
        "  otherwise forbid. So `classify` returns a set of names.\n"
        "\n"
        "SETTLED — even the र् of रीश्वरात् is deliberate: रेफोच्चारणम्\n"
        "  ईश्वरे तोसुन्कसुनौ इत्ययम् अवधिर् मा विज्ञायि इति — pronounced so\n"
        "  that the limit is not mistaken for 3.4.13, which also has ईश्वरे."
    ),
    "1.4.57": (
        "SETTLED — प्रसज्यप्रतिषेधोऽयम्, सत्त्वमिति द्रव्यमुच्यते: the negation\n"
        "  is of the whole, and सत्त्व means a substance. पशुर्वै पुरुषः is the\n"
        "  counter-example — there पशु names a thing.\n"
        "\n"
        "SETTLED — चादि is an ākṛtigaṇa of 155 members in the corpus, and the\n"
        "  Kāśikā lists them out. Read, not typed."
    ),
    "1.4.58": (
        "SETTLED — the प्रादि gaṇa is closed and has exactly twenty-two\n"
        "  members, which are the twenty-two upasargas: प्र, परा, अप, सम्, अनु,\n"
        "  अव, निस्, निर्, दुस्, दुर्, वि, आङ्, नि, अधि, अपि, अति, सु, उद्, अभि,\n"
        "  प्रति, परि, उप. Read off the gaṇapāṭha.\n"
        "\n"
        "SCOPE — two vārttikas add मरुत् and श्रत्. Not codified."
    ),
    "1.4.59": (
        "SETTLED — क्रियायोगे is the whole condition, and the counter-example\n"
        "  turns on it: प्रगतो नायकोऽस्माद् देशात् प्रनायको देशः — there प्र is\n"
        "  not construed with a verb, so no उपसर्ग, and 7.4.47's त् does not\n"
        "  come. प्रणयति, परिणयति against प्रनायकः."
    ),
    "1.4.60": (
        "SETTLED — two devices in one short sūtra, and the Kāśikā names both.\n"
        "\n"
        "  चकारः संज्ञासमावेशार्थः — the च is so that गति stands *beside*\n"
        "  उपसर्ग rather than displacing it. Both names are wanted: गति for\n"
        "  6.2.49's accent, उपसर्ग for 8.4.14's ण and 8.3.65's ष.\n"
        "\n"
        "  योगविभाग उत्तरार्थः — and गति was split off into its own sūtra\n"
        "  rather than added to 1.4.59, so that everything from 1.4.61 on gets\n"
        "  गति *only*: उत्तरत्र गतिसंज्ञैव यथा स्यात्, उपसर्गसंज्ञा मा भूत्.\n"
        "  Otherwise ऊरीस्यात् would take 8.3.87's ṣatva. The codification\n"
        "  carries the split — the ūryādi provisions give one name where the\n"
        "  prādi ones give two.\n"
        "\n"
        "SCOPE — three vārttikas: कारिकाशब्दस्य, पुनश्चनसौ छन्दसि, and\n"
        "  दुरः षत्वणत्वयोः उपसर्गत्वप्रतिषेधः. None codified."
    ),
    "1.4.62": (
        "SETTLED — two conditions and the second is easy to lose: अनुकरणम्\n"
        "  *च अनितिपरम्*, an imitative word and not one followed by इति.\n"
        "  खाट्कृत्य, but not खाट् इति कृत्वा. An earlier draft of the\n"
        "  codification omitted both conditions, and the provision then fired\n"
        "  for every word construed with a verb — which is the failure mode of\n"
        "  a rule whose conditions are all semantic."
    ),
    "1.4.80": (
        "SETTLED — ते is there for the उपसर्गs alone: तेग्रहणम् उपसर्गार्थम्,\n"
        "  गतयो ह्यनन्तराः — a गति is adjacent to the root anyway, so only the\n"
        "  उपसर्गs needed placing."
    ),
    "1.4.83": (
        "SETTLED — a second adhikāra of the same shape as 1.4.56, running to\n"
        "  1.4.98: यान् इत ऊर्ध्वम् अनुक्रमिष्यामः कर्मप्रवचनीयसंज्ञास्ते\n"
        "  वेदितव्याः, अधिरीश्वरे इति यावत्.\n"
        "\n"
        "SETTLED — and what divides these from the उपसर्गs of 1.4.59 is one\n"
        "  thing only: क्रियायोगे. The same word is an उपसर्ग when construed\n"
        "  with a verb and a कर्मप्रवचनीय when it is not."
    ),
    "1.4.90": (
        "SETTLED — three words against five senses, and the mismatch is the\n"
        "  point. This is the sūtra 1.3.10 यथासंख्यम् uses as its\n"
        "  counter-example: समानामिति किम्? Because the numbers are unequal the\n"
        "  words do *not* pair off with the senses, and each of प्रति, परि and\n"
        "  अनु holds for any of the five. The codification of 1.3.10 refuses\n"
        "  rather than truncating, and this is the case it refuses for."
    ),
    "1.4.97": (
        "SETTLED — the sūtra 1.4.56's प्राक् stops short of, and 1.4.83's\n"
        "  runs up to. So the कर्मप्रवचनीय name comes from the heading and the\n"
        "  निपात name does not — though अधि is प्रादि and so a निपात by 1.4.58\n"
        "  in any case, which is what the codification returns."
    ),
    "1.4.99": (
        "SETTLED — and here the name is finally given to what 1.3.12 has been\n"
        "  using for ninety-odd sūtras. लः is a genitive looking forward to\n"
        "  the substitutes — लादेशाः परस्मैपदसंज्ञा भवन्ति — so what is named\n"
        "  is not ल् but the nine endings that replace it: तिप्, तस्, झि; सिप्,\n"
        "  थस्, थ; मिप्, वस्, मस्. And शतृ and क्वसु with them.\n"
        "\n"
        "SCOPE — 3.4.78, which teaches the eighteen, is not codified, so the\n"
        "  list is the Kāśikā's."
    ),
    "1.4.101": (
        "SETTLED — the sūtra says त्रीणि त्रीणि and the arrangement does the\n"
        "  rest. Eighteen endings, nine of each pada, each nine in three rows\n"
        "  of three; and the three rows are प्रथम, मध्यम, उत्तम in order. The\n"
        "  Kāśikā sets all eighteen out in exactly that shape, and the\n"
        "  codification indexes them by position rather than naming each.\n"
        "\n"
        "SETTLED — 1.4.102 then takes each row three at a time — एकशः — for\n"
        "  the three numbers, and 1.4.103 says the same of सुप्. Four sūtras\n"
        "  that do nothing separately, so they are answered together."
    ),
    "1.4.105": (
        "SETTLED — स्थानिनि is the word that carries the weight, and the\n"
        "  Kāśikā unpacks it as प्रयुज्यमानेऽप्यप्रयुज्यमानेऽपि: whether the\n"
        "  pronoun is actually uttered or not. That is why पचसि alone is second\n"
        "  person with no त्वम् anywhere. It also widens the adjacency —\n"
        "  व्यवहिते चाव्यवहिते, separated or not."
    ),
    "1.4.106": (
        "SETTLED — प्रहासः परिहासः क्रीडा, and the rule is a joke made\n"
        "  grammatical. In mockery with मन् beside it, the main verb takes the\n"
        "  *second* person and मन् itself the *first*: एहि मन्ये ओदनं भोक्ष्यसे\n"
        "  — 'come, I think you will eat the rice' — नहि भोक्ष्यसे, भुक्तः\n"
        "  सोऽतिथिभिः, 'no you won't, the guests have eaten it'.\n"
        "\n"
        "SETTLED — मध्यमोत्तमयोः प्राप्तयोर् उत्तममध्यमौ विधीयेते: the two are\n"
        "  exchanged, which is what makes the construction what it is. And एकवत्\n"
        "  — मन्ये stays singular whatever the number.\n"
        "\n"
        "SETTLED — प्रहासे इति किम्? एहि मन्यसे ओदनं भोक्ष्ये: said seriously,\n"
        "  the persons fall where they ordinarily would."
    ),
    "1.4.108": (
        "SETTLED — the residue clause of the three persons, and the same shape\n"
        "  as 1.3.78 शेषात् for the two padas: what the earlier rules have not\n"
        "  claimed falls here."
    ),
    "1.4.109": (
        "SETTLED — परशब्दोऽतिशये वर्तते, संनिकर्षः प्रत्यासत्तिः: not merely\n"
        "  proximity but the closest, and the Kāśikā measures it —\n"
        "  अर्धमात्राकालव्यवधानम्, an interval of half a mātrā. दध्यत्र,\n"
        "  मध्वत्र.\n"
        "\n"
        "SETTLED — this is the condition 1.2.39 स्वरितात् संहितायाम् was\n"
        "  already using, ninety sūtras before it is defined here. Ordinary in\n"
        "  this text, and worth recording rather than smoothing over: the\n"
        "  Aṣṭādhyāyī is not written to be read once forwards."
    ),
    "1.4.110": (
        "SETTLED — विरतिर्विरामः, or विरम्यतेऽनेनेति वा विरामः: the stopping,\n"
        "  or that by which one stops. दधिँ, मधुँ.\n"
        "\n"
        "SETTLED — and the Kāśikā notices something about how the name is used\n"
        "  later. In 8.3.15 खरवसानयोर्विसर्जनीयः the locative is a विषयसप्तमी\n"
        "  with respect to अवसान and a परसप्तमी with respect to खर् — one\n"
        "  ending doing two jobs in one word, पौर्वापर्याभावात्, because a stop\n"
        "  has nothing after it to be 'before'. Not modelled; 8.3.15 is not\n"
        "  codified.\n"
        "\n"
        "SETTLED — the last sūtra of adhyāya 1."
    ),
}


def _tail_note(sutra, provisions=None):
    note = _TAIL_NOTES.get(sutra)
    if note is not None:
        return note
    if not provisions:
        return None
    first = provisions[0]
    note = "SETTLED — " + first.gloss + "."
    worked = [p.example for p in provisions if p.example]
    against = [p.counter for p in provisions if p.counter]
    if worked:
        note += " Worked as " + "; ".join(dict.fromkeys(worked)) + "."
    if against:
        note += " Its counter-example is " + "; ".join(
            dict.fromkeys(against)) + "."
    return note


def _register_tail() -> None:
    # 1.4.56, 1.4.83 and 1.4.80–1.4.82 contribute no provision of their own.
    for sutra, codification in (
        ("1.4.56", "in_nipata_range(sutra) -> whether 1.4.56's प्राक् reaches "
                   "it, and so whether निपात is added to the names."),
        ("1.4.60", "No provision of its own: its च is what makes 1.4.59 "
                   "give two names rather than one, and its yogavibhāga is "
                   "what makes 1.4.61 onwards give गति alone."),
        ("1.4.80", "placement(particle) -> where an उपसर्ग or गति stands."),
        ("1.4.81", "The same, with छन्दसि allowing it to follow the root."),
        ("1.4.82", "And with छन्दसि allowing it to stand apart."),
        ("1.4.83", "The second range, 1.4.83 to 1.4.98."),
    ):
        register(sutra, apply=names_of, codification=codification,
                 notes=_tail_note(sutra) or "SETTLED — see the block note.")

    grouped = {}
    for provision in NIPATA_PROVISIONS:
        grouped.setdefault(provision.sutra, []).append(provision)
    for sutra in sorted(grouped, key=lambda s: int(s.rsplit(".", 1)[1])):
        provisions = grouped[sutra]
        register(
            sutra, apply=names_of,
            codification=" · ".join(
                dict.fromkeys(p.describe() for p in provisions)),
            notes=_tail_note(sutra, provisions),
        )

    for sutra, fn, codification in (
        ("1.4.99", ending_facts,
         "ending_facts(ending) -> its pada, person and number together."),
        ("1.4.100", ending_facts, "The same, for the ātmanepada nine."),
        ("1.4.101", ending_facts,
         "The eighteen indexed by position: row gives the person."),
        ("1.4.102", ending_facts, "And position within the row, the number."),
        ("1.4.103", ending_facts, "The same for सुप्. Not separately modelled."),
        ("1.4.104", ending_facts, "And both sets are called विभक्ति."),
        ("1.4.105", person_for, "person_for(upapada=...) -> which person."),
        ("1.4.106", person_for, "The प्रहास case, where the two are swapped."),
        ("1.4.107", person_for, "अस्मद् → uttama."),
        ("1.4.108", person_for, "The residue → prathama."),
        ("1.4.109", juncture, "juncture(gap_matras=...) -> संहिता."),
        ("1.4.110", juncture, "juncture(stopped=True) -> अवसान."),
    ):
        register(sutra, apply=fn, codification=codification,
                 notes=_tail_note(sutra)
                 or "SETTLED — answered together with the sūtras it works "
                    "with; see the note on the first of them.")


_register_tail()


__all__ = [
    "KARAKA_PROVISIONS",
    "NIPATA_PROVISIONS",
    "ending_facts",
    "in_nipata_range",
    "juncture",
    "names_of",
    "person_for",
    "placement",
    "anga",
    "karaka_of",
    "eka_samjna",
    "ghi",
    "nadi",
    "pada_or_bha",
    "vacana",
    "vipratisedha",
    "weight",
]
