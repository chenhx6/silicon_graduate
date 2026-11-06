**At exactly fixed charge geometry, the all-J+2 proxy changes from 0.322617
to 1.026250 and leaves its real-angle domain, while the complete moments
remain q2 = 1, q3 = 0.5 and gamma = 20°.** This unpaired rotor control
provides an explicit example of proxy variation with unchanged intrinsic
charge shape. It addresses the geometric gap left by observing nearly
constant q2 in an IBFM calculation. It does not establish that the IBFM
wavefunctions themselves have unchanged geometry.

The [protocol](protocol.json) was frozen at
2026-11-06T08:30:38.890261+00:00, before any Hamiltonian/proxy results.
The production calculation began at 08:35:26.616364 UTC.
All prescribed points C = 0, 1, 2, 4, 8 MeV are retained, with no refinements,
parameter selection, charge adjustment or nuclear fit.

The fixed inputs are j = 11/2, gamma = 20°, intrinsic charge amplitude
mathcalQ = 1, and irrotational J0 = 30 hbar²/MeV in the explicitly declared
convention J_k = (4/3) J0 sin²(gamma−2pi k/3). The unsorted principal inertias
are (38.793852416, 16.527036447, 4.679111138) hbar²/MeV.
The bare unpaired Hamiltonian is sum_k (I_right,k−j_k)²/(2J_k) + C Q_j,
using I_right,y = −Jy. The charge tensor is core-only:
q20 = cos(gamma), q2,±2 = sin(gamma)/sqrt(2), times the fermion identity.
The field Q_j has the normalization stated in the protocol; it is not
identified with a fitted Ba interaction strength.

Every physical D2 state is solved for I = 1/2 through 15/2. Initial state
selection is always the lowest 11/2 state. This gives 216 multiplets and 2448
magnetic states. The required 7/2–15/2 intermediate channels are exhaustive
for the initial-state q2/q3 calculation. Completeness is restricted to that
purpose and the declared window, not the infinite rotor at every spin.
The analytic argument and independent controls are in [proof.md](proof.md).

| C, MeV | q2 full | q3 full | Proxy n1 raw | Proxy n5 raw | Proxy n10 raw | Proxy all raw | Proxy-all angle |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 0.5 | 0.578501 | 0.322617 | 0.322617 | 0.322617 | 23.7262° |
| 1 | 1 | 0.5 | 0.814612 | 0.716370 | 0.717145 | 0.716734 | 14.7382° |
| 2 | 1 | 0.5 | 0.958418 | 0.853502 | 0.851472 | 0.851096 | 10.5563° |
| 4 | 1 | 0.5 | **1.078496** | 0.971119 | 0.966264 | 0.966276 | 4.9741° |
| 8 | 1 | 0.5 | **1.140119** | **1.027976** | **1.026226** | **1.026250** | **undefined** |

The full angle is 20° at every point. Bold raw ratios exceed one; the
corresponding angles are null, with no clipping to zero degrees. There are
five such outcomes among the twenty prescribed C/count combinations.
“All” retains all 48 physical 15/2 states. Thus the final domain failure
survives removing the within-spin state-count truncation. The restricted
quantity is still rotationally invariant; its arccos conversion is the
operation that fails at those points.

At C = 0, only the two R=2 core eigenstates carry strength into each final
spin. Their ranks in the 15/2 block are 0 and 2, so n5 already exhausts that
sector. Its raw ratio 0.322617 still differs from the complete 0.5. This
illustrates a spin-sector restriction even when the selected sector's
strength is fully exhausted.

The change has a concrete angular-correlation mechanism. The fixed core
charge tensor is sampled by different particle-rotor eigenvectors. The
restricted strength and signed chain are:

| C, MeV | S, all J+2 | Signed chain | Middle diagonal | Middle off-diagonal |
|---:|---:|---:|---:|---:|
| 0 | 3.200000 | −2.207308 | −3.310962 | +1.103654 |
| 1 | 3.804718 | −6.357596 | −6.887667 | +0.530071 |
| 2 | 3.657109 | −7.114371 | −7.634827 | +0.520456 |
| 4 | 3.513520 | −7.606163 | −8.075496 | +0.469333 |
| 8 | 3.446951 | −7.849771 | −8.296711 | +0.446941 |

These enter sqrt(7/10)|chain|/S^(3/2). Relative to C = 0, the magnitude of the
middle-diagonal chain grows while the opposing off-diagonal contribution
shrinks. Across C = 1 to 8, the retained strength also decreases. The signed
full cubic sectors compensate to keep their total geometrically fixed:

| C, MeV | Positive spin-pair sum | Negative spin-pair sum | Net q3 |
|---:|---:|---:|---:|
| 0 | +0.500000 | 0 | 0.5 |
| 1 | +0.761555 | −0.261555 | 0.5 |
| 2 | +0.820506 | −0.320506 | 0.5 |
| 4 | +0.865959 | −0.365959 | 0.5 |
| 8 | +0.886899 | −0.386899 | 0.5 |

All nineteen angularly allowed ordered spin-pair sectors per C are retained
in [cubic-spin-sectors.csv](cubic-spin-sectors.csv); the other six of the
twenty-five possible pairs have zero rank-2/6j weight. These are derived model
contractions, not experimental transition data.

The static moment and quadratic fractions also change at fixed geometry:

| C, MeV | Qs/mathcalQ | Static q2 fraction | Other same-I fraction | All J+2 q2 fraction | P(R0) |
|---:|---:|---:|---:|---:|---:|
| 0 | ≈0 | ≈0 | 0.200000 | 0.266667 | 1.000000 |
| 1 | −1.089812 | 0.195471 | 0.052498 | 0.317060 | 0.647638 |
| 2 | −1.281619 | 0.270332 | 0.029994 | 0.304759 | 0.498004 |
| 4 | −1.412734 | 0.328473 | 0.014310 | 0.292793 | 0.367779 |
| 8 | −1.477981 | 0.359515 | 0.006653 | 0.287246 | 0.278370 |

Qs uses sqrt(16pi/5) times the stretched lab Q20 expectation and agrees with
the signed diagonal RME convention. Its unit is the declared charge amplitude,
not eb. P(R0) and mean R² describe rotor-state composition; geometry is fixed
by the input charge tensor and the proven operator identities, not inferred
from those probabilities.

All sampled same-I gaps are resolved. State matching uses squared overlaps
in the same bare D2 coordinate basis:

| C, MeV | Next 11/2 gap, MeV | Squared fidelity from preceding C | Forward/backward best rank |
|---:|---:|---:|---|
| 0 | 0.126795 | — | — |
| 1 | 0.385532 | 0.647638 | 0 / 0 |
| 2 | 0.526891 | 0.961761 | 0 / 0 |
| 4 | 0.617763 | 0.964740 | 0 / 0 |
| 8 | 0.717396 | 0.978074 | 0 / 0 |

The first interval contains substantial wavefunction reorientation. Its
next-largest forward overlap is 0.275848 with an excited state, below the
0.647638 lowest-to-lowest match. The sampled best ranks remain zero in both
directions. No extra grid was authorized or run, so this is not a
continuous-parameter no-switching theorem. The geometric identity is
state-independent and does not rely on such a continuity claim.

Verification includes independent checks beyond reuse of the two RME/closure
helpers:

- The initial-I quadratic and cubic matrices equal 1 and 0.5 times the
  identity before any eigenstate is selected; both maximum residuals are
  5.56e-16. This tests all 36 initial-spin D2 coordinates.
- The independent D2 group projector agrees with P P† to 1.29e-15.
  Hrot and charge-product D2 leakages are at most 1.78e-15 and 4.45e-16.
  The assembled lab tensor satisfies spherical Hermiticity and rank-2
  covariance to 2.23e-16 and 1.00e-15.
- Independent Euler-angle integration agrees with the product-RME route to
  2.74e-14; doubling quadrature nodes from 24 to 48 changes results by at
  most 1.95e-14. This integral contains no CG calculation.
- The exact spectator R0 vector has zero rotational energy and Qs, with
  overlap unity with the C = 0 lowest 11/2 eigenstate. All E2-carrying
  levels match the independently solved core R2 energies
  0.1267949192 and 0.4732050808 MeV. The analytic spin fractions
  (2I_f+1)/60 agree to 5.83e-16. The deliberately wrong body-Iy sign gives
  the same R0 vector a spurious 1.442081489-MeV energy.
- Every production point passes direct lab-tensor versus signed6j closure
  at M = 1/2 and M = 11/2. The C = 2 complex multiplet-rephasing test
  changes q3 by 1.12e-16 and any proxy raw ratio by at most 3.34e-16.
- Deliberately omitting the 15/2 outer channel at the spectator point loses
  0.266667 of q2. At initial I = 15/2, the finite window's average q2 is
  0.525 because required higher-spin channels are missing. Both diagnostics
  retain the distinction between exact initial-state closure and global
  infinite-rotor completeness.

The numerical main calculation, including serialization, took **2.534 s**
on this workspace; the recorded calculation before output serialization was
2.478 s, including 0.307 s of preflight. These timings exclude Python import
startup. Both loaded NumPy/SciPy OpenBLAS libraries were queried through their
exported runtime functions and each reported **one thread**. The execution
log, thread counts, actual UTC timestamps and artifact hashes are retained.

[summary.csv](summary.csv) preserves every proxy/count outcome;
[results.json](results.json) contains compact state, scalar, spin and
verification summaries; [run_control.py](run_control.py) is the executable
driver. No full eigenvectors, RME matrices or state-pair arrays are written.
[checks.json](checks.json) records the scoped final audit and helper hashes.
The model modules and initial protocol remain unchanged.

The justified conclusion is that changing angular coupling alone can change,
and even invalidate the real-angle conversion of, this J+2 proxy while the
charge tensor's complete geometric invariants are rigorously fixed. It is
an illustrative exact-unpaired rigid-core control. It neither calibrates a
physical Ba nucleus nor transfers a claim of rigid or unchanged intrinsic
geometry to the separate IBFM study. The parent experimental benchmark and
manuscript remain outside this sidecar.
