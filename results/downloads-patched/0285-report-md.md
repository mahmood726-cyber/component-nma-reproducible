# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                    |
|--------------------------------|--------------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","nri","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.01990865494159731                                                      |
| Q                              | 64.58070485952368                                                        |
| df                             | 54                                                                       |
| components.hypericum.est       | 0.7148221407457308                                                       |
| components.hypericum.se        | 0.11945699209761346                                                      |
| components.low-dose sari.est   | 0.6156877179135554                                                       |
| components.low-dose sari.se    | 0.2209744347754611                                                       |
| components.nassa.est           | 0.3870073346925098                                                       |
| components.nassa.se            | 0.21138317329269019                                                      |
| components.nri.est             | 0.6178217587395193                                                       |
| components.nri.se              | 0.26792043303739205                                                      |
| components.rmao-a.est          | 0.458224236375536                                                        |
| components.rmao-a.se           | 0.19487331606435293                                                      |
| components.snri.est            | 0.7433256701630259                                                       |
| components.snri.se             | 0.15437904852777182                                                      |
| components.ssri.est            | 0.6179595092735204                                                       |
| components.ssri.se             | 0.10236543425639968                                                      |
| components.tca.est             | 0.6683393304085326                                                       |
| components.tca.se              | 0.10791908857316172                                                      |
| combinations.hypericum.est     | 0.7148221407457308                                                       |
| combinations.hypericum.se      | 0.11945699209761346                                                      |
| combinations.low-dose sari.est | 0.6156877179135554                                                       |
| combinations.low-dose sari.se  | 0.2209744347754611                                                       |
| combinations.nassa.est         | 0.3870073346925098                                                       |
| combinations.nassa.se          | 0.21138317329269019                                                      |
| combinations.nri.est           | 0.6178217587395193                                                       |
| combinations.nri.se            | 0.26792043303739205                                                      |
| combinations.rmao-a.est        | 0.458224236375536                                                        |
| combinations.rmao-a.se         | 0.19487331606435293                                                      |
| combinations.snri.est          | 0.7433256701630259                                                       |
| combinations.snri.se           | 0.15437904852777182                                                      |
| combinations.ssri.est          | 0.6179595092735204                                                       |
| combinations.ssri.se           | 0.10236543425639968                                                      |
| combinations.tca.est           | 0.6683393304085326                                                       |
| combinations.tca.se            | 0.10791908857316172                                                      |
