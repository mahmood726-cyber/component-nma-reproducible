# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                     | value                                                                         |
|-----------------------------------------|-------------------------------------------------------------------------------|
| comps                                   | ["budesonide","fluticasone","formoterol","placebo","salmeterol","tiotropium"] |
| tau2                                    | 0.002571669585471232                                                          |
| Q                                       | 99.67641278966907                                                             |
| df                                      | 71                                                                            |
| components.budesonide.est               | -0.12291168452791443                                                          |
| components.budesonide.se                | 0.042978255747662154                                                          |
| components.fluticasone.est              | -0.035909553727994356                                                         |
| components.fluticasone.se               | 0.02481794975756358                                                           |
| components.formoterol.est               | -0.022379677673846216                                                         |
| components.formoterol.se                | 0.041731444551750756                                                          |
| components.placebo.est                  | 0.0013963109382071348                                                         |
| components.placebo.se                   | 0.03210632450238746                                                           |
| components.salmeterol.est               | -0.07718834097287873                                                          |
| components.salmeterol.se                | 0.026454208374235517                                                          |
| components.tiotropium.est               | -0.19961859067915189                                                          |
| components.tiotropium.se                | 0.04415941556569004                                                           |
| combinations.budesonide.est             | -0.12291168452791443                                                          |
| combinations.budesonide.se              | 0.042978255747662154                                                          |
| combinations.budesonide+formoterol.est  | -0.14529136220176064                                                          |
| combinations.budesonide+formoterol.se   | 0.0657753007804348                                                            |
| combinations.fluticasone.est            | -0.035909553727994356                                                         |
| combinations.fluticasone.se             | 0.02481794975756358                                                           |
| combinations.fluticasone+salmeterol.est | -0.11309789470087309                                                          |
| combinations.fluticasone+salmeterol.se  | 0.04357938343448002                                                           |
| combinations.formoterol.est             | -0.022379677673846216                                                         |
| combinations.formoterol.se              | 0.041731444551750756                                                          |
| combinations.placebo.est                | 0.0013963109382071348                                                         |
| combinations.placebo.se                 | 0.03210632450238746                                                           |
| combinations.salmeterol.est             | -0.07718834097287873                                                          |
| combinations.salmeterol.se              | 0.026454208374235517                                                          |
| combinations.tiotropium.est             | -0.19961859067915189                                                          |
| combinations.tiotropium.se              | 0.04415941556569004                                                           |
