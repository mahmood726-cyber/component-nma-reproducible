# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                       | value                             |
|---------------------------|-----------------------------------|
| comps                     | ["ics","laba","tio-hh","tio-smi"] |
| tau2                      | 0                                 |
| Q                         | 55.87393461734511                 |
| df                        | 78                                |
| components.ics.est        | -0.03947889454827376              |
| components.ics.se         | 0.04055089627516963               |
| components.laba.est       | -0.15316301298496604              |
| components.laba.se        | 0.040898235092315945              |
| components.tio-hh.est     | -0.08663149033936879              |
| components.tio-hh.se      | 0.05781281235194825               |
| components.tio-smi.est    | 0.39884370875734876               |
| components.tio-smi.se     | 0.18340932894529696               |
| combinations.ics.est      | -0.03947889454827376              |
| combinations.ics.se       | 0.04055089627516963               |
| combinations.ics+laba.est | -0.1926419075332398               |
| combinations.ics+laba.se  | 0.05731634301161121               |
| combinations.laba.est     | -0.15316301298496604              |
| combinations.laba.se      | 0.040898235092315945              |
| combinations.tio-hh.est   | -0.08663149033936879              |
| combinations.tio-hh.se    | 0.05781281235194825               |
| combinations.tio-smi.est  | 0.39884370875734876               |
| combinations.tio-smi.se   | 0.18340932894529696               |
