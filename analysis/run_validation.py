"""Fresh full R refit + comparison (called by validate.R). No archived R result seeds this run:
reference.R and bus_reference.R start in an empty .validate-work with only the corpora.
Usage: python analysis/run_validation.py <Rscript>"""
import json, math, shutil, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def run(cmd, cwd, log):
    with open(log, 'w', encoding='utf-8') as f:
        r = subprocess.run(cmd, cwd=cwd, stdout=f, stderr=subprocess.STDOUT)
    text = Path(log).read_text(encoding='utf-8', errors='replace')
    if r.returncode:
        print(text[-3000:])
        raise SystemExit(f'Command failed ({r.returncode}): {" ".join(map(str, cmd))}')
    return text


def numbers(x, path=''):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from numbers(v, path + '.' + k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from numbers(v, f'{path}[{i}]')
    else:
        yield path, x


def main():
    start = time.monotonic()
    rscript = sys.argv[1]
    work = ROOT / '.validate-work'
    if work.exists():
        raise SystemExit('Existing .validate-work refused; move it aside before repeating a full run')
    work.mkdir()
    for n in ['reference.R', 'bus_reference.R', 'r_session.R', 'json17.R']:
        shutil.copyfile(ROOT / 'bench' / n, work / n)
    for n in ['corpus.json', 'focused-corpus.json', 'bus-corpus.json']:
        shutil.copyfile(ROOT / 'data' / n, work / n)
    assert not (work / 'reference.json').exists()
    t0 = time.monotonic()
    log = run([rscript, '--vanilla', 'reference.R'], work, work / 'reference.log')
    r_seconds = time.monotonic() - t0
    print([l for l in log.splitlines() if l.startswith('REFERENCE')][-1], flush=True)
    log = run([rscript, '--vanilla', 'bus_reference.R'], work, work / 'bus_reference.log')
    print([l for l in log.splitlines() if l.startswith('BUS REFERENCE')][-1], flush=True)

    # Fresh R refit versus the archived R reference: identical statuses/reasons/structure, numbers <= 1e-12.
    fresh = {x['key']: x for x in load(work / 'reference.json')}
    arch = {x['key']: x for x in load(ROOT / 'results/reference.json')}
    assert set(fresh) == set(arch), 'Fresh reference keys differ from archived reference'
    worst, nnum, structural = 0.0, 0, 0
    for k in arch:
        a, f = dict(numbers(arch[k])), dict(numbers(fresh[k]))
        if set(a) != set(f):
            structural += 1
            continue
        for p, v in a.items():
            w = f[p]
            if isinstance(v, (int, float)) and not isinstance(v, bool) and isinstance(w, (int, float)) and not isinstance(w, bool):
                nnum += 1
                if math.isfinite(v) and math.isfinite(w):
                    worst = max(worst, abs(v - w) / max(1, abs(v)))
                elif not (v == w):
                    structural += 1
            elif v != w:
                structural += 1
    print(f'FRESH vs ARCHIVED R REFERENCE: {len(arch)} configurations, {nnum} numbers, max scaled difference {worst:.3g}, structural differences {structural}', flush=True)
    assert structural == 0 and worst <= 1e-12, 'Fresh R refit does not reproduce the archived reference'

    fresh_out = ROOT / 'outputs/fresh'
    fresh_out.mkdir(parents=True, exist_ok=True)
    exp = load(ROOT / 'expected/paper_values.json')
    ok = True
    for v in ['original', 'patched']:
        r = subprocess.run([sys.executable, str(ROOT / 'analysis/compare.py'), v, str(work / 'reference.json'), str(fresh_out), str(ROOT)], capture_output=True, text=True)
        if r.returncode:
            print(r.stdout[-2000:], r.stderr[-2000:])
            raise SystemExit('compare.py failed: ' + v)
        res = load(fresh_out / f'results-{v}.json')
        for q, s in sorted(res['quantities'].items()):
            e = exp[v]['quantities'].get(q)
            same = e is not None and (s['checks'], s['passed']) == (e['checks'], e['passed'])
            ok &= same
            print(f'{v} {q}: {s["passed"]}/{s["checks"]}, maximum {s["max_difference"]:.3g}{"" if same else "  <-- differs from expected"}', flush=True)
        ok &= set(res['quantities']) == set(exp[v]['quantities'])
        ok &= (res['passed'], res['checks']) == (exp[v]['passed'], exp[v]['checks'])
        print(f'{v}: {res["passed"]}/{res["checks"]} checks pass', flush=True)
    r = subprocess.run([sys.executable, str(ROOT / 'analysis/compare_bus.py'), str(work / 'bus-reference.json'), str(fresh_out), str(ROOT)], capture_output=True, text=True)
    print(r.stdout.strip(), flush=True)
    bus = load(fresh_out / 'bus-results.json')
    ok &= r.returncode == 0 and all((bus[v]['checks'], bus[v]['passed']) == (exp['bus'][v]['checks'], exp['bus'][v]['passed']) for v in exp['bus'])
    patched = load(fresh_out / 'results-patched.json')
    ok &= patched['passed'] == patched['checks']
    seconds = time.monotonic() - start
    (ROOT / 'outputs/validate_runtime.json').write_text(json.dumps(dict(seconds=round(seconds, 1), r_reference_seconds=round(r_seconds, 1), configurations=len(arch), r_processes=1, exit_code=0 if ok else 1), indent=2) + '\n', encoding='utf-8', newline='\n')
    if not ok:
        raise SystemExit('VALIDATION FAILED: counts differ from expected/paper_values.json')
    print(f'{patched["passed"]}/{patched["checks"]} checks pass', flush=True)


if __name__ == '__main__':
    main()
