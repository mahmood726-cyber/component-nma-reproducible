# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                                                                    |
|--------------------------------|--------------------------------------------------------------------------|
| comps                          | ["hypericum","low-dose sari","nassa","nri","rmao-a","snri","ssri","tca"] |
| tau2                           | 0.006934680286696824                                                     |
| Q                              | 51.027931317235314                                                       |
| df                             | 42                                                                       |
| components.hypericum.est       | 0.43977314935223144                                                      |
| components.hypericum.se        | 0.10345061153738216                                                      |
| components.low-dose sari.est   | 0.5353200489507837                                                       |
| components.low-dose sari.se    | 0.16139393543528668                                                      |
| components.nassa.est           | 0.36842995748084373                                                      |
| components.nassa.se            | 0.12280337999616714                                                      |
| components.nri.est             | 0.35566909557308446                                                      |
| components.nri.se              | 0.19748462293814253                                                      |
| components.rmao-a.est          | 0.261582230254357                                                        |
| components.rmao-a.se           | 0.1215206553824917                                                       |
| components.snri.est            | 0.4232430728185067                                                       |
| components.snri.se             | 0.0993482397312607                                                       |
| components.ssri.est            | 0.3557791126258386                                                       |
| components.ssri.se             | 0.07524241790171221                                                      |
| components.tca.est             | 0.37000329068128057                                                      |
| components.tca.se              | 0.07864579895008111                                                      |
| combinations.hypericum.est     | 0.43977314935223144                                                      |
| combinations.hypericum.se      | 0.10345061153738216                                                      |
| combinations.low-dose sari.est | 0.5353200489507837                                                       |
| combinations.low-dose sari.se  | 0.16139393543528668                                                      |
| combinations.nassa.est         | 0.36842995748084373                                                      |
| combinations.nassa.se          | 0.12280337999616714                                                      |
| combinations.nri.est           | 0.35566909557308446                                                      |
| combinations.nri.se            | 0.19748462293814253                                                      |
| combinations.rmao-a.est        | 0.261582230254357                                                        |
| combinations.rmao-a.se         | 0.1215206553824917                                                       |
| combinations.snri.est          | 0.4232430728185067                                                       |
| combinations.snri.se           | 0.0993482397312607                                                       |
| combinations.ssri.est          | 0.3557791126258386                                                       |
| combinations.ssri.se           | 0.07524241790171221                                                      |
| combinations.tca.est           | 0.37000329068128057                                                      |
| combinations.tca.se            | 0.07864579895008111                                                      |
