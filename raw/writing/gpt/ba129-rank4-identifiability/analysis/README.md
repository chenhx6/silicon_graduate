# Reproducible coefficient diagnostics

From the article directory:

```bash
python3 analysis/rank4_invariant.py --input data/ba129_same_parent_A4.csv --output analysis/results/rank4-invariant.json
python3 analysis/companion_profile.py
python3 analysis/physical_population_witness.py
python3 figures/made/generate_figures.py --results analysis/results/rank4-invariant.json --output figures/rank4_companion_gate.pdf
python3 figures/made/generate_profile_figure.py
python3 analysis/validate_case.py
```

Python 3, NumPy, SciPy and Matplotlib are needed for the profiles and figures.
SymPy is required to run the independent standard-Wigner and photon-projection
verification. The validator reports that part as not run if SymPy is absent;
this is not an algebra-validation pass. The recorded run used Python 3.12.3,
NumPy 2.5.4, SciPy 1.18.1 and SymPy 1.14.0; actual output records take precedence
if local versions differ.

Optional `--wiki-root /path/to/wiki` checks the raw ENSDF and publisher JSON
hashes named by `data/input-contract.json`. Those copyrighted/local upstream
materials are not included in a public reproduction package.

The analysis keeps two source versions separate: the 2014 evaluated record and
the visually verified 1977 primary table. Their coefficient means agree, but
three margins and the reported transition energies differ. They are analyzed
as alternatives, never pooled as independent experiments. The unknown
covariance is represented by a finite chosen correlation family. Response
ratios are fixed to one for those diagnostic runs.

The additional population program minimizes a common literal margin multiplier
subject to seven nonnegative substate-pair weights summing to one. It checks
primal feasibility and a dual certificate. It is an existence test under unit
response, not a measurement of alignment or a calibrated confidence region.

For each mixing angle, reference coefficients are profiled as unrestricted
real nuisances. The projected-residual quadratic form equals the direct
whitened GLS minimum. This is profiling at fixed covariance, not marginalizing
reference coefficients; adding a projected log determinant would change the
problem. Physical population-positivity constraints are not imposed, so a low
distance is not proof of a realizable parent population.

No actual delta estimate, experimental p-value, confidence interval, branch
probability, detector response, lifetime or wobbling classification is produced.
