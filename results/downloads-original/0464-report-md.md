# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                      | value                                                                                                                                             |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| comps                                    | ["aerobic exercise","aquatic exercise","education","electrical stimulation","placebo","proprioception exercise","strength exercise","ultrasound"] |
| tau2                                     | 2.0479731558375507                                                                                                                                |
| Q                                        | 301.58520941427975                                                                                                                                |
| df                                       | 13                                                                                                                                                |
| components.aerobic exercise.est          | -1.5776302848107155                                                                                                                               |
| components.aerobic exercise.se           | 0.6677372277063519                                                                                                                                |
| components.aquatic exercise.est          | -0.6129595154397951                                                                                                                               |
| components.aquatic exercise.se           | 1.1381904596497274                                                                                                                                |
| components.education.est                 | -1.1939862524886262                                                                                                                               |
| components.education.se                  | 0.8750124977215514                                                                                                                                |
| components.electrical stimulation.est    | -0.17079614692157696                                                                                                                              |
| components.electrical stimulation.se     | 1.9846291439495645                                                                                                                                |
| components.placebo.est                   | 0.38836971518928576                                                                                                                               |
| components.placebo.se                    | 1.659542326574568                                                                                                                                 |
| components.proprioception exercise.est   | -0.7716573661550274                                                                                                                               |
| components.proprioception exercise.se    | 0.9168245747929171                                                                                                                                |
| components.strength exercise.est         | -0.5508386881497747                                                                                                                               |
| components.strength exercise.se          | 0.7124298016765171                                                                                                                                |
| components.ultrasound.est                | 0.07113212953749226                                                                                                                               |
| components.ultrasound.se                 | 1.9635576441023925                                                                                                                                |
| combinations.aerobic exercise.est        | -1.5776302848107155                                                                                                                               |
| combinations.aerobic exercise.se         | 0.6677372277063519                                                                                                                                |
| combinations.aquatic exercise.est        | -0.6129595154397951                                                                                                                               |
| combinations.aquatic exercise.se         | 1.1381904596497274                                                                                                                                |
| combinations.education.est               | -1.1939862524886262                                                                                                                               |
| combinations.education.se                | 0.8750124977215514                                                                                                                                |
| combinations.electrical stimulation.est  | -0.17079614692157696                                                                                                                              |
| combinations.electrical stimulation.se   | 1.9846291439495645                                                                                                                                |
| combinations.placebo.est                 | 0.38836971518928576                                                                                                                               |
| combinations.placebo.se                  | 1.659542326574568                                                                                                                                 |
| combinations.proprioception exercise.est | -0.7716573661550274                                                                                                                               |
| combinations.proprioception exercise.se  | 0.9168245747929171                                                                                                                                |
| combinations.strength exercise.est       | -0.5508386881497747                                                                                                                               |
| combinations.strength exercise.se        | 0.7124298016765171                                                                                                                                |
| combinations.ultrasound.est              | 0.07113212953749226                                                                                                                               |
| combinations.ultrasound.se               | 1.9635576441023925                                                                                                                                |
