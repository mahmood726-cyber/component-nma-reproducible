# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                      | value                                                                                                                                                                                  |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| comps                                    | ["aerobic exercise","aquatic exercise","diathermy (high)","diathermy (low)","education","electrical stimulation","placebo","proprioception exercise","strength exercise","ultrasound"] |
| tau2                                     | 0.10738070344728415                                                                                                                                                                    |
| Q                                        | 89.13170728409226                                                                                                                                                                      |
| df                                       | 26                                                                                                                                                                                     |
| components.aerobic exercise.est          | -0.45438648526657466                                                                                                                                                                   |
| components.aerobic exercise.se           | 0.16776472388979843                                                                                                                                                                    |
| components.aquatic exercise.est          | -0.17417885919176224                                                                                                                                                                   |
| components.aquatic exercise.se           | 0.21383164698930818                                                                                                                                                                    |
| components.diathermy (high).est          | 0.1328370933645065                                                                                                                                                                     |
| components.diathermy (high).se           | 0.4831523482071795                                                                                                                                                                     |
| components.diathermy (low).est           | 0.265091749234409                                                                                                                                                                      |
| components.diathermy (low).se            | 0.4828057288884675                                                                                                                                                                     |
| components.education.est                 | -0.2339001239161791                                                                                                                                                                    |
| components.education.se                  | 0.19623913506739338                                                                                                                                                                    |
| components.electrical stimulation.est    | 0.12135969174450151                                                                                                                                                                    |
| components.electrical stimulation.se     | 0.5351853487075706                                                                                                                                                                     |
| components.placebo.est                   | 0.3956438930549447                                                                                                                                                                     |
| components.placebo.se                    | 0.43367982946924477                                                                                                                                                                    |
| components.proprioception exercise.est   | -0.47059840799417396                                                                                                                                                                   |
| components.proprioception exercise.se    | 0.2657405569649561                                                                                                                                                                     |
| components.strength exercise.est         | -0.3126296230143987                                                                                                                                                                    |
| components.strength exercise.se          | 0.1544169315474447                                                                                                                                                                     |
| components.ultrasound.est                | 0.19375193894003828                                                                                                                                                                    |
| components.ultrasound.se                 | 0.523027316369767                                                                                                                                                                      |
| combinations.aerobic exercise.est        | -0.45438648526657466                                                                                                                                                                   |
| combinations.aerobic exercise.se         | 0.16776472388979843                                                                                                                                                                    |
| combinations.aquatic exercise.est        | -0.17417885919176224                                                                                                                                                                   |
| combinations.aquatic exercise.se         | 0.21383164698930818                                                                                                                                                                    |
| combinations.diathermy (high).est        | 0.1328370933645065                                                                                                                                                                     |
| combinations.diathermy (high).se         | 0.4831523482071795                                                                                                                                                                     |
| combinations.diathermy (low).est         | 0.265091749234409                                                                                                                                                                      |
| combinations.diathermy (low).se          | 0.4828057288884675                                                                                                                                                                     |
| combinations.education.est               | -0.2339001239161791                                                                                                                                                                    |
| combinations.education.se                | 0.19623913506739338                                                                                                                                                                    |
| combinations.electrical stimulation.est  | 0.12135969174450151                                                                                                                                                                    |
| combinations.electrical stimulation.se   | 0.5351853487075706                                                                                                                                                                     |
| combinations.placebo.est                 | 0.3956438930549447                                                                                                                                                                     |
| combinations.placebo.se                  | 0.43367982946924477                                                                                                                                                                    |
| combinations.proprioception exercise.est | -0.47059840799417396                                                                                                                                                                   |
| combinations.proprioception exercise.se  | 0.2657405569649561                                                                                                                                                                     |
| combinations.strength exercise.est       | -0.3126296230143987                                                                                                                                                                    |
| combinations.strength exercise.se        | 0.1544169315474447                                                                                                                                                                     |
| combinations.ultrasound.est              | 0.19375193894003828                                                                                                                                                                    |
| combinations.ultrasound.se               | 0.523027316369767                                                                                                                                                                      |
