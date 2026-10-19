import json,math
from pathlib import Path
W=json.loads(Path('wrapper-reference.json').read_text());R={r['key']:r for r in json.loads(Path('reference.json').read_text())}
checks=[]
def ck(key,q,a,b):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        d=abs(a-b)/max(1,abs(b));ok=math.isfinite(d) and d<=1e-9
    else:d=0 if a==b else None;ok=a==b
    checks.append(dict(key=key,quantity=q,wrapper=a,engine=b,difference=d,passed=ok))
for w in W:
    r=R[w['key']];key=w['key'];ck(key,'status',w['status'],r['status'])
    if w['status']=='ok' and r['status']=='ok':
        # Public discomb retains input combination label order; the page sorts
        # components inside each displayed/exported combination label.
        w['combinations']={'+'.join(sorted(n.split('+'))):z for n,z in w['combinations'].items()}
        for q in ['Q','df','tau2']:ck(key,q,w[q],r[q])
        for g in ['components','combinations']:
            ck(key,g+'_membership',sorted(w[g]),sorted(r[g]))
            for n,z in w[g].items():
                for q in ['est','se','lo','hi']:ck(key,g+'.'+n+'.'+q,z[q],r[g][n][q])
        if w.get('native') and r.get('native'):
            a,b=w['native'],r['native'];ck(key,'native_status','error' in a,'error' in b)
            if 'error' not in a and 'error' not in b:
                for q in ['Q','df','tau2']:ck(key,'native_'+q,a[q],b[q])
                for g in ['components','combinations']:
                    for n,z in a[g].items():
                        for q in ['est','se','lo','hi']:ck(key,'native_'+g+'.'+n+'.'+q,z[q],b[g][n][q])
result=dict(configurations=len(W),checks=len(checks),passed=sum(x['passed'] for x in checks),max_difference=max((x['difference'] or 0 for x in checks),default=0),failures=[x for x in checks if not x['passed']])
Path('wrapper-bridge.json').write_text(json.dumps(result,indent=2)+'\n');print(f"WRAPPER BRIDGE: {result['passed']}/{result['checks']} checks pass")
