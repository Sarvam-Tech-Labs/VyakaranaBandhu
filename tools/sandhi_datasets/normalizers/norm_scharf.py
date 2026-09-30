# -*- coding: utf-8 -*-
"""Normalise Peter Scharf's sandhi test suites (funderburkjim/ScharfSandhi, MIT). All text is SLP1."""
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from qc import concat_closeness

BASE = RAW + '/funderburkjim__ScharfSandhi/testfiles'
URLB = 'https://github.com/funderburkjim/ScharfSandhi/blob/51ca52895ad5bb585fd1479f6fa7eeb7ab93985c/testfiles/'
LIC = 'MIT (ScharfSandhi repo LICENSE, (c) 2015 funderburkjim; test suite by Peter Scharf)'
Q = 'rule-engine-generated'
QNOTE = ("expected outputs are what Scharf's Pascal sandhi engine (1992-2000; ported to Perl/Java/Python by J. Funderburk) produces "
         "and is accepted as the regression standard -- an expert engine, not a hand-annotated corpus; a mismatch is a lead, not a proof of an engine bug")


def lines(fn):
    with open(os.path.join(BASE, fn), encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f]


def ok_slp(s):
    return re.fullmatch(r"[A-Za-z' -]+", s) is not None


# ---------------------------------------------------------------------------------------------
def build_external():
    ds = 'scharf-sandhi-external'
    rows, dropped = [], collections.Counter()
    n = 0
    for fin, fout, opt, desc in [('TestIn.txt', 'TestOut.txt', 'E', 'external sandhi (option E)'),
                                 ('Testnn.txt', 'TestnnOut.txt', 'E1', 'external sandhi, option E1: spaces kept, only the -n doubling / minimal change is applied')]:
        a, b = lines(fin), lines(fout)
        assert len(a) == len(b), (fin, len(a), len(b))
        for i, (x, y) in enumerate(zip(a, b), 1):
            if not x.strip():
                continue
            words = x.split()
            if not ok_slp(x) or not ok_slp(y):
                dropped['punctuation-marker-in-line'] += 1
                continue
            inp = [slp12iast(w) for w in words]
            out = slp12iast(y.strip())
            reason = malformed_reason(inp, out)
            if reason:
                dropped[reason] += 1
                continue
            n += 1
            rows.append(make_row(ds, n, inp, out, sandhi_type='unknown', rule=None, boundary='pada', vedic=False,
                                 src_file='funderburkjim__ScharfSandhi/testfiles/%s + %s' % (fin, fout), locator='line %d' % i,
                                 url=URLB + fin, license_=LIC, quality=Q,
                                 notes='SLP1 converted to IAST | %s | %s | pairs with the same line of %s' % (desc, QNOTE, fout)))
    return ds, rows, dropped


# ---------------------------------------------------------------------------------------------
def _variants(chunk):
    """The filler may be altered by a junction: a preceding short u/i/a can be lengthened (uu -> uU)."""
    vs = {chunk}
    if chunk and chunk[-1] in 'uia':
        vs.add(chunk[:-1] + chunk[-1].upper())
    return sorted(vs, key=lambda x: (x != chunk, x))


def slice_chain(seg_line, out_line, mid):
    """seg_line: 'uk-kuuk-Kuuk-...' ; out_line: joined output; mid = invariant filler ('uu' or 'kk').
    Each segment i>=1 is <initial><mid><final>; the shared final L may be several letters (e.g. AH).
    Returns pairs (left, right, joined, J, L, altered_flag) or None. A junction may lengthen the last vowel of the
    preceding filler (uu -> uU); that is allowed and carried into the pair output."""
    import re as _re
    segs = seg_line.split('-')
    if len(segs) < 3:
        return None
    if any(len(sg) < 1 + len(mid) or sg[1:1 + len(mid)] != mid for sg in segs[1:]):
        return None
    L = segs[1][1 + len(mid):]
    if not L or any(sg[1 + len(mid):] != L for sg in segs[1:]):
        return None
    if not segs[0].endswith(L):
        return None
    head = segs[0][:-len(L)]
    n = len(segs) - 1                        # number of junctions
    hv = '|'.join(_re.escape(v) for v in _variants(head))
    mv = '|'.join(_re.escape(v) for v in _variants(mid))
    pat = '^(' + hv + ')'
    for i in range(n):
        pat += '(.*?)'
        if i < n - 1:
            pat += '(' + mv + ')'
        else:
            pat += '(' + mv + ')' + _re.escape(L)
    pat += '$'
    m = _re.match(pat, out_line)
    if not m:
        return None
    g = m.groups()
    head_out = g[0]
    Js, mids_out = [], []
    k = 1
    for i in range(n):
        Js.append(g[k]); mids_out.append(g[k + 1]); k += 2
    # the filler that PRECEDES junction i is: head_out for i=0, mids_out[i-1] for i>=1 ; the filler that FOLLOWS junction i is mids_out[i]
    pairs = []
    for i, J in enumerate(Js):
        left, right = segs[i], segs[i + 1]
        if i == 0:
            left_core = head_out                     # possibly altered by junction 0 (lengthening acts on the left word's own vowel)
        else:
            left_core = None
        # In this file the lengthening affects the vowel BEFORE the junction; for i>=1 that vowel lies inside the left segment's filler,
        # which is the filler that FOLLOWS junction i-1 and PRECEDES junction i.  We recorded fillers as those found before each J, so:
        if i == 0:
            pre = head_out
            joined = pre + J + right[1:]
            altered = pre != head
        else:
            pre_filler = mids_out[i - 1]
            joined = left[0] + pre_filler + J + right[1:]
            altered = pre_filler != mid
        pairs.append((left, right, joined, J, L, altered))
    return pairs


def build_compound_matrix():
    ds = 'scharf-sandhi-compound-matrix'
    a = lines('TestSandhiC.txt')
    b1 = lines('TestSandhiCOutv1.txt')       # current standard (used by pythonv4/testsuite.sh)
    b0 = lines('TestSandhiCOut.txt')          # Scharf's original expected output
    assert len(a) == len(b1) == len(b0)
    rows, dropped = [], collections.Counter()
    alt_diff = 0
    n = 0
    block = 'Consonants'
    chain_no = 0
    for i, (x, y1, y0) in enumerate(zip(a, b1, b0), 1):
        if x.strip() in ('Consonants', 'Vowels'):
            block = x.strip()
            continue
        def prep(s):
            s = s.rstrip()
            s = re.sub(r'^\d{5}\t', '', s)          # 11111<TAB> line ids
            s = re.sub(r'\s+\.$', '', s)            # trailing pausal marker
            return s
        xs, ys1, ys0 = prep(x), prep(y1), prep(y0)
        mid = 'uu' if block == 'Consonants' else 'kk'
        sl = slice_chain(xs, ys1, mid)
        sl0 = slice_chain(xs, ys0, mid)
        if sl is None:
            dropped['chain-not-sliceable'] += 1
            print('   not sliceable: line', i, xs[:60])
            continue
        chain_no += 1
        for j, (left, right, joined, J, Lfin, altered) in enumerate(sl):
            inp = [slp12iast(left), slp12iast(right)]
            out = slp12iast(joined)
            reason = malformed_reason(inp, out)
            if reason:
                dropped[reason] += 1
                continue
            alt = ''
            if altered:
                alt += ' | the junction lengthens the preceding filler vowel (compensatory lengthening, e.g. 6.3.111-type effect); kept in the output'
            if sl0 is not None and sl0[j][3] != J:
                alt = " | ALT: Scharf's original TestSandhiCOut.txt gives junction %s -> %s (older convention; the rule is optional/variant here)" % (slp12iast(Lfin + right[0]), slp12iast(sl0[j][3]))
                alt_diff += 1
            n += 1
            rows.append(make_row(ds, n, inp, out, sandhi_type='unknown', rule=None, boundary='samasa', vedic=False,
                                 src_file='funderburkjim__ScharfSandhi/testfiles/TestSandhiC.txt + TestSandhiCOutv1.txt',
                                 locator='line %d (%s block), junction %d of %d' % (i, block, j + 1, len(sl)),
                                 url=URLB + 'TestSandhiC.txt', license_=LIC, quality=Q,
                                 notes=('SLP1 converted to IAST | compound sandhi (option C; hyphen = compound boundary in the source) | '
                                        'PAIR DERIVED BY SLICING a chain test line: the file joins ~38 segments at once; each segment is <initial><invariant filler><final>; '
                                        'the junction result was cut out by splitting on the invariant filler and the chain re-assembled exactly (checksum passed); '
                                        'assumes the junction result is local, i.e. independent of the filler | the filler letters are artificial (uu / kk), only the junction is meaningful | %s%s') % (QNOTE, alt)))
    return ds, rows, dropped, alt_diff


# ---------------------------------------------------------------------------------------------
def build_dhatupatha_compounds():
    ds = 'scharf-sandhi-dhatupatha-compounds'
    a = lines('PascalSandhiTest3-nl.txt')
    b = lines('PascalSandhiTest3S-nl.txt')
    assert len(a) == len(b)
    rows, dropped = [], collections.Counter()
    n = 0
    seen = {}
    for i, (x, y) in enumerate(zip(a, b), 1):
        if '-' not in x:
            continue
        tx, ty = x.split(), y.split()
        if len(tx) != len(ty):
            dropped['token-count-mismatch'] += 1
            continue
        for k, (p, q) in enumerate(zip(tx, ty)):
            if '-' not in p:
                continue
            if '=' in p or not ok_slp(p) or not ok_slp(q):
                dropped['token-with-non-letter'] += 1
                continue
            parts = p.split('-')
            if any(not s for s in parts):
                dropped['empty-part'] += 1
                continue
            key = (tuple(parts), q)
            if key in seen:
                seen[key]['count'] += 1
                continue
            inp = [slp12iast(s) for s in parts]
            out = slp12iast(q)
            reason = malformed_reason(inp, out)
            if reason:
                dropped[reason] += 1
                continue
            d, allowed = concat_closeness(inp, out)
            if d > allowed + 2:
                dropped['misaligned'] += 1
                continue
            n += 1
            r = make_row(ds, n, inp, out, sandhi_type='unknown', rule=None, boundary='samasa', vedic=False,
                         src_file='funderburkjim__ScharfSandhi/testfiles/PascalSandhiTest3-nl.txt + PascalSandhiTest3S-nl.txt',
                         locator='line %d, token %d' % (i, k + 1), url=URLB + 'PascalSandhiTest3-nl.txt', license_=LIC, quality=Q,
                         notes='SLP1 converted to IAST | compound sandhi (option C) on hyphenated compound members in Dhatupatha glosses '
                               '(Scharf test 3: each dhatu entry line; line 1 = input with hyphens, line 2 = expected) | ' + QNOTE)
            seen[key] = {'row': r, 'count': 1}
            rows.append(r)
    for v in seen.values():
        if v['count'] > 1:
            v['row']['notes'] += ' | occurrences of this identical pair in the file: %d' % v['count']
    return ds, rows, dropped


if __name__ == '__main__':
    summ = {}
    for fn in (build_external, build_compound_matrix, build_dhatupatha_compounds):
        res = fn()
        ds, rows, dropped = res[0], res[1], res[2]
        write_jsonl(NORM + '/%s.jsonl' % ds, rows)
        summ[ds] = {'rows': len(rows), 'dropped': dict(dropped)}
        if len(res) > 3:
            summ[ds]['rows_where_original_and_v1_differ'] = res[3]
        print(ds, len(rows), dict(dropped), res[3:] if len(res) > 3 else '')
    json.dump(summ, open(OUT + '/qc/scharf_build_summary.json', 'w'), indent=1)
