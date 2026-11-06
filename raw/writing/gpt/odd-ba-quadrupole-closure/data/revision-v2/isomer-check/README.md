# Standalone 137Ba isomer check

This self-contained numerical package reproduces the frozen 137Ba isomer
comparison and its conditional E2-radiative width addendum. It contains the
original protocols, energy-first four-pair mapping, 28 strengths, 14 width
sums, 84 branches, unchanged original producers, required numerical modules,
and the exact JSON snapshots required by the original hash checks.

No parameter, operator root or state ordinal is fitted or selected in this
replay. No original Wiki checkout, PDF, ENSDF file, source page, network
connection or original authors' code is required. NumPy, SciPy and Python
remain ordinary external runtime dependencies; they are not bundled.

With the dependencies installed, copy this entire directory anywhere and run:

```bash
python3 -B reproduce.py --output /absolute/path/to/a-new-isomer-run
```

The output directory must not exist and must be outside the package directory.
The tested environment is Python 3.12.3, NumPy 2.5.4 and SciPy 1.18.1; the
Python packages are recorded in `requirements.txt`. This package installs
nothing and does not change interpreter or BLAS configuration globally.
Child processes set their own BLAS thread limits to one.

The energy diagnostic compares the two level energies relative to the lowest
11/2 anchor, using equal-weight squared residuals. It does not minimize the
photon-energy residual alone and does not use B(E2) to choose a pair. Ordinal
integers in the JSON are zero-based; the `..._1_...` pair labels are one-based.
All four strength pairs are retained even if a model photon energy is
negative. Width sums include only energetically open model E2 routes.

## Contents

- `frozen/`: byte-identical research protocols, reference mapping and JSON/CSV
  results.
- `producers/`: unchanged `run_benchmark.py` and `run_decay_widths.py`.
- `code/`: the unchanged numerical modules and their existing MIT license.
- `inputs/`: exact frozen numerical/provenance JSON snapshots.
- `layout.json`: package-to-temporary-layout mapping, all relative.
- `inventory.json`: hashes and sizes of immutable replay payload files,
  including the adapter and documentation; it does not include itself or
  subsequently added verification receipts.
- `source-declarations.json`: raw-source and embedded historical hash
  declarations, explicitly distinguished from actual payload verification.
- `comparison-policy.json`: tolerances fixed before the reproduction.
- `verification/`: the completed standalone check, its reproduced products,
  comparison, read-boundary records and a separate verification inventory.

## Why two layouts are used

The original producers resolve their root from their directory depth. The
adapter builds that relative layout twice and executes each original producer
once. It does not edit either protocol or replace any `sha` function.

The strength job writes a fresh mapping and result. Their new timestamps mean
that their file hashes generally differ from the historical ones even when
all scientific values agree.

The width protocol explicitly hashes the ORIGINAL strength result. The
separate width layout therefore includes that packaged frozen `results.json`
as its real, byte-verified provenance prerequisite. The width producer
recomputes the model E2 rates from the fixed parameters and operator roots.
It does not substitute the reference rates for its calculation. The newly
computed strength result is compared independently with the reference in the
strength job.

All six paths in the base protocol's `input_sha256` map are physically present
in each temporary root. All original file-hash assertions run against those
actual copies. There are no missing-file placeholders or fabricated
verification successes.

## What is, and is not, verified

Three layers must remain separate:

1. **Packaged frozen numerical inputs and reference results.** Their exact
   bytes, sizes and hashes are checked against `inventory.json`. The original
   protocols additionally hash the staged input files during each calculation.
   The linear-calibration JSON supplies five already-frozen operator roots;
   this replay does not rederive or refit those roots. The original producers
   retain their positive-eB normalization to the same frozen core
   B(E2; 0 to 2) = 0.407 e²b² for each operator.
2. **Historical source declarations inside the JSON snapshots.** These
   include original raw/PDF/ENSDF paths, prior run hashes, cited measurements
   and recorded source-audit conclusions. The snapshots are preserved
   verbatim. Hashing the snapshot does not reverify the external source or the
   historical event it describes.
3. **Actual verification performed by this replay.** The receipt records
   payload verification, the original producer checks, all compared scientific
   fields, 28 strengths, 14 sums, 84 branches, the energy-only mapping and both
   CSV tables. It claims no fresh hash validation of unbundled raw sources.

Publisher full texts and source-page reproductions are absent. Embedded
published numerical records and provenance are retained in the frozen JSON
inputs. See `source-declarations.json` for explicit not-packaged/not-reverified
entries. Historical verification flags in those snapshots describe the prior
record, not a new verification made by this package.

## Read boundary and comparison

Each producer runs under Python isolated mode (`-I -B`). The worker allows
scientific-file reads only from the copied package and generated run tree;
Python/runtime libraries remain accessible. A deliberately forbidden
file-read probe must be blocked. Network and nested subprocess attempts are
denied, and successful file accesses and unexpected denials are recorded.
This is a Python-level audit boundary, not an OS security sandbox or a claim
to trace every native library access.

The comparison checks every non-excluded JSON field and both CSV tables.
Exclusions are limited to run times, elapsed time, the hash of the newly
timestamped energy-mapping record, and an exact eigenvector-basis byte hash.
The latter is reported separately; energies, signed RMEs, interference terms,
all strengths and rates remain compared. The original producer/protocol
hashes must still match the frozen references.

`comparison.json` reports discrepancies and maximum numerical differences.
No tolerance is fitted to the result. `receipt.json` identifies the tested
payload inventory, runtime, generated-file hashes and read-boundary reports.
The five reproduced JSON/CSV products are also collected under `reproduced/`
in the run directory.

## Scientific boundary

The experimental 589(20)-ns half-life and 0.46(3)-W.u. strength share a
measurement origin. They are not independent validation data. The modeled
19/2 state assignments are conditional, and the energy-nearest of four
declared pairs is not a certified physical assignment.

The frozen protocol records an internal prospective test after the published
data were already known. Packaging and replay do not turn that record into
external preregistration. Its source locators and quoted experimental values
are preserved declarations; the external originals are not re-read here.

The width calculation sums open MODEL E2 radiative rates at MODEL photon
energies. It gives a conditional upper bound on half-life for that unchanged
scheme, not a complete lifetime prediction or a model-independent empirical
bound. Missing internal conversion and other radiative widths are not
invented. Their positive contributions would shorten the lifetime of the
unchanged scheme.

This package reproduces the declared model family. It does not reproduce the
original source authors' electromagnetic figures, validate the isomer decay
scheme, or establish nuclear-shape or publication-readiness claims.
