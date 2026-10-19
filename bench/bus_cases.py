import json
from pathlib import Path
cases=[]
for sm in ['OR','RR','MD','SMD']:
    for zero in ([False,True] if sm in ['OR','RR'] else [False]):
        arms=[dict(treatment='a',events=0 if zero else 3,n=20,mean=3,sd=1.2),dict(treatment='control',events=5,n=25,mean=2,sd=1.5)]
        studies=[dict(id='one',arms=arms),dict(id='two',arms=[dict(**{**a,'n':a['n']+3}) for a in arms])]
        cases.append(dict(key='bus::'+sm+('::zero' if zero else ''),env=dict(_schema='ma-comparisons-v1',_savedAt='2026-01-01',effectMeasure=sm,studies=studies)))
base=cases[0]['env']
cases.append(dict(key='bus::empty',env=None,expected_refusal='Shared network bus is empty.'))
cases.append(dict(key='bus::unsupported-RD',env={**base,'effectMeasure':'RD'},expected_refusal='Bus measure RD yielded no contrasts (needs OR/RR with events/n, or MD/SMD with mean/sd/n).'))
cases.append(dict(key='bus::multi-arm',env={**base,'studies':[dict(id='one',arms=[*base['studies'][0]['arms'],dict(treatment='a+b',events=4,n=30)])]},expected_refusal='Multi-arm or repeated-study bus inputs are unsupported: contrast covariance is required.'))
cases.append(dict(key='bus::repeated-study',env={**base,'studies':[base['studies'][0],base['studies'][0]]},expected_refusal='Multi-arm or repeated-study bus inputs are unsupported: contrast covariance is required.'))
Path('bus-corpus.json').write_text(json.dumps(cases,indent=2)+'\n')
