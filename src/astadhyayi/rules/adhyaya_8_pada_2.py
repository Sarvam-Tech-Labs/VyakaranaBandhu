# -*- coding: utf-8 -*-
"""अध्याय ८, पाद २ — the tripādī, and what cannot see it."""

from __future__ import annotations

from src.astadhyayi.anga import sasajuso_ruh
from src.astadhyayi.asiddha import blocks_vipratisedha, visible
from src.astadhyayi.nalopa_matup import in_the_word
from src.astadhyayi.samyoganta import at_the_end
from src.astadhyayi.nistha_natva import the_nistha
from src.astadhyayi.ru_adesa import the_word_end
from src.astadhyayi.pluta import the_pluta
from src.astadhyayi.sources import register



register(
    '8.2.1',
    apply=visible,
    codification=(
        "visible(done, to, ...) -> whether one rule's work is visible to another; blocks_vipratisedha(a, b) -> whether 1.4.2 is switched off for the pair."
    ),
    notes=(
        'SETTLED — an adhikāra to the end of the text, 8.4.68, and it\n'
        '  runs in *two* directions, both of which the Kāśikā states.\n'
        '  The whole tripādī is asiddha to the seven adhyāyas and a\n'
        '  quarter before it — एतस्याम् अयं पादोनोऽध्यायोऽसिद्धो भवति —\n'
        '  and within the tripādī each later sūtra is asiddha to each\n'
        '  earlier: इत उत्तरं चोत्तर उत्तरो योगः पूर्वत्र पूर्वत्रासिद्धो\n'
        '  भवति. The second is the one easily missed and does most of\n'
        '  the work. Both are codified.\n'
        '\n'
        'SETTLED — what asiddhatva *is*: सिद्धकार्यं न करोतीत्यर्थः. And\n'
        '  what it is for, in two halves: आदेशलक्षणप्रतिषेधार्थम्\n'
        '  उत्सर्गलक्षणभावार्थं च — so a substitute shall not become the\n'
        '  cause of a further operation, and what it replaced shall go\n'
        '  on being one.\n'
        '\n'
        'SETTLED — the sharpest consequence, and the reason this sūtra\n'
        '  matters as much as 1.4.2 itself: **1.4.2 stops working here.**\n'
        '  येन पूर्वेण लक्षणेन सह स्पर्धते परं लक्षणम्, तत् प्रति\n'
        '  तस्यासिद्धत्वात् न प्रवर्तते — a later rule cannot compete\n'
        '  with an earlier one it is invisible to, so there is no\n'
        '  contest to settle and the earlier simply stands. विस्फोर्यम्,\n'
        "  अवगोर्यम्: the guṇa is not displaced by 8.2.77's lengthening\n"
        '  though that stands later. Codified as `blocks_vipratisedha`.\n'
        '\n'
        'SETTLED — two things escape it. The case-endings of the\n'
        "  tripādī's own sūtras are read by 1.1.49, 1.1.66 and 1.1.67\n"
        '  regardless, because कार्यकालं हि संज्ञापरिभाषम् — a paribhāṣā\n'
        '  is invoked at the moment it is wanted and so is never\n'
        "  'earlier' than what it reads. And an अपवाद is visible even\n"
        '  standing later: अपवादस्य तु परस्यापि उत्सर्गे कर्तव्ये\n'
        '  वचनप्रामाण्याद् असिद्धत्वं न भवति.\n'
        '\n'
        'SCOPE — the Kāśikā works six forms through the rule —\n'
        '  शुष्किका, शुष्कजङ्घा, क्षामिमान्, औजढत्, गुडलिण्मान् and the\n'
        '  rest — and none is derived here. What is codified is the\n'
        '  visibility relation, which is what a derivation would consult;\n'
        '  the derivations themselves need an engine that does not exist\n'
        '  yet.'
    ),
)


register(
    '8.2.2',
    apply=visible,
    codification=(
        'visible(done_is_nalopa=True, operation=...) -> and the four operations it is asiddha in.'
    ),
    notes=(
        'SETTLED — a नियम and not a grant, which is the whole of it:\n'
        '  अत्र सिद्धे सत्यारम्भो नियमार्थः — एतेष्वेव नलोपोऽसिद्धो\n'
        '  भवति, नान्यत्र. The न्-elision is asiddha in a sup-operation,\n'
        '  an accent-operation, a saṃjñā-operation and a tuk before a\n'
        '  kṛt, and *nowhere else*. So राजभिः keeps its भिस् against\n'
        '  7.1.9, and पञ्च ब्राह्मण्यः still counts as षट् by 1.1.24 —\n'
        '  but राजीयति, राजायते and राजाश्व come out with the elision\n'
        '  fully visible.\n'
        '\n'
        'SETTLED — the tuk clause is arguably redundant, and the Kāśikā\n'
        '  says why it is there anyway: some hold that\n'
        '  सन्निपातलक्षणो विधिर् अनिमित्तं तद्विघातस्य would settle it,\n'
        '  or the bahiraṅga rule; तत् तु क्रियते परिभाषाद्वयस्य\n'
        '  अनित्यत्वं ज्ञापयितुम् — it is stated to show that those two\n'
        '  paribhāṣās are not invariable. A sūtra put there to make a\n'
        '  point about two other rules.'
    ),
)


register(
    '8.2.3',
    apply=visible,
    codification=(
        'visible(done_is_mu=True, applying_nabhava=True) -> and the exception inside the narrowing.'
    ),
    notes=(
        'SETTLED — मुभावो नाभावे कर्तव्ये नासिद्धो भवति, किं तर्हि?\n'
        '  सिद्ध एव. Without it the मु of अमुना could not bring on\n'
        "  7.3.120's नाभाव, which wants a घि.\n"
        '\n'
        'SETTLED — and the Kāśikā notes a second effect got for free.\n'
        "  Once the नाभाव is done, 7.3.102's lengthening threatens; it\n"
        '  does not come, because सन्निपातलक्षणो विधिर् अनिमित्तं\n'
        '  तद्विघातस्य — an operation conditioned by a combination does\n'
        '  not destroy that combination.\n'
        '\n'
        'SCOPE — nine vārttikas hang on this sūtra. They come from\n'
        '  Kātyāyana and reach us through the bhāṣya, and only TWO are in this\n'
        '  corpus to be checked: एकादेशस्वरोऽन्तरङ्गः in the Kāśikā and\n'
        '  निष्ठादेशः षत्वस्वरप्रत्ययविधीड्विधिषु under the vārttika source.\n'
        '  The remaining seven below are reported from the literature and are\n'
        '  not verifiable against anything on disk. Each\n'
        '  declaring some further operation सिद्ध where 8.2.1 would have\n'
        '  hidden it: एकादेशस्वरोऽन्तरङ्गः, संयोगान्तलोपो रोरुत्वे,\n'
        '  सिज्लोप एकादेशे, निष्ठादेशः षत्वस्वरप्रत्ययविधीड्विधिषु,\n'
        '  प्लुतविकारस्तुग्विधौ छे, श्चुत्वं धुटि, अभ्यासजश्त्वचर्त्वे\n'
        '  एत्वतुकोः, द्विर्वचने परसवर्णत्वम्, and the nine of\n'
        '  पदाधिकारश्चेत्. None codified. Together they are a substantial\n'
        '  qualification of 8.2.1 and the largest single body of\n'
        '  uncodified vārttika material this project has met.'
    ),
)


register(
    '8.2.66',
    apply=sasajuso_ruh,
    codification='sasajuso_ruh(pada) -> the pada with its final स् as रु.',
    related=('8.2.1', '8.3.15'),
    notes=(
        'SETTLED — सकारान्तस्य पदस्य सजुष् इत्येतस्य च रुर्भवति:\n'
        '  अग्निरत्र, वायुरत्र.\n'
        '\n'
        'SETTLED — the रु is a step and not a result. 8.3.15 turns it into\n'
        '  the visarga one actually hears, and the two are kept apart\n'
        '  because they part company before a vowel, where the र् stays a\n'
        '  र्: अग्निरत्र, not *अग्निःअत्र.\n'
        '\n'
        'NOTE — it stands in the tripādī, so what it does is असिद्ध to\n'
        '  everything before 8.2.1. The engine asks rather than assumes.'
    ),
)


_IN_THE_WORD = (
    'in_the_word(word, gana=..., before=..., sense=..., chandasi=...) '
    '-> the accent of a merged vowel, the n dropped, the v of matup '
    'and r becoming l, by rule of 8.2.4-22.'
)

register(
    '8.2.4',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य — after a यण् that\n'
        '  stands for an उदात्त or a स्वरित, a following अनुदात्त becomes\n'
        '  स्वरित: **कुमार्यौ, कुमार्यः** for the first, **सकृल्ल्व्याशा,\n'
        '  खलप्व्याशा** for the second. The derivation is worth following:\n'
        '  6.1.161 puts the accent on the ई of कुमारी, that ई becomes य् by\n'
        '  the semivowel rule, and the य् carries its accent forward onto\n'
        '  what follows'
    ),
)

register(
    '8.2.5',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — एकादेश उदात्तेनोदात्तः — where an अनुदात्त and an उदात्त\n'
        '  have become ONE vowel, that vowel is उदात्त: **अग्नी, वायू,\n'
        '  वृक्षैः, प्लक्षैः**. And the counter-example turns on a rule of\n'
        '  the tripādī being invisible to the ordinary grammar — **पररूपे\n'
        '  कर्तव्ये स्वरितस्य असिद्धत्वात्**: in पचन्ति both vowels are\n'
        "  अनुदात्त, so nothing here applies, and 8.4.66's स्वरित cannot be\n"
        '  seen from where 6.1.97 stands'
    ),
)

register(
    '8.2.6',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — स्वरितो वाऽनुदात्ते पदादौ — but where the अनुदात्त began a\n'
        '  WORD, the merged vowel is स्वरित or उदात्त, either: **सु उत्थितः →\n'
        '  सूत्थितः** heard two ways, **वि ईक्षते → वीक्षते**, **वसुकः असि →\n'
        '  वसुकोऽसि**. The सु of सूत्थितः is the कर्मप्रवचनीय of 1.4.94 —\n'
        '  **सुः पूजायाम्** — which is why it counts as a word of its own and\n'
        '  its vowel is the first of a पद'
    ),
)

register(
    '8.2.7',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — नलोपः प्रातिपदिकान्तस्य — a word that is a प्रातिपदिक\n'
        '  loses its final न्: **राजा, राजभ्याम्, राजभिः, राजता, राजतरः,\n'
        '  राजतमः**. This is the rule that makes राजन् end in आ in the\n'
        '  nominative singular and keeps the न् out of every ending beginning\n'
        '  with a consonant.\n'
        '\n'
        'SETTLED — **AND BOTH ITS WORDS ARE TESTED.** **प्रातिपदिकग्रहणं\n'
        "  किम्? अहन्नहिम्** — a verb's न् is not touched; **अन्तग्रहणं किम्?\n"
        '  राजानौ, राजानः** — a न् that is not last is not touched. And the\n'
        '  naming is of an UNCOMPOUNDED stem: **प्रातिपदिकग्रहणम् असमस्तम् एव\n'
        '  7.1.39 इति षष्ठ्या लुका निर्दिष्टम्**'
    ),
)

register(
    '8.2.8',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — न ङिसम्बुद्ध्योः — but not before ङि and not in the\n'
        '  vocative singular: **आर्द्रे चर्मन्; लोहिते चर्मन्; हे राजन्; हे\n'
        "  तक्षन्**. The ङि of the first pair is dropped by 7.1.39's लुक् and\n"
        '  the न् stays all the same.\n'
        '\n'
        'SETTLED — **AND THE REFUSAL IS READ AS PROOF ABOUT WHAT A प्रातिपदिक\n'
        '  IS.** **एतस्माद् एव नलोपप्रतिषेधवचनाद् अप्रत्ययः इति\n'
        '  प्रत्ययलक्षणेन प्रातिपदिकसंज्ञा न प्रतिषिध्यते इति ज्ञाप्यते** —\n'
        '  with the ending gone the word would not be a प्रातिपदिक at all,\n'
        '  and the refusal would have nothing to refuse; that it is stated\n'
        '  shows 1.1.62 keeps the name alive'
    ),
)

register(
    '8.2.9',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — मादुपधायाश्च मतोर्वोऽयवादिभ्यः — the म् of मतुप् becomes\n'
        '  व् after a stem ending in म् or अ, or having म् or अ as its\n'
        '  penult, but not after the यवादि: **किंवान्, शंवान्** after म्;\n'
        "  **शमीवान्** after a म् penult; **वृक्षवान्** after अ. The sūtra's\n"
        '  म् and अ are got by reading the word मत् as naming the affix and\n'
        '  मात् as qualifying both the end and the penult —\n'
        '  **मकारावर्णविशिष्टया च उपधया इत्ययमर्थो भवति**'
    ),
)

register(
    '8.2.10',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — झयः — and after a झय्-final stem: **अग्निचित्वान् ग्रामः;\n'
        '  उदश्वित्वान् घोषः; विद्युत्वान् बलाहकः; इन्द्रो मरुत्वान्;\n'
        '  दृषद्वान् देशः**. The झय् is every stop, voiced or not, aspirate\n'
        '  or not, which is the widest of the four conditions the run gives\n'
        '  for this one substitute'
    ),
)

register(
    '8.2.11',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — संज्ञायाम् — and wherever the word is a NAME, whatever it\n'
        '  ends in: **अहीवती, कपीवती, ऋषीवती, मुनीवती**. All four are\n'
        '  ई-final, which neither 8.2.9 nor 8.2.10 reaches, so the sense is\n'
        '  doing the whole work and the shape none of it'
    ),
)

register(
    '8.2.12',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — आसन्दीवदष्ठीवच्चक्रीवत्कक्षीवद्रुमण्वच्चर्मण्वती — six\n'
        '  names laid down whole: **आसन्दीवान् ग्रामः; आसन्दीवद् अहिस्थलम्**.\n'
        '  The व् itself was already available — **वत्वं पूर्वेण एव सिद्धम्,\n'
        '  आदेशार्थानि निपातनानि** — so what each निपातन gives is the STEM:\n'
        '  आसन becomes आसन्दी, and आसनवान् is what stands anywhere else.\n'
        '\n'
        'SETTLED — **AND THE KĀŚIKĀ RECORDS A SECOND OPINION.** **अपरे तु\n'
        '  आहुः — आसन्दीशब्दोऽपि प्रकृत्यन्तरम् एव अस्ति** — that आसन्दी is\n'
        '  simply another stem and no substitution is needed at all'
    ),
)

register(
    '8.2.13',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — उदन्वानुदधौ च — **उदन्वान्** is laid down: उदक becomes\n'
        '  उदन् before मतुप्, in the sense of the SEA and as a name.\n'
        '  **उदन्वान् नाम ऋषिः; यस्मिन् उदकं धीयते, स एवम् उच्यते**. And the\n'
        '  counter-example is exact about why the pot is left out — **उदकवान्\n'
        '  घटः इत्यत्र तु दधात्यर्थो न विवक्ष्यते। किं तर्हि?\n'
        '  उदकसत्तासम्बन्धसामान्यम्**: the pot merely HAS water, the sea\n'
        '  HOLDS it'
    ),
)

register(
    '8.2.14',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — राजन्वान् सौराज्ये — and **राजन्वान्** where GOOD\n'
        '  GOVERNMENT is meant: **शोभनो राजा यस्मिन् इति स राजन्वान् देशः;\n'
        '  राजन्वती पृथ्वी**. Anywhere else 8.2.7 takes the न् off and\n'
        '  राजवान् stands. The pair is the neatest thing in the run: one word\n'
        '  keeps its न् if the king is a good one'
    ),
)

register(
    '8.2.15',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — छन्दसीरः — and in the VEDA after an इ-final or a र्-final\n'
        '  stem: **त्रिवती याज्यानुवाक्या भवति; अधिपतिवतीर् जुहोति; चरुर्\n'
        '  अग्निवाँ इव** for the first, and **हरिवो मेदिनं त्वा; आरेवान् एतु\n'
        '  मा विशत्; सरस्वतीवान् भारतीवान्** for the second. The इ-final case\n'
        '  is what 8.2.11 gives outside the Veda only for a name; here it is\n'
        '  general'
    ),
)

register(
    '8.2.16',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — अनो नुट् — and after an अन्-final stem मतुप् takes a नुट्\n'
        '  in the Veda: **अक्षण्वन्तः कर्णवन्तः सखायः; अस्थन्वन्तं यद् अनस्था\n'
        '  बिभर्ति; अक्षण्वता लाङ्गलेन; शीर्षण्वती; मूर्धन्वती**. And the\n'
        '  augment blocks the very substitute this run is about —\n'
        '  **नुटोऽसिद्धत्वात् तस्य च वत्वं न भवति**: with the न् of नुट्\n'
        '  invisible, मतुप् is not after a म् or an अ and stays a म्'
    ),
)

register(
    '8.2.17',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — नाद्घस्य — and after a न्-final stem the घ — that is तर\n'
        '  and तम — takes a नुट् in the Veda: **सुपथिन्तरः; दस्युहन्तमः**.\n'
        '  Two vārttikas widen it: **भूरिदाव्नस् तुड् वक्तव्यः** for\n'
        '  **भूरिदावत्तरः**, a तुक् and not a नुट्; and **ईद् रथिनः** for\n'
        '  **रथीतरः**, where रथिन् takes ई before the घ — or, the Kāśikā\n'
        '  adds, the ई is simply a मत्वर्थीय affix on रथ itself'
    ),
)

register(
    '8.2.18',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — कृपो रो लः — the र् of कृप् becomes ल्: **कल्प्ता,\n'
        '  कल्प्तुम्, कल्प्तव्यम्**. Both letters are named by their bare\n'
        '  sound and not by a class — **र इति श्रुतिसामान्यम् उपादीयते** — so\n'
        '  both a plain रेफ and the र् inside an ऋ are reached, and what\n'
        '  comes out is either a ल् or a ऌ. That is what makes 1.3.93 लुटि च\n'
        '  क्ऌपः intelligible: the root is written with ऌ there because this\n'
        '  rule has already put one in'
    ),
)

register(
    '8.2.19',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — उपसर्गस्यायतौ — the र् of a PREVERB before अय् becomes ल्:\n'
        "  **प्लायते, पलायते**. The Kāśikā works through what the sūtra's\n"
        '  grammar allows at some length, and settles it with a paribhāṣā:\n'
        '  **येन नाव्यवधानं तेन व्यवहितेऽपि वचनप्रामाण्यात्** — where a rule\n'
        '  tolerates no gap it may still act across one on the strength of\n'
        '  its being stated, which is how पल्ययते comes out with a whole\n'
        '  sound in between'
    ),
)

register(
    '8.2.20',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — ग्रो यङि — the र् of गॄ becomes ल् before यङ्:\n'
        '  **निजेगिल्यते, निजेगिल्येते, निजेगिल्यन्ते** — the यङ् being\n'
        "  3.1.24's, given of self-reproach.\n"
        '\n'
        'SETTLED — **AND THE COMMENTARY SPLITS ON WHICH गॄ IS MEANT.**\n'
        '  **केचिद् ग्र इति गिरतेर् गृणातेश् च सामान्येन ग्रहणम् इच्छन्ति।\n'
        '  अपरे तु गिरतेर् एव, न गृणातेः। गृणातेर् हि यङ् एव नास्ति,\n'
        '  अनभिधानाद् इति** — one party takes both roots, the other only\n'
        "  'swallow', since 'praise' has no यङ् anyone uses"
    ),
)

register(
    '8.2.21',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — अचि विभाषा — and OPTIONALLY before a vowel-initial affix:\n'
        '  **निगिरति, निगिलति; निगरणम्, निगलनम्; निगारकः, निगालकः**.\n'
        '\n'
        "SETTLED — **AND THE OPTION IS NOT THE SPEAKER'S.** **इयं तु\n"
        '  व्यवस्थितविभाषा। तेन गल इति प्राण्यङ्गे नित्यं लत्वं भवति, गर इति\n'
        '  विषे नित्यं न भवति** — a throat is always गल and poison is always\n'
        '  गर. The rule reads as a free choice and is not one; which\n'
        '  alternative holds is settled by the word. And in निगार्यते the\n'
        "  causal's णि is gone but counts as there, so the option is\n"
        '  available at all'
    ),
)

register(
    '8.2.22',
    apply=in_the_word,
    codification=_IN_THE_WORD,
    notes=(
        'SETTLED — परेश्च घाङ्कयोः — and the र् of परि before घ and अङ्क,\n'
        '  optionally: **परिघः, पलिघः; पर्यङ्कः, पल्यङ्कः**. The घ here is\n'
        "  the SOUND and not 1.1.22's name for तर and तम — **घ इति\n"
        '  स्वरूपग्रहणम् अत्र इष्यते** — which the run needs said, 8.2.17\n'
        '  having used the name five sūtras back. A vārttika adds a third\n'
        '  word: **योगे च इति वक्तव्यम्। परियोगः, पलियोगः**'
    ),
)


_AT_THE_END = (
    'at_the_end(root, gana=..., before=...) -> the cluster loss and '
    'the consonant change at a word end, by rule of 8.2.23-41.'
)

register(
    '8.2.23',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — संयोगान्तस्य लोपः — a word ending in a CLUSTER loses its\n'
        '  last sound: **गोमान्, यवमान्, कृतवान्, हतवान्** — गोमन्त् gives\n'
        '  गोमान्, and the त् is simply gone.\n'
        '\n'
        'SETTLED — **AND ITS OWN VṚTTI WORKS THREE ORDERINGS AND GETS THREE\n'
        '  DIFFERENT ANSWERS.** In श्रेयान् and भूयान् the रुँ of 8.2.66 is\n'
        '  LATER and therefore invisible — **रुत्वं परम् अपि असिद्धत्वात्\n'
        "  संयोगान्तस्य लोपं न बाधते** — so the cluster's loss goes through.\n"
        '  In यशः and पयः the जश्त्व of 8.2.39 would have had no other chance\n'
        '  at all — **जश्त्वे तु न अप्राप्ते तद् आरभ्यत इति तस्य बाधकं भवति**\n'
        '  — so it displaces this rule. And in दध्यत्र the semivowel is\n'
        '  बहिरङ्ग and invisible, so there is no cluster here to lose. Three\n'
        '  answers from one heading'
    ),
)

register(
    '8.2.24',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — रात् सस्य — and where the cluster has a र् in it, it is\n'
        '  the स् that goes and not the last sound: **गोभिर् अक्षाः;\n'
        '  प्रत्यञ्चम् अत्साः**. Without it 8.2.23 would take the स् off\n'
        '  अक्षार्स् and leave *अक्षार्. The vṛtti derives both forms in full\n'
        '  — the aorist of क्षर् and त्सर् with no इट्, **सिचः छान्दसत्वाद्\n'
        '  ईडभावः 7.3.97 इति वचनात्** — and adds that मातुः and पितुः come\n'
        "  out the same way through 6.1.111's उत्"
    ),
)

register(
    '8.2.25',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        "SETTLED — धि च — and the aorist's स् goes before a ध-initial ending:\n"
        '  **अलविध्वम्, अलविढ्वम्; अपविध्वम्, अपविढ्वम्**.\n'
        '\n'
        'SETTLED — **AND WITHOUT IT THE ध् WOULD NEVER BE HEARD AT ALL.**\n'
        '  **यद्य् अत्र सकारलोपो न स्यात्, सिचः षत्वे जश्त्वे च विभाषेटः इति\n'
        '  मूर्धन्याभावपक्षेऽपि न धकारः श्रूयेत** — with the स् in place the\n'
        '  following ध् is swallowed by the cerebralisation and the voicing,\n'
        '  and the form comes out with no ध् in it. **इतः प्रभृति सिचः\n'
        "  सकारस्य लोप इष्यते** — from here on it is the aorist's स् that\n"
        '  these rules mean, which is why पयो धावति is untouched'
    ),
)

register(
    '8.2.26',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        "SETTLED — झलो झलि — the aorist's स् goes after a झल् and before a\n"
        '  झल्: **अभित्त, अभित्थाः; अच्छित्त, अच्छित्थाः**. Both conditions\n'
        '  are tested and both hold. And अवात्ताम् shows the ordering again —\n'
        '  **सिचः सकारलोपस्य असिद्धत्वात् 7.4.49 इति सकारस्य तकारः**: the\n'
        '  loss is invisible to the rule that turns a स् into a त्, so the त्\n'
        '  is made and only then does the स् go'
    ),
)

register(
    '8.2.27',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — ह्रस्वादङ्गात् — and after a stem ending in a SHORT vowel,\n'
        '  before a झल्: **अकृत, अकृथाः; अहृत, अहृथाः**. Both words are\n'
        '  tested — **ह्रस्वाद् इति किम्? अच्योष्ट; अङ्गाद् इति किम्?\n'
        "  अलाविष्टाम्** — and it is the aorist's स् here too, which is why\n"
        '  द्विष्टराम् keeps its own'
    ),
)

register(
    '8.2.28',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — इट ईटि — and after an इट् before an ईट्: **अदेवीत्,\n'
        '  असेवीत्, अकोषीत्, अमोषीत्**. This is the fourth and last of the\n'
        "  aorist's स्-losses, and the four between them cover every place\n"
        '  the sound would otherwise be heard: after a र्, before a ध्,\n'
        '  between two झल्, and between the two augments'
    ),
)

register(
    '8.2.29',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — स्कोः संयोगाद्योरन्ते च — the स् or क् at the HEAD of a\n'
        "  cluster goes, at a word's end and before a झल्: from लस्ज्\n"
        '  **लग्नः, लग्नवान्, साधुलक्**, from मस्ज् **मग्नः**, and for the क्\n'
        '  from तक्ष् **तट्, तष्टः, तष्टवान्, काष्ठतट्**. A vārttika narrows\n'
        '  the झल् — **झलि सङि इति वक्तव्यम्** — where सङ् is a pratyāhāra\n'
        '  from स of सन् to the ङ of महिङ्, so that काष्ठशक् स्थाता keeps its\n'
        '  क्'
    ),
)

register(
    '8.2.30',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — चोः कुः — a PALATAL becomes the answering guttural before\n'
        "  a झल् and at a word's end: **पक्ता, पक्तुम्, पक्तव्यम्, ओदनपक्;\n"
        '  वक्ता, वक्तुम्, वक्तव्यम्, वाक्**. This is the rule that makes पच्\n'
        '  end in क् and वच् in क् wherever no vowel follows, and it is what\n'
        '  the whole of 8.2.30–41 is arranged around'
    ),
)

register(
    '8.2.31',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — हो ढः — and ह् becomes ढ्: **सोढा, सोढुम्, सोढव्यम्,\n'
        '  जलाषाट्; वोढा, वोढुम्, वोढव्यम्, प्रष्ठवाट्, दित्यवाट्**. The ढ्\n'
        '  is then acted on further by the rules of 8.4, so what is heard is\n'
        '  often a ट् — जलाषाट् — and the ढ् is only ever an intermediate\n'
        '  step'
    ),
)

register(
    '8.2.32',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — दादेर्धातोर्घः — but the ह् of a root BEGINNING WITH द्\n'
        '  becomes घ् instead: **दग्धा, दग्धुम्, दग्धव्यम्, काष्ठधक्; दोग्धा,\n'
        '  दोग्धुम्, दोग्धव्यम्, गोधुक्**. Both words are tested — **दादेर्\n'
        '  इति किम्? लेढा** — and धातोः is there so that the द-initial is\n'
        '  asked of the ROOT and not of whatever stands in front of it'
    ),
)

register(
    '8.2.33',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — वा द्रुहमुहष्णुहष्णिहाम् — and for द्रुह्, मुह्, ष्णुह्\n'
        '  and ष्णिह् the घ् comes only optionally, the ढ् standing beside\n'
        '  it: **द्रोग्धा, द्रोढा; मित्रध्रुक्, मित्रध्रुट्; उन्मोग्धा,\n'
        '  उन्मोढा; उन्मुक्, उन्मुट्**. None of the four begins with द्, so\n'
        '  8.2.32 could not have reached them at all — the option is between\n'
        '  this rule and 8.2.31'
    ),
)

register(
    '8.2.34',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — नहो धः — and the ह् of नह् becomes ध्: **नद्धम्, नद्धुम्,\n'
        '  नद्धव्यम्; उपानत्, परीणत्**. उपानह् is the shoe that is tied on,\n'
        "  and उपानत् is what is left of it after this rule and 8.4's have\n"
        '  both run — one root and four sūtras between the written form and\n'
        '  the spoken one'
    ),
)

register(
    '8.2.35',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — आहस्थः — and the ह् of आह् becomes थ्: **इदम् आत्थ; किम्\n'
        '  आत्थ**. The substitute is a fourth different sound for the same\n'
        '  ह्, and the vṛtti says why one was needed at all — **आदेशान्तरकरणं\n'
        '  8.2.40 इत्यस्य निवृत्त्यर्थम्**: a ढ् would have been turned into\n'
        '  ध् by that rule, and थ् is chosen to keep it out.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA GIVES THE VEDA A FIFTH.** **हृग्रहोर् भश्\n'
        '  छन्दसि हस्य इति वक्तव्यम्** — the ह् of हृ and ग्रह् becomes भ् in\n'
        '  the Veda'
    ),
)

register(
    '8.2.36',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः — seven roots named\n'
        '  outright, and every छ-final and every श-final root besides, become\n'
        '  ष्: **व्रष्टा, व्रष्टुम्, व्रष्टव्यम्, मूलवृट्; भ्रष्टा; स्रष्टा;\n'
        '  मार्ष्टा; यष्टा; राट्; भ्राट्**. The ष् then goes on to become ट्\n'
        "  at a word's end by 8.4's rules, which is why मूलवृट् and राट् are\n"
        '  heard with a stop where the sūtra puts a sibilant'
    ),
)

register(
    '8.2.37',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — एकाचो बशो भष् झषन्तस्य स्ध्वोः — where a MONOSYLLABIC part\n'
        '  of a root ends in a झष् and begins with a बश्, that बश् becomes\n'
        '  the answering भष् — the aspiration moves from the end of the\n'
        '  syllable to its beginning. **अत्र चत्वारो बशः स्थानिनो भषादेशाश्\n'
        "  चत्वार एव** — four sounds replaced and four replacing, so 1.3.10's\n"
        '  one-to-one matching would apply; the vṛtti has to note that there\n'
        '  is no ड् among the four to take the ढ्'
    ),
)

register(
    '8.2.38',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — दधस्तथोश्च — and for दध् — that is धा with its\n'
        '  reduplication already made — before त्, थ्, and by the च before स्\n'
        '  and ध्व too: **धत्तः, धत्थः, धत्से, धत्स्व, धद्ध्वम्**.\n'
        '  **वचनसामर्थ्याद् आतो लोपस्य स्थानिवद्भावः** — the आ is gone and\n'
        '  counts as there, which is the only way the root still ends in a\n'
        '  झष् for this rule to reach'
    ),
)

register(
    '8.2.39',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        "SETTLED — झलां जशोऽन्ते — a झल् at a WORD'S END becomes the\n"
        '  answering जश् — the plain voiced stop: **वागत्र; श्वलिडत्र;\n'
        '  अग्निचिदत्र; त्रिष्टुबत्र**. वाच् becomes वाक् by 8.2.30 and then\n'
        '  वाग् by this, and which of the two is heard depends on what\n'
        '  follows. **अन्तग्रहणं झलि इत्येतस्य निवृत्त्यर्थम्** — saying\n'
        '  अन्ते is what stops the rule reaching inside a word'
    ),
)

register(
    '8.2.40',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — झषस्तथोर्धोऽधः — a त् or थ् after a झष् becomes ध्, except\n'
        '  after दध्: **लब्धा, लब्धुम्, लब्धव्यम्, अलब्ध, अलब्धाः; दोग्धा,\n'
        '  अदुग्ध; लेढा, अलीढ**. This is what makes the whole cluster voiced\n'
        '  and aspirated together — लभ् plus त gives लब्ध and not *लब्त — and\n'
        "  it is the rule 8.2.35's थ् was chosen to keep out"
    ),
)

register(
    '8.2.41',
    apply=at_the_end,
    codification=_AT_THE_END,
    notes=(
        'SETTLED — षढोः कः सि — ष् and ढ् become क् before स्: from पिष्\n'
        '  **पेक्ष्यति, अपेक्ष्यत्, पिपिक्षति**, and from लिह् **लेक्ष्यति,\n'
        '  अलेक्ष्यत्, लिलिक्षति**. The ढ् meant is the one 8.2.31 has just\n'
        '  made out of a ह्, so लिह् reaches this rule only by going through\n'
        '  that one — which is what makes लेक्ष्यति and लेढा two steps apart\n'
        '  from the same root'
    ),
)


_THE_NISTHA = (
    'the_nistha(root, gana=..., sense=..., upasarga=..., '
    'chandasi=...) -> what the nistha t becomes, by rule of '
    '8.2.42-61.'
)

register(
    '8.2.42',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — रदाभ्यां निष्ठातो नः पूर्वस्य च दः — after a र् or a द्,\n'
        "  the निष्ठा's त् becomes न् — and a preceding द् becomes न् with\n"
        '  it. After र्: **आस्तीर्णम्, विस्तीर्णम्, विशीर्णम्, निगीर्णम्,\n'
        '  अवगूर्णम्**. After द्: **भिन्नः, भिन्नवान्; छिन्नः, छिन्नवान्** —\n'
        '  where भिद् and छिद् lose their own द् to a न् as well, which is\n'
        '  what पूर्वस्य च दः adds and what makes the whole cluster न्न'
    ),
)

register(
    '8.2.43',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — संयोगादेरातो धातोर्यण्वतः — and after a root that begins\n'
        '  with a CLUSTER, ends in आ, and has a यण् in it: **प्रद्राणः,\n'
        '  प्रद्राणवान्; म्लानः, म्लानवान्**. All three conditions are tested\n'
        '  — **संयोगादेर् इति किम्? यातः। आत इति किम्? च्युतः** — and the यण्\n'
        '  is what द्रा and म्ला have and या has not'
    ),
)

register(
    '8.2.44',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — ल्वादिभ्यः — and after the ल्वादि roots: **लूनः, लूनवान्;\n'
        '  धूनः, धूनवान्; जीनः, जीनवान्**. The class is bounded by the root\n'
        '  list itself — **लूञ् छेदने इत्येतत्प्रभृति व्री वरणे इति यावत्\n'
        '  वृत्करणेन समापिताः** — from लू to व्री, closed off by the marker\n'
        '  वृ, so the ग्रन्थ and not the grammar says where it stops'
    ),
)

register(
    '8.2.45',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — ओदितश्च — and after a root marked with ओ: from ओलस्जी\n'
        '  **लग्नः, लग्नवान्**; from ओविजी **उद्विग्नः**; from ओप्यायी\n'
        '  **आपीनः**; and from the ओदित् roots of the fifth class **सूनः,\n'
        '  दूनः**. The marker is put on the root in the list for this rule\n'
        '  and for almost nothing else, which is what makes it a cheap way of\n'
        '  naming a set that has no shape in common'
    ),
)

register(
    '8.2.46',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — क्षियो दीर्घात् — and after क्षि when its vowel is LONG:\n'
        '  **क्षीणाः क्लेशाः; क्षीणो जाल्मः; क्षीणस् तपस्वी**. The length is\n'
        '  given by 6.4.59–61 — क्षियः, निष्ठायाम् अण्यदर्थे, वा\n'
        '  क्रोशदैन्ययोः — so the rule is stated for the output of three\n'
        '  earlier sūtras and does nothing where they have not run'
    ),
)

register(
    '8.2.47',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — श्योऽस्पर्शे — and after श्यै where TOUCH is not meant:\n'
        '  **शीनं घृतम्; शीनं मेदः; शीना वसा** — congealed ghee, fat, marrow.\n'
        '  Where the sense is what the hand feels the त् stays: **शीतं\n'
        '  वर्तते; शीतो वायुः**. And the vṛtti notes that in शीतम् उदकम्\n'
        '  touch is present only as a secondary sense, which is enough to\n'
        '  keep the न् off'
    ),
)

register(
    '8.2.48',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — अञ्चोऽनपादाने — and after अञ्च् where there is no अपादान:\n'
        '  **समक्नौ शकुनेः पादौ; तस्मात् पशवो न्यक्नाः**. Water drawn from a\n'
        '  well has one — **उदक्तम् उदकं कूपात्** — and the त् stands. The\n'
        '  vṛtti adds that व्यक्तम् is a different root altogether, अञ्ज् and\n'
        '  not अञ्च्'
    ),
)

register(
    '8.2.49',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — दिवोऽविजिगीषायाम् — and after दिव् where no wish to WIN is\n'
        '  meant: **आद्यूनः, परिद्यूनः** — a wretch, one who is played out.\n'
        '  Of gambling the त् stands, and the vṛtti says exactly why the two\n'
        '  senses part: **विजिगीषया हि तत्र अक्षपातनादि क्रियते** — the dice\n'
        '  are thrown in order to win, so द्यूत has the wish in it and आद्यून\n'
        '  has not'
    ),
)

register(
    '8.2.50',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — निर्वाणोऽवाते — **निर्वाण** is laid down: वा with निस् in\n'
        "  front takes न् for the निष्ठा's त्, provided the sense is not the\n"
        "  WIND's blowing. **निर्वाणोऽग्निः; निर्वाणः प्रदीपः; निर्वाणो\n"
        '  भिक्षुः** — the fire gone out, the lamp gone out, and the monk.\n'
        '  **अवात इति किम्? निर्वातो वातः**'
    ),
)

register(
    '8.2.51',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        "SETTLED — शुषः कः — after शुष् the निष्ठा's त् becomes क्: **शुष्कः,\n"
        '  शुष्कवान्**. Three sūtras in a row now give three different sounds\n'
        '  to three single roots, and nothing but the root distinguishes them\n'
        '  — which is why the run reads as a list rather than as a rule'
    ),
)

register(
    '8.2.52',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — पचो वः — and after पच् it becomes व्: **पक्वः, पक्ववान्**.\n'
        "  The क् of पक्व is 8.2.30's — पच् before a झल् — so the finished\n"
        '  word has both this rule and that one in it, and neither is visible\n'
        '  in the written stem'
    ),
)

register(
    '8.2.53',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — क्षायो मः — and after क्षै it becomes म्: **क्षामः,\n'
        '  क्षामवान्**. This is the third of the single-root substitutes and\n'
        '  the one the next sūtra borrows'
    ),
)

register(
    '8.2.54',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — प्रस्त्योऽन्यतरस्याम् — and after स्त्यै with प्र in\n'
        '  front, OPTIONALLY: **प्रस्तीमः, प्रस्तीमवान्** beside **प्रस्तीतः,\n'
        '  प्रस्तीतवान्**. And the alternative where the म् does not come is\n'
        '  not the plain form either — **यदा मत्वं नास्ति तदा 8.2.43 इत्यस्य\n'
        '  पूर्वत्रासिद्धत्वात्** the न् of that rule cannot come, स्त्यै\n'
        '  being cluster-initial and आ-final; so the त् stands and प्रस्तीतः\n'
        '  is what is heard'
    ),
)

register(
    '8.2.55',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः — four words laid down\n'
        '  where no preverb stands in front. **फुल्ल** is ञिफला with ल् for\n'
        "  the निष्ठा's त् — **उत्वम् इडभावश् च सिद्ध एव** — and the\n"
        '  क्तवतु-form takes it too. The other three are given whole, and the\n'
        '  condition is one all four share: with a preverb, none of them\n'
        '  holds'
    ),
)

register(
    '8.2.56',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम् — and after these\n'
        '  six the न् comes only OPTIONALLY, so each has two निष्ठा-forms:\n'
        '  **नुन्नः, नुत्तः; विन्नः, वित्तः; समुन्नः, समुत्तः; त्राणः,\n'
        '  त्रातः; घ्राणः, घ्रातः; ह्रीणः, ह्रीतः**. Two of the twelve are\n'
        '  then taken up again by 8.2.58 and 8.2.59, which lay down वित्त and\n'
        '  भित्त in particular senses'
    ),
)

register(
    '8.2.57',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — न ध्याख्यापॄमूर्छिमदाम् — but for ध्या, ख्या, पॄ, मूर्छ्\n'
        '  and मद् the न् does NOT come: **ध्यातः, ख्यातः, पूर्तः, मूर्तः,\n'
        '  मत्तः**. It is the only refusal in the run, and it is aimed at\n'
        '  three different rules at once — 8.2.42 would have reached पॄ and\n'
        '  मूर्छ् through their र्, 8.2.43 ध्या and ख्या, and 8.2.56 would\n'
        '  have made मद् optional'
    ),
)

register(
    '8.2.58',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — वित्तो भोगप्रत्यययोः — **वित्त** is laid down with its त्\n'
        '  in two senses: of WEALTH and of RENOWN. **वित्तम् अस्य बहु** — his\n'
        '  wealth is great, and the vṛtti explains why the word for enjoying\n'
        '  names the thing: **धनं हि भुज्यत इति भोगोऽभिधीयते**. And\n'
        '  **वित्तोऽयं मनुष्यः**, प्रतीत इत्यर्थः — this man is well known.\n'
        "  In any other sense 8.2.56's option leaves both विन्नः and वित्तः\n"
        '  standing'
    ),
)

register(
    '8.2.59',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — भित्तं शकलम् — and **भित्तम्** where a FRAGMENT is meant:\n'
        '  **भित्तं तिष्ठति; भित्तं प्रपतति**. **शकलपर्यायोऽयम्** — it is\n'
        '  simply another word for a chip, and the vṛtti is careful that the\n'
        '  root is only its etymology: **भिदिक्रिया शब्दव्युत्पत्तेर् एव\n'
        '  निमित्तम्**. Where the SPLITTING is meant, भिन्नम् stands and\n'
        '  8.2.42 has its way'
    ),
)

register(
    '8.2.60',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        "SETTLED — ऋणमाधमर्ण्ये — and **ऋणम्** — ऋ with the निष्ठा's त्\n"
        '  turned न् — in the sense of DEBT: **अधम ऋणे अधमर्णः**, and the\n'
        '  state of being one is आधमर्ण्य. The निपातन buys a compound besides\n'
        '  — **एतस्माद् एव निपातनात् सप्तम्यन्तेन उत्तरपदेन समासः** — a\n'
        '  locative first member compounded with what follows, which no\n'
        '  ordinary rule allows'
    ),
)

register(
    '8.2.61',
    apply=the_nistha,
    codification=_THE_NISTHA,
    notes=(
        'SETTLED — नसत्तनिषत्तानुत्तप्रतूर्तसूर्तगूर्तानि छन्दसि — six Vedic\n'
        '  forms laid down whole: **नसत्तम् अञ्जसा; निषत्तः; अनुत्तम्;\n'
        '  प्रतूर्तम्; सूर्तम्; गूर्तम्**. The first two are सद् with नञ् and\n'
        '  नि in front, and what is laid down in each is the ABSENCE of the\n'
        '  न् — **नत्वाभावो निपात्यते** — so the whole sūtra is a list of\n'
        "  places where the run's own rule is set aside. The spoken language\n"
        '  keeps नसन्नम्'
    ),
)


_THE_WORD_END = (
    'the_word_end(word, gana=..., before=..., chandasi=...) -> what '
    'a word last sound becomes, by rule of 8.2.62-81.'
)

register(
    '8.2.62',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — क्विन्प्रत्ययस्य कुः — a word whose root took क्विन् ends\n'
        '  in a GUTTURAL, wherever it ends: **घृतस्पृक्** from स्पृश् by\n'
        '  3.2.58, and so for every other क्विन्-formation. **क्विन् प्रत्ययो\n'
        '  यस्माद् धातोः स क्विन्प्रत्ययः** — the name is of the whole word\n'
        '  and not of the affix, which is why the guttural lands on the LAST\n'
        '  sound and not where the affix was. **पदस्येति वर्तते**, and\n'
        '  **सर्वत्र पदान्ते कुत्वम् इष्यते**'
    ),
)

register(
    '8.2.63',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — नशेर्वा — and नश् does so only optionally: **सा वै\n'
        '  जीवनगाहुतिः; सा वै जीवनडाहुतिः** — **जीवस्य नाशो जीवनक्, जीवनट्**,\n'
        '  both standing. The word is नश् with the क्विप् of the सम्पदादि\n'
        "  class, and the option is against 8.3's cerebralisation: **षत्वे\n"
        '  प्राप्ते कुत्वविकल्पः**, so where the guttural does not come a ष्\n'
        '  does, and the two alternatives are ट् and क् rather than क् and\n'
        '  nothing'
    ),
)

register(
    '8.2.64',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — मो नो धातोः — a word from a म्-final ROOT ends in न्:\n'
        '  **प्रशान्, प्रतान्, प्रदान्** — शम्, तन् and दम् with the क्विप्,\n'
        '  lengthened by 6.4.15. And the न् this rule makes is invisible to\n'
        '  the rule that would drop it — **नत्वस्य असिद्धत्वान् नलोपो न\n'
        '  भवति** — so 8.2.7 cannot reach it and the word keeps a न् it was\n'
        '  given four sūtras earlier in the same pāda'
    ),
)

register(
    '8.2.65',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — म्वोश्च — and before a म् or a व्. **अगन्म तमसस् पारम्;\n'
        '  अगन्व** — गम् in the imperfect with the class sign dropped by\n'
        "  2.4.73's बहुलं छन्दसि; and **जगन्वान्**, by 7.2.68's option. The\n"
        "  condition is not a word's end at all, which is why the sūtra has\n"
        '  to be stated apart from the one before'
    ),
)

register(
    '8.2.67',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — अवयाःश्वेतवाःपुरोडाश्च — three words laid down whole:\n'
        '  **अवयाः** from यज् with अव, **श्वेतवाः** from वह् with श्वेत,\n'
        '  **पुरोडाः** from दाश् with पुरस्. Each takes the ण्विन् of\n'
        '  3.2.71–72 and then the substitution of श्वेतवहादि, and what the\n'
        '  निपातन gives is the स् at the end, which the रुँ of 8.2.66 then\n'
        '  works on'
    ),
)

register(
    '8.2.68',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — अहन् — the word अहन् takes रुँ: **अहोभ्याम्, अहोभिः**.\n'
        '\n'
        "SETTLED — **AND THE SŪTRA'S OWN SPELLING IS READ AS PROOF.**\n"
        '  **नलोपम् अकृत्वा निर्देशो ज्ञापकः — नलोपाभावो यथा स्याद् इति** —\n'
        '  Pāṇini writes अहन् with its न् still on, and could have written\n'
        '  अहः; that he did not shows the न्-loss of 8.2.7 is not to come\n'
        '  here. **दीर्घाहा निदाघः; हे दीर्घाहोऽत्र** are what the ज्ञापक\n'
        '  buys'
    ),
)

register(
    '8.2.69',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — रोऽसुपि — and a plain र् where no case ending follows:\n'
        '  **अहर् ददाति; अहर् भुङ्क्ते**. The objection and its answer are\n'
        '  worth the space: one might say a सुप् IS there by 1.1.62, having\n'
        '  been dropped — **ननु च अत्र अपि प्रत्ययलक्षणेन सुब् अस्ति?** — and\n'
        '  the reply is that it is not, on a principle stated earlier in the\n'
        '  work'
    ),
)

register(
    '8.2.70',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — अम्नरूधरवरित्युभयथा छन्दसि — and in the Veda अम्नस्, ऊधस्\n'
        '  and अवस् go BOTH WAYS, with a रुँ or with a plain र्: **अम्न एव**\n'
        '  beside **अम्नर् एव**, **ऊध एव** beside **ऊधर्**, **अवः** beside\n'
        '  **अवर्**. उभयथा is the rarest kind of option in the work — not a\n'
        '  choice between doing and not doing, but between two substitutes\n'
        '  that differ only in what happens to them afterwards'
    ),
)

register(
    '8.2.71',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — भुवश्च महाव्याहृतेः — and भुवस् where it is the\n'
        '  MAHĀVYĀHṚTI, either way: **भुव इत्य् अन्तरिक्षम्; भुवर् इत्य्\n'
        '  अन्तरिक्षम्** — the second of the three great utterances भूर् भुवः\n'
        '  स्वः. Anywhere else the option does not come, and the vṛtti quotes\n'
        '  a ṛc where भुवस् is an ordinary verb'
    ),
)

register(
    '8.2.72',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — वसुस्रंसुध्वंस्वनडुहां दः — a वसु-final word, and स्रंस्,\n'
        '  ध्वंस् and अनडुह्, end in द्.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI HAS TO SAY WHICH OF THE FOUR THE स्\n'
        '  CARRIED DOWN FROM 8.2.66 QUALIFIES.** **तेन सम्भवाद् व्यभिचाराच् च\n'
        '  वसुर् एव विशेष्यते, न स्रंसुध्वंसू व्यभिचाराभावाद्, असम्भवाच् च न\n'
        '  अनडुह्शब्दः** — वसु alone is qualified by it, since वसु may or may\n'
        '  not end in स्; स्रंस् and ध्वंस् always do, so qualifying them\n'
        '  would say nothing; and अनडुह् never does, so it cannot be\n'
        '  qualified at all'
    ),
)

register(
    '8.2.73',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — तिप्यनस्तेः — before तिप् a स्-final word takes द्, unless\n'
        '  the root is अस्: **अचकाद् भवान्; अन्वशाद् भवान्**. Both conditions\n'
        '  are tested, and the second is tested with a Vedic form of अस् in\n'
        '  the imperfect — **आ इत्य् अस्तेर् लङि तिपि** — where the word ends\n'
        '  in स् and the द् does not come'
    ),
)

register(
    '8.2.74',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — सिपि धातो रुर्वा — and before सिप् a स्-final word FROM A\n'
        '  ROOT takes रुँ, or else द्: **अचकास् त्वम्, अचकात् त्वम्; अन्वशास्\n'
        '  त्वम्, अन्वशात् त्वम्**. **धातुग्रहणं च उत्तरार्थं रुग्रहणं च** —\n'
        '  both words are said with the next sūtra in view, which borrows\n'
        '  them and gives them to a द्-final word'
    ),
)

register(
    '8.2.75',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — दश्च — and a द्-final word from a root, before सिप्, the\n'
        '  same way: **अभिनस् त्वम्, अभिनत् त्वम्; अच्छिनस् त्वम्, अच्छिनत्\n'
        '  त्वम्**. The pair of sūtras is the neatest borrowing in the pāda —\n'
        '  one says धातोः and रुः so that the other need say only दः, and the\n'
        '  two together cover both endings before one affix'
    ),
)

register(
    '8.2.76',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — र्वोरुपधाया दीर्घ इकः — the इक् PENULT of a word from a\n'
        '  र्-final or व्-final root lengthens: **गीः, धूः, पूः, आशीः**.\n'
        '  **वकारग्रहणम् उत्तरार्थम्** — the व् is said for the two sūtras\n'
        '  after; here only the र् does any work. And उपधाग्रहणम् is what\n'
        "  keeps the reduplication's vowel out of reach in अबिभर् भवान्"
    ),
)

register(
    '8.2.77',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — हलि च — and before a हल्, whether or not a word ends\n'
        '  there: **आस्तीर्णम्, विस्तीर्णम्, विशीर्णम्, अवगूर्णम्** for the\n'
        '  र्, and **दीव्यति, सीव्यति** for the व् — which is the first place\n'
        '  वकारग्रहणम् earns its keep. **धातोर् इत्येव** is what keeps the\n'
        '  denominatives out'
    ),
)

register(
    '8.2.78',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — उपधायां च — and where the र् or व् is itself the PENULT\n'
        '  with a हल् after it, the इक् before THAT lengthens: **हूर्छिता,\n'
        '  मूर्छिता, ऊर्विता, धूर्विता** — from हुर्छा, मुर्छा, उर्वी,\n'
        '  धुर्वी. The rule reaches one sound further back than the two\n'
        '  before it, which is what the whole of its wording is for'
    ),
)

register(
    '8.2.79',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — न भकुर्छुराम् — but not of a भ, and not of कुर् or छुर्:\n'
        '  **धुरं वहति धुर्यः; धुरि साधुर् धुर्यः; दिव्यम्; कुर्यात्;\n'
        '  छुर्यात्**. The भ must be one whose र् or व् is FINAL —\n'
        '  **रेफवकाराभ्यां भविशेषणं किम्? प्रतिदीव्ना** — so the refusal is\n'
        '  narrower than it reads, and it takes back all three of the\n'
        '  lengthening rules at once'
    ),
)

register(
    '8.2.80',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — अदसोऽसेर्दादु दो मः — in अदस्, every sound after the द्\n'
        '  except a final स् becomes उ, and the द् itself becomes म्:\n'
        '  **अमुम्, अमू, अमून्; अमुना, अमूभ्याम्**. The उ takes the length of\n'
        '  what it replaces — **भाव्यमानेन अपि उकारेण सवर्णानां ग्रहणम्\n'
        '  इष्यते** — so a one-mātrā sound gives a short उ and a two-mātrā\n'
        '  one a long ऊ, which is how अमू and अमुना come from one rule'
    ),
)

register(
    '8.2.81',
    apply=the_word_end,
    codification=_THE_WORD_END,
    notes=(
        'SETTLED — एत ईद्बहुवचने — and the ए after that द् becomes ई in the\n'
        '  PLURAL, the द् becoming म् as before: **अमी, अमीभिः, अमीभ्यः,\n'
        '  अमीषाम्, अमीषु**. **बहुवचन इत्यर्थनिर्देशोऽयम्** — the word names\n'
        '  the SENSE of plurality and not the grammatical plural ending,\n'
        '  because अमी has no ending left to be plural with. With this the\n'
        '  reshaping of अदस् is finished, and not one of its own sounds but\n'
        '  the first is left'
    ),
)


_THE_PLUTA = (
    'the_pluta(word, gana=..., sense=..., position=..., view=...) '
    '-> where the pluta comes and what accent it takes, by rule '
    'of 8.2.82-108.'
)

register(
    '8.2.82',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — वाक्यस्य टेः प्लुत उदात्तः — a heading of THREE words at\n'
        '  once: **वाक्यस्य टेर् इति, प्लुत इति, उदात्त इति च, एतत् त्रयम्\n'
        '  अपि अधिकृतं वेदितव्यम् आ पादपरिसमाप्तेः**. What is lengthened is\n'
        '  the टि — the last vowel of a sentence with whatever follows it;\n'
        '  the lengthening is to three mātrās; and the accent is high. Every\n'
        '  rule to 8.2.108 borrows all three, and only the third is ever\n'
        '  changed — twice, at 8.2.100 and 8.2.103'
    ),
)

register(
    '8.2.83',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        "SETTLED — प्रत्यभिवादेऽशूद्रे — in a teacher's RETURN GREETING to\n"
        '  one who is not a śūdra: **अभिवादये देवदत्तोऽहं भोः — आयुष्मान् एधि\n'
        '  देवदत्त३**. **प्रत्यभिवादो नाम यद् अभिवाद्यमानो गुरुर् आशिषं\n'
        '  प्रयुङ्क्ते** — the blessing the elder speaks back. It is the\n'
        '  first rule under the heading and the one the Kāśikā uses to prove\n'
        '  all three of its words at once'
    ),
)

register(
    '8.2.84',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — दूराद्धूते च — and in CALLING FROM A DISTANCE: **आगच्छ भो\n'
        '  माणवक देवदत्त३; आगच्छ भो माणवक यज्ञदत्त३**. **आह्वानं हूतम्,\n'
        '  शब्देन सम्बोधनम्** — a summons by voice. And distance is settled\n'
        '  by the calling and not measured: **दूरं यद्यपि अपेक्षाभेदाद्\n'
        '  अनवस्थितम्, तथापि हूतापेक्षम्** — far enough that one must raise\n'
        "  one's voice"
    ),
)

register(
    '8.2.85',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — हैहेप्रयोगे हैहयोः — but where है or हे is used in such a\n'
        "  call, it is THEY that are lengthened and not the sentence's last\n"
        '  vowel: **है३ देवदत्त; हे३ देवदत्त; देवदत्त है३; देवदत्त हे३**.\n'
        '  Both orders are given, and the reason the two words are named\n'
        '  twice over is exactly that: **पुनर् हैहयोर् ग्रहणम् अनन्त्ययोर्\n'
        '  अपि यथा स्यात्** — so the rule shall reach them where they do not\n'
        '  stand last'
    ),
)

register(
    '8.2.86',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — गुरोरनृतोऽनन्त्यस्याप्येकैकस्य प्राचाम् — and in the\n'
        "  EASTERNERS' view any heavy vowel that is not an ऋ may be\n"
        '  lengthened, one at a time, even where it does not stand last:\n'
        '  **अपिशब्दाद् अन्त्यस्यापि**. The rule is about the प्लुत the\n'
        '  sūtras before have already given — **यः प्लुतो विहितः, तस्य एव अयं\n'
        '  स्थानिविशेष उच्यते** — so it does not add a lengthening anywhere\n'
        '  but says which syllable may carry one that is already due. Naming\n'
        '  the Easterners makes it an option'
    ),
)

register(
    '8.2.87',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — ओमभ्यादाने — and ओम् at the OPENING of a recitation:\n'
        '  **ओ३म् अग्निम् ईळे पुरोहितम्**. **अभ्यादानं प्रारम्भः**. The\n'
        '  counter-example is from the Chāndogya, where the syllable is the\n'
        '  subject of the sentence rather than the start of one, and no\n'
        '  lengthening comes'
    ),
)

register(
    '8.2.88',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — ये यज्ञकर्मणि — and ये in a SACRIFICIAL ACT: **ये३\n'
        '  यजामहे**. The vṛtti narrows it to that one formula — **ये यजामह\n'
        '  इत्यत्र एव अयं प्लुत इष्यते** — and the counter-example is the\n'
        '  same words counted as five syllables during study, where the rite\n'
        '  is not being performed'
    ),
)

register(
    '8.2.89',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — प्रणवष्टेः — and in a sacrificial act the टि is replaced\n'
        '  by the प्रणव. The vṛtti has to say what that is: **पादस्य वा\n'
        '  अर्धर्चस्य वा अन्त्यम् अक्षरम् उपसंगृह्य तदाद्यक्षरशेषस्य स्थाने\n'
        '  त्रिमात्रम् ओकारम् ओङ्कारं वा विदधति, तं प्रणवम् इत्याचक्षते** —\n'
        '  the last syllable of a quarter or half-verse is taken and what\n'
        '  remains of it is replaced by a three-mātrā ओ. It is a substitution\n'
        '  and not a lengthening, which is why it needs its own word'
    ),
)

register(
    '8.2.90',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — याज्याऽन्तः — and the LAST syllable of a याज्या:\n'
        '  **स्तोमैर् विधेमाग्नये३; जिह्वाम् अग्ने चकृषे हव्यवाह३म्**.\n'
        '  **याज्या नाम ये याज्याकाण्डे पठ्यन्ते मन्त्राः** — the invitatory\n'
        '  verses collected in their own section, and it is the last यष्टि of\n'
        '  them that is lengthened'
    ),
)

register(
    '8.2.91',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — ब्रूहिप्रेष्यश्रौषड्वौषडावहानामादेः — and the FIRST\n'
        '  syllable of five words in a sacrificial act: **अग्नयेऽनुब्रू३हि;\n'
        '  अग्नये गोमयान् प्रे३ष्य; अस्तु श्रौ३षट्; वौ३षट्; आ३वह**. This is\n'
        "  the first rule of the run to move the प्लुत off the sentence's end\n"
        "  and onto a word's beginning, and it does so by saying आदेः against\n"
        "  the heading's टेः"
    ),
)

register(
    '8.2.92',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        "SETTLED — अग्नीत्प्रेषणे परस्य च — and in the AGNĪDH'S SUMMONS, the\n"
        '  first syllable and the one after it as well: **आ३श्रा३वय;\n'
        '  ओ३श्रा३वय** — two lengthenings in one word, which happens nowhere else\n'
        '  in the Aṣṭādhyāyī. **अग्नीधः प्रेषणम् अग्नीत्प्रेषणम्**, and\n'
        '  **अत्रैव अयं प्लुत इष्यते** confines it to that call'
    ),
)

register(
    '8.2.93',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — विभाषा पृष्टप्रतिवचने हेः — and OPTIONALLY हि in an ANSWER\n'
        '  to a question: **अकार्षीः कटं देवदत्त? अकार्षं हि३, अकार्षं हि;\n'
        '  अलावीः केदारं देवदत्त? अलाविषं हि३, अलाविषं हि**. Both words are\n'
        '  tested and both do work — the answer must be to a question, and\n'
        '  the particle must be हि'
    ),
)

register(
    '8.2.94',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — निगृह्यानुयोगे च — and in REFUTING and then putting the\n'
        '  question again: **स्वमतात् प्रच्यावनं निग्रहः। अनुयोगस् तस्य मतस्य\n'
        '  आविष्करणम्** — one has been driven off his own position, and the\n'
        "  winner then says it back to him. The vṛtti's example is a debate\n"
        '  about whether sound is eternal, which is as close as the\n'
        '  Aṣṭādhyāyī comes to reporting a philosophical argument'
    ),
)

register(
    '8.2.95',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — आम्रेडितं भर्त्सने — and the आम्रेडित in a THREAT:\n'
        '  **चौरचौ३र, वृषलवृष३ल, दस्योदस्यो३ घातयिष्यामि त्वा, बन्धयिष्यामि\n'
        "  त्वा**. The doubling itself is 8.1.8's — **वाक्यादेर्\n"
        '  आमन्त्रितस्य० इति भर्त्सने द्विर्वचनम् उक्तम्, तस्य आम्रेडितं\n'
        '  प्लवते** — so the two ends of the adhyāya meet: one pāda doubles\n'
        '  the word and the next lengthens the copy. A vārttika adds that the\n'
        '  two may alternate: **भर्त्सने पर्यायेण इति वक्तव्यम्**'
    ),
)

register(
    '8.2.96',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — अङ्गयुक्तं तिङ् आकाङ्क्षम् — and a finite verb construed\n'
        '  with अङ्ग and leaving something EXPECTED, in a threat: **अङ्ग\n'
        '  कू३ज, अङ्ग व्याह३र — इदानीं ज्ञास्यसि जाल्म** — go on, coo; you\n'
        '  will find out, wretch. All three conditions are tested, and the\n'
        '  second — आकाङ्क्षम् — is what keeps the plain अङ्ग पच out'
    ),
)

register(
    '8.2.97',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — विचार्यमाणानाम् — and of sentences being WEIGHED against\n'
        '  each other: **प्रमाणेन वस्तुपरीक्षणं विचारः**. **होतव्यं\n'
        '  दीक्षितस्य गृहा३इ** — is one to make the offering in the\n'
        "  initiate's house or not? **तिष्ठेद् यूपा३इ; अनुप्रहरेद् यूपा३इ**.\n"
        "  The इ at the end of each is 8.2.107's — the ए of the locative\n"
        '  split into a प्लुत आ and an इ — which is why these sentences look\n'
        '  as they do'
    ),
)

register(
    '8.2.98',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — पूर्वं तु भाषायाम् — but in the SPOKEN language it is the\n'
        '  FIRST of the alternatives that is lengthened and not each: **अहिर्\n'
        '  नु३ रज्जुर् नु; लोष्टो नु३ कपोतो नु** — a snake, or a rope?\n'
        '  **प्रयोगापेक्षं पूर्वत्वम्** — first in the order of speaking. And\n'
        "  the sūtra's own भाषा is read as confining the rule before it to\n"
        '  the Veda: **इह भाषाग्रहणात् पूर्वयोगश् छन्दसि विज्ञायते**'
    ),
)

register(
    '8.2.99',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — प्रतिश्रवणे च — and in ASSENT: **प्रतिश्रवणम् अभ्युपगमः,\n'
        '  प्रतिज्ञानम्, श्रवणाभिमुख्यं च। तत्र अविशेषात् सर्वस्य ग्रहणम्** —\n'
        '  three senses of the word and all three taken, since the sūtra\n'
        '  distinguishes none. **देवदत्त भोः — किम् आत्थ३?** and **गां मे\n'
        '  देहि भोः — अहं ते ददामि३**'
    ),
)

register(
    '8.2.100',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        "SETTLED — अनुदात्तं प्रश्नान्ताभिपूजितयोः — and here the heading's\n"
        "  THIRD word is changed: the प्लुत is अनुदात्त at a question's END\n"
        '  and of what is honoured. **अगम३ः पूर्वा३न् ग्रामा३न् अग्निभूता३इ,\n'
        '  पटा३उ** — the vocatives at the close take the low-toned\n'
        '  lengthening and the rest of the words their own by 8.2.105. This\n'
        '  is the first of three sūtras that take the उदात्त away'
    ),
)

register(
    '8.2.101',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — चिदिति चोपमाऽर्थे प्रयुज्यमाने — and where चित् is used to\n'
        '  make a COMPARISON: **अग्निचिद् भाया३त्; राजचिद् भाया३त्** — let\n'
        '  him shine like a fire, like a king. And the vṛtti is careful that\n'
        '  the whole lengthening is being prescribed here and not only its\n'
        '  accent — **प्लुतोऽप्य् अत्र विधीयते, न गुणमात्रम्**'
    ),
)

register(
    '8.2.102',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — उपरिस्विदासीदिति च — and in उपरि स्विद् आसीत्: **अधः\n'
        '  स्विद् आसी३द् उपरि स्विद् आसी३त्**. The two halves of the same\n'
        '  Vedic line take two different accents — **अधः स्विद् आसीद् इत्यत्र\n'
        '  8.2.97 इत्य् उदात्तः प्लुतः**, the deliberation rule giving the\n'
        '  first a high tone, and this sūtra giving the second a low one'
    ),
)

register(
    '8.2.103',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु — and here the\n'
        '  accent changes a second time: the प्लुत before an आम्रेडित is\n'
        '  स्वरित, in envy, approval, anger or contempt. The doubling is\n'
        "  8.1.8's again, and the four senses are four of that sūtra's five —\n"
        '  the fifth, threatening, having been given its own rule with its\n'
        '  own accent at 8.2.95'
    ),
)

register(
    '8.2.104',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — क्षियाऽऽशीःप्रैषेषु तिङ् आकाङ्क्षम् — and a finite verb\n'
        '  that leaves something expected, where a breach of custom, a\n'
        '  blessing or a summons is meant: **क्षिया आचारभेदः, आशीः\n'
        '  प्रार्थनाविशेषः, शब्देन व्यापारणं प्रैषः**. This is the rule\n'
        "  8.1.60's example needed — स्वयं ह रथेन याति३, उपाध्यायं पदातिं\n"
        '  गमयति — where the first verb keeps its accent by that sūtra and\n'
        '  takes its प्लुत by this one'
    ),
)

register(
    '8.2.105',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — अनन्त्यस्यापि प्रश्नाख्यानयोः — and in a QUESTION and its\n'
        '  ANSWER even a word that does not stand last takes it: **अगम३ः\n'
        '  पूर्वा३न् ग्रामा३न् अग्निभूता३इ, पटा३उ**. **सर्वेषाम् एव पदानाम्\n'
        '  एष स्वरितः प्लुतः** — every word in the sentence, and the last one\n'
        '  alone takes the अनुदात्त of 8.2.100 instead. One sentence, two\n'
        '  accents, and the two sūtras five apart'
    ),
)

register(
    '8.2.106',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — प्लुतावैच इदुतौ — where an ऐ or औ is to be lengthened, it\n'
        '  is the इ or उ INSIDE it that is: **ऐ३तिकायन; औ३पमन्यव**. **यद्\n'
        '  एवर्णोवर्णयोर् अवर्णस्य च समविभागः, तद् एदुतौ द्विमात्रौ अनेन\n'
        '  प्लुतौ क्रियेते** — the diphthong is halved, and the second half\n'
        '  is what carries the three mātrās. So the lengthening lands inside\n'
        '  a vowel rather than on it'
    ),
)

register(
    '8.2.107',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ\n'
        '  — a non-प्रगृह्य ए or ओ that is to be lengthened splits: the FIRST\n'
        '  half becomes a प्लुत आ and the second an इ or उ. अग्ने gives\n'
        '  **अग्ना३इ** and पटो gives **पटा३उ**. A vārttika lists where it\n'
        '  holds — **प्रश्नान्ताभिपूजितविचार्यमाणप्रत्यभिवादयाज्यान्तेषु इति\n'
        '  वक्तव्यम्** — five settings, which is why the deliberating\n'
        '  sentences of 8.2.97 all end in that इ'
    ),
)

register(
    '8.2.108',
    apply=the_pluta,
    codification=_THE_PLUTA,
    notes=(
        'SETTLED — तयोर्य्वावचि संहितायाम् — and those इ and उ become य् and\n'
        '  व् before a vowel, in संहिता: **अग्ना३याशा; पटा३वाशा;\n'
        '  अग्ना३यिन्द्रम्; पटा३वुदकम्**.\n'
        '\n'
        "SETTLED — **AND THE SŪTRA'S LAST WORD OPENS A HEADING THAT RUNS TO\n"
        '  THE END OF THE WORK.** **संहितायाम् इत्येतच् च अधिकृतम्। इत\n'
        '  उत्तरम् आध्यायपरिसमाप्तेर् यद् वक्ष्यामः संहितायाम् इत्येवं तद्\n'
        '  वेदितव्यम्** — everything in 8.3 and 8.4 is said of sounds in\n'
        '  close juncture, and no sūtra of those two pādas has to say so'
    ),
)


__all__ = [
    'at_the_end',
    'in_the_word',
    'sasajuso_ruh',
    'the_nistha',
    'the_pluta',
    'the_word_end',
    'visible',
]
