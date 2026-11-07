---
type: research-note
title: "Half-filled single-j E2 node lifted by a normalized three-body scalar"
aliases: []
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [book-jain-nuclear-isomers]
created_from: project
promotion_target: high-spin-isomers-and-decay-modes-systematics
tags: [seniority, particle-hole-symmetry, three-body, e2, exact-diagonalization]
---

# Half-filled single-j E2 node lifted by a normalized three-body scalar

## Research Trigger

Round 2 T2 L4 asks whether an explicitly normalized, rotationally scalar, **pure three-body** interaction can break particle–hole symmetry and lift the half-filled E2 node for the states adiabatically connected to \(j^{6}\), \(J=10,v=2\) and \(J=8,v=2\), with \(j=11/2\). This is a controlled mathematical model investigation, not a calculation of a particular nucleus. The preceding [[seniority-mid-shell-cross-region-model-test-20261107]] already established the pure-pairing node and its survival under a \(J=2\) two-body perturbation; these are controls, not new discoveries here.

## Assumptions

The 12 orbitals are \(m=-11/2,\ldots,11/2\), and \(n=6\). The normalized pairing Hamiltonian is \(H_0=-A_{00}^{\dagger}A_{00}\). Let \(|27/2,27/2\rangle=c^{\dagger}_{11/2}c^{\dagger}_{9/2}c^{\dagger}_{7/2}|0\rangle\) up to a determinant phase; it is the unique maximal-\(J\) three-fermion highest-weight state. Generate all 28 normalized states using \(J_-\) and its standard ladder factors. If \(B^{\dagger}_{JM}|0\rangle=|JM\rangle\), take

\[
H(\lambda)=H_0+\lambda V_3,\qquad V_3=\sum_{M=-27/2}^{27/2}B^{\dagger}_{27/2,M}B_{27/2,M}.
\]

Each \(B\) annihilates exactly three fermions; \(V_3\) is explicitly normal ordered with three creation and three annihilation operators, number conserving, and vanishes on sectors with fewer than three particles. No \(C\)-odd projection is applied: such a projection generally generates lower-body terms after normal ordering and would not by itself establish a pure three-body example. \(\lambda\), energy, tensor matrix elements and strengths are dimensionless; \(\langle j\Vert Q_2\Vert j\rangle=1\). Pair normalization, Slater ordering, particle–hole phase \(C c_m^\dagger C^{-1}=(-1)^{j-m}c_{-m}\), and tensor convention are those of the imported preceding script. \(B_{10\to8}=|\langle8\Vert Q_2\Vert10\rangle|^2/21\).

## Provisional Reasoning

**New model result.** The candidate is scalar and breaks \(C\). At \(M=8\), \(\|V_3-V_3^\dagger\|_F=0\), \(\|V_3(M+1)J_+-J_+V_3(M)\|_F=2.50\times10^{-14}\), and \(\|[V_3,C]\|_F=5.45553\); \(\|V_3\|_F=16.85085\). For \(M=9,10\), commutator norms are 4.88027 and 4.40771, and rotational residuals are below \(2.36\times10^{-14}\). \(C\) is orthogonal and squares to the identity; \(H_0\) is \(C\)-even and \(Q_{20}\) is \(C\)-odd to roundoff. These are actual full fixed-\(M\) matrix tests, not inferred from a nonzero transition.

For \(\lambda=0\), the two specified states both have energy \(-1\), with one target state per fixed \(J\) and a gap \(2/3\) to the other states of that same \(J\). Their mutual degeneracy is harmless for scalar \(H\) because rotational invariance forbids mixing different \(J\); the zero-coupling quantity is only a transition matrix element, without a radiative energy. Within each \(J\) the nearby \(v=4\) and \(v=6\) multiplets are degenerate, so the first-order resolvent sums whole eigenspaces; it does not select arbitrary individual vectors. States at nonzero \(\lambda\) are continuously followed in positive and negative directions by maximum overlap, with the phase fixed by a positive overlap with the preceding state. State labels \(v=2\) at nonzero coupling mean their \(\lambda=0\) ancestry, not exact conserved seniority.

| \(\lambda\) | \(Q_{20}\) amplitude \(M_i=M_f=8\) | \(B_{10\to8}\) | \(\langle C\rangle_{10}\) | \(\langle C\rangle_8\) | \(E_{10}-E_8\) |
|---:|---:|---:|---:|---:|---:|
| -0.01 | -3.6461113e-5 | 4.2098070e-8 | -0.99998407 | -0.99990460 | -0.00616220 |
| -0.001 | -3.7662916e-6 | 4.4919016e-10 | -0.99999984 | -0.99999903 | -0.000617934 |
| +0.001 | +3.7924500e-6 | 4.5545145e-10 | -0.99999984 | -0.99999903 | +0.000618320 |
| +0.01 | +3.9075622e-5 | 4.8351968e-8 | -0.99998344 | -0.99990123 | +0.00620084 |

The signed amplitude convention depends on independently chosen state phases; its absolute value, \(B\), overlap squares and \(C\) expectations do not. In this convention, perturbation theory gives an initial-state contribution \(+0.00711479428\), a final-state contribution \(-0.00333539787\), and their nonzero coherent sum
\[
\mathcal A_{q=0}=0.00377939641\lambda+O(\lambda^2),\qquad
B_{10\to8}=0.000452321513\lambda^2+O(\lambda^3).
\]
The independent symmetric finite difference with step \(10^{-4}\) gives slope 0.00377939616. For \(\lambda=\pm10^{-4}\), \(B/\lambda^2=0.0004520084,0.0004526346\), approaching the first-order coefficient from either side. Nonlinear terms matter at larger coupling: at \(\pm0.05\), \(B/\lambda^2\) is 0.0002983 and 0.0006021 respectively. A broken Hamiltonian symmetry alone does not mathematically guarantee a nonzero transition; the explicit nonzero first-order matrix element establishes it for this particular channel.

\(E_{10}-E_8\) is positive throughout the sampled positive-coupling points and negative throughout the sampled negative-coupling points. Thus \(10\to8\) is energetically downward for the former and upward for the latter; a downward ordering alone does not establish a measurable decay or lifetime. At \(\lambda=+0.01\), squared overlaps with the two original states are 0.99997690 and 0.99994337; the associated \(C\) expectations demonstrate small but finite opposite-signature admixtures.

## Grounded Evidence

- **Author's model and scope:** Jain, Maheshwari and Goel, *Nuclear Isomers: A Primer*, Chapter 3, printed pp. 41–43 (PDF pp. 52–54), especially Eqs. (3.15), (3.20) and (3.21), distinguish the same-seniority even-rank reduction and \(\Delta v=2\) transitions. Directly inspected the local [book source](../sources/book-jain-nuclear-isomers.md) and the cited PDF pages. This book provides the baseline, not the present \(J=27/2\) three-body proposal or numbers.
- **Experiment:** none used or newly inferred. The cited book discusses experiment elsewhere; no experimental claim is attributed to the present simulation.
- **Task calculation:** [script](../../system/scripts/isomer_three_body_ph_breaking.py), [machine-readable output](../../outputs/l4/20261107-isomer-cross-region-round2/three-body/results.json), and [provenance receipt](../../outputs/l4/20261107-isomer-cross-region-round2/three-body/run-provenance.json). It imports the previously existing computational primitives as an explicit hashed input. The raw book, original note and original script are read only. No independent external literature search or novelty claim was attempted.

## Competing Explanations

The prior \(J=2\) scalar two-body interaction changes states yet keeps their \(C\) signatures equal, leaving the node at numerical zero. Here the same control over the sampled \(|\lambda|\le0.05\) has maximum \(B=1.85\times10^{-31}\), while the three-body channel gives the nonzero values above. To test the minimal-body-order claim more broadly, the code checks **all six** antisymmetric scalar pair channels \(J_p=0,2,4,6,8,10\) in both \(M=8\) and \(M=10\); their largest \(\|[V_{2,J_p},C]\|_F\) is \(4.70\times10^{-15}\). These channels span rotationally scalar two-body operators in this single identical-fermion \(j\) shell. A rotational scalar one-body operator is proportional to particle number and is constant in the fixed-\(n\) space. Thus order three is minimal **within this specified single-orbit, number-conserving rotational-scalar setting**. This does not establish minimality among multi-orbit, non-scalar, number-nonconserving or effective operators, or among all possible three-body channels; the maximum-\(J\) choice is a simple unique channel, not a proven globally optimal one.

A generic multi-orbit configuration admixture, an effective E2 operator with higher-body terms, or symmetry-breaking external structure could also remove a node, but is outside this Hamiltonian. A \(\Delta v=2\) transition at half filling can already be nonzero without breaking \(C\), as demonstrated by the preceding note; that separate transition is not the same tracked pair studied here.

## Transfer Conditions

**Parent operator check.** With normalized pair operators
\(\mathcal P_J=\sum_M A^\dagger_{JM}A_{JM}\), particle–hole conjugation from
the \(n\) sector to \(12-n\) gives
\[
C_n^\dagger\mathcal P_J^{(12-n)}C_n-\mathcal P_J^{(n)}
=(2J+1)(1-n/\Omega)\mathbf 1,\qquad\Omega=6.
\]
This follows by normal ordering the conjugated two-body operator: rotational
invariance leaves a scalar one-body contraction and a constant, fixed by the
empty/full-shell limits. At half filling the difference vanishes. The parent
checked all six channels at \(n=0,2,4,6,8,10,12\), giving 42 matrix identities.
It also checked the full \(n=6\), 924-determinant trace of the three-body
operator: \(28\binom{9}{3}=2352\), obtained numerically as
2352.0000000000014. These are extra operator/combinatorial checks on reused
matrix primitives, not a second independent complete many-body solver.

**Matrix strength versus rate.** A parent extension,
`system/scripts/isomer_three_body_rate_scaling.py`, evaluates the dimensionless
proxy \(R=(E_{10}-E_8)^5B_{10\to8}\) only for downward points.
With pure pairing, the same perturbation opens the gap linearly,
\(E_{10}-E_8\simeq0.618127\lambda\), while \(B\propto\lambda^2\);
therefore \(R\propto\lambda^7\). The small-step numerical logarithmic slope is
7.000012. This seventh power is **not** a general node-lifting law.
Adding the symmetry-preserving baseline \(+0.05\mathcal P_2\) already gives
a gap 0.0125349 at \(\lambda=0\), while the E2 node remains protected.
After adding \(V_3\), \(B\) still starts quadratically but \(R\) starts as
\(\lambda^2\), with numerical slope 2.000366. No physical energy scale,
radiation constant, ICC or competing width was supplied, so neither proxy
is a rate in seconds or a half-life prediction.

The counterexample applies to 12 exactly degenerate single-particle substates, six identical fermions, a scalar single-\(j\) Hamiltonian and the stated one-body E2 tensor. No real three-nucleon-force coupling, effective charge, fitted spectrum, photon energy in MeV, Weisskopf unit or lifetime is supplied. Generalizing to an actual nucleus requires an independently specified valence space, calibrated interaction and E2 operator, uncertainty analysis, competing configurations, and measured level energies. The word “minimal” refers to body order under the assumptions above, not physical magnitude or empirical necessity.

## Failure Conditions

The main claim fails if \(V_3\) is not a pure, normalized three-body scalar; if the fixed-\(J\) target degeneracy invalidates the chosen branch; if \([V_3,C]\) vanishes; if the matrix element tends to zero faster than first order under a convergent calculation; or if the observed strength is a tensor or phase convention artifact. At sufficiently large \(|\lambda|\), crossings and mixing can invalidate maximum-overlap ancestry; the present data only cover \(|\lambda|\le0.05\). The \(\lambda=0\) inter-\(J\) degeneracy and upward negative-\(\lambda\) ordering preclude treating every tabulated \(10\to8\) entry as a decay. No full-space numerical commutator over all \(M\) sectors was computed: the matrix tests cover \(M=8,9,10\), with exact multiplet construction furnishing the scalar argument.

## Falsification or Reverse Tests

- The normalized three-particle multiplet and corresponding \(n=3\) projector are checked at all 28 projections; lowering factors are explicit. Particle-number conservation follows algebraically from each \(B^\dagger B\), rather than an assumed numerical expectation value.
- Across all sampled data, maximum Hamiltonian eigenvector residual is \(1.54\times10^{-15}\), highest-weight residual \(4.07\times10^{-15}\), and maximum disagreement of the signed Wigner–Eckart reduced amplitude for \((M_i,q)=(8,0),(9,-1),(10,-2)\) is \(2.17\times10^{-15}\). Independent eigenvector sign reversal leaves \(B\) invariant; an explicit Slater basis reversal and rephasing changes the amplitude by at most \(3.47\times10^{-17}\).
- At \(\lambda=\pm0.01\), doubling tracking steps from 20 to 40 changes endpoint squared overlaps by at most \(8.89\times10^{-16}\), and the reported strengths agree to displayed machine precision. The minimum adjacent-step overlap squared over all scans is 0.999425. Rotating each degenerate fixed-\(J\) eigenspace changes the first-order response vector norm by at most \(3.12\times10^{-16}\).
- The identical command was rerun: original and replay JSON are byte-identical in this environment. The program computes tensor strengths from wavefunctions; it does not insert a preselected expected \(B\) into the generator. Other machines or library versions may differ in eigenvector phases and last digits; compare physical invariants and stated tolerances.

## Open Questions

How do other normalized three-fermion angular-momentum channels compare in size and sign, and is the cancellation between initial- and final-state first-order contributions special to this \(J=27/2\) choice? Can an independently constructed full Fock-space implementation reproduce the same invariant strength and projected resolvent without importing the preceding script? How does a calibrated multi-orbit calculation separate genuine three-body effects from effective operators and configuration mixing? A real-nucleus bridge is [[sn136-seniority-anomaly-and-three-body-identifiability-round2-20261107]]; it does not turn this toy interaction into a unique diagnosis of a fundamental 3N force.

## Human Review

No user review occurred in this task. Historical review fields do not determine use or certainty. The parent freshly replayed all 40 rows with byte-identical output and added the 42 operator identities and full-space trace check above. This remains a conditional model with shared computational primitives, not an independently implemented nuclear calculation.

## Promotion or Rejection History

2026-11-07: created as provisional L4 model finding, with source and numerical provenance; no formal synthesis promotion. The local first run exposed a NumPy scalar-conversion error and the first degeneracy-rotation check exposed rounding in its denominator; both were corrected before the final runs. These software issues did not constitute evidence that the physical candidate failed.
