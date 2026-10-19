# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                               | value                             |
|-----------------------------------|-----------------------------------|
| comps                             | ["chlorpheniramine","doxylamine"] |
| tau2                              | 0.029055897247474434              |
| Q                                 | 11.969811126681961                |
| df                                | 6                                 |
| components.chlorpheniramine.est   | 0.17280846705518557               |
| components.chlorpheniramine.se    | 0.12261279871509846               |
| components.doxylamine.est         | 0.19236570424438182               |
| components.doxylamine.se          | 0.13916235879966626               |
| combinations.chlorpheniramine.est | 0.17280846705518557               |
| combinations.chlorpheniramine.se  | 0.12261279871509846               |
| combinations.doxylamine.est       | 0.19236570424438182               |
| combinations.doxylamine.se        | 0.13916235879966626               |
