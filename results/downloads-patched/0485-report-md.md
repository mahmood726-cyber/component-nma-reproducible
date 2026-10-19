# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                    |
|--------------------------------|--------------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","nri","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.0069374463543356414                                                    |
| Q                              | 89.13670482698436                                                        |
| df                             | 65                                                                       |
| components.hypericum.est       | 0.292324524504858                                                        |
| components.hypericum.se        | 0.05015636193083786                                                      |
| components.low-dose sari.est   | 0.21088121919548175                                                      |
| components.low-dose sari.se    | 0.0906118890240803                                                       |
| components.nassa.est           | 0.057766853992999787                                                     |
| components.nassa.se            | 0.06974154821403221                                                      |
| components.nri.est             | 0.12909086201154715                                                      |
| components.nri.se              | 0.14074598813337633                                                      |
| components.rmao-a.est          | 0.02663115426406787                                                      |
| components.rmao-a.se           | 0.09799342108787783                                                      |
| components.snri.est            | 0.24810880877203487                                                      |
| components.snri.se             | 0.06249853467970864                                                      |
| components.ssri.est            | 0.23507528135136174                                                      |
| components.ssri.se             | 0.04043783640061413                                                      |
| components.tca.est             | 0.23523582915081437                                                      |
| components.tca.se              | 0.04365002544834432                                                      |
| combinations.hypericum.est     | 0.292324524504858                                                        |
| combinations.hypericum.se      | 0.05015636193083786                                                      |
| combinations.low-dose sari.est | 0.21088121919548175                                                      |
| combinations.low-dose sari.se  | 0.0906118890240803                                                       |
| combinations.nassa.est         | 0.057766853992999787                                                     |
| combinations.nassa.se          | 0.06974154821403221                                                      |
| combinations.nri.est           | 0.12909086201154715                                                      |
| combinations.nri.se            | 0.14074598813337633                                                      |
| combinations.rmao-a.est        | 0.02663115426406787                                                      |
| combinations.rmao-a.se         | 0.09799342108787783                                                      |
| combinations.snri.est          | 0.24810880877203487                                                      |
| combinations.snri.se           | 0.06249853467970864                                                      |
| combinations.ssri.est          | 0.23507528135136174                                                      |
| combinations.ssri.se           | 0.04043783640061413                                                      |
| combinations.tca.est           | 0.23523582915081437                                                      |
| combinations.tca.se            | 0.04365002544834432                                                      |
