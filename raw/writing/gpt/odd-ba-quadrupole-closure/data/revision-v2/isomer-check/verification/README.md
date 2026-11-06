# Recorded standalone replay

The unchanged strength producer and unchanged width producer each ran once
from a physical copy of this payload. Both completed successfully. No model,
operator root, state ordinal or comparison tolerance was fitted in this run.

| Comparison | Records | Maximum absolute difference |
| --- | ---: | ---: |
| Energy-first mapping | 4 pairs | 0 |
| Strength results, including signed RMEs and interference | 28 | 0 |
| E2 radiative width sums and half-life bounds | 14 | 0 |
| Open E2 branch records | 84 | 0 |
| Strength and width CSV tables | 28 + 14 | 0 |

All 1865 compared floating fields agree exactly after parsing.
The state-basis byte hash agrees as well. Both CSV files are byte-identical
to their frozen references. JSON files have fresh run timestamps; the exact
metadata exclusions and comparison tolerances are in `comparison.json`.
All other fields, including original protocol/producer hashes, are compared.

The tested payload inventory SHA-256 is
`6e51a52f5155f312221624320eab910ffcf0798b2334d38df63612d00d2ca8c9`.
The `receipt.json` in this directory identifies the actual run from
2026-11-06T11:08:08.163416+00:00 to 2026-11-06T11:08:15.081171+00:00.
Its paths record the physical execution location; these historical paths
are not runtime dependencies after this package is moved.

The run used Python 3.12.3, NumPy 2.5.4 and
SciPy 1.18.1. Only that runtime was tested.
Each modeled first 19/2 parent has three open E2 branches, and each modeled
second 19/2 parent has nine; seven operators give 7*(3+9)=84 branch records.

The energy diagnostic again chose `19half_1_to_15half_2`.
It uses squared residuals of both levels relative to the lowest 11/2 anchor.
It is an internal frozen mapping rule, not a certified experimental assignment.

The two workers blocked their deliberate forbidden-file probes. They recorded
no unexpected denied access and no network/nested-subprocess attempt.
Every allowed scientific-file access event was within the staged run tree.
`allowed_file_reads` records Python audit events before the operating system
completes the operation: it therefore includes attempts to read absent `.pyc`
cache files and directory enumeration. It is not a count of successful file
opens or a complete native/OS-level trace. Runtime libraries are allowed
under the exact interpreter roots recorded in the boundary reports.

The width layout uses the real packaged frozen strength result to satisfy its
unchanged historical file-hash prerequisite. The width calculation is newly
executed; newly computed strengths are compared separately. No hash checker
was patched and no missing scientific file was simulated.

The 23 payload files are checked by `../inventory.json`. This directory has
its own relative `inventory.json` for the 14 verification artifacts. The
top-level `../manifest.json` is a repository archive envelope whose paths
are repository-relative; it is not a standalone runtime dependency.

No external PDF, ENSDF file, publisher crop, historical source page or prior
calibration run was bundled or reverified. Historical source declarations
remain in `../source-declarations.json` and the exact input snapshots.
This is numerical reproduction of the frozen model family. The decay sums
remain conditional model-scheme E2-radiative upper half-life bounds, with
no physical assignment, complete-lifetime or source-author validation claim.
