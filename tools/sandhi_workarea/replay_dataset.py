# Replay the dataset agent's Bash/Write/Edit calls (downloads + normalisation) with remapped paths.
import json, os, re, subprocess, sys, time
SRC = "/home/codespace/.claude/projects/-workspaces-codespaces-blank/14581267-db0b-459c-a73b-438634dd89d5/subagents/agent-a3c9e923538070713.jsonl"
OLD_SCRATCH = "/tmp/claude-1000/-workspaces-codespaces-blank/14581267-db0b-459c-a73b-438634dd89d5/scratchpad"
NEW = "/workspaces/codespaces-blank/sandhi_work"
OLD_REPO = "/workspaces/codespaces-blank/VyakaranaBandhu"
def remap(s):
    return (s.replace(OLD_SCRATCH + "/external_data", NEW + "/external_data")
             .replace(OLD_SCRATCH, NEW + "/scratch_ds")
             .replace(OLD_REPO, NEW + "/repo_ro"))
def calls():
    for line in open(SRC, encoding="utf-8"):
        try: e = json.loads(line)
        except Exception: continue
        msg = e.get("message", {}); content = msg.get("content") if isinstance(msg, dict) else None
        if isinstance(content, list):
            for c in content:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    yield c
os.makedirs(NEW + "/external_data", exist_ok=True); os.makedirs(NEW + "/scratch_ds", exist_ok=True)
STATE = NEW + "/replay_dataset.state"
done = set(int(x) for x in open(STATE).read().split()) if os.path.exists(STATE) else set()
log = open(NEW + "/replay_dataset.log", "a", buffering=1)
ok = fail = 0
for i, c in enumerate(calls()):
    name, inp = c["name"], c["input"]
    if i in done and name == "Bash":
        continue
    try:
        if name == "Write":
            fp = remap(inp["file_path"])
            if not fp.startswith(NEW): continue
            os.makedirs(os.path.dirname(fp), exist_ok=True)
            open(fp, "w", encoding="utf-8").write(remap(inp["content"]))
        elif name == "Edit":
            fp = remap(inp["file_path"])
            if not fp.startswith(NEW) or not os.path.exists(fp): continue
            t = open(fp, encoding="utf-8").read(); o, n = remap(inp["old_string"]), remap(inp["new_string"])
            if o in t:
                open(fp, "w", encoding="utf-8").write(t.replace(o, n) if inp.get("replace_all") else t.replace(o, n, 1))
        elif name == "Bash":
            cmd = remap(inp["command"])
            t0 = time.time()
            r = subprocess.run(["bash", "-c", cmd], capture_output=True, text=True, errors="replace", timeout=1200, cwd=NEW + "/repo_ro")
            ok += r.returncode == 0; fail += r.returncode != 0
            if r.returncode == 0:
                with open(STATE, "a") as st: st.write(f"{i}\n")
            log.write(f"#{i} rc={r.returncode} {time.time()-t0:.0f}s {cmd[:110]!r}\n")
            if r.returncode: log.write("   " + r.stderr[-200:].replace("\n", " | ") + "\n")
    except subprocess.TimeoutExpired:
        fail += 1; log.write(f"#{i} TIMEOUT {inp.get('command','')[:100]!r}\n")
    except Exception as ex:
        fail += 1; log.write(f"#{i} EXC {type(ex).__name__}: {ex}\n")
print(f"dataset replay: {ok} ok, {fail} failed", flush=True)
