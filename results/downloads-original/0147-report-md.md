# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                     | value                                                  |
|-----------------------------------------|--------------------------------------------------------|
| comps                                   | ["fluticasone","formoterol","salmeterol","tiotropium"] |
| tau2                                    | 0.005599962454523819                                   |
| Q                                       | 33.92985655938104                                      |
| df                                      | 25                                                     |
| components.fluticasone.est              | -0.08333606363949048                                   |
| components.fluticasone.se               | 0.05359900783973422                                    |
| components.formoterol.est               | -0.08962821026358245                                   |
| components.formoterol.se                | 0.1192469408185914                                     |
| components.salmeterol.est               | -0.17931954002255188                                   |
| components.salmeterol.se                | 0.054687967858437686                                   |
| components.tiotropium.est               | -0.259836144991699                                     |
| components.tiotropium.se                | 0.04534544446316683                                    |
| combinations.fluticasone.est            | -0.08333606363949048                                   |
| combinations.fluticasone.se             | 0.05359900783973422                                    |
| combinations.fluticasone+salmeterol.est | -0.2626556036620423                                    |
| combinations.fluticasone+salmeterol.se  | 0.06473191797344223                                    |
| combinations.formoterol.est             | -0.08962821026358245                                   |
| combinations.formoterol.se              | 0.1192469408185914                                     |
| combinations.salmeterol.est             | -0.17931954002255188                                   |
| combinations.salmeterol.se              | 0.054687967858437686                                   |
| combinations.tiotropium.est             | -0.259836144991699                                     |
| combinations.tiotropium.se              | 0.04534544446316683                                    |
