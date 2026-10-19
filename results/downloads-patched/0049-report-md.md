# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                    |
|--------------------------------|--------------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","nri","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.03392627832914861                                                      |
| Q                              | 88.14386693035453                                                        |
| df                             | 65                                                                       |
| components.hypericum.est       | 0.6485127409350306                                                       |
| components.hypericum.se        | 0.10619714916495668                                                      |
| components.low-dose sari.est   | 0.49842939891949756                                                      |
| components.low-dose sari.se    | 0.1983618181123371                                                       |
| components.nassa.est           | 0.07071549870554755                                                      |
| components.nassa.se            | 0.1524222497640081                                                       |
| components.nri.est             | 0.3232266009713981                                                       |
| components.nri.se              | 0.2633830590389853                                                       |
| components.rmao-a.est          | 0.012935505413319393                                                     |
| components.rmao-a.se           | 0.2140264285574117                                                       |
| components.snri.est            | 0.5581365538244457                                                       |
| components.snri.se             | 0.15790717739154056                                                      |
| components.ssri.est            | 0.49218932927193954                                                      |
| components.ssri.se             | 0.08321449287998779                                                      |
| components.tca.est             | 0.5113390736991237                                                       |
| components.tca.se              | 0.09037663220714258                                                      |
| combinations.hypericum.est     | 0.6485127409350306                                                       |
| combinations.hypericum.se      | 0.10619714916495668                                                      |
| combinations.low-dose sari.est | 0.49842939891949756                                                      |
| combinations.low-dose sari.se  | 0.1983618181123371                                                       |
| combinations.nassa.est         | 0.07071549870554755                                                      |
| combinations.nassa.se          | 0.1524222497640081                                                       |
| combinations.nri.est           | 0.3232266009713981                                                       |
| combinations.nri.se            | 0.2633830590389853                                                       |
| combinations.rmao-a.est        | 0.012935505413319393                                                     |
| combinations.rmao-a.se         | 0.2140264285574117                                                       |
| combinations.snri.est          | 0.5581365538244457                                                       |
| combinations.snri.se           | 0.15790717739154056                                                      |
| combinations.ssri.est          | 0.49218932927193954                                                      |
| combinations.ssri.se           | 0.08321449287998779                                                      |
| combinations.tca.est           | 0.5113390736991237                                                       |
| combinations.tca.se            | 0.09037663220714258                                                      |
