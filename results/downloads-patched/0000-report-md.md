# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                     | value                                                                         |
|-----------------------------------------|-------------------------------------------------------------------------------|
| comps                                   | ["budesonide","fluticasone","formoterol","placebo","salmeterol","tiotropium"] |
| tau2                                    | 0.0076245240011060915                                                         |
| Q                                       | 88.93078743065453                                                             |
| df                                      | 71                                                                            |
| components.budesonide.est               | -0.29898739441273026                                                          |
| components.budesonide.se                | 0.08760776177717843                                                           |
| components.fluticasone.est              | -0.07612146977359116                                                          |
| components.fluticasone.se               | 0.04824636506345713                                                           |
| components.formoterol.est               | -0.02285856576032208                                                          |
| components.formoterol.se                | 0.0819810167935103                                                            |
| components.placebo.est                  | 0.029058088374649405                                                          |
| components.placebo.se                   | 0.06255277623957196                                                           |
| components.salmeterol.est               | -0.15167647182434107                                                          |
| components.salmeterol.se                | 0.05244897020962303                                                           |
| components.tiotropium.est               | -0.32864715683517015                                                          |
| components.tiotropium.se                | 0.07920455241520576                                                           |
| combinations.budesonide.est             | -0.29898739441273026                                                          |
| combinations.budesonide.se              | 0.08760776177717843                                                           |
| combinations.budesonide+formoterol.est  | -0.32184596017305234                                                          |
| combinations.budesonide+formoterol.se   | 0.12815764677365127                                                           |
| combinations.fluticasone.est            | -0.07612146977359116                                                          |
| combinations.fluticasone.se             | 0.04824636506345713                                                           |
| combinations.fluticasone+salmeterol.est | -0.22779794159793224                                                          |
| combinations.fluticasone+salmeterol.se  | 0.08578826737110687                                                           |
| combinations.formoterol.est             | -0.02285856576032208                                                          |
| combinations.formoterol.se              | 0.0819810167935103                                                            |
| combinations.placebo.est                | 0.029058088374649405                                                          |
| combinations.placebo.se                 | 0.06255277623957196                                                           |
| combinations.salmeterol.est             | -0.15167647182434107                                                          |
| combinations.salmeterol.se              | 0.05244897020962303                                                           |
| combinations.tiotropium.est             | -0.32864715683517015                                                          |
| combinations.tiotropium.se              | 0.07920455241520576                                                           |
