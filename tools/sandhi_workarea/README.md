# Sandhi work-area tooling (kept so nothing is lost)

Scripts that lived outside the repo in `/workspaces/codespaces-blank/sandhi_work/`
while the sandhi engine was built by agents in isolated repo copies. They hard-code
that directory (`ws/<family>/`, `repo_ro/`, `external_data/`); edit the paths before
using them elsewhere. **No third-party data is here** (see
`docs/notes/sandhi_datasets_SOURCES.md` and `tools/sandhi_datasets/fetch.sh`).

| file | what |
|---|---|
| `merge_families.py` | copy a family's module + tests from `ws/<family>/` into the repo; dry-run by default, `--apply` to write; core files it reports as DIFFERS are stale copies — never copy them |
| `gold_import.py` | import extracted gold cases into `data/sandhi/gold/` |
| `recover.py`, `replay.py`, `replay_dataset.py` | rebuild files by replaying Write/Edit tool calls from a Claude Code session transcript (`~/.claude/projects/.../*.jsonl`); files written through Bash heredocs are not replayed |
| `workflow_scripts/impl_A.js`, `impl_B.js`, `tier2.js` | the Workflow scripts that ran the implementer agents (generic "continue from what is on disk"); impl_B run id was `wf_89751008-1aa` |
| `ac_ekadesa_audit/` | the ac_ekadesa agent's quote audit (`audit_quotes.py`, `audit1.py`), mutation testing (`mutate.py`), fuzzing (`fuzz.py`), gold adaptation and replay helpers — useful as a model for auditing the other families |

The handover is `docs/notes/sandhi_engine_handover.md`.
