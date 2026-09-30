# -*- coding: utf-8 -*-
"""Extract assert_has_sandhi(first, second, &[results]) cases from vidyut-prakriya/tests/integration/kashika_*.rs (MIT)."""
import sys, os, re, json, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from qc import qc_dataset

BASE = RAW + '/ambuda-org_vidyut/vidyut-prakriya/tests/integration'
COMMIT = '8da2f90bee3ce1c07505fa432fc3729e3f7e02ea'
URLB = 'https://github.com/ambuda-org/vidyut/blob/%s/vidyut-prakriya/tests/integration/' % COMMIT
LIC = 'MIT (ambuda-org/vidyut, Cargo.toml license = "MIT")'
ds = 'vidyut-kashika-sandhi'
STR = re.compile(r'"((?:[^"\\]|\\.)*)"')


def find_calls(text):
    out = []
    for m in re.finditer(r'assert_has_sandhi\s*\(', text):
        i = m.end()
        depth = 1
        j = i
        instr = False
        while j < len(text) and depth > 0:
            ch = text[j]
            if instr:
                if ch == '\\':
                    j += 1
                elif ch == '"':
                    instr = False
            else:
                if ch == '"':
                    instr = True
                elif ch == '(':
                    depth += 1
                elif ch == ')':
                    depth -= 1
            j += 1
        args = text[i:j - 1]
        out.append((m.start(), args))
    return out


rows, dropped = [], collections.Counter()
rejected = []
per_file = collections.Counter()
for path in sorted(glob.glob(BASE + '/*.rs')):
    fn = os.path.basename(path)
    text = open(path, encoding='utf-8').read()
    if 'assert_has_sandhi' not in text:
        continue
    lines = text.split('\n')
    line_starts = [0]
    for l in lines:
        line_starts.append(line_starts[-1] + len(l) + 1)
    import bisect
    for pos, args in find_calls(text):
        lineno = bisect.bisect_right(line_starts, pos)      # 1-based
        strs = [s for s in STR.findall(args)]
        if len(strs) < 3:
            dropped['unparsed-args'] += 1
            continue
        first, second, results = strs[0], strs[1], strs[2:]
        # enclosing fn
        k = lineno - 1
        fname = None
        while k >= 0:
            mm = re.match(r'\s*(?:pub\s+)?fn\s+(\w+)\s*\(', lines[k])
            if mm:
                fname = mm.group(1)
                break
            k -= 1
        ignored = False
        kk = k - 1
        while kk >= 0 and (lines[kk].strip().startswith('#[') or lines[kk].strip() == ''):
            if 'ignore' in lines[kk]:
                ignored = True
            kk -= 1
            if k - kk > 4:
                break
        # preceding comments (consecutive // lines directly above the call, or the line above them)
        cm = []
        c = lineno - 2
        while c >= 0 and lines[c].strip().startswith('//'):
            cm.insert(0, lines[c].strip().lstrip('/').strip())
            c -= 1
        m2 = re.match(r'sutra_(\d+)_(\d+)_(\d+)(?:_(.+))?$', fname or '')
        if not m2:
            dropped['no-sutra-in-fn-name'] += 1
            continue
        rule = '%s.%s.%s' % m2.group(1, 2, 3)
        suffix = m2.group(4)
        inp = [slp12iast(first), slp12iast(second)]
        outs = [slp12iast(r) for r in results]
        reason = malformed_reason(inp, outs[0])
        if reason or any(malformed_reason(inp, o) for o in outs):
            dropped[(reason or 'bad-alt').split(':')[0]] += 1
            continue
        # stems must survive: interior of each input word must appear in the (space-stripped) output
        o0 = outs[0].replace(' ', '')
        core1 = inp[0][1:-2]
        core2 = inp[1][2:-1]
        if (len(core1) >= 2 and core1 not in o0) or (len(core2) >= 2 and core2 not in o0):
            dropped['stem-not-in-output(source test inconsistent)'] += 1
            rejected.append({'file': fn, 'line': lineno, 'fn': fname, 'input': inp, 'results': outs})
            continue
        nt = ['%s line %d, fn %s%s' % (fn, lineno, fname, ' (#[ignore]: author TODO, engine did not yet reproduce it)' if ignored else '')]
        if suffix:
            nt.append('fn suffix "%s" (vartika/variant of the sutra)' % suffix)
        nt.append('expected set is exact: the test asserts the space-stripped set of results equals this list; spaces are for readability (Vidyut compares without spaces)')
        if len(outs) > 1:
            nt.append('ALT_OUTPUTS=' + json.dumps(outs[1:], ensure_ascii=False))
        if cm:
            nt.append('test comment: ' + ' / '.join(cm)[:200])
        nt.append('pre-sandhi pair joined as two padas (Vidyut derive_vakyas, external sandhi across a word boundary)')
        nt.append('source is SLP1, converted to IAST; "~" candrabindu written as m with candrabindu')
        rows.append(make_row(ds, len(rows) + 1, inp, outs[0], sandhi_type='unknown', rule=rule, boundary='pada', vedic=False,
                             src_file='ambuda-org_vidyut/vidyut-prakriya/tests/integration/' + fn, locator='line %d (%s)' % (lineno, fname),
                             url=URLB + fn, license_=LIC, quality='hand-annotated', notes=' | '.join(nt)))
        per_file[fn] += 1
write_jsonl(NORM + '/%s.jsonl' % ds, rows)
os.makedirs(OUT + '/qc/rejected', exist_ok=True)
write_jsonl(OUT + '/qc/rejected/%s.rejected.jsonl' % ds, rejected)
for x in rejected: print('REJECTED', x)
rep, r2 = qc_dataset(ds, NORM + '/%s.jsonl' % ds, dropped=dict(dropped), notes_extra={'per_file': dict(per_file)})
print(ds, len(rows), dict(dropped), dict(per_file))
print('close', rep['concat_close_fraction'], rep['concat_close_fraction_lenient'], 'distinct rules', rep['distinct_rules'], 'far', rep['concat_far_examples'][:5])
ign = sum(1 for r in rows if '#[ignore]' in r['notes']); alt = sum(1 for r in rows if 'ALT_OUTPUTS' in r['notes'])
print('ignored', ign, 'with alternatives', alt)
for r in rows[::4][:60]:
    print('%-9s %-22s + %-16s => %-28s %s' % (r['rule'], r['input'][0], r['input'][1], r['output'], ('ALT' if 'ALT_OUTPUTS' in r['notes'] else '') + (' IGN' if '#[ignore]' in r['notes'] else '')))
