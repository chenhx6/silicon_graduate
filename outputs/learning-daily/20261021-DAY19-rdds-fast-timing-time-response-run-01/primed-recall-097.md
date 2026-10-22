# checkpoint097 primed recall before TQM and Qspec falsification audit
Same run/session; original 2026-10-22 15:00 Shanghai research deadline. Strongly primed by checkpoint 008, 088, and previous Day 20 pre-study. No blind recall and no independent experimental data.
Core purpose: Re-audit the remaining unverified Day 20 preview assertions in knowledge/observables/transition-quadrupole-moment.md, specifically:
1. Falsify the assertion that Qs = 0 is a unique geometric fingerprint of gamma = 30 deg triaxiality.
   - Counter-example: For an axially symmetric rotor (gamma = 0) with I=3, K=2, the spectroscopic quadrupole moment is proportional to [3K^2 - I(I+1)] = 3*(4) - 3*(4) = 0! Thus, Qs vanishes identically in a purely axial rotor without any triaxiality.
   - For an odd-A nucleus with K=1/2, [3K^2 - I(I+1)] can also vanish or change sign depending on decoupling parameter and core mixing.
2. Verify Davydov-Filippov vs Bohr-Mottelson axial limit:
   - For a 2+_1 state in an axial rotor (K=0), Q_spec = -2/7 Q0.
   - Any formula that fails to reproduce -2/7 at gamma = 0 violates the axial correspondence principle.
3. Quantify K-rotor extraction sensitivity:
   - Contrast K=1/2 vs K=11/2 in 131Ce: G(K=1/2) = 26/75, G(K=11/2) = 76/325; ratio sqrt(169/114) = 1.21756.
   - Demonstrates that cross-paper differences in reported Qt (e.g. 2.28 eb vs 2.72 eb) are pure K-convention shifts, not physical shape changes.
Implement day19_tqm_qspec_falsification097.py and verify mathematical controls.
