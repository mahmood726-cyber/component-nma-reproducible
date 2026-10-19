import runpy,json
from pathlib import Path
checks=[]
for variant in ['original','patched']:
    for p in sorted(Path(f'app-{variant}/component-nma/tests').glob('test_*.py')):
        scope=runpy.run_path(str(p))
        for name,fn in scope.items():
            if name.startswith('test_') and callable(fn):
                error=None
                try:fn()
                except Exception as e:error=str(e)
                checks.append(dict(variant=variant,file=p.as_posix(),test=name,passed=error is None,error=error))
result=dict(runner='stdlib runpy: execute shipped standalone assertion functions; pytest unavailable',checks=len(checks),passed=sum(x['passed'] for x in checks),tests=checks)
Path('static-tests.json').write_text(json.dumps(result,indent=2)+'\n');print(f"SHIPPED STATIC TESTS: {result['passed']}/{result['checks']} pass")
