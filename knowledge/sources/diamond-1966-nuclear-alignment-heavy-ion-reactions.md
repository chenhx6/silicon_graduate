---
type: source
title: "Nuclear Alignment in Heavy-Ion Reactions"
aliases: [Diamond 1966 nuclear alignment, heavy-ion reaction alignment]
created: 2026-07-13
updated: 2026-07-13
status: ai-draft
review_status: human-reviewed
source_type: journal-article-experiment-method
reading_depth: deep-read
title_original: "Nuclear Alignment in Heavy-Ion Reactions"
authors: [R. M. Diamond, E. Matthias, J. O. Newton, F. S. Stephens]
journal: Physical Review Letters
year: 1966
volume: 16
number: 26
pages: 1205-1207
doi: 10.1103/PhysRevLett.16.1205
language: en
canonical_source: doi:10.1103/PhysRevLett.16.1205
zotero_item_key:
citation_key: diamond_1966_NuclearAlignment
zotero_uri:
library_file:
raw_file: "raw/papers/1966_Diamond et al_Nuclear Alignment in Heavy-Ion Reactions.pdf"
raw_sha256: 06FB82ECEBC0F1DA5441CAA5FB9272D481F469B1B39F402342AD31C8E55C8614
nuclei: [199tl]
reactions: ["heavy-ion (HI,xn)", "197Au(4He,2n)199Tl"]
experiments: []
models: [compound-nucleus-reaction-model]
observables: [angular-distribution-coefficient]
methods: [angular-distribution, gamma-ray-spectroscopy]
tags: [nuclear-alignment, heavy-ion, compound-nucleus, magnetic-substate-population, pado-support]
---

# Diamond et al. (1966): Nuclear Alignment in Heavy-Ion Reactions

## Bibliographic Record

Physical Review Letters 16 (1966) 1205-1207. DOI `10.1103/PhysRevLett.16.1205`; BibTeX key `diamond_1966_NuclearAlignment`.

## Scope and Reading Depth

Full three-page Physical Review Letters article deep-read. The paper is an early heavy-ion alignment and angular-distribution study, not a modern universal prescription for magnetic-substate populations. Its 199Tl example is kept as an example rather than as the scope of every heavy-ion reaction.

## Summary

The authors connect the entrance-channel orbital angular momentum of a heavy-ion fusion-evaporation reaction to alignment of the compound and residual nuclei, then test the persistence of that alignment with stretched-E2 angular distributions. The data are broadly compatible with a Gaussian magnetic-substate population centered at m=0, but the paper explicitly shows deviations from that simple approximation. It also explains how a calibrated alignment can reduce spin-sequence ambiguity and support mixed-transition E2/M1 mixing-ratio estimates.

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| D66-1 | In a heavy-ion fusion-evaporation reaction, the entrance orbital angular momentum contributes predominantly to m=0 substates when the beam direction is used as the quantization axis; because the orbital contribution is large, the compound nucleus is expected to be strongly aligned perpendicular to the beam. | method-formalism / author interpretation | direct | PDF p.1205, first column | false |
| D66-2 | Target and projectile intrinsic spins can produce deviations from the ideal entrance-channel alignment. Evaporation of a few neutrons is described as leaving the initial spin distribution largely intact while broadening the m distribution, because the evaporated neutrons carry relatively little angular momentum. | author interpretation | direct | PDF p.1205, first column | false |
| D66-3 | The paper reports pronounced anisotropies in stretched-E2 cascades from a set of twelve heavy-ion reactions producing nuclei in the mass-160--200 region. | observed fact | direct | PDF p.1205, Fig. 1 discussion | false |
| D66-4 | The angular distribution is written as W(theta) = 1 + A2 P2(cos theta) + A4 P4(cos theta). For the stretched-E2 comparison, the expected A4--A2 relation for a Gaussian m-substate population centered at m=0 is used as an approximate reference; the measured points show significant deviations from the simple curve. | method-formalism / observed fact | direct | PDF p.1205, Fig. 1 and caption | false |
| D66-5 | The plotted A2 and A4 values cluster near the approximate averages A2 = +0.30 +/- 0.09 and A4 = -0.09 +/- 0.05, with the precise point-by-point values supplied by Fig. 1 rather than by a universal alignment law. | observed fact | direct | PDF p.1205, Fig. 1 caption/discussion | false |
| D66-6 | Angular-distribution coefficients can constrain candidate spin sequences through their signs and magnitudes. Transitions emitted from the same initial state must be consistent with one common alignment description. | method-formalism | direct | PDF p.1206, discussion of Fig. 2 | false |
| D66-7 | In the example 197Au(4He,2n)199Tl reaction, the 331-, 370- and 701-keV transitions above a 749-keV isomeric level show large anisotropies. | observed fact | direct | PDF p.1206, Fig. 2 and surrounding text | false |
| D66-8 | For the 199Tl example, angular distributions alone reduce the number of possible spin sequences, and an expected alignment range reduces it further; conversion coefficients and other independent information are then needed to select among the remaining candidates. | method-formalism / author interpretation | direct | PDF p.1206, Fig. 2 discussion | false |
| D66-9 | When the initial alignment can be deduced, for example from a pure transition emitted by the same state, the angular distribution of a mixed transition can be used to infer an E2/M1 amplitude mixing ratio. Without an alignment calibration, only a probable range is justified. | method-formalism | direct | PDF p.1206, paragraph following Fig. 2 | false |
| D66-10 | Alignment is useful only while it is not destroyed by extranuclear interactions. The authors discuss recoil transport and host materials as experimental boundary conditions that can attenuate or preserve angular distributions. | author interpretation / limitation | direct | PDF pp.1205-1207, alignment and host-material discussion | false |
| D66-11 | The paper concludes that a large and reasonably uniform alignment can persist through neutron and gamma cascades under suitable reaction and environment conditions, making it useful for spin and multipolarity assignments and for nuclear-moment studies. | author interpretation | direct | PDF p.1207, concluding paragraph | false |

## Competing Interpretations and Limitations

- The entrance-channel m=0 argument is a reaction-geometry expectation, not a direct measurement of every residual magnetic-substate population.
- A Gaussian population is an approximation used to organize the A2/A4 comparison; the observed deviations are part of the result.
- Neutron evaporation is described as broadening, not as leaving every alignment quantity unchanged.
- Angular distributions constrain candidate spin sequences and mixing ratios only with an alignment model or calibration; they do not by themselves uniquely determine all spin, parity, or delta values.
- The persistence statement is conditional on extranuclear deorientation and the host/recoil environment.

## Related Concepts, Methods and Projects

- Concepts: [[magnetic-substate-population]], [[spin-alignment]], [[angular-momentum-alignment]], [[deorientation]], [[rotational-bands]]
- Methods/observables: [[angular-distribution]], [[angular-distribution-coefficient]], [[multipole-mixing-ratio]]
- Project: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Project Relation

This is an early foundational source for the sigma-over-I project: it links heavy-ion reaction alignment to angular-distribution coefficients and to alignment-dependent mixed-transition analysis. It does not define a universal sigma/I value and does not replace later feeding, attenuation, lifetime, or detector-specific sources.

## Human Review Triage

### P0 Focus

1. **D66-1/D66-2, PDF p.1205, first column, method-formalism / author interpretation.** Check that the entrance-channel orbital-angular-momentum argument and the neutron-evaporation broadening statement are not rewritten as an unconditional residual-population theorem.
2. **D66-4/D66-5, PDF p.1205, Fig. 1 and caption, method-formalism / observed fact.** Check the W(theta) convention, the Gaussian reference curve, the stated average A2/A4 values, and the wording that deviations are significant.
3. **D66-6--D66-9, PDF p.1206, Fig. 2 discussion, method-formalism / observed fact.** Check the example transition energies, the reduction of candidate spin sequences, and the condition that a pure transition from the same state calibrates the alignment before extracting delta.

### Remaining P0

- **D66-10/D66-11, PDF pp.1205-1207, author interpretation / limitation.** Check the conditional wording around extranuclear deorientation and the conclusion that alignment persists through cascades only under suitable conditions.

### P1

- Verify the exact Fig. 1 point-by-point values and the OCR-sensitive signs of the Fig. 2 coefficients before using numerical values in a paper-facing context.

## Extracted Pages

- Nucleus/example: `199Tl` (example reaction in the source; no separate nucleus page is created in this round)
- Concepts: [[magnetic-substate-population]], [[spin-alignment]], [[angular-momentum-alignment]], [[deorientation]]
- Methods/observables: [[angular-distribution]], [[angular-distribution-coefficient]], [[multipole-mixing-ratio]]
- Project: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Review Status

All D66 claims were reviewed by the user on 2026-07-13; `needs_review` is cleared for this source note.


## 2026-10-19 Codex续核：取向预期与适用边界

本节为Day16新self-audit，不属于上述旧用户审核；旧前缀/claims/状态逐字节保留。原三页完整主线、Fig1/2及1207上半结尾重读；1207下半Coppi等地磁文章不摄入。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| D66-D16-1 | Fig1排除2→0；正文说I>2数据落在A2=.30±.09、A4=−.09±.05的范围，并明确有significant Gaussian deviations。这不是任意核素的σ先验或一个给定统计置信水平的普适区间。 | population-domain-boundary | direct-reinspection | p1205 Fig1/两栏正文 | true |
| D66-D16-2 | Fig2原331/370/701的(A2,A4)依次为(−.58(.03),−.02(.03))、(−.36(.02),−.03(.02))、(+.26(.04),−.03(.04))；作者称AD把19种spin序列减至5种，再以expectedalignment减至3种，仍需ICC/其它资料。 | actual-AD-and-attributed-selection | direct-original | p1206 Fig2/caption/左栏 | true |
| D66-D16-3 | 本run的完整CGtrace条件分析给高spin低L保号域，也给低spin/大j/方向门反例；这是Codex模型，不把本文入口几何预期写成Rh99实际u2测量。 | conditional-transfer-design | Codex-exact-model | 本页续核；unobserved-feeding-alignment-sign | true |

新可复用推导见[[unobserved-feeding-alignment-sign]]，同源反应/环境/参考限制继续保留；不重计本文为一次新实验。新知识支持条件分析、限制fusion名称本身的证明力。
