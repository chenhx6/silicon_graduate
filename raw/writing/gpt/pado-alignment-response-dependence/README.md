# Reaction-dependent alignment response in P-ADO

This is the primary article work package selected on 2026-11-05.

The manuscript has one central claim to test:

> A single shared `sigma/J` alignment nuisance cannot automatically be transferred
> across projectile, beam-energy and feeding conditions in P-ADO analysis.

The public benchmark is the `^{67}Ga` 958-keV pure-E2 table from Zobel et al.
(1983). The result is intended to improve the evidence chain used in A≈130
wobbling, chirality, tilted-precession and signature-partner studies.

## Directory

- `data/`: publication-authorized base table and provenance;
- `analysis/`: model fits, covariance scans, fixed-\(\rho\) sensitivity toys and
  profile-preserving pseudo-experiment calibration;
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
