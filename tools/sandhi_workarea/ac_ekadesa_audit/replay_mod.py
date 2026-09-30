# Replays the module- and test-modifying steps of the original implementer agent
# (transcript wf_9af0c39b) onto a bare sandbox, to recover what its Bash
# appends/patches did that recover.py (Write/Edit only) missed.
import json, os, re, subprocess, sys
calls = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "orig_calls.json")))
SB = sys.argv[1]
MOD = "src/astadhyayi/sandhi/families/ac_ekadesa.py"
TST = "tests/test_sandhi_ac_ekadesa.py"
for rel in (MOD, TST):
    os.makedirs(os.path.dirname(os.path.join(SB, rel)), exist_ok=True)
MODS = {72, 74, 75, 76, 77, 79, 80, 81, 85, 87, 97, 106}
TSTS = {89, 98, 99, 100, 107, 108}
def heredoc(cmd, marker):
    m = re.search(r"<<'%s'\n" % marker, cmd)
    start = m.end()
    end = cmd.index("\n%s\n" % marker, start) if ("\n%s\n" % marker) in cmd[start:] + "\n" and cmd.find("\n%s\n" % marker, start) != -1 else cmd.index("\n%s" % marker, start)
    return cmd[start:end] + "\n"
for i, c in enumerate(calls, 1):
    if i not in MODS | TSTS: continue
    inp = c["input"]
    if c["name"] == "Write":
        rel = TST if "/tests/" in inp["file_path"] else MOD
        open(os.path.join(SB, rel), "w", encoding="utf-8").write(inp["content"])
        print(i, "Write", rel); continue
    cmd = inp["command"]
    if i == 79:
        p = os.path.join(SB, MOD)
        s = open(p, encoding="utf-8").read()
        old = '_varttika("6.1.89", "अक्षादूहिन्याम्")'; new = '_varttika("6.1.89", "अक्षादूहिन्या")'
        assert old in s; open(p, "w", encoding="utf-8").write(s.replace(old, new)); print(i, "sed"); continue
    if "cat >> " in cmd:
        m = re.search(r"cat >> (\S+) <<'PYEOF'\n", cmd)
        body_start = m.end(); body_end = cmd.index("\nPYEOF", body_start)
        with open(os.path.join(SB, m.group(1)), "a", encoding="utf-8") as f:
            f.write(cmd[body_start:body_end] + "\n")
        print(i, "append", m.group(1), body_end - body_start); continue
    code = heredoc(cmd, "EOF")
    r = subprocess.run([sys.executable, "-c", code], cwd=SB, capture_output=True, text=True)
    print(i, "patch", "rc", r.returncode, r.stderr[-300:])
    assert r.returncode == 0, (i, r.stderr)
