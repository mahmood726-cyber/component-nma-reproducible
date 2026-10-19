import json,csv,sys,math,collections,xml.etree.ElementTree as ET
from pathlib import Path
variant=sys.argv[1] if len(sys.argv)>1 else 'patched'
def load(n):return json.loads(Path(n).read_text(encoding='utf-8'))
corpus=load('corpus.json')+load('focused-corpus.json');refs=load('reference.json');apps=load(f'app-{variant}.json')
stats={};failures=[];native=[]
def ck(q,ok,key='',got=None,ref=None,diff=None):
    s=stats.setdefault(q,dict(checks=0,passed=0,max_difference=0,invalid=0));s['checks']+=1;s['passed']+=bool(ok)
    if diff is not None and math.isfinite(diff):s['max_difference']=max(s['max_difference'],diff)
    elif not ok:s['invalid']+=1
    if not ok:failures.append(dict(quantity=q,key=key,got=got,reference=ref,difference=diff))
def exact(q,a,b,key):ck(q,a==b,key,a,b,0 if a==b else 1)
def num(q,a,b,key):
    if b is None:return exact(q+'_undefined',a,None,key)
    valid=isinstance(a,(int,float)) and not isinstance(a,bool) and math.isfinite(a) and math.isfinite(b)
    d=abs(a-b)/max(1,abs(b)) if valid else None
    ck(q,valid and d<=1e-9,key,a,b,d)
def index(a,name):
    keys=[x['key'] for x in a];exact(name+'_unique',len(set(keys)),len(keys),'coverage');return {x['key']:x for x in a}
C=index(corpus,'corpus');R=index(refs,'reference');A=index(apps,'app')
exact('reference_coverage',sorted(R),sorted(C),'coverage');exact('app_coverage',sorted(A),sorted(C),'coverage')
def fmt(x,n=3):return f'{x:.{n}f}' if isinstance(x,(int,float)) and math.isfinite(x) else '—'
def flat(obj,prefix=''):
    out=[]
    for k,v in obj.items():
        path=prefix+'.'+k if prefix else k
        if isinstance(v,dict):out+=flat(v,path)
        else:out.append((path,v))
    return out
for key,c in C.items():
    r=R.get(key);a=A.get(key)
    ck('reference_evidence',bool(r) and r.get('status') in ['ok','refused'],key, r.get('reason') if r else None,'valid R result or supported refusal')
    ck('app_evidence',bool(a),key)
    if not r or not a:continue
    exact('execution_error',a.get('error'),None,key);exact('export_error',a.get('exportError'),None,key)
    out=a.get('result')
    if r['status']=='refused':
        exact('refusal_state',out,None,key)
        ck('refusal_reason',r['reason'] in a.get('toasts',[]),key,a.get('toasts'),r['reason'])
        exact('refusal_component_table',a.get('componentTable'),[],key);exact('refusal_combination_table',a.get('combinationTable'),[],key);exact('refusal_forest',a.get('forestMarkup'),'',key)
    elif r['status']=='ok':
        ck('fit_present',isinstance(out,dict),key)
        out=out or {}
        for q in ['Q','tau2']:num(q,out.get(q),r[q],key)
        exact('df',out.get('df'),r['df'],key)
        exact('input_rows',len(a.get('parsed') or []),r['k'],key)
        exact('component_membership',sorted(out.get('components',{})),sorted(r['comps']),key)
        exact('combination_membership',sorted(out.get('combinations',{})),sorted(r['combination_names']),key)
        exact('component_design',a.get('design'),r['design'],key)
        items=[]
        for group,names,table in [('components',r['comps'],'componentTable'),('combinations',r['combination_names'],'combinationTable')]:
            actual=out.get(group,{})
            wanted=[];selfrows=[]
            for name in sorted(names):
                expected=r[group][name];got=actual.get(name,{})
                for q in ['est','se']:num(group+'_'+q,got.get(q),expected[q],key+'::'+name)
                e,se=expected['est'],expected['se'];lo,hi=expected['lo'],expected['hi']
                wanted.append([name,fmt(e)]+([fmt(se)] if group=='components' else [])+[f'[{fmt(lo)}, {fmt(hi)}]'])
                if isinstance(got.get('est'),(int,float)) and isinstance(got.get('se'),(int,float)):
                    e2,s2=got['est'],got['se'];selfrows.append([name,fmt(e2)]+([fmt(s2)] if group=='components' else [])+[f'[{fmt(e2-1.959963984540054*s2)}, {fmt(e2+1.959963984540054*s2)}]'])
                items.append((name,group,e,lo,hi))
            exact('display_'+group,a.get(table),wanted,key)
            exact('display_export_'+group,a.get(table),selfrows,key)
        try:
            svg=ET.fromstring('<svg>'+a['forestMarkup']+'</svg>');lines=svg.findall('line');rects=svg.findall('rect');texts=svg.findall('text')
            exact('plot_line_count',len(lines),len(items)+2,key);exact('plot_rect_count',len(rects),len(items),key)
            exact('plot_labels',[''.join(t.itertext()) for t in texts[:len(items)]],[('[C] ' if g=='components' else '')+n for n,g,*_ in items],key)
            low=min(0,*[v[3] for v in items]);high=max(0,*[v[4] for v in items]);pad=(high-low)*.1 or .5
            xx=lambda x:220+(x-low+pad)/(high-low+2*pad)*350
            for i,((n,g,e,lo,hi),line,rect) in enumerate(zip(items,lines[1:],rects)):
                for q,v in [('x1',xx(lo)),('x2',xx(hi)),('y1',30+i*26),('y2',30+i*26)]:num('plot_CI_'+q,float(line.attrib[q]),v,key+'::'+g+'::'+n)
                for q,v in [('x',xx(e)-4),('y',26+i*26)]:num('plot_point_'+q,float(rect.attrib[q]),v,key+'::'+g+'::'+n)
            exact('plot_viewBox',a['viewBox'],f'0 0 600 {max(220,70+len(items)*26)}',key)
            ck('plot_evidence',True,key)
        except Exception as e:ck('plot_evidence',False,key,str(e),'finite valid SVG')
        if r.get('native'):
            nn=r['native']; dif=[]
            if 'error' not in nn:
                for q in ['Q','df','tau2']:
                    if isinstance(out.get(q),(int,float)) and isinstance(nn.get(q),(int,float)):dif.append(dict(quantity=q,app=out[q],native=nn[q],difference=abs(out[q]-nn[q])/max(1,abs(nn[q]))))
                for g in ['components','combinations']:
                    for name,z in out.get(g,{}).items():
                        for q in ['est','se']:
                            ref=nn.get(g,{}).get(name,{}).get(q);val=z.get(q)
                            if isinstance(val,(int,float)) and isinstance(ref,(int,float)):dif.append(dict(quantity=g+'.'+name+'.'+q,app=val,native=ref,difference=abs(val-ref)/max(1,abs(ref))))
            native.append(dict(key=key,error=nn.get('error'),checks=len(dif),passed=sum(x['difference']<=1e-9 for x in dif),max_difference=max([x['difference'] for x in dif],default=None),comparisons=dif))
    # Every captured real download is checked, including refused configurations.
    expected=a.get('result') or {}
    for action in ['json','csv','md','report-md','report-txt']:
        p=a.get('exports',{}).get(action);exists=bool(p) and Path(p).is_file();ck('export_present_'+action,exists,key)
        if not exists:continue
        text=Path(p).read_text(encoding='utf-8')
        if action=='json':exact('json_export',json.loads(text),expected,key)
        elif action=='csv':
            rows=list(csv.reader(text.splitlines()));actual=rows[1:];wanted=[]
            for k,v in flat(expected):
                value=json.dumps(v,separators=(',',':'),ensure_ascii=False) if isinstance(v,list) else '' if v is None else str(v)
                wanted.append([k,value])
            exact('csv_keys',[x[0] for x in actual],[x[0] for x in wanted],key)
            for (k,v),row in zip(flat(expected),actual):
                if isinstance(v,(int,float)):ck('csv_number',float(row[1])==v,key+'::'+k,row[1],v)
                elif isinstance(v,list):exact('csv_array',json.loads(row[1]),v,key+'::'+k)
                else:exact('csv_scalar',row[1],'' if v is None else str(v),key+'::'+k)
        elif action=='md':
            rows=[line.split('|')[1:-1] for line in text.splitlines()[2:]];vals=[(k.strip(),v.strip()) for k,v in rows]
            exact('md_keys',[k for k,v in vals],[k for k,v in flat(expected)],key)
            for (k,v),(_,value) in zip(flat(expected),vals):
                if isinstance(v,(int,float)):ck('md_number',float(value)==v,key+'::'+k,value,v)
                elif isinstance(v,list):exact('md_array',json.loads(value),v,key+'::'+k)
                else:exact('md_scalar',value,'' if v is None else str(v),key+'::'+k)
        elif action=='report-md':
            md=Path(a['exports']['md']).read_text(encoding='utf-8');ck('report_md_data',md in text if expected else 'No results yet' in text,key)
        else:
            ck('report_txt_data',all(k+': ' in text for k,v in flat(expected)) if expected else 'No results yet' in text,key)
result=dict(variant=variant,checks=sum(x['checks'] for x in stats.values()),passed=sum(x['passed'] for x in stats.values()),quantities=stats,failures=failures,native_summary=dict(configurations=len(native),checks=sum(x['checks'] for x in native),passed=sum(x['passed'] for x in native),errors=sum(bool(x['error']) for x in native)))
Path(f'results-{variant}.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
Path(f'native-{variant}.json').write_text(json.dumps(native,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
lines=[f"{q}: {s['passed']}/{s['checks']} pass; max={s['max_difference']:.12g}; invalid={s['invalid']}" for q,s in sorted(stats.items())]
lines+=[f"{result['passed']}/{result['checks']} checks pass",'Native-study diagnostics (separate): '+str(result['native_summary'])]
Path(f'comparison-{variant}.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8');print('\n'.join(lines))
