# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                     | value                                                            |
|-----------------------------------------|------------------------------------------------------------------|
| comps                                   | ["fluticasone","formoterol","placebo","salmeterol","tiotropium"] |
| tau2                                    | 0.014710521512016383                                             |
| Q                                       | 31.306277647823382                                               |
| df                                      | 24                                                               |
| components.fluticasone.est              | -0.20894598238905915                                             |
| components.fluticasone.se               | 0.12844716650247806                                              |
| components.formoterol.est               | -0.13629782407386148                                             |
| components.formoterol.se                | 0.2685193591685053                                               |
| components.placebo.est                  | -0.04358006032317441                                             |
| components.placebo.se                   | 0.20984462790242844                                              |
| components.salmeterol.est               | -0.3057263009364841                                              |
| components.salmeterol.se                | 0.20999468255185363                                              |
| components.tiotropium.est               | -0.4741210895407133                                              |
| components.tiotropium.se                | 0.23072244720594937                                              |
| combinations.fluticasone.est            | -0.20894598238905915                                             |
| combinations.fluticasone.se             | 0.12844716650247806                                              |
| combinations.fluticasone+salmeterol.est | -0.5146722833255433                                              |
| combinations.fluticasone+salmeterol.se  | 0.29398861001217413                                              |
| combinations.formoterol.est             | -0.13629782407386148                                             |
| combinations.formoterol.se              | 0.2685193591685053                                               |
| combinations.placebo.est                | -0.04358006032317441                                             |
| combinations.placebo.se                 | 0.20984462790242844                                              |
| combinations.salmeterol.est             | -0.3057263009364841                                              |
| combinations.salmeterol.se              | 0.20999468255185363                                              |
| combinations.tiotropium.est             | -0.4741210895407133                                              |
| combinations.tiotropium.se              | 0.23072244720594937                                              |
