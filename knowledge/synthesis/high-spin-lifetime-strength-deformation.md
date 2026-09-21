---
type: synthesis
title: "High-spin lifetimes, transition strengths and deformation"
aliases: [高自旋寿命跃迁强度形变综合]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
scope: high-spin-lifetime-strength-deformation
confidence: medium
sources: [mukhopadhyay-2007-135nd-chiral-vibration-static, mukhopadhyay-2008-136nd-transition-rates, petrache-2006-near-degenerate-chiral-misinterpretation, petrache-2018-chiral-bands-even-even-136nd]
tags: [high-spin, lifetime, transition-strength, deformation, evidence-map]
---

# High-spin lifetimes, transition strengths and deformation

## Question and Scope

This synthesis follows the evidence chain from level identity and line shape to lifetime, transition strength, alignment and deformation interpretation.

## Evidence Matrix

`coincidence gates → Doppler shift/line shape → stopping and feeding model → τ → B(M1)/B(E2), Qt → configuration/deformation interpretation`

The chain is explicit in Jensen, Mukhopadhyay 2007/2008, Petrache, Herzan and the lifetime-method review. The uncertainty is carried by stopping powers, side feeding, gate choice, branching normalization and configuration assignment.

## Synthesis

The `136Nd` history is a useful internal control. Early near-degenerate bands were discussed as possible chiral partners, but Mukhopadhyay 2008 found substantially different `B(E2)` values and favored distinct configurations with band mixing. Petrache 2006 reached the same methodological warning from `134Pr/136Pm` crossing, alignment and quadrupole-moment analysis. Petrache 2018 later strengthened one `136Nd` pair with partner-resolved strength while retaining four weaker candidates. These papers form a chronological evidence gradient, not contradictory labels to average.

## Model Dependence

- `Qt` and `B(E2)` are observables derived through analysis assumptions; they are stronger than energy proximity but do not directly measure an intrinsic shape.
- A band crossing can change alignment and transition strengths without establishing a phase transition.
- Magnetic-rotation and band-termination interpretations require configuration tracking and, where possible, lifetimes and moments.
- Review sources organize methods and examples; they do not add independent replications.

## Counter-evidence

Band crossings, configuration mixing and stopping/feeding alternatives can reproduce energy or strength changes without a unique shape transition.

## Open L3 questions

- Which partner-resolved strength set is minimally sufficient to reject crossing and configuration-mixing alternatives?
- Can DSAM and RDDS results be compared after harmonizing stopping, feeding and transition identity?
- Which observables distinguish a shrinking quadrupole collectivity at termination from a change of configuration?

## Limitations and Missing Evidence

The batch does not contain a complete common raw-data and response package for a reproducible L4 re-fit. Future L4 work requires an explicit data path, transition map, stopping model, uncertainty propagation and a negative/control case.

## Sources

- [[mukhopadhyay-2007-135nd-chiral-vibration-static]], [[mukhopadhyay-2008-136nd-transition-rates]]
- [[petrache-2006-near-degenerate-chiral-misinterpretation]], [[petrache-2018-chiral-bands-even-even-136nd]]
- [[jensen-2001-165tm-h9-2-configuration]], [[herzan-2015-193bi-spectroscopy]], [[nolan-sharpey-schafer-1979-lifetime-measurements]]
- [[afanasjev-1999-termination-rotational-bands]], [[walker-dracoulis-2001-exotic-isomers]]

## Self-audit

- Experimental strength, author interpretation and model calculation are kept in separate layers.
- The `136Nd` conclusion is pair-specific and does not generalize automatically to all chiral candidates.
- This synthesis is a Codex self-audit and remains unreviewed.
