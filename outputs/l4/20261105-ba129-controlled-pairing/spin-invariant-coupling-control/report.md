# 135Ba fixed-core coupling control

**Result:** in this frozen finite model, quadrupole coupling reorganizes the
angular-momentum and signed E2 network; the attractive monopole term enhances the
restricted ratio mainly through its denominator, while the exchange term
counteracts the excursion. The complete cubic scalar has strong cancellation
between spin sectors. The resulting discrepancy concerns the raw proxy ratio
and its conversion domain: the calibrated primary proxy has **no real angle**,
while the complete folded moment coordinate is29.034704degrees.

This is a conditional model-intervention result. It does not establish an
intrinsic axial shape, gamma rigidity/softness, a unique microscopic explanation
for real135Ba, or a correction to the source author's figures.

**Supplement completed:** the separately frozen
[fixed-exchange/monopole Gamma path](gamma-path-report.md) adds exactly three
interior points. Bidirectional overlap tracking keeps the lowest state at all
five points, with minimum fidelity0.907339 and minimum same-J gap0.481285MeV.
This supports smooth reorientation at that sampling resolution and addresses
the first-stage endpoint-only ambiguity below. The original protocol and
numerical results remain unchanged.

## Frozen question and exact primary match

[protocol.json](protocol.json) was written before any new control run. It
declares the base grid, three single-term removals, diagnostics, and a bounded
refinement rule. It acknowledges that the earlier core-only pilot and the
parent's calibrated primary endpoint were already known. This is an internal
prospective diagnostic, not external preregistration.

The target is the lowest-energy \(J=11/2\) state in the complete
\(sd^{N_B=5}\otimes h_{11/2}\) representation: full dimension3024 and
fixed-\(M=1/2\) dimension226. The frozen parameters are

```text
eps_d=0.38, kappa=-0.124, chi=-0.24, v2=0.81
Q_jj=-1.081027387032316
Gamma0=0.6, Lambda0=1.0, A0=-0.9
chi_E2=+0.35, eF=0.125 eb
core134 B(E2;0->2)=0.679 e^2 b^2
eB=+0.1298423794528743 eb
```

The same core calibration was reconstructed once as an identity check and then
held fixed. The even-core Hamiltonian, \(v^2,Q_{jj},e_B,e_F,\chi_{E2}\) remain
unchanged in every intervention. Zero boson–fermion Hamiltonian coupling at
\(t=0\) does not turn off the fermion term in the E2 operator.

At \(t=1\), the independently executed endpoint matches the135Ba entry of
[parent study.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/shape-closure-v1/study.json)
exactly at the recorded floating-point precision for q2, q3, full ratio,
static/other-same-J fractions, both proxy ratios and signed spin-sector sums:

| Quantity | Matched primary value |
|---|---:|
| Complete \(q_2\), \(e^2b^2\) | 0.676622789828095 |
| Complete signed \(q_3\), \(e^3b^3\) | −0.0281186360017683 |
| \(q_3/q_2^{3/2}\) | −0.050521276780232 |
| Signed / folded moment coordinate | 30.965296246° /29.034703754° |
| \(J+2,n=5\) raw ratio | **1.026114564730946**, angle undefined |
| All25 \(J+2\) states, raw ratio | **1.024144142719368**, angle undefined |
| Static \(q_2\) / full \(q_2\) | 0.336925367778404 |
| Other same-J \(q_2\) / full \(q_2\) | 0.037405571706288 |

No material out-of-domain ratio was clipped.

## Prospective common-coupling path

The common control is
\((\Gamma_0,\Lambda_0,A_0)\mapsto t(\Gamma_0,\Lambda_0,A_0)\).
Direct lab contraction and independent complete reduced-6j closure were required
at every point.

| \(t\) | Complete \(q_2\) | Full signed ratio | Full folded coordinate, ° | Proxy raw ratio, n5 | Proxy raw ratio, all | \(P(R=0)\) | Same-J gap, MeV |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.738911 | −0.180048 | 26.542489 | 0.163372 | 0.165740 | 1.000000 | 0.598055 |
| 0.25 | 0.742737 | −0.158433 | 26.961358 | 0.484102 | 0.487410 | 0.899396 | 0.578016 |
| 0.50 | 0.725564 | −0.120412 | 27.694700 | 0.745797 | 0.748366 | 0.714379 | 0.676931 |
| 0.75 | 0.701706 | −0.082626 | 28.420154 | 0.914936 | 0.915192 | 0.577421 | 0.770583 |
| 1 | 0.676623 | −0.050521 | 29.034704 | 1.026115 | 1.024144 | 0.488610 | 0.805218 |

The predeclared largest-argument-change rule selected the interval0–0.25 for one
round of refinement, adding \(t=0.0625,0.125,0.1875\). The all-channel proxy
ratios there are0.243984,0.325572,0.407688. These points resolve a smooth early
reconfiguration; they do not reveal a sharp jump. The conversion-domain crossing
is bracketed by the sampled points0.75 and1; no critical value was fitted.

The smallest sampled same-J gap on the common path is0.565763MeV.
Every adjacent maximum-overlap match remains the lowest state of that spin;
the smallest adjacent squared overlap is0.933805. This supports continuity
through the sampled path and gives no sampled evidence of a level swap. It is
not a mathematical proof against every unsampled crossing.

Long-range endpoint overlaps require care: the \(t=1\) state has overlaps0.432372
and0.437353 with the lowest and first-excited \(J=11/2\) states at \(t=0\).
That nearly tied, long-range match does not overturn the local continuation
checks or demonstrate a crossing.

## Which coupling changes the anomaly?

Only the named coefficient is removed; the other two retain their primary
values. The state selection remains lowest-energy \(J=11/2\).

| Intervention | Proxy ratio n5 / all | Full folded coordinate, ° | Static \(q_2\) fraction | \(P(R=0)\) | Overlap with primary lowest |
|---|---:|---:|---:|---:|---:|
| Primary | 1.026115 /1.024144 | 29.034704 | 0.336925 | 0.488610 | 1 |
| Remove quadrupole \(\Gamma_0\) | 0.097372 /0.087945 | 27.512791 | 0.00009134 | 0.952237 | 0.342641 |
| Remove exchange \(\Lambda_0\) | 1.177982 /1.179809 | 29.895910 | 0.410910 | 0.366059 | 0.965830 |
| Remove monopole \(A_0\) | 0.827138 /0.832888 | 27.600058 | 0.262155 | 0.632227 | 0.867805 |

The quadrupole removal is a strong intervention on the defined lowest-state
observable, but **not a verified same-character adiabatic comparison**:
the primary state overlaps more with the first excited same-J state of the
quadrupole-removed Hamiltonian (0.433387) than its lowest state (0.342641).
The latter still has a0.519131MeV same-J gap. The interpretation is therefore
conditional on the requested energy-ranked state, with substantial
reconfiguration. No separate quadrupole-only continuation was available at this
initial stage; the supplemental report above supplies that continuation.
No refit was performed.

The exchange- and monopole-removed endpoints both have their largest primary
overlap in the lowest same-J state. Their removal responses give opposite signs:
the exchange term suppresses the excursion in this model, while the monopole
term helps the primary cross the proxy's angle domain.

## Concrete matrix-element mechanism

Define, over all \(J'=J+2=15/2\) intermediate states,

\[
S=\sum_a |R_{ai}|^2,\qquad
C=\sum_{ab}R_{ai}^{*}R_{ab}R_{bi},\qquad
r_{\rm proxy}=\sqrt{7/10}\,\frac{|C|}{S^{3/2}}.
\]

These are restricted, rotationally invariant quantities. Their normalization
and angular weights differ from the complete polynomial scalar.

| Case | \(S\), \(e^2b^2\) | Signed \(C\), \(e^3b^3\) | Middle-diagonal part of \(C\) | Middle-offdiagonal part of \(C\) |
|---|---:|---:|---:|---:|
| \(t=0\) | 2.362643494 | 0.719408921 | −0.602087715 | 1.321496636 |
| Primary | 1.625942884 | 2.537873635 | 1.167091825 | 1.370781810 |
| Remove quadrupole | 2.320703958 | 0.371615505 | −0.734668517 | 1.106284022 |
| Remove exchange | 1.420763364 | 2.388061263 | 1.307720072 | 1.080341191 |
| Remove monopole | 1.967365853 | 2.747042284 | 1.372068138 | 1.374974146 |

Along the common path from0 to1, \(C\) increases by a factor3.52772, while \(S\)
falls to0.688188 of its initial value. Together they increase the raw proxy
ratio by a factor6.17922. The middle-diagonal contribution changes sign. This
explicit signed-network change explains the ratio, rather than assigning
causal meaning to \(P(R=0)\) alone.

The quadrupole removal makes the distinction particularly concrete:
total \(q_2\) changes only **+0.5178%**, and \(\langle n_d\rangle\) changes only
**+0.2317%**, relative to the primary. Yet the static diagonal reduced matrix
element changes from1.653982 to−0.027303eb, the static \(q_2\) fraction falls
from33.6925% to0.00913%, and the restricted cubic chain becomes strongly
cancelled between its negative diagonal and positive offdiagonal parts.
The main response is angular recoupling and static/network polarization,
without a comparable change in total quadratic collectivity or d-boson number.

The monopole term is exactly \(A_0 n_d\) in the validated one-fermion kernel.
Keeping the bare core fixed, its presence changes the effective coefficient of
\(n_d\) in the odd Hamiltonian from0.38 to−0.52MeV. Relative to the monopole-removed
control, the primary has \(\langle n_d\rangle=2.348401\), instead of1.491237.
Its \(S\) is0.826457 times as large and its \(C\) is0.923857 times as large.
Thus the smaller \(S^{3/2}\) dominates, increasing the proxy ratio by22.963%
and moving it from0.832888 to1.024144. The scalar core Hamiltonian itself and
the E2 calibration were not changed.

Removing exchange decreases \(S\) further and produces the larger raw
ratio1.179809. The exchange term is therefore a conditional counteracting term
at these fixed parameters, not the necessary origin of the out-of-domain
primary ratio. Single-term ablations do not provide additive or universally
unique causal fractions.

## Why the complete ratio remains close to zero

The complete signed cubic sum in the primary is

\[
q_3=(+0.2908557020)+(-0.3189743380)
=-0.0281186360\ e^3b^3.
\]

With the spin-sector cancellation measure
\(1-|\sum c|/\sum|c|\), the cancellation is95.3891%.
The value of this measure depends on the explicitly stated grouping; the
spin-pair grouping is primary here.

Important ordered-spin sectors, already including their6j coefficients, are:

| Sector or combined sectors | Signed contribution, \(e^3b^3\) |
|---|---:|
| \((11/2,11/2)\) | +0.123349978 |
| \((11/2,13/2)+(13/2,11/2)\) | +0.119499714 |
| \((11/2,15/2)+(15/2,11/2)\) | −0.098360809 |
| \((7/2,11/2)+(11/2,7/2)\) | −0.087013965 |
| \((15/2,15/2)\) | −0.063823383 |

The complete \(15/2,15/2\) contribution is−0.0638233833, and all other spin
sectors sum to+0.0357047473. Their normalized contributions to the full ratio
are−0.114672661 and+0.064151384, giving−0.050521277.
The unweighted absolute proxy chain cannot represent this cancellation.

Static and dynamic same-J terms are distinct:

```text
static q2                         = 0.2279713823 e^2 b^2 = 33.6925% of full q2
other same-J q2                   = 0.0253094623 e^2 b^2 =  3.7406% of full q2
initial triple (i,i intermediates)= +0.0984687516 e^3 b^3
exactly one initial intermediate  = -0.0306731015 e^3 b^3
neither intermediate is initial   = -0.0959142861 e^3 b^3
```

Even the large positive initial triple is outweighed by the remaining signed
loops. The entire same-J quadratic strength cannot be called static, and the
static triple alone cannot determine the full cubic coordinate.

Only20.0252% of the complete quadratic scalar belongs to all \(J+2\) states.
The first five retain99.8539% of that sector. Increasing from five to all25
changes the proxy ratio by only0.00197042; both remain outside the real-angle
domain. The within-channel state cutoff therefore does not repair the missing
cross-spin cancellations or the shape-conversion regime.

The primary core-spin probabilities are
\(P(R=0)=0.488610\), \(P(R=2)=0.483684\), \(P(R=4)=0.0275363\), with the
remaining probabilities stored in the compact JSON. The core ground-state
probability is0.432372; it is not the total R=0 probability. These composition
changes support the network interpretation but are not the sole causal test.

## Numerical and scientific limits

Across11 points, the largest reduced-minus-direct residual is
\(2.25\times10^{-13}\ e^2b^2\) forq2 and
\(1.44\times10^{-13}\ e^3b^3\) forq3. Every required reduced closure is complete,
and probability/energy/decomposition checks pass.
All numerical producer and frozen-input hashes were checked before and after
execution. `checks.json` records the final local reconciliation.

The driver forces OpenBLAS/OMP/MKL/BLIS/NumExpr/VecLib thread environment values
to1 before importing NumPy/SciPy; the launch also set single-thread variables.
The optional `threadpoolctl` package was unavailable, so a separate runtime
thread-count query is not claimed. Nothing was installed or configured.

The main evidence comes from the declared interventions and signed contractions,
not a fit, calibration-error scan, or claimed physical phase transition.
The complete angle is a conditional moment coordinate, not a unique static
shape. The source/operator replay issue discussed in the
[precedent review](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-precedent-review/audit.md)
and [pilot assessment](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-precedent-review/pilot-assessment.md)
remains in force. Restricted proxies are legitimate rotational scalars; the
issue here is their information content and conversion domain.

## Compact artifacts and replay

- [summary.csv](summary.csv):11 scalar control rows.
- [controls.json](controls.json): full/reduced moments, core probabilities,
  static decomposition,19 nonzero signed spin-pair sectors per point, and
  overlap/gap diagnostics; approximately97kB, no state-pair arrays or RMEs.
- [cubic-spin-sectors.csv](cubic-spin-sectors.csv): compact ordered-spin
  contributions, with no redundant state-pair dump.
- [protocol.json](protocol.json), [run_controls.py](run_controls.py),
  [execution.log](execution.log): prospective design, producer and execution.

Replay in a fresh copy of this output directory, retaining the same root-relative
input locations:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
PYTHONDONTWRITEBYTECODE=1 python3 -u -B run_controls.py
```

The driver refuses to overwrite `controls.json`. Only this new output subtree
was written; frozen producers, parent study, chain contract, calibration,
other sessions, PLAN and get-paper were not modified. No test suite belonging
to another session, installation, configuration change or commit was performed.
