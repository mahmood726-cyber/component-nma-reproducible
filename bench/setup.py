import pathlib, shutil, re, hashlib, json, subprocess
root=pathlib.Path(__file__).resolve().parent
source=root/'allmeta'
out=root/'app-original'
paths={'component-nma/index.html','component-nma/README.md','LICENSE'}
paths.add('hub/shared/vendor/jspdf.min.js')  # lazy-loaded by chart-export-auto
html=(source/'component-nma/index.html').read_text(encoding='utf-8')
paths.update(p[3:] for p in re.findall(r'(?:src|href)="(\.\./[^"?#]+\.(?:js|css))"',html))
paths.update(p.relative_to(source).as_posix() for p in (source/'component-nma/tests').rglob('*') if p.is_file())
for p in sorted(paths):
    (out/p).parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(source/p,out/p)
manifest={p:hashlib.sha256((out/p).read_bytes()).hexdigest() for p in sorted(paths)}
(root/'source-manifest.json').write_text(json.dumps({'commit':subprocess.check_output(['git','-C',str(source),'rev-parse','HEAD'],text=True).strip(),'files':manifest},indent=2)+'\n')
(root/'documentation').mkdir(exist_ok=True)
shutil.copyfile(source/'hub/shared/tests/component-nma-parity.spec.mjs',root/'documentation/component-nma-parity.spec.mjs')
print('Copied',len(manifest),'source files')
