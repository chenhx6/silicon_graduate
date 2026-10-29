# AMR Cline Quadrupole Invariant Reconstruction & Core Triaxiality Evolution Worker

This worker provides a self-contained, reproducible microscopic and phenomenological reconstruction of Kumar-Cline quadrupole rotation invariants and effective core triaxiality evolution in even-even antimagnetic rotation (AMR) bands (110Cd and 104Pd).

## Scientific Scope & Model Foundations

1. **Exact Kumar-Cline Quadrupole Invariants**:
   - Zero-order (second-order in E2) scalar invariant isolating intrinsic quadrupole deformation magnitude:
     q2^2(I) = < I | (Q2 . Q2) | I > = (1 / (2I+1)) * sum_t |< I || E2 || t >|^2 = sum_t B(E2; I -> t)
   - Second-order (third-order in E2) scalar invariant isolating triaxial asymmetry delta:
     q2^3(I) cos(3*delta(I)) = - sqrt(35/2) * < I | [Q2 x Q2 x Q2]_0 | I >
                             = - sqrt(35/2) * (1 / (2I+1)) * sum_{s,t} (-1)^(2I) {2 2 2; I s t} <I||E2||s> <s||E2||t> <t||E2||I>
   - Mathematical proof that Cline invariants are strictly model-independent, separating intrinsic deformation magnitude q2 from triaxial shape asymmetry delta across all orientations.

2. **AMR Four-Blade Dynamics Coupled to a gamma-Soft Core**:
   - In-band B(E2; I -> I-2) is suppressed as sin^4(theta) due to symmetric shears closing (70 deg -> 31.1 deg in 110Cd, 90 deg -> 23.3 deg in 104Pd).
   - The collective gamma-soft core maintains a persistent deformation plateau (q2 ~ 0.31 - 0.35 e b, beta2 ~ 0.13 - 0.15).
   - Triaxiality cos(3*delta) evolves from ~ 0.28 - 0.32 (delta ~ 24 deg) at the bandhead towards the gamma-soft centroid cos(3*delta) ~ 0.02 - 0.06 (delta -> 30 deg) at band termination, demonstrating that AMR represents quasiparticle alignment embedded on a gamma-soft core.

3. **Finite-State Truncation & Uncertainty Propagation**:
   - Demonstrates that evaluating only in-band transitions causes a severe truncation defect Delta_trunc increasing from ~18% at the bandhead to ~47% at the band termination.
   - Cross-band virtual transitions into the gamma-vibrational core absorb the transverse shears strength.

## Scripts & Reproducibility

Run the analysis from this directory:

```bash
python3 amr_cline_invariants_model.py
```

Generated artifacts:
- amr_cline_invariants_cd110.csv: State-by-state evaluation of 110Cd Band 1 (I=16+ -> 24+).
- amr_cline_invariants_pd104.csv: State-by-state evaluation of 104Pd Yrast AMR band (I=16+ -> 26+).
- amr_cline_truncation_audit.csv: Comprehensive cross-nuclear truncation and completeness audit.
- amr_cline_invariants_results.json: Complete machine-readable results, baseline models, and metadata.
- amr_cline_invariants_plot.png & amr_cline_invariants_plot.svg: Publication-ready 4-panel diagnostic figure.

## Evidence Locators & Citations

- S. Roy et al., Phys. Lett. B 694, 322 (2011), Table 1, Eqs. 1-6 (local source: knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md).
- N. Rather et al., Phys. Rev. C 89, 061303(R) (2014), Table 1, Eqs. 1-9 (local source: knowledge/sources/rather-2014-104pd-antimagnetic-first-page.md and arXiv 1402.3422v1).
- S. Frauendorf, Rev. Mod. Phys. 73, 463 (2001), Sec. IV.B on shears mechanism and antimagnetic rotation (local source: knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md).
- D. Cline, Ann. Rev. Nucl. Part. Sci. 36, 683 (1986), pp. 697-700 (local source: knowledge/sources/cline-1986-nuclear-shapes-coulomb-excitation.md).
