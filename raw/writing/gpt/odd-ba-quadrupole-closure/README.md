# Spin-channel redistribution in quadrupole shape diagnostics of odd barium

**Focused revision, 2026-11-06:** `main.pdf` is now the 12-page revised
candidate. It integrates the exact rigid-charge control, the 135/137Ba
source-spectrum comparison and the conditional 137Ba isomer failure.
Three standalone calculation packages have each been replayed successfully.
The internal text review found no remaining must-fix scientific wording issue
within its stated scope. The scoped three-source overlap comparison now confirms only an incremental
model-study candidate; it does not certify priority or journal-level significance.
Human authorship/accountability information, the final public data/code destination
and an accountable contribution assessment remain unresolved. The manuscript
has not been submitted and is **not submission-ready**.
See [the final evidence boundary](analysis/final-evidence-closure.md),
[the current revision record](analysis/revision-v2/summary.md),
[the earlier closeout disposition](analysis/closeout-20261106.md) and the
[Chinese stage report](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/closeout/a130-stage-report-20261106.pdf).

This is a focused English research manuscript prepared in the Springer Nature
two-column template for an EPJ A candidate. Its single question is how a nearly
saturated selected spin channel can respond to angular recoupling while carrying
only part of the complete charge moment.

Read `main.pdf` or edit `main.tex`, `controls.tex`, `rigid-control.tex` and
`revision-appendices.tex`. The numerical inputs,
model results and runnable code are in `data/`; its README gives reproduction
commands. Figures and their plotting scripts are in `figures/`, with disposable
plot views under `figures/made/data/`.

To regenerate the figures without overwriting the supplied versions:

```bash
python3 -B figures/made/plot_primary.py --output-dir /path/to/new-primary-figures
python3 -B figures/made/plot_coupling.py --output-dir /path/to/new-coupling-figures
python3 -B figures/made/plot_rigid_control.py --output-dir /path/to/new-rigid-figures
```

The main calculation covers the lowest 11/2-negative states of 129–137Ba.
A fixed-core quadrupole-coupling path in 135Ba isolates redistribution and
signed interference with little change in total quadratic strength. The
manuscript also retains the conclusion-changing findings: alternate E2
operators remove the particular arccos-domain violation, and the primary
model overpredicts the evaluated 135Ba static quadrupole moment.

This is an independent, explicitly defined finite-model study. The original
authors' electromagnetic/invariant figures have not been reproduced, and the
paper does not claim to correct them. Algebraic quadrupole invariants,
selected-observable diagnostics and truncation studies are established prior
work; the proposed contribution is the quantified mechanism in this declared
odd-Ba family, now accompanied by an independent fixed-geometry counterexample.

The new [revision data packages](data/revision-v2/README.md) preserve their
original producers and clearly identify adaptations for standalone replay.
The original 45-file manifest is unchanged. The preceding 10-page text/PDF
is retained under `analysis/revision-v2/previous-text/`; it is a historical
checkpoint, not the current candidate.

The package has completed internal scientific review and targeted rechecks.
It has not been submitted. Human author
and affiliation information remains an explicit placeholder. A compiled PDF
and successful numerical checks alone do not establish journal readiness.
The source-to-claim map and remaining scientific questions are recorded in
`sources/claim-ledger.md` and the review records under `analysis/`.

The class and numeric bibliography style derive from the archived official
Springer Nature December 2024 package. Their manuscript working copies have
only line-ending/trailing-whitespace normalization; the original package is
unchanged and original/working-copy hashes are recorded. The EPJ A instructions were rechecked
on 2026-11-06 and recommend that template with `iicol`. Template provenance is
recorded in `sources/template-and-source-record.json`.

This package uses public inputs and generated model data. It includes no
private experimental data and no source-paper full-text files. Frozen numerical
code retains the repository's MIT license in `data/code/LICENSE`.
The local Git attributes preserve the exact bytes under `data/`, including
CSV line endings, so a checkout does not silently change the registered hashes.
