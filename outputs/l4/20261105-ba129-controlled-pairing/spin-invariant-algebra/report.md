**Independent general-spin quadrupole-invariant audit**

**Result:** the literal \(J'=J+2\) expressions in the archived Nomura et al. arXiv v2 are well-defined spin-restricted RME proxies, invariant under spatial rotations and independent rephasing of the nuclear states when whole magnetic multiplets are retained. They can be related to scalar contractions containing spectral/spin projectors, which need not be local charge-tensor polynomials. Under the requested Wigner–Eckart convention, they are not the complete RME expansions of \(q_2=\langle Q\cdot Q\rangle\) and signed \(q_3=-\sqrt{7/2}\langle[Q\times Q]^{(2)}\cdot Q\rangle\) at general \(J\). The controls establish this nonidentity and delimit the effective-to-intrinsic shape calibration. They do not invalidate explicitly defined effective observables.

All quoted strong-\(K=J\) rotor numbers are independently reproduced. All three parent spectator conjectures are confirmed under the assumptions stated below. These are algebraic results about the supplied convention and literal formulas. At fixed \(J\), changes in the strength carried by the selected channel can reflect real particle–core dynamics and isotope-dependent redistribution. A varying-spin spectator control does not identify such changes as artifacts. **No novelty claim, published-code-error claim, invalid-effective-definition claim, figure reconstruction, or claim about the version of record is made.**

**Source scope and locators**

The inspected [13-page PDF](</workspace/wiki/raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf>) carries the banner `arXiv:1704.07101v2`, **8 July 2017**. Its generated `Dated: November 21, 2021` line is not used as the version date; the supplied TeX uses `\today` at line 32. The TeX file's `v4` member name is not interpreted as an arXiv version identifier.

The [page-11 image](/workspace/wiki/tmp/ba129-spin-invariant-algebra/nomura2017-v2-p11.png) confirms the target equations, including the absolute value, the \(J'=J+2\) restriction and \(n=5\).

| Source item | Precise location |
|---|---|
| Eq. (12): raw quadratic RME sum | PDF p.11; [TeX L1264](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:1264), formula L1267–1268 |
| Eq. (13): absolute cubic RME sum | PDF p.11; [TeX L1271](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:1271) |
| \(J'=J+2\), increasing excitation energy, \(n=5\) | PDF p.11; [TeX L1277](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:1277) |
| Eq. (14): beta conversion with the CG coefficient | PDF p.11; [TeX L1306](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:1306) |
| Eq. (15): gamma from arccos | PDF p.11; [TeX L1308](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:1308) |
| Boson Hamiltonian quadrupole operator | [TeX L214](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:214) |
| Actual E2 operator has boson and fermion terms | [TeX L552](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:552); boson E2 parameter \(\chi'=0.35\) at L574 |

The calculations below use the convention declared for this audit. They do not assume that an undocumented source-code normalization has been independently established.

**1. Conventions and complete scalar moments**

Let the reference state be \(|rJM\rangle\), and write

\[
M_{ab}\equiv\langle aJ_a\Vert Q^{(2)}\Vert bJ_b\rangle,\qquad
\langle aJ_aM_a|Q_\mu|bJ_bM_b\rangle
=\frac{C(J_bM_b,2\mu\mid J_aM_a)}{\sqrt{2J_a+1}}M_{ab}.
\]

Use Condon–Shortley CG coefficients, the tensor Hermiticity relation
\(Q_\mu^\dagger=(-1)^\mu Q_{-\mu}\), and the definitions

\[
A^{(k)}\cdot B^{(k)}
=\sum_\mu(-1)^\mu A_\mu B_{-\mu},
\qquad
[Q\times Q]^{(2)}_\nu
=\sum_{\mu\kappa}C(2\mu,2\kappa\mid2\nu)Q_\mu Q_\kappa.
\]

Operator order is retained. Commutativity of quadrupole components is not assumed. Hermiticity gives

\[
M_{ab}=(-1)^{J_a-J_b}M_{ba}^{*}.
\]

Inserting complete sets of intermediate states and performing the magnetic sums gives

\[
\boxed{
q_2(rJ)=
\frac{1}{2J+1}
\sum_{a,J_a}(-1)^{J_a-J}M_{ra}M_{ar}
=\frac{1}{2J+1}\sum_{a,J_a}|M_{ar}|^2 .
}
\tag{1}
\]

The sum includes every allowed intermediate spin
\(|J-2|\le J_a\le J+2\), all contributing states at those spins, and any additional E2 selection rules. Diagonal/static matrix elements and other states of the same spin contribute when the triangle condition permits them. For \(J=1/2\), a rank-two diagonal matrix element is forbidden; the complete spin set is \(3/2,5/2\), not \(1/2,3/2,5/2\).

For the ordered cubic contraction defined in the question,

\[
\boxed{
q_3(rJ)=
-\frac{(-1)^{2J}}{2J+1}\sqrt{\frac{35}{2}}
\sum_{\substack{a,J_a\\b,J_b}}
\begin{Bmatrix}
2&2&2\\
J&J_a&J_b
\end{Bmatrix}
M_{ra}M_{ab}M_{br}.
}
\tag{2}
\]

Both outer intermediate spins obey the rank-two triangle with \(J\); the middle RME also obeys \(|J_a-J_b|\le2\le J_a+J_b\). The labels \(a,b\) include state multiplicities and quantum numbers. The factor \((-1)^{2J}\) distinguishes integer and half-integer reference spin and must not be omitted under this convention.

For clarity, an intermediate step in the derivation is

\[
\langle rJ\Vert[Q\times Q]^{(2)}\Vert bJ_b\rangle
=(-1)^{J+J_b+2}\sqrt5
\sum_{a,J_a}
\begin{Bmatrix}2&2&2\\J_b&J&J_a\end{Bmatrix}
M_{ra}M_{ab}.
\]

Contracting this rank-two tensor with the last \(Q\) gives a factor
\((-1)^{J_b-J}/(2J+1)\). Their combined phase is
\((-1)^{2J_b+2}=(-1)^{2J}\); column symmetries of the \(6j\) give Eq. (2). This derivation does not replace RMEs by their magnitudes.

The cubic scalar is Hermitian even if the components do not commute. In fact,

\[
[Q\times Q]^{(2)}\cdot Q
=\sqrt5\sum_{\mu\nu\lambda}
\begin{pmatrix}2&2&2\\\mu&\nu&\lambda\end{pmatrix}
Q_\mu Q_\nu Q_\lambda.
\]

The \(222\) \(3j\) coefficient is symmetric under permutations and simultaneous reversal of its magnetic indices. Taking the adjoint and relabeling dummy indices therefore returns the same operator. Its expectation is real; its **sign** is physical information in a signed invariant.

**2. Zero-spin reduction and the meaning of the restricted proxy**

At \(J=0\), both intermediate spins are necessarily 2 and
\(\left\{\begin{smallmatrix}2&2&2\\0&2&2\end{smallmatrix}\right\}=1/5\). Thus

\[
q_2(0)=\sum_a M_{0,2_a}M_{2_a,0},
\qquad
q_3(0)=-\sqrt{\frac7{10}}
\sum_{ab}M_{0,2_a}M_{2_a,2_b}M_{2_b,0}.
\tag{3}
\]

These are the standard zero-spin expressions under the specified signed definition. With complete sums, source Eq. (12) agrees with the first, and source Eq. (13) yields \(|q_3(0)|\). The absolute value discards the sign; within a valid rigid-shape interpretation it folds the usual \(0^\circ\)–\(60^\circ\) gamma range into \(0^\circ\)–\(30^\circ\). It is a defined convention, not a recovery of the signed invariant.

To distinguish the objects, denote the literal source expressions by
\(\widetilde q_2,\widetilde q_3\), set \(L=J+2\), and let
\(\Pi_{L,n}\) project onto the selected \(n\) complete magnetic multiplets:

\[
S_{L,n}=\sum_{a,b\in(L,n)}M_{ra}M_{ab}M_{br},
\qquad
\widetilde q_2=\sum_{a\in(L,n)}M_{ra}M_{ar},
\quad
\widetilde q_3=\sqrt{7/10}\,|S_{L,n}|.
\]

Each RME and closed RME loop is independent of the laboratory orientation. An individual RME changes under independent state phases, \(M_{ab}\mapsto e^{-i\phi_a}e^{i\phi_b}M_{ab}\), but the phases cancel in \(M_{ra}M_{ar}\) and \(M_{ra}M_{ab}M_{br}\). Both proxy sums, their absolute-value version, and \(\Pi_{L,n}\) are therefore invariant under these state-phase conventions. Since \(\Pi_{L,n}\) commutes with rotations, the corresponding projected contractions are also scalars:

\[
\langle Q\cdot\Pi_{L,n}Q\rangle
=\frac{\widetilde q_2}{2J+1},
\]

\[
-\sqrt{\frac72}
\sum_{\mu\nu}(-1)^{\mu+\nu}C(2\mu,2\nu\mid2,\mu+\nu)
\langle Q_\mu\Pi_{L,n}Q_\nu\Pi_{L,n}Q_{-\mu-\nu}\rangle
=-\frac{(-1)^{2J}}{2J+1}\sqrt{\frac{35}{2}}
\begin{Bmatrix}2&2&2\\J&L&L\end{Bmatrix}S_{L,n}.
\tag{4}
\]

The absolute value of a scalar expectation is still rotation- and state-phase-invariant. It is generally a nonlinear function of that expectation: \(|\langle O\rangle|\) need not equal \(\langle|O|\rangle\). No identification of these two operations is needed to regard source Eq. (13) as a well-defined effective scalar quantity.

Thus three distinctions are necessary:

1. A restricted RME proxy can be rotationally scalar.
2. It is not the complete \(Q\cdot Q\) or cubic tensor moment.
3. Neither rotational scalar character nor a numerical arccos guarantees a general intrinsic-shape interpretation. This is a limitation on that interpretation, not a verdict that an explicitly stated effective definition is wrong.

For \(J>0\), the literal quadratic expression lacks the full scalar's \(1/(2J+1)\) normalization and other spin channels. The literal cubic expression additionally uses the zero-spin coefficient instead of the required spin-dependent \(6j\) weight and takes an absolute value. Its spin dependence cannot generally be removed by the beta conversion alone.

**3. Axial strong-\(K=J\) rotor control**

Use exactly the supplied control:

\[
\langle J_f\Vert Q\Vert J_i\rangle
=\sqrt{2J_i+1}\,
C(J_iK,20\mid J_fK)\,q_0,
\qquad K=J_{\rm initial}.
\]

For a fixed nonfluctuating axial intrinsic quadrupole \(q_0>0\), full closure gives

\[
q_2=q_0^2,\qquad q_3=q_0^3,\qquad
q_3/q_2^{3/2}=1,\qquad \gamma=0.
\]

This was checked both with Eqs. (1)–(2) and by explicit magnetic-substate contraction, at several \(M\)'s for each tested spin. No parent calculation was imported.

Only the \(J,J+1,J+2\) spins can contribute in this bandhead control: lower spins are excluded by \(K=J\). Their respective contributions to full \(q_2/q_0^2\) are

\[
\frac{J(2J-1)}{(J+1)(2J+3)},\qquad
\frac{3J}{(J+1)(J+2)},\qquad
\frac6{(J+2)(2J+3)}.
\tag{5}
\]

They sum to one. The first vanishes where a diagonal rank-two matrix element is forbidden. In particular, at \(J=11/2\) the \(J+2\) channel contains only \(2/35\) of the full quadratic strength; including every state at that spin would not add the missing \(J\) and \(J+1\) strength.

For the literal source proxy there is a single nonzero state at \(L=J+2\). Four zero-strength channels may be appended to make \(n=5\) without changing any number. Its arccos argument is

\[
\widetilde c_{\rm rotor}(J)
=\sqrt{\frac7{10}}\,
\frac{|C(LK,20\mid LK)|}{|C(LK,20\mid JK)|},
\quad L=J+2,\quad K=J,
\]

with the closed form

\[
\boxed{
\widetilde c_{\rm rotor}^{\,2}
=
\frac{7(2J^2-5J-6)^2(2J+5)}
{60(2J+1)(J+3)(2J+7)} .
}
\tag{6}
\]

| Initial \(J=K\) | Literal argument \(\widetilde c_{\rm rotor}\) | Literal \(\widetilde\gamma\) | Full-closure gamma |
|---:|---:|---:|---:|
| \(1/2\) | 0.8944271910 | \(8.855017^\circ\) | \(0^\circ\) |
| \(3/2\) | 0.6480740698 | \(16.534483^\circ\) | \(0^\circ\) |
| \(5/2\) | 0.3256694736 | \(23.664620^\circ\) | \(0^\circ\) |
| \(7/2\) | 0.0438529010 | \(29.162203^\circ\) | \(0^\circ\) |
| \(9/2\) | 0.4427188724 | \(21.240838^\circ\) | \(0^\circ\) |
| \(11/2\) | 0.8609160648 | \(10.193468^\circ\) | \(0^\circ\) |
| \(13/2\) | 1.2924884200 | **Outside the real arccos domain; not clipped** | \(0^\circ\) |

The six numerical conjectures and the \(13/2\) domain failure are confirmed. The turnover is produced by angular-momentum geometry, including the sign change of \(2J^2-5J-6\) before the absolute value; the intrinsic control shape did not change.

The beta proxy behaves differently in this particular control. Let
\(C_\beta=4\pi/(3ZR_0^2)\), using a common charge/unit convention, and define
\(\beta_{\rm inv}=C_\beta\sqrt{q_2}\). Because

\[
\widetilde q_2=(2L+1)|C(LJ,20\mid JJ)|^2q_0^2,
\]

the CG division in source Eq. (14) gives
\(\widetilde\beta=C_\beta|q_0|=\beta_{\rm inv}\).
That agreement is a calibration to this strong-\(K=J\) rotor geometry. It does not establish a general-spin scalar definition of \(\widetilde q_2\), or validate its application to a different coupling limit.

**4. Spectator control and all three parent conjectures**

Assume:

- the initial state is exactly \(|0_r\rangle_{\rm core}\otimes|jm\rangle\), with core spin \(R=0\);
- \(Q=Q_{\rm core}\otimes1_j\), with **no fermion E2 term**;
- a fixed spectator \(j\), with the same tensor/charge convention in core and odd system;
- complete intermediate-state closure when “full” is used, and all relevant states at \(L=j+2\) when the restricted formula is used;
- \(q_{2,\rm core}>0\); the beta comparison uses the same \(C_\beta\), including radius.

Then the full scalar moments are exactly those of the core. This follows directly from the tensor-product operator, irrespective of whether the core components commute or an effective gamma exists:

\[
q_{2,\rm odd}=q_{2,\rm core},\qquad
q_{3,\rm odd}=q_{3,\rm core}.
\tag{7}
\]

For an independent angular-momentum check, the code constructs coupled RMEs by direct sums of magnetic CG coefficients and verifies the recoupling identity

\[
\langle(R_fj)J_f\Vert Q_{\rm core}\Vert(R_ij)J_i\rangle
=(-1)^{R_f+j+J_i+2}
\sqrt{(2J_f+1)(2J_i+1)}
\begin{Bmatrix}R_f&J_f&j\\J_i&R_i&2\end{Bmatrix}
\langle R_f\Vert Q_{\rm core}\Vert R_i\rangle.
\]

All intermediates connected to the \(R=0\) initial state have core spin 2, with total spins \(L=|2-j|,\ldots,2+j\). Their full quadratic contributions are
\((2L+1)q_{2,\rm core}/[5(2j+1)]\), which sum to Eq. (7).

For the restricted **maximally coupled** \(L=j+2\), write
\(t_a=\langle2_a\Vert Q_{\rm core}\Vert0_r\rangle\). Direct coupling gives

\[
\langle(2_aj)L\Vert Q_{\rm core}\Vert(0_rj)j\rangle
=\sqrt{\frac{2L+1}{5}}\,t_a.
\]

It follows that the parent's first conjecture is exact:

\[
\boxed{\widetilde q_2=\frac{2j+5}{5}\,q_{2,\rm core}.}
\tag{8}
\]

For source Eq. (14),

\[
|C(j+2,j;2,0\mid j,j)|^2
=\frac{12(2j+1)}{(2j+5)(2j+4)(2j+3)}.
\]

Consequently, the second conjecture is also exact at common \(C_\beta\):

\[
\boxed{
\frac{\widetilde\beta}{\beta_{\rm inv}}
=\sqrt{\frac{(2j+5)(2j+4)(2j+3)}{60(2j+1)}} .
\tag{9}
\]

At \(j=11/2\) this is \(\sqrt{14/3}=2.16024689947\).
Different radii or charge normalizations would multiply this ratio by the corresponding prefactor ratio.

The middle matrix element follows most directly from the stretched product state
\(|(2j)L,L\rangle=|2,2\rangle|j,j\rangle\):

\[
\langle(2_aj)L\Vert Q_{\rm core}\Vert(2_bj)L\rangle
=\sqrt{\frac{2L+1}{5}}\,
\frac{C(22,20\mid22)}{C(LL,20\mid LL)}
\langle2_a\Vert Q_{\rm core}\Vert2_b\rangle .
\]

Thus, defining a **folded ratio**, without assuming it is in the cosine domain,
\[
c_{\rm core}^{\rm fold}=
\frac{|q_{3,\rm core}|}{q_{2,\rm core}^{3/2}},
\]
the parent's third conjecture is confirmed:

\[
\boxed{
\widetilde c_{\rm spectator}=F_jc_{\rm core}^{\rm fold},
\qquad
F_j=\frac{C(22,20\mid22)}{C(j+2,j+2;2,0\mid j+2,j+2)}
=\sqrt{\frac{2(j+3)(2j+7)}{7(j+2)(2j+3)}} .
}
\tag{10}
\]

When \(q_{3,\rm core}=0\), Eq. (10) is still a valid proportionality, but a numerical quotient \(\widetilde c/c_{\rm core}^{\rm fold}\) is undefined.

These factors were checked for both a one-\(2^+\)-multiplet axial-core control and a separate two-\(2^+\)-multiplet control with nontrivial middle RMEs. The latter verifies the sums rather than only a single transition product. No energy or nuclear data were fitted.

For the axial core, \(q_{2,\rm core}=q_{3,\rm core}=1\) and full gamma is zero:

| Spectator \(j\) | \(\widetilde q_2/q_{2,\rm core}\) | \(\widetilde\beta/\beta_{\rm inv}\) | \(F_j\) | Literal gamma |
|---:|---:|---:|---:|---:|
| \(1/2\) | 1.2 | 1.000000000 | 0.894427191 | \(8.855017^\circ\) |
| \(3/2\) | 1.6 | 1.183215957 | 0.782460796 | \(12.837854^\circ\) |
| \(5/2\) | 2.0 | 1.414213562 | 0.723746864 | \(14.545100^\circ\) |
| \(7/2\) | 2.4 | 1.658312395 | 0.687551651 | \(15.521129^\circ\) |
| \(9/2\) | 2.8 | 1.907878403 | 0.662993544 | \(16.157140^\circ\) |
| \(11/2\) | 3.2 | 2.160246899 | 0.645233702 | \(16.605600^\circ\) |
| \(13/2\) | 3.6 | 2.414243448 | 0.631790839 | \(16.939210^\circ\) |

This is a different physical limit from the strong-\(K=J\) rotor. In particular, the rotor's beta CG correction is exact for that rotor control but overstates the spectator beta relative to the core invariant. No single universal deformation calibration follows from agreement in one limit.

**5. Spectral cutoff and missing spins are separate effects**

Increasing \(n\) at fixed \(L=J+2\) completes \(\Pi_{L,n}\) within that spin. It never restores intermediate \(J-2,J-1,J,J+1\) multiplets allowed by the tensor triangles. The geometric factors in Eqs. (6), (8)–(10) remain when **all states at the selected spin** are retained.

The controls have one or two nonzero core-2 channels; \(n=5\) already exceeds those numbers. Their failures to reproduce full moments therefore cannot be attributed to a five-state spectral truncation. In a real calculation, a finite energy-ordered cutoff can add a separate error. Quadratic strength is nonnegative after the proper Hermitian phase/normalization, but the signed cubic sum contains cross terms and need not converge monotonically.

The exact spectator factors require complete relevant \(L\)-space closure. With an incomplete set of mixed eigenstates, the selected spectral projector need not retain all the core-2 strength, and the factors relative to **full** core invariants need not hold. They may relate matching truncated core sums only under an additional correspondence of the retained subspaces.

**Physical redistribution at fixed \(J\).** For \(q_2>0\), define the fraction of full quadratic strength in a retained channel by

\[
f_{L,n}(rJ)=
\frac{\sum_{a\in(L,n)}|M_{ar}|^2}{(2J+1)\,q_2(rJ)}.
\]

For \(L=J+2\),

\[
\widetilde q_2=(2J+1)\,f_{J+2,n}(rJ)\,q_2(rJ).
\tag{11}
\]

At fixed \(J\), the factor \(2J+1\) is fixed, whereas \(f_{J+2,n}\) can change with particle–core coupling, configuration mixing, fragmentation of E2 strength, or changes in the core and fermion E2 contributions. Such redistribution is a possible physical signal, even if the full quadratic moment happens to remain constant. The cubic proxy additionally depends on middle RMEs and interference, so a quadratic strength fraction alone cannot correct it.

The spectator \(j\)-control holds the core and the core-only operator fixed while varying spectator angular momentum; its factors isolate geometry in that stipulated limit. An isotope sequence at the same selected \(J\), such as an individual fixed-spin curve in the source's effective-deformation plots, is not that control. Its kinematic factors do not vary merely because neutron number changes, while the RMEs can vary dynamically. Neither the spectator factors nor the strong-\(K=J\) control can, by themselves, explain away an isotope trend or show that a channel-sensitive effective observable is unphysical. Conversely, a change of the effective observable alone does not establish the same change in a full charge-tensor polynomial moment or in an intrinsic shape.

**6. Neither noncommuting IBM tensors nor beta fluctuations permit an unconditional cosine bound**

For a single fixed classical quadrupole shape in the chosen normalization,
\(q_2=a^2\beta^2\) and \(q_3=a^3\beta^3\cos3\gamma\), so the ratio is a cosine. Two different extensions break the inference that the ratio must always lie in \([-1,1]\).

First, even for commuting collective coordinates with a shape distribution,

\[
\frac{q_3}{q_2^{3/2}}
=\frac{\langle\beta^3\cos3\gamma\rangle}
{\langle\beta^2\rangle^{3/2}}.
\]

Although the numerator's magnitude is at most \(\langle\beta^3\rangle\), that moment is not bounded above by \(\langle\beta^2\rangle^{3/2}\). For \(\beta=0\) or 1 with equal probability, and axial \(\gamma=0\) at nonzero beta, the ratio is \(\sqrt2>1\). This is a shape-fluctuation example, not evidence of an incorrect tensor contraction.

Second, finite-space IBM quadrupole components need not commute, so the fixed classical-shape identity cannot be imposed on their operator moments. An explicit small operator-algebra control uses one boson in the \(s\) state and

\[
Q_\mu=d^\dagger_\mu s+s^\dagger\tilde d_\mu
+\chi[d^\dagger\times\tilde d]^{(2)}_\mu,\qquad
\chi=-\sqrt7/2.
\]

Direct multiplication of its six-dimensional \(s,d_m\) matrices gives

\[
q_2=5,\quad q_3=\frac{35\sqrt2}{4},\quad
\frac{q_3}{q_2^{3/2}}=\frac7{2\sqrt{10}}
=1.10679718106,
\]

and \(\|[Q_2,Q_{-2}]\|_F^2=45/8\ne0\).
This is a valid Hermitian quadrupole-tensor example. It is **not** a calculation with the paper's E2 \(\chi'=0.35\), not a reconstruction of its figures, and not an A130 nuclear result.

Accordingly, an outside-domain ratio must be retained and diagnosed. **No clipping to \(\pm1\) is justified here.** A failure of the effective-angle mapping can result from operator algebra or fluctuations even for correct full moments; in the fixed nonfluctuating rotor control, however, the outside-domain restricted ratio demonstrably comes from the proxy geometry. These explanations must not be conflated.

**7. What is established and what remains untested**

- Established: Eqs. (1)–(3), with the displayed \(6j\), phase and normalization, reproduce direct magnetic-substate contractions under the declared convention.
- Established: the literal restricted expressions do not generally reproduce those full scalar moments, even with no spectral truncation.
- Established: all proposed rotor and spectator algebraic controls, including the three spectator factors and their assumptions.
- Established: a real effective gamma is not guaranteed by arbitrary full quantum or fluctuating-shape moments; no clipping is used.
- Interpretation retained: the source's proxies are rotation- and state-phase-invariant effective quantities. Their distinction from full charge-tensor polynomial moments does not make their definitions wrong.
- Interpretation retained: changing channel-strength fractions at fixed \(J\) can represent real particle–core dynamics; the pure-geometry controls do not classify actual isotope-dependent redistribution as an artifact.
- Not established: a software error in Nomura et al.'s implementation, incorrect figure points, invalidity of its explicitly defined effective observables, a changed empirical shape-transition conclusion, an error in the published version of record, or novelty of the general-spin algebra or diagnostic idea.

The source's actual E2 operator includes a fermion term and a specific boson E2 parameter; an interacting odd-system eigenstate need not be the spectator product used above. A targeted figure reconstruction would need the authors' RME normalization and phases, the exact operator and fitted inputs, the state ordering and retained multiplets, and a comparison of literal Eqs. (12)–(15) with full contractions for the **same** states. It should assess convergence within each spin separately from strength redistribution among spins, and examine fixed-\(J\) isotope trends separately from changes of the reference spin. Calling the published quantities “effective” is compatible with their use as operational diagnostics; any stronger intrinsic-shape interpretation must be assessed on its stated calibration and the actual calculation. The present audit establishes the distinctions to test; it does not supply those missing implementation facts.

The independent [exact-check script](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-algebra/exact_checks.py) imports only Python's standard library. CG and \(6j\) coefficients use factorial sums and exact rational/square-free-root arithmetic; direct magnetic contractions and recoupled expressions are computed separately. [Exact results](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-algebra/exact_checks.json) contain 1,486 passed coefficient, phase, tensor, and control checks, including elementary CG completeness checks. This count is not a count of independent physical validations. Floating point is used only to display final values and angles; the arccos-domain decision in these controls is made from the exact squared ratio.

All notes and check artifacts are confined to `outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-algebra/`. Source page extracts and the inspected page image are confined to `tmp/ba129-spin-invariant-algebra/`. No parent or production code was imported, no model data were changed, and no commit was made.
