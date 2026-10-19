# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                | value                |
|--------------------|----------------------|
| comps              | ["1","2","3"]        |
| tau2               | 0.014074252162799247 |
| Q                  | 11.6388302094275     |
| df                 | 9                    |
| components.1.est   | 0.0439453125         |
| components.1.se    | 7908855.468687605    |
| components.2.est   | 0.044921875          |
| components.2.se    | 7908855.468687606    |
| components.3.est   | 0.0966796875         |
| components.3.se    | 7908855.468687629    |
| combinations.1.est | 0.0439453125         |
| combinations.1.se  | 7908855.468687605    |
| combinations.2.est | 0.044921875          |
| combinations.2.se  | 7908855.468687606    |
| combinations.3.est | 0.0966796875         |
| combinations.3.se  | 7908855.468687629    |
