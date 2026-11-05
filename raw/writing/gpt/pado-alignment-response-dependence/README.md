# A contract-conditional audit of alignment transfer in oriented-state gamma-ray angular distributions

This is the primary article work package selected on 2026-11-05.

The manuscript has one central methodological contribution:

> A reproducible audit workflow tests whether a shared `sigma/J` alignment proxy
> can be transferred across reaction conditions under an explicit covariance and
> coverage contract.

The public benchmark is the `^{67}Ga` 958-keV pure-E2 table from Zobel et al.
(1983). The public result is a conditional table-level calibration case study
intended to improve the evidence chain used in A≈130 wobbling, chirality,
tilted-precession and signature-partner studies; it is not a new alignment
theory, an event-level reanalysis, or a universal P-ADO rejection.

## Directory

- `data/`: normalized benchmark table and provenance; redistribution status remains pending author/license review;
- `analysis/`: model fits, covariance scans, fixed-\(\rho\) sensitivity toys,
  profile-preserving pseudo-experiment calibration, response-map validation and
  leave-one-row-out influence checks;
- `figures/`: article figures;
- `figures/made/data/`: regenerable plotting data;
- `sources/`: claim-to-locator and source manifest;
- `sources/claim-ledger.md`: paper-use P0/P1 claim audit;
- `main.tex`, `references.bib`: created after the evidence and journal gates.
- `main.pdf`: locally compiled draft using Tectonic 0.17.0, the Springer Nature
  `sn-jnl` class and the EPJ A-recommended `iicol` option; author metadata
  remains a placeholder.

The old `a130-triaxial` package remains a separate legacy audit case and is not
used as the manuscript structure or as an unverified numerical source.
