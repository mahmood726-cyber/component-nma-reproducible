# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                    |
|--------------------------------|--------------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","nri","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.06095644067198282                                                      |
| Q                              | 92.09901493396316                                                        |
| df                             | 65                                                                       |
| components.hypericum.est       | -0.27043560659060695                                                     |
| components.hypericum.se        | 0.1583862902598192                                                       |
| components.low-dose sari.est   | -0.37129815753729867                                                     |
| components.low-dose sari.se    | 0.26404805598425724                                                      |
| components.nassa.est           | 0.08443459759183922                                                      |
| components.nassa.se            | 0.22208516254084285                                                      |
| components.nri.est             | 0.5478176317775567                                                       |
| components.nri.se              | 0.34723652085067724                                                      |
| components.rmao-a.est          | -0.1153692854229189                                                      |
| components.rmao-a.se           | 0.23443898048974576                                                      |
| components.snri.est            | -0.010490081366474238                                                    |
| components.snri.se             | 0.17315041166992448                                                      |
| components.ssri.est            | -0.00278378980637721                                                     |
| components.ssri.se             | 0.11989545596032819                                                      |
| components.tca.est             | -0.009227188912921416                                                    |
| components.tca.se              | 0.11577572694776385                                                      |
| combinations.hypericum.est     | -0.27043560659060695                                                     |
| combinations.hypericum.se      | 0.1583862902598192                                                       |
| combinations.low-dose sari.est | -0.37129815753729867                                                     |
| combinations.low-dose sari.se  | 0.26404805598425724                                                      |
| combinations.nassa.est         | 0.08443459759183922                                                      |
| combinations.nassa.se          | 0.22208516254084285                                                      |
| combinations.nri.est           | 0.5478176317775567                                                       |
| combinations.nri.se            | 0.34723652085067724                                                      |
| combinations.rmao-a.est        | -0.1153692854229189                                                      |
| combinations.rmao-a.se         | 0.23443898048974576                                                      |
| combinations.snri.est          | -0.010490081366474238                                                    |
| combinations.snri.se           | 0.17315041166992448                                                      |
| combinations.ssri.est          | -0.00278378980637721                                                     |
| combinations.ssri.se           | 0.11989545596032819                                                      |
| combinations.tca.est           | -0.009227188912921416                                                    |
| combinations.tca.se            | 0.11577572694776385                                                      |
