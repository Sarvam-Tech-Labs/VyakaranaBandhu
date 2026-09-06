# -*- coding: utf-8 -*-
"""
३.४.१८–२४ — क्त्वा and णमुल्, the affixes of the prior act.

The run turns on one condition stated at 3.4.21 and carried a long way:
**समानकर्तृकयोः पूर्वकाले** — two acts with ONE doer, and the affix
goes on the earlier. भुक्त्वा व्रजति, having eaten he goes.

Three things here have no precedent in 3.2 or 3.3.

  * 3.4.18 and 3.4.19 attribute a rule to a NAMED SCHOOL —
    प्राचामाचार्याणां मतेन, उदीचामाचार्याणां मतेन, the teachers of the
    east and of the north — and the vṛtti reads the naming itself as
    making the rule optional, since the other school's usage stands
    too.
  * 3.4.23 is a प्रतिषेध that reaches BACKWARD: णमुल् is given in the
    rule immediately before, but क्त्वा comes from 3.4.21, and both
    are refused.
  * 3.4.24 establishes a SEVENTH suspension of 3.1.94, and by a ground
    none of the six used: क्त्वाणमुलौ यत्र सह विधीयेते तत्र
    वासरूपविधिर्नास्ति — *wherever these two are given together*.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.upapada_krt import Added, NotAdded


@dataclass(frozen=True)
class Ktva:
    """One rule of the क्त्वा and णमुल् run."""

    sutra: str
    gives: str
    also: str = ""
    #: The word standing beside, where the rule names one.
    beside: Tuple[str, ...] = ()
    #: The root, where the rule names one. Only 3.4.19 does, and it
    #: names it in the shape the root takes AFTER a vowel-change —
    #: मा for मेङ् — which the vṛtti then reads as a ज्ञāपaka.
    of_root: str = ""
    #: 3.4.21's condition, carried by most of the run.
    samana_kartrka: bool = False
    purvakala: bool = False
    #: 3.4.22's आभीक्ष्ण्य — again and again.
    abhiksnya: bool = False
    #: 3.4.20's परावरयोग — the earlier act tied to what is beyond, or
    #: the later to what is nearer.
    paravara: bool = False
    #: 3.4.19's व्यतीहार — exchange.
    vyatihara: bool = False
    #: 3.4.23 REFUSES both affixes.
    refuses: bool = False
    optional: bool = False
    #: Which school the rule is attributed to, where it is.
    school: str = ""
    #: From 3.4.25 the companion is the OBJECT of the act, not a
    #: particle: कर्मण्युपपदे, चोरंकारम्.
    karman: bool = False
    #: The sense, where a rule names one.
    sense: str = ""
    #: 3.4.27 and 3.4.28's सिद्धाप्रयोग — the सuffixed root's
    #: own sense adds nothing and is therefore not uttered. The
    #: condition 3.3.154 made of a word being meant and not said,
    #: now made of a ROOT.
    siddha_aprayoga: object = None
    #: 3.4.36's यथासंख्यम् — three companions bound to three
    #: roots, each entry (companion, root).
    bound: Tuple[Tuple[str, str], ...] = ()
    #: From 3.4.37 the rules divide by WHICH kāraka the companion
    #: is — करण, अधिकरण, कर्तृ, अपादान, उपमान — where 3.4.25 to
    #: 3.4.36 all wanted the object.
    karaka: str = ""
    #: And from 3.4.47 by the companion's CASE-ENDING rather than
    #: by its role: तृतीयायाम्, सप्तम्याम्, द्वितीयायाम्. A
    #: condition on the surface form of the companion, which the
    #: pādas before this never used.
    vibhakti: str = ""
    #: 3.4.42's संज्ञायाम्.
    samjna: bool = False
    #: 3.4.54 and 3.4.55's स्वाङ्ग — a part of one's own body —
    #: and 3.4.54's अध्रुव, a part one can lose and live.
    svanga: bool = False
    adhruva: object = None
    why: str = ""


KTVA: Tuple[Ktva, ...] = (
    Ktva("3.4.18", "ktvā", beside=("alam", "khalu"), optional=True,
         school="prācām",
         why="अलंखल्वोः प्रतिषेधयोः प्राचां क्त्वा — अलं कृत्वा, खलु "
             "कृत्वा, अलं बाले रुदित्वा.\n\n"
             "A RULE ATTRIBUTED TO A NAMED SCHOOL, which nothing in "
             "3.2 or 3.3 was: प्राचामाचार्याणां मतेन, by the opinion "
             "of the teachers of the EAST. And "
             "प्राचांग्रहणं विकल्पार्थम् — naming them is itself what "
             "makes the rule optional, since the other usage stands "
             "too: अलं रोदनेन.\n\n"
             "BOTH conditions tested. अलंखल्वोरिति किम्? मा कार्षीः. "
             "प्रतिषेधयोरिति किम्? अलंकारः — where अलम् means "
             "ornament and not 'enough'. So the two words must be "
             "there AND must be forbidding.\n\n"
             "वासरूपविधिश्चेत् पूजार्थम् — and if 3.1.94 is invoked "
             "here it is for honouring the teachers, not for the "
             "grammar. A principle cited as a courtesy"),
    Ktva("3.4.19", "ktvā", of_root="mā", vyatihara=True,
         optional=True, school="udīcām",
         why="उदीचां माङो व्यतीहारे — अपमित्य याचते, अपमित्य हरति. "
             "व्यतीहारः, exchange: having borrowed, he asks.\n\n"
             "अपूर्वकालत्वादप्राप्तः क्त्वा विधीयते — the affix is "
             "given where 3.4.21 could NOT reach, the borrowing not "
             "being the earlier act. And उदीचांग्रहणात् तु "
             "यथाप्राप्तमपि भवति: naming the NORTHERN teachers lets "
             "the ordinary form stand as well, याचित्वापमयते. The "
             "same device as 3.4.18's and the other school.\n\n"
             "AND A ज्ञापक FROM HOW THE ROOT IS SPELT. मेङः "
             "कृतात्वस्यायं निर्देशः कृतो ज्ञापनार्थः — the rule "
             "writes मा, the form the root मेङ् takes after its "
             "vowel-change, and that spelling tells us "
             "नानुबन्धकृतमनेजन्तत्वम्: a marker does not make a stem "
             "count as not-ending-in-a-diphthong. तेन दाधा घ्वदाप् "
             "इति दैपोऽपि प्रतिषेधो भवति — so 1.1.20's exclusion "
             "reaches दैप् too. A spelling in one rule settling the "
             "membership of a class three adhyāyas back, and 1.1.20 "
             "is codified"),
    Ktva("3.4.20", "ktvā", paravara=True,
         why="परावरयोगे च — अप्राप्य नदीं पर्वतः स्थितः, the mountain "
             "standing short of the river; अतिक्रम्य तु पर्वतं नदी "
             "स्थिता, the river lying beyond the mountain.\n\n"
             "परेण पूर्वस्य योगे गम्यमानेऽवरेण च परस्य — the earlier "
             "thing tied to what is FURTHER, or the later to what is "
             "NEARER, and the vṛtti says which is qualified by which "
             "in each: परनदीयोगेन पर्वतो विशिष्यते. A condition about "
             "how two things are placed, where every condition before "
             "it was about an act"),
    Ktva("3.4.21", "ktvā", samana_kartrka=True, purvakala=True,
         why="समानकर्तृकयोः पूर्वकाले — भुक्त्वा व्रजति, पीत्वा "
             "व्रजति. THE RULE THE WHOLE RUN STANDS ON, and its two "
             "conditions carry a long way.\n\n"
             "शक्तिशक्तिमतोर्भेदस्याविवक्षितत्वात् समानकर्तृकता — the "
             "sameness of doer holds because the difference between a "
             "power and what has it is not meant to be marked. A "
             "philosophical ground for a grammatical condition.\n\n"
             "द्विवचनमतन्त्रम्: the DUAL in the rule is not binding, "
             "so more than two acts are reached — स्नात्वा पीत्वा "
             "भुक्त्वा दत्त्वा व्रजति. The same reading 3.3.18 gave "
             "its own masculine singular.\n\n"
             "Both conditions tested: समानकर्तृकयोरिति किम्? "
             "भुक्तवति ब्राह्मणे व्रजति देवदत्तः. पूर्वकाल इति किम्? "
             "व्रजति च जल्पति च.\n\n"
             "SCOPE — आस्यं व्यादाय स्वपिति, चक्षुः संमील्य हसति "
             "इत्युपसंख्यानम्, अपूर्वकालत्वात्: two forms where the "
             "acts are SIMULTANEOUS and the affix comes anyway"),
    Ktva("3.4.22", "ṇamul", also="क्त्वा", abhiksnya=True,
         samana_kartrka=True, purvakala=True,
         why="आभीक्ष्ण्ये णमुल् च — भोजंभोजं व्रजति, भुक्त्वाभुक्त्वा "
             "व्रजति, पायंपायं व्रजति. आभीक्ष्ण्यं पौनःपुन्यम्.\n\n"
             "AND NEITHER AFFIX SHOWS THE SENSE ALONE. "
             "द्विर्वचनसहितौ क्त्वाणमुलावाभीक्ष्ण्यं द्योतयतः, न "
             "केवलौ — only WITH the doubling, आभीक्ष्ण्ये द्वे भवतः "
             "(वा० ८.१.१२) supplying it. The same vārttika 3.4.2 "
             "needed for the same reason, and the same shape: an "
             "affix that cannot carry its own sense"),
    Ktva("3.4.23", "", also="", beside=("yad",), refuses=True,
         why="न यद्यनाकाङ्क्षे — यदयं भुङ्क्ते ततः पठति, where "
             "neither affix comes. यत्र पूर्वोत्तरे क्रिये स्तः, "
             "तच्चेद् वाक्यं न परं किञ्चिदाकाङ्क्षति: where the "
             "sentence holding both acts looks for nothing further. "
             "अनाकाङ्क्ष इति किम्? यदयं भुक्त्वा व्रजति अधीत एव ततः "
             "परम्.\n\n"
             "A प्रतिषेध REACHING BACKWARD PAST ITS NEIGHBOUR. "
             "णमुलनन्तरः, क्त्वा तु पूर्वसूत्रविहितोऽपि प्रतिषिध्यते "
             "— णमुल् is given in the rule immediately before, but "
             "क्त्वा comes from 3.4.21, and BOTH are refused. 3.3.45 "
             "had shown the nearest word losing to a further one in "
             "an अनुवृत्ति; this shows a refusal reaching past its "
             "neighbour to take in an earlier rule as well"),
    Ktva("3.4.24", "ktvā", also="णमुल्", optional=True,
         beside=("agre", "prathama", "pūrva"), samana_kartrka=True,
         purvakala=True,
         why="विभाषाग्रेप्रथमपूर्वेषु — अग्रे भोजं व्रजति, अग्रे "
             "भुक्त्वा व्रजति, and so for the other two. "
             "अप्राप्तविभाषेयम्.\n\n"
             "AND A SEVENTH SUSPENSION OF 3.1.94, ON A GROUND NONE OF "
             "THE SIX USED. विभाषाग्रहणमेताभ्यां मुक्ते लडादयोऽपि "
             "यथा स्युः — the option is there so the ordinary endings "
             "may come instead: अग्रे भुङ्क्ते ततो व्रजति. Then ननु च "
             "वासरूप इति भविष्यति? — could 3.1.94 not have let them "
             "stand beside anyway? — क्त्वाणमुलौ यत्र सह विधीयेते "
             "तत्र वासरूपविधिर्नास्तीत्येतदनेन ज्ञाप्यते: WHEREVER "
             "THESE TWO ARE GIVEN TOGETHER the principle does not "
             "hold. तेनाभीक्ष्ण्ये लडादयो न भवन्ति, so 3.4.22's "
             "ground is shut.\n\n"
             "The six before it bounded the suspension by SECTION — "
             "the तच्छीलादि run, the क्रियार्थ ground, the feminine "
             "section. This bounds it by a PAIR OF AFFIXES, wherever "
             "in the grammar they occur together.\n\n"
             "SCOPE — उपपदसमासः कस्माद् न भवति? अमैव यत्तुल्यविधानम् "
             "उपपदं तत् समस्यते, नान्यदिति: no compound forms here, "
             "and the ground is a word in another rule entirely"),
    Ktva("3.4.25", "khamuñ", of_root="kṛ", karman=True,
         sense="ākrośa",
         why="कर्मणि भृत्यादिषु — चोरंकारमाक्रोशति, calling a man a "
             "thief. AND THE ACT IS NOT DONE: चोरकरणम् "
             "आक्रोशसंपादनार्थमेव, न त्वसौ चोरः क्रियते — the making "
             "is only for the abusing, and nobody is actually made a "
             "thief. A rule whose form says one thing does another, "
             "and the vṛtti has to say so.\n\n"
             "From here the companion is the OBJECT of the act rather "
             "than a particle, which is what कर्मणि brings"),
    Ktva("3.4.26", "ṇamul", of_root="kṛ", karman=True,
         beside=("svādu", "sampanna", "lavaṇa"),
         samana_kartrka=True, purvakala=True,
         why="स्वादुमि णमुल् — स्वादुंकारं भुङ्क्ते, संपन्नंकारं "
             "भुङ्क्ते, लवणंकारम्: having made it tasty, he eats.\n\n"
             "THE RULE'S OWN SPELLING DOES THREE THINGS AT ONCE. "
             "स्वादुमीति मकारान्तनिपातनम् — the म-final shape is "
             "fixed — ईकाराभावार्थम्, so no feminine ई comes; "
             "च्व्यन्तस्यापि मकारार्थम्, so a च्वि-stem gets the म "
             "too; दीर्घाभावार्थं च, and no lengthening. One "
             "orthographic choice carrying three grammatical "
             "consequences.\n\n"
             "AND THE समानकर्तृक CONDITION IS READ DIFFERENTLY HERE. "
             "3.4.21 grounded it on शक्तिशक्तिमतोर्भेदस्य"
             "अविवक्षितत्वात्; this rule says न चास्मिन् प्रकरणे "
             "शक्तिशक्तिमतोर्भेदो विवक्ष्यते, समानकर्तृकत्वं हि "
             "विरुध्यते — the very same distinction, and here it is "
             "not drawn BECAUSE drawing it would contradict the "
             "condition. The same ground reached for twice and used "
             "in opposite directions"),
    Ktva("3.4.27", "ṇamul", of_root="kṛ",
         beside=("anyathā", "evam", "katham", "ittham"),
         siddha_aprayoga=True,
         why="कर्मण्यन्यथैवंकथमित्थंसु सिद्धाप्रयोगश्चेत् — "
             "अन्यथाकारं भुङ्क्ते, एवंकारं, कथंकारं, इत्थंकारम्.\n\n"
             "AND THE CONDITION IS THAT THE ROOT ADD NOTHING. कथं "
             "पुनरसौ सिद्धाप्रयोगः? निरर्थकत्वाद् न "
             "प्रयोगमर्हतीत्येवमेव प्रयुज्यते — 'made' contributes no "
             "meaning here and is used only as a matter of form: "
             "अन्यथा भुङ्क्त इति यावानर्थः, तावानेवान्यथाकारं भुङ्क्त "
             "इति गम्यते, the compound means exactly what the two "
             "words meant. 3.3.154 made a condition of a WORD being "
             "meant and not said; this makes one of a ROOT adding "
             "nothing to what is said.\n\n"
             "सिद्धाप्रयोग इति किम्? अन्यथा कृत्वा शिरो भुङ्क्ते — "
             "where the making is real, the affix does not come"),
    Ktva("3.4.28", "ṇamul", of_root="kṛ", beside=("yathā", "tathā"),
         siddha_aprayoga=True, sense="asūyā-prativacana",
         why="यथातथयोरसूयाप्रतिवचने — यथाकारमहं भोक्ष्ये तथाकारमहम्, "
             "किं तवानेन? 'I shall eat how I shall eat — what is that "
             "to you?'\n\n"
             "यद्यसूयन् पृच्छति प्रतिवक्ति तत्र प्रतिवचनम् — the "
             "condition is on ANSWERING somebody who asks in "
             "resentment, so it is about the whole exchange and not "
             "about the speaker alone. असूयाप्रतिवचन इति किम्? यथा "
             "कृत्वाहं भोक्ष्ये, तथा त्वं द्रक्ष्यसि"),
    Ktva("3.4.29", "ṇamul", of_root="dṛś", karman=True,
         sense="sākalya",
         why="कर्मणि दृशिविदोः साकल्ये — कन्यादर्शं वरयति, यायाः "
             "कन्याः पश्यति तास्ता वरयति: every girl he sees he "
             "woos. ब्राह्मणवेदं भोजयति — यंयं ब्राह्मणं जानाति "
             "लभते विचारयति वा तान् सर्वान् भोजयति, and the vṛtti "
             "gives THREE senses for the second root before settling "
             "that all of them are reached.\n\n"
             "साकल्य is not exhaustiveness of the act but of the "
             "OBJECTS: साकल्य इति किम्? ब्राह्मणं दृष्ट्वा भोजयति, "
             "where one brahmin is seen and fed"),
    Ktva("3.4.30", "ṇamul", of_root="vid", beside=("yāvat",),
         why="यावति विन्दजीवोः — यावद्वेदं भुङ्क्ते, यावल्लभते तावद् "
             "भुङ्क्ते; यावज्जीवमधीते, यावज्जीवति तावदधीते. The "
             "compound means 'as much as' or 'as long as', and which "
             "of the two depends on which root — the rule says "
             "neither"),
    Ktva("3.4.31", "ṇamul", of_root="pūr", karman=True,
         beside=("carman", "udara"),
         why="चर्मोदरयोः पूरेः — चर्मपूरं स्तृणाति, उदरपूरं भुङ्क्ते: "
             "spreading a hide's fill, eating a belly's fill"),
    Ktva("3.4.32", "ṇamul", of_root="pūr", karman=True,
         sense="varṣa-pramāṇa", optional=True,
         why="वर्षप्रमाण ऊलोपश्चास्यान्यतरस्याम् — गोष्पदपूरं वृष्टो "
             "देवः, and with the ऊ dropped गोष्पदप्रं; सीतापूरं and "
             "सीताप्रम्. The rain measured by what it fills.\n\n"
             "अस्यग्रहणं किमर्थम्? उपपदस्य मा भूत् — the word अस्य is "
             "there so the vowel-loss falls on the ROOT and not on "
             "the companion: मूषिकाबिलपूरं keeps its own ऊ and only "
             "the root's goes. A word spent to say WHICH of two "
             "adjacent things an operation touches"),
    Ktva("3.4.33", "ṇamul", of_root="knūy", karman=True,
         beside=("cela", "vastra", "vasana"), sense="varṣa-pramāṇa",
         why="चेलार्थेषु क्नूयेर्ण्यन्तस्य वर्षप्रमाणे — चेलक्नोपं "
             "वृष्टो देवः, वस्त्रक्नोपम्, वसनक्नोपम्: rain enough to "
             "wet a garment. The companion is named by SENSE — "
             "चेलार्थेषु, words meaning cloth — so the three the "
             "vṛtti gives are examples and not a list"),
    Ktva("3.4.34", "ṇamul", of_root="kaṣ", karman=True,
         beside=("nimūla", "samūla"),
         why="निमूलसमूलयोः कषः — निमूलकाषं कषति, समूलकाषं कषति: "
             "scraping it out root and all.\n\n"
             "AND THE VṚTTI MARKS THE START OF A GROUP HERE. इतः "
             "प्रभृति कषादीन् यान् वक्ष्यति, तत्र कषादिषु "
             "यथाविध्यनुप्रयोगः — from this rule on, the roots named "
             "form a class called कषादि, and 3.4.46 will say that the "
             "SAME root must be said after each. A group defined by "
             "where a run begins rather than by a list, and named "
             "after its first member"),
    Ktva("3.4.35", "ṇamul", of_root="piṣ", karman=True,
         beside=("śuṣka", "cūrṇa", "rūkṣa"),
         why="शुष्कचूर्णरूक्षेषु पिषः — शुष्कपेषं पिनष्टि, चूर्णपेषं, "
             "रूक्षपेषम्. And each is glossed by dropping the affix: "
             "शुष्कं पिनष्टीत्यर्थः — the compound means no more than "
             "the two words did, which is the सिद्धाप्रयोग reading of "
             "3.4.27 met again without being named"),
    Ktva("3.4.36", "ṇamul", karman=True,
         bound=(("samūla", "han"), ("akṛta", "kṛ"),
                ("jīva", "grah")),
         why="समूलाकृतजीवेषु हन्कृञ्ग्रहः — यथासंख्यम्: समूलघातं "
             "हन्ति, अकृतकारं करोति, जीवग्राहं गृह्णाति. Three "
             "companions bound to three roots, so the row holds pairs "
             "and the lists may not be crossed — the device 3.2.5 "
             "established and 3.3.37 stretched to three lists at "
             "once"),
    Ktva("3.4.37", "ṇamul", of_root="han", karaka="karaṇa",
         why="करणे हनः — पाणिघातं वेदिं हन्ति, पादघातं भूमिं हन्ति. "
             "From here the rules divide by WHICH kāraka the "
             "companion is, where 3.4.25 to 3.4.36 all wanted the "
             "object.\n\n"
             "AND AN EARLIER RULE IS MADE TO WIN OVER A LATER ONE. "
             "3.4.48 will give णमुल् for roots meaning HARM, and this "
             "rule would then be needless for those — "
             "अहिंसार्थोऽयमारम्भः. But पूर्वविप्रतिषेधेन हन्तेर् "
             "हिंसार्थस्यापि प्रत्ययोऽनेनैवेष्यते: by PRIOR "
             "CONTRADICTION the affix comes by THIS rule even in the "
             "sense of harm — असिघातं हन्ति, शरघातं हन्ति.\n\n"
             "परत्व, a later rule winning, was 3.3.142's ground. "
             "पूर्वविप्रतिषेध is the reverse and has to be asked for; "
             "the codification reaches the same answer by "
             "specificity, and the two grounds agree here without "
             "having to"),
    Ktva("3.4.38", "ṇamul", of_root="piṣ", karaka="karaṇa",
         sense="snehana",
         why="स्नेहने पिषः — उदपेषं पिनष्टि, तैलपेषं पिनष्टि, तैलेन "
             "पिनष्टीत्यर्थः. स्निह्यते येन तत् स्नेहनम्, what one "
             "moistens with"),
    Ktva("3.4.39", "ṇamul", of_root="vṛt", karaka="karaṇa",
         beside=("hasta", "kara", "pāṇi"),
         why="हस्ते वर्तिग्रहोः — हस्तेन वर्तयति हस्तवर्तं वर्तयति; "
             "करवर्तम्, पाणिवर्तम्; and for the other root "
             "हस्तग्राहं गृह्णाति. हस्त इत्यर्थग्रहणम् — the word is "
             "taken BY SENSE, so कर and पाणि are reached and the "
             "three given are examples"),
    Ktva("3.4.40", "ṇamul", of_root="puṣ", karaka="karaṇa",
         beside=("sva", "ātman", "go", "pitṛ", "mātṛ", "dhana", "rai"),
         why="स्वे पुषः — स्वपोषं पुष्णाति, आत्मपोषम्, गोपोषम्, "
             "पितृपोषम्, मातृपोषम्, धनपोषम्, रैपोषम्. स्व इत्यर्थ"
             "ग्रहणम्, and the vṛtti gives its range: आत्मात्मीय"
             "ज्ञातिधनवचनः स्वशब्दः — oneself, one's own, one's kin, "
             "one's wealth. Four senses of one word, and the seven "
             "examples run across all of them"),
    Ktva("3.4.41", "ṇamul", of_root="bandh", karaka="adhikaraṇa",
         why="अधिकरणे बन्धः — चक्रबन्धं बध्नाति, कूटबन्धम्, "
             "मुष्टिबन्धम्, चोरकबन्धं बध्नाति, चोरके "
             "बध्नातीत्यर्थः"),
    Ktva("3.4.42", "ṇamul", of_root="bandh", samjna=True,
         why="संज्ञायाम् — क्रौञ्चबन्धं बध्नाति, मयूरिकाबन्धम्, "
             "अट्टालिकाबन्धं बद्धः. बन्धविशेषाणां नामधेयान्येतानि, "
             "names of particular knots. Same root as the rule "
             "before and no kāraka named: what carries it is that the "
             "whole word is a NAME"),
    Ktva("3.4.43", "ṇamul", karaka="kartṛ",
         bound=(("jīva", "naś"), ("puruṣa", "vah")),
         why="जीवपुरुषयोर्नशिवहोः — यथासंख्यम्: जीवनाशं नश्यति, "
             "जीवो नश्यतीत्यर्थः; पुरुषवाहं वहति, पुरुषः प्रेष्यो "
             "भूत्वा वहतीत्यर्थः. कर्तरीति किम्? जीवेन नष्टः, "
             "पुरुषेणोढः — where the companion is the MEANS the rule "
             "does not reach, though the words are the same"),
    Ktva("3.4.44", "ṇamul", of_root="śuṣ", karaka="kartṛ",
         beside=("ūrdhva",),
         why="ऊर्ध्वे शुषिपूरोः — ऊर्ध्वशोषं शुष्यति, ऊर्ध्वं "
             "शुष्यतीत्यर्थः; ऊर्ध्वपूरं पूर्यते. कर्तृग्रहणम् runs "
             "down from 3.4.43"),
    Ktva("3.4.45", "ṇamul", karaka="upamāna",
         why="उपमाने कर्मणि च — घृतनिधायं निहितः, घृतमिव निहित "
             "इत्यर्थः; सुवर्णनिधायम्. And by the च the AGENT too: "
             "अजकनाशं नष्टः, अजक इव नष्टः; चूडकनाशम्, दन्तनाशम्.\n\n"
             "उपमीयतेऽनेनेत्युपमानम् — what a thing is likened TO. "
             "3.2.79 and 3.2.101 had उपमान as a role the companion "
             "plays; here it is the kāraka itself"),
    Ktva("3.4.47", "ṇamul", of_root="daṃś", vibhakti="tṛtīyā",
         why="उपदंशस्तृतीयायाम् — मूलकोपदंशं भुङ्क्ते, मूलकेनोपदंशम्; "
             "आर्द्रकोपदंशम्. FROM HERE THE RULES DIVIDE BY THE "
             "COMPANION'S CASE-ENDING rather than by its role, which "
             "no pāda before this did: a condition on the surface "
             "form of the companion.\n\n"
             "अत्र विकल्पेनोपपदसमासः तृतीयाप्रभृतीन्यन्यतरस्याम् इति "
             "— so the compound is optional, and both forms are "
             "given for each example. 2.2.21 is codified.\n\n"
             "AND THE SUSPENSION OF 3.4.24 IS QUALIFIED HERE. "
             "सर्वस्मिन्नेवात्र णमुल्प्रकरणे क्रियाभेदे सति "
             "वासरूपविधिना क्त्वापि भवति — throughout this णमुल् "
             "section क्त्वा stands beside by 3.1.94 WHERE THE ACTS "
             "DIFFER. 3.4.24 had said the principle does not hold "
             "wherever the two affixes are given together; this says "
             "it holds again once the acts are distinct. The seventh "
             "suspension, bounded from inside twenty-three sūtras "
             "later.\n\n"
             "SETTLED — मूलकादि चोपदंशेः कर्म, भुजेः करणम्: the same "
             "word is the OBJECT of one verb and the MEANS of the "
             "other, which is why the rule names a case-ending and "
             "not a kāraka"),
    Ktva("3.4.48", "ṇamul", vibhakti="tṛtīyā", sense="hiṃsā",
         why="हिंसार्थानां च समानकर्मकाणाम् — दण्डोपघातं गाः कालयति, "
             "दण्डेनोपघातम्, दण्डताडम्. हिंसा प्राण्युपघातः.\n\n"
             "समानकर्मकाणामिति किम्? चोरं दण्डेनोपहत्य गोपालको गाः "
             "कालयति — the two acts must have the SAME OBJECT, and "
             "here the thief is struck while the cattle are driven. "
             "3.4.21's condition was one DOER for both acts; this is "
             "one object, and it is stated afresh rather than "
             "inherited"),
    Ktva("3.4.49", "ṇamul", of_root="pīḍ", vibhakti="saptamī",
         why="सप्तम्यां चोपपीडरुधकर्षः — पार्श्वोपपीडं शेते, "
             "पार्श्वयोरुपपीडम्, पार्श्वाभ्यामुपपीडम्; व्रजोपरोधं "
             "गाः स्थापयति; पाण्युपकर्षं धानाः संगृह्णाति. And by the "
             "च the third case too, so three forms stand for each.\n\n"
             "उपशब्दः प्रत्येकमभिसंबध्यते — the उप is to be joined to "
             "EACH of the three roots separately, which the compound "
             "in the rule does not show. And कर्षतेरिदं ग्रहणम्, न "
             "कृषतेः: the root meant is the one meaning to drag and "
             "not the one meaning to plough — two roots spelt alike, "
             "settled by naming which"),
    Ktva("3.4.50", "ṇamul", vibhakti="tṛtīyā", sense="samāsatti",
         why="समासत्तौ — केशग्राहं युध्यन्ते, केशेषु ग्राहम्, "
             "केशैर्ग्राहम्; हस्तग्राहम्. समासत्तिः सन्निकर्षः, "
             "closeness — and the vṛtti explains the scene: "
             "युद्धसंरम्भादत्यन्तं सन्निकृष्यन्त इत्यर्थः, in the "
             "fury of a fight they come to close quarters"),
    Ktva("3.4.51", "ṇamul", vibhakti="tṛtīyā", sense="pramāṇa",
         why="प्रमाणे — द्व्यङ्गुलोत्कर्षं खण्डिकां छिनत्ति, "
             "द्व्यङ्गुल उत्कर्षम्, द्व्यङ्गुलेनोत्कर्षम्; "
             "त्र्यङ्गुलोत्कर्षम्. प्रमाणमायामः, दैर्घ्यम् — the "
             "measure here is LENGTH in particular, which the word "
             "alone does not say"),
    Ktva("3.4.52", "ṇamul", karaka="apādāna", sense="parīpsā",
         why="अपादाने परीप्सायाम् — शय्योत्त्थायं धावति, शय्याया "
             "उत्त्थायम्; रन्ध्रापकर्षं पयः पिबति; भ्राष्ट्रापकर्षम् "
             "अपूपान् भक्षयति. परीप्सा त्वरा, haste.\n\n"
             "AND THE VṚTTI PAINTS THE HASTE RATHER THAN GLOSSING IT: "
             "एवं नाम त्वरते यदवश्यं कर्तव्यमपि नापेक्षते, "
             "शय्योत्त्थानमात्रमाद्रियते — such is his hurry that he "
             "does not attend even to what must be done, and cares "
             "only for getting out of bed. परीप्सायामिति किम्? "
             "आसनादुत्त्थाय गच्छति"),
    Ktva("3.4.53", "ṇamul", vibhakti="dvitīyā", sense="parīpsā",
         why="द्वितीयायां च — यष्टिग्राहं युध्यन्ते, यष्टिं ग्राहम्; "
             "लोष्टग्राहम्. Again the scene: एवं नाम त्वरते यद् "
             "आयुधग्रहणमपि नाद्रियते, लोष्टादिकं यत् किञ्चिदासन्नम् "
             "तद् गृह्णाति — in such haste that he does not stop for "
             "a weapon and snatches up whatever clod is nearest"),
    Ktva("3.4.54", "ṇamul", vibhakti="dvitīyā", svanga=True,
         adhruva=True,
         why="स्वाङ्गेऽध्रुवे — अक्षिनिकाणं जल्पति, भ्रूविक्षेपं "
             "कथयति. अध्रुव इति किम्? उत्क्षिप्य शिरः कथयति.\n\n"
             "AND अध्रुव IS DEFINED BY WHAT SURVIVES ITS LOSS: "
             "यस्मिन्नङ्गे छिन्नेऽपि प्राणी न म्रियते तदध्रुवम् — a "
             "limb whose cutting off does not kill. A grammatical "
             "condition defined by a fact about bodies. And "
             "स्वाङ्ग itself is quoted from another rule: अद्रवं "
             "मूर्तिमत्स्वाङ्गम् (1.1.59's neighbourhood)"),
    Ktva("3.4.55", "ṇamul", vibhakti="dvitīyā", svanga=True,
         sense="parikleśa",
         why="परिक्लिश्यमाने च — उरःपेषं युध्यन्ते, उरःप्रतिपेषम्, "
             "शिरःपेषम्. परिक्लेशः सर्वतो विबाधनम्, दुःखनम्, and "
             "कृत्स्नमुरः पीडयन्तो युध्यन्ते — the whole chest "
             "crushed. ध्रुवार्थोऽयमारम्भः: the rule exists for the "
             "limbs 3.4.54's अध्रुव shut out"),
    Ktva("3.4.56", "ṇamul", vibhakti="dvitīyā",
         of_root="viś", sense="vyāpti",
         why="विशिपतिपदिस्कन्दां व्याप्यमानासेव्यमानयोः — "
             "गेहानुप्रवेशमास्ते, गेहानुप्रपातम्, गेहानुप्रपादम्, "
             "गेहावस्कन्दम्.\n\n"
             "TWO SENSES, AND THE DOUBLING FALLS ON DIFFERENT WORDS "
             "IN EACH. व्याप्तिः is the acts covering the things "
             "entire, आसेवा is repetition — द्रव्ये व्याप्तिः, "
             "क्रियायामासेवा. So असमासपक्षे व्याप्यमानतायां "
             "द्रव्यवचनस्य द्विर्वचनम्, आसेव्यमानतायां तु "
             "क्रियावचनस्य: गेहंगेहम् अनुप्रवेशमास्ते for the one, "
             "गेहम् अनुप्रवेशमनुप्रवेशमास्ते for the other. The vṛtti "
             "quotes a verse for it — सुप्सु वीप्सा, तिङ्क्षु "
             "नित्यता.\n\n"
             "AND THE RULE IS ASKED WHY IT EXISTS AT ALL. ननु "
             "चाभीक्ष्ण्ये णमुल् विहित एव, आसेवा चाभीक्ष्ण्यमेव — "
             "3.4.22 gives the affix for repetition already. "
             "क्त्वानिवृत्त्यर्थमिति चेत्, न, इष्टत्वात् तस्य: not to "
             "keep क्त्वा out, since that IS wanted. "
             "द्वितीयोपपदार्थं तर्हि वचनम्, उपपदसमासः पक्षे यथा "
             "स्यात् — it is for the second case, so that the "
             "compound may optionally form. A rule whose only work is "
             "to license a compound, as 3.3.116's was"),
    Ktva("3.4.57", "ṇamul", vibhakti="dvitīyā", of_root="as",
         sense="kriyāntara",
         why="अस्यतितृषोः क्रियान्तरे कालेषु — द्व्यहात्यासं गाः "
             "पाययति, द्व्यहमत्यासम्; द्व्यहतर्षं गाः पाययति. "
             "क्रियामन्तरयति क्रियान्तरः, क्रियाव्यवधायकः — an act "
             "that INTERRUPTS another: अद्य पाययित्वा द्व्यहम् "
             "अतिक्रम्य पुनः पाययति.\n\n"
             "THREE CONDITIONS AND THREE COUNTERS. अस्यतितृषोरिति "
             "किम्? द्व्यहमुपोष्य भुङ्क्ते. क्रियान्तर इति किम्? "
             "अहरत्यस्येषून् गतः, न गतिर्व्यवधीयते — the going is not "
             "interrupted. कालेष्विति किम्? योजनमत्यस्य गाः पाययति, "
             "and the reason: अध्वकर्मकमत्यसनं व्यवधायकम्, न "
             "कालकर्मकम् — an interval of ROAD interrupts, an "
             "interval of time does not"),
    Ktva("3.4.58", "ṇamul", vibhakti="dvitīyā", of_root="ādiś",
         beside=("nāman",),
         why="नाम्न्यादिशिग्रहोः — नामादेशमाचष्टे, नामग्राहमाचष्टे. "
             "Two roots, one companion, and no ground given for "
             "either"),
    Ktva("3.4.59", "ṇamul", also="क्त्वा", of_root="kṛ",
         beside=("avyaya", "nīcais", "uccais"),
         sense="ayathābhipretākhyāna",
         why="अव्यये यथाभिप्रेताख्याने कृञः क्त्वाणमुलौ — and the "
             "vṛtti stages it as a scene: ब्राह्मण पुत्रस्ते जातः; "
             "किं तर्हि वृषल नीचैः कृत्याचक्षे? — 'a son is born to "
             "you, brahmin!' 'Why then, wretch, do you tell it in a "
             "LOW voice?' उच्चैर्नाम प्रियमाख्येयम्, good news should "
             "be told loudly. And the converse: कन्या ते गर्भिणी told "
             "loudly, नीचैर्नामाप्रियमाख्येयम्.\n\n"
             "TWO WORDS OF THE RULE, EACH SPENT ON SOMETHING OTHER "
             "THAN ITS AFFIX. क्त्वाग्रहणं किम्, यावता सर्वस्मिन्नेव "
             "अत्र प्रकरणे वासरूपेण क्त्वा भवतीत्युक्तम्? "
             "समासार्थं वचनम् — क्त्वा is named for the COMPOUND, "
             "since 2.2.22 needs 2.2.21's condition read into it. And "
             "णमुलधिकारे पुनर्णमुल्ग्रहणं तुल्यकक्षत्वज्ञापनार्थम्: "
             "णमुल् is named again, though the section is about it, "
             "to show the two stand at the SAME LEVEL — तेनोत्तरत्र "
             "द्वयोरप्यनुवृत्तिर्भविष्यति, so both carry down "
             "together. A repetition that makes two things equal, "
             "which is a sixth use of the device"),
    Ktva("3.4.60", "ktvā", also="णमुल्", of_root="kṛ",
         beside=("tiryac",), sense="apavarga",
         why="तिर्यच्यपवर्गे — तिर्यक्कृत्य गतः, तिर्यक् कृत्वा गतः, "
             "तिर्यक्कारं गतः: having FINISHED it, he went. अपवर्गः "
             "समाप्तिः. अपवर्ग इति किम्? तिर्यक् कृत्वा काष्ठं गतः.\n\n"
             "SETTLED — तिर्यचीति शब्दानुकरणम्: the rule's word is an "
             "IMITATION of the word it speaks of, न च प्रकृतिवद् "
             "अनुकरणेन भवितव्यम्, अनुक्रियमाणरूपविनाशप्रसङ्गात् — an "
             "imitation must not behave like its original, or the "
             "shape being imitated would be destroyed. 2.4.33 and "
             "1.1.12 are cited for it. A rule about how a rule may "
             "NAME a word"),
    Ktva("3.4.61", "ktvā", also="णमुल्", of_root="kṛ", svanga=True,
         beside=("mukhatas", "pṛṣṭhatas"),
         why="स्वाङ्गे तस्प्रत्यये कृभ्वोः — मुखतःकृत्य गतः, "
             "मुखतःकारं गतः; मुखतोभूय तिष्ठति; पृष्ठतःकृत्य गतः.\n\n"
             "यथासंख्यमत्र नेष्यते, अस्वरितत्वात् — the counting-off "
             "does NOT apply, and the ground is that the rule is not "
             "marked with a svarita. An argument from an ACCENT the "
             "sūtrapāṭha on disk does not carry, so it is recorded "
             "and cannot be checked.\n\n"
             "THREE CONDITIONS, THREE COUNTERS, and each removes a "
             "different word: स्वाङ्ग इति किम्? सर्वतः कृत्वा गतः. "
             "तस्ग्रहणं किम्? मुखीकृत्य गतः. प्रत्ययग्रहणं किम्? मुखे "
             "तस्यतीति मुखतः — where the तस् is not an AFFIX but part "
             "of a root, the rule does not reach"),
    Ktva("3.4.62", "ktvā", also="णमुल्", of_root="kṛ",
         beside=("nānā", "vinā", "dvidhā", "dvaidham"),
         sense="cvi",
         why="नाधार्थप्रत्यये च्व्यर्थे — नानाकृत्य गतः, नाना कृत्वा "
             "गतः, नानाकारं गतः; विनाकृत्य; द्विधाकृत्य; "
             "द्वैधंकृत्य — and each of the four again with the other "
             "root, twenty-four forms in all.\n\n"
             "प्रत्ययग्रहणं किम्? हिरुक् कृत्वा, पृथक् कृत्वा — where "
             "the ending is not an affix the rule does not reach. "
             "च्व्यर्थ इति किम्? नाना कृत्वा काष्ठानि गतः.\n\n"
             "SETTLED — धार्थमर्थग्रहणम्, ना पुनरेक एव: the धा is "
             "taken BY SENSE and the ना is one particular affix, "
             "5.2.27 giving it. Two halves of one compound read two "
             "different ways"),
    Ktva("3.4.63", "ktvā", also="णमुल्", of_root="bhū",
         beside=("tūṣṇīm",),
         why="तूष्णीमि भुवः — तूष्णींभूय गतः, तूष्णीं भूत्वा, "
             "तूष्णींभावम्. भूग्रहणं कृञो निवृत्त्यर्थम् — भू is "
             "named to STOP कृ, which had been running from 3.4.61. A "
             "root named to exclude another"),
    Ktva("3.4.64", "ktvā", also="णमुल्", of_root="bhū",
         beside=("anvac",), sense="ānulomya",
         why="अन्वच्यानुलोम्ये — अन्वग्भूयास्ते, अन्वग् भूत्वास्ते, "
             "अन्वग्भावमास्ते. आनुलोम्यमनुलोमता, अनुकूलत्वम्, "
             "परचित्तानुविधानम् — falling in with another's mind, and "
             "the vṛtti glosses it three times over, each gloss "
             "further from the word. आनुलोम्य इति किम्? अन्वग् भूत्वा "
             "तिष्ठति"),
)


def ktva_namul(*, beside: str = "", root: str = "",
               karman: bool = False, sense: str = "",
               karaka: str = "", vibhakti: str = "",
               samjna: bool = False, svanga: bool = False,
               adhruva: bool = False,
               siddha_aprayoga: bool = False,
               samana_kartrka: bool = False, purvakala: bool = False,
               abhiksnya: bool = False, paravara: bool = False,
               vyatihara: bool = False, anakanksa: bool = False,
               wants: str = "") -> object:
    """
    3.4.18 to 3.4.24 — क्त्वा and णमुल्, the affixes of the prior act.

    3.4.21 समानकर्तृकयोः पूर्वकाले is the rule the run stands on: two
    acts with ONE doer, and the affix goes on the earlier. Everything
    else either narrows that or reaches ground it could not.

    3.4.23 refuses both affixes where यद् stands and the sentence
    wants nothing further — and it refuses BY NAME, since refusing is
    the whole of what it does, which is the case 3.2.23 marked off.
    """
    if beside == "yad" and anakanksa:
        row = next(r for r in KTVA if r.sutra == "3.4.23")
        return NotAdded("3.4.23", row.why)

    matched = [row for row in KTVA
               if not row.refuses
               and (not row.bound
                    or any(w == beside and r == root
                           for w, r in row.bound))
               and (row.bound or not row.beside or beside in row.beside)
               and (row.bound or not row.of_root
                    or root == row.of_root)
               and (not row.karman or karman)
               and (not row.karaka or karaka == row.karaka)
               and (not row.vibhakti or vibhakti == row.vibhakti)
               and (not row.samjna or samjna)
               and (not row.svanga or svanga)
               and (row.adhruva is None
                    or bool(row.adhruva) == adhruva)
               and (not row.sense or sense == row.sense)
               and (row.siddha_aprayoga is None
                    or bool(row.siddha_aprayoga) == siddha_aprayoga)
               and (not row.samana_kartrka or samana_kartrka)
               and (not row.purvakala or purvakala)
               and (not row.abhiksnya or abhiksnya)
               and (not row.paravara or paravara)
               and (not row.vyatihara or vyatihara)
               and (not wants or wants == row.gives
                    or wants in row.also)]
    if not matched:
        return NotAdded(
            "",
            "No rule of 3.4.18 to 3.4.24 reaches this. क्त्वा comes "
            "where two acts share a doer and this is the earlier; "
            "णमुल् where the act is repeated; and three rules reach "
            "ground that condition could not")
    best = max(matched, key=_how_specific)
    gives = wants if wants and (wants == best.gives
                                or wants in best.also) else best.gives
    return Added(gives, best.sutra, best.why,
                 also=best.also if gives == best.gives else "")


def _how_specific(row: Ktva) -> int:
    """How much a row states."""
    return (3 * (len(row.beside) > 0) + 3 * bool(row.of_root)
            + 4 * (len(row.bound) > 0) + 2 * row.karman
            + 2 * bool(row.sense) + 2 * bool(row.karaka)
            + 2 * bool(row.vibhakti) + 2 * row.samjna
            + 2 * row.svanga + (row.adhruva is not None)
            + 2 * (row.siddha_aprayoga is not None)
            + 2 * row.abhiksnya + 2 * row.paravara
            + 2 * row.vyatihara
            + row.samana_kartrka + row.purvakala)


def attributed_schools() -> Tuple[Tuple[str, str], ...]:
    """
    The rules of this run given on a named school's authority, read
    from the table.

    प्राचाम् and उदीचाम् — the teachers of the east and of the north.
    Nothing in 3.2 or 3.3 attributed a rule this way, and in both
    places the vṛtti reads the attribution itself as making the rule
    OPTIONAL: the other school's usage stands too.
    """
    return tuple((row.sutra, row.school) for row in KTVA if row.school)
