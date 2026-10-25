---
type: source
title: "Ødegård et al. 2001 - Evidence for the Wobbling Mode in Nuclei"
aliases: [Odegard 2001 163Lu wobbling, Evidence for the Wobbling Mode in Nuclei]
created: 2026-07-16
updated: 2026-10-24
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
- DCO/angular distributions allow two `δ` branches; electric-character polarization rejects the small-magnitude branch → links are about `90.6(13)%` E2 (PDF p.3).
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
| OD01-D21-1 | superseded by checkpoint092：旧P>0、全核区唯一及25–35 W.u.直接测量认证撤回。原文仅报告电性质偏振选解、相对B及带模型比较；见OD01-D22-R092-1/2。 | task-correction | direct-original-audit | 本页R092原件条目；旧任务数值不认证 | true |

## Day22 原件复核：一声子基准与两种alignment

全文正文与图表实际重读；关键数据/图表视觉核验，raw哈希保持。以下仅Codex self-audit，原page review/既有claim flags不改；新增claims均needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| OD01-D22-001 | 152MeV Euroball IV采集的DCO/角分布/偏振共同用于TSD2→TSD1混合比；作者将多个连接线在无可见spin依赖前提下平均为δ=−3.10(+.36/−.44)，以electric偏振排除另一−.22(+.05/−.03)解。该平均不是九条线各自独立测得同一个δ。 | experimental-analysis-and-dependence | direct-original | 5867, multipolarity paragraph; 5868, first paragraph | true |
| OD01-D22-002 | 文中的σ/I=.25(.02)是磁子态布居宽度校准；Fig3另用Iref=25ω+45ω³（对应ℏ/MeV单位）定义实验i_x并比较J(2)。两种alignment概念必须分开；相近i_x/J(2)支持共同结构，但不是j沿主轴分量的直接测量。 | observable-identity-and-inference-boundary | direct-original-and-bounded-inference | 5867, final paragraph; 5868, Fig.3 caption | true |
| OD01-D22-003 | 5869 Table I在43/2→41/2给λ=.36(.04)和平均δ，并将模型计算矩阵元配实测Eγ生成δ/λ；实验与schematic PRM比较支持作者一声子指认，模型列不是另一份实验。 | data-and-model-lineage | direct-original | 5869, Table I and notes | true |

### Knowledge Impact and Learning Decision

Supports/limits：保留作者的支持或反对解释，并将逐线测量、选解前提、模型结果和依赖链分开。四列比较与条件强度重建见[[wobbling-geometry-phonon-observable-contract]]；不以模型或跨采集中心值差替代新实验置信区间。


## Day22 checkpoint092：163Lu原始观测与强度对象复核

本次完整重读4页、视觉核5868的选解/参考与5869表；SHA256 0ff38adfcbe031fb21c43b3bba290ca44a21898564bb78cf335fbb47b05ba379。未取得Ref.7全文/寿命producer。Crossref另核Ref.7两条书目身份：NPA539,112 DOI10.1016/0375-9474(92)90238-f；PLB303,230 DOI10.1016/0370-2693(93)91425-m。书目不是本轮直接寿命证据。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| OD01-D22-R092-1 | 作者用偏振判定definite electric character并排除−.22混合比解，采纳平均δ=−3.10(+.36/−.44)。本文没有给出P或A的数值/正负号，不能改写成实测P<0或P>0。本文由分支和δ给相对B，不新增TSD2寿命或25–35 W.u.绝对强度测量；p.5866的Qt≈10.7 b引自Ref.7早期实验。 | experimental-analysis-and-measurement-scope | direct-original-and-bounded-reconstruction | 5866, paragraph citing Ref.7; 5867–5868, multipolarity and first paragraph | true |
| OD01-D22-R092-2 | 九条连接线、相近i_x/J(2)、电磁相对比与schematic PRM共同支持作者一声子解释；作者比较并排除其指定UC signature-partner/三准粒子方案。该局部模型比较不能扩张为全核区唯一、自然界只容TSD摆动，或独立测得j主轴矢量。 | author-interpretation-and-comparison-domain | direct-original-and-bounded-reconstruction | 5868, alternative-configuration paragraphs and Fig.3; 5869, Fig.5, Table I and Summary | true |

## Day22 checkpoint122：既有原实验回读与缺测边界

本次同SHA原件四页全文文本回读，fresh visual核5869 Fig5/TableI及其限制段；不是新增数据/寿命或重新测量偏振。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| OD01-D22-R122-1 | Fig5邻文明确交替自旋的一组连接因跃迁能量很低而受抑，数据不能给有意义的upper limits。缺少这些实验点不表示强度严格为零，也不能将模型zigzag图当作全部交替支路已独立测得。TableI所称E2/M1 approximately forbidden属于其crankinglike模型列，非普适守恒禁戒。 | missing-observable-and-model-zero-boundary | direct-original-and-bounded-inference | 5869Fig5paragraph/TableIfootnoteb | true |
