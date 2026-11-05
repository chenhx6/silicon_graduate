# 129Ba particle–hole/shape duality: source and operator audit

Date: 2026-11-05. Scope: read-only source/code study. Audit artifacts are
confined to this directory; this review's publisher-page renders are stored
under `tmp/ba129-model-readiness/symmetry-review/pages/`. No parent fits,
raw files, knowledge pages, PLAN, installation files, other sessions'
artifacts, or Git commits were changed.
The RMS is **parent computation, not independently refitted**:
39.925201699389206 keV, read from
`best.RMS_residual_keV_excluding_anchor` in the
[parent exact-fit record](/workspace/wiki/outputs/l4/20261105-ba129-model-readiness/model-fit-free-inertias-C120/energy-calibration.json).

**Finding:** particle–hole/shape isospectrality and its electromagnetic
consequences have an explicit 1975 precedent. The exact
130Ba(d,t)129Ba reaction was already used to constrain wavefunctions in 1998,
including comparisons with electromagnetic decays. A fixed removal channel
can distinguish the declared model's dual solutions because the duality
exchanges addition and removal. That is a conditional operator result, not a
new general spectroscopy principle or a validated shape determination.

## Primary-source locations

| Source | Verified location | Relevant finding |
|---|---|---|
| [Meyer-ter-Vehn I, NPA 249 (1975) 111–140](/workspace/wiki/raw/papers/1975_MeyerTerVehn_CollectiveOddANuclei_PartI.pdf) | Printed pp.113–115; Eqs.(2.1)–(2.14) | One complete j shell, one quasiparticle, fixed beta/gamma; spherical shell energy set to zero; phenomenological pairing/core; same rotor Hamiltonian in particle and hole sectors, Eq.(2.13). |
| Same | pp.116–117, Eqs.(2.18)–(2.22) | Gamma reflection requires particle–hole conjugation, Fermi-energy reflection, axis transformation and a pairing-phase convention. Eq.(2.19) explicitly changes Delta's sign; its sign does not affect the spectrum. |
| Same | pp.118–119, Eqs.(2.25)–(2.33) | BCS occupations and the discarded quasiparticle–quasihole coupling. The positive retained branch is the h*xi + E problem; eta is omitted in the numerical approximation. |
| Same | pp.119–121, Eqs.(2.34)–(2.51); p.133 | E2 reduced matrix elements reverse sign; M1 matrix elements do not. Spectroscopic Q and signed delta reverse, B(E2), B(M1), and magnetic moments remain unchanged. |
| Same | p.133, Table 2; pp.134–135, Fig.11 | The broader delta sign rule is a bounded numerical observation, not a general theorem. Changing the inertia prescription changes spectra; gamma and inertia cannot be inferred independently from a good energy fit. |
| [Meyer-ter-Vehn II, NPA 249 (1975) 141–165](/workspace/wiki/raw/papers/1975_MeyerTerVehn_CollectiveOddANuclei_PartII.pdf) | pp.142–144, §2 | Missing fluctuations, Coriolis attenuation, blocking and extra configurations; adjacent A−1/A+1 cores and shell information constrain the physical particle/hole interpretation. Lambda was partly adjusted to the first j−1 state. |
| Same | pp.156–157, §3.2.2 and Table 5 | 129,131La B(E2) comparisons constrain a restricted axial-versus-triaxial calculation, with neighboring-core strength calibration. These are neither 129Ba measurements nor a comparison of the full dual pair. |
| Same | pp.159–164, §4–5; Table 6 | Fitted rigid shapes are an approximation. Rejecting a completely gamma-independent limit does not establish a strictly rigid PES. |
| [Bucurescu et al., NPA 630 (1998) 643–660](/workspace/wiki/raw/papers/gpt/query/20261105-ba129-model-readiness/bucurescu1998-main.pdf) | pp.644–648; Table 1 | Direct precedent: 25-MeV polarized 130Ba(d,t)129Ba; DWBA/angular distributions/analyzing powers. Unknown target thickness prevents an absolute cross-section scale. |
| Same | p.651, §3.1 | Already compares pickup fragmentation with Nilsson C_j² v_j² and explicitly warns that Coriolis mixing can drastically change it. |
| Same | pp.652–655, §3.2, Tables 2–3 | Uses previously established IBFM wavefunctions with a mapped, boson-assisted transfer operator; pickup and gamma decay probe different wavefunction components. |
| Same | pp.657–659, §3.2.2 and conclusion | Negative-parity transfer includes h11/2, h9/2, f and p fragments. The strongest h11/2 fragment is the 279-keV 11/2− state; higher fragments and spin ambiguities must be retained. |

Part I has 30 pages, Part II 25. Their physical PDF pages equal printed
page minus 110 and minus 140, respectively. Bucurescu has 18 PDF pages,
with physical page = printed page minus 642. SHA-256 values are recorded
in `symmetry-checks.json`; both restored 1975 PDFs match the Wiki source
records. Existing source-card statements that the originals remain only in
tmp were not used as the availability verdict.

## Exact algebra and electromagnetic dependence

For the code's explicitly declared Q_j convention, use a proper pi/2
rotation about axis 1, D_j = exp(−i*pi*j_1/2). Direct matrix evaluation gives

    h_sp(60°−gamma) = −D_j h_sp(gamma) D_j†,
    U_dual = D_j V D_j†,  V_dual = D_j U D_j†,
    E_dual = D_j E D_j†,
    H_plus(dual) = W H_plus(original) W†,  W = D_I* ⊗ D_j,

when lambda changes sign and J2/J3 are exchanged. The positive gap is held
fixed in this gauge. This is a proof/check for the declared positive-energy
projection, not a claim to have diagonalized the full Nambu Hamiltonian.
The paper prints a cyclic axis relabelling in Eq.(2.19); the present signed
2/3 interchange is verified in the code convention rather than identified
with that printed tuple by name. Reflection about a nonzero shell reference
would require lambda' = 2*epsilon_0−lambda, not an arbitrary absolute-energy
sign change. Sorting inertias would destroy the required correspondence.

Under the original paper's matched operators and physical scales:

| Quantity between matched states | Exact dual behavior |
|---|---|
| Energies; E_gamma | Unchanged |
| B(E2), B(M1), their ratios, absolute magnitudes of transition moments | Unchanged |
| E2/M1-only decay rates and lifetimes, with matched branches/ICC | Unchanged, as a derived consequence of unchanged energies and strengths |
| Spectroscopic Q, signed E2/M1 mixing ratio delta | Opposite sign |
| Magnetic moment mu and g at the same I | Unchanged |

A lifetime holdout can test the model but cannot select between this exact
dual pair. Signed Q or phase-consistent E2/M1 interference can. A sign change
of an individual eigenvector changes both RMEs together and does not reverse
their ratio; therefore the dual delta reversal is not removable by state
rephasing. A measured polarization sign alone is not a measurement of delta's
sign.

The original E2 operator has a core term and a time-even single-particle
term; the latter has opposite particle/hole signs. The neutron bare charge
is zero in Eq.(2.36). Its magnetic operator is
g_R I + (g_j−g_R)j, with specified effective g factors. Consequently a
single-particle E2 coherence factor is uu−vv, whereas core E2 and
time-odd j use uu+vv.
[paired_single_j_em.py:24](/workspace/wiki/system/scripts/analysis/paired_single_j_em.py:24)
uses that distinction for its two implemented unit tensors, but supplies
neither calibrated Q0/g factors nor the full diagonal magnetic moment.
Effective neutron charges, additional orbitals or induced operators must be
transformed consistently before invoking the original invariance.

## Fixed-channel transfer check at the parent fit

The replay now reads every parameter digit from `best.model_parameters` in
the parent exact-fit record linked above, superseding the earlier audit's
rounded-context input. For display only, the parameters are
C=65.632863613 MeV, gamma=16.864401057°, lambda=−8.267968448 MeV,
J=(16.971317938,13.050682723,7.588657978), Delta=1 MeV.
The dual has gamma=43.135598943°, lambda=+8.267968448 MeV and
J=(16.971317938,7.588657978,13.050682723).
Across I=9/2 through 19/2, the full retained spectra agree within
5.0e−11 keV. Unit electromagnetic strengths agree to floating-point accuracy;
the phase-invariant E2–j interference product changes sign as required.

For the bare R0=0 operator, the R0 vector is invariant under W. Exchanging
U and V therefore gives, for corresponding states,

    S_minus,n(dual) = S_plus,n(original),
    S_plus,n(dual)  = S_minus,n(original),
    sum_n S_minus,n = Tr(V²),  sum_n S_plus,n = Tr(U²),
    Tr(V²) + Tr(U²) = 2j+1 = 12.

These are the full 36-state I=j sums, not sums over a hand-picked low-energy
band or probabilities normalized to one.
[paired_single_j_transfer.py:32](/workspace/wiki/system/scripts/analysis/paired_single_j_transfer.py:32)

| Bare result | Original | Dual |
|---|---:|---:|
| Complete removal sum | 4.039398 | 7.960602 |
| Complete addition sum | 7.960602 | 4.039398 |
| First 11/2-state removal strength | 0.462878 | 1.809016 |
| Fourth / first 11/2-state removal strength | 3.37137 | 0.0225783 |

The fourth state is 898.40 keV above the first 11/2 state. These labels are
model eigenvalue ranks, not assigned experimental states. The removal/addition
exchange holds within 3.5e−14. Relative fragmentation thus differs even after
an arbitrary overall normalization for this parameter pair. Such differences
are not guaranteed for every model point: the undeformed constant-U/V limit
has the same normalized R0 fragmentation in the two channels.

### Energy placement and finite windows

The **parent convention** fixes the lowest 11/2− model state at Ex=278.81 keV:

    Ex_parent(n) = E_n(11/2) − E_0(11/2) + 0.27881 MeV.

The **reviewer's alternative**, used in the earlier audit, fixed the lowest
9/2− model state at Ex=182.04 keV:

    Ex_review(n) = E_n(11/2) − E_0(9/2) + 0.18204 MeV.

The parent convention predicts the lowest 9/2− at 191.468786 keV.
Consequently Ex_parent − Ex_review = +9.428786 keV for every state in
this comparison. Fixing the alternative 9/2 placement is a reviewer-added
translation, not the parent's calibration or a new fitted anchor.

| Placement, evaluated with exact parent parameters | First 11/2 Ex (keV) | Fourth 11/2 Ex (keV) | States in 0 ≤ Ex < 2 MeV | Original / dual removal fraction |
|---|---:|---:|---:|---:|
| Parent: fixed 11/2− at 278.81 keV | 278.810000 | 1177.208665 | 6 | 56.926691% / 31.020397% |
| Reviewer alternative: fixed 9/2− at 182.04 keV | 269.381214 | 1167.779879 | 6 | 56.926691% / 31.020397% |

The window fractions happen to agree because both placements select the
same six eigenstates here. They are not interchangeable energy conventions;
a narrower window or a state near its edge can give different membership.
`symmetry-checks.json` records both formulas, origins, masks and per-state
energies separately under `transfer.windows` and `transfer.first_six_states`.

## Strongest counterarguments to a physical shape verdict

1. **The original papers already contain the symmetry and EM result.**
   Bucurescu already used this exact reaction, spectroscopic strengths and
   gamma decay to test wavefunctions. Its p.644 and Ref.[5], p.660, also cite
   Griffioen–Sheline, PRC 10 (1974) 624, as an earlier (d,t) study; that older
   paper was not reread here. The inspected precedents establish the broad
   method's age, without establishing who first tested this exact paired
   numerical dual. No novelty conclusion follows from search absence.

2. **The bare model cannot describe the complete pickup data.**
   A rank-j annihilation operator on a 0+ target reaches only I=j; bare
   h11/2 removal cannot populate 9/2− even if the final rotor has 9/2−
   eigenstates. Bucurescu Table 2 gives G(9/2−)=0.07 and
   G(11/2−)=1.33, a printed ratio 0.0526; this is not a mixing probability.
   Its nonzero value demands additional structure/reaction ingredients before
   a joint-channel fit. It does not by itself overturn an h11/2-dominated band
   interpretation. Ambiguous l=5 peaks cannot all be assumed to be 11/2−.

3. **The precedent's operator is not the new bare operator.**
   At p.652, the displayed expression is
   p_j† = zeta_j a_j† + sum_j' zeta_jj' [s† d_tilde a_j'†]^(j),
   with coefficients from a boson–fermion mapping and an odd neutron-hole
   representation. Creation of that effective fermion is not necessarily
   physical neutron addition. The paper uses multi-shell spaces and notes
   that remote orbitals can alter small transfer components while barely
   changing energies or gamma decay. A bare mismatch can therefore diagnose
   the operator/truncation rather than the wrong gamma branch.

4. **Absolute sum-rule discrimination is unavailable from the printed data.**
   Target-thickness uncertainty makes experimental G relative
   (pp.647–648). Table 1 sets the 1/2+ ground-state value to one; Table 2
   uses 7/2+; Fig.5 uses 11/2−. These are rescalings, not independent
   measurements. With the parent's fixed 11/2−, Ex=278.81-keV convention,
   the 0 ≤ Ex < 2-MeV window retains only 56.9% and 31.0% of the
   original/dual removal sums. The earlier reviewer-only 9/2 placement
   happens to select the same states, as separately documented above.
   The complete mathematical sum over all retained states cannot be imposed
   on this finite experimental window, particularly beyond the original
   one-quasiparticle validity range.

5. **Lambda is fitted, not number-constrained, and the physical channel must
   stay fixed.** The module solves neither number nor gap equations.
   Tr(V²)=4.039 or 7.961 is a conditional shell occupancy of its paired
   vacuum, not a measured 130Ba occupancy. Both hypotheses need the actual
   130Ba target, total neutron number, other-shell occupations and core
   constraints. Physical addition to 130Ba makes 131Ba; addition to form
   129Ba would start from 128Ba. The formal exchange is not a statement
   that (d,t) and (d,p) on the same target measure the same final nucleus.
   Transforming the state, vacuum and operator together gives a representation
   equivalence; comparing the same physical removal channel requires distinct
   structural hypotheses with their target definitions made explicit.

6. **The energy residual is much smaller than an untested discarded coupling.**
   Part I p.119 motivates neglect of h*eta using nearby single-particle
   levels and weak deformation. At the exact parent-fit point the single-particle
   shell spans 43.68 MeV. Reconstructing the discarded block
   P†(−U H_R V+V H_R U)P at I=11/2 gives a spectral norm of 1.095 MeV,
   and coupling norms of 0.73–1.01 MeV for the first six retained states.
   These are **not eigenvalue corrections or error bars**; they show that
   smallness at the 39.925-keV fit scale has not been demonstrated.
   Free C and three inertias also depart from the source's standard
   beta/mass/irrotational calibration. A low energy RMS does not validate
   the transfer amplitudes, effective shape, or the original approximation.

The defensible next use is a fixed-operator, fixed-target comparison of the
two energy-equivalent hypotheses against identified same-j relative pickup
fragments, with finite-window losses and state ambiguities explicit. A branch
preference should survive plausible core/induced-operator extensions and be
checked against signed EM information; otherwise retain it as a conditional
model sensitivity.

## Verification and limits

Reproduction:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B \
  outputs/l4/20261105-ba129-model-readiness/symmetry-review/symmetry_probe.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B -m unittest discover \
  -s system/tests -p test_paired_single_j_transfer.py -v
```

The five existing transfer tests passed in the initial audit.
`symmetry-checks.json` was regenerated from the exact parent-fit record and
records the input JSON path/hash/field locators, source/module hashes,
matrix/eigenvalue residuals, transfer sums, separately identified energy
placements/windows, unit-EM checks and discarded-block norms. The current
rotor hash matches the parent's recorded model hash; input hashes were
unchanged during the replay. No optimizer or fit was rerun.

Focused text reread: Part I PDF pp.2–12, 22–25; Part II pp.1–4, 16–24;
all 55 pages searched for symmetry/transfer terminology. Both 1975 papers
present particle/hole states and EM operators, but the inspected material
does not supply the present 130Ba pickup calculation. Bucurescu's 18-page
main text was read, with its transfer operator and Tables 1–2 visually checked.
Seven rendered source pages were moved, with identical SHA-256 hashes, to
[temporary source-page renders](/workspace/wiki/tmp/ba129-model-readiness/symmetry-review/pages).
The archived raw PDFs remain the canonical sources and were unchanged.
No publisher-page reproductions remain in this audit's publishable outputs.
The individual moves and verified hashes are recorded in
[publisher-page-move.json](/workspace/wiki/outputs/l4/20261105-ba129-model-readiness/symmetry-review/publisher-page-move.json).

| Temporary render | Original locator |
|---|---|
| [Part I, PDF 7](/workspace/wiki/tmp/ba129-model-readiness/symmetry-review/pages/mtv-I-pdf7.png) | Printed p.117, Eqs.(2.18)–(2.24) |
| [Part I, PDF 8](/workspace/wiki/tmp/ba129-model-readiness/symmetry-review/pages/mtv-I-pdf8.png) | Printed p.118, Eqs.(2.25)–(2.32) |
| [Part I, PDF 10](/workspace/wiki/tmp/ba129-model-readiness/symmetry-review/pages/mtv-I-pdf10.png) | Printed p.120, Eqs.(2.39)–(2.45) |
| [Part I, PDF 11](/workspace/wiki/tmp/ba129-model-readiness/symmetry-review/pages/mtv-I-pdf11.png) | Printed p.121, Eqs.(2.46)–(2.53) |
| [Bucurescu, PDF 5](/workspace/wiki/tmp/ba129-model-readiness/symmetry-review/pages/bu98-pdf5.png) | Printed p.647, Table 1 |
| [Bucurescu, PDF 10](/workspace/wiki/tmp/ba129-model-readiness/symmetry-review/pages/bu98-pdf10.png) | Printed p.652, §3.2 transfer operator |
| [Bucurescu, PDF 11](/workspace/wiki/tmp/ba129-model-readiness/symmetry-review/pages/bu98-pdf11.png) | Printed p.653, Table 2 and Fig.3 |

No new external full text was acquired; the earlier web requests returned
no usable evidence. This is not an exhaustive priority survey, full Nambu
refit, DWBA replay, calibrated transfer exclusion, or independent refit of
the parent's energy-calibration result.
