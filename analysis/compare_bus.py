"""Bus-import checks (validation archive copy of the lane's compare_bus.py; logic unchanged).
Usage: python analysis/compare_bus.py <bus-reference.json> <out-dir> [archive-root]"""
import json,math,sys
from pathlib import Path
ROOT=Path(sys.argv[3]) if len(sys.argv)>3 else Path(__file__).resolve().parents[1]
OUT=Path(sys.argv[2]);OUT.mkdir(parents=True,exist_ok=True)
def load(n):return json.loads(Path(n).read_text(encoding='utf-8'))
R={x['key']:x for x in load(sys.argv[1])};out={}
for variant in ['original','patched']:
    A=load(ROOT/'results'/f'bus-{variant}.json');checks=[]
    def check(key,q,got,expected,ok):checks.append(dict(key=key,quantity=q,got=got,expected=expected,pass_=bool(ok)))
    check('coverage','keys',sorted(x['key'] for x in A),sorted(R),sorted(x['key'] for x in A)==sorted(R))
    for a in A:
        key=a['key'];r=R[key]
        check(key,'execution',a['error'],None,a['error'] is None)
        if 'reason' in r:
            for q in ['result','componentTable','forestMarkup']:
                want=None if q=='result' else '';check(key,'refusal_'+q,a[q],want,a[q]==want)
            check(key,'refusal_reason',a['toasts'],r['reason'],r['reason'] in a['toasts'])
        else:
            check(key,'rows',len(a['converted']),len(r['rows']),len(a['converted'])==len(r['rows']))
            for i,e in enumerate(r['rows']):
                g=a['converted'][i] if i<len(a['converted']) else {}
                for q in ['te','se']:
                    v=g.get(q);check(key,f'{i}.{q}',v,e[q],isinstance(v,(int,float)) and math.isfinite(v) and abs(v-e[q])/max(1,abs(e[q]))<=1e-9)
            check(key,'fit_present',bool(a['result']),True,bool(a['result']))
    result=dict(passed=sum(c['pass_'] for c in checks),checks=len(checks),failures=[c for c in checks if not c['pass_']])
    out[variant]=result;print(f"BUS {variant}: {result['passed']}/{result['checks']} checks pass")
(OUT/'bus-results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
