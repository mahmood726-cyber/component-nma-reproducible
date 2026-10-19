# P19 component NMA validation

Start with [RESULTS.md](RESULTS.md). Statistical scope and explicit evidence
limits are in [AUDIT_SCOPE.md](AUDIT_SCOPE.md). The source checkout was not
modified; [fix.patch](fix.patch) applies only to the copied app and its README.

The archive contains original/patched source, offline Node dependencies and
licenses, the serialized corpus, installed R help/source snapshots, dataset and
configuration ledgers, actual page captures and downloads, reference values,
per-check results, native-study diagnostics, and reproduction scripts.

## Reproduce

Use Python 3, Node 24, and the offline R 4.6 installation with netmeta 3.7.0.
Set `RSCRIPT`, `AUDIT_R_LIBS_USER`, and `AUDIT_R_LIBS` if the wrapper cannot find
the supplied R installation/libraries. `R_ENVIRON_USER=NUL` is set by the wrapper.
No packages are installed or downloaded. Run only one R command at a time.

```text
python run_r.py inventory.R
python run_r.py corpus.R
python configure.py
python focused.py
python bus_cases.py
python make_patch.py
node run_node.cjs original
node run_node.cjs patched
python run_r.py reference.R
python run_r.py bus_reference.R
python run_r.py metadata.R
python run_r.py bridge_disconnected.R
python compare.py original
python compare.py patched
python bridge.py
python compare_bus.py
python test_static.py
python report.py
python verify_archive.py
python archive.py
```

`reference.R` reuses existing reference results by configuration key. For a full
fresh reference run, rename the supplied `reference.json` before running it.
`wrapper_reference.R` preserves the slower original wrapper approach; the
initial completed checkpoint is `wrapper-reference.json`. Do not run it at the
same time as another R process. The direct installed-engine results are bridged
against those wrapper values, not against a JavaScript reimplementation.

`setup.py` and `vendor_node.py` record initial source/dependency collection from
the supplied workspace. They are unnecessary when reproducing from this archive,
which already contains those files. Archive verification checks hashes, source
integrity, unique keys and coverage, export files, and an actual patch replay.

The numerical pass count applies to the declared independent-row model.
Native multi-arm diagnostic differences, source dependence, and unverified
browser layout/chart-download behavior are reported separately in RESULTS.md.

Packaging portability: the unused upstream `cnma-oracle.R` fixture has repository-relative paths in both source snapshots. `source-manifest.json` retains upstream hashes and records the normalized snapshot hash separately. The checkout, executed page code, statistical evidence, and app-only patch are unaffected. Run `python portable_snapshot.py` before `python verify_archive.py` and `python archive.py` when rebuilding the archive.
