# -*- coding: utf-8 -*-
"""
The conditions the कृत् sections turn on, each asked of the rule that
owns it.

These are not rules. They are the handful of questions that rules of
adhyāya 3 keep asking about a root or its neighbours — does it end in
आ, is there a preverb, is its penultimate an इक् — and every one of
them is settled somewhere in adhyāya 1. So each is a call and none is
a restatement:

    ends in आ        the last sound, and nothing else — see below
    ends in हल्      1.1.71 आदिरन्त्येन सहेता, since हल् is a span
    an इक् penult    1.1.65 अलोऽन्त्यात्पूर्व उपधा, with इक्
    a preverb        1.4.59 उपसर्गाः क्रियायोगे

`ends_in_a` is the odd one and the odd one matters: आ is a PLAIN
SOUND, not a pratyāhāra, so no rule makes it denote a span and 1.1.71
is not asked. This line once read as though it were, and 3.2.3 was
registered declaring a reuse of 1.1.71 on the strength of it. The
guard refused the declaration; the entry is corrected rather than the
declaration re-argued.

They lived in `krt_agent` while only 3.1.133–150 needed them. 3.2 asks
the same three from the first sūtra onward, and a second copy is how
two answers to one question start to drift — so they were moved here
rather than copied there.

The reuse guard walks two calls deep from a rule's own function, so a
caller must ask these DIRECTLY rather than through another layer. That
is a constraint on where they are called from, not on what they are,
and it is why each one below calls the registered entry point instead
of a convenience wrapper.
"""

def ends_in_a(root: str) -> bool:
    """
    आकारान्त — whether the root's last sound is आ.

    A root the धातुपाठ taught with an एच् final IS one, by 6.1.45
    आदेच उपदेशे‍शिति, and the vṛtti there insists on the
    order: **अशितीति प्रसज्यप्रतिषेधो‍यम्। तेनैतदात्वमनैमित्तिकं
    प्रागेव प्रत्ययोत्पत्तेर् भवति** — the आ is not caused by the affix
    that follows, so it is already there when a kṛt affix arrives to
    ask this question. That is what lets 3.1.136's क reach
    **सुग्लः** and 3.3.128's युच् reach **सुग्लानः**.

    आ is a PLAIN SOUND, not a pratyāhāra, so no rule makes it denote
    a span and 1.1.71 is not asked. This line once read as though it
    were, and 3.2.3 was registered declaring a reuse of 1.1.71 on the
    strength of it.
    """
    from src.astadhyayi.adesa import scan_phonemes
    from src.astadhyayi.atva import becomes_a

    sounds = scan_phonemes(root)
    if not sounds:
        return False
    last = sounds[-1].text
    if last == "ā":
        return True
    return becomes_a(root, final=last).does == "ā"


def ends_in_hal(root: str) -> bool:
    """
    हलन्त — whether the last sound is a consonant.

    हल् is a pratyāhāra, and 1.1.71 आदिरन्त्येन सहेता is what makes a
    pratyāhāra denote anything, so `resolve` is asked. A hand-written
    vowel list stood in for this once and is the reason the rule is
    stated here in full.
    """
    from src.astadhyayi.adesa import scan_phonemes
    from src.astadhyayi.sivasutra import resolve

    sounds = scan_phonemes(root)
    return bool(sounds) and sounds[-1].text in resolve("hal").sounds


def is_igupadha(root: str) -> bool:
    """
    इगुपध — an इक् vowel as the penultimate sound.

    Two codified rules answer it between them: 1.1.65
    अलोऽन्त्यात्पूर्व उपधा for WHICH sound is the penult, and the
    pratyāhāra इक् for whether it falls in that span.

    What asking buys is visible at 3.1.135, which names ज्ञा, प्री and
    कॄ beside the इगुपध roots. Why becomes plain only here: ज्ञा's
    penult is ञ्, no इक् at all, so the rule could never have reached
    it. Passed in as a flag, the naming looks arbitrary.
    """
    from src.astadhyayi.adesa import upadha
    from src.astadhyayi.sivasutra import resolve

    if not root:
        return False
    penult = upadha(root)
    return bool(penult) and penult in resolve("ik").sounds


def has_upasarga(word: str) -> bool:
    """
    Whether a preverb stands before the root — 1.4.59 उपसर्गाः
    क्रियायोगे, which is codified, so it is asked.

    Rules across 3.1 and 3.2 turn on this, some wanting a preverb and
    some refusing one, and a hand-kept list of the twenty-two would
    have to be corrected in as many places as it was copied.
    """
    from src.astadhyayi.nipata import names_of

    if not word:
        return False
    verdict = names_of(word, kriya_yoga=True)
    return any(name.value == "upasarga" for name in verdict.names)


def in_dhatupatha_span(root: str, first: str, last: str) -> bool:
    """
    Whether a root falls in a stretch of the dhātupāṭha, by code.

    Some gaṇas are given by naming both ends rather than listing —
    3.1.140's ज्वल इत्येवमादिभ्यः कस इत्येवमन्तेभ्यः is one — and a
    span is something the corpus already records. Copying the members
    out would be a second statement of it.
    """
    from src.astadhyayi.pada import entries_for

    return any(first <= entry.code <= last for entry in entries_for(root))


# There is deliberately no helper here for WHICH kāraka an उपपद is.
#
# 3.1.92 says a word a rule states in the locative is an उपपद, and
# 3.2.1 कर्मण्यण् wants the object specifically — so it looks as though
# 1.4.49 कर्तुरीप्सिततमं कर्म could be asked. It cannot. `karaka_of`
# takes the semantic facts ASSERTED of a participant, not a word:
# deciding a kāraka needs the whole clause and not the one word, which
# is why 2.3.1 passes the kāraka in rather than working it out. The
# same debt, recorded in the same way, and a helper that pretended
# otherwise would have been the worst kind of restatement — one that
# looks like a call.
