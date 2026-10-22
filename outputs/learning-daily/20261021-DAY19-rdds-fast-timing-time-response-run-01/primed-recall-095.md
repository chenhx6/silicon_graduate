# checkpoint095 primed recall before decision tree and checklist synthesis
Same run/session; original 2026-10-22 15:00 Shanghai research deadline. Strongly primed by 088–094 source audits and previous Wiki notes. No blind recall and no independent experimental data.
Core purpose: Synthesize the full-scope Method Selection Decision Tree and the 8-item Minimal Calibration Checklist, explicitly stripping out all ungrounded universal hard windows (e.g. "DSAM strictly capped at 2 ps", "RDDS impossible below 1 ps", "Fast timing universal 50 ps floor", "TDPAD identical to lifetime clock").
Basis:
1. DSAM observable is velocity-attenuation weighted by stopping time; range depends on medium (solid ~300 fs, gas ~10–1000 ps per Nolan). Requires stopping power (fe, fn), feeding model/gate, recoil angle projection.
2. RDDS observable is flight/stopped component ratio as a function of distance; range set by v and mechanical/foil limits (down to ~0.5 ps with degrader/inverse kinematics per Suzuki/Klemme, up to ~ns per Nolan/Radeck). Requires distance zero/gain, finite-stopping/foil transition, feeding gate, and deorientation/angular boost corrections.
3. Fast timing (MSCD/slope/centroid) observable is electronic delayed coincidence time distribution; range spans picoseconds to microseconds (slope for tau > FWHM, centroid/MSCD down to few ps depending on PMT/CFD and PRD accuracy). Requires matched prompt calibration (full-energy PRD), walk compensation, active background suppression (BGO/HPGe), and intermediate level delay isolation.
4. TDPAD observable is perturbation factor G_k(t) and Larmor/quadrupole precession frequency; measures magnetic/quadrupole moments; lifetime requires population decay envelope or companion fast timing, not to be confused with hyper-fine oscillation period.
Minimal calibration checklist must cover:
(1) Level, branch and conversion electron identity;
(2) Decay and stopped component definition and slow tail partition;
(3) Distance zero and velocity distribution / transport;
(4) Stopping material properties and finite-foil transit;
(5) Feeder gate purity and cascade normalization;
(6) Angle, boost and efficiency response;
(7) PRF/PRD calibration matched in energy, settings, and drift;
(8) Full joint covariance and shared reference floors.
Design mathematical and decision logic tests in day19_method_selection_and_minimal_checklist095.py.
