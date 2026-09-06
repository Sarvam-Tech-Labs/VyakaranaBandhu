# -*- coding: utf-8 -*-
r"""अध्याय २, पाद २ — पूर्वनिपात, which member is spoken first."""

from __future__ import annotations

from src.astadhyayi.purvanipata import spoken_first
from src.astadhyayi.sources import register

_CODIFICATION = (
    "spoken_first(members, samasa=..., upasarjana=..., ...) -> which word "
    "comes first and which rule fixed it, or why none does."
)

_ORDER = {
    "2.2.30": (
        (),
        'SETTLED — उपसर्जनसंज्ञकं समासे पूर्वं प्रयोक्तव्यम्: the member\n'
        '  some rule marked subordinate is spoken first, and the whole of\n'
        '  the ordinary case is here. The Kāśikā walks the cases one by\n'
        '  one — कष्टश्रितः, शङ्कुलाखण्डः, यूपदारु, वृकभयम्, राजपुरुषः,\n'
        '  अक्षशौण्डः — second through seventh.\n'
        '\n'
        'SETTLED — पूर्ववचनं परप्रयोगनिवृत्त्यर्थम्, अनियमो हि स्यात्.\n'
        '  The word पूर्वम् is there to shut the other order out; without\n'
        '  it there would be no rule at all rather than a free choice.\n'
        '\n'
        'SETTLED — which member is the upasarjana is 1.2.43\'s and is\n'
        '  stated rather than worked out, because it depends on the rule\n'
        '  that formed the compound and not on the two words.\n'
        '\n'
        'SCAR — this declared it reuses 1.2.43, which it does not: the\n'
        '  upasarjana is STATED here, not computed, precisely because the\n'
        '  two words do not carry it. A dependency that is real in the\n'
        '  grammar is not thereby a call in the code, and the reuse test\n'
        '  caught the difference.'
    ),
    "2.2.31": (
        (),
        'SETTLED — राजदन्तादिषु उपसर्जनं परं प्रयोक्तव्यम्: in this list\n'
        '  of fifty-seven the subordinate member comes LAST. दन्तानां\n'
        '  राजा gives राजदन्तः; वनस्याग्रे gives अग्रेवणम्, and\n'
        '  निपातनाद् अलुक् keeps the locative ending in place.\n'
        '\n'
        'SETTLED — and it reverses more than 2.2.30. न केवलम्\n'
        '  उपसर्जनस्य, अन्यस्यापि यथालक्षणं विहितस्य पूर्वनिपातस्य अयम्\n'
        '  अपवादः — whatever rule would have put a member first, this\n'
        '  overrides it.'
    ),
    "2.2.32": (
        ("1.4.7",),
        'SETTLED — द्वन्द्वे घ्यन्तं पूर्वं प्रयोक्तव्यम्: पटुगुप्तौ,\n'
        '  मृदुगुप्तौ. Which words are घि is 1.4.7\'s and is asked.\n'
        '\n'
        'SETTLED — अनेकप्राप्तावेकस्य नियमः, शेषे त्वनियमः. The rule\n'
        '  fixes one place and leaves the rest free: पटुमृदुशुक्लाः and\n'
        '  पटुशुक्लमृदवः both stand.\n'
        '\n'
        'SETTLED — 2.2.33 beats it where both could act, and the Kāśikā\n'
        '  says so outright: द्वन्द्वे घ्यन्ताद् अजाद्यदन्तं विप्रतिषेधेन.'
    ),
    "2.2.33": (
        (),
        'SETTLED — अजाद्यदन्तं शब्दरूपं द्वन्द्वे पूर्वं प्रयोक्तव्यम्:\n'
        '  उष्ट्रखरम्, उष्ट्रशशकम्. And over 2.2.32 by विप्रतिषेध —\n'
        '  इन्द्राग्नी, इन्द्रवायू.\n'
        '\n'
        'SETTLED — the final अ is tapara, and the Kāśikā asks why:\n'
        '  तपरकरणं किम्? अश्वावृषौ, वृषाश्व इति वा — a long ā does not\n'
        '  qualify, and that pair is left unordered.\n'
        '\n'
        'SETTLED — बहुष्वनियमः: अश्वरथेन्द्राः and इन्द्ररथाश्वाः both\n'
        '  stand, so the rule is for two members and not more.'
    ),
    "2.2.34": (
        (),
        'SETTLED — अल्पाच्तरं शब्दरूपं द्वन्द्वे पूर्वं प्रयोक्तव्यम्:\n'
        '  प्लक्षन्यग्रोधौ, धवखदिरपलाशाः. The last of the three dvandva\n'
        '  rules and the one that decides where the others do not.\n'
        '\n'
        'SETTLED — बहुष्वनियमः again: शङ्खदुन्दुभिवीणाः beside\n'
        '  वीणाशङ्खदुन्दुभयः.\n'
        '\n'
        'SCOPE — ऋतुनक्षत्राणाम् आनुपूर्व्येण समानाक्षराणां पूर्वनिपातो\n'
        '  वक्तव्यः — seasons and asterisms of equal syllables go in their\n'
        '  natural order, हेमन्तशिशिरवसन्ताः, कृत्तिकारोहिण्यौ. Not\n'
        '  modelled: it wants a list of seasons and asterisms in order,\n'
        '  and the gaṇapāṭha has none.'
    ),
    "2.2.35": (
        (),
        'SETTLED — सप्तम्यन्तं विशेषणं च बहुव्रीहिसमासे पूर्वं\n'
        '  प्रयोक्तव्यम्: कण्ठेकालः, उरसिलोमा; and for the qualifier,\n'
        '  चित्रगुः, शबलगुः.\n'
        '\n'
        'SETTLED — why the rule is needed at all: सर्वोपसर्जनत्वाद्\n'
        '  बहुव्रीहेर् अनियमे प्राप्ते नियमार्थं वचनम्. Every member of a\n'
        '  bahuvrīhi is subordinate, so 2.2.30 names them all and settles\n'
        '  nothing.\n'
        '\n'
        'SCOPE — सर्वनामसंख्ययोरुपसंख्यानम् adds pronouns and numerals —\n'
        '  सर्वश्वेतः, द्विशुक्लः — and between those two the numeral\n'
        '  leads परत्वात्. Recorded, not modelled.'
    ),
    "2.2.36": (
        (),
        'SETTLED — निष्ठान्तं बहुव्रीहिसमासे पूर्वं प्रयोक्तव्यम्:\n'
        '  कृतकटः, भिक्षितभिक्षः, अवमुक्तोपानत्कः. Which affixes are\n'
        '  निष्ठा is 1.1.26\'s and is asked.\n'
        '\n'
        'SETTLED — the Kāśikā answers an objection worth keeping: is a\n'
        '  निष्ठा not always the qualifier, so that 2.2.35 covers it?\n'
        '  नैष नियमः — which member qualifies which turns on how it is\n'
        '  meant, विवक्षानिबन्धनत्वात्, and कटे कृतम् अनेन can be read\n'
        '  the other way.\n'
        '\n'
        'SETTLED — निष्ठायाः पूर्वनिपाते जातिकालसुखादिभ्यः परवचनम्: after\n'
        '  a word of kind, of time or of ease the निष्ठा goes SECOND —\n'
        '  शार्ङ्गजग्धी, पलाण्डुभक्षिती, मासजातः. Codified, since it\n'
        '  reverses the rule rather than qualifying it.'
    ),
    "2.2.37": (
        (),
        'SETTLED — निष्ठेति पूर्वनिपाते प्राप्ते विकल्प उच्यते: in this\n'
        '  list 2.2.36 becomes a choice. अग्न्याहितः beside आहिताग्निः,\n'
        '  जातपुत्रः beside पुत्रजातः, तैलपीतः, ऊढभार्यः.\n'
        '\n'
        'SETTLED — आकृतिगणश्चायम्, तेन गडुकण्ठप्रभृतय इहैव द्रष्टव्याः.\n'
        '  The file marks it open too.'
    ),
    "2.2.38": (
        (),
        'SETTLED — गुणशब्दानां विशेषणत्वात् पूर्वनिपाते प्राप्ते विकल्प\n'
        '  उच्यते: these are quality-words, so 2.2.35 would have put them\n'
        '  first as qualifiers, and this makes it a choice.\n'
        '  कडारजैमिनिः beside जैमिनिकडारः.\n'
        '\n'
        'SETTLED — कर्मधारय इति किम्? कडारपुरुषो ग्रामः — outside a\n'
        '  karmadhāraya there is no choice.\n'
        '\n'
        'SETTLED — and this is where प्राक् कडारात् समासः ends. 2.1.3\n'
        '  opened the section by naming everything up to this sūtra, and\n'
        '  the Kāśikā closes the pāda on it.'
    ),
}

for _sutra, (_reuses, _notes) in _ORDER.items():
    register(
        _sutra,
        apply=spoken_first,
        codification=_CODIFICATION,
        notes=_notes,
        reuses=_reuses,
    )


__all__ = ["spoken_first"]
