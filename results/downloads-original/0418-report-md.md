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
| Q                         | 52.66319538799181                           |
| df                        | 77                                          |
| components.ics.est        | -0.11549257227768943                        |
| components.ics.se         | 0.05868547887552053                         |
| components.laba.est       | -0.22969234178672826                        |
| components.laba.se        | 0.05913353181093844                         |
| components.placebo.est    | -0.1430754089591634                         |
| components.placebo.se     | 0.07984771248289613                         |
| components.tio-hh.est     | -0.22210624447249516                        |
| components.tio-hh.se      | 0.09517656107254817                         |
| components.tio-smi.est    | 0.2557682997981854                          |
| components.tio-smi.se     | 0.20003659448439776                         |
| combinations.ics.est      | -0.11549257227768943                        |
| combinations.ics.se       | 0.05868547887552053                         |
| combinations.ics+laba.est | -0.3451849140644177                         |
| combinations.ics+laba.se  | 0.10262806023422319                         |
| combinations.laba.est     | -0.22969234178672826                        |
| combinations.laba.se      | 0.05913353181093844                         |
| combinations.placebo.est  | -0.1430754089591634                         |
| combinations.placebo.se   | 0.07984771248289613                         |
| combinations.tio-hh.est   | -0.22210624447249516                        |
| combinations.tio-hh.se    | 0.09517656107254817                         |
| combinations.tio-smi.est  | 0.2557682997981854                          |
| combinations.tio-smi.se   | 0.20003659448439776                         |
