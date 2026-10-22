# checkpoint105 primed recall before gamma-soft/rigid timing synthesis
Same run/session; original 2026-10-22 15:00 Shanghai research deadline. Strongly primed by checkpoints 088–104 and gamma-soft/rigid synthesis history. No blind recall and no independent experimental data.
Core purpose: Connect Day 19 time measurement techniques (DSAM, RDDS, Fast Timing) to the discrimination between gamma-soft and gamma-rigid triaxial dynamics in knowledge/synthesis/gamma-soft-vs-gamma-rigid-diagnostics.md:
1. Re-evaluate Zamfir-Casten 1991 dual watershed: S(4,3,2) = -2.00 (O(6) soft) vs +1.67 (DF rigid 30 deg); and B(E2; 2_2 -> 0_1) = 0 (soft) vs 2/11 = 0.1818 (rigid).
2. Contrast lifetime-derived transition strengths in soft vs rigid benchmarks:
   - 136Sm (Babra 2019 DSAM): Qt drop -10.3% across crossing, stopping power scale invariance z = -2.179;
   - 98Ru (Radeck 2012 RDDS): B4/2 = 1.86(16) supporting quadrupole vibrational / quasi-O(6) softness;
   - 176W (Regis 2011 fast timing): B4/2 = 1.335 ruling out X(5) and placing the nucleus in the deformed rotor basin.
3. Integrate the 8-item minimal calibration checklist to prevent stopping power or uncalibrated walk errors from falsifying the gamma-potential landscape.
Implement day19_gamma_soft_timing_audit105.py.
