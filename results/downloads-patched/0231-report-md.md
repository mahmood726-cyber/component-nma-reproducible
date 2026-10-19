# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                      |
|--------------------------------|------------------------------------------------------------|
| comps                          | ["bromocriptine","cabergoline","pramipexole","ropinirole"] |
| tau2                           | 0                                                          |
| Q                              | 2.5283805764012293                                         |
| df                             | 5                                                          |
| components.bromocriptine.est   | -0.56956602246079                                          |
| components.bromocriptine.se    | 0.42653018360545164                                        |
| components.cabergoline.est     | -0.8695660224607901                                        |
| components.cabergoline.se      | 0.47466378545715665                                        |
| components.pramipexole.est     | -1.8586607947368643                                        |
| components.pramipexole.se      | 0.31456939361757835                                        |
| components.ropinirole.est      | -0.5140569278798094                                        |
| components.ropinirole.se       | 0.455491305314931                                          |
| combinations.bromocriptine.est | -0.56956602246079                                          |
| combinations.bromocriptine.se  | 0.42653018360545164                                        |
| combinations.cabergoline.est   | -0.8695660224607901                                        |
| combinations.cabergoline.se    | 0.47466378545715665                                        |
| combinations.pramipexole.est   | -1.8586607947368643                                        |
| combinations.pramipexole.se    | 0.31456939361757835                                        |
| combinations.ropinirole.est    | -0.5140569278798094                                        |
| combinations.ropinirole.se     | 0.455491305314931                                          |
