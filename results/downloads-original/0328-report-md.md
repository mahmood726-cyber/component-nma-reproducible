# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                             | value                                                                                |
|---------------------------------|--------------------------------------------------------------------------------------|
| comps                           | ["f2f cbt","hybrid cbt","multimedia cbt","no treatment","placebo","tau","wait list"] |
| tau2                            | 0.37309496455716284                                                                  |
| Q                               | 27124.78133919542                                                                    |
| df                              | 50                                                                                   |
| components.f2f cbt.est          | 2                                                                                    |
| components.f2f cbt.se           | 9686330.1738525                                                                      |
| components.hybrid cbt.est       | 0                                                                                    |
| components.hybrid cbt.se        | 9686330.173852505                                                                    |
| components.multimedia cbt.est   | 1                                                                                    |
| components.multimedia cbt.se    | 9686330.173852498                                                                    |
| components.no treatment.est     | 2                                                                                    |
| components.no treatment.se      | 9686330.173852501                                                                    |
| components.placebo.est          | 2                                                                                    |
| components.placebo.se           | 9686330.173852501                                                                    |
| components.tau.est              | 3                                                                                    |
| components.tau.se               | 9686330.1738525                                                                      |
| components.wait list.est        | 2                                                                                    |
| components.wait list.se         | 9686330.173852496                                                                    |
| combinations.f2f cbt.est        | 2                                                                                    |
| combinations.f2f cbt.se         | 9686330.1738525                                                                      |
| combinations.hybrid cbt.est     | 0                                                                                    |
| combinations.hybrid cbt.se      | 9686330.173852505                                                                    |
| combinations.multimedia cbt.est | 1                                                                                    |
| combinations.multimedia cbt.se  | 9686330.173852498                                                                    |
| combinations.no treatment.est   | 2                                                                                    |
| combinations.no treatment.se    | 9686330.173852501                                                                    |
| combinations.placebo.est        | 2                                                                                    |
| combinations.placebo.se         | 9686330.173852501                                                                    |
| combinations.tau.est            | 3                                                                                    |
| combinations.tau.se             | 9686330.1738525                                                                      |
| combinations.wait list.est      | 2                                                                                    |
| combinations.wait list.se       | 9686330.173852496                                                                    |
