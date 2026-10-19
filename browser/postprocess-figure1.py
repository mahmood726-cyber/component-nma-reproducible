import json,sys
from pathlib import Path
from PIL import Image
F=Path(r'<AUDIT_ROOT>\fig');A=Path(r'<AUDIT_ROOT>\component-nma-reproducible')
AP={c['key']:c for c in json.loads((A/'results/app-patched.json').read_text(encoding='utf-8'))}
log=json.loads((F/'p19_shots_log.json').read_text(encoding='utf-8'))
lines=[]
for n,run in log['runs'].items():
    a=AP[run['key']]
    same=run['result']==a['result'] and run['componentTable']==a['componentTable'] and run['combinationTable']==a['combinationTable']
    lines.append(f"{n} {run['key']}: browser result/tables == archived app-patched.json: {same}; toasts={run['toasts']}")
    assert same or (run['result'] is None and a['result'] is None and run['componentTable']==[]==a['componentTable']),n
lines.append(f"refusal toast: {log['refusal_toast']}; cleared after refusal: {log['cleared']}")
lines.append(f"browser {log['browser']}; console: {log['console']}")
(F/'figure_vs_archive.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines))
MAXW=3000;rep={}
for p in sorted(F.glob('p19_*.png')):
    if p.stem.endswith('_300'):continue
    im=Image.open(p).convert('RGB')
    if im.width>MAXW: im=im.resize((MAXW,round(im.height*MAXW/im.width)),Image.LANCZOS)
    im.save(F/(p.stem+'.png'),dpi=(300,300),optimize=True)
    im.save(F/(p.stem+'.tif'),compression='tiff_lzw',dpi=(300,300))
    t=Image.open(F/(p.stem+'.tif'));q=Image.open(F/(p.stem+'.png'))
    assert t.mode=='RGB' and t.info.get('compression')=='tiff_lzw' and all(abs(float(x)-300)<1e-6 for x in t.info['dpi'])
    assert t.convert('RGB').tobytes()==q.convert('RGB').tobytes()
    rep[p.stem]=dict(w=im.width,h=im.height,tif_mode=t.mode,tif_compression=t.info.get('compression'),tif_dpi=[float(x) for x in t.info['dpi']],png_dpi=[round(float(x),3) for x in q.info['dpi']],print_width_mm=round(im.width/300*25.4,1))
(F/'tif_report.json').write_text(json.dumps(rep,indent=1),encoding='utf-8');print(json.dumps(rep,indent=0))
