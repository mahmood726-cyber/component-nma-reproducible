# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                            |
|--------------------------------|----------------------------------|
| comps                          | ["beta-blocker","sclerotherapy"] |
| tau2                           | 0.3941279787314937               |
| Q                              | 77.66064153722758                |
| df                             | 22                               |
| components.beta-blocker.est    | -0.4450472571069516              |
| components.beta-blocker.se     | 0.31424640065383713              |
| components.sclerotherapy.est   | -0.42325094522672163             |
| components.sclerotherapy.se    | 0.1920310458113017               |
| combinations.beta-blocker.est  | -0.4450472571069516              |
| combinations.beta-blocker.se   | 0.31424640065383713              |
| combinations.sclerotherapy.est | -0.42325094522672163             |
| combinations.sclerotherapy.se  | 0.1920310458113017               |
