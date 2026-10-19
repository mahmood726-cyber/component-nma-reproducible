# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                               | value                             |
|-----------------------------------|-----------------------------------|
| comps                             | ["chlorpheniramine","doxylamine"] |
| tau2                              | 0.18709774755647254               |
| Q                                 | 10.32449913786175                 |
| df                                | 7                                 |
| components.chlorpheniramine.est   | 0.39280203489105847               |
| components.chlorpheniramine.se    | 0.3824630130261195                |
| components.doxylamine.est         | 0.8006028644875244                |
| components.doxylamine.se          | 0.33661818498519475               |
| combinations.chlorpheniramine.est | 0.39280203489105847               |
| combinations.chlorpheniramine.se  | 0.3824630130261195                |
| combinations.doxylamine.est       | 0.8006028644875244                |
| combinations.doxylamine.se        | 0.33661818498519475               |
