# -*- coding: utf-8 -*-
"""
The rules the engine can apply, as operations on a form.

A sūtra registered in `rules/` answers a question: *is this letter an इत्*.
The same sūtra here does something: *mark it*. Both are the rule, seen from
two sides, and they share the machinery underneath — nothing in this file
decides which letters are indicatory, it asks `itsamjna.analyze`, which is
what the question-answering side asks too.

**What is here, and why so little.** The it-deletion sequence, 1.3.2 to
1.3.9. That is not an arbitrary starting point: it is the only complete
operational chain among the 379 codified sūtras. Adhyāya 1 is overwhelmingly
saṃjñā and paribhāṣā — rules that name things and rules about reading rules —
and the rules that change a form live in adhyāyas 6 and 7, which are not
codified. So the engine's rule set will stay small until those are done, and
saying so plainly is better than padding it.

What the chain does show is the shape a derivation has, with every part real:
rules that confer a name, a rule that acts on what has been named, an order
that matters, and each step attributing itself to the sūtra that authorised
it.

**1.3.4 न विभक्तौ तुस्माः is not among the rules below**, and the omission is
deliberate rather than an oversight. It is a प्रतिषेध — it takes the name
away rather than conferring one — and `itsamjna.analyze` already applies it
when deciding what is marked at all, so a term never carries a mark that
1.3.4 has withheld. Adding it here as a rule that fires and undoes another
would put a step in the trace that the grammar does not take. The effect is
visible all the same: भ्यस् as a case ending comes through untouched, while
the same letters as an ordinary affix lose the final स्.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Dict, FrozenSet, List, Tuple

from src.astadhyayi.itsamjna import (
    DHATU, PLAIN, PRATYAYA, TADDHITA, VIBHAKTI, Context, analyze,
)
from src.astadhyayi.prakriya import Operational, State, Term
from src.astadhyayi.varna import SVARA
from src.astadhyayi.vipratisedha import Strength


#: What a term's role means to the it-analysis. Half the it-rules ask what
#: kind of thing they are looking at — 1.3.6 षः प्रत्ययस्य only marks a final
#: ष् on an affix, 1.3.4 spares a case ending — so the role is not decoration.
_CONTEXTS: Dict[str, Context] = {
    "dhātu": DHATU,
    "pratyaya": PRATYAYA,
    "vibhakti": VIBHAKTI,
    "taddhita": TADDHITA,
    "form": PLAIN,
}


def context_for(term: Term) -> Context:
    return _CONTEXTS.get(term.role, PLAIN)


#: The eight sūtras that confer the name इत्, with what each one looks for.
#: The text is the codification's own summary of the rule, not a fresh gloss.
MARKING: Tuple[Tuple[str, str], ...] = (
    ("1.3.2", "उपदेशेऽजनुनासिक इत् — a nasalised vowel in the enunciation"),
    ("1.3.3", "हलन्त्यम् — the final consonant"),
    ("1.3.5", "आदिर्ञिटुडवः — an initial ञि, टु or डु"),
    ("1.3.6", "षः प्रत्ययस्य — a final ष् of an affix"),
    ("1.3.7", "चुटू — an initial cu or ṭu consonant of an affix"),
    ("1.3.8", "लशक्वतद्धिते — an initial ल्, श् or ku, off a taddhita"),
)


def _unrecorded(state: State, sutra: str) -> List[Tuple[int, str]]:
    """Marks this sūtra makes that the derivation has not yet recorded."""
    found: List[Tuple[int, str]] = []
    holding = sutra == "1.3.7" and _jha_still_open(state)
    for index, term in enumerate(state.terms):
        # 1.3.2 उपदेशे — read down over the whole it-section. A term an
        # operation has already changed is not the form the grammar
        # enunciates, so none of these rules looks at it.
        if term.stripped or not term.upadesa:
            continue
        for mark in analyze(term.text, context_for(term)).by(sutra):
            if holding and mark.letters == "jh" and "tiṅ" in term.samjnas:
                continue
            if (mark.letters, sutra) not in term.marked:
                found.append((index, mark.letters))
    return found


def _jha_still_open(state: State) -> bool:
    """
    Whether the झ् of an ending is still an open question.

    Four rules reach it — 1.3.7 चुटू, which would call it an इत्; 7.1.3
    झोऽन्तः, which makes it अन्त्; and 7.1.4 अदभ्यस्तात् and 7.1.5
    आत्मनेपदेष्वनतः, which make it अत् instead. The last two ask what the
    **aṅga** is: whether it is अभ्यस्त, and whether it ends in अ. Neither
    can be answered before the विकरण is there and 6.1.10's doubling has
    run, and answered too early the whole site went to whichever rule
    could speak: जुह्वन्ति for जुह्वति, एधते for एधन्ते, and — when only
    7.1.3 was made to wait — भवै for भवन्ति, 1.3.7 having taken the झ्
    away in the meantime.

    So the question is held open for all four together, which is what the
    grammar does by not applying its rules in a sequence at all.
    """
    if not any("vikaraṇa" in term.samjnas for term in state.terms):
        return True
    # The third class's aṅga is not finished when its विकरण arrives: 2.4.75
    # takes शप् away again by श्लु and 6.1.10 doubles the root, and only
    # then is there an अभ्यस्त for 7.1.4 to see. Waiting on a term already
    # marked श्लु was too late — शप् is a विकरण from the moment 3.1.68 puts
    # it there, and 7.1.3 had already fired.
    root = _index_of(state, "dhātu")
    if root is not None and state.terms[root].gana == "03":
        return not any("abhyāsa" in term.samjnas for term in state.terms)
    return False


def _marking_rule(sutra: str, what: str) -> Operational:
    def matches(state: State, _sutra=sutra) -> bool:
        return bool(_unrecorded(state, _sutra))

    def perform(state: State, _sutra=sutra) -> State:
        # One mark per step. A rule that did all of its work at once would
        # collapse two applications of 1.3.3 into a single line of the
        # trace, and the trace is the point.
        index, letters = _unrecorded(state, _sutra)[0]
        term = state.terms[index]
        return state.replace_term(
            index, term.with_mark(letters, _sutra).named("it"))

    def site(state: State, _sutra=sutra):
        # The letters this rule would mark, and in which term. 1.3.5 acting
        # on the opening of डुकृञ् and 1.3.3 on its final are two places,
        # not one, so they never reach 1.4.2.
        found = _unrecorded(state, _sutra)
        return ("mark",) + found[0] if found else ("mark", -1, "")

    return Operational(sutra=sutra, what=what, matches=matches,
                       perform=perform, site=site)


def _tasya_lopah() -> Operational:
    """
    1.3.9 तस्य लोपः — and what was named इत् disappears.

    It must not run while any marking rule still has work, or a form loses
    its final consonant before 1.3.5 has looked at its opening. The engine
    has no notion of rule order beyond 1.4.2, so the condition is stated
    here as the rule itself states it: लोप applies to *that* — to what has
    been named — and nothing is named until the naming rules have run.
    """
    def matches(state: State) -> bool:
        if any(_unrecorded(state, sutra) for sutra, _ in MARKING):
            return False
        return any(term.marked and not term.stripped
                   for term in state.terms)

    def perform(state: State) -> State:
        for index, term in enumerate(state.terms):
            if not term.marked or term.stripped:
                continue
            stem = analyze(term.text, context_for(term)).stem
            from dataclasses import replace
            return state.replace_term(
                index, replace(term, text=stem, stripped=True))
        return state

    def site(state: State):
        for index, term in enumerate(state.terms):
            if term.marked and not term.stripped:
                return ("lopa", index)
        return ("lopa", -1)

    return Operational(
        sutra="1.3.9",
        operation="lopa",
        what="तस्य लोपः — what was named इत् disappears",
        matches=matches,
        perform=perform,
        site=site,
    )


def it_deletion() -> Tuple[Operational, ...]:
    """The chain 1.3.2–1.3.9, in the form the engine applies."""
    return tuple(_marking_rule(sutra, what) for sutra, what in MARKING) \
        + (_tasya_lopah(),)


# ---------------------------------------------------------------------------
# The rules जयति needs — 3.1.68, 7.3.84, 6.1.78
# ---------------------------------------------------------------------------
#
# Chosen by working backwards from one word rather than down the list. जयति
# needs exactly these three, plus 3.4.113 for a name and the it-deletion
# chain already here, and the interpretive rules 1.1.3, 1.1.50 and 1.3.10
# that they lean on. Nothing else. The result is checkable against a
# derivation any grammarian can confirm.


def _index_of(state: State, role: str):
    for index, term in enumerate(state.terms):
        if term.role == role:
            return index
    return None


def _root_ends_at(state: State):
    """
    The last term of the root — **3.1.32 सनाद्यन्ता धातवः**.

    सन्नादयः प्रत्यया अन्ते येषां ते सनाद्यन्ताः, ते धातुसंज्ञा भवन्ति.
    Once णिच् has been added, चोर् and इ are not a root and an affix but
    one root चोरि, and what comes after a root comes after both. शप्
    inserted at the root's own index instead put itself between them and
    गave चुरशपि.

    3.1.32 is a संज्ञा and changes no letter, so it is a helper and not a
    rule of its own: a step in the trace that altered nothing would end
    the derivation rather than advance it.
    """
    index = _index_of(state, "dhātu")
    if index is None:
        return None
    while (index + 1 < len(state.terms)
           and "sanādi" in state.terms[index + 1].samjnas):
        index += 1
    return index


def _karta_sap() -> Operational:
    """3.1.68 कर्तरि शप् — the अ between the root and the ending."""
    def matches(state: State) -> bool:
        root = _root_ends_at(state)
        if root is None or root + 1 >= len(state.terms):
            return False
        # Not "has शप् already" but "has a विकरण already". Nine of the ten
        # classes take something else by 3.1.69–3.1.81, and once one of
        # those has acted 3.1.68 has nothing left to do.
        if any("vikaraṇa" in t.samjnas for t in state.terms):
            return False
        # And a चुरादि root is not yet the root it will be. 3.1.25 has to
        # give it णिच् first, or शप् goes in before the णिच् and the
        # strengthening 7.2.116 owes चुर् never happens: चुरयति for
        # चोरयति.
        if state.terms[root].gana == "10":
            return False
        following = state.terms[root + 1]
        return {"sārvadhātuka", "kartari"} <= following.samjnas

    def perform(state: State) -> State:
        root = _root_ends_at(state)
        # शप् carries its name from 3.4.113, which reaches it because its
        # श् is an इत् — a name conferred by a letter 1.3.9 will remove.
        # `enunciated` matters as much here as on the root. By the time
        # 1.2.4 is asked whether the affix is अपित्, 1.3.9 has taken शप्'s
        # प् away and left a bare अ — which reads as अपित्, makes the affix
        # ङिद्वत्, and blocks the very guṇa that gives जयति its अय्.
        added = Term(text="śap", role="pratyaya", enunciated="śap",
                     samjnas=frozenset({"śap", "pratyaya", "sārvadhātuka",
                                        "vikaraṇa"}))
        return state.insert_term(root + 1, added)

    return Operational(
        sutra="3.1.68", what="कर्तरि शप् — शप् after the root",
        matches=matches, perform=perform,
        site=lambda _s: ("sap",))


def _next_affix(state: State, index: int):
    """
    The affix that follows this term, past anything लुक् has emptied.

    An elided affix is kept as an empty term so 1.1.62 प्रत्ययलोपे
    प्रत्ययलक्षणम् can still see it, and it must not be mistaken for the
    thing a rule is conditioned by.
    """
    return next((term for term in state.terms[index + 1:] if term.text), None)


@lru_cache(maxsize=None)
def _affix_marks(written: str, sarvadhatuka: bool) -> FrozenSet[str]:
    """The it-letters and the अतिदेशs, worked out once per affix."""
    from src.astadhyayi.itsamjna import PRATYAYA, analyze
    from src.astadhyayi.kittva import behaves_as

    its = set(analyze(written, PRATYAYA).it_letters)
    if sarvadhatuka:
        for behaves in behaves_as("", "sārvadhātuka", ending=written).behaves:
            its.add({"ṅit": "ṅ", "kit": "k"}[behaves])
    return frozenset(its)


def _affix_view(term):
    """
    The affix as 1.1.5 क्ङिति च has to see it — its own marks, and the
    marks 1.2.1–1.2.26 make it behave as though it had.

    Two separate readings, and a rule that took only the first got guṇa
    wrong wherever an अतिदेश was what mattered. श (śa) carries no क् and
    no ङ्; it is अपित्, and 1.2.4 सार्वधातुकमपित् makes it ङिद्वत्, which
    is the whole reason तुदति has no guṇa while तोदति would. The marks are
    read off the affix AS ENUNCIATED — शप् and not the अ it leaves — since
    1.3.9 has usually taken them away by the time this is asked.
    """
    from src.astadhyayi.adesa import Adesa

    written = term.enunciated or term.text
    return Adesa(form=written, its=_affix_marks(
        written, "sārvadhātuka" in term.samjnas))


def _strengthening_rule(sutra: str, strengthen, what: str,
                        wants=None) -> Operational:
    """
    7.3.84 and 7.3.86 as operations — they differ only in which vowel.

    **The aṅga is not always the root.** 1.4.13 यस्मात् प्रत्ययविधिस्तदादि
    प्रत्ययेऽङ्गम् makes the aṅga whatever the affix was added after, and
    for सु + श्नु + ति that is सुनु and not सु — the उ that takes guṇa in
    सुनोति belongs to the class-marker. Reading only the root term gave
    सुनुति. So every term is a candidate, and what makes one the aṅga is
    that an affix stands after it.
    """
    def _target(state: State):
        for index, term in enumerate(state.terms):
            if not term.text or (term.marked and not term.stripped):
                continue
            following = _next_affix(state, index)
            if following is None or (following.marked
                                     and not following.stripped):
                continue
            names = following.samjnas
            if not names & {"sārvadhātuka", "ārdhadhātuka"}:
                continue
            if wants is not None and not wants(_affix_view(following)):
                continue
            # 1.1.4 न धातुलोप आर्धधातुके needs to know whether the root
            # has already lost a piece to this very affix — 6.4.48's अ —
            # and only the term remembers.
            lost = "dhātu-lopa" in term.samjnas
            # 1.1.57 अचः परस्मिन् पूर्वविधौ — and where 6.4.48 has taken
            # a final vowel off, that vowel is still there as far as a
            # rule about the उपधा can see.
            gone = "elided-final" in term.samjnas
            found = (
                strengthen(term.text, affix=_affix_view(following),
                           dhatu_lopa=lost, elided_final=gone)
                if wants is not None else
                strengthen(term.text,
                           sarvadhatuka="sārvadhātuka" in names,
                           ardhadhatuka="ārdhadhātuka" in names,
                           affix=_affix_view(following), dhatu_lopa=lost,
                           elided_final=gone))
            if found.result is not None:
                return index, found
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        index, found = _target(state)
        return state.replace_term(
            index, state.terms[index].altered(found.result))

    # No "already done" flag, and none is needed: 1.1.2 अदेङ् गुणः makes
    # the substitutes अ, ए and ओ, and 1.1.51 adds a र् or ल् — not one of
    # them is an इक्, so a vowel that has taken guṇa can never be a target
    # again. A flag would only have to be cleared again at 3.1.32.
    return Operational(
        sutra=sutra, operation="guṇa", what=what,
        matches=matches, perform=perform,
        site=lambda _s: ("guna",))


#: The classes whose विकरण this engine adds after the root, exactly as
#: 3.1.68 adds शप्. The other three are elsewhere: 01 is 3.1.68 itself,
#: 02 and 03 elide rather than add, and 10's णिच् is not a विकरण at all
#: but a सनादि affix making a new root by 3.1.32.
INSERTED_MARKERS: Tuple[str, ...] = ("04", "05", "06", "08", "09")


def _vikarana_rule(code: str) -> Operational:
    """
    One class's विकरण, put after the root — 3.1.69 to 3.1.81.

    Every one of these is an अपवाद of 3.1.68 कर्तरि शप्, and the engine is
    told so rather than ordered by hand: they are given शप्'s own `site`,
    so 1.4.2 विप्रतिषेधे परं कार्यम् is asked at every root and declines to
    decide by position, an exception defeating its उत्सर्ग whatever the
    numbers. The trace then shows which rule won and which it displaced.

    **The class comes from the dhātupāṭha's code and never from the root's
    name.** दिव् (div) is read in the first gaṇa, the fourth and the
    tenth; only 04.0001 दिवुँ says श्यन्. `Term.gana` carries the code.

    The marker is inserted **as the grammar enunciates it** — श्यन् and not
    य — so that 1.3.8 लशक्वतद्धिते and 1.3.3 हलन्त्यम् take its श् and its
    न् away in the trace, and so that 3.4.113 तिङ्शित् सार्वधातुकम् has a
    श् to read. That is not decoration: for श (śa) and श्यन् (śyan) the
    श् is what makes them सार्वधातुक, 1.2.4 सार्वधातुकमपित् then makes them
    ङिद्वत्, and 1.1.5 क्ङिति च keeps guṇa off — which is the whole
    difference between तुदति and *तोदति.
    """
    from src.astadhyayi.itsamjna import PRATYAYA, analyze
    from src.astadhyayi.vikarana import marker_of_class

    marker, sutra = marker_of_class(code)
    its = analyze(marker, PRATYAYA).it_letters
    # 3.4.113 तिङ्शित् सार्वधातुकम्, and 3.4.114 आर्धधातुकं शेषः for the
    # rest. उ (3.1.79) is the one marker here with no श्, and the
    # difference is visible: करोति has its guṇa because 1.2.4 cannot
    # reach an ārdhadhātuka to make it ṅidvat.
    names = frozenset({"pratyaya", "vikaraṇa", marker} | {
        "sārvadhātuka" if "ś" in its else "ārdhadhātuka"})
    # `marker` is the upadeśa — श्ना, श्नु — and 6.4.112 names श्ना by it.

    def matches(state: State) -> bool:
        root = _index_of(state, "dhātu")
        if root is None or root + 1 >= len(state.terms):
            return False
        if state.terms[root].gana != code:
            return False
        if any("vikaraṇa" in t.samjnas for t in state.terms):
            return False
        following = state.terms[root + 1]
        return {"sārvadhātuka", "kartari"} <= following.samjnas

    def perform(state: State) -> State:
        root = _index_of(state, "dhātu")
        return state.insert_term(root + 1, Term(
            text=marker, role="pratyaya", enunciated=marker, samjnas=names))

    return Operational(
        sutra=sutra, standing=Strength.APAVADA,
        what="%s — the class-marker of gaṇa %s" % (marker, code),
        matches=matches, perform=perform,
        site=lambda _s: ("sap",))


def _rudhadi_snam() -> Operational:
    """
    3.1.78 रुधादिभ्यः श्नम् — the seventh class, whose marker goes INSIDE.

    रुधिरावरणे इत्येवमादिभ्यो धातुभ्यः श्नम् प्रत्ययो भवति। शपोऽपवादः।
    **मकारो देशविध्यर्थः** — the म् is there to say WHERE, and by 1.1.47
    मिदचोऽन्त्यात्परः a मित् affix goes after the last vowel of what it is
    added to, not after the whole of it. रुध् takes it as रु-न-ध्, and
    **रुणद्धि, भिनत्ति** are the vṛtti's own two examples.

    **शकारः श्नान्नलोपः इति विशेषणार्थः** — the श् is for 6.4.23 to point
    at, and it also makes the affix सार्वधातुक by 3.4.113, which makes it
    ङिद्वत् by 1.2.4 and so keeps guṇa off the उ of रुध्.

    The root is split into two terms rather than having the marker spliced
    into its text, because what follows still has to reach the pieces
    separately: 6.4.111 श्नसोरल्लोपः drops the अ of this very affix in
    रुन्धः, and it could not find it inside a root.
    """
    from src.astadhyayi.anga import _sounds_of
    from src.astadhyayi.itsamjna import PRATYAYA, analyze

    its = analyze("śnam", PRATYAYA).it_letters
    names = frozenset({"pratyaya", "vikaraṇa", "śnam", "sārvadhātuka"}
                      | ({"sārvadhātuka"} if "ś" in its else set()))

    def _cut(text: str) -> int:
        """1.1.47 — just past the last vowel."""
        vowels = [one for one in _sounds_of(text) if one.kind == "vowel"]
        return -1 if not vowels else vowels[-1].start + len(vowels[-1].text)

    def matches(state: State) -> bool:
        root = _index_of(state, "dhātu")
        if root is None or root + 1 >= len(state.terms):
            return False
        term = state.terms[root]
        if term.gana != "07" or (term.marked and not term.stripped):
            return False
        if any("vikaraṇa" in one.samjnas for one in state.terms):
            return False
        if _cut(term.text) in (-1, len(term.text)):
            return False
        return {"sārvadhātuka", "kartari"} <= state.terms[root + 1].samjnas

    def perform(state: State) -> State:
        from dataclasses import replace as _replace
        root = _index_of(state, "dhātu")
        term = state.terms[root]
        cut = _cut(term.text)
        opened = state.replace_term(
            root, _replace(term, text=term.text[:cut]))
        rest = Term(text=term.text[cut:], role="aṅga", stripped=True,
                    upadesa=False, samjnas=frozenset({"dhātu-śeṣa"}))
        with_marker = opened.insert_term(root + 1, Term(
            text="śnam", role="pratyaya", enunciated="śnam", samjnas=names))
        return with_marker.insert_term(root + 2, rest)

    return Operational(
        sutra="3.1.78", standing=Strength.APAVADA,
        what="रुधादिभ्यः श्नम् — inside the root, by 1.1.47",
        matches=matches, perform=perform,
        site=lambda _s: ("sap",))


def _snasor_allopah() -> Operational:
    """
    6.4.111 श्नसोरल्लोपः — and श्नम् loses its अ before a ङित् ending.

    श्नस्य अस्तेश्च अकारस्य लोपो भवति सार्वधातुके क्ङिति परतः:
    **रुन्धः, रुन्धन्ति; भिन्तः, भिन्दन्ति**; and of अस्, **स्तः, सन्ति**.
    **क्ङितीत्येव** — भिनत्ति, अस्ति, where the ending is पित् and the अ
    stands.

    It is what makes the seventh class's singular and plural differ:
    रुणद्धि keeps the अ and रुन्धः does not, and one rule accounts for
    both. अस् is not reached here — the engine has no अस् yet.
    """
    def _target(state: State):
        marker = next((index for index, term in enumerate(state.terms)
                       if "śnam" in term.samjnas), None)
        if marker is None:
            return None
        term = state.terms[marker]
        if not term.text.endswith("a") or not term.stripped:
            return None
        ending = state.terms[-1]
        if "tiṅ" not in ending.samjnas or (ending.marked
                                           and not ending.stripped):
            return None
        return marker if _affix_view(ending).its & {"ṅ", "k"} else None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        marker = _target(state)
        term = state.terms[marker]
        return state.replace_term(marker, term.altered(term.text[:-1]))

    return Operational(
        sutra="6.4.111", operation="lopa",
        what="श्नसोरल्लोपः — श्नम्'s अ goes before a ङित्: रुन्धः",
        matches=matches, perform=perform,
        site=lambda _s: ("snasor",))


def _snabhyastayor_atah() -> Operational:
    """
    6.4.112 श्नाभ्यस्तयोरातः — श्ना's आ, and an अभ्यस्त's, before a ङित्.

    श्ना इत्येतस्य अभ्यस्तानां च अङ्गानाम् आकारस्य लोपो भवति सार्वधातुके
    क्ङिति परतः: **लुनते, लुनताम्**; of the अभ्यस्त, **मिमते, संजिहते**.

    **श्नाभ्यस्तयोरिति किम्?** यान्ति, वान्ति — the आ belongs to the root
    and to neither of the two. **आत इति किम्?** बिभ्रति. **क्ङितीत्येव** —
    अलुनात्, अजहात्.

    It is 6.4.111's twin, one rule down: that one takes श्नम्'s अ and this
    one श्ना's आ, and between them the ninth class's singular and plural
    part — क्रीणाति keeps its आ before the पित् ति and **क्रीणन्ति** loses
    it before the अपित् झि.
    """
    def _target(state: State):
        ending = state.terms[-1]
        if "tiṅ" not in ending.samjnas or (ending.marked
                                           and not ending.stripped):
            return None
        if not _affix_view(ending).its & {"ṅ", "k"}:
            return None
        # हलीति किम्? लुनन्ति, मिमते — the vṛtti's counter-example to
        # 6.4.113 is this rule's example, so the two divide the ङित्
        # endings between them by what they begin with. Before a
        # consonant it is 6.4.113's ई: क्रीणीतः, not *क्रीन्तः.
        if not ending.text or ending.text[0] not in SVARA:
            return None
        for index, term in enumerate(state.terms):
            reached = term.samjnas & {"śnā", "abhyasta"}
            # 6.1.5 उभे अभ्यस्तम् names both halves, but the आ the rule
            # takes is the **aṅga's** final one and the copy is not final.
            # Reading the copy too, दा came out ददति as *द्दति.
            if "abhyāsa" in term.samjnas:
                continue
            if not reached or not term.text.endswith("ā"):
                continue
            if term.marked and not term.stripped:
                continue
            return index
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        index = _target(state)
        term = state.terms[index]
        return state.replace_term(index, term.altered(term.text[:-1]))

    return Operational(
        sutra="6.4.112", operation="lopa",
        what="श्नाभ्यस्तयोरातः — the आ goes before a ङित्: क्रीणन्ति",
        matches=matches, perform=perform,
        site=lambda _s: ("snabhyasta",))


def _i_haly_aghoh() -> Operational:
    """
    6.4.113 ई हल्यघोः — and before a consonant the same आ becomes ई.

    श्नान्तानाम् अङ्गानाम् अभ्यस्तानां च **घुवर्जितानाम्** आत ईकारादेशो
    भवति हलादौ सार्वधातुके क्ङिति परतः: **लुनीतः, पुनीतः, लुनीथः**; of
    the अभ्यस्त, **मिमीते, संजिहीते**.

    **हलीति किम्?** लुनन्ति, मिमते — where 6.4.112 drops the आ instead.
    **अघोरिति किम्?** दत्तः, धत्तः — दा and धा are घु by 1.1.20 and are
    left out, which is why the third class's दा does not go this way.
    **क्ङितीत्येव** — लुनाति, जहाति.

    Between this and 6.4.112 the ninth class's whole paradigm is settled:
    क्रीणाति before the पित् ति, क्रीणीतः before the अपित् तस्,
    क्रीणन्ति before the vowel-initial अन्ति.
    """
    def _target(state: State):
        ending = state.terms[-1]
        if "tiṅ" not in ending.samjnas or (ending.marked
                                           and not ending.stripped):
            return None
        if not _affix_view(ending).its & {"ṅ", "k"}:
            return None
        if not ending.text or ending.text[0] in SVARA:
            return None
        root = _index_of(state, "dhātu")
        if root is not None and _is_ghu(state.terms[root]):
            return None
        for index, term in enumerate(state.terms):
            reached = term.samjnas & {"śnā", "abhyasta"}
            # 6.1.5 उभे अभ्यस्तम् names both halves, but the आ the rule
            # takes is the **aṅga's** final one and the copy is not final.
            # Reading the copy too, दा came out ददति as *द्दति.
            if "abhyāsa" in term.samjnas:
                continue
            if not reached or not term.text.endswith("ā"):
                continue
            if term.marked and not term.stripped:
                continue
            return index
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        index = _target(state)
        term = state.terms[index]
        return state.replace_term(index, term.altered(term.text[:-1] + "ī"))

    return Operational(
        sutra="6.4.113", operation="ādeśa",
        what="ई हल्यघोः — the आ becomes ई before a consonant: क्रीणीतः",
        matches=matches, perform=perform,
        site=lambda _s: ("snabhyasta",))


def _is_ghu(term) -> bool:
    """
    1.1.20 दाधा घ्वदाप् — whether the root bears the name घु.

    6.4.113 excepts them by name — **अघोरिति किम्? दत्तः, धत्तः** — so
    the question is put to the sūtra that confers the name, which reads
    the six out of the dhātupāṭha rather than listing them.
    """
    from src.astadhyayi.samjna import ghu_roots

    return (term.enunciated or term.text) in ghu_roots()


def _jha_after_abhyasta() -> Tuple[Operational, ...]:
    """
    7.1.4 अदभ्यस्तात् and 7.1.5 आत्मनेपदेष्वनतः — झ becomes अत्, twice over.

    **अभ्यस्तात् अङ्गात् उत्तरस्य झकारस्य अत् इत्ययम् आदेशो भवति**:
    ददति, दधति, जक्षति, जाग्रति. **अन्तादेशापवादोऽयम्** — it is an
    exception to 7.1.3 झोऽन्तः, which would have given अन्त्.

    And 7.1.5, of the middle endings after a stem that does not end in
    अ: **चिन्वते, पुनते, लुनते**. **आत्मनेपदेष्विति किम्?** चिन्वन्ति,
    लुनन्ति. **अनत इति किम्?** च्यवन्ते, प्लवन्ते — where the stem does
    end in अ and 7.1.3 stands.

    Both are given 7.1.3's own site so 1.4.2 is asked and the exception
    wins, which is the same arrangement 7.1.3 itself has against 1.3.7.
    """
    def _rule(sutra: str, wants_atmanepada: bool, what: str) -> Operational:
        def _target(state: State):
            for index, term in enumerate(state.terms):
                if "tiṅ" not in term.samjnas or term.stripped:
                    continue
                if not term.text.startswith("jh"):
                    continue
                middle = "ātmanepada" in term.samjnas
                if middle is not wants_atmanepada:
                    continue
                before = _preceding_text(state, index)
                if wants_atmanepada:
                    if before.endswith("a"):
                        continue          # अनत इति किम्? — च्यवन्ते
                elif not any("abhyasta" in one.samjnas
                             for one in state.terms):
                    continue
                return index
            return None

        def matches(state: State) -> bool:
            return _target(state) is not None

        def perform(state: State) -> State:
            index = _target(state)
            term = state.terms[index]
            return state.replace_term(
                index, term.altered("at" + term.text[2:]))

        def site(state: State):
            found = _target(state)
            # the shape 1.3.7's marking rule makes, so the three contend
            return ("mark", found, "jh") if found is not None else ("jha", -1)

        return Operational(sutra=sutra, standing=Strength.APAVADA,
                           what=what, matches=matches, perform=perform,
                           site=site)

    return (
        _rule("7.1.4", False,
              "अदभ्यस्तात् — झ becomes अत् after an अभ्यस्त: ददति"),
        _rule("7.1.5", True,
              "आत्मनेपदेष्वनतः — and in the middle after a non-अ stem: "
              "चिन्वते"),
    )


def _preceding_text(state: State, index: int) -> str:
    """Everything of the form that stands before this term."""
    return "".join(term.text for term in state.terms[:index])


def _tripadi_hardening() -> Tuple[Operational, ...]:
    """
    8.2.40 झषस्तथोर्धोऽधः and 8.4.53 झलां जश् झशि, in that order.

    Both act on the surface and across terms, and the order between them
    and 8.4.55 खरि च is not chosen here: all three sit in the tripādī, and
    8.2.1 पूर्वत्रासिद्धम् decides, which `_asiddha_settles` now asks.
    रुणध् + ति would otherwise have gone to रुणत्ति by खरि च.
    """
    from src.astadhyayi.anga import (
        coh_kuh, jhalam_jas_jhasi, jhasas_tathoh_dhah)

    def _rule(sutra: str, change, what: str, does: str) -> Operational:
        def _target(state: State):
            if any(term.marked and not term.stripped
                   for term in state.terms):
                return None
            found = change(state.surface)
            if found.result is None:
                return None
            where = _term_holding(state, found.at)
            return None if where is None else (where, found)

        def matches(state: State) -> bool:
            return _target(state) is not None

        def perform(state: State) -> State:
            (index, offset), found = _target(state)
            term = state.terms[index]
            return state.replace_term(index, term.altered(
                term.text[:offset] + found.now
                + term.text[offset + len(found.was):]))

        return Operational(sutra=sutra, operation=does, what=what,
                           matches=matches, perform=perform,
                           site=lambda _s: ("khari",))

    return (
        _rule("8.2.30", coh_kuh,
              "चोः कुः — the चु becomes its कु: पक्ता, युनक्ति", "kutva"),
        _rule("8.2.40", jhasas_tathoh_dhah,
              "झषस्तथोर्धोऽधः — the त् becomes ध्: लब्धा, रुणद्धि",
              "dhatva"),
        _rule("8.4.53", jhalam_jas_jhasi,
              "झलां जश् झशि — the झल् takes its जश्: रुणद्धि", "jaś"),
    )


def _juhotyadi_slu() -> Operational:
    """
    2.4.75 जुहोत्यादिभ्यः श्लुः — the third class, and why not simply लुक्.

    शबनुवर्तते, न यङ्। जुहोत्यादिभ्य उत्तरस्य शपः श्लुर्भवति:
    **जुहोति, बिभर्ति, नेनेक्ति**.

    **लुकि प्रकृते श्लुविधानं द्विर्वचनार्थम्** — लुक् was already
    available two sūtras back and would have elided शप् just as well. श्लु
    is named instead **so that the root may double**, 6.1.10 श्लौ being
    conditioned on this elision and no other. The whole difference between
    अत्ति and जुहोति is which word the grammar chose for the same silence.
    """
    def _target(state: State):
        root = _index_of(state, "dhātu")
        if root is None or state.terms[root].gana != "03":
            return None
        for index, term in enumerate(state.terms):
            if "śap" in term.samjnas and term.text and "ślu" not in term.samjnas:
                return index
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        from dataclasses import replace as _replace
        index = _target(state)
        term = state.terms[index]
        return state.replace_term(index, _replace(
            term, text="", samjnas=term.samjnas | {"ślu", "luk-done"}))

    return Operational(
        sutra="2.4.75", operation="luk",
        what="जुहोत्यादिभ्यः श्लुः — शप् goes, and the root will double",
        matches=matches, perform=perform,
        site=lambda _s: ("slu",))


def _dvirvacana() -> Operational:
    """
    6.1.10 श्लौ — the root is doubled, and 6.1.4 names the first the अभ्यास.

    श्लौ परतः **अनभ्यासस्य धातोः अवयवस्य प्रथमस्य एकाचो** द्वे भवतः:
    **जुहोति, बिभेति, जिह्रेति**. 6.1.1 एकाचो द्वे प्रथमस्य is the
    heading that supplies एकाच् and प्रथमस्य, and 6.1.4 पूर्वोऽभ्यासः
    gives the first of the two its name — every rule of 7.4.58–97 speaks
    of it by that name and none of them could reach it otherwise.

    **अनभ्यासस्य** is why this fires once: what is already an अभ्यास is
    not doubled again.

    **SCOPE.** एकाच् is read here as the whole root, which is what the
    third class's roots are — हु, दा, धा, भी, भृ, मा are all of one
    vowel. A polysyllabic root would need 6.1.1's प्रथमस्य read strictly,
    and none of the twenty-six needs it.
    """
    def _target(state: State):
        if not any("ślu" in term.samjnas for term in state.terms):
            return None
        if any("abhyāsa" in term.samjnas for term in state.terms):
            return None
        root = _index_of(state, "dhātu")
        if root is None:
            return None
        term = state.terms[root]
        if not term.text or (term.marked and not term.stripped):
            return None
        return root

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        root = _target(state)
        term = state.terms[root]
        from dataclasses import replace as _replace
        # 6.1.5 उभे अभ्यस्तम् — BOTH are called अभ्यस्त, not the copy
        # alone, and 6.4.112 asks after that name on the root's own half:
        # जुहु + अति is जुह्वति because the pair bears it.
        doubled = state.replace_term(root, _replace(
            term, samjnas=term.samjnas | {"abhyasta"}))
        return doubled.insert_term(root, Term(
            text=term.text, role="abhyāsa", stripped=True, upadesa=False,
            samjnas=frozenset({"abhyāsa", "abhyasta"})))

    return Operational(
        sutra="6.1.10", operation="dvirvacana",
        what="श्लौ — the root is doubled, and 6.1.4 names the first अभ्यास",
        matches=matches, perform=perform,
        site=lambda _s: ("dvirvacana",))


def _abhyasa_rules() -> Tuple[Operational, ...]:
    """
    7.4.59, 7.4.60, 7.4.62, 7.4.66, 7.4.76 and 8.4.54, on the copy alone.

    Six rules with one condition between them — that what they act on is
    the अभ्यास 6.1.4 named — and each is asked of that term and no other.
    7.4.76 भृञामित् carries APAVADA standing against 7.4.66 उरत् at the
    same site, because both reach भृ and the word is बिभर्ति.
    """
    from src.astadhyayi.anga import (
        abhyasa_hrasvah, abhyase_car, bhrnam_it, haladih_sesah, kuhos_cuh,
        urat)

    def _rule(sutra, change, what, standing=Strength.EQUAL,
              site="abhyasa", wants_root=False) -> Operational:
        def _target(state: State):
            for index, term in enumerate(state.terms):
                if "abhyāsa" not in term.samjnas or not term.text:
                    continue
                root = _index_of(state, "dhātu")
                enunciated = ("" if root is None
                              else state.terms[root].enunciated)
                found = (change(term.text, root=enunciated) if wants_root
                         else change(term.text))
                if found.result is not None:
                    return index, found
            return None

        def matches(state: State) -> bool:
            return _target(state) is not None

        def perform(state: State) -> State:
            index, found = _target(state)
            return state.replace_term(
                index, state.terms[index].altered(found.result))

        return Operational(sutra=sutra, standing=standing, what=what,
                           matches=matches, perform=perform,
                           site=lambda _s, _site=site: (_site,))

    return (
        _rule("7.4.60", haladih_sesah,
              "हलादिः शेषः — only the copy's first consonant stays"),
        _rule("7.4.59", abhyasa_hrasvah,
              "ह्रस्वः — the अभ्यास's vowel is short: ददाति"),
        _rule("7.4.66", urat, "उरत् — an ऋ-final अभ्यास takes अ",
              site="abhyasa-vowel"),
        _rule("7.4.76", bhrnam_it,
              "भृञामित् — बिभर्ति, मिमीते, जिहीते",
              standing=Strength.APAVADA, site="abhyasa-vowel",
              wants_root=True),
        _rule("7.4.62", kuhos_cuh,
              "कुहोश्चुः — the copy's कु or ह् becomes a चु: जुहोति",
              site="abhyasa-sound"),
        _rule("8.4.54", abhyase_car,
              "अभ्यासे चर् च — and it loses its aspiration: दधाति",
              site="abhyasa-sound"),
    )


def _vikarana_rules() -> Tuple[Operational, ...]:
    """The five classes whose marker is added after the root."""
    return tuple(_vikarana_rule(code) for code in INSERTED_MARKERS)


def _guna_before_affix() -> Operational:
    """7.3.84 — guṇa of the इगन्त aṅga before a sārvadhātuka."""
    from src.astadhyayi.anga import guna_before_affix

    return _strengthening_rule(
        "7.3.84", guna_before_affix,
        "सार्वधातुकार्धधातुकयोः — guṇa of the इगन्त अङ्ग")


def _laghupadha_guna() -> Operational:
    """7.3.86 — and guṇa of an aṅga whose penult is light."""
    from src.astadhyayi.anga import pugantalaghupadhasya

    return _strengthening_rule(
        "7.3.86", pugantalaghupadhasya,
        "पुगन्तलघूपधस्य च — guṇa of the light penult: बोधति, कर्षति")


def _nnit_vrddhi() -> Tuple[Operational, ...]:
    """
    7.2.115 अचो ञ्णिति and 7.2.116 अत उपधायाः, the two halves of one job.

    Both fire only where the affix that follows carries a ञ् or a ण् — and
    that is read off the affix as enunciated, णिच् and not the इ 1.3.9
    leaves. They do not reach the same root: one wants a vowel at the end
    and the other an अ before it, so they never contend and neither needs
    to defeat the other.
    """
    from src.astadhyayi.anga import aco_nniti, ato_upadhayah

    def nnit(affix) -> bool:
        return bool(affix.its & {"ñ", "ṇ"})

    return (
        _strengthening_rule(
            "7.2.115", aco_nniti,
            "अचो ञ्णिति — vṛddhi of the final vowel: चेता, लाविता",
            wants=nnit),
        _strengthening_rule(
            "7.2.116", ato_upadhayah,
            "अत उपधायाः — vṛddhi of the penult अ: पाठयति", wants=nnit),
    )


def _ato_lopah() -> Operational:
    """
    6.4.48 अतो लोपः, and it is done though two later rules reach the same अ.

    Its `site` is the one the strengthening rules share, so 7.2.115 and
    this arrive at `_settle` together. The standing is **PURVA**, because
    the Kāśikā ends its entry on 6.4.48 by saying so in as many words —
    वृद्धिदीर्घाभ्यामतो लोपः पूर्वविप्रतिषेधेन — and 1.4.2 would otherwise
    give the place to the later number and make काथयति of कथयति.

    The term is marked as having lost part of the root. 1.1.4 न धातुलोप
    आर्धधातुके then keeps 7.2.116 off the अ that is left, which is the
    second half of why कथ (katha) gives कथयति.
    """
    from src.astadhyayi.anga import ato_lopah

    def _target(state: State):
        for index, term in enumerate(state.terms):
            if not term.text or (term.marked and not term.stripped):
                continue
            following = _next_affix(state, index)
            if following is None or "ārdhadhātuka" not in following.samjnas:
                continue
            if following.marked and not following.stripped:
                continue
            found = ato_lopah(term.text)
            if found.result is not None:
                return index, found
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        from dataclasses import replace as _replace
        index, found = _target(state)
        term = state.terms[index]
        return state.replace_term(index, _replace(
            term.altered(found.result),
            samjnas=term.samjnas | {"dhātu-lopa", "elided-final"}))

    return Operational(
        sutra="6.4.48", operation="lopa", standing=Strength.PURVA,
        what="अतो लोपः — the अ-final aṅga loses its अ: चिकीर्षिता",
        matches=matches, perform=perform,
        site=lambda _s: ("guna",))


def _curadi_nic() -> Operational:
    """
    3.1.25 चुरादिभ्यो णिच् — the tenth class, and why it is not a विकरण.

    सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो णिच् — a
    long list of words ending in **चुरादि**, which is 509 of the
    dhātupāṭha's roots. The affix is not a class-marker like शप् or श:
    3.1.32 सनाद्यन्ता धातवः makes what ends in it a **root**, so शप् then
    comes after that root in the ordinary way and चोरयति has both. That
    is why this rule does not contend with 3.1.68 at its site — nothing
    is being displaced, and both apply in turn.

    णिच् is ञित्-or-णित् by its ण्, which 7.2.115 and 7.2.116 read; and
    आर्धधातुक by 3.4.114 आर्धधातुकं शेषः, having neither तिङ् nor श्, so
    1.2.4 cannot make it ङिद्वत् and the strengthening stands.
    """
    def matches(state: State) -> bool:
        root = _index_of(state, "dhātu")
        if root is None:
            return False
        if state.terms[root].gana != "10":
            return False
        return not any("sanādi" in t.samjnas for t in state.terms)

    def perform(state: State) -> State:
        root = _index_of(state, "dhātu")
        return state.insert_term(root + 1, Term(
            text="ṇic", role="pratyaya", enunciated="ṇic",
            samjnas=frozenset({"pratyaya", "ṇic", "sanādi",
                               "ārdhadhātuka"})))

    return Operational(
        sutra="3.1.25", what="चुरादिभ्यो णिच् — the tenth class takes णिच्",
        matches=matches, perform=perform,
        site=lambda _s: ("nic",))


def _sino_guna() -> Operational:
    """7.4.21 शीङः सार्वधातुके गुणः — the one root that overrides 1.1.5."""
    from src.astadhyayi.anga import sino_guna

    def _target(state: State):
        index = _index_of(state, "dhātu")
        if index is None:
            return None
        term = state.terms[index]
        if term.marked and not term.stripped:
            return None
        following = _next_affix(state, index)
        if following is None or "sārvadhātuka" not in following.samjnas:
            return None
        if following.marked and not following.stripped:
            return None
        found = sino_guna(term.text, sarvadhatuka=True,
                          enunciated=term.enunciated)
        return None if found.result is None else (index, found)

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        index, found = _target(state)
        return state.replace_term(
            index, state.terms[index].altered(found.result))

    return Operational(
        sutra="7.4.21", operation="guṇa",
        what="शीङः सार्वधातुके गुणः — शेते, शयाते",
        matches=matches, perform=perform,
        site=lambda _s: ("guna",))


def _ayadi() -> Operational:
    """6.1.78 एचोऽयवायावः — ए, ओ, ऐ, औ before a vowel."""
    from src.astadhyayi.anga import ayadi
    from src.astadhyayi.varna import SVARA

    def _target(state: State):
        for index in range(len(state.terms) - 1):
            here = state.terms[index]
            # The same guard the guṇa rule had wrong: wait while marks are
            # pending, not for ever. णीञ् reached णेअति and stopped, because
            # its ñ had once been marked.
            if here.marked and not here.stripped:
                continue
            # अचि — the *sound* that follows, which is not always the next
            # term. 2.4.72's लुक् leaves शप् standing as an empty term (so
            # that 1.1.62 प्रत्ययलोपे प्रत्ययलक्षणम् can still see it), and
            # reading only `terms[index + 1]` found that emptiness and gave
            # up: या (yā) + अन्ति came out यााअन्ति → 'yāanti' with the two
            # vowels never meeting. An elided affix is not a sound between
            # two sounds. `_khari_ca` has looked past it from the start;
            # this rule and the एकादेश pair had not.
            nxt = next((t for t in state.terms[index + 1:] if t.text), None)
            if nxt is None or nxt.text[0] not in SVARA:
                continue
            found = ayadi(here.text, before_vowel=True)
            if found.result is not None:
                return index, found
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        index, found = _target(state)
        return state.replace_term(
            index, state.terms[index].altered(found.result))

    return Operational(
        sutra="6.1.78", operation="sandhi",
        what="एचोऽयवायावः — एच् before a vowel, यथासंख्यम्",
        matches=matches, perform=perform,
        site=lambda _s: ("ayadi",))


def _dhatvadeh_rule() -> Operational:
    """6.1.64 धात्वादेः षः सः and 6.1.65 णो नः, on the root's opening."""
    from src.astadhyayi.anga import dhatvadeh

    def _target(state: State):
        index = _index_of(state, "dhātu")
        if index is None:
            return None
        term = state.terms[index]
        if not term.upadesa:
            return None
        found = dhatvadeh(term.text)
        return (index, found) if found.changed else None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        from dataclasses import replace as _replace
        index, found = _target(state)
        # The upadeśa flag is NOT cleared. These sūtras change how the root
        # is enunciated, and the it-rules still have to reach what is left:
        # णीञ् must lose its ñ after becoming नीञ्, or नयति never appears.
        return state.replace_term(
            index, _replace(state.terms[index], text=found.result))

    return Operational(
        sutra="6.1.65", what="धात्वादेः — the root's initial ष् or ण्",
        matches=matches, perform=perform,
        site=lambda _s: ("dhatvadeh",))


def _tit_atmanepada() -> Operational:
    """3.4.79 टित आत्मनेपदानां टेरे — the ending's टि becomes ए."""
    from src.astadhyayi.anga import tit_atmanepada

    def _target(state: State):
        for index, term in enumerate(state.terms):
            if "ātmanepada" not in term.samjnas:
                continue
            if "ṭi-done" in term.samjnas:
                continue
            if term.marked and not term.stripped:
                continue
            found = tit_atmanepada(term.text)
            if found.changed:
                return index, found
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        from dataclasses import replace as _replace
        index, found = _target(state)
        term = state.terms[index]
        return state.replace_term(index, _replace(
            term.altered(found.ending),
            samjnas=term.samjnas | {"ṭi-done"}))

    return Operational(
        sutra="3.4.79", what="टित आत्मनेपदानां टेरे — the टि becomes ए",
        matches=matches, perform=perform,
        site=lambda _s: ("tite",))



def _thasah_se() -> Operational:
    """
    3.4.80 थासः से, standing against 3.4.79 for the same ending.

    टित इत्येव — the rule borrows 3.4.79's word and takes only थास्,
    replacing the whole of it rather than its टि: पचसे (pacase), एधसे
    (edhase). Without it 3.4.79 reached थास् too, turned its टि into ए
    and produced एधथे (edhathe), which is not a word.

    Its `site` is deliberately 3.4.79's own, so the two arrive at
    `_settle` together and 1.4.2 विप्रतिषेधे परं कार्यम् is asked. With
    APAVADA standing 3.4.80 wins — which is 1.4.2 declining to decide by
    position, as it does for every exception. The ending is then marked
    settled, because 3.4.79 has nothing left to do to a से that is
    already ए-final.
    """
    from src.astadhyayi.tin_adesha import tin_adesha

    def _target(state: State):
        for index, term in enumerate(state.terms):
            if "ātmanepada" not in term.samjnas or "ṭi-done" in term.samjnas:
                continue
            if term.marked and not term.stripped:
                continue
            got = tin_adesha(term.text, lakara="laṭ",
                             ending_pada="ātmanepada")
            if getattr(got, "changed", False) and got.by == "3.4.80":
                return index, got.gives
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        from dataclasses import replace as _replace
        index, gives = _target(state)
        term = state.terms[index]
        return state.replace_term(index, _replace(
            term.altered(gives),
            samjnas=term.samjnas | {"ṭi-done"}))

    return Operational(
        sutra="3.4.80", standing=Strength.APAVADA,
        what="थासः से — थास् is replaced whole, not in its टि",
        matches=matches, perform=perform,
        site=lambda _s: ("tite",))


def _jho_antah() -> Operational:
    """
    7.1.3 झोऽन्तः, standing against 1.3.7 चुटू for the same झ्.

    Its `site` is deliberately the *same tuple* 1.3.7's marking rule
    produces, so the two arrive at `_settle` together and 1.4.2 is asked
    about them. Given APAVADA standing it wins — which is 1.4.2 declining
    to decide by position, exactly as it declines for an exception.
    """
    from src.astadhyayi.anga import jho_antah

    def _target(state: State):
        if _jha_still_open(state):
            return None
        for index, term in enumerate(state.terms):
            if term.stripped or not term.upadesa:
                continue
            found = jho_antah(term.text)
            if found.result is not None:
                return index, found
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        index, found = _target(state)
        return state.replace_term(
            index, state.terms[index].altered(found.result))

    def site(state: State):
        found = _target(state)
        # the shape _marking_rule uses, so the two contend
        return ("mark", found[0], "jh") if found else ("jho", -1)

    return Operational(
        sutra="7.1.3", standing=Strength.APAVADA,
        what="झोऽन्तः — the झ् of the affix becomes अन्त्",
        matches=matches, perform=perform, site=site)


def _ato_dirgho() -> Operational:
    """7.3.101 अतो दीर्घो यञि — the अ of शप् before मि, वः, मः."""
    from src.astadhyayi.anga import ato_dirgho_yani

    def _target(state: State):
        for index in range(len(state.terms) - 1):
            here, nxt = state.terms[index], state.terms[index + 1]
            if here.marked and not here.stripped:
                continue
            if "dīrgha-done" in here.samjnas:
                continue
            if "sārvadhātuka" not in nxt.samjnas:
                continue
            if nxt.marked and not nxt.stripped:
                continue
            found = ato_dirgho_yani(here.text, nxt.text)
            if found.result is not None:
                return index, found
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        from dataclasses import replace as _replace
        index, found = _target(state)
        term = state.terms[index]
        return state.replace_term(index, _replace(
            term.altered(found.result),
            samjnas=term.samjnas | {"dīrgha-done"}))

    return Operational(
        sutra="7.3.101", operation="dīrgha",
        what="अतो दीर्घो यञि — the अ lengthens",
        matches=matches, perform=perform,
        site=lambda _s: ("dirgha",))


def _final_visarga() -> Tuple[Operational, ...]:
    """
    8.2.66 ससजुषो रुः and 8.3.15 खरवसानयोर्विसर्जनीयः.

    Both stand in the tripādī, and both wait until nothing else applies:
    a final स् is only a *pada*-final स् once the word is otherwise made.
    The engine has no phase marker, so the condition is stated as the rules
    state it — the term must be settled, with no marks pending and no
    affix still to come.
    """
    from src.astadhyayi.anga import kharavasanayoh, sasajuso_ruh

    def _last(state: State):
        index = len(state.terms) - 1
        term = state.terms[index]
        if term.marked and not term.stripped:
            return None
        return index, term

    def _ru():
        def matches(state: State) -> bool:
            found = _last(state)
            return bool(found) and sasajuso_ruh(found[1].text).result

        def perform(state: State) -> State:
            index, term = _last(state)
            return state.replace_term(
                index, term.altered(sasajuso_ruh(term.text).result))

        return Operational(
            sutra="8.2.66", what="ससजुषो रुः — the final स् becomes रु",
            matches=matches, perform=perform, site=lambda _s: ("ru",))

    def _visarga():
        def matches(state: State) -> bool:
            found = _last(state)
            return bool(found) and kharavasanayoh(found[1].text).result

        def perform(state: State) -> State:
            index, term = _last(state)
            return state.replace_term(
                index, term.altered(kharavasanayoh(term.text).result))

        return Operational(
            sutra="8.3.15",
            what="खरवसानयोर्विसर्जनीयः — and रु becomes the visarga",
            matches=matches, perform=perform, site=lambda _s: ("visarga",))

    return (_ru(), _visarga())


def _ekadesa() -> Tuple[Operational, ...]:
    """
    6.1.101 अकः सवर्णे दीर्घः and 6.1.97 अतो गुणे, which excepts it.

    They are given the same `site`, so both reach `_settle` together and
    1.4.2 is asked. 6.1.97 carries APAVADA standing and wins — पच + अन्ति
    gives पचन्ति and not पचान्ति. The Kāśikā states the relationship in so
    many words, so this is the grammar's own verdict rather than the
    engine's preference.
    """
    from src.astadhyayi.anga import akah_savarne_dirghah, ato_gune

    def _pair(state: State, fn):
        """
        The first junction where *this rule* applies.

        Written first to return the first junction of any kind, which
        stopped at पच् + अ — where neither rule acts — and never reached
        the अ + अन्ति that needed them. A search that halts on the first
        candidate rather than the first match finds nothing.
        """
        for index in range(len(state.terms) - 1):
            here = state.terms[index]
            if (here.marked and not here.stripped) or not here.text:
                continue
            # Past whatever लुक् emptied — see the note on 6.1.78. The pair
            # is returned as two indices and not one, because the second
            # term is no longer always the next one.
            beyond = [(offset, term)
                      for offset, term in enumerate(state.terms[index + 1:],
                                                    index + 1)
                      if term.text]
            if not beyond:
                continue
            after, nxt = beyond[0]
            if nxt.marked and not nxt.stripped:
                continue
            if fn(here.text[-1], nxt.text[0]).result is not None:
                return index, after, here.text[-1], nxt.text[0]
        return None

    def _rule(sutra, fn, standing, what):
        def matches(state: State) -> bool:
            return _pair(state, fn) is not None

        def perform(state: State) -> State:
            index, second_index, first, second = _pair(state, fn)
            result = fn(first, second).result
            here, nxt = state.terms[index], state.terms[second_index]
            after = state.replace_term(index, here.altered(here.text[:-1]))
            return after.replace_term(
                second_index, nxt.altered(result + nxt.text[1:]))

        return Operational(sutra=sutra, standing=standing, what=what,
                           matches=matches, perform=perform,
                           site=lambda _s: ("ekadesa",))

    return (
        _rule("6.1.101", akah_savarne_dirghah, Strength.EQUAL,
              "अकः सवर्णे दीर्घः — one long vowel for the two"),
        _rule("6.1.97", ato_gune, Strength.APAVADA,
              "अतो गुणे — the later form stands"),
    )


def _yan() -> Operational:
    """
    6.1.77 इको यणचि, contending with 6.1.101 at the same junction.

    Unlike the two एकादेश rules beside it this one does not replace the
    pair with a single sound — the इक् becomes a consonant and the vowel
    after it stands, which is why it cannot share their `perform`. It
    shares their `site`, so 1.4.2 is asked where both reach: for इ + इ
    6.1.101 has the later number and gives दधीन्द्रः; for इ + अ nothing
    else reaches and this gives दध्यत्र.
    """
    from src.astadhyayi.anga import yan_sandhi

    def _target(state: State):
        for index in range(len(state.terms) - 1):
            here = state.terms[index]
            if (here.marked and not here.stripped) or not here.text:
                continue
            beyond = [(offset, term)
                      for offset, term in enumerate(state.terms[index + 1:],
                                                    index + 1)
                      if term.text]
            if not beyond:
                continue
            after, nxt = beyond[0]
            if nxt.marked and not nxt.stripped:
                continue
            found = yan_sandhi(here.text[-1], nxt.text)
            if found.result is not None:
                return index, after, found
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        index, _after, found = _target(state)
        here = state.terms[index]
        return state.replace_term(
            index, here.altered(here.text[:-1] + found.result))

    return Operational(
        sutra="6.1.77", operation="sandhi",
        what="इको यणचि — the इक् becomes its यण्: दध्यत्र",
        matches=matches, perform=perform,
        site=lambda _s: ("ekadesa",))


def _sapo_luk() -> Operational:
    """
    2.4.72 अदिप्रभृतिभ्यः शपः — and the second gaṇa loses the शप् it was
    just given.

    3.1.68 adds it and this takes it away, which looks wasteful and is how
    the grammar works: शप् is added generally and withdrawn where a gaṇa
    says so, rather than 3.1.68 carrying a list of exceptions. The trace
    shows both steps, because both happen.

    The term is emptied rather than removed, so that what was there stays
    visible to 1.1.62 प्रत्ययलोपे प्रत्ययलक्षणम् — an elided affix still
    conditions what it would have conditioned.
    """
    from src.astadhyayi.anga import adiprabhrtibhyah_sapah

    def _target(state: State):
        root = _index_of(state, "dhātu")
        if root is None:
            return None
        # The enunciation, where the caller gave one. 2.4.72 asks which
        # gaṇa the root is read in, and the dhātupāṭha is indexed by the
        # upadeśa: अदिँ (adi̐) is 01.0064 and अदँ (ada̐) is 02.0001, while
        # the stem both leave behind is the one string अद् (ad), read in
        # both. Passing the stem elided शप् for the first as well, so
        # 01.0064 अदिँ बन्धने came out अत्ति (atti) instead of अदति
        # (adati). `adiprabhrtibhyah_sapah` was written to be asked this
        # way — its own docstring says a full upadeśa is looked up
        # exactly — and was simply never given the chance.
        asked = state.terms[root].enunciated or state.terms[root].text
        for index, term in enumerate(state.terms):
            if "śap" not in term.samjnas or "luk-done" in term.samjnas:
                continue
            if not term.text:
                continue
            if adiprabhrtibhyah_sapah(asked).elided:
                return index
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        from dataclasses import replace as _replace
        index = _target(state)
        term = state.terms[index]
        return state.replace_term(index, _replace(
            term, text="", samjnas=term.samjnas | {"luk-done", "luk"}))

    return Operational(
        sutra="2.4.72", operation="luk",
        what="अदिप्रभृतिभ्यः शपः — शप् is elided by लुक्",
        matches=matches, perform=perform,
        site=lambda _s: ("sapo-luk",))


def _term_holding(state: State, offset: int):
    """Which term a character of the surface belongs to, and where in it."""
    seen = 0
    for index, term in enumerate(state.terms):
        if seen <= offset < seen + len(term.text):
            return index, offset - seen
        seen += len(term.text)
    return None


def _hali_ca() -> Operational:
    """8.2.77 हलि च — दीव्यति, सीव्यति, the fourth class's own example."""
    from src.astadhyayi.anga import hali_ca

    def _target(state: State):
        for index, term in enumerate(state.terms):
            if not term.text or (term.marked and not term.stripped):
                continue
            following = _next_affix(state, index)
            if following is None or (following.marked
                                     and not following.stripped):
                continue
            found = hali_ca(term.text, following.text)
            if found.result is not None:
                return index, found
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        index, found = _target(state)
        return state.replace_term(
            index, state.terms[index].altered(found.result))

    return Operational(
        sutra="8.2.77", operation="dīrgha",
        what="हलि च — the इक् उपधा of a र्- or व्-final root lengthens",
        matches=matches, perform=perform,
        site=lambda _s: ("hali",))


def _natva() -> Tuple[Operational, ...]:
    """
    8.4.1 रषाभ्यां नो णः समानपदे and 8.4.2 अट्कुप्वाङ्नुम्व्यवायेऽपि.

    The first rule of the last pāda, and the one every क्रीणाति in the
    language passes through: the ninth class's श्ना puts a न् right after
    a root that ends in र् or ॠ, and this turns it. It is the first rule
    the engine applies **across terms** — the र् of क्री and the न् of
    श्ना are in different pieces of the form, and 8.4.1's समानपदे asks
    only that they be in one *word*, which they are.

    Two sūtras and not one, because the Kāśikā keeps them apart: 8.4.1
    for कुष्णाति where nothing stands between, 8.4.2 for करणम् and
    क्रीणाति where something does. The trace says which.
    """
    from src.astadhyayi.anga import cerebral_n

    def _rule(sutra: str, direct: bool) -> Operational:
        def _target(state: State):
            if any(term.marked and not term.stripped
                   for term in state.terms):
                return None
            found = cerebral_n(state.surface, direct=direct)
            if found.result is None:
                return None
            where = _term_holding(state, found.at)
            return None if where is None else (where, found)

        def matches(state: State) -> bool:
            return _target(state) is not None

        def perform(state: State) -> State:
            (index, offset), _found = _target(state)
            term = state.terms[index]
            return state.replace_term(index, term.altered(
                term.text[:offset] + "ṇ" + term.text[offset + 1:]))

        return Operational(
            sutra=sutra, operation="ṇatva",
            what=("रषाभ्यां नो णः समानपदे — कुष्णाति" if direct else
                  "अट्कुप्वाङ्नुम्व्यवायेऽपि — क्रीणाति, करणम्"),
            matches=matches, perform=perform,
            site=lambda _s: ("natva",))

    return (_rule("8.4.1", True), _rule("8.4.2", False))


def _khari_ca() -> Operational:
    """8.4.55 खरि च — the root's final hardens before the ending."""
    from src.astadhyayi.anga import khari_ca

    def _target(state: State):
        for index in range(len(state.terms) - 1):
            here = state.terms[index]
            if (here.marked and not here.stripped) or not here.text:
                continue
            nxt = next((t for t in state.terms[index + 1:] if t.text), None)
            if nxt is None or (nxt.marked and not nxt.stripped):
                continue
            found = khari_ca(here.text[-1], nxt.text)
            if found.result is not None:
                return index, found
        return None

    def matches(state: State) -> bool:
        return _target(state) is not None

    def perform(state: State) -> State:
        index, found = _target(state)
        term = state.terms[index]
        return state.replace_term(
            index, term.altered(term.text[:-1] + found.result))

    return Operational(
        sutra="8.4.55", operation="car",
        what="खरि च — the झल् becomes its चर्",
        matches=matches, perform=perform,
        site=lambda _s: ("khari",))


def present_tense() -> Tuple[Operational, ...]:
    """
    Everything beyond it-deletion that a लट् form needs.

    It began as the three rules जयति wanted and has grown by working
    backwards from one word at a time, which is why the list reads as it
    does rather than as a section of the grammar.
    """
    return ((_dhatvadeh_rule(), _karta_sap(), _sapo_luk(),)
            + _vikarana_rules() + _nnit_vrddhi()
            + _jha_after_abhyasta()
            + (_juhotyadi_slu(), _dvirvacana(), _snabhyastayor_atah(),
               _i_haly_aghoh(),
               _rudhadi_snam(), _snasor_allopah(),
               _curadi_nic(), _ato_lopah(),
             _jho_antah(),
             _guna_before_affix(), _laghupadha_guna(), _sino_guna(),
             _ato_dirgho(), _ayadi(),
             _thasah_se(), _tit_atmanepada(), _yan()) + _ekadesa()
            + _abhyasa_rules()
            + (_hali_ca(),) + _natva() + _tripadi_hardening()
            + (_khari_ca(),) + _final_visarga())


def verb(root: str, *, ending: str = "", person: int = 0,
         number: int = 0, gana: str = "") -> State:
    """
    A starting state for a present-tense verb: the root and its ending.

    **Which** ending is not chosen here. It used to be — the default was
    तिप्, written in, so every root came out parasmaipada however the
    grammar classified it. एध् is anudāttet and 1.3.12 अनुदात्तङित
    आत्मनेपदम् makes it middle, so एधति was simply wrong — while eighty
    codified sūtras of pada selection sat unconsulted and the engine
    guessed.

    The pada now comes from `atmanepada.pada_of_usage`, which is 1.3.12 to
    1.3.93, and the ending from the tables at 1.4.99–102 rather than from a
    literal here. Pass `ending` to override both, which the tests do when
    they want one particular form.

    The ending carries the names the later rules ask after: सार्वधातुक by
    3.4.113 because it is a तिङ्, कर्तरि because it denotes the agent, and
    ātmanepada where 1.3.12 has said so. None is read off the spelling, and
    none could be.
    """
    from src.astadhyayi.atmanepada import Pada, pada_of_usage
    from src.astadhyayi.vibhakti import (
        ATMANEPADA_ENDINGS, PARASMAIPADA_ENDINGS)

    # Which class the root is read in, for the विकरण rules. Given by the
    # caller where it is known — the dhātupāṭha's code settles it and a
    # root's name does not — and otherwise read off the corpus, but only
    # where the corpus gives ONE answer. जि (ji) is read in the first
    # gaṇa and the tenth, so asked as a bare name it stays unstated and
    # 3.1.68 कर्तरि शप् stands as the उत्सर्ग, which is what it is for.
    if not gana:
        from src.astadhyayi.pada import verbal_gana

        classes = verbal_gana(root)
        gana = next(iter(classes)) if len(classes) == 1 else ""

    names = {"pratyaya", "tiṅ", "sārvadhātuka", "kartari"}
    if ending:
        chosen = ending
    else:
        verdict = pada_of_usage(root)
        middle = getattr(verdict, "pada", None) is Pada.ATMANEPADA
        table = ATMANEPADA_ENDINGS if middle else PARASMAIPADA_ENDINGS
        chosen = table[person][number]
        if middle:
            names.add("ātmanepada")

    return State((
        Term(text=root, role="dhātu", enunciated=root, gana=gana),
        # role="vibhakti", not "pratyaya". 1.4.104 विभक्तिश्च names both
        # सुप् and तिङ् विभक्ति, and 1.3.4 न विभक्तौ तुस्माः then spares a
        # final त-series, स् or म् from being an इत्. Called a plain affix,
        # तस् lost its स् and पचतः came out पचत — and the Kāśikā on 1.3.4
        # cites those very forms, पचतः and पचथः, as what the rule is for.
        Term(text=chosen, role="vibhakti", enunciated=chosen,
             samjnas=frozenset(names)),
    ))


def all_rules() -> Tuple[Operational, ...]:
    """
    Every operational rule the engine has.

    One function, so that the day adhyāya 6 is codified there is a single
    place its rules join the engine and a single count to check against.
    """
    return it_deletion() + present_tense()


def upadesa(form: str, role: str = "dhātu") -> State:
    """A starting state: one term, as the grammar enunciates it."""
    return State((Term(text=form, role=role),))


__all__ = [
    "MARKING", "context_for", "it_deletion", "all_rules", "upadesa",
]
