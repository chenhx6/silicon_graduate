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

python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/profile_coverage.py \
  --n-toys 1000 \
  --output raw/writing/gpt/pado-alignment-response-dependence/analysis/results/profile-coverage.json

python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/validate_response_map.py \
  --output raw/writing/gpt/pado-alignment-response-dependence/analysis/results/response-map-validation.json

python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/influence_checks.py \
  --output raw/writing/gpt/pado-alignment-response-dependence/analysis/results/influence-checks.json

python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/row_covariance_envelope.py \
  --output raw/writing/gpt/pado-alignment-response-dependence/analysis/results/row-covariance-envelope.json

python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/profile_coverage_grid.py \
  --n-toys 500 \
  --output raw/writing/gpt/pado-alignment-response-dependence/analysis/results/profile-coverage-grid.json

python3 raw/writing/gpt/pado-alignment-response-dependence/figures/made/generate_figures.py

python3 raw/writing/gpt/pado-alignment-response-dependence/figures/made/generate_coverage_grid.py

python3 raw/writing/gpt/pado-alignment-response-dependence/analysis/validate_outputs.py
```

The manuscript was compiled with the temporary Linux x86_64 Tectonic 0.17.0
binary into `main.pdf` using the EPJ A-recommended `iicol` option. The compiler
emitted underfull layout warnings but completed successfully; the six-page PDF
was visually inspected. The
Tectonic binary and cache remain under `tmp/` and are not part of the article
package.

The exact compiler/output record is in `results/compile-record.json`.

The coverage run uses random seed `20261105`; the fixed-rho grid uses
`20261106`; the profile-preserving calibration uses seed `20261107` and 1000
toys per true-rho value. Each profile toy repeats the same
`min_rho max_row_D2` operation used for the observed table, and the
`profile-coverage-toys.csv` file records the resulting toy statistics. The
profile is a table-level Gaussian sensitivity analysis with a block-diagonal
covariance contract: rows are treated as independent, quoted marginal errors
are treated as fixed standard errors, and one common rho is scanned as a
declared sensitivity parameter. It does not reconstruct source event counts,
detector response, or the missing row-internal or cross-row covariance.

BIC uses the ten rows as the independent observational units. The two
coordinates within each row are represented by the row covariance rather than
counted as separate independent samples.

The `mixture` model is a deliberately minimal direct/cascade population
negative control. It linearly mixes two Gaussian-substate alignment predictions;
it is a sensitivity model, not a validated feeding simulation.

`validate_response_map.py` independently replays the published
Der Mateosian--Sunyar \(J=23/2,\sigma/J=0.2\) attenuation-table row and checks a
narrow-width mathematical limit. This is a finite-\(J\) convention check; it
does not validate the Zobel detector response or recover missing event-level
inputs.

`influence_checks.py` repeats the profiled maximum-row calculation after removing
each row in turn. The result is a descriptive influence diagnostic; its
leave-one-row-out null distribution is not treated as a calibrated p-value.

`row_covariance_envelope.py` allows each row to choose its own within-row
correlation on the declared finite grid while retaining one shared response
proxy. It is an uncalibrated sensitivity envelope and does not resolve
cross-row dependence.

`profile_coverage_grid.py` repeats the complete profile statistic on a
five-by-seven \((r_{\rm true},\rho_{\rm true})\) nuisance grid. The reported
worst-case empirical 95% quantile is a conservative reference only within the
declared independent-row Gaussian contract.
