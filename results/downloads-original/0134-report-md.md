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
| Q                                 | 6.406634794465061                         |
| df                                | 25                                        |
| components.cq.est                 | 0.25                                      |
| components.cq.se                  | 8967799.16798601                          |
| components.hcq.est                | -0.5                                      |
| components.hcq.se                 | 8967799.167985993                         |
| components.placebo.est            | -0.25                                     |
| components.placebo.se             | 8967799.167985998                         |
| components.standard of care.est   | -0.5                                      |
| components.standard of care.se    | 8967799.167985994                         |
| combinations.cq.est               | 0.25                                      |
| combinations.cq.se                | 8967799.16798601                          |
| combinations.hcq.est              | -0.5                                      |
| combinations.hcq.se               | 8967799.167985993                         |
| combinations.placebo.est          | -0.25                                     |
| combinations.placebo.se           | 8967799.167985998                         |
| combinations.standard of care.est | -0.5                                      |
| combinations.standard of care.se  | 8967799.167985994                         |
