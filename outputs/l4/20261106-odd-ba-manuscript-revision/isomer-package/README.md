# Standalone isomer package: completed numerical check

The independent bundle is `raw/writing/gpt/odd-ba-quadrupole-closure/data/revision-v2/isomer-check/`.
Its original producers each ran once from `standalone-copy/package/`;
the full generated layouts and logs are retained in `standalone-copy/run-01/`.
The numerical comparison passed: four energy mappings, 28 strengths, 14
width sums and all 84 branches agree exactly with the frozen references.
All 1865 compared floating fields have zero difference.
Both CSV files and the eigenvector-basis hash also agree exactly.

The runnable entry point is `reproduce.py`; from a copy of the bundle, run:

```bash
python3 -B reproduce.py --output /absolute/path/to/a-new-isomer-run
```

The output must be new and outside the package. The tested environment is
Python 3.12.3, NumPy 2.5.4 and SciPy 1.18.1. The bundle's English README
documents the frozen inputs, the two-layout design, scientific limits and
standalone use. No new fit, operator, source search or scientific input was
introduced. The original positive-eB normalization to frozen Bup=0.407
is retained in both original producers.

For manuscript integration, the recorded energy-nearest alternative remains
19/2_1 to 15/2_2, chosen by the two anchored level energies before E2
evaluation. The primary pair retains B=22.46884935273523 W.u. and a
1173.6101707745688-keV model photon energy. The energy-nearest primary-
operator branch retains 2.1776211421936043 W.u. and 48.32504893857603 keV.
The conditional Q136=+0.07 root gives 0.42002440210282804 W.u. on that
alternative branch. These are preserved model results, not a state
assignment or validation of the decay network. All 14 summed model-scheme
upper half-life bounds remain at or below 0.0002810411363297495 ns.

`source-declarations.json` distinguishes 16 exact copied originals from 101
embedded historical source/hash/locator declarations. All six original
protocol dependencies are real staged files with matching hashes. The
width protocol's frozen historical `results.json` prerequisite is provided
as an actual file in a separate width layout; no hash checker is replaced.
Unbundled PDFs, ENSDF files, publisher crops and prior source-audit events
are not reverified. The replay is not certification of source-author code,
the original electromagnetic figures, physical state assignments or paper
readiness.

Both deliberate forbidden-read probes were blocked; no unexpected denied
access or network/nested-process attempt occurred. Allowed scientific-file
events stayed in the staged trees. The logs are Python audit events, including
failed cache-read attempts, not an exhaustive OS/native trace.

The original 45 data-manifest files, shared data manifest and frozen benchmark
files match the preservation baseline. A concurrent change to shared
`main.tex` was observed by hash; this task neither wrote nor reverted it.
See `preservation-check.json` for the exact snapshot. All task writes are
within the two assigned directories, and no commit was made.

`package-review.json` reports numerical checks and payload hashes.
`archive-gate.json` and `receipt.json` record final archive verification.
The package carries its own `inventory.json`, `verification/inventory.json`,
`verification/receipt.json` and repository-relative `manifest.json`; the
shared manuscript manifest has not been edited.
