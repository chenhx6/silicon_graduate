# Supplemental fixed-exchange/monopole quadrupole path

**Result:** the sampled quadrupole-only path supports smooth reorientation of the
lowest \(J=11/2\) eigenbranch. Forward and backward maximum-overlap tracking both
retain state ordinal0 throughout. No lowest-state switching is observed on this
five-point path, and every sampled same-J gap remains above0.48MeV.

This supplements the [initial mechanism report](report.md). Its first-stage
endpoint caveat is resolved at the stated sampling resolution; no claim is made
about every unsampled parameter value.

## Prospective addendum and scope

[gamma-path-protocol.json](gamma-path-protocol.json) was written after the first
stage and before the three new interior results. The original `protocol.json`
and `controls.json` remained byte-identical. The new path is

\[
\Gamma_0=0.6s,\qquad \Lambda_0=1,\qquad A_0=-0.9,
\qquad s=0,\tfrac14,\tfrac12,\tfrac34,1 .
\]

Bare core, model space, occupation, signed \(Q_{jj}\), E2 operator,
\(e_B=0.1298423794528743\), \(e_F=0.125\), and \(\chi_{E2}=0.35\) remain fixed.
The target is always the lowest-energy \(J=11/2\) state.
The scalar results at0 and1 are reused from `remove_Gamma0` and `common_t1`.
The identical endpoint Hamiltonians were diagonalized only to recover
eigenvectors for overlap tracking and to check the energy, gap and state index.
**Only the three interior scalar points are new.** No broader grid or fit was run.

## Results

| \(s\) | \(\Gamma_0\) | Complete \(q_2\), \(e^2b^2\) | Proxy raw ratio, n5 | Proxy raw ratio, all | Static \(q_2\) fraction | \(P(R=0)\) | \(\langle n_d\rangle\) | Same-J gap, MeV |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0.680126 | 0.097372 | 0.087945 | 0.00009134 | 0.952237 | 2.353843 | 0.519131 |
| 0.25 | 0.15 | 0.691797 | 0.364214 | 0.357592 | 0.038911 | 0.917994 | 2.336507 | 0.481285 |
| 0.50 | 0.30 | 0.694132 | 0.666752 | 0.664207 | 0.155551 | 0.760371 | 2.323672 | 0.524753 |
| 0.75 | 0.45 | 0.686595 | 0.892091 | 0.890756 | 0.267015 | 0.597798 | 2.331223 | 0.645190 |
| 1 | 0.60 | 0.676623 | 1.026115 | 1.024144 | 0.336925 | 0.488610 | 2.348401 | 0.805218 |

The all-state proxy's real angle is28.3182°,23.0159°,16.1262°,9.01055°, then
**undefined**. The raw argument was never clipped. The complete folded
coordinate is27.5128°,27.4587°,27.9099°,28.5244°,29.0347°.

The gap and fidelity audit is:

| Adjacent \(s\) interval | Lowest-to-lowest squared overlap | Best right-state ordinal from left lowest | Best left-state ordinal from right lowest | Next-largest right-state overlap |
|---|---:|---:|---:|---:|
| 0→0.25 | 0.907396 | 0 | 0 | 0.0893374, ordinal1 |
| 0.25→0.50 | 0.907339 | 0 | 0 | 0.0900132, ordinal1 |
| 0.50→0.75 | 0.949921 | 0 | 0 | 0.0491535, ordinal1 |
| 0.75→1 | 0.979390 | 0 | 0 | 0.0203332, ordinal1 |

Both propagated rank sequences are `[0,0,0,0,0]`. The endpoint's relatively
small direct overlap0.342641 therefore accompanies accumulated wavefunction
rotation along a locally well-matched lowest branch. Its largest long-range
overlap with an excited state at the opposite endpoint is not evidence of a
sampled lowest-state switch.

## Mechanism sharpened by the path

The quadrupole term changes angular recoupling and static polarization while
total quadratic collectivity and d-boson number vary much less:

- Complete \(q_2\) remains between0.676623 and0.694132.
- \(\langle n_d\rangle\) remains between2.323672 and2.353843.
- The static fraction rises continuously at the sampled points from0.00009134
  to0.336925, while the other-same-J fraction falls from0.131700 to0.037406.
- \(P(R=2)\) grows from0.015090 through0.049547,0.233215,0.396579 to0.483684.
  The recorded full \(P(R)\) distribution accompanies this statement; the
  mechanism is not inferred from \(P(R=0)\) alone.

For the all-\(J+2\) proxy chain, the middle-diagonal contribution changes from
−0.734669 at0 to+0.022616,+0.627071,+0.836639,+1.167092. Thus the severe
diagonal/offdiagonal cancellation at the removed-quadrupole endpoint is
progressively replaced by reinforcement. Simultaneously the retained strength
\(S\) decreases:

| \(s\) | \(S=\sum|R_{ai}|^2\), \(e^2b^2\) | Signed chain \(C\), \(e^3b^3\) |
|---:|---:|---:|
| 0 | 2.320704 | 0.371616 |
| 0.25 | 2.154831 | 1.351943 |
| 0.50 | 1.922220 | 2.115725 |
| 0.75 | 1.741391 | 2.446549 |
| 1 | 1.625943 | 2.537874 |

These quantities enter \(\sqrt{7/10}|C|/S^{3/2}\) directly. They supply the
concrete signed-network explanation for the proxy's rising raw argument.
The complete6j cubic sum instead combines other spin sectors. At the primary,
its positive and negative sector sums are+0.290855702 and−0.318974338,
leaving−0.028118636 and the small signed full ratio−0.050521277.

The additional path therefore strengthens the conditional interpretation:
**at fixed exchange, monopole, core and E2 operator, quadrupole coupling smoothly
polarizes and recouples the sampled lowest11/2 branch, changes the restricted
chain's interference and denominator, and drives its shape-conversion argument
out of domain, while cross-spin cancellations keep the complete cubic ratio
small.** It is not an inference of an intrinsic axial state.

## Verification and boundaries

Each new interior point has complete reduced6j closure and an independent direct
contraction. The maximum absolute differences over the three new points are
\(2.37\times10^{-14}\ e^2b^2\) inq2 and
\(1.39\times10^{-14}\ e^3b^3\) inq3. Existing endpoint closure checks were reused.
Endpoint energies, gaps and state indices match their earlier results exactly.
Frozen input, initial-protocol and initial-result hashes were checked before
and after the supplemental execution.

Five points with resolved gaps and bidirectional matching support continuity at
this resolution. They are not a continuous-parameter theorem, a fitted critical
coupling or a parameter-uncertainty band. The full moment coordinate also retains
its finite-model/operator/fluctuation interpretation limits. The source-author
EM-figure replay and the independent137Ba static-calibration review remain
outside this task.

Artifacts: [gamma-path-summary.csv](gamma-path-summary.csv),
[gamma-path.json](gamma-path.json),
[run_gamma_path.py](run_gamma_path.py),
[gamma-path-execution.log](gamma-path-execution.log).
The JSON contains compact state/spin summaries for three new points, not a
state-pair matrix dump. All writes remained in the owned output directory.
