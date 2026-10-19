# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                 | value                |
|---------------------|----------------------|
| comps               | ["aa","c","r","ut"]  |
| tau2                | 0                    |
| Q                   | 16.90657559229479    |
| df                  | 18                   |
| components.aa.est   | 0.5960691754129008   |
| components.aa.se    | 0.42919266929418587  |
| components.c.est    | -0.12446740404554638 |
| components.c.se     | 0.12659392734409325  |
| components.r.est    | -0.4019298510238219  |
| components.r.se     | 0.3251176614310677   |
| components.ut.est   | -0.1790601164026847  |
| components.ut.se    | 0.35350632942870897  |
| combinations.aa.est | 0.5960691754129008   |
| combinations.aa.se  | 0.42919266929418587  |
| combinations.c.est  | -0.12446740404554638 |
| combinations.c.se   | 0.12659392734409325  |
| combinations.r.est  | -0.4019298510238219  |
| combinations.r.se   | 0.3251176614310677   |
| combinations.ut.est | -0.1790601164026847  |
| combinations.ut.se  | 0.35350632942870897  |
