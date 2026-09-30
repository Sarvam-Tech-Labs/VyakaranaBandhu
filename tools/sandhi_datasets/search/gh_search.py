import requests, json, sys, time
UA={'User-Agent':'sandhi-data-survey/0.1 (research; unauthenticated)','Accept':'application/vnd.github+json'}
def search(q, kind='repositories', per=30, sort=None):
    p={'q':q,'per_page':per}
    if sort: p['sort']=sort
    r=requests.get(f'https://api.github.com/search/{kind}',params=p,headers=UA,timeout=30)
    if r.status_code!=200:
        return {'error':r.status_code,'msg':r.text[:200]}
    return r.json()
queries=sys.argv[1:]
for q in queries:
    j=search(q)
    print('=== QUERY:',q)
    if 'error' in j: print('  ERROR',j); time.sleep(8); continue
    print('  total_count',j.get('total_count'))
    for it in j.get('items',[]):
        print('  %-55s * %-4s upd=%s lic=%s | %s' % (it['full_name'], it['stargazers_count'], it['pushed_at'][:10], (it.get('license') or {}).get('spdx_id'), (it.get('description') or '')[:110]))
    time.sleep(8)
