# Claim-to-source map

| Manuscript claim | Source / artifact | Locator or output |
|---|---|---|
| Zobel reaction identity, transition and ten-row table | `knowledge/sources/zobel-1983-energy-projectile-alignment.md` | printed p.392 / PDF p.4, Table 1; source claims Z83-11 to Z83-15 |
| Shared-alignment baseline | `knowledge/research-notes/pado-shared-alignment-null-profile.md` | Real-table Result; provisional max-Mahalanobis contract |
| Profile results in this package | `analysis/profile_alignment_models.py` | `analysis/results/alignment-profile.json` |
| Toy coverage result | `analysis/coverage_check.py` | `analysis/results/coverage.json`; seed 20261105 |
| Profile-preserving toy calibration | `analysis/profile_coverage.py` | `analysis/results/profile-coverage.json`; seed 20261107; 300 toys per true-rho value |
| Fixed-rho coverage sensitivity | `analysis/coverage_grid.py` | `analysis/results/coverage-grid.json`; seed 20261106; 5x7 grid |
| Historical source lineage | `knowledge/sources/zobel-1980-magnetic-substate-distributions.md` and `knowledge/sources/ionescu-1981-improved-angular-distribution-analysis-particle-xn.md` | Related method sources; not silently merged into the 1983 fixture |
| Public release candidate | `sources/public-release-manifest.json` | SHA-256 inventory; pending author license, metadata and permanent archive |
| Figure | `figures/made/generate_figures.py` | `figures/alignment_response_profile.pdf` and `.png` |
| A≈130 motivation and competing interpretations | `knowledge/sources/matta-2015-transverse-wobbling-135pr.md`, `knowledge/sources/lawrie-2020-tilted-precession-wobbling.md`, `knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md`, `knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md` | Source-specific locators must be checked again for final submission |

The paper is currently a Codex self-audited local draft. The main numerical
result is table-level and conditional on the stated covariance contract.

`claim-ledger.md` is the paper-use P0/P1 audit. It does not mark any claim as
human-reviewed or admitted for final submission.

`zobel-covariance-audit.md` records the direct PDF visual check that the source
mentions error ellipses and correlation but does not publish their numerical
parameters or raw counts.
