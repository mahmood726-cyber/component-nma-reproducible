# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                       | value                                        |
|---------------------------|----------------------------------------------|
| comps                     | ["ics","laba","laba-ics","tio-hh","tio-smi"] |
| tau2                      | 0                                            |
| Q                         | 18.65507833642108                            |
| df                        | 26                                           |
| components.ics.est        | -0.09558471636316627                         |
| components.ics.se         | 0.19651273922717596                          |
| components.laba.est       | 0.05506857000538506                          |
| components.laba.se        | 0.1627896369839955                           |
| components.laba-ics.est   | -0.3593390073237464                          |
| components.laba-ics.se    | 0.21918187360699382                          |
| components.tio-hh.est     | -0.06576792495969133                         |
| components.tio-hh.se      | 0.07090845149592714                          |
| components.tio-smi.est    | 0.4081760205652836                           |
| components.tio-smi.se     | 0.18727044459884148                          |
| combinations.ics.est      | -0.09558471636316627                         |
| combinations.ics.se       | 0.19651273922717596                          |
| combinations.laba.est     | 0.05506857000538506                          |
| combinations.laba.se      | 0.1627896369839955                           |
| combinations.laba-ics.est | -0.3593390073237464                          |
| combinations.laba-ics.se  | 0.21918187360699382                          |
| combinations.tio-hh.est   | -0.06576792495969133                         |
| combinations.tio-hh.se    | 0.07090845149592714                          |
| combinations.tio-smi.est  | 0.4081760205652836                           |
| combinations.tio-smi.se   | 0.18727044459884148                          |
