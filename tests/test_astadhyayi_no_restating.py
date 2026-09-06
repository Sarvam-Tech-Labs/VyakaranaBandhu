# -*- coding: utf-8 -*-
"""
Nothing the grammar defines once may be defined twice in the code.

The Aṣṭādhyāyī states each thing in one place and refers to it everywhere
after. इक् is fixed by the śivasūtras and 1.1.71; गुण is fixed by 1.1.2; the
ten operations 1.1.58 withholds are fixed by 1.1.58. A rule that needs one of
those does not restate it — it names it, and the naming is what makes the
grammar as short as it is.

The codification is supposed to work the same way, and mostly does. What
makes that checkable is not "does A call B" — plenty of real dependencies are
conditions taken as parameters, or headings, with no function to call. It is
the narrower question this file asks: **is the same set of sounds or words
written out in two different modules?**

That is the form the failure actually takes. It was found by audit before it
was found by a test, and the one real instance was fresh: 6.1.78's एच् had
been written as ("e", "o", "ai", "au") in `anga.py`, four sounds listed by
hand in the very rule whose point is that they are an abbreviation. It now
comes from `sivasutra.resolve("eC")`, which is 1.1.71 doing its job.

What this deliberately does not flag: two collections that share members
without being the same fact. `VARGA["ṭu"]` is the retroflex varga; the keys
of `pada._UNRETROFLEX` are the same five sounds mapped to their dentals.
Same letters, different statements, and only one of them is a definition of
the varga. Reading assignments through `ast` rather than matching text is
what keeps those apart.
"""

from __future__ import annotations

import ast
import collections
import io
import pathlib
import unittest

PACKAGE = pathlib.Path("src/astadhyayi")

#: Collections small enough to be a coincidence rather than a definition.
#: Two modules both mentioning ("a", "i") prove nothing.
LEAST = 3

#: A member longer than this is prose, not a sound or a technical term, and
#: two modules sharing a sentence is a different problem from this one.
LONGEST_MEMBER = 16


def _string_literals(node) -> tuple:
    """The members, if this node is a literal collection of short strings."""
    if not isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        return ()
    members = []
    for element in node.elts:
        if not isinstance(element, ast.Constant):
            return ()
        if not isinstance(element.value, str):
            return ()
        if not element.value or len(element.value) > LONGEST_MEMBER:
            return ()
        members.append(element.value)
    return tuple(members)


def _defined_collections(path: pathlib.Path):
    """Every named assignment of a literal collection of strings."""
    tree = ast.parse(io.open(path, encoding="utf-8").read())
    found = {}
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        value = node.value
        if value is None:
            continue
        # frozenset(("a", "b")) and tuple(...) count as the collection
        if isinstance(value, ast.Call) and value.args:
            value = value.args[0]
        members = _string_literals(value)
        if len(members) < LEAST:
            continue
        targets = ([node.target] if isinstance(node, ast.AnnAssign)
                   else node.targets)
        for target in targets:
            if isinstance(target, ast.Name):
                found[target.id] = frozenset(members)
    return found


class TheSameThingIsNotDefinedTwice(unittest.TestCase):

    def setUp(self):
        self.by_module = {}
        for path in sorted(PACKAGE.rglob("*.py")):
            if "__pycache__" in path.parts:
                continue
            self.by_module[path.name] = _defined_collections(path)
        self.assertGreater(len(self.by_module), 20)

    def test_no_set_of_sounds_or_words_is_written_out_in_two_modules(self):
        where = collections.defaultdict(dict)
        for module, defined in self.by_module.items():
            for name, members in defined.items():
                where[members][module] = name

        clashes = [
            (sorted(members), sorted(f"{m}:{n}" for m, n in seen.items()))
            for members, seen in where.items() if len(seen) > 1
        ]
        self.assertEqual(
            clashes, [],
            "the same collection is defined in more than one module — "
            "one of them should be asking the other:\n"
            + "\n".join(f"  {', '.join(m)[:60]}  →  {s}" for m, s in clashes),
        )

    def test_the_check_can_actually_see_the_definitions(self):
        """
        A scan that found nothing would pass the test above and mean
        nothing at all. It has to be reading real collections.
        """
        total = sum(len(d) for d in self.by_module.values())
        self.assertGreater(total, 25, "the ast scan is not finding much")

    def test_and_it_would_catch_the_one_that_was_there(self):
        """
        6.1.78's एच्, as it was written before the audit. The detector has
        to flag this exact shape or it is not guarding anything.
        """
        import tempfile

        with tempfile.TemporaryDirectory() as folder:
            path = pathlib.Path(folder) / "restated.py"
            path.write_text(
                'EC = ("e", "o", "ai", "au")\n', encoding="utf-8")
            found = _defined_collections(path)
        self.assertEqual(found["EC"], frozenset({"e", "o", "ai", "au"}))

    def test_ec_itself_is_no_longer_written_out(self):
        """
        The fix, asserted directly rather than only through the scan.

        Written first as `assertNotIn('("e", "o", "ai", "au")', source)`,
        which failed — the tuple is still in `anga.py`, inside the docstring
        that explains why it is no longer a definition. Text-matching cannot
        tell a definition from prose about a definition, which is the whole
        reason the rest of this file reads assignments through `ast`. The
        test had the defect it was written to guard against.
        """
        from src.astadhyayi.anga import ec

        defined = _defined_collections(PACKAGE / "anga.py")
        self.assertNotIn(frozenset({"e", "o", "ai", "au"}), defined.values())
        self.assertEqual(ec(), ("e", "o", "ai", "au"))

    def test_the_varga_and_the_retroflex_map_are_not_treated_as_a_clash(self):
        """
        The false positive the text-matching version produced. Both name
        the five retroflex stops; only one of them is defining the varga.
        A dict is not a definition of its keys.
        """
        from src.astadhyayi.varna import VARGA

        retroflex = frozenset(VARGA["ṭu"])
        pada = self.by_module.get("pada.py", {})
        self.assertNotIn(
            retroflex, set(pada.values()),
            "pada.py is being read as defining the ṭu varga, which it is "
            "not — it maps those sounds to their dentals",
        )


if __name__ == "__main__":
    unittest.main()
