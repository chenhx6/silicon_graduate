---
type: project
title: "129Ba 同母态角分布一致性与混合比分支"
aliases: [129Ba rank-4 gate, 129Ba 365-keV companion-line audit]
created: 2026-11-05
updated: 2026-11-05
status: active
review_status: unreviewed
project_stage: source-audit-and-conditional-profile
publication_status: exploratory-draft-not-ready
confidentiality: public-summary-with-source-boundary
nuclei: [129ba]
tags: [a130, angular-distribution, mixing-ratio, rank4, identifiability, wobbling]
---

# 129Ba 同母态角分布一致性与混合比分支

## Research Question

Can a pure-\(E2\) companion transition from the same parent state provide a
necessary pre-fit check on a mixed \(M1/E2\) transition, before a
large-\(\lvert\delta\rvert\) or small-\(\lvert\delta\rvert\) branch is selected
for a collective-mode interpretation?

## Current Hypotheses

- H1: Under the shared selected-parent and pure-reference assumptions,
  rank four constrains \(f_{E2}s_4\). An independently calibrated nonzero
  \(s_4\) is required to identify \(\lvert\delta\rvert\); its sign is still lost.
- H2: The same-sign evaluated central \(A_4\) pair motivates a consistency
  investigation. Its noisy margins alone do not reject the experimental data.
- H3: The sign diagnostic alone cannot distinguish an invalid response
  contract from an incorrect historical coefficient or an incomplete
  reference-line assignment.

## Method and novelty boundary

The same-state pure-transition reference principle is already present in
[[diamond-1966-nuclear-alignment-heavy-ion-reactions]] D66-6/D66-9
(printed p.1206), and the angular formalism is standard
[[yamazaki-1967-aligned-angular-coefficients]] pp.1–2, Eqs.1–4.
The earlier draft's description of a new identification method is withdrawn.
What is under investigation is its application to this specific legacy pair;
publication-level novelty and empirical closure are unproven.

Under a same-parent, same-postselection, common-coefficient-layer contract,
with the target restricted to \(M1+E2\) and the reference treated as pure
\(E2\), the rank-4 coefficient obeys

\[
A_4^{(t)}=-\frac{8}{3}f_{E2}s_4A_4^{(r)},\qquad
f_{E2}=\frac{\delta^2}{1+\delta^2}.
\]

The \(-8/3\) factor is an exact angular-momentum result for
\(13/2\rightarrow11/2\) and \(13/2\rightarrow9/2\) \(E2\) channels. It
eliminates the common rank-4 alignment tensor without assuming a Gaussian
magnetic-substate population.

## Evidence Available

The evaluated \(^{129}\)Ba summary gives
\(A_4^{(t)}=+0.16(5)\) for the 364.7-keV target and
\(A_4^{(r)}=+0.08(5)\) for the 461.6-keV same-parent \(E2\) candidate. The
central relation requires \(f_{E2}s_4=-0.75\). Both one-sigma marginal
intervals are positive, so the positive-\(s_4\) contract is not closed by the
public summary.

This is a conditional response/readiness diagnostic. It does not prove that
the historical experiment is wrong, does not select the physical mixing-ratio
root and does not classify wobbling, signature partner or tilted precession.

## New primary source and uncertainty lineage

[[gizon-1977-ba129-angular-distribution-primary]] GI77-5 now has a full
13-page PDF and a visual Table 1 check. The original errors are
(0.05,0.05) for the target and (0.04,0.06) for the reference, confirming the
previous OCR lead. The reason for the smaller evaluation errors remains open.
The source versions are kept separate and are not independent data samples.

With the original reference error 0.06, the two-margin rank-4 boxes overlap
for s4=1. With evaluated errors, s4=1.125 already permits contact. In the
stronger four-coefficient check, a nonnegative common substate population at
chosen delta=-2 reaches a minimum common margin multiplier1.85768 for the
primary table (3.39629 for the evaluation). Primal and dual LP checks certify
the mathematical witness. It is not a measured population, confidence level,
reaction-realizability proof or mode assignment.

## Joint coefficient-space diagnostic

For the same selected parent, in the stated mixing-ratio phase,

\[
q(\delta)=\frac{-7+14\sqrt{11}\delta-\delta^2}{10(1+\delta^2)},\qquad
\frac{A_{2,t}}{A_{2,r}}=s_2q(\delta).
\]

The allowed Rayleigh-quotient range is
\([(-2-\sqrt{137})/5,(-2+\sqrt{137})/5]\). At \(s_2=1\),
the evaluated central ratio \(-35/11\) falls below the lower endpoint
\(-2.74094\); a positive \(s_2\ge1.16085\) can remove this central amplitude
obstruction. This is another condition on the same data, not independent
experimental evidence.

To avoid dividing by the weak \(A_{4,r}\), define
\(y=(A_{2,t},A_{4,t},A_{2,r},A_{4,r})\) and the two-rank response matrix
\(B_\delta\) in the manuscript. For fixed covariance,
\[
D(\delta)=\min_{b_2,b_4}(y-B_\delta b)^TV^{-1}(y-B_\delta b).
\]
Free real reference coefficients relax population-positivity constraints.
With \(s_2=s_4=1\) and chosen diagonal errors, the evaluated case gives
\(D_{\min}=12.8797\), at diagnostic \(\delta=-1.0270\), and
\(D_{\rm small}-D_{\rm large}=0.01356\).
The primary-table case gives \(8.2357\), \(-1.2412\) and \(0.46848\).
These are scenario-specific model diagnostics, not revised experimental roots.

The 50-cell analysis uses two scale scenarios and a \(5\times5\)
Kronecker correlation family. Even with cross-line correlation fixed to zero,
the evaluated small-minus-large ordering changes sign across the specified
within-line correlation slice. No actual covariance, calibrated p-value,
confidence interval or branch probability is obtained.

## Risks and Blockers

- The 2024 PRC result is a reanalysis of legacy observables and reports a
  large-root solution as a possibility/likely interpretation.
- The ENSDF rows are evaluated summary coefficients, not raw counts.
- The 461.6-keV \(E2\) label is a candidate reference input; purity,
  higher-multipole contamination, gate identity, finite-angle response and
  covariance remain unverified.
- \(s_4=Q_{4,t}/Q_{4,r}\) must be measured or modeled with its sign and
  uncertainty. It cannot be silently set to one in a final experimental
  claim.
- The public record lacks event counts, detector response, feeding history,
  lifetime and absolute branching information.
- Different postselection belongs to the nuclear \(\rho_k\) layer; reference
  contamination changes the radiation operator. Neither may be silently
  renamed as an instrumental \(Q_k\) effect.
- Standard same-parent algebra and a compiled draft do not establish a
  publishable innovation.

## Reproducibility

The article package is
`raw/writing/gpt/ba129-rank4-identifiability/`. The self-contained script
`analysis/rank4_invariant.py` verifies the exact \(-8/3\) and \(64/9\) algebra,
the public central diagnostic, literal marginal-box controls and a synthetic
algebra control. `analysis/companion_profile.py` implements the fixed-covariance
profile without a ratio-Gaussian approximation. Independent standard Wigner
symbols, direct photon projections for all 14 parent substates, direct GLS,
grid refinement and invalid-input checks are in `analysis/validate_case.py`.
The data contract records actual upstream hashes and the separate source-version roles.

## Next Actions

1. The 1977 scan is obtained; seek the 1978 revision/evaluation record to
   resolve the uncertainty lineage.
2. Establish response ratios, selected-parent identity, reference purity and
   covariance before interpreting any inferred root.
3. Test an independently characterized companion pair or a fully declared
   observation model to establish practical information gain and coverage.
4. Reassess novelty against the established reference method; retain this as
   an exploratory application if it cannot support a focused paper.
5. For a separate nuclear-structure follow-up, use Gizon1977 GI77-8 (p.475)
   as the motivation for an energy-calibrated electromagnetic prediction
   test. The original paper reports poor EM agreement despite useful energy
   systematics; reproducing energies alone does not resolve that limitation.

### Source-internal control discovered during continuation

[[zobel-1979-high-spin-states-67ga]] provides an archived, visually readable
Table 2 (printed p.171): the 843.161-keV \(7/2^-\to5/2^-\) and
1202.249-keV \(7/2^-\to3/2^-\) lines have \(A_4=0.156(30)\) and
\(-0.097(9)\). The corresponding pure-\(E2\) factor ratio is \(-16/9\).
At the explicitly assumed response ratio one, their coefficient ratio gives
\(f_{E2}=0.904639\), or \(\lvert\delta\rvert=3.080014\), near the paper's
3.1(3) (Table 2) and 3.08 (p.175). This is a conditional reconstruction.
Because the source uses its own angular/alignment analysis, this may reproduce
the same information that generated its reported mixing ratio. It is an
internal arithmetic/definition control, **not an independent holdout**.
It does not establish the signed phase or experimental coverage, and it is
not pooled with 129Ba.

## Related sources

- [[chakraborty-2024-possibility-wobbling-129ba]]
- [[chakraborty-2024-ba129-365-mixing-ratio-arxiv-v3]]
- [[nndc-2014-129ba-365-coefficient-records]]
- [[gizon-1977-ba129-angular-distribution-primary]]
- [[diamond-1966-nuclear-alignment-heavy-ion-reactions]]
- [[yamazaki-1967-aligned-angular-coefficients]]
- [[ba129-365-mixing-reference-boundary]]
- [[multipole-mixing-ratio]]
- [[angular-distribution]]

The physical-model route is maintained separately in [[ba129-model-input-and-holdout-contract]], using transfer strengths and lifetimes without expanding this angular-consistency draft into an omnibus paper.
