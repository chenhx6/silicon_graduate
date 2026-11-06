**Fixed intrinsic charge geometry fixes the complete moments independently of
the particle-rotor eigenstate. A restriction to one intermediate-spin sector
does not inherit that identity.** This is a mathematical control using standard
angular-momentum algebra, not a new theorem or a physical Ba assignment.

The model and numerical design were fixed in [protocol.json](protocol.json)
before results. The unpaired Hamiltonian is assembled directly as

\[
H(C)=\sum_{k=1}^3\frac{R_k^2}{2\mathcal J_k}
       +C\,1_I\otimes Q_j(\gamma),\qquad
R_k=I_{k,\mathrm{right}}\otimes1-1\otimes j_k .
\]

The right-body representation is
\(I_{\rm right}=(J_x,-J_y,J_z)\), so
\([I_1,I_2]=-iI_3\); the particle has ordinary commutators.
Consequently \([R_1,R_2]=-iR_3\). The three axes remain in their supplied order.
The dimensionless field is explicitly

\[
Q_j(\gamma)=
\frac{\cos\gamma[3j_z^2-j(j+1)1]
+\sqrt3\sin\gamma(j_x^2-j_y^2)}{4j(j+1)} .
\]

It is distinct from the core-only charge operator. Its normalization is the
local helper's declared convention, not a fitted nuclear single-particle field.
The code uses \(P_I^\dagger H P_I\) in the bare physical D2 subspace and
diagonalizes that entire block. It never uses a paired solution, positive-energy
embedding, zero-gap limit or Nambu projection.

For fixed \(\mathcal Q=1\), write the intrinsic charge tensor as

\[
a_0=\cos\gamma,\qquad
a_{\pm2}=\frac{\sin\gamma}{\sqrt2},\qquad a_{\pm1}=0,
\qquad
Q_{2\mu}(\Omega)=\sum_\nu D^{2*}_{\mu\nu}(\Omega)a_\nu\,1_j.
\]

These are multiplication operators on rotor orientation. Rotational
orthogonality gives the pointwise scalar identity

\[
Q\cdot Q=\sum_\nu |a_\nu|^2\,1
=\bigl(\cos^2\gamma+\sin^2\gamma\bigr)1=1 .
\]

The cubic sign and normalization can be checked without the reduced-RME code.
Associate the intrinsic tensor with a real traceless Cartesian matrix whose
principal values, in the same axis order, are

\[
\lambda_x=-\frac{\cos\gamma}{\sqrt6}+\frac{\sin\gamma}{\sqrt2},
\quad
\lambda_y=-\frac{\cos\gamma}{\sqrt6}-\frac{\sin\gamma}{\sqrt2},
\quad
\lambda_z=\sqrt{\frac23}\cos\gamma .
\]

Then \(\operatorname{tr}A^2=1\) and

\[
\sqrt6\,\operatorname{tr}A^3
=\cos^3\gamma-3\cos\gamma\sin^2\gamma
=\cos3\gamma .
\]

With the specified Condon–Shortley tensor convention, the same cubic is
\(-\sqrt{7/2}[Q\times Q]^{(2)}\cdot Q\).
At the axial normalization check \(a_0=1\),
\(\langle20,20|20\rangle=-\sqrt{2/7}\), fixing the positive cubic sign.
Thus, for every normalized state of this rigid-charge model,

\[
q_2=1,\qquad q_3=\cos3\gamma .
\]

At the frozen \(\gamma=20^\circ\), these are \(1\) and \(1/2\), so the complete
rigid-equivalent angle is exactly \(20^\circ\). Changing \(C\) changes the
eigenvectors and angular correlations; it does not change these geometric
identities, the charge amplitude or the inertia tensor.

The normalized product basis and RME convention used for the numerical
calculation are

\[
\Phi_{IMK,\Omega}=
\sqrt{\frac{2I+1}{8\pi^2}}D^{I*}_{MK}|j,\Omega\rangle ,
\qquad
\langle I_fM_f|Q_{2\mu}|I_iM_i\rangle
=\frac{\langle I_iM_i,2\mu|I_fM_f\rangle}{\sqrt{2I_f+1}}R_{fi},
\]

\[
(T_{\rm product})_{K_f\Omega_f,K_i\Omega_i}
=\sqrt{2I_i+1}\sum_\nu
\langle I_iK_i,2\nu|I_fK_f\rangle
a_\nu\delta_{\Omega_f\Omega_i},
\qquad
R_{fi}=V_f^\dagger P_f^\dagger T_{\rm product}P_iV_i .
\]

The bare D2 columns combine
\((|K,\Omega\rangle+(-1)^{I-j}|-K,-\Omega\rangle)/\sqrt2\), with the
specified signature representatives. An independent group-projector check
uses \(G=[1+\exp(-i\pi R_1)+\exp(-i\pi R_2)+\exp(-i\pi R_3)]/4\) and verifies
\(G=P_IP_I^\dagger\). This checks the physical subspace separately from merely
checking \(P_I^\dagger P_I=1\).

At each fixed \(I\), all physical D2 states are retained. The registry includes
\(I=1/2,\ldots,15/2\), totaling 216 whole multiplets and 2448 magnetic states.
For an initial \(I=11/2\), a rank-2 tensor connects only
\(I_a=7/2,\ldots,15/2\). Both intermediate states in a closed cubic loop are
also connected to the initial state, so both lie in that same interval.
All their eigenstates and middle RMEs are present. Therefore the finite
registry gives exact infinite-rotor \(q_2,q_3\) for this initial spin even though
it is not globally complete for the infinite rotor.

The numerical direct calculation constructs all five lab components in the
whole-magnetic-state window using Wigner–Eckart, then contracts them without
6j coefficients. It verifies \(Q\cdot Q=1\) and the cubic \(=\tfrac12\,1\)
as **36-by-36 matrices on the entire initial \(I=11/2,M=1/2\) D2 subspace**,
before selecting any Hamiltonian eigenstate. Their maximum matrix residuals
are both \(5.56\times10^{-16}\). The independent Euler-angle integral validates
the underlying product lab elements: alpha/gamma Fourier selection is exact,
while beta is integrated at 24 and 48 Gauss–Legendre nodes using exponentials
of a separately constructed \(J_y\). No CG appears in that integral.
Its maximum disagreement with the product-RME/Wigner–Eckart route is
\(2.74\times10^{-14}\).

The boundary qualification has an explicit negative check. For initial
\(I=15/2\), the same projected window omits the required \(17/2,19/2\) outer
channels. Its mean quadratic expectation over the D2 coordinate basis is
0.525, not 1. The `complete=True` flag in the numerical reduced table refers
only to the declared projected window; it never asserts global completeness
of the infinite rotor.

The unpaired \(C=0\) spectator limit checks the Hamiltonian convention
independently of charge closure. At \(I=j\),

\[
|R=0\rangle=\frac1{\sqrt{2j+1}}\sum_K|K,\Omega=K\rangle .
\]

Every \(R_k\) annihilates this vector with the stated right-body convention.
It lies in the physical D2 space, has zero rotational energy, and its
spectroscopic quadrupole moment is zero. Reversing the body \(I_y\) sign
incorrectly raises this same analytic vector's energy to 1.442081489 MeV;
this is a deliberately wrong-sign diagnostic, not an alternative production
Hamiltonian.

The spectator charge tensor excites core \(R=0\) only to \(R=2\). Summing the
two physical core \(R=2\) states gives, for each final total spin,

\[
q_2(I_f)=\frac{2I_f+1}{5(2j+1)}
=\frac{2I_f+1}{60},
\qquad I_f=7/2,9/2,11/2,13/2,15/2.
\]

The two core eigenenergies are independently obtained by projecting a
five-dimensional integer \(R=2\) rotor onto its D2-invariant subspace:
0.1267949192 and 0.4732050808 MeV. They also follow from

\[
E_{2,\pm}=2(A_1+A_2+A_3)
\pm2\sqrt{A_1^2+A_2^2+A_3^2-A_1A_2-A_2A_3-A_3A_1},
\qquad A_k=\frac1{2\mathcal J_k}.
\]

All ten E2-carrying spectator levels across the five final spins occur at
those two energies. The five spin fractions agree with the analytic rule to
\(5.83\times10^{-16}\). Deliberately omitting the \(15/2\) outer sector leaves
only \(11/15=0.7333333333\) of the quadratic closure, visibly failing the
geometric identity.

Finally, define the restricted contraction, for selected \(I+2\) states,

\[
S=\sum_a|R_{ai}|^2,\qquad
C_{\rm chain}=\sum_{ab}R_{ai}^{*}R_{ab}R_{bi},\qquad
z_{\rm proxy}=\sqrt{\frac7{10}}\frac{|C_{\rm chain}|}{S^{3/2}} .
\]

It remains a rotational scalar: the restrictions select whole multiplets.
However, it keeps one spin sector and an unweighted chain, whereas the
complete cubic includes all allowed spin sectors with their signed 6j
weights. No geometric multiplication identity fixes this restricted ratio
or guarantees its arccos domain. Consistent complex rephasing of all
multiplets leaves the complete and restricted contractions unchanged;
the numerical control checks this separately.

The read-only implementation lineage is
`system/scripts/analysis/paired_single_j_rotor.py`, L199–222 and L234–252
(pure spin, single-j field and D2 embedding);
`system/scripts/analysis/paired_single_j_em.py`, L5–15, L127 and L235–249
(basis/CG/product-RME convention); and
`system/scripts/analysis/quadrupole_scalar_invariants.py`, L18–27,
L296–331 and L395–498 (signed closure, direct tensor and proxy contractions).
Their hashes are pinned in the protocol. The proof and controls above state
the independent geometric, group-theoretic, integral and spectator checks;
agreement between reused routines alone is not the verification argument.
