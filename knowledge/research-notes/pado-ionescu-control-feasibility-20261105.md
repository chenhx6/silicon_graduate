---
type: research-note
title: "Ionescu 1981 as an independent public control for the P-ADO audit"
aliases: [Ionescu 1981 P-ADO control feasibility, feeding-aware angular-distribution control]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [ionescu-1981-improved-angular-distribution-analysis-particle-xn, yamazaki-1967-aligned-angular-coefficients]
scope: pado/public-control/feeding-aware-angular-distribution
nuclei: [167tm]
tags: [pado, angular-distribution, feeding, gaussian-hypothesis, public-control, evidence-boundary]
---

# Ionescu 1981 as an independent public control for the P-ADO audit

## Question

Can the `165Ho(alpha,2n)167Tm` angular-distribution data of Ionescu et al.
(1981) be added as a second public benchmark for the
`pado-alignment-response-dependence` article?

## Directly available fields

The archived nine-page paper provides:

- ten pure-\(E2\) rows in Table 1, with experimental and calculated
  \(A_2,A_4\), quoted errors, total intensity \(I_T\), peak-role labels and
  \(\rho_2,\rho_4\)-like population factors;
- three mixed/E1 interband groups in Tables 2--3, with angular-distribution
  coefficients, allowed width intervals, \(\Delta J\) hypotheses and
  `arctan(delta)` branches;
- a source-specific feeding-aware model in Eqs. (9)--(11), where a Gaussian
  side-feeding term is combined with discrete direct feeding through the
  yrast region.

The source explicitly reports that the global Gaussian population hypothesis is
inadequate for this studied `167Tm` case. It then constrains the population
model with pure-\(E2\) transitions before fitting mixed-transition mixing ratios.

## Why it cannot be pooled with the \(^{67}\)Ga audit

The paper is a strong methodological precedent, but it is not a drop-in second
sample for the current common-\(\rho\) statistic:

1. the source uses \(\rho_2,\rho_4\) statistical-tensor factors and radiative
   \(A_2,A_4\), whereas the \(^{67}\)Ga package uses finite-\(J\)
   attenuation-style \(\alpha_2,\alpha_4\);
2. the Ionescu model requires parent tensors, disorientation coefficients,
   angle-averaged conversion-corrected intensities and discrete feeding paths;
3. the source does not publish the complete per-row covariance, detector
   response, all parent inputs or the full fit grid;
4. the `167Tm` rows have different spin sequences, feeding history, reaction
   conditions and notation contracts from the \(^{67}\)Ga table;
5. treating the ten Ionescu rows as another common-\(r\) sample would silently
   impose the very transfer assumption that the source warns against.

## Control value that is supportable now

Ionescu 1981 can be used as an **independent public negative precedent**:
it shows that a pure-\(E2\)-first, feeding-aware population audit can reject a
global Gaussian description in a carefully measured case. It can support the
motivation and discussion of the EPJ A paper, while remaining a separate source
lineage and a separate analysis contract.

It cannot currently support a second numerical \(T_{\mathrm{prof}}\), a pooled
coverage curve, or a cross-nucleus estimate of a universal alignment response.

## Minimum future control design

If a second numerical control is needed, the next bounded task is to create a
separate `ionescu1981` control package containing:

- a source-transcribed Table 1 CSV with `A2`, `A4`, \(\rho_2\), \(\rho_4\),
  errors, spin/transition identity and peak-role fields;
- an explicit notation map to Yamazaki \(p_k/B_k\) and a sign-convention audit;
- a source-replay check against the printed improved-model rows;
- a declared feeding-aware forward model with all missing inputs marked
  `needs_review`;
- no pooling with the \(^{67}\)Ga common-\(\rho\) sample unless a complete
  covariance and response contract is obtained.

## Decision

For the current manuscript, use Ionescu 1981 as a verified methodological
precedent and explicit limitation. Do not claim that an independent numerical
public control has been completed. The \(^{67}\)Ga table remains the only
quantitative benchmark in the article.
