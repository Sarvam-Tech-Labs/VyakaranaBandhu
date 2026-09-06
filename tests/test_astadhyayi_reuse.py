# -*- coding: utf-8 -*-
"""
Declared reuse — `reuses=` on a registered sūtra — and whether it holds.

The graph beside each sūtra shows what it hangs on. The question that
matters is whether those connections exist in the *code*: if 7.3.84 depends
on 1.1.3, then 7.3.84's implementation should obtain the ik vowels from
1.1.3 rather than carry its own copy.

Inferring that automatically does not work, and three attempts proved it.
A scan of the function body misses reuse that happens when a module-level
constant is built — 1.1.1's set is `sound_class("ā", "aiC")`, and
`is_vrddhi` is then a bare membership test with nothing in it. Widening to
the whole module credits anything that merely shares a file: it had
`guna_vrddhi_blocked` reusing `guna_of`, which it never calls. Narrowing
again loses the first case. Each version gave a different answer and each
was wrong.

So the dependency is **declared**, by someone who has read the code, and
this file checks the part that is decidable: the cited sūtra is codified,
and its implementation is genuinely reachable — through the function,
through what the function calls, or through the imports of the module the
function lives in. Remove the call and this goes red.

What it deliberately does not do is require a declaration on every edge.
Most textual dependencies are not calls: 6.1.77's *aci* descends into
6.1.78 as a condition the caller states, and 6.4.1 *aṅgasya* is a heading.
`reuses` is for the ones where one rule's code genuinely runs another's.
"""

from __future__ import annotations

import inspect
import re
import sys
import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.sutra import REGISTRY

SUTRA_IN_DOC = re.compile(r"\b([1-8]\.[1-4]\.\d{1,3})\b")


def _source(obj) -> str:
    try:
        return inspect.getsource(obj)
    except (OSError, TypeError):
        return ""


def _names_for(sutra_id: str) -> set:
    """Every callable in the package that claims to implement this sūtra."""
    names = set()
    if REGISTRY.has(sutra_id):
        fn = REGISTRY.get(sutra_id).apply
        if fn is not None:
            names.add(getattr(fn, "__name__", ""))
    for module_name, module in list(sys.modules.items()):
        if not module_name.startswith("src.astadhyayi"):
            continue
        for attr in dir(module):
            obj = getattr(module, attr, None)
            if not callable(obj):
                continue
            if not getattr(obj, "__module__", "").startswith("src.astadhyayi"):
                continue
            if sutra_id in SUTRA_IN_DOC.findall(
                    (inspect.getdoc(obj) or "")[:600]):
                names.add(attr)
    return {n for n in names if n}


def _reach(sutra_id: str, depth: int = 2) -> str:
    """
    The function, what it calls, and its module's import lines.

    The imports are included and the module body is not. That is the line
    between the two failures: a module-level `from … import sound_class`
    is how construction-time reuse shows up, while the rest of a shared
    file is just neighbours.
    """
    fn = REGISTRY.get(sutra_id).apply
    if fn is None:
        return ""
    text, seen, frontier = [], set(), [fn]
    module = sys.modules.get(getattr(fn, "__module__", "") or "")
    if module is not None:
        whole = _source(module)
        text.extend(line for line in whole.splitlines()
                    if line.startswith(("import ", "from ")) or
                    re.match(r"^[A-Z_]+[A-Z0-9_]*(\s*:.*)?\s*=", line))
    for _ in range(depth):
        following = []
        for func in frontier:
            key = getattr(func, "__qualname__", str(func))
            if key in seen:
                continue
            seen.add(key)
            body = _source(func)
            text.append(body)
            own = sys.modules.get(getattr(func, "__module__", "") or "")
            if own is None:
                continue
            for called in set(re.findall(r"\b([a-z_][a-z0-9_]{2,})\s*\(",
                                         body)):
                other = getattr(own, called, None)
                if callable(other) and getattr(
                        other, "__module__", "").startswith("src.astadhyayi"):
                    following.append(other)
        frontier = following
    return "\n".join(text)


class EveryDeclaredReuseHolds(unittest.TestCase):

    def setUp(self):
        self.declared = [
            (str(s.id), other)
            for s in REGISTRY.all() for other in s.reuses
        ]
        self.assertTrue(self.declared, "nothing declares reuse yet")

    def test_the_cited_sutra_is_itself_codified(self):
        for sutra_id, other in self.declared:
            with self.subTest(sutra=sutra_id, reuses=other):
                self.assertTrue(
                    REGISTRY.has(other),
                    f"{sutra_id} says it reuses {other}, which is not "
                    f"codified — nothing to reuse")

    def test_the_implementation_is_actually_reachable(self):
        for sutra_id, other in self.declared:
            names = _names_for(other)
            with self.subTest(sutra=sutra_id, reuses=other):
                self.assertTrue(names, f"nothing implements {other}")
                source = _reach(sutra_id)
                hit = [n for n in names
                       if re.search(r"\b" + re.escape(n) + r"\b", source)]
                self.assertTrue(
                    hit,
                    f"{sutra_id} declares it reuses {other} and reaches "
                    f"none of {sorted(names)[:6]} — either the call went "
                    f"away or the declaration was wrong")

    def test_two_sutras_sharing_one_function_do_not_declare_reuse(self):
        """
        Where a block is codified as one resolver over a table — the nine
        pragṛhya sūtras, the ten sarvanāman ones — `reuses` has nothing to
        say. The two are not calling each other; they are the same code, and
        the reachability check above cannot fail for them: everything either
        one does is trivially reachable from the other.

        That is not a hypothetical. 1.1.15 declared it reused 1.1.14, and the
        check passed, and it was wrong — 1.1.15's branch is
        `if nipata and final == "o"` and never touches `_is_single_vowel`.
        The निपात the Kāśikā reads down from 1.1.14 is real in the text, but
        in the code it is one parameter that two branches read, which is
        already as shared as it can be.
        """
        for sutra_id, other in self.declared:
            with self.subTest(sutra=sutra_id, reuses=other):
                if not REGISTRY.has(other):
                    continue
                self.assertIsNot(
                    REGISTRY.get(sutra_id).apply, REGISTRY.get(other).apply,
                    f"{sutra_id} and {other} are the same function, so the "
                    f"declaration asserts nothing and the reachability check "
                    f"cannot fail — drop it")

    def test_a_rule_does_not_declare_itself(self):
        for sutra_id, other in self.declared:
            with self.subTest(sutra=sutra_id):
                self.assertNotEqual(sutra_id, other)


class TheFirstSixAreVerified(unittest.TestCase):
    """
    1.1.1 to 1.1.6, checked by reading rather than by the tool — which had
    called all six of them gaps.
    """

    def test_the_three_sound_classes_come_from_the_sivasutras(self):
        """
        None of 1.1.1, 1.1.2, 1.1.3 lists its vowels. Each names a
        pratyāhāra and lets 1.1.71 resolve it.
        """
        for sutra_id in ("1.1.1", "1.1.2", "1.1.3"):
            with self.subTest(sutra=sutra_id):
                self.assertIn("1.1.71", REGISTRY.get(sutra_id).reuses)

    def test_and_the_sets_they_produce_are_right(self):
        from src.astadhyayi.rules.adhyaya_1_pada_1 import GUNA, IK, VRDDHI

        self.assertEqual(VRDDHI, ("ā", "ai", "au"))
        self.assertEqual(GUNA, ("a", "e", "o"))
        self.assertEqual(set(IK), {"i", "u", "ṛ", "ḷ"})

    def test_the_pragrhya_block_is_one_resolver(self):
        """
        1.1.11 to 1.1.19 are nine table rows behind one function. The point
        of recording it is that the block is DRY by construction — and that
        no `reuses` declaration among them would mean anything.
        """
        applies = {REGISTRY.get(f"1.1.{n}").apply for n in range(11, 20)}
        self.assertEqual(len(applies), 1)
        for n in range(11, 20):
            with self.subTest(sutra=f"1.1.{n}"):
                self.assertEqual(REGISTRY.get(f"1.1.{n}").reuses, ())

    def test_the_three_prohibitions_ask_1_1_3(self):
        """
        1.1.4, 1.1.5 and 1.1.6 all carry इकः down, and all three honour it
        — इक इत्येव, as the Kāśikā says under each. They call `is_ik`.
        """
        for sutra_id in ("1.1.4", "1.1.5", "1.1.6"):
            with self.subTest(sutra=sutra_id):
                self.assertIn("1.1.3", REGISTRY.get(sutra_id).reuses)

    def test_and_a_target_outside_ik_is_not_blocked(self):
        """The behaviour that declaration stands for."""
        from src.astadhyayi.adesa import Adesa
        from src.astadhyayi.rules.adhyaya_1_pada_1 import guna_vrddhi_blocked

        kit = Adesa(form="ktvā", its=frozenset({"k"}))
        self.assertIsNotNone(
            guna_vrddhi_blocked("ū", affix=kit, ardhadhatuka=True))
        for outside in ("a", "e", "ā"):
            with self.subTest(target=outside):
                self.assertIsNone(
                    guna_vrddhi_blocked(outside, affix=kit,
                                        ardhadhatuka=True))


class SomeReuseIsDeliberatelyAbsent(unittest.TestCase):
    """
    The walk's other product. Most candidates it raised were citations —
    a docstring naming a sūtra as its example, which is not a call. But a
    few are rules that could plausibly have called another and must not,
    and those are worth holding, because the next person to notice the
    near-duplication will be tempted to collapse it.
    """

    def test_1_3_9_drops_the_whole_it_and_not_its_last_sound(self):
        """
        तस्यग्रहणं सर्वलोपार्थम्, अलोऽन्त्यस्य मा भूत् — the word तस्य is in
        1.3.9 precisely so that 1.1.52 does NOT cut the deletion down to the
        final sound. डुकृञ् gives कृ: the ḍu goes entire.

        Had 1.3.9 been routed through `replace_antya` — which is what the
        rest of this file spends its time encouraging — डुकृञ् would keep
        its ḍ and the root would come out wrong.
        """
        from src.astadhyayi.adesa import replace_antya
        from src.astadhyayi.itsamjna import DHATU, analyze, lopa

        self.assertEqual(analyze("ḍukṛñ", DHATU).stem, "kṛ")

        marks = sorted(analyze("ḍukṛñ", DHATU).its, key=lambda m: m.start)
        first = marks[0]
        self.assertEqual("ḍukṛñ"[first.start:first.end], "ḍu",
                         "the it is the two-letter ḍu, not the u alone")

        # What 1.1.52 would have done to that same span, for contrast.
        self.assertNotEqual(replace_antya("ḍu", ""), "",
                            "अलोऽन्त्यस्य removes one sound and would leave ḍ")
        self.assertEqual(lopa("ḍukṛñ", marks), "kṛ")

    def test_1_1_70_and_1_2_27_are_one_answer_not_two_that_agree(self):
        """
        `grahana.kala` and `svara.duration` were identical line for line,
        kept honest by a test that they matched. Now 1.1.70 asks 1.2.27.
        """
        import inspect

        from src.astadhyayi.grahana import kala

        self.assertIn("duration", inspect.getsource(kala))
        self.assertIn("1.2.27", REGISTRY.get("1.1.70").reuses)


if __name__ == "__main__":
    unittest.main()
