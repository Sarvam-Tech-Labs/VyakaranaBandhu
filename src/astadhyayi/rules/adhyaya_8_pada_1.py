# -*- coding: utf-8 -*-
"""अध्याय ८, पाद १ — the word said twice, and the accent taken away."""

from __future__ import annotations

from src.astadhyayi.amredita import doubles
from src.astadhyayi.nighata import after_a_pada
from src.astadhyayi.nighata_sesa import in_the_sentence
from src.astadhyayi.sources import register


_DOUBLES = (
    'doubles(word, gana=..., sense=..., position=..., chandasi=...) '
    '-> what is said twice and what the pair then counts as, by '
    'rule of 8.1.1-15.'
)

register(
    '8.1.1',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — सर्वस्य द्वे — the heading अध्याय ८ opens on: **सर्वस्येति\n'
        '  च द्वे इति च एतद् अधिकृतं वेदितव्यम्। इत उत्तरं यद् वक्ष्यामः\n'
        '  प्राक् पदस्य इत्यतः** — everything down to just before 8.1.16 is\n'
        '  about a WHOLE word being said twice.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI SETTLES AT ONCE WHAT THE TWO ARE.** **के\n'
        '  द्वे भवतः? ये शब्दतश् च अर्थतश् च उभयथा अन्तरतमे** — nearest in\n'
        '  sound and nearest in sense, both at once, so that **एकस्य\n'
        '  पचतिशब्दस्य द्वौ पचतिशब्दौ भवतः**. Without that the substitution\n'
        '  rule would let any word stand for any other. पचतिपचति;\n'
        '  ग्रामोग्रामो रमणीयः.\n'
        '\n'
        'SETTLED — **AND सर्वस्य IS THE WORD THAT MAKES IT A WHOLE WORD.**\n'
        '  The doubling of 6.1.1, which every reduplicated stem in अध्याय ७\n'
        '  came from, copies ONE syllable; this copies everything. The two\n'
        '  rules share a name and nothing else'
    ),
)

register(
    '8.1.2',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — तस्य परमाम्रेडितम् — of what has been said twice, the\n'
        '  LATER of the two is called आम्रेडित: **चौरचौर३, वृषलवृषल३,\n'
        '  दस्योदस्यो३ घातयिष्यामि त्वा**. The name is what the next rule and\n'
        '  8.2.95 आम्रेडितं भर्त्सने speak to, and it is given to the second\n'
        '  copy alone — the first stays an ordinary word'
    ),
)

register(
    '8.1.3',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — अनुदात्तं च — and what is called आम्रेडित is अनुदात्त\n'
        '  throughout: **भुङ्क्तेभुङ्क्ते, पशून्पशून्**. This is what makes a\n'
        '  doubled word one thing to the ear rather than two: the second copy\n'
        '  has no accent of its own left, so the pair carries a single high\n'
        '  tone between them'
    ),
)

register(
    '8.1.4',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — नित्यवीप्सयोः — a word doubles in the sense of CONSTANCY\n'
        '  or of DISTRIBUTION: **पचतिपचति, जल्पतिजल्पति; भुक्त्वाभुक्त्वा\n'
        '  व्रजति; लुनीहिलुनीहि इत्येवायं लुनाति**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI HAS TO SAY WHERE CONSTANCY CAN LIVE.**\n'
        '  **केषु नित्यता? तिङ्षु नित्यता अव्ययकृत्सु च** — in finite verbs\n'
        '  and in indeclinable kṛt forms, and the reason is that constancy is\n'
        '  a property of an ACTION: **आभीक्ष्ण्यं च क्रियाधर्मः। यां क्रियां\n'
        '  कर्ता प्राधान्येन अनुपरमन् करोति तन् नित्यम्** — what the agent\n'
        '  goes on doing without stopping. वीप्सा wants a noun instead, and\n'
        '  gives ग्रामोग्रामो रमणीयः'
    ),
)

register(
    '8.1.5',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — परेर्वर्जने — परि doubles in the sense of LEAVING OUT:\n'
        '  **परिपरि त्रिगर्तेभ्यो वृष्टो देवः; परिपरि सौवीरेभ्यः; परिपरि\n'
        '  सर्वसेनेभ्यः** — it rained everywhere except on the Trigartas.\n'
        '  **वर्जनं परिहारः**.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA MAKES IT OPTIONAL OUTSIDE A COMPOUND AND\n'
        '  IMPOSSIBLE INSIDE ONE.** **परेर्वर्जनेऽसमासे वा इति वक्तव्यम्** —\n'
        '  परि त्रिगर्तेभ्यः stands beside the doubled form; and in a\n'
        '  compound it cannot come at all, **समासे तु तेनैव उक्तत्वाद्\n'
        '  वर्जनस्य नैव भवति**, since परित्रिगर्तं वृष्टो देवः has already\n'
        '  said the exclusion by compounding'
    ),
)

register(
    '8.1.6',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — प्रसमुपोदः पादपूरणे — प्र, सम्, उप and उद् double to FILL\n'
        '  OUT a metrical quarter, and only if the doubling is what fills it:\n'
        '  **द्विर्वचनेन चेत् पादः पूर्यते**. **प्रप्रायम् अग्निर् भरतस्य\n'
        '  शृण्वे; संसमिद् युवसे वृषन्; उपोप मे परा मृश; किं नो दुदु हर्षसे\n'
        '  दातवा उ**. The vṛtti reads the restriction to the Veda out of the\n'
        "  rule's own sense rather than out of a word in it — **सामर्थ्यात्\n"
        '  छन्दसि एव एतद् विधानम्**, since ordinary speech has no quarters to\n'
        '  fill'
    ),
)

register(
    '8.1.7',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — उपर्यध्यधसः सामीप्ये — उपरि, अधि and अधस् double in the\n'
        '  sense of NEARNESS: **उपर्युपरि दुःखम्; उपर्युपरि ग्रामम्; अध्यधि\n'
        '  ग्रामम्; अधोऽधो नगरम्**. **सामीप्यं प्रत्यासत्तिः कालकृता देशकृता\n'
        '  च** — nearness made by time or by place, either one. The pot held\n'
        '  over the head is the sharpest counter-case: उपरि is there in its\n'
        '  plain sense of ABOVE, and no doubling comes'
    ),
)

register(
    '8.1.8',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — वाक्यादेरामन्त्रितस्यासूयासम्मतिकोपकुत्सनभर्त्सनेषु — a\n'
        '  VOCATIVE at the head of a sentence doubles in five senses: envy,\n'
        '  approval, anger, contempt and threat. **माणवक३ माणवक, अभिरूपक३\n'
        '  अभिरूपक रिक्तं त आभिरूप्यम्** of envy.\n'
        '\n'
        "SETTLED — **AND ALL FIVE ARE THE SPEAKER'S AND NONE OF THEM THE\n"
        '  THING SPOKEN OF.** **एते च प्रयोक्तृधर्माः, न अभिधेयधर्माः** —\n'
        '  nothing about the boy makes the vocative double; what does is the\n'
        '  mood of whoever is calling him. And वाक्य is defined for the\n'
        '  occasion: **एकार्थः पदसमूहः वाक्यम्**, a group of words with one\n'
        '  meaning'
    ),
)

register(
    '8.1.9',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — एकं बहुव्रीहिवत् — एक said twice behaves like a बहुव्रीहि:\n'
        '  **एकैकम् अक्षरं पठति; एकैकया आहुत्या जुहोति**. **बहुव्रीहिवत्त्वे\n'
        '  प्रयोजनं सुब्लोपपुंवद्भावौ** — the case ending of the first member\n'
        '  goes and the feminine reverts to the masculine, which is the whole\n'
        '  of what the comparison buys.\n'
        '\n'
        'SETTLED — **AND THE LIKENESS IS NOT A MEMBERSHIP.**\n'
        '  **सर्वनामसंज्ञाप्रतिषेधस्वरसमासान्ताः समासाधिकारविहिते बहुव्रीहौ\n'
        '  विज्ञायन्ते। तेन आतिदेशिके बहुव्रीहौ न भवन्ति** — the pronoun\n'
        '  refusal of 1.1.29, the accent and the compound endings belong to a\n'
        '  real बहुव्रीहि and not to one made by a likeness, so एकैकस्मै\n'
        '  keeps the pronoun ending'
    ),
)

register(
    '8.1.10',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — आबाधे च — and in the sense of DISTRESS: **गतगतः,\n'
        '  नष्टनष्टः, पतितपतितः**, and in the feminine **गतगता, नष्टनष्टा,\n'
        '  पतितपतिता**, the pair again behaving like a बहुव्रीहि. **आबाधनम्\n'
        '  आबाधः, पीडा प्रयोक्तृधर्मः, न अभिधेयधर्मः** — the pain is the\n'
        "  speaker's, as the five senses of 8.1.8 were: **प्रियस्य\n"
        '  चिरगमनादिना पीड्यमानः कश्चिद् एवं प्रयुङ्क्ते**, someone worn down\n'
        "  by a loved one's long absence says गतगतः"
    ),
)

register(
    '8.1.11',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — कर्मधारयवद् उत्तरेषु — and from here on the doublings\n'
        '  behave like a कर्मधारय instead: **इत उत्तरेषु द्विर्वचनेषु\n'
        '  कर्मधारयवत् कार्यं भवति इत्येतद् वेदितव्यम्**. What it buys is one\n'
        "  thing more than 8.1.9's likeness:\n"
        '  **सुब्लोपपुंवद्भावान्तोदात्तत्वानि** — the case ending goes\n'
        '  (पटुपटुः, मृदुमृदुः), the feminine reverts (पटुपट्वी, कालककालिका),\n'
        '  and the accent falls on the last syllable (पटुपटुः).\n'
        '\n'
        'SETTLED — **AND THE REVERSION REACHES A क-FINAL STEM BECAUSE OF THE\n'
        '  LIKENESS AND NOT IN SPITE OF IT.** **कोपधाया अपि हि\n'
        '  कर्मधारयवद्भावात् 6.3.42 इति पुंवद्भावो भवति** — कालककालिका comes\n'
        '  out that way only because the pair counts as a कर्मधारय for that\n'
        "  rule's purposes too"
    ),
)

register(
    '8.1.12',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — प्रकारे गुणवचनस्य — a QUALITY-word doubles in the sense of\n'
        '  a SORT: **पटुपटुः, मृदुमृदुः, पण्डितपण्डितः**, which the vṛtti\n'
        '  glosses **अपरिपूर्णगुण इत्यर्थः** — not quite clever, said of the\n'
        '  lesser when the fuller is the measure. **प्रकारो भेदः सादृश्यं\n'
        '  च**, and it is the likeness and not the difference that is taken\n'
        '  here.\n'
        '\n'
        'SETTLED — **AND IT DOES NOT DISPLACE THE AFFIX THAT SAYS THE SAME\n'
        '  THING.** **जातीयरः अनेन द्विर्वचनेन बाधनं न इष्यते** — पटुजातीयः\n'
        '  and मृदुजातीयः stand beside the doubled forms, and the option is\n'
        '  carried down from the sūtra after: **वक्ष्यमाणम्\n'
        '  अन्यतरस्यांग्रहणम्**'
    ),
)

register(
    '8.1.13',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — अकृच्छ्रे प्रियसुखयोरन्यतरस्याम् — प्रिय and सुख double\n'
        '  OPTIONALLY where ease is to be conveyed: **प्रियप्रियेण ददाति;\n'
        '  सुखसुखेन ददाति**, beside प्रियेण ददाति and सुखेन ददाति. **कृच्छ्रं\n'
        '  दुःखम्, तदभावः अकृच्छ्रम्** — and the sense is **अखिद्यमानो\n'
        "  ददाति**, he gives without being put out. It is this sūtra's\n"
        '  अन्यतरस्याम् that the rule before borrows to keep पटुजातीयः alive'
    ),
)

register(
    '8.1.14',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — यथास्वे यथायथम् — **यथायथम्** is laid down in the sense of\n'
        '  यथास्व: **यो य आत्मा, यद् यद् आत्मीयम्, तत् तद् यथास्वम्**. Two\n'
        '  things are given at once — **यथाशब्दस्य द्विर्वचनं नपुंसकलिङ्गता च\n'
        '  निपात्यते**, the doubling of यथा and the neuter gender, neither of\n'
        '  which any rule would supply. **ज्ञाताः सर्वे पदार्था यथायथम्**,\n'
        '  each according to its own nature; **सर्वेषां तु यथायथम्**, each\n'
        '  according to what is his'
    ),
)

register(
    '8.1.15',
    apply=doubles,
    codification=_DOUBLES,
    notes=(
        'SETTLED — द्वन्द्वं\n'
        '  रहस्यमर्यादावचनव्युत्क्रमणयज्ञपात्रप्रयोगाभिव्यक्तिषु —\n'
        '  **द्वन्द्वम्** is laid down in five senses, and THREE separate\n'
        '  departures go into the one word: **द्विशब्दस्य द्विर्वचनम्,\n'
        '  पूर्वपदस्य आम्भावः, अत्वं च उत्तरपदस्य निपात्यते** — द्वि is\n'
        '  doubled, the first member takes आम् and the second becomes अ.\n'
        '\n'
        'SETTLED — **AND ONLY ONE OF THE FIVE SENSES IS WHAT THE WORD\n'
        '  MEANS.** **तत्र रहस्यं द्वन्द्वशब्दवाच्यम्, इतरे विषयभूताः** —\n'
        '  secrecy is what द्वन्द्वम् SAYS, and the other four are occasions\n'
        '  on which it is said. **द्वन्द्वं मन्त्रयन्ते** of secrecy;\n'
        '  **आचतुरं ही इमे पशवो द्वन्द्वं मिथुनीयन्ति** of a limit not\n'
        '  overstepped'
    ),
)


_AFTER_A_PADA = (
    'after_a_pada(gana=..., after=..., joined=..., case=..., sense=..., '
    'position=..., chandasi=...) -> what loses its accent after a '
    'word and what keeps it, by rule of 8.1.16-50.'
)

register(
    '8.1.16',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — पदस्य — a heading, and the longest of the three this pāda\n'
        '  opens: **पदस्येत्ययम् अधिकारः प्राग् अपदान्ताधिकारात्**, running\n'
        '  from here to 8.3.55. What is said from here on is said OF A WORD\n'
        '  and not of a stem or an affix — **वक्ष्यति संयोगान्तस्य लोपः,\n'
        '  पचन्, यजन्; पदस्येति किम्? पचन्तौ, यजन्तौ**.\n'
        '\n'
        'SETTLED — **AND THE GENITIVE IN IT IS READ TWO WAYS.**\n'
        '  **वक्ष्यमाणवाक्यापेक्षया पदस्य अधिकृतस्य षष्ठ्यर्थव्यवस्था\n'
        '  द्रष्टव्या — क्वचित् स्थानषष्ठी क्वचिद् अवयवषष्ठी** — sometimes it\n'
        '  names what a substitute stands FOR and sometimes the whole a part\n'
        '  belongs to, and which one is settled by the sūtra that borrows it'
    ),
)

register(
    '8.1.17',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — पदात् — and a second heading over the first: **पदाद्\n'
        '  इत्ययम् अधिकारः प्राक् कुत्सने च सुप्यगोत्रादौ इत्येतस्मात्**,\n'
        '  from here to 8.1.68. It says what must stand BEFORE — **वक्ष्यति\n'
        '  आमन्त्रितस्य च। आमन्त्रितस्य पदात् परस्य अनुदात्तादेशो भवति इति।\n'
        '  पचसि देवदत्त**. And the test of it is the same example turned\n'
        '  round: **पदाद् इति किम्? देवदत्त पचसि** — with the vocative first\n'
        '  there is no word in front of it, and its accent stays'
    ),
)

register(
    '8.1.18',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — अनुदात्तं सर्वम् अपादादौ — the third heading, and it\n'
        '  carries THREE words down at once: **अनुदात्तम् इति च, सर्वम् इति\n'
        '  च, अपादादाव् इति च। एतत् त्रयम् अधिकृतं वेदितव्यम् आ\n'
        '  पादपरिसमाप्तेः** — toneless, WHOLLY, and not at the head of a\n'
        '  metrical quarter. सर्वम् is why पचसि देवदत्त loses every\n'
        "  syllable's accent and not one; अपादादौ is why **यत् ते नियानं रजसं\n"
        '  मृत्यो अनवधर्ष्यम्** keeps its own, standing where a quarter\n'
        '  begins'
    ),
)

register(
    '8.1.19',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — आमन्त्रितस्य च — a VOCATIVE that stands after a word, and\n'
        '  not at the head of a quarter, is toneless throughout: **पचसि\n'
        '  देवदत्त; पचसि यज्ञदत्त**. It is stated against 6.1.198, which\n'
        '  would have given the vocative an accent on its first syllable —\n'
        '  **आमन्त्रिताद्युदात्तत्वे प्राप्ते वचनम्**.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA CONFINES IT TO ONE SENTENCE.**\n'
        '  **समानवाक्ये निघातयुष्मदस्मदादेशा वक्तव्याः** — the toneless\n'
        '  vocative, and the enclitics of the four sūtras after, want the two\n'
        '  words in ONE sentence. **ओदनं पच तव भविष्यति** keeps तव, the two\n'
        '  clauses being separate; **इह देवदत्त माता ते कथयति** takes the\n'
        '  enclitic, being one'
    ),
)

register(
    '8.1.20',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ — युष्मद्\n'
        '  and अस्मद् standing in the genitive, dative or accusative DUAL\n'
        '  become वाम् and नौ, one to one: **ग्रामो वां स्वम्; जनपदो नौ\n'
        '  स्वम्; ग्रामो वां दीयते; ग्रामो वां पश्यति**. The two are toneless\n'
        '  because 8.1.18 says so, and the sūtra does not have to.\n'
        '  **एकवचनबहुवचनान्तयोर् आदेशान्तरविधानाद् द्विवचनान्तयोर् एतौ आदेशौ\n'
        '  विज्ञायेते** — the singular and the plural get substitutes of\n'
        '  their own in the next two sūtras, and that is how the dual is\n'
        '  known to be meant here'
    ),
)

register(
    '8.1.21',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — बहुवचने वस्नसौ — and in the PLURAL they become वस् and\n'
        '  नस्: **ग्रामो वः स्वम्; जनपदो नः स्वम्; ग्रामो वो दीयते; ग्रामो वः\n'
        '  पश्यति**. All three cases again, and the accent again from the\n'
        '  heading rather than from the rule'
    ),
)

register(
    '8.1.22',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — ते मयावेकवचनस्य — and in the SINGULAR ते and मे, but only\n'
        '  in the genitive and dative: **ग्रामस् ते स्वम्; ग्रामो मे स्वम्;\n'
        '  ग्रामस् ते दीयते**. The accusative is left out, and the reason is\n'
        '  that the next sūtra gives it something else — **द्वितीयान्तस्य\n'
        '  आदेशान्तरविधानसामर्थ्यात् षष्ठीचतुर्थ्योर् एव अयं योगः**'
    ),
)

register(
    '8.1.23',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — त्वामौ द्वितीयायाः — and in the singular ACCUSATIVE त्वा\n'
        '  and मा: **ग्रामस् त्वा पश्यति; ग्रामो मा पश्यति**. एकवचनस्य is\n'
        '  carried down from the sūtra before, so the whole of what युष्मद्\n'
        '  and अस्मद् do in these three cases is said in four sūtras and\n'
        '  eight substitutes'
    ),
)

register(
    '8.1.24',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — न चवाहाहैवयुक्ते — but NOT where the word is construed\n'
        '  with च, वा, ह, अह or एव: **ग्रामस् तव च स्वम्; ग्रामो मम च स्वम्;\n'
        '  युष्माकं च स्वम्; ग्रामस् तुभ्यं च दीयते**. **पूर्वेण प्रकरणेन\n'
        '  प्राप्ताः प्रतिषिध्यन्ते** — the four rules before had supplied\n'
        '  the enclitics and this takes all four back at once. The list is\n'
        '  the one 8.1.58 and 8.1.63 later call चादि'
    ),
)

register(
    '8.1.25',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — पश्यार्थैश्च अनालोचने — nor where it is construed with a\n'
        '  verb of SEEING used of knowing and not of the eye: **ग्रामस् तव\n'
        '  स्वं समीक्ष्य आगतः; ग्रामस् त्वां समीक्ष्य आगतः**. The vṛtti\n'
        '  splits the two senses in a line — **दर्शनं ज्ञानम्। आलोचनं\n'
        '  चक्षुर्विज्ञानम्** — and the refusal is for the first, so that a\n'
        '  सम्+ईक्ष् of thinking keeps तव and one of looking does not'
    ),
)

register(
    '8.1.26',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — सपूर्वायाः प्रथमाया विभाषा — and OPTIONALLY after a\n'
        '  nominative that has a word before it: **ग्रामे कम्बलस् ते स्वम्,\n'
        '  ग्रामे कम्बलस् तव स्वम्; ग्रामे छात्रास् त्वा पश्यन्ति**. Both\n'
        '  forms stand, and what makes the option available at all is the\n'
        '  word before the nominative — a bare प्रथमा leaves the enclitic\n'
        '  compulsory'
    ),
)

register(
    '8.1.27',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — तिङो गोत्रादीनि कुत्सनाभीक्ष्ण्ययोः — the words of the\n'
        '  गोत्रादि class, standing after a finite verb, are toneless in the\n'
        '  sense of CONTEMPT or of REPETITION: **पचति गोत्रम्; जल्पति\n'
        '  गोत्रम्; पचतिपचति गोत्रम्**, and with ब्रुवम् for गोत्रम्\n'
        "  likewise. The doubled verb in the second set is 8.1.4's, so the\n"
        '  two runs of this pāda meet in one example. **ब्रुवः इति ब्रुवः कन्\n'
        '  निपातनात्** — the form is laid down with its own affix'
    ),
)

register(
    '8.1.28',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — तिङ्ङतिङः — **THE NIGHĀTA.** A finite verb standing after\n'
        '  a word that is NOT a finite verb loses its accent altogether:\n'
        '  **देवदत्तः पचति; यज्ञदत्तः पचति**, with पचति toneless throughout.\n'
        '\n'
        'SETTLED — **AND IT IS THE RULE THE REST OF THE PĀDA IS STATED\n'
        '  AGAINST.** From 8.1.29 to 8.1.66 almost every sūtra is a प्रतिषेध\n'
        '  of this one — a list of particles, senses and positions in which\n'
        '  the verb keeps what it had. Both words of the sūtra are tested and\n'
        '  both do work: **तिङ् इति किम्? नीलम् उत्पलम्; अतिङः इति किम्? भवति\n'
        '  पचति**, where the first word is itself a verb and the second is\n'
        '  spared'
    ),
)

register(
    '8.1.29',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — न लुट् — but the periphrastic future keeps its accent:\n'
        '  **श्वः कर्ता; श्वः कर्तारौ; मासेन कर्तारः**. **पूर्वेण अतिप्रसक्ते\n'
        '  प्रतिषेध आरभ्यते** — the rule before had reached too far and this\n'
        '  pulls it back.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI SAYS WHERE THE ACCENT THEN SITS.** **तासेः\n'
        '  परस्य लसार्वधातुकस्य अनुदात्तत्वे सति सर्वतासिर् एव उदात्तः। यत्र\n'
        '  तु टिलोपः, तत्र उदात्तनिवृत्तिस्वरो भवति** — with the ending\n'
        '  toneless the तास् carries the whole accent, and where the ending\n'
        '  is lost outright the accent falls back by 6.1.161'
    ),
)

register(
    '8.1.30',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — निपातैर्यद्यदिहन्तकुविन्नेच्चेच्चण्कच्चिद्यत्रयुक्तम् —\n'
        '  nor a verb construed with any of NINE particles: **यत् करोति; यदि\n'
        '  पचति; हन्त करोति; कुवित् करोति; नेज् जिह्मायन्त्यो नरके पताम; स\n'
        '  चेद् भुङ्क्ते; कच्चित् पचति; यत्र पचति**. This is the longest\n'
        '  single list of the run and the one later sūtras keep pointing back\n'
        "  to — 8.1.54 has to say that हन्त's refusal here is compulsory\n"
        '  while its own is optional'
    ),
)

register(
    '8.1.31',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — नह प्रत्यारम्भे — nor with नह in REMONSTRANCE: **नह\n'
        '  भोक्ष्यसे; नह अध्येष्यसे**. The sense is defined for the occasion\n'
        '  — **चोदितस्य अवधीरणे उपालिप्सया प्रतिषेधयुक्तः प्रत्यारम्भः\n'
        '  क्रियते** — one who has been urged to something brushes it aside,\n'
        '  and the speaker takes him up on it'
    ),
)

register(
    '8.1.32',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — सत्यं प्रश्ने — nor with सत्यम् in a QUESTION: **सत्यं\n'
        '  भोक्ष्यसे? सत्यम् अध्येष्यसे?** The same word in a statement\n'
        "  leaves the verb toneless, and the vṛtti's counter-example is a\n"
        '  whole line of the Atharvan to make the difference audible'
    ),
)

register(
    '8.1.33',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — अङ्गाप्रातिलोम्ये — nor with अङ्ग where nothing CONTRARY\n'
        '  is meant: **अङ्ग कुरु; अङ्ग पच; अङ्ग पठ**. Where the speaker is\n'
        '  set against what he names — **कूजनम् अनभिमतम् असौ कुर्वन्\n'
        '  प्रतिलोमो भवति** — the refusal lapses and 8.1.28 has its way'
    ),
)

register(
    '8.1.34',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — हि च — and with हि, under the same condition: **स हि कुरु;\n'
        '  स हि पच; स हि पठ**, and **अप्रातिलोम्ये इत्येव — स हि कूज३ वृषल**.\n'
        '  The sense is carried down from the sūtra before rather than said\n'
        '  again, which is what makes the pair one rule in two parts'
    ),
)

register(
    '8.1.35',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — छन्दस्यनेकम् अपि साकाङ्क्षम् — and in the Veda MORE THAN\n'
        '  ONE verb construed with हि keeps its accent, if the sense is still\n'
        '  expectant: **कदाचिद् एकं कदाचिद् अनेकम् इत्यर्थः**. Two together —\n'
        '  **अनृतं हि मत्तो वदति, पाप्मा एनं विपुनाति**, neither toneless;\n'
        '  and one only — **अग्निर् हि पूर्वम् उदजयत्, तम् इन्द्रोऽनूदजयत्**,\n'
        '  where both verbs stand with हि and the second is toneless all the\n'
        '  same'
    ),
)

register(
    '8.1.36',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — यावद्यथाभ्याम् — nor with यावत् or यथा: **यावद् भुङ्क्ते;\n'
        '  यथा भुङ्क्ते; यावद् अधीते; यथा अधीते**. And the particle need not\n'
        '  come first — **परेण अपि योगे भवति प्रतिषेधः; देवदत्तः पचति यावत्;\n'
        '  देवदत्तः पचति यथा** — which is why the two sūtras after it have to\n'
        '  say ANANTARA to get the refusal back'
    ),
)

register(
    '8.1.37',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — पूजायां न अनन्तरम् — but where the sense is PRAISE and the\n'
        '  verb stands NEXT to यावत् or यथा, the refusal lapses: **यावत् पचति\n'
        '  शोभनम्; यथा करोति चारु**, with the verb toneless after all.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI HAS TO SPELL OUT THE DOUBLE NEGATIVE.**\n'
        '  **न अनुदात्तं न भवति। किं तर्हि? अनुदात्तम् एव** — it is not that\n'
        '  it fails to be toneless; it is toneless. A refusal of a refusal is\n'
        '  an assertion, and the commentary will not let the reader take it\n'
        '  for anything else'
    ),
)

register(
    '8.1.38',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — उपसर्गव्यपेतं च — and where only a PREVERB stands between:\n'
        '  **यावत् प्रपचति शोभनम्; यथा प्रकरोति चारु**. **पूर्वम् अनन्तरम्\n'
        '  इत्युक्तम्, उपसर्गव्यवधानार्थोऽयम् आरम्भः** — the sūtra exists for\n'
        '  the gap a preverb makes and for nothing else, and a full word in\n'
        '  the gap still stops it: **यावद् देवदत्तः प्रपचति शोभनम्**'
    ),
)

register(
    '8.1.39',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — तुपश्यपश्यताहैः पूजायाम् — nor with तु, पश्य, पश्यत or अह\n'
        '  where the sense is PRAISE: **माणवकस् तु भुङ्क्ते शोभनम्; पश्य\n'
        '  माणवको भुङ्क्ते शोभनम्; अह माणवको भुङ्क्ते शोभनम्**.\n'
        '\n'
        'SETTLED — **AND पूजायाम् IS SAID TWICE OVER ON PURPOSE.** **पूजायाम्\n'
        '  इति वर्तमाने पुनः पूजायाम् इत्युच्यते निघातप्रतिषेधार्थम्** — the\n'
        '  word was already running down from 8.1.37, where it belonged to an\n'
        '  assertion; saying it again here attaches it to a refusal instead'
    ),
)

register(
    '8.1.40',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — अहो च — and with अहो in praise: **अहो देवदत्तः पचति\n'
        '  शोभनम्; अहो विष्णुमित्रः करोति चारु**. **पृथग्योगकरणम्\n'
        '  उत्तरार्थम्** — it is a separate sūtra only so that the next one\n'
        '  can take अहो up again in every OTHER sense'
    ),
)

register(
    '8.1.41',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — शेषे विभाषा — and with अहो in any sense BUT praise,\n'
        '  optionally: **कटम् अहो करिष्यसि; मम गेहम् अहो एष्यसि** —\n'
        '  **असूयावचनम् एतत्**, said in spite. **कश् च शेषः? यद् अन्यत्\n'
        '  पूजायाः**. The vṛtti notes that शेष did not strictly have to be\n'
        '  said at all, praise having stopped with the sūtra before —\n'
        '  **अनधिकारे सिद्धे शेषवचनं विस्पष्टार्थम्**, it is there for\n'
        '  clarity'
    ),
)

register(
    '8.1.42',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — पुरा च परीप्सायाम् — and with पुरा where HASTE is meant,\n'
        '  optionally: **परीप्सा त्वरा। अधीष्व माणवक, पुरा विद्योतते\n'
        '  विद्युत्; पुरा स्तनयति स्तनयित्नुः** — study, boy, before the\n'
        '  lightning flashes. **पुराशब्दोऽत्र भविष्यदासत्तिं द्योतयति** — the\n'
        '  word points at something close ahead, which is the opposite of\n'
        '  what it usually does'
    ),
)

register(
    '8.1.43',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — नन्वित्यनुज्ञैषणायाम् — and with ननु where LEAVE is being\n'
        '  asked: **ननु करोमि भोः; ननु गच्छामि भोः** — **अनुजानीष्व मां करणं\n'
        '  प्रति इत्यर्थः**, let me do it. **अनुज्ञायाः एषणा प्रार्थना\n'
        '  अनुज्ञैषणा**. The same words answering a question leave the verb\n'
        '  toneless'
    ),
)

register(
    '8.1.44',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — किं क्रियाप्रश्नेऽनुपसर्गम् अप्रतिषिद्धम् — and with किम्\n'
        '  in a question ABOUT AN ACTION, where the verb has no preverb and\n'
        '  no other refusal has already reached it: **किं देवदत्तः पचति,\n'
        '  आहोस्विद् भुङ्क्ते? किं देवदत्तः शेते, आहोस्विद् अधीते?**\n'
        '\n'
        'SETTLED — **AND THE VṚTTI RECORDS A DISAGREEMENT ABOUT THE SECOND\n'
        '  VERB.** **अत्र केचिद् आहुः — पूर्वं किंयुक्तम् इति तद् न निहन्यते,\n'
        '  उत्तरं तु न किंयुक्तम् इति तद् निहन्यत एव इति। अपरे तु आहुः** —\n'
        '  one party spares only the verb the किम् actually stands with,\n'
        '  another spares both, and the Kāśikā reports the two and settles\n'
        '  neither'
    ),
)

register(
    '8.1.45',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — लोपे विभाषा — and optionally where the किम् is there in\n'
        '  sense but not in sound: **क्व च अस्य लोपः? यत्र गम्यते च अर्थः, न\n'
        '  च प्रयुज्यते किंशब्दः** — **देवदत्तः पचति, आहोस्वित् पठति**, a\n'
        '  question with no interrogative in it. **प्राप्तविभाषा इयं किमर्थेन\n'
        '  योगात्** — the option is of something already available, since the\n'
        '  SENSE of किम् is present'
    ),
)

register(
    '8.1.46',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — एहिमन्ये प्रहासे लृट् — and a FUTURE construed with एहि\n'
        '  मन्ये in JEST: **प्रकृष्टो हासः प्रहासः, क्रीडा**. **एहि मन्ये\n'
        '  ओदनं भोक्ष्यसे, नहि भोक्ष्यसे, भुक्तः सोऽतिथिभिः** — come, you\n'
        '  think you will eat the rice; you will not, the guests have eaten\n'
        '  it. The whole idiom is one the rule exists to keep audible'
    ),
)

register(
    '8.1.47',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — जात्वपूर्वम् — and with जातु, provided nothing stands\n'
        '  before it: **जातु भोक्ष्यसे; जातु करिष्यामि**. **अपूर्वम् इति\n'
        '  किम्? कटं जातु करिष्यति** — with a word in front, the verb is\n'
        "  toneless as usual. The condition is about the PARTICLE's place in\n"
        "  the sentence and not the verb's, which is what makes it worth a\n"
        '  column'
    ),
)

register(
    '8.1.48',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — किम्वृत्तं च चिदुत्तरम् — and a किम्-form with चित् after\n'
        '  it and nothing before it: **कश्चिद् भुङ्क्ते; कश्चिद् भोजयति;\n'
        '  कस्मैचिद् ददाति; कतरश्चित् करोति; कतमश्चिद् भुङ्क्ते**.\n'
        '  **किम्वृत्तग्रहणेन तद्विभक्त्यन्तं प्रतीयात्, डतरडतमौ च प्रत्ययौ**\n'
        '  — the name covers किम् in any case AND the stems made from it with\n'
        '  डतर and डतम, which is why कतरश्चित् is in the list'
    ),
)

register(
    '8.1.49',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — आहो उताहो चानन्तरम् — and with आहो or उताहो, where the\n'
        '  verb stands NEXT to the particle and nothing stands before it:\n'
        '  **आहो भुङ्क्ते; उताहो भुङ्क्ते; आहो पठति**. Both conditions come\n'
        "  from elsewhere — अनन्तरम् is the sūtra's own word and अपूर्वम् is\n"
        '  carried down from 8.1.47, two sūtras back'
    ),
)

register(
    '8.1.50',
    apply=after_a_pada,
    codification=_AFTER_A_PADA,
    notes=(
        'SETTLED — शेषे विभाषा — and elsewhere, optionally: **कश् च शेषः? यद्\n'
        '  अन्यद् अनन्तरात्** — where a word stands between. **आहो देवदत्तः\n'
        '  पचति** beside **आहो देवदत्तः पचति** with the verb toneless;\n'
        '  **उताहो देवदत्तः पठति** likewise. It is the second शेषे विभाषा of\n'
        "  the pāda, the first being 8.1.41's, and each takes back what the\n"
        '  sūtra just before it had confined'
    ),
)


_IN_THE_SENTENCE = (
    'in_the_sentence(gana=..., after=..., before=..., joined=..., '
    'sense=..., position=..., chandasi=...) -> what loses its accent '
    'and what escapes, by rule of 8.1.51-74.'
)

register(
    '8.1.51',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — गत्यर्थलोटा लृण् न चेत् कारकं सर्वान्यत् — a FUTURE\n'
        '  construed with the imperative of a verb of motion keeps its\n'
        '  accent, provided the कारक is not wholly different: **आगच्छ\n'
        '  देवदत्त, ग्रामं द्रक्ष्यसि**. **यत्रैव कारके कर्तरि कर्मणि वा\n'
        '  लोट्, तत्रैव यदि लृड् अपि भवति इत्यर्थः** — the same agent or the\n'
        '  same object in both halves, and the vṛtti is careful that only\n'
        '  those two count: **कर्तृकर्मणी एव अत्र कारकग्रहणेन गृह्येते, न\n'
        '  करणादि कारकान्तरम्**'
    ),
)

register(
    '8.1.52',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — लोट् च — and an IMPERATIVE so construed: **आगच्छ देवदत्त,\n'
        '  ग्रामं पश्य; आगच्छ विष्णुमित्र, ग्रामं शाधि**, and in the passive\n'
        '  **आगम्यतां देवदत्तेन ग्रामो दृश्यतां यज्ञदत्तेन**. The condition\n'
        '  is the same one word for word — **लोडन्तयोर् एकं कारकं यदि भवति\n'
        '  इत्यर्थः** — so the pair of sūtras differs in nothing but which\n'
        '  tense is spared'
    ),
)

register(
    '8.1.53',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — विभाषितं सोपसर्गम् अनुत्तमम् — but where the imperative\n'
        '  has a PREVERB and is not first person, the sparing is only\n'
        '  optional: **आगच्छ देवदत्त ग्रामं प्रविश** beside **प्रविश** with\n'
        '  the accent kept; **आगच्छ देवदत्त ग्रामं प्रशाधि, प्रशाधि**.\n'
        '  **प्राप्तविभाषा इयम्** — what is made optional was already\n'
        '  available from the sūtra before'
    ),
)

register(
    '8.1.54',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — हन्त च — and with हन्त, an imperative with a preverb and\n'
        '  not first person, optionally: **हन्त प्रविश, प्रविश; हन्त प्रशाधि,\n'
        '  प्रशाधि**. **पूर्वं सर्वम् अनुवर्तते गत्यर्थलोटं वर्जयित्वा** —\n'
        '  everything is carried down except the verb of motion.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI HAS TO SAY WHY हन्त IS HERE AT ALL.** हन्त\n'
        "  was already in 8.1.30's list of nine, where the sparing is\n"
        '  compulsory — **निपातैर्यद्यदिहन्त० इति नित्यम् अत्र निघातप्रतिषेधो\n'
        '  भवति**. This sūtra is for the preverb case, where the option is\n'
        '  wanted'
    ),
)

register(
    '8.1.55',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — आम एकान्तरम् आमन्त्रितम् अनन्तिके — a VOCATIVE standing\n'
        '  after आम् with ONE word between, of someone not close by, keeps\n'
        "  its accent: **आम् पचसि देवदत्त३; आम् भो देवदत्त३**. It is 8.1.19's\n"
        '  refusal, and the vṛtti notes that भो counts as a vocative-final\n'
        '  word here — **भो इत्यामन्त्रितान्तम् अपि 8.1.73 इति न अविद्यमानवद्\n'
        '  भवति**, so the rule at the end of the pāda and this one meet'
    ),
)

register(
    '8.1.56',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — यद्धितुपरं छन्दसि — and in the VEDA a finite verb followed\n'
        '  by यत्, हि or तु keeps its accent: **गवां गोत्रम् उदसृजो यद्\n'
        '  अङ्गिरः; इन्दवो वाम् उशन्ति हि; आख्यास्यामि तु ते**. **आमन्त्रितम्\n'
        '  इत्येतद् अस्वरितत्वान् न अनुवर्तते** — the vocative of the sūtra\n'
        '  before is not carried down, being unmarked; तिङ् is. The same\n'
        '  three particles spare a verb they PRECEDE by 8.1.30 and 8.1.34,\n'
        '  and what is new here is that they may follow'
    ),
)

register(
    '8.1.57',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — चनचिदिवगोत्रादितद्धिताम्रेडितेष्वगतेः — a finite verb\n'
        '  keeps its accent before चन, चित्, इव, a गोत्रादि word, a taddhita\n'
        '  or an आम्रेडित, provided it does not itself stand after a गति:\n'
        '  **देवदत्तः पचति चन; पचति चित्; पचतीव; पचति गोत्रम्; पचति ब्रुवम्;\n'
        '  पचति प्रवचनम्**. The गोत्रादि here are the ones 8.1.27 named and\n'
        '  in the senses that sūtra named — **इह अपि गोत्रादयः\n'
        '  कुत्सनाभीक्ष्ण्ययोर् एव गृह्यन्ते** — so the two rules read each\n'
        '  other'
    ),
)

register(
    '8.1.58',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — चादिषु च — and before the चादि particles: **देवदत्तः पचति\n'
        '  च, खादति च; पचति वा, खादति वा; पचति ह; पचत्यह; पचत्येव**. **चादयो\n'
        '  न चवाहाहैवयुक्ते इत्यत्र ये निर्दिष्टाः, त इह परिगृह्यन्ते** — the\n'
        "  list is 8.1.24's five and not the whole चादि class of 1.4.57,\n"
        '  which is the only place in the pāda where a गण name is narrowed by\n'
        '  pointing at an earlier sūtra'
    ),
)

register(
    '8.1.59',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — चवायोगे प्रथमा — where two verbs are construed with च or\n'
        '  वा, the FIRST keeps its accent and the second does not:\n'
        '  **गर्दभांश् च कालयति, वीणां च वादयति; गर्दभान् वा कालयति, वीणां वा\n'
        '  वादयति**. Both words of the sūtra are load-bearing — **योगग्रहणं\n'
        '  पूर्वाभ्याम् अपि योगे निघातप्रतिषेधो यथा स्याद् इति; प्रथमाग्रहणं\n'
        '  द्वितीयादेस् तिङन्तस्य मा भूद् इति** — and अगतेः, carried down\n'
        '  into the sūtra before, stops here'
    ),
)

register(
    '8.1.60',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — हेति क्षियायाम् — and the first of two verbs construed\n'
        '  with ह, where a BREACH OF CUSTOM is meant: **क्षिया\n'
        '  धर्मव्यतिक्रमः, आचारभेदः**. **स्वयं ह रथेन याति३, उपाध्यायं पदातिं\n'
        '  गमयति; स्वयं ह ओदनं भुङ्क्ते३, उपाध्यायं सक्तून् पाययति** — he\n'
        '  rides while he makes his teacher walk. The प्लुत on the first verb\n'
        "  is 8.2.104's, and the two rules are cited side by side"
    ),
)

register(
    '8.1.61',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — अहेति विनियोगे च — and with अह where a DISTRIBUTIVE\n'
        '  ASSIGNMENT is meant, and by the च in the breach of custom as well:\n'
        '  **नानाप्रयोजनो नियोगो विनियोगः। त्वम् अह ग्रामं गच्छ, त्वम् अह\n'
        '  अरण्यं गच्छ** — you to the village and you to the forest, with the\n'
        '  first verb accented and the second not. The क्षिया examples are\n'
        "  the sūtra before's over again with अह for ह"
    ),
)

register(
    '8.1.62',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — चाहलोप एवेत्यवधारणम् — and where the च or the अह is there\n'
        '  in sense but not in sound, provided एव is used for EMPHASIS: **क्व\n'
        '  च अस्य लोपः? यत्र गम्यते च अर्थो न च प्रयुज्यते**. **देवदत्त एव\n'
        '  ग्रामं गच्छतु, स देवदत्त एव अरण्यं गच्छतु**. And the vṛtti tells\n'
        '  the two elisions apart by whose agent is whose — **समानकर्तृके\n'
        '  चलोपः, नानाकर्तृके अहलोपः**, since च joins and अह singles out'
    ),
)

register(
    '8.1.63',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — चादिलोपे विभाषा — and where any of the चादि is elided,\n'
        '  optionally: **शुक्ला व्रीहयो भवन्ति, श्वेता गा आज्याय दुहन्ति** —\n'
        '  भवन्ति keeps its accent or loses it. With वा elided, **व्रीहिभिर्\n'
        "  यजेत, यवैर् यजेत**. The list is again 8.1.24's, pointed at by name\n"
        '  — **चादयो न चवाहाहैवयुक्ते इति सूत्रनिर्दिष्टा गृह्यन्ते**'
    ),
)

register(
    '8.1.64',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — वैवावेति च च्छन्दसि — and with वै or वाव in the Veda,\n'
        '  optionally: **अहर् वै देवानाम् आसीद् रात्रिर् असुराणाम्;\n'
        '  बृहस्पतिर् वै देवानां पुरोहित आसीत् शण्डामर्कावसुराणाम्; अयं वाव\n'
        '  हस्त आसीत्, नेतर आसीत्**. In each pair the first verb is spared\n'
        '  and the second is not, which is the shape every rule from 8.1.59\n'
        '  has taken'
    ),
)

register(
    '8.1.65',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — एकान्याभ्यां समर्थाभ्याम् — and with एक and अन्य where\n'
        '  they are construed with the verb, optionally, in the Veda:\n'
        '  **प्रजाम् एका जिन्वत्य् ऊर्जम् एका राष्ट्रम् एका रक्षति\n'
        '  देवयूनाम्** — जिन्वति is spared on one alternative and not on the\n'
        '  other; **तयोर् अन्यः पिप्पलं स्वाद्वत्त्य् अनश्नन्न् अन्यो अभि\n'
        '  चाकशीति**, with अत्ति the same way'
    ),
)

register(
    '8.1.66',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — यद्वृत्तान्नित्यम् — a finite verb after ANY word with यद्\n'
        '  in it keeps its accent, and this one says ALWAYS: **यो भुङ्क्ते;\n'
        '  यं भोजयति; येन भुङ्क्ते**. **यत्र पदे यच्छब्दो वर्तते तत् सर्वं\n'
        '  यद्वृत्तम्** — every word containing यद्, however made.\n'
        '\n'
        'SETTLED — **AND THE NAME IS READ MORE WIDELY HERE THAN IT WAS AT\n'
        '  8.1.48.** **इह वृत्तग्रहणेन तद्विभक्त्यन्तं प्रतीयात् डतरडतमौ च\n'
        '  प्रत्ययौ इत्येतद् न आश्रीयते** — किंवृत्त was confined to the\n'
        '  inflected forms and the two affixes; यद्वृत्त is not, and neither\n'
        '  is the option: छन्दसि and प्रथमा both stop before this sūtra'
    ),
)

register(
    '8.1.67',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — पूजनात् पूजितम् अनुदात्तम् — after a word of PRAISE of the\n'
        '  काष्ठादि class, what is praised is toneless: **काष्ठाध्यापकः,\n'
        '  काष्ठाभिरूपकः; दारुणाध्यापकः; अमातापुत्राध्यापकः; अयुताभिरूपकः;\n'
        '  अद्भुताध्यापकः; अनुक्ताध्यापकः; भृशाध्यापकः; घोराध्यापकः;\n'
        '  परमाध्यापकः** — a teacher and a half. The pāda turns here: from\n'
        '  8.1.28 to 8.1.66 every sūtra kept an accent, and from here five\n'
        '  sūtras take one away'
    ),
)

register(
    '8.1.68',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — सगतिरपि तिङ् — and a finite verb after those, WITH or\n'
        '  without a preverb: **यत् काष्ठं पचति; यत् काष्ठं प्रपचति; यद्\n'
        '  दारुणं पचति; यद् दारुणं प्रपचति**. **तिङ्ङतिङः इति निघातस्य\n'
        '  निपातैर्यद्यदिहन्त० इति प्रतिषेधे प्राप्ते पुनर्विधानम्** — the\n'
        '  यत् in the examples had spared the verb by 8.1.30, and this puts\n'
        '  the निघात back. **सगतिग्रहणात् च गतिर् अपि निहन्यते** — the\n'
        '  preverb goes toneless with it, which is what saying सगति buys'
    ),
)

register(
    '8.1.69',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — कुत्सने च सुप्यगोत्रादौ — and a finite verb before a noun\n'
        '  of CONTEMPT that is not a गोत्रादि word: **पचति पूति; प्रपचति\n'
        '  पूति; पचति मिथ्या; प्रपचति मिथ्या**. **पदाद् इति निवृत्तम्** —\n'
        "  8.1.17's heading stops with the sūtra before, so this rule needs\n"
        '  nothing to stand in front; सगतिरपि तिङ् is carried down and the\n'
        '  preverb goes toneless too'
    ),
)

register(
    '8.1.70',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — गतिर्गतौ — a गति standing before another गति is toneless:\n'
        '  **अभ्युद्धरति; समुदानयति; अभिसम्पर्याहरति**. In each the last\n'
        '  preverb keeps an accent and every earlier one loses it, which is\n'
        '  how a string of four is heard as one word. **गतौ इति किम्? आ\n'
        '  मन्द्रैर् इन्द्र हरिभिर् याहि मयूररोमभिः** — आ is a गति there but\n'
        '  nothing follows it, and without the second word the rule would\n'
        '  make it toneless with no condition at all'
    ),
)

register(
    '8.1.71',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — तिङि चोदात्तवति — and a गति before a finite verb THAT HAS\n'
        '  an accent: **यत् प्रपचति; यत् प्रकरोति**. **तिङ्ग्रहणम् उदात्तवतः\n'
        '  परिमाणार्थम्** — saying तिङ् measures how much must carry the\n'
        '  accent: without it the root alone would have to, and यत् प्रकरोति,\n'
        '  where the accent is on the affix, would fall outside. The vṛtti\n'
        '  quotes the paribhāṣā that makes a प्र a गति in the first place —\n'
        '  **यत्क्रियायुक्ताः प्रादयस् तेषां तं प्रति गत्युपसर्गसंज्ञे भवतः**'
    ),
)

register(
    '8.1.72',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — आमन्त्रितं पूर्वम् अविद्यमानवत् — a VOCATIVE standing\n'
        '  first counts as not being there: **तस्मिन् सति यत् कार्यं तन् न\n'
        '  भवति, असति यत् तद् भवति**. **कानि पुनर् अविद्यमानवत्त्वे\n'
        '  प्रयोजनानि? आमन्त्रिततिङ्निघातयुष्मदस्मदादेशाभावाः** — three\n'
        "  things do not happen: the vocative's own निघात by 8.1.19, the\n"
        "  verb's by 8.1.28, and the enclitics of 8.1.20–23. In **देवदत्त\n"
        '  यज्ञदत्त** the second vocative has nothing in front of it and\n'
        "  keeps 6.1.198's accent on its first syllable"
    ),
)

register(
    '8.1.73',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — न आमन्त्रिते समानाधिकरणे सामान्यवचनम् — but a GENERAL\n'
        '  vocative followed by one that agrees with it does NOT count as\n'
        '  absent: **अग्ने गृहपते; माणवक जटिलकाध्यापक**. **किं तर्हि?\n'
        '  विद्यमानवद् एव** — it is there, and so the second vocative has a\n'
        '  word in front of it and goes toneless by 8.1.19: **पूर्वस्य\n'
        '  विद्यमानवत्त्वात् परम् अनुदात्तम् एव भवति**'
    ),
)

register(
    '8.1.74',
    apply=in_the_sentence,
    codification=_IN_THE_SENTENCE,
    notes=(
        'SETTLED — विभाषितं विशेषवचने बहुवचनम् — and a PLURAL vocative before\n'
        '  a specifying one counts as absent only optionally: **देवाः\n'
        '  शरण्याः** beside **देवाः शरण्याः** with the second word toneless;\n'
        '  **ब्राह्मणा वैयाकरणाः** the same way. **सामान्यवचनाधिकारादेव\n'
        '  विशेषवचन इति सिद्धे विशेषवचनग्रहणं विस्पष्टार्थम्** — the\n'
        '  qualifying word was already implied by the sūtra before and is\n'
        '  said again for plainness. With this the pāda closes'
    ),
)


__all__ = [
    'after_a_pada',
    'doubles',
    'in_the_sentence',
]
