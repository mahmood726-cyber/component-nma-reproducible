# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                               | value                             |
|-----------------------------------|-----------------------------------|
| comps                             | ["chlorpheniramine","doxylamine"] |
| tau2                              | 0                                 |
| Q                                 | 4.687518776659753                 |
| df                                | 7                                 |
| components.chlorpheniramine.est   | 0.34819604705108476               |
| components.chlorpheniramine.se    | 0.09918345990488063               |
| components.doxylamine.est         | 0.1889658887770965                |
| components.doxylamine.se          | 0.08234910497233895               |
| combinations.chlorpheniramine.est | 0.34819604705108476               |
| combinations.chlorpheniramine.se  | 0.09918345990488063               |
| combinations.doxylamine.est       | 0.1889658887770965                |
| combinations.doxylamine.se        | 0.08234910497233895               |
