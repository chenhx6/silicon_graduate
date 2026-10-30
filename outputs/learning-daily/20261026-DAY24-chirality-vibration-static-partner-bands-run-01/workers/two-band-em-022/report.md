# Two-band coherent E2 kernel: what an extra off-diagonal element changes

This is a bounded mathematical extension of PE06's specified two-band space, during the uncredited Day25 preview inside Day24. It does not fit the branching data again, assign a Q confidence interval, change the energy Hamiltonian or establish a competing geometry. All new derivations are conditional, `needs_review: true`. Day26 remains closed; no canonical/raw/Git or course-state writes were made.

Primary checked: Petrache et al., PRL96,112502(2006), local SHA256 `ec32a76efbeebf1a924a1c95eb9d404a99158fc9226605414b324e982cfe1d4f`. Source PDF2/printed112502-2 gives Eqs1–2 and the explicit assumptions of no off-diagonal E2 and short-segment constant interaction. PDF3/112502-3 gives Eqs3–5/TableI; it was freshly viewed. This unit uses no new paper, no prior114 producer and no experimental events.

## Basis, amplitudes and units

Let original band states be columns in the fixed order(1,2), and observed states in the order(y,ny). Source Eqs1–2 are

\[
|y_I\rangle=a_I|1_I\rangle+b_I|2_I\rangle,\qquad
|ny_I\rangle=b_I|1_I\rangle-a_I|2_I\rangle,
\quad b_I=\sqrt{1-a_I^2}.
\]

Thus

\[
R_I=\begin{pmatrix}a_I&b_I\\b_I&-a_I\end{pmatrix},
\qquad R_I^TR_I=1,\qquad\det R_I=-1.
\]

The alpha printed on a `ny` row of TableI still means the original-band1 amplitude in **Eq1's yrast state**; it is not replaced by its complementary amplitude just because of the row label. Use a15=.894,a17=.118,a16=.427,a18=.099 exactly as the source's rounded forward baseline.

For a transition i=I→f=I−2, extend the source's diagonal transition kernel to

\[
Q_{fi}=\begin{pmatrix}q_1&q_{12}\\q_{12}&q_2\end{pmatrix},
\qquad M_{fi}=R_f^TQ_{fi}R_i.
\]

All q and M entries have the same E2-amplitude/transition-moment unit. The script expresses them in an arbitrary common Qref, taking q2=1 only as a normalization; it does not choose a physical eb scale. With a common source-style geometric normalization, B(E2) is a common positive factor times abs(M)^2, so same-parent ratios remove that factor and the parent's lifetime.

The real equality Q12=Q21 is an **additional one-parameter ansatz for this extension**. Hermiticity of the physical E2 operator relates a forward-spin reduced matrix element to its reverse-spin counterpart; by itself it does not force the two different off-diagonal forward transitions1_i→2_f and2_i→1_f to be equal. A fully general forward real2×2 kernel would permit two off-diagonal entries and would require still more input. This task follows the requested symmetric q12 extension only.

## General coherent matrix

Rows are(y_f,ny_f), columns(y_i,ny_i). Writing ai,bi,af,bf for the corresponding real amplitudes gives

\[
\begin{aligned}
M_{yy}&=q_1a_fa_i+q_{12}(a_fb_i+b_fa_i)+q_2b_fb_i,\\
M_{y,ny}&=q_1a_fb_i+q_{12}(b_fb_i-a_fa_i)-q_2b_fa_i,\\
M_{ny,y}&=q_1b_fa_i+q_{12}(b_fb_i-a_fa_i)-q_2a_fb_i,\\
M_{ny,ny}&=q_1b_fb_i-q_{12}(b_fa_i+a_fb_i)+q_2a_fa_i.
\end{aligned}
\]

The linear q12 terms interfere coherently with the diagonal terms. They cannot be inserted as an incoherent extra positive width. A zero denominator can make a particular ratio diverge even while the full finite transition matrix is regular; no physical threshold or new configuration follows from that ratio pole.

For q12=0, Eq4 is abs(M_y,ny/M_ny,ny)^2 and Eq5 is abs(M_ny,y/M_yy)^2. Those are defined by **energy-order y/ny endpoints**, not automatically the source's original-band-continuity out/in labels.

## Actual TableI label contract

At17, the yrast state is predominantly original2 because a17 is small; at15 the yrast state is predominantly original1 because a15 is large. Original-band continuity therefore swaps which final energy-order state is “in.” At18 and16 both yrast amplitudes are small and that swap is absent.

|Source parent|Table out Eγ / in Eγ,keV|Out / in in observed endpoint notation|Matrix ratio|
|---|---|---|---|
|17ny|991 /1027|ny15 /y15|abs(M_ny,ny/M_y,ny)^2 = inverse Eq4|
|17y|909 /873|y15 /ny15|abs(M_yy/M_ny,y)^2 = inverse Eq5|
|18ny|1113 /1069|y16 /ny16|abs(M_y,ny/M_ny,ny)^2 = Eq4|
|18y|896 /940|ny16 /y16|abs(M_ny,y/M_yy)^2 = Eq5|

The original row-specific photon energies, y/ny labels and spin pair must travel with each ratio. Reciprocating a ratio is a label operation, not new physics; it remains required when q12 is nonzero.

Using only q1/q2=2,q12=0 and the printed alpha values gives the source forward baseline:

|Transition|Calculated Table-continuity out/in,ny theny|Source printed calculation|
|---|---|---|
|17→15|.333870180,.703521726|.33,.70|
|18→16|.170381787,.062384067|.17,.062|

This checks transcription, coherence and labels only. Source experimental values are.3(.1),.6(.1),.22(.09),<.08; the last is an upper limit, not a central value. No error distribution, likelihood or new fit is inferred from their proximity to the forward numbers. Source2.0(4) remains its diagonal-kernel allowed range result, not a new Gaussian Q measurement.

## What survives, and what does not

Same-parent lifetime cancellation, a common overall kernel scale, and explicit endpoint-label reciprocation survive q12. Consistent intrinsic rephasing also leaves physical M unchanged: for S=diag(1,−1), transform Q→SQS and R_i,f→SR_i,f together. Changing only the sign of q12 while freezing all mixing conventions instead changes an interference term; those two operations must not be confused.

For a **fixed** Q, orthogonal changes between intrinsic and observed bases preserve

\[
\|M\|_F^2=q_1^2+q_2^2+2q_{12}^2,\qquad
\det M=q_1q_2-q_{12}^2,
\qquad \sigma_k(M)=\sigma_k(Q).
\]

The determinant sign is written in the selected source phase convention; det² and singular values are insensitive to observed-state sign flips. These are invariants under basis mixing, **not invariants under changing q12**. The trace of M is generally not invariant because initial and final mixing matrices differ. Only when Rf=Ri does the transformation become a similarity and trace(M)=trace(Q); otherwise a signed known Rf/Ri is needed to reconstruct the kernel before using its trace.

The source's Eq4/Eq5 equality shortcuts require the diagonal kernel. In that case q1=q2 or ai=0 makes those two raw energy-order ratios equal. With q12≠0 neither implication is universal. As a conditional illustration, q1=q2=1,q12=.3 gives Table-continuity ratios(.082004,1.290102) for17→15 and(.565982,.005077) for18→16. These are **not fits to TableI**. They merely show that unequal observed ratios no longer logically force unequal diagonal q1/q2 when the off-diagonal transition kernel is allowed. They do not show that an equal-diagonal alternative describes the actual data, lifetimes or energy spectrum.

SVD determines the eigenvalue magnitudes of a real symmetric Q, not its individual diagonal entries unless its orientation/off-diagonal structure is also specified. Even complete eigenvalues do not by themselves identify the source-basis ratio q1/q2. That basis is tied to the original-band model, not freely relabeled to make q12 vanish without simultaneously changing the state/energy Hamiltonian.

## What the two measured ratios alone omit

At17→15 define raw energy-order ratios r_y=abs(M_ny,y/M_yy)^2 and r_ny=abs(M_y,ny/M_ny,ny)^2. The TableI central continuity ratios imply r_y=1/.6 and r_ny=1/.3. Up to row/column sign conventions, write

\[
M=\left(\sqrt A\,u_y,\ \sqrt B\,u_{ny}\right),\quad
u_y=\frac{(1,s_y\sqrt{r_y})^T}{\sqrt{1+r_y}},\quad
u_{ny}=\frac{(s_n\sqrt{r_{ny}},1)^T}{\sqrt{1+r_{ny}}},
\quad s_y,s_n=\pm1.
\]

Here A andB are the two column norms squared, which require absolute transition strengths, not just the ratio in each column. Relative branch signs also remain unmeasured. Let c=u_y^Tu_ny. Then

\[
\|M\|_F^2=A+B,\qquad
(\det M)^2=AB(1-c^2),
\]
\[
\sigma_\pm^2=\frac{A+B\pm\sqrt{(A-B)^2+4ABc^2}}2.
\]

Thus the two ratios do not supply any absolute Frobenius norm, determinant or singular values. Without the relative column normalization A/B they also do not fix the singular-value **ratio**, even though an overall common scale would cancel from that ratio. The signed loop product M11M22M12M21 controls the determinant interference; full four strengths alone leave this discrete sign ambiguity if no phase information is supplied.

For the actual17 central ratios, abs(c) can be.9168634 or.1573089 depending on the unmeasured branch-sign loop. If the two columns are chosen to have equal norms only as an illustration, the resulting condition numbers are4.80175 and1.17190, respectively. Unknown relative column norms can make the condition number arbitrarily large as one column becomes weak. These are conditional properties of the ratio-only family, not a recovered physical SVD range with experimental uncertainty.

The script records examples with the same central ratios but different signs or A/B, verifying the analytic formula. **These ratio-only examples use an unrestricted real observed matrix**; they are not claimed to fit the additional symmetric-Q/source-alpha ansatz. This separation is essential: imposing known mixing matrices and a symmetric kernel adds constraints beyond the two measured ratios.

## Identification after adding q12: the precise conclusion

The printed alpha values were extracted within the original assumptions and are reused here only for a forward baseline. They are not independent experimental measurements that can be fixed while assigning a new confidence interval to the enlarged kernel. The old diagonal-kernel solution therefore cannot automatically identify q1/q2 once q12 is admitted.

This is not a proof that every enlarged inverse problem has a continuous degeneracy. If mixing matrices are known independently, a common geometry is fixed and two ratios are measured exactly, the two scale-free symmetric-kernel parameters(q1/q2,q12/q2) can generically have isolated solutions within each selected amplitude-sign branch. Additional energies, shared-spin assumptions or multiple transitions may constrain them further. Existence, uniqueness and uncertainty would need their actual response/likelihood and consistent energy mixing; no such inverse fit was performed.

Useful additional information is therefore specific: independently constrained state mixing and phase convention; complete same-parent E2 branch accounting/limits; absolute column norms from state lifetimes and branching/ICC; and phase-sensitive interference constraints or a justified transition-kernel sign model. Complete **signed**2×2 M with known Rf/Ri gives Q=Rf M Ri^T and hence all three kernel entries. Four unsigned widths plus lifetimes add scale and magnitude information, but do not automatically give that signed reconstruction or validate the underlying two-band truncation.

This identifies how band mixing can redistribute EM strength while leaving a nearby energy pair, but it does not establish a new quantum geometry or make the band-mixing alternative win. The original energy-mixing V and spacings remain distinct from the transition-operator q12. No old crossing threshold, rigid-shape inference or exclusive chirality rejection is revived.

## Reproducible scope and stop

`kernel_checks.py` uses NumPy for the explicit source-basis matrix multiplication, direct component formulas, orthogonality/rephasing, q12=0 source baseline, Eq4/Eq5 diagonal limits, Frobenius/determinant/SVD identities and a few ratio-only column examples. Executed output is `kernel-results.json`. No model producer, optimization, Monte Carlo likelihood or experimental error fit was run. Floating-point agreements check the stated finite algebra; they are not physical confidence intervals.

The added information is saturated at this level: accurate out/in labels plus the distinction between basis invariants and ratio-identifiable quantities. Further unrestricted scans would not recover missing phases, column strengths or original-band mixing evidence and are not needed for the preview component.
