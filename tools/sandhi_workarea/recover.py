# Replay Write/Edit tool calls from agent transcripts onto a base tree.
import json, glob, os, re, sys, collections
T = "/home/codespace/.claude/projects/-workspaces-codespaces-blank/14581267-db0b-459c-a73b-438634dd89d5/subagents/workflows"
OLD = "/tmp/claude-1000/-workspaces-codespaces-blank/14581267-db0b-459c-a73b-438634dd89d5/scratchpad/"
REPO = "/workspaces/codespaces-blank/VyakaranaBandhu"
OUT = "/workspaces/codespaces-blank/sandhi_work/recovered"

def events(path):
    for line in open(path, encoding="utf-8"):
        try: e = json.loads(line)
        except Exception: continue
        msg = e.get("message", {})
        content = msg.get("content") if isinstance(msg, dict) else None
        if isinstance(content, list):
            for c in content:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    yield c

def relative(fp):
    # ws/<family>/<rest>  -> (family, rest)
    m = re.match(re.escape(OLD) + r"ws/([^/]+)/(.*)$", fp)
    return (m.group(1), m.group(2)) if m else (None, fp.replace(OLD, "SCRATCH/"))

report = []
for wf in sorted(os.listdir(T)):
    for path in sorted(glob.glob(f"{T}/{wf}/agent-*.jsonl")):
        desc = json.load(open(path.replace(".jsonl", ".meta.json"))).get("description", "")
        if not desc.startswith("implement:"):
            continue
        family = desc.split(":")[1]
        state = {}          # rel path -> content
        failed = []
        bash_writes = []
        for c in events(path):
            name, inp = c["name"], c["input"]
            if name == "Write":
                fam, rel = relative(inp["file_path"])
                if fam == family:
                    state[rel] = inp["content"]
            elif name == "Edit":
                fam, rel = relative(inp["file_path"])
                if fam != family: continue
                if rel not in state:
                    base = os.path.join(REPO, rel)
                    if os.path.exists(base):
                        state[rel] = open(base, encoding="utf-8").read()
                    else:
                        failed.append((rel, "no base")); continue
                old, new = inp["old_string"], inp["new_string"]
                if old not in state[rel]:
                    failed.append((rel, "old_string not found: " + old[:60].replace("\n", "\\n"))); continue
                state[rel] = state[rel].replace(old, new) if inp.get("replace_all") else state[rel].replace(old, new, 1)
            elif name == "Bash":
                cmd = inp.get("command", "")
                if re.search(rf"ws/{family}/(src|tests)/[^\s'\"]*\.py", cmd) and re.search(r"sed -i|cat\s*>|tee |open\([^)]*['\"]w|write_text|\.write\(|patch|perl -", cmd):
                    bash_writes.append(cmd[:200].replace("\n", "\\n"))
        for rel, content in state.items():
            dst = os.path.join(OUT, family, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            open(dst, "w", encoding="utf-8").write(content)
        report.append((family, {r: len(c) for r, c in state.items()}, failed, bash_writes))
for family, sizes, failed, bw in report:
    print(f"== {family}")
    for r, n in sizes.items(): print(f"   recovered {r} ({n} chars)")
    for f in failed: print("   EDIT FAILED", f)
    print(f"   {len(bw)} Bash commands that may have modified source files")
    for b in bw[:4]: print("      ", b)
