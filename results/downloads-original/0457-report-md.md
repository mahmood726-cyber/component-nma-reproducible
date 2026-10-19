# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                      | value                                                                                                                                                            |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| comps                                    | ["aerobic exercise","aquatic exercise","education","electrical stimulation","no treatment","placebo","proprioception exercise","strength exercise","ultrasound"] |
| tau2                                     | 0.24208394868740896                                                                                                                                              |
| Q                                        | 178.93893713728175                                                                                                                                               |
| df                                       | 33                                                                                                                                                               |
| components.aerobic exercise.est          | -0.171875                                                                                                                                                        |
| components.aerobic exercise.se           | NaN                                                                                                                                                              |
| components.aquatic exercise.est          | -0.421875                                                                                                                                                        |
| components.aquatic exercise.se           | NaN                                                                                                                                                              |
| components.education.est                 | -0.296875                                                                                                                                                        |
| components.education.se                  | NaN                                                                                                                                                              |
| components.electrical stimulation.est    | -0.625                                                                                                                                                           |
| components.electrical stimulation.se     | NaN                                                                                                                                                              |
| components.no treatment.est              | -0.171875                                                                                                                                                        |
| components.no treatment.se               | NaN                                                                                                                                                              |
| components.placebo.est                   | -0.15625                                                                                                                                                         |
| components.placebo.se                    | NaN                                                                                                                                                              |
| components.proprioception exercise.est   | -0.25                                                                                                                                                            |
| components.proprioception exercise.se    | NaN                                                                                                                                                              |
| components.strength exercise.est         | -0.171875                                                                                                                                                        |
| components.strength exercise.se          | NaN                                                                                                                                                              |
| components.ultrasound.est                | -0.5625                                                                                                                                                          |
| components.ultrasound.se                 | NaN                                                                                                                                                              |
| combinations.aerobic exercise.est        | -0.171875                                                                                                                                                        |
| combinations.aerobic exercise.se         | 0                                                                                                                                                                |
| combinations.aquatic exercise.est        | -0.421875                                                                                                                                                        |
| combinations.aquatic exercise.se         | 0                                                                                                                                                                |
| combinations.education.est               | -0.296875                                                                                                                                                        |
| combinations.education.se                | 0                                                                                                                                                                |
| combinations.electrical stimulation.est  | -0.625                                                                                                                                                           |
| combinations.electrical stimulation.se   | 0                                                                                                                                                                |
| combinations.no treatment.est            | -0.171875                                                                                                                                                        |
| combinations.no treatment.se             | 0                                                                                                                                                                |
| combinations.placebo.est                 | -0.15625                                                                                                                                                         |
| combinations.placebo.se                  | 0                                                                                                                                                                |
| combinations.proprioception exercise.est | -0.25                                                                                                                                                            |
| combinations.proprioception exercise.se  | 0                                                                                                                                                                |
| combinations.strength exercise.est       | -0.171875                                                                                                                                                        |
| combinations.strength exercise.se        | 0                                                                                                                                                                |
| combinations.ultrasound.est              | -0.5625                                                                                                                                                          |
| combinations.ultrasound.se               | 0                                                                                                                                                                |
