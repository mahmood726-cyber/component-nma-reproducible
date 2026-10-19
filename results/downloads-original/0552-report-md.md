# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                                  | value                             |
|--------------------------------------|-----------------------------------|
| comps                                | ["bone grafts","emd","gtr","prp"] |
| tau2                                 | 0.21229161450116613               |
| Q                                    | 134.10855614838994                |
| df                                   | 41                                |
| components.bone grafts.est           | 0.12477097883749802               |
| components.bone grafts.se            | 0.18524074996423873               |
| components.emd.est                   | 0.8270032456111693                |
| components.emd.se                    | 0.15100286850919736               |
| components.gtr.est                   | 0.7856318219485625                |
| components.gtr.se                    | 0.12769439994139098               |
| components.prp.est                   | -0.02000611693645094              |
| components.prp.se                    | 0.26277864851705346               |
| combinations.bone grafts+emd.est     | 0.9517742244486673                |
| combinations.bone grafts+emd.se      | 0.2328771593883338                |
| combinations.bone grafts+emd+prp.est | 0.9317681075122164                |
| combinations.bone grafts+emd+prp.se  | 0.3511187683408971                |
| combinations.bone grafts+gtr.est     | 0.9104028007860605                |
| combinations.bone grafts+gtr.se      | 0.20208592664866815               |
| combinations.bone grafts+gtr+prp.est | 0.8903966838496096                |
| combinations.bone grafts+gtr+prp.se  | 0.33149862724587564               |
| combinations.emd.est                 | 0.8270032456111693                |
| combinations.emd.se                  | 0.15100286850919736               |
| combinations.emd+gtr.est             | 1.6126350675597318                |
| combinations.emd+gtr.se              | 0.22073520654763093               |
| combinations.gtr.est                 | 0.7856318219485625                |
| combinations.gtr.se                  | 0.12769439994139098               |
