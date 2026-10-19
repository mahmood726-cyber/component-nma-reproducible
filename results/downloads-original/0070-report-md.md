# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                              |
|--------------------------------|------------------------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","nri","placebo","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.01610732758100308                                                                |
| Q                              | 71.17851077931391                                                                  |
| df                             | 43                                                                                 |
| components.hypericum.est       | 0.25                                                                               |
| components.hypericum.se        | 5931641.601515724                                                                  |
| components.low-dose sari.est   | 0                                                                                  |
| components.low-dose sari.se    | 5931641.601515727                                                                  |
| components.nassa.est           | 0.5                                                                                |
| components.nassa.se            | 5931641.601515724                                                                  |
| components.nri.est             | 1                                                                                  |
| components.nri.se              | 5931641.601515726                                                                  |
| components.placebo.est         | 1                                                                                  |
| components.placebo.se          | 5931641.601515725                                                                  |
| components.rmao-a.est          | 0.375                                                                              |
| components.rmao-a.se           | 5931641.601515725                                                                  |
| components.snri.est            | 0.625                                                                              |
| components.snri.se             | 5931641.601515722                                                                  |
| components.ssri.est            | 0.5                                                                                |
| components.ssri.se             | 5931641.601515722                                                                  |
| components.tca.est             | 0.75                                                                               |
| components.tca.se              | 5931641.601515722                                                                  |
| combinations.hypericum.est     | 0.25                                                                               |
| combinations.hypericum.se      | 5931641.601515724                                                                  |
| combinations.low-dose sari.est | 0                                                                                  |
| combinations.low-dose sari.se  | 5931641.601515727                                                                  |
| combinations.nassa.est         | 0.5                                                                                |
| combinations.nassa.se          | 5931641.601515724                                                                  |
| combinations.nri.est           | 1                                                                                  |
| combinations.nri.se            | 5931641.601515726                                                                  |
| combinations.placebo.est       | 1                                                                                  |
| combinations.placebo.se        | 5931641.601515725                                                                  |
| combinations.rmao-a.est        | 0.375                                                                              |
| combinations.rmao-a.se         | 5931641.601515725                                                                  |
| combinations.snri.est          | 0.625                                                                              |
| combinations.snri.se           | 5931641.601515722                                                                  |
| combinations.ssri.est          | 0.5                                                                                |
| combinations.ssri.se           | 5931641.601515722                                                                  |
| combinations.tca.est           | 0.75                                                                               |
| combinations.tca.se            | 5931641.601515722                                                                  |
