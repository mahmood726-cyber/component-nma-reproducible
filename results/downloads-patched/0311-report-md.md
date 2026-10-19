# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                              |
|--------------------------------|--------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.07570231524326967                                                |
| Q                              | 50.19205127094128                                                  |
| df                             | 29                                                                 |
| components.hypericum.est       | -0.06658055174711275                                               |
| components.hypericum.se        | 0.2099127184404851                                                 |
| components.low-dose sari.est   | -0.5967757611162152                                                |
| components.low-dose sari.se    | 0.5922959595153242                                                 |
| components.nassa.est           | -0.19534747089322946                                               |
| components.nassa.se            | 0.4073182175902875                                                 |
| components.rmao-a.est          | 0.14741465286959032                                                |
| components.rmao-a.se           | 0.33777573563393015                                                |
| components.snri.est            | 0.42970237886654183                                                |
| components.snri.se             | 0.2657403016166663                                                 |
| components.ssri.est            | 0.2661975891075452                                                 |
| components.ssri.se             | 0.17520834165885762                                                |
| components.tca.est             | 0.6749469284651602                                                 |
| components.tca.se              | 0.18670017807362602                                                |
| combinations.hypericum.est     | -0.06658055174711275                                               |
| combinations.hypericum.se      | 0.2099127184404851                                                 |
| combinations.low-dose sari.est | -0.5967757611162152                                                |
| combinations.low-dose sari.se  | 0.5922959595153242                                                 |
| combinations.nassa.est         | -0.19534747089322946                                               |
| combinations.nassa.se          | 0.4073182175902875                                                 |
| combinations.rmao-a.est        | 0.14741465286959032                                                |
| combinations.rmao-a.se         | 0.33777573563393015                                                |
| combinations.snri.est          | 0.42970237886654183                                                |
| combinations.snri.se           | 0.2657403016166663                                                 |
| combinations.ssri.est          | 0.2661975891075452                                                 |
| combinations.ssri.se           | 0.17520834165885762                                                |
| combinations.tca.est           | 0.6749469284651602                                                 |
| combinations.tca.se            | 0.18670017807362602                                                |
