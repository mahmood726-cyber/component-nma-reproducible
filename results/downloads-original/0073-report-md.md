# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                    |
|--------------------------------|--------------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","nri","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.023467889647057268                                                     |
| Q                              | 69.3136960282615                                                         |
| df                             | 64                                                                       |
| components.hypericum.est       | 0.029835570520502452                                                     |
| components.hypericum.se        | 0.26358466956623866                                                      |
| components.low-dose sari.est   | 0.33102113311056125                                                      |
| components.low-dose sari.se    | 0.30241463283693987                                                      |
| components.nassa.est           | 1.1448107146135644                                                       |
| components.nassa.se            | 0.24081148497104823                                                      |
| components.nri.est             | 1.5595649267374356                                                       |
| components.nri.se              | 0.2861754591280207                                                       |
| components.rmao-a.est          | -0.022060253871452495                                                    |
| components.rmao-a.se           | 0.3212376926537587                                                       |
| components.snri.est            | 0.877913705745415                                                        |
| components.snri.se             | 0.21039626092278346                                                      |
| components.ssri.est            | 0.6303179958980676                                                       |
| components.ssri.se             | 0.17185089094855527                                                      |
| components.tca.est             | 0.7980691088877659                                                       |
| components.tca.se              | 0.18092242676581474                                                      |
| combinations.hypericum.est     | 0.029835570520502452                                                     |
| combinations.hypericum.se      | 0.26358466956623866                                                      |
| combinations.low-dose sari.est | 0.33102113311056125                                                      |
| combinations.low-dose sari.se  | 0.30241463283693987                                                      |
| combinations.nassa.est         | 1.1448107146135644                                                       |
| combinations.nassa.se          | 0.24081148497104823                                                      |
| combinations.nri.est           | 1.5595649267374356                                                       |
| combinations.nri.se            | 0.2861754591280207                                                       |
| combinations.rmao-a.est        | -0.022060253871452495                                                    |
| combinations.rmao-a.se         | 0.3212376926537587                                                       |
| combinations.snri.est          | 0.877913705745415                                                        |
| combinations.snri.se           | 0.21039626092278346                                                      |
| combinations.ssri.est          | 0.6303179958980676                                                       |
| combinations.ssri.se           | 0.17185089094855527                                                      |
| combinations.tca.est           | 0.7980691088877659                                                       |
| combinations.tca.se            | 0.18092242676581474                                                      |
