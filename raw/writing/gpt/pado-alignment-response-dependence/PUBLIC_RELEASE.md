# Public release manifest (author action required)

This file defines the smallest sanitized release that can accompany the
P-ADO table-level manuscript. It is a release plan and provenance contract; it
does not itself grant publication or collaboration permission.

The machine-readable file inventory and SHA-256 values are in
`sources/public-release-manifest.json`. Its status is intentionally
`pending-author-metadata-license-and-permanent-archive`.

## Candidate public files

- `data/zobel83_958_table1.csv`
- `data/README.md`
- `analysis/profile_alignment_models.py`
- `analysis/coverage_check.py`
- `analysis/coverage_grid.py`
- `analysis/profile_coverage.py`
- `analysis/validate_response_map.py`
- `analysis/influence_checks.py`
- `analysis/row_covariance_envelope.py`
- `analysis/profile_coverage_grid.py`
- `analysis/validate_outputs.py`
- `analysis/results/alignment-profile.json`
- `analysis/results/coverage.json`
- `analysis/results/coverage-grid.json`
- `analysis/results/profile-coverage.json`
- `analysis/results/profile-coverage-toys.csv`
- `analysis/results/response-map-validation.json`
- `analysis/results/influence-checks.json`
- `analysis/results/row-covariance-envelope.json`
- `analysis/results/profile-coverage-grid.json`
- `analysis/results/profile-coverage-grid-toys.csv`
- `figures/made/generate_figures.py`
- `figures/made/generate_coverage_grid.py`
- `figures/alignment_response_profile.pdf`
- `figures/coverage_grid.pdf`
- `main.tex`
- `references.bib`

## Materials excluded from redistribution

- publisher PDFs and copyrighted source scans;
- raw event counts, detector response matrices and source covariance, because
  they were not supplied by the source;
- private iThemba/South Africa data, which are unrelated to this public
  benchmark package and remain local-only;
- author, collaboration and institution metadata until the author group
  confirms the final record.

## Reproducibility contract

The release must record:

1. the repository commit or permanent archive identifier;
2. Python, NumPy and SciPy versions;
3. the exact commands in `analysis/README.md`;
4. SHA-256 values for the normalized CSV, scripts and JSON outputs;
5. the independent-row, fixed-marginal-error, common-\(\rho\) Gaussian contract;
6. the distinction between fixed-\(\rho\) sensitivity toys and the
   profile-preserving calibration;
7. the finite-\(J\) response-map convention check and its limitation;
8. the fact that no experimental p-value or event-level likelihood is provided.

The final public DOI, license and author authorization are unresolved gates.
Until they are filled, the manuscript remains a local reproducible candidate.
