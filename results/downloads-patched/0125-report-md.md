# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                | value               |
|--------------------|---------------------|
| comps              | ["b","c","d"]       |
| tau2               | 0.5774954007605713  |
| Q                  | 205.52087727939076  |
| df                 | 25                  |
| components.b.est   | 0.41293876138007063 |
| components.b.se    | 0.3486346536028629  |
| components.c.est   | 0.7273110388830994  |
| components.c.se    | 0.21131564307311249 |
| components.d.est   | 0.7987079070951876  |
| components.d.se    | 0.37033906413366746 |
| combinations.b.est | 0.41293876138007063 |
| combinations.b.se  | 0.3486346536028629  |
| combinations.c.est | 0.7273110388830994  |
| combinations.c.se  | 0.21131564307311249 |
| combinations.d.est | 0.7987079070951876  |
| combinations.d.se  | 0.37033906413366746 |
