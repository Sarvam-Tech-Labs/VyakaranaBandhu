import requests, sys, json, time
UA={'User-Agent':'sandhi-data-survey/0.1 (research; unauthenticated)','Accept':'application/vnd.github+json'}
for full in sys.argv[1:]:
    r=requests.get(f'https://api.github.com/repos/{full}',headers=UA,timeout=30)
    if r.status_code!=200:
        print(full,'ERR',r.status_code, r.text[:100]); 
        if r.status_code==403: print('rate-limited?', r.headers.get('X-RateLimit-Remaining'), r.headers.get('X-RateLimit-Reset'))
        continue
    j=r.json()
    lic=j.get('license') or {}
    print('%-55s size=%6dKB lic=%s branch=%s pushed=%s archived=%s | %s' % (full,j['size'],lic.get('spdx_id'),j['default_branch'],j['pushed_at'][:10],j['archived'],(j.get('description') or '')[:100]))
    time.sleep(1)
