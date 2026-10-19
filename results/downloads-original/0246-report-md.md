# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                       | value                  |
|---------------------------|------------------------|
| comps                     | ["placebo","warfarin"] |
| tau2                      | 0                      |
| Q                         | 2.029551030130513      |
| df                        | 4                      |
| components.placebo.est    | -0.5672021433545495    |
| components.placebo.se     | 0.6717455505854477     |
| components.warfarin.est   | -1.5356717621944913    |
| components.warfarin.se    | 0.6482046778447613     |
| combinations.placebo.est  | -0.5672021433545495    |
| combinations.placebo.se   | 0.6717455505854477     |
| combinations.warfarin.est | -1.5356717621944913    |
| combinations.warfarin.se  | 0.6482046778447613     |
