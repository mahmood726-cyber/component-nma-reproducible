# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The random-effects model uses a generalized DerSimonian–Laird estimator and normal 95% confidence intervals. It estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                  | value                                       |
|--------------------------------------|---------------------------------------------|
| comps                                | ["bone grafts","emd","flap op","gtr","prp"] |
| tau2                                 | 0.21435321392669499                         |
| Q                                    | 132.18924162990268                          |
| df                                   | 40                                          |
| components.bone grafts.est           | 0.10990295008502089                         |
| components.bone grafts.se            | 0.18624070414106084                         |
| components.emd.est                   | 0.3044401480508183                          |
| components.emd.se                    | 0.4566414272642243                          |
| components.flap op.est               | -0.5374734719201566                         |
| components.flap op.se                | 0.44281064340652515                         |
| components.gtr.est                   | 0.29814250435335765                         |
| components.gtr.se                    | 0.42190231319169147                         |
| components.prp.est                   | -0.01996256174197562                        |
| components.prp.se                    | 0.2635689987710025                          |
| combinations.bone grafts+emd.est     | 0.4143430981358392                          |
| combinations.bone grafts+emd.se      | 0.5008538876880183                          |
| combinations.bone grafts+emd+prp.est | 0.39438053639386356                         |
| combinations.bone grafts+emd+prp.se  | 0.565971053964203                           |
| combinations.bone grafts+gtr.est     | 0.40804545443837853                         |
| combinations.bone grafts+gtr.se      | 0.4611801836109812                          |
| combinations.bone grafts+gtr+prp.est | 0.3880828926964029                          |
| combinations.bone grafts+gtr+prp.se  | 0.5311833759339679                          |
| combinations.emd.est                 | 0.3044401480508183                          |
| combinations.emd.se                  | 0.4566414272642243                          |
| combinations.emd+gtr.est             | 0.602582652404176                           |
| combinations.emd+gtr.se              | 0.8616995292579708                          |
| combinations.flap op.est             | -0.5374734719201566                         |
| combinations.flap op.se              | 0.44281064340652515                         |
| combinations.gtr.est                 | 0.29814250435335765                         |
| combinations.gtr.se                  | 0.42190231319169147                         |
