# multipolePDM grid and threshold study

## Result for the report

Use **0.1 deg in arctan(delta) and 0.005 in sigma/I** for all the interval and component-mode checks in this study. The proposed **0.1 deg / 0.01** passed all checks in six of nine cases. It reproduced the connected angle and alignment HDI counts and the domain warnings in all nine. Its maximum angle HDI endpoint, quantile and CDF differences were 0.0140 deg, 0.0147 deg and 0.000204. It is sufficient here for those angle summaries if an angle mode shift of 0.200 deg is acceptable. It exceeded frozen tolerances for component modes and an alignment endpoint.

- In P-ADO at delta = -0.1, the lower alignment component mode was 0.100 on the proposed grid and 0.094 on the reference.
- In P-ADO at delta = -10, the small lower alignment component started at 0.09930 on the proposed grid and 0.09128 on the reference. One alignment component mode shifted by 0.005.
- In PDCO at delta = -10, the positive-angle component mode was 83.30 deg on the proposed grid and 83.10 deg on the reference. The positive interval endpoints changed by less than 0.006 deg.
- The coarsest grid failed at least one check in every case. It changed the alignment HDI component count in P-ADO at delta = +1 and -10. Its maximum angle quantile and alignment CDF differences were 0.2623 deg and 0.00745.
- Both 0.005 alignment grids and 0.1 deg / 0.001 passed all nine cases. The 0.1 deg / 0.005 grid uses 350,805 nodes, the fewest among the passing grids. Refining the angle alone at 0.01 alignment retained the same three failed cases.

Both angle boundaries triggered the production finite-domain warning in all three delta = -10 cases at every resolution. These cases are sensitive to the fixed angle domain. The true angle lies outside their 68% angle HDIs. Convergence here measures agreement with the reference under the tested geometries, error scales and scan limits.

The 0.1 deg / 0.005 grid had the fastest passing median in the completed run at 0.553 s per case and 153 MiB peak process RSS. At the same angle step, 0.001 alignment took 0.684 s and 303 MiB. The reference took 1.050 s and 495 MiB. Relative to the reference, 0.1 deg / 0.005 changed angle endpoints by up to 0.00535 deg, angle component modes by up to 0.100 deg, alignment endpoints by up to 0.00168, and alignment component modes by up to 0.002. The aggregate run took 66.3 s, with wall times subject to host load.

## Held-out verification

All six held-out cases at delta = -0.5 and +5 across the three modes passed the original convergence criteria for 0.1 deg / 0.005 against 0.05 deg / 0.001. Geometry, sigma/I = 0.3, and error rules were inherited. The 0.1075 absolute P error floor applied to all six. At delta = +5, forward P was -0.000531 for P-ADO and P-DCO and -0.013647 for PDCO. The greatest angle and alignment HDI endpoint differences were 0.00147 deg and 0.000421, and the greatest CDF differences were 0.0000466 and 0.000330. All +5 cases retained finite-domain warnings on both grids.

The truth was inside both marginal 68% HDIs on each grid in all six held-out cases. Truth inclusion is recorded separately from grid convergence. The primary delta = -10 cases still exclude the true angle from their 68% HDIs. See `heldout.json` and `heldout.csv` for per-case results. The frozen inputs and digest are in `heldout_inputs.json` and `heldout_inputs.sha256`.

```bash
OPENBLAS_NUM_THREADS=1 python -B raw/code/PDM/analysis/research/grid_resolution/heldout.py run
```

## Frozen design

The target is M1/E2 5 to 4. The DCO modes use a subsequent pure E2 4 to 2 gate. The ratio polar angles are 125 and 90 deg. The P detector is at 90 deg. PDCO conditions P on a 125 deg gate. Both DCO ratios use production azimuthal averaging, as does the PDCO polarization gate. P-ADO uses single-line intensities. The study reused the response fields for the three observations within each mode and grid.

The nine observation centers come from exact forward evaluations at delta = -0.1, +1 and -10 and sigma/I = 0.3. Errors are independent symmetric Gaussians. The ratio standard deviation is 0.10 times its forward center. The P standard deviation is `max(0.1075, 0.8*abs(P0))`. The floor comes from the median across ten distinct main-tier experimental lines after taking the arithmetic mean of each line's lower and upper absolute P errors. The uncertainties were checked against the archived publication tables and the audited candidate extraction. The relative term set the final P error in all nine cases, which span 0.1663 to 0.5966.

The frozen input file retains an incorrect printed-page locator for 132Ce 351.7 keV, source R037. The correct locator is **PDF p. 4 (printed p. 180), Table 2**. The same `0.03(5)` appears again on PDF p. 11 (printed p. 187), Table 4. The input hash and all numeric inputs were preserved. The freeze script uses the corrected locator for any subsequent freeze.

Each axis uses `linspace` with the prescribed endpoints and integer interval counts. The angle range is [-89.9, 89.9] deg. The alignment range is [0.03, 1]. The nominal 0.02 alignment step is 0.0202083333 on 49 nodes because the 0.97 span was divided into 48 intervals. All other actual steps equal their nominal values to floating-point precision. The reference is the 0.05 deg / 0.001 grid, with 3,492,687 nodes.

## Acceptance and threshold checks

The normalized angle density is integrated and summarized per degree. The alignment density is per unit sigma/I. The production piecewise-linear marginal summarizer evaluates 68% HDIs and equal-tail quantiles on these coordinates. A connected interval's mode maximizes that interval's interpolated density, including its endpoints. The mean and variance are integrated against the piecewise-linear density. The comparison evaluates the exact supremum CDF distance for those piecewise-linear curves. Joint mass, both marginal areas, CDF endpoints, and total HDI masses were checked to an absolute tolerance of `5e-12`.

Frozen convergence tolerances versus the reference are 0.15 deg for angle HDI endpoints and component modes, 0.10 deg for angle quantiles and mean or standard deviation, 0.005 for alignment HDI endpoints and component modes, 0.002 for alignment quantiles and mean or standard deviation, and 0.002 for each CDF distance. Branch counts and boundary warning flags must agree. Components with equal counts are compared in coordinate order.

`_NEAR_SINGULAR` at `1e-14`, `1e-12` and `1e-10` left the PDF and Jacobian bitwise identical and kept normalization and other warnings identical in the normal case and a small-Jacobian toy. The three cutoffs flagged 0/0/0 nodes in the normal case and 45/153/261 in the toy.

`_SIGMA_EPS_MULTIPLIER` was swept through 32/64/128. The normal case stayed valid, the 0-epsilon toy was rejected as an exactly zero Jacobian, and the 16-epsilon toy stayed unresolved. The 48-epsilon toy was valid only at 32. The 96-epsilon toy was valid at 32 and 64. The 192-epsilon toy stayed valid. These are classification tests of numerical resolvability. The production default was restored in the audit process. The registry's hardcoded `1e-12` clipping tolerance was inspected and remains untested.

## Reproduce from the Wiki root

```bash
work=raw/code/PDM/analysis/research/grid_resolution
(cd "$work" && sha256sum -c frozen_inputs.sha256)
OPENBLAS_NUM_THREADS=1 python -B "$work/study.py" run
OPENBLAS_NUM_THREADS=1 MPLCONFIGDIR="$PWD/tmp/pdm-current-research/grid/mpl" \
  python -B "$work/plot_marginals.py"
```

`run` verifies the frozen input, archived evidence, and production source hashes. It uses one fresh serial Python process per mode and grid on Linux, 27 groups for 81 mappings. It saves per-group intermediate files in `tmp/pdm-current-research/grid/`. Timing is forward build wall time plus mapping and marginal wall time for one observation, reported as a median across the nine cases. The memory column is the largest whole-process peak RSS across the three groups for that grid. The wall-time estimates exclude plotting, export, and process launch. The aggregate run time includes process launch, all three mappings per response, the threshold audit, and data export.

| Output | Contents |
| --- | --- |
| `frozen_inputs.json`, `frozen_inputs.sha256` | Nine observations, exact grid counts and spacings, thresholds, evidence and source hashes |
| `results.json`, `results.csv` | All 81 sets of angle and alignment statistics, per-component modes and masses, warnings, and timings |
| `comparisons.csv`, `grid_tradeoff.csv` | Differences and failed checks by case, and convergence, wall time and RSS by grid |
| `marginals.npz`, `marginals.pdf` | One-dimensional coordinate, PDF and CDF arrays and two diagnostic pages. Array keys use `<grid>__<mode>__<field>_<array_index>` for each PDF or CDF. Coordinates omit the trailing index. |
| `threshold_audit.json`, `near_singular.csv`, `sigma_resolvability.csv` | Threshold settings, observed classifications, node counts, and exact invariance tests |
