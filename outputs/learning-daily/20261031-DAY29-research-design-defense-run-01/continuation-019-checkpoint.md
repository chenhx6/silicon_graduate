---
type: output
graph-excluded: true
created: 2026-11-01
updated: 2026-11-01
---

# Day29 continuation 019: doctoral research synthesis and pre-closeout consolidation

## Run state

- run_id: `2026-10-31-day-29-01`
- session_id: `01a191e7-29f8-79f2-8276-9a88282a4ed5`
- day_index: 29
- completed_day_indices: [29]
- partial_day_indices: [30]
- next_day_index: 30
- time_snapshot: `2026-11-01T14:10:00+08:00` (Asia/Shanghai)
- hard_deadline: `2026-11-01T15:00:00+08:00`
- minutes_to_deadline: 50
- closeout_decision: finish-current-no-new-unit
- resume_command: `codex resume 01a191e7-29f8-79f2-8276-9a88282a4ed5 -C /workspace/wiki -s danger-full-access -a never`

## Doctoral research integration (`131Ce` & `133Ce`)

Following user instructions and the author's doctoral midterm review
(`raw/personal/graduation_process/midterm_review/附件4：中期报告模板.doc`),
the target-nucleus research program is consolidated across two complementary
spectroscopy experiments:

1. **`133Ce` in-beam experiment (iThemba LABS PR295)**:
   - 21 new $\gamma$ transitions identified.
   - New rotational band with bandhead spin $13/2^-$ (12 transitions) in the
     low-spin domain.
   - Multipole mixing ratios $\delta$ of interband connecting transitions are
     negative with small absolute values ($|\delta| \lesssim 0.5$), proving
     predominant $M1$ character. This disfavors transverse wobbling (which
     requires $|\delta| \gg 1$ and enhanced $E2$).
   - Signature splitting exhibits signature inversion with increasing spin,
     indicative of non-axial Coriolis coupling on $h_{11/2}$ quasiparticles.
   - Systematics across $N=75$ isotones ($^{131}\text{Ba} \to {}^{133}\text{Ce} \to {}^{135}\text{Nd}$)
     tracks a triaxial core evolution from $\gamma$-soft to $\gamma$-rigid.
2. **`131Ce` in-beam experiment (CIAE Beijing Tandem HI-13)**:
   - Data processing, energy calibration and coincidence sorting are in progress
     to complete the high-spin level scheme, determine key transition
     multipolarities and spin/parity assignments.
   - Positioned at $N=73$, bracketing the $N=74$ triaxial core $^{132}\text{Ce}$
     symmetrically opposite to $^{133}\text{Ce}$ ($N=75$).
3. **NuclearMap PC-PK1 RHB even-even core context**:
   - $^{130}\text{Ce}$ ($N=72$): $\beta=0.25, \gamma=0^\circ$ (prolate).
   - $^{132}\text{Ce}$ ($N=74$): $\beta=0.22, \gamma=17^\circ$ (triaxial ground-state minimum).
   - $^{134}\text{Ce}$ ($N=76$): $\beta=0.17, \gamma=0^\circ$ (prolate with $\gamma$-soft valley).
   - Archived locally at `raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/`
     with `manifest.json`.
4. **Probability-Density Mapping (PDM)**:
   - The PDM method developed by the author (*Chen, Guo et al., NST under review*)
     provides the exact framework needed to extract $\delta$ from $(R_{ADO}, P)$
     without preset spin alignment $\sigma/I$.

## SouthAfrica dataset reorganization summary

- **First pass**: 37 files moved (including 3 backup drawings to `archive/`
  and 3 shared calibration utilities to `calibration/_shared/`), and 4 exact
  duplicate utility copies removed.
- **Second pass**: 5 ROOT matrices placed in `133Ce_iThemba2019/mat/root/` and
  source calibration spectra placed in `133Ce_iThemba2019/calibration/source-spectra/`
  (2,751 files, 4.52 GB).
- **Integrity**: 41/41 hash checks and existence verifications passed.
  `raw/**` remains gitignored.

## Matrix bin-by-bin integer audit

- `g45allmatprompt.root` and `g90allmatprompt.root` match `m4b/g45allmatprompt.m4b`
  and `m4b/g90allmatprompt.m4b` with zero mismatches across all 16,777,216 bins.
- `gg.root`, `hgg.root`, `vgg.root` match `m4b/ggmat.m4b`, `m4b/hggmat.m4b`,
  `m4b/vggmat.m4b` (unprompted) with zero mismatches.
- They represent two distinct coincidence windows (prompted vs unprompted) and
  must not be pooled without gate/time-cut harmonization.

## Verification baseline

- `validate_writeback_items.py`: 29 items valid, 0 errors.
- `wiki_automation_preflight.py`: ok: true.
- `wiki_archive_gate.py --changed`: ok: true.
- `wiki_lint.py --no-git --fail-on error`: 0 errors.
- `git diff --check`: clean.
- 76 unit/regression tests passed.
- Live processes: clock PID 628, Farmer PID 520, Codex session 01a191e7-29f8-79f2-8276-9a88282a4ed5.

## Pre-closeout invariant

At the 15:00 hard cutoff, enter closeout-only phase to finalize the daily
report, update the final session receipt, run preflight/lint/diff checks, and
execute non-force git publication while maintaining `completed_day_indices: [29]`,
`partial_day_indices: [30]`, `next_day_index: 30`.
