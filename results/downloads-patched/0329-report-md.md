# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                             | value                                                                 |
|---------------------------------|-----------------------------------------------------------------------|
| comps                           | ["f2f cbt","hybrid cbt","multimedia cbt","placebo","tau","wait list"] |
| tau2                            | 0.3004079625241687                                                    |
| Q                               | 12325.456828074535                                                    |
| df                              | 51                                                                    |
| components.f2f cbt.est          | -1.3067924765417427                                                   |
| components.f2f cbt.se           | 0.2300384682202037                                                    |
| components.hybrid cbt.est       | -1.210096052273422                                                    |
| components.hybrid cbt.se        | 0.37599655139495886                                                   |
| components.multimedia cbt.est   | -0.823851667849917                                                    |
| components.multimedia cbt.se    | 0.28857575152902987                                                   |
| components.placebo.est          | -0.5700123755400677                                                   |
| components.placebo.se           | 0.32134737318996115                                                   |
| components.tau.est              | -0.11968848938398757                                                  |
| components.tau.se               | 0.2640965999143359                                                    |
| components.wait list.est        | 0.4438171897923686                                                    |
| components.wait list.se         | 0.2737497320962733                                                    |
| combinations.f2f cbt.est        | -1.3067924765417427                                                   |
| combinations.f2f cbt.se         | 0.2300384682202037                                                    |
| combinations.hybrid cbt.est     | -1.210096052273422                                                    |
| combinations.hybrid cbt.se      | 0.37599655139495886                                                   |
| combinations.multimedia cbt.est | -0.823851667849917                                                    |
| combinations.multimedia cbt.se  | 0.28857575152902987                                                   |
| combinations.placebo.est        | -0.5700123755400677                                                   |
| combinations.placebo.se         | 0.32134737318996115                                                   |
| combinations.tau.est            | -0.11968848938398757                                                  |
| combinations.tau.se             | 0.2640965999143359                                                    |
| combinations.wait list.est      | 0.4438171897923686                                                    |
| combinations.wait list.se       | 0.2737497320962733                                                    |
