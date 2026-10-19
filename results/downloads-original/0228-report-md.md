# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                       | value                                       |
|---------------------------|---------------------------------------------|
| comps                     | ["ics","laba","placebo","tio-hh","tio-smi"] |
| tau2                      | 0                                           |
| Q                         | 18.42419307441132                           |
| df                        | 26                                          |
| components.ics.est        | -0.40607513488112656                        |
| components.ics.se         | 0.20407111040966908                         |
| components.laba.est       | -0.2557647313212341                         |
| components.laba.se        | 0.2793538027089195                          |
| components.placebo.est    | -0.3145749526274676                         |
| components.placebo.se     | 0.2746701484927384                          |
| components.tio-hh.est     | -0.3737673120320394                         |
| components.tio-hh.se      | 0.2821131389419973                          |
| components.tio-smi.est    | 0.08426875612988116                         |
| components.tio-smi.se     | 0.33027666041848475                         |
| combinations.ics.est      | -0.40607513488112656                        |
| combinations.ics.se       | 0.20407111040966908                         |
| combinations.ics+laba.est | -0.6618398662023607                         |
| combinations.ics+laba.se  | 0.42532016984314147                         |
| combinations.laba.est     | -0.2557647313212341                         |
| combinations.laba.se      | 0.2793538027089195                          |
| combinations.placebo.est  | -0.3145749526274676                         |
| combinations.placebo.se   | 0.2746701484927384                          |
| combinations.tio-hh.est   | -0.3737673120320394                         |
| combinations.tio-hh.se    | 0.2821131389419973                          |
| combinations.tio-smi.est  | 0.08426875612988116                         |
| combinations.tio-smi.se   | 0.33027666041848475                         |
