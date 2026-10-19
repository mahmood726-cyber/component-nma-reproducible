# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                          | value                                                |
|------------------------------|------------------------------------------------------|
| comps                        | ["aspirin","clopidogrel","ticagrelor","ticlopidine"] |
| tau2                         | 0                                                    |
| Q                            | 2.0352421996559276                                   |
| df                           | 3                                                    |
| components.aspirin.est       | 0.0234375                                            |
| components.aspirin.se        | NaN                                                  |
| components.clopidogrel.est   | -0.0390625                                           |
| components.clopidogrel.se    | NaN                                                  |
| components.ticagrelor.est    | 0.0703125                                            |
| components.ticagrelor.se     | NaN                                                  |
| components.ticlopidine.est   | 0.0859375                                            |
| components.ticlopidine.se    | NaN                                                  |
| combinations.aspirin.est     | 0.0234375                                            |
| combinations.aspirin.se      | 0                                                    |
| combinations.clopidogrel.est | -0.0390625                                           |
| combinations.clopidogrel.se  | 0                                                    |
| combinations.ticagrelor.est  | 0.0703125                                            |
| combinations.ticagrelor.se   | 0                                                    |
| combinations.ticlopidine.est | 0.0859375                                            |
| combinations.ticlopidine.se  | 0                                                    |
