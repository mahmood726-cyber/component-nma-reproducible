# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                      | value                                                                                                                                                  |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| comps                                    | ["aerobic exercise","aquatic exercise","education","electrical stimulation","no treatment","proprioception exercise","strength exercise","ultrasound"] |
| tau2                                     | 2.047973155837624                                                                                                                                      |
| Q                                        | 301.5852094142797                                                                                                                                      |
| df                                       | 13                                                                                                                                                     |
| components.aerobic exercise.est          | -1.9659999999999984                                                                                                                                    |
| components.aerobic exercise.se           | 1.5192786868865242                                                                                                                                     |
| components.aquatic exercise.est          | -1.0013292306290813                                                                                                                                    |
| components.aquatic exercise.se           | 1.9359932557116961                                                                                                                                     |
| components.education.est                 | -1.582355967677911                                                                                                                                     |
| components.education.se                  | 1.695011042804063                                                                                                                                      |
| components.electrical stimulation.est    | -0.5591658621108629                                                                                                                                    |
| components.electrical stimulation.se     | 1.0884264354201842                                                                                                                                     |
| components.no treatment.est              | -0.3883697151892842                                                                                                                                    |
| components.no treatment.se               | 1.6595423265745954                                                                                                                                     |
| components.proprioception exercise.est   | -1.16002708134431                                                                                                                                      |
| components.proprioception exercise.se    | 1.8852654081678237                                                                                                                                     |
| components.strength exercise.est         | -0.9392084033390602                                                                                                                                    |
| components.strength exercise.se          | 1.7745426490431535                                                                                                                                     |
| components.ultrasound.est                | -0.3172375856517935                                                                                                                                    |
| components.ultrasound.se                 | 1.049513167149629                                                                                                                                      |
| combinations.aerobic exercise.est        | -1.9659999999999984                                                                                                                                    |
| combinations.aerobic exercise.se         | 1.5192786868865242                                                                                                                                     |
| combinations.aquatic exercise.est        | -1.0013292306290813                                                                                                                                    |
| combinations.aquatic exercise.se         | 1.9359932557116961                                                                                                                                     |
| combinations.education.est               | -1.582355967677911                                                                                                                                     |
| combinations.education.se                | 1.695011042804063                                                                                                                                      |
| combinations.electrical stimulation.est  | -0.5591658621108629                                                                                                                                    |
| combinations.electrical stimulation.se   | 1.0884264354201842                                                                                                                                     |
| combinations.no treatment.est            | -0.3883697151892842                                                                                                                                    |
| combinations.no treatment.se             | 1.6595423265745954                                                                                                                                     |
| combinations.proprioception exercise.est | -1.16002708134431                                                                                                                                      |
| combinations.proprioception exercise.se  | 1.8852654081678237                                                                                                                                     |
| combinations.strength exercise.est       | -0.9392084033390602                                                                                                                                    |
| combinations.strength exercise.se        | 1.7745426490431535                                                                                                                                     |
| combinations.ultrasound.est              | -0.3172375856517935                                                                                                                                    |
| combinations.ultrasound.se               | 1.049513167149629                                                                                                                                      |
