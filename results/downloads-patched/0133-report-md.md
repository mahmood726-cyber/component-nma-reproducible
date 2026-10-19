# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                               | value                           |
|-----------------------------------|---------------------------------|
| comps                             | ["cq","hcq","standard of care"] |
| tau2                              | 0                               |
| Q                                 | 5.7781400633254485              |
| df                                | 30                              |
| components.cq.est                 | 0.44394033141737865             |
| components.cq.se                  | 0.4221843604727315              |
| components.hcq.est                | -0.10427636180127542            |
| components.hcq.se                 | 0.2377715818786593              |
| components.standard of care.est   | -0.19551143739482257            |
| components.standard of care.se    | 0.24664028260447962             |
| combinations.cq.est               | 0.44394033141737865             |
| combinations.cq.se                | 0.4221843604727315              |
| combinations.hcq.est              | -0.10427636180127542            |
| combinations.hcq.se               | 0.2377715818786593              |
| combinations.standard of care.est | -0.19551143739482257            |
| combinations.standard of care.se  | 0.24664028260447962             |
