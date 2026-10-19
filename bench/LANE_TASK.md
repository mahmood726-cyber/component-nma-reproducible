# Job P19 (paper 19): component-nma app vs R (netmeta::netcomb / discomb) - run on BASEIMAGE

Read ../kit/codex_common3.md first and follow it. Model this job on ../P16 (TASK.md, RESULTS.md, corpus.R, reference.R,
compare.py, ledgers, documentation/, P16-validation.zip layout) and ../kit/codex16 (paper 14 lane): same rigour, same
deliverables, same archive-ready layout. This is a v1 validation: validate what the page does now; do not add features.

App: ./allmeta/component-nma/index.html (allmeta main, cloned in ./allmeta - record the commit), its README and tests/, and
every shared file it loads. Find exactly what the page computes and displays/exports: additive component model (component
design matrix C, how treatment labels are split into components, inactive/reference component), component effects with
SE/CI/z/p, combination effects, standard NMA comparison if any, Q additive / Q difference tests, tau2 estimator, common vs
random effects, multi-arm handling, disconnected-network handling (netcomb vs discomb), refusals and caps. Read
hub/shared/tests/component-nma-parity.spec.mjs for orientation. Validate THAT; do not re-implement it.

Reference: R 4.6.0 with netmeta 3.7.0 and meta from R_LIBS_USER=<R_LIBS_USER>,
R_LIBS=<R_LIBS>, R_ENVIRON_USER=NUL; Rscript at <RSCRIPT>
(or <RSCRIPT_ALTERNATIVE> if that exists). Print .libPaths() and package versions in every R log.
Corpus: every network dataset with multi-component (combination) treatments available offline in the installed packages
(netmeta: Linde2016, Linde2015, Dong2013?, ... ; metadat; discover them, do not trust this list), plus every network dataset
whose treatments can be expressed as components under the page's own label-splitting rule, each in every configuration the
page offers. Record every candidate and every exclusion with its reason in dataset-ledger.csv; one row per configuration in
configuration-ledger.csv.
Tolerances as in ../kit/codex16/TASK.md (closed form 1e-9 relative to max(1,|ref|); iterative 1e-6 with convergence
settings stated for both sides; p-values 1e-9 absolute; exact for k, membership, refusals, displayed strings vs exports at
shown decimals).
Page capture: run the page's own code in node (linkedom/jsdom, as P17 did with run_node.cjs) if the engine is pure JS, else
headless Edge via Playwright - state which.

Then: fix.patch for any defect (root cause, file:line; app-side only), rerun, RESULTS.md (counts before/after, faults with
before/after numbers, honest limits). Missing or invalid app evidence is never a pass; unique keys and exact coverage;
record every refusal with its reason; no machine paths in deliverables. Do not edit ./allmeta; copy the page into this
folder for patching. Do not git commit/push. Run at most ONE R process at a time (the machine is shared). Keep PROGRESS.md
updated so the job can resume. Final deliverable: P19-validation.zip in this folder (same layout as P16-validation.zip).
