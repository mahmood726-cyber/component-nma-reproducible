# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                      | value                                                                                                                                                  |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| comps                                    | ["aerobic exercise","aquatic exercise","education","electrical stimulation","no treatment","proprioception exercise","strength exercise","ultrasound"] |
| tau2                                     | 0.23638430598429738                                                                                                                                    |
| Q                                        | 77.95098089798212                                                                                                                                      |
| df                                       | 13                                                                                                                                                     |
| components.aerobic exercise.est          | -0.8500303783215202                                                                                                                                    |
| components.aerobic exercise.se           | 0.5375284126850098                                                                                                                                     |
| components.aquatic exercise.est          | -0.43646619793794694                                                                                                                                   |
| components.aquatic exercise.se           | 0.6886084266426876                                                                                                                                     |
| components.education.est                 | -0.668381666405645                                                                                                                                     |
| components.education.se                  | 0.5989235067069719                                                                                                                                     |
| components.electrical stimulation.est    | -0.27404365904079186                                                                                                                                   |
| components.electrical stimulation.se     | 0.40369171994781716                                                                                                                                    |
| components.no treatment.est              | -0.17510143615029516                                                                                                                                   |
| components.no treatment.se               | 0.5953090756346964                                                                                                                                     |
| components.proprioception exercise.est   | -0.6358188320653956                                                                                                                                    |
| components.proprioception exercise.se    | 0.6831622881910803                                                                                                                                     |
| components.strength exercise.est         | -0.4676089152129026                                                                                                                                    |
| components.strength exercise.se          | 0.636235173865558                                                                                                                                      |
| components.ultrasound.est                | -0.20082206822310333                                                                                                                                   |
| components.ultrasound.se                 | 0.38728927795374524                                                                                                                                    |
| combinations.aerobic exercise.est        | -0.8500303783215202                                                                                                                                    |
| combinations.aerobic exercise.se         | 0.5375284126850098                                                                                                                                     |
| combinations.aquatic exercise.est        | -0.43646619793794694                                                                                                                                   |
| combinations.aquatic exercise.se         | 0.6886084266426876                                                                                                                                     |
| combinations.education.est               | -0.668381666405645                                                                                                                                     |
| combinations.education.se                | 0.5989235067069719                                                                                                                                     |
| combinations.electrical stimulation.est  | -0.27404365904079186                                                                                                                                   |
| combinations.electrical stimulation.se   | 0.40369171994781716                                                                                                                                    |
| combinations.no treatment.est            | -0.17510143615029516                                                                                                                                   |
| combinations.no treatment.se             | 0.5953090756346964                                                                                                                                     |
| combinations.proprioception exercise.est | -0.6358188320653956                                                                                                                                    |
| combinations.proprioception exercise.se  | 0.6831622881910803                                                                                                                                     |
| combinations.strength exercise.est       | -0.4676089152129026                                                                                                                                    |
| combinations.strength exercise.se        | 0.636235173865558                                                                                                                                      |
| combinations.ultrasound.est              | -0.20082206822310333                                                                                                                                   |
| combinations.ultrasound.se               | 0.38728927795374524                                                                                                                                    |
