---
type: source
title: "Königshofen et al. 2001 - Multipole mixing ratios in 130Ba"
aliases: [Königshofen 2001 130Ba mixing ratios]
created: 2026-09-20
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Multipole mixing ratios in 130Ba"
authors: [C. T. Königshofen, K. Jessen, A. Gade, I. Wiedenhöver, H. Meise, P. von Brentano]
journal: "Physical Review C"
year: 2001
volume: 64
article: 037302
pages: "1-3"
doi: "10.1103/PhysRevC.64.037302"
citation_key: K_nigshofen_2001
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevC.64.037302"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/2001_Königshofen et al_Multipole mixing ratios in 130 Ba.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/2001_Königshofen et al_Multipole mixing ratios in 130 Ba.pdf"
raw_sha256: "34428af79a8dcc3a7dc27a6a416c3fa556a2d37e763df76cb1218241f370a755"
nuclei: [130Ba, 130La]
reactions: [120Sn(14N,4n)130La]
experiments: [cologne-osiris8-euroball-cluster]
models: [interacting-boson-model-1, consistent-q-iba]
observables: [multipole-mixing-ratio, gamma-gamma-angular-correlation, branching-ratio, B(E2)]
methods: [angular-correlation, gamma-gamma-coincidence]
tags: [130Ba, mixing-ratio, low-spin, A130, gamma-gamma]
---

# Multipole mixing ratios in 130Ba

## Bibliographic Record

- C. T. Königshofen *et al.*, *Physical Review C* **64**, 037302 (2001), DOI `10.1103/PhysRevC.64.037302`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/纲图/2001_Königshofen et al_Multipole mixing ratios in 130 Ba.pdf`。
- 3-page selectable-text PRC Brief Report; title page, authors, DOI, volume/article number and publication date agree.

## Scope and Reading Depth

- PDF pp.037302-1–3 fully read: reaction/off-beam β-decay setup, Osiris-8/Euroball cluster geometry, three-angle matrices, Figs.1–3, complete Table I, Rose–Brink sign convention, B(E2) correction, IBA-CQF comparison and conclusions.
- Figure/table audit: gated spectrum quality (Fig.1), `W(180)/W(90)` and `W(55)/W(90)` versus `arctan δ` unique-branch example (Fig.2), partial `130Ba` level scheme (Fig.3), and all 18 transition rows in Table I.
- Not covered: raw coincidence matrices, detector-pair efficiency files, decay-scheme source data and IBA code.

## Paper Question and Experimental Logic

The paper asks whether multi-angle γγ directional correlations can determine unique multipole mixing ratios for low-spin `130Ba` transitions and correct the inferred `B(E2)` branchings used in IBA-1/consistent-Q comparisons.

1. Produce `130La` with `120Sn(14N,4n)` at 65 MeV, collect off-beam β+/EC decay γγ coincidences in Osiris-8 plus one Euroball cluster (47 million events; detector-pair angles 180°, 90° and 55°; PDF p.037302-1).
2. Use efficiency-corrected ratios `W(180°)/W(90°)` and `W(55°)/W(90°)` and compare with calculated angular-correlation curves for spin/parity and multipolarity hypotheses.
3. Analyze cascades containing one pure E2 transition so the two measured ratios intersect at a unique `δ` (Rose–Brink convention); correct branching/B(E2) ratios for M1 admixtures and compare with IBA-CQF.

## Key Evidence and Reasoning Chain

- Two independent detector-angle ratios give unique solutions for 18 transitions; the high sensitivity comes from sizable `P2` and `P4` coefficients (example `−0.0321` and `−0.0778`) and clean β-decay spectra (PDF pp.037302-1–2, Fig.2).
- A new `3−` assignment for the 1918.3-keV level is adopted because its decays are consistent with pure E1 and its β population is much weaker than the positive-parity `3+` state at 2053.3 keV (PDF p.037302-2). This is an author assignment built on the measured mixing patterns and population.
- The `2+_3→2+_1` transition is `91.7%` M1 and `2+_3→2+_2` is pure M1 within limits; `4+_3→4+_1` is `97.8%` M1. M1 corrections remove earlier B(E2) discrepancies (PDF p.037302-2, Table I).
- `4+_3→3+_1` has no unique δ; pure M1 is excluded. The source therefore demonstrates both the power and the multi-solution boundary of angular-correlation extraction.
- Strong M1 components near 1.7 MeV are interpreted as evidence for mixed-symmetry/proton-neutron degrees of freedom beyond simple IBA-1; absolute M1 strengths are still needed for an unambiguous mixed-symmetry assignment (PDF p.037302-3).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KO01-1 | Three-angle γγ correlations and clean β-decay spectra determine unique mixing ratios for 18 low-spin `130Ba` transitions. | experimental-method-result | direct | PDF pp.037302-1–2, Fig.2, Table I | true |
| KO01-2 | `2+_3` decays contain dominant/pure M1 components, and `4+_3→4+_1` is 97.8% M1. | experimental-result | direct | PDF p.037302-2, Table I | true |
| KO01-3 | M1 corrections reconcile earlier `B(E2)` ratios for `2+_3` and `4+_3` branches with consistent-Q calculations. | model-data-comparison | mixed | PDF p.037302-2, Table I | true |
| KO01-4 | `4+_3→3+_1` has no unique mixing ratio; only pure M1 is excluded. | ambiguity/limitation | direct | PDF p.037302-2 | false |
| KO01-5 | Strong M1 admixtures near 1.7 MeV are consistent with mixed-symmetry states, but absolute M1 strengths are needed. | author-interpretation | indirect | PDF p.037302-3 | true |
| KO01-6 | 原文TableI共40条跃迁行，18行给finite delta/error；其余pure/unknown/parenthesized标签及污染asterisk条目不同层。旧Scope的all18transitionrows措辞不准确，以本条及原表优先；“18个唯一numeric值”不等于全表40行都唯一。 | table-scope-correction | direct-and-self-audit | 037302-2 TableI与caption；037302-1 abstract/body | true |
| KO01-7 | Fig2实例为1003.3-keV的3+_1→2+_1→0+_1、第二条pureE2，TableI/Fig2报告RoseBrink delta=−4.5(.4)。正文−.0321/−.0778明确是作者calculated P2/P4系数，不是两份新实测独立coefficients。 | experimental-example-and-calculation-identity | direct | 037302-1右栏；037302-2 Fig2/caption/TableI | true |
| KO01-8 | 三个角是两个gamma的openingangles180/90/55度，不是beam-angle DCO交换式。两correctedW ratios共享W90与数据/efficiency条件，不能因函数形式不同就当统计独立；原文未提供完整Cov或pair效率/finite-response文件。 | observable-and-covariance-boundary | direct-and-self-audit | 037302-1实验/分析段、Fig1；037302-2 Fig2 | true |
| KO01-9 | 在本任务unoriented3→2→0 point模型、normalizedRB→KS/D96换号后，deltaRB−4.5给A2−.03214156/A4−.07779112，与作者四小数计算值按舍入相容。从这些印刷计算系数构造的R180 witness仍有两根，R55可区分；不是重提取原实验delta或原response重放。 | bounded-formula-reconstruction | task-calculation | KO01 Fig2/TableI；D96 Eq3/7；day16_ko01_three_angle_audit.py | true |
| KO01-10 | 1918.3-keV3-到正宇称4+/2+的delta.06(.05)/.03(.08)若按最低mixedmultipoles解释是M2/E1，不是E2/M1。TableI的RoseBrink sign仍需按operator定义用；generic delta平方份额不能全部叫E2 fraction。 | parity-and-multipole-pair-boundary | direct-and-self-audit | 037302-2新3-赋值段、TableI末两行；037302-3 Fig3 | true |
| KO01-11 | 4+_3→3+_1的483.5线仍没有unique delta、只排pureM1；其branch92*与BE2<130*来自污染估计无error，不能当普通Gaussian data。强M1支持mixedsymmetry解释但作者仍要求absoluteM1，不由relative fraction直接确认模式。 | unresolved-case-and-structure-boundary | direct | 037302-2正文/TableIcaption及483.5行；037302-3结论 | true |

## Summary

### 2026-10-18独立Day16原件重核

已先冻结受旧source摘要priming的回忆，再完整读3页原件/所有Fig1–3和TableI关键列，原hash匹配；Crossref重新核六作者、2001/PRC64/DOI，metadata页码空白不补造。所有40行的parent/gammaenergy/delta标签已typed核数，18行finite值；branching/BE2列只在当前问题必要行核原图，没有将全部派生列作为本session新重算。

旧Scope中“all18transitionrows”按KO01-6更正使用，但原KO01-1–5的review flags保持。新6–11及本段是Codex self-audit、needs_review:true，未产生人审。主线是offbeam130Laβ+/EC→三openingangle组→效率修正的两个形状比→pureE2-gatedδ→修正M1对BE2的影响→IBA比较和absoluteM1缺口；不外推为所有case的唯一模式。

[[angular-correlation]]“130Ba的两个opening-angle比值”保存本session的新fixedpath核验、单ratio两根、第二shape区分和shared-denominatorΣ门。作者calculated四小数与本任务精确point结果在舍入范围相容，不能把calculatedcoefs又作为独立experiment叠加。Fig2未给rawcounts/数表/联合likelihood，本任务未从图的横线伪造experimentalCov或重新测δ。

Königshofen *et al.* provide a direct three-angle angular-correlation determination of 18 `130Ba` mixing ratios. The results correct B(E2) systematics and expose strong M1 components in higher collective states, while preserving a concrete no-unique-solution case.

## Competing Interpretations and Limitations

Spin/parity hypotheses, detector-pair efficiency corrections, Rose–Brink sign convention and assumed pure-E2 reference transitions are part of the inference. A unique intersection in two ratios is source-specific; rows marked estimated/asterisk or without a unique δ cannot be treated as equally precise. Mixed-symmetry interpretation requires absolute M1 strengths and independent structure evidence.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| KO01-AR-1 | Observable chain | Detector-angle yields → efficiency-corrected `W` ratios → angular-correlation curves → δ and multipolarity → M1-corrected branching/B(E2). | PDF pp.037302-1–2, Fig.2, Table I | self-checking |
| KO01-AR-2 | Convention | δ signs follow Rose–Brink; cross-source use requires convention mapping. | Table I caption; Ref.14 | self-checking |
| KO01-AR-3 | Transfer condition | Ratios and sensitivity depend on Osiris-8/cluster geometry and three fixed angles; no universal detector calibration follows. | PDF p.037302-1 | self-checking |
| KO01-AR-4 | Failure condition | Contamination/asterisk rows, assumed pure transitions and unresolved δ branches can alter B(E2) correction. | Table I; PDF pp.037302-2–3 | active-L3 |
| KO01-AR-5 | Independence | Direct `130Ba` experiment; cited 128Xe/126Xe/132Ce mixed-symmetry studies are background, not new measurements here. | Introduction/References | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` and `methodological-bridge` for angular-correlation/mixing-ratio analysis; `revises` the assumption that low-spin `130Ba` B(E2) tables can be read without M1 corrections.
- Persistence: update [[angular-correlation]], [[multipole-mixing-ratio]], [[a130-high-spin-collective-modes-evidence-map]] and the A≈130 γ-soft/mixed-symmetry map.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[angular-correlation]] | Three-angle `W` ratios and unique/multi-solution δ inference. |
| supports | [[multipole-mixing-ratio]] | Direct Rose–Brink sign-convention and M1-corrected B(E2) example. |
| supports | [[gamma-soft-deformation]] | Low-spin `130Ba` collective/mixed-symmetry context; does not by itself fix γ softness. |
| candidate-L3 | [[a130-high-spin-collective-modes-evidence-map]] | Compare robust δ rows with wobbling/signature/chiral candidate evidence requirements. |

## Human Review Triage

### P0

- `KO01-P0-1`: preserve the Rose–Brink δ convention and detector-angle calibration; do not transplant Table I values to another array or convention.

### P1

- `KO01-P1-1`: asterisk/estimated rows and the unresolved `4+_3→3+_1` δ need original spectra or follow-up before paper-level quantitative use.
- `KO01-P1-2`: mixed-symmetry interpretation remains provisional without absolute M1 strengths.

## Extracted Pages

- Nuclei: `130Ba` (source-level low-spin map).
- Methods: [[angular-correlation]], [[multipole-mixing-ratio]]。
- Projects: [[a130-high-spin-collective-modes-evidence-map]]。

## L3/L4 Follow-up

- L3 question: how often do A≈130 low-spin angular-correlation datasets provide a unique δ once detector-angle coverage, reference transitions and M1 contamination are modeled consistently? Required counter-checks are convention mapping and unresolved-branch sensitivity.
- No L4 run: raw matrices/response files and a machine-readable Table I are not supplied.
