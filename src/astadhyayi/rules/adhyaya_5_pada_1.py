# -*- coding: utf-8 -*-
"""
अध्याय ५, पाद १ — three headings in thirty sūtras.

छ from 5.1.1, ठञ् from 5.1.18, and ठक् from 5.1.19 inside the ठञ्.
The chapter before had one heading to a pāda; this one opens three
before its thirtieth rule, and the third is bounded by आ rather than
प्राक्, so it takes in the very sūtra that names it.

And the senses change again. अध्याय ४ asked whose descendant a man
was, where a thing came from, what it was made of, what he did by
means of it. Here it is what a thing is GOOD FOR, what it is MADE
FOR, what it might BELONG to, and what it is WORTH — and the base
stands in the dative for the first three and the instrumental for
the last.
"""

from __future__ import annotations

from src.astadhyayi.krita import fit_for
from src.astadhyayi.sources import register

_RULES = {
    '5.1.1': (
        'SETTLED — प्राक्क्रीताच्छः. **तेन क्रीतम् इति वक्ष्यति।\n'
        '  प्रागेतस्मात् क्रीतसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामः,\n'
        '  छप्रत्ययस्तेष्वधिकृतो वेदितव्यः** — छ is the affix for every sense\n'
        '  named from here to the rule that says क्रीत, unless a rule says\n'
        '  otherwise. वत्सेभ्यो हितो **वत्सीयो** गोधुक्, a milkman kept for\n'
        '  the calves; करभीय उष्ट्रः.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI SAYS WHAT A प्राक्-HEADING MEASURES.** The\n'
        '  rule could have been worded *before the ठञ्*, since 5.1.18 is\n'
        '  where छ actually stops. It is not: **अर्थोऽवधित्वेन गृहीतः, न\n'
        '  प्रत्ययः; तेन प्राक् ठञः छ इति नोक्तम्** — the SENSE is taken as\n'
        '  the limit and not the affix. Every one of these headings names a\n'
        '  sense-word, and this is the rule that says why'
    ),
    '5.1.2': (
        'SETTLED — उगवादिभ्यो यत्, the उवर्णान्त half. **प्राक्\n'
        "  क्रीतादित्येव** — the heading's senses are carried, and only the\n"
        '  affix changes. छस्यापवादः. **शङ्कव्यं** दारु, wood for a peg;\n'
        '  पिचव्यः कार्पासः; कमण्डलव्या मृत्तिका\n'
        '\n'
        'SETTLED — उगवादिभ्यो यत्, the गवादि half. **गव्यम्**; हविष्यम्.\n'
        '\n'
        'SETTLED — **AND THREE LATER RULES ARE BEATEN BY AN EARLIER ONE.**\n'
        '  सनङ्गु is a kind of leather, so 5.1.15 चर्मणोऽञ् would take it by\n'
        '  standing later; चरु is an oblation, so 5.1.4 would; सक्तु is a\n'
        '  preparation of grain, so the अन्नविकारेभ्यश्च of the अपूपादि list\n'
        '  would. **तत्र सर्वत्र पूर्वविप्रतिषेधेन यत् प्रत्यय एवेष्यते** —\n'
        '  in every one of the three the EARLIER rule is wanted: सनङ्गव्यं\n'
        '  चर्म, चरव्यास्तण्डुलाः, सक्तव्या धानाः.\n'
        '\n'
        'SETTLED — गो, हविस्, बर्हिस्, खट, अष्टका, युग, मेधा, स्रक्, नाभि,\n'
        '  शुनि, ऊधस्, कूप, उदर, खर, स्खद, अक्षर, विष — गवादिः\n'
        '\n'
        'SETTLED — उगवादिभ्यो यत्, the गवादि entry **नाभि नभं च** (ग०सू०१०८)\n'
        '  — and a गण-entry that does two things at once. **नाभिशब्दो\n'
        '  यत्प्रत्ययमुत्पादयति, नभं चादेशम् आपद्यते**: the word takes यत्\n'
        '  AND becomes नभ. नाभये हितो **नभ्योऽक्षः**, an axle greased for the\n'
        '  nave; नभ्यमञ्जनम्.\n'
        '\n'
        'SETTLED — **AND THE SUBSTITUTION IS TIED TO THE ENTRY, NOT TO THE\n'
        '  WORD.** नाभि is also a part of the body, and as that it is taken\n'
        '  by 5.1.6 शरीरावयवाद् यत् instead — same affix, different rule.\n'
        '  **गवादिषु यता सन्नियुक्तो नभभावोऽत्र न भवति**: the नभ that is\n'
        '  yoked to the गवादि यत् does not happen there, and the form is\n'
        '  नाभये हितं **नाभ्यं** तैलम्. One word, two rules, and only one of\n'
        '  them changes its shape\n'
        '\n'
        'SETTLED — उगवादिभ्यो यत्, the गवादि entry **शुनः संप्रसारणं वा च\n'
        '  दीर्घत्वं तत्सन्नियोगेन चान्तोदात्तत्वम्** (ग०सू०१०९) — श्वन्\n'
        '  takes संप्रसारण, optionally with lengthening, and an end-accent\n'
        '  yoked to it: **शुन्यम्, शून्यम्**.\n'
        '\n'
        'SETTLED — **AND THE च OF THE ENTRY DOES A JOB.** Without it 6.4.144\n'
        '  नस्तद्धिते would drop the न् of शुन् before the taddhita and there\n'
        '  would be no न to lengthen around: **चकारस्यानुक्तसमुच्चयार्थत्वाद्\n'
        '  नस्तद्धिते इति लोपो न स्यात्** — the च gathers in what is not\n'
        '  said, and what it gathers in is the blocking of that elision\n'
        '\n'
        'SETTLED — उगवादिभ्यो यत्, the गवादि entry **ऊधसोऽनङ् च** (ग०सू०११०)\n'
        '  — the same double duty नाभि had, with a different substitute.\n'
        '  **ऊधन्यः**'
    ),
    '5.1.3': (
        'SETTLED — कम्बलाच्च संज्ञायाम्, छस्यापवादः. यत् after कम्बल when the\n'
        '  word is a NAME. **कम्बल्यम्** ऊर्णापलशतम्, a hundred palas of wool\n'
        '  that go to make a blanket — and the name is of that quantity, not\n'
        '  of the wool. संज्ञायामिति किम्? **कम्बलीया ऊर्णा**, wool for a\n'
        "  blanket, which is not a name and so takes the heading's छ"
    ),
    '5.1.4': (
        'SETTLED — विभाषा हविरपूपादिभ्यः, the हविस् half — and it names a\n'
        '  CLASS and not the word. **हविर्विशेषवाचिभ्यः**: from the words\n'
        '  that name particular oblations, optionally यत्. **आमिक्ष्यं दधि,\n'
        '  आमिक्षीयं दधि**; पुरोडाश्यास्तण्डुलाः, पुरोडाशीयाः.\n'
        '\n'
        'SETTLED — **AND THE WORD हविस् ITSELF IS NOT OPTIONAL.**\n'
        '  **हविश्शब्दात्तु गवादिपाठाद् नित्यमेव भवति** — हविस् stands in the\n'
        '  गवादि list of 5.1.2, so it takes यत् always, and only the words\n'
        '  for particular oblations get the choice\n'
        '\n'
        'SETTLED — विभाषा हविरपूपादिभ्यः, the अपूपादि half. **अपूप्यम्,\n'
        '  अपूपीयम्**; तण्डुल्यम्, तण्डुलीयम्. अपूप, तण्डुल, अभ्यूष, पृथुक,\n'
        '  अर्गल, मुसल, सूप, कटक, कर्णवेष्टक, किण्व, **अन्नविकारेभ्यश्च**\n'
        '  (ग०सू०१११), पूप, स्थूणा, पीप, अश्व, पत्र — अपूपादिः. The last of\n'
        '  the fourteen is not a word but a class: anything that is a\n'
        '  PREPARATION OF FOOD joins the list'
    ),
    '5.1.5': (
        'SETTLED — तस्मै हितम्. **तस्मा इति चतुर्थीसमर्थाद् हितम्\n'
        '  इत्येतस्मिन्नर्थे यथाविहितं प्रत्ययो भवति** — from a base in the\n'
        '  DATIVE, in the sense *good for that*, the affix as already\n'
        '  enjoined. वत्सेभ्यो हितो गोधुक् **वत्सीयः**; पटव्यम्; गव्यम्;\n'
        '  हविष्यम्; अपूप्यम्, अपूपीयम्.\n'
        '\n'
        'SETTLED — **यथाविहितम् IS A FALL-THROUGH, AND THE RESOLVER EXECUTES\n'
        '  IT AS ONE.** The rule gives no affix of its own; it names a sense\n'
        '  and sends the question back to whatever rule the base itself\n'
        '  answers to — छ by the heading, यत् by 5.1.2, either by 5.1.4. The\n'
        '  same device 4.3.25 used, and asking under this sense asks again\n'
        '  without it.\n'
        '\n'
        'SETTLED — **AND THIS IS THE SŪTRA THAT BOUNDED यत्.** 4.4.75\n'
        '  प्राग्घिताद् यत् lifted the word हित out of THIS rule to fix its\n'
        '  own limit, two pādas back and a chapter away. The debt that named\n'
        '  it is paid here'
    ),
    '5.1.6': (
        'SETTLED — शरीरावयवाद् यत्, छस्यापवादः. **शरीरं प्राणिकायः** — a body\n'
        "  is a living creature's frame, and from the words that name a PART\n"
        '  of one, यत्. **दन्त्यम्**, good for the teeth; कण्ठ्यम्, ओष्ठ्यम्,\n'
        '  नाभ्यम्, नस्यम्. A rule that names no word and no list, only what\n'
        '  the word must mean'
    ),
    '5.1.7': (
        'SETTLED — खलयवमाषतिलवृषब्रह्मणश्च, छस्यापवादः. खलाय हितं **खल्यम्**;\n'
        '  यव्यम्, माष्यम्, तिल्यम्, वृष्यम्, ब्रह्मण्यम्.\n'
        '\n'
        'SETTLED — **AND TWO OF THE SIX ARE NOT WHAT THEY LOOK LIKE.** वृष्णे\n'
        '  हितम् and ब्राह्मणेभ्यो हितम् — for the BULL, for the BRĀHMAṆAS —\n'
        '  do not take this affix at all: **वाक्यमेव भवति; छप्रत्ययोऽपि न\n'
        "  भवति, अनभिधानात्**, the phrase stands, and not even the heading's\n"
        '  छ comes, because the language does not say it that way. So वृष is\n'
        '  the plant and ब्रह्मन् the sacred word, not the animal and not the\n'
        '  priest.\n'
        '\n'
        'SETTLED — **चकारोऽनुक्तसमुच्चयार्थः** — and the च gathers in what is\n'
        '  not listed: रथाय हिता **रथ्या**'
    ),
    '5.1.8': (
        'SETTLED — अजाविभ्यां थ्यन्, छस्यापवादः. **अजथ्या** यूथिः, a herd\n'
        '  kept for the goats; अविथ्या'
    ),
    '5.1.9': (
        'SETTLED — आत्मन्विश्वजनभोगोत्तरपदात् खः, छस्यापवादः; the named-word\n'
        '  half. आत्मने हितम् **आत्मनीनम्**; विश्वजनेभ्यो हितं\n'
        '  **विश्वजनीनम्**.\n'
        '\n'
        'SETTLED — **AND THE RULE SPELLS आत्मन् OUT TO TEACH ITS OWN SCOPE.**\n'
        '  6.4.134 would drop that न्, so the rule could have said आत्म; it\n'
        '  does not: **आत्मन्निति नलोपो न कृतः प्रकृतिपरिमाणज्ञापनार्थम्** —\n'
        '  the elision is left undone to show how much of the word is meant.\n'
        '  **तेनोत्तरपदग्रहणं भोगशब्देनैव संबध्यते, न तु प्रत्येकम्**: the\n'
        '  word उत्तरपद goes with भोग ALONE and not with all three, so आत्मन्\n'
        '  and विश्वजन are taken whole and not as compound-ends. (6.4.169\n'
        '  आत्माध्वानौ खे then keeps आत्मन् unchanged before this very\n'
        '  affix.)\n'
        '\n'
        'SETTLED — **AND ONLY ONE KIND OF COMPOUND QUALIFIES.**\n'
        '  **कर्मधारयादेवेष्यते; षष्ठीसमासाद् बहुव्रीहेश्च छ एव भवति** — from\n'
        '  a कर्मधारय, ख; from a genitive तत्पुरुष or a बहुव्रीहि, the\n'
        "  heading's छ: विश्वजनाय हितं **विश्वजनीयम्**\n"
        '\n'
        'SETTLED — आत्मन्विश्वजनभोगोत्तरपदात् खः, the भोगोत्तरपद half — and\n'
        '  here the word भोग means the BODY. **मातृभोगीणः**, पितृभोगीणः.\n'
        '\n'
        'SETTLED — **AND THE COMPOUND IS REQUIRED, NOT INCIDENTAL.**\n'
        '  **केवलेभ्यो मात्रादिभ्यश्छ एव भवति** — from मातृ and पितृ alone it\n'
        "  is the heading's छ: मात्रीयम्, पित्रीयम्. Two vārttikas press the\n"
        '  point: **राजाचार्याभ्यां तु नित्यम्** — with राजन् and आचार्य the\n'
        '  compound is obligatory, **भोगोत्तरपदाभ्यामेव खः प्रत्यय इष्यते, न\n'
        '  केवलाभ्याम्**, and **केवलाभ्यां वाक्यमेव भवति**: alone they take\n'
        '  no affix whatever, only the phrase राज्ञे हितम्. राजभोगीनः; and\n'
        '  **आचार्यादणत्वं च** adds a vowel-strengthening — आचार्यभोगीनः\n'
        '\n'
        'SETTLED — आत्मन्विश्वजनभोगोत्तरपदात् खः — **पञ्चजनाद् उपसंख्यानम्**,\n'
        '  a vārttika adding a fourth base. **पञ्चजनीनम्**, and **अत्रापि\n'
        '  कर्मधारयादिष्यते**: here too only from a कर्मधारय, **अन्यत्र\n'
        '  पञ्चजनीयम्**\n'
        '\n'
        'SETTLED — आत्मन्विश्वजनभोगोत्तरपदात् खः — **सर्वजनाट् ठञ् खश् च**, a\n'
        '  vārttika giving TWO affixes where the sūtra gives one.\n'
        '  **सार्वजनिकम्, सर्वजनीनम्**; and the same restriction, **अत्रापि\n'
        '  कर्मधारयादेव — सर्वजनीयमन्यत्र**\n'
        '\n'
        'SETTLED — आत्मन्विश्वजनभोगोत्तरपदात् खः — **महाजनाद् नित्यं ठञ्\n'
        '  वक्तव्यः**, and this one gives ठञ् ALONE where the rule before it\n'
        '  gave both. महाजनाय हितं **माहाजनिकम्**, and **तत्पुरुषादेव** —\n'
        '  from a तत्पुरुष only, where the others wanted a कर्मधारय.\n'
        '  **बहुव्रीहेस्तु छ एव भवति**: महाजनीयम्. Four vārttikas on one\n'
        '  sūtra, and each names a different compound'
    ),
    '5.1.10': (
        'SETTLED — सर्वपुरुषाभ्यां णढञौ, छस्यापवादः; the सर्व member.\n'
        '  **यथासंख्यम्** — the two affixes are matched to the two bases in\n'
        '  order, so सर्व takes ण and पुरुष ढञ्. सर्वस्मै हितं **सार्वम्**.\n'
        '  **सर्वाद् णस्य वा वचनम्**: a vārttika makes it optional — सर्वीयम्\n'
        '\n'
        'SETTLED — सर्वपुरुषाभ्यां णढञौ, the पुरुष member. **पौरुषेयम्**.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA GIVES THE SAME AFFIX FOUR MORE SENSES.**\n'
        '  **पुरुषाद् वधविकारसमूहतेनकृतेष्विति वक्तव्यम्** — a killing, an\n'
        '  alteration, a group, and a thing MADE BY: पौरुषेयो वधः, पौरुषेयो\n'
        '  विकारः, पौरुषेयः समूहः, and पौरुषेयो ग्रन्थः, a book made by a\n'
        '  man. One form for five senses'
    ),
    '5.1.11': (
        'SETTLED — माणवचरकाभ्यां खञ्, छस्यापवादः. माणवाय हितं **माणवीनम्**;\n'
        '  चारकीणम्'
    ),
    '5.1.12': (
        'SETTLED — तदर्थं विकृतेः प्रकृतौ. **प्रकृतिरुपादानकारणम्, तस्यैव\n'
        '  उत्तरमवस्थान्तरं विकृतिः** — the प्रकृति is the material a thing\n'
        '  is made OF, the विकृति the later state of that same material. From\n'
        '  the word for the FINISHED thing, in the sense of the MATERIAL:\n'
        '  अङ्गारेभ्यो हितानि काष्ठानि **अङ्गारीयाणि काष्ठानि**, wood for\n'
        '  charcoal; प्राकारीया इष्टकाः; शङ्कव्यं दारु.\n'
        '\n'
        'SETTLED — **AND तदर्थम् IS WHAT KEEPS IT FROM BEING MERE SEQUENCE.**\n'
        '  **तदर्थग्रहणेन प्रकृतेरनन्यार्थताख्यायते; न प्रकृतिविकारसंभवमात्रे\n'
        '  प्रत्ययः** — the material must be FOR nothing else. यवानां धानाः,\n'
        '  धानानां सक्तवः take nothing: barley does become groats and groats\n'
        '  do become meal, but there **प्रकृत्यन्तरनिवृत्तिर्विवक्षिता न\n'
        '  तादर्थ्यम्**, what is meant is *from THIS grain and not another*,\n'
        '  not purpose.\n'
        '\n'
        'SETTLED — **AND EACH OF THE THREE WORDS IS TESTED.** विकृतेरिति\n'
        '  किम्? **उदकार्थः कूपः** — a well is where water comes to be, so a\n'
        "  well is water's source, **न तूदकं तस्य विकृतिः, अत्यन्तभेदात्**,\n"
        "  but water is not the well's later state, the two being altogether\n"
        '  different things. प्रकृताविति किम्? **अस्यर्था कोशी** — a scabbard\n'
        '  is for a sword, and a sword IS a modification of iron, but the\n'
        '  scabbard is not what the sword was made of.\n'
        '\n'
        'SETTLED — The affix is यथाविहितम् again, and the dative comes not\n'
        '  from the rule but from the sense: **प्रत्ययार्थस्य च तदर्थत्वे सति\n'
        '  सामर्थ्याल् लभ्या चतुर्थी समर्थविभक्तिः**. **केचित् तु तस्मै हितम्\n'
        '  इत्यनुवर्तयन्ति** — and some carry 5.1.5 down instead'
    ),
    '5.1.13': (
        'SETTLED — छदिरुपधिबलेर्ढञ्, छस्यापवादः. **छादिषेयाणि तृणानि**, grass\n'
        '  for a roof; औपधेयं दारु; बालेयास्तण्डुलाः.\n'
        '\n'
        'SETTLED — **AND ONE OF THE THREE ALREADY CARRIES AN AFFIX.**\n'
        '  **उपधीयत इत्युपधिः रथाङ्गम्** — an उपधि is a part of a chariot,\n'
        '  named from being laid on, and **उपधिशब्दात् स्वार्थे प्रत्ययः**:\n'
        '  the affix here is in its OWN sense, so **औपधेयमपि तदेव दारु**\n'
        '  means the same wood over again'
    ),
    '5.1.14': (
        'SETTLED — ऋषभोपानहोर्ञ्यः, छस्यापवादः. **आर्षभ्यो वत्सः**, a calf to\n'
        '  become a bull; औपानह्यो मुञ्जः, grass for a shoe.\n'
        '\n'
        'SETTLED — **AND IT BEATS THE RULE THAT STANDS AFTER IT.** 5.1.15\n'
        '  चर्मणोऽञ् would take leather made into shoes by standing later; it\n'
        '  does not: **चर्मण्यपि प्रकृतित्वेन विवक्षिते पूर्वविप्रतिषेधाद्\n'
        '  अयमेव इष्यते** — even where the material meant is leather, THIS\n'
        '  rule is wanted by पूर्वविप्रतिषेध. **औपानह्यं चर्म**'
    ),
    '5.1.15': (
        'SETTLED — चर्मणोऽञ्, छस्यापवादः — and the genitive in the sūtra is\n'
        "  doing something the other rules' ablatives do not. **चर्मण इति\n"
        '  षष्ठी; चर्मणो या विकृतिः तद्वाचिनः प्रातिपदिकाद् अञ्**: the affix\n'
        '  comes not after the word चर्मन् but after the word for WHATEVER IS\n'
        "  MADE of leather. **वार्ध्रं चर्म**, वारत्रं चर्म — a strap's\n"
        "  leather, a thong's"
    ),
    '5.1.16': (
        'SETTLED — तदस्य तदस्मिन् स्यादिति. **तदिति प्रथमा समर्थविभक्तिः,\n'
        '  अस्येति प्रत्ययार्थः, स्यादिति प्रकृतिविशेषणम्** — the base stands\n'
        '  in the NOMINATIVE, and the affix reports *this would be OF that*\n'
        '  or *would be IN that*. प्राकार आसाम् इष्टकानां स्यात् **प्राकारीया\n'
        '  इष्टकाः**, bricks that might make a rampart; प्रासादीयं दारु;\n'
        '  प्राकारोऽस्मिन् देशे स्यात् **प्राकारीयो देशः**.\n'
        '\n'
        'SETTLED — **AND स्यात् IS A REAL OPTATIVE, NOT A FIGURE.**\n'
        '  **स्यादिति संभावनायां लिङ्, संभावनेऽलमिति चेत् इत्यादिना**\n'
        '  (3.3.154) — the mood is the one for what might be, and what makes\n'
        '  it likely is stated each time: **इष्टकानां बहुत्वेन तत्\n'
        '  संभाव्यते**, by the sheer number of the bricks; **देशस्य च\n'
        '  गुणेन**, by the quality of the ground.\n'
        '\n'
        'SETTLED — **AND इति IS THE WORD THAT KEEPS THE RULE HONEST.**\n'
        '  **इतिकरणो विवक्षार्थः** — it marks what the speaker MEANS to say.\n'
        '  Otherwise प्रासादो देवदत्तस्य स्यात्, *Devadatta could come by a\n'
        '  palace*, would take the affix too, and it does not.\n'
        '\n'
        'SETTLED — **AND THE DOUBLED तद् IS A LESSON IN METHOD.**\n'
        '  **द्विस्तद्ग्रहणं न्यायप्रदर्शनार्थम् — अनेकस्मिन् प्रत्ययार्थे\n'
        '  प्रत्येकं समर्थविभक्तिः संबन्धनीया**: when one rule states several\n'
        '  senses, the case-relation must be joined to EACH of them\n'
        '  separately, and saying तद् twice shows how.\n'
        '  **प्रकृतिविकारभावस्तादर्थ्यं चेह न विवक्षितम्; किं तर्हि?\n'
        '  योग्यतामात्रम्** — neither material nor purpose is meant here,\n'
        '  only fitness, **तेन पूर्वस्यायमविषयः**'
    ),
    '5.1.17': (
        'SETTLED — परिखाया ढञ्, छस्यापवादः. **पारिखेयी भूमिः**, ground where\n'
        '  a moat might go.\n'
        '\n'
        'SETTLED — **AND THE HEADING CLOSES HERE, IN THE WORDS THE PĀDA\n'
        '  BEFORE USED TWICE.** **छयतोः पूर्णोऽवधिः। इतः परमन्यः प्रत्ययो\n'
        '  विधीयते** — the limit of छ and of यत् both is complete, and from\n'
        '  here another affix is enjoined. 4.4.74 said it of ठक् and 4.4.144\n'
        "  of यत्, word for word. So छ's marker is 5.1.37, twenty sūtras\n"
        '  further on, and its last rule is this one, because 5.1.18 opens\n'
        '  ठञ् inside the range'
    ),
    '5.1.18': (
        'SETTLED — प्राग्वतेष्ठञ्. **तेन तुल्यं क्रिया चेद् वतिरिति वक्ष्यति।\n'
        '  प्रागेतस्माद् वतिसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामः, ठञ्\n'
        '  प्रत्ययस्तेष्वधिकृतो वेदितव्यः** — ठञ् is the affix from here to\n'
        '  the rule that says वति, 5.1.115. **पारायणिकः, तौरायणिकः,\n'
        '  चान्द्रायणिकः** (5.1.72).\n'
        '\n'
        "SETTLED — **AND THIS IS WHAT 4.3.156 WAS WAITING FOR.** That rule's\n"
        '  अतिदेश pointed forward out of its own pāda to this heading; the\n'
        '  debt was written as a test asserting this sūtra was ABSENT, and it\n'
        '  comes due here. The fourth of the great प्राक्-headings, and the\n'
        '  second one this chapter opens'
    ),
    '5.1.19': (
        'SETTLED — आर्हादगोपुच्छसंख्यापरिमाणाट्ठक्. **तदर्हतीति वक्ष्यति। आ\n'
        '  एतस्माद् अर्हसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामः, ठक्\n'
        '  प्रत्ययस्तेष्वधिकृतो वेदितव्यो गोपुच्छादीन् वर्जयित्वा** — ठक् for\n'
        '  every sense named from here to 5.1.63, the three excepted bases\n'
        '  aside. **ठञधिकारमध्ये तदपवादः ठग् विधीयते**: a heading enjoined\n'
        '  INSIDE another heading, as its exception. तेन क्रीतं\n'
        '  **नैष्किकम्**, पाणिकम्.\n'
        '\n'
        'SETTLED — **AND THE आ IS NOT प्राक्.** **अभिविधावयमाकारः,\n'
        '  तेनार्हत्यर्थेऽपि ठग् भवत्येव** — this आ is an अभिविधि, an\n'
        '  inclusive limit, so ठक् applies in the sense of अर्हति TOO. Every\n'
        '  other great heading stops SHORT of the sūtra that names it; this\n'
        '  one reaches that sūtra and takes it in.\n'
        '\n'
        'SETTLED — **AND THE THREE EXCEPTIONS NEED FOUR TERMS TO SEPARATE.**\n'
        '  गोपुच्छेन क्रीतं **गौपुच्छिकम्**, षाष्टिकम् for a numeral,\n'
        '  प्रास्थिकम् and कौडविकम् for a measure — all ठञ् by the heading\n'
        '  above. And संख्यापरिमाणयोः को विशेषः? **भेदगणनं संख्या एकत्वादिः;\n'
        '  गुरुत्वमानमुन्मानं पलादि; आयाममानं प्रमाणं वितस्त्यादि;\n'
        '  आरोहपरिणाहमानं परिमाणं प्रस्थादि** — counting, weight, length, and\n'
        '  girth, of which the rule excepts the first and the last and leaves\n'
        '  the middle two inside'
    ),
    '5.1.20': (
        'SETTLED — असमासे निष्कादिभ्यः, ठञोऽपवादः. **आर्हादित्येव** — the\n'
        '  आर्हीय senses are carried. **नैष्किकम्**, पाणिकम्, पादिकम्,\n'
        '  माषिकम्. निष्क, पण, पाद, माष, वाह, द्रोण, षष्टि — निष्कादिः.\n'
        '\n'
        'SETTLED — **असमास इति किम्?** द्विनैष्किकम्, त्रिनैष्किकम् — in a\n'
        "  compound it is the heading's ठञ् instead, and 7.3.17 then\n"
        '  strengthens the LATTER member.\n'
        '\n'
        'SETTLED — **AND THE WORD असमासे IS A ज्ञापक FOR THE WHOLE HEADING.**\n'
        '  It should be needless, since **ग्रहणवता प्रातिपदिकेन तदन्तविधिः\n'
        '  प्रतिषिध्यते** — a rule naming a word does not reach compounds\n'
        '  ending in it. That it is said anyway tells you the opposite holds\n'
        '  elsewhere: **निष्कादिष्वसमासग्रहणं ज्ञापकं पूर्वत्र\n'
        '  तदन्ताप्रतिषेधस्य**. So गव्यम् and सुगव्यम् and अतिसुगव्यम् by\n'
        '  5.1.2; यवापूप्यम् by 5.1.4; राजदन्त्यम् by 5.1.6 — all of them\n'
        '  compounds, all of them taken.\n'
        '\n'
        'SETTLED — **AND FROM HERE ON IT HOLDS ONLY OF NUMERALS, AND ONLY\n'
        '  WITHOUT ELISION.** **प्राग् वतेः संख्यापूर्वपदानां\n'
        '  तदन्तग्रहणमलुकि** (वा० ५.१.२०): द्वैपारायणिकः, त्रैपारायणिकः. But\n'
        '  द्विशूर्पेण क्रीतम् is **द्विशौर्पिकम्** and not by 5.1.26,\n'
        '  because द्विशूर्पम् already had its affix removed —\n'
        '  **लुगन्तायास्तु प्रकृतेर्नेष्यते**'
    ),
    '5.1.21': (
        'SETTLED — शताच्च ठन्यतावशते, कनोऽपवादः — and the exception is of the\n'
        '  NEXT rule, not of the heading, since शत is a numeral and 5.1.22\n'
        '  would take it. शतेन क्रीतं **शतिकम्, शत्यम्**.\n'
        '\n'
        'SETTLED — **अशत इति किम्?** शतं परिमाणमस्य **शतकं** निदानम् — where\n'
        '  the thing meant IS the hundred, the affix is refused, because\n'
        '  **प्रत्ययार्थोऽत्र संघः शतमेव वस्तुतः प्रकृत्यर्थाद् न भिद्यते**:\n'
        '  what the affix would report does not differ from what the base\n'
        '  already says.\n'
        '\n'
        'SETTLED — **AND THE TEST IS WHETHER THE WORD ITSELF SAYS IT.** शतेन\n'
        '  क्रीतं **शत्यं शाटकशतम्** is allowed, though a hundred is meant\n'
        '  twice over — **वाक्येन ह्यत्र प्रत्ययार्थस्य तत्त्वं गम्यते, न\n'
        '  श्रुत्या**, the identity is got from the SENTENCE and not from the\n'
        "  word's own sound. **शतप्रतिषेधेऽन्यशतत्वेऽप्रतिषेधः** (वा०\n"
        '  ५.१.२१): the refusal does not apply when it is a different\n'
        '  hundred.\n'
        '\n'
        'SETTLED — **चकारोऽसमास इत्यनुकर्षणार्थः** — and the च drags असमासे\n'
        '  down from the rule before, though the vārttika at 5.1.20 lets a\n'
        '  numeral-compound in anyway: द्विशतेन क्रीतं द्विशतकम्, त्रिशतकम्'
    ),
    '5.1.22': (
        'SETTLED — संख्याया अतिशदन्तायाः कन्, ठञोऽपवादः. From a NUMERAL — but\n'
        '  not from ति, and not from one ending in शद्. पञ्चभिः क्रीतः\n'
        '  **पञ्चकः** पटः; बहुकः, गणकः.\n'
        '\n'
        'SETTLED — **अतिशदन्ताया इति किम्?** साप्ततिकम्, चात्वारिंशत्कम् —\n'
        '  seventy ends in ति and forty in शद्, so both fall back on the\n'
        "  heading's ठञ्.\n"
        '\n'
        'SETTLED — **AND THE ति EXCEPTED IS A MEANINGFUL ONE.**\n'
        '  **अर्थवतस्तिशब्दस्य ग्रहणाद् डतेः पर्युदासो न भवति** — the\n'
        '  exclusion takes the ति that MEANS something, so the डति of कति is\n'
        '  untouched: **कतिकः**'
    ),
    '5.1.23': (
        'SETTLED — वतोरिड्वा — and the rule adds nothing but an आगम.\n'
        '  **वत्वन्तस्य संख्यात्वात् कन् सिद्ध एव, तस्य त्वनेन वा इडागमो\n'
        '  विधीयते**: a word ending in वतु is already a numeral, so 5.1.22\n'
        '  gives it कन् without help; all this rule does is put इट् before\n'
        '  that कन्, optionally. **तावतिकः, तावत्कः**; यावतिकः, यावत्कः'
    ),
    '5.1.24': (
        'SETTLED — विंशतित्रिंशद्भ्यां ड्वुन्नसंज्ञायाम्. **विंशकः,\n'
        '  त्रिंशकः** — and 6.4.142 ति विंशतेर्डिति drops the ति of विंशति\n'
        '  before this ड-marked affix, which is what the ड is for.\n'
        '\n'
        'SETTLED — **असंज्ञायामिति किम्?** विंशतिकम्, त्रिंशत्कम्.\n'
        '\n'
        'SETTLED — **AND THAT COUNTER-EXAMPLE RAISES A PROBLEM THE VṚTTI\n'
        '  SOLVES BY SPLITTING THE RULE.** How can कन् come there at all,\n'
        '  when 5.1.22 excepts what ends in ति and in शद्, and these two do?\n'
        '  **योगविभागः करिष्यते — विंशतित्रिंशद्भ्यां कन् प्रत्ययो भवति, ततो\n'
        '  ड्वुन्नसंज्ञायाम् इति**: the rule is read as two, the first\n'
        '  restoring कन् to just these two words against the exception, the\n'
        '  second giving ड्वुन् where they are not names'
    ),
    '5.1.25': (
        "SETTLED — कंसाट्टिठन्, ठञोऽपवादः — and every letter of the affix's\n"
        '  name is accounted for. **टकारो ङीबर्थः** — the ट makes the\n'
        '  feminine take ङीप् (4.1.15); **इकार उच्चारणार्थः** — the इ is only\n'
        '  so the thing can be pronounced; **नकारः स्वरार्थः** — the न is for\n'
        '  the accent. **कंसिकः, कंसिकी**.\n'
        '\n'
        'SETTLED — Three vārttikas add bases: **अर्धाच्चेति वक्तव्यम्** —\n'
        '  अर्धिकः, अर्धिकी; **कार्षापणाट् टिठन् वक्तव्यः** — कार्षापणिकः,\n'
        '  कार्षापणिकी; and **प्रतिशब्दश्चास्यादेशो वा वक्तव्यः**, which lets\n'
        '  प्रति stand in for कार्षापण: **प्रतिकः, प्रतिकी**\n'
        '\n'
        'SETTLED — कंसाट्टिठन् — the vārttika base कार्षापण, held apart\n'
        '  because it carries a substitution the others do not.\n'
        '  **कार्षापणिकः**, and optionally **प्रतिकः** by\n'
        '  प्रतिशब्दश्चास्यादेशो वा. The substitute matters again at 5.1.29,\n'
        '  where the elision is optional and this replacement is optional\n'
        '  inside the non-eliding half'
    ),
    '5.1.26': (
        'SETTLED — शूर्पादञन्यतरस्याम्, ठञोऽपवादः — and an अपवाद that leaves\n'
        '  its own exception standing. **पक्षे सोऽपि भवति**: in the other\n'
        '  alternative the ठञ् comes too. शूर्पेण क्रीतं **शौर्पम्,\n'
        '  शौर्पिकम्**'
    ),
    '5.1.27': (
        'SETTLED — शतमानविंशतिकसहस्रवसनादण् — and this one displaces BOTH the\n'
        '  heading above it and the heading it stands under:\n'
        '  **ठक्ठञोरपवादः**. शतमानेन क्रीतं **शातमानं** शतम्; वैंशतिकम्,\n'
        '  साहस्रम्, वासनम्'
    ),
    '5.1.28': (
        'SETTLED — अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्, the अध्यर्धपूर्व half.\n'
        '  **आर्हादित्येव** — and what is removed is the आर्हीय affix,\n'
        '  whichever of them came. **अध्यर्धकंसम्, अध्यर्धशूर्पम्**.\n'
        '\n'
        'SETTLED — **असंज्ञायामिति किम्?** पाञ्चलोहितिकम्, पाञ्चकलापिकम् —\n'
        '  and the word असंज्ञा qualifies the DERIVED form and not the base:\n'
        '  **प्रत्ययान्तस्य विशेषणमसंज्ञाग्रहणम्, न चेत् प्रत्ययान्तं\n'
        '  संज्ञेति**.\n'
        '\n'
        'SETTLED — **AND अध्यर्ध IS NAMED SEPARATELY THOUGH IT IS A NUMERAL\n'
        '  ALREADY.** Why? **ज्ञापकार्थम्, क्वचिदस्य संख्याकार्यं न भवति** —\n'
        '  to let you know that somewhere it does NOT act as one, and 5.4.17\n'
        '  is where\n'
        '\n'
        'SETTLED — अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्, the द्विगु half.\n'
        '  **द्विकंसम्, त्रिकंसम्; द्विशूर्पम्, त्रिशूर्पम्**. And this is\n'
        "  the elision 5.1.20's vārttika excepts: once it has run, a rule\n"
        '  naming शूर्प no longer reaches द्विशूर्प, **लुगन्तायास्तु\n'
        '  प्रकृतेर्नेष्यते**'
    ),
    '5.1.29': (
        'SETTLED — विभाषा कार्षापणसहस्राभ्याम् — and it does not add an\n'
        '  elision, it loosens one. **पूर्वेण लुकि नित्ये प्राप्ते\n'
        '  विकल्प्यते**: the rule before made it obligatory, and here it\n'
        '  becomes a choice. **अध्यर्धकार्षापणम्, अध्यर्धकार्षापणिकम्**;\n'
        '  द्विकार्षापणम्, द्विकार्षापणिकम्.\n'
        '\n'
        'SETTLED — **AND THE OPTION IS DOUBLE.** **औपसंख्यानिकस्य टिठनो लुक्;\n'
        '  अलुक्पक्षे च प्रतिरादेशो विकल्पितः** — the टिठन् that a vārttika\n'
        '  gave at 5.1.25 is what drops, and in the non-dropping alternative\n'
        '  the प्रति-substitution is itself optional: अध्यर्धप्रतिकम्,\n'
        '  द्विप्रतिकम्.\n'
        '\n'
        'SETTLED — सहस्रात् — **अध्यर्धसहस्रम्, अध्यर्धसाहस्रम्**, and in the\n'
        '  non-eliding half 7.3.15 strengthens the latter member.\n'
        '  **सुवर्णशतमानयोरुपसंख्यानम्** adds two more: अध्यर्धसुवर्णम्,\n'
        '  अध्यर्धसौवर्णिकम्; अध्यर्धशतमानम्, अध्यर्धशातमानम्'
    ),
    '5.1.30': (
        'SETTLED — द्वित्रिपूर्वान्निष्कात्. **द्विगोरित्येव** — only from a\n'
        '  द्विगु, and only one whose first member is two or three.\n'
        '  **द्विनिष्कम्, द्विनैष्किकम्**; त्रिनिष्कम्, त्रिनैष्किकम्.\n'
        '  **बहुपूर्वाच्चेति वक्तव्यम्**: and बहु as well — बहुनिष्कम्,\n'
        '  बहुनैष्किकम्, where 7.3.17 gives the vṛddhi in the non-eliding\n'
        '  half'
    ),
    '5.1.31': (
        'SETTLED — बिस्ताच्च. **द्वित्रिपूर्वादिति चकारेणानुकृष्यते** — the च\n'
        '  drags द्वित्रिपूर्व down from the rule before, so this is the same\n'
        '  option over a different word. **द्विबिस्तम्, द्विबैस्तिकम्**;\n'
        '  त्रिबिस्तम्, त्रिबैस्तिकम्; बहुबिस्तम्, बहुबैस्तिकम्'
    ),
    '5.1.32': (
        'SETTLED — विंशतिकात् खः. From a compound beginning with अध्यर्ध or a\n'
        '  द्विगु and ENDING in विंशतिक. **अध्यर्धविंशतिकीनम्,\n'
        '  द्विविंशतिकीनम्**. **AND THE AFFIX SURVIVES THE ELISION THAT WOULD\n'
        '  HAVE TAKEN IT.** 5.1.28 removes the आर्हीय affix after exactly\n'
        '  these compounds, and this one is given after them too — so it\n'
        '  would be removed the moment it arrived. **विधानसामर्थ्यादस्य लुङ्\n'
        '  न भवति**: the sheer force of its being enjoined here keeps it. An\n'
        '  argument the pāda will use twice more'
    ),
    '5.1.33': (
        'SETTLED — खार्या ईकन्. **अध्यर्धखारीकम्, द्विखारीकम्**, and two\n'
        '  vārttikas widen it in both directions: **केवलायाश्चेति वक्तव्यम्**\n'
        '  — from the bare word too, खारीकम्; **काकिण्याश्चोपसंख्यानम्** —\n'
        '  and from काकिणी, अध्यर्धकाकिणीकम्, द्विकाकिणीकम्, and\n'
        '  **केवलायाश्च**, काकिणीकम्'
    ),
    '5.1.34': (
        'SETTLED — पणपादमाषशताद् यत्. **अध्यर्धपण्यम्, द्विपण्यम्**;\n'
        '  अध्यर्धमाष्यम्; अध्यर्धशत्यम्. **AND पाद KEEPS ITS SHAPE HERE\n'
        '  BECAUSE IT IS A MEASURE AND NOT A FOOT.** 6.3.53 पद्यत्यतदर्थे\n'
        '  would turn पाद into पद् before a य-affix; it does not —\n'
        '  **प्राण्यङ्गस्य स इष्यते, इदं तु परिमाणम्**, that substitution is\n'
        '  wanted for the limb of a living thing, and this is a unit of\n'
        '  measure. **अध्यर्धपाद्यम्**, not अध्यर्धपद्यम्'
    ),
    '5.1.35': (
        'SETTLED — शाणाद् वा, ठञोऽपवादः — and the alternative is not silence.\n'
        '  **पक्षे सोऽपि भवति, तस्य च लुक्**: in the other half the ठञ् comes\n'
        '  and is then removed by 5.1.28, so both members of the option are\n'
        '  visible. **अध्यर्धशाण्यम्, अध्यर्धशाणम्**; द्विशाण्यम्, द्विशाणम्.\n'
        '  **शताच्चेति वक्तव्यम्** adds शत: अध्यर्धशत्यम्, अध्यर्धशतम्'
    ),
    '5.1.36': (
        'SETTLED — द्वित्रिपूर्वाद् अण् च. **शाणाद् वेत्येव** — and the च\n'
        '  brings the यत् of the rule before along, so THREE forms stand\n'
        '  together: **तेन त्रैरूप्यं संपद्यते** — द्वैशाणम्, द्विशाण्यम्,\n'
        '  द्विशाणम्; त्रैशाणम्, त्रिशाण्यम्, त्रिशाणम्. And 7.3.17 names शाण\n'
        '  in its own exclusion, **परिमाणान्तस्यासंज्ञाशाणयोः**, so the\n'
        '  strengthening falls on the FIRST syllable and not the last:\n'
        '  **आदिवृद्धिरेव भवति**'
    ),
    '5.1.37': (
        'SETTLED — तेन क्रीतम् — and the vṛtti here states the architecture\n'
        '  of the whole section. **ठञादयस्त्रयोदश प्रत्ययाः प्रकृताः।\n'
        '  तेषामितः प्रभृति समर्थविभक्तयः प्रत्ययार्थाश्च निर्दिश्यन्ते**:\n'
        '  thirteen affixes have been given from 5.1.18 on, and FROM HERE\n'
        '  what is stated is the case each takes and the sense each serves.\n'
        '  Two halves — which affix, then in what sense — and the table is\n'
        '  built the way the vṛtti divides it. सप्तत्या क्रीतं\n'
        '  **साप्ततिकम्**; नैष्किकम्, पाणिकम्, शत्यम्, द्विकम्. **AND THE\n'
        '  INSTRUMENTAL IS THE PRICE AND NOT THE BUYER.** **तेनेति मूल्यात्\n'
        '  करणे तृतीया समर्थविभक्तिः; अन्यत्रानभिधानाद् न भवति** — देवदत्तेन\n'
        '  क्रीतम् takes nothing, and neither does पाणिना क्रीतम्, *bought\n'
        '  with the hand*. **AND THE NUMBER OF THE BASE MATTERS, UNTIL IT\n'
        '  DOES NOT.** प्रस्थाभ्यां क्रीतम् and प्रस्थैः क्रीतम् take\n'
        '  nothing, **अनभिधानादेव**. But **यत्र तु प्रकृत्यर्थस्य\n'
        '  संख्याभेदावगमे प्रमाणमस्ति तत्र द्विवचनबहुवचनान्तादपि प्रत्ययो\n'
        '  भवति**: where the plurality is itself the point, the affix comes —\n'
        '  द्वाभ्यां क्रीतं **द्विकम्**, and मुद्गैः क्रीतं **मोद्गिकम्**,\n'
        '  because **न ह्येकेन मुद्गेन क्रयः संभवति**, nobody buys anything\n'
        '  with a single bean'
    ),
    '5.1.38': (
        'SETTLED — तस्य निमित्तं संयोगोत्पातौ — and the sense is narrowed\n'
        '  twice over. **संयोगः संबन्धः** is a meeting; **प्राणिनां\n'
        '  शुभाशुभसूचको महाभूतपरिणाम उत्पातः** is a portent, an upheaval of\n'
        '  the elements that foretells good or ill for living things. शतस्य\n'
        '  निमित्तं धनपतिना संयोगः **शत्यः, शतिकः** — a meeting with a rich\n'
        '  man that will bring a hundred. And as an omen: शतस्य निमित्तम्\n'
        '  उत्पातो **दक्षिणाक्षिस्पन्दनम्**, a twitch of the right eye,\n'
        '  **शत्यम्**. Two vārttikas add the humours: **तस्य निमित्तप्रकरणे\n'
        '  वातपित्तश्लेष्मभ्यः शमनकोपनयोरुपसंख्यानम्** — for what QUIETS or\n'
        '  what ROUSES wind, bile or phlegm, **वातिकम्, पैत्तिकम्,\n'
        '  श्लैष्मिकम्**; and **सन्निपाताच्चेति वक्तव्यम्**, सान्निपातिकम्,\n'
        '  for all three at once'
    ),
    '5.1.39': (
        'SETTLED — गोद्व्यचोऽसंख्यापरिमाणाश्वादेर्यत्, ठञादीनामपवादः; the गो\n'
        '  half. गोर्निमित्तं संयोग उत्पातो वा **गव्यः**\n'
        '\n'
        'SETTLED — गोद्व्यचोऽसंख्यापरिमाणाश्वादेर्यत्, the द्व्यच् half —\n'
        '  from any two-vowelled stem, three kinds excepted. **धन्यम्,\n'
        '  स्वर्ग्यम्, यशस्यम्, आयुष्यम्** — what portends wealth, heaven,\n'
        '  fame, long life. **असंख्यापरिमाणाश्वादेरिति किम्?** पञ्चानां\n'
        '  निमित्तं **पञ्चकम्**; परिमाण — प्रास्थिकम्, खारीकम्; अश्वादि —\n'
        '  आश्विकः. **ब्रह्मवर्चसादुपसंख्यानम्** adds one more:\n'
        '  ब्रह्मवर्चसस्य निमित्तं गुरुणा संयोगो **ब्रह्मवर्चस्यम्**. अश्व,\n'
        '  अश्मन्, गण, ऊर्णा, उमा, वसु, वर्ष, भङ्ग — अश्वादिः'
    ),
    '5.1.40': (
        'SETTLED — पुत्राच्छ च. **द्व्यच इति नित्ये यति प्राप्ते वचनम्** —\n'
        '  पुत्र has two vowels, so 5.1.39 would give it यत् and nothing\n'
        '  else; the rule is stated to add छ beside it, and the च keeps the\n'
        '  यत्. पुत्रस्य निमित्तं संयोग उत्पातो वा **पुत्रीयम्, पुत्र्यम्**'
    ),
    '5.1.41': (
        'SETTLED — सर्वभूमिपृथिवीभ्यामणञौ, ठकोऽपवादौ; the सर्वभूमि member,\n'
        '  **यथासंख्यम्**. सर्वभूमेर्निमित्तं संयोग उत्पातो वा **सार्वभौमः**\n'
        '  — and the strengthening falls on BOTH members,\n'
        '  **सर्वभूमेरनुशतिकादिपाठाद् उभयपदवृद्धिः** (7.3.20)\n'
        '\n'
        'SETTLED — सर्वभूमिपृथिवीभ्यामणञौ, the पृथिवी member. **पार्थिवः**'
    ),
    '5.1.42': (
        'SETTLED — तस्येश्वरः — the same two words, the same two affixes, a\n'
        '  different sense. सर्वभूमेरीश्वरः **सार्वभौमः**; पार्थिवः. **AND\n'
        '  THE GENITIVE IS RESTATED THOUGH IT IS ALREADY RUNNING.** Why,\n'
        '  inside a section of genitives? **षष्ठीप्रकरणे पुनः\n'
        '  षष्ठीसमर्थविभक्तिनिर्देशः प्रत्ययार्थस्य निवृत्तये** — to stop the\n'
        '  SENSE carrying over. Without it, **अन्यथा संयोगोत्पाताविव\n'
        '  ईश्वरोऽपि प्रत्ययार्थस्य निमित्तस्य विशेषणं संभाव्येत**: *lord*\n'
        '  would have been read as a further qualification of *omen*, the way\n'
        '  *meeting* and *portent* were. Restating the case is how the sense\n'
        '  is cut off\n'
        '\n'
        'SETTLED — तस्येश्वरः, the पृथिवी member. **पार्थिवः** — a king, one\n'
        '  who is lord of the earth'
    ),
    '5.1.43': (
        'SETTLED — तत्र विदित इति च — and now the base stands in the\n'
        '  LOCATIVE. **विदितो ज्ञातः प्रकाशित इत्यर्थः**, known or famous.\n'
        '  सर्वभूमौ विदितः **सार्वभौमः**. The same form for the third time in\n'
        '  three rules, and only the case and the sense divide them\n'
        '\n'
        'SETTLED — तत्र विदित इति च, the पृथिवी member. **पार्थिवः**'
    ),
    '5.1.44': (
        'SETTLED — लोकसर्वलोकाट् ठञ्. लोके विदितो **लौकिकः**, known in the\n'
        "  world; **सार्वलौकिकः**, where 7.3.20's अनुशतिकादि list again\n"
        '  strengthens both members'
    ),
    '5.1.45': (
        'SETTLED — तस्य वापः — and the sense is a FIELD, named from the\n'
        '  sowing. **उप्यतेऽस्मिन् वापः, क्षेत्रमुच्यते**: what is sown in is\n'
        '  a वाप, and that means the field. प्रस्थस्य वापः क्षेत्रं\n'
        '  **प्रास्थिकम्**, land that takes a prastha of seed; द्रौणिकम्,\n'
        '  खारीकम्. A measure of land given as a measure of grain'
    ),
    '5.1.46': (
        'SETTLED — पात्रात् ष्ठन्, ठञोऽपवादः — and the two letters of the\n'
        "  affix's name are told apart: **नकारः स्वरार्थः; षकारो ङीषर्थः**,\n"
        '  the न for the accent and the ष for the feminine. **पात्रशब्दः\n'
        '  परिमाणवाची** — the word here is a MEASURE and not a vessel.\n'
        '  पात्रस्य वापः **पात्रिकं क्षेत्रम्**; पात्रिकी क्षेत्रभक्तिः'
    ),
    '5.1.47': (
        'SETTLED — तदस्मिन् वृद्ध्यायलाभशुल्कोपदा दीयते — five things given,\n'
        '  and each is defined. **यदधमर्णेनोत्तमर्णाय मूलधनातिरिक्तं देयं तद्\n'
        '  वृद्धिः**, interest, what a debtor pays a creditor above the\n'
        '  principal; **ग्रामादिषु स्वामिग्राह्यो भाग आयः**, revenue;\n'
        '  **पटादीनामुपादानमूलादतिरिक्तं द्रव्यं लाभः**, profit over cost;\n'
        '  **रक्षानिर्वेशो राजभागः शुल्कः**, a toll paid for protection;\n'
        '  **उत्कोच उपदा**, a bribe. **दीयत इत्येकवचनान्तं वृद्ध्यादिभिः\n'
        '  प्रत्येकम् अभिसंबध्यते** — the verb is singular and joins each of\n'
        '  the five separately. पञ्च अस्मिन् वृद्धिर्वा आयो वा दीयते\n'
        '  **पञ्चकः**; शत्यः, शतिकः, साहस्रः. **चतुर्थ्यर्थ उपसंख्यानम्**\n'
        '  adds the dative — पञ्च अस्मै दीयते पञ्चको देवदत्तः — and then\n'
        '  withdraws the addition as needless: **सिद्धं त्वधिकरणत्वेन\n'
        '  विवक्षितत्वात्**, the man can be MEANT as the place the thing is\n'
        '  given in, **सममब्राह्मणे दानम्** (मनु० ७.८५) being said the same\n'
        '  way'
    ),
    '5.1.48': (
        'SETTLED — पूरणार्धाट् ठन्, **यथायथं ठक्टिठनोरपवादः** — an exception\n'
        '  to each of two affixes as each applies. From an ORDINAL: द्वितीयो\n'
        '  वृद्ध्यादिरस्मिन् दीयते **द्वितीयिकः**; तृतीयिकः, पञ्चमिकः,\n'
        '  सप्तमिकः\n'
        '\n'
        'SETTLED — पूरणार्धाट् ठन्, the अर्ध half — and the word is not\n'
        '  *half* in general. **अर्धशब्दो रूपकार्धस्य रूढिः**: it is the\n'
        '  settled name of half a रूपक, a coin. **अर्धिकः**'
    ),
    '5.1.49': (
        'SETTLED — भागाद् यच्च, ठञोऽपवादः — and the च brings ठन् in beside\n'
        '  the यत्. भागो वृद्ध्यादिरस्मिन् दीयते **भाग्यम्, भागिकं शतम्**;\n'
        '  भाग्या, भागिका विंशतिः. **भागशब्दोऽपि रूपकार्धस्य वाचकः** — this\n'
        '  word too means half a coin, like the अर्ध of the rule before'
    ),
    '5.1.50': (
        'SETTLED — तद्धरति वहति आवहति भाराद् वंशादिभ्यः — and the Kāśikā\n'
        '  gives TWO readings and refuses to choose. On the first,\n'
        '  **वंशादिभ्यः परो यो भारशब्दस्तदन्तात् प्रातिपदिकात्**: from a stem\n'
        '  ending in भार preceded by a वंशादि word — वंशभारं हरति\n'
        '  **वांशभारिकः**. On the second, **अपरा वृत्तिः — भाराद् वंशादिभ्य\n'
        '  इति, भारभूतेभ्यो वंशादिभ्य इत्यर्थः**: from the वंशादि words\n'
        '  themselves when they are a LOAD, भार qualifying them through the\n'
        '  sense — भारभूतान् वंशान् हरति **वांशिकः**. **सूत्रार्थद्वयमपि\n'
        '  चैतद् आचार्येण शिष्याः प्रतिपादिताः। तदुभयमपि ग्राह्यम्** — the\n'
        '  teacher taught his pupils both meanings of the sūtra, and both are\n'
        '  to be accepted. Each reading has its own counter-examples, and the\n'
        '  vṛtti supplies both sets. The three verbs are separated too:\n'
        '  **हरति देशान्तरं प्रापयति चोरयति वा** — carries off, or steals;\n'
        '  **वहति उत्क्षिप्य धारयति**, holds up and bears; **आवहति\n'
        '  उत्पादयति**, brings about. वंश, कुटज, बल्वज, मूल, अक्ष, स्थूणा,\n'
        '  अश्मन्, अश्व, इक्षु, खट्वा — वंशादिः'
    ),
    '5.1.51': (
        'SETTLED — वस्नद्रव्याभ्यां ठन्कनौ, **यथासंख्यम्**; the वस्न member.\n'
        '  वस्नं हरति वहति वा **वस्निकः**\n'
        '\n'
        'SETTLED — वस्नद्रव्याभ्यां ठन्कनौ, the द्रव्य member. **द्रव्यकः**'
    ),
    '5.1.52': (
        'SETTLED — संभवत्यवहरति पचति — three more verbs, each defined.\n'
        '  **तत्राधेयस्य प्रमाणानतिरेकः संभवः**, holding, where what is put\n'
        '  in does not exceed the measure; **उपसंहरणम् अवहारः**, taking up;\n'
        '  **विक्लेदनं पाकः**, cooking, which is a softening. प्रस्थं संभवति\n'
        '  अवहरति पचति वा **प्रास्थिकः**; कौडविकः, खारीकः. **ननु च पाके च\n'
        '  संभवोऽस्ति?** If a pot cooks a prastha it also HOLDS one, so why\n'
        '  name both? **नास्त्यत्र नियोगः** — there is no necessity in it,\n'
        '  and the two senses come apart: प्रस्थं पचति ब्राह्मणी\n'
        '  **प्रास्थिकी**, where the woman cooks it and does not contain it.\n'
        '  **तत्पचतीति द्रोणादण् च** — a vārttika adds अण् after द्रोण in the\n'
        '  cooking sense alone: द्रोणं पचति **द्रौणी, द्रौणिकी**'
    ),
    '5.1.53': (
        'SETTLED — आढकाचितपात्रात् खोऽन्यतरस्याम्, ठञोऽपवादः — and **पक्षे\n'
        '  सोऽपि भवति**, in the other half the ठञ् comes. आढकं संभवति अवहरति\n'
        '  पचति वा **आढकीना, आढकिकी**; आचितीना, आचितिकी; पात्रीणा, पात्रिकी'
    ),
    '5.1.54': (
        'SETTLED — द्विगोः ष्ठंश्च — and the counting of the forms is the\n'
        '  point. **विधानसामर्थ्याद् अनयोर्लुग् न भवति**: ष्ठन् and ख are\n'
        '  given after a द्विगु and so survive 5.1.28, the same argument\n'
        '  5.1.32 used. **ठञस्तु पक्षेऽनुज्ञातस्य अध्यर्धपूर्वद्विगोः इति\n'
        '  लुग् भवत्येव** — but the ठञ् allowed in the other alternative IS\n'
        '  removed. So three forms: **द्व्याढकिकी, द्व्याढकीना, द्व्याढकी**.\n'
        "  **नकारः स्वरार्थः; षकारो ङीषर्थः** again, and 4.1.22's\n"
        '  अपरिमाणबिस्ताचित… blocks ङीप् in द्व्याचिता'
    ),
    '5.1.55': (
        'SETTLED — कुलिजाल् लुक्खौ च — and now there are FOUR.\n'
        '  **अन्यतरस्यांग्रहणानुवृत्त्या लुगपि विकल्प्यते; ठञः पक्षे श्रवणं\n'
        '  भवति। तेन चातूरूप्यं संपद्यते**: the elision is itself one of the\n'
        '  alternatives, the ठञ् is heard in another, and ख and ष्ठन् make\n'
        '  the other two. **द्विकुलिजिकी, द्विकुलिजीना, द्विकुलिजी,\n'
        '  द्वैकुलिजिकी**. Three forms at 5.1.36, three at 5.1.54, four here\n'
        '  — the vṛtti counts them each time, त्रैरूप्यम् and चातूरूप्यम्.\n'
        "  And 7.3.17's exclusion is read as covering कुलिज too,\n"
        '  **तेनोत्तरपदवृद्धिरपि न भवति**'
    ),
    '5.1.56': (
        'SETTLED — सोऽस्यांशवस्नभृतयः — three more, and three one-word\n'
        '  glosses. **अंशो भागः**, a share; **वस्नं मूल्यम्**, a price;\n'
        '  **भृतिर्वेतनम्**, wages. पञ्च अंशो वस्नो वा भृतिर्वास्य\n'
        '  **पञ्चकः**; सप्तकः, साहस्रः'
    ),
    '5.1.57': (
        'SETTLED — तदस्य परिमाणम्. प्रस्थः परिमाणमस्य **प्रास्थिको राशिः**;\n'
        '  शत्यः, द्रौणिकः; वर्षशतं परिमाणमस्य **वार्षशतिकः**;\n'
        '  षष्टिर्जीवितपरिमाणमस्य **षाष्टिकः**, a man of sixty years. **AND\n'
        '  THE RULE RESTATES WHAT IS ALREADY RUNNING, IN ORDER TO BEAT AN\n'
        '  ELISION.** **समर्थविभक्तिः प्रत्ययार्थश्च\n'
        '  पूर्वसूत्रादेवानुवर्तिष्यते, किमर्थं पुनरनयोरुपादानम्?\n'
        '  पुनर्विधानार्थम्** — the case and the sense would both have\n'
        '  carried down from 5.1.56, so saying them again must be for the\n'
        '  sake of the ENJOINING being fresh: **पुनर्विधानसामर्थ्याद्\n'
        '  अध्यर्धपूर्वद्विगोर्लुग् न भवति**, and द्वे षष्टी जीवितपरिमाणमस्य\n'
        '  is **द्विषाष्टिकः** with its affix intact. The third time this\n'
        '  pāda saves an affix by the force of its being enjoined where it is'
    ),
    '5.1.58': (
        'SETTLED — संख्यायाः संज्ञासंघसूत्राध्ययनेषु — from a numeral, in\n'
        '  four settings, and the four are worked one by one. A NAME, where\n'
        '  **संज्ञायां स्वार्थे प्रत्ययो वाच्यः**, the affix changing\n'
        '  nothing: पञ्चैव **पञ्चकाः** शकुनयः. A GROUP: पञ्चकः संघः. An\n'
        '  ĀDHYAYANA, a reading: **पञ्चकोऽधीतः**, **तस्य संख्यापरिमाणं\n'
        '  पञ्चावृत्तयः पञ्च वाराः**, five times through. **AND A SŪTRA-WORK,\n'
        '  WHERE THE GRAMMAR NAMES ITSELF.** **अष्टावध्यायाः परिमाणमस्य\n'
        '  सूत्रस्य अष्टकं पाणिनीयम्** — a work of sūtras eight chapters in\n'
        '  measure is *the eight of Pāṇini*. दशकं वैयाघ्रपदीयम्; त्रिकं\n'
        '  काशकृत्स्नम्. The rule by which the Aṣṭādhyāyī is called the\n'
        '  Aṣṭādhyāyī. **ननु चाध्यायसमूहः सूत्रसंघ एव भवति?** Is a collection\n'
        '  of chapters not just a GROUP, already covered? **नैतदस्ति।\n'
        '  प्राणिसमूहे संघशब्दो रूढः** — *group* is settled usage for a\n'
        '  collection of living things. Three more supplements: **स्तोमे\n'
        '  डविधिः पञ्चदशाद्यर्थः** — पञ्चदशः स्तोमः; **शन्शतोर्डिनिश्\n'
        '  छन्दसि** — प॑ञ्चद॒शिनो॑ऽर्धमा॒साः; **विंशतेश्चेति वक्तव्यम्** —\n'
        '  विंशिनोऽङ्गिरसः'
    ),
    '5.1.59': (
        'SETTLED —\n'
        '  पङ्क्तिविंशतित्रिंशच्चत्वारिंशत्पञ्चाशत्षष्टिसप्तत्यशीतिनवतिशतम् —\n'
        '  ten words laid down ready-made. **यदिह लक्षणेनानुपपन्नं तत्सर्वं\n'
        '  निपातनात् सिद्धम्**: whatever cannot be got by rule is settled by\n'
        '  the laying-down. पञ्चानां टिलोपः, तिश्च प्रत्ययः —\n'
        '  **पङ्क्तिश्छन्दः**; द्वयोर्दशतोर्विन्भावः शतिच् च — **विंशतिः**;\n'
        '  त्रयाणां त्रिन्भावः शत् च — **त्रिंशत्**; and so to शतम्. **AND\n'
        '  THE VṚTTI WARNS AGAINST TAKING THE ANALYSIS SERIOUSLY.**\n'
        '  **विंशत्यादयो गुणशब्दाः, ते यथाकथंचिद् व्युत्पाद्याः।\n'
        '  नात्रावयवार्थे ऽभिनिवेष्टव्यम्** — these are quality-words, to be\n'
        '  derived somehow or other, and one must not insist on a meaning for\n'
        '  the parts. The proof: **पङ्क्तिरिति क्रमसंनिवेशेऽपि वर्तते** —\n'
        '  पङ्क्ति also means a mere row, ब्राह्मणपङ्क्तिः, पिपीलिकापङ्क्तिः,\n'
        '  **न चात्रावयवार्थः कश्चिदस्ति**, and there is no *five* in an\n'
        "  ant's file at all. **सहस्रादयोऽप्येवंजातीयकाः तद्वदेव द्रष्टव्याः;\n"
        '  उदाहरणमात्रमेतत्** — the list is examples and not an inventory'
    ),
    '5.1.60': (
        'SETTLED — पञ्चद्दशतौ वर्गे वा. **संख्यायाः इति कनि प्राप्ते\n'
        '  डतिर्निपात्यते; वावचनात् पक्षे सोऽपि भवति** — 5.1.58 would give\n'
        '  कन्, and डति is laid down instead, with the वा letting the कन्\n'
        '  stand in the other half. पञ्च परिमाणमस्य **पञ्चद् वर्गः**, and\n'
        '  **पञ्चको वर्गः**'
    ),
    '5.1.61': (
        'SETTLED — सप्तनोऽञ् छन्दसि. **वर्ग इत्येव** — the group is carried\n'
        '  down, and the register is the Veda. स॒प्त **साप्ता**नि असृजत्'
    ),
    '5.1.62': (
        'SETTLED — त्रिंशच्चत्वारिंशतोर्ब्राह्मणे संज्ञायां डण्. **वर्ग इति\n'
        '  निवृत्तम्** — the group lapses and a ब्राह्मण text takes its\n'
        '  place. त्रिंशदध्यायाः परिमाणमेषां ब्राह्मणानां **त्रैंशानि\n'
        '  ब्राह्मणानि**; चात्वारिंशानि. **अभिधेयसप्तम्येषा, न विषयसप्तमी** —\n'
        '  the locative ब्राह्मणे says what the word MEANS, not what body of\n'
        '  text the rule is confined to, **तेन मन्त्रभाषयोरपि भवति**: so the\n'
        '  form occurs in mantra and in ordinary speech as well. A\n'
        '  distinction between two uses of the locative, drawn in five words'
    ),
    '5.1.63': (
        'SETTLED — तदर्हति — and the आर्हीय heading closes on the word that\n'
        '  named it. श्वेतच्छत्रमर्हति **श्वैतच्छत्रिकः**, one who deserves a\n'
        '  white parasol; वास्त्रयुग्मिकः; शत्यः, शतिकः, साहस्रः. **AND THE\n'
        '  HEADING TAKES THIS RULE IN RATHER THAN STOPPING BEFORE IT.**\n'
        '  5.1.19 said आ and not प्राक्, **अभिविधावयमाकारः, तेनार्हत्यर्थेऽपि\n'
        '  ठग् भवत्येव** — so ठक् is the affix HERE too, and श्वैतच्छत्रिकः\n'
        '  has it. Every other great heading of the grammar stops one short\n'
        '  of the sūtra it is named from; this is the one that reaches it'
    ),
    '5.1.64': (
        'SETTLED — छेदादिभ्यो नित्यम्. **नित्यग्रहणं प्रत्ययार्थविशेषणम्** —\n'
        "  the word *always* qualifies what the affix reports, not the rule's\n"
        '  own application. छेदं नित्यमर्हति **छैदिकः**, one who is always\n'
        '  deserving of being cut; भैदिकः. छेद, भेद, द्रोह, दोह, वर्त, कर्ष,\n'
        '  संप्रयोग, विप्रयोग, प्रेषण, संप्रश्न, विप्रकर्ष, **विराग विरङ्गं\n'
        '  च** (ग०सू०११२) — छेदादिः, where the last entry substitutes as well\n'
        '  as listing: वैरङ्गिकः'
    ),
    '5.1.65': (
        'SETTLED — शीर्षच्छेदाद् यच्च — and the च keeps the यथाविहितम् of the\n'
        '  rule before, so both forms stand: शिरश्छेदं नित्यमर्हति\n'
        '  **शीर्षच्छेद्यः, शैर्षच्छेदिकः**. **प्रत्ययसन्नियोगेन शिरसः\n'
        '  शीर्षभावो निपात्यते**: the change of शिरस् to शीर्ष is laid down\n'
        '  as yoked to the affix, so the substitution and the affix come\n'
        '  together or not at all'
    ),
    '5.1.66': (
        'SETTLED — दण्डादिभ्यः, ठकोऽपवादः. **नित्यमिति निवृत्तम्** — the\n'
        '  *always* of 5.1.64 lapses here. दण्डमर्हति **दण्ड्यः**, one who\n'
        '  deserves the rod; मुसल्यः. दण्ड, मुसल, मधुपर्क, कशा, अर्घ, मेधा,\n'
        '  मेघ, युग, उदक, वध, गुहा, भाग, इभ — दण्डादिः'
    ),
    '5.1.67': (
        'SETTLED — छन्दसि च, ठञादीनामपवादः — and in the Veda the affix comes\n'
        '  after ANY stem whatever, **प्रातिपदिकमात्रात्**. **उदक्या**\n'
        '  वृत्तयः; यूप्यः पलाशः; गर्त्यो देशः'
    ),
    '5.1.68': (
        'SETTLED — पात्राद् घंश्च, ठक्ठञोरपवादः — and the च brings यत् in\n'
        '  beside the घन्. **पात्रं परिमाणमप्यस्ति** — the word is a measure\n'
        '  here as it was at 5.1.46. पात्रमर्हति **पात्रियः, पात्र्यः**'
    ),
    '5.1.69': (
        'SETTLED — कडङ्करदक्षिणाच्छ च, ठकोऽपवादः. कडङ्करमर्हति **कडङ्करीयो\n'
        '  गौः**, कडङ्कर्यः; दक्षिणामर्हति **दक्षिणीयो भिक्षुः**, दक्षिण्यो\n'
        '  ब्राह्मणः. **AND THE ORDER OF THE TWO WORDS IS ITSELF A SIGN.**\n'
        '  **दक्षिणाशब्दस्याल्पाच्तरस्यापूर्वनिपातेन लक्षणव्यभिचारचिह्नेन\n'
        '  यथासंख्याभावं सूचयति** — दक्षिणा has fewer vowels and so should\n'
        '  have stood first in the compound; that it does not breaks a rule,\n'
        '  and the breach is the mark that the two affixes are NOT to be\n'
        '  matched to the two words in order. Both words take both affixes'
    ),
    '5.1.70': (
        'SETTLED — स्थालीबिलात्, ठकोऽपवादौ. **छयतावनुवर्तते** — both affixes\n'
        '  of the rule before are carried down. स्थालीबिलमर्हन्ति\n'
        '  **स्थालीबिलीयास्तण्डुलाः**, स्थालीबिल्याः — grain fit for the\n'
        "  pot's hollow, **पाकयोग्या इत्यर्थः**, fit to be cooked"
    ),
    '5.1.71': (
        'SETTLED — यज्ञर्त्विग्भ्यां घखञौ, **यथासंख्यम्**, ठकोऽपवादौ; the\n'
        '  यज्ञ member. **यज्ञियो ब्राह्मणः**. **यज्ञर्त्विग्भ्यां\n'
        '  तत्कर्मार्हतीत्युपसंख्यानम्** — a vārttika extends it to deserving\n'
        '  the WORK of these: यज्ञकर्मार्हति **यज्ञियो देशः**, a place fit\n'
        '  for the work of sacrifice. **AND THE आर्हीय SECTION ENDS HERE,\n'
        '  EIGHT SŪTRAS PAST ITS OWN MARKER.** **आर्हीयाणां ठगादीनां\n'
        '  पूर्णोऽवधिः। अतः परं प्राग्वतीयष्ठञेव भवति** — the limit of ठक्\n'
        '  and the affixes under it is complete, and from here it is the ठञ्\n'
        '  of 5.1.18 alone. The same formula 4.4.74, 4.4.144 and 5.1.17 used,\n'
        '  for the fourth time. So even the one heading bounded by अभिविधि\n'
        '  has a marker apart from its last rule. The difference is not that\n'
        '  the two coincide — it is that this heading REACHES its marker and\n'
        '  takes it in, where the others stop short of theirs, and then runs\n'
        '  on past it while the rules keep naming its sense\n'
        '\n'
        'SETTLED — यज्ञर्त्विग्भ्यां घखञौ, the ऋत्विज् member. **आर्त्विजीनो\n'
        '  ब्राह्मणः**, and by the vārttika ऋत्विक्कर्मार्हति **आर्त्विजीनं\n'
        '  ब्राह्मणकुलम्**'
    ),
    '5.1.72': (
        'SETTLED — पारायणतुरायणचान्द्रायणं वर्तयति. **समर्थविभक्तिरनुवर्तते;\n'
        '  अर्हतीति निवृत्तम्** — the case carries and the sense does not.\n'
        '  पारायणं **वर्तयत्यधीते** — carries on, that is, studies:\n'
        '  **पारायणिकश्छात्रः**; तौरायणिको यजमानः; चान्द्रायणिकस्तपस्वी. This\n'
        '  is the rule 5.1.18 named its own examples from — the first\n'
        '  ordinary ठञ् rule after the आर्हीय section closes'
    ),
    '5.1.73': (
        'SETTLED — संशयमापन्नः. **संशयमापन्नः प्राप्तः** — one who has COME\n'
        '  INTO doubt. **सांशयिकः स्थाणुः**, a post that one is in doubt\n'
        '  about'
    ),
    '5.1.74': (
        'SETTLED — योजनं गच्छति. योजनं गच्छति **यौजनिकः**. Two vārttikas add\n'
        '  two long distances: **क्रोशशतयोजनशतयोरुपसंख्यानम्** — क्रौशशतिकः,\n'
        '  यौजनशतिकः; and **ततोऽभिगमनमर्हतीति च** — and one who DESERVES to\n'
        '  be come to from that far: क्रोशशतादभिगमनमर्हति **क्रौशशतिको\n'
        '  भिक्षुः**, **यौजनशतिक आचार्यः**, a teacher worth a hundred\n'
        "  leagues' journey"
    ),
    '5.1.75': (
        'SETTLED — पथः ष्कन्. **नकारः स्वरार्थः; षकारो ङीषर्थः** — the same\n'
        '  accounting 5.1.25 and 5.1.46 gave. पन्थानं गच्छति **पथिकः, पथिकी**'
    ),
    '5.1.76': (
        'SETTLED — पन्थो ण नित्यम् — and again **नित्यग्रहणं\n'
        '  प्रत्ययार्थविशेषणम्**, the *always* qualifying what is reported.\n'
        '  The rule does two things at once: **पथः पन्थ इत्ययमादेशो भवति णश्च\n'
        '  प्रत्ययः**. पन्थानं नित्यं गच्छति **पान्थो** भिक्षां याचते, a\n'
        '  wayfarer, one always on the road. **नित्यमिति किम्?** पथिकः'
    ),
    '5.1.77': (
        'SETTLED — उत्तरपथेनाहृतं च — and the case is got from the wording\n'
        '  itself, **निर्देशादेव समर्थविभक्तिः**, since the sūtra shows the\n'
        '  instrumental in उत्तरपथेन. **चकारः प्रत्ययार्थसमुच्चये, गच्छतीति\n'
        '  च**: the च gathers in the sense of the rule three back too, so one\n'
        '  affix serves both — उत्तरपथेनाहृतम् **औत्तरपथिकम्**, and उत्तरपथेन\n'
        '  गच्छति **औत्तरपथिकः**. **आहृतप्रकरणे\n'
        '  वारिजङ्गलस्थलकान्तारपूर्वपदादुपसंख्यानम्** adds four roads —\n'
        '  वारिपथिकम्, जाङ्गलपथिकम्, स्थालपथिकम्, कान्तारपथिकम् — and\n'
        '  **अजपथशङ्कुपथाभ्यां चोपसंख्यानम्** two more. **मधुकमरिचयोरण्\n'
        '  स्थलात्** gives a different affix for two goods: **स्थालपथं\n'
        '  मधुकम्**, liquorice brought by the land road'
    ),
    '5.1.78': (
        'SETTLED — कालात्. **कालादित्यधिकारः। यदित ऊर्ध्वम् अनुक्रमिष्यामः\n'
        '  कालादित्येवं तद् वेदितव्यम्** — everything stated from here on is\n'
        '  understood to be from a word for TIME. मासेन निर्वृत्तं\n'
        '  **मासिकम्**; आर्धमासिकम्, सांवत्सरिकम्. **कालादित्यधिकारो\n'
        '  व्युष्टादिभ्योऽण् इति यावत्** — the heading runs as far as 5.1.97.\n'
        '  And this heading is unlike the four great ones: it carries not an\n'
        '  AFFIX but a CONDITION on the base, so it does not compete with the\n'
        '  ठञ् it stands inside'
    ),
    '5.1.79': (
        'SETTLED — तेन निर्वृत्तम् — brought about by it. अह्ना निर्वृत्तम्\n'
        "  **आह्निकम्**, a day's work; आर्धमासिकम्, सांवत्सरिकम्"
    ),
    '5.1.80': (
        'SETTLED — तमधीष्टो भृतो भूतो भावी — four senses, each glossed.\n'
        '  **अधीष्टः सत्कृत्य व्यापारितः**, engaged with honour; **भृतो\n'
        '  वेतनेन क्रीतः**, hired for wages; **भूतः स्वसत्तया व्याप्तकालः**,\n'
        '  one whose own being has filled that time; **भावी तादृश एवानागतः**,\n'
        '  the same but still to come. 2.3.5 कालाध्वनोः gives the accusative.\n'
        '  मासमधीष्टो **मासिकोऽध्यापकः**; मासं भृतो मासिकः कर्मकरः; मासं भूतो\n'
        '  मासिको व्याधिः; मासं भावी मासिक उत्सवः. **AND AN OBJECTION ABOUT\n'
        '  WHAT CAN FILL A MONTH.** **ननु चाध्येषणं भरणं च मुहूर्तं क्रियते,\n'
        '  तेन कथं मासो व्याप्यते?** — the engaging and the hiring take a\n'
        '  moment, so how do they occupy a month? **अध्येषणभरणे क्रियार्थे,\n'
        '  तत्र फलभूतया क्रियया मासो व्याप्यमानस्ताभ्यामेव व्याप्त\n'
        '  इत्युच्यते**: both are FOR an action, and the month filled by that\n'
        '  resulting action is said to be filled by them'
    ),
    '5.1.81': (
        'SETTLED — मासाद् वयसि यत्खञौ, ठञोऽपवादौ — and only one of the four\n'
        '  senses reaches here. **अधीष्टादीनां चतुर्णाम् अधिकारेऽपि\n'
        '  सामर्थ्याद् भूत एवात्राभिसंबध्यते**: though all four are running,\n'
        '  only भूत can join, since an AGE is time already lived. मासं भूतो\n'
        '  **मास्यः, मासीनः**. **वयसीति किम्?** मासिकम्'
    ),
    '5.1.82': (
        'SETTLED — द्विगोर्यप्. **मासाद् वयसीति वर्तते** — from a numeral\n'
        '  compound ending in मास, of an age. द्वौ मासौ भूतो **द्विमास्यः**;\n'
        '  त्रिमास्यः'
    ),
    '5.1.83': (
        'SETTLED — षण्मासाण् ण्यच्च. **वयसीत्येव**, and the counting again:\n'
        '  **औत्सर्गिकष्ठञपीष्यते, स चकारेण समुच्चेतव्यः;\n'
        '  स्वरितत्वाच्चानन्तरोऽनुवर्तिष्यते। तेन त्रैरूप्यं भवति** — the\n'
        '  general ठञ् is wanted too and is gathered by the च, the यप् of the\n'
        '  rule before carries on by its accent, and so THREE forms:\n'
        '  **षाण्मास्यः, षण्मास्यः, षाण्मासिकः**'
    ),
    '5.1.84': (
        'SETTLED — अवयसि ठंश्च — the same word, and now NOT of an age.\n'
        '  **चकारेणानन्तरस्य ण्यतः समुच्चयः क्रियते**, the च gathering the\n'
        '  ण्यत् of the rule before. **षण्मासिको रोगः**, a six-month illness;\n'
        '  षाण्मास्यः'
    ),
    '5.1.85': (
        'SETTLED — समायाः खः, ठञोऽपवादः. **अधीष्टादयश्चत्वारोऽर्था\n'
        '  अनुवर्तन्ते** — all four senses are back. समामधीष्टो भृतो भूतो\n'
        '  भावी वा **समीनः**. **केचित् तु तेन निर्वृत्तम् इति\n'
        '  सर्वत्रानुवर्तयन्ति** — and some carry 5.1.79 down everywhere as\n'
        '  well, giving समया निर्वृत्तः समीनः'
    ),
    '5.1.86': (
        'SETTLED — द्विगोर्वा. **पूर्वेण नित्यः प्राप्तो विकल्प्यते** — what\n'
        '  the rule before made obligatory becomes a choice, and **खेन मुक्ते\n'
        '  पक्षे ठञपि भवति**: where the ख is released the ठञ् comes.\n'
        '  **द्विसमीनः, द्वैसमिकः**. And a compound is reached at all only by\n'
        '  the vārttika of 5.1.20: **प्राग्वतेः संख्यापूर्वपदानां\n'
        '  तदन्तग्रहणमलुकि इति प्राप्तिरस्त्येव**'
    ),
    '5.1.87': (
        'SETTLED — रात्र्यहस्संवत्सराच्च. **खेन मुक्ते पक्षे ठञपि भवति**.\n'
        '  **द्विरात्रीणः, द्वैरात्रिकः**; द्व्यहीनः, द्वैयह्निकः;\n'
        '  द्विसंवत्सरीणः, द्विसांवत्सरिकः, where 7.3.15 संख्यायाः\n'
        '  संवत्सरसंख्यस्य च strengthens the LATTER member'
    ),
    '5.1.88': (
        'SETTLED — वर्षाल् लुक् च — and here the elision joins the option, so\n'
        '  **तयोश्च वा लुग् भवति। एवं त्रीणि रूपाणि भवन्ति**: three forms\n'
        '  again. **द्विवर्षीणो व्याधिः, द्विवार्षिकः, द्विवर्षः**. 7.3.16\n'
        '  वर्षस्याभविष्यति strengthens the latter member — **भाविनि तु\n'
        '  त्रैवर्षिकः**, and where the sense is *still to come* the\n'
        '  strengthening moves to the first'
    ),
    '5.1.89': (
        'SETTLED — चित्तवति नित्यम् — and where what is meant HAS A MIND the\n'
        '  elision is no longer a choice. **पूर्वेण विकल्पे प्राप्ते वचनम्**:\n'
        '  the rule before made it optional and this makes it fixed.\n'
        '  **द्विवर्षो दारकः**, a two-year-old child. **चित्तवतीति किम्?**\n'
        '  द्विवर्षीणो व्याधिः — an illness has no mind, so it keeps the\n'
        '  choice'
    ),
    '5.1.90': (
        'SETTLED — षष्टिकाः षष्टिरात्रेण पच्यन्ते — a laid-down form, and\n'
        '  three things are laid down at once: the affix कन्, the dropping of\n'
        '  रात्रि, and the sense. **बहुवचनमतन्त्रम्** — the plural in the\n'
        '  sūtra is not binding. षष्टिरात्रेण पच्यन्ते **षष्टिकाः**, rice\n'
        '  that ripens in sixty nights. **संज्ञैषा धान्यविशेषस्य। तेन\n'
        '  मुद्गादिष्वतिप्रसङ्गो न भवति** — it is the NAME of one particular\n'
        '  grain, so the rule does not overreach to beans and the rest that\n'
        '  might also take sixty nights'
    ),
    '5.1.91': (
        'SETTLED — वत्सरान्ताच्छश्छन्दसि, ठञोऽपवादः. **इद्वत्सरीयः,\n'
        '  इदावत्सरीयः** (काठ०सं० १३.१५)'
    ),
    '5.1.92': (
        'SETTLED — संपरिपूर्वात् ख च — from a वत्सर-final stem with सम् or\n'
        '  परि in front, and the च keeps the छ of the rule before.\n'
        '  सं॒व॒त्स॒**रीणाः**; परिवत्स॒**रीण**म्; संवत्सरीया, परिवत्सरीया'
    ),
    '5.1.93': (
        'SETTLED — तेन परिजय्यलभ्यकार्यसुकरम् — four more senses, and one\n'
        '  form answers all four. मासेन परिजय्यः, **शक्यते जेतुम्**, that can\n'
        '  be got the better of in a month — **मासिको व्याधिः**; मासेन लभ्यो\n'
        '  मासिकः पटः; मासेन कार्यं मासिकं चान्द्रायणम्; मासेन सुकरो **मासिकः\n'
        '  प्रासादः**, a palace easily built in a month'
    ),
    '5.1.94': (
        'SETTLED — तदस्य ब्रह्मचर्यम् — and here too the Kāśikā gives two\n'
        '  readings and keeps both. On the first the base is in the\n'
        '  ACCUSATIVE and **सा चात्यन्तसंयोगे**, of unbroken connection: मासं\n'
        '  ब्रह्मचर्यमस्य **मासिको ब्रह्मचारी**, and the affix reports the\n'
        '  STUDENT. On the second, **अपरा वृत्तिः**, the base is in the\n'
        '  NOMINATIVE: मासोऽस्य ब्रह्मचर्यस्य **मासिकं ब्रह्मचर्यम्**, and\n'
        '  the affix reports the STUDY. **पूर्वत्र ब्रह्मचारी प्रत्ययार्थः,\n'
        '  उत्तरत्र ब्रह्मचर्यमेव। उभयमपि प्रमाणम्, उभयथा सूत्रप्रणयनात्** —\n'
        '  both are authoritative, the sūtra being framed both ways. The\n'
        '  second time this pāda refuses to choose between two readings. Five\n'
        '  vārttikas follow, on observances rather than time:\n'
        '  **महानाम्न्यादिभ्यः षष्ठीसमर्थेभ्य उपसंख्यानम्** — माहानामिकम्,\n'
        '  गौदानिकम्, आदित्यव्रतिकम्; **तच्चरतीति च** — and one who PRACTISES\n'
        '  it, **महानाम्न्य ऋचः, तत्सहचरितं व्रतं तच्छब्देनोच्यते**, the word\n'
        '  naming the vow that goes with those verses: महानाम्नीश्चरति\n'
        '  माहानामिकः. **अवान्तरदीक्षादिभ्यो डिनिर्वक्तव्यः** —\n'
        '  अवान्तरदीक्षी, तिलव्रती; **अष्टाचत्वारिंशतो ड्वुंश्च डिनिश्च** —\n'
        '  अष्टाचत्वारिंशकः, अष्टाचत्वारिंशी; **चातुर्मास्यानां यलोपश्च** —\n'
        '  चातुर्मासकः, चातुर्मासी'
    ),
    '5.1.95': (
        'SETTLED — तस्य च दक्षिणा यज्ञाख्येभ्यः. अग्निष्टोमस्य दक्षिणा\n'
        '  **आग्निष्टोमिकी**; वाजपेयिकी, राजसूयिकी. **AND THE WORD आख्या IS\n'
        '  WHAT LETS THE RULE OUT OF THE TIME-HEADING.** **आख्याग्रहणम्\n'
        '  अकालादपि यज्ञवाचिनो यथा स्यादिति। इतरथा हि कालाधिकाराद्\n'
        '  एकाहद्वादशाहप्रभृतय एव यज्ञा गृह्येरन्** — without it the काल\n'
        '  heading would have confined the rule to sacrifices NAMED FROM\n'
        '  their length, the one-day and the twelve-day; saying *named* takes\n'
        "  in every sacrifice's name"
    ),
    '5.1.96': (
        'SETTLED — तत्र च दीयते कार्यं भववत् — and the affix is borrowed from\n'
        '  the *born in* rules: **भववत् प्रत्ययो भवति**, as in मासे भवं\n'
        '  **मासिकम्**, so मासे दीयते मासिकम्. प्रावृषेण्यम्, वासन्तिकम्,\n'
        '  हैमन्तिकम्, शारदम्. **वतिः सर्वसादृश्यार्थः** — the वति takes in\n'
        '  every likeness, the same words 4.2.34 and 4.3.156 used.\n'
        '  **योगविभागश्चात्र कर्तव्यः। तत्र च दीयते, यज्ञाख्येभ्य इति** — and\n'
        '  the rule is to be split, so that the sacrifice-names of 5.1.95 are\n'
        '  reached too: **आग्निष्टोमिकं भक्तम्**, food given at an\n'
        '  अग्निष्टोम. **AND THE TIME-HEADING ENDS HERE.** **कालाधिकारस्य\n'
        '  पूर्णोऽवधिः। अतः परं सामान्येन प्रत्ययविधानम्** — its limit is\n'
        '  complete, and from here the affixes are given generally. 5.1.78\n'
        '  named 5.1.97 as the boundary and the heading stops one short of\n'
        '  it, which is the fifth time this project has met the formula and\n'
        '  the fifth heading whose marker is not its last rule'
    ),
    '5.1.97': (
        'SETTLED — व्युष्टादिभ्योऽण् — and the base is no longer a word for\n'
        '  time, which is why the heading stopped before this rule. व्युष्टे\n'
        '  दीयते कार्यं वा **वैयुष्टम्**; नैत्यम्. **अण्प्रकरणे अग्निपदादिभ्य\n'
        '  उपसंख्यानम्** proposes adding two words, and the vṛtti refuses the\n'
        '  addition as needless: **किं वक्तव्यम्? न वक्तव्यम्। अत्रैव ते\n'
        '  पठितव्याः** — put them in the list itself. व्युष्ट, नित्य,\n'
        '  निष्क्रमण, प्रवेशन, तीर्थ, संभ्रम, आस्तरण, संग्राम, संघात,\n'
        '  अग्निपद, पीलुमूल, प्रवास, उपसंक्रमण — व्युष्टादिः, and the last\n'
        '  four are the words the vārttika wanted added'
    ),
    '5.1.98': (
        'SETTLED — तेन यथाकथाचहस्ताभ्यां णयतौ — two affixes and two words,\n'
        '  and the vṛtti refuses to match them in order. **दीयते\n'
        '  कार्यमित्येतयोरर्थयोः प्रत्येकम् अभिसंबन्धः, यथासंख्यं नेष्यते**:\n'
        '  each affix goes with each sense, and the pairing is not wanted.\n'
        '  **यथाकथाचशब्दोऽव्ययसमुदायोऽनादरे वर्तते** — यथाकथाच is a bundle of\n'
        '  indeclinables meaning *anyhow*, carelessly. And being indeclinable\n'
        '  it cannot really stand in a case: **तृतीयार्थमात्रं चात्र संभवति,\n'
        '  न तु तृतीया समर्थविभक्तिः**, only the MEANING of the instrumental\n'
        '  is possible here, not the instrumental itself. **याथाकथाचम्**;\n'
        '  हस्तेन दीयते कार्यं वा **हस्त्यम्**'
    ),
    '5.1.99': (
        'SETTLED — संपादिनि. **गुणोत्कर्षः संपत्तिः** — a संपत्ति is an\n'
        '  excellence of quality, so the sense is *what sets a thing off*.\n'
        '  कर्णवेष्टकाभ्यां संपादि मुखं **कार्णवेष्टकिकं मुखम्**, a face that\n'
        '  earrings set off; **वास्त्रययुगिकं शरीरम्**, **वस्त्रयुगेण विशेषतः\n'
        "  शोभत इत्यर्थः**. (3.3.170's णिनि is what made संपादिन् itself,\n"
        '  **आवश्यके णिनिः**)'
    ),
    '5.1.100': (
        'SETTLED — कर्मवेषाद् यत्, ठञोऽपवादः. कर्मणा संपद्यते **कर्मण्यं\n'
        '  शरीरम्**, a body that work sets off; वेषेण संपद्यते **वेष्यो\n'
        '  नटः**, an actor his costume sets off'
    ),
    '5.1.101': (
        'SETTLED — तस्मै प्रभवति संतापादिभ्यः. **समर्थः शक्तः\n'
        '  प्रभवतीत्युच्यते** — one who is able, equal to it; **अलमर्थे\n'
        '  चतुर्थी**, the dative of being adequate. संतापाय प्रभवति\n'
        '  **सान्तापिकः**; सान्नाहिकः. संताप, संनाह, संग्राम, संयोग, संपराय,\n'
        '  संपेष, निष्पेष, निसर्ग, असर्ग, विसर्ग, उपसर्ग, उपवास, प्रवास,\n'
        '  संघात, संमोदन, **सक्तुमांसौदनाद् विगृहीतादपि** (ग०सू०११३) —\n'
        '  संतापादिः, and the last entry lets three words in even\n'
        '  UNCOMPOUNDED'
    ),
    '5.1.102': (
        'SETTLED — योगाद् यच्च — and the च keeps the ठञ्, so both stand.\n'
        '  योगाय प्रभवति **योग्यः, यौगिकः**'
    ),
    '5.1.103': (
        'SETTLED — कर्मण उकञ्, ठञोऽपवादः. कर्मणे प्रभवति **कार्मुकं धनुः**, a\n'
        '  bow, *equal to the work*. **धनुषोऽन्यत्र न भवति, अनभिधानात्** —\n'
        '  and of nothing but a bow, because the language does not say it of\n'
        '  anything else. A rule whose scope is fixed not by a word in it but\n'
        '  by usage'
    ),
    '5.1.104': (
        'SETTLED — समयस्तदस्य प्राप्तम्. समयः प्राप्तोऽस्य **सामयिकं\n'
        '  कार्यम्**, **उपनतकालम् इत्यर्थः** — a thing whose time has come\n'
        '  round. **समर्थविभक्तिनिर्देश उत्तरार्थः** — and the case is\n'
        '  spelled out here for the sake of the rules AFTER this one, which\n'
        '  carry it down'
    ),
    '5.1.105': (
        'SETTLED — ऋतोरण्. ऋतुः प्राप्तोऽस्य **आर्तवं पुष्पम्**, a flower\n'
        '  whose season has come. **तदस्य प्रकरण उपवस्त्रादिभ्य उपसंख्यानम्**\n'
        '  adds two more: औपवस्त्रम्, प्राशित्रम्'
    ),
    '5.1.106': (
        'SETTLED — छन्दसि घस्, अणोऽपवादः. अ॒यं ते॒ योनि॑र्**ऋ॒त्वियः**॒\n'
        '  (ऋ०३.२९.१०) — and the affix is given for one word in one register,\n'
        '  where the rule before gave another for the same word everywhere\n'
        '  else'
    ),
    '5.1.107': (
        'SETTLED — कालाद् यत्. कालः प्राप्तोऽस्य **काल्यस्तापः**, heat that\n'
        '  has come in its time; **काल्यं शीतम्**'
    ),
    '5.1.108': (
        'SETTLED — प्रकृष्टे ठञ्. **प्राप्तमिति निवृत्तम्** — the *come\n'
        '  round* sense lapses and only काल is carried. **प्रकर्षेण कालो\n'
        '  विशेष्यते**: the time is qualified as LONG. प्रकृष्टो दीर्घः\n'
        '  कालोऽस्य **कालिकमृणम्**, a debt of long standing; **कालिकं\n'
        '  वैरम्**, an old enmity. **ठञ्ग्रहणं विस्पष्टार्थम्** — and the ठञ्\n'
        "  is named though it is already the heading's, merely for clarity"
    ),
    '5.1.109': (
        'SETTLED — प्रयोजनम्. इन्द्रमहः प्रयोजनमस्य **ऐन्द्रमहिकम्**, a thing\n'
        '  whose occasion is the festival of Indra; गाङ्गामहिकम्'
    ),
    '5.1.110': (
        'SETTLED — विशाखाषाढादण् मन्थदण्डयोः — two words, two affixes and two\n'
        '  THINGS MEANT, matched **यथासंख्यम्**. विशाखा प्रयोजनमस्य **वैशाखो\n'
        '  मन्थः**, a churning stick; **आषाढो दण्डः**, a staff. **चूडादिभ्य\n'
        '  उपसंख्यानम्** adds a list: चौडम्, **श्राद्धम्** — the rite whose\n'
        '  occasion is faith'
    ),
    '5.1.111': (
        'SETTLED — अनुप्रवचनादिभ्यश्छः, ठञोऽपवादः. अनुप्रवचनं प्रयोजनमस्य\n'
        '  **अनुप्रवचनीयम्**, उत्त्थापनीयम्. Three vārttikas widen and one\n'
        '  narrows. **विशिपूरिपतिरुहिप्रकृतेरनात् सपूर्वपदाद् उपसंख्यानम्** —\n'
        '  any अन-form of four roots with a word before it: गृहप्रवेशनीयम्,\n'
        '  प्रपापूरणीयम्, अश्वप्रपतनीयम्, प्रासादारोहणीयम्. **स्वर्गादिभ्यो\n'
        '  यद् वक्तव्यः** — a different affix for a list: **स्वर्ग्यम्,\n'
        '  यशस्यम्, आयुष्यम्, काम्यम्, धन्यम्**. And **पुण्याहवाचनादिभ्यो\n'
        '  लुग् वक्तव्यः** — no affix at all for three: पुण्याहवाचनं\n'
        '  प्रयोजनमस्य **पुण्याहवाचनम्**, the word standing unchanged'
    ),
    '5.1.112': (
        'SETTLED — समापनात् सपूर्वपदात्, ठञोऽपवादः — from समापन with a word\n'
        '  before it. छन्दस्समापनं प्रयोजनमस्य **छन्दःसमापनीयम्**;\n'
        '  व्याकरणसमापनीयम्. **पदग्रहणं बहुच्पूर्वनिरासार्थम्** — the word पद\n'
        '  is there to shut out a बहुच् standing in front, which is a prefix\n'
        '  and not a word'
    ),
    '5.1.113': (
        'SETTLED — ऐकागारिकट् चौरे — a form laid down, and the whole point of\n'
        '  laying it down is to NARROW it. एकागारं प्रयोजनमस्य **ऐकागारिकः\n'
        '  चौरः**, a burglar, one whose object is a single house; ऐकागारिकी.\n'
        '  **किमर्थमिदं निपात्यते, यावता प्रयोजनमित्येव सिद्धष्ठञ्? चौरे\n'
        '  नियमार्थं वचनम्** — 5.1.109 would have given the same ठञ् anyway;\n'
        '  the rule is stated to CONFINE the word to a thief, **इह मा भूत् —\n'
        '  एकागारं प्रयोजनमस्य भिक्षोरिति**, so that a monk with the same\n'
        '  single-house object is not called it. **टकारः कार्यावधारणार्थः;\n'
        '  ङीबेव भवति, न ञित्स्वर इति** — the ट settles which operations\n'
        '  follow. **अपरे पुनरिकट् प्रत्ययं वृद्धिं च निपातयन्ति**'
    ),
    '5.1.114': (
        'SETTLED — आकालिकड् आद्यन्तवचने — another laid-down form, and again\n'
        '  several things at once: **समानकालशब्दस्य आकालशब्द आदेशः** and\n'
        '  **इकट् प्रत्ययश्च निपात्यते**, the substitution and the affix\n'
        '  together. **आद्यन्तयोश्चैतद् विशेषणम्** — the sense qualifies the\n'
        '  BEGINNING and the END. समानकालावाद्यन्तावस्य **आकालिकः\n'
        '  स्तनयित्नुः**, a thunderclap; **आकालिकी विद्युत्**, lightning,\n'
        '  **जन्मना तुल्यकालविनाशा; उत्पादानन्तरं विनाशिनी इत्यर्थः** — whose\n'
        '  ending is of one time with its beginning, perishing the instant it\n'
        '  arises. A whole rule for a word meaning *momentary*. **आकालाट्\n'
        '  ठंश्च; चात् ठञ् च** — a vārttika adds two more affixes: आकालिका\n'
        '  विद्युत्. **AND THE ठञ् HEADING ENDS HERE.** **ठञः पूर्णोऽवधिः** —\n'
        '  the sixth time this project has met the formula, and the narrowest\n'
        '  gap yet: the marker 5.1.115 stands one sūtra past the last rule'
    ),
    '5.1.115': (
        'SETTLED — तेन तुल्यं क्रिया चेद् वतिः — the sūtra whose word bounded\n'
        '  the ठञ् heading. ब्राह्मणेन तुल्यं वर्तते **ब्राह्मणवत्**; राजवत्.\n'
        '  **क्रियाग्रहणं किम्? गुणद्रव्यतुल्ये मा भूत्** — the likeness must\n'
        '  be one of ACTION and not of quality or substance: पुत्रेण तुल्यः\n'
        '  स्थूलः, पुत्रेण तुल्यः पिङ्गलः, पुत्रेण तुल्यो गोमान् take nothing'
    ),
    '5.1.116': (
        'SETTLED — तत्र तस्येव — and one rule for two cases at once.\n'
        '  **तत्रेति सप्तमीसमर्थात् तस्येति षष्ठीसमर्थात् च इवार्थे वतिः**:\n'
        '  मथुरायामिव **मथुरावत्** स्रुघ्ने प्राकारः, a rampart in Srughna as\n'
        '  in Mathurā; पाटलिपुत्रवत् साकेते परिखा\n'
        '\n'
        'SETTLED — तत्र तस्येव, the genitive half. देवदत्तस्येव\n'
        "  **देवदत्तवत्** यज्ञदत्तस्य गावः — Yajñadatta's cows like\n"
        "  Devadatta's; यज्ञदत्तवत् देवदत्तस्य दन्ताः"
    ),
    '5.1.117': (
        'SETTLED — तदर्हम्. राजानमर्हति **राजवत् पालनम्**, protection such as\n'
        '  a king deserves; ब्राह्मणवत्, ऋषिवत्, क्षत्रियवत्'
    ),
    '5.1.118': (
        'SETTLED — उपसर्गाच्छन्दसि धात्वर्थे — and the affix changes nothing\n'
        '  but the shape. **उपसर्गात् ससाधने धात्वर्थे वर्तमानात् स्वार्थे\n'
        '  वतिः**: from a preverb standing for a verbal sense together with\n'
        '  its means. यद्**उद्वतो॑ नि॒वतो॒** यासि॒ बप्स॒द् (ऋ०१०.१४२.४) —\n'
        '  **उद्गतानि निगतानि च**'
    ),
    '5.1.119': (
        'SETTLED — तस्य भावस्त्वतलौ — and the vṛtti says what भाव means in\n'
        '  this grammar. **भवतोऽस्मादभिधानप्रत्ययाविति भावः; शब्दस्य\n'
        '  प्रवृत्तिनिमित्तं भावशब्देनोच्यते** — a भाव is that from which the\n'
        '  naming and the notion arise, the GROUND on which a word is applied\n'
        '  at all. अश्वस्य भावः **अश्वत्वम्, अश्वता**; गोत्वम्, गोता'
    ),
    '5.1.120': (
        'SETTLED — आ च त्वात्. **ब्रह्मणस्त्वः इति वक्ष्यति। आ एतस्मात्\n'
        '  त्वसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामः, तत्र त्वतलौ\n'
        '  प्रत्ययावधिकृतौ वेदितव्यौ** — त्व and तल् are governed as far as\n'
        '  5.1.136, and the आ is अभिविधि again, so that rule is taken in.\n'
        '  **AND THIS HEADING DOES NOT DISPLACE WHAT IT MEETS — IT STANDS\n'
        '  BESIDE IT.** **अपवादैः सह समावेशार्थं वचनम्**: the rule is stated\n'
        '  so that त्व and तल् come TOGETHER WITH the affixes that would\n'
        '  otherwise displace them. प्रथिमा by 5.1.122 and पार्थवम् and\n'
        '  **पृथुत्वम्** and **पृथुता**, all four standing. Every other\n'
        '  heading of this pāda was displaced by its own exceptions; this one\n'
        '  is not. **कर्मणि च विधानार्थम्** — and it reaches the कर्मन् sense\n'
        '  5.1.124 will add. **चकारो नञ्स्नञ्भ्यामपि समावेशार्थः**: the च\n'
        '  puts them beside नञ् and स्नञ् too — स्त्रैणम् and **स्त्रीत्वम्**\n'
        '  and स्त्रीता; पौंस्नम् and पुंस्त्वम् and पुंस्ता'
    ),
    '5.1.121': (
        'SETTLED — न नञ्पूर्वात् तत्पुरुषाद् अचतुरसंगतलवणवटयुधकतरसलसेभ्यः — a\n'
        '  प्रतिषेध, and it governs the whole stretch: **इत उत्तरे ये\n'
        '  भावप्रत्ययाः ते नञ्पूर्वात् तत्पुरुषाद् न भवन्ति चतुरादीन्\n'
        '  वर्जयित्वा**. अपतित्वम्, अपतिता — the त्व and तल् stand, and the\n'
        '  special affixes do not. Three conditions, each with its\n'
        '  counter-example. **नञ्पूर्वादिति किम्?** बार्हस्पत्यम्,\n'
        '  प्राजापत्यम् — no नञ् there. **तत्पुरुषादिति किम्?** नास्य पटवः\n'
        '  सन्तीत्यपटुः, तस्य भाव **आपटवम्** — a बहुव्रीहि, not a तत्पुरुष.\n'
        '  **अचतुरादिभ्य इति किम्?** आचतुर्यम्, आसंगत्यम्, आलवण्यम्, आवट्यम्,\n'
        '  आबुध्यम्, आकत्यम्, आरस्यम्, **आलस्यम्** — the eight the rule\n'
        '  excepts'
    ),
    '5.1.122': (
        'SETTLED — पृथ्वादिभ्य इमनिच् वा. **वावचनम् अणादेः समावेशार्थम्** —\n'
        '  and the option is there so that the अण् and the rest come TOO, not\n'
        '  so that one is chosen. पृथोर्भावः **प्रथिमा, पार्थवम्**, and\n'
        '  **त्वतलौ सर्वत्र भवत एव**: पृथुत्वम्, पृथुता stand everywhere.\n'
        '  Four forms for one sense. 6.4.154 तुरिष्ठेमेयस्सु and 6.4.155 टेः\n'
        '  give the टि-elision, 6.4.161 र ऋतो हलादेर्लघोः the र. पृथु, मृदु,\n'
        '  महत्, पटु, तनु, लघु, बहु, साधु, वेणु, आशु, बहुल, गुरु, दण्ड, ऊरु,\n'
        '  खण्ड, चण्ड, बाल, अकिंचन, होड, पाक, वत्स, मन्द, स्वादु, ह्रस्व,\n'
        '  दीर्घ, प्रिय, वृष, ऋजु, क्षिप्र, क्षुद्र — पृथ्वादिः'
    ),
    '5.1.123': (
        'SETTLED — वर्णदृढादिभ्यः ष्यञ् च; the वर्ण half — from the words for\n'
        '  COLOURS. शुक्लस्य भावः **शौक्ल्यम्, शुक्लिमा, शुक्लत्वम्,\n'
        '  शुक्लता**; कार्ष्ण्यम्, कृष्णिमा. **षकारो ङीषर्थः** — the ष is for\n'
        '  the feminine: औचिती, याथाकामी\n'
        '\n'
        'SETTLED — वर्णदृढादिभ्यः ष्यञ् च, the दृढादि half. **दार्ढ्यम्,\n'
        '  द्रढिमा, दृढत्वम्, दृढता**. दृढ, परिवृढ, भृश, कृश, चक्र, आम्र,\n'
        '  लवण, ताम्र, अम्ल, शीत, उष्ण, जड, बधिर, पण्डित, मधुर, मूर्ख, मूक,\n'
        '  **वेर्यातलाभमतिमनःशारदानाम्** (ग०सू०११४), **समो मतिमनसोः**\n'
        '  (ग०सू०११५) — दृढादिः'
    ),
    '5.1.124': (
        'SETTLED — गुणवचनब्राह्मणादिभ्यः कर्मणि च; the गुणवचन half.\n'
        '  **गुणमुक्तवन्तो गुणवचनाः** — the words that have spoken a quality.\n'
        '  And the च adds a second sense: **कर्मशब्दः क्रियावचनः**, कर्मन्\n'
        '  here means an ACTIVITY. जडस्य भावः कर्म वा **जाड्यम्**. **आ\n'
        '  पादपरिसमाप्तेर्भावकर्माधिकारः** — and from here the भाव-and-कर्मन्\n'
        '  sense governs to the END OF THE PĀDA, so every rule after this one\n'
        '  has both\n'
        '\n'
        'SETTLED — गुणवचनब्राह्मणादिभ्यः कर्मणि च, the ब्राह्मणादि half — and\n'
        '  the list is open. **ब्राह्मणादिराकृतिगणः; आदिशब्दः प्रकारवचनः**:\n'
        '  an आकृतिगण, a list defined by its shape and not its members, and\n'
        '  the word *and the rest* means *and things of that kind*.\n'
        '  **ब्राह्मण्यम्**, माणव्यम्. **चातुर्वर्ण्यादीनां स्वार्थ\n'
        '  उपसंख्यानम्** adds a set in their OWN sense: **चत्वार एव वर्णाश्\n'
        '  चातुर्वर्ण्यम्**, the four classes as such; त्रैलोक्यम्,\n'
        '  षाड्गुण्यम्, सैन्यम्, सामीप्यम्, औपम्यम्, सौख्यम्'
    ),
    '5.1.125': (
        'SETTLED — स्तेनाद् यन्नलोपश्च — the affix and the dropping of the न्\n'
        '  together. स्तेनस्य भावः कर्म वा **स्तेयम्**, theft. **स्तेनादिति\n'
        '  केचिद् योगविभागं कुर्वन्ति** — some split the rule in two:\n'
        '  **स्तेनात् ष्यञ् भवति**, स्तैन्यम्, **ततो यन्नलोपश्च**, स्तेयम्.\n'
        '  Two forms where the unsplit rule gives one'
    ),
    '5.1.126': (
        'SETTLED — सख्युर्यः. सख्युर्भावः कर्म वा **सख्यम्**, friendship.\n'
        '  **दूतवणिग्भ्यां चेति वक्तव्यम्** adds two: दूत्यम्, वणिज्यम्.\n'
        '  **कथं वाणिज्यम्? ब्राह्मणादित्वात्** — and the other form comes\n'
        '  from the open list of 5.1.124'
    ),
    '5.1.127': (
        'SETTLED — कपिज्ञात्योर्ढक्. कपेर्भावः कर्म वा **कापेयम्**;\n'
        '  **ज्ञातेयम्**, kinship. **यथासंख्यम् अर्थयोः सर्वत्रैवात्र प्रकरणे\n'
        '  न इष्यते** — and the matching in order is not wanted anywhere in\n'
        '  this section BETWEEN THE TWO SENSES. So each of भाव and कर्मन्\n'
        '  goes with each base, and no rule of the stretch pairs them off'
    ),
    '5.1.128': (
        'SETTLED — पत्यन्तपुरोहितादिभ्यो यक्; the पत्यन्त half — from any\n'
        '  stem ending in पति. सेनापतेर्भावः कर्म वा **सैनापत्यम्**;\n'
        '  गार्हपत्यम्, प्राजापत्यम्\n'
        '\n'
        'SETTLED — पत्यन्तपुरोहितादिभ्यो यक्, the पुरोहितादि half.\n'
        '  **पौरोहित्यम्, राज्यम्**. पुरोहित, राजन्, संग्रामिक, एषिक, वर्मित,\n'
        '  खण्डिक, दण्डिक, छत्रिक, बाल, मन्द, कृषिक, पत्रिक, सूचिक, सारथिक,\n'
        '  अञ्जलिक, **राजासे** (ग०सू०११९) — पुरोहितादिः'
    ),
    '5.1.129': (
        'SETTLED — प्राणभृज्जातिवयोवचनोद्गात्रादिभ्योऽञ्; the प्राणभृज्जाति\n'
        '  half — from the words for KINDS of living creature. अश्वस्य भावः\n'
        '  कर्म वा **आश्वम्**; औष्ट्रम्\n'
        '\n'
        'SETTLED — प्राणभृज्जातिवयोवचनोद्गात्रादिभ्योऽञ्, the वयोवचन half —\n'
        '  from the words for stages of life. **कौमारम्, कैशोरम्**\n'
        '\n'
        'SETTLED — प्राणभृज्जातिवयोवचनोद्गात्रादिभ्योऽञ्, the उद्गात्रादि\n'
        '  half — priests and a few besides. **औद्गात्रम्, औन्नेत्रम्**.\n'
        '  उद्गातृ, उन्नेतृ, प्रतिहर्तृ, रथगणक, पक्षिगणक, सुष्ठु, दुष्ठु,\n'
        '  अध्वर्यु, वधू, **सुभग मन्त्रे** (ग०सू०१२०) — उद्गात्रादिः'
    ),
    '5.1.130': (
        'SETTLED — हायनान्तयुवादिभ्योऽण्; the हायनान्त half. द्विहायनस्य भावः\n'
        '  कर्म वा **द्वैहायनम्**; त्रैहायनम्\n'
        '\n'
        'SETTLED — हायनान्तयुवादिभ्योऽण्, the युवादि half. **यौवनम्,\n'
        '  स्थाविरम्**. **श्रोत्रियस्य यलोपश्च वाच्यः** — and श्रोत्रिय drops\n'
        '  its य: **श्रौत्रम्**. युवन्, स्थविर, होतृ, यजमान, कमण्डलु, सुहृद्,\n'
        '  यातृ, श्रवण, कुस्त्री, सुभ्रातृ, वृषल, क्षेत्रज्ञ, परिव्राजक,\n'
        '  कुशल, चपल, निपुण, पिशुन, सब्रह्मचारिन्, कुतूहल, अनृशंस — युवादिः'
    ),
    '5.1.131': (
        'SETTLED — इगन्ताच्च लघुपूर्वात् — and the vṛtti gives two analyses\n'
        '  of the compound. On the first, **लघुः पूर्वो यस्मादिकः तदन्तात्\n'
        '  प्रातिपदिकात्**: from a stem ending in an इक् that has a LIGHT\n'
        '  sound before it — **इक्संनिधानादिक इति विज्ञायते**, the *it* being\n'
        '  the इक् from its standing next to it. **अपरे तत्पुरुषकर्मधारयं\n'
        '  वर्णयन्ति**, and on that reading **अस्मिन्\n'
        '  व्याख्यानेऽन्तग्रहणमतिरिच्यते; लघुपूर्वादिक इत्येतावदेव वाच्यं\n'
        '  स्यात्** — the word अन्त would be redundant. A reading rejected\n'
        '  because it makes a word of the sūtra idle. शुचेर्भावः कर्म वा\n'
        '  **शौचम्**; मौनम्, नागरम्, पाटवम्, लाघवम्. **इगन्तादिति किम्?**\n'
        '  पटत्वम्. **लघुपूर्वादिति किम्?** कण्डूत्वम्, पाण्डुत्वम्. **कथं\n'
        '  काव्यम्? ब्राह्मणादिषु कविशब्दो द्रष्टव्यः** — and the open list\n'
        '  of 5.1.124 catches what this rule misses'
    ),
    '5.1.132': (
        'SETTLED — योपधाद् गुरूपोत्तमाद् वुञ् — and उपोत्तम is defined on the\n'
        '  spot. **त्रिप्रभृतीनाम् अन्तस्य समीपम् उपोत्तमम्** — in a word of\n'
        '  three syllables or more, the one next to the last; **गुरुरुपोत्तमं\n'
        '  यस्य तद् गुरूपोत्तमम्**, and that syllable must be heavy. रमणीयस्य\n'
        '  भावः कर्म वा **रामणीयकम्**; वासनीयकम्. **योपधादिति किम्?**\n'
        '  विमानत्वम्. **गुरूपोत्तमादिति किम्?** क्षत्रियत्वम्. **सहायाद्\n'
        '  वेति वक्तव्यम्**: साहायकम्, साहाय्यम्'
    ),
    '5.1.133': (
        'SETTLED — द्वन्द्वमनोज्ञादिभ्यश्च; the द्वन्द्व half — from a\n'
        '  copulative compound. गोपालपशुपालानां भावः कर्म वा\n'
        '  **गौपालपशुपालिका**; शैष्योपाध्यायिका, कौत्सकुशिकिका\n'
        '\n'
        'SETTLED — द्वन्द्वमनोज्ञादिभ्यश्च, the मनोज्ञादि half. **मानोज्ञकम्,\n'
        '  काल्याणकम्**. मनोज्ञ, कल्याण, प्रियरूप, छान्दस, छात्र, मेधाविन्,\n'
        '  अभिरूप, आढ्य, कुलपुत्र, श्रोत्रिय, चोर, धूर्त, वैश्वदेव, युवन्,\n'
        '  ग्रामपुत्र, अमुष्यपुत्र, शतपुत्र, कुशल — मनोज्ञादिः'
    ),
    '5.1.134': (
        'SETTLED — गोत्रचरणाच्छ्लाघात्याकारतदवेतेषु — three settings, each\n'
        '  glossed. **श्लाघा विकत्थनम्**, boasting; **अत्याकारः\n'
        '  पराधिक्षेपः**, running others down; **तदवेतस्तत्प्राप्तस्तज्ज्ञो\n'
        '  वा**, one who has come to it or knows it. **गार्गिकया श्लाघते** —\n'
        '  boasts of being a Gārgya, **गार्ग्यत्वेन विकत्थत इत्यर्थः**;\n'
        '  **गार्गिकयात्याकुरुते**, uses it to put others down;\n'
        '  **गार्गिकामवेतः**, has come into it. **श्लाघादिष्विति किम्?**\n'
        '  गार्ग्यत्वम्, कठत्वम् — outside those three it is the plain त्व'
    ),
    '5.1.135': (
        'SETTLED — होत्राभ्यश्छः. **होत्राशब्द ऋत्विग्विशेषवचनः** — होत्रा\n'
        '  names a PARTICULAR kind of officiant. अच्छावाकस्य भावः कर्म वा\n'
        '  **अच्छावाकीयम्**; मित्रावरुणीयम्, ब्राह्मणाच्छंसीयम्,\n'
        '  आग्नीध्रीयम्, पोत्रीयम्. **बहुवचनं स्वरूपविधिनिरासार्थम्** — the\n'
        '  plural in the sūtra is there to stop the rule applying to the WORD\n'
        '  होत्रा itself'
    ),
    '5.1.136': (
        'SETTLED — ब्रह्मणस्त्वः, छस्यापवादः — and the last rule of the pāda.\n'
        '  **होत्राभ्य इत्यनुवर्तते**, so the ब्रह्मन् meant is the officiant\n'
        '  of that name. ब्रह्मणो भावः कर्म वा **ब्रह्मत्वम्**. **AND THE\n'
        '  AFFIX IS NAMED WHERE A REFUSAL WOULD HAVE DONE.** **नेति वक्तव्ये\n'
        '  त्ववचनं तलो बाधनार्थम्** — the rule could have said *not छ*, and\n'
        '  the त्व would have come by 5.1.119 anyway. Naming त्व instead\n'
        '  shuts out the तल् that would have come with it. A प्रतिषेध would\n'
        '  have left two affixes; a विधि leaves one. **यस्तु जातिशब्दो\n'
        '  ब्राह्मणपर्यायो ब्रह्मन्शब्दः, ततस्त्वतलौ भवत एव** — and where\n'
        '  ब्रह्मन् is the ordinary word for a brahmin, both come back:\n'
        '  ब्रह्मत्वम्, ब्रह्मता. **भवनावधिकयोर्नञ्स्नञोरधिकारः समाप्तः** —\n'
        '  and with that the heading closes. इति श्रीजयादित्यविरचितायां\n'
        '  काशिकायां वृत्तौ पञ्चमाध्यायस्य प्रथमः पादः'
    ),
}

_FIT_FOR_LINE = (
    'fit_for(stem, gana=..., sense=..., case=..., result=..., '
    'samjna=..., stem_final=..., uttarapada=..., pre=..., '
    'compounded=..., wants=...) -> which affix comes for what a '
    'thing is good for, made for, might belong to, or is worth.'
)

#: 5.1.5, 5.1.12, 5.1.16 and the sense-rules after them leave
#: the affix yathavihitam, and the resolver executes that by
#: asking again as though the rule were not there. That
#: fall-through happens INSIDE fit_for, so it is not a reuse
#: edge: an edge is one codified rule reaching another rule's
#: FUNCTION, and here there is only one function. The walk says
#: so, and it is right.
_REUSES = {}

for _sutra, _notes in _RULES.items():
    register(
        _sutra,
        apply=fit_for,
        codification=_FIT_FOR_LINE,
        notes=_notes,
        reuses=_REUSES.get(_sutra, ()),
    )
