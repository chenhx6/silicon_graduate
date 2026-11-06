# Rigid-control manuscript package: completed replay

The standalone package is complete at
`raw/writing/gpt/odd-ba-quadrupole-closure/data/revision-v2/rigid-control/`.
Exactly one packaged execution of the unchanged original producer reproduced
the frozen five-point study. All scientific values compared were identical
in this environment.

The manuscript figure entry is the package-root **summary.csv**:

- [Figure CSV](../../../../raw/writing/gpt/odd-ba-quadrupole-closure/data/revision-v2/rigid-control/summary.csv)
- SHA-256: `6ec8ce0c3e9f29d065c2ba8282f2d5727b967acfeedf81dd893439a2fcacad34`
- 5295 bytes; original bytes and filename preserved.
- Twenty prescribed rows, including every undefined-angle outcome.
- Figure generation remains with the parent task.

## Package contents and provenance

The [standalone English README](../../../../raw/writing/gpt/odd-ba-quadrupole-closure/data/revision-v2/rigid-control/README.md)
documents the runnable command, parameter conventions, and model boundaries.
The [portable inventory](../../../../raw/writing/gpt/odd-ba-quadrupole-closure/data/revision-v2/rigid-control/inventory.json)
pins 22 files; including the inventory itself, the package contains 23 files.

Fifteen entries are verbatim copies: eleven original rigid-core sidecar files,
the three frozen modules needed by its producer, and the additional package-root
copy of the figure CSV. Original source paths, byte counts and SHA-256 digests
are recorded per entry. The figure CSV and `frozen/summary.csv` have one source
lineage and are not independent data.

`frozen/run_control.py` is the original scientific producer. The new
`reproduce.py` only checks package integrity, copies runtime files into a new
relative layout, launches the original producer once, and compares results.
It contains no scientific model equations. Its provenance is identified
separately from the original producer and dependencies.

All eighteen files pinned before the execution remain byte-identical.
Afterwards, four replay records were copied into `validation/`.
The pre-execution inventory bytes are preserved in
`validation/inventory-at-replay.json`; the final portable inventory records
those additional validation files. The inventory does not hash itself;
its final hash is recorded in this directory's `inventory.json`.

## One independent execution

The adapter ran from this output directory, using only package-local inputs.
It created a new virtual root at
`tmp/20261106-odd-ba-rigid-package-replay/` and staged exactly five files:
the original protocol, original producer, and three dependencies.
The original relative `outputs/l4/...` and `system/scripts/analysis/...`
layout was recreated there. The producer ran with Python `-I -B` and the
virtual root as its working directory.

No Wiki raw dataset or other scientific data collection is needed by the
adapter or producer. The copied reports contain historical Wiki links, but
these are not runtime inputs. Python and installed NumPy/SciPy are the
external software prerequisites.

The exact replay command was:

```bash
python3 -I -B \
  /workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/data/revision-v2/rigid-control/reproduce.py \
  --output-dir /workspace/wiki/outputs/l4/20261106-odd-ba-manuscript-revision/rigid-package/replay \
  --work-dir /workspace/wiki/tmp/20261106-odd-ba-rigid-package-replay
```

Those paths now contain the completed run. Future executions must use new
output/work directories; the adapter does not overwrite existing directories
or delete the work area.

The process ran from 2026-11-06T10:57:40.886995+00:00 to
2026-11-06T10:57:43.759423+00:00. Actual process time, including Python imports,
was **2.872406496 s**. The original producer reported 2.437326404 s for its
main calculation including output. Both loaded OpenBLAS libraries reported
one thread through runtime introspection. Versions were Python 3.12.3,
NumPy 2.5.4 and SciPy 1.18.1; nothing was installed or reconfigured.

## Comparison result

The [replay receipt](replay/replay-receipt.json) records:

- One producer invocation and exactly the original five C points.
- Five complete q2/q3 comparisons and all twenty proxy/count comparisons.
- 1310 floating values and 521 exact values checked.
- **Maximum absolute numerical difference: 0.0; failures: 0.**
- Byte-identical reference and replayed `summary.csv`.
- Agreement of both CSV tables and the full scientific JSON payload:
  D2/Hermiticity/eigenpair checks, Euler integral, geometric operator identities,
  spectator R0 and core R2 limits, wrong-sign/truncation controls, complex
  rephasing, state gaps and fidelities, static moments and signed cubic sectors.

The declared floating tolerance was `1e-10 + 1e-10*abs(reference)`.
Counts, labels, domain/null states and flags were compared exactly.
Only UTC timestamps, execution times, and platform-specific BLAS-library
metadata were excluded from scientific equality comparison.

The [twenty-row proxy comparison](replay/comparison-proxies.csv),
[execution log](replay/execution.log), and
[complete replayed results](replay/replayed/results.json) remain available.
Copies of the receipt, comparison CSV, execution log and execution inventory
are also included in the standalone package.

This is a packaging/reproducibility result, with no new physical computation
beyond the requested exact replay. The frozen normalization of C, fixed
charge geometry, finite-window closure for initial I=11/2, and absence of a
physical Ba fit remain as documented. The result does not establish unchanged
IBFM geometry.

## Scope and handoff

The new persistent writes are confined to this output directory and the
exclusive `data/revision-v2/rigid-control/` package, with the explicitly
authorized new temporary replay layout retained for inspection.
The original rigid-core artifacts and modules were preserved.
No pre-existing manuscript data files, total manuscript manifest, main.tex,
shared README, shared knowledge, index or handoff were edited.
No figure, new grid, parameter adjustment, configuration change or commit
was made. No `manifest.json` was created.

The existing knowledge result remains
`knowledge/research-notes/fixed-shape-particle-rotor-quadrupole-proxy-control.md`;
this task adds no new scientific claim and performs no shared knowledge write.
The parent task can read the package-root figure CSV and integrate the
standalone package using its own manuscript manifest.
