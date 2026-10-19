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
| Q                            | 4.312270636608236                                    |
| df                           | 5                                                    |
| components.aspirin.est       | -0.015625                                            |
| components.aspirin.se        | 4069072.568929565                                    |
| components.clopidogrel.est   | -0.03125                                             |
| components.clopidogrel.se    | 4069072.5689295656                                   |
| components.ticagrelor.est    | 0.078125                                             |
| components.ticagrelor.se     | 4069072.568929568                                    |
| components.ticlopidine.est   | -0.078125                                            |
| components.ticlopidine.se    | 4069072.568929566                                    |
| combinations.aspirin.est     | -0.015625                                            |
| combinations.aspirin.se      | 4069072.568929565                                    |
| combinations.clopidogrel.est | -0.03125                                             |
| combinations.clopidogrel.se  | 4069072.5689295656                                   |
| combinations.ticagrelor.est  | 0.078125                                             |
| combinations.ticagrelor.se   | 4069072.568929568                                    |
| combinations.ticlopidine.est | -0.078125                                            |
| combinations.ticlopidine.se  | 4069072.568929566                                    |
