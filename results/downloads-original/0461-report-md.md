# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                      | value                                                                                                                                                                                  |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| comps                                    | ["aerobic exercise","aquatic exercise","diathermy (high)","diathermy (low)","education","electrical stimulation","placebo","proprioception exercise","strength exercise","ultrasound"] |
| tau2                                     | 0.8850099243226233                                                                                                                                                                     |
| Q                                        | 310.2180260955123                                                                                                                                                                      |
| df                                       | 26                                                                                                                                                                                     |
| components.aerobic exercise.est          | -1.3266095316784334                                                                                                                                                                    |
| components.aerobic exercise.se           | 0.4085808985973444                                                                                                                                                                     |
| components.aquatic exercise.est          | -0.42067518715255375                                                                                                                                                                   |
| components.aquatic exercise.se           | 0.5404617779003953                                                                                                                                                                     |
| components.diathermy (high).est          | 0.06478963965978612                                                                                                                                                                    |
| components.diathermy (high).se           | 1.279074284813741                                                                                                                                                                      |
| components.diathermy (low).est           | 0.3947915016863788                                                                                                                                                                     |
| components.diathermy (low).se            | 1.2832001017901735                                                                                                                                                                     |
| components.education.est                 | -0.8769097808041968                                                                                                                                                                    |
| components.education.se                  | 0.5059118976847005                                                                                                                                                                     |
| components.electrical stimulation.est    | 0.07958281785786381                                                                                                                                                                    |
| components.electrical stimulation.se     | 1.383934355244872                                                                                                                                                                      |
| components.placebo.est                   | 0.6393904683215657                                                                                                                                                                     |
| components.placebo.se                    | 1.1455054987258892                                                                                                                                                                     |
| components.proprioception exercise.est   | -0.8323246874688416                                                                                                                                                                    |
| components.proprioception exercise.se    | 0.637897530645912                                                                                                                                                                      |
| components.strength exercise.est         | -0.6623861910513722                                                                                                                                                                    |
| components.strength exercise.se          | 0.38177101051632384                                                                                                                                                                    |
| components.ultrasound.est                | 0.3218872050739068                                                                                                                                                                     |
| components.ultrasound.se                 | 1.3535796002519953                                                                                                                                                                     |
| combinations.aerobic exercise.est        | -1.3266095316784334                                                                                                                                                                    |
| combinations.aerobic exercise.se         | 0.4085808985973444                                                                                                                                                                     |
| combinations.aquatic exercise.est        | -0.42067518715255375                                                                                                                                                                   |
| combinations.aquatic exercise.se         | 0.5404617779003953                                                                                                                                                                     |
| combinations.diathermy (high).est        | 0.06478963965978612                                                                                                                                                                    |
| combinations.diathermy (high).se         | 1.279074284813741                                                                                                                                                                      |
| combinations.diathermy (low).est         | 0.3947915016863788                                                                                                                                                                     |
| combinations.diathermy (low).se          | 1.2832001017901735                                                                                                                                                                     |
| combinations.education.est               | -0.8769097808041968                                                                                                                                                                    |
| combinations.education.se                | 0.5059118976847005                                                                                                                                                                     |
| combinations.electrical stimulation.est  | 0.07958281785786381                                                                                                                                                                    |
| combinations.electrical stimulation.se   | 1.383934355244872                                                                                                                                                                      |
| combinations.placebo.est                 | 0.6393904683215657                                                                                                                                                                     |
| combinations.placebo.se                  | 1.1455054987258892                                                                                                                                                                     |
| combinations.proprioception exercise.est | -0.8323246874688416                                                                                                                                                                    |
| combinations.proprioception exercise.se  | 0.637897530645912                                                                                                                                                                      |
| combinations.strength exercise.est       | -0.6623861910513722                                                                                                                                                                    |
| combinations.strength exercise.se        | 0.38177101051632384                                                                                                                                                                    |
| combinations.ultrasound.est              | 0.3218872050739068                                                                                                                                                                     |
| combinations.ultrasound.se               | 1.3535796002519953                                                                                                                                                                     |
