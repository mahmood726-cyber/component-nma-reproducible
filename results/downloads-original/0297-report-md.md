# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                    |
|--------------------------------|--------------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","nri","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.02692262581388197                                                      |
| Q                              | 87.64228024134205                                                        |
| df                             | 65                                                                       |
| components.hypericum.est       | -0.2195959057506039                                                      |
| components.hypericum.se        | 0.12543198747243545                                                      |
| components.low-dose sari.est   | -0.28151613342957027                                                     |
| components.low-dose sari.se    | 0.19679075551011146                                                      |
| components.nassa.est           | 0.05796407812153239                                                      |
| components.nassa.se            | 0.15529665610648238                                                      |
| components.nri.est             | 0.44542567184668985                                                      |
| components.nri.se              | 0.25555872795458184                                                      |
| components.rmao-a.est          | -0.09553910461326233                                                     |
| components.rmao-a.se           | 0.17488196381213894                                                      |
| components.snri.est            | -0.0029219971019997584                                                   |
| components.snri.se             | 0.12254183406593763                                                      |
| components.ssri.est            | -0.0022406172804431204                                                   |
| components.ssri.se             | 0.08961409117926077                                                      |
| components.tca.est             | -0.0029204073984523404                                                   |
| components.tca.se              | 0.08403800121188192                                                      |
| combinations.hypericum.est     | -0.2195959057506039                                                      |
| combinations.hypericum.se      | 0.12543198747243545                                                      |
| combinations.low-dose sari.est | -0.28151613342957027                                                     |
| combinations.low-dose sari.se  | 0.19679075551011146                                                      |
| combinations.nassa.est         | 0.05796407812153239                                                      |
| combinations.nassa.se          | 0.15529665610648238                                                      |
| combinations.nri.est           | 0.44542567184668985                                                      |
| combinations.nri.se            | 0.25555872795458184                                                      |
| combinations.rmao-a.est        | -0.09553910461326233                                                     |
| combinations.rmao-a.se         | 0.17488196381213894                                                      |
| combinations.snri.est          | -0.0029219971019997584                                                   |
| combinations.snri.se           | 0.12254183406593763                                                      |
| combinations.ssri.est          | -0.0022406172804431204                                                   |
| combinations.ssri.se           | 0.08961409117926077                                                      |
| combinations.tca.est           | -0.0029204073984523404                                                   |
| combinations.tca.se            | 0.08403800121188192                                                      |
