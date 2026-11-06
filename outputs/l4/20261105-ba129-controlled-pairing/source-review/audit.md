# Meyer–ter–Vehn qp/qh coupling: source consistency and state selection

2026-11-05. Read-only review of archived originals and the frozen
`8c9ad67e` checkpoint. New notes are confined to this directory. Publisher
renders and extracted text are confined to
`tmp/ba129-controlled-pairing/source-review/`. No frozen model, fit, PLAN,
installation, other session's artifact, or commit was changed.

**Decision:** the printed physical-particle/physical-hole labels must not be
identified with our positive/negative BCS blocks without qualification.
Their literal identification conflicts with the displayed positive
quasiparticle energies and the stipulated dual transformation. A
rank-preserving continuation of Hplus can define a mathematical reference
when its spectral subspace is isolated; it is not, by itself, a source-proven
physical one-quasiparticle prescription or validation of the full model.

## 1. What the primary sources actually state

| Primary locator | Directly verified statement |
|---|---|
| [Part I, printed p.113](/workspace/wiki/raw/papers/1975_MeyerTerVehn_CollectiveOddANuclei_PartI.pdf), introduction | One complete j shell, BCS treatment, and only one-quasiparticle configurations; applicability is restricted to low excitations below about 2 Delta. |
| Part I, pp.114–115, Eqs.(2.1), (2.6), (2.9), (2.11)–(2.13) | Bare particle/hole states use creation/time-reversed annihilation operators relative to an even reference. Their intrinsic energies are measured relative to lambda_F. The spherical shell energy is set to zero; a core expectation value is absorbed into lambda and an additive constant. The same HR acts in both Nambu sectors. |
| Part I, p.117, Eqs.(2.19)–(2.24) | Combined shape/axis/particle–hole transformation is a similarity of the total Hamiltonian. The intrinsic BCS transformation diagonalizes Hp into positive e_nu and negative −e_nu. |
| [Part I, p.118 image](/workspace/wiki/tmp/ba129-controlled-pairing/source-review/mtv-I-printed-118.png), Eqs.(2.25)–(2.32) | e_nu is the positive square root. Eq.(2.28) retains off-diagonal h*eta blocks; Eq.(2.30) drops them. Eq.(2.31) explicitly contains h*xi ± e_nu. The following sentence calls the minus-sign set rotor-plus-hole, while Eq.(2.32) asserts particle/shape–Fermi-reflected-hole isospectrality. All these printed statements are retained as evidence; none is silently corrected. |
| [Part I, p.119 image](/workspace/wiki/tmp/ba129-controlled-pairing/source-review/mtv-I-printed-119.png), Eqs.(2.33a,b) | Neglect of h*eta is motivated by small eta for nearby levels and small rotational couplings for widely separated levels, particularly at beta about 0.1–0.2. No uniform error bound or full-coupling physical-state-selection algorithm is supplied here. |
| Part I, pp.126,129–131, Figs.5–7 | Particle plots are mapped to hole cases by changing gamma/lambda; plots use energy differences from the basic j state. Same-spin near-crossings and different-spin crossings are discussed. These are not a prescription for selecting physical states from a coupled doubled matrix. |
| [Part II, pp.142–144](/workspace/wiki/raw/papers/1975_MeyerTerVehn_CollectiveOddANuclei_PartII.pdf), §§1–2 | Shape fluctuations, Coriolis attenuation, blocking, other j shells and higher quasiparticle configurations remain omitted. Physical particle/hole cases are connected to shell filling and neighboring A−1/A+1 cores. |
| [Part II, p.147 image](/workspace/wiki/tmp/ba129-controlled-pairing/source-review/mtv-II-printed-147.png), Fig.2 caption; pp.148–149 | Displayed spectra use energies relative to a basic state; this supplies a scalar plotting reference, not a sign change of the quasiparticle operator. |
| Part II, pp.159–164, §§4–5 | Fixed shape is an approximation; success is not a literal rigidity measurement. More quantitative dynamical treatment and experimental checks remain necessary. |

For Part I, PDF page = printed page −110; for Part II, −140.
The restored original SHA-256 values are
`10cb7aca223dcbccb17ee7aa224a7a1c13fb9f1e6e58a04fcdd8ab1e4b888da9`
and `fd1ba7f9280e8bafd86bbec06ec18e8a7089f93e84306829a4be897d9dd8439d`.
The source page supplied by the parent,
`tmp/ba129-controlled-pairing/source-pages/mtv118.png`, was also visually
checked without modification.

## 2. Resolving the sign/reference issue as far as the evidence permits

Use distinct notation:

- xi_nu = epsilon_nu − lambda_F: signed intrinsic single-particle energy;
- e_nu = sqrt(xi_nu² + Delta²) > 0: positive BCS energy;
- tau particle/hole: the original Nambu component labels of Eq.(2.9);
- +/− BCS sectors: the eigenspaces of Hp after Eq.(2.23);
- physical particle/hole character: shell filling and the even reference,
  not a synonym for the sign of e_nu or of a total eigenvalue.

In the stipulated custom convention, put

    A = U HR U + V HR V,       E = diag(e_nu) > 0,
    Hplus = A + E,            Hminus = A − E,
    K = −U HR V + V HR U.

The product-space expressions are reduced to the same D2 space where
appropriate. Under the declared shape/Fermi duality, with the axis rotation
represented by W,

    A' = W A W†,              E' = W E W†,
    Hplus' = W Hplus W†,      Hminus' = W Hminus W†,
    K' = −W K W†

in the positive-gap gauge. The last sign can also be changed by rephasing the
negative BCS sector. Thus the full-matrix similarity can be written with
diag(W,−W) in this gauge. It preserves each intrinsic Hp eigenvalue branch:
positive maps to positive. Exchanging bare Nambu components is a different
operation from exchanging the diagonalized +/− BCS branches.

Consequently

    Tr(Hplus) − Tr(Hminus') = 2 Tr(E) > 0.

Absolute Hplus/Hminus' isospectrality is impossible under these definitions.
The fixed frozen I=11/2 example gives a trace difference of **947.126215 MeV**,
equal to 2 Tr(E) at numerical precision.

**A plotting zero does not generally repair this.** Part II does subtract a
basic-state energy, so a trace test alone is not sufficient to reject every
interpretation involving excitation energies. However, ±E differ by a
scalar only in special cases such as E=e0*identity. For a generic BCS block
A=0, E=diag(1,2,4), the sorted excitation spectra after subtracting each
lowest eigenvalue are (0,1,3) and (0,2,3). For the frozen I=11/2 rotor, the
two sorted spectra still differ by **11.128601 MeV at maximum after each
centroid is subtracted**. No scalar offset can make those complete spectra
equal. Changing a state's sign or changing Delta's gauge cannot repair this
spectral difference. Reversing all hole energies instead would also change
the sign of A, and is not the same-core HR prescription printed in Eq.(2.13).

The physically consistent reading of the full similarity is that a
particle-like positive-Hp branch maps to a hole-like positive-Hp branch of
the reflected problem. For example, when lambda moves well above a shell,
v² approaches one and the **positive** BCS quasiparticle becomes hole-like.
This explains how physical particle–hole isospectrality can coexist with
positive-to-positive branch mapping.

**Source boundary:** this reading does not explain away the explicit
minus-sign sentence on p.118. With e_nu defined by the positive root,
the association of that minus sign with the physical hole in Eq.(2.32)
has an unresolved sign/label consistency problem. An internal printing or
terminological issue is possible; an unstated energy convention would need
to do more than add a constant. No original numerical code, author
clarification or verified erratum establishes which correction is intended.
Do not attribute our Hplus/Hminus interpretation or future full-block
implementation to a certified reproduction of the original calculation.

## 3. What retaining K actually computes

Let B = [[U,−V],[V,U]], with U and V commuting Hermitian functions of the
single-particle Hamiltonian and U²+V²=identity. Direct multiplication gives

    B† (HR*identity_Nambu + Hp) B
      = [[A+E, K], [K†, A−E]].

K†=−K for the displayed real-gap convention; replacing the lower block by K
instead of K† is generally non-Hermitian. Scaling the coupling by t defines
the proposed artificial homotopy, not a self-consistent gap solution or real
nuclear time evolution. It restores the term discarded in Eq.(2.30) within
this matrix model. It does not add the missing three-quasiparticle,
blocking, shape-fluctuation or multi-shell physics listed in Part II.

Positive inertias imply HR≥0 and hence A≥0. With Delta>0, E≥Delta*identity,
so Hplus≥Delta*identity before any display offset. **Hminus need not be
negative.** Negativity of the entire lower block would require E−A>0.
Moreover, HR enters with the same sign in both sectors, so the full matrix
does not generally have an E↔−E spectral symmetry at fixed parameters.
Do not import a generic fermionic BdG positive-eigenvalue filter or a bosonic
RPA norm-sign filter without deriving the appropriate physical construction.

In the frozen I=11/2 case, min(e_nu)=2.558409 MeV, but Hminus ranges from
−32.204138 to +2.427042 MeV and has six positive eigenvalues. The complete
72-dimensional matrix has **42 positive eigenvalues at t=0 and 41 at t=1**,
whereas the retained Hplus rank is 36. Adding 100 MeV times identity changes
the positive count to 72 without changing any eigenvector. Total-energy sign
therefore cannot define the retained reference.

## 4. What adiabatic continuation can legitimately define

Start separately in each fixed I/parity/exact-symmetry block, with the
declared rank-d projector P(0)=diag(identity_d,0). If the chosen d-dimensional
spectral subspace remains separated from its complement along the entire
path, it can be followed continuously. Internal degeneracies are handled as
projectors; a degeneracy with the discarded complement needs an extra exact
quantum label or an explicit unresolved-state boundary.

This gives an **Hplus-connected full-block reference under the declared
homotopy**. It avoids automatic doubling if only those d states are counted.
It is not sufficient evidence that they constitute the physical
one-quasiparticle space of a particular odd nucleus: the paired vacuum,
particle number, even-core identity, physical inner product/state
construction and observable operators still have to be specified.

There is a useful rigorous sufficient condition. If

    b = max spec(Hminus) < a = min spec(Hplus),

principal-submatrix interlacing gives, for the 2d sorted full eigenvalues,

    lambda_d(H(t)) ≤ b < a ≤ lambda_(d+1)(H(t))

for every t, regardless of K's norm. The upper d states are then the
Hplus-connected reference, with a gap of at least a−b. This is a statement
about the declared matrices and does not depend on the arbitrary zero.

Static checks of the frozen parent parameters give:

| I | Hplus rank d | min(Hplus)−max(Hminus), MeV | Minimum discrete +/− distance at t=0, MeV |
|---|---:|---:|---:|
| 9/2 | 30 | +2.842170 | 2.842170 |
| 11/2 | 36 | +1.569364 | 1.569364 |
| 13/2 | 42 | +1.318890 | 1.318890 |
| 15/2 | 48 | −0.270334 | 0.096242 |
| 17/2 | 54 | −0.522582 | 0.107247 |
| 19/2 | 60 | −2.424761 | 0.006849 |

Thus the ordered-gap theorem applies at the first three spins for this
fixed point. At higher spins the spectra interleave: selecting the upper d
already substitutes some lower-block states at t=0. The positive discrete
distance means continuation is locally definable there, but it does not
establish separation along the complete path or throughout a fit domain.
No full continuation was performed in this source audit.

At avoided crossings, energy-continuous eigenstates can exchange their
initial character. “Most Hplus-like at each t” is a different, diabatic
selection and can jump discontinuously. Use complete overlap matrices and
cluster projectors, adaptive t steps, reverse tracking, and exact symmetry
labels; do not silently switch rules to improve a fit. Different-I
crossings do not mix states and should not be confused with same-block
selection failures.

## 5. Gap assumptions and perturbative checks

Equation (2.33) supplies a heuristic for small h*eta, not a proof that
Delta>0 controls all rotational mixing. With u=cos(theta), v=sin(theta),
eta_mu,nu=sin(theta_nu−theta_mu) and

    |d theta / d epsilon| = Delta / [2((epsilon−lambda)²+Delta²)]
                          ≤ 1/(2 Delta).

Therefore |epsilon_mu−epsilon_nu| much smaller than 2 Delta gives a small
eta bound; merely being below 2 Delta does not ensure a small number.
Finite-distance Fermi energies outside the shell approach, rather than
mathematically enforce, constant U/V unless an additional limiting
approximation is adopted.

For an isolated nondegenerate Hplus state with energy z_a, the leading shift
is

    Delta z_a(t) =
      t² sum_b |<a|K|b_minus>|² / (z_a−z_b_minus) + O(t⁴).

The relevant denominators are cross-sector **total** energies, not simply
2 Delta. The shift is positive when every minus state is below z_a;
interleaved spectra permit either sign. After subtracting an anchor, an
excitation-energy shift is the difference of two such shifts. Retaining K
does not automatically compress spectra or improve the energy fit.

Exact elimination, where the resolvent exists, gives

    Heff(z) = Hplus + t² K (z−Hminus)^−1 K†,
    y = t (z−Hminus)^−1 K† x,
    1 = x†[identity + t² K(z−Hminus)^−2 K†]x.

This explains why a coupling norm alone is not an energy error, and why
normalizing x alone or reusing projected operators after mixing is unsafe.
Near a resolvent pole, use the full system/cluster treatment; do not clip
denominators into a purported controlled correction.

## 6. Negative controls required before fitting

| Control | Required result or failure boundary |
|---|---|
| Printed-sign and energy-reference audit | Preserve e_nu>0 and distinguish physical hole from −BCS. Verify +↔+ and −↔− covariance. An asserted +↔− similarity must fail the trace/shift-invariant checks above. |
| Full reconstruction | Check B†B=identity, K†=−K, Hermiticity, D2 closure, and equality of the transformed original matrix and the assembled full blocks for every tested I. The frozen Hplus reconstruction here agrees within 7.2e−15 MeV. |
| Exact zero coupling | HR=0 or commuting U,V,HR must give K=0 and exactly recover the declared Hplus reference, with no additional physical levels. The A=diag(0,3), E=identity example has three positive total eigenvalues but a retained rank of two. |
| Finite-gap but initial degeneracy | A structured example with Delta=1, xi=(1,−1), HR=[[3,2],[2,3]] has Hplus=(3,5.828427) and Hminus=(0.171573,3). For arbitrarily small nonzero t, the two states near 3 MeV are 50/50 mixtures; there is no unique pure-plus eigenbranch limit. Mark this unresolved instead of choosing a numerical tie-break. |
| Zero/gap limits | Delta→0 with a Fermi crossing needs a separately defined occupation limit. Distinguish BCS gap, ordered block gap and instantaneous selected/complement gaps. Large separation is a convergence control, not a replacement for the actual denominators. |
| Shift, gauge and tracking controls | H+c*identity must leave the selected projector and transitions unchanged. t and −t have the same spectrum. Rephasing and negative-sector unitary rotations must not alter observables. Refine and reverse the t path; track projectors near degeneracies, not raw eigenvector signs. |
| Perturbative response | Where isolated, verify zero first derivative at t=0 and the t² coefficient above; report selected/complement weights and denominator-dependent mixing. Test a deliberately near-resonant failure case. |
| State count and physical identity | Keep d states only when the declared continuation is well defined; no “all positive,” “lowest d,” “upper d everywhere,” or independent re-zeroing of both blocks. State the reference vacuum, particle number, core and physical addition/removal channel. |
| Full operators and normalization | Use the full mixed vector and transformed EM/transfer operators, including cross-sector terms. The frozen positive-energy embedding alone is insufficient. Recover the old operators at t=0. |
| Transfer closure/doubling | For a full orthonormal 2d basis, bare particle and hole source norms separately close to 2j+1; summing both gives 2(2j+1). Counting that as the old one-quasiparticle strength sum is doubling. For a selected projector P(t), derive the sums as f†P(t)f; the old Tr(U²),Tr(V²) values are not automatic after mixing. |
| Independent physical checks | Test number/occupation/core consistency and withheld EM/transfer observables only after the state contract is fixed. Restoring K does not remove the original below-2Delta, one-j and fixed-shape restrictions or prove a global fit optimum. |

The two structured algebraic counterexamples and frozen numerical checks
are recorded in [static-controls.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/source-review/static-controls.json).
They are not measurements, a fit, or selected physical full-coupling spectra.

## 7. Readiness statement and provenance

The source supports retaining the off-diagonal block as a well-defined
extension of its displayed Nambu matrix. It does **not** supply a validated
adiabatic physical-state selection rule for that extension. The proposed
continuation is suitable as a controlled numerical reference only after
gap/identity/operator checks; physical one-quasiparticle interpretation
remains conditional. The p.118 minus-sign/physical-hole association is an
explicit unresolved source issue, not an implementation instruction.

The numerical checks read the model and exact parent parameter JSON directly
from Git commit `8c9ad67e`, executing the model in memory with bytecode writes
disabled. They did not import or edit a developing full-Nambu implementation.
The model SHA-256 is
`1d9dd8814892556e7731b41dd2edd98ab83951fca168711fcb5951f8ca647908`;
the exact parent-fit blob SHA-256 is
`3365fe1b6f3dc6eaa990b7ec6e62e1ef1e4dcd91196c0c22e3fc5706f8a3799d`.
No RMS was independently refitted.

Focused reread: Part I pp.113–119 and 125–131; Part II pp.141–149 and the
validity discussion pp.159–164, with the latter also checked in the preceding
source review. Full PDFs were searched for energy-reference and qp/qh terms.
Thirteen selected pages and text extractions are stored exclusively in
`tmp/ba129-controlled-pairing/source-review/`, with `page-locators.json`.
Online lookup returned no usable additional evidence; no erratum or
original producer code was verified.
