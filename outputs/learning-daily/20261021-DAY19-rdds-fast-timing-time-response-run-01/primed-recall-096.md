# checkpoint096 primed recall before experiment design and counter-evidence audit
Same run/session; original 2026-10-22 15:00 Shanghai research deadline. Strongly primed by 088–095 source audits and previous Wiki notes. No blind recall and no independent experimental data.
Core purpose: Address the Day 19 curriculum required exercise and counter-evidence:
- Exercise: Choose between DSAM, RDDS, or Fast Timing for a candidate state in the overlap region (e.g. tau = 5 ps in A ~ 100-130), contrasting resolution, feeding pathways, and stopping material constraints.
- Counter-evidence: Construct an explicit, quantitative failure case where an apparent high precision (e.g. quoted sigma ~ 0.1 ps) is completely counterfeit, being dominated by:
  (a) Uncalibrated CFD walk / PRD baseline offset (producing false ps shift);
  (b) Unnoticed unmodeled side-feeding in RDDS (exponential tail counterfeiting delayed decay);
  (c) Stopping power nuclear/electronic partition error in DSAM lineshape fitting;
Demonstrate how the 8-item minimal calibration checklist acts as a definitive falsification filter.
Implement this in day19_experiment_design_falsification096.py, generating experiment-design-falsification-result-096.json.
