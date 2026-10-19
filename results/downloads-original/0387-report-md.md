# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                            | value                            |
|--------------------------------|----------------------------------|
| comps                          | ["beta-blocker","sclerotherapy"] |
| tau2                           | 0.9449258581711636               |
| Q                              | 93.15713624152843                |
| df                             | 22                               |
| components.beta-blocker.est    | -0.5680182744568087              |
| components.beta-blocker.se     | 0.44566121879827053              |
| components.sclerotherapy.est   | -0.6576287205803665              |
| components.sclerotherapy.se    | 0.28479024134838915              |
| combinations.beta-blocker.est  | -0.5680182744568087              |
| combinations.beta-blocker.se   | 0.44566121879827053              |
| combinations.sclerotherapy.est | -0.6576287205803665              |
| combinations.sclerotherapy.se  | 0.28479024134838915              |
