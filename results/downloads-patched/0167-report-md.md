# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                 | value                |
|---------------------|----------------------|
| comps               | ["aa","c","p","r"]   |
| tau2                | 0                    |
| Q                   | 16.90657559229479    |
| df                  | 18                   |
| components.aa.est   | 0.7751292918155852   |
| components.aa.se    | 0.5414459191307549   |
| components.c.est    | 0.05459271235713814  |
| components.c.se     | 0.3300616647018508   |
| components.p.est    | 0.1790601164026846   |
| components.p.se     | 0.35350632942870835  |
| components.r.est    | -0.22286973462113724 |
| components.r.se     | 0.47432240639547124  |
| combinations.aa.est | 0.7751292918155852   |
| combinations.aa.se  | 0.5414459191307549   |
| combinations.c.est  | 0.05459271235713814  |
| combinations.c.se   | 0.3300616647018508   |
| combinations.p.est  | 0.1790601164026846   |
| combinations.p.se   | 0.35350632942870835  |
| combinations.r.est  | -0.22286973462113724 |
| combinations.r.se   | 0.47432240639547124  |
