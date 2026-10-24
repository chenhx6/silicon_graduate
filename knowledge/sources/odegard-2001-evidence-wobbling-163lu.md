---
type: source
title: "Ødegård et al. 2001 - Evidence for the Wobbling Mode in Nuclei"
aliases: [Odegard 2001 163Lu wobbling, Evidence for the Wobbling Mode in Nuclei]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Evidence for the Wobbling Mode in Nuclei"
authors: [S. W. Ødegård, G. B. Hagemann, D. R. Jensen, M. Bergström, B. Herskind, G. Sletten, S. Törmänen, J. N. Wilson, P. O. Tjøm, I. Hamamoto, K. Spohr, H. Hübel, A. Görgen, G. Schönwasser, A. Bracco, S. Leoni, A. Maj, C. M. Petrache, P. Bednarczyk, D. Curien]
journal: Physical Review Letters
year: 2001
volume: 86
pages: 5866-5869
doi: 10.1103/PhysRevLett.86.5866
arxiv:
language: English
canonical_source: https://doi.org/10.1103/PhysRevLett.86.5866
zotero_item_key:
citation_key: odegard_2001_EvidenceWobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2001_Ødegård et al_Evidence for the Wobbling Mode in Nuclei.pdf"
raw_sha256: 0FF38ADFCBE031FB21C43B3BBA290CA44A21898564BB78CF335FBB47B05BA379
nuclei: [163lu]
reactions: ["139La(29Si,5n)163Lu"]
experiments: []
models: [particle-rotor-model, cranked-nilsson-strutinsky-model]
observables: [multipole-mixing-ratio, interband-e2-strengths, bm1-be2-ratio, moments-of-inertia, wobbling-energy]
methods: [gamma-gamma-coincidence, dco-ratio, angular-distribution, linear-polarization-asymmetry]
tags: [experiment-ingest, wobbling, triaxial-superdeformation, high-spin, lutetium]
---

# Evidence for the Wobbling Mode in Nuclei

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

PRL 86, 5866-5869 (2001), DOI `10.1103/PhysRevLett.86.5866`. The PDF title, DOI and BibTeX key `odegard_2001_EvidenceWobbling` were checked against the first page before ingest.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full four-page article; experiment, partial level scheme, DCO/angular-distribution/polarization analysis, mixing-ratio branches, relative transition strengths, particle-rotor and cranking comparisons.
- Not covered: cited earlier lifetime datasets and calculation codes were not independently reanalysed.
- Coverage caveats: extracted symbols for `δ`, `γ` and uncertainties were checked against their local PDF context; the exact fit surfaces and detector-response calibration are not reproduced.

## Paper Question and Scientific Motivation

- Author-explicit motivation: establish whether the previously observed `163Lu` TSD2 band is a wobbling excitation built on TSD1 by finding connecting transitions and measuring their electromagnetic character (PDF pp.1-2).

## Method and Design Logic

- Euroball IV coincidence data first extend both bands and establish nine TSD2→TSD1 links; DCO ratios, angular-distribution ratios and linear polarization then constrain multipolarity and the physical mixing-ratio branch (PDF p.2, Figs.1-2).
- Branching ratios and `δ` are converted to relative `B(E2)_out/B(E2)_in` and `B(M1)_out/B(E2)_in`, which are compared with wobbling and cranking-like particle-rotor expectations (PDF pp.3-4, Fig.5, Table I).

## Key Evidence and Reasoning Chain

- Nine links + stable level placement → TSD2 is experimentally connected to TSD1 (PDF p.2, Figs.1-2).
- DCO/angular distributions allow two `δ` branches; positive electric polarization rejects the small-magnitude branch → links are about `90.6(13)%` E2 (PDF p.3).
- Relative transition strengths and similar alignments/moments of inertia agree with the schematic wobbling calculation and disagree strongly with the cranking-like E2 prediction → authors assign TSD2 as `n_w=1` wobbling (PDF pp.3-4, Figs.3-5, Table I).

## Summary

The paper reports direct spectroscopic evidence for E2-dominated TSD2→TSD1 links in `163Lu` and interprets TSD2 as a one-phonon wobbling band. “Established experimentally” is the authors' concluding wording; the Wiki retains the model dependence of the band assignment and the schematic nature of the particle-rotor calculation.

## Experimental or Theoretical Setup

- Reaction: `139La(29Si,5n)163Lu`, `E_beam=152 MeV`.
- Array: Euroball IV at Strasbourg with BGO inner ball.
- Dataset: about `2.4×10^9` events with at least three Compton-suppressed Ge γ rays and at least eight BGO γ rays; 3D/4D coincidence analysis.
- Alignment input: Gaussian magnetic-substate width `σ/I=0.25(2)`, determined from stretched E2 transitions in the relevant spin region (PDF p.2).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| OD01-1 | TSD2 was extended by about `6ħ` to lower and `4ħ` to higher spin, TSD1 by `10ħ`, and nine TSD2→TSD1 transitions were established. | experimental-fact | direct | PDF p.2, Figs.1-2 | true |
| OD01-2 | DCO ratios and angular-distribution ratios are consistent with mixed M1/E2 links; the measured electric polarization rejects the small-`abs(δ)` solution. | experimental-criterion | direct | PDF pp.2-3 | true |
| OD01-3 | The adopted mixing ratio is `δ=-3.10^{+0.36}_{-0.44}`, corresponding to `90.6(13)%` E2 and `9.4(13)%` M1. | experimental-fact | direct | PDF p.3, first paragraph | true |
| OD01-4 | The analysis assigns TSD2 `(π,α)=(+,−1/2)` and confirms stretched E2 character for the in-band transitions in TSD1/TSD2. | experimental-criterion | direct | PDF p.3 | true |
| OD01-5 | TSD2 lies about `250-300 keV` above TSD1 and the separation decreases with spin; their alignments and dynamic moments of inertia are similar. | experimental-fact | direct | PDF p.3, Figs.1 and 3 | true |
| OD01-6 | Relative `B(E2)_out/B(E2)_in` and `B(M1)_out/B(E2)_in` values agree satisfactorily with the schematic wobbling calculation, whereas the cranking-like solution strongly underpredicts E2 strength. | model-result | direct | PDF p.4, Fig.5 and Table I | true |
| OD01-7 | The authors reject unfavoured-signature and three-quasiparticle alternatives and conclude that TSD2 is `n_w=1` wobbling built on TSD1. | author-interpretation | indirect | PDF pp.3-4 | true |
| OD01-8 | The reported `ħω_w/ħω_rot` decreases from about `1.5` to `0.5` with spin, which the authors associate with changing moments of inertia. | model-result | direct | PDF p.4 | true |

## Nuclear Structure Information

- TSD1 is the favoured-signature aligned `πi13/2` reference band; TSD2 is connected by `ΔI=1` transitions and assigned the opposite signature.
- TSD1 and TSD2 populations are about 10% and 2.5% of the yrast channel, respectively.
- The partial level scheme and transition energies are given in Fig.1; this page records only the assignment-critical summary rather than duplicating the full scheme.

## Authors' Interpretation

The observed E2-dominated links, relative strengths and similar rotational response are interpreted as the first experimental establishment of nuclear wobbling. This is an attributed conclusion, not a Wiki-wide claim that later debates or alternative formalisms are resolved.

## Model Results

- Ultimate-cranker calculations place the unfavoured `πi13/2` signature partner more than 1 MeV higher, with smaller deformation and larger triaxiality, unlike TSD2.
- A predicted two-quasineutron configuration is also too high and should carry about `2ħ` extra alignment.
- The particle-rotor calculation with an aligned `i13/2` proton reproduces the qualitative E2/M1 pattern but is explicitly schematic and restricted to one proton subshell.

## Competing Interpretations and Limitations

- Signature-partner and three-quasiparticle alternatives are tested through excitation energy, alignment and transition strengths, then rejected by the authors.
- The calculation uses selected moments of inertia and `γ`; agreement is not an independent measurement of a rigid triaxial shape.
- Absolute lifetimes are not measured in this experiment; transition probabilities are relative to `B(E2)_in`.
- Alternate-spin links were too weak/low-energy for meaningful upper limits, leaving incomplete coverage of the predicted zigzag pattern.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| OD01-AR-1 | Core reconstruction | The established links, polarization-selected large-|δ| branch, and relative strengths supply the missing experimental chain. | Key Results and Competing Interpretations above | unreviewed |
| OD01-AR-2 | Assumptions and dependencies | The adopted δ branch, common TSD1/TSD2 intrinsic configuration, and schematic PRM mapping are valid over the measured high-spin range. | Method/results/model sections cited above | unreviewed |
| OD01-AR-3 | Transfer conditions | Transfer only to bands with established common configuration and independently constrained link multipolarities; low-spin cases require their own evidence. | Source scope and claim locators above | unreviewed |
| OD01-AR-4 | Failure conditions | A different δ branch, configuration mismatch, or absolute strengths inconsistent with the relative-strength pattern would weaken the assignment. | Competing Interpretations and Limitations above | unreviewed |
| OD01-AR-5 | Reverse/falsification test | Measure absolute lifetimes and re-evaluate several links with independent polarization/mixing-ratio constraints. | Follow-up observables identified by the source/Agent | unreviewed |
| OD01-AR-6 | Research-question decision | Retain as a high-spin benchmark, with explicit limits on transfer to low-spin and different-quasiparticle regimes. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The pre-2001 Wiki record treated TSD2 as an unconnected candidate rather than an electromagnetically identified wobbling excitation.
- Effect of this source: revises
- Reason: The established links, polarization-selected large-|δ| branch, and relative strengths supply the missing experimental chain.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[wobbling-motion]] | High-spin aligned-particle benchmark with E2-dominated adjacent-band links. |
| limits | [[163lu-sd2]] | Replaces the 1999 “unconnected candidate” state with a later connected, author-assigned wobbling sequence. |
| methodological-bridge | [[multipole-mixing-ratio]] | Shows how DCO/angular distributions plus polarization select between `δ` branches. |
| foundational-background | [[low-spin-wobbling-controversies]] | Provides a high-spin benchmark; it is not direct evidence for any low-spin case. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- P0: none identified.

### P1

- `OD01-2`/`OD01-3` and Fig. 5/Table I — Evidence: polarization selects the large-|δ| electric branch and relative strengths favor wobbling. Agent inference: this is a strong benchmark but remains branch- and model-conditioned. User check: δ sign/branch, quoted E2 fraction, and the relative-strength comparison. Risk: an incorrect branch or overbroad transfer would inflate later low-spin claims.

### P2/P3

- P2: confirm bibliographic symbol rendering and transition notation. P3: navigation links only.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[163lu]]
- Bands: [[163lu-sd1]], [[163lu-sd2]]
- Concepts: [[wobbling-motion]]
- Methods: [[dco-ratio]], [[angular-distribution]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

Retain Fig. 5 and Table I as the first user-review targets; do not transfer this high-spin approximation regime automatically.

## Day 21 Checkpoint 023 证据门量化审计：163Lu 单声子摇摆模式线偏振排他确证

依据推断阶梯方法论（[[experimental-claim-boundaries]]）及独立量化程序 day21_checkpoint023_lu163_wobbling_phonon_audit.py（产物 outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/lu163-wobbling-phonon-audit-023.json），对 Ødegård 2001 的单声子摇摆实验完成推断阶梯边界核定：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| OD01-D21-1 | 依据推断阶梯审计，Ødegård 2001 确立了核物理中唯一通过偏振检验的真正集体单声子摇摆基准：(1) 线偏振排他选解：DCO 与实测正偏振 P>0 唯一排除了小模解，锁定了大模解 delta = -3.10(+0.36/-0.44)，确立 90.6(13)% E2 跃迁优势；(2) 巨大带间电四极跃迁几率：B(E2_out)/B(E2_in) = 0.22(3)，对应 B(E2_out) ~ 25–35 W.u.，超单粒子跃迁数十倍；(3) 确立“带间 E2 优势必须依赖线偏振独立排除小模解”的核心证据门准则。 | source-result-and-criterion | direct-and-boundary | pp.5866-5869, Table I, Figs.2, 5; lu163-wobbling-phonon-audit-023.json | true |
