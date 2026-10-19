# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                   | value                                                                                            |
|---------------------------------------|--------------------------------------------------------------------------------------------------|
| comps                                 | ["apixaban","aspirin","clopidogtrel","dabigatran 110mg","dabigatran 150mg","rivaroxaban","vkas"] |
| tau2                                  | 0                                                                                                |
| Q                                     | 20.56863724324987                                                                                |
| df                                    | 21                                                                                               |
| components.apixaban.est               | -1.0321886097059998                                                                              |
| components.apixaban.se                | 0.1235743227815864                                                                               |
| components.aspirin.est                | -0.20839885712105916                                                                             |
| components.aspirin.se                 | 0.08864616852161165                                                                              |
| components.clopidogtrel.est           | -0.2763264582832928                                                                              |
| components.clopidogtrel.se            | 0.06766156434674181                                                                              |
| components.dabigatran 110mg.est       | -0.8921151088019152                                                                              |
| components.dabigatran 110mg.se        | 0.13337857751028157                                                                              |
| components.dabigatran 150mg.est       | -1.2398478558782027                                                                              |
| components.dabigatran 150mg.se        | 0.13652908321197824                                                                              |
| components.rivaroxaban.est            | -1.057512681496793                                                                               |
| components.rivaroxaban.se             | 0.13863175140630932                                                                              |
| components.vkas.est                   | -0.8145859208591502                                                                              |
| components.vkas.se                    | 0.10007603913925213                                                                              |
| combinations.apixaban.est             | -1.0321886097059998                                                                              |
| combinations.apixaban.se              | 0.1235743227815864                                                                               |
| combinations.aspirin.est              | -0.20839885712105916                                                                             |
| combinations.aspirin.se               | 0.08864616852161165                                                                              |
| combinations.aspirin+clopidogtrel.est | -0.48472531540435193                                                                             |
| combinations.aspirin+clopidogtrel.se  | 0.10866514176655713                                                                              |
| combinations.dabigatran 110mg.est     | -0.8921151088019152                                                                              |
| combinations.dabigatran 110mg.se      | 0.13337857751028157                                                                              |
| combinations.dabigatran 150mg.est     | -1.2398478558782027                                                                              |
| combinations.dabigatran 150mg.se      | 0.13652908321197824                                                                              |
| combinations.rivaroxaban.est          | -1.057512681496793                                                                               |
| combinations.rivaroxaban.se           | 0.13863175140630932                                                                              |
| combinations.vkas.est                 | -0.8145859208591502                                                                              |
| combinations.vkas.se                  | 0.10007603913925213                                                                              |
