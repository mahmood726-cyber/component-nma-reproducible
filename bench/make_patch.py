import pathlib,shutil,difflib
src=pathlib.Path('app-original');dst=pathlib.Path('app-patched')
shutil.copytree(src,dst,dirs_exist_ok=True)
p=dst/'component-nma/index.html';s=p.read_text(encoding='utf-8')
start=s.index('    function parse(text) {');end=s.index('\n    // --- matrix math',start)
s=s[:start]+'''    function parse(text) {
      return text.trim().split(/\\n/).filter(l => l.trim()).map(l => {
        const parts = l.split(/\\|/).map(s => s.trim());
        if (parts.length !== 4 || parts.some(s => !s)) throw new Error("Invalid contrast input.");
        const te = Number(parts[2]), se = Number(parts[3]);
        if (!Number.isFinite(te) || !Number.isFinite(se) || se <= 0) throw new Error("Invalid contrast input.");
        const splitArm = s => {
          if (s.toLowerCase() === "control") return [];
          const a = s.split(/\\s*\\+\\s*/).map(c => c.toLowerCase());
          if (a.some(c => !c) || new Set(a).size !== a.length) throw new Error("Invalid contrast input.");
          return a;
        };
        const A = splitArm(parts[0]), B = splitArm(parts[1]);
        if (A.slice().sort().join("+") === B.slice().sort().join("+")) throw new Error("Invalid contrast input.");
        return { A, B, te, se };
      });
    }
''' + s[end:]
# Structural rank is determined before weighting: integer component incidence
# must not become "identifiable" due to roundoff in a singular normal matrix.
target='      const y = rows.map(r => r.te);'
s=s.replace(target,'''      const rankWork = X.map(r => r.slice());
      let rank = 0;
      for (let j = 0; j < p && rank < rows.length; j++) {
        let pivot = rank;
        for (let i = rank + 1; i < rows.length; i++) if (Math.abs(rankWork[i][j]) > Math.abs(rankWork[pivot][j])) pivot = i;
        if (Math.abs(rankWork[pivot][j]) < 1e-12) continue;
        [rankWork[rank], rankWork[pivot]] = [rankWork[pivot], rankWork[rank]];
        for (let i = rank + 1; i < rows.length; i++) {
          const v = rankWork[i][j] / rankWork[rank][j];
          for (let k = j; k < p; k++) rankWork[i][k] -= v * rankWork[rank][k];
        }
        rank++;
      }
      if (!p || rank < p) throw new Error("Components are not identifiable from the contrasts.");
''' + target)
s=s.replace('const df = Math.max(1, rows.length - p);','const df = rows.length - p;')
s=s.replace('const tau2 = denom <= 1e-12 ? 0 : Math.max(0, (Q - df) / denom);','const tau2 = df === 0 ? null : (denom <= 1e-12 ? 0 : Math.max(0, (Q - df) / denom));')
start=s.index('    function run() {');end=s.index('\n      // Component table',start)
s=s[:start]+'''    function clearResults() {
      _lastCnma = null;
      for (const id of ["comp-body", "int-body", "forest"]) document.getElementById(id).innerHTML = "";
    }
    function escapeLabel(s) {
      return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;");
    }
    function run() {
      clearResults();
      let rows, f;
      try {
        rows = parse(document.getElementById("src").value);
        if (rows.length < 2) throw new Error("At least 2 valid contrasts are required.");
        f = fit(rows);
      } catch (e) {
        if (window.Toast) window.Toast.show(e.message, "warn");
        return;
      }
''' + s[end:]
s=s.replace('${r.name}', '${escapeLabel(r.name)}')
s=s.replace('if (!env || !Array.isArray(env.studies) || !env.studies.length) { notify(', 'if (!env || !Array.isArray(env.studies) || !env.studies.length) { clearResults(); notify(')
s=s.replace('      var rows = MaComparisons.toContrasts(env);','''      if (env.studies.some(s => Array.isArray(s.arms) && s.arms.length > 2) || new Set(env.studies.map(s => s.id)).size !== env.studies.length) {
        clearResults(); notify("Multi-arm or repeated-study bus inputs are unsupported: contrast covariance is required."); return;
      }
      var rows = MaComparisons.toContrasts(env);''')
s=s.replace('if (!rows.length) { notify(', 'if (!rows.length) { clearResults(); notify(')
s=s.replace('The model estimates one effect per component;', 'The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component;')
s=s.replace('For multi-arm trials with the correct correlation, use', 'The bus importer refuses multi-arm trials; pasted rows must be independent two-arm contrasts. For multi-arm trials with the correct correlation, use')
s=s.replace('Use <code>control</code> for no intervention.', 'Use <code>control</code> for no intervention. Labels are case-insensitive. Empty or repeated components and malformed rows are refused. At least two contrasts and an identifiable component design are required. With zero residual degrees of freedom, heterogeneity is not estimable (exported as null); effects use sampling variances.')
p.write_bytes(s.replace(chr(10),chr(13)+chr(10) if b'\r\n' in (src/p.relative_to(dst)).read_bytes() else chr(10)).encode('utf-8'))
p=dst/'component-nma/README.md';s=p.read_text(encoding='utf-8');s=s.replace('multi-arm trials in NMA shape — multiple rows per study, one per arm.', 'independent two-arm contrasts: component labels for A and B, effect, and SE. Multi-arm bus imports are refused; pasted rows carry no study identifier.')
s=s.replace('- Receipts and JSON exports include `producedBy` (app version, git SHA, build timestamp) — see `shared/build-info.js`.', '- Results export as JSON, CSV, Markdown, and Methods+Results reports. This page does not attach build metadata or a signed receipt.')
s='\n'.join(line for line in s.split('\n') if 'Shinylive' not in line)
s+='''
## Statistical scope

One additive random-effects model is fitted with a generalized DL moment
estimator and normal 95% intervals. Only the whole label `control` denotes an
empty intervention; `+` splits other labels into lowercase components. The
component contrast design must have full column rank, even for disconnected
treatment networks. There is no common-effect selector, p-value display,
standard NMA comparison, or additivity-difference test. Q, its residual df,
and tau-squared are exposed in data exports. Zero residual df gives null tau2
and sampling-variance effect intervals. Failed inputs clear tables, plot and
export state. JSON/CSV/Markdown and prose reports are generic results exports;
this page does not supply a signed receipt or build-identity field.
'''
p.write_bytes(s.replace(chr(10),chr(13)+chr(10) if b'\r\n' in (src/p.relative_to(dst)).read_bytes() else chr(10)).encode('utf-8'))
patch=''
for p in sorted(dst.rglob('*')):
 if p.is_file():
  rel=p.relative_to(dst).as_posix();before=(src/rel).read_bytes();after=p.read_bytes()
  if before!=after:patch+=''.join(difflib.unified_diff(before.decode('utf-8').splitlines(True),after.decode('utf-8').splitlines(True),fromfile='a/'+rel,tofile='b/'+rel))
pathlib.Path('fix.patch').write_text(patch,encoding='utf-8',newline='\n')
print('App-only patch written')
