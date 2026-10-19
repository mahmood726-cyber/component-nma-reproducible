# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                             | value                                           |
|---------------------------------|-------------------------------------------------|
| comps                           | ["grp_counseling","ind_counseling","self_help"] |
| tau2                            | 0.3641575424861575                              |
| Q                               | 150.20431539281896                              |
| df                              | 19                                              |
| components.grp_counseling.est   | 1.086292122156803                               |
| components.grp_counseling.se    | 0.4468638719433391                              |
| components.ind_counseling.est   | 0.5841671321333316                              |
| components.ind_counseling.se    | 0.18388748122435358                             |
| components.self_help.est        | 0.36209259422067375                             |
| components.self_help.se         | 0.31859364027037                                |
| combinations.grp_counseling.est | 1.086292122156803                               |
| combinations.grp_counseling.se  | 0.4468638719433391                              |
| combinations.ind_counseling.est | 0.5841671321333316                              |
| combinations.ind_counseling.se  | 0.18388748122435358                             |
| combinations.self_help.est      | 0.36209259422067375                             |
| combinations.self_help.se       | 0.31859364027037                                |
