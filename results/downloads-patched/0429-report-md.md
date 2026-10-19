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
| Q                              | 1.9493530293133459                                         |
| df                             | 5                                                          |
| components.bromocriptine.est   | -0.16227708967659363                                       |
| components.bromocriptine.se    | 0.10469936002192985                                        |
| components.cabergoline.est     | -0.283205347013352                                         |
| components.cabergoline.se      | 0.13439295005527913                                        |
| components.pramipexole.est     | -0.49205655465896964                                       |
| components.pramipexole.se      | 0.08356362207625785                                        |
| components.ropinirole.est      | -0.1348516160162247                                        |
| components.ropinirole.se       | 0.11953047004605753                                        |
| combinations.bromocriptine.est | -0.16227708967659363                                       |
| combinations.bromocriptine.se  | 0.10469936002192985                                        |
| combinations.cabergoline.est   | -0.283205347013352                                         |
| combinations.cabergoline.se    | 0.13439295005527913                                        |
| combinations.pramipexole.est   | -0.49205655465896964                                       |
| combinations.pramipexole.se    | 0.08356362207625785                                        |
| combinations.ropinirole.est    | -0.1348516160162247                                        |
| combinations.ropinirole.se     | 0.11953047004605753                                        |
