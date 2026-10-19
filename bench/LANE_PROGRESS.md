# P19 progress

Validation complete; archive generation and verification is the final operation.

- Checkout unchanged: acd363fa33f0decd2fcafcf08814f663bb9d6178. No commit or push.
- 639 catalogue entries; 54 included datasets; 576 configurations plus 19 focused cases.
- R reference: 595 cases, 330 numerical fits, 265 support refusals, zero errors.
- Original: 88736/91238 checks pass. Patched: 72148/72150. Remaining failures are signed-zero strings versus R; numerical and display/export comparisons pass.
- Public-wrapper bridge: 2064/2064 across 45 cases. Bus: 49/63 original, 63/63 patched. Shipped static assertions: 14/14.
- Native multi-arm and split-mouth limitations are explicitly reported. No browser layout or raster/PDF export validation is claimed.
- App-only fix.patch preserves source line endings. Exact replay and artifact integrity: 88/88 checks pass (verification.json).
- RESULTS.md, results.json, ledgers, documentation, captures, exports and offline Node dependencies are final.
- archive.py writes P19-validation.zip and archive-manifest.json, verifies every entry and CRC, and writes archive-verification.json alongside the ZIP. Check that file for final archive status and SHA-256.
