# -*- coding: utf-8 -*-
"""
Making a codified sūtra runnable from a form.

Every entry in the registry carries an `apply` — the rule as a function. To put
one behind a web form we need to know what it takes, and the functions differ:
some take a string, some three booleans, some a dataclass, some an enum. Rather
than write a form per sūtra, this reads the signature and builds the fields.

Four kinds of parameter are handled, which between them cover everything
codified so far:

    str, bool, int      one field each
    an Enum             a select, with the members as options
    a frozen dataclass  expanded into a field per attribute, so `Adesa` becomes
                        a form-and-its pair and `Context` becomes four flags
    Sequence[str]       a comma-separated field

Anything else makes the spec `runnable=False` with a note saying which
parameter defeated it, rather than producing a form that cannot work. That is
the same discipline the records keep: say what is missing instead of guessing.
"""

from __future__ import annotations

import builtins
import dataclasses
import inspect
import typing
from dataclasses import dataclass, is_dataclass
from enum import Enum
from typing import Any, Dict, List, Optional, Sequence, Tuple

# Importing the rules is what fills the registry — each pāda module calls
# `register` at module level. It has to happen here and not only in report.py,
# because a caller may reach the playground first: a POST to /api/astadhyayi/run
# on a freshly started server did exactly that and found nothing codified.
import src.astadhyayi.rules  # noqa: F401
from src.astadhyayi.sutra import REGISTRY
from src.astadhyayi.fieldhelp import label_and_hint
from src.normalizer import devanagari_to_iast, is_devanagari


@dataclass(frozen=True)
class Field:
    """One input the form should offer."""

    name: str                       # the parameter, or "parent.attribute"
    label: str
    kind: str                       # text | bool | number | select | list
    default: Any = None
    options: Tuple[str, ...] = ()
    positional: bool = False
    group: str = ""                 # set when the field came out of a dataclass
    #: False where the parameter takes a float rather than an int. `kind`
    #: collapses the two into "number", and the collapse was not harmless:
    #: 1.4.109's gap_matras is a half-mātrā interval, and parsing it with
    #: int() threw, so 0.5 became 0 — which still reads as saṃhitā, so the
    #: answer looked right while the rule was asked a different question.
    whole: bool = True
    #: True where the parameter is Optional[...]. It decides what an empty box
    #: means, and the two readings are not close: a rule that asks after the
    #: sense of a root wants `None` for 'not stated' and treats `""` as a
    #: sense that nothing matches. Left flat, every optional condition in the
    #: codification silently fails whenever its box is blank.
    optional: bool = False

    #: One line saying what is being asked for, and naming the Sanskrit term
    #: the parameter stands for. Without it the label is a parameter name
    #: with the underscores taken out — `al vidhi`, `purva vidhi` — which a
    #: reader who needs the form cannot act on, and a reader who could act
    #: on it does not need. See fieldhelp.py.
    hint: str = ""


@dataclass(frozen=True)
class Spec:
    """What a sūtra's rule can be given, and whether a form can give it."""

    sutra_id: str
    function: str
    doc: str
    fields: Tuple[Field, ...] = ()
    runnable: bool = True
    note: str = ""


_SCALARS = {str: "text", bool: "bool", int: "number", float: "number"}


def _unwrap(annotation: Any) -> Any:
    """Strip Optional[...] down to the type inside it."""
    origin = typing.get_origin(annotation)
    if origin is typing.Union:
        args = [a for a in typing.get_args(annotation) if a is not type(None)]
        if len(args) == 1:
            return args[0]
    return annotation


def _is_optional(annotation: Any, raw: Any = None) -> bool:
    """
    Was the parameter declared Optional[...] — that is, may it be None?

    The raw annotation has to be consulted as well as the resolved one. These
    modules use `from __future__ import annotations`, so a signature hands
    back the *string* "Optional[str]"; `_resolve` then finds no such key and
    falls back to the head, giving bare `typing.Optional`, which carries no
    arguments and looks like nothing at all. Reading the text is what catches
    it.
    """
    if typing.get_origin(annotation) is typing.Union:
        return type(None) in typing.get_args(annotation)
    text = str(raw if raw is not None else annotation)
    return text.startswith("Optional[") or "None]" in text or text.endswith(
        "typing.Optional")


def _resolve(annotation: Any, fn) -> Any:
    """
    Turn a string annotation back into the object it names.

    Every module here uses `from __future__ import annotations`, so annotations
    arrive as strings and have to be looked up in the function's own globals.
    """
    if not isinstance(annotation, str):
        return annotation
    text = annotation.strip().strip('"').strip("'")
    if text.startswith("Optional[") and text.endswith("]"):
        text = text[len("Optional["):-1]
    # A forward reference inside Optional keeps its quotes: Optional['Adesa'].
    text = text.strip().strip('"').strip("'")
    namespace = dict(vars(builtins))
    namespace.update(getattr(fn, "__globals__", {}))
    if text in namespace:
        return namespace[text]
    # Sequence[str], Tuple[str, ...] and the like: only the container matters.
    head = text.split("[", 1)[0]
    if head in namespace:
        return namespace[head]
    return annotation


def _fields_for(name: str, annotation: Any, default: Any, fn,
                positional: bool) -> Optional[List[Field]]:
    """The form fields one parameter needs, or None if it cannot have any."""
    resolved = _resolve(annotation, fn)
    optional = _is_optional(resolved, annotation)
    annotation = _unwrap(resolved)

    if annotation in _SCALARS:
        shown, hint = label_and_hint(name)
        # A parameter naming an operation has a closed vocabulary behind it,
        # so it is offered as a list rather than a text box. Typing `dirgha`
        # for `dīrgha` used to return the opposite verdict under a different
        # sūtra; now the spelling cannot be got wrong in the first place.
        if name == "operation" and annotation is str:
            from src.astadhyayi.operations import names as operation_names

            return [Field(name, shown, "select", default or "",
                          ("",) + operation_names(),
                          hint=hint, positional=positional,
                          optional=optional)]
        return [Field(name, shown, _SCALARS[annotation],
                      default, hint=hint, positional=positional,
                      whole=annotation is not float, optional=optional)]

    if isinstance(annotation, type) and issubclass(annotation, Enum):
        shown, hint = label_and_hint(name)
        return [Field(
            name, shown, "select",
            default.value if isinstance(default, Enum) else default,
            tuple(member.value for member in annotation),
            hint=hint, positional=positional,
        )]

    if is_dataclass(annotation):
        import collections.abc

        out = []
        for member in dataclasses.fields(annotation):
            inner = _unwrap(_resolve(member.type, fn))
            container = typing.get_origin(inner) or inner
            if container in (list, tuple, set, frozenset,
                             collections.abc.Sequence, collections.abc.Set):
                # A collection member — Adesa.its is a FrozenSet[str] — needs a
                # list field and a rebuilt container, or a bare string reaches
                # code that expects a set and fails on the first operator.
                kind = "list"
            else:
                kind = _SCALARS.get(inner, "text")
            member_default = (
                member.default
                if member.default is not dataclasses.MISSING else None
            )
            dotted = f"{name}.{member.name}"
            shown, hint = label_and_hint(dotted)
            out.append(Field(
                dotted, shown, kind, member_default, group=name,
                hint=hint, whole=inner is not float,
            ))
        return out

    import collections.abc

    origin = typing.get_origin(annotation) or annotation
    if origin in (list, tuple, frozenset, set, collections.abc.Sequence,
                  collections.abc.Set, typing.Sequence):
        shown, hint = label_and_hint(name)
        return [Field(name, shown, "list", default,
                      hint=hint or "Comma-separated.",
                      optional=optional, positional=positional)]

    if annotation is inspect.Parameter.empty:
        # No annotation at all: treat it as text, which is right for every
        # unannotated parameter in the codification so far.
        shown, hint = label_and_hint(name)
        return [Field(name, shown, "text", default, hint=hint,
                      optional=optional,
                      positional=positional)]
    return None


def spec_for(sutra_id: str) -> Spec:
    """Read a sūtra's rule and say what a form would have to offer."""
    sutra = REGISTRY.get(sutra_id)
    fn = sutra.apply
    if fn is None:
        return Spec(sutra_id, "", "", runnable=False,
                    note="No rule is registered for this sūtra.")

    doc = inspect.getdoc(fn) or ""
    # The reader sees this text in the panel beside the form, so it follows
    # the same rule as every other Sanskrit shown to them: neither script
    # alone. Code tokens and pratyāhāra names are left as they are.
    from src.astadhyayi.glosses import both_scripts
    doc = both_scripts(doc)
    try:
        signature = inspect.signature(fn)
    except (TypeError, ValueError):
        return Spec(sutra_id, getattr(fn, "__name__", "?"), doc,
                    runnable=False, note="Its signature cannot be read.")

    fields: List[Field] = []
    for parameter in signature.parameters.values():
        if parameter.kind in (parameter.VAR_POSITIONAL, parameter.VAR_KEYWORD):
            continue
        positional = parameter.kind in (
            parameter.POSITIONAL_ONLY, parameter.POSITIONAL_OR_KEYWORD
        )
        default = (
            None if parameter.default is inspect.Parameter.empty
            else parameter.default
        )
        built = _fields_for(
            parameter.name, parameter.annotation, default, fn, positional
        )
        if built is None:
            return Spec(
                sutra_id, fn.__name__, doc, tuple(fields), runnable=False,
                note=(
                    f"The parameter {parameter.name!r} takes a "
                    f"{parameter.annotation}, which a form cannot supply. "
                    f"Call the rule directly."
                ),
            )
        fields.extend(built)

    return Spec(sutra_id, fn.__name__, doc, tuple(fields))


# ---------------------------------------------------------------------------
# Running it
# ---------------------------------------------------------------------------



# ---------------------------------------------------------------------------
# Either script
# ---------------------------------------------------------------------------

#: The combining candrabindu the dhātupāṭha loader puts on an anunāsika vowel.
#: `corpus._dhatu_to_iast` explains why it is this and not m̐: 1.3.2 asks
#: whether a *vowel* is anunāsika, and m̐ reads as a consonant.
_CANDRABINDU = "\u0310"

#: What the general transliterator produces for the same mark. It is right for
#: the sūtrapāṭha's ऊँ and सँ, which is why it stays the default there — but a
#: root typed as आसँ has to come out as the dhātupāṭha writes it, or it will
#: not be found.
_ANUSVARA_TILDE = "m\u0310"

_VOWELS = "aāiīuūṛṝḷḹeaioau"


def to_iast(text: str) -> str:
    """
    Whatever the reader typed, in the script the rules are written in.

    Both scripts are accepted everywhere a form takes a word, because there is
    no reason a reader who thinks in Devanāgarī should have to transliterate
    by hand before asking a question. What comes back is echoed in the
    `called` line of the result, so it is always visible what was understood.

    Anything with no Devanāgarī in it is left exactly as it is — a sūtra
    number, a sense-name like `gandhana`, an asserted condition like
    `akarmaka`. Those are not Sanskrit words and must not be touched.
    """
    if not text or not is_devanagari(text):
        return text
    out = devanagari_to_iast(text)
    # आसँ comes back as āsam̐; the dhātupāṭha writes āsa̐, and 1.3.2 is asked
    # of the vowel. Move the mark back onto it.
    while _ANUSVARA_TILDE in out:
        at = out.index(_ANUSVARA_TILDE)
        if at and out[at - 1] in _VOWELS:
            out = out[:at] + _CANDRABINDU + out[at + len(_ANUSVARA_TILDE):]
        else:
            break
    return out


def _signature(fn):
    return inspect.signature(fn)


def _blank_number(field: Field) -> Any:
    """
    What an empty number field means.

    Its own default if it has one. Otherwise `None` where the parameter is
    optional, and only then 0 — a blank Optional[int] arriving as 0 is a
    quiet lie in the echoed call, which says the rule was asked about
    vibhakti 0 when it was asked about nothing. The three earlier coercion
    bugs were all of this shape: a value the form could not express becoming
    a value the signature could.
    """
    if isinstance(field.default, int) and not isinstance(field.default, bool):
        return field.default
    return None if field.optional else 0


def _coerce(field: Field, raw: Any, fn) -> Any:
    if field.kind == "bool":
        return raw in (True, "true", "True", "on", "1", 1)
    if field.kind == "number":
        # A field with no default arrives as "" or the string "None" — a form
        # left blank, or a parameter the signature gives no default for. Both
        # mean nothing was entered.
        text = "" if raw is None else str(raw).strip()
        if text in ("", "None"):
            return _blank_number(field)
        try:
            return int(text) if field.whole else float(text)
        except ValueError:
            return _blank_number(field)
    if field.kind == "list":
        if isinstance(raw, (list, tuple)):
            items = [to_iast(str(item)) for item in raw
                     if str(item).strip() not in ("", "None")]
        elif raw is None or str(raw).strip() in ("", "None"):
            items = []
        else:
            items = [to_iast(part.strip())
                     for part in str(raw).split(",") if part.strip()]
        # An empty list and "nothing was entered" are the same thing to a
        # form and different things to a signature. `str(None)` splitting
        # into ["None"] is how this went wrong: a blank field arrived as a
        # list holding the word None, which then failed every membership
        # test for a reason no reader could see.
        if not items and field.optional and field.default is None:
            return None
        return items
    if field.kind == "select":
        # A select field carries an Enum's *value*, and the parameter wants the
        # member. Handing the string through reaches code that compares with
        # `is` and never matches — 1.1.28's dik-samāsa condition silently
        # failed that way, and the rule reported 1.1.27 instead.
        annotation = _resolve(_signature(fn).parameters[
            field.name.split(".")[0]].annotation, fn)
        annotation = _unwrap(annotation)
        if isinstance(annotation, type) and issubclass(annotation, Enum):
            for member in annotation:
                if member.value == raw or member.name == raw:
                    return member
        return raw
    text = "" if raw is None else str(raw)
    # An absent default round-trips through the form as the literal "None",
    # which is not what anyone typed.
    if text == "None" and field.default is None:
        text = ""
    # And an empty box on an Optional parameter means the condition was not
    # stated. Handing the rule "" instead says it *was* stated, as the empty
    # string, which no condition matches — so the rule silently fails and the
    # answer falls through to whatever the residue clause is. That is how
    # 1.3.66 भुजोऽनवने came out parasmaipada with nothing in the form but its
    # own root.
    if text == "" and field.optional:
        return None
    return to_iast(text)


def _rebuild_members(annotation: Any, members: Dict[str, Any], fn) -> Dict[str, Any]:
    """
    Put a dataclass's collection members back in the container it declares.

    The form hands back a list for every collection field. `Adesa.its` is a
    frozenset and is used with `&`, so a list — or worse a string — would fail
    at the first set operation.
    """
    import collections.abc

    if not is_dataclass(annotation):
        return members
    declared = {f.name: f.type for f in dataclasses.fields(annotation)}
    out = {}
    for key, value in members.items():
        inner = _unwrap(_resolve(declared.get(key), fn))
        container = typing.get_origin(inner) or inner
        if container in (frozenset, collections.abc.Set):
            out[key] = frozenset(value if isinstance(value, (list, tuple, set))
                                 else [value])
        elif container in (set,):
            out[key] = set(value)
        elif container in (tuple, collections.abc.Sequence):
            out[key] = tuple(value)
        elif container is list:
            out[key] = list(value)
        elif isinstance(inner, type) and issubclass(inner, Enum):
            # An enum-typed MEMBER, which the loop above never rebuilt.
            # A top-level parameter goes through `_rebuild_enum`, but a
            # member reached this line as the bare string the form sent
            # and was handed to the rule as one: `Compound.samasa` came
            # in as 'DVIGU' rather than Samasa.DVIGU, so every 2.4 rule
            # that keys on the compound's name silently matched nothing.
            out[key] = _rebuild_enum(inner, value, fn)
        else:
            out[key] = value
    return out


def _rebuild_enum(annotation: Any, value: Any, fn) -> Any:
    annotation = _unwrap(_resolve(annotation, fn))
    if isinstance(annotation, type) and issubclass(annotation, Enum):
        for member in annotation:
            if member.value == value or member.name == value:
                return member
    return value


def jsonable(value: Any) -> Any:
    """A result, in a shape the UI can render without knowing its type."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Enum):
        return value.value
    if is_dataclass(value) and not isinstance(value, type):
        return {
            member.name: jsonable(getattr(value, member.name))
            for member in dataclasses.fields(value)
        }
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set, frozenset)):
        return [jsonable(item) for item in value]
    return str(value)


def run(sutra_id: str, values: Dict[str, Any]) -> Dict[str, Any]:
    """
    Run a sūtra's rule on values from the form.

    Errors are returned rather than raised. A rule refusing its input is
    informative — `scan_phonemes` rejecting a letter that is not a Sanskrit
    sound is the engine doing its job — and the message is worth showing.
    """
    spec = spec_for(sutra_id)
    if not spec.runnable:
        return {"ok": False, "error": spec.note}

    sutra = REGISTRY.get(sutra_id)
    fn = sutra.apply
    signature = inspect.signature(fn)

    positional: List[Any] = []
    keywords: Dict[str, Any] = {}
    groups: Dict[str, Dict[str, Any]] = {}

    for field in spec.fields:
        raw = values.get(field.name, field.default)
        coerced = _coerce(field, raw, fn)
        if field.group:
            groups.setdefault(field.group, {})[field.name.split(".", 1)[1]] = coerced
            continue
        parameter = signature.parameters[field.name]
        coerced = _rebuild_enum(parameter.annotation, coerced, fn)
        if field.positional:
            positional.append(coerced)
        else:
            keywords[field.name] = coerced

    for name, members in groups.items():
        parameter = signature.parameters[name]
        annotation = _unwrap(_resolve(parameter.annotation, fn))
        members = _rebuild_members(annotation, members, fn)
        try:
            built = annotation(**members)
        except Exception as err:            # noqa: BLE001 — reported, not raised
            return {"ok": False, "error": f"{name}: {err}"}
        if parameter.kind in (parameter.POSITIONAL_ONLY,
                              parameter.POSITIONAL_OR_KEYWORD):
            positional.append(built)
        else:
            keywords[name] = built

    try:
        result = fn(*positional, **keywords)
    except Exception as err:                # noqa: BLE001 — reported, not raised
        return {"ok": False, "error": f"{type(err).__name__}: {err}"}

    return {
        "ok": True,
        "result": jsonable(result),
        "empty": result is None or result == () or result == [],
        "called": f"{spec.function}({_call_repr(positional, keywords)})",
    }


def _call_repr(positional: Sequence[Any], keywords: Dict[str, Any]) -> str:
    parts = [repr(value) for value in positional]
    parts += [
        f"{name}={value!r}" for name, value in keywords.items()
        if value not in (None, "", False)
    ]
    return ", ".join(parts)


__all__ = ["Field", "Spec", "jsonable", "run", "spec_for"]
