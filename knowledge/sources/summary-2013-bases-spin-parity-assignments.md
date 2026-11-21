---
type: source
title: "Summary of Bases for Spin and Parity Assignments"
aliases: [Summary of Bases 2013, 2013 spin-parity assignment guide, NDS spin and parity assignments summary]
created: 2026-07-09
updated: 2026-07-09
status: ai-draft
review_status: human-reviewed
source_type: reference-guide-article
reading_depth: deep-read
title_original: "Summary of Bases for Spin and Parity Assignments"
authors: []
journal: Nuclear Data Sheets
year: 2013
volume: 114
pages: viii-x
doi: 10.1016/S0090-3752(13)00011-2
language: en
canonical_source: doi:10.1016/S0090-3752(13)00011-2
citation_key: _2013_SummaryBases
raw_file: "raw/papers/2013_Summary of Bases for Spin and Parity Assignments.pdf"
raw_sha256: 8267F34C2423F5EBFDCD5E4DB1AA31E38472F4532392A26BD6E93EFC2767C6BB
observables: [angular-distribution-coefficient, multipole-mixing-ratio]
methods: [angular-distribution, dco-ratio, linear-polarization-asymmetry]
tags: [spin-parity-assignment, reference-guide, angular-distribution, dco-ratio, sigma-over-i, pado-support]
---

# Summary of Bases (2013): Spin/Parity Assignment Reference Guide

## Bibliographic Record

*Nuclear Data Sheets* **114** (2013) viii-x, DOI `10.1016/S0090-3752(13)00011-2`, citation key `_2013_SummaryBases`.

The PDF is a 3-page reference guide (`84178` bytes; local timestamp `2026-06-30 15:43:03`) rather than an original research article.

## Scope and Reading Depth

The full 3-page PDF was read. This ingest focuses on the guide's statements about high-spin spin/parity assignment, angular distributions, DCO ratios, and the status of regular-band arguments as strong or weak evidence.

This is a `reference-guide-ingest + targeted-ingest + project-ingest` source. It is not an original experiment and does not provide a theory derivation of `sigma-over-i`. Its role is to document reference-guide practice and terminology used in high-spin assignment work.

## Summary

The document is a compact reference guide listing propositions treated as strong or weak arguments for spin/parity assignments. For the current project, the relevant part is the high-spin section: it says high-spin spin/parity assignments are commonly constrained by angular distributions, DCO ratios, linear polarizations, internal conversion coefficients, and level-energy/intensity patterns.

Its most relevant targeted content is that the angular-distribution and DCO heuristics are stated for a typical `σ/I = 0.3`, with the magnetic-substate population parameter understood as the same `sigma` symbol family used in later Gaussian-substate descriptions. This is useful as experimental-practice background, but it remains a guide-level heuristic rather than a universal prior.

## Experimental or Theoretical Setup

Not an original experiment. The source is a compact Nuclear Data Sheets reference summary that collects assignment rules and heuristics from earlier literature.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SB13-1 | 该 guide 在 high-spin states 段明确说，重离子反应、裂变产物或 Coulomb excitation 中产生的高自旋态，其跃迁多极性与相对 `Jπ` 一般由 angular distributions、angular correlations (`DCO` ratios)、linear polarizations、internal-conversion coefficients，以及能级间距和强度随激发能变化等线索共同判定。 | reference-guide rule | direct | p.vi, "High-spin states" paragraph | false |
| SB13-2 | 在 high-spin reaction 的 gamma angular distribution 规则中，本文给出的是一个典型 `σ/I = 0.3`，其中 magnetic-substate population parameter 一般记为 `σ`；若 `A2 ≈ +0.3` 且 `A4 ≈ -0.1`，一般对应 `ΔJ = 2` stretched quadrupole。 | reference-guide rule | direct | p.iv, item 19 and heading "J Angular Distribution"; user audit | false |
| SB13-3 | 同一角分布规则还写明：若 `A2 ≈ -0.2` 且 `A4 ≈ 0`，一般对应 `ΔJ = 1` stretched dipole；若 `A4 > 0` 且 `A2` 约在 `+0.5` 到 `-0.8` 之间，则对应 `ΔJ = 1, D+Q`。 | reference-guide rule | direct | p.iv, item 19b-c | false |
| SB13-4 | 在 DCO 规则中，本文同样以典型 `σ/I = 0.3` 为前提：当 stretched quadrupole 作为 gating transition 时，`R(DCO) ≈ 1.0` 一般对应 stretched quadrupole，`R(DCO) ≈ 0.5` 一般对应 stretched dipole，显著偏离则多为 `D+Q`。 | reference-guide rule | direct | p.iv, item 20; user audit | false |
| SB13-5 | 当 stretched dipole 作为 gate 时，本文给出 `R(DCO) ≈ 2.0` 一般对应 stretched quadrupole，`R(DCO) ≈ 1.0` 一般对应 stretched dipole，显著偏离则多为 `D+Q`。 | reference-guide rule | direct | p.v, item 21 | false |
| SB13-6 | 对变形核，guide 认为只有在至少一个能级自旋宇称和至少一个 in-band 或 crossover transition 的多极性有较稳依据时，规则的 `ΔJ = 2` 或 `ΔJ = 1` rotational-band structure 指认才算 strong argument。 | reference-guide rule | direct | p.vi, item 37 | false |
| SB13-7 | 该 guide 还把“在缺少 angular distribution/correlation 或其他 supporting arguments 时，仅凭规则 gamma sequence 给高自旋带做 tentative spin-parity assignment”列入 weak arguments。 | reference-guide rule | direct | p.vi, "Propositions on which weak arguments are based", item 12 | false |

## Nuclear Structure Information

This source does not report new nucleus-specific measurements. It is a general reference guide for assignment practice and evidentiary strength.

## Authors' Interpretation

The document is not a narrative interpretation paper. Its main contribution is classification of assignment arguments into stronger and weaker categories.

## Model Results

None.

## Competing Interpretations and Limitations

- This is a guide page, not an original experiment.
- The high-spin angular-distribution and DCO rules are heuristic practice statements, not universal proofs.
- The guide-level parameter recorded for this project is `σ/I = 0.3`; it is still a heuristic practice value, not a universal prior.
- The guide itself explicitly retains ambiguity: several angular-distribution and DCO signatures are stated as "generally" true rather than unique.

## Project Relation

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this source supports the statement that empirical orientation parameters are routinely built into high-spin spectroscopy practice. It is useful background for saying that assignment heuristics are often quoted for a "typical" substate-population parameter.

The boundary is still critical: this guide gives a typical `σ/I = 0.3` as reference-guide practice language. It should therefore be cited as experimental-practice / reference-guide background, not as an original measurement and not as a primary theory source for a universal alignment-width prior.

## Extracted Pages

- Nuclei:
- Bands:
- Concepts:
- Methods: [[angular-distribution]], [[dco-ratio]], [[linear-polarization-asymmetry]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Human Review Triage

- P0 focus resolved: `SB13-2` / `SB13-4`, p.iv. The user review corrected this page to `σ/I = 0.3`, with the magnetic-substate population parameter understood as the same `sigma` symbol family used elsewhere in the project.
- P0 focus resolved: `Project Relation`. The Wiki keeps this source at the reference-guide background level and does not promote it into an original `sigma-over-i` theory or measurement source.
- P0 focus resolved: `SB13-7`, p.vi weak-arguments item 12. The guide explicitly downgrades band-assignment claims made without AD/correlation or other support.
- Remaining P0: none identified after the 2026-07-09 user review.
- P1: `SB13-1`, p.vi high-spin states paragraph, for the list of assignment observables.
- P1: `SB13-3`, p.iv item 19b-c, for the dipole and `D+Q` angular-distribution heuristics.
- P1: `SB13-5/SB13-6`, p.v--vi, for DCO gating conventions and strong-argument band criteria.

## Personal Notes

This guide is valuable because it records what spectroscopy practitioners treat as normal assignment heuristics. For the current project, the important caution is not a symbol split but scope: its "typical" `σ/I = 0.3` is guide-level practice language, not a universal prior that can simply be imported into every P-ADO fit.

## 2026-11-21 — Assignment heuristics and their scope

The three printed pages iv–vi were verified. Propositions 19–21 use the example magnetic-substate parameter \(\sigma/J=0.3\) to give angular-distribution and DCO heuristics for high-spin assignments. The DCO expectations depend on the stated stretched dipole or quadrupole gate and can overlap other spin paths. The guide neither counts fitting procedures in a defined literature population nor supplies a new measured \(P\) and \(\delta\) pair. Its contributions remain reference guidance.
