# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                | value                 |
|--------------------|-----------------------|
| comps              | ["2"]                 |
| tau2               | 0                     |
| Q                  | 7.786494391820532     |
| df                 | 8                     |
| components.2.est   | -0.013565966547594469 |
| components.2.se    | 0.05393813676967978   |
| combinations.2.est | -0.013565966547594469 |
| combinations.2.se  | 0.05393813676967978   |
