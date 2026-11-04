# Reproduction

Run from the repository root:

```bash
python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/profile_alignment_models.py \
  --output raw/writing/gpt/pado-alignment-response-dependence/analysis/results/alignment-profile.json

python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/coverage_check.py \
  --n-toys 1000 \
  --output raw/writing/gpt/pado-alignment-response-dependence/analysis/results/coverage.json

python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/coverage_grid.py \
  --n-toys 1000 \
  --output raw/writing/gpt/pado-alignment-response-dependence/analysis/results/coverage-grid.json

python3 raw/writing/gpt/pado-alignment-response-dependence/figures/made/generate_figures.py

python3 raw/writing/gpt/pado-alignment-response-dependence/figures/made/generate_coverage_grid.py

python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/validate_outputs.py
```

The manuscript was compiled with the temporary Linux x86_64 Tectonic 0.17.0
binary into `main.pdf`. The compiler emitted underfull-vbox layout warnings but
completed successfully; the seven-page PDF was visually inspected. The
Tectonic binary and cache remain under `tmp/` and are not part of the article
package.

The exact compiler/output record is in `results/compile-record.json`.

The coverage run uses random seed `20261105`. The profile is a table-level
Gaussian sensitivity analysis. It does not reconstruct source event counts,
detector response, or the missing row-internal covariance.

The `mixture` model is a deliberately minimal direct/cascade population
negative control. It linearly mixes two Gaussian-substate alignment predictions;
it is a sensitivity model, not a validated feeding simulation.
