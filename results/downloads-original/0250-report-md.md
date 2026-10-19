# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                      | value                                                                                                                                                                                  |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| comps                                    | ["choice of product","gum","inhalator","intranasal spray","oral spray","patch","patch and gum","patch and inhalator","patch and lozenge","patch, gum, and lozenge","tablets/lozenges"] |
| tau2                                     | 0.05636324760195601                                                                                                                                                                    |
| Q                                        | 201.94326906173094                                                                                                                                                                     |
| df                                       | 125                                                                                                                                                                                    |
| components.choice of product.est         | 0.4995112145774687                                                                                                                                                                     |
| components.choice of product.se          | 0.1367535013150128                                                                                                                                                                     |
| components.gum.est                       | 0.5095118044653703                                                                                                                                                                     |
| components.gum.se                        | 0.058577434562282406                                                                                                                                                                   |
| components.inhalator.est                 | 0.7615384086802411                                                                                                                                                                     |
| components.inhalator.se                  | 0.23946190786851718                                                                                                                                                                    |
| components.intranasal spray.est          | 0.8494486593947775                                                                                                                                                                     |
| components.intranasal spray.se           | 0.22167348886491067                                                                                                                                                                    |
| components.oral spray.est                | 0.9977174710402479                                                                                                                                                                     |
| components.oral spray.se                 | 0.44769433081652626                                                                                                                                                                    |
| components.patch.est                     | 0.5795293711711518                                                                                                                                                                     |
| components.patch.se                      | 0.060440319589078716                                                                                                                                                                   |
| components.patch and gum.est             | 0.11455555687782858                                                                                                                                                                    |
| components.patch and gum.se              | 0.4725000341158572                                                                                                                                                                     |
| components.patch and inhalator.est       | 0.07738666361542013                                                                                                                                                                    |
| components.patch and inhalator.se        | 0.43850758465063694                                                                                                                                                                    |
| components.patch and lozenge.est         | 0.8661663446915865                                                                                                                                                                     |
| components.patch and lozenge.se          | 0.46294724656875375                                                                                                                                                                    |
| components.patch, gum, and lozenge.est   | 2.7767046058402878                                                                                                                                                                     |
| components.patch, gum, and lozenge.se    | 1.0643521000559417                                                                                                                                                                     |
| components.tablets/lozenges.est          | 0.6083589136731195                                                                                                                                                                     |
| components.tablets/lozenges.se           | 0.13222639179797818                                                                                                                                                                    |
| combinations.choice of product.est       | 0.4995112145774687                                                                                                                                                                     |
| combinations.choice of product.se        | 0.1367535013150128                                                                                                                                                                     |
| combinations.gum.est                     | 0.5095118044653703                                                                                                                                                                     |
| combinations.gum.se                      | 0.058577434562282406                                                                                                                                                                   |
| combinations.inhalator.est               | 0.7615384086802411                                                                                                                                                                     |
| combinations.inhalator.se                | 0.23946190786851718                                                                                                                                                                    |
| combinations.intranasal spray.est        | 0.8494486593947775                                                                                                                                                                     |
| combinations.intranasal spray.se         | 0.22167348886491067                                                                                                                                                                    |
| combinations.oral spray.est              | 0.9977174710402479                                                                                                                                                                     |
| combinations.oral spray.se               | 0.44769433081652626                                                                                                                                                                    |
| combinations.patch.est                   | 0.5795293711711518                                                                                                                                                                     |
| combinations.patch.se                    | 0.060440319589078716                                                                                                                                                                   |
| combinations.patch and gum.est           | 0.11455555687782858                                                                                                                                                                    |
| combinations.patch and gum.se            | 0.4725000341158572                                                                                                                                                                     |
| combinations.patch and inhalator.est     | 0.07738666361542013                                                                                                                                                                    |
| combinations.patch and inhalator.se      | 0.43850758465063694                                                                                                                                                                    |
| combinations.patch and lozenge.est       | 0.8661663446915865                                                                                                                                                                     |
| combinations.patch and lozenge.se        | 0.46294724656875375                                                                                                                                                                    |
| combinations.patch, gum, and lozenge.est | 2.7767046058402878                                                                                                                                                                     |
| combinations.patch, gum, and lozenge.se  | 1.0643521000559417                                                                                                                                                                     |
| combinations.tablets/lozenges.est        | 0.6083589136731195                                                                                                                                                                     |
| combinations.tablets/lozenges.se         | 0.13222639179797818                                                                                                                                                                    |
