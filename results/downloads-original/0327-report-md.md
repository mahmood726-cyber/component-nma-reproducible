# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                             | value                                                                    |
|---------------------------------|--------------------------------------------------------------------------|
| comps                           | ["f2f cbt","hybrid cbt","multimedia cbt","no treatment","placebo","tau"] |
| tau2                            | 0.2887444224306886                                                       |
| Q                               | 13362.816616080285                                                       |
| df                              | 60                                                                       |
| components.f2f cbt.est          | -1.829972855375646                                                       |
| components.f2f cbt.se           | 0.13756791339974944                                                      |
| components.hybrid cbt.est       | -1.745941873928364                                                       |
| components.hybrid cbt.se        | 0.2316151327111558                                                       |
| components.multimedia cbt.est   | -1.3341205698799705                                                      |
| components.multimedia cbt.se    | 0.1766187962572703                                                       |
| components.no treatment.est     | -0.5235469228042542                                                      |
| components.no treatment.se      | 0.26436136302661467                                                      |
| components.placebo.est          | -1.0200331940107576                                                      |
| components.placebo.se           | 0.21496747932882                                                         |
| components.tau.est              | -0.7013992131034295                                                      |
| components.tau.se               | 0.16972597231841888                                                      |
| combinations.f2f cbt.est        | -1.829972855375646                                                       |
| combinations.f2f cbt.se         | 0.13756791339974944                                                      |
| combinations.hybrid cbt.est     | -1.745941873928364                                                       |
| combinations.hybrid cbt.se      | 0.2316151327111558                                                       |
| combinations.multimedia cbt.est | -1.3341205698799705                                                      |
| combinations.multimedia cbt.se  | 0.1766187962572703                                                       |
| combinations.no treatment.est   | -0.5235469228042542                                                      |
| combinations.no treatment.se    | 0.26436136302661467                                                      |
| combinations.placebo.est        | -1.0200331940107576                                                      |
| combinations.placebo.se         | 0.21496747932882                                                         |
| combinations.tau.est            | -0.7013992131034295                                                      |
| combinations.tau.se             | 0.16972597231841888                                                      |
