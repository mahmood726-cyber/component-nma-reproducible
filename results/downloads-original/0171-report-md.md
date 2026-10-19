# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                 | value                |
|---------------------|----------------------|
| comps               | ["aa","c","p","r"]   |
| tau2                | 0.005993010256846914 |
| Q                   | 20.14268028695339    |
| df                  | 20                   |
| components.aa.est   | 0.7592949390235992   |
| components.aa.se    | 0.9381925171084872   |
| components.c.est    | -0.02758153836074137 |
| components.c.se     | 0.5364659139679987   |
| components.p.est    | 0.2917836376553941   |
| components.p.se     | 0.5719715941832375   |
| components.r.est    | 0.22107894551822904  |
| components.r.se     | 0.8221700280198753   |
| combinations.aa.est | 0.7592949390235992   |
| combinations.aa.se  | 0.9381925171084872   |
| combinations.c.est  | -0.02758153836074137 |
| combinations.c.se   | 0.5364659139679987   |
| combinations.p.est  | 0.2917836376553941   |
| combinations.p.se   | 0.5719715941832375   |
| combinations.r.est  | 0.22107894551822904  |
| combinations.r.se   | 0.8221700280198753   |
