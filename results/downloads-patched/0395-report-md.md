# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                     | value                                                  |
|-----------------------------------------|--------------------------------------------------------|
| comps                                   | ["fluticasone","formoterol","salmeterol","tiotropium"] |
| tau2                                    | 0.012034889493248381                                   |
| Q                                       | 31.411277959300616                                     |
| df                                      | 25                                                     |
| components.fluticasone.est              | -0.1882703604172415                                    |
| components.fluticasone.se               | 0.0980385070972723                                     |
| components.formoterol.est               | -0.09762135801832957                                   |
| components.formoterol.se                | 0.16280519773457355                                    |
| components.salmeterol.est               | -0.26221789952495406                                   |
| components.salmeterol.se                | 0.08119497158780004                                    |
| components.tiotropium.est               | -0.4234711975322361                                    |
| components.tiotropium.se                | 0.06892906452498906                                    |
| combinations.fluticasone.est            | -0.1882703604172415                                    |
| combinations.fluticasone.se             | 0.0980385070972723                                     |
| combinations.fluticasone+salmeterol.est | -0.45048825994219555                                   |
| combinations.fluticasone+salmeterol.se  | 0.10903723138991968                                    |
| combinations.formoterol.est             | -0.09762135801832957                                   |
| combinations.formoterol.se              | 0.16280519773457355                                    |
| combinations.salmeterol.est             | -0.26221789952495406                                   |
| combinations.salmeterol.se              | 0.08119497158780004                                    |
| combinations.tiotropium.est             | -0.4234711975322361                                    |
| combinations.tiotropium.se              | 0.06892906452498906                                    |
