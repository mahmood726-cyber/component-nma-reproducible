# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                | value                                                                                                        |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| comps                              | ["choice of product","gum","inhalator","intranasal spray","lozenge","oral spray","patch","tablets/lozenges"] |
| tau2                               | 0.042104503210554346                                                                                         |
| Q                                  | 207.16301829702738                                                                                           |
| df                                 | 123                                                                                                          |
| components.choice of product.est   | 0.40141375984667066                                                                                          |
| components.choice of product.se    | 0.11670809193210592                                                                                          |
| components.gum.est                 | 0.3806888589788214                                                                                           |
| components.gum.se                  | 0.04797352503152019                                                                                          |
| components.inhalator.est           | 0.40371971660658684                                                                                          |
| components.inhalator.se            | 0.18218809381620943                                                                                          |
| components.intranasal spray.est    | 0.6927517074810352                                                                                           |
| components.intranasal spray.se     | 0.1870216860659837                                                                                           |
| components.lozenge.est             | 1.87862781197926                                                                                             |
| components.lozenge.se              | 1.050821348878816                                                                                            |
| components.oral spray.est          | 0.9063180387863278                                                                                           |
| components.oral spray.se           | 0.40815077218677936                                                                                          |
| components.patch.est               | 0.44873353014412865                                                                                          |
| components.patch.se                | 0.05185379003160291                                                                                          |
| components.tablets/lozenges.est    | 0.5135031815142425                                                                                           |
| components.tablets/lozenges.se     | 0.11865714258698148                                                                                          |
| combinations.choice of product.est | 0.40141375984667066                                                                                          |
| combinations.choice of product.se  | 0.11670809193210592                                                                                          |
| combinations.gum.est               | 0.3806888589788214                                                                                           |
| combinations.gum.se                | 0.04797352503152019                                                                                          |
| combinations.gum+lozenge+patch.est | 2.7080502011022105                                                                                           |
| combinations.gum+lozenge+patch.se  | 1.0484928266865108                                                                                           |
| combinations.gum+patch.est         | 0.82942238912295                                                                                             |
| combinations.gum+patch.se          | 0.06991637609619585                                                                                          |
| combinations.inhalator.est         | 0.40371971660658684                                                                                          |
| combinations.inhalator.se          | 0.18218809381620943                                                                                          |
| combinations.inhalator+patch.est   | 0.8524532467507155                                                                                           |
| combinations.inhalator+patch.se    | 0.18609658279677066                                                                                          |
| combinations.intranasal spray.est  | 0.6927517074810352                                                                                           |
| combinations.intranasal spray.se   | 0.1870216860659837                                                                                           |
| combinations.oral spray.est        | 0.9063180387863278                                                                                           |
| combinations.oral spray.se         | 0.40815077218677936                                                                                          |
| combinations.patch.est             | 0.44873353014412865                                                                                          |
| combinations.patch.se              | 0.05185379003160291                                                                                          |
| combinations.tablets/lozenges.est  | 0.5135031815142425                                                                                           |
| combinations.tablets/lozenges.se   | 0.11865714258698148                                                                                          |
