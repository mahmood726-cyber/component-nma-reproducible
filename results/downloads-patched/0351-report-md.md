# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                             |
|--------------------------------|-----------------------------------|
| comps                          | ["beta-blockers","sclerotherapy"] |
| tau2                           | 0.3941279787314935                |
| Q                              | 77.66064153722753                 |
| df                             | 22                                |
| components.beta-blockers.est   | -0.4450472571069517               |
| components.beta-blockers.se    | 0.3142464006538371                |
| components.sclerotherapy.est   | -0.42325094522672163              |
| components.sclerotherapy.se    | 0.19203104581130168               |
| combinations.beta-blockers.est | -0.4450472571069517               |
| combinations.beta-blockers.se  | 0.3142464006538371                |
| combinations.sclerotherapy.est | -0.42325094522672163              |
| combinations.sclerotherapy.se  | 0.19203104581130168               |
