# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                             | value                                           |
|---------------------------------|-------------------------------------------------|
| comps                           | ["grp_counseling","ind_counseling","self_help"] |
| tau2                            | 0.3358993865022123                              |
| Q                               | 162.79056541858387                              |
| df                              | 25                                              |
| components.grp_counseling.est   | 0.6299769724682036                              |
| components.grp_counseling.se    | 0.2950883796599611                              |
| components.ind_counseling.est   | 0.5809557698561133                              |
| components.ind_counseling.se    | 0.1669637346092239                              |
| components.self_help.est        | 0.3411858797355235                              |
| components.self_help.se         | 0.27266558433476734                             |
| combinations.grp_counseling.est | 0.6299769724682036                              |
| combinations.grp_counseling.se  | 0.2950883796599611                              |
| combinations.ind_counseling.est | 0.5809557698561133                              |
| combinations.ind_counseling.se  | 0.1669637346092239                              |
| combinations.self_help.est      | 0.3411858797355235                              |
| combinations.self_help.se       | 0.27266558433476734                             |
