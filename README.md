# Additive component network meta-analysis in the browser: validation of the allmeta component-nma app against netmeta

Validated original page: allmeta commit acd363f (acd363fa33f0decd2fcafcf08814f663bb9d6178); component-nma and every file it loads are unchanged on main da66b89. Corrections: pull request #153, branch fix/component-nma-validate, head f7a78dc (f7a78dc542270ca461c3fa0b3fedca5c8e4a62a5), not yet merged. Release containing the corrections: allmeta <ALLMETA_RELEASE>, DOI <ALLMETA_RELEASE_DOI>. Upstream: https://github.com/mahmood726-cyber/allmeta.

R 4.6.0, netmeta 3.7.0, meta 8.5.0, metafor 5.2-1 (packageVersion 5.2.1), metadat 1.6-0, jsonlite 2.0.0; corpus construction also used metabook 0.2.0, mixmeta 1.2.2 and mvmeta 1.0.3. The installed data catalogue (639 entries) was screened; 54 package datasets supply 576 configurations, plus 19 focused cases, 595 in all. The R reference fits 330 and refuses 265 (256 unidentifiable component designs, 2 with fewer than two contrasts, 7 invalid inputs). Package examples are software fixtures, not clinical analyses.

Original page: **88736/91238** checks pass. Corrected page: **72150/72150**. Bus-import checks: 49/63 original, 63/63 corrected. The denominators differ because failed fits on the original page exported stale results that are counted; the corrected page clears them.

## Reproduce

Requires R and the package versions above (no downloads), Python 3 (standard library only) and git. Set R_LIBS_USER (and R_LIBS if needed) to the library holding them and R_ENVIRON_USER to an empty file. From this archive root:

```text
python analysis/verify_archive.py
Rscript validate.R
```

validate.R checks versions and SHA-256 of every input, then refits all 595 configurations in a fresh `.validate-work` with the archived bench/reference.R (one R process; no archived R result is read), checks that the fresh refit reproduces results/reference.json, recomputes the bus-import reference, compares both page captures against the fresh reference and prints per-quantity counts and `72150/72150 checks pass`. It exits non-zero on wrong versions, an inventory mismatch, missing or extra coverage, or any count that differs from expected/paper_values.json. An existing `.validate-work` is refused; move it aside before repeating. The refit pins R's collation to C, the order in which the page's JavaScript sorts component names; under a locale collation, names such as `lidocaine pretreatment` and `lidocaine-propofol admixture` (metabook Jalota2011) sort differently and the design checks fail.

The page captures are archived observations. To regenerate them, copy data/corpus.json, data/focused-corpus.json, data/bus-corpus.json and bench/run_node.cjs into an empty folder with `app-original/` and `app-patched/` (copies of app/original and app/patched) and a `node_modules` copy of bench/node_modules, then run `node run_node.cjs original` and `node run_node.cjs patched` (Node 24; linkedom from bench/node_modules, offline).

## Layout

- app/: the page and every file it loads, as git blob bytes (LF), at acd363f (original) and f7a78dc (patched), with the shipped tests and app-sha256.json. The upstream cnma-oracle.R fixture contains a machine path; the lane's portable snapshot is used (noted in app-sha256.json).
- data/: corpus (every configuration's contrast rows and source recipe), focused and bus cases, installed-data catalogue, dataset, configuration and refusal ledgers, row exclusions, construction attempts, source manifest and versions.
- results/: page captures (app-*.json, bus-*.json, runtime-*.json) and the five real downloads per configuration (downloads-*/) captured from app/ bytes; the archived R reference (reference.json, bus-reference.json), the public-wrapper bridge (wrapper-reference.json, wrapper-bridge.json: 2064/2064), comparison outputs, native-study diagnostics and shipped static tests.
- expected/paper_values.json: pinned counts, recomputed by analysis/make_expected.py.
- analysis/: compare.py and compare_bus.py (the lane's comparison logic with parameterised paths), run_validation.py, verify_archive.py, make_expected.py.
- bench/: the validation lane's scripts, logs and reports (LANE_RESULTS.md, AUDIT_SCOPE.md), lane-fix.patch (verbatim, for CRLF working copies), branch.patch (complete correction, LF), signed-zero.patch (the display fix added after the lane), installed package documentation and the offline Node dependencies with their licences.
- SOURCE_SHA256.json inventories every file except outputs/ and .git.

## Method and limits

The page fits one additive random-effects model (generalized DerSimonian–Laird τ², normal 95% intervals) to independent two-arm contrasts; labels split on `+`, and only the whole label `control` is the empty set. The reference calls the installed, unmodified `netmeta:::prepare` and `netmeta:::nma_additive`, the implementation behind netcomb/discomb, bypassing only the standard-NMA decomposition the page does not report; 45 public-wrapper cases bridge it (2064/2064). The page's own scripts run in Node.js with linkedom. Tolerance is 1e-9 relative to max(1, |R|); df, membership, refusals and displayed strings are exact.

Display rule: the corrected page shows floating-point roundoff of an exact zero (|x| < 1e-12) as `0.000`. analysis/compare.py models each page's own formatter; for the corrected page the rule changes 2 strings (both page-side, Hamza2021 nefazodone@300, −9.0e-17) and no R reference value. With the lane's unmodified formatter the corrected page scores 72148/72150, the 2 failures being its display-versus-own-export strings for that value.

Not validated: multi-arm or split-mouth inference (pasted rows carry no study identifier; native study-aware R diagnostics disagree in 4775 of 4989 comparisons and are reported separately in results/native-*.json), browser layout, raster/PDF/chart downloads, autosave and navigation. The corrected page refuses multi-arm bus imports where study identity is available; pasted dependence cannot be detected.

| Item | Static | Dynamic/source-backed |
|---|---|---|
| Rules | Tolerances, page semantics, display rule | Keyed coverage, refusal reasons, exact strings |
| Corpus | Archived recipes and ledgers | Configurations, contrast rows, page captures, fresh R refit |
| Findings | Pinned expected counts | Recomputed per-quantity comparisons |
| Provenance | Commits acd363f, f7a78dc; PR #153; release tokens | SHA-256 inventory, patch replay |

MIT applies to archive tooling. Bundled package documentation and Node dependencies retain their upstream licences.

## Browser checks (supplementary)

`browser/` records checks run in a real browser on the corrected page (pull request #153, commit f7a78dc). They supplement, and are not
part of, the `validate.R` comparison above.

- `playwright-corrected-page.log`: Playwright (Chromium, one worker) on the corrected page: 35 tests passed, including the 9
  component-nma parity tests in `app/patched/hub/shared/tests/component-nma-parity.spec.mjs` (R reference values at 1e-9, saturated design,
  refusals clear results, labels as text, roundoff zero displayed unsigned).
- `playwright-original-page.log`: the same parity spec on the released page: 5 tests fail (saturated design, two refusal cases, labels,
  signed zero) — the spec can fail.
- `figure1-vs-archive.txt`, `figure1-shots-log.json`, `figure1-tif-report.json`, `capture-figure1.cjs`: Figure 1 captured in Microsoft Edge
  151; the captured results and tables equal the archived corrected-page output.

Not covered: browser layout, raster/PDF chart downloads, browsers other than Chromium/Edge.
