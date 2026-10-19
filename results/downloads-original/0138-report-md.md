# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                               | value                                     |
|-----------------------------------|-------------------------------------------|
| comps                             | ["cq","hcq","placebo","standard of care"] |
| tau2                              | 0                                         |
| Q                                 | 6.134855254742309                         |
| df                                | 25                                        |
| components.cq.est                 | 0.375                                     |
| components.cq.se                  | NaN                                       |
| components.hcq.est                | -0.125                                    |
| components.hcq.se                 | NaN                                       |
| components.placebo.est            | 0                                         |
| components.placebo.se             | NaN                                       |
| components.standard of care.est   | -0.125                                    |
| components.standard of care.se    | NaN                                       |
| combinations.cq.est               | 0.375                                     |
| combinations.cq.se                | 0                                         |
| combinations.hcq.est              | -0.125                                    |
| combinations.hcq.se               | 0                                         |
| combinations.placebo.est          | 0                                         |
| combinations.placebo.se           | 0                                         |
| combinations.standard of care.est | -0.125                                    |
| combinations.standard of care.se  | 0                                         |
