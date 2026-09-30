# Mutation sweep: each mutant breaks one condition of the module; the tests must notice.
# Run from the workspace root:  python3 .work/mutate.py  (restores the module on exit).
import re, subprocess, sys, shutil
P = "src/astadhyayi/sandhi/families/ac_ekadesa.py"
BAK = ".work/ac_ekadesa.py.bak"
shutil.copyfile(P, BAK)
orig = open(P, encoding="utf-8").read()
MUTS = [
 ("6.1.87 avarna unchecked", "        if left.s not in AVARNA:\n            continue\n        sub = guna_of", "        sub = guna_of"),
 ("6.1.88 eC unchecked", "if left.s not in AVARNA or right.s not in eC:", "if left.s not in AVARNA:"),
 ("6.1.89 any root is eti", '        if root in ("i", "iṇ"):\n            return "eti"', '        if True:\n            return "eti"'),
 ("6.1.89 uth unchecked", 'if _is_uth(word) and right.s == "ū":', 'if right.s == "ū":'),
 ("6.1.89 no declaration vs 6.1.94", '("6.1.94", _quote("kashika", "6.1.89", "एत्येधत्योस्त्वेङिपररूपापवादः")),', ''),
 ("6.1.90 aat unchecked", "or not v.word(left).has(F_AAT):", "or False:"),
 ("6.1.91 upasarga unchecked", "return j.left.s in AVARNA and _rt(j.right.s) and _upasarga_dhatu(v, j)", "return j.left.s in AVARNA and _rt(j.right.s)"),
 ("6.1.91 long r allowed", "return sound in RVARNA and kala(sound) == kala(\"a\")", "return sound in RVARNA"),
 ("6.1.92 not optional", 'yield _step(\n            left, right, sounds, optional="वा",\n            via=_base([*_upasarga_via(v, j), S.tapara(right.s), *via]),', 'yield _step(\n            left, right, sounds, optional="",\n            via=_base([*_upasarga_via(v, j), S.tapara(right.s), *via]),'),
 ("6.1.93 any vowel before a", 'if left.s != "o" or right.s != "a":', 'if right.s != "a":'),
 ("6.1.93 ending unchecked", "if name not in _AM_SAS:", "if False:"),
 ("6.1.94 eng unchecked", "if left.s not in AVARNA or right.s not in eng or not _upasarga_dhatu(v, j):", "if left.s not in AVARNA or not _upasarga_dhatu(v, j):"),
 ("6.1.94 upasarga unchecked", "if left.s not in AVARNA or right.s not in eng or not _upasarga_dhatu(v, j):", "if left.s not in AVARNA or right.s not in eng:"),
 ("6.1.94 vartika eva unchecked", "or not v.word(right).has(F_ANIYOGA)):", "or False):"),
 ("6.1.94 otu needs samasa", "or j.kind != SAMASA or right.s not in S.members(\"eṄ\")", "or right.s not in S.members(\"eṄ\")"),
 ("6.1.95 om needs nipata", 'if v.begins_word(right) and word.has(F_NIPATA) and _bare(word) in _OM:', 'if v.begins_word(right) and _bare(word) in _OM:'),
 ("6.1.95 ang ignores lw", "    for index in sorted(_idx(right.seg)):", "    for index in [right.w]:"),
 ("6.1.95 no declaration vs 6.1.101", '("6.1.101", _quote("kashika", "6.1.95", "अकः सवर्णे दीर्घत्वं बाधते"))', '("6.1.88", _quote("kashika", "6.1.95", "वृद्धिरेचि इत्यस्यापवादः"))'),
 ("6.1.96 padanta allowed", "if left.s not in AVARNA or v.pada_final(left):\n            continue\n        if right.s != \"u\"", "if left.s not in AVARNA:\n            continue\n        if right.s != \"u\""),
 ("6.1.96 s unchecked", 'if after is None or after.s != "s" or after.w != right.w:', 'if after is None:'),
 ("6.1.97 padanta allowed", "if v.pada_final(left) or ato_gune(left.s, right.s).result is None:", "if ato_gune(left.s, right.s).result is None:"),
 ("6.1.97 no declaration vs 6.1.101", '("6.1.101", _quote("kashika", "6.1.97", "अकः सवर्णे दीर्घस्य अपवादः")),', ''),
 ("6.1.98 avyakta unchecked", "    if not v.word(t).has(F_AVYAKTA):\n        return None\n    a = v.prev(t)", "    a = v.prev(t)"),
 ("6.1.98 iti unchecked", '    if t.s != "t" or i.s != "i" or not v.ends_word(t) or not _named(v, i, "iti"):', '    if t.s != "t" or i.s != "i" or not v.ends_word(t):'),
 ("6.1.98 amredita allowed", "        if a is None or v.word(j.left).has(F_AMREDITA):\n            continue\n        t, i = j.left, j.right\n        yield _step(\n            t, i, _para(t, i), first=a,", "        if a is None:\n            continue\n        t, i = j.left, j.right\n        yield _step(\n            t, i, _para(t, i), first=a,"),
 ("6.1.98 whole at not covered", "t, i, _para(t, i), first=a, adesa", "t, i, _para(t, i), adesa"),
 ("6.1.99 not optional", 't, i, _para(t, i), optional="वा", adesa=f"{i.s} (pararūpa)", via=_base(),', 't, i, _para(t, i), optional="", adesa=f"{i.s} (pararūpa)", via=_base(),'),
 ("6.1.100 dac unchecked", "if not (word.has(F_AMREDITA) and word.has(F_DAC)):", "if not word.has(F_AMREDITA):"),
 ("6.1.101 aK unchecked", 'if not S.is_member(left.s, "aK"):\n            continue\n        sub = _dirgha(left.s, right.s)', 'sub = _dirgha(left.s, right.s)'),
 ("6.1.101 vartika r not optional", 'left, right, (NewSeg(sound, frozenset({DVIMATRA})),), optional="वा",', 'left, right, (NewSeg(sound, frozenset({DVIMATRA})),), optional="",'),
 ("6.1.102 all cases", "return name if name in _first_two_cases() else None", "return name"),
 ("6.1.102 ignores 104 mark", "if not S.is_member(left.s, \"aK\") or NO_PURVASAVARNA in left.marks:", "if not S.is_member(left.s, \"aK\"):"),
 ("6.1.103 pum unchecked", "if not v.state.words[before.seg.lw].has(F_PUM):", "if False:"),
 ("6.1.103 any ending", 'if _ending_of(v.word(s)) != "śas" or before.seg.lw is None:', 'if before.seg.lw is None:'),
 ("6.1.104 iC unchecked", "if name is None or left.s not in AVARNA or right.s not in S.members(\"iC\"):", "if name is None or left.s not in AVARNA:"),
 ("6.1.105 short allowed", 'if name is None or kala(left.s) != kala("ā"):\n            continue\n        if not (name == "jas" or right.s in S.members("iC")):\n            continue\n        yield _refuse(', 'if name is None:\n            continue\n        if not (name == "jas" or right.s in S.members("iC")):\n            continue\n        yield _refuse('),
 ("6.1.106 classical too", '@rule("6.1.106", name=_name("6.1.106"), families=FAMILIES, vedic=True,', '@rule("6.1.106", name=_name("6.1.106"), families=FAMILIES, vedic=False,'),
 ("6.1.107 ending unchecked", 'if not S.is_member(left.s, "aK") or right.s != "a" or _sup(v, right) != "am":', 'if not S.is_member(left.s, "aK") or right.s != "a":'),
 ("6.1.108 flag unchecked", "if (not v.word(left).has(F_SAMPRASARANA) or not v.ends_word(left)", "if (False or not v.ends_word(left)"),
 ("6.1.109 padanta unchecked", "if left.s not in eng or not v.pada_final(left):\n            continue\n        if right.s != \"a\":", "if left.s not in eng:\n            continue\n        if right.s != \"a\":"),
 ("6.1.109 no declaration vs 6.1.78", '("6.1.78", _quote("kashika", "6.1.109", "अयवादेशयोरयमपवादः"))', '("6.1.77", _quote("kashika", "6.1.109", "अयवादेशयोरयमपवादः"))'),
 ("6.1.110 ending unchecked", 'if left.s not in eng or right.s != "a" or _sup(v, right) not in _NGASI_NGAS:\n            continue\n        name = _sup(v, right)\n        yield _step(\n            left, right, _purva(left)', 'if left.s not in eng or right.s != "a":\n            continue\n        name = _sup(v, right) or "ṅas"\n        yield _step(\n            left, right, _purva(left)'),
 ("6.1.111 raparatva dropped", "sounds = _sounds(raparatva(left.s, \"u\"))", "sounds = (\"u\",)"),
 ("6.1.112 y not from 6.1.77", 'if y.s != "y" or y.seg.made_by != "6.1.77" or a.s != "a":', 'if y.s != "y" or a.s != "a":'),
 ("6.1.112 any consonant", 'before.s not in _before_y()', 'before.s in ("",)'),
 ("6.1.94 sakandhvadi list unchecked", "        found = _sakandhvadi_entry(joined)\n        if found is None:\n            continue", "        found = _sakandhvadi_entry(joined) or ((), 0)"),
]
MUTS += [
 ("6.1.89 uth route ignores lw", "        for index in sorted(_idx(right.seg)))", "        for index in [right.w])"),
 ("6.1.108 uth is not a samprasarana", "    return word.has(F_SAMPRASARANA) or _is_uth(word)", "    return word.has(F_SAMPRASARANA)"),
 ("6.1.89 uth unchecked (through lw)", "_is_uth(v.state.words[index]) and _begins(v, right, index)", "_begins(v, right, index)"),
 ("6.1.108 flag unchecked (now)", "if (not _samprasarana(v.word(left)) or not v.ends_word(left)", "if (False or not v.ends_word(left)"),
 ("6.1.103 ending via stem: dropped", "    stem = word.flag_value(\"stem\")\n    return stem if stem in SUP else None", "    return None"),
]
ONLY = sys.argv[1:]
if ONLY:
    MUTS = [m for m in MUTS if any(o in m[0] for o in ONLY)]
res = []
try:
    for name, old, new in MUTS:
        if old not in orig:
            res.append((name, "NOT APPLICABLE (pattern not found)")); continue
        open(P, "w", encoding="utf-8").write(orig.replace(old, new, 1))
        r = subprocess.run([sys.executable, "-m", "unittest", "tests.test_sandhi_ac_ekadesa"], capture_output=True, text=True)
        failed = len(re.findall(r"^(FAIL|ERROR):", r.stderr, flags=re.M))
        res.append((name, "killed by %d tests" % failed if failed else "SURVIVED"))
        print(res[-1], flush=True)
finally:
    shutil.copyfile(BAK, P)
print("---")
for n, v in res:
    if "killed" not in v: print(n, v)
print(len([1 for _, v in res if "killed" in v]), "killed of", len(res))
