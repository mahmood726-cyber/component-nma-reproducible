# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                               | value                             |
|-----------------------------------|-----------------------------------|
| comps                             | ["chlorpheniramine","doxylamine"] |
| tau2                              | 0.027169530108014556              |
| Q                                 | 11.10305394450442                 |
| df                                | 7                                 |
| components.chlorpheniramine.est   | 0.17666177241180214               |
| components.chlorpheniramine.se    | 0.12801678125128807               |
| components.doxylamine.est         | 0.2509545915080707                |
| components.doxylamine.se          | 0.13961496704716067               |
| combinations.chlorpheniramine.est | 0.17666177241180214               |
| combinations.chlorpheniramine.se  | 0.12801678125128807               |
| combinations.doxylamine.est       | 0.2509545915080707                |
| combinations.doxylamine.se        | 0.13961496704716067               |
