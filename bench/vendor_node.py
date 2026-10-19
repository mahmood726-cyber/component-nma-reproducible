import json,shutil
from pathlib import Path
src=Path('../P17/node_modules');dst=Path('node_modules');seen=set()
def copy(name):
    if name in seen:return
    seen.add(name);p=src/name;q=dst/name
    shutil.copytree(p,q,dirs_exist_ok=True)
    for dep in json.loads((p/'package.json').read_text(encoding='utf-8')).get('dependencies',{}):copy(dep)
copy('linkedom')
Path('node-dependencies.json').write_text(json.dumps({n:json.loads((dst/n/'package.json').read_text(encoding='utf-8'))['version'] for n in sorted(seen)},indent=2)+'\n')
print('Vendored',len(seen),'offline Node dependencies')
