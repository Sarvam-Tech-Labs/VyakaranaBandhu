# -*- coding: utf-8 -*-
"""Mine sandhi junctions from the Digital Corpus of Sanskrit (CoNLL-U, CC BY 4.0; Hellwig 2010-2024).

Two kinds of rows:
  MWT    : multiword-token line  'i-j <surface>'  + its component words' Unsandhied forms  ->  (unsandhied words) => surface token
  SPACED : two adjacent single-word tokens of a sandhied text: (Unsandhied1, Unsandhied2) => 'FORM1 FORM2'
           (sandhi applied although a typographic space remains)
Only edge-clean spaced pairs with a visible change are kept (see README)."""
import os, sys, re, json, collections, subprocess, time, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from qc import lev

ROOT = RAW + '/OliverHellwig_sanskrit/dcs/data/conllu/files'
WORK = OUT + '/../work/dcs_tmp'
os.makedirs(WORK, exist_ok=True)
REPO_URL = 'https://github.com/OliverHellwig/sanskrit'
LIC = 'CC-BY-4.0'
COMMIT = '8aeed5a1343d0e48b64eb32af8c00e8c6eb29359'

VEDIC = set("""Aitareya-Āraṇyaka|Aitareyabrāhmaṇa|Aitareyopaniṣad|Atharvaprāyaścittāni|Atharvaveda (Paippalāda)|Atharvaveda (Śaunaka)|Atharvavedapariśiṣṭa|
Baudhāyanadharmasūtra|Baudhāyanagṛhyasūtra|Baudhāyanaśrautasūtra|Bhāradvājagṛhyasūtra|Bhāradvājaśrautasūtra|Bṛhadāraṇyakopaniṣad|Chāndogyopaniṣad|Drāhyāyaṇaśrautasūtra|
Gautamadharmasūtra|Gobhilagṛhyasūtra|Gopathabrāhmaṇa|Hiraṇyakeśigṛhyasūtra|Hiraṇyakeśiśrautasūtra|Jaiminigṛhyasūtra|Jaiminīya-Upaniṣad-Brāhmaṇa|Jaiminīyabrāhmaṇa|Jaiminīyaśrautasūtra|
Kauśikasūtra|Kauṣītakagṛhyasūtra|Kauṣītakibrāhmaṇa|Kauṣītakyupaniṣad|Kaṭhopaniṣad|Kaṭhāraṇyaka|Khādiragṛhyasūtra|Kātyāyanaśrautasūtra|Kāṭhakagṛhyasūtra|Kāṭhakasaṃhitā|Lāṭyāyanaśrautasūtra|
Maitrāyaṇīsaṃhitā|Mānavagṛhyasūtra|Mānavaśrautasūtra|Muṇḍakopaniṣad|Nirukta|Pañcaviṃśabrāhmaṇa|Pāraskaragṛhyasūtra|Sāmavidhānabrāhmaṇa|Taittirīyabrāhmaṇa|Taittirīyasaṃhitā|Taittirīyopaniṣad|Taittirīyāraṇyaka|
Vaikhānasadharmasūtra|Vaikhānasagṛhyasūtra|Vaikhānasaśrautasūtra|Vaitānasūtra|Vasiṣṭhadharmasūtra|Vājasaneyisaṃhitā (Mādhyandina)|Vārāhagṛhyasūtra|Vārāhaśrautasūtra|
Āpastambadharmasūtra|Āpastambagṛhyasūtra|Āpastambaśrautasūtra|Āśvalāyanagṛhyasūtra|Āśvālāyanaśrautasūtra|Śatapathabrāhmaṇa|Śira'upaniṣad|Śvetāśvataropaniṣad|Śāṅkhāyanagṛhyasūtra|Śāṅkhāyanaśrautasūtra|Śāṅkhāyanāraṇyaka|
Ṛgveda|Ṛgvedakhilāni|Ṛgvedavedāṅgajyotiṣa|Ṛgvidhāna|Ṣaḍviṃśabrāhmaṇa""".replace('\n', '').split('|'))

ALLOWED = set("abcdefghijklmnopqrstuvwxyzāīūṛṝḷḹṅñṭḍṇśṣṃḥ'")


def norm(s):
    s = unicodedata.normalize('NFC', s)
    return s.replace('ṁ', 'ṃ').replace('’', "'")


def clean_ok(s):
    return bool(s) and all(ch in ALLOWED or ch == ' ' for ch in s.lower())


def parse_misc(m):
    d = {}
    if m and m != '_':
        for kv in m.split('|'):
            if '=' in kv:
                k, v = kv.split('=', 1)
                d[k] = v
    return d


def list_files():
    out = []
    for text in sorted(os.listdir(ROOT)):
        d = os.path.join(ROOT, text)
        if not os.path.isdir(d):
            continue
        names = sorted(os.listdir(d))
        base = {}
        for fn in names:
            if fn.endswith('.conllu'):
                base[fn[:-7]] = fn
        for fn in names:
            if fn.endswith('.conllu_parsed') and fn[:-14] not in base:
                base[fn[:-14]] = fn
        for b in sorted(base):
            out.append((text, base[b]))
    return out


def sentences(path):
    """Yield dict(text, sent_id, words{id:dict}, mwts[(a,b,surface)], order[ids])"""
    cur = None
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if line.startswith('# text ='):
                if cur and cur['words']:
                    yield cur
                cur = {'text': line[8:].strip(), 'sent_id': '', 'words': {}, 'mwts': [], 'order': []}
                continue
            if cur is None:
                continue
            if line.startswith('# sent_id'):
                cur['sent_id'] = line.split('=', 1)[1].strip()
                continue
            if line.startswith('#'):
                continue
            if not line.strip():
                continue
            c = line.split('\t')
            if len(c) < 10:
                continue
            idx = c[0]
            if '.' in idx:
                continue
            if '-' in idx:
                a, b = idx.split('-')
                cur['mwts'].append((int(a), int(b), c[1]))
                continue
            wid = int(idx)
            cur['words'][wid] = {'form': c[1], 'lemma': c[2], 'upos': c[3], 'feats': c[5], 'misc': parse_misc(c[9])}
            cur['order'].append(wid)
    if cur and cur['words']:
        yield cur


def surface_tokens(s):
    """Sequence of surface tokens: ('M', a, b, surface) for multiword tokens, ('W', id, None, form) for single words."""
    mw = {a: (a, b, sf) for a, b, sf in s['mwts']}
    covered = set()
    for a, b, _ in s['mwts']:
        covered.update(range(a, b + 1))
    toks = []
    for wid in s['order']:
        if wid in mw:
            a, b, sf = mw[wid]
            toks.append(('M', a, b, sf))
        elif wid in covered:
            continue
        else:
            toks.append(('W', wid, None, s['words'][wid]['form']))
    return toks


def uns(w):
    u = w['misc'].get('Unsandhied')
    if u is None or u == '_' or not u:
        return None
    return norm(u)


def is_cpd(w):
    return 'Case=Cpd' in w['feats']


def recon(w):
    return w['misc'].get('UnsandhiedReconstructed') == 'True'


# ------------------------------------------------------------------------------------------
def zone_left(U, F):
    """differences at the END of a word: returns (tailU, tailF, n_sounds_tailU, n_sounds_tailF)"""
    a, b = sounds(U), sounds(F)
    p = 0
    while p < len(a) and p < len(b) and a[p] == b[p]:
        p += 1
    return ''.join(a[p:]), ''.join(b[p:]), len(a) - p, len(b) - p


def zone_right(U, F):
    """differences at the START of a word: (headU, headF, n_sounds...)"""
    a, b = sounds(U), sounds(F)
    p = 0
    while p < len(a) and p < len(b) and a[len(a) - 1 - p] == b[len(b) - 1 - p]:
        p += 1
    return ''.join(a[:len(a) - p]), ''.join(b[:len(b) - p]), len(a) - p, len(b) - p


def edge_flags_mwt(U, S):
    left_clean = first_sound(S) == first_sound(U[0])
    right_clean = last_sound(S) == last_sound(U[-1]) and norm(S).endswith(U[-1][-1:])
    return left_clean, right_clean


def main():
    files = list_files()
    print('files', len(files))
    t0 = time.time()
    # ------------------------- pass 1: per-file evidence + signature counts -----------------------
    file_info = {}
    sigL = collections.Counter()
    sigR = collections.Counter()
    for fi, (text, fn) in enumerate(files):
        path = os.path.join(ROOT, text, fn)
        words = changed = mwt = 0
        cand = []
        for s in sentences(path):
            toks = surface_tokens(s)
            for t in toks:
                if t[0] == 'M':
                    mwt += 1
                    words += t[2] - t[1] + 1
                else:
                    w = s['words'][t[1]]
                    words += 1
                    u = uns(w)
                    if u is not None and norm(w['form']) != u:
                        changed += 1
        evidence = (mwt + changed) / max(1, words)
        file_info[(text, fn)] = {'words': words, 'mwt': mwt, 'changed': changed, 'evidence': evidence}
    print('pass 1a done', time.time() - t0)
    # sandhied-typed files: evidence >= 0.02
    sandhied = {k for k, v in file_info.items() if v['evidence'] >= 0.02}
    print('files considered sandhied-typed for SPACED mining:', len(sandhied), 'of', len(files))
    # pass 1b: signature counts on candidate pairs
    for fi, (text, fn) in enumerate(files):
        if (text, fn) not in sandhied:
            continue
        path = os.path.join(ROOT, text, fn)
        for s in sentences(path):
            toks = surface_tokens(s)
            for a, b in zip(toks, toks[1:]):
                if a[0] != 'W' or b[0] != 'W':
                    continue
                w1, w2 = s['words'][a[1]], s['words'][b[1]]
                u1, u2 = uns(w1), uns(w2)
                f1, f2 = norm(w1['form']), norm(w2['form'])
                if u1 is None or u2 is None or not clean_ok(f1) or not clean_ok(f2) or not clean_ok(u1) or not clean_ok(u2):
                    continue
                if first_sound(f1) != first_sound(u1) or last_sound(f2) != last_sound(u2):
                    continue
                tl = zone_left(u1, f1)
                tr = zone_right(u2, f2)
                sigL[(tl[0], tl[1])] += 1
                sigR[(tr[0], tr[1])] += 1
    print('pass 1b done', time.time() - t0, 'sigL', len(sigL), 'sigR', len(sigR))
    json.dump({'sigL_top': [[list(k), v] for k, v in sigL.most_common(60)], 'sigR_top': [[list(k), v] for k, v in sigR.most_common(60)],
               'sigL_rare_examples': [[list(k), v] for k, v in sigL.items() if v < 5][:80],
               'sigR_rare_examples': [[list(k), v] for k, v in sigR.items() if v < 5][:80],
               'n_sigL': len(sigL), 'n_sigR': len(sigR), 'n_sigL_rare': sum(1 for v in sigL.values() if v < 5), 'n_sigR_rare': sum(1 for v in sigR.values() if v < 5)},
              open(OUT + '/qc/dcs_signature_counts.json', 'w'), ensure_ascii=False, indent=1)
    json.dump({'%s/%s' % k: v for k, v in file_info.items()}, open(OUT + '/qc/dcs_file_evidence.json', 'w'), ensure_ascii=False)
    MIN_SIG = 5
    # ------------------------- pass 2: emit TSV candidate lines ----------------------------------
    f_mwt = open(WORK + '/mwt.tsv', 'w', encoding='utf-8')
    f_sp = open(WORK + '/spaced.tsv', 'w', encoding='utf-8')
    cnt = collections.Counter()
    for fi, (text, fn) in enumerate(files):
        path = os.path.join(ROOT, text, fn)
        loc_file = '%s/%s' % (text, fn)
        vedic_text = text in VEDIC
        for s in sentences(path):
            toks = surface_tokens(s)
            # ---- MWT rows
            for t in toks:
                if t[0] != 'M':
                    continue
                a, b, sf = t[1], t[2], norm(t[3])
                comps = [s['words'].get(k) for k in range(a, b + 1)]
                if any(c is None for c in comps):
                    cnt['mwt-missing-component'] += 1
                    continue
                U = [uns(c) for c in comps]
                if any(u is None for u in U):
                    cnt['mwt-missing-unsandhied'] += 1
                    continue
                if not clean_ok(sf) or ' ' in sf or any((not clean_ok(u)) or ' ' in u for u in U):
                    cnt['mwt-nonsanskrit-char'] += 1
                    continue
                nj = len(U) - 1
                d = lev([x for x in sounds(''.join(U)) if x != "'"], [x for x in sounds(sf) if x != "'"])
                if d > 2 * nj + 3:
                    cnt['mwt-misaligned'] += 1
                    continue
                lc, rc = edge_flags_mwt(U, sf)
                mant = any(c['misc'].get('IsMantra') == 'True' for c in comps)
                rec = sum(1 for c in comps if recon(c))
                bnd = ','.join('s' if is_cpd(c) else 'p' for c in comps[:-1])
                rflag = 'all' if rec == len(comps) else ('none' if rec == 0 else 'part')
                vd = 1 if (vedic_text or mant) else 0
                f_mwt.write('\t'.join(['+'.join(U), sf, str(vd), bnd, rflag, ('L' if lc else 'l') + ('R' if rc else 'r'), loc_file, s['sent_id'], text]) + '\n')
                cnt['mwt-kept-raw'] += 1
            # ---- SPACED rows
            if (text, fn) not in sandhied:
                continue
            for a, b in zip(toks, toks[1:]):
                if a[0] != 'W' or b[0] != 'W':
                    continue
                w1, w2 = s['words'][a[1]], s['words'][b[1]]
                u1, u2 = uns(w1), uns(w2)
                if u1 is None or u2 is None:
                    cnt['sp-missing-unsandhied'] += 1
                    continue
                f1, f2 = norm(w1['form']), norm(w2['form'])
                if not (clean_ok(f1) and clean_ok(f2) and clean_ok(u1) and clean_ok(u2)) or ' ' in f1 + f2 + u1 + u2:
                    cnt['sp-nonsanskrit-char'] += 1
                    continue
                if first_sound(f1) != first_sound(u1) or last_sound(f2) != last_sound(u2):
                    cnt['sp-edge-affected'] += 1
                    continue
                if f1 == u1 and f2 == u2:
                    cnt['sp-no-visible-change'] += 1
                    continue
                tl = zone_left(u1, f1)
                tr = zone_right(u2, f2)
                if tl[2] > 3 or tl[3] > 3 or tr[2] > 3 or tr[3] > 3:
                    cnt['sp-change-zone-too-wide'] += 1
                    continue
                if sigL[(tl[0], tl[1])] < MIN_SIG or sigR[(tr[0], tr[1])] < MIN_SIG:
                    cnt['sp-rare-signature'] += 1
                    continue
                mant = w1['misc'].get('IsMantra') == 'True' or w2['misc'].get('IsMantra') == 'True'
                vd = 1 if (vedic_text or mant) else 0
                rflag = ('r' if recon(w1) else 'm') + ('r' if recon(w2) else 'm')
                bd = 's' if is_cpd(w1) else 'p'
                f_sp.write('\t'.join([u1, u2, f1, f2, str(vd), bd, rflag, loc_file, s['sent_id'], text]) + '\n')
                cnt['sp-kept-raw'] += 1
        if fi % 2000 == 0:
            print(fi, len(files), dict(cnt), round(time.time() - t0))
    f_mwt.close(); f_sp.close()
    json.dump(dict(cnt), open(OUT + '/qc/dcs_extract_counts.json', 'w'), indent=1)
    print('pass 2 done', time.time() - t0, dict(cnt))


if __name__ == '__main__':
    main()
