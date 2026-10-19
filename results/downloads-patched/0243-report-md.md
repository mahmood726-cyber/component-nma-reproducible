# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                       | value                                                                                         |
|-------------------------------------------|-----------------------------------------------------------------------------------------------|
| comps                                     | ["antithrombin iii","aprotonin","eaca","rfviia","solvent detergent plasma","tranexamic acid"] |
| tau2                                      | 0                                                                                             |
| Q                                         | 3.8711545256870883                                                                            |
| df                                        | 10                                                                                            |
| components.antithrombin iii.est           | -1.408767216971949                                                                            |
| components.antithrombin iii.se            | 1.5050979587122777                                                                            |
| components.aprotonin.est                  | -0.8299336519813145                                                                           |
| components.aprotonin.se                   | 0.46174703056989985                                                                           |
| components.eaca.est                       | -0.21903734245613454                                                                          |
| components.eaca.se                        | 0.6482852388925661                                                                            |
| components.rfviia.est                     | 0.3546939854386779                                                                            |
| components.rfviia.se                      | 0.7235614309226788                                                                            |
| components.solvent detergent plasma.est   | 0.07696104113612844                                                                           |
| components.solvent detergent plasma.se    | 1.961103242036463                                                                             |
| components.tranexamic acid.est            | -0.12332238169462864                                                                          |
| components.tranexamic acid.se             | 0.5108302038771639                                                                            |
| combinations.antithrombin iii.est         | -1.408767216971949                                                                            |
| combinations.antithrombin iii.se          | 1.5050979587122777                                                                            |
| combinations.aprotonin.est                | -0.8299336519813145                                                                           |
| combinations.aprotonin.se                 | 0.46174703056989985                                                                           |
| combinations.eaca.est                     | -0.21903734245613454                                                                          |
| combinations.eaca.se                      | 0.6482852388925661                                                                            |
| combinations.rfviia.est                   | 0.3546939854386779                                                                            |
| combinations.rfviia.se                    | 0.7235614309226788                                                                            |
| combinations.solvent detergent plasma.est | 0.07696104113612844                                                                           |
| combinations.solvent detergent plasma.se  | 1.961103242036463                                                                             |
| combinations.tranexamic acid.est          | -0.12332238169462864                                                                          |
| combinations.tranexamic acid.se           | 0.5108302038771639                                                                            |
