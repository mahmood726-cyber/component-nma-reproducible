import json,csv,hashlib,copy,re
from pathlib import Path
def write(name,x): Path(name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
base=json.loads(Path('network-corpus.json').read_text(encoding='utf-8'))
expanded=[]
for item in base:
    item['component_mapping']={};item['label_mode']='original'
    expanded.append(item)
    mapping={}
    for label in {r[k] for r in item['rows'] for k in ['A','B']}:
        if item['dataset'].lower().removeprefix('dat.')=='dong2013' and label=='LABA-ICS':mapping[label]='LABA+ICS'
        if item['dataset'] in ['dat.hartmannboyce2018','dat.nissen2007'] and ' and ' in label and not any(s in label for s in [' or ','with or without']):
            mapping[label]=re.sub(r',? and ', '+',label).replace(', ','+')
    if mapping:
        c=copy.deepcopy(item);c['component_mapping']=mapping;c['label_mode']='explicit-combinations';c['key']+='::explicit-combinations'
        for r in c['rows']:
            for k in ['A','B']:r[k]=mapping.get(r[k],r[k])
        expanded.append(c)
base=expanded
corpus=[]
for item in base:
    labels=sorted({r[k] for r in item['rows'] for k in ['A','B']})
    refs=[x for x in labels if x.lower() in ['placebo','plac','p','placebo/control','control/placebo','no treatment','no_contact','flap op','hand vein','wait list','ut']]
    short=item['dataset'].lower().removeprefix('dat.')
    if short in ['franchini2012','parkinson','dietaryfat'] and '1' in labels: refs=['1']
    if item['package'] in ['mixmeta','mvmeta'] and short=='smoking': refs=['a']
    if short in ['smokingcessation','hasselblad1998'] and 'A' in labels: refs=['A']
    for ref in [None,*refs]:
        c=copy.deepcopy(item);c['encoding']='source-labels' if ref is None else 'inactive='+ref
        c['key']+='::'+c['encoding'];c['inactive_mapping']=ref
        if ref is not None:
            for r in c['rows']:
                for k in ['A','B']:
                    if r[k]==ref:r[k]='control'
        c['text']='\n'.join(' | '.join([r['A'],r['B'],repr(r['te']),repr(r['se'])]) for r in c['rows'])
        c['input_sha256']=hashlib.sha256(c['text'].encode()).hexdigest()
        c['dependence']='multi-arm rows treated independently by page' if c['multiarm_studies'] else 'no multi-arm studies'
        if short=='su2018': c['dependence']+='; includes split-mouth designs (page cannot model covariance)'
        corpus.append(c)
write('corpus.json',corpus)
ledger=json.loads(Path('dataset-ledger.json').read_text(encoding='utf-8'))
for x in ledger:
    x['configurations']=sum(c['package']==x['package'] and c['dataset']==x['dataset'] for c in corpus)
    x['decision']='included' if x['configurations'] else 'excluded'
    x['documentation']=f"documentation/{x['package']}-{x['dataset']}.txt"
    if not x['configurations']:x['reason']=x['title']+'; no documented multi-treatment network with compatible aggregate arm/contrast data in this dataset; see installed schema and help'
known={(x['package'],x['dataset']) for x in ledger}
for x in csv.DictReader(Path('installed-data-catalogue.csv').open(encoding='utf-8')):
    if (x['Package'],x['Item']) not in known:
        ledger.append(dict(package=x['Package'],dataset=x['Item'],decision='excluded',configurations=0,documentation='installed-data-catalogue.csv',reason=x['Title']+'; catalogue screen: diagnostic accuracy, individual-level, general statistical illustration, or non-network data outside aggregate intervention-network scope'))
write('dataset-ledger.json',ledger)
with Path('dataset-ledger.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['package','dataset','decision','configurations','reason','documentation']);w.writeheader();w.writerows({k:x[k] for k in w.fieldnames} for x in ledger)
with Path('configuration-ledger.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['key','package','dataset','outcome','measure','subset','model','label_mode','encoding','dependence','input_sha256','rows','recipe']);w.writeheader();w.writerows({**{k:c.get(k) for k in w.fieldnames},'rows':len(c['rows'])} for c in corpus)
print(f"{len(corpus)} configurations; {sum(x['decision']=='included' for x in ledger)} datasets included / {len(ledger)} catalogue entries")
