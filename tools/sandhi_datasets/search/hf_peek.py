import sys, json, requests, time
UA={'User-Agent':'sandhi-data-survey/0.1 (research; unauthenticated)'}
def peek(ds, n=4):
    r=requests.get('https://datasets-server.huggingface.co/splits',params={'dataset':ds},headers=UA,timeout=60)
    if r.status_code!=200:
        print('  splits ERR',r.status_code,r.text[:150]); return
    sp=r.json().get('splits',[])
    print('  splits:',[(s['config'],s['split']) for s in sp][:8])
    if not sp: return
    s=sp[0]
    r=requests.get('https://datasets-server.huggingface.co/first-rows',params={'dataset':ds,'config':s['config'],'split':s['split']},headers=UA,timeout=60)
    if r.status_code!=200:
        print('  first-rows ERR',r.status_code,r.text[:150]); return
    j=r.json()
    print('  features:',[(f['name'],f['type'].get('dtype') if isinstance(f['type'],dict) else f['type']) for f in j['features']])
    for row in j['rows'][:n]:
        print('   ',json.dumps(row['row'],ensure_ascii=False)[:420])
for ds in sys.argv[1:]:
    print('='*90); print(ds)
    try: peek(ds)
    except Exception as e: print('ERR',e)
    time.sleep(1)
