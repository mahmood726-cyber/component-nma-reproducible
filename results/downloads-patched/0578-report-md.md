# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                  | value              |
|----------------------|--------------------|
| comps                | ["a","b"]          |
| tau2                 | 7.158660219603102  |
| Q                    | 633.7830640866324  |
| df                   | 3                  |
| components.a.est     | 0.9931858230468759 |
| components.a.se      | 1.5491260942829301 |
| components.b.est     | 0.3720201065677137 |
| components.b.se      | 1.342793186106681  |
| combinations.a.est   | 0.9931858230468759 |
| combinations.a.se    | 1.5491260942829301 |
| combinations.a+b.est | 1.3652059296145895 |
| combinations.a+b.se  | 2.052829070088502  |
| combinations.b.est   | 0.3720201065677137 |
| combinations.b.se    | 1.342793186106681  |
