# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                    |
|--------------------------------|--------------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","nri","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.011353616790994234                                                     |
| Q                              | 67.47745244715746                                                        |
| df                             | 64                                                                       |
| components.hypericum.est       | 0.03829455896917289                                                      |
| components.hypericum.se        | 0.2452063679781268                                                       |
| components.low-dose sari.est   | 0.3476568193353593                                                       |
| components.low-dose sari.se    | 0.2638281490885924                                                       |
| components.nassa.est           | 0.9856172694120995                                                       |
| components.nassa.se            | 0.21043718825980756                                                      |
| components.nri.est             | 1.123350039376906                                                        |
| components.nri.se              | 0.21603469372929518                                                      |
| components.rmao-a.est          | 0.025492131088853176                                                     |
| components.rmao-a.se           | 0.28625536645285105                                                      |
| components.snri.est            | 0.7992937396274504                                                       |
| components.snri.se             | 0.1851585103003106                                                       |
| components.ssri.est            | 0.5849925163017425                                                       |
| components.ssri.se             | 0.15826521777222616                                                      |
| components.tca.est             | 0.7336258335309853                                                       |
| components.tca.se              | 0.16421240873165371                                                      |
| combinations.hypericum.est     | 0.03829455896917289                                                      |
| combinations.hypericum.se      | 0.2452063679781268                                                       |
| combinations.low-dose sari.est | 0.3476568193353593                                                       |
| combinations.low-dose sari.se  | 0.2638281490885924                                                       |
| combinations.nassa.est         | 0.9856172694120995                                                       |
| combinations.nassa.se          | 0.21043718825980756                                                      |
| combinations.nri.est           | 1.123350039376906                                                        |
| combinations.nri.se            | 0.21603469372929518                                                      |
| combinations.rmao-a.est        | 0.025492131088853176                                                     |
| combinations.rmao-a.se         | 0.28625536645285105                                                      |
| combinations.snri.est          | 0.7992937396274504                                                       |
| combinations.snri.se           | 0.1851585103003106                                                       |
| combinations.ssri.est          | 0.5849925163017425                                                       |
| combinations.ssri.se           | 0.15826521777222616                                                      |
| combinations.tca.est           | 0.7336258335309853                                                       |
| combinations.tca.se            | 0.16421240873165371                                                      |
