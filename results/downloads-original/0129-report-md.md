# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                | value               |
|--------------------|---------------------|
| comps              | ["b","c","d"]       |
| tau2               | 0.3358993865022123  |
| Q                  | 162.7905654185839   |
| df                 | 25                  |
| components.b.est   | 0.34118587973552356 |
| components.b.se    | 0.2726655843347674  |
| components.c.est   | 0.5809557698561133  |
| components.c.se    | 0.1669637346092239  |
| components.d.est   | 0.6299769724682036  |
| components.d.se    | 0.2950883796599611  |
| combinations.b.est | 0.34118587973552356 |
| combinations.b.se  | 0.2726655843347674  |
| combinations.c.est | 0.5809557698561133  |
| combinations.c.se  | 0.1669637346092239  |
| combinations.d.est | 0.6299769724682036  |
| combinations.d.se  | 0.2950883796599611  |
