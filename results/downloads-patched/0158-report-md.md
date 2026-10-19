# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                 | value               |
|---------------------|---------------------|
| comps               | ["aa","c","p","r"]  |
| tau2                | 0.11407121642058031 |
| Q                   | 29.653220424641997  |
| df                  | 21                  |
| components.aa.est   | 1.5148968381563845  |
| components.aa.se    | 0.8727720390053141  |
| components.c.est    | 0.5503457810234926  |
| components.c.se     | 0.6644216670539611  |
| components.p.est    | 0.6513050194692898  |
| components.p.se     | 0.6810365646874709  |
| components.r.est    | 0.14800383592546806 |
| components.r.se     | 0.8236407305863589  |
| combinations.aa.est | 1.5148968381563845  |
| combinations.aa.se  | 0.8727720390053141  |
| combinations.c.est  | 0.5503457810234926  |
| combinations.c.se   | 0.6644216670539611  |
| combinations.p.est  | 0.6513050194692898  |
| combinations.p.se   | 0.6810365646874709  |
| combinations.r.est  | 0.14800383592546806 |
| combinations.r.se   | 0.8236407305863589  |
