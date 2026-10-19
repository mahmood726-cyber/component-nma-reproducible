# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                              |
|--------------------------------|------------------------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","nri","placebo","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.027290931129039655                                                               |
| Q                              | 66.75453923368677                                                                  |
| df                             | 53                                                                                 |
| components.hypericum.est       | -0.75                                                                              |
| components.hypericum.se        | 5931641.601515722                                                                  |
| components.low-dose sari.est   | -1.25                                                                              |
| components.low-dose sari.se    | 5931641.601515725                                                                  |
| components.nassa.est           | -1.5                                                                               |
| components.nassa.se            | 5931641.601515725                                                                  |
| components.nri.est             | -0.75                                                                              |
| components.nri.se              | 5931641.601515725                                                                  |
| components.placebo.est         | -1.5                                                                               |
| components.placebo.se          | 5931641.601515722                                                                  |
| components.rmao-a.est          | -1                                                                                 |
| components.rmao-a.se           | 5931641.601515724                                                                  |
| components.snri.est            | -0.75                                                                              |
| components.snri.se             | 5931641.601515721                                                                  |
| components.ssri.est            | -0.75                                                                              |
| components.ssri.se             | 5931641.60151572                                                                   |
| components.tca.est             | -0.75                                                                              |
| components.tca.se              | 5931641.601515722                                                                  |
| combinations.hypericum.est     | -0.75                                                                              |
| combinations.hypericum.se      | 5931641.601515722                                                                  |
| combinations.low-dose sari.est | -1.25                                                                              |
| combinations.low-dose sari.se  | 5931641.601515725                                                                  |
| combinations.nassa.est         | -1.5                                                                               |
| combinations.nassa.se          | 5931641.601515725                                                                  |
| combinations.nri.est           | -0.75                                                                              |
| combinations.nri.se            | 5931641.601515725                                                                  |
| combinations.placebo.est       | -1.5                                                                               |
| combinations.placebo.se        | 5931641.601515722                                                                  |
| combinations.rmao-a.est        | -1                                                                                 |
| combinations.rmao-a.se         | 5931641.601515724                                                                  |
| combinations.snri.est          | -0.75                                                                              |
| combinations.snri.se           | 5931641.601515721                                                                  |
| combinations.ssri.est          | -0.75                                                                              |
| combinations.ssri.se           | 5931641.60151572                                                                   |
| combinations.tca.est           | -0.75                                                                              |
| combinations.tca.se            | 5931641.601515722                                                                  |
