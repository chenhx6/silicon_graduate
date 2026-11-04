# Reproduction

Run from the repository root:

```bash
python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/profile_alignment_models.py \
  --output raw/writing/gpt/pado-alignment-response-dependence/analysis/results/alignment-profile.json

python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/coverage_check.py \
  --n-toys 1000 \
  --output raw/writing/gpt/pado-alignment-response-dependence/analysis/results/coverage.json

python3 raw/writing/gpt/pado-alignment-response-dependence/figures/made/generate_figures.py
```

The coverage run uses random seed `20261105`. The profile is a table-level
Gaussian sensitivity analysis. It does not reconstruct source event counts,
detector response, or the missing row-internal covariance.
