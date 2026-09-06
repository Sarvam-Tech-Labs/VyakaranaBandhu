# -*- coding: utf-8 -*-
"""अध्याय ३, पाद ३ — which tense-ending, and the affixes of the act."""

from __future__ import annotations

from src.astadhyayi.bhava_krt import (
    bhava_affix, kriyartha_affix, krtya_lyut_bahulam, nipatana,
)
from src.astadhyayi.lakara import (
    lakara_for, lrn_is_optional, lrt_substitute,
)
from src.astadhyayi.sources import register
from src.astadhyayi.tense_transfer import tense_transfer
from src.astadhyayi.vidhi_krt import vidhi_affix
from src.astadhyayi.unadi import gamyadi, unadi

# -------------------------------------------------------------------------
# 3.3.1 to 3.3.15 — three rules licensing what the grammar does not derive,
# then everything under भविष्यति, which is dropped at 3.3.16.
# -------------------------------------------------------------------------

_UNADI_LINE = (
    'unadi(word, past=..., samjna=...) -> whether an उणादि word stands, '
    'and which sūtra of the उणादिपाठ the Kāśikā cites for it.'
)

_GAMYADI_LINE = (
    'gamyadi(word, anadyatana=...) -> whether a गम्यादि word stands for '
    'the future, and on whose authority.'
)

_LAKARA_LINE = (
    'lakara_for(time=..., beside=..., nipata=..., kimvrtta=..., lipsa=..., '
    'lipsyamana_siddhi=..., lodartha=..., urdhvamauhurtika=..., '
    'anadyatana=...) -> which tense-ending comes, and by which rule. The '
    'same table 3.2.110 to 3.2.123 answer from, filtered on time.'
)

_KRIYARTHA_LINE = (
    'kriyartha_affix(wants=..., karman=..., bhava=..., kriya=..., '
    'kriyartha=...) -> which affix comes where the act is done for another '
    'act, and by which rule.'
)

_LRT_SAT_LINE = (
    'lrt_substitute(aprathama=..., sambodhana=..., wants=...) -> whether '
    'शतृ or शानच् stands in place of लृट्, obligatorily or by choice.'
)

_RULES = {
    "3.3.1":
      "SETTLED — उणादयो बहुलम्: कारुः, वायुः, पायुः, जायुः, मायुः,\n"
      "  स्वादुः, साधुः, आशुः, all by प०उ० १.१\n"
      "  कृवापाजिमिस्वदिसाध्यशूभ्य उण्.\n\n"
      "SETTLED — THE RULE STATES NEITHER OF ITS OWN CONDITIONS.\n"
      "  वर्तमान इत्येव, संज्ञायामिति च — the present runs down from\n"
      "  3.2.123 and the name-sense from 3.2.185, and the sūtra says\n"
      "  only that the उणादि affixes come बहुलम्. Two अनुवृत्ति from\n"
      "  two different rules of the pāda just finished, meeting in\n"
      "  the pāda's first sūtra.\n\n"
      "SETTLED — AND WHAT IT LICENSES IS ANOTHER TEXT. The उणादिपाठ\n"
      "  is 748 sūtras in five pādas, and it is ON DISK — read at\n"
      "  import by `corpus.load_unadipatha`, which nothing had used\n"
      "  before this rule. So the codification does not restate the\n"
      "  affixes: it holds a locator into that text and quotes it\n"
      "  back. The Kāśikā's citation प०उ० १.१ is that file's first\n"
      "  row, verbatim, which is what makes the locator checkable.\n\n"
      "SCAR — बहुलम् IS NOT RESOLVED AND CANNOT BE. The vṛtti gives\n"
      "  its reach in two directions and both are open:\n"
      "  यतो विहितास्ततोऽन्यत्रापि भवन्ति, they occur where they were\n"
      "  not prescribed; केचिदविहिता एव प्रयोगत उन्नीयन्ते, some are\n"
      "  inferred from usage having never been prescribed at all. So\n"
      "  a word's ABSENCE from the उणादिपाठ refuses nothing, and the\n"
      "  entry point says so rather than answering no.\n\n"
      "SCOPE — the Kāśikā closes with three verses on how the उणादि\n"
      "  are to be read (म०भा० वा० १–७), of which the last is the\n"
      "  operative one: संज्ञासु धातुरूपाणि प्रत्ययाश्च ततः परे,\n"
      "  कार्याद् विद्यादनूबन्धम् — in names, a root-shape with an\n"
      "  affix after it, and the marks are to be inferred FROM THE\n"
      "  OPERATION rather than read off the affix. An analysis run\n"
      "  backwards from its result, which is the opposite of how\n"
      "  this grammar works everywhere else.",
    "3.3.2":
      "SETTLED — भूतेऽपि दृश्यन्ते: वृत्तमिदं वर्त्म, चरितं तदिति\n"
      "  चर्म, भसितं तदिति भस्म. पूर्वत्र वर्तमानाधिकाराद् भूतार्थमिदं\n"
      "  वचनम् — the rule exists because the present was running.\n\n"
      "SETTLED — दृशिग्रहणं प्रयोगानुसारार्थम्, AND THIS IS THE THIRD\n"
      "  TIME THAT WORD HAS BEEN READ. At 3.2.75 the vṛtti read\n"
      "  दृश्यते as प्रयोगानुसरणार्थम्, the rule following usage; at\n"
      "  3.2.178 as विध्यन्तरोपसंग्रहार्थम्, gathering in other\n"
      "  operations. This one sides with 3.2.75, and in almost the\n"
      "  same words. So the word has two readings and not three, and\n"
      "  which one is meant is settled at each place by the\n"
      "  commentary and by nothing in the sūtra.",
    "3.3.3":
      "SETTLED — भविष्यति गम्यादयः: गमी ग्रामम्, आगामी, प्रस्थायी,\n"
      "  प्रतिरोधी, प्रतिबोधी, प्रतियोधी, प्रतियोगी, प्रतियायी,\n"
      "  आयायी, भावी.\n\n"
      "SETTLED — प्रत्ययस्यैव भविष्यत्कालता विधीयते न प्रकृतेः. It is\n"
      "  the AFFIX that is given the future sense and not the root,\n"
      "  which the shape of the rule hides: भविष्यति looks like a\n"
      "  condition on the root's meaning and is not. What the rule\n"
      "  licenses is a finished word.\n\n"
      "SCOPE — अनद्यतन उपसंख्यानम् is a vārttika: श्वो गमी ग्रामम्,\n"
      "  reaching the not-today future as well.\n\n"
      "SETTLED — भविष्यति then RUNS from here to 3.3.15, and the\n"
      "  vṛtti says where it stops rather than leaving it to be\n"
      "  inferred: भविष्यतीति निवृत्तम् at 3.3.16.",
    "3.3.4":
      "SETTLED — यावत्पुरानिपातयोर्लट्: यावद् भुङ्क्ते, पुरा भुङ्क्ते.\n"
      "  The PRESENT ending used of the future, on no ground but the\n"
      "  company the verb keeps.\n\n"
      "SETTLED — निपातयोरिति किम्? यावद् दास्यति तावद् भोक्ष्यते;\n"
      "  करणभूतया पुरा व्रजिष्यति. Where the same two syllables are a\n"
      "  case-form rather than a particle the rule does not reach\n"
      "  them, and what stands instead is 3.3.13's लृट् — which the\n"
      "  counter-example itself uses. So the condition is on WHAT\n"
      "  PART OF SPEECH the companion is, a question no rule of 3.2\n"
      "  asked. Codified as a tri-state, since silence about it is\n"
      "  not a demand that the word NOT be a particle.\n\n"
      "SETTLED — codified into the same table as 3.2.110 to 3.2.123\n"
      "  rather than a new one beside it. The question is identical —\n"
      "  which tense-ending, given a time and a situation of speaking\n"
      "  — and `Lakara` already carried a per-row time defaulting to\n"
      "  the past, with the resolver filtering on it, so a future row\n"
      "  cannot answer a past question.",
    "3.3.5":
      "SETTLED — विभाषा कदाकर्ह्योः: कदा भुङ्क्ते, कदा भोक्ष्यते, कदा\n"
      "  भोक्ता — all three stand, which is what विभाषा buys. कर्हि\n"
      "  likewise.\n\n"
      "SCAR — WHY THIS ONE IS OPTIONAL AND 3.3.4 IS NOT, nothing\n"
      "  says. Both name particles, both give लट् for the future, and\n"
      "  the only difference between them is that this one carries\n"
      "  विभाषा. Recorded as a fact about the text rather than\n"
      "  explained.",
    "3.3.6":
      "SETTLED — किंवृत्ते लिप्सायाम्: कं भवन्तो भोजयन्ति? कतरो\n"
      "  भिक्षां दास्यति, ददाति, दाता वा?\n\n"
      "SETTLED — लिप्सा, लब्धुमिच्छा प्रार्थनाभिलाषः — the wish to\n"
      "  obtain, and the vṛtti sets the scene rather than glossing\n"
      "  the word: लब्धुकामः पृच्छति, one who wants something asks.\n"
      "  लिप्सायामिति किम्? कः पाटलिपुत्रं गमिष्यति — asking who will\n"
      "  go, wanting nothing by it, the rule does not reach.\n\n"
      "SETTLED — किंवृत्त's EXTENT IS FIXED BY परिसंख्यान AND NOT BY\n"
      "  THE WORD. किमो वृत्तं किंवृत्तम् would take in anything\n"
      "  derived from किम्; वृत्तग्रहणेन तद् विभक्त्यन्तं प्रतीयात्,\n"
      "  डतरडतमौ चेति परिसंख्यानं स्मर्यते — the case-inflected forms,\n"
      "  and डतर and डतम besides. A list REMEMBERED (स्मर्यते) rather\n"
      "  than derived, which is why कतर and कतम are examples here.",
    "3.3.7":
      "SETTLED — लिप्स्यमानसिद्धौ च: यो भक्तं ददाति, स स्वर्गं गच्छति.\n"
      "  लिप्स्यमानात् सिद्धिर्लिप्स्यमानसिद्धिः — that what is wanted\n"
      "  will come of it.\n\n"
      "SETTLED — अकिंवृत्तार्थोऽयमारम्भः: the rule exists FOR the\n"
      "  ground 3.3.6 could not reach, where no form of किम् stands.\n"
      "  A rule defined by the gap in the one before it, as 3.2.17\n"
      "  and 3.2.21 were.\n\n"
      "SETTLED — and the vṛtti explains the USE rather than the form:\n"
      "  लिप्स्यमानाद् भक्तात् स्वर्गसिद्धिमाचक्षाणो दातारं\n"
      "  प्रोत्साहयति — one urges a giver on by telling him what his\n"
      "  gift will get him. A rule of grammar glossed by what the\n"
      "  speaker is doing.",
    "3.3.8":
      "SETTLED — लोडर्थलक्षणे च: उपाध्यायश्चेदागच्छति, अथ त्वं\n"
      "  छन्दोऽधीष्व.\n\n"
      "SETTLED — लोडर्थः प्रैषादिर्लक्ष्यते येन, स लोडर्थलक्षणो\n"
      "  धात्वर्थः. The act is what MARKS OUT the command and is not\n"
      "  itself commanded: उपाध्यायागमनमध्ययनप्रैषस्य लक्षणम् — the\n"
      "  teacher's coming is the sign of the order to study, and the\n"
      "  future ending falls on the sign and not on the order.",
    "3.3.9":
      "SETTLED — लिङ् चोर्ध्वमौहूर्तिके, and चकाराल्लट् च, so both\n"
      "  endings stand: उपाध्यायश्चेदागच्छेत्, उपाध्यायश्चेदागच्छति.\n"
      "  भविष्यति, विभाषा and लोडर्थलक्षण all run down into it.\n\n"
      "SETTLED — ऊर्ध्वं मुहूर्ताद् भव ऊर्ध्वमौहूर्तिकः, later than\n"
      "  this hour. And भविष्यतश्चैतद् विशेषणम् — it QUALIFIES the\n"
      "  future rather than being a time of its own, which is why the\n"
      "  row states it beside the future and not instead of it.\n\n"
      "SCOPE — निपातनात् समासः, उत्तरपदवृद्धिश्च: the compound in the\n"
      "  rule is itself a निपातन, both its formation and the\n"
      "  strengthening in its second member fixed by being stated.\n"
      "  A rule whose own wording needs a निपातन to exist.",
    "3.3.10":
      "SETTLED — तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम्: भोक्तुं व्रजति,\n"
      "  भोजको व्रजति. भुजिक्रियार्थो व्रजिरत्रोपपदम्.\n\n"
      "SETTLED — TWO CONDITIONS, TWO COUNTER-EXAMPLES, NEITHER\n"
      "  REDUNDANT. क्रियायामिति किम्? भिक्षिष्य इत्यस्य जटाः — what\n"
      "  stands beside is not an act. क्रियार्थायामिति किम्? धावतस्ते\n"
      "  पतिष्यति दण्डः — an act stands beside, but the root's act is\n"
      "  not done FOR it: the stick falls as he runs, not so that he\n"
      "  may run.\n\n"
      "SETTLED — AND THE VĀSARŪPA SUSPENSION, A THIRD TIME. The vṛtti\n"
      "  asks why ण्वुल् is given when 3.1.133 gives it already, and\n"
      "  the answer runs through two steps: लृटा क्रियार्थोपपदेन\n"
      "  बाध्यते, 3.3.13's लृट् would displace it; and वासरूपविधिना\n"
      "  सोऽपि भविष्यति — could it not stand beside by 3.1.94? एवं\n"
      "  तर्ह्येतज् ज्ञाप्यते: क्रियायामुपपदे क्रियार्थायां वासरूपेण\n"
      "  तृजादयो न भवन्ति (महाभाष्य २.१४१). The rule's own redundancy\n"
      "  is the evidence that वासरूप does not hold here, and तेन\n"
      "  कर्ता व्रजति, विक्षिपो व्रजति are ruled out by it.\n"
      "  This is the SAME MOVE 3.2.146 made from वुञ् and 3.2.177\n"
      "  relied on, now in another pāda and over other ground. The\n"
      "  ज्ञापक is not one section's quirk: it is how the commentary\n"
      "  establishes a suspension wherever it needs one.",
    "3.3.11":
      "SETTLED — भाववचनाश्च: पाकाय व्रजति, भूतये व्रजति, पुष्टये\n"
      "  व्रजति. The affixes given under 3.3.18 भावे come here too.\n\n"
      "SETTLED — AND IT EXISTS BECAUSE OF THE SUSPENSION THE RULE\n"
      "  BEFORE IT ESTABLISHED. किमर्थमिदं यावता विहिता एव ते?\n"
      "  क्रियार्थोपपदे विहितेनास्मिन्विषये तुमुना बाध्येरन् — 3.3.10's\n"
      "  तुमुन्, given for this very ground, would displace them; and\n"
      "  वासरूपविधिश्चात्र नास्तीत्युक्तम्, the escape by 3.1.94 was\n"
      "  shut one sūtra back. Two rules in a row whose whole reason\n"
      "  is what the ज्ञापक took away.\n\n"
      "SETTLED — वचनग्रहणं किमर्थम्? वाचका यथा स्युः. The word वचन is\n"
      "  there so the affixes must actually NAME the act, and the\n"
      "  vṛtti says what that comes to: याभ्यः प्रकृतिभ्यो येन\n"
      "  विशेषणेन विहिताः, यदि ताभ्यस्तथैव भवन्ति — from the same\n"
      "  roots under the same conditions they were given for,\n"
      "  नासामञ्जस्येन, and not irregularly. A word in the rule\n"
      "  holding the borrowed affixes to the terms of their own.\n\n"
      "DEBT — 3.3.18 AND AFTER ARE NOT CODIFIED, so the class this\n"
      "  rule names cannot yet be enumerated. It points FORWARD\n"
      "  inside its own pāda, and the debt is asserted as a test so\n"
      "  that reaching 3.3.18 collects it.",
    "3.3.12":
      "SETTLED — अण् कर्मणि च: काण्डलावो व्रजति, अश्वदायो व्रजति,\n"
      "  गोदायो व्रजति, कम्बलदायो व्रजति. चकारः सन्नियोगार्थः — the च\n"
      "  joins this condition to the ones running rather than adding\n"
      "  a ground of its own.\n\n"
      "SETTLED — AND THE अण् IS 3.2.1's, RESTATED. कर्मण्यण् इति\n"
      "  सामान्येन विहितो वासरूपविधेरभावाद् ण्वुला बाधितः पुनरण्\n"
      "  विधीयते: the affix 3.2.1 gives for an object was displaced\n"
      "  here by 3.3.10's ण्वुल्, and could not stand beside it\n"
      "  because वासरूप is suspended, so it is said again. The third\n"
      "  rule in a row that the suspension explains, and the pāda's\n"
      "  first backward reach into 3.2.\n\n"
      "SETTLED — once restated it wins twice over, by two different\n"
      "  principles: सोऽपवादत्वाद् ण्वुलं बाधते, being narrower it\n"
      "  defeats ण्वुल्; परत्वात् कादीन्, being later it defeats क and\n"
      "  the rest. तेनापवादविषयेऽपि भवत्येव — it holds even on ground\n"
      "  those others had taken. The resolver reaches the first by\n"
      "  specificity; the second is recorded, since a table has no\n"
      "  order to appeal to.",
    "3.3.13":
      "SETTLED — लृट् शेषे च: करिष्यति, हरिष्यति; and करिष्यामीति\n"
      "  व्रजति for the च.\n\n"
      "SETTLED — शेषः क्रियार्थोपपदादन्यः. The rule is defined by the\n"
      "  ones around it and states no condition of its own — 'the\n"
      "  rest' means whatever 3.3.10 to 3.3.12 did not take.\n\n"
      "SETTLED — AND THE च REACHES BACK INTO WHAT शेष EXCLUDED.\n"
      "  चकारात् क्रियायां चोपपदे क्रियार्थायाम्: लृट् stands there\n"
      "  too. So the rule means 'everything else, and also the thing\n"
      "  else was defined against' — which is why 3.3.10 had to argue\n"
      "  that its ण्वुल् survives this rule at all.",
    "3.3.14":
      "SETTLED — लृटः सद्वा: करिष्यन्तं देवदत्तं पश्य, करिष्यमाणं\n"
      "  देवदत्तं पश्य, हे करिष्यन्, अर्जयिष्यमाणो वसति.\n\n"
      "SETTLED — THE RULE NAMES ITS AFFIXES BY A संज्ञा AND NOT BY\n"
      "  THEIR FORMS. लृटः स्थाने सत्संज्ञौ शतृशानचौ वा भवतः — सत् is\n"
      "  the name 3.2.127 तौ सत् confers, so this rule reaches\n"
      "  whatever that one names. Codified by ASKING 3.2.127 rather\n"
      "  than restating the pair: `lrt_substitute` calls\n"
      "  `sat_samjna`, so the dependence is a real call and not a\n"
      "  declaration. And 3.2.127's own vṛtti had already widened the\n"
      "  name past the rules that gave it — शतृशानज्मात्रस्य संज्ञा\n"
      "  भवति — which is exactly what lets this rule borrow it.\n\n"
      "SETTLED — व्यवस्थितविभाषेयम्, AND THE CONDITIONS ARE BORROWED\n"
      "  TOO. The वा is not free: तेन यथा लटः शतृशानचौ तथास्यापि\n"
      "  भवतः, अप्रथमासमानाधिकरणादिषु नित्यम्, अन्यत्र विकल्पः. So\n"
      "  3.2.124's अप्रथमासमानाधिकरण decides whether this rule may be\n"
      "  declined. 3.3.14 states NO condition of its own — it takes\n"
      "  its affixes from one rule and its conditions from another,\n"
      "  and is nothing but the instruction to do for लृट् what was\n"
      "  done for लट्.\n\n"
      "SETTLED — प्रथमासमानाधिकरणे विकल्पः: करिष्यन् देवदत्तः stands\n"
      "  and so does करिष्यति.",
    "3.3.15":
      "SETTLED — अनद्यतने लुट्: श्वःकर्ता, श्वो भोक्ता. लृटोऽपवादः.\n\n"
      "SETTLED — अनद्यतन इति बहुव्रीहिनिर्देशः, तेन व्यामिश्रे न\n"
      "  भवति: अद्य श्वो वा भविष्यति. The compound's FORM excludes the\n"
      "  mixed case — and this is the identical device, with the\n"
      "  identical wording and the identical reason, that 3.2.111 used\n"
      "  for the past. One grammatical trick serving two tenses a\n"
      "  pāda apart, which is why both rows carry the same field.\n\n"
      "SCOPE — परिदेवने श्वस्तनी भविष्यदर्थे वक्तव्या is a vārttika\n"
      "  for LAMENT: इयं नु कदा गन्ता, यैवं पादौ निदधाति — when will\n"
      "  she ever get there, walking like that. अयं नु कदाध्येता, य\n"
      "  एवमनभियुक्तः. The ending of the not-today future used of\n"
      "  something exasperating now.",
    "3.3.16": "SETTLED — पदरुजविशस्पृशो घञ्. The first rule of the घञ् run, and\n  where भविष्यति stops: भविष्यतीति निवृत्तम्, इत उत्तरं त्रिष्वपि\n  कालेषु प्रत्ययाः — from here the affixes hold in all three\n  times. A heading dropped with nothing put in its place, which\n  the commentary must say because the sūtras cannot.\n\nSETTLED — TWO ROWS FOR ONE SŪTRA. The vārttika स्पृश उपताप holds\n  स्पृश् to affliction, and it CHANGES THE OUTPUT: without it the\n  rule reaches स्पर्शो देवदत्तः, which takes 3.1.134's अच्\n  instead. 3.2.24 settled that such a vārttika belongs in the\n  table and not in a note, so the sūtra has a row for its three\n  plain roots and another for स्पृश् with its sense.\n\nSCAR — स्वरे विशेषः. The two स्पर्श forms differ in ACCENT alone,\n  and the sūtrapāṭha on disk is unaccented. So the distinction is\n  recorded and cannot be checked against the corpus — the same\n  boundary NORTH_STAR §7 states for accent generally.",
    "3.3.17": "SETTLED — सृ स्थिरे, with a vārttika व्याधिमत्स्यबलेषु adding\n  three senses.\n\nSETTLED — and the vṛtti REASONS the root into the sense rather\n  than asserting the fit: स चिरं तिष्ठन् कालान्तरं सरतीति\n  धात्वर्थस्य कर्ता युज्यते — what stays on 'moves' into another\n  time, so a root meaning motion suits a word meaning what\n  endures. An argument from the sense of the root to the sense of\n  the word, which the rule does not make.",
    "3.3.18": "SETTLED — भावे, THE RULE THE WHOLE RUN STANDS ON. 3.3.11 pointed\n  forward to it from seven sūtras back, and that debt is now\n  paid: the class it named can be enumerated.\n\nSETTLED — WHY भू AND NOT ANOTHER ROOT. क्रियासामान्यवाची भवतिः,\n  तेनार्थनिर्देशः क्रियमाणः सर्वधातुविषयः कृतो भवति — भू names\n  action at large, so naming the sense with it reaches every\n  root. The choice of word in the rule is itself an argument.\n\nSETTLED — AND WHAT THE AFFIX ADDS IS NOT THE MEANING.\n  धात्वर्थश्च धातुनैवोच्यते — the root already says its own\n  meaning — यस्तस्य सिद्धता नाम धर्मः तत्र घञादयः प्रत्यया\n  विधीयन्ते: what the affix adds is the act's standing as an\n  accomplished THING. A careful separation, and the reason भावे\n  is not simply 'in the sense of the root'.\n\nSETTLED — पुँल्लिङ्गमेकवचनं चात्र न तन्त्रम्: the masculine\n  singular of the word भावे is not binding, and पक्तिः, पचनम्,\n  पक्वम्, पाकौ, पाकाः all come. A grammatical form inside a rule\n  read as NOT meaning what that form means anywhere else.",
    "3.3.19": "SETTLED — अकर्तरि च कारके संज्ञायाम्, and चकारः\n  संज्ञाव्यभिचारार्थः — the च lets the name-sense be departed\n  from.\n\nSETTLED — A ज्ञापक FROM A WORD THAT NEED NOT HAVE BEEN THERE.\n  कारकग्रहणं पर्युदासे न कर्तव्यम्: read as an exclusion, अकर्तरि\n  makes the word कारक unnecessary. तत् क्रियते\n  प्रसज्यप्रतिषेधेऽपि समासोऽस्तीति ज्ञापनार्थम् — it is stated to\n  show that a compound forms even with a flat negation, which\n  6.1.45 then relies on. A redundancy in one rule licensing a\n  compound in another, and the third kind of evidence this\n  project has met from a rule's own wording after 3.2.111's\n  compound form and 3.3.16's spelling.\n\nSETTLED — इत उत्तरं भावे अकर्तरि च कारक इति च द्वयमनुवर्तते. Two\n  conditions run forward from here. The codification cannot hold\n  a running condition, so each row states its own — and the rows\n  that name a preverb and a root state neither, which is exactly\n  what the अनुवृत्ति is for.\n\nDEBT — 6.1.45 is not codified, and this rule's ज्ञापक is stated\n  FOR it. 3.2.2 and 3.2.8 already owe that rule for their\n  आ-final shapes; this is a third claim on it, of a different\n  kind.",
    "3.3.20": "SETTLED — परिमाणाख्यायां सर्वेभ्यः.\n\nSETTLED — A RULE REACHING FORWARD BY SAYING 'ALL'.\n  सर्वग्रहणमपोऽपि बाधनार्थम् — the word is there to defeat अप् as\n  well, and the reason is that it could not otherwise:\n  पुरस्तादपवादन्यायेन ह्यचमेव बाधेत नापम्, by the ordinary\n  reading an अपवाद displaces only what PRECEDES it, and अप् comes\n  at 3.3.57. So a word is spent to reach a rule thirty-seven\n  sūtras ahead.\n\nSETTLED — आख्याग्रहणं रूढिनिरासार्थम्, तेन संख्यापि गृह्यते, न\n  प्रस्थाद्येव: आख्या keeps out mere established usage, so NUMBER\n  counts as a measure and not only the named units.\n\nSCOPE — स्त्रीप्रत्ययास्तु न बाध्यन्ते, एका तिलोच्छ्रितिः, द्वे\n  प्रसृती — the feminine affixes are not displaced. And\n  दारजारौ कर्तरि णिलुक् च is a vārttika.",
    "3.3.21": 'SETTLED — इङश्च, अचोऽपवादः. Two vārttikas, one giving the\n  feminine and one three senses for शृ, the last quoted with a\n  verse.',
    "3.3.22": 'SETTLED — उपसर्गे रुवः. The rule wants A PREVERB WITHOUT SAYING\n  WHICH — a third thing to do with the category, beside naming\n  one (3.3.23) and refusing one (3.3.24). Three rules in a row,\n  three different uses, which is why the row carries\n  `any_upasarga` as its own field rather than an empty list.',
    "3.3.23": 'SETTLED — समि युद्रुदुवः. समीति किम्? प्रयवः.',
    "3.3.24": "SETTLED — श्रिणीभुवोऽनुपसर्गे, अजपोरपवादः.\n\nSETTLED — AND THE VṚTTI DEFENDS IT AGAINST TWO FORMS RATHER THAN\n  LETTING THEM STAND. कथं प्रभावो राज्ञः? प्रकृष्टो भाव इति\n  प्रादिसमासो भविष्यति — that is प्र compounded with भाव, not\n  this affix after a preverbed root, so it is parsed away. कथं च\n  नयो राज्ञः? कृत्यल्युटो बहुलम् इत्यज् भविष्यति — that one is\n  sent to 3.3.113.\n\nDEBT — 3.3.113, and this is the first of FOUR appeals to it in\n  this run alone (3.3.24, 3.3.26, 3.3.43, 3.3.44), on top of\n  3.2.53 and 3.2.153. It is the commentary's standing answer for\n  a form the run does not give, and it is codified in this very\n  pāda — so the debt test will collect the lot at once.",
    "3.3.25": 'SETTLED — वौ क्षुश्रुवः, अपोऽपवादः. वाविति किम्? क्षवः,\n  श्रवः.',
    "3.3.26": 'SETTLED — अवोदोर्नियः.\n\nDEBT — कथमुन्नयः पदार्थानाम्? कृत्यल्युटो बहुलम् इत्यज् भविष्यति.\n  The second appeal to 3.3.113 in three sūtras.',
    "3.3.27": 'SETTLED — प्रे द्रुस्तुस्रुवः. प्र इति किम्? द्रवः, स्तवः,\n  स्रवः.',
    "3.3.28": 'SETTLED — निरभ्योः पूल्वोः, and यथासंख्यमुपसर्गसंबन्धः: निस् with\n  पू, अभि with लू, the lists not to be crossed. Held as bound\n  pairs for the reason 3.2.5 established.\n\nSETTLED — पू इति पूङ्पूञोः सामान्येन ग्रहणम्, both roots spelt\n  alike being meant. The same question 3.2.39 settled with\n  द्वयोरपि ग्रहणम्, and the same answer.',
    "3.3.29": "SETTLED — उन्न्योर्ग्रः, with गृ शब्दे and गृ निगरणे both meant —\n  द्वयोरपि ग्रहणम् again, one sūtra after 3.3.28 used it. The\n  formula is the commentary's standing move for two roots spelt\n  alike, and the two instances sit adjacent.",
    "3.3.30": 'SETTLED — कॄ धान्ये, with उन्न्योः running down from 3.3.29.\n\nSETTLED — AND ONE OF TWO ROOTS IS EXCLUDED BY अनभिधानात्.\n  विक्षेपार्थस्य किरतेर्ग्रहणम्, न हिंसार्थस्य, अनभिधानात् — the\n  कॄ meaning to scatter, not the one meaning to hurt, and the\n  ground is that no such word is in use. The same limit 3.2.1 and\n  3.1.108 were held by. Not codified as a condition because there\n  is no condition to codify: the check is against usage.',
    "3.3.31": 'SETTLED — यज्ञे समि स्तुवः, and the vṛtti defines by the\n  SITUATION rather than by a synonym: समेत्य स्तुवन्ति यस्मिन्\n  देशे छन्दोगाः, स देशः संस्ताव इत्युच्यते — the place where the\n  chanters gather. The same kind of gloss 3.2.179 gave प्रतिभूः.',
    "3.3.32": 'SETTLED — प्रे स्त्रोऽयज्ञे. The rule before REQUIRED the\n  sacrifice and this one refuses it — a pair divided by one\n  sense, one sūtra apart, as 3.2.9 and 3.2.10 were by उद्यमन.',
    "3.3.33": 'SETTLED — प्रथने वावशब्दे, and TWO CONDITIONS ON DIFFERENT AXES.\n  The sense must be spreading AND what is spread must not be\n  speech: प्रथन इति किम्? तृणविस्तरः; अशब्द इति किम्? विस्तरो\n  वचसाम्.\n\nSCAR — WRITTEN FIRST WITH BOTH ON ONE AXIS, WHERE THEY CANCEL.\n  The refusal went into the same field as the requirement, and\n  one input cannot be प्रथन and शब्द at once, so विस्तरो वचसाम्\n  could not be tested at all. A field-name collision of the kind\n  that splits — the ninth so far, and seven of the nine have\n  gone this way.',
    "3.3.34": "SETTLED — छन्दोनाम्नि च, वौ स्त्र इति वर्तते.\n\nSETTLED — WHICH छन्दस् IS MEANT, READ OFF THE WORD नामन्.\n  वृत्तमत्र छन्दो गृह्यते, यस्य गायत्र्यादयो विशेषाः, न\n  मन्त्रब्राह्मणम्, नामग्रहणात् — METRE, of which गायत्री and the\n  rest are kinds, and not sacred text; and the ground is that the\n  rule says 'name', because metres have names and scripture is\n  not named that way. An argument from one word to the whole\n  scope of the rule.\n\nSETTLED — and the NAME is the whole word: विष्टारपङ्क्तिशब्दोऽत्र\n  छन्दोनाम, न घञन्तं शब्दरूपम्, तत्र त्ववयवत्वेन वर्तते. The\n  fifth समुदायोपाधि met, after 3.2.80, 3.2.92, 3.2.99 and\n  3.2.185.",
    "3.3.35": "SETTLED — उदि ग्रहः, अपोऽपवादः.\n\nSCOPE — छन्दसि निपूर्वादपीष्यते स्रुगुद्यमननिपातनयोः, with\n  हकारस्य भकारः: उद्ग्राभं च निग्राभं च ब्रह्म देवा अवीवृधन्\n  (मा०सं० १७.६४). A Vedic form in which the root's ह becomes भ,\n  quoted with its passage — the citation is checkable and is\n  recorded as the attribution rule requires.",
    "3.3.36": 'SETTLED — समि मुष्टौ, with मुष्टिरङ्गुलिसंनिवेशः and\n  दृढमुष्टिताख्यायते — the sense is a firm grip and not the hand\n  itself. मुष्टाविति किम्? संग्रहो धान्यस्य.',
    "3.3.37": 'SETTLED — परिन्योर्नीणोर्द्यूताभ्रेषयोः, अचोऽपवादः.\n\nSETTLED — यथासंख्यम् BINDING THREE LISTS AT ONCE, which no rule\n  of the pāda before did. द्यूताभ्रेषयोः, अत्रापि यथासंख्यमेव\n  संबन्धः: परि with नी and with dicing, नि with इण् and with\n  correctness — द्यूतविषयश्चेन्नयतेरर्थः, अभ्रेषविषयश्चेदिणर्थः.\n  3.2.5 and 3.2.13 bound two lists of words; 3.2.186 bound a\n  kāraka to a kind of being; this binds preverb, root AND sense\n  in one stroke, so the row holds triples rather than pairs.\n\nSETTLED — अभ्रेष is glossed by what it is not:\n  पदार्थानामनपचारो यथाप्राप्तकरणमभ्रेषः, doing things as they\n  should be done.',
    "3.3.38": 'SETTLED — परावनुपात्यय इणः. One preverb and one root giving two\n  words that differ by a single sound and mean contrary things:\n  पर्यायः is a turn taken in order, पर्ययः is the overstepping of\n  it. क्रमप्राप्तस्यानतिपातोऽनुपात्ययः.',
    "3.3.39": 'SETTLED — व्युपयोः शेतेः पर्याये, and the vṛtti glosses by the\n  situation as 3.2.179 and 3.3.31 did: तव राजानमुपशयितुं पर्याय\n  इत्यर्थः.',
    "3.3.40": "SETTLED — हस्तादाने चेरस्तेये, TWO CONDITIONS ON DIFFERENT\n  FOOTINGS as 3.3.33 had. हस्तादान इति किम्? वृक्षशिखरे\n  फलप्रचयं करोति. अस्तेय इति किम्? फलप्रचयश्चौर्येण — picking by\n  theft IS within reach and is still refused, so the second is\n  not a kind of the first and needs its own axis.\n\nSETTLED — हस्तादानग्रहणेन प्रत्यासत्तिरादेयस्य लक्ष्यते: naming\n  the hand MARKS OUT nearness, and is not itself the condition.\n  The same shape as 3.3.52's merchants.\n\nSCOPE — उच्चयस्य प्रतिषेधो वक्तव्यः.",
    "3.3.41": "SETTLED — निवासचितिशरीरोपसमाधानेष्वादेश्च कः. FOUR SENSES IN ONE\n  RULE, each glossed: निवसन्त्यस्मिन्निति निवासः, चीयतेऽसौ चितिः,\n  पाण्यादिसमुदायः शरीरम्, राशीकरणमुपसमाधानम्. This is why the\n  sense field holds alternatives rather than one string — a\n  migration made for this rule.\n\nSETTLED — AND IT CHANGES THE ROOT AS WELL AS ADDING TO IT.\n  आदेश् च कः: चि's first sound becomes क, giving काय. With 3.3.42\n  the only rules of the run that touch the root, so the\n  substitute is stated per row.\n\nSCAR — A FORM REFUSED BY WHAT THE SPEAKER MEANT. इह कस्माद् न\n  भवति महान् काष्ठनिचयः? बहुत्वमत्र विवक्षितं नोपसमाधानम् — mere\n  muchness is meant and not heaping-up. The situation is the\n  same and the intention is not, and विवक्षा cannot be read off a\n  form. Passed in like every other semantic condition, and the\n  boundary NORTH_STAR §7 states.",
    "3.3.42": 'SETTLED — संघे चानौत्तराधर्ये, AND THE CONDITION IS CARVED OUT OF\n  A DEFINITION THE RULE DOES NOT GIVE. प्राणिनां समुदायः संघः, स\n  च द्वाभ्यां प्रकाराभ्यां भवति — एकधर्मसमावेशेन, औत्तराधर्येण\n  वा; तत्र औत्तराधर्यपर्युदासादितरो गृह्यते. The rule names one\n  half to exclude it, and what is left is the other.\n\nSETTLED — so two counter-examples fall outside for two different\n  reasons. सूकरनिचयः fails the stated half. कृताकृतसमुच्चयः and\n  प्रमाणसमुच्चयः fail the UNSTATED one — प्राणिविषयत्वात्\n  संघस्येह न भवति, they are not groups of living beings at all.\n  A rule whose reach depends on a definition found only in the\n  commentary.',
    "3.3.43": 'SETTLED — कर्मव्यतिहारे णच् स्त्रियाम्. कर्म क्रिया, व्यतिहारः\n  परस्परकरणम् — and कर्मन् here is the ACT, not the kāraka and\n  not the word, which is a third reading of that term after the\n  two 3.2.1 and 3.2.22 needed.\n\nSETTLED — चकारो विशेषणार्थः for 5.4.14 णचः स्त्रियामञ्: the च is\n  spent so a rule two adhyāyas on can pick this affix out.\n\nSCOPE — बाधकविषयेऽपि क्वचिदिष्यते, व्यावचोरी, व्यावचर्ची; and\n  यह न भवति — व्यतीक्षा, व्यत्युक्षी. तदेतद् वैचित्र्यं कथं\n  लभ्यते? कृत्यल्युटो बहुलम् — 3.3.113 invoked for the\n  IRREGULARITY itself and not for one form.',
    "3.3.44": 'SETTLED — अभिविधौ भाव इनुण्. अभिविधिरभिव्याप्तिः,\n  क्रियागुणाभ्यां कार्त्स्न्येन संबन्धः.\n\nSETTLED — वासरूप SUSPENDED BY REPEATING A WORD, NOT BY A ज्ञापक.\n  भाव इति वर्तमाने पुनर्भावग्रहणं वासरूपनिरासार्थम्, तेन घञ् न\n  भवति: भावे was already running from 3.3.18, and saying it again\n  cancels 3.1.94 so घञ् cannot stand beside. The FOURTH\n  suspension this project has met and the first done this way —\n  3.2.146, 3.2.177 and 3.3.10 all argued from a ज्ञापक. Repeating\n  a running word was already known to WIDEN (3.2.106, 3.2.124)\n  and to FENCE OFF (3.2.14, 3.1.141); this is a third use of it.\n\nSETTLED — and the suspension is not total: ल्युटा तु समावेश\n  इष्यते, संकूटनं वर्तते, तत् कथम्? 3.3.113 कृत्यल्युटो बहुलम् — the fourth appeal to that rule in this run.',
    "3.3.45": "SETTLED — आक्रोशेऽवन्योर्ग्रहः. आक्रोशः शपनम्.\n\nSETTLED — AND THE AFFIX CARRIED DOWN IS NOT THE NEAREST ONE.\n  दृष्टानुवृत्तिसामर्थ्याद् घञनुवर्तते, नानन्तर इनुण् — घञ् runs\n  down from further back and 3.3.44's इनुण्, standing immediately\n  before, does not. The ground is the STRENGTH of an अनुवृत्ति\n  already seen at work.\n  A third fact about how conditions travel: 3.2.122 showed one\n  vaulting forward over rules that had dropped it\n  (मण्डूकप्लुति), 3.3.49 shows one read backward\n  (सिंहावलोकित), and this shows the nearest word LOSING to a\n  further one. None of the three is inferable from position.",
    "3.3.46": "SETTLED — प्रे लिप्सायाम्. लिप्सा was 3.3.6's condition too, forty\n  sūtras back and for a tense-ending rather than an affix — the\n  same sense doing work in two different questions of one pāda.",
    "3.3.47": "SETTLED — परौ यज्ञे, and यज्ञविषयश्चेत् प्रत्ययान्ताभिधेयः स्यात्\n  — the condition is on what the FINISHED WORD denotes, which is\n  the field 3.2.25 had to be split off from the act's sense.",
    "3.3.48": "SETTLED — नौ वृ धान्ये, अपोऽपवादः. धान्य इति किम्? निवरा कन्या.\n\nSETTLED — वृ इति वृङ्वृञोः सामान्येन ग्रहणम्, the THIRD time in\n  twenty sūtras that a spelling is taken generally over two\n  roots: 3.3.28's पू, 3.3.29's गृ, and this. The formula\n  द्वयोरपि ग्रहणम् / सामान्येन ग्रहणम् is the commentary's\n  standing move for the ambiguity, and NORTH_STAR §7 records\n  that the dhātupāṭha on disk carries 174 such doubled names.",
    "3.3.49": "SETTLED — उदि श्रयतियौतिपूद्रुवः, अजपोरपवादः.\n\nSETTLED — AND ITS OPTIONALITY IS BORROWED FROM THE RULE AFTER IT,\n  BY A DEVICE NOT MET BEFORE. कथं पतनान्ताः समुच्छ्रयाः?\n  वक्ष्यमाणं विभाषाग्रहणमिह सिंहावलोकितन्यायेन संबध्यते — the\n  विभाषा about to be stated at 3.3.50 is read BACK into this rule\n  by the LION'S BACKWARD GLANCE.\n  अनुवृत्ति runs forward. मण्डूकप्लुति, met at 3.2.122, vaults\n  forward over rules that had dropped a condition. This looks\n  BACKWARD: a word not yet uttered conditions a rule already\n  given. Codified as `optional` on the row, with the borrowing\n  recorded — there is no way to represent a word that has not\n  been said yet, and the honest thing is to say where it came\n  from.",
    "3.3.50": 'SETTLED — विभाषाङि रुप्लुवोः: आरावः and आरवः both stand. The word\n  विभाषा is spent twice over — 3.3.49 borrows it BACKWARD by\n  सिंहावलोकित, and it runs FORWARD from here through 3.3.55.',
    "3.3.51": 'SETTLED — अवे ग्रहो वर्षप्रतिबन्धे. प्राप्तकालस्य वर्षस्य\n  कुतश्चिन्निमित्तादभावो वर्षप्रतिबन्धः — rain due and withheld.\n  वर्षप्रतिबन्ध इति किम्? अवग्रहः पदस्य, where the same word means\n  the pause between the parts of a compound. And 3.3.45 has the\n  same root and preverb with a different sense, so the two are\n  told apart by nothing else.',
    "3.3.52": "SETTLED — प्रे वणिजाम्, AND THE MERCHANTS ARE NOT THE CONDITION.\n  वणिक्संबन्धेन च तुलासूत्रं लक्ष्यते, न तु वणिजस्तन्त्रम् —\n  naming them MARKS OUT the scale-cord: तुला प्रगृह्यते येन\n  सूत्रेण स शब्दार्थः. So वणिगन्यो वा, a merchant or anyone else.\n  A rule whose stated condition is a pointer to the real one, as\n  3.3.40's hand was.",
    "3.3.53": 'SETTLED — रश्मौ च. ग्रहो विभाषा प्र इति वर्तते — three things\n  carried down at once from three different places, which is as\n  much as any rule of this pāda leaves unsaid.',
    "3.3.54": 'SETTLED — वृणोतेराच्छादने. प्रत्ययान्तेन चेदाच्छादनविशेष उच्यते —\n  again a condition on what the finished word denotes. आच्छादन\n  इति किम्? प्रवरा गौः.',
    "3.3.55": 'SETTLED — परौ भुवोऽवज्ञाने. अवज्ञानमसत्कारः. अवज्ञान इति किम्?\n  सर्वतो भवनं परिभवः — where the word means being all round, the\n  short form stands for both senses and the affix does not come.\n\nSCAR — THE TWO WITNESSES TO THE MŪLA DISAGREE, AND THE COMMENTARY\n  SETTLES IT. GRETIL reads प्रौ, Vidyut reads परौ, and those are\n  different preverbs — not a spelling or a sandhi. The Kāśikā is\n  decisive: परिशब्द उपपदे भवतेः, and every form it gives is\n  परिभावः, परिभवः. So परौ stands and GRETIL is wrong here.\n  The collation already flagged the pair as divergent; what the\n  vṛtti adds is WHICH WITNESS TO BELIEVE, which no amount of\n  comparing two mūla texts could have given. The first time in\n  this project that a commentary has decided a reading.',
    "3.3.56": "SETTLED — एरच्, घञोऽपवादः, and the FIRST rule of the run to reach\n  by the root's SHAPE rather than by naming roots.\n\nSETTLED — AND IT STATES HOW FAR THE TWO HEADINGS REACH. भावे,\n  अकर्तरि च कारक इति प्रकृतमनुवर्तते यावत् कृत्यल्युटो बहुलम्\n  इति — 3.3.18's and 3.3.19's conditions run all the way to\n  3.3.113. An extent stated outright, as 3.2.134's आ क्वेः was,\n  and this one NAMES the closing rule rather than giving a\n  number. The same debt as everything else in this pāda: it can\n  be recorded now and checked when 3.3.113 is codified.\n\nSETTLED — चकारो विशेषणार्थः for 6.2.143 and 6.2.144, two accent\n  rules three adhyāyas on. A च spent to be picked out later, as\n  3.3.43's was for 5.4.14.\n\nSCOPE — अज्विधौ भयादीनामुपसंख्यानम्, नपुंसके क्तादिनिवृत्त्यर्थम्:\n  भयम्, वर्षम्. And जवसवौ छन्दसि वक्तव्यौ, both with their\n  passages — ऊर्वोरस्तु मे जवः (पै०सं० २०.३६.७), पञ्चौदनस् सवः\n  (पै०सं० ८.१९.३).",
    "3.3.57": "SETTLED — ॠदोरप्, घञोऽपवादः. And 3.3.20's सर्वग्रहण was spent\n  thirty-seven sūtras back precisely to reach FORWARD and defeat\n  this affix, since पुरस्तादपवादन्यायेन it could not have been\n  reached otherwise.\n\nSETTLED — TWO MARKS IN THE RULE, NEITHER DOING GRAMMAR.\n  पित्करणं स्वरार्थम् — the प is for the accent. दकारो\n  मुखसुखार्थः, मा भूत् तादपि परस्तपरः — the द is for EASE OF\n  PRONUNCIATION, so the rule does not read as तपर. A letter put\n  in a sūtra to keep the sūtra sayable, which is a use of a\n  letter this project had not met.",
    "3.3.58": 'SETTLED — ग्रहवृदृनिश्चिगमश्च, घञोऽपवादः,\n  निश्चिनोतेस्त्वचोऽपवादः. निश्चिग्रहणं स्वरार्थम् — that root\n  is named for the ACCENT alone, the affix being reachable\n  without naming it.\n\nSCOPE — वशिरण्योरुपसंख्यानम्: वशः, रणः. And घञर्थे कविधानं\n  स्थास्नापाव्यधिहनियुध्यर्थम् giving six words with क where घञ्\n  would be looked for: प्रस्थः, प्रस्नः, प्रपा, आविधः, विघ्नः,\n  आयुधम्. Recorded rather than codified — the vārttika supplies\n  finished words, not a rule for making them.',
    "3.3.59": 'SETTLED — उपसर्गेऽदः. The second rule of the pāda to want A\n  PREVERB without saying which, after 3.3.22. उपसर्ग इति किम्?\n  घासः.',
    "3.3.60": "SETTLED — नौ णश्च, and the rule gives TWO affixes: ण by its own\n  word and अप् by the च — चकारादप् च, so न्यादः and निघसः both\n  stand. The first row of this table to need the `also` field,\n  which `Added` has carried since 3.2.44's चकारात् खच्च.",
    "3.3.61": 'SETTLED — व्यधजपोरनुपसर्गे, घञोऽपवादः. अनुपसर्ग इति किम्?\n  आव्याधः, उपजापः.',
    "3.3.62": 'SETTLED — स्वनहसोर्वा: स्वनः and स्वानः, हसः and हासः. And the\n  वा runs down from here to 3.3.65, until 3.3.66 stops it by\n  naming its opposite.',
    "3.3.63": 'SETTLED — यमः समुपनिविषु च. The rule ADDS four preverbs to a\n  condition of NO preverb running down from 3.3.61, and both\n  grounds stand together: संयमः, उपयमः, नियमः, वियमः, and\n  अनुपसर्गात् खल्वपि — यमः, यामः.',
    "3.3.64": 'SETTLED — नौ गदनदपठस्वनः, घञोऽपवादः. Four roots, one\n  preverb, both forms of each.',
    "3.3.65": 'SETTLED — क्वणो वीणायां च, घञोऽपवादः.\n\nSETTLED — सोपसर्गार्थं वीणाया ग्रहणम्: the lute is named so that\n  the rule reaches a PREVERBED root, नौ and अनुपसर्गे being all\n  it would otherwise have had. A condition stated for the sake of\n  widening rather than narrowing — the reverse of what a sense\n  usually does in this pāda. एतेष्विति किम्? अतिक्वाणो वर्तते.',
    "3.3.66": 'SETTLED — नित्यं पणः परिमाणे. संव्यवहाराय मूलकादीनां यः परिमितो\n  मुष्टिर्बध्यते, तस्येदमभिधानम् — the measured bundle tied for\n  sale.\n\nSETTLED — AND नित्यम् IS THERE TO STOP AN अनुवृत्ति.\n  नित्यग्रहणं विकल्पनिवृत्त्यर्थम्: the option running down from\n  3.3.62 had reached this far, and the rule cancels it by naming\n  its opposite. A third way a rule undoes something already\n  running — 3.3.44 repeated a word to cancel a principle, 3.3.75\n  repeats one to cancel a sibling heading, and this names the\n  contrary of a running word. परिमाण इति किम्? पाणः.',
    "3.3.67": 'SETTLED — मदोऽनुपसर्गे, घञोऽपवादः. अनुपसर्ग इति किम्?\n  उन्मादः, प्रमादः.',
    "3.3.68": "SETTLED — प्रमदसंमदौ हर्षे, and BOTH WORDS ARE निपातन.\n  कन्यानां प्रमदः, कोकिलानां संमदः. हर्ष इति किम्? प्रमादः,\n  संमादः.\n\nSETTLED — प्रसंभ्यामिति नोक्तम्, निपातनं रूढ्यर्थम्: the rule\n  does NOT say 'after प्र and सम्', and the vṛtti says why — the\n  fixing is for the established usage, these two words and not\n  whatever else those preverbs would give. A निपातन justified by\n  what it does NOT generalise to.",
    "3.3.69": "SETTLED — समुदोरजः पशुषु, घञोऽपवादः. पशुष्विति किम्? समाजो\n  ब्राह्मणानाम्, उदाजः क्षत्रियाणाम् — of men the long form, of\n  beasts the short.\n\nSETTLED — and the vṛtti divides the root's two senses between the\n  two preverbs though the rule does not: अज गतिक्षेपणयोः, स\n  संपूर्वः समुदाये वर्तते, उत्पूर्वश्च प्रेरणे. With सम् it is\n  gathering, with उद् driving. Recorded rather than codified,\n  since the rule licenses both either way and the division is the\n  commentary's reading of usage.",
    "3.3.70": "SETTLED — अक्षेषु ग्लहः, a निपातन. अक्षेष्विति किम्? ग्रहः\n  पादस्य.\n\nSETTLED — AND WHAT IS FIXED IS ONE SOUND. ग्रहेरप् सिद्ध एव,\n  लत्वार्थं निपातनम् — the affix would have come anyway by\n  3.3.58; the whole निपातन is for the र becoming ल. A fixed form\n  stated for a single letter of itself, which is why the entry\n  carries its own affix rather than the entry point supplying\n  one — the mistake 3.2's निपातन table made and had corrected.\n\nSCOPE — अन्ये ग्लहिं प्रकृत्यन्तरमाहुः, ते घञं प्रत्युदाहरन्ति,\n  ग्लाहः. A second opinion taking ग्लह् for a root in its own\n  right, recorded and not chosen between.",
    "3.3.71": 'SETTLED — प्रजने सर्तेः, घञोऽपवादः. प्रजनं प्रथमं गर्भग्रहणम्,\n  and the vṛtti spells the situation out rather than glossing the\n  word: स्त्रीगवीषु पुंगवानां गर्भाधानाय प्रथममुपसरणमुच्यते.',
    "3.3.72": "SETTLED — ह्वः संप्रसारणं च न्यभ्युपविषु, घञोऽपवादः. एतेष्विति\n  किम्? प्रह्वायः.\n\nSETTLED — THE RULE VOCALISES THE ROOT AS WELL AS ADDING TO IT:\n  ह्वे gives हु, so निहवः and not *निह्वायः. With 3.3.41's क and\n  3.3.76's वध, the third kind of rule in this pāda that changes\n  the root — and this one changes it by a general operation\n  rather than by naming a substitute.",
    "3.3.73": 'SETTLED — आङि युद्धे: आहूयन्तेऽस्मिन्नित्याहवः, a battle being\n  the place into which men are CALLED. युद्ध इति किम्? आह्वायः.',
    "3.3.74": 'SETTLED — निपानमाहावः, a निपातन, and THREE things are fixed in\n  it at once: संप्रसारणम्, अप् and वृद्धि. आहावः पशूनाम्.\n  निपिबन्त्यस्मिन्निति निपानमुदकाधार उच्यते, and the vṛtti ties\n  the name to the root: कूपोपसरेषु य उदकाधारस्तत्र हि पानाय पशव\n  आहूयन्ते — cattle are called to it. निपानमिति किम्? आह्वायः.',
    "3.3.75": "SETTLED — भावेऽनुपसर्गस्य: हवः, with the Ṛgveda quoted for it —\n  हवे हवे सुहवं शूरमिन्द्रम् (ऋ० ६.४७.११). अनुपसर्गस्येति किम्?\n  आह्वायः.\n\nSETTLED — AND भाव IS SAID HERE TO SHUT OUT ITS SIBLING HEADING.\n  भावग्रहणम् अकर्तरि च कारके संज्ञायाम् इत्यस्य निरासार्थम् —\n  3.3.18's भावे and 3.3.19's अकर्तरि कारके have run side by side\n  since they were stated, and naming ONE cancels the other. The\n  second time a running word is repeated in order to take\n  something away, after 3.3.44 did it to 3.1.94.",
    "3.3.76": 'SETTLED — हनश्च वधः: वधश्चोराणाम्. The root is REPLACED,\n  तत्संनियोगेन च वधादेशः, and the substitute is अन्तोदात्त so\n  that तत्रोदात्तनिवृत्तिस्वरेण the affix comes out उदात्त. भाव\n  इत्येव — घातः; अनुपसर्गस्येत्येव — प्रघातः, विघातः.\n\nSETTLED — AND THE च IS READ AGAINST ITS OWN POSITION IN THE RULE.\n  चकारो भिन्नक्रमत्वाद् नादेशेन संबध्यते, किं तर्हि? प्रकृतेन\n  प्रत्ययेन — standing where it does, the च would join the\n  SUBSTITUTE; it is taken instead with the affix running down.\n  अप् च, यश्चापरः प्राप्नोति, तेन घञपि भवति, घातो वर्तते. So घञ्\n  stands beside after all. The word ORDER of a sūtra overruled by\n  what makes sense of it — 3.2.29 and 3.2.30 read order as\n  evidence; this rule sets it aside.',
    "3.3.77": 'SETTLED — मूर्तौ घनः: अभ्रघनः, दधिघनः. मूर्तिः काठिन्यम्.\n\nSETTLED — AND A FIGURE OF SPEECH IS ADMITTED TO SAVE A FORM.\n  कथं घनं दधीति? — how can the curd BE the hardening? —\n  धर्मशब्देन धर्मी भण्यते, a word for the quality names the thing\n  that has it. The grammar reaching outside itself for a\n  rhetorical principle, as 3.3.42 reached outside for a\n  definition.',
    "3.3.78": 'SETTLED — अन्तर्घनो देशे: संज्ञीभूतो वाहीकेषु देशविशेष उच्यते.\n  देश इति किम्? अन्तर्घातोऽन्यः.\n\nSETTLED — AND A VARIANT READING IS RECORDED WITHOUT BEING CHOSEN.\n  अन्ये णकारं पठन्ति — अन्तर्घणो देश इति, तदपि ग्राह्यमेव: others\n  read ण, and that too is acceptable. Twenty-three sūtras after\n  3.3.55, where the commentary DID choose between two readings.\n  Both moves are available to it, and which one it makes is a\n  fact about the case and not about the commentary.',
    "3.3.79": 'SETTLED — अगारैकदेशे प्रघणः प्रघाणश्च, TWO forms fixed by one\n  rule and differing in a vowel, both standing. द्वारप्रकोष्ठो\n  बाह्य उच्यते, the outer porch. अगारैकदेश इति किम्?\n  प्रघातोऽन्यः.',
    "3.3.80": 'SETTLED — उद्घनोऽत्याधाने, a निपातन. यस्मिन् काष्ठे स्थापयित्वा\n  अन्यानि काष्ठानि तक्ष्यन्ते तदभिधीयते — the block other wood is\n  laid on to be cut. उद्घातोऽन्यः.',
    "3.3.81": 'SETTLED — अपघनोऽङ्गम्, a निपातन.\n\nSETTLED — and the vṛtti NARROWS what अङ्ग means here by putting\n  the question to itself: अवयवः, एकदेशो न सर्वः; किं तर्हि?\n  पाणिः पादश्चाभिधीयते — a limb, not the body; a hand or a foot.\n  A gloss that corrects the obvious reading of its own word.\n  अपघातोऽन्यः.',
    "3.3.82": "SETTLED — अयस्विद्रुहनः, करणे कारके, घनादेशः. And करण is a\n  NARROWING of a condition already running: 3.3.19's अकर्तरि\n  कारके asks only for something other than the agent, and this\n  says which.\n\nSCOPE — द्रुघण इति केचिदुदाहरन्ति, कथं णत्वम्? अरीहणादिषु\n  पाठात्, 8.4.3 पूर्वपदात् संज्ञायामगः इति वा. A variant with ण,\n  and the vṛtti offers TWO grounds for it without choosing —\n  the same declining as 3.3.78's. Neither rule is codified.",
    "3.3.83": 'SETTLED — स्तम्बे क च: स्तम्बघ्नः by the क, स्तम्बघनः by the च\n  bringing अप् down. And the feminines are wanted too: स्त्रियां\n  स्तम्बघ्ना स्तम्बघनेतीष्यते. करण इत्येव — स्तम्बघातः.',
    "3.3.84": 'SETTLED — परौ घः: परिहन्यतेऽनेनेति परिघः, a door-bar; पलिघः.\n  The substitute is घ where the two rules before had घन, and\n  nothing says why beyond that each states its own.',
    "3.3.85": "SETTLED — उपघ्नमाश्रये, a निपातन: पर्वतोपघ्नः, ग्रामोपघ्नः.\n  अप् AND the loss of the penultimate are fixed together —\n  उपधालोपश्च निपात्यते.\n\nSETTLED — आश्रयशब्दः सामीप्यं प्रत्यासत्तिं लक्षयति: the word\n  'shelter' MARKS OUT nearness rather than being the condition,\n  as 3.3.40's hand and 3.3.52's merchants did. Three times now\n  in this pāda a stated word points at the real condition.\n  आश्रय इति किम्? पर्वतोपघात एवान्यः.",
    "3.3.86": 'SETTLED — संघोद्घौ गणप्रशंसयोः, टिलोपो घत्वं च निपात्यते, and\n  यथासंख्यम् binds सम् to the GROUP and उद् to the PRAISE:\n  संघः पशूनाम्, उद्घो मनुष्याणाम्. गणप्रशंसयोरिति किम्? संघातः.',
    "3.3.87": 'SETTLED — निघो निमितम्, a निपातन: निघा वृक्षाः, निघाः शालयः.\n  समन्ताद् मितं निमितम्, समारोहपरिणाहम् — measured all round,\n  in height and girth. निमितमिति किम्? निघातः.',
    "3.3.88": "SETTLED — ड्वितः क्त्रिः: पक्त्रिमम्, उप्त्रिमम्, कृत्रिमम्.\n  THE FIRST RULE OF THE RUN TO REACH BY A ROOT'S उपदेश MARK,\n  after reaching by name, by shape and by sense.\n\nSETTLED — AND THE AFFIX IS NEVER SEEN ALONE. क्त्रेर्मम् नित्यम्\n  इति वचनात् केवलो न प्रयुज्यते — 4.4.20 always adds मम् after\n  it, so no word ends in क्त्रि and every form the vṛtti gives is\n  क्त्रिम. A rule whose output cannot be observed on its own,\n  which is why the codification reports the affix and not a form.\n\nDEBT — 4.4.20 is not codified, so that this affix never stands\n  alone is recorded and cannot be checked.",
    "3.3.89": 'SETTLED — ट्वितोऽथुच्: वेपथुः, श्वयथुः, क्षवथुः. The pair to\n  3.3.88 — two adjacent rules dividing roots by which of two\n  उपदेश marks they carry, and the marks differ by one letter.',
    "3.3.90": 'SETTLED — यजयाचयतविच्छप्रच्छरक्षो नङ्: यज्ञः, याच्ञा, यत्नः,\n  विश्नः, प्रश्नः, रक्ष्णः. ङकारो गुणप्रतिषेधार्थः.\n\nSETTLED — AND A ज्ञापक DRAWN FROM A RULE THIS PROJECT HAS\n  CODIFIED. प्रच्छेरसंप्रसारणं ज्ञापकात् प्रश्ने चासन्नकाले इति —\n  प्रच्छ् does not vocalise here, and the EVIDENCE is 3.2.117,\n  which writes प्रश्ने and could not have if it did.\n  Recorded as a citation and not declared as reuse: 3.2.117\n  answers which लकार comes after a question about lately, which\n  is not the question asked here. What is borrowed is its\n  WORDING, not its answer — and the reuse guard is right to want\n  a call before it believes a declaration.',
    "3.3.91": "SETTLED — स्वपो नन्: स्वप्नः. नकारः स्वरार्थः — the third mark\n  in this pāda put in a rule for the ACCENT alone, after 3.3.57's\n  प and 3.3.58's निश्चि. The sūtrapāṭha on disk is unaccented, so\n  all three are recorded and none can be checked.",
    "3.3.92": "SETTLED — उपसर्गे घोः किः: प्रदिः, प्रधिः, अन्तर्धिः.\n  कित्करणमातो लोपार्थम्.\n\nSETTLED — THE RULE NAMES ITS ROOTS BY A संज्ञा, AND THE\n  RESOLVER ASKS FOR IT. घु is conferred by 1.1.20 दाधा घ्वदाप्,\n  which is codified as `is_ghu`, so the row lists no roots — it\n  calls. The same treatment 3.3.14 gave 3.2.127's सत्, and the\n  second real cross-adhyāya call in this pāda.\n  A third rule of the run to want A PREVERB without saying which,\n  after 3.3.22 and 3.3.59.",
    "3.3.93": 'SETTLED — कर्मण्यधिकरणे च: जलं धीयतेऽस्मिन्निति जलधिः, शरधिः.\n  घोरित्येव, so 1.1.20 is asked here as well.\n\nSETTLED — TWO WORDS IN A THREE-WORD SŪTRA, EACH REACHING\n  OUTSIDE IT. अधिकरणग्रहणमर्थान्तरनिरासार्थम् — naming the locus\n  shuts out the other senses that were running; चकारः\n  प्रत्ययानुकर्षणार्थः — the च drags the affix down from the rule\n  before. One cancels an अनुवृत्ति and one continues another.',
    "3.3.94": "SETTLED — स्त्रियां क्तिन्, घञजपामपवादः: it defeats three affixes\n  of this run at once.\n\nSCOPE — SIX VĀRTTIKAS, more than any rule of the pāda, and one of\n  them keeps its own list OPEN: आबादयः प्रयोगतोऽनुसर्तव्याः, the\n  members are to be followed FROM USAGE. The others give करणे\n  forms (श्रुतिः, इष्टिः, स्तुतिः), नि for four roots (ग्लानिः,\n  म्लानिः, ज्यानिः, हानिः), क्तिन् read as a निष्ठा after ॠ and\n  लू (कीर्णिः, लूनिः), and संपदादिभ्यः क्विप् — with क्तिन्नपीष्यते\n  besides, so संपत् and संपत्तिः both stand.\n\nSETTLED — and the गणपाठ on disk keys संपदादि to 3.3.108, where\n  the Kāśikā gives the vārttika here. Recorded as a difference\n  between the corpus's keying and this commentary's placing, not\n  resolved: both are witnesses and neither is obviously wrong.",
    "3.3.95": "SETTLED — स्थागापापचो भावे. अङोऽपवादस्य बाधकः — it defeats a rule\n  that was ITSELF an अपवाद, so the displacing runs two deep.\n  भावग्रहणमर्थान्तरनिरासार्थम्.\n\nSETTLED — AND TWO FORMS IT SHOULD HAVE DESTROYED SURVIVE.\n  कथमवस्था संस्थेति? व्यवस्थायामसंज्ञायाम् इति ज्ञापकाद्\n  नात्यन्ताय बाधा भवति — an अपवाद does not displace ABSOLUTELY,\n  and the evidence is 1.1.34, three adhyāyas back, which\n  presupposes the very words. 1.1.34 IS codified, so this is a\n  ज्ञापक drawn from a rule the project holds — the second in this\n  pāda after 3.3.90's, and like that one a citation of WORDING\n  rather than a call.",
    "3.3.96": "SETTLED — मन्त्रे वृषेषपचमनविदभूवीरा उदात्तः, with eight forms\n  and each one's passage: वृष्टिः (ऋ० १.३.८.८), इष्टिः (ऋ० ४.४.७),\n  पक्तिः (ऋ० १.२४.५), मतिः (ऋ० १.१४१.१), वित्तिः and भूतिः (मा०सं०\n  १८.१४), वीतिः (शौ०सं० २०.६९.३), रातिः (ऋ० १.३४.१).\n\nSETTLED — AND THE WHOLE RULE IS FOR THE ACCENT. सर्वत्र\n  सर्वधातुभ्यः सामान्येन विहित एव क्तिन्, उदात्तार्थं वचनम् —\n  3.3.94 gives the affix to every root already, and this exists to\n  make it उदात्त in a mantra; मन्त्रादन्यत्रादिरुदात्तः elsewhere.\n  The fourth accent-only statement of the pāda and the first that\n  is a whole SŪTRA rather than a letter — after 3.3.57's प,\n  3.3.58's निश्चि and 3.3.91's न.\n\nSCAR — THE RULE'S CASES DO NOT CONSTRUE AS WRITTEN.\n  प्रकृतिप्रत्यययोर्विभक्तिविपरिणामेन संबन्धः, and asked why —\n  कस्मादेवं कृतम्? — the answer is वैचित्र्यार्थम्, for variety.\n  A grammarian saying outright that the wording is simply not\n  uniform, which is not an argument and is honest.\n\nSETTLED — and it points FORWARD: इषेस्तु इच्छा इति निपातनं\n  वक्ष्यति, ततः क्तिन्नपि विधीयते. 3.3.101 is that निपातन.",
    "3.3.97": "SETTLED — ऊतियूतिजूतिसातिहेतिकीर्तयश्च, six words fixed and EACH\n  FOR A DIFFERENT REASON, which is why they are entries and not a\n  row: ऊतिः is स्वरार्थं वचनम् after 6.4.20's ऊठ्; यूतिः and\n  जूतिः lengthen; सातिः either keeps इत्व off स्यति or is\n  स्वरार्थ from सनोति after 6.4.42; हेतिः is from हन् or हिनोति,\n  the vṛtti offering both; कीर्तिः from कीर्तयति. Six words, six\n  grounds, one rule.\n\nDEBT — 6.4.20 and 6.4.42 are not codified.",
    "3.3.98": "SETTLED — व्रजयजोर्भावे क्यप्: व्रज्या, इज्या. क्तिनोऽपवादः, and\n  उदात्त runs down from 3.3.96.\n  पित्करणमुत्तरत्र तुगर्थम् — the प is spent for a तुक् in a\n  LATER rule, as 3.3.43's च and 3.3.56's were spent forward.",
    "3.3.99": "SETTLED — संज्ञायां समजनिषदनिपतमनविदषुञ्शीङ्भृञिणः: समज्या,\n  निषद्या, निपत्या, मन्या, विद्या, सुत्या, शय्या, भृत्या, इत्या.\n\nSETTLED — AND THE VṚTTI DENIES THAT भाव IS A HEADING HERE. भाव\n  इति न स्वर्यते, पूर्व एवात्रार्थाधिकारः. Asked about the line\n  स्त्रियां भावाधिकारोऽस्ति तेन भार्या प्रसिध्यति, it answers\n  भावाधिकारो भावव्यापारो वाच्यत्वेन विवक्षितः, न तु शास्त्रीयोऽ\n  धिकारः — 'the heading of भाव' there means the SENSE being\n  expressed and not a heading of the grammar. One phrase read two\n  ways, and the commentary saying which reading is technical.",
    "3.3.100": 'SETTLED — कृञः श च: क्रिया by the श, कृत्या by the च.\n\nSETTLED — AND A योगविभाग IS CALLED FOR TO GET A THIRD FORM.\n  योगविभागोऽत्र कर्तव्यः, क्तिन्नपि यथा स्यात् — split the rule\n  and क्तिन् comes as well, giving कृतिः. 3.2.4 needed a\n  योगविभाग for a SENSE; this needs one for an affix the rule as\n  written shuts out.',
    "3.3.101": 'SETTLED — इच्छा, a निपातन fixing BOTH the affix and the absence\n  of यक्: इषेर्धातोः शः प्रत्ययो यगभावश्च निपात्यते. 3.3.96\n  pointed forward to it — इषेस्तु इच्छा इति निपातनं वक्ष्यति —\n  and the debt is paid five sūtras later.\n\nSCOPE — परिचर्यापरिसर्यामृगयाटाट्यानामुपसंख्यानम्, and\n  जागर्तेरकारो वा giving जागरा beside जागर्या.',
    "3.3.102": 'SETTLED — अ प्रत्ययात्, क्तिनोऽपवादः. The stem is ALREADY MADE\n  with an affix, so the rule reaches चिकीर्ष and पुत्रीय rather\n  than a bare root. 3.2.166 and 3.2.168 wanted particular such\n  stems — यङन्त, सन्नन्त — and this wants any at all, which is\n  the widest form that condition has taken.',
    "3.3.103": "SETTLED — गुरोश्च हलः, क्तिनोऽपवादः. TWO conditions and each\n  tested separately: गुरोरिति किम्? भक्तिः; हल इति किम्? नीतिः.\n  One about the vowel's weight and one about the final sound, and\n  neither follows from the other — the third such pair in the\n  pāda after 3.3.33 and 3.3.40.",
    "3.3.104": "SETTLED — षिद्भिदादिभ्योऽङ्. गणपरिपठितेषु भिदादिषु निष्कृष्य\n  प्रकृतयो गृह्यन्ते, and the members are READ FROM THE गणपाठ ON\n  DISK rather than typed out of the vṛtti.\n\nSCAR — WHICH IS THE REMEDY FOR A MISTAKE MADE TWICE. 3.2.5 and\n  3.2.15 recorded that the corpus held gaṇas the code did not\n  read; the lesson was applied in that pāda and NOT carried into\n  this one, so 3.3.3's गम्यादि was typed out by hand and came to\n  ten members where the corpus has nine — आगामी for आगमी, and an\n  आयायी the list does not carry. Both now read from the corpus.\n  The गणपाठ keys exactly three gaṇas to this pāda and asking it\n  is a thirty-second check.\n\nSCOPE — five गणसूत्र fix a sense for one member each, four of\n  them BY CONTRAST with the क्तिन् form: भिदा विदारणे,\n  भित्तिरन्या; छिदा द्वैधीकरणे, छित्तिरन्या; आरा शस्त्र्याम्,\n  आर्तिरन्या; धारा प्रपाते, धृतिरन्या. And गुहा गिर्योषध्योः,\n  क्रपेः संप्रसारणं च giving कृपा. So the gaṇa is not a flat\n  list.",
    "3.3.105": 'SETTLED — चिन्तिपूजिकथिकुम्बिचर्चश्च: चिन्ता, पूजा, कथा, कुम्बा,\n  चर्चा; and चकाराद् युजपि भवति, चिन्तना. All five are चुरादि, so\n  युच् would have come by 3.3.107 — युचि प्राप्ते — and this gives\n  अङ् instead while the च lets युच् stand beside anyway.',
    "3.3.106": 'SETTLED — आतश्चोपसर्गे, क्तिनोऽपवादः. The fourth rule of the run\n  to want A PREVERB without saying which, after 3.3.22, 3.3.59\n  and 3.3.92.\n\nSETTLED — AND TWO WORDS THAT ARE NOT PREVERBS COUNT AS ONE.\n  श्रदन्तरोरुपसर्गवद् वृत्तिः: श्रद् and अन्तर् BEHAVE LIKE\n  preverbs here, giving श्रद्धा and अन्तर्धा. 1.4.59 उपसर्गाः\n  क्रियायोगे is codified and would refuse both, so this is an\n  extension the vṛtti makes and the rule does not. Recorded rather\n  than folded into the condition, since folding it in would make\n  the code disagree with 1.4.59 silently.',
    "3.3.107": "SETTLED — ण्यासश्रन्थो युच्, अकारस्यापवादः. कथमास्या? ऋहलोर्ण्यत्\n  भविष्यति — the awkward form is sent to 3.1.124, WHICH IS\n  CODIFIED.\n\nSETTLED — A FIFTH वासरूप SUSPENSION, AND THE FIRST THAT IS\n  EXPLICITLY BOUNDED. वासरूपप्रतिषेधश्च\n  स्त्रीप्रकरणविषयस्यैवोत्सर्गापवादस्य — the suspension of 3.1.94\n  holds only for general-and-special pairs WITHIN the feminine\n  section. The four before it (3.2.146, 3.2.177, 3.3.10, 3.3.44)\n  each suspended it over ground the commentary marked out by\n  argument; this one states its own limit.\n\nSETTLED — TWO ROOTS SPELT ALIKE, SETTLED FROM REDUNDANCY AND NOT\n  FROM SENSE. श्रन्थिः क्र्यादिर्गृह्यते, न चुरादिः,\n  ण्यन्तत्वेनैव सिद्धत्वात् — the चुरादि one is not meant BECAUSE\n  it would already be covered by the ण्यन्त half of this very\n  rule. The vārttika घट्टिवन्दिविदिभ्य उपसंख्यानम् makes the same\n  choice for घट्ट on the same ground. This is a FOURTH ground for settling\n  which of two roots spelt alike is meant, and the four are\n  genuinely different: साहचर्यात् from the company a word keeps\n  (3.2.59, 3.2.61); स्वभावात् from how the world is (3.2.161,\n  3.2.162); अनभिधानात् from there being no such word (3.3.30);\n  and this, from the reading that would make the rule say\n  nothing new.\n\nSCAR — THIS NOTE FIRST CITED साहचर्यात् AT 3.2.162, WHICH SAYS\n  स्वभावात्. Two different grounds merged into one wrong\n  citation, caught by a test that named the place. The rule\n  `test_astadhyayi_attribution.py` holds is exactly this: a\n  quotation is either checkable where the note says, or the note\n  says it is not checkable.\n\nSCOPE — इषेरनिच्छार्थस्य युज्वक्तव्यः, अध्येषणा, अन्वेषणा; and\n  परेर्वा, पर्येषणा beside परीष्टिः.",
    "3.3.108": "SETTLED — रोगाख्यायां ण्वुल् बहुलम्, क्तिन्नादीनामपवादः.\n  आख्याग्रहणं रोगस्य चेत् प्रत्ययान्तेन संज्ञा भवति, and\n  बहुलग्रहणं व्यभिचारार्थम् — the बहुलम् is there so the rule may\n  FAIL: न च भवति शिरोऽर्तिः.\n\nSETTLED — AND THE GRAMMAR'S VOCABULARY FOR TALKING ABOUT ITSELF\n  IS SUPPLIED BY VĀRTTIKAS ON A RULE ABOUT DISEASES. Seven of\n  them, and most are about NAMING grammatical things rather than\n  making words: इक्श्तिपौ धातुनिर्देशे — भिदिः, छिदिः, पचतिः,\n  पठतिः, how to refer to a root; वर्णात् कारः — अकारः, इकारः,\n  how to refer to a letter; रादिफः — रेफः, the name of र. Also\n  धात्वर्थनिर्देशे ण्वुल्, मत्वर्थाच्छः, इणजादिभ्यः and इक्\n  कृष्यादिभ्यः.\n\nSETTLED — the गणपाठ keys संपदादि to THIS sūtra, where the Kāśikā\n  gives that vārttika under 3.3.94. Recorded at both.",
    "3.3.109": 'SETTLED — संज्ञायाम्: उद्दालकपुष्पभञ्जिका, वारणपुष्पप्रचायिका,\n  अभ्यूषखादिका, आचोषखादिका, शालभञ्जिका, तालभञ्जिका — names of\n  games and festivals, each a whole compound. The समुदायोपाधि\n  again, met at 3.2.80, 3.2.92, 3.2.99, 3.2.185 and 3.3.34.',
    "3.3.110": "SETTLED — विभाषाख्यानपरिप्रश्नयोरिञ् च, and the option is wide:\n  चकाराद् ण्वुलपि, and विभाषाग्रहणात् परोऽपि यः प्राप्नोति\n  सोऽपि भवति — even a LATER affix stands, so five forms answer\n  one question: कां कारिम्, कां कारिकाम्, कां क्रियाम्, कां\n  कृत्याम्, कां कृतिम्.\n\nSETTLED — AND THE RULE'S WORD ORDER IS EXPLAINED AWAY. पूर्वं\n  परिप्रश्नः, पश्चादाख्यानम् — the asking comes first and the\n  telling after, though the rule names them the other way; and\n  सूत्रेऽल्पाच्तरस्य पूर्वनिपातः, the shorter word stands first\n  by 2.2.34. 3.2.29 and 3.2.30 read exactly that fact as EVIDENCE\n  of a rule's intent; here it is an artefact to be discounted, and\n  3.3.76 set word order aside on other grounds again. Three\n  positions on one question, all in the commentary's hands.\n\n  आख्यानपरिप्रश्नयोरिति किम्? कृतिः, हृतिः.",
    "3.3.111": 'SETTLED — पर्यायार्हर्णोत्पत्तिषु ण्वुच्, क्तिन्नादीनामपवादः.\n  Four senses, each glossed: पर्यायः परिपाटी क्रमः, अर्हणमर्हः\n  तद्योग्यता, ऋणं तत् यत् परस्य धार्यते, उत्पत्तिर्जन्म.\n\nSETTLED — ण्वुलि प्रकृते प्रत्ययान्तरकरणं स्वरार्थम्: ण्वुल् was\n  already running and a DIFFERENT affix is given for the accent\n  alone. The fifth accent-only statement of the pāda, and the same\n  device 3.2.12 and 3.2.16 used to reach a feminine.',
    "3.3.112": "SETTLED — आक्रोशे नञ्यनिः. विभाषेति निवृत्तम्, the option having\n  run out. BOTH conditions tested: आक्रोश इति किम्? अकृतिस्तस्य\n  कटस्य; नञीति किम्? मृतिस्ते वृषल भूयात् — a curse without the\n  negative particle, which the rule does not reach.\n\nSETTLED — आक्रोश was 3.3.45's condition too, for अप् after ग्रह्.\n  One sense reached for twice in a pāda for two different affixes,\n  as लिप्सा was at 3.3.6 and 3.3.46.\n\nSCAR — the two witnesses differ: GRETIL reads अतिः, Vidyut अनिः.\n  The vṛtti settles it — धातोरनिः प्रत्ययो भवति, and the form is\n  अकरणिः. So अनिः stands. The second reading this commentary has\n  decided, after 3.3.55.",
    "3.3.113": "SETTLED — कृत्यल्युटो बहुलम्, AND THE DEBT SIX RULES HAVE BEEN\n  CARRYING IS PAID. 3.2.53, 3.2.153, 3.3.24, 3.3.26, 3.3.43 and\n  3.3.44 each sent a form here that their own run would not give,\n  and 3.3.56 cited it for a different reason again.\n  कृत्यसंज्ञकाः प्रत्यया ल्युट् च बहुलमर्थेषु भवन्ति, यत्र\n  विहितास्ततोऽन्यत्रापि भवन्ति — the affixes OCCUR BEYOND WHERE\n  THEY WERE PRESCRIBED, which is exactly what a commentary needs\n  when usage has a word the rules do not make.\n\nSETTLED — AND IT CLOSES THE TWO HEADINGS, EXACTLY WHERE 3.3.56\n  SAID IT WOULD. भावे अकर्तरि च कारक इति निवृत्तम्: the\n  conditions running since 3.3.18 and 3.3.19 stop here, and\n  3.3.56 had stated the extent fifty-seven sūtras early by NAMING\n  this rule — यावत् कृत्यल्युटो बहुलम् इति. A claim made early and\n  confirmed by the rule it named, as 3.2.134's आ क्वेः was\n  confirmed by 3.2.177.\n\nSETTLED — THREE KINDS OF GOING-BEYOND, KEPT APART BY THE VṚTTI.\n  भावकर्मणोः कृत्या विहिताः कारकान्तरेऽपि भवन्ति — स्नानीयं\n  चूर्णम्, दानीयो ब्राह्मणः. करणाधिकरणयोर्भावे च ल्युट्,\n  अन्यत्रापि भवति — अपसेचनम्, अवस्रावणम्, राजभोजनाः शालयः,\n  राजाच्छादनानि वासांसि, प्रस्कन्दनम्, प्रपतनम्. And\n  बहुलग्रहणादन्येऽपि कृतो यथाप्राप्तमभिधेयं व्यभिचरन्ति —\n  पादाभ्यां ह्रियते पादहारकः, गले चोप्यते गलेचोपकः.\n\nSCAR — बहुलम् IS NOT RESOLVED, AND CANNOT BE. This is the same\n  refusal 3.3.1 made about the उणादि affixes at the other end of\n  the pāda, and the two rules bracket it: one licenses a text the\n  grammar does not contain, the other licenses forms the grammar\n  does not derive. What the codification can say is WHICH KIND of\n  going-beyond is meant, and it says that and no more.",
    "3.3.114": 'SETTLED — नपुंसके भावे क्तः. THE NEUTER RUN BEGINS, and with it\n  the third gender to organise this end of the pāda: 3.3.94 to\n  3.3.112 wanted स्त्रियाम्, 3.3.118 wants the masculine.\n\nSETTLED — AND STATING भावे HERE IS NOT THE OLD HEADING. That one\n  ran from 3.3.18 and stopped at 3.3.113, which 3.3.56 had said\n  it would. This rule says भावे in its own words, so the sense is\n  back and the अधिकार is not — a distinction easy to lose, and\n  one that made a test of ours wrong for a few minutes.\n\nSETTLED — the gender OUTRANKS a named root in the resolver, which\n  is what the text says: these runs displace the affixes given\n  earlier, 3.3.94 being घञजपामपवादः in so many words. Without it\n  हसितम् came back as हसः, by 3.3.62, which happens to name हस्.',
    "3.3.115": "SETTLED — ल्युट् च: हसनं छात्रस्य, शयनम्, आसनम्.\n\nSETTLED — योगविभाग उत्तरार्थः. The affix could have been given\n  with 3.3.114's, and the rule is split off FOR THE SAKE OF WHAT\n  COMES AFTER, so 3.3.116 and 3.3.117 have something to carry\n  down. 3.2.4 and 3.3.100 wanted a योगविभाग for what the split\n  itself buys; this one is made for its neighbours.\n\nSETTLED — it reaches the same ground as 3.3.114 and gives a\n  different affix, so `wants` names the one asked after — the\n  idiom three entry points of 3.2 needed. हसितम् and हसनम् both\n  stand.",
    "3.3.116": 'SETTLED — कर्मण्यधिकरणे च, AND THE RULE GIVES NOTHING BUT A\n  COMPOUND. पूर्वेणैव सिद्धे प्रत्यये नित्यसमासार्थं वचनम्,\n  उपपदसमासो हि नित्यः समासः — 3.3.115 supplies the affix already;\n  this exists so the two words MUST compound. A whole sūtra spent\n  on a compound, as 3.3.96 was on an accent and 3.3.123 will be\n  on a prohibition.\n\nSETTLED — FOUR CONDITIONS, FOUR COUNTER-EXAMPLES, and one of them\n  turns on a kāraka: कर्तुरिति किम्? गुरोः स्नापनं सुखम् —\n  स्नापयतेर्न गुरुः कर्ता, किं तर्हि? कर्म. Another turns on a\n  gloss: शरीरग्रहणं किम्? पुत्रस्य परिष्वञ्जनं सुखम्, सुखं मानसी\n  प्रीतिः — that pleasure is of the mind and not the body.\n\nSETTLED — AND EVERY COUNTER-EXAMPLE DIFFERS FROM ITS EXAMPLE IN\n  NOTHING BUT A SPACE. सर्वत्रासमासः प्रत्युदाह्रियते: the affix\n  still comes in each of them and only the compulsory compounding\n  is lost, so the counters are printed UNCOMPOUNDED. The\n  codification cannot show that — it reports the affix, and the\n  affix is the same either way. Recorded as the limit it is.',
    "3.3.117": "SETTLED — करणाधिकरणयोश्च: इध्मप्रव्रश्चनः, पलाशशातनः for the\n  means; गोदोहनी, सक्तुधानी for the place. The two kārakas\n  3.3.19's heading had left general, now named — and the heading\n  itself has stopped, so this rule states them.",
    "3.3.118": 'SETTLED — पुंसि संज्ञायां घः प्रायेण. The MASCULINE run, and the\n  sixth समुदायोपाधि: समुदायेन चेत् संज्ञा गम्यते, after 3.2.80,\n  3.2.92, 3.2.99, 3.2.185 and 3.3.34.\n\nSETTLED — AND THE RULE ADMITS ITS OWN LEAKS IN ITS OWN WORDING.\n  प्रायग्रहणमकार्त्स्न्यार्थम् — प्रायेण is there to say the rule\n  does NOT hold throughout. A hedge written into the sūtra, where\n  बहुलम् at 3.3.1, 3.3.108 and 3.3.113 does the same work with a\n  different word.\n\nSETTLED — घकारः छादेर्घे इति विशेषणार्थः, the घ spent so 6.4.96\n  can pick this affix out. DEBT: that rule is not codified.',
    "3.3.119": "SETTLED — गोचरसंचरवहव्रजव्यजापणनिगमाश्च, all निपातन, with\n  चकारोऽनुक्तसमुच्चयार्थः adding कषः and निकषः.\n\nSETTLED — AN EXCEPTION STATED BEFORE THE RULE IT EXCEPTS.\n  हलश्च इति घञं वक्ष्यति, तस्यायमपवादः — the rule excepted comes\n  at 3.3.121, two sūtras LATER. 3.3.20's सर्वग्रहण reached\n  forward the same way and needed a word to do it; this needs\n  none, being a निपातन.\n\nSETTLED — and one word is fixed for what does NOT happen to it:\n  निपातनाद् अजेर्व्यघञपोः इति वीभावो न भवति, so व्यज keeps its\n  अज where 2.4.56 would have replaced it. 2.4.56 IS codified.",
    "3.3.120": "SETTLED — अवे तॄस्त्रोर्घञ्, घस्यापवादः: अवतारः, अवस्तारः.\n  ञकारो वृद्ध्यर्थः स्वरार्थश्च, घकार उत्तरत्र कुत्वार्थः — one\n  mark doing two jobs and another spent forward.\n\nSETTLED — AND THE RULE LEAKS, BY THE HEDGE TWO SŪTRAS BACK.\n  कथमवतारो नद्याः, न हीयं संज्ञा? प्रायानुवृत्तेरसंज्ञायामपि\n  भवति — 3.3.118's प्रायेण runs down, so the form stands even\n  where no name is meant. A hedge written in one rule doing work\n  in another.",
    "3.3.121": "SETTLED — हलश्च, घस्यापवादः. पुंसि संज्ञायां करणाधिकरणयोश्चेति\n  सर्वमनुवर्तते — everything from 3.3.118 runs down, so the rule\n  states only the root's shape. Four words carried, one stated.",
    "3.3.122": "SETTLED — अध्यायन्यायोद्यावसंहारावायाश्च, निपातन.\n  अहलन्तार्थ आरम्भः — the rule exists for roots NOT ending in a\n  consonant, 3.3.121 having taken those. 3.3.118's घ would\n  otherwise have come and घञ् is fixed instead.",
    "3.3.123": 'SETTLED — उदङ्कोऽनुदके, a निपातन WHOSE WORK IS ENTIRELY\n  NEGATIVE. ननु च हलश्च इति सिद्ध एव घञ्? — 3.3.121 gives the\n  affix already — उदके प्रतिषेधार्थमिदं वचनम्: the statement\n  exists to keep the form OFF where water is meant. तैलोदङ्कः;\n  अनुदक इति किम्? उदकोदञ्चनः.\n\nSETTLED — and the vṛtti explains why it gives no counter-form:\n  घः कस्माद् न प्रत्युदाह्रियते? विशेषाभावात्, घञ्यपि\n  थाथादिस्वरेणान्तोदात्त एव — there would be no visible\n  difference, both coming out accented alike. A counter-example\n  omitted BECAUSE it would look identical.',
    "3.3.124": 'SETTLED — आनायोऽनहः, a निपातन for a net, and only where a net is\n  meant: जालं चेत् तद् भवति. आनायो मत्स्यानाम्, आनायो मृगाणाम्.',
    "3.3.125": 'SETTLED — खनो घ च: आखनः by the घ, आखानः by the च.\n\nSCOPE — FIVE VĀRTTIKAS, EACH GIVING ONE MORE AFFIX FOR THIS ONE\n  ROOT: डो वक्तव्यः (आखः), डरो वक्तव्यः (आखरः), इको वक्तव्यः\n  (आखनिकः), इकवको वक्तव्यः (आखनिकवकः). Seven words from one root,\n  five of them supplements. No rule of the pāda has been\n  supplemented this densely for so little.',
    "3.3.126": 'SETTLED — ईषद्दुःसुषु कृच्छ्राकृच्छ्रार्थेषु खल्.\n\nSETTLED — THE THREE COMPANIONS DIVIDE TWO SENSES BETWEEN THEM\n  WITHOUT यथासंख्यम्. कृच्छ्रं दुःखम्, तद् दुरो विशेषणम्;\n  अकृच्छ्रं सुखम्, तदितरयोर्विशेषणम्, संभवात् — HARD goes with\n  दुर् and EASY with the other two, and the ground is संभवात्,\n  what each can sensibly mean. Where 3.3.37 and 3.3.86 counted\n  off crosswise, this divides by FIT. A third way of binding two\n  lists, and the only one that needs no rule.\n\nSETTLED — two marks, neither doing grammar here: लकारः स्वरार्थः,\n  खित्करणमुत्तरत्र मुमर्थम् — one for the accent and one for an\n  augment in a later rule.',
    "3.3.127": 'SETTLED — कर्तृकर्मणोश्च भूकृञोः, यथासंख्यम् binding भू to the\n  AGENT and कृ to the OBJECT. चकारादीषदादिषु च.\n\nSCOPE — कर्तृकर्मणोश्च्व्यर्थयोरिति वक्तव्यम्: the two must be in\n  the sense of च्वि, इह मा भूत् स्वाढ्येन भूयते.',
    "3.3.128": "SETTLED — आतो युच्, खलोऽपवादः. ईषदादयोऽनुवर्तन्ते,\n  कर्तृकर्मणोरिति न स्वर्यते — the three companions carry down\n  and 3.3.127's two kārakas do NOT. Nothing in the wording shows\n  which of two adjacent conditions travels, and the vṛtti has to\n  say. The third fact of that kind in this pāda, after 3.3.45's\n  नानन्तर इनुण् and 3.3.49's सिंहावलोकित.",
    "3.3.129": 'SETTLED — छन्दसि गत्यर्थेभ्यः, खलोऽपवादः: सूपसदनोऽग्निः (तै०सं०\n  ७.५.२०.१). Vedic only, and codified one-way as छन्दसि was\n  throughout 3.2.',
    "3.3.130": "SETTLED — अन्येभ्योऽपि दृश्यते: सुदोहनाम् (निरु० ११.४३),\n  सुवेदनामकृणोर्ब्रह्मणे गाम् (ऋ० १०.११२.८).\n\nSETTLED — दृश्यते A FOURTH TIME, and it takes the usage-following\n  reading: the rule OPENS the class rather than closing it, as at\n  3.2.75 and 3.3.2. So three of the four readings are that one\n  and 3.2.178's विध्यन्तरोपसंग्रह stands alone.\n\nSCOPE — AND THE VĀRTTIKA UNDOES THE RULE'S OWN RESTRICTION.\n  भाषायां शासियुधिदृशिधृषिमृषिभ्यो युज् वक्तव्यः — दुःशासनः,\n  दुर्योधनः, दुर्दर्शनः, दुर्धर्षणः, दुर्मर्षणः: five roots given\n  the affix OUTSIDE the Veda, against a rule that holds only\n  inside it. A supplement contradicting the condition of the rule\n  it supplements, which nothing before this has done.",
    "3.3.133": "SETTLED — क्षिप्रवचने लृट्, भूतवच्चेत्यस्यायमपवादः.\n\nSETTLED — वचनग्रहणं पर्यायार्थम्: the word वचन is there so any\n  SYNONYM of 'soon' counts — क्षिप्रं शीघ्रमाशु त्वरितम्. The\n  identical device and the identical wording as 3.2.112's\n  अभिज्ञावचने, a pāda apart.\n\nSETTLED — नेति वक्तव्ये लृड्ग्रहणं लुटोऽपि विषये यथा स्यात्: the\n  rule could have been a plain प्रतिषेध and NAMES the ending\n  instead, so that it reaches लुट्'s ground too — श्वः\n  क्षिप्रमध्येष्यामहे. A rule made positive in order to reach\n  further than a refusal would.",
    "3.3.134": "SETTLED — आशंसावचने लिङ्. The companion is a word that EXPRESSES\n  the hope and not the hope itself — आशंसा येनोच्यते\n  तदाशंसावचनम् — so the condition is on the sentence and not on\n  the sense, which is the distinction 3.3.8's लोडर्थलक्षण drew.",
    "3.3.139": "SETTLED — लिङ्निमित्ते लृङ् क्रियातिपत्तौ.\n  कुतश्चिद् वैगुण्यादनभिनिर्वृत्तिः क्रियायाः क्रियातिपत्तिः —\n  the act failing of something.\n\nSETTLED — A CONDITION ABOUT ANOTHER RULE HAVING APPLIED, which\n  nothing in either pāda had asked before. लिङ्निमित्त means some\n  rule — 3.3.156 हेतुहेतुमतोर्लिङ् and the like — would have given\n  लिङ् here. Every other condition met so far has been about the\n  act, the speaker, the company or the form; this is about the\n  GRAMMAR'S OWN state.\n\nSETTLED — and the vṛtti works the example as an inference:\n  लिङ्गिलिङ्गे बुद्ध्वा तदतिपत्तिं च प्रमाणान्तरादवगम्य वक्ता\n  वाक्यं प्रयुङ्क्ते — the speaker knows the sign and the thing\n  signified, learns from elsewhere that it failed, and only then\n  says the sentence.",
    "3.3.140": "SETTLED — भूते च: the rule before gave लृङ् for a failed FUTURE\n  act and this for a failed past one.\n\nSETTLED — ITS TIME IS THE PAST AND IT IS NOT UNDER 3.2.84. That\n  heading runs 3.2.84 to 3.2.122 and this rule is in another\n  pāda; the row's `time` says what the rule is ABOUT. A test read\n  the one as the other and was right only while 3.2 held every\n  past rule.",
    "3.3.141": "SETTLED — वोताप्योः, AND THE OPTION'S EXTENT IS READ OFF A\n  PREFIX. मर्यादायामयमाङ् नाभिविधौ — the आ marks a BOUNDARY and\n  not inclusion, so 3.3.140's लृङ् is optional up to but NOT\n  including 3.3.152, which the vṛtti confirms from the other end:\n  इतः प्रभृति ... नित्यं लृङ्.\n  Two readings of one prefix, and the choice moves where the\n  option stops. The third extent in this pāda stated by naming\n  its far end rather than counting — after 3.2.134's आ क्वेः and\n  3.3.56's यावत् कृत्यल्युटो बहुलम्.\n\nSETTLED — codified as `lrn_is_optional`, a range whose far end is\n  the NAMED sūtra. It gives no affix, so it has no row.",
    "3.3.142": 'SETTLED — गर्हायां लडपिजात्वोः. गर्हा कुत्सेत्यनर्थान्तरम्.\n\nSETTLED — AND IT DEFEATS THE TENSE RULES BY STANDING LATER.\n  वर्तमाने लट् उक्तः कालसामान्ये न प्राप्नोतीति विधीयते — 3.2.123\n  gives लट् for the present and could not reach every time; then\n  कालविशेषविहितांश्चापि प्रत्ययानयं परत्वाद् अस्मिन् विषये बाधते.\n  The first rule of the pāda to win by परत्व rather than by\n  narrowness — and the resolver, which has no order to appeal to,\n  reaches it by specificity instead. Recorded, since the two\n  grounds agree here and need not always.',
    "3.3.143": 'SETTLED — विभाषा कथमि लिङ् च: लिङ् by the rule and लट् by the च.\n  विभाषाग्रहणं यथास्वं कालविषये विहितानामबाधनार्थम् — the option\n  is there so the ordinary tense endings are NOT defeated, and\n  the vṛtti lists seven forms standing together.',
    "3.3.144": 'SETTLED — किंवृत्ते लिङ्लृटौ, सर्वलकाराणामपवादः.\n  लिङ्ग्रहणं लटोऽपरिग्रहार्थम् — लिङ् is named so that लट् is NOT\n  taken in, which 3.3.143 had allowed one sūtra earlier. A word\n  spent to un-include what the rule before included.',
    "3.3.145": 'SETTLED — अनवक्ऌप्त्यमर्षयोरकिंवृत्तेऽपि. अनवक्ऌप्तिरसंभावना,\n  अमर्षोऽक्षमा — disbelief and indignation.\n\nSETTLED — AND यथासंख्यम् IS REFUSED ON THE GROUND 3.2.29 USED.\n  बह्वचः पूर्वनिपातो लक्षणव्यभिचारचिह्नम्, तेन यथासंख्यं न भवति:\n  the LONGER word standing first is the sign that the counting-off\n  does not apply, since 2.2.34 अल्पाच्तरम् would have put the\n  shorter first. The identical argument and the identical rule\n  appealed to as at 3.2.29 and 3.2.30, a pāda and a half apart.\n  3.3.110 read the same fact the OTHER way — as an artefact to be\n  discounted — so the commentary has both moves and picks.',
    "3.3.146": "SETTLED — किंकिलास्त्यर्थेषु लृट्, लिङोऽपवादः. अस्त्यर्था\n  अस्तिभवतिविद्यतयः — three verbs counted as meaning 'is'.\n\nSETTLED — A RULE'S ABSENCE AS A CONDITION. लिङ्निमित्तमिह नास्ति\n  तेन लृङ् न भवति: because no rule gives लिङ् here, 3.3.139's\n  ending cannot come either. The counterpart of 3.3.139's\n  condition, and the same fact stated negatively.",
    "3.3.147": 'SETTLED — जातुयदोर्लिङ्, लृटोऽपवादः. SCOPE:\n  जातुयदोर्लिङ्विधाने यदायद्योरुपसंख्यानम् adds यदा and यदि.',
    "3.3.148": 'SETTLED — यच्चयत्रयोः, लृटोऽपवादः. योगविभाग उत्तरार्थः — split\n  for the sake of the two rules after, as 3.3.115 was. And\n  यथासंख्यं नेष्यते here too, without the argument 3.3.145 gave.',
    "3.3.149": 'SETTLED — गर्हायां च, सर्वलकाराणामपवादः. The same two companions\n  as 3.3.148 with a different sense — which is what the योगविभाग\n  bought.',
    "3.3.150": 'SETTLED — चित्रीकरणे च. चित्रीकरणमाश्चर्यमद्भुतं विस्मयनीयम्.\n  The THIRD sense given to one pair of companions in three sūtras\n  — disbelief, blame, wonder — which is what splitting 3.3.148 off\n  was for.',
    "3.3.151": 'SETTLED — शेषे लृडयदौ, सर्वलकाराणामपवादः. शेषः is whatever is\n  not यच् or यत्र, so the rule is defined by the three before it,\n  as 3.3.13 was. And it REFUSES यदि: अयदाविति किम्? आश्चर्यं यदि\n  स भुञ्जीत. लिङ्निमित्ताभावादिह लृङ् न भवति.',
    "3.3.152": 'SETTLED — उताप्योः समर्थयोर्लिङ्, सर्वलकाराणामपवादः. समर्थयोः\n  means the two are used in ONE sense, बाढम्; समर्थयोरिति किम्?\n  उत दण्डः पतिष्यति — there they mark a question.\n\nSETTLED — AND IT IS THE FAR END OF AN OPTION STATED ELEVEN SŪTRAS\n  BACK. वोताप्योः इति विकल्पो निवृत्तः: 3.3.141 named THIS rule\n  as its boundary, and the boundary excludes it —\n  मर्यादायामयमाङ् नाभिविधौ. So इतः प्रभृति भूतेऽपि लिङ्निमित्ते\n  क्रियातिपत्तौ नित्यं लृङ्.',
    "3.3.131": 'SETTLED — वर्तमानसामीप्ये वर्तमानवद् वा. The rule names NO\n  affix: it says the affixes of one time are used for another,\n  which is a different question from which ending comes, and it\n  answers from its own entry point for that reason.\n\nSETTLED — AND THE TRANSFER CARRIES EVERYTHING. वत्करणं\n  सर्वसादृश्यार्थम्, येन विशेषणेन वर्तमाने प्रत्यया विहिताः\n  प्रकृत्युपपदादिना तथैवात्र भवन्ति — whatever conditions an\n  affix had in its own time it keeps in the borrowed one, root\n  and companion alike. पवमानः, यजमानः, अलंकरिष्णुः.\n\nSETTLED — the extent transferred is stated at BOTH ENDS by\n  naming rules: वर्तमाने लट् इत्यारभ्य यावद् उणादयो बहुलम् इति —\n  3.2.123 to 3.3.1, which is precisely the run this project has\n  just read. Both ends are codified, so the claim is checkable.\n\nSCAR — AND THE VṚTTI CONCEDES THE SECTION MAY BE UNNECESSARY.\n  यो मन्यते गच्छामीति पदं वर्तमाने काल एव वर्तते,\n  कालान्तरगतिस्तु वाक्याद् भवति, न च वाक्यगम्यः कालः\n  पदसंस्कारवेलायामुपयुज्यत इति, तादृशं वाक्यार्थप्रतिपत्तारं\n  प्रति प्रकरणमिदं नारभ्यते — for a reader who holds that the\n  WORD is present-tense and the other time comes from the\n  sentence, this whole stretch of the grammar is not undertaken.\n  A commentary saying a section answers a question one need not\n  ask. Recorded and not acted on: the rules are in the text.',
    "3.3.132": "SETTLED — आशंसायां भूतवच्च, चकाराद् वर्तमानवच्च. आशंसनमाशंसा,\n  अप्राप्तस्य प्रियार्थस्य प्राप्तुमिच्छा, तस्याश्च भविष्यत्कालो\n  विषयः — the PAST's affixes used for a hoped-for future.\n\nSETTLED — AND A GENERAL TRANSFER DOES NOT CARRY THE SPECIAL\n  CASES. सामान्यातिदेशे विशेषानतिदेशात् लङ्लिटौ न भवतः: लङ् and\n  लिट् do not come, being given for particular kinds of past. A\n  limit on the सर्वसादृश्य 3.3.131 asserted, stated one sūtra\n  later and needed at once.",
    "3.3.135": "SETTLED — नानद्यतनवत् क्रियाप्रबन्धसामीप्ययोः. What is refused\n  is 3.2.111's लङ् and 3.3.15's लुट् — one rule from each pāda,\n  and both codified.\n  क्रियाणां प्रबन्धः सातत्येनानुष्ठानम्; कालानां सामीप्यं\n  तुल्यजातीयेनाव्यवधानम्.\n\nSETTLED — द्वौ प्रतिषेधौ यथाप्राप्तस्याभ्यनुज्ञापनाय: TWO\n  prohibitions, so that what would ordinarily come is thereby\n  ALLOWED. A refusal read as a licence for everything it does not\n  refuse — the same move as 3.3.146's लिङ्निमित्तमिह नास्ति, and\n  the opposite of how 3.2.23's प्रतिषेध was read.\n\nSETTLED — a refusal here NAMES ITSELF, which 3.2.23 marked off as\n  the case where it may: refusing is the whole of what these four\n  rules do, and there is no rule that supplies instead.",
    "3.3.136": 'SETTLED — भविष्यति मर्यादावचनेऽवरस्मिन्. अक्रियाप्रबन्धार्थम्\n  असामीप्यार्थं च वचनम् — the rule exists for the ground 3.3.135\n  left over.\n\nSETTLED — THREE CONDITIONS, THREE COUNTER-EXAMPLES, and each is a\n  WHOLE SCENE REBUILT with one word changed: the same journey in\n  the past, the same journey with no limit named, the same\n  journey on the farther side. The commentary tests a condition\n  by reprinting the sentence, which no rule of 3.2 needed.\n\nSETTLED — इह सूत्रे देशकृता मर्यादा, उत्तरत्र कालकृता: the limit\n  here is of PLACE and at 3.3.137 of TIME, and तत्र न विशेषं\n  वक्ष्यति — the difference is stated in NEITHER rule and is read\n  off the examples alone. Codified as two senses because that is\n  the only place the distinction lives.',
    "3.3.137": 'SETTLED — कालविभागे चानहोरात्राणाम्.\n  पूर्वेणैव सिद्धे वचनमिदमहोरात्रनिषेधार्थम् — 3.3.136 settles it\n  already and this exists to EXCEPT days and nights. A rule\n  stated for what it takes away, as 3.3.123 was.\n  अनहोरात्राणामिति किम्? and the vṛtti gives त्रिविधमुदाहरणम्,\n  three ways a period can touch a day, closing\n  सर्वथाहोरात्रस्पर्शे प्रतिषेधः.\n\nSETTLED — योगविभाग उत्तरार्थः, split for the rule after, as\n  3.3.115 and 3.3.148 were. Three in one pāda.',
    "3.3.138": 'SETTLED — परस्मिन् विभाषा.\n\nSETTLED — AND IT INHERITS EVERYTHING BUT ONE WORD.\n  अवरस्मिन्वर्जं पूर्वमनुवर्तते — all of 3.3.137 carries down\n  EXCEPT अवरस्मिन्, which this rule replaces with its own\n  परस्मिन्. An अनुवृत्ति with a single word cut out of it, which\n  the codification cannot represent and each row therefore\n  states in full.\n\nSETTLED — अवरस्मिन् पूर्वेण प्रतिषेध उक्तः, संप्रति\n  परस्मिन्नप्राप्त एव विकल्प उच्यते: the nearer side was already\n  refused, so on the farther side an option is offered where\n  nothing had applied — a विभाषा over ground no rule reached.',
    "3.3.153": "SETTLED — कामप्रवेदनेऽकच्चिति, सर्वलकाराणामपवादः.\n  स्वाभिप्रायाविष्करणं कामप्रवेदनम् — making one's OWN wish\n  known, which is what the refused companion cuts against.\n  अकच्चितीति किम्? and the vṛtti answers with a VERSE —\n  कच्चिज्जीवति ते माता कच्चिज्जीवति ते पिता — where कच्चित् asks\n  after another's welfare. A counter-example quoted as poetry.",
    "3.3.154": "SETTLED — संभावनेऽलमिति चेत् सिद्धाप्रयोगे. संभावनं क्रियासु\n  योग्यताध्यवसानम्, शक्तिश्रद्धानम्.\n\nSETTLED — AND THE CONDITION IS THAT A WORD BE UNDERSTOOD AND NOT\n  SAID. सिद्धश्चेदलमोऽप्रयोगः; क्व चासौ सिद्धः? यत्र गम्यते\n  चार्थो न चासौ प्रयुज्यते — अलम् must be MEANT and NOT uttered.\n  सिद्धाप्रयोग इति किम्? अलं देवदत्तो हस्तिनं हनिष्यति, where it\n  is uttered and the rule fails.\n  A condition on a word's ABSENCE, which nothing in either pāda\n  had asked. 3.2's conditions were about the root, the companion,\n  the sense or the finished word; this is about what the speaker\n  left out.",
    "3.3.155": 'SETTLED — विभाषा धातौ संभावनवचनेऽयदि. पूर्वेण नित्यप्राप्तौ\n  विकल्पार्थं वचनम् — the rule before made it obligatory and this\n  offers a choice. अयदीति किम्? संभावयामि यद् भुञ्जीत भवान्.',
    "3.3.156": 'SETTLED — हेतुहेतुमतोर्लिङ्. हेतुः कारणम्, हेतुमत् फलम्.\n\nSETTLED — AND THIS IS WHAT 3.3.139 AND 3.3.140 MEANT BY\n  लिङ्निमित्त: हेतुहेतुमतोर्लिङ् इत्येवमादिकं लिङो निमित्तम्.\n  A condition stated seventeen sūtras earlier is only now given\n  its content — the reader of 3.3.139 could not know what\n  satisfied it. The codification records the debt at both ends.\n\nSETTLED — लिङिति वर्तमाने पुनर्लिङ्ग्रहणं\n  कालविशेषप्रतिपत्त्यर्थम्: लिङ् was already running and is named\n  AGAIN so that a particular time is understood, तेनेह न भवति —\n  हन्तीति पलायते, वर्षतीति धावति. A fourth use of repeating a\n  running word: 3.2.106 and 3.2.124 widened, 3.1.141 and 3.2.14\n  fenced off, 3.3.44 and 3.3.75 cancelled, and this NARROWS.',
    "3.3.157": 'SETTLED — इच्छार्थेषु लिङ्लोटौ, सर्वलकाराणामपवादः.\n  SCOPE — कामप्रवेदन इति वक्तव्यम्, इह मा भूत् इच्छन् करोति.',
    "3.3.158": 'SETTLED — समानकर्तृकेषु तुमुन्. It gives a कृत् affix where the\n  rules around it choose a लकार, so it answers from a different\n  entry point — the close of this pāda divides between those two\n  questions.\n\nSETTLED — तुमुन्प्रकृत्यपेक्षमेव समानकर्तृकत्वम्: the sameness of\n  doer is judged from the root the AFFIX GOES ON and not from the\n  other. समानकर्तृकेष्विति किम्? देवदत्तं भुञ्जानमिच्छति\n  यज्ञदत्तः.\n\nSETTLED — इह कस्माद् न भवति इच्छन् करोति? अनभिधानात्. The limit\n  that is not a condition, met at 3.2.1, 3.1.108 and 3.3.30: the\n  check is against usage and there is nothing to codify.',
    "3.3.159": 'SETTLED — लिङ् च. योगविभाग उत्तरार्थः — the FOURTH split in this\n  pāda made for the rule after, with 3.3.115, 3.3.137 and\n  3.3.148. A device used more here than anywhere yet read.',
    "3.3.160": "SETTLED — इच्छार्थेभ्यो विभाषा वर्तमाने. लटि प्राप्ते वचनम् —\n  3.2.123's लट् had the ground and this offers लिङ् beside:\n  इच्छति and इच्छेत्, वष्टि and उश्यात्.\n  The first row of the लकार table with the PRESENT as its time\n  since 3.2.123 itself, a hundred and eighty-seven sūtras back.",
    "3.3.161": 'SETTLED — विधिनिमन्त्रणामन्त्रणाधीष्टसंप्रश्नप्रार्थनेषु लिङ्,\n  सर्वलकाराणामपवादः. Six senses, each glossed, and two of them\n  told apart by whether the thing is BINDING: निमन्त्रणं\n  नियोगकरणम् obliges, आमन्त्रणं कामचारकरणम् leaves one free.\n\nSETTLED — विध्यादयश्च प्रत्ययार्थविशेषणम्: the senses qualify\n  what the AFFIX means and not the root —\n  विध्यादिविशिष्टेषु कर्त्रादिषु लिङ् प्रत्ययो भवति. 3.3.172 and\n  3.3.173 do the opposite, and the vṛtti marks the difference in\n  each place. A distinction between two kinds of semantic\n  condition, which no rule of 3.2 had needed.',
    "3.3.162": 'SETTLED — लोट् च. योगविभाग उत्तरार्थः, the fifth such split — and\n  what it creates is precisely what 3.3.163 then has to protect\n  the कृत्य affixes from.',
    "3.3.163": "SETTLED — प्रैषातिसर्गप्राप्तकालेषु कृत्याश्च, चकाराल्लोट् च.\n  प्रेषणं प्रैषः, कामचाराभ्यनुज्ञानमतिसर्गः, निमित्तभूतस्य\n  कालस्यावसरः प्राप्तकालता.\n\nSETTLED — AND THE SIXTH वासरूप SUSPENSION IS ESTABLISHED HERE, IN\n  ITS GENERAL FORM. किमर्थं प्रैषादिषु कृत्या विधीयन्ते, न\n  सामान्येन भावकर्मणोर्विहिता एव? विशेषविहितेनानेन लोटा बाध्यन्ते\n  — 3.3.162's लोट्, given for this very ground, would displace\n  them. वासरूपविधिना भविष्यन्ति? एवं तर्हि ज्ञापयति —\n  स्त्र्यधिकारात् परेण वासरूपविधिर्नावश्यं भवति: 3.1.94 is NOT\n  OBLIGATORY after the feminine section.\n  3.3.107 had bounded the suspension from the other side, holding\n  it WITHIN that section. Between them the two rules fence the\n  principle off at both ends, and 3.3.167 and 3.3.169 both lean\n  on this one.\n\nSCOPE — विधिप्रैषयोः को विशेषः? केचिदाहुः — अज्ञातज्ञापनं विधिः,\n  प्रेषणं प्रैष इति. Attributed to others and not adopted.",
    "3.3.164": "SETTLED — लिङ् चोर्ध्वमौहूर्तिके, चकाराद् यथाप्राप्तं च.\n  ऊर्ध्वमौहूर्तिक was 3.3.9's condition too — a hundred and\n  fifty-five sūtras back, and for the same ending. The pāda's\n  opening and its close reach for one word.",
    "3.3.165": 'SETTLED — स्मे लोट्, लिङ्कृत्यानामपवादः: it displaces BOTH the\n  ending 3.3.164 gives and the कृत्य affixes 3.3.163 gives, and\n  names neither. One rule excepting two others that answer from\n  two different entry points here.',
    "3.3.166": 'SETTLED — अधीष्टे च. अधीष्टं व्याख्यातम् — the vṛtti points back\n  to 3.3.161 rather than glossing the word again, which is a\n  small thing worth noting: the commentary keeps its own index.',
    "3.3.167": "SETTLED — कालसमयवेलासु तुमुन्.\n\nSETTLED — TWO QUESTIONS ANSWERED BY BORROWING FROM ELSEWHERE.\n  इह कस्माद् न भवति कालः पचति भूतानि? प्रैषादिग्रहणमिहाभिसंबध्यते\n  — 3.3.163's senses are read in, so the rule wants an enjoining.\n  And इह कस्माद् न भवति कालो भोजनस्य? वासरूपेण ल्युडपि भवति,\n  उक्तमिदम् — स्त्र्यधिकारात् परत्र वासरूपविधिरनित्यः: the\n  ज्ञापक of 3.3.163, cited four sūtras later as already settled.",
    "3.3.168": 'SETTLED — लिङ् यदि, तुमुनोऽपवादः: it displaces the affix 3.3.167\n  gives on the same companions. Two adjacent rules, one giving a\n  कृत् affix and one a लकार over the same ground, and they answer\n  from two entry points because they answer two questions.',
    "3.3.169": "SETTLED — अर्हे कृत्यतृचश्च, चकाराल्लिङ् च.\n\nSETTLED — AND THE RULE PROTECTS HALF OF ITSELF FROM THE OTHER\n  HALF. अथ कस्मादर्हे कृत्यतृचो विधीयन्ते, यावता सामान्येन\n  विहितत्वादर्हेऽपि भविष्यन्ति? योऽयमिह लिङ् विधीयते, तेन बाधा मा\n  भूदिति — they are stated so that the लिङ् THIS SAME RULE gives\n  shall not displace them. 3.3.172 and 3.3.174 do the same, three\n  times in this closing run.\n  वासरूपविधिश्चानित्यः, the third citation of 3.3.163's ज्ञापक.",
    "3.3.170": "SETTLED — आवश्यकाधमर्ण्ययोर्णिनिः. अवश्यंभाव आवश्यकम्.\n  उपाधिरयम्, नोपपदम् — these are QUALIFICATIONS of the sense and\n  not companion words, which the rule's form does not show and\n  the vṛtti has to say. The same distinction 3.3.161 drew about\n  what a sense qualifies, drawn here about what a word IS.\n  मयूरव्यंसकादित्वात् समासः accounts for the compound.",
    "3.3.171": "SETTLED — कृत्याश्च. किमर्थमिदम्, यावता सामान्येन विहिता\n  अस्मिन्नपि विषये भविष्यन्ति? विशेषविहितेन णिनिना बाध्येरन् —\n  the rule before, given for this very ground, would displace\n  them. The same shape as 3.3.163 and 3.3.169.\n\nSCAR — AND AN OBJECTION THE VṚTTI DOES NOT FULLY ANSWER.\n  कर्तरि णिनिः, भावकर्मणोः कृत्याः, तत्र कुतो बाधप्रसङ्गः? —\n  णिनि names the doer and the कृत्य affixes the act or the\n  object, so how could one displace the other at all? तत्र\n  केचिदाहुः — भव्यगेयादयः कर्तृवाचिनः कृत्याः, त इहोदाहरणमिति:\n  SOME say certain कृत्य affixes do name the doer. Attributed to\n  others and left there — the objection is not withdrawn and the\n  answer is not the commentator's own.",
    "3.3.172": "SETTLED — शकि लिङ् च, चकारात् कृत्याश्च.\n  शकीति प्रकृत्यर्थविशेषणम् — the sense qualifies what the ROOT\n  means, the opposite of 3.3.161's प्रत्ययार्थविशेषणम्, and the\n  vṛtti marks the difference in both places.\n  सामान्यविहितानां पुनर्वचनं लिङा बाधा मा भूदिति — the second\n  of the three self-protecting rules.",
    "3.3.173": 'SETTLED — आशिषि लिङ्लोटौ. आशंसनमाशीः,\n  अप्राप्तस्येष्टस्यार्थस्य प्राप्तुमिच्छा — which is word for\n  word the gloss 3.3.132 gave आशंसा, forty sūtras back. Two\n  different words with one definition, and nothing in either\n  place remarks on it. आशिषीति किम्? चिरं जीवति देवदत्तः.',
    "3.3.174": 'SETTLED — क्तिच्क्तौ च संज्ञायाम्, समुदायेन चेत् संज्ञा गम्यते —\n  the SEVENTH समुदायोपाधि, after 3.2.80, 3.2.92, 3.2.99, 3.2.185,\n  3.3.34, 3.3.109 and 3.3.118.\n  सामान्येन विहितः क्तः पुनरुच्यते, क्तिचा बाधा मा भूदिति — the\n  third self-protecting rule of the run. And चकारो विशेषणार्थः\n  न क्तिचि दीर्घश्च इति, the च spent so 6.4.39 can pick the affix\n  out. DEBT: 6.4.39 is not codified.',
    "3.3.175": 'SETTLED — माङि लुङ्, सर्वलकाराणामपवादः: मा कार्षीत्, मा हार्षीत्.\n\nSCAR — AND A FORM IN USE IS CALLED WRONG. कथं मा भवतु तस्य पापम्,\n  मा भविष्यतीति? असाधुरेवायम् — that is simply not correct. Then\n  केचिदाहुः — अङिदपरो माशब्दो विद्यते, तस्यायं प्रयोगः: SOME say\n  there is another मा, not the one this rule names, and this is\n  its use.\n  The commentary condemning a form and then recording a way to\n  save it, without choosing. Everywhere else in these two pādas\n  an awkward form was parsed away, sent to 3.3.113, or admitted\n  by बहुलम्; here it is first refused outright.',
    "3.3.176": "SETTLED — स्मोत्तरे लङ् च, चकाराल्लुङ् च: मा स्म करोत्, मा स्म\n  कार्षीत्.\n\nSETTLED — THE LAST SŪTRA OF THE PĀDA. The Kāśikā closes with its\n  colophon — इति श्रीजयादित्यविरचितायां काशिकायां वृत्तौ\n  तृतीयाध्यायस्य तृतीयः पादः — which is how 3.2.188 closed too,\n  and is the corpus's own statement that there is no 3.3.177.",
}

#: Which entry point answers for which rules, and the line describing
#: it — one row per kind, as 3.2's dispatch was collapsed to.
_UNADI = ("3.3.1", "3.3.2")
_GAMYADI = ("3.3.3",)
_KRIYARTHA = ("3.3.10", "3.3.11", "3.3.12")
_LRT_SAT = ("3.3.14",)

#: The rules that choose a लकार on a SENSE or a companion. They
#: are rows in the same table 3.2.110 to 3.2.123 answer from, as
#: 3.3.4 to 3.3.15 are: one question, one resolver.
_LAKARA_SENSE = ("3.3.133", "3.3.134", "3.3.139", "3.3.140",
                 "3.3.142", "3.3.143", "3.3.144", "3.3.145",
                 "3.3.146", "3.3.147", "3.3.148", "3.3.149",
                 "3.3.150", "3.3.151", "3.3.152",
                 "3.3.153", "3.3.154", "3.3.155",
                 "3.3.156", "3.3.157", "3.3.159",
                 "3.3.160", "3.3.161", "3.3.162",
                 "3.3.164", "3.3.165", "3.3.166",
                 "3.3.168", "3.3.172", "3.3.173",
                 "3.3.175", "3.3.176")

#: The rules of the close that give a कृत् affix instead of
#: choosing a लकार — तुमुन्, the कृत्य affixes, तृच्, णिनि,
#: क्तिच्. Four of them exist BECAUSE a लकार rule of the
#: same run would otherwise have displaced what a general
#: rule gives, and 3.3.163's answer to that is where the
#: sixth वासरूप suspension is established.
_VIDHI_KRT = ("3.3.158", "3.3.163", "3.3.167", "3.3.169",
              "3.3.170", "3.3.171", "3.3.174")

_VIDHI_KRT_LINE = (
    'vidhi_affix(sense=..., beside=..., samana_kartrka=..., '
    'samjna=..., wants=...) -> which कृत् affix comes in a sense of '
    'enjoining, deserving, necessity or blessing.'
)

#: 3.3.141 gives no affix: it makes 3.3.140's optional, and says
#: how far by naming the sūtra where the option stops.
_LRN_RANGE = ("3.3.141",)

#: 3.3.131, 3.3.132 and 3.3.135 to 3.3.138 name no affix at all:
#: they move one tense's affixes to another time, and four of the
#: six refuse that. A different question, so a different entry
#: point.
_TRANSFER = ("3.3.131", "3.3.132", "3.3.135", "3.3.136",
             "3.3.137", "3.3.138")

_TRANSFER_LINE = (
    'tense_transfer(like=..., sense=..., for_time=...) -> whether one '
    'tense\'s affixes may stand for another time, and by which rule.'
)

_LRN_RANGE_LINE = (
    'lrn_is_optional(sutra_id) -> whether 3.3.140\'s लृङ् may be declined '
    'at a given rule — the extent 3.3.141 states by naming its far end.'
)
#: 3.3.68, 3.3.70, 3.3.74 and 3.3.79 to 3.3.81 fix a word outright
#: rather than reaching it by conditions, so they answer from their
#: own entry point — the split 3.1's कृत्य run and 3.2 both made.
_FIXED = ("3.3.68", "3.3.70", "3.3.74", "3.3.79", "3.3.80",
          "3.3.81", "3.3.85", "3.3.87", "3.3.97",
          "3.3.101", "3.3.119", "3.3.122", "3.3.123",
          "3.3.124")

#: 3.3.113 is a बहुलम् rule and answers from its own entry
#: point, as 3.3.1 does. It resolves nothing: what it can say
#: is which KIND of going-beyond the vṛtti licenses.
_BAHULAM = ("3.3.113",)

_BAHULAM_LINE = (
    'krtya_lyut_bahulam(group=...) -> that the कृत्य affixes and ल्युट् '
    'come beyond where they were prescribed, and in which of three '
    'ways.'
)

_BHAVA_KRT = tuple("3.3.%d" % _n for _n in range(16, 131)
                   if "3.3.%d" % _n not in _FIXED
                   and "3.3.%d" % _n not in _BAHULAM)

_NIPATANA_LINE = (
    'nipatana(word) -> a form the grammar fixes outright, given as it '
    'stands, with what the vṛtti says is being fixed in it.'
)

_BHAVA_KRT_LINE = (
    'bhava_affix(root, upasarga=..., sense=..., about=..., names_a=..., '
    'bhava=..., akartari_karake=..., samjna=..., parimana=...) -> whether '
    'घञ् comes, and by which rule.'
)

_DISPATCH = (
    (_UNADI, unadi, _UNADI_LINE),
    (_GAMYADI, gamyadi, _GAMYADI_LINE),
    (_KRIYARTHA, kriyartha_affix, _KRIYARTHA_LINE),
    (_LRT_SAT, lrt_substitute, _LRT_SAT_LINE),
    (_LRN_RANGE, lrn_is_optional, _LRN_RANGE_LINE),
    (_TRANSFER, tense_transfer, _TRANSFER_LINE),
    (_VIDHI_KRT, vidhi_affix, _VIDHI_KRT_LINE),
    (_FIXED, nipatana, _NIPATANA_LINE),
    (_BAHULAM, krtya_lyut_bahulam, _BAHULAM_LINE),
    (_BHAVA_KRT, bhava_affix, _BHAVA_KRT_LINE),
)

#: What each rule of this pāda declares it leans on. 3.3.12 restates
#: 3.2.1's अण् and says so; 3.3.14 asks 3.2.127 for its affixes and
#: 3.2.124 for its conditions. All three are calls or citations in the
#: notes, not guesses at kinship.
_REUSES = {
    "3.3.12": ("3.2.1",),
    "3.3.92": ("1.1.20",),
    "3.3.14": ("3.2.124", "3.2.127"),
}

for _sutra, _notes in _RULES.items():
    _apply, _line = lakara_for, _LAKARA_LINE
    for _which, _fn, _describes in _DISPATCH:
        if _sutra in _which:
            _apply, _line = _fn, _describes
            break
    register(
        _sutra,
        apply=_apply,
        codification=_line,
        notes=_notes,
        reuses=_REUSES.get(_sutra, ()),
    )
