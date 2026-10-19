# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                | value               |
|--------------------|---------------------|
| comps              | ["b","c","d"]       |
| tau2               | 0.6394971545226695  |
| Q                  | 193.73023886898315  |
| df                 | 19                  |
| components.b.est   | 0.4385445895520005  |
| components.b.se    | 0.41322499030699794 |
| components.c.est   | 0.736127367132533   |
| components.c.se    | 0.23547189069418165 |
| components.d.est   | 1.3793531699403467  |
| components.d.se    | 0.5635749038391109  |
| combinations.b.est | 0.4385445895520005  |
| combinations.b.se  | 0.41322499030699794 |
| combinations.c.est | 0.736127367132533   |
| combinations.c.se  | 0.23547189069418165 |
| combinations.d.est | 1.3793531699403467  |
| combinations.d.se  | 0.5635749038391109  |
