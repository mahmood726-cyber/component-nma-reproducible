# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                               | value                                |
|-----------------------------------|--------------------------------------|
| comps                             | ["comti","dopamine agonist","maobi"] |
| tau2                              | 0.023457016606459838                 |
| Q                                 | 46.7183992158227                     |
| df                                | 25                                   |
| components.comti.est              | -0.3772596170447749                  |
| components.comti.se               | 0.07074367489124124                  |
| components.dopamine agonist.est   | -0.40980991232762387                 |
| components.dopamine agonist.se    | 0.06196867728089988                  |
| components.maobi.est              | -0.4841106192290525                  |
| components.maobi.se               | 0.14958431380803                     |
| combinations.comti.est            | -0.3772596170447749                  |
| combinations.comti.se             | 0.07074367489124124                  |
| combinations.dopamine agonist.est | -0.40980991232762387                 |
| combinations.dopamine agonist.se  | 0.06196867728089988                  |
| combinations.maobi.est            | -0.4841106192290525                  |
| combinations.maobi.se             | 0.14958431380803                     |
