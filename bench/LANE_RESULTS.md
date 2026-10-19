# Component NMA validation

Source commit: `acd363fa33f0decd2fcafcf08814f663bb9d6178`. The checkout is unchanged. Proposed app-only fixes are in [fix.patch](fix.patch); no commit or push was made.

Original: **88736/91238 checks pass**. Patched: **72148/72150 checks pass**. Bus checks: **49/63** original and **63/63** patched. Shipped standalone static assertions: **14/14**.

All 9698 numerical effect/SE/Q/tau2 checks pass at 1e-9 relative to max(1, |reference|). The patched run also passes all df, design/membership, refusal, plot-coordinate, and display-versus-export checks. Two additional rounded-R string comparisons remain different: the Hamza OR full input's nefazodone@300 effect is `-9.0205620750793969e-17` in JavaScript and `8.6042284408449632e-16` in R, displayed as `-0.000` versus `0.000` in both tables. These two signed-zero string failures are retained, not relabeled as passes. The numeric difference is far below tolerance, and the page's strings agree exactly with its own exports.

**These totals do not establish multi-arm or split-mouth inference, browser layout, or raster/PDF/chart-download correctness.** Native-study diagnostic failures are reported separately below. Refusals are support checks, not numerical R parity passes.

## Coverage

639 installed dataset catalogue entries were screened; 187 datasets in seven meta-analysis packages were loaded and documented. 54 datasets produced 576 configurations, plus 19 focused cases (including the built-in example and an uncapped 2,001-row input). The final R statuses are `{'ok': 330, 'refused': 265}`. [dataset-ledger.csv](dataset-ledger.csv), [configuration-ledger.csv](configuration-ledger.csv), [construction-attempts.json](construction-attempts.json), and [row-exclusions.json](row-exclusions.json) record inclusion, exclusion, encodings, and construction warnings. There are no unresolved construction errors.

Original labels and explicitly recorded `control` encodings remain separate. Dong's LABA-ICS and unambiguous 'and' combinations have additional '+' encodings; mappings are in corpus.json. Landenberger's documented CBT component indicators are included. No fixed combination is invented for 'or' or 'with or without' labels. Package aliases and full/two-arm-only subsets remain distinct. See [AUDIT_SCOPE.md](AUDIT_SCOPE.md) for recipes, all scope decisions, and restrictions.

Refusal counts: `{'Components are not identifiable from the contrasts.': 256, 'At least 2 valid contrasts are required.': 2, 'Invalid contrast input.': 7}`. Every refusal and the before/after behavior is recorded in [refusal-ledger.csv](refusal-ledger.csv), including four bus refusals. No missing or invalid app/reference evidence is counted as a pass. Keys are unique and exact coverage is checked.

The original/patched denominators differ because failed original fits exported stale or invalid result objects; the patch clears them. Both runs use the same configurations and R reference keys. Actual downloads are archived for all five data/report formats for every case.

## Method and evidence

The page fits one additive random-effects model with generalized DerSimonian-Laird tau2 and normal 95% intervals. It lowercases labels, splits on '+', and treats only the whole label `control` as the empty component set. The contrast design is C(A)-C(B). Combination variance includes component covariance. The exported Q is common-weight additive residual Q. There is no common-effect selector, alternative estimator, z/p output, standard-NMA comparison, or Q-difference test. A disconnected treatment graph is supported if the component design is identifiable. There is no statistical input cap.

R 4.6.0, netmeta 3.7.0, meta 8.5.0, metafor 5.2.1, metadat 1.6.0, metabook 0.2.0, mixmeta 1.2.2, mvmeta 1.0.3 and jsonlite 2.0.0 were used from offline libraries. Completed R logs print library paths (portable placeholders) and versions. Installed help and source are in documentation/; [versions.json](versions.json) records package versions.

The complete reference calls installed, unmodified `netmeta:::prepare` and `netmeta:::nma_additive`, the statistical implementation used by netcomb/discomb, bypassing only the costly standard-NMA decomposition that the page does not report. The direct route is cross-checked against 45 public-wrapper cases: **2064/2064 bridge checks pass**, maximum scaled difference 6.92057872706e-15. This includes public discomb calls with automatic component matrices, an identifiable disconnected network, no literal control, and saturated designs. The initial bridge caught a native-adapter error: prepare requires lexically oriented contrasts. The corrected adapter applies the same sign/swap preprocessing and chkmultiarm checks as netmeta. Initial and corrected evidence is retained; R-package code was never changed.

The original slow wrapper run was interrupted after preserving 40 completed cases. An initial engine run produced all 594 then-current results but exited on a script-tail parse error after an in-flight edit; reference-initial.log records the nonzero exit. The finalized script was rerun successfully, adding the built-in case and preserving matrix dimensions, then native diagnostics were recomputed after the orientation correction. Only finalized reference.json is compared. These earlier partial/error runs are not presented as completed validations.

The permitted Node route executes the complete page scripts with linkedom, plus shared export/bus/autosave/navigation/toast scripts. Statistical and rendering functions are the shipped functions; observers only capture their arguments/output. Real export buttons generate the archived Blobs. SVG coordinates are generated-markup evidence, not browser-layout evidence. The chart-export script and lazy PDF dependency are copied and reviewed but browser chart-download execution is unverified. Timers and storage use an isolated adapter. No internet or package installation was used.

All estimators checked here are closed form. Numerical tolerance is 1e-9 relative to max(1, |reference|); no iterative relaxation is used. The requested p-value tolerance is inapplicable because the page exposes no p-values. Membership, matrices, counts, refusal state/reasons, and displayed strings versus their own exports are exact. Rounding-to-R comparisons remain exact too, retaining the two signed-zero failures.

## Defects and proposed fixes

1. **False identifiability and stale results:** original index.html:131 uses an absolute inversion pivot threshold; roundoff can make a singular component design appear invertible. index.html:195 returns on failure without clearing the prior tables, forest, or export state. The patch checks the unweighted component design rank, clears state before each run, and reports refusal reasons.

2. **Saturated-model heterogeneity:** index.html:174 forces residual df to at least one, and line 185 emits tau2=0 where heterogeneity cannot be estimated. The patch exports df=0 and tau2=null, using sampling variances for effect intervals, matching netmeta's saturated-model result.

3. **Input parsing:** index.html:114 accepts numeric prefixes such as `.3oops`, silently drops malformed rows, and accepts empty/repeated components despite describing interventions as sets. The patch validates the full row and rejects invalid component sets and identical arms.

4. **Unescaped labels:** index.html:210 and 271 interpolate component names into HTML/SVG. A label such as `<tag>&x` loses text and creates invalid SVG. The patch escapes labels while preserving original statistical keys.

5. **Bus dependence and stale imports:** index.html:349-353 discards study identity and flattens multi-arm studies. The patch refuses multi-arm/repeated-study bus inputs and clears state for empty or unsupported imports. It does not add a multi-arm estimator; pasted rows still require independent contrasts.

6. **Documentation:** README's arm-level data-shape, build-metadata and Verify-in-R claims do not describe this page. The copied README now documents the actual contrast input, outputs, statistical scope, and refusal behavior.

| Case | Original | Reference / required | Patched |
|---|---|---|---|
| focused::saturated, df | 1 | 0 | 0 |
| focused::saturated, tau2 | 0 | undefined | null |
| focused::numeric-junk, component a | 0.3500000000000001 | refuse malformed effect | refused; export cleared |
| focused::singular | prior unrelated component results retained | refuse unidentifiable design | refused; tables/forest/export cleared |
| focused::html-label | `<tag>` lost; invalid SVG | literal `<tag>&x` label | exact literal text; valid SVG markup |
| bus::multi-arm | dependent rows imported | unsupported covariance | refused; export cleared |

## Native-study diagnostics and limits

Across 149 configurations with repeated original study IDs, **214/4989** finite native-reference comparisons agree at 1e-9; 10 native reference calls refuse the supplied study structure. These are separate from independent-row validation and remain failures/limitations, not passes. [native-original.json](native-original.json) and [native-patched.json](native-patched.json) retain every value and refusal. Correcting dependence would require a new estimator and richer pasted input, outside this v1 task; the bus refusal prevents known unsupported imports.

| Native example | Quantity | Page (independent rows) | Native study-aware R |
|---|---|---:|---:|
| `netmeta::Baker2009::exac::OR::full::DL::source-labels` | Q | 88.9307874307 | 62.6425028576 |
| `netmeta::Baker2009::exac::OR::full::DL::source-labels` | df | 71 | 49 |
| `netmeta::Baker2009::exac::OR::full::DL::source-labels` | tau2 | 0.00762452400111 | 0.00995902578333 |
| `netmeta::Baker2009::exac::OR::full::DL::inactive=Placebo` | Q | 89.0398917297 | 62.7576407115 |
| `netmeta::Baker2009::exac::OR::full::DL::inactive=Placebo` | df | 72 | 50 |
| `netmeta::Baker2009::exac::OR::full::DL::inactive=Placebo` | tau2 | 0.00694509988049 | 0.00870340638894 |

Su2018's split-mouth covariance is not supplied by this page. Its native diagnostics use the package's ordinary multi-arm preparation, not a validated split-mouth analysis. Incomplete pair sets, repeated contrasts, and inconsistent multi-arm effects are retained as native refusals. Binary effect-size constructions and source treatment encodings are computational fixtures, not clinical endorsements of the additive assumption.

## Per-quantity results

| Quantity | Original pass/checks | Patched pass/checks | Original max difference | Patched max difference |
|---|---:|---:|---:|---:|
| Q | 330/330 | 330/330 | 6.96229219388e-16 | 6.96229219388e-16 |
| app_coverage | 1/1 | 1/1 | 0 | 0 |
| app_evidence | 595/595 | 595/595 | 0 | 0 |
| app_unique | 1/1 | 1/1 | 0 | 0 |
| combination_membership | 330/330 | 330/330 | 0 | 0 |
| combinations_est | 2386/2386 | 2386/2386 | 6.03961325396e-14 | 6.03961325396e-14 |
| combinations_se | 2386/2386 | 2386/2386 | 2.63307816072e-14 | 2.63307816072e-14 |
| component_design | 330/330 | 330/330 | 0 | 0 |
| component_membership | 330/330 | 330/330 | 0 | 0 |
| components_est | 2134/2134 | 2134/2134 | 6.03961325396e-14 | 6.03961325396e-14 |
| components_se | 2134/2134 | 2134/2134 | 2.63307816072e-14 | 2.63307816072e-14 |
| corpus_unique | 1/1 | 1/1 | 0 | 0 |
| csv_array | 595/595 | 330/330 | 0 | 0 |
| csv_keys | 595/595 | 595/595 | 0 | 0 |
| csv_number | 18746/18746 | 10028/10028 | 0 | 0 |
| csv_scalar | 0/583 | 2/2 | 1 | 0 |
| df | 328/330 | 330/330 | 1 | 0 |
| display_combinations | 328/330 | 329/330 | 1 | 1 |
| display_components | 328/330 | 329/330 | 1 | 1 |
| display_export_combinations | 329/330 | 330/330 | 1 | 0 |
| display_export_components | 329/330 | 330/330 | 1 | 0 |
| execution_error | 595/595 | 595/595 | 0 | 0 |
| export_error | 595/595 | 595/595 | 0 | 0 |
| export_present_csv | 595/595 | 595/595 | 0 | 0 |
| export_present_json | 595/595 | 595/595 | 0 | 0 |
| export_present_md | 595/595 | 595/595 | 0 | 0 |
| export_present_report-md | 595/595 | 595/595 | 0 | 0 |
| export_present_report-txt | 595/595 | 595/595 | 0 | 0 |
| fit_present | 330/330 | 330/330 | 0 | 0 |
| input_rows | 330/330 | 330/330 | 0 | 0 |
| json_export | 595/595 | 595/595 | 0 | 0 |
| md_array | 595/595 | 330/330 | 0 | 0 |
| md_keys | 595/595 | 595/595 | 0 | 0 |
| md_number | 18746/18746 | 10028/10028 | 0 | 0 |
| md_scalar | 0/583 | 2/2 | 1 | 0 |
| plot_CI_x1 | 4514/4514 | 4520/4520 | 1.60286970874e-14 | 1.60286970874e-14 |
| plot_CI_x2 | 4514/4514 | 4520/4520 | 1.18486874239e-14 | 1.18486874239e-14 |
| plot_CI_y1 | 4514/4514 | 4520/4520 | 0 | 0 |
| plot_CI_y2 | 4514/4514 | 4520/4520 | 0 | 0 |
| plot_evidence | 329/330 | 330/330 | 0 | 0 |
| plot_labels | 329/329 | 330/330 | 0 | 0 |
| plot_line_count | 329/329 | 330/330 | 0 | 0 |
| plot_point_x | 4514/4514 | 4520/4520 | 1.22551534816e-14 | 1.22551534816e-14 |
| plot_point_y | 4514/4514 | 4520/4520 | 0 | 0 |
| plot_rect_count | 329/329 | 330/330 | 0 | 0 |
| plot_viewBox | 329/329 | 330/330 | 0 | 0 |
| reference_coverage | 1/1 | 1/1 | 0 | 0 |
| reference_evidence | 595/595 | 595/595 | 0 | 0 |
| reference_unique | 1/1 | 1/1 | 0 | 0 |
| refusal_combination_table | 0/265 | 265/265 | 1 | 0 |
| refusal_component_table | 0/265 | 265/265 | 1 | 0 |
| refusal_forest | 0/265 | 265/265 | 1 | 0 |
| refusal_reason | 0/265 | 265/265 | 0 | 0 |
| refusal_state | 0/265 | 265/265 | 1 | 0 |
| report_md_data | 595/595 | 595/595 | 0 | 0 |
| report_txt_data | 595/595 | 595/595 | 0 | 0 |
| tau2 | 328/328 | 328/328 | 5.2909759532e-14 | 5.2909759532e-14 |
| tau2_undefined | 0/2 | 2/2 | 1 | 0 |

Maxima are scaled numerical differences; exact checks use 0/1 mismatch indicators. Invalid/missing values are separately counted in results JSON. Original invalid SVG is explicitly a failed evidence check, with no fabricated coordinate comparisons.

## Commands and verbatim final lines

See [README.md](README.md) for reproduction commands. Executed final commands included `node run_node.cjs original`, `node run_node.cjs patched`, `python run_r.py reference.R`, `python run_r.py reference.R native`, `python run_r.py bridge_disconnected.R`, `python run_r.py bus_reference.R`, `python run_r.py metadata.R`, both compare.py variants, bridge.py, compare_bus.py, and test_static.py.

```text
APP original: 595 configurations; 2975 real export blobs; 0 execution errors
APP patched: 595 configurations; 2975 real export blobs; 0 execution errors
REFERENCE 595 configurations; 330 numerical fits; 265 support refusals; 0 errors
88736/91238 checks pass
72148/72150 checks pass
WRAPPER BRIDGE: 2064/2064 checks pass
BUS original: 49/63 checks pass
BUS patched: 63/63 checks pass
SHIPPED STATIC TESTS: 14/14 pass
```

Packaging portability: the unused upstream `cnma-oracle.R` fixture has repository-relative paths in both source snapshots. `source-manifest.json` retains upstream hashes and records the normalized snapshot hash separately. The checkout, executed page code, statistical evidence, and app-only patch are unaffected. Run `python portable_snapshot.py` before `python verify_archive.py` and `python archive.py` when rebuilding the archive.
