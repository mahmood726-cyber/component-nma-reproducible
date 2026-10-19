# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                | value               |
|--------------------|---------------------|
| comps              | ["a"]               |
| tau2               | 0                   |
| Q                  | 0.5000000000000002  |
| df                 | 1                   |
| components.a.est   | 0.3500000000000001  |
| components.a.se    | 0.07071067811865477 |
| combinations.a.est | 0.3500000000000001  |
| combinations.a.se  | 0.07071067811865477 |
