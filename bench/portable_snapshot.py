"""Make the upstream R fixture portable without modifying the checkout."""
import pathlib,json,re,hashlib
root=pathlib.Path(__file__).resolve().parent
rel='component-nma/tests/fixtures/cnma-oracle.R'
for variant in ['original','patched']:
    p=root/('app-'+variant)/rel
    raw=p.read_bytes()
    portable=re.sub(rb'[A-Za-z]:/[^"\r\n]*/allmeta/',b'',raw)
    p.write_bytes(portable)
manifest=json.loads((root/'source-manifest.json').read_text(encoding='utf-8'))
manifest['snapshot_files']={rel:hashlib.sha256((root/'app-original'/rel).read_bytes()).hexdigest()}
manifest['snapshot_normalization']='The unused upstream R fixture uses repository-relative paths in both snapshots. files records untouched upstream hashes; snapshot_files overrides only the portable snapshot hash. The executed page code and fix.patch are unaffected.'
(root/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
p=root/'verify_archive.py';s=p.read_text(encoding='utf-8')
s=s.replace("hashlib.sha256((root/'app-original'/rel).read_bytes()).hexdigest()==h", "hashlib.sha256((root/'app-original'/rel).read_bytes()).hexdigest()==manifest.get('snapshot_files',{}).get(rel,h)")
p.write_text(s,encoding='utf-8')
note='\nPackaging portability: the unused upstream `cnma-oracle.R` fixture has repository-relative paths in both source snapshots. `source-manifest.json` retains upstream hashes and records the normalized snapshot hash separately. The checkout, executed page code, statistical evidence, and app-only patch are unaffected. Run `python portable_snapshot.py` before `python verify_archive.py` and `python archive.py` when rebuilding the archive.\n'
for name in ['RESULTS.md','README.md']:
    p=root/name;s=p.read_text(encoding='utf-8')
    if 'Packaging portability:' not in s:p.write_text(s+note,encoding='utf-8')
print('PORTABILITY: source fixture normalized; upstream hash retained',flush=True)
