# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                               | value                           |
|-----------------------------------|---------------------------------|
| comps                             | ["cq","hcq","standard of care"] |
| tau2                              | 0                               |
| Q                                 | 4.3268499427615925              |
| df                                | 26                              |
| components.cq.est                 | 0.4802234207501988              |
| components.cq.se                  | 0.44401341117312126             |
| components.hcq.est                | -0.1149842009395996             |
| components.hcq.se                 | 0.2412097608121323              |
| components.standard of care.est   | -0.2048458309006369             |
| components.standard of care.se    | 0.25051669158034745             |
| combinations.cq.est               | 0.4802234207501988              |
| combinations.cq.se                | 0.44401341117312126             |
| combinations.hcq.est              | -0.1149842009395996             |
| combinations.hcq.se               | 0.2412097608121323              |
| combinations.standard of care.est | -0.2048458309006369             |
| combinations.standard of care.se  | 0.25051669158034745             |
