# -*- coding: utf-8 -*-
"""
What each input on the playground form is asking for.

The form is built from the signature of the function that codifies a rule, so
without this table its labels are Python parameter names with the underscores
swapped for spaces: `al vidhi`, `purva vidhi`, `dvirvacana caused by vowel`.
Those are unusable. A reader who could act on them would not need the form,
and a reader who needs the form cannot act on them — which is the whole of
the fifth rule in the north star, met head-on.

So every field carries two things:

  * a **label** a person can read — "operates on sounds?" rather than
    `al vidhi`;
  * a **hint** naming the Sanskrit term the parameter stands for, so the
    label is a way in rather than a substitute. The beginner reads the
    label; the reader who knows the śāstra reads the term and skips the rest.

Keys are the parameter name. A dotted key — `affix.its` — is a member of a
dataclass parameter, and is matched on the full dotted name first, then on
the part after the dot, so a member shared between rules is described once.
"""

from __future__ import annotations

from typing import Dict, NamedTuple, Optional, Tuple


class Help(NamedTuple):
    label: str
    hint: str = ""


#: The whole vocabulary of the forms. 172 names across the codified rules.
HELP: Dict[str, Help] = {
    # --- the commonest, shared across many blocks -------------------------
    "sense": Help(
        "in what sense?",
        "अर्थ — what the word or root means here. Many rules turn on the "
        "sense alone, and nothing in the form shows it, so it must be said.",
    ),
    "given": Help(
        "facts you are asserting",
        "Conditions no form can carry — semantics, context, intent. Give "
        "them comma-separated; a rule that needs one you have not stated "
        "withholds its answer rather than guessing.",
    ),
    "upasargas": Help(
        "prefixes on the verb",
        "उपसर्ग — प्र, परा, अप, सम् and the rest. Comma-separated, in order.",
    ),
    "root": Help(
        "the verbal root",
        "धातु — as the dhātupāṭha enunciates it (डुकृञ्) or in its plain "
        "form (कृ). Either is accepted.",
    ),
    "artha": Help(
        "the root's meaning",
        "The sense the dhātupāṭha assigns, used to tell apart roots that "
        "are spelled alike.",
    ),
    "upapada": Help(
        "the word standing beside it",
        "उपपद — a companion word the rule requires nearby, such as the "
        "अकर्मक noun that some middle-voice rules look for.",
    ),
    "bhava_or_karman": Help(
        "impersonal or passive?",
        "भावकर्मणोः — whether the form is impersonal or passive, which "
        "1.3.13 makes ātmanepada regardless of the root.",
    ),
    "karmakartari": Help(
        "the object acting as agent?",
        "कर्मकर्तरि — भिद्यते कुठारः, where what is acted on is spoken of "
        "as if it acted.",
    ),
    "affixes": Help(
        "affixes present",
        "The प्रत्ययs attached — सन्, णिच्, यङ् and the like. "
        "Comma-separated.",
    ),
    "lakara": Help(
        "which लकार",
        "The tense-mood slot: लट्, लिट्, लुङ्, लोट् and the rest.",
    ),
    "form": Help(
        "the word or particle",
        "The form being asked about, in either script.",
    ),
    "chandas": Help(
        "in the Vedic language?",
        "छन्दसि — many rules hold only in the Veda, or only outside it.",
    ),
    "kriya_yoga": Help(
        "construed with a verb?",
        "क्रियायोगे — whether the word stands with an action. It is what "
        "separates a गति or उपसर्ग from a mere particle.",
    ),
    "sattva": Help(
        "naming a substance?",
        "सत्त्ववचन — a चादि word denoting a thing is not a निपात.",
    ),
    "with_kr": Help(
        "used with कृ?",
        "Some words take their name only in construction with कृ.",
    ),
    "anukarana": Help(
        "an imitative word?",
        "अनुकरण — a sound-imitation, which several rules treat apart.",
    ),
    "followed_by_iti": Help(
        "followed by इति?",
        "इति after the word changes what several rules do with it.",
    ),
    "verb": Help("the verb", "The action the participant stands in."),
    "verb_sense": Help(
        "what the verb means",
        "The sense-class the kāraka rules ask after — गति, हिंसा, भी, and "
        "so on. Comma-separated.",
    ),
    "causative": Help(
        "a causative?",
        "णिच् — whether the verb is causative, which moves the agent.",
    ),
    "affix": Help(
        "which affix are you asking about?",
        "प्रत्यय (pratyaya) — named in its उपदेश (upadeśa) form, "
        "the shape the grammar states it in, marks and all: क्त "
        "(kta), शतृ (śatṛ), ण्वुल् (ṇvul). Some rules do not ADD "
        "an affix but say something about one — 3.2.102 says the "
        "affix called निष्ठा (niṣṭhā) comes in the past, 3.2.127 "
        "gives शतृ and शानच् (śānac) the name सत् (sat). Those "
        "are asked by naming the affix.",
    ),
    "word": Help(
        "which fixed word are you asking about?",
        "निपातन (nipātana) — a form the grammar GIVES rather than "
        "derives. यदिह लक्षणेनानुपपन्नं तत् सर्वं निपातनात् सिद्धम् "
        "(yadiha lakṣaṇenānupapannaṃ tat sarvaṃ nipātanāt siddham): "
        "whatever the rules do not reach, the fixing supplies. Ask by "
        "the finished word — ऋत्विक् (ṛtvik) a priest, आत्मम्भरिः "
        "(ātmambhariḥ) one who feeds only himself — and the answer "
        "names the rule that fixes it and says what is being fixed.",
    ),
    "ending": Help(
        "the ending attached",
        "The तिङ् or सुप् ending, in its upadeśa form.",
    ),
    "first": Help("the first sound or word", "What stands earlier."),
    "second": Help("the second sound or word", "What stands later."),
    "words": Help(
        "the words, in order",
        "Comma-separated. Where a rule needs more than the spelling, a "
        "member may be written stem:tag — गार्ग्य:vṛddha.",
    ),
    "connected": Help(
        "are they connected in sense?",
        "सामर्थ्य — 2.1.1 requires it of every rule about words. Two words "
        "adjacent by accident compound nothing.",
    ),
    "first_vibhakti": Help(
        "case of the first member",
        "1 to 7. Leave blank if not stated. 2.1.24 onward want 2 here — "
        "the accusative, the case for what an action reaches.",
    ),
    "second_vibhakti": Help(
        "case of the second member",
        "1 to 7. Leave blank if not stated.",
    ),
    "first_vacana": Help("number of the first member", "1, 2 or 3."),
    "second_vacana": Help("number of the second member", "1, 2 or 3."),
    "nipata": Help("is it a particle?", "निपात — by 1.4.56 and after."),
    "stem": Help("the nominal stem", "प्रातिपदिक — the form before endings."),
    "is_name": Help("is it a proper name?", "संज्ञायाम् — a name, not a description."),
    "samasa": Help(
        "what kind of compound",
        "Which compound the word stands in, where the rule asks.",
    ),
    "operation": Help(
        "which operation",
        "The rule you are asking about — dīrgha, dvirvacana, svara and the "
        "rest. Several rules name particular operations and exclude them.",
    ),
    "dvivacana": Help("a dual form?", "द्विवचन — 1.1.11's प्रगृह्य turns on it."),
    "ang": Help("the particle अङ्ग?", "One of the vocative particles 1.1.14 names."),
    "sambuddhi": Help("a vocative singular?", "सम्बुद्धि."),
    "before_iti": Help("standing before इति?", ""),
    "arsa": Help("a Vedic ṛṣi usage?", "आर्ष — of the seers."),
    "saptami_artha": Help("in a locative sense?", "सप्तम्यर्थे."),
    "before_jas": Help("before जस्?", "The nominative plural ending."),
    "vyavastha": Help(
        "a fixed relative position?",
        "व्यवस्थायाम् — पूर्व and its fellows are pronouns only when they "
        "place a thing relatively, not absolutely.",
    ),
    "means_kin_or_wealth": Help(
        "does स्व mean kin or wealth?",
        "स्व is a pronoun in the sense 'one's own', not when it means a "
        "kinsman or property.",
    ),
    "bahiryoga_or_upasamvyana": Help(
        "outer connection, or clothing?",
        "The two senses 1.1.36 excepts for अन्तर.",
    ),
    "sutra_id": Help("which sūtra", "Its number, as 1.1.49."),
    "accents": Help(
        "the accents, in order",
        "उदात्त, अनुदात्त or स्वरित for each syllable. Comma-separated.",
    ),
    "setting": Help("where it is being recited", "The rite or context."),
    "japa": Help("muttered recitation?", "जप."),
    "nyunkha": Help("with न्युङ्ख?", ""),
    "saman": Help("a सामन् chant?", ""),
    "vasatkara": Help("the वषट्कार?", ""),
    "samhita": Help("continuous recitation?", "संहिता — as against pada-pāṭha."),
    "jati": Help(
        "does the word name a CLASS of things?",
        "जाति (jāti) — a class or kind, as against an individual "
        "or a quality. 3.2.78 wants a companion that is NOT one: "
        "उष्णभोजी (uṣṇabhojī), one who eats his food hot, is "
        "formed — but of ब्राह्मण (brāhmaṇa), which names a class, "
        "the affix does not come.",
    ),
    "stri_akhya": Help("does it itself mean a woman?", "स्त्र्याख्या — 1.4.3's condition."),
    "before_ngit": Help("before a ङित् affix?", ""),
    "ends_in_sup_or_tin": Help("ends in a सुप् or तिङ्?", "What makes a पद."),
    "before_kya": Help("before क्य?", ""),
    "before_sit": Help("before a शित् affix?", ""),
    "sup_affix": Help("which सुप् ending", "In upadeśa form."),
    "sarvanamasthana": Help("a सर्वनामस्थान ending?", "The strong cases."),
    "matvartha": Help("a possessive suffix?", "मत्वर्थ — meaning 'having'."),
    "ayasmayadi": Help("one of the अयस्मयादि?", ""),
    "napumsaka": Help("neuter?", "नपुंसक."),
    "vowel": Help("the vowel", "A single vowel, in either script."),
    "pratyaya": Help("is it an affix?", "प्रत्यय."),
    "counted": Help("how many", "The number of things meant."),
    "asmad": Help("is अस्मद् among them?", "1.4.107's condition."),
    "star": Help("the star's name", "नक्षत्र."),
    "nakshatra": Help("a star name?", ""),
    "dvandva_of": Help("the members of the द्वन्द्व", "Comma-separated."),
    "with_numeral": Help("with a numeral?", "संख्या beside it."),
    "taddhita_final": Help("ends in a तद्धित?", ""),
    "sarvavibhakti": Help("does it take every case?", "1.1.38 turns on it."),
    "krt_final": Help("ends in a कृत्?", ""),
    "krt_affix": Help("which कृत् affix", ""),
    "avyayibhava": Help("an अव्ययीभाव compound?", "1.1.41 makes it indeclinable."),
    "topic": Help("which definition", "The old definition being asked about."),
    "sound": Help("the sound", "A single sound, in either script."),
    "text": Help("the text", "The stretch being asked about."),
    "al_vidhi": Help(
        "does the rule work on sounds?",
        "अल्विधि — a rule operating on a sound as a sound (lengthen this "
        "vowel) rather than on a grammatical thing (attach this to a root). "
        "This is the pivot of 1.1.56: substitutes do not inherit for these.",
    ),
    "sthanin_is_vowel": Help(
        "was the thing replaced a vowel?",
        "स्थानिन् — what the substitute stands in for. One of 1.1.57's "
        "three conditions.",
    ),
    "caused_by_following": Help(
        "was it caused by what follows?",
        "परस्मिन् — the substitution occasioned by something after it. The "
        "second of 1.1.57's three.",
    ),
    "purva_vidhi": Help(
        "does the operation act on what precedes?",
        "पूर्वविधि — the third of 1.1.57's conditions. All three must hold "
        "together for a sound-rule to see the substitute as its original.",
    ),
    "dvirvacana_caused_by_vowel": Help(
        "is reduplication occasioned by a vowel?",
        "द्विर्वचनेऽचि — 1.1.59's narrow re-admission, after 1.1.58 has "
        "shut reduplication out.",
    ),
    "term": Help("the term", "A word or pratyāhāra used in a rule."),
    "upasarjana": Help("is it subordinate?", "उपसर्जन — the lesser member."),
    "ends_in_go": Help("ends in गो?", ""),
    "stri_pratyaya": Help("ends in a feminine suffix?", "स्त्रीप्रत्यय."),
    "taddhita_luk": Help("a तद्धित elided by लुक्?", ""),
    "ends_in_goni": Help("ends in गोणी?", ""),
    "iyan_uvan_place": Help(
        "will इयङ् or उवङ् go here?",
        "1.4.4 excepts these places — श्री, भ्रू — from नदी.",
    ),
    "is_stri": Help("is the word स्त्री?", "Excepted by name in 1.4.4."),
    "before_am": Help("before आम्?", ""),
    "coreferential": Help("do they refer to the same thing?", "सामानाधिकरण्य."),
    "prahasa": Help("said in mockery?", "प्रहासे — 1.4.106's condition."),
    "is_manyati": Help("is the verb मन्?", "1.4.106 needs मन् beside it."),
    "done": Help("what has already been done", "The earlier operation."),
    "to": Help("the rule now being applied", "The later operation."),
    "same_locus": Help(
        "do both rest on the same thing?",
        "समानाश्रय — 6.4.22's asiddhavat holds only then.",
    ),
    "done_is_apavada": Help("was it an अपवाद?", "An exception rule."),
    "reading_a_case_ending": Help("is a case ending being read?", ""),
    "done_is_nalopa": Help("was it न-elision?", ""),
    "done_is_mu": Help("was it the मु augment?", ""),
    "applying_nabhava": Help("applying न-substitution?", ""),
    "target": Help("what the operation would change", ""),
    "ardhadhatuka": Help("an आर्धधातुक affix?", ""),
    "kriyasamabhihara": Help(
        "is the action repeated or intense?",
        "क्रियासमभिहार — पौनःपुन्यं भृशार्थो वा, doing a thing again and "
        "again or doing it hard. यङ् is for this sense and no other.",
    ),
    "sopasarga": Help(
        "does the root carry a preverb?",
        "सोपसर्ग — 3.1.22 says धातोः, so the affix does not come after a "
        "root with a preverb on it: भृशं प्राटति.",
    ),
    "sanadyanta": Help(
        "does the stem end in one of the सनादि affixes?",
        "सनाद्यन्त — सन्, यङ् and the rest. 3.1.32 makes such a stem a "
        "root in its own right, which no list needs to record.",
    ),
    "yananta": Help(
        "is this a यङन्त stem?",
        "यङन्त — a stem ending in यङ्. पचादि is an आकृतिगण, an open list, "
        "and the Kāśikā puts these stems in it by name.",
    ),
    "before_ac": Help(
        "is a vowel affix following?",
        "अचि — 2.4.74 drops the यङ् only before an affix beginning with a "
        "vowel, and the अच् of 3.1.134 is one.",
    ),
    "snu": Help(
        "does the stem end in the affix श्नु?",
        "श्नु — one of the three things 6.4.77 reaches, beside a धातु and "
        "भ्रू: आप्नुवन्ति, शक्नुवन्ति.",
    ),
    "bhru": Help(
        "is the word भ्रू?",
        "भ्रू, 'brow' — named in 6.4.77 by itself, since it is neither a "
        "श्नु-stem nor a root: भ्रुवौ, भ्रुवः.",
    ),
    "div": Help(
        "is the verb दिव् in the gaming sense?",
        "दिवस्तदर्थस्य — the sense व्यवहृ and पण् share at 2.3.57. "
        "शतस्य दीव्यति. तदर्थस्येति किम्? ब्राह्मणं दीव्यति.",
    ),
    "tadartha": Help(
        "in the sense the rule before it names?",
        "तदर्थ — दिव् only where it means what व्यवहृ and पण् mean.",
    ),
    "upasarga": Help(
        "is a preverb attached?",
        "उपसर्ग — with one, 2.3.58's invariable sixth becomes a choice: "
        "शतस्य प्रतिदीव्यति beside शतं प्रतिदीव्यति.",
    ),
    "brahmana": Help(
        "is this in a Brāhmaṇa text?",
        "ब्राह्मणे — there दिव् takes a second where 2.3.58 gave a sixth.",
    ),
    "presya_bruva": Help(
        "is it the oblation at the call?",
        "प्रेष्यब्रुवोः — प्रेष्य is one form of one root in one class, "
        "the singular imperative of the दैवादिक इष्, and ब्रू is taken "
        "in the same setting साहचर्यात्.",
    ),
    "chandas": Help(
        "is this Vedic?",
        "छन्दसि — 2.3.62 and 2.3.63 hold there only, and both say "
        "बहुलम्, so what they give stands beside what would else come.",
    ),
    "yaj_karana": Help(
        "is it the instrument of यज्?",
        "यजेश्च करणे — घृतस्य यजते beside घृतेन यजते, in the Veda.",
    ),
    "krtvo_artha": Help(
        "is a 'so many times' affix used?",
        "कृत्वोऽर्थ — पञ्चकृत्वोऽह्नो भुङ्क्ते. प्रयोगग्रहणं किम्? "
        "अहनि भुक्तम् has the sense but not the affix.",
    ),
    "krt": Help(
        "which कृत् affix follows",
        "कृत् — 2.3.65 gives doer and object a sixth before one. Seven "
        "of them refuse it (2.3.69) and two more (2.3.70); क्त in the "
        "present or place sense takes it back.",
    ),
    "ubhaya_prapti": Help(
        "could both the doer and the object take it?",
        "उभयप्राप्तौ — and then only the OBJECT does: आश्चर्यो गवां "
        "दोहोऽगोपालकेन, the milker falling to a third.",
    ),
    "kta_vartamana": Help(
        "is the क्त in the present sense?",
        "वर्तमाने — राज्ञां मतः. वर्तमान इति किम्? ग्रामं गतः.",
    ),
    "kta_adhikarana": Help(
        "does the क्त name the place of the act?",
        "अधिकरणवाचिनः, by 3.4.76 — इदमेषाम् आसितम्.",
    ),
    "krtya": Help(
        "is it a कृत्य affix?",
        "कृत्य — तव्य, अनीयर्, यत् and the rest. With one, the doer "
        "takes the sixth optionally and the object not at all.",
    ),
    "tulya_artha": Help(
        "which word meaning 'like'",
        "तुल्यार्थ — तुल्य, सदृश and their fellows take a third or a "
        "sixth. तुला and उपमा are excepted by name though they mean "
        "the same.",
    ),
    "blessing_with": Help(
        "which of the seven blessing-words",
        "आयुष्य, मद्र, भद्र, कुशल, सुख, अर्थ, हित — each takes a fourth "
        "where a blessing is meant, and a sixth beside it.",
    ),
    "vibhakta": Help(
        "is the singling-out a comparison between groups?",
        "विभक्त — माथुराः पाटलिपुत्रकेभ्यः सुकुमारतराः, the men of "
        "Mathurā more delicate than those of Pāṭaliputra. It takes the "
        "case out of 2.3.41.",
    ),
    "sadhu_nipuna": Help(
        "is it with साधु or निपुण?",
        "Those two take a seventh for the one they are good TO: मातरि "
        "साधुः.",
    ),
    "arca": Help(
        "is praise meant?",
        "अर्चा — अर्चायामिति किम्? साधुर्भृत्यो राज्ञः is plain "
        "statement, तत्त्वकथने न भवति.",
    ),
    "prati": Help(
        "is प्रति used with it?",
        "अप्रतेः — साधुर्देवदत्तो मातरं प्रति. With प्रति the rule "
        "stands off and 2.3.8 gives a second instead.",
    ),
    "prasita_utsuka": Help(
        "is it with प्रसित or उत्सुक?",
        "प्रसितः प्रसक्तः, one bound up in a thing for good. Both take "
        "a third or a seventh: केशैः प्रसितः beside केशेषु प्रसितः.",
    ),
    "naksatra_lup": Help(
        "is it a lunar mansion whose affix has been elided?",
        "नक्षत्रे लुपि — पुष्येण पायसमश्नीयात् beside पुष्ये. "
        "लुपीति किम्? मघासु ग्रहः has no elision.",
    ),
    "pratipadika_artha": Help(
        "is nothing but the stem's own meaning intended?",
        "प्रातिपदिकार्थमात्र — and मात्र attaches to gender, measure and "
        "number as well. Anything ADDED takes the case elsewhere.",
    ),
    "sambodhana": Help(
        "is someone being called out to?",
        "सम्बोधन (sambodhana) — आभिमुख्यकरणम्, turning toward "
        "someone: हे देवदत्त (he devadatta). That form is then "
        "आमन्त्रित by 2.3.48 and its singular संबुद्धि by 2.3.49. "
        "3.2.125 asks the same question for a different purpose: "
        "the participle हे पचन् (he pacan) is formed only in "
        "address, because the rule before it had shut out "
        "agreement with a first-case word.",
    ),
    "vacana": Help(
        "how many — one, two or many",
        "वचन. 2.3.49 names the SINGULAR of an आमन्त्रित संबुद्धि; the "
        "dual and plural stay merely आमन्त्रित.",
    ),
    "sesa": Help(
        "is it the leftover relation?",
        "शेष — कर्मादिभ्योऽन्यः, whatever is left when every kāraka has "
        "been taken and the stem-meaning too: राज्ञः पुरुषः. Asked "
        "last, because a remainder cannot be found first.",
    ),
    "jna_avidartha": Help(
        "is it ज्ञा NOT meaning 'know'?",
        "अविदर्थ — सर्पिषो जानीते, and it is the INSTRUMENT that takes "
        "the sixth. What अविदर्थ excludes is left OPEN: the Kāśikā "
        "offers two readings and settles on neither.",
    ),
    "sixth_object_verb": Help(
        "which verb whose object takes a sixth",
        "2.3.52 to 2.3.57 name them: remembering, pitying, ruling, "
        "bettering, hurting, asking a blessing, six of violence, and "
        "dealing. Each gives its object a sixth शेषत्वेन विवक्षिते — "
        "the object spoken of as a mere relation.",
    ),
    "sarvanaman": Help(
        "is the word a pronoun?",
        "सर्वनामन् — 1.1.27's list. With one of those and the word हेतु, "
        "the cause may take a third as well as the sixth.",
    ),
    "fifth_after": Help(
        "which word of difference is it after",
        "अन्य, आरात्, इतर, ऋते and the rest of 2.3.29's eight. अन्य is "
        "taken by its SENSE, so भिन्न and विलक्षण come with it.",
    ),
    "atas_affix": Help(
        "does the other word carry an अतसुच्-type affix?",
        "By 5.3.28 — दक्षिणतः, पुरस्तात्, उपरिष्टात्. What they govern "
        "takes a sixth.",
    ),
    "enap": Help(
        "does it carry the एनप् affix?",
        "By 5.3.35 — दक्षिणेन, उत्तरेण. It gives a second where 2.3.30 "
        "would have given a sixth, and the sixth is wanted too.",
    ),
    "prthag_vina_nana": Help(
        "is it with पृथक्, विना or नाना?",
        "Those three take a third or a fifth, either — पृथग् देवदत्तेन "
        "beside पृथग् देवदत्तात्.",
    ),
    "little_and_hard": Help(
        "which of स्तोक, अल्प, कृच्छ्र, कतिपय",
        "2.3.33's four. They add a fifth beside the third the instrument "
        "already had: स्तोकाद् मुक्तः beside स्तोकेन मुक्तः.",
    ),
    "asattva": Help(
        "does it name a quality rather than a thing?",
        "असत्त्ववचन — यदा धर्ममात्रं करणतया विवक्ष्यते न द्रव्यम्. "
        "Naming a substance, and 2.3.33 does not reach it.",
    ),
    "dura_antika": Help(
        "does the word mean far or near?",
        "दूरान्तिकार्थ — and these take four cases across 2.3.34 to "
        "2.3.36: दूरं, दूरात्, दूरेण, दूरे ग्रामस्य.",
    ),
    "bhava_laksana": Help(
        "does this one's action mark when another happened?",
        "भावलक्षण — गोषु दुह्यमानासु गतः. प्रसिद्धा क्रिया क्रियान्तरं "
        "लक्षयति: only a known act can mark another.",
    ),
    "holding": Help(
        "which word of holding or standing-for",
        "स्वामिन्, ईश्वर, अधिपति, दायाद, साक्षिन्, प्रतिभू, प्रसूत — "
        "and आयुक्त, कुशल from 2.3.40. Each takes a sixth or a seventh.",
    ),
    "asevaa": Help(
        "is habitual application meant?",
        "आसेवा तात्पर्यम् — आयुक्तः कटकरणे, set to mat-making as his "
        "work. आयुक्तो गौः शकटे is an ox in a place, and not this.",
    ),
    "nirdharana": Help(
        "is one being singled out of a group?",
        "निर्धारण — जातिगुणक्रियाभिः समुदायाद् एकदेशस्य पृथक्करणम्. The "
        "group takes a sixth or a seventh, and 2.2.10 keeps that "
        "genitive from ever compounding.",
    ),
    "kriyartha_upapada": Help(
        "is the verb of purpose left unspoken?",
        "क्रियार्थोपपद — एधेभ्यो व्रजति, 'goes for firewood', where the "
        "fetching is understood and never said. What that unspoken verb "
        "would have reached takes a fourth.",
    ),
    "tumartha_bhava": Help(
        "is it a noun of action meaning 'in order to'?",
        "तुमर्थ भाववचन — पाकाय व्रजति. तुमर्थादिति किम्? पाकः alone is "
        "no purpose; भाववचनादिति किम्? कारकः names a doer.",
    ),
    "namas_yoga": Help(
        "which word of blessing is it with",
        "नमस्, स्वस्ति, स्वाहा, स्वधा, अलम्, वषट्. अलम् is taken by its "
        "SENSE of sufficiency, so प्रभु and शक्त come with it.",
    ),
    "manya_karman": Help(
        "is it what मन् thinks of?",
        "मन्यकर्म — and the sūtra says मन्य, not मन्, which keeps out "
        "the same root in another class: न त्वा तृणं मन्वे.",
    ),
    "anadara": Help(
        "is it being thought little of?",
        "अनादरस्तिरस्कारः — contempt. Without it the verse "
        "अश्मानं दृषदं मन्ये takes no fourth.",
    ),
    "apranin": Help(
        "is the thing not alive?",
        "अप्राणिषु — 2.3.17 reaches only what has no life in it.",
    ),
    "saha_yukta": Help(
        "is it construed with सह?",
        "सहयुक्त — and the rule is worded by SENSE, सहार्थेन, so "
        "सार्धम् serves as well.",
    ),
    "apradhana": Help(
        "is this the lesser of the two?",
        "अप्रधान — पुत्रेण सहागतः पिता: the father is what the sentence "
        "speaks of, the son only understood. अप्रधान इति किम्? "
        "शिष्येण सहोपाध्यायस्य गौः.",
    ),
    "anga_vikara": Help(
        "does a defect in this limb mark the whole person?",
        "येनाङ्गविकारः — अक्ष्णा काणः. अवयवधर्मेण समुदायो व्यपदिश्यते. "
        "अङ्गविकार इति किम्? अक्षि काणमस्य.",
    ),
    "itthambhuta_laksana": Help(
        "is it the mark you know him by?",
        "इत्थंभूतलक्षण — कमण्डलुना छात्रम्, the student known by his "
        "water-pot. Not where the mark is already inside a compound.",
    ),
    "samjna_karman": Help(
        "is it what सञ्जानीते recognises?",
        "The object of सम् + ज्ञा takes a third or a second, either: "
        "पित्रा संजानीते beside पितरं संजानीते.",
    ),
    "hetu": Help(
        "is it the cause?",
        "हेतु — फलसाधनयोग्यः पदार्थः, what is fit to bring a result "
        "about: धनेन कुलम्, विद्यया यशः.",
    ),
    "rna": Help(
        "is the cause a debt?",
        "ऋण — शताद् बद्धः, bound for a hundred. It takes a fifth "
        "instead of 2.3.23's third.",
    ),
    "akartari": Help(
        "is the debt NOT what set the act going?",
        "अकर्तरि — शतेन बन्धितः has the same hundred as a कर्तृ, "
        "प्रयोजकत्वात्, and there 2.3.18 gives it a third instead.",
    ),
    "guna": Help(
        "is the cause a quality?",
        "गुण — जाड्याद् बद्धः beside जाड्येन बद्धः, either way. "
        "गुणग्रहणं किम्? धनेन कुलम् — wealth is no quality.",
    ),
    "astri": Help(
        "is that quality-word not feminine?",
        "अस्त्रियाम् — बुद्ध्या मुक्तः and प्रज्ञया मुक्तः are feminine, "
        "and only the third stands there.",
    ),
    "hetu_prayoga": Help(
        "is the word हेतु itself used?",
        "हेतुप्रयोग — अन्नस्य हेतोर् वसति, and then the cause takes a "
        "sixth rather than a third.",
    ),
    "karaka": Help(
        "which kāraka is this?",
        "कारक — कर्म, करण, सम्प्रदान and the rest. 1.4.23 to 1.4.55 "
        "decide it and this section gives it an ending, so the answer "
        "comes from there.",
    ),
    "expressed_by": Help(
        "has something already said it?",
        "अनभिहिते — a kāraka takes an ending only if nothing else has "
        "expressed it. Four things can, and no more: तिङ्, कृत्, "
        "तद्धित, समास. क्रियते कटः needs no accusative.",
    ),
    "karmapravacaniya": Help(
        "which कर्मप्रवचनीय particle is it construed with",
        "कर्मप्रवचनीय — अनु, उप, अधि, अप, आङ्, परि and the rest, named "
        "at 1.4.83 to 1.4.98. Which one it is decides the ending.",
    ),
    "antara": Help(
        "is it construed with अन्तरा or अन्तरेण?",
        "Those two words take a second case and displace a genitive: "
        "अन्तरा त्वां च मां च कमण्डलुः.",
    ),
    "kala_adhvan": Help(
        "does the word name a time or a distance?",
        "कालाध्वन् — three rules turn on it, and which ending it takes "
        "depends on how the time or road is involved.",
    ),
    "atyanta_samyoga": Help(
        "is the whole stretch taken up?",
        "अत्यन्तसंयोग — साकल्येन संबन्धः. मासमधीते fills the month; "
        "मासस्य द्विरधीते does not.",
    ),
    "apavarga": Help(
        "was it carried through to its result?",
        "अपवर्ग — फलप्राप्तौ सत्यां क्रियापरिसमाप्तिः. मासेनानुवाकोऽधीतः "
        "learnt the chapter; मासमधीतः only spent the month.",
    ),
    "karaka_madhye": Help(
        "does the time or distance stand between two kārakas?",
        "कारकमध्ये — अद्य भुक्त्वा देवदत्तो द्व्यहे भोक्ता: the two days "
        "lie between the eater and his eating.",
    ),
    "adhika": Help(
        "is one thing more than the other?",
        "यस्मादधिकम् — उप खार्यां द्रोणः, a droṇa over and above a "
        "khārī. The thing exceeded takes a seventh.",
    ),
    "isvara_vacana": Help(
        "is an owner or a possession meant?",
        "यस्य चेश्वरवचनम् — and either may take the seventh: अधि "
        "ब्रह्मदत्ते पञ्चालाः beside अधिपञ्चालेषु ब्रह्मदत्तः.",
    ),
    "pratinidhi_pratidana": Help(
        "is something being substituted or repaid?",
        "प्रतिनिधि is a stand-in — मुख्यसदृशः — and प्रतिदान is paying "
        "back what was given: माषानस्मै तिलेभ्यः प्रति यच्छति.",
    ),
    "gati_artha": Help(
        "is the verb one of going?",
        "गत्यर्थ — गम्, व्रज् and the like. गत्यर्थग्रहणं किम्? "
        "ओदनं पचति is no going.",
    ),
    "cesta": Help(
        "is the motion bodily?",
        "चेष्टा — परिस्पन्दक्रिया, a movement of the body. "
        "चेष्टायामिति किम्? मनसा पाटलिपुत्रं गच्छति — the mind travels "
        "and the man stays put.",
    ),
    "adhvan": Help(
        "is what is reached a road?",
        "अनध्वनि — the rule stops at a road, and अध्वनीत्यर्थग्रहणम् "
        "takes पन्थानम् and मार्गम् with it.",
    ),
    "chandas_hu": Help(
        "is this हु in the Veda?",
        "छन्दसि — there हु's object may take a third as well as a "
        "second: यवाग्वा अग्निहोत्रं जुहोति.",
    ),
    "members": Help(
        "the two words, in either order",
        "The rules of 2.2.30 onward decide which is spoken first, so the "
        "order you type them in is not the answer. More than two and no "
        "rule applies — बहुष्वनियमः.",
    ),
    "saptami": Help(
        "which member stands in the locative",
        "सप्तमी — 2.2.35 puts it first in a बahuvrīhi: कण्ठेकालः.",
    ),
    "visesana": Help(
        "which member qualifies the other",
        "विशेषण — भेदकं विशेषणम्, the one that narrows. 2.2.35 puts it "
        "first in a बahuvrīhi: चित्रगुः.",
    ),
    "nistha": Help(
        "which member ends in a निष्ठा affix",
        "निष्ठा — क्त and क्तवतु, by 1.1.26. Stated rather than worked "
        "out, since that rule is about the affix and this is a word.",
    ),
    "jati_kala_sukha": Help(
        "is the other member a word of kind, time or ease?",
        "The vārttika on 2.2.36 — निष्ठायाः पूर्वनिपाते "
        "जातिकालसुखादिभ्यः परवचनम् — sends the निष्ठा to SECOND place "
        "after such a word: मासजातः, शार्ङ्गजग्धी.",
    ),
    "after": Help(
        "which affix occasioned the doubling",
        "6.1.9 names two, सन् and यङ्. Only यङ् — the one that means "
        "doing a thing again and again — is codified so far.",
    ),
    "yan_luk": Help(
        "has यङ् itself dropped out?",
        "यङ्लुक् — the intensive affix is added and then elided, leaving "
        "the doubling behind as the only sign of it. नर्नर्ति is यङ्लुक्; "
        "नरीनृत्यते keeps its यङ्.",
    ),
    "augment": Help(
        "which addition the copy takes",
        "रीक्, रिक् or रुक् — री, रि or a bare र्. 7.4.90 gives रीक् "
        "wherever the root has an ऋ; the other two are 7.4.91's and are "
        "refused unless यङ् has dropped.",
    ),
    "kit": Help(
        "is the addition marked क्?",
        "कित् — 7.4.83 lengthens the copy's vowel only अकितः, where no "
        "क्-marked addition has come in. यंयम्यते has one and stays short.",
    ),
    "dhatu_lopa": Help("has part of the root been elided?", "धातुलोप — and the question is about THIS affix, not any elision "
        "that happened earlier. लोलूय loses its य when अच् is added, "
        "and it is that same अच् which would have strengthened the "
        "vowel, so it forfeits the right. Say no where only an "
        "it-letter went: लूञ् drops its ञ् and still gives लविता."),
    "elided_final": Help("has the aṅga's final vowel been elided?",
        "1.1.57 अचः परस्मिन् पूर्वविधौ — a vowel dropped because of what "
        "follows still counts as standing, for any rule that looks to its "
        "LEFT. So after 6.4.48 has taken the अ off कथ (katha), the थ् has "
        "not become the penult and 7.2.116 अत उपधायाः finds no अ to "
        "lengthen: कथयति (kathayati), not काथयति. Say yes only where a "
        "vowel went, and only where what took it stands after it."),
    "item": Help("the item", ""),
    "sthanin": Help("what is being replaced", "स्थानिन्."),
    "candidates": Help("the possible substitutes", "Comma-separated."),
    "praci_desa": Help("an eastern place name?", "प्राचां देशे — 1.1.75."),
    "dhatu": Help("is it a root?", "धातु."),
    "in_compound": Help("inside a compound?", "1.4.8 gives पति the name only there."),
    "chandas_with_genitive": Help("Vedic, with a genitive?", ""),
    "before_conjunct": Help("before a consonant cluster?", "संयोग — makes a syllable heavy."),
    "varttika": Help("apply the vārttika?", "A supplement to the sūtra."),
    "scheme": Help("which scheme", "Fourfold or fivefold, for 1.1.9."),
    "its": Help("the it-letters", "The indicatory marks. Comma-separated."),
    "substitute": Help("the substitute", "आदेश."),
    "pancami": Help("stated in the fifth case?", "पञ्चमी — 1.1.67's ablative."),
    "elision": Help("which elision", "लुक्, श्लु or लुप्."),
    "anga": Help("is it the अङ्ग?", "The stem an affix attaches to."),
    "samasa_vidhi": Help("a rule about compounding?", ""),
    "marked": Help("the marked form", "A form written with its accent."),
    "ekavibhakti": Help("stated in one case throughout?", "एकविभक्ति — 1.2.43."),
    "purvanipata": Help("does it come first?", "पूर्वनिपात."),
    "arthavat": Help("is it meaningful?", "अर्थवत् — 1.2.45's requirement."),
    "krdanta": Help("ends in a कृत्?", ""),
    "taddhitanta": Help("ends in a तद्धित?", ""),
    "vakya": Help("is it a phrase?", "वाक्य — excluded from प्रातिपदिक."),
    "gender": Help("the gender", "masculine, feminine or neuter."),
    "number": Help("the number", "1, 2 or 3."),
    "lup": Help("elided by लुप्?", "1.2.51 keeps gender and number then."),
    "qualifier": Help("is it a qualifier?", "विशेषण."),
    "count": Help("how many things", ""),
    "gap_matras": Help(
        "gap between the sounds, in mātrās",
        "Half a mātrā or less is संहिता. Fractions are accepted — 0.5.",
    ),
    "stopped": Help("is this a full stop?", "अवसान — the end of an utterance."),
    "restriction": Help("read as a restriction?", ""),
    "enumeration": Help("read as an enumeration?", ""),
    "length": Help("how long", "In mātrās."),
    "index": Help("which position", "Counting from the start."),
    "before": Help("what stands before", ""),
    "after": Help("what stands after", ""),
    "present": Help("what is actually there", "For 1.1.60, whose subject is absence."),
    "name": Help("the pratyāhāra's name", "As aiC, iK, haL."),
    "samasa_or_pratyaya_vidhi": Help("a rule about a compound or an affix?", ""),
    "tatpurusa": Help("a तत्पुरुष?", ""),
    "samanadhikarana": Help("do the members refer to one thing?", "सामानाधिकरण्य — 1.2.42."),
    "vibhakti": Help(
        "which case is it in?",
        "विभक्ति (vibhakti) — the case-ending slot, 1 for the nominative "
        "through 7 for the locative. 2.4.83 excepts the fifth by name, so "
        "उपकुम्भादानय (upakumbhādānaya) keeps its ending where "
        "उपकुम्भं तिष्ठति (upakumbhaṃ tiṣṭhati) does not; 2.4.84 makes the "
        "third and the seventh a choice.",
    ),
    "taddhita": Help("is it a तद्धित affix?", ""),
    "uddesin": Help("the first list", "उद्देशिन् — what is pointed to."),
    "anudesin": Help("the second list", "अनुदेशिन् — what is assigned. 1.3.10 pairs them in order, and refuses unequal lists."),
    "base": Help("the base", "What the affix attaches to."),
    "prescribed_from": Help("prescribed after what", "1.4.13's condition for अङ्ग."),
    "padavidhi": Help("is it a rule about words?", "पदविधि — 2.1.1 reaches no rule about sounds."),
    "preceding_is_sup": Help("is the word before a subanta?", "सुप् — 2.1.2's first condition."),
    "following_is_amantrita": Help("is the word after a vocative?", "आमन्त्रित."),
    "second_is": Help("what the second member is", "'sup' for a noun, 'tiṅ' for a finite verb."),
    "utsarga": Help("the general rule", "उत्सर्ग — the rule being excepted."),
    "apavada": Help("the exception", "अपवाद — the rule that excepts it."),
    "utsarga_affix": Help("the general rule's affix", ""),
    "apavada_affix": Help("the exception's affix", ""),
    "varna_vidhi": Help("a rule about sounds?", "वर्णविधि — 6.1.85 does not reach these."),
    # --- 2.4.1 to 2.4.31 : the number and gender of a compound ----------
    "anga_of": Help(
        "a limb — of what?",
        "अङ्ग (aṅga) here is a LIMB, not the अङ्ग of 6.4.1 that an affix "
        "attaches to. 2.4.2 takes three kinds and takes them separately: "
        "prāṇin, a living body — पाणिपादम् (pāṇipādam), hand-and-foot; "
        "tūrya, an instrument — मार्दङ्गिकपाणविकम् (mārdaṅgikapāṇavikam); "
        "senā, an army — रथिकाश्वारोहम् (rathikāśvāroham). A limb "
        "compounded with a drum-part is none of the three.",
    ),
    "jati_of": Help(
        "a class of what?",
        "जाति (jāti) — a kind rather than an individual. 2.4.6 makes one "
        "only of a class of SUBSTANCES, dravya: आराशस्त्रि (ārāśastri). A "
        "class of qualities (guṇa) or of actions (kriyā) is not made one "
        "— रूपरसगन्धस्पर्शाः (rūparasagandhasparśāḥ) stays plural.",
    ),
    "member_count": Help(
        "how many things are compounded",
        "बहुप्रकृति (bahuprakṛti) — 2.4.12's vārttika opens its option "
        "only where MORE than two are joined, for eight of its ten kinds: "
        "न द्विप्रकृतिः (na dviprakṛtiḥ). So बदरामलके (badarāmalake) stays "
        "dual and प्लक्षन्यग्रोधम् (plakṣanyagrodham) does not.",
    ),
    "names": Help(
        "what the members name",
        "The rules that turn on what is being spoken of: nadī, a river, "
        "and deśa, a settled country — गङ्गाशोणम् (gaṅgāśoṇam), "
        "कुरुकुरुक्षेत्रम् (kurukurukṣetram) at 2.4.7; kratu, a rite laid "
        "down in the Yajurveda — अर्काश्वमेधम् (arkāśvamedham) at 2.4.4. "
        "नदी देश इत्यसमासनिर्देश एवायम् — the first two are separate "
        "conditions and not a pair.",
    ),
    "people": Help(
        "which people the words name",
        "Two rules name groups of people. caraṇa, the followers of a "
        "vedic recension — कठकालापम् (kaṭhakālāpam) at 2.4.3, where the "
        "word names the MEN by way of the branch they recite. śūdra at "
        "2.4.10 — तक्षायस्कारम् (takṣāyaskāram), a carpenter and a "
        "smith.",
    ),
    "group": Help(
        "which of 2.4.12's ten kinds",
        "विभाषा (vibhāṣā) — the ten the sūtra names in its own body: "
        "vṛkṣa, mṛga, tṛṇa, dhānya, vyañjana, paśu, śakuni, aśvavaḍava, "
        "pūrvāpara, adharottara. Either reading stands: प्लक्षन्यग्रोधम् "
        "(plakṣanyagrodham) beside प्लक्षन्यग्रोधाः (plakṣanyagrodhāḥ).",
    ),
    "apatya.kind": Help(
        "which degree of descendant?",
        "अनन्तर (anantara) — the immediate child. गोत्र "
        "(gotra) — 4.1.162's name for a descendant from the "
        "grandson onward. युवन् (yuvan) — 4.1.163's, the one "
        "whose elder is still living. Which affix comes turns "
        "on it: कौञ्जिः (kauñjiḥ) for the child and "
        "कौञ्जायन्यः (kauñjāyanyaḥ) for the line.",
    ),
    "kind": Help(
        "which sort of tatpuruṣa",
        "The vārttika on 2.4.26 keeps 'the gender of the last member' off "
        "five kinds: dvigu — पञ्चकपालः (pañcakapālaḥ); prāpta — "
        "प्राप्तजीविकः (prāptajīvikaḥ); āpanna; alam — अलंजीविकः "
        "(alaṃjīvikaḥ); gati — निष्कौशाम्बिः (niṣkauśāmbiḥ). Each keeps "
        "the gender of what it denotes instead.",
    ),
    "ends_in": Help(
        "what the compound ends in",
        "2.4.20 to 2.4.25 and 2.4.29 turn on the last member: kanthā, "
        "upajñā, upakrama, chāyā, sabhā, senā, surā, śālā, niśā, and the "
        "three of 2.4.29 — rātra, ahna, aha, named with their समासान्त "
        "(samāsānta) already made: द्विरात्रः (dvirātraḥ), पूर्वाह्णः "
        "(pūrvāhṇaḥ).",
    ),
    # --- 2.4.32 to 2.4.57 : one thing standing in for another ----------
    "of": Help(
        "what is being replaced",
        "स्थानिन् (sthānin) — what a substitute stands in for. In "
        "2.4 that is a root or a pronoun: idam and etad, then ad, veñ, "
        "han, iṇ, iṅ, as, brū, cakṣiṅ and aj — give it as the grammar "
        "names it, since इण् (iṇ) and इङ् (iṅ) are two roots and "
        "take different substitutes. From 3.4.80 on it is one of the "
        "eighteen endings, or a single sound within one: the इ (i) of "
        "पचति (pacati), the स् (s) of करवावः (karavāvaḥ).",
    ),
    "before": Help(
        "what follows it",
        "The affix or ending the substitution happens before. लुङ् (luṅ) "
        "the aorist, लिट् (liṭ) the perfect, लिङ् (liṅ) the benedictive, "
        "सन् (san) the desiderative, णि (ṇi) the causative, ल्यप् (lyap), "
        "घञ् (ghañ), अप् (ap), ल्युट् (lyuṭ). 2.4.51 needs a pair — "
        "ṇi-san or ṇi-caṅ — because णि follows the root and सन् follows "
        "णि. 2.4.79 uses the same field for two ENDINGS rather "
        "than affixes, त (ta) and थास् (thās), and means the "
        "middle त — known by the company थास् keeps it in.",
    ),
    "before_vibhakti": Help(
        "which case-ending follows",
        "2.4.32 says तृतीयादौ (tṛtīyādau) — from the THIRD case onward, "
        "so 3 to 7 are reached and the first two are not: those go to "
        "2.4.34 instead. Not a yes-or-no about whether an ending is "
        "there; which one it is.",
    ),
    "atmanepada": Help(
        "is it in the middle voice?",
        "आत्मनेपद (ātmanepada) — the endings used where the fruit of the "
        "act falls to the agent. 2.4.44 alone turns on it: हन् (han) "
        "becomes वध (vadha) optionally there, आवधिष्ट (āvadhiṣṭa) beside "
        "आहत (āhata). Not the पद (pada) of 1.4.14, which means a "
        "finished word.",
    ),
    # --- 2.4.58 to 2.4.71 : affixes added and then taken away ----------
    "descendant": Help(
        "which kind of descendant?",
        "Not what a word means — which KINSHIP the affix names. गोत्र "
        "(gotra) is a remote descendant, a grandson onward; युवन् (yuvan) "
        "is a young one named while the elder is still living. The first "
        "four rules drop the yuvan affix so father and son are called "
        "alike — कौरव्यः पिता, कौरव्यः पुत्रः (kauravyaḥ pitā, kauravyaḥ "
        "putraḥ); the rest drop the gotra affix in the plural.",
    ),
    "stem_kind": Help(
        "what sort of stem is it?",
        "2.4.58's four: ṇya — a stem taking ण्य (ṇya) by 4.1.151; "
        "kṣatriya-gotra; ārṣa — descended from a ṛṣi; and ñit — a stem "
        "whose affix is marked with ञ् (ñ). Each of the four loses its "
        "yuvan अण् (aṇ) or इञ् (iñ).",
    ),
    "plural": Help(
        "is it plural?",
        "बहुषु (bahuṣu) — everything from 2.4.62 to 2.4.70 holds in the "
        "plural ONLY. अङ्गाः (aṅgāḥ) loses its affix; आङ्गः (āṅgaḥ), the "
        "singular, keeps it.",
    ),
    "feminine": Help(
        "is it feminine?",
        "अस्त्रियाम् (astriyām) — 2.4.62 to 2.4.70 hold for what is NOT "
        "feminine. आङ्ग्यः स्त्रियः (āṅgyaḥ striyaḥ) and यास्क्यः स्त्रियः "
        "(yāskyaḥ striyaḥ) keep their affixes.",
    ),
    "by_that_affix": Help(
        "did that affix make it plural?",
        "तेनैव (tenaiva) — the plurality must be made by the "
        "descendant-affix itself. In प्रियवाङ्गाः (priyavāṅgāḥ) and "
        "प्रिययास्काः (priyayāskāḥ) the plural comes from the बहुव्रीहि "
        "(bahuvrīhi) instead, so no elision. Say no where the many are "
        "made some other way.",
    ),
    "region": Help(
        "of which region?",
        "prāc — the easterners, for 2.4.60; prācya and bharata, for "
        "2.4.66. The two are worth keeping apart: 2.4.66 names भरत "
        "(bharata) where it did not have to, and the commentary reads "
        "that as teaching that प्राच् (prāc) said ANYWHERE ELSE leaves "
        "the Bharatas out — so 2.4.60 does not reach them, and आर्जुनिः "
        "पिता, आर्जुनायनः पुत्रः (ārjuniḥ pitā, ārjunāyanaḥ putraḥ) stay "
        "different.",
    ),
    "dvandva": Help(
        "is it a dvandva compound?",
        "द्वन्द्व (dvandva) — two or more things joined as equals. 2.4.68 "
        "holds in one and 2.4.69 outside one, and the word अद्वन्द्वे "
        "(advandve) is there to cancel the heading 2.4.68 set up. Three "
        "words are in both lists, and for those the elision is "
        "obligatory in a dvandva and a choice outside it.",
    ),
    "bahvac": Help(
        "does the stem have many syllables?",
        "बह्वच् (bahvac) — more than two vowels. 2.4.66 needs it: "
        "पन्नागाराः (pannāgārāḥ) qualifies, बैकयः (baikayaḥ) and पौष्पयः "
        "(pauṣpayaḥ) do not and keep their affix.",
    ),
    "becomes": Help(
        "what has the word become?",
        "2.4.71 only. The सुप् (sup) ending is dropped where what carries "
        "it has itself been named a धातु (dhātu, a verbal root) or a "
        "प्रातिपदिक (prātipadika, a nominal stem): पुत्रीयति (putrīyati) "
        "for the first, राजपुरुषः (rājapuruṣaḥ) for the second. An "
        "ordinary inflected word keeps its ending — वृक्षः (vṛkṣaḥ).",
    ),
    # --- 2.4.73 and 2.4.75 to 2.4.85 : the pāda's closing rules --------
    "gana": Help(
        "which class of roots?",
        "गण (gaṇa) — the dhātupāṭha sorts roots into ten classes, and "
        "nine of them decide which class-marker a root takes. Give it "
        "as the two-digit code the corpus uses — 04 for दिवादि "
        "(divādi), 07 for रुधादि (rudhādi) — and give it wherever a "
        "root is read in more than one class, as रुध् (rudh) is in "
        "both 04 and 07 and takes a different marker in each. Two "
        "classes are also named by name: juhotyādi, the third, "
        "replaces its शप् "
        "(śap) with श्लु (ślu) by 2.4.75 and reduplicates: जुहोति "
        "(juhoti), बिभर्ति (bibharti). tanādi, the eighth, drops its सिच् "
        "(sic) optionally by 2.4.79: अतत (atata) beside अतनिष्ट "
        "(ataniṣṭa).",
    ),
    "parasmaipada": Help(
        "is it in the active voice?",
        "परस्मैपद (parasmaipada) — the endings used where the fruit of the "
        "act does not fall to the agent. 2.4.77 and 2.4.78 hold in the "
        "active ONLY: अगात् (agāt) loses its सिच्, but अगासाताम् "
        "(agāsātām) keeps it. The opposite of आत्मनेपद (ātmanepada).",
    ),
    "mantra": Help(
        "is it in a mantra?",
        "मन्त्रे (mantre) — 2.4.80 holds in mantra language only, and the "
        "condition stops there: 2.4.81 आमः (āmaḥ) does not carry it, so "
        "ईहांचक्रे (īhāṃcakre) works anywhere. Narrower than छन्दसि "
        "(chandasi), which is Vedic usage at large.",
    ),
    "ends_in_a": Help(
        "does the compound end in short a?",
        "अतः (ataḥ) — 2.4.83 divides the अव्ययीभाव (avyayībhāva) "
        "compounds by their last sound. One ending in अ takes अम् (am): "
        "उपकुम्भं तिष्ठति (upakumbhaṃ tiṣṭhati). One that does not falls "
        "back to 2.4.82 and loses its ending outright: अधिस्त्रि "
        "(adhistri), अधिकुमारि (adhikumāri).",
    ),
    # --- 3.1.1 to 3.1.31 : affixes, and the ones that make a root ------
    "prescribes": Help(
        "which of the six is it?",
        "3.1.1 names everything from 3.1.5 to the end of adhyāya 5 a "
        "प्रत्यय (pratyaya) — but not everything a rule mentions. The "
        "commentary excludes five by name: prakṛti, the base it is added "
        "to; upapada, a word that must stand beside it; upādhi, a "
        "condition; vikāra, a change; āgama, an inserted augment. Only "
        "'pratyaya' is the affix itself.",
    ),
    "sup": Help(
        "is it a सुप् ending?",
        "सुप् (sup) — the twenty-one nominal case endings, named at "
        "4.1.2. 3.1.4 makes them unaccented against 3.1.3's general "
        "rule: दृषदौ (dṛṣadau), दृषदः (dṛṣadaḥ).",
    ),
    "pit": Help(
        "is it marked with प्?",
        "पित् (pit) — an affix carrying प् as a silent mark. 3.1.4 leaves "
        "these unaccented too: पचति (pacati), पठति (paṭhati). The mark "
        "does nothing but this and a few other rules; it is written to "
        "be referred to.",
    ),
    "is_root": Help(
        "is the base a verbal root?",
        "This run adds affixes to two different things. 3.1.5 to 3.1.7 "
        "take a धातु (dhātu, a root) — चिकीर्षति (cikīrṣati) from कृ; "
        "3.1.8 to 3.1.21 take a finished word, a सुबन्त (subanta) — "
        "पुत्रीयति (putrīyati) from पुत्र. Say no for a word, yes for a "
        "root.",
    ),
    "upamana": Help(
        "what role does the thing compared play?",
        "उपमान (upamāna) — the thing likened to. 3.1.10 and 3.1.11 both "
        "mean behaving LIKE something, and divide by which role it "
        "plays. Say karman at 3.1.10, where it is the object — "
        "छात्रम् (putrīyati chātram), treating a pupil like a son; at "
        "3.1.11 the agent — श्येन इवाचरति काकः, श्येनायते (śyenāyate), "
        "a crow acting like a hawk. 3.2.79 asks the same question "
        "and wants the agent: उष्ट्र इव क्रोशति उष्ट्रक्रोशी "
        "(uṣṭra iva krośati uṣṭrakrośī), one who cries like a "
        "camel.",
    ),
    # --- 3.1.33 to 3.1.67 : the affix a lakāra brings with it ----------
    "voice": Help(
        "whose action is the form about?",
        "kartari — the agent's, अकार्षीत् (akārṣīt). bhāvakarmaṇoḥ — the "
        "act's or the object's, अकारि कटः (akāri kaṭaḥ). karmakartari — "
        "where the OBJECT is spoken of as acting on itself, अकारि कटः "
        "स्वयमेव (akāri kaṭaḥ svayameva), the mat as good as making "
        "itself. 3.1.62 to 3.1.66 divide on exactly this.",
    ),
    "affix_final": Help(
        "does the stem end in an affix?",
        "प्रत्ययात् (pratyayāt) — 3.1.35 gives आम् (ām) in the perfect "
        "after any stem built with an affix, which is what carries the "
        "whole सनादि run of 3.1.5–31 into the perfect: लोलूयाञ्चके "
        "(lolūyāñcake) from the very stem 3.1.22 and 3.1.32 built.",
    ),
    "ijadi_guru": Help(
        "does it start with इच् and have a heavy vowel?",
        "इजादि गुरुमत् (ijādi gurumat) — 3.1.36's two conditions "
        "together: beginning with a vowel other than अ, and carrying a "
        "heavy syllable. ईहाञ्चक्रे (īhāñcakre), ऊहाञ्चक्रे. Fails "
        "either and the perfect is plain — ततक्ष (tatakṣa) is not "
        "vowel-initial, इयज (iyaja) is not heavy.",
    ),
    "after_am": Help(
        "is there an आम् for it to follow?",
        "3.1.40 puts a second verb after the आम् (ām) of 3.1.35–39 — "
        "कृ, भू or अस्, all three: पाचयाञ्चकार (pācayāñcakāra), "
        "पाचयाम्बभूव, पाचयामास. Without an आम् there is nothing for it "
        "to follow.",
    ),
    "shal_igupadha_anit": Help(
        "all three of 3.1.45's conditions?",
        "शल् इगुपध अनिट् (śal igupadha aniṭ) — ending in a शल् sound, "
        "with an इक् vowel before that, and taking no इट्. All three "
        "together give क्स (ksa): अधुक्षत् (adhukṣat), अलिक्षत्. Miss "
        "any one and the aorist is सिच् instead — अभैत्सीत्, अधाक्षीत्, "
        "अकोषीत् fail one apiece.",
    ),
    "ac_final": Help(
        "does the root end in a vowel?",
        "अचः (acaḥ) — 3.1.62 gives चिण् (ciṇ) only to a vowel-final root "
        "where the object is spoken of as acting: अकारि कटः स्वयमेव "
        "(akāri kaṭaḥ svayameva). अभेदि काष्ठं स्वयमेव is the counter — "
        "भिद् (bhid) ends in a consonant, so 3.1.63 has to name दुह् "
        "(duh) separately.",
    ),
    "nyanta": Help(
        "is it a causative stem?",
        "ण्यन्त (ṇyanta) — a stem ending in णि (ṇi), which 3.1.26 "
        "हेतुमति च gives for causing. 3.1.48 gives any such stem चङ् "
        "(caṅ) in the aorist: अचीकरत् (acīkarat). The three roots that "
        "rule also names — श्रि, द्रु, स्रु — take it without being "
        "causatives.",
    ),
    # --- 3.1.69 to 3.1.95 : the class-marker, and three headings -------
    "before_hi": Help(
        "is the ending हि?",
        "3.1.83 turns श्ना (śnā) into शानच् (śānac) before हि (hi), the "
        "second-person singular imperative — and only after a consonant. "
        "मुषाण (muṣāṇa) has both conditions; क्रीणीहि (krīṇīhi) fails the "
        "first and मुष्णाति (muṣṇāti) the second.",
    ),
    "tulyakriya": Help(
        "is the agent acting as the object would?",
        "कर्मणा तुल्यक्रियः (karmaṇā tulyakriyaḥ) — the wood as good as "
        "splitting itself, भिद्यते काष्ठं स्वयमेव (bhidyate kāṣṭhaṃ "
        "svayameva). Where that holds, the agent takes four things that "
        "belong to an object: यक्, the middle endings, चिण्, and "
        "चिण्वद्भाव. Where it does not, nothing is transferred.",
    ),
    "object_of_tap": Help(
        "is तपस् the object?",
        "3.1.88 reaches तप् (tap) only where तपस् is what it governs: "
        "तप्यते तपस्तापसः (tapyate tapastāpasaḥ), the ascetic performing "
        "austerities. उत्तपति सुवर्णं सुवर्णकारः — a goldsmith heating "
        "gold is the same root with another object, and the rule does "
        "not reach it.",
    ),
    "pracam": Help(
        "on the eastern teachers' view?",
        "प्राचाम् (prācām) — naming earlier teachers is how 3.1.90 "
        "expresses an option, प्राचांग्रहणं विकल्पार्थम्. And it is a "
        "व्यवस्थितविभाषा (vyavasthitavibhāṣā), settled by where one is "
        "rather than chosen: not in the perfect, the benedictive, or the "
        "स्य futures, where चुकुषे (cukuṣe) keeps the middle.",
    ),
    "in_locative": Help(
        "does the rule state it in the locative?",
        "सप्तमीस्थम् (saptamīstham) — 3.1.92 names a word an उपपद "
        "(upapada), one that must stand beside, only where a rule of the "
        "धातोः section puts it in the LOCATIVE. 3.2.1 कर्मण्यण् does, so "
        "the object is one and कुम्भकारः (kumbhakāraḥ) is formed.",
    ),
    "is_tin": Help(
        "is it a finite verb ending?",
        "तिङ् (tiṅ) — the eighteen personal endings named at 1.4.104. "
        "3.1.93 calls every affix of this section कृत् (kṛt) EXCEPT "
        "those: कर्तव्यम् (kartavyam) is a कृत्, चीयात् (cīyāt) is a "
        "तिङ् form and keeps its own name.",
    ),
    # --- 3.1.96 to 3.1.132 : the kṛtya affixes -------------------------
    "root_ends_in": Help(
        "what sound does the ROOT end in?",
        "Not the last member of a compound — that is `ends_in`, which "
        "2.4.20 to 2.4.29 use. Here it is the root's own final, and four "
        "rules divide on it: ac, any vowel, for यत् (yat) — गेयम् "
        "(geyam); pu, a labial with a short अ before it, also यत् — "
        "शप्यम् (śapyam); u for ण्यत् (ṇyat) — लाव्यम् (lāvyam); and "
        "ṛ-or-hal, ऋ or a consonant, also ण्यत् — कार्यम् (kāryam), "
        "वाक्यम् (vākyam).",
    ),
    "penult": Help(
        "what is the second-to-last sound?",
        "उपधा (upadhā) — the sound before the last. 3.1.98 wants a short "
        "अ there, 3.1.110 an ऋ: वृत्यम् (vṛtyam), वृध्यम् (vṛdhyam). "
        "3.1.110 excepts two roots that have it anyway — कॢप् and चृत् "
        "give कल्प्यम् and चर्त्यम् instead.",
    ),
    # --- 3.1.133 to 3.1.150 : the agent affixes ------------------------
    "craftsman": Help(
        "is a craftsman meant?",
        "शिल्पिन् (śilpin) — someone who does a thing as their trade, "
        "not merely on one occasion. 3.1.145 gives such an agent ष्वुन् "
        "(ṣvun) — नर्तकः (nartakaḥ) a dancer, खनकः (khanakaḥ) a digger, "
        "रजकः (rajakaḥ) a washerman — and 3.1.146 gives one who sings a "
        "different affix again, गाथकः (gāthakaḥ).",
    ),
    # --- 3.2.1 to 3.2.20 : a word standing beside the root ---------------
    "beside": Help(
        "which word stands beside the root?",
        "उपपद (upapada) — the word a rule names as standing next to the "
        "root. From 3.2.1 onward the affix depends on it: कुम्भ "
        "(kumbha) a pot beside कृ (kṛ) to make gives कुम्भकारः "
        "(kumbhakāraḥ) a potter. Some rules take any word at all and "
        "ask only what its role is; others name the word itself — चर् "
        "(car) to move takes one affix after भिक्षा (bhikṣā) alms and "
        "another after a place.",
    ),
    "role": Help(
        "what part does that word play?",
        "कारक (kāraka) — how the word beside the root takes part in the "
        "act. कर्मन् (karman) is what the act is done TO, अधिकरण "
        "(adhikaraṇa) where it is done, कर्तृ (kartṛ) who does it, and "
        "सुप् (sup) means the rule takes any finished word whatever and "
        "does not care. It has to be told rather than worked out: "
        "पूर्व (pūrva) beside सृ (sṛ) to go gives पूर्वसरः (pūrvasaraḥ) "
        "as the doer but पूर्वसारः (pūrvasāraḥ) as the thing gone to — "
        "same two words, two different words made of them.",
    ),
    "names_a": Help(
        "what does the finished word name?",
        "Some rules turn not on the sense of the ACT but on what the "
        "word made from it ends up naming. 3.2.25 gives दृतिहरिः "
        "(dṛtihariḥ) only of a पशु (paśu), an animal — of anything "
        "else it is दृतिहारः (dṛtihāraḥ). 3.2.24 likewise wants a "
        "व्रीहि (vrīhi), a rice-plant, or a वत्स (vatsa), a calf. This "
        "is a separate question from the sense, and both can be needed "
        "at once.",
    ),
    "chandasi": Help(
        "is this in the Veda?",
        "छन्दस् (chandas) — Vedic usage, as against the ordinary "
        "language the grammar otherwise describes. A handful of rules "
        "hold there only: 3.2.27 gives चतुर् (catur) roots इन् (in) in "
        "the Veda and nowhere else, ब्रह्मवनिम् (brahmavanim). The "
        "Veda has the ordinary grammar too, so a rule that says "
        "nothing about it still applies there.",
    ),
    "causative": Help(
        "is the root in its causative form?",
        "ण्यन्त (ṇyanta) — a root with the causative affix णिच् (ṇic) "
        "already added, so that it means 'cause to —'. 3.2.28 gives "
        "खश् (khaś) after एज् (ej) TO SHAKE only in that form: "
        "अङ्गमेजयः (aṅgamejayaḥ), one who makes his limbs shake.",
    ),
    "agent": Help(
        "is the doer a human being?",
        "कर्तृ (kartṛ) — who or what performs the act. 3.2.53 gives its "
        "affix only where the doer is NOT a person: श्लेष्मघ्नं मधु "
        "(śleṣmaghnaṃ madhu), honey that kills phlegm; पतिघ्नी "
        "पाणिरेखा (patighnī pāṇirekhā), a line on the palm that kills "
        "a husband. Of a person the ordinary affix comes instead — "
        "आखुघातः शूद्रः (ākhughātaḥ śūdraḥ), a mouse-killer.",
    ),
    "cvi_sense": Help(
        "does the word mean BECOMING what it was not?",
        "च्व्यर्थ (cvyartha) — the sense of turning into something. "
        "3.2.56 and 3.2.57 want it: अनाढ्यम् आढ्यं करोति (anāḍhyam "
        "āḍhyaṃ karoti), making rich what was not rich. Merely "
        "applying something is not this — आढ्यं तैलेन कुर्वन्ति "
        "(āḍhyaṃ tailena kurvanti) is only anointing, and the rules "
        "do not reach it.",
    ),
    "cvi_ending": Help(
        "does the word actually carry the च्वि affix?",
        "च्वि (cvi) is the affix that itself expresses that becoming. "
        "The two rules want the MEANING without it — अच्वौ (acvau), "
        "'not ending in च्वि' — so आढ्यंकरणम् (āḍhyaṃkaraṇam) is "
        "reached but आढ्यीकुर्वन्ति (āḍhyīkurvanti), where the च्वि is "
        "present, is not. Two separate questions, and the commentary "
        "asks after each in turn.",
    ),
    "mantra": Help(
        "is this a मन्त्र (mantra) passage?",
        "मन्त्र (mantra) — the verse portion of the Veda, as against "
        "the ब्राह्मण (brāhmaṇa) prose. Narrower than छन्दस् (chandas), "
        "which covers Vedic language generally, and the commentary "
        "keeps the two apart. 3.2.71 and 3.2.72 hold in a mantra only: "
        "श्वेतवा इन्द्रः (śvetavā indraḥ), Indra whom white horses draw.",
    ),
    "pada_final": Help(
        "does the root stand at the end of a metrical quarter?",
        "पाद (pāda) — a quarter of a verse. 3.2.66 is the one rule in "
        "this chapter whose condition is about VERSE and not grammar: "
        "अनन्तः पादम् (anantaḥ pādam), the root must not stand at the "
        "quarter's end. So हव्यवाहनः (havyavāhanaḥ) is formed within "
        "the line, but हव्यवाट् (havyavāṭ) where the line ends.",
    ),
    "attested": Help(
        "is this form actually found in use?",
        "3.2.75 says these affixes दृश्यन्ते (dṛśyante), 'are seen' — "
        "and the commentary is explicit that the word is chosen for "
        "that reason: दृशिग्रहणं प्रयोगानुसरणार्थम् (dṛśigrahaṇaṃ "
        "prayogānusaraṇārtham), so that one FOLLOWS USAGE. Read as an "
        "ordinary rule it would give four affixes to every root there "
        "is; read as the commentary reads it, it licenses what is "
        "attested. So say yes only for a form actually met with.",
    ),
    "past": Help(
        "is the act a PAST one?",
        "भूत (bhūta) — past time. From 3.2.84 onward this is a "
        "heading over every rule as far as 3.2.122, and none of those "
        "rules says so itself: अग्निष्टोमयाजी (agniṣṭomayājī) is one "
        "who HAS sacrificed with the Agniṣṭoma. Of one sacrificing "
        "now — अग्निष्टोमेन यजते (agniṣṭomena yajate) — no affix comes.",
    ),
    "wants": Help(
        "which affix are you asking about?",
        "Optional, and needed only where two rules reach the same root "
        "and give different affixes: 3.2.75 and 3.2.76 are both open "
        "and both reach स्रंस् (sraṃs), one giving four affixes and "
        "the other giving क्विप् (kvip). Name the affix and the rule "
        "that supplies it answers. Left blank, the most specific rule "
        "answers as usual.",
    ),
    "anadyatana": Help(
        "did it happen before today?",
        "अनद्यतन (anadyatana) — past, but not today. The commentary "
        "reads the word as a बहुव्रीहि (bahuvrīhi), 'having no today "
        "in it', and says the form is chosen so that a MIXED case is "
        "left out: अद्य ह्यो वा अभुक्ष्महि (adya hyo vā abhukṣmahi), "
        "'we ate today or yesterday', is reached by no rule here.",
    ),
    "paroksa": Help(
        "was it out of the speaker's sight?",
        "परोक्ष (parokṣa) — beyond the eye. The commentary asks "
        "whether every act is not out of sight, since one sees things "
        "and never actions, and answers that people do take themselves "
        "to see an act in the people and objects doing it — परोक्ष is "
        "where they do not. It can hold even of oneself: सुप्तोऽहं "
        "किल विललाप (supto'haṃ kila vilalāpa), 'asleep, I am told, I "
        "wailed'.",
    ),
    "question": Help(
        "is this a question?",
        "प्रश्न (praśna) — something asked rather than told. 3.2.117 "
        "gives two endings in a question about lately: अगच्छद् "
        "देवदत्तः (agacchad devadattaḥ), 'did Devadatta go?' Told "
        "rather than asked, and only the one ending comes.",
    ),
    "recent": Help(
        "is the question about something lately?",
        "आसन्नकाल (āsannakāla) — near in time. 3.2.117 wants the "
        "question to be about the recent past. Ask about the far past "
        "— जघान कंसं किल वासुदेवः (jaghāna kaṃsaṃ kila vāsudevaḥ), "
        "'did Vāsudeva kill Kaṃsa?' — and the rule does not reach it.",
    ),
    "answer": Help(
        "is this an answer to something asked?",
        "पृष्टप्रतिवचन (pṛṣṭaprativacana) — a reply to a question. "
        "3.2.120 and 3.2.121 want one: अकार्षीः कटं देवदत्त? ननु "
        "करोमि भोः (akārṣīḥ kaṭaṃ devadatta? nanu karomi bhoḥ), "
        "'did you make the mat?' — 'why, I am making it'. Said "
        "unprompted and the rule does not apply.",
    ),
    "sakanksa": Help(
        "does the speaker expect more to follow?",
        "साकाङ्क्ष (sākāṅkṣa) — expectant. The commentary defines it "
        "by the relation between two clauses: one MARKS the time and "
        "the other is placed by it — वासो लक्षणम्, भोजनं तु लक्ष्यम् "
        "(vāso lakṣaṇam, bhojanaṃ tu lakṣyam), the dwelling marks and "
        "the eating is marked. So a clause is expectant only because "
        "another follows it, and the condition is about the sentence "
        "rather than any word in it.",
    ),
    "with_yad": Help(
        "does the word यद् stand with it?",
        "यद् (yad) — the relative 'that'. 3.2.113 refuses the future "
        "ending where it stands: अभिजानासि देवदत्त यत् "
        "कश्मीरेष्ववसाम (abhijānāsi devadatta yat kaśmīreṣvavasāma), "
        "'do you recall that we lived in Kashmir?' But 3.2.114 lets "
        "the option back in either way, so यद् bars it only where "
        "nothing further is expected.",
    ),
    "time": Help(
        "which time is meant?",
        "The headings of this chapter divide by time. भूत (bhūta), "
        "the past, runs from 3.2.84 to 3.2.122; वर्तमान (vartamāna), "
        "the present, begins at 3.2.123 — and the commentary defines "
        "that one by the act's own course rather than by the moment "
        "of speaking: प्रारब्धोऽपरिसमाप्तश्च (prārabdho'parisamāptaśca), "
        "begun and not finished.",
    ),
    "aprathama": Help(
        "does it agree with a word NOT in the first case?",
        "अप्रथमासमानाधिकरण (aprathamā-samānādhikaraṇa). 3.2.124 wants "
        "the participle to agree with a word in some case other than "
        "the nominative: पचन्तं देवदत्तं पश्य (pacantaṃ devadattaṃ "
        "paśya), 'see Devadatta cooking'. Agreeing with a nominative "
        "— देवदत्तः पचति (devadattaḥ pacati) — and the ordinary "
        "present verb stands instead.",
    ),
    "lakshana_hetu": Help(
        "is it a MARK of something, or its CAUSE?",
        "लक्षण (lakṣaṇa) is what something is recognised by — "
        "लक्ष्यते चिह्न्यते येन — and हेतु (hetu) is what brings it "
        "about, जनको हेतुः. शयाना भुञ्जते यवनाः (śayānā bhuñjate "
        "yavanāḥ), 'the Greeks eat lying down'; अर्जयन् वसति "
        "(arjayan vasati), 'he lives by earning'. The mark must be an "
        "ACT and not a thing or a quality.",
    ),
    "akrcchri": Help(
        "does the act come EASILY to the doer?",
        "अकृच्छ्री (akṛcchrī) — one for whom the act is no trouble: "
        "अकृच्छ्रः सुखसाध्यो यस्य कर्तुर्धात्वर्थः. 3.2.130 gives its "
        "affix only then — अधीयन् पारायणम् (adhīyan pārāyaṇam), "
        "reciting the whole text with ease. Of one who labours at it, "
        "कृच्छ्रेणाधीते (kṛcchreṇādhīte), no participle comes.",
    ),
    "amitra": Help(
        "is the one hated an ENEMY?",
        "अमित्र (amitra) — a foe, अमित्रः शत्रुः. 3.2.131 gives its "
        "affix only of hating an enemy: द्विषन् (dviṣan). Of a wife "
        "hating a husband — द्वेष्टि भार्या पतिम् (dveṣṭi bhāryā "
        "patim) — the rule does not reach, the hatred not being an "
        "enemy's.",
    ),
    "yajna": Help(
        "is the pressing part of a SACRIFICE?",
        "यज्ञसंयोग (yajñasaṃyoga) — joined to a sacrifice. And the "
        "commentary says the word संयोग is chosen so the PRINCIPAL "
        "doer is meant, the sacrificer and not the officiating "
        "priests: सर्वे सुन्वन्तः (sarve sunvantaḥ). Pressing liquor "
        "instead — सुनोति सुराम् (sunoti surām) — and the rule does "
        "not apply.",
    ),
    "akarmaka": Help(
        "does the root take no object?",
        "अकर्मक (akarmaka) — intransitive. 3.2.148 and 3.2.149 want "
        "one: चलनः (calanaḥ), moving, is formed, but पठिता विद्याम् "
        "(paṭhitā vidyām), reciting a subject, is not — an object "
        "being present there.",
    ),
    "anudattet": Help(
        "is the root marked with a low-toned vowel?",
        "अनुदात्तेत् (anudāttet) — a root whose उपदेश (upadeśa) form "
        "carries an अनुदात्त marker. That mark decides several things "
        "elsewhere in the grammar; here 3.2.149 wants it. भू (bhū) is "
        "not one of them, so भविता (bhavitā) stands rather than the "
        "participle.",
    ),
    "hal_adi": Help(
        "does the root BEGIN with a consonant?",
        "हलादि (halādi) — starting with a हल् (hal), a consonant. "
        "3.2.149 wants it, so एधिता (edhitā) is left out. And the "
        "commentary notes the word आदि is chosen so the question is "
        "about the ROOT: जुगुप्सनः (jugupsanaḥ) counts even though a "
        "reduplication stands in front.",
    ),
    "y_final": Help(
        "does the root END in य?",
        "यकारान्त (yakārānta). 3.2.152 refuses its affix to such a "
        "root: क्नूयिता (knūyitā), क्ष्मायिता (kṣmāyitā) take the "
        "ordinary agent affix instead of the participle the rule "
        "before would have given.",
    ),
    "yan_anta": Help(
        "is the stem an intensive one?",
        "यङन्त (yaṅanta) — a stem built with यङ् (yaṅ), which makes a "
        "root mean doing the thing over and over or intensely. 3.2.166 "
        "and 3.2.176 want one: यायजूकः (yāyajūkaḥ), constantly "
        "sacrificing, and यायावरः (yāyāvaraḥ), a wanderer. The affix "
        "attaches to that stem and not to the bare root, so the stem "
        "has to exist before the rule can reach it.",
    ),
    "san_anta": Help(
        "is the stem a desiderative one?",
        "सन्नन्त (sannanta) — a stem built with सन् (san), which makes "
        "a root mean WISHING to do the thing. 3.2.168 gives such a "
        "stem its affix: चिकीर्षुः (cikīrṣuḥ), one who wants to act. "
        "The commentary is careful that the rule names the AFFIX सन् "
        "and not the similarly written root.",
    ),
    "kya_anta": Help(
        "is the stem built with one of the क्य affixes?",
        "क्य (kya) here stands for three affixes at once — क्यच् "
        "(kyac), क्यङ् (kyaṅ) and क्यष् (kyaṣ) — which turn a noun "
        "into a verb: wanting a thing, behaving like it, becoming it. "
        "3.2.170 gives such a stem its affix in the Veda: मित्रयुः "
        "(mitrayuḥ), seeking a friend.",
    ),
    "a_final": Help(
        "does the root end in आ?",
        "आकारान्त (ākārānta). 3.2.171 reaches roots by their SHAPE as "
        "well as by name, and this is one of the two shapes it takes: "
        "पपिः (papiḥ), one who drinks; ददिः (dadiḥ), one who gives. "
        "In the Veda only.",
    ),
    "r_final": Help(
        "does the root end in ऋ or ॠ?",
        "ऋवर्णान्त (ṛvarṇānta) — ending in either of the ṛ vowels. "
        "The other shape 3.2.171 reaches: ततुरिः (taturiḥ), one who "
        "crosses over; जगुरिः (jaguriḥ), one who goes. Also in the "
        "Veda only.",
    ),
    "samjna": Help(
        "is the finished word being used as a NAME?",
        "संज्ञा (saṃjñā) — a proper name, as against a word used for "
        "what it means. Two rules divide one word by this: विभुः "
        "(vibhuḥ) is the all-pervading, विभूः (vibhūḥ) is somebody so "
        "called. 3.2.185 wants a name too, and there the name is "
        "carried by the whole word together — दर्भः पवित्रम् (darbhaḥ "
        "pavitram), the sacred grass.",
    ),
    "karaka": Help(
        "what part does the thing named play in the act?",
        "कारक (kāraka). Several rules at the close of this chapter "
        "divide by it: 3.2.181 names what the act is done TO — धात्री "
        "(dhātrī), a wet-nurse; 3.2.182 and after name the MEANS — "
        "नेत्रम् (netram) an eye, अरित्रम् (aritram) an oar. Say "
        "karman or karaṇa.",
    ),
    "part_of": Help(
        "what is the instrument a part OF?",
        "3.2.183 is the only rule here whose condition is neither what "
        "a thing does nor what it is called, but what it BELONGS to: "
        "the word पोत्रम् (potram) names a ploughshare and a boar's "
        "snout, and nothing else. Say hala for the plough or sūkara "
        "for the boar.",
    ),
    "rsi_devata": Help(
        "is a seer or a deity being spoken of?",
        "ऋषि (ṛṣi) or देवता (devatā). 3.2.186 pairs these crosswise "
        "with two roles: of a SEER the word names the means of "
        "purifying — पवित्रोऽयम् ऋषिः (pavitro'yam ṛṣiḥ); of a DEITY "
        "it names the one who purifies — अग्निः पवित्रम् (agniḥ "
        "pavitram). One form read two ways by what it is said of.",
    ),
    "nit": Help(
        "is the root marked with ञि?",
        "ञीत् (ñīt) — a root carrying ञि in its उपदेश (upadeśa) form. "
        "3.2.187 gives such a root क्त (kta) in the PRESENT: धृष्टः "
        "(dhṛṣṭaḥ), bold; मिन्नः (minnaḥ), moist. That excepts an "
        "earlier rule of the same chapter, which had given the affix "
        "for the past.",
    ),
    "kriya": Help(
        "does an ACT stand beside the root?",
        "क्रिया (kriyā) — an action, as against a thing. 3.3.10 wants "
        "one standing beside: भोक्तुं व्रजति (bhoktuṃ vrajati), he "
        "goes in order to eat, where the EATING is the companion. "
        "क्रियायामिति किम्? भिक्षिष्य इत्यस्य जटाः — where what "
        "stands beside is not an act at all, the rule does not "
        "reach.",
    ),
    "kriyartha": Help(
        "is the root's act done FOR that other act?",
        "क्रियार्था क्रिया (kriyārthā kriyā) — the companion act is "
        "the PURPOSE of the root's. Both this and `kriya` must hold, "
        "and the commentary gives a separate counter-example for "
        "each: धावतस्ते पतिष्यति दण्डः (dhāvatas te patiṣyati "
        "daṇḍaḥ), the stick falls as he runs — an act stands beside, "
        "but the running is not done so that the stick may fall.",
    ),
    "karman": Help(
        "does an OBJECT stand beside as well?",
        "कर्मन् (karman) — what the act is done to. 3.3.12 adds it to "
        "the two conditions already running, and the affix that comes "
        "then is 3.2.1's own अण् (aṇ), said over again: काण्डलावो "
        "व्रजति (kāṇḍalāvo vrajati), he goes to cut reeds.",
    ),
    "bhava": Help(
        "is the affix one that names the ACT itself?",
        "भाववचन (bhāvavacana) — an affix naming the action rather "
        "than a doer or a thing done. 3.3.11 lets those come here "
        "too: पाकाय व्रजति (pākāya vrajati), he goes for the cooking. "
        "Which affixes those are is settled from 3.3.18 onward.",
    ),
    "nipata": Help(
        "is the companion a PARTICLE, not a case-form?",
        "निपात (nipāta) — an indeclinable particle. 3.3.4 wants "
        "यावत् (yāvat) and पुरा (purā) as particles: यावद् भुङ्क्ते "
        "(yāvad bhuṅkte). Said as case-forms the same two syllables "
        "fall outside it — यावद् दास्यति तावद् भोक्ष्यते (yāvad "
        "dāsyati tāvad bhokṣyate) — and what stands there instead is "
        "3.3.13's लृट् (lṛṭ). A condition about what PART OF SPEECH "
        "a word is.",
    ),
    "kimvrtta": Help(
        "does a form of किम् stand beside?",
        "किंवृत्त (kiṃvṛtta) — a word 'turned from' किम् (kim), "
        "which. Its extent is fixed by a remembered list and not by "
        "the word itself: the case-inflected forms of किम्, and "
        "डतर (ḍatara) and डतम (ḍatama) besides — कतरो भिक्षां "
        "दास्यति (kataro bhikṣāṃ dāsyati), which of the two will "
        "give alms?",
    ),
    "lipsa": Help(
        "does the speaker WANT to get something by asking?",
        "लिप्सा (lipsā) — लब्धुमिच्छा, the wish to obtain. 3.3.6 "
        "needs it: कं भवन्तो भोजयन्ति (kaṃ bhavanto bhojayanti), "
        "whom are you feeding — asked by someone hoping to be fed. "
        "Without it the rule does not reach: कः पाटलिपुत्रं "
        "गमिष्यति (kaḥ pāṭaliputraṃ gamiṣyati), who will go to "
        "Pāṭaliputra, is merely a question.",
    ),
    "lipsyamana_siddhi": Help(
        "will what is wanted actually COME of it?",
        "लिप्स्यमानसिद्धि (lipsyamānasiddhi) — that the thing hoped "
        "for follows from the act. 3.3.7 exists for the case 3.3.6 "
        "could not reach, where no form of किम् stands: यो भक्तं "
        "ददाति, स स्वर्गं गच्छति (yo bhaktaṃ dadāti, sa svargaṃ "
        "gacchati) — one urges a giver on by telling him what his "
        "gift will get him.",
    ),
    "lodartha": Help(
        "does the act MARK OUT a command?",
        "लोडर्थलक्षण (loḍarthalakṣaṇa) — the act by which an order "
        "or the like is signalled. It is the sign, not the thing "
        "ordered: उपाध्यायश्चेदागच्छति, अथ त्वं छन्दोऽधीष्व "
        "(upādhyāyaś ced āgacchati, atha tvaṃ chando'dhīṣva) — if "
        "the teacher comes, then study; the coming is the sign of "
        "the order.",
    ),
    "urdhvamauhurtika": Help(
        "is it later than the present hour?",
        "ऊर्ध्वमौहूर्तिक (ūrdhvamauhūrtika) — ऊर्ध्वं मुहूर्तात्, "
        "beyond this hour. 3.3.9 gives लिङ् (liṅ) there, and by its "
        "च लट् (laṭ) as well. The word QUALIFIES the future rather "
        "than naming a time of its own.",
    ),
    "about": Help(
        "what is the finished word ABOUT?",
        "3.3.33 needs two things at once: the sense must be spreading "
        "out, AND what is spread must not be speech. पटस्य विस्तारः "
        "(paṭasya vistāraḥ), the spread of a cloth, takes the affix; "
        "विस्तरो वचसाम् (vistaro vacasām), speech spread out, does "
        "not — though the spreading is just as real. Say śabda where "
        "words are the subject.",
    ),
    "akartari_karake": Help(
        "does the word name a part in the act OTHER than the doer?",
        "अकर्तरि कारके (akartari kārake) — 3.3.19 wants the finished "
        "word to name what the act is done to, or with, or from, but "
        "not the one who does it: आहरन्ति तस्माद् रसम् इति आहारः "
        "(āharanti tasmād rasam iti āhāraḥ), food, that from which "
        "juice is taken. अकर्तरीति किम्? मिषत्यसौ मेषः — a ram, the "
        "one who blinks, is named as the DOER and falls outside. This "
        "condition runs on from 3.3.19 through the rules after it.",
    ),
    "parimana": Help(
        "is a MEASURE being named?",
        "परिमाणाख्या (parimāṇākhyā) — 3.3.20 gives घञ् (ghañ) after "
        "any root at all where one is: एकस्तण्डुलनिश्चायः "
        "(ekas taṇḍulaniścāyaḥ), one husking of rice. The word आख्या "
        "keeps out mere established usage, and by that NUMBER counts "
        "as a measure too, not only the named units. "
        "परिमाणाख्यायामिति किम्? निश्चयः.",
    ),
    "stri": Help(
        "is the finished word feminine?",
        "स्त्रियाम् (striyām). 3.3.43 gives णच् (ṇac) where two "
        "people do a thing to each other AND the word is feminine: "
        "व्यावक्रोशी (vyāvakrośī), a slanging-match. स्त्रियामिति "
        "किम्? व्यतिपाको वर्तते — the masculine falls outside.",
    ),
    "steya": Help(
        "is the taking a THEFT?",
        "स्तेय (steya), चौर्य — stealing. 3.3.40 needs the fruit to "
        "be within reach and NOT stolen, and the two are separate "
        "questions: फलप्रचयश्चौर्येण (phalapracayaś cauryeṇa), "
        "picking by theft, is perfectly within reach and is still "
        "refused. So say True only where the taking is a theft; the "
        "rule wants its absence.",
    ),
    "root_final": Help(
        "what sound does the root END in?",
        "3.3.56 and 3.3.57 are the first rules of this run to reach by "
        "the root's SHAPE rather than by naming roots: एरच् (er ac) "
        "wants an इ-final root — चयः (cayaḥ), जयः (jayaḥ) — and "
        "ॠदोरप् (ṝdor ap) wants one ending in ॠ or in उ — करः "
        "(karaḥ), यवः (yavaḥ). Say i, ī, ṝ, u or ū.",
    ),
    "gurumat": Help(
        "does the root have a HEAVY vowel?",
        "गुरु (guru) — a long vowel, or a short one before two "
        "consonants. 3.3.103 wants a heavy root that ALSO ends in a "
        "consonant, and tests the two apart: गुरोरिति किम्? भक्तिः "
        "(bhaktiḥ), where the root is light. See `hal_final` for the "
        "other half.",
    ),
    "hal_final": Help(
        "does the root end in a CONSONANT?",
        "हल् (hal) — any consonant. The second half of 3.3.103's "
        "condition, and the commentary shows it is not implied by the "
        "first: हल इति किम्? नीतिः (nītiḥ), where the root is heavy "
        "and ends in a vowel, so the rule does not reach.",
    ),
    "pratyayanta": Help(
        "is the stem already MADE with an affix?",
        "प्रत्ययान्त (pratyayānta) — a stem built from a root with an "
        "affix already on it, rather than a bare root. 3.3.102 "
        "reaches चिकीर्ष (cikīrṣ), the desiderative of कृ, giving "
        "चिकीर्षा (cikīrṣā), a wish to do; and पुत्रीय (putrīya), "
        "giving पुत्रीया. Two rules of the chapter before wanted "
        "particular such stems; this wants any.",
    ),
    "pum": Help(
        "is the finished word masculine?",
        "पुंसि (puṃsi). 3.3.118 and 3.3.121 want it, where 3.3.94 "
        "onward wanted the feminine and 3.3.114 onward the neuter — "
        "so all three genders divide the close of this pāda between "
        "them: आकरः (ākaraḥ), a mine; लेखः (lekhaḥ), writing. "
        "पुंसीति किम्? प्रसाधनम्.",
    ),
    "isadadi": Help(
        "does ईषद्, दुर् or सु stand before?",
        "ईषद् (īṣad) a little, दुर् (dur) badly or with difficulty, "
        "सु (su) well or easily. 3.3.126 onward want one of the "
        "three, AND the sense must be difficulty or ease: दुष्करः "
        "(duṣkaraḥ), hard to do; सुकरः (sukaraḥ), easy. The "
        "commentary divides the two senses between the three without "
        "counting them off — hard goes with दुर्, ease with the "
        "other two, संभवात्, by what each can sensibly mean.",
    ),
    "like": Help(
        "which tense's affixes are being borrowed?",
        "वत् (vat), 'as if'. 3.3.131 lets the PRESENT's affixes stand "
        "for what is near the present — वर्तमानवत् — and 3.3.132 the "
        "PAST's for a hoped-for future. Say vartamāna, bhūta or "
        "anadyatana. The transfer carries everything: whatever "
        "conditions an affix had in its own time it keeps in the "
        "borrowed one, which is why पवमानः (pavamānaḥ) comes out of "
        "a rule about the present read for the past.",
    ),
    "for_time": Help(
        "which time are they being used FOR?",
        "The time the borrowed affixes stand in. 3.3.131 lends them "
        "to what is NEAR the present, past or future alike — कदा "
        "देवदत्तागतोऽसि? अयमागच्छामि (kadā devadattāgato'si? "
        "ayamāgacchāmi), 'when did you come?' 'I am coming' — and "
        "3.3.132 to a hoped-for future.",
    ),
    "kriyatipatti": Help(
        "did the act FAIL to come off?",
        "क्रियातिपत्ति (kriyātipatti) — कुतश्चिद् वैगुण्याद् "
        "अनभिनिर्वृत्तिः क्रियायाः, the act not happening through "
        "something going wrong. 3.3.139 and 3.3.140 give लृङ् (lṛṅ) "
        "for it: यदि कमलकमाह्वास्यन्न शकटं पर्याभविष्यत् (yadi "
        "kamalakam āhvāsyan na śakaṭaṃ paryābhaviṣyat), had they "
        "called Kamalaka the cart would not have overturned.",
    ),
    "lin_nimitta": Help(
        "would some rule have given लिङ् here?",
        "लिङ्निमित्त (liṅnimitta) — that a rule such as 3.3.156 "
        "हेतुहेतुमतोर्लिङ् applies to this situation. A condition "
        "about the GRAMMAR'S own state rather than about the act, "
        "the speaker or the company, and the only one of its kind in "
        "these two pādas. 3.3.139 needs it; 3.3.146 notes that where "
        "no rule gives लिङ्, the ending of a failed act cannot come "
        "either.",
    ),
    "samana_kartrka": Help(
        "do both acts have the SAME doer?",
        "समानकर्तृक (samānakartṛka). 3.3.158 gives तुमुन् (tumun) "
        "only when the one who wishes is the one who acts: इच्छति "
        "भोक्तुम् (icchati bhoktum), he wants to eat. "
        "समानकर्तृकेष्विति किम्? देवदत्तं भुञ्जानम् इच्छति यज्ञदत्तः "
        "— Yajñadatta wants Devadatta to eat, two doers, and the "
        "affix does not come.",
    ),
    "related": Help(
        "do two acts stand in a relation of qualifier and qualified?",
        "धातुसंबन्ध (dhātusaṃbandha). 3.4.1 says that where they do, "
        "an affix stated for the WRONG TIME is correct anyway: "
        "अग्निष्टोमयाज्यस्य पुत्रो जनिता (agniṣṭomayājyasya putro "
        "janitā), where the first word is of the past and the second "
        "of the future. And only one way round — the qualifier "
        "accommodates the qualified's time, not the reverse.",
    ),
    "gathered": Help(
        "are SEVERAL acts being gathered together?",
        "समुच्चय (samuccaya). 3.4.4 says the doubled verb is followed "
        "by the SAME root; 3.4.5 says that where several acts are "
        "gathered, one root covering them all is used instead — ओदनं "
        "भुङ्क्ष्व, सक्तून् पिब, धानाः खाद इत्येवायम् अभ्यवहरति, "
        "three particular acts answered by one general word for "
        "taking food.",
    ),
    "doubled": Help(
        "is the verb DOUBLED?",
        "द्विर्वचन (dvirvacana). 3.4.2 and 3.4.3 give an ending that "
        "needs the verb said twice to show its sense — "
        "लुनीहिलुनीहि (lunīhi lunīhi), 'cut and cut'. The commentary "
        "notes that the affix यङ् (yaṅ), given for the very same "
        "sense, needs no doubling: two routes to one meaning, only "
        "one of them self-sufficient.",
    ),
    "krtya_artha": Help(
        "is the sense that of the कृत्य affixes?",
        "कृत्यानामर्थो भावकर्मणी — the act itself, or what the act is "
        "done to. 3.4.14 gives four Vedic affixes in that sense "
        "rather than in the infinitive's: अन्वेतवै (anvetavai), to be "
        "followed. One of the four had already been given for the "
        "infinitive five rules back, so the commentary reads its "
        "statement here as being about something else.",
    ),
    "bhava_laksana": Help(
        "does the root's sense MARK OUT a state?",
        "भावलक्षण (bhāvalakṣaṇa) — भावो लक्ष्यते येन. 3.4.16 and "
        "3.4.17 give affixes whose words then mean 'until' or "
        "'before' rather than the act itself: पुरा सूर्यस्योदेतोः "
        "(purā sūryasyodetoḥ), before sunrise. It qualifies what the "
        "ROOT means, not what the affix does.",
    ),
    "purvakala": Help(
        "is this the EARLIER of the two acts?",
        "पूर्वकाल (pūrvakāla). 3.4.21 puts क्त्वा (ktvā) on the "
        "earlier act where two acts share a doer: भुक्त्वा व्रजति "
        "(bhuktvā vrajati), having eaten, he goes. पूर्वकाल इति "
        "किम्? व्रजति च जल्पति च — where neither act is earlier, the "
        "affix does not come.",
    ),
    "abhiksnya": Help(
        "is the act done again and again?",
        "आभीक्ष्ण्यं पौनःपुन्यम् (ābhīkṣṇyaṃ paunaḥpunyam). 3.4.22 "
        "gives णमुल् (ṇamul) for it — भोजंभोजं व्रजति (bhojaṃbhojaṃ "
        "vrajati), eating and eating he goes — and neither affix "
        "shows the sense without the verb being DOUBLED.",
    ),
    "paravara": Help(
        "is one thing placed beyond or short of the other?",
        "परावरयोग (parāvarayoga). 3.4.20's condition is about how two "
        "things STAND rather than about an act: अप्राप्य नदीं पर्वतः "
        "स्थितः (aprāpya nadīṃ parvataḥ sthitaḥ), the mountain "
        "standing short of the river; अतिक्रम्य तु पर्वतं नदी स्थिता, "
        "the river lying beyond the mountain.",
    ),
    "vyatihara": Help(
        "is it an EXCHANGE?",
        "व्यतीहार (vyatīhāra) — one thing given for another. 3.4.19 "
        "gives क्त्वा for it after one root: अपमित्य याचते (apamitya "
        "yācate), having borrowed, he asks. The rule is attributed to "
        "the teachers of the north, and naming them is itself what "
        "leaves the ordinary form standing too.",
    ),
    "anakanksa": Help(
        "does the sentence look for nothing further?",
        "अनाकाङ्क्ष (anākāṅkṣa). 3.4.23 REFUSES both affixes where "
        "यद् (yad) stands and the sentence is complete in itself: "
        "यदयं भुङ्क्ते ततः पठति (yad ayaṃ bhuṅkte tataḥ paṭhati). "
        "अनाकाङ्क्ष इति किम्? — where more IS looked for, the affix "
        "comes after all.",
    ),
    "siddha_aprayoga": Help(
        "does the verb 'make' add nothing to the sense?",
        "सिद्धाप्रयोग (siddhāprayoga). 3.4.27 and 3.4.28 give an "
        "affix after words like 'otherwise' and 'how', but only where "
        "the verb contributes no meaning: अन्यथा भुङ्क्त इति "
        "यावानर्थः, तावानेवान्यथाकारं भुङ्क्ते — the compound says "
        "exactly what the two words said. सिद्धाप्रयोग इति किम्? "
        "अन्यथा कृत्वा शिरो भुङ्क्ते, where somebody really does "
        "something and the affix does not come. The companion "
        "condition to 3.3.154's, which wanted a WORD "
        "meant and not said; this wants a ROOT that adds nothing to "
        "what is said.",
    ),
    "vibhakti": Help(
        "what CASE-ENDING does the companion carry?",
        "From 3.4.47 the rules divide by the companion's ending "
        "rather than by its role — तृतीयायाम् (tṛtīyāyām) the third "
        "case, सप्तम्याम् the seventh, द्वितीयायाम् the second. No "
        "chapter before this used a condition on the SURFACE FORM of "
        "a companion, and 3.4.47 shows why it must: मूलकादि "
        "चोपदंशेः कर्म, भुजेः करणम् — the same word is the object of "
        "one verb and the means of the other, so no single role "
        "could have been named.",
    ),
    "svanga": Help(
        "is the companion a part of one's OWN body?",
        "स्वाङ्ग (svāṅga) — अद्रवं मूर्तिमत्स्वाङ्गम्, a solid "
        "bodily part. 3.4.54 and 3.4.55 want one: अक्षिनिकाणं "
        "जल्पति (akṣinikāṇaṃ jalpati), he talks with a wink; "
        "उरःपेषं युध्यन्ते, they fight chest to chest.",
    ),
    "adhruva": Help(
        "is it a part one could lose and live?",
        "अध्रुव (adhruva), defined by what survives its loss: "
        "यस्मिन्नङ्गे छिन्नेऽपि प्राणी न म्रियते तदध्रुवम् — a limb "
        "whose cutting off does not kill. 3.4.54 wants such a part "
        "and 3.4.55 exists for the others, so the two cover the body "
        "between them. A grammatical condition settled by a fact "
        "about bodies.",
    ),
    "kashadi": Help(
        "is the root one of the कषादि class?",
        "कषादि (kaṣādi) — the roots named from 3.4.34 onward, called "
        "after the first of them. 3.4.46 says the SAME root must be "
        "said after each. Unlike every other gaṇa met here, the "
        "class is defined by where a run BEGINS rather than by a "
        "list: इतः प्रभृति कषादीन् यान् वक्ष्यति.",
    ),
    "adikarman": Help(
        "is only the BEGINNING of the act meant?",
        "आदिकर्मन् (ādikarman) — आदिभूतः क्रियाक्षणः, the first "
        "moment of an act. 3.4.71 lets the past affix क्त (kta) "
        "denote the DOER there: प्रकृतः कटं देवदत्तः (prakṛtaḥ kaṭaṃ "
        "devadattaḥ), Devadatta has begun the mat. The beginning is "
        "spoken of AS PAST, which is what lets a past affix reach it "
        "— a matter of how the moment is meant, not of when it was.",
    ),
    "sense_stated": Help(
        "did the rule that GAVE the affix name a sense of its own?",
        "3.4.67 कर्तरि कृत् supplies the DOER as the sense of every "
        "कृत् affix — but only where the rule giving it named none: "
        "तत्र येष्वर्थादेशो नास्ति तत्रेदमुपतिष्ठते, "
        "अर्थाकाङ्क्षत्वात्. Where a sense was stated outright the "
        "heading has nothing to supply. A heading that fills gaps "
        "rather than covering ground, which no earlier one did.",
    ),
    "root_sense": Help(
        "what KIND of sense does the root have?",
        "3.4.72 wants roots meaning MOTION, 3.4.76 those meaning "
        "fixity, motion or consuming — ध्रौव्य, गति, प्रत्यवसान. And "
        "the three reach different sets: fixity gives the doer, the "
        "act and the locus; motion adds the object; consuming drops "
        "the doer. The rule states none of that and the commentary "
        "supplies it.",
    ),
    "name": Help(
        "which of the ten tense-endings?",
        "3.4.77 enumerates them — लट् (laṭ), लिट्, लुट्, लृट्, लेट्, "
        "लोट्, लङ्, लिङ्, लुङ्, लृङ् — ordered as the alphabet is by "
        "the vowel each carries. Six are marked ट and four ङ, and "
        "the mark is not decoration: 3.4.79 replaces part of an "
        "ātmanepada ending after a ट-marked one, which is why लट् "
        "gives पचते and not *पचत.",
    ),
    "lakara": Help(
        "which of the ten tense-endings?",
        "3.4.78 gives the eighteen substitutes that stand in place of "
        "any लकार (lakāra) — three persons by three numbers in each "
        "of two voices, तिप् (tip) through महिङ् (mahiṅ). The ṅ on "
        "the LAST of them is what lets the whole set be named तिङ् "
        "(tiṅ), and 3.4.113 stands on that name.",
    ),
    "unadi": Help(
        "is the word one of the उणादि formations?",
        "उणादि (uṇādi) — a word made with an affix from the separate "
        "book of 748 sūtras that 3.3.1 licenses. 3.4.75 says such a "
        "word denotes a part OTHER than the doer and the source: "
        "कृषितोऽसौ कृषिः (kṛṣito'sau kṛṣiḥ), ploughing, that which is "
        "ploughed.\u0020Two rules speak of these words and they ask "
        "different things — whether the word stands, and what it "
        "denotes.",
    ),
    "ending_pada": Help(
        "which set of endings — active or middle?",
        "परस्मैपद (parasmaipada) or आत्मनेपद (ātmanepada). 3.4.78 gives "
        "nine of each, and many rules of this run hold to one set: "
        "3.4.82 replaces the nine active ones in the perfect, 3.4.81 "
        "two of the middle. NOT the पद (pada) of 1.4.14, which means a "
        "finished word — this codebase asks that one under `pada`.",
    ),
    "person": Help(
        "which person?",
        "उत्तम (uttama) is the FIRST person in the Indian ordering — "
        "पचामि (pacāmi), I cook — and it is the one these rules single "
        "out: 3.4.92 gives it an augment, 3.4.98 and 3.4.99 drop its "
        "स्. मध्यम (madhyama) is the second and प्रथम (prathama) the "
        "third, which is the reverse of the European numbering.",
    ),
    "preceded_by": Help(
        "what stands in front of the ending?",
        "The condition several rules of this run state: सिच् (sic), an "
        "अभ्यस्त (abhyasta) reduplicated stem, a long आ (ā), or the स "
        "and व that 3.4.91 wants. Not `after`, which this codebase "
        "already asks for the sound that FOLLOWS.",
    ),
    "after_a_root": Help(
        "is the affix given after a root?",
        "धातोः (dhātoḥ) — 3.4.114 names only affixes given after a "
        "root, and the काशिका (Kāśikā) marks the edge with four forms "
        "that are not: वृक्षत्वम् (vṛkṣatvam) and वृक्षतास्ति "
        "(vṛkṣatāsti), from a noun; लूभ्याम् (lūbhyām) and लूभिः "
        "(lūbhiḥ), case-endings on a stem; and जुगुप्सते (jugupsate), "
        "where सन् (san) is given to MAKE a root rather than after one.",
    ),
    "final": Help(
        "what did the धातुपाठ give the root for its last sound?",
        "6.1.45 आदेच उपदेशे‍शिति turns on the shape the root was "
        "TAUGHT with, not the shape standing here. ग्लै (glai) was "
        "taught with an ऐ and gives ग्लाता (glātā); चि (ci) was "
        "taught with an इ and its ए in चेता (cetā) is guṇa "
        "arrived at later, so the rule does not reach it. Answer with "
        "one of e, ai, o, au — the एच् (eC) — or leave it empty.",
    ),
    "across": Help(
        "does anything stand between the preverb and the क्?",
        "6.1.136 अडभ्यासव्यवाये‍पि is the whole of what that "
        "rule contributes: the सुट् still goes in before the क् "
        "even where the अट् (aṭ) of the imperfect or the "
        "reduplicated syllable has come between. समस्करोत् "
        "(samaskarot) shows the first and संचस्कार (saṃcaskāra) "
        "the second. Answer aṭ or abhyāsa, or leave it empty.",
    ),
    "marker": Help(
        "which इत् does the affix carry?",
        "The accent rules of this pāda turn on an affix's markers "
        "more than "
        "on anything else: चित् accents the end (6.1.163), ञित् "
        "and नित् the first (6.1.197), तित् gives a स्वरित "
        "(6.1.185), लित् accents the syllable before the affix "
        "(6.1.193), and रित् the one before the last (6.1.217). One "
        "affix can carry two — च्फञ् has a च् and a ञ्, and 6.1.164 "
        "is stated to settle which of the two decides.",
    ),
    "bhasayam": Help(
        "is this ordinary speech rather than the Veda?",
        "6.1.181 विभाषा भाषायाम् is the one rule of the pāda whose "
        "condition is that the language is NOT Vedic: the penult "
        "accent 6.1.180 fixes for पञ्चभिः (pañcábhiḥ) becomes a "
        "choice, so पञ्चभिः (pañcabhíḥ) stands beside it. Every "
        "other corpus condition in the pāda runs the other way.",
    ),
    "yajusi": Help(
        "is this the यजुर्वेद in particular?",
        "Kept apart from the general Vedic corpus because 6.1.115 "
        "wants a position INSIDE a verse-foot and that corpus has "
        "none: यजुषि पादानामभावाद् अनन्तःपादार्थं वचनम्. "
        "6.1.117 to 6.1.121 are stated over again for prose, and "
        "reach nothing without this answered."
    ),
    "teacher": Help(
        "whose opinion is the rule reported as?",
        "Four आचार्य are named outright in this pāda: आपिशलि "
        "(Āpiśali) at 6.1.92, स्फोटायन (Sphoṭāyana) at 6.1.123, "
        "शाकल्य (Śākalya) at 6.1.127 and 6.1.128, and चाक्रवर्मण "
        "(Cākravarmaṇa) at 6.1.130. For three of them the vṛtti says "
        "the name is पूजार्थम्, for honour, since the वा already "
        "makes the rule optional; for the fourth it says "
        "चाक्रवर्मणग्रहणं विकल्पार्थम् — the name is what makes it "
        "a choice at all. Name one to reach that teacher's rule.",
    ),
    "part": Help(
        "which half of the doubled form?",
        "अभ्यास (abhyāsa) is the FIRST of the two copies and "
        "अभ्यस्त (abhyasta) is the two together. 6.1.4 names the "
        "one, 6.1.5 the other, and the difference decides where an "
        "accent falls: नेनिजति (nenijati) takes it once, on the "
        "first vowel of the pair. Answer pūrva for the copy alone, "
        "ubhe for both.",
    ),
    "at": Help(
        "where in the portion does that sound stand?",
        "6.1.3 keeps न् (n), द् (d) and र् (r) out of the copy only "
        "where they OPEN a cluster — संयोगादि (saṃyogādi). "
        "उन्दिदिषति (undidiṣati) drops its न् because न्द् is a "
        "cluster; प्राणिणिषति (prāṇiṇiṣati) keeps its ण् "
        "because nothing follows it.",
    ),
    "already": Help(
        "has a semivowel already been vocalised in this word?",
        "6.1.37 न संप्रसारणे संप्रसारणम् turns on a state "
        "rather than on a root or an affix: once one यण् (yaṇ) has "
        "given up its consonant, the one before it does not. "
        "व्यध् (vyadh) has both व् and य्, and only the य् goes "
        "— विद्धः (viddhaḥ), never *उद्धः.",
    ),
    "purvapada": Help(
        "what is the FIRST member of the compound?",
        "पूर्वपद (pūrvapada) — and 6.2 is about almost nothing "
        "else. 6.1.223 put the accent at the end of a compound and "
        "silenced every other syllable; 6.2.1 to 6.2.110 are the "
        "cases where the FIRST member keeps or takes one instead. "
        "गोस्वामी (gosvāmī) keeps गो's own accent where "
        "परमस्वामी (paramasvāmī) does not.",
    ),
    "purvapada_gana": Help(
        "what CLASS does the FIRST member belong to?",
        "The rules of 6.2.111-199 reach the first member "
        "sometimes by name and sometimes by the class it falls "
        "in: a गति (gati), a कारक (kāraka) or an उपपद (upapada) at 6.2.139, "
        "an उपसर्ग (upasarga) at 6.2.177, a word for a man at "
        "6.2.132, a numeral at 6.2.163. Answer with the class "
        "where the rule names one; where it names a word, use "
        "`purvapada` instead.",
    ),
    "uttarapada_gana": Help(
        "what CLASS does the second member belong to?",
        "Some rules of 6.2 name the second member outright and some "
        "name a class it falls in — घोषादि (ghoṣādi) at 6.2.85, "
        "a lineage or a pupil at 6.2.69, a village- or "
        "country-name at 6.2.103. Answer with the class where the "
        "rule names one; where it names a word, use `uttarapada` "
        "instead.",
    ),
    "uttarapada_affix": Help(
        "what does the SECOND member end in?",
        "Some rules of 6.2 name a word that must follow and some "
        "name an AFFIX it must end in — क्त (kta) at 6.2.45 to "
        "6.2.49, तवै (tavai) at 6.2.51, the वि (vi) of अञ्च् "
        "(añc) at 6.2.52. Answer with the affix where the rule "
        "names one; where it names a word, use `uttarapada` "
        "instead.",
    ),
    "uttarapada": Help(
        "what is the LAST member of the compound?",
        "उत्तरपद (uttarapada) — the second member of a compound, "
        "where a rule names that member and takes any compound "
        "ending in it. 5.1.9 wants भोग (bhoga): मातृभोगीणः "
        "(mātṛbhogīṇaḥ) and पितृभोगीणः (pitṛbhogīṇaḥ) are taken, and "
        "मातृ (mātṛ) alone is not. Distinct from `stem_final`, which "
        "asks after a SOUND or a stem's own ending rather than a "
        "member the compound is built from.",
    ),
    "compounded": Help(
        "is the base standing in a compound?",
        "समास (samāsa) — pass \"yes\" where the base is a compound "
        "and \"no\" or nothing where it is not. 5.1.20 says "
        "असमासे (asamāse), *not in a compound*: निष्केण क्रीतं "
        "नैष्किकम् (naiṣkikam), but द्विनैष्किकम् (dvinaiṣkikam) "
        "falls back on the heading. Saying it there is a ज्ञापक "
        "(jñāpaka) that compounds were NOT excluded from the rules "
        "before it — सुगव्यम् (sugavyam), राजदन्त्यम् "
        "(rājadantyam).",
    ),
    "stem_final": Help(
        "what does the stem end in?",
        "The last sound or last member of a प्रातिपदिक (prātipadika). "
        "4.1.5 wants ऋ (ṛ) or न् (n), 4.1.7 वन् (van), 4.1.11 मन् "
        "(man), 4.1.25 ऊधस् (ūdhas). Not `ends_in`, which this "
        "codebase asks for a compound's last member, nor `root_final`, "
        "which it asks for a root's last sound.",
    ),
    "marked": Help(
        "which इत् did the stem's own affix carry?",
        "अनुबन्ध (anubandha) — a silent letter on the affix that made "
        "the stem. 4.1.6 wants उगित् (ugit), one marked with उ (u), ऋ "
        "(ṛ) or ऌ (ḷ); 4.1.15 names thirteen kinds at once; 4.1.16 "
        "यञ् (yañ). The mark is gone from the word and the rule still "
        "finds it, which is what makes these conditions invisible "
        "without saying so.",
    ),
    "gana": Help(
        "which गण does the stem belong to?",
        "गण (gaṇa) — a named list in the गणपाठ (gaṇapāṭha) that a "
        "sūtra cites by its first member: अजादि (ajādi), स्वस्रादि "
        "(svasrādi), सपत्न्यादि (sapatnyādi). The lists are on disk "
        "and are read from there, not retyped.",
    ),
    "compound": Help(
        "is the stem a compound, and of which kind?",
        "बहुव्रीहि (bahuvrīhi) — a compound denoting something other "
        "than its own members, सुपर्वन् (suparvan), one having good "
        "joints. द्विगु (dvigu) — one beginning with a numeral, "
        "पञ्चपूली (pañcapūlī). Several rules here turn on which.",
    ),
    "samjna": Help(
        "which name has the grammar already given the stem?",
        "संज्ञा (saṃjñā) — a technical name conferred elsewhere and "
        "used here as a condition. षट् (ṣaṭ) is 1.1.24's name for the "
        "numerals from five up; उपधालोपिन् (upadhālopin) is a stem "
        "that drops its penultimate; संख्यादि (saṃkhyādi) one "
        "beginning with a numeral.",
    ),
    "upasarjana": Help(
        "is the stem a subordinate member of a compound?",
        "उपसर्जन (upasarjana) — 1.2.43's name for the member of a "
        "compound that is not the principal one. 4.1.14 अनुपसर्जनात् "
        "(anupasarjanāt) refuses every feminine affix to such a "
        "member: बहुकुक्कुटा (bahukukkuṭā) against कुक्कुटी "
        "(kukkuṭī).",
    ),
    "pratipadika": Help(
        "is a bare nominal stem in question?",
        "प्रातिपदिक (prātipadika) — 1.2.45's name for a meaningful "
        "word that is neither a root nor an affix, widened by 1.2.46 "
        "to take in what a कृत् (kṛt), a तद्धित (taddhita) or a "
        "compound makes. It is the first of the three things 4.1.1 "
        "names.",
    ),
    "ngi": Help(
        "is one of the ङी affixes in question?",
        "ङी (ṅī) — 4.1.1's class-word for ङीप् (ṅīp), ङीष् (ṅīṣ) and "
        "ङीन् (ṅīn) taken together: ङीब्ङीष्ङीनां सामान्येन ग्रहणं "
        "ङीति. All three make a feminine stem in ई (ī) and differ in "
        "accent and in what else their marks bring.",
    ),
    "ap": Help(
        "is one of the आप् affixes in question?",
        "आप् (āp) — 4.1.1's class-word for टाप् (ṭāp), डाप् (ḍāp) and "
        "चाप् (cāp): टाप्डाप्चापामाबिति. All three make a feminine "
        "stem in आ (ā), and खट्वा (khaṭvā) is the first one's.",
    ),
    "accent": Help(
        "where is the stem accented?",
        "अनुदात्तान्त (anudāttānta) — unaccented at the end, which "
        "4.1.39 and 4.1.40 both require. अन्तोदात्त (antodātta) — "
        "accented at the end, which 4.1.52 wants. Three pairs of rules "
        "in this quarter give affixes that differ in NOTHING BUT the "
        "accent they leave, so it is a condition and not a footnote.",
    ),
    "elided": Help(
        "are you asking after the form the affix has gone from?",
        "Some rules give an affix and others take one away, and a few "
        "pairs do both on the same ground: 4.3.165 जम्ब्वा वा "
        "(jambvā vā) gives अण् (aṇ) and 4.3.166 लुप् च (lup ca) "
        "removes it, so जाम्बवानि फलानि (jāmbavāni phalāni) and "
        "जम्बूः फलम् (jambūḥ phalam) are both correct. Nothing in the "
        "words distinguishes them — only which form is being asked "
        "for.",
    ),
    "usage": Help(
        "which register is the rule confined to?",
        "छन्दसि (chandasi) — the Veda only, as at 4.3.19 and 4.3.106; "
        "भाषा (bhāṣā) — the spoken language only, as at 4.3.143 and "
        "4.3.144; and nothing at all for the rules that hold in both. "
        "One field rather than two flags, because a rule belongs to "
        "one register, the other, or neither, and never to both.",
    ),
    "vowels": Help(
        "how many vowels does the base have?",
        "बह्वच् (bahvac), *of many vowels*, is 4.3.67's condition; "
        "द्व्यच् (dvyac), *of two*, is 4.3.72's; एकाच् (ekāc), *of "
        "one*, is what the counter-examples between them show. One "
        "field and not three flags, because the rules are the halves "
        "of a single question — **बह्वच इति किम्? द्व्यचष्ठकं "
        "वक्ष्यति** — and a base cannot be two of them at once.",
    ),
    "upadha": Help(
        "what is the stem's penultimate sound?",
        "उपधा (upadhā) — the sound before the last, named by 1.1.65. "
        "4.1.39 wants त (t) there and turns it into न (n): एता (etā) "
        "beside एनी (enī).",
    ),
    "not_upadha": Help(
        "which penultimate does the rule REFUSE?",
        "Some rules of this run are stated against a neighbour's "
        "condition rather than for one of their own. 4.1.40 अन्यतः "
        "(anyataḥ) means *with any penultimate but the one just "
        "named*; 4.1.54 wants असंयोगोपध (asaṃyogopadha), no conjunct "
        "there; 4.1.63 wants अयोपध (ayopadha), no य (ya).",
    ),
    "pre": Help(
        "what stands in front, as first member?",
        "करणपूर्व (karaṇapūrva) — the first member names the MEANS, "
        "वस्त्रक्रीती (vastrakrītī), bought with a cloth. दिक्पूर्व "
        "(dikpūrva) — a direction, प्राङ्मुखी (prāṅmukhī). And the "
        "सह-नञ्-विद्यमान (saha-nañ-vidyamāna) of 4.1.57, three words "
        "whose presence in front refuses the affix.",
    ),
    "position": Help(
        "which of the connected words is in question?",
        "4.1.82 says the affix comes after the FIRST of the words "
        "that go together — समर्थानां प्रथमात् (samarthānāṃ "
        "prathamāt). In उपगोरपत्यम् (upagor apatyam), *Upagu's "
        "descendant*, that is उपगु (upagu), the one in the genitive, "
        "and not अपत्य (apatya).",
    ),
    "connected": Help(
        "do the words actually go together?",
        "सामर्थ्य (sāmarthya) — being syntactically connected. Two "
        "words can sit in one sentence without it: कम्बल उपगोः, "
        "अपत्यं देवदत्तस्य (kambala upagoḥ, apatyaṃ devadattasya) "
        "has उपगु (upagu) and अपत्य (apatya) side by side and "
        "belonging to different phrases, and 4.1.82's first word is "
        "what stops the affix crossing between them.",
    ),
    "gotra": Help(
        "is a lineage-name in question?",
        "गोत्र (gotra) — 4.1.162 defines it as a descendant from the "
        "grandson onward, and a गोत्र affix is one given in that "
        "sense. 4.1.89 refuses to drop such an affix before a "
        "vowel-initial one: गार्गीयाः (gārgīyāḥ).",
    ),
    "before_ac": Help(
        "does a vowel-initial affix follow?",
        "अच् (ac) — 4.1.89's अलुगचि (aluk aci) and 4.1.90's अजादौ "
        "(ajādau) both turn on it. Whether an affix already dropped "
        "comes back, and whether one about to be formed is dropped, "
        "depend on what follows.",
    ),
    "apatya": Help(
        "is it a patronymic?",
        "अपत्य (apatya) — a descendant, the sense 4.1.92 गives its "
        "whole section to. 4.1.88 drops a taddhita after a numeral "
        "compound EXCEPT a patronymic: पञ्चकपालः (pañcakapālaḥ) "
        "loses its affix and द्वैदेवदत्तिः (dvaidevadattiḥ) keeps "
        "its own.",
    ),
    "yuvan": Help(
        "is a young descendant in question?",
        "युवन् (yuvan) — 4.1.163 names the descendant whose father "
        "or elder is still living. 4.1.90 drops the affix given in "
        "that sense before it is even formed, and 4.1.91 makes that "
        "optional for two of them.",
    ),
    "among": Help(
        "whose family is meant?",
        "Five rules of this run turn on a lineage the word itself "
        "says nothing about: भार्गव (bhārgava), वात्स्य (vātsya), "
        "आग्रायण (āgrāyaṇa), ब्राह्मण (brāhmaṇa), कौशिक (kauśika), "
        "आङ्गिरस (āṅgirasa), त्रैगर्त (traigarta). शारद्वतायनः "
        "(śāradvatāyanaḥ) if a Bhārgava is meant and शारद्वतः "
        "(śāradvataḥ) otherwise — same word, same sense, different "
        "family.",
    ),
    "feminine": Help(
        "is a woman meant?",
        "स्त्री (strī). 4.1.94 ends with अस्त्रियाम् (astriyām), and "
        "the काशिका (Kāśikā) splits the rule in two to make that "
        "clause work: what it refuses is the NAME युवन् (yuvan), so "
        "a woman is named by the lineage-affix instead — दाक्षी "
        "(dākṣī), प्लाक्षी (plākṣī).",
    ),
    "dvyac": Help(
        "does the stem have exactly two vowels?",
        "द्व्यच् (dvyac). 4.1.121 and 4.1.122 both state it, and it "
        "is the second condition of sheer length in the quarter after "
        "4.1.56's बह्वच् (bahvac). दात्तेयः (dātteyaḥ) has it and "
        "यामुनः (yāmunaḥ) does not.",
    ),
    "stri_pratyaya": Help(
        "does the stem end in a feminine affix?",
        "4.1.120's स्त्री (strī) names the AFFIX and not the sense — "
        "इह स्त्रीग्रहणेन टाबादिप्रत्ययान्ताः शब्दा गृह्यन्ते. So "
        "इडबिडा (iḍabiḍā) and दरदा (daradā), feminine in meaning and "
        "carrying no feminine affix, are outside it. The exact "
        "reverse of 4.1.115 five rules earlier.",
    ),
    "not_marked": Help(
        "which affix must the stem NOT carry?",
        "4.1.122 wants a stem in इ (i) but NOT one whose इ is 4.1.95's "
        "इञ् (iñ): आत्रेयः (ātreyaḥ) but दाक्षिः (dākṣiḥ). A "
        "condition not on the shape of the word but on which rule "
        "produced it.",
    ),
    "authority": Help(
        "whose view is being asked for?",
        "प्राचाम् (prācām), the eastern teachers; उदीचाम् (udīcām), "
        "the northern; शाकटायन (śākaṭāyana), one man. A rule given on "
        "a teacher's authority does not apply unless that view is "
        "asked for — 4.1.130's आरक् (ārak) stands BESIDE 4.1.129's "
        "ढ्रक् (ḍhrak) rather than over it, and the काशिका (Kāśikā) "
        "says the word *teachers* is there for honour.",
    ),
    "attitude": Help(
        "is respect or contempt being expressed?",
        "कुत्सन (kutsana) — disparagement, which conditions 4.1.147 "
        "to 4.1.149 and 4.1.167. पूजा (pūjā) — respect, which "
        "conditions 4.1.166. Two adjacent rules make the same pair of "
        "names optional in opposite directions: the young-name used "
        "of an elder out of respect, the lineage-name used of a young "
        "man out of contempt.",
    ),
    "janapada": Help(
        "does the base name a country whose people are kṣatriyas?",
        "जनपदशब्दात् क्षत्रियात् (janapadaśabdāt kṣatriyāt) — the "
        "ground of 4.1.168 and the eight rules after it, whose "
        "affixes 4.1.174 names तद्राज (tadrāja). And what is said of "
        "the descendant holds of the RULER: पञ्चालानां राजा पाञ्चालः "
        "(pañcālānāṃ rājā pāñcālaḥ).",
    ),
    "generation": Help(
        "how many generations down?",
        "4.1.162 confers गोत्र (gotra) from the grandson onward — "
        "पौत्रप्रभृति (pautraprabhṛti) — so the son is outside it. "
        "And 4.1.163's commentary changes the case of that very word "
        "so that युवन् (yuvan) starts from the FOURTH generation "
        "instead of the third.",
    ),
    "elder_alive": Help(
        "is an elder of the line still living?",
        "जीवति वंश्ये (jīvati vaṃśye) — 4.1.163's condition, and the "
        "whole difference between the two names. 4.1.164 extends it "
        "to an elder BROTHER, though a brother is not an ancestor: "
        "अकारणत्वात् (akāraṇatvāt), not being a cause of the person.",
    ),
    "elder": Help(
        "which elder?",
        "वंश्य (vaṃśya) — a father or forefather, 4.1.163's. भ्रातृ "
        "(bhrātṛ) — an elder brother, 4.1.164's. सपिण्ड (sapiṇḍa) — "
        "4.1.165's, and the काशिका (Kāśikā) defines it by RITUAL "
        "rather than by descent: those for whom the family's food may "
        "not be eaten for ten days, citing मनु (Manu).",
    ),
    "case": Help(
        "in which case does the base stand?",
        "समर्थविभक्ति (samartha-vibhakti) — the case-relation between "
        "the two connected words. तृतीया (tṛtīyā), instrumental: "
        "*dyed BY that*. सप्तमी (saptamī), locative: *prepared IN "
        "that*. प्रथमा (prathamā), nominative. Each run of rules "
        "carries one, and the काशिका (Kāśikā) names the rule where "
        "each stops.",
    ),
    "joined": Help(
        "what particle or word is it construed with?",
        "पाद ८.१ turns on this and almost nothing else. A finite "
        "verb after a noun loses its accent by 8.1.28, and some thirty "
        "sūtras give it back where the verb is CONSTRUED WITH a "
        "particular word: यत् (yat), यदि (yadi), हन्त (hanta), "
        "नह (naha), सत्यम् (satyam), यावत् (yāvat), "
        "अहो (aho), पुरा (purā), ननु (nanu), जातु (jātu) "
        "and the rest. It is not the same as what stands before or "
        "after: देवदत्तः पचति यावत् (devadattaḥ pacati "
        "yāvat) has the particle LAST and the verb is spared all "
        "the same. Give the particle in roman, as \"yāvat\" or "
        "\"aho\"; leave it empty where the verb stands alone.",
    ),
    "what": Help(
        "which piece of the word is the rule about?",
        "The Vedic rules of 7.1.34–50 act on very different things: "
        "an affix such as क्त्वा (ktvā), a case ending such as "
        "सुप् (sup), a personal ending such as ध्वम् (dhvam), or a "
        "whole word laid down such as इष्ट्वीनम् (iṣṭvīnam). So the "
        "field asks for the piece by name rather than by what kind "
        "of thing it is. यजध्वैनम् (yajadhvainam) at 7.1.43 is one "
        "answer and सुप् (sup) at 7.1.39 is another.",
    ),
    "abhyasa": Help(
        "is the change stated after a reduplication?",
        "अभ्यास (abhyāsa) — 1.1.59 names the doubled syllable, and four rules of "
        "7.3.55–58 state their change AFTER one: जिघांसति (jighāṃsati), "
        "जिगीषति (jigīṣati). Answer yes only where the reduplication is the "
        "root’s own — जिहननीयिषति (jihananīyiṣati) has one that belongs to a "
        "derived stem, and the change does not come.",
    ),
    "view": Help(
        "whose reading of the rule do you want?",
        "A few sūtras record a named teacher’s opinion rather than settling "
        "one. 7.3.46–48 give the northern teachers’ refusal, which is an "
        "option in the language — इभ्यका (ibhyakā) beside इभ्यिका (ibhyikā). "
        "7.3.49 gives the teachers’ आ (ā), which is a fifth form: खट्वाका (khaṭvākā). "
        "Leave it empty for the ordinary answer.",
    ),
    "result": Help(
        "what kind of thing is the result?",
        "Several rules of this run state it in the sūtra rather than "
        "leaving it to the sense: काल (kāla), a time; सामन् (sāman), "
        "a chant; रथ (ratha), a chariot; भक्ष (bhakṣa), something "
        "eaten. पुष्येण युक्तः कालः (puṣyeṇa yuktaḥ kālaḥ) takes the "
        "affix and पुष्येण युक्तश्चन्द्रमाः (puṣyeṇa yuktaś "
        "candramāḥ) does not.",
    ),
    "upadha": Help(
        "which sound is the stem's SECOND-TO-LAST?",
        "उपधा (upadhā) — 1.1.65 defines it as the sound before the "
        "last, and six rules of 4.2.119\u2013145 turn on it. 4.2.121 "
        "wants य् (y), 4.2.123 र् (r), 4.2.132 क् (k), 4.2.141 ख् "
        "(kh). Not `stem_final`: सांकाश्य (sāṃkāśya) has य् (y) for "
        "its penultimate and does not end in it, and asking the wrong "
        "one would reach words the rule never touches.",
    ),
    "ends_with": Help(
        "which word is the compound's LAST MEMBER?",
        "उत्तरपद (uttarapada). 4.2.122 names प्रस्थ (prastha), पुर "
        "(pura) and वह (vaha); 4.2.126 four more; 4.2.142 five. "
        "**अन्तशब्दः प्रत्येकमभिसंबध्यते** — *ending in* attaches to "
        "each of the words named and not to the string of them read "
        "as one compound. मालाप्रस्थकः (mālāprasthakaḥ).",
    ),
    "desa": Help(
        "does the stem name a COUNTRY?",
        "देश (deśa) — the heading that enters at 4.2.119 ओर्देशे "
        "(ordeśe) and runs to the end of the pāda; a dozen vṛttis "
        "along the way open with देश इत्येव (deśa ityeva). "
        "नैषादकर्षुकः (naiṣādakarṣukaḥ) is inside it; पटोश्छात्राः "
        "पाटवाः (paṭoś chātrāḥ pāṭavāḥ) is the counter-example the "
        "opening rule gives.",
    ),
    "unspecified": Help(
        "is no particular part of the day meant?",
        "अविशेषे (aviśeṣe) — 4.2.4's condition, and the only thing "
        "separating it from 4.2.3. The same base, the same case, the "
        "same sense: one gives an affix and the other takes it away. "
        "अद्य पुष्यः (adya puṣyaḥ) against पौषी रात्रिः (pauṣī "
        "rātriḥ).",
    ),
    # --- the first operational rules, 3.1.68 to 7.3.84 -------------------
    "kartari": Help(
        "does the ending denote the agent?",
        "कर्तरि — 3.1.68's condition. Where the sārvadhātuka denotes the "
        "action or the object instead, 3.1.67 gives यक् and not शप्.",
    ),
    "sarvadhatuka_follows": Help(
        "does a सार्वधातुक affix follow?",
        "The ending after the root. 3.4.113 says which affixes bear that "
        "name: a तिङ्, and any शित्.",
    ),
    "sarvadhatuka": Help(
        "is the affix सार्वधातुक?",
        "सार्वधातुक — a तिङ् ending or a शित् affix, by 3.4.113. शप् is one, "
        "which is how जि comes to take guṇa in जयति.",
    ),
    "ardhadhatuka": Help(
        "is the affix आर्धधातुक?",
        "आर्धधातुक — the other half of 7.3.84's condition: कर्ता, चेता, "
        "स्तोता.",
    ),
    "tin": Help(
        "is it a तिङ् ending?",
        "One of the eighteen verbal endings.",
    ),
    "sit": Help(
        "is it a शित् affix?",
        "शित् — marked with श्. शप् is, and that is what brings it under "
        "3.4.113.",
    ),
    "before_vowel": Help(
        "does a vowel follow?",
        "अचि — read down into 6.1.78 from 6.1.77. एच् becomes अय्, अव्, "
        "आय् or आव् only before a vowel.",
    ),
    "tit_lakara": Help(
        "is the लकार टित्?",
        "टित् — marked with ट्. लट् is, which is why एध् gives एधते and "
        "not एधत.",
    ),
    "pada": Help(
        "the finished word",
        "पद — a word as it stands before a pause or the next word. The "
        "tripādī rules act on these, not on stems mid-derivation.",
    ),
    "at_pause": Help(
        "does the word end the utterance?",
        "अवसान — one of 8.3.15's two conditions; the other is a following "
        "खर् sound.",
    ),
    "following": Help(
        "what follows the word",
        "Leave blank at a pause. 8.3.15 acts before खर् or a pause, and "
        "nowhere else: अग्निर्नयति keeps its र्.",
    ),
    # --- members of dataclass parameters, matched on the dotted name ------
    "context.pratyaya": Help("in an affix?", "Where the form stands."),
    "context.vibhakti": Help("in a case ending?", ""),
    "context.taddhita": Help("in a तद्धित?", ""),
    "context.dhatu": Help("in a root?", ""),
    "affix.form": Help("the affix", "In upadeśa form."),
    "affix.its": Help("its it-letters", "Comma-separated."),
    "adesa.form": Help("the substitute", "आदेश."),
    "adesa.its": Help("the substitute's it-letters", "Comma-separated."),
}


def _humanise(name: str) -> str:
    return name.replace("_", " ").replace(".", " · ")


def help_for(name: str) -> Optional[Help]:
    """
    The label and hint for one field, or None where none is written.

    A dotted name is tried whole first — `affix.its` may need saying
    differently from `adesa.its` — and then on its last part, so a member
    shared between rules is described once.
    """
    if name in HELP:
        return HELP[name]
    if "." in name:
        return HELP.get(name.rsplit(".", 1)[1])
    return None


def label_and_hint(name: str) -> Tuple[str, str]:
    """
    What to show for a field, falling back to the parameter name.

    Both halves go through the two-script pairing before they leave here,
    which is the same treatment the docstring panel beside the form gets.
    It was not the same for a while: the panel paired its scripts and the
    field labels under it did not, so a hint could say आर्धधातुक with no
    roman beside it to a reader who cannot yet read the script. Doing it
    at the single point every caller goes through is what keeps the two
    surfaces from drifting apart again.
    """
    from src.astadhyayi.glosses import both_scripts

    def paired(text: str) -> str:
        return both_scripts(text) if text else text

    found = help_for(name)
    if found is None:
        return _humanise(name), ""
    return paired(found.label), paired(found.hint)


def missing(names) -> Tuple[str, ...]:
    """Which of these field names have no help written."""
    return tuple(sorted({n for n in names if help_for(n) is None}))


__all__ = ["Help", "HELP", "help_for", "label_and_hint", "missing"]
