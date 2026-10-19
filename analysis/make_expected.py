"""Pin the archive's counts in expected/paper_values.json (every number in the paper is read from here
or from the files it names). Usage: python analysis/make_expected.py [archive-root]"""
import json, csv, sys, collections
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
R = ROOT / 'results'
D = ROOT / 'data'


def load(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def rows(n):
    with (D / n).open(encoding='utf-8') as f:
        return list(csv.DictReader(f))


out = {}
for v in ['original', 'patched']:
    r = load(R / f'results-{v}.json')
    out[v] = dict(checks=r['checks'], passed=r['passed'],
                  quantities={q: dict(checks=s['checks'], passed=s['passed'], max_difference=s['max_difference'])
                              for q, s in sorted(r['quantities'].items())},
                  native_summary=r['native_summary'], display_zero_normalised=len(r.get('display_zero_normalised', [])))
bus = load(R / 'bus-results.json')
out['bus'] = {v: dict(checks=bus[v]['checks'], passed=bus[v]['passed']) for v in bus}
st = load(R / 'static-tests.json')
out['static_tests'] = {v: dict(checks=sum(t['variant'] == v for t in st['tests']), passed=sum(t['variant'] == v and t['passed'] for t in st['tests'])) for v in ['original', 'patched']}
wb = load(R / 'wrapper-bridge.json')
out['wrapper_bridge'] = dict(checks=wb['checks'], passed=wb['passed'])
ref = load(R / 'reference.json')
status = collections.Counter(x['status'] for x in ref)
reasons = collections.Counter(x.get('reason') for x in ref if x['status'] == 'refused')
corpus = load(D / 'corpus.json')
focused = load(D / 'focused-corpus.json')
cfg = rows('configuration-ledger.csv')
dsl = rows('dataset-ledger.csv')
cat = rows('installed-data-catalogue.csv')
included = sorted({(r['package'], r['dataset']) for r in cfg})
out['corpus'] = dict(
    catalogue_entries=len(cat), dataset_ledger_rows=len(dsl), included_datasets=len(included),
    included_packages=sorted({p for p, _ in included}), configurations=len(corpus), focused_cases=len(focused),
    reference_configurations=len(ref), reference_ok=status['ok'], reference_refused=status['refused'],
    reference_error=status.get('error', 0), refusal_reasons=dict(reasons),
    two_arm_only=sum(r['subset'] == 'two-arm-only' for r in cfg), full=sum(r['subset'] == 'full' for r in cfg),
    with_repeated_study_ids=sum('multi-arm rows treated independently' in r['dependence'] for r in cfg),
    split_mouth=sum('split-mouth' in r['dependence'] for r in cfg),
    max_rows=max(len(c['rows']) for c in corpus + focused if c.get('rows')),
)
(ROOT / 'expected').mkdir(exist_ok=True)
(ROOT / 'expected/paper_values.json').write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8', newline='\n')
print('EXPECTED pinned:', {v: f"{out[v]['passed']}/{out[v]['checks']}" for v in ['original', 'patched']})
