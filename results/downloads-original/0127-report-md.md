# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                | value               |
|--------------------|---------------------|
| comps              | ["b","c","d"]       |
| tau2               | 0.6314741947327951  |
| Q                  | 192.15575582332343  |
| df                 | 19                  |
| components.b.est   | 0.43564439215054285 |
| components.b.se    | 0.41105192838551385 |
| components.c.est   | 0.7428891383989824  |
| components.c.se    | 0.23423703671265272 |
| components.d.est   | 1.381586774054892   |
| components.d.se    | 0.5611663414902311  |
| combinations.b.est | 0.43564439215054285 |
| combinations.b.se  | 0.41105192838551385 |
| combinations.c.est | 0.7428891383989824  |
| combinations.c.se  | 0.23423703671265272 |
| combinations.d.est | 1.381586774054892   |
| combinations.d.se  | 0.5611663414902311  |
