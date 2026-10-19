# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                             | value                                           |
|---------------------------------|-------------------------------------------------|
| comps                           | ["grp_counseling","ind_counseling","self_help"] |
| tau2                            | 0.5774954007605718                              |
| Q                               | 205.5208772793909                               |
| df                              | 25                                              |
| components.grp_counseling.est   | 0.7987079070951876                              |
| components.grp_counseling.se    | 0.3703390641336676                              |
| components.ind_counseling.est   | 0.7273110388830997                              |
| components.ind_counseling.se    | 0.21131564307311257                             |
| components.self_help.est        | 0.41293876138007074                             |
| components.self_help.se         | 0.34863465360286305                             |
| combinations.grp_counseling.est | 0.7987079070951876                              |
| combinations.grp_counseling.se  | 0.3703390641336676                              |
| combinations.ind_counseling.est | 0.7273110388830997                              |
| combinations.ind_counseling.se  | 0.21131564307311257                             |
| combinations.self_help.est      | 0.41293876138007074                             |
| combinations.self_help.se       | 0.34863465360286305                             |
