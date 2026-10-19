# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                                                                       |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| comps                          | ["acarbose","benfluorex","metformin","miglitol","pioglitazone","rosiglitazone","sitagliptin","sulfonylurea","vildagliptin"] |
| tau2                           | 0.06032222723617649                                                                                                         |
| Q                              | 67.1544454150493                                                                                                            |
| df                             | 16                                                                                                                          |
| components.acarbose.est        | -1.233069338570889                                                                                                          |
| components.acarbose.se         | 0.2704472786575525                                                                                                          |
| components.benfluorex.est      | -0.5942456226186859                                                                                                         |
| components.benfluorex.se       | 0.21708292609875862                                                                                                         |
| components.metformin.est       | -0.9022334198675801                                                                                                         |
| components.metformin.se        | 0.12180298556628262                                                                                                         |
| components.miglitol.est        | -0.8487149931325515                                                                                                         |
| components.miglitol.se         | 0.18370002042567898                                                                                                         |
| components.pioglitazone.est    | -0.915147725734419                                                                                                          |
| components.pioglitazone.se     | 0.17308001992724906                                                                                                         |
| components.rosiglitazone.est   | -1.0586639048840574                                                                                                         |
| components.rosiglitazone.se    | 0.09953344955142113                                                                                                         |
| components.sitagliptin.est     | -0.6063829787234043                                                                                                         |
| components.sitagliptin.se      | 0.28294411019312954                                                                                                         |
| components.sulfonylurea.est    | -0.46620381292608226                                                                                                        |
| components.sulfonylurea.se     | 0.19299932520884955                                                                                                         |
| components.vildagliptin.est    | -0.661465163775494                                                                                                          |
| components.vildagliptin.se     | 0.27501830345019923                                                                                                         |
| combinations.acarbose.est      | -1.233069338570889                                                                                                          |
| combinations.acarbose.se       | 0.2704472786575525                                                                                                          |
| combinations.benfluorex.est    | -0.5942456226186859                                                                                                         |
| combinations.benfluorex.se     | 0.21708292609875862                                                                                                         |
| combinations.metformin.est     | -0.9022334198675801                                                                                                         |
| combinations.metformin.se      | 0.12180298556628262                                                                                                         |
| combinations.miglitol.est      | -0.8487149931325515                                                                                                         |
| combinations.miglitol.se       | 0.18370002042567898                                                                                                         |
| combinations.pioglitazone.est  | -0.915147725734419                                                                                                          |
| combinations.pioglitazone.se   | 0.17308001992724906                                                                                                         |
| combinations.rosiglitazone.est | -1.0586639048840574                                                                                                         |
| combinations.rosiglitazone.se  | 0.09953344955142113                                                                                                         |
| combinations.sitagliptin.est   | -0.6063829787234043                                                                                                         |
| combinations.sitagliptin.se    | 0.28294411019312954                                                                                                         |
| combinations.sulfonylurea.est  | -0.46620381292608226                                                                                                        |
| combinations.sulfonylurea.se   | 0.19299932520884955                                                                                                         |
| combinations.vildagliptin.est  | -0.661465163775494                                                                                                          |
| combinations.vildagliptin.se   | 0.27501830345019923                                                                                                         |
