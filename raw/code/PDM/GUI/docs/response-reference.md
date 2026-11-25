# PDM angular-correlation reference

`angular_correlation.py` evaluates Droste's generalized 9j radiation
coefficients and couples statistical tensors through an emission-ordered
cascade. It uses a factorial Wigner small-d implementation and SymPy's angular
momentum symbols. It never constructs a nuclear emission matrix, an observed
density matrix, or production quadratic coefficients. The standalone tests
also compare against Cartesian or closed-form cases derived separately from
the recoupled kernel.

## Input and normalization

- `Transition.mixed(Ji, Jf, delta)` takes the signed **Droste / Krane-Steffen**
  radiation amplitude ratio \(a(E2)/a(M1)\). It uses real, normalized weights
  \((1,\delta)/\sqrt{1+\delta^2}\). Pure E2 uses `Transition.pure`.
- Populations are in ascending \(m\), with axial alignment and
  \(p_m=p_{-m}\). `gaussian` uses the source state's \(\sigma\) in spin
  units. Unobserved steps use normalized radiative multipole weights and
  propagate each tensor component without fitting a new \(\sigma\).
- The direction is \((\theta,\phi)\) in radians in the common lab frame.
  Parallel and perpendicular refer to the photon **electric field** along
  \(\mathbf e_\theta\) and \(\mathbf e_\phi\). At a pole the supplied \(\phi\)
  fixes the analyzer meridian. Polarization is a channel difference divided
  by the channel sum and is undefined at zero total intensity. For an
  experiment, the relation to Compton scattering counts uses the calibrated
  sensitivity and analyzer response.
- Multiply the single density in \(\mathrm{sr}^{-1}\) by \(4\pi\), or the
  joint density in \(\mathrm{sr}^{-2}\) by \((4\pi)^2\), to get the module
  outputs. Unpolarized isotropic emission has scaled intensity one.
  `joint(target=1)` is POL--DIR and `joint(target=2)` is DIR--POL. The
  other photon is always summed over helicity. The reference is exercised
  for real dipole/quadrupole radiation and at most one linear analyzer.

## Tensor construction

Let \(j_i,j_f\) be the spin before and after a step, \(a,b\) the outgoing
and incoming tensor ranks, \(k\) a radiation rank, and \(d^k\) use
\(\exp(-i\theta J_y)\), with \(d^1_{10}=-\sin\theta/\sqrt2\).
Droste's Eq. (2) gives

\[
B_b(j_i)=\sqrt{2j_i+1}\sum_m(-1)^{j_i+m}
\langle j_i,-m;j_i,m\mid b,0\rangle p_m .
\]

With normalized multipole weights \(v_{TL}\), the two radiation coefficients
are sums of \(v_{TL}v_{T'L'}\) times

\[
(-1)^{L-1}
\sqrt{(2j_i+1)(2j_f+1)(2L+1)(2L'+1)(2a+1)(2b+1)}
\begin{Bmatrix} j_i&j_i&b\\ L&L'&k\\ j_f&j_f&a\end{Bmatrix}
\]

times the following helicity factors.

| Coefficient | Helicity factor |
| --- | --- |
| \(A^{ab}_{k0}\) | \(\langle L,-1;L',1\mid k,0\rangle\) |
| \(A^{ab}_{k2}\) | \((-1)^{[T'=M]}\langle L,-1;L',-1\mid k,-2\rangle\) |

These are Droste Eqs. (3), (4), (7), and (8), with the **primed**
magnetic indicator from Starosta p. 17 footnote 1. In the second row the
Clebsch-Gordan coefficient is put into \(H_k F_k\) directly. This also
defines the product when the denominator of \(H_k\) vanishes. Substituting
the original printed unprimed indicator leaves pure terms alone and reverses
the mixed E/M contribution to the Stokes numerator.

For singles or the full directional marginal of the other photon,

\[
\begin{split}
W(\theta)&=\sum_k B_k U^{\rm before}_k A^{0k}_{k0} d^k_{00}(\theta),\\
S(\theta)&=-\sum_k B_k U^{\rm before}_k A^{0k}_{k2} d^k_{02}(\theta),\\
I_\parallel&=(W+S)/2,\qquad I_\perp=(W-S)/2 .
\end{split}
\]

For the joint response a term in the directional sum is

\[
B_b U^{\rm before}_b U^{\rm between}_a(2-\delta_{\mu0})
\langle b,0;a,\mu\mid k,\mu\rangle\cos(\mu\Delta\phi)
\; A^{ab}_{k0}(1)d^k_{\mu0}(\theta_1)\,
A^{0a}_{a0}(2)d^a_{\mu0}(\theta_2).
\]

For \(S\), replace the analyzed leg's \(A_{k0}d^k_{\mu0}\) with
\(-A_{k2}(d^k_{\mu2}+(-1)^k d^k_{\mu,-2})/2\) for the first leg. For
the second leg substitute \(a\) for \(k\), which is even there. This is
Droste Eq. (16) restricted to \(\psi=0,\pi/2\) and one analyzer. With
\(U_0=1\), and \(U_k\) from the Steffen--Alder 6j expression, the fully
integrated directional intensity is one. An empty product of \(U_k\) gives
the adjacent cascade. Integrating a direction removes that detector's
angular conditioning. It preserves its unobserved spin transfer when
it occurs upstream of the target.

## Bridge to the production helicity basis

Use \(q=m_i-m_f\), \(h=\pm1\),
\(D^L_{qh}(\phi,\theta,0)=e^{-iq\phi}d^L_{qh}(\theta)\), and define
\(\eta_E(h)=1,\ \eta_M(h)=h\). With Condon--Shortley CG coefficients,
a helicity realization of the source weights is

\[
\mathcal A_h =
\sum_{TL} v_{TL}(-1)^L \eta_T(h)
\sqrt{\frac{2L+1}{8\pi}}\,
\langle j_f m_f,Lq\mid j_i m_i\rangle D^{L*}_{qh} .
\]

Choose linear combinations \((\mathcal A_+-\mathcal A_-)/\sqrt2\)
for parallel and \((\mathcal A_++\mathcal A_-)/\sqrt2\) for perpendicular,
up to a phase per analyzer. In this helicity gauge, the \(+\) helicity
has unit E and M factor. The \(-\) helicity on the primed leg of the
off-diagonal photon product gives exactly \((-1)^{[T'=M]}\).
Changing to \(\mathcal A'_h=h\mathcal A_h\) produces the production gauge
\(\eta'_E(h)=h,\ \eta'_M(h)=1\), with parallel given by the sum.
The phase change of the analyzer and helicity conventions is common to
the multipoles.

For each fixed \(h\), integrating \(D^*_{qh}D_{q'h}\) gives
\(4\pi\,\delta_{qq'}\delta_{LL'}/(2L+1)\), with the ranks on the two
rotation factors understood to be \(L,L'\). The two helicities and
orthogonality of the nuclear CG coefficients then give
\(\sum_h\int d\Omega\,\mathcal A_h^\dagger\mathcal A_h=1\) on the
parent spin space for \(\sum_{TL}|v_{TL}|^2=1\).

Three steps give the relative \((-1)^L\) through CG/9j recoupling.

1. Use \((-1)^{j+m'}\langle j,-m';j,m\mid b,B\rangle\) on the
   spin tensor. In the conjugated photon leg reverse the CG projections
   and use \(D^L_{qh}=(-1)^{q-h}D^{L*}_{-q,-h}\). With \(m'_i=m'_f+q\)
   the resulting phase before permuting the 9j is \((-1)^{L-1}\).
2. The four-angular-momentum recoupling gives the 9j with rows
   \((j_f,j_f,a)\), \((L,L',k)\), \((j_i,j_i,b)\) after transposition.
   Exchanging the top and bottom rows to match Droste Eq. (7) gives
   \((-1)^{L+L'+a+k+b}\). This uses even \(2j_i+2j_f\) for a photon
   transition. Rewriting the axial coupling
   \(\langle a,\mu;k,-\mu\mid b,0\rangle\) into
   \(\langle b,0;a,\mu\mid k,\mu\rangle\) and reversing the Wigner
   projection contributes \((-1)^{k+b}\) for the even helicity
   differences \(0,\pm 2\). The intermediate tensor rank \(a\) is even
   in the one-analyzer problem.
3. Bare helicities therefore carry an extra \((-1)^{L+L'}\) in
   the source coefficient. The amplitude phase \((-1)^L\) cancels it
   in every pair. Either sign of a common overall amplitude phase gives
   the same observables.

An axial sign anchor is \(3/2\to1/2\) at \(\theta=\pi/2\) with only
\(|m_i|=3/2\) occupied. For \(m_i=3/2\), the \(q=1\) CGs are
\(1\) and \(1/\sqrt5\) for \(L=1,2\). The electric quadrupole \(q=2\)
CG is \(-2/\sqrt5\). Evaluating the two analyzer combinations gives
\(I_\parallel=(\sqrt3+\delta)^2/[4(1+\delta^2)]\) and
\(I_\perp=\delta^2/(1+\delta^2)\). The \(q=1\) parallel amplitudes
therefore interfere constructively at positive source \(\delta\).
Droste's 9j expression reproduces this without the helicity calculation.
At \(\delta=+0.5\) the corrected scaled Stokes numerator is
0.796410161514. Using the printed phase yields 0.103589838486.

| E2/M1 coordinate for the same transition | Relation |
| --- | --- |
| Droste Eq. (5) and Krane--Steffen Eq. (9) | \(\delta_{\rm D96}=\delta_{\rm KS}\) for the same Bohr--Mottelson operator and state conventions |
| Bare \(CG\,D^*\) projection using the same analyzer gauge | \(\delta_{\rm bare}=-\delta_{\rm D96}\) |
| Rose--Brink normalized interaction RME ratio | \(\delta_{\rm RB}=-\delta_{\rm KS}\), from KS Eq. (5) and RB Eq. (3.39) |
| Biedenharn--Rose as related by KS Eqs. (12a,b) | \(\delta_{\rm BR}=-\delta_{\rm KS}\) for the populating gamma and \(+\delta_{\rm KS}\) for the radiating gamma |

KS Eq. (4b) uses the magnetic factor \(-i^{L-1}=i^{L+1}\).
Its electric factor is \(i^L\). Droste Eq. (5) uses the same factors
and an extra common transition normalization, so the M1 and E2 terms
share \(i^2\). This does not fix the CG/rotation basis by itself. Likewise
the KS Eq. (5) conversion to RB contains \((-1)^{I_i-I_f+L}\) after
absorbing \(\sqrt{2L+1}\) into the RB normalized ratio. The resulting
odd-rank/even-rank sign is separate from Starosta's primed-phase correction.
Use KS/Droste for production input, record source conventions when importing
signed values, and convert legacy bare-basis coordinates exactly once.

## Numerical checks

- The standalone suite passed 24 tests. It checks angle/spin normalization,
  pure E/M reciprocity, zero-spin cascades, both signs of the mixed anchor,
  DCO labels and detector inversion, and numerical gate marginals in both
  emission orders with a preceding step and a mixed gap. Full angular
  quadrature gives unit total probability for an aligned nonadjacent cascade.
- With \(x=\cos\beta\), the analytic scaled directional responses are
  \(3(1+x^2)/4\) for \(0\to1\to0\) and
  \(5(1-3x^2+4x^4)/4\) for \(0\to2\to0\). The electric relative-plane
  analyzer pairs are \((3x^2/4,3/4)\) and
  \((5(2x^2-1)^2/4,5x^2/4)\). The dipole pair follows from the
  transverse projector onto the unobserved photon's polarization plane.
  The quadrupole pair follows by rotating the projected \(m=\pm1\)
  substate along the gate direction and using \(d^2_{11}\pm d^2_{1,-1}\).
  Rotating these analyzer pairs geometrically to the lab meridian verifies
  both emission orders at noncoplanar and polar angles.
- For a nonadjacent \(0\to1\to1\to0\) case, the gap has \(U_0=1\),
  \(U_2(M1)=-1/2\), \(U_2(E2)=1/10\), and \(U_2=-0.38\) at
  \(\delta=\pm0.5\). The gap multiplies the rank-two parts of both the
  closed-form directional and Stokes responses by \(-0.38\).
- For \(5\to4\), \(\xi=+0.4\) rad and \(\sigma=1.5\), the separate
  source and radiation factors are \(B_2=-0.878251841624\) and
  \(A^{02}_{20}=-0.418073711391\). Their product is the coefficient
  \(+0.367174006964\) multiplying \(P_2\) in the singles distribution.
- A separate read-only production comparison of the seven `examples.py`
  configurations checked both raw linear channels in each emission order,
  both singles and both DCO ratios. Maximum absolute differences were
  \(4.66\times10^{-15}\) for scaled joint intensities,
  \(3.55\times10^{-15}\) for scaled singles, and \(1.78\times10^{-15}\)
  for DCO ratios. The comparison covered the `joint_channels` and
  `single_channels` physics entry points.

Droste Fig. 7 uses \(5\to4\to2\), \(\sigma=1.5\), an E2 second
transition, and the two polarization directions at \(90^\circ\) with
\(\Delta\phi=0\). The DCO ratio below puts the first photon at
\(0^\circ\) versus \(90^\circ\) in the numerator versus denominator.

| First transition | \(P_{\rm single}(1)\) | POL--DIR | DIR--POL | \(R_{\rm DCO}\) |
| --- | ---: | ---: | ---: | ---: |
| Pure E1 | 0.343428707 | 0.560408130 | 0.560408130 | 0.406200548 |
| Pure M1 | -0.343428707 | -0.560408130 | 0.560408130 | 0.406200548 |
| \(\arctan\delta=-70^\circ\) | 0.273255004 | 0.437181265 | 0.173582689 | 0.362034032 |
| \(\arctan\delta=+70^\circ\) | -0.177717135 | -0.498826923 | 0.675959927 | 1.355587917 |

The first and third rows reproduce the approximate values discussed on
p. 523. The article gives the mixed ratio as approximately 0.4. The
extra digits are reference calculations, with no digitization or refit.

Krämer--Flecken p. 334 Table 1 sets the second line as the gate and
gives \(90^\circ,38^\circ,18^\circ,\sigma/I=0.3\). Six rows match
the printed values within 0.005. Four rows give the following residuals
with the stated point geometry and a Gaussian standard deviation of
\(0.3I\). They remain unresolved as published-table replay checks.

| Cascade | Multipole orders | Printed | Reference |
| --- | --- | ---: | ---: |
| 10--8--7 | 2;2 | 0.66 | 0.637340759 |
| 10--8--8 | 2;1 | 1.07 | 1.029279931 |
| 9--8--7 | 1;2 | 0.92 | 0.970704300 |
| 9--8--8 | 1;2 | 1.12 | 1.188657467 |

The theory and experimental fractions on the same page label the generic
gate \(\gamma_1\) and target \(\gamma_2\); the numerator is target
in detector 1 with gate in detector 2. Table 1 uses the second **emitted**
line as gate. The reference treats detector labels, target/gate identities,
and emission order as independent inputs.

## Original evidence

| Original checked | Printed locator (one-based PDF page) | Local source record |
| --- | --- | --- |
| Droste et al., NIM A 378 (1996) 518--525, DOI `10.1016/0168-9002(96)00426-3` | p. 519 (2), Eqs. (1)--(6) and Fig. 2; p. 520 (3), Eqs. (7), (8), (12); p. 521 (4), Eqs. (13)--(16); p. 522 (5), Eqs. (19)--(21); pp. 523--524 (6--7), discussion and Fig. 7 | `knowledge/sources/droste-1996-pdco-formalism.md` |
| Starosta et al., NIM A 423 (1999) 16--26, DOI `10.1016/S0168-9002(98)01220-0` | p. 17 (2), Eq. (1) and footnote 1 | `knowledge/sources/starosta-1999-pdco-experimental-test.md` |
| Steffen & Alder, ch. 12 in W. D. Hamilton (ed., 1975) | p. 552 (563), Eqs. (12.209)--(12.213), including the radiative-only condition | `knowledge/sources/book-hamilton-electromagnetic-interaction.md` |
| D. R. Hamilton, Phys. Rev. 74 (1948) 782--788 | pp. 783--784 (2--3), Eq. (1) and the E/M interchange of transverse field axes | `knowledge/sources/hamilton-1948-successive-quanta-polarization.md` |
| Krämer--Flecken et al., NIM A 275 (1989) 333--339, DOI `10.1016/0168-9002(89)90706-7` | p. 334 (2), Fig. 1, directional/experimental fractions, Table 1 | `knowledge/sources/kramer-flecken-1989-use-dco-ratios.md` |
| Krane & Steffen, Phys. Rev. C 2 (1970) 724--734 | p. 727 (4), Eqs. (4a), (4b), (5), (9), (12a), (12b) | `knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md` |
| Rose & Brink, Rev. Mod. Phys. 39 (1967) 306--347 | p. 319 (14), Eq. (3.39) | `knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md` |

The Wiki worksheet `knowledge/methods/dco-pdco-ambiguity-worksheet.md`
provided the original KS/RB locators. The signed D96 implementation was
assembled directly from the original equations before reading the
production prototype or the worksheet's audit script.

## PDF coordinates and reported statistics

For $\xi=\arctan(\delta)$, the exported `marginal_delta.csv` evaluates
$p_\delta(\delta)=p_\xi(\arctan\delta)/(1+\delta^2)$, with the existing
adaptive coordinate refinement and numerical normalization. It is not the
angle density with a different horizontal-axis label.

The reporting convention evaluates all intervals and moments in the angle
PDF first. Display the resulting quantities as `tan{mode[arctan(δ)]}`,
`tan{HDI68%[arctan(δ)]}`, and `tan{mean[arctan(δ)]}`. Retain every angle HDI
component, its mass, and its transformed local mode ranges. Neither the
transformed mode nor the transformed HDI is generally the corresponding
statistic of the delta PDF. The transformed angle mean is not the arithmetic
mean of delta. `tan(mu +/- std)` denotes transformed endpoints only, with mu
and std evaluated on the angle PDF.

The angle HDI cutoff has density units per radian. On a delta density plot,
its transformed height would depend on delta as `cutoff / (1 + delta**2)`;
it must not be reused as a horizontal delta-density threshold. The evaluated
marginal renderer rejects the legacy mixed-coordinate aggregate for this
reason. Plot `summary.delta_pdf.coordinate` and `.density` directly when a
delta PDF without angle-based guides is wanted.

New result schema v3 separates `delta_pdf` from `tan_angle_statistics` in
`summary.json`. The latter has `tan_mode`, `tan_median`, `tan_mean`,
`tan_mean_std_endpoints`, and intervals containing `tan_eti`,
`tan_hdi_segments`, and `angle_hdi_threshold`; labels and cutoff coordinate
are stored explicitly. The Python views expose the same separation.
`Summary.delta` remains a legacy compatibility aggregate, not a newly
evaluated delta-statistics object. The loader accepts v1/v2/v3 without
rewriting stored files. No physical/statistical kernel, observation error,
floating-point precision or default 68% mass changes in this naming update.

## Run

```sh
python -m pytest tests/test_independent_reference.py tests/test_reference_bridge.py -q
PYTHONPATH=tests python -m reference.examples
```
