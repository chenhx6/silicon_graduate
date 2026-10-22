# checkpoint103 primed recall before A~130 thesis evidence matrix integration
Same run/session; original 2026-10-22 15:00 Shanghai research deadline. Strongly primed by checkpoints 088–101 and A~130 thesis evidence pipeline. No blind recall and no independent experimental data.
Core purpose: Integrate the Day 19 timing and response contracts into the A~130 thesis evidence matrix (knowledge/projects/a130-thesis-evidence-matrix.md):
1. Establish the physical clock classification and nuisance mapping for key A~130 benchmark states:
   - 128Cs (9+, 56 ns): TDPAD magnetic Larmor precession clock; nuisance: spin alignment attenuation, requires B-field calibration;
   - 129,131Ce (9/2-, 60/88 ns): TDPAD electric quadrupole interaction clock; nuisance: host EFG, eliminated by isotopic ratio;
   - 131Ce (27/2-, 1.23/1.24 ps): DSAM vs RDDS clock reconciliation; nuisance: K-projection convention in Qt extraction;
   - 134Nd (2+, 45.4 ps): RDDS mechanical flight clock; nuisance: finite stopping in stopper foil;
   - 103Rh (9/2+, 0.72 ps): Degrader-RDDS inverse-kinematics clock; nuisance: foil transit time and degrader straggling;
   - 98Ru (2+, 8.36 ps): Vacuum-flight RDDS clock; nuisance: hyperfine vacuum deorientation G_k(t).
2. Formulate explicit criteria for thesis-grade lifetime adoption based on the 8-item minimal calibration checklist.
Implement day19_a130_matrix_timing_contract103.py.
