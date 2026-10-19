# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                | value               |
|--------------------|---------------------|
| comps              | ["b","c","d"]       |
| tau2               | 0.3692284894328466  |
| Q                  | 151.4492095836472   |
| df                 | 19                  |
| components.b.est   | 0.36405622527411086 |
| components.b.se    | 0.3203699695129733  |
| components.c.est   | 0.5780628770750555  |
| components.c.se    | 0.18493564971135834 |
| components.d.est   | 1.0836144992634944  |
| components.d.se    | 0.4489049779848266  |
| combinations.b.est | 0.36405622527411086 |
| combinations.b.se  | 0.3203699695129733  |
| combinations.c.est | 0.5780628770750555  |
| combinations.c.se  | 0.18493564971135834 |
| combinations.d.est | 1.0836144992634944  |
| combinations.d.se  | 0.4489049779848266  |
