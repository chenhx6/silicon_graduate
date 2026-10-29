# Alpha clustering versus mean-field octupole: reproducible surrogate

This directory contains a standard-library-only calculation for the research note
`knowledge/research-notes/alpha-clustering-vs-meanfield-octupole-boundary.md`.
It compares four illustrative core+alpha partitions:

| System | Relative channel | Role |
|---|---|---|
| `16O` | `12C+alpha` | light cluster limit |
| `20Ne` | `16O+alpha` | strong alpha molecular candidate |
| `212Po` | `208Pb+alpha` | heavy alpha-decay channel |
| `224Ra` | `220Rn+alpha` | octupole collectivity versus alpha-channel boundary |

Run:

```bash
python3 alpha_clustering_octupole_model.py
```

The script writes `systematics.csv`, `overlap_scan.csv`, `chart_data.json`, and
`results.json` in the same directory. The 7,688-point overlap grid is over `R`
and `beta3` for the `0+` and `3-` projected sectors of each system.

## Model objects

The cluster calculation uses the center-of-mass-corrected point-charge formula

```text
D0_cluster = e (A_core*Z_alpha - A_alpha*Z_core)/A * R
Q3_cluster = 2 e c3 R^3
c3 = Z_core (A_alpha/A)^3 - Z_alpha (A_core/A)^3
```

The sign of `D0` changes with the intrinsic axis convention; its square is used
for `B(E1)`. The axial `K=0` conversion is
`B(E1;1->0)=3 D0^2/(4 pi)` and
`B(E3;3->0)=7 Q3^2/(16 pi)`.

The mean-field comparison uses the requested liquid-drop-inspired scale

```text
D0_mf_raw = C_MF Z A^(1/3) beta2 beta3
C_MF = 9 r0/(4 pi),  r0 = 1.20 fm
Q3_mf = 3 Z (r0 A^(1/3))^3 beta3 / sqrt(7 pi)
```

`D0_mf_raw` is an unquenched scale. It intentionally does not pretend to include
the proton-neutron polarization and single-particle cancellation that make a
physical E1 amplitude small. The note compares this raw scale with the cluster
geometry and keeps the cancellation as a model boundary.

The overlap grid is the explicit surrogate for

```text
|<Psi_cluster(R)| P^pi P^J |Psi_MF(beta3)>|^2
```

It is a Gaussian collective-coordinate norm kernel with a two-lobe parity
factor and a finite-J damping factor. It is not an antisymmetrized microscopic
overlap, not a spectroscopic factor, and not an alpha preformation probability.
An actual result requires the same EDF, particle-number/parity/angular-momentum
projection, Pauli treatment, norm kernels, and asymptotic matching convention
on both sides.

`alpha_loc` is an explicitly labelled diagnostic, not a standard observable. It
combines a finite packet width (`k_F sigma_R`), a phenomenological Pauli-overlap
penalty, and the Coulomb ratio `V_C/E_F`. The decrease from the light systems to
`212Po/224Ra` is therefore a controlled model trend, not an extracted datum.

`G_wildermuth` values are conventional shell-occupancy inputs (`4, 8, 18, 18`)
for this comparison. Exact Wildermuth numbers depend on the oscillator basis and
the daughter configuration; changing that convention is a required sensitivity
study for a microscopic calculation.

## Interpretation of the generated values

The exact `16O=12C+alpha` and `20Ne=16O+alpha` charge-to-mass matching gives
`c1=0`, hence a point-cluster `D0_cluster=0` while `Q3_cluster` remains finite.
This is an algebraic counterexample to using a large E3 or a small E1 as a
unique alpha-cluster diagnostic. In the heavy systems the point-cluster dipole
is nonzero, but the surrogate locality factor and projected overlap fall; this
illustrates why an alpha-decay channel coordinate and a low-energy octupole
collective coordinate need not be the same degree of freedom.

The numbers are useful for formula, unit, symmetry, and limiting-case checks.
They are not fitted to ENSDF or GOSIA and should not be cited as measured
`B(E1)`, `B(E3)`, `beta3`, or overlap probabilities.
