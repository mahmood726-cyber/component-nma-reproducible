# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                       | value                             |
|---------------------------|-----------------------------------|
| comps                     | ["ics","laba","tio-hh","tio-smi"] |
| tau2                      | 0                                 |
| Q                         | 19.735865398499964                |
| df                        | 27                                |
| components.ics.est        | -0.23242934004996776              |
| components.ics.se         | 0.1365903085103703                |
| components.laba.est       | 0.012784714500792799              |
| components.laba.se        | 0.15184272727944897               |
| components.tio-hh.est     | -0.05869493375091217              |
| components.tio-hh.se      | 0.06249281124612662               |
| components.tio-smi.est    | 0.39884370875734876               |
| components.tio-smi.se     | 0.18340932894529696               |
| combinations.ics.est      | -0.23242934004996776              |
| combinations.ics.se       | 0.1365903085103703                |
| combinations.ics+laba.est | -0.21964462554917497              |
| combinations.ics+laba.se  | 0.17838987898306088               |
| combinations.laba.est     | 0.012784714500792799              |
| combinations.laba.se      | 0.15184272727944897               |
| combinations.tio-hh.est   | -0.05869493375091217              |
| combinations.tio-hh.se    | 0.06249281124612662               |
| combinations.tio-smi.est  | 0.39884370875734876               |
| combinations.tio-smi.se   | 0.18340932894529696               |
