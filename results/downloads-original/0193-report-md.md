# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                               | value                             |
|-----------------------------------|-----------------------------------|
| comps                             | ["chlorpheniramine","doxylamine"] |
| tau2                              | 0.03527644944394622               |
| Q                                 | 10.225713681876208                |
| df                                | 6                                 |
| components.chlorpheniramine.est   | 0.22599910904151552               |
| components.chlorpheniramine.se    | 0.16029386416333397               |
| components.doxylamine.est         | 0.2142880051758703                |
| components.doxylamine.se          | 0.13814324038901332               |
| combinations.chlorpheniramine.est | 0.22599910904151552               |
| combinations.chlorpheniramine.se  | 0.16029386416333397               |
| combinations.doxylamine.est       | 0.2142880051758703                |
| combinations.doxylamine.se        | 0.13814324038901332               |
