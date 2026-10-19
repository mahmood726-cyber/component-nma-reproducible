# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                               | value                             |
|-----------------------------------|-----------------------------------|
| comps                             | ["chlorpheniramine","doxylamine"] |
| tau2                              | 0.0014942171074729539             |
| Q                                 | 6.282432102127103                 |
| df                                | 6                                 |
| components.chlorpheniramine.est   | -0.012890335991610255             |
| components.chlorpheniramine.se    | 0.08093794631105083               |
| components.doxylamine.est         | 0.14912361315430028               |
| components.doxylamine.se          | 0.06845775242686697               |
| combinations.chlorpheniramine.est | -0.012890335991610255             |
| combinations.chlorpheniramine.se  | 0.08093794631105083               |
| combinations.doxylamine.est       | 0.14912361315430028               |
| combinations.doxylamine.se        | 0.06845775242686697               |
