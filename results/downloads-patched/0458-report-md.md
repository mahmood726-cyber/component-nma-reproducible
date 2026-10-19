# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                      | value                                                                                                                                             |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| comps                                    | ["aerobic exercise","aquatic exercise","education","electrical stimulation","placebo","proprioception exercise","strength exercise","ultrasound"] |
| tau2                                     | 0.23242283192445284                                                                                                                               |
| Q                                        | 171.85575317461047                                                                                                                                |
| df                                       | 34                                                                                                                                                |
| components.aerobic exercise.est          | -0.3880911439211968                                                                                                                               |
| components.aerobic exercise.se           | 0.18953941176522657                                                                                                                               |
| components.aquatic exercise.est          | -0.47754196556261835                                                                                                                              |
| components.aquatic exercise.se           | 0.2999373723250568                                                                                                                                |
| components.education.est                 | -0.14964745120154224                                                                                                                              |
| components.education.se                  | 0.22454091777733096                                                                                                                               |
| components.electrical stimulation.est    | -0.6619748583651601                                                                                                                               |
| components.electrical stimulation.se     | 0.29897329787799076                                                                                                                               |
| components.placebo.est                   | -0.06555351682649446                                                                                                                              |
| components.placebo.se                    | 0.40456585782410875                                                                                                                               |
| components.proprioception exercise.est   | -0.4287316697051268                                                                                                                               |
| components.proprioception exercise.se    | 0.286322274601128                                                                                                                                 |
| components.strength exercise.est         | -0.49790704247833434                                                                                                                              |
| components.strength exercise.se          | 0.1709134641289804                                                                                                                                |
| components.ultrasound.est                | -0.46555315188839574                                                                                                                              |
| components.ultrasound.se                 | 0.5591636018712816                                                                                                                                |
| combinations.aerobic exercise.est        | -0.3880911439211968                                                                                                                               |
| combinations.aerobic exercise.se         | 0.18953941176522657                                                                                                                               |
| combinations.aquatic exercise.est        | -0.47754196556261835                                                                                                                              |
| combinations.aquatic exercise.se         | 0.2999373723250568                                                                                                                                |
| combinations.education.est               | -0.14964745120154224                                                                                                                              |
| combinations.education.se                | 0.22454091777733096                                                                                                                               |
| combinations.electrical stimulation.est  | -0.6619748583651601                                                                                                                               |
| combinations.electrical stimulation.se   | 0.29897329787799076                                                                                                                               |
| combinations.placebo.est                 | -0.06555351682649446                                                                                                                              |
| combinations.placebo.se                  | 0.40456585782410875                                                                                                                               |
| combinations.proprioception exercise.est | -0.4287316697051268                                                                                                                               |
| combinations.proprioception exercise.se  | 0.286322274601128                                                                                                                                 |
| combinations.strength exercise.est       | -0.49790704247833434                                                                                                                              |
| combinations.strength exercise.se        | 0.1709134641289804                                                                                                                                |
| combinations.ultrasound.est              | -0.46555315188839574                                                                                                                              |
| combinations.ultrasound.se               | 0.5591636018712816                                                                                                                                |
