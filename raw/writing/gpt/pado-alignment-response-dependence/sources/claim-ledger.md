# Claim ledger and paper evidence gate

The manuscript is a local Codex draft. This ledger separates source-grounded
facts, new table-level calculations, and claims that remain outside the paper
evidence gate.

| ID | Manuscript location | Claim | Kind | Evidence | Status | Required action |
|---|---|---|---|---|---|---|
| PADO-01 | Introduction | P-ADO observables depend on substate population, feeding, detector response and angular-distribution treatment | method/background | Hamilton 1975; Yamazaki 1967; Zobel 1983 source cards | candidate evidence | Recheck exact source locators before submission |
| PADO-02 | Benchmark | The ten rows are the \(^{67}\mathrm{Ga}\) 958-keV \(13/2^+\to9/2^+\) table with the stated reactions and quoted errors | experimental source fact | Zobel 1983 printed p.392 / PDF p.4 Table 1; `data/zobel83_958_table1.csv` | self-audited, needs targeted review | Verify table transcription against the archived PDF during paper review |
| PADO-03 | Methods | Row-internal covariance is unavailable and \(\rho\) is a declared sensitivity parameter | evidence boundary | Zobel source Z83-11/Z83-12; `sources/zobel-covariance-audit.md`, printed p.393/PDF p.5 | admitted as boundary | Preserve wording; do not call \(\rho\) measured |
| PADO-04 | Results | At \(\rho=0\), shared \(r_0=0.280146\) and the family/energy/mixture fit values are as reported | new table-level calculation | `analysis/profile_alignment_models.py`, `alignment-profile.json`, fixed seed/inputs | self-audited, provisional | Re-run after any fixture or model change |
| PADO-05 | Results | Extended models do not improve AIC/BIC at the center covariance contract | new table-level calculation | same JSON output | self-audited, provisional | Add covariance/profile sensitivity to final table |
| PADO-06 | Results | The maximum row-wise discrepancy remains above the single-row threshold over the explored \(\rho\) range | new sensitivity result | `alignment-profile.json` rho profile | self-audited, conditional | Do not report as a calibrated p-value |
| PADO-07 | Results | The single-row \(q_{0.95}^{(2)}\) threshold has empirical maximum-row coverage 0.654 in the declared toy model | new toy-coverage result | `coverage_check.py`, `coverage.json`, seed 20261105 | self-audited, conditional | Add additional \(\rho\)/true-\(r\) coverage grid |
| PADO-07b | Results | Across the \(5\times5\) true-\(r\)/true-\(\rho\) grid, matched-covariance coverage remains about 0.62--0.68; forcing \(\rho=0\) can lower it to about 0.52 | new toy-coverage result | `coverage_grid.py`, `coverage-grid.json`, seed 20261106 | self-audited, conditional | Treat as calibration sensitivity, not experimental p-value |
| PADO-07c | Results | The profiled observed shared-model \(D^2_{\max}\) minimum is 22.18 at \(\rho=0.64\), while matched toy 95% maximum-statistic quantiles are 9.60--10.59 | cross-output conditional comparison | `alignment-profile.json` plus `coverage-grid.json` | self-audited, conditional | Recompute if the covariance contract changes |
| PADO-08 | Discussion | The result does not invalidate P-ADO or identify a unique physical replacement model | inference boundary | PADO-04--PADO-07 plus Zobel limitations | required wording | Retain calibrated wording |
| PADO-09 | A≈130 implication | Alignment transfer and coverage must be checked before using a mixing-ratio branch as a collective-mode discriminator | cross-source inference | Zobel 1983 plus Matta/Lawrie/Lv/Nomura source cards | candidate evidence | User targeted review before final paper admission |
| PADO-10 | Data availability | No raw events, source covariance or detector response were reconstructed | data boundary | archived source and local package manifest | admitted boundary | Keep DAS explicit and do not claim event-level reanalysis |

## P0/P1 paper-use review queue

- **P0**: PADO-02, PADO-04, PADO-05, PADO-06, PADO-07.
- **P1**: PADO-01, PADO-08, PADO-09, PADO-10.

No claim in this ledger is marked `human-reviewed`. Final paper admission requires
focused user review of the listed P0/P1 claims and the exact manuscript wording.
