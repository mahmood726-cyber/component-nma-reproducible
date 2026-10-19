# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                | value                |
|--------------------|----------------------|
| comps              | ["2","3"]            |
| tau2               | 0.006191557158166111 |
| Q                  | 11.622340193194105   |
| df                 | 10                   |
| components.2.est   | -0.01319631080496221 |
| components.2.se    | 0.06522958296913209  |
| components.3.est   | 0.040716325184813815 |
| components.3.se    | 0.6219126273438915   |
| combinations.2.est | -0.01319631080496221 |
| combinations.2.se  | 0.06522958296913209  |
| combinations.3.est | 0.040716325184813815 |
| combinations.3.se  | 0.6219126273438915   |
