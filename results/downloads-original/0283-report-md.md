# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                    |
|--------------------------------|--------------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","nri","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.006463967663231899                                                     |
| Q                              | 58.99722340029089                                                        |
| df                             | 44                                                                       |
| components.hypericum.est       | 0.3859755257271339                                                       |
| components.hypericum.se        | 0.06987449121351336                                                      |
| components.low-dose sari.est   | 0.4852129294512688                                                       |
| components.low-dose sari.se    | 0.12556485828316685                                                      |
| components.nassa.est           | 0.24135712498279996                                                      |
| components.nassa.se            | 0.10090390714624056                                                      |
| components.nri.est             | 0.22154284885879294                                                      |
| components.nri.se              | 0.14550301396006385                                                      |
| components.rmao-a.est          | 0.14929860040663442                                                      |
| components.rmao-a.se           | 0.10745026914936108                                                      |
| components.snri.est            | 0.31953092340631045                                                      |
| components.snri.se             | 0.08589631902140898                                                      |
| components.ssri.est            | 0.32752726819860756                                                      |
| components.ssri.se             | 0.05891002630867347                                                      |
| components.tca.est             | 0.3480722509497322                                                       |
| components.tca.se              | 0.06338088804823211                                                      |
| combinations.hypericum.est     | 0.3859755257271339                                                       |
| combinations.hypericum.se      | 0.06987449121351336                                                      |
| combinations.low-dose sari.est | 0.4852129294512688                                                       |
| combinations.low-dose sari.se  | 0.12556485828316685                                                      |
| combinations.nassa.est         | 0.24135712498279996                                                      |
| combinations.nassa.se          | 0.10090390714624056                                                      |
| combinations.nri.est           | 0.22154284885879294                                                      |
| combinations.nri.se            | 0.14550301396006385                                                      |
| combinations.rmao-a.est        | 0.14929860040663442                                                      |
| combinations.rmao-a.se         | 0.10745026914936108                                                      |
| combinations.snri.est          | 0.31953092340631045                                                      |
| combinations.snri.se           | 0.08589631902140898                                                      |
| combinations.ssri.est          | 0.32752726819860756                                                      |
| combinations.ssri.se           | 0.05891002630867347                                                      |
| combinations.tca.est           | 0.3480722509497322                                                       |
| combinations.tca.se            | 0.06338088804823211                                                      |
