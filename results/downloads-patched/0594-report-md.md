# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                | value                  |
|--------------------|------------------------|
| comps              | ["a"]                  |
| tau2               | 0                      |
| Q                  | 1.5415143274875434e-28 |
| df                 | 2000                   |
| components.a.est   | 0.20000000000000004    |
| components.a.se    | 0.00223550917004948    |
| combinations.a.est | 0.20000000000000004    |
| combinations.a.se  | 0.00223550917004948    |
