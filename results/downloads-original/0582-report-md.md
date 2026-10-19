# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                  | value               |
|----------------------|---------------------|
| comps                | ["a","b"]           |
| tau2                 | 0                   |
| Q                    | 0.13793103448275854 |
| df                   | 1                   |
| components.a.est     | 0.2689655172413792  |
| components.a.se      | 0.12456821978060995 |
| components.b.est     | 0.14482758620689662 |
| components.b.se      | 0.13390681268239724 |
| combinations.a.est   | 0.2689655172413792  |
| combinations.a.se    | 0.12456821978060995 |
| combinations.a+b.est | 0.4137931034482758  |
| combinations.a+b.se  | 0.09284766908852593 |
| combinations.b.est   | 0.14482758620689662 |
| combinations.b.se    | 0.13390681268239724 |
