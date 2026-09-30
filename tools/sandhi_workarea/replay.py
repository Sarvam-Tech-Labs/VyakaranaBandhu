# Replay an agent transcript's Write/Edit/Bash calls in a sandbox with remapped paths.
import json, glob, os, re, subprocess, sys, time
T = "/home/codespace/.claude/projects/-workspaces-codespaces-blank/14581267-db0b-459c-a73b-438634dd89d5/subagents/workflows/wf_bf58bc65-dee"
OLD_SCRATCH = "/tmp/claude-1000/-workspaces-codespaces-blank/14581267-db0b-459c-a73b-438634dd89d5/scratchpad"
NEW_SCRATCH = "/workspaces/codespaces-blank/sandhi_work/scratch"
OLD_REPO = "/workspaces/codespaces-blank/VyakaranaBandhu"
NEW_REPO = "/workspaces/codespaces-blank/sandhi_work/repo_ro"

def remap(s):
    return s.replace(OLD_SCRATCH, NEW_SCRATCH).replace(OLD_REPO, NEW_REPO)

def calls(path):
    for line in open(path, encoding="utf-8"):
        try: e = json.loads(line)
        except Exception: continue
        msg = e.get("message", {}); content = msg.get("content") if isinstance(msg, dict) else None
        if isinstance(content, list):
            for c in content:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    yield c

def replay(family, log):
    path = next(p for p in glob.glob(f"{T}/agent-*.jsonl")
                if json.load(open(p.replace(".jsonl", ".meta.json")))["description"] == f"extract:{family}")
    n_ok = n_fail = 0
    for c in calls(path):
        name, inp = c["name"], c["input"]
        try:
            if name == "Write":
                fp = remap(inp["file_path"])
                if not fp.startswith(NEW_SCRATCH): continue
                os.makedirs(os.path.dirname(fp), exist_ok=True)
                open(fp, "w", encoding="utf-8").write(remap(inp["content"]))
            elif name == "Edit":
                fp = remap(inp["file_path"])
                if not fp.startswith(NEW_SCRATCH) or not os.path.exists(fp): continue
                txt = open(fp, encoding="utf-8").read()
                old, new = remap(inp["old_string"]), remap(inp["new_string"])
                if old in txt:
                    txt = txt.replace(old, new) if inp.get("replace_all") else txt.replace(old, new, 1)
                    open(fp, "w", encoding="utf-8").write(txt)
            elif name == "Bash":
                cmd = remap(inp["command"])
                r = subprocess.run(["bash", "-c", cmd], capture_output=True, text=True, errors='replace', timeout=300,
                                   cwd=NEW_REPO)
                if r.returncode == 0: n_ok += 1
                else:
                    n_fail += 1
                    log.write(f"[{family}] rc={r.returncode}: {cmd[:120]!r}\n  {r.stderr[-200:]!r}\n")
        except subprocess.TimeoutExpired:
            n_fail += 1; log.write(f"[{family}] TIMEOUT {inp.get('command','')[:100]!r}\n")
        except Exception as ex:
            n_fail += 1; log.write(f"[{family}] EXC {type(ex).__name__}: {ex}\n")
    return n_ok, n_fail

if __name__ == "__main__":
    with open("replay.log", "a", buffering=1) as log:
        for fam in sys.argv[1:]:
            t = time.time()
            ok, fail = replay(fam, log)
            print(f"{fam}: {ok} commands ok, {fail} failed, {time.time()-t:.0f}s", flush=True)
