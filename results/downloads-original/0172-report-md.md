# Component NMA

_Generated 2026-10-19 with allmeta — browser-only evidence synthesis (https://github.com/)._

## Methods

Additive model for multi-component interventions (Welton et al., Am J Epidemiol 2009). Each intervention is a set of components (e.g., "drug + exercise + education"). The model estimates one effect per component; any combination's effect is the sum of its components.

Welton NJ, Caldwell DM, Adamopoulos E, Vedhara K. Mixed treatment comparison meta-analysis of complex interventions: psychological interventions in coronary heart disease. Am J Epidemiol 2009;169:1158-1165. R-parity: the additive engine matches netmeta::discomb(inactive="control") to 1e-4 on component effects + SE and the additive Q decomposition (hub/shared/tests/component-nma-parity.spec.mjs).

## Results

| key                 | value                |
|---------------------|----------------------|
| comps               | ["aa","c","r","ut"]  |
| tau2                | 0                    |
| Q                   | 19.43120159478877    |
| df                  | 20                   |
| components.aa.est   | 0.40711669720439825  |
| components.aa.se    | 0.7351544188706414   |
| components.c.est    | -0.285630319536534   |
| components.c.se     | 0.177568456561137    |
| components.r.est    | -0.06763873898668803 |
| components.r.se     | 0.5676176357941461   |
| components.ut.est   | -0.2544069768417326  |
| components.ut.se    | 0.5242256660416873   |
| combinations.aa.est | 0.40711669720439825  |
| combinations.aa.se  | 0.7351544188706414   |
| combinations.c.est  | -0.285630319536534   |
| combinations.c.se   | 0.177568456561137    |
| combinations.r.est  | -0.06763873898668803 |
| combinations.r.se   | 0.5676176357941461   |
| combinations.ut.est | -0.2544069768417326  |
| combinations.ut.se  | 0.5242256660416873   |
