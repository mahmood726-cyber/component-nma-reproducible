# Equivalence of the archived corrected page with allmeta v1.8.0

allmeta v1.8.0: tag `v1.8.0`, commit `1cb3f8409c7af75ed41f7e1811f9c502f900fc79`, DOI 10.5281/zenodo.23515177.
The corrected page was validated at commit `f7a78dc542270ca461c3fa0b3fedca5c8e4a62a5` (pull request #153), which is an
ancestor of v1.8.0. `component-nma/` is unchanged between the two commits.

Of the 23 files in `app/patched/`, 20 are byte-identical to the v1.8.0 blobs. The other three differ as follows:

| File | Difference from v1.8.0 | Effect on results |
|---|---|---|
| `component-nma/tests/fixtures/cnma-oracle.R` | the archive keeps the portable copy (machine path removed), as noted in `app/app-sha256.json` | none (test fixture; not loaded by the page) |
| `hub/shared/results-export.js` | v1.8.0 adds `flex-wrap:wrap;max-width:100%` to the export-bar CSS | none (layout only) |
| `shared/build-info.js` | v1.8.0 build stamp (version, sha, build time) | none (display only) |

Check by execution (21 Oct 2026, Node v24.22.0, Windows): `bench/run_node.cjs patched` was re-run on the 23 files
at their **v1.8.0 bytes** (keeping the portable fixture), with the archived `data/corpus.json`,
`data/focused-corpus.json`, `data/bus-corpus.json` and `bench/node_modules`. It reported 595 configurations, 2,975 real
export blobs and 0 execution errors.

- `app-patched.json`: SHA-256 `2e148ac9909694484ec66f728dd4d9249f0fcd7b93cbc63fe1d47842586808f9`, byte-identical to the archived `results/app-patched.json`.
- `bus-patched.json`: SHA-256 `63fd03d89b506d3dbbb695a3712a84af0feb1740cac31642493241ed69ed7b70`, byte-identical to the archived `results/bus-patched.json`.

All of the archive's comparison results for the corrected page therefore apply unchanged to allmeta v1.8.0.
