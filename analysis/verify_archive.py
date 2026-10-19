"""Fail-closed integrity check of this archive (no R needed).
python analysis/verify_archive.py          verify
python analysis/verify_archive.py --pin    rewrite SOURCE_SHA256.json (maintainer only)"""
import hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {'.git', '__pycache__', '.pytest_cache', 'outputs', '.validate-work'}
THIRD_PARTY = ('bench/node_modules/', 'bench/documentation/')
VERBATIM = ('results/downloads-',)  # real page downloads, kept byte for byte (the CSV export uses CRLF rows)
VERBATIM_CRLF = {'bench/lane-fix.patch'}
TEXT = {'.py', '.r', '.cjs', '.js', '.json', '.md', '.html', '.txt', '.csv', '.cff', '.css', '.patch', '.log', '.mjs'}
ALLOWED = {'<ALLMETA_RELEASE>', '<ALLMETA_RELEASE_DOI>', '<R_LIBS_USER>', '<R_LIBS>', '<R_HOME>', '<AUDIT_ROOT>',
           '<RSCRIPT>', '<RSCRIPT_ALTERNATIVE>'}
MACHINE = [re.compile(r'\b[A-Za-z]:[\\/](?:Users|Projects|claude-temp|Program Files)[\\/]'),
           re.compile(r'/(?:home|mnt/[cdf]|Users)/[^\s"\'<>]+')]
ORIG = 'acd363fa33f0decd2fcafcf08814f663bb9d6178'
FIX = 'f7a78dc542270ca461c3fa0b3fedca5c8e4a62a5'


def source_files():
    out = []
    for d, dirs, names in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in EXCLUDE and not x.startswith('.verify-')]
        out += [Path(d) / n for n in names if n not in {'SOURCE_SHA256.json', 'PROGRESS.md'}]
    return sorted(out)


def rel(p):
    return p.relative_to(ROOT).as_posix()


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def clean_text(name, raw):
    assert not raw.startswith(b'\xef\xbb\xbf'), 'UTF-8 BOM: ' + name
    text = raw.decode('utf-8')
    for m in MACHINE:
        assert not m.search(text), 'Machine path: ' + name
    if not name.startswith(THIRD_PARTY + VERBATIM) and name not in VERBATIM_CRLF:
        assert '\r\n' not in text, 'CRLF line ending: ' + name
        bad = set(re.findall(r'<[A-Z][A-Z0-9_]{2,}>', text)) - ALLOWED
        assert not bad, f'Unknown placeholder {bad}: {name}'


def verify():
    files = source_files()
    pins = load(ROOT / 'SOURCE_SHA256.json')
    got = {rel(p): sha(p) for p in files}
    missing, extra = sorted(set(pins) - set(got)), sorted(set(got) - set(pins))
    changed = sorted(k for k in set(pins) & set(got) if pins[k] != got[k])
    assert not (missing or extra or changed), f'Inventory mismatch: missing={missing[:5]} extra={extra[:5]} changed={changed[:5]}'
    sizes = [p.stat().st_size for p in files]
    assert max(sizes) < 90_000_000 and sum(sizes) < 500_000_000, 'Archive size limit'
    for p in files:
        if p.suffix.lower() in TEXT:
            clean_text(rel(p), p.read_bytes())
    app = load(ROOT / 'app/app-sha256.json')
    assert app['original_commit'] == ORIG and app['patched_commit'] == FIX
    on_disk = {p.relative_to(ROOT / 'app').as_posix(): sha(p) for p in (ROOT / 'app').rglob('*') if p.is_file() and p.name != 'app-sha256.json'}
    assert on_disk == app['files'], 'app/ inventory mismatch'
    for v in ['original', 'patched']:
        page = ROOT / 'app' / v / 'component-nma/index.html'
        for ref in re.findall(r'<(?:script|link)\b[^>]*(?:src|href)=["\']([^"\']+)', page.read_text(encoding='utf-8')):
            assert not re.match(r'https?://', ref), 'Network asset: ' + ref
            assert (page.parent / ref).resolve().is_file(), f'Missing page asset {v}: {ref}'
    # The complete fix replays exactly: app/original + bench/branch.patch == app/patched.
    with tempfile.TemporaryDirectory(prefix='cnma-verify-') as tmp:  # outside any git work tree
        t = Path(tmp)
        for f in ['component-nma/index.html', 'component-nma/README.md']:
            (t / f).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / 'app/original' / f, t / f)
        r = subprocess.run(['git', '-c', 'core.autocrlf=false', '-c', 'core.eol=lf', 'apply', str(ROOT / 'bench/branch.patch')], cwd=t, capture_output=True, text=True)
        assert r.returncode == 0, 'branch.patch does not apply: ' + r.stderr
        for f in ['component-nma/index.html', 'component-nma/README.md']:
            assert (t / f).read_bytes() == (ROOT / 'app/patched' / f).read_bytes(), 'Patch replay differs: ' + f
    corpus = load(ROOT / 'data/corpus.json') + load(ROOT / 'data/focused-corpus.json')
    keys = [c['key'] for c in corpus]
    assert len(keys) == len(set(keys)), 'Duplicate corpus key'
    for n in ['results/reference.json', 'results/app-original.json', 'results/app-patched.json']:
        k = [x['key'] for x in load(ROOT / n)]
        assert len(k) == len(set(k)) and set(k) == set(keys), 'Coverage: ' + n
    for v in ['original', 'patched']:
        app_v = load(ROOT / f'results/app-{v}.json')
        downloads = [p for a in app_v for p in a.get('exports', {}).values()]
        assert len(downloads) == 5 * len(keys) == len(set(downloads)), 'Download coverage: ' + v
        assert all((ROOT / 'results' / p).is_file() for p in downloads), 'Missing download: ' + v
    exp = load(ROOT / 'expected/paper_values.json')
    for v in ['original', 'patched']:
        r = load(ROOT / f'results/results-{v}.json')
        assert (r['passed'], r['checks']) == (exp[v]['passed'], exp[v]['checks']), 'Expected totals: ' + v
        assert {q: (s['checks'], s['passed']) for q, s in r['quantities'].items()} == {q: (s['checks'], s['passed']) for q, s in exp[v]['quantities'].items()}
    assert exp['patched']['passed'] == exp['patched']['checks'], 'Patched page does not pass every check'
    for name in ['README.md', 'CITATION.cff', '.zenodo.json']:
        text = (ROOT / name).read_text(encoding='utf-8')
        assert '<ALLMETA_RELEASE>' in text and '<ALLMETA_RELEASE_DOI>' in text, 'Release tokens missing: ' + name
        assert FIX[:7] in text and ORIG[:7] in text, 'Provenance commits missing: ' + name
    print(f'ARCHIVE PASS: {len(files)} source files; inventory, coverage, patch replay, expected counts verified', flush=True)


if __name__ == '__main__':
    if '--pin' in sys.argv:
        pins = {rel(p): sha(p) for p in source_files()}
        (ROOT / 'SOURCE_SHA256.json').write_text(json.dumps(pins, indent=1, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
        print('PINNED', len(pins))
    else:
        verify()
