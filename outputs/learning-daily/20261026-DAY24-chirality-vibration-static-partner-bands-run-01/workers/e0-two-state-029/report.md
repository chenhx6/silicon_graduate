# Same-Iπ two-state E0 kernel: a conditional extension of HW11 Eq14

This is a bounded extension of the already recorded off-diagonal-E0 caveat, not a new theorem or a new paper/data fit. All new formulae below are conditional task algebra, `needs_review:true`. It remains Day25 uncredited preview inside Day24;029 is a worker number, not a course day. Day26 is not opened. No canonical/raw/Git or course-state writes.

Direct source check: HW11 actual55-page PDF, SHA256 `660c376e493e638501bfc8596d4eda46f490becb811ba5f30259d6f78c652183`, native text and fresh visual PDF13/printed1479 Eq14 and surrounding paragraph. The relevant prior source remark is HW11-D25P-003/006 and its following two-config discussion. No full-review reread, new isotope calculation, actualβ/γ or186Pb mixing percentage is inferred.

## Same space, one unitary transformation

Choose two orthonormal **configurations of the same Iπ**, with a specified physical/model meaning. Define the normalized scalar charge-radius operator by

\[
T=\begin{pmatrix}R_1&t\\t^*&R_2\end{pmatrix},\qquad
R_k=\langle r^2\rangle_k,\quad\Delta=R_1-R_2.
\]

All T entries have length² units. In HW11's normalization, the E0 charge amplitude is eZ times the off-diagonal element of this radius operator andρ²(E0)=Z² abs(A)²/R0⁴. This definition avoids silently substituting an E2 reduced matrix element or a differently normalized scalar RME.

Both bra and ket spaces are the **same two-state Hilbert space**, so the energy-state representation is T_E=U†TU and remains Hermitian. This differs from022's forward E2 block between distinct Ii andIf spaces, where M=Rf†Q Ri has two generally different transformations and is not automatically symmetric/Hermitian. Hermiticity of the physical E2 operator constrains the reverse-spin block; it does not impose equality of two distinct forward off-diagonal transitions.

Write the two-state Hamiltonian in this defined configuration basis as

\[
H=\begin{pmatrix}E_1&W e^{i\phi}\\W e^{-i\phi}&E_2\end{pmatrix},\quad
W=|V|,\quad\delta=E_2-E_1,\quad D=\sqrt{\delta^2+4W^2}>0.
\]

Letη=sin²θ=(1−δ/D)/2, c=cosθ,s=sinθ, withθ∈[0,π/2]. A consistent lower/upper eigenstate convention is

\[
U=\begin{pmatrix}c&s\\-e^{-i\phi}s&e^{-i\phi}c\end{pmatrix},\qquad
cs=W/D,\quad c^2-s^2=\delta/D.
\]

η here labels a specified configuration probability of the lower eigenstate. It is not independently observed by the energy gap alone. The HW11 producta²(1−a²) is unchanged by exchangingη with1−η.

## General E0 amplitude and diagonal radii

Put z=t e^(−iφ)=x+iy, using the same phase convention that makes H's off-diagonal element real. Direct multiplication gives

\[
A=(T_E)_{lu}=cs\Delta+(c^2-s^2)x+i y
=\frac{W\Delta+\delta x}{D}+iy,
\]
\[
R_l=(1-\eta)R_1+\eta R_2-2\sqrt{\eta(1-\eta)}x,
\]
\[
R_u=\eta R_1+(1-\eta)R_2+2\sqrt{\eta(1-\eta)}x.
\]

Consequently

\[
\rho^2(E0)=\frac{Z^2}{R_0^4}
\left[\frac{(W\Delta+\delta x)^2}{D^2}+y^2\right],
\qquad
d\equiv R_l-R_u=\frac{\delta\Delta-4Wx}{D}.
\]

The trace and the spectral spread of the radius block obey

\[
R_l+R_u=R_1+R_2,\qquad
d^2+4|A|^2=\Delta^2+4|t|^2.
\]

The latter is a useful radius/E0 consistency relation within the closed two-state block. It is not a β/γ inversion or a proof that the eigenvectors ofT represent two rigid intrinsic shapes. Length² quantities squared have length⁴ units; the factorZ²/R0⁴ makesρ² dimensionless. HamiltonianW,δ,D are energies, so all terms inA andd have length² units.

With t0 this reduces to HW11 Eq14:

\[
|A|^2=\eta(1-\eta)\Delta^2=\frac{W^2}{D^2}\Delta^2.
\]

Thus the compact Eq14 expression implicitly requires a diagonal radius operator in the **same configuration basis used to define the mixing amplitudes**. Calling the states “two configurations” alone does not eliminate an arbitrary off-diagonal scalar matrix element. A new fit with t≠0 cannot reuse old extractedη/Δ/V as independent measurements without their original assumptions.

## Small E0 and necessary limits

Forδ≠0, a real aligned off-diagonal term can cancel the mixing-induced part: x=−WΔ/δ andy0 givesA0 even ifW andΔ are nonzero. For example, using arbitrary illustrative units, δ=1/√2MeV,W=1/(2√2)MeV,R1=10fm²,R2=12fm²,t=1fm² givesD=1MeV,A0 and radiiR_l=9.585786fm²,R_u=12.414214fm². T is positive definite. This is not a nucleus, fit or assignment of a mixing percentage to186Pb.

The cancellation is not universal. Atδ0,W>0,η1/2 andA=Δ/2+iy: the real part of t changes the diagonal radii but cannot cancel a nonzeroΔ in the E0 amplitude. A nonzero relative-imaginary componenty also supplies a residual|A|²≥y² in this defined configuration convention. AtW0 with nondegenerateH, the eigenstates can coincide with the configurations andA=t: E0 need not vanish when the energy Hamiltonian has no mixing if the operator is not diagonal. AtD0 the degenerate Hamiltonian does not select a uniqueθ; the formulas using1/D cannot define a measured mixing angle there.

An independent invariant statement is

\[
\|[H,T]\|_F^2=2D^2|A|^2.
\]

For nondegenerateH, A0 means H andT commute within this block. Hence a small E0 amplitude can indicate near-commutation, not uniquely small configuration mixing or small configuration-radius difference. This is conditional two-state operator algebra, not a new empirical signature.

## Phases, reconstruction and what “unmixed” means

Rephasing the two defined configuration states changes H12 andt by the same phase factor; z=tV*/W is invariant under that restricted phase convention whenW≠0. It is **not** invariant under an arbitrary mixing/redefinition of the two configuration states. Such a redefinition transforms H andT together and changes the numericalW,δ,η,R1,R2,t while preserving the physical energy-state observables.

In the nondegenerate energy basis, H is diagonal and one remaining relative eigenstate phase can make its single off-diagonal T element real. Therefore the standalone sign/phase of this one Hermitian E0 transition is not a four-edge gauge-invariant loop like026. Its magnitude and the two diagonal radii determineT up to that residual state convention. Full phase-consistent operator information must not be confused with an independently measured absolute sign.

Even complete energy-basis H andT do not by themselves select unique **unmixed configurations**. Choosing any specified U gives H_C=U H_E U† andT_C=U T_E U†. To interpret their diagonal entries as particular configurations/shapes requires an additional physical definition or model constraint on that basis. IfU is independently fixed, reconstruction is well-defined up to consistent state phases. Alternatively one may diagonalizeT mathematically and write an Eq14-type formula in that radius-eigenbasis, but those radius eigenvectors are not automatically the original intruder/normal configurations or physical shape minima. A simultaneous basis change is not a new physical shape-coexistence solution.

## Reproducible scope and stop

`e0_kernel_check.py` directly compares U†HU andU†TU with the continuous formulas, checks Hermiticity/unitarity, trace/determinant/spread and commutator identities, and evaluates the diagonal-kernel, cancellation, exact-crossing and zero-Hmixing limits. Output:`e0-kernel-results.json`. No Z/R0 or actual nuclearE0 strength was assigned; no data/percent fit or statistical interval was produced, and no check count is used as scientific certification.

The useful increment beyond the source's existing caveat is the explicit coherent t term, its relation to both mixed radii, and the nonuniversal cancellation limit. Additional arbitrary scans would not identify an actual configuration basis or missing experimental matrix elements, so this bounded component stops here.
