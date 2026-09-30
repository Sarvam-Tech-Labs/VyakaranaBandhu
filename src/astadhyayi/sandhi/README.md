# The sandhi engine

Derives what happens where two words (or two pieces of a word) meet, **one sūtra
at a time**, and says for every step which sūtra of Pāṇini it is, what that
sūtra says (quoted from the corpus, never retyped), what was replaced by what,
and which further sūtras made the operation land where it did.

```python
from src.astadhyayi.sandhi import sandhi

r = sandhi("iti ādi")          # or Devanāgarī: sandhi("इति आदि")
r.surface                      # 'ityādi'
r.surfaces                     # every form the grammar allows (options fork)
print(r.trace())               # the derivation, in both scripts
r.to_dict()                    # the same, for the browser
```

```
python cli.py --sandhi "rāmas ca"
python -m src.astadhyayi.sandhi "rāmas ca"
```

Nothing is looked up. There is no table of junctions. Each step is a sūtra
applied to the form, and every choice the grammar makes is asked of the rule that
makes it, not decided in the loop.

## What it is called on

Words are separated by a space or `+` (two padas in unbroken speech, *saṃhitā*).
Any other separator says what *kind* of junction it is, because the rules ask:

| written | means | the left word is |
|---|---|---|
| `iti ādi`, `iti+ādi` | two padas | pada-final |
| `deva-indra` | first member of a compound | a pada (1.4.14 with 1.1.62) |
| `pra\|ejate` | a preverb and its dhātu | a pada |
| `ne~a` | two pieces of ONE pada (stem \| affix) | **not** pada-final |

A word may carry what its letters cannot say, in braces — `harī{dvivacana} etau`.
Whether an ī is a dual ending decides 1.1.11 and no reading of the letters settles
it, so it is a parameter (NORTH_STAR §5). The closed vocabulary is `dvivacana`,
`adas`, `nipata`, `ang`, `sambuddhi`, `saptamyartha`, `upasarga`, `dhatu[:ROOT]`,
`stem:X`, `arsa`, `pluta`; `infer.py` fills in what a closed class can prove and
records each such assumption as *inferred*, so it is never mistaken for
something the caller said.

**A visarga does not say what it came from.** `रामः` is *rāmas* and `पुनः` is
*punar*, and they part company before a vowel. Write the underlying final where it
matters (`punar atra`); a visarga is read as coming from `s` and the trace says so.

## How it stays faithful — the four things it consults

1. **8.2.1 पूर्वत्रासिद्धम्.** Each sound remembers what it was before the rule
   that made it (`Seg.prior`). A rule is handed a `View` — the row of sounds *as
   that rule, and no other, is entitled to see it* — and visibility is asked of
   `asiddha.visible`, not decided here. This is what gets **वाक्पतिः** (8.2.30 →
   8.2.39 → 8.4.55, no ping-pong), **हर इह** (the loss of a य् does not let
   6.1.87 join the vowels it leaves), and **मनोरथः** right.
2. **वचनप्रामाण्यात्.** A rule whose own wording names the product of a tripādī
   rule — 6.1.113 names the रु of 8.2.66; 6.3.111 names the loss of 8.3.13–14 —
   may see it though 8.2.1 would hide it. It says so, per rule, in
   `Rule.consumes`; take that away and the rule goes blind (there is a test).
3. **Which rule wins.** First the अपवाद relations each rule declares
   (`Rule.overrides`, each with the tradition's reason, quoted); then 8.2.1 again
   (a later tripādī rule cannot contest an earlier one); then 1.4.2
   विप्रतिषेधे परं कार्यम् for what is left. The last two are
   `asiddha.blocks_vipratisedha` and `vipratisedha.vipratisedha`, asked and not
   re-implemented.
4. **Which sound.** 1.1.50 स्थानेऽन्तरतमः via `adesa.antaratama` (with the
   Kāśikā's tie-break by ābhyantara prayatna, `supports.nearest`); 1.1.9 via
   `varna.savarna`; 1.3.10 via `reading.yathasamkhya`; pratyāhāras via
   `sivasutra.resolve`. **No sound is ever tabulated**, and two repository tests
   read every source file to make sure: `test_astadhyayi_no_restating` and the
   guṇa-literal scan in `test_astadhyayi_adesa`.

Options (विभाषा) **fork** the derivation: both courses are correct, so both are
returned, each with its own trace, the option-taken course first.

## What it does not decide

* Where two applications lie in different places the grammar says nothing about
  their order (both hold at once, युगपत्). The leftmost is taken first. That is a
  reading order, stated as one; it changes no result, since the two touch no
  common sound. Where they DO share a sound — a one-sound word between two
  words, *iti a iti* — they contend for it like any two rules that reach one
  place, and 1.4.2 settles them.
* **The insides of the words it is given.** They are finished words, as the
  grammar left them — the च्छ् of *गच्छति* is a च् that 8.4.40 made out of a त्
  long ago, and 8.2.30 must not read it as a च् before a झल्. So the engine acts
  at junctions, and at sounds a step of *this* derivation has made.
* **6.1.85 अन्तादिवत्** is *not* applied to a rule that rests on the sounds
  themselves (वर्णाश्रयविधौ नेष्यते), which is every rule of sandhi. Without that
  the र् of अर् in *महर्षि* is a pada-final र् and 8.3.15 makes it महःषि.
* Meaning. Whether a form is a dual, a vocative, a locative, Vedic: the caller says.

## Writing a rule

A rule is a function of a `View` that yields `Application`s, declared with
`@rule`. Read `families/ac_ekadesa.py` and `families/visarga_ru.py` first; they
are the pattern.

```python
@rule("6.1.88", name="वृद्धिरेचि", families=("ac", "ekadesa"),
      overrides=(("6.1.87", "आद्गुणस्यापवादः (Kāśikā on 6.1.88)"),))
def vrddhir_eci(v: View):
    for j in v.vowel_pairs():                 # never touch v.state directly
        left, right = j.left, j.right
        ...
        yield Application(site=site(left, right),
                          edits=(ekadesa(left, right, *sounds),),
                          detail=Detail(kind=EKADESA, sthanin=..., adesa=...,
                                        nimitta=..., because=..., via=(...)))
```

**The conventions, each one paid for by a failure:**

* **Ask the `View`, never the `State`.** A rule that reads the state sees sounds it
  is not entitled to see, and gets 8.2.1 wrong silently.
* **A rule may not edit what it sees only through its past.** Use the builders
  (`replace`, `ekadesa`, `delete`, `insert_after`, `insert_before`, `remark`); they
  record `Edit.hidden`, and the engine drops such an application. This is not an
  error — the rule already had its chance at that place.
* **Iterate `v.pairs()`, `v.junctions()`, `v.vowel_pairs()` — not `v.live` with
  `v.next()` — when the rule is about two sounds meeting.** `pairs()` skips the
  interior of finished words (see above); a raw `next()` does not, and will
  rewrite `गच्छति`. Rules about a single pada-final sound scan `v.live` and ask
  `v.pada_final(s)` / `v.at_pause(s)`.
* **`site` is every sound the rule read or will change**, named by
  `site(*sights)`. Two applications with a common sound are contending for one
  place; that is what makes 1.4.2 and 8.2.1 the right questions.
* **A refusal is an application with no edits.** 8.4.44 शात् refuses 8.4.40:
  `edits=()`, `kind=PRATISEDHA`, the *same site* as the rule it refuses, and
  `overrides=(("8.4.40", reason),)`. The engine records that neither is offered
  there again. For a vowel junction a prakṛtibhāva rule instead uses `remark(v,
  PRAKRTYA)`, so no other rule touches those vowels afterwards.
* **A loss is an empty sound, not a deletion** (`delete`). Earlier rules still find
  what it replaced; a rule that *names* the loss lists its mark in `consumes`.
* **`consumes`** names the marks a rule may see through 8.2.1 because its own
  wording names them. It is an exception, so it is per-rule and explicit.
* **`overrides`** is a fact the tradition states about a *pair* and carries its
  reason: quote the Kāśikā/Kaumudī/Bhāṣya from the corpus
  (`corpus.commentary_on(id, "kashika")`) — verbatim, checkable.
* **Never write a sūtra's words yourself.** `Via.role` says what the sūtra did *in
  this step*; the trace prints the sūtra's own text from the corpus. (A hand-typed
  quote of 1.1.66 once read निर्देशे for the real निर्दिष्टे.)
* **Explanations** are English with Sanskrit in braces — `{ik}`, `sk("ā")` — and the
  trace prints each in both scripts, देवनागरी (iast). Say what THIS form did, not
  what the rule says in general.
* **Never type a class of sounds.** `S.members("iK")`, `S.is_member(sound, "jhaL")`,
  `sivasutra.resolve`, `varna.VARGA`. Never write a pairing (`i → y`, `c → k`);
  choose with `S.nearest` (1.1.50) or take it from `adesa` / `anga` / `reading`.
  Where `anga.py` already codifies a sūtra as a question (`ato_gune`,
  `akah_savarne_dirghah`, …) *call it*: a notion another rule already decides is
  asked, not redecided.
* **Vārttikas are not Pāṇini.** `@rule(sutra, authority=VARTTIKA,
  varttika="<the text>")` — the base sūtra's id, the vārttika's own words, verbatim
  from `corpus.varttikas_on(...)` or the commentary. The trace labels it.
* **Optional rules** pass `optional="विभाषा"` (or the sūtra's own word) on the
  `Application`. Two kinds differ (1.3.43 against 1.3.50: अप्राप्तविभाषा yields to
  an invariable rule, प्राप्तविभाषा displaces one) — say which in the reason.
* **Semantic and lexical conditions are flags**, read as `v.flags(sight)` /
  `v.word(sight).has("nipata")`, and `SCOPE`-noted where they cannot be computed.

A family module owns its file. It exports `RULES`; `rulebook.py` collects it and
`rulebook.problems()` must stay empty (every cited id must be a sūtra in the
corpus). Each family has `tests/test_sandhi_<family>.py` whose expectations are
**the commentaries' own worked examples and counter-examples**, quoted with
their source, plus the derivation's *steps* wherever the result could come out
right by luck.

## Layout

| file | what it holds |
|---|---|
| `segs.py` | `Seg`, `Word`, `State`; `View` — the row as one rule may see it (8.2.1) |
| `rule.py` | `Rule`, `Application`, `Detail`, `Via`, and the edit builders |
| `engine.py` | the loop: collect, settle (overrides → 8.2.1 → 1.4.2), apply, fork on options |
| `supports.py` | the recurring paribhāṣā sūtras as `Via`s; pratyāhāra membership; `nearest` |
| `parse.py` | Devanāgarī/IAST in; boundary syntax; flags |
| `infer.py` | what a closed class can prove about a word, and why |
| `trace.py` | both scripts, sūtra text from the corpus, JSON |
| `rulebook.py` | the rules of every family, validated against the corpus |
| `families/` | one module per family of rules |

## Tests

`tests/test_sandhi_engine.py` tests the machinery with the derivations the
tradition itself uses to argue about ordering. Family tests are
`tests/test_sandhi_<family>.py`. The suite runs green and its count grows with the
rules.
