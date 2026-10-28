# AMR double-shears/core-coupling worker

This worker contains a standard-library-only, conditional calculation for the
110Cd and 104Pd AMR comparison.

Run from this directory:

```bash
python3 amr_double_shears_core.py
```

Outputs:

- `amr_double_shears_core.json`: tensor residuals, literal particle-plus-rotor rows, reported experimental rows, beta2 core scale, source hashes, and boundaries.
- `angle_and_core_scale.csv`: normalized `T22` and `sin^4(theta)` values.
- `beta2_core_scale.csv`: uniform-charge K=0 high-spin core B(E2) scale for beta2 = 0.10, 0.12, 0.14.

Evidence locators used by the calculation:

- Roy et al., PLB 694 (2011), pp. 324–326: Table 1, Eqs. 3–6, Fig. 4; local source page `knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md`.
- Rather et al., PRC 89, 061303(R) (2014), full arXiv v1: pp. 1–5 and Table I on printed p. 11; the Wiki source page currently records the publisher first-page acquisition boundary.
- Zhang, CPC 43, 054107 (2019), arXiv v1 pp. 4–7: fixed-shape limitation and fitted epsilon2 path; local source page `knowledge/sources/zhang-2019-104pd-pnc-antimagnetic-rotation.md`.

The calculation validates algebra and reproduces the order of magnitude of the
published particle-plus-rotor rows. It does not perform an EDF calculation,
wave-function projection, DSAM refit, or an experimental decomposition of
`B(E2)` into core and shears amplitudes.
