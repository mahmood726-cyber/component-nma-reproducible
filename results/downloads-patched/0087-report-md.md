# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                              |
|--------------------------------|--------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.009625065990325084                                               |
| Q                              | 52.45753519962573                                                  |
| df                             | 29                                                                 |
| components.hypericum.est       | -0.01210571002143801                                               |
| components.hypericum.se        | 0.09896796836749806                                                |
| components.low-dose sari.est   | -0.23033741543036657                                               |
| components.low-dose sari.se    | 0.23487037947063263                                                |
| components.nassa.est           | 0.014957085418725369                                               |
| components.nassa.se            | 0.13241852285758646                                                |
| components.rmao-a.est          | -0.05571233357896799                                               |
| components.rmao-a.se           | 0.15456443944898018                                                |
| components.snri.est            | 0.1624335969926627                                                 |
| components.snri.se             | 0.0948924644021842                                                 |
| components.ssri.est            | 0.11569342781444047                                                |
| components.ssri.se             | 0.06864703637986146                                                |
| components.tca.est             | 0.2521678896523447                                                 |
| components.tca.se              | 0.07138898796049567                                                |
| combinations.hypericum.est     | -0.01210571002143801                                               |
| combinations.hypericum.se      | 0.09896796836749806                                                |
| combinations.low-dose sari.est | -0.23033741543036657                                               |
| combinations.low-dose sari.se  | 0.23487037947063263                                                |
| combinations.nassa.est         | 0.014957085418725369                                               |
| combinations.nassa.se          | 0.13241852285758646                                                |
| combinations.rmao-a.est        | -0.05571233357896799                                               |
| combinations.rmao-a.se         | 0.15456443944898018                                                |
| combinations.snri.est          | 0.1624335969926627                                                 |
| combinations.snri.se           | 0.0948924644021842                                                 |
| combinations.ssri.est          | 0.11569342781444047                                                |
| combinations.ssri.se           | 0.06864703637986146                                                |
| combinations.tca.est           | 0.2521678896523447                                                 |
| combinations.tca.se            | 0.07138898796049567                                                |
