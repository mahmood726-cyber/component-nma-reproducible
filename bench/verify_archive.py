import json,csv,hashlib,pathlib,subprocess,uuid,shutil
root=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((root/n).read_text(encoding='utf-8'))
checks=[]
def check(n,ok,detail=None):checks.append(dict(check=n,passed=bool(ok),detail=detail))
manifest=load('source-manifest.json')
for rel,h in manifest['files'].items():
    check('original_hash:'+rel,hashlib.sha256((root/'app-original'/rel).read_bytes()).hexdigest()==manifest.get('snapshot_files',{}).get(rel,h))
    if (root/'allmeta'/rel).exists():check('checkout_hash:'+rel,hashlib.sha256((root/'allmeta'/rel).read_bytes()).hexdigest()==h)
corpus=load('corpus.json')+load('focused-corpus.json');keys=[c['key'] for c in corpus]
check('corpus_unique',len(keys)==len(set(keys)))
for name in ['reference.json','app-original.json','app-patched.json']:
    found=[x['key'] for x in load(name)];check(name+':unique',len(found)==len(set(found)));check(name+':coverage',set(found)==set(keys))
for name in ['dataset-ledger.csv','configuration-ledger.csv']:
    data=list(csv.DictReader((root/name).open(encoding='utf-8')))
    found=[r['key'] if 'key' in r else r['package']+'::'+r['dataset'] for r in data]
    check(name+':unique',len(found)==len(set(found)))
    if 'configuration' in name:check(name+':coverage',set(found)=={c['key'] for c in load('corpus.json')})
check('reference_no_errors',all(r['status'] in ['ok','refused'] for r in load('reference.json')))
check('construction_no_errors',not any(x['error'] for x in load('construction-attempts.json')))
for variant in ['original','patched']:
    app=load('app-'+variant+'.json');runtime=load('runtime-'+variant+'.json')
    check('default_uninstrumented:'+variant,runtime['defaultResult']==next(a['result'] for a in app if a['key']=='focused::built-in'))
    downloads=[p for a in app for p in a.get('exports',{}).values()]
    check('download_count:'+variant,len(downloads)==5*len(keys));check('download_unique:'+variant,len(downloads)==len(set(downloads)));check('downloads_exist:'+variant,all((root/p).is_file() for p in downloads))
check('wrapper_bridge',load('wrapper-bridge.json')['passed']==load('wrapper-bridge.json')['checks'])
check('patched_bus',load('bus-results.json')['patched']['passed']==load('bus-results.json')['patched']['checks'])
check('static_tests',load('static-tests.json')['passed']==load('static-tests.json')['checks'])
replay=root/('patch-replay-'+uuid.uuid4().hex[:10]);replay.mkdir()
shutil.copytree(root/'app-original',replay,dirs_exist_ok=True)
for mode in ['--check',None]:
    args=['git','-C',str(replay),'apply','--whitespace=nowarn']+([mode] if mode else [])+[str(root/'fix.patch')]
    result=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',errors='replace');check('patch_'+('check' if mode else 'apply'),result.returncode==0,result.stderr.replace(str(root),'<AUDIT_ROOT>'))
for rel in manifest['files']:check('patch_replay:'+rel,(replay/rel).read_bytes()==(root/'app-patched'/rel).read_bytes())
result=dict(checks=len(checks),passed=sum(x['passed'] for x in checks),checks_detail=checks)
(root/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f"INTEGRITY: {result['passed']}/{result['checks']} checks pass")
if result['passed']!=result['checks']:raise SystemExit(1)
