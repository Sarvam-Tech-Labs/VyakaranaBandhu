# -*- coding: utf-8 -*-
"""Shared helpers for the external sandhi-data normalisation (written under scratchpad only)."""
import json, re, os, hashlib, random, unicodedata, collections
from indic_transliteration import sanscript

OUT = '/workspaces/codespaces-blank/sandhi_work/external_data'
RAW = OUT + '/raw'
NORM = OUT + '/normalized'

# ----------------------------------------------------------------------------
# Transliteration
# ----------------------------------------------------------------------------
_ZW = dict.fromkeys(map(ord, '‌‍​⁠﻿'), None)   # ZWNJ ZWJ ZWSP WJ BOM
_DEV_ACCENTS = dict.fromkeys(map(ord, '॒॑॓॔᳐᳑᳒᳓᳔᳕᳖᳗᳘᳙᳜᳝᳞᳟᳚᳛᳠'), None)


def nfc(s):
    return unicodedata.normalize('NFC', s)


def dev2iast(s, strip_accents=False):
    """Devanagari -> IAST (indic-transliteration), after removing ZW characters.
    Avagraha -> ASCII apostrophe; anusvara -> m with dot below; visarga -> h with dot below."""
    s = s.translate(_ZW)
    if strip_accents:
        s = s.translate(_DEV_ACCENTS)
    out = sanscript.transliterate(s, sanscript.DEVANAGARI, sanscript.IAST)
    out = out.replace('’', "'").replace('ʼ', "'")
    out = out.replace('~', 'm̐')          # candrabindu -> m + combining candrabindu (IAST convention)
    return nfc(out)


def slp12iast(s):
    out = sanscript.transliterate(s, sanscript.SLP1, sanscript.IAST)
    out = out.replace('~', 'm̐')
    return nfc(out)


def iast2slp1(s):
    return sanscript.transliterate(nfc(s), sanscript.IAST, sanscript.SLP1)


def iast2dev(s):
    return sanscript.transliterate(nfc(s), sanscript.IAST, sanscript.DEVANAGARI)


def hk2iast(s):
    return nfc(sanscript.transliterate(s, sanscript.HK, sanscript.IAST))


# ----------------------------------------------------------------------------
# IAST sound segmentation (for junction statistics)
# ----------------------------------------------------------------------------
_SOUNDS = ['ai', 'au', 'kh', 'gh', 'ch', 'jh', 'ṭh', 'ḍh', 'th', 'dh', 'ph', 'bh',
           'ā', 'ī', 'ū', 'ṝ', 'ḹ', 'ṛ', 'ḷ', 'a', 'i', 'u', 'e', 'o',
           'k', 'g', 'ṅ', 'c', 'j', 'ñ', 'ṭ', 'ḍ', 'ṇ', 't', 'd', 'n', 'p', 'b', 'm',
           'y', 'r', 'l', 'v', 'ś', 'ṣ', 's', 'h', 'ṃ', 'ḥ', "'"]
_SOUND_RE = re.compile('|'.join(sorted(map(re.escape, _SOUNDS), key=lambda x: -len(x))) + '|m̐')
VOWELS = {'a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'ḹ', 'e', 'ai', 'o', 'au'}


def sounds(w):
    """Split an IAST word into sounds (digraph aware). Returns list, ignoring non-IAST chars."""
    w = nfc(w.lower())
    return _SOUND_RE.findall(w)


def last_sound(w):
    w = re.sub(r"[\s\-'’]+$", '', w)
    s = sounds(w)
    return s[-1] if s else ''


def first_sound(w):
    w = re.sub(r"^[\s\-]+", '', w)
    s = sounds(w)
    return s[0] if s else ''


def sound_class(x):
    if x in VOWELS:
        return 'V'
    if x in ('ṃ', 'm̐'):
        return 'ANUSVARA'
    if x == 'ḥ':
        return 'VISARGA'
    if x == "'":
        return 'AVAGRAHA'
    if x in ('k', 'kh', 'g', 'gh', 'ṅ'):
        return 'K-series'
    if x in ('c', 'ch', 'j', 'jh', 'ñ'):
        return 'C-series'
    if x in ('ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ'):
        return 'T-series(retroflex)'
    if x in ('t', 'th', 'd', 'dh', 'n'):
        return 'dental'
    if x in ('p', 'ph', 'b', 'bh', 'm'):
        return 'P-series'
    if x in ('y', 'r', 'l', 'v'):
        return 'semivowel'
    if x in ('ś', 'ṣ', 's'):
        return 'sibilant'
    if x == 'h':
        return 'h'
    return 'other'


# ----------------------------------------------------------------------------
# Row writing / QC
# ----------------------------------------------------------------------------
IAST_LETTERS = set("abcdefghijklmnopqrstuvwxyzāīūṛṝḷḹṅñṭḍṇśṣṃḥḻ") | {'̐'}
ALLOWED_OUT = IAST_LETTERS | set(" '-") | {'ṁ'}


def malformed_reason(inp, out):
    """Return a string describing why a row is malformed, or None."""
    if not inp or any(not x.strip() for x in inp):
        return 'empty-input-piece'
    if not out or not out.strip():
        return 'empty-output'
    for x in list(inp) + [out]:
        xs = x.lower()
        if xs.count('(') != xs.count(')') or xs.count('[') != xs.count(']') or xs.count('{') != xs.count('}'):
            return 'unmatched-bracket'
        bad = [ch for ch in xs if ch not in ALLOWED_OUT]
        if bad:
            return 'non-sanskrit-char:' + ''.join(sorted(set(bad)))[:12]
    return None


def junction_of(inp):
    if len(inp) == 2:
        return {'left_final': last_sound(inp[0]), 'right_initial': first_sound(inp[1])}
    return None


def make_row(dataset, idx, inp, out, sandhi_type='unknown', rule=None, boundary='unknown', vedic=False,
             src_file='', locator='', url='', license_='', quality='unknown', notes='', junction=True):
    r = {
        'id': '%s-%06d' % (dataset, idx),
        'dataset': dataset,
        'input': list(inp),
        'output': out,
    }
    if junction:
        j = junction_of(inp)
        if j:
            r['junction'] = j
    r.update({
        'sandhi_type': sandhi_type,
        'rule': rule,
        'boundary': boundary,
        'vedic': vedic,
        'source': {'file': src_file, 'locator': str(locator), 'url': url},
        'license': license_,
        'quality': quality,
        'notes': notes,
    })
    return r


def write_jsonl(path, rows):
    with open(path, 'w', encoding='utf-8') as f:
        n = 0
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False, separators=(',', ':')) + '\n')
            n += 1
    return n


def read_jsonl(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def sha256_file(path, blocksize=1 << 20):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(blocksize), b''):
            h.update(b)
    return h.hexdigest()


def sample_file(src, dst, n=10000, seed=1):
    rows = list(read_jsonl(src))
    rnd = random.Random(seed)
    if len(rows) > n:
        rows = rnd.sample(rows, n)
        rows.sort(key=lambda r: r['id'])
    return write_jsonl(dst, rows)


def roundtrip_check(words, to_iast, from_iast, n=100, seed=7):
    """Round trip check for a transliteration pair on a sample of words; returns (n_checked, n_fail, fails[:10])."""
    rnd = random.Random(seed)
    ws = list(words)
    if len(ws) > n:
        ws = rnd.sample(ws, n)
    fails = []
    for w in ws:
        try:
            back = from_iast(to_iast(w))
        except Exception as e:  # pragma: no cover
            fails.append((w, 'EXC ' + str(e)))
            continue
        if back != w:
            fails.append((w, back))
    return len(ws), len(fails), fails[:10]
