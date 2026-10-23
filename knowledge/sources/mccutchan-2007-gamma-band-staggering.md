---
type: source
title: "McCutchan et al. 2007 - Staggering in gamma-band energies and structural symmetries"
aliases: [McCutchan 2007 gamma-band staggering S4]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-theory-systematics
reading_depth: deep-read
title_original: "Staggering in γ-band energies and the transition between different structural symmetries in nuclei"
authors: [E. A. McCutchan, Dennis Bonatsos, N. V. Zamfir, R. F. Casten]
journal: "Physical Review C"
year: 2007
volume: 76
article: 024306
pages: "1-10"
doi: "10.1103/PhysRevC.76.024306"
citation_key: McCutchan_2007
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevC.76.024306"
library_file: "raw/papers/gpt/high-spin-20260920/转动/2007_McCutchan et al_Staggering in γ-band energies and the transition between different structural.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/转动/2007_McCutchan et al_Staggering in γ-band energies and the transition between different structural.pdf"
raw_sha256: "83acbb32d23d0f7bbe726a28d91e298bda1fa06871020fd18c2c6fc05f52d2ed"
nuclei: [rare-earths, actinides, Xe, Ba, Ce]
reactions: []
experiments: []
models: [Bohr-Hamiltonian, E5, X5, Z4, Z5, interacting-boson-model]
observables: [gamma-band-staggering, S4, gamma-softness, gamma-rigidity]
methods: [level-energy-systematics]
tags: [gamma-band, staggering, triaxiality, gamma-soft, phase-transition]
---

# Staggering in γ-band energies and structural symmetries

## Bibliographic Record

- E. A. McCutchan *et al.*, *Physical Review C* **76**, 024306 (2007), DOI `10.1103/PhysRevC.76.024306`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/转动/2007_McCutchan et al_Staggering in γ-band energies and the transition between different structural.pdf`。

## Scope and Reading Depth

- PDF pp.1–10 fully read: S(J)/S(4) definition, vibrator/γ-soft/axial/rigid-triaxial benchmarks, Xe/Ba/Ce/Sm–Er/actinide systematics, Bohr E(5)/X(5)/Z(4)/Z(5) models, IBA calculations and phase-transition discussion.
- Not covered: raw level compilations and later microscopic calculations.

## Key Results

- `S(J)` is a discrete derivative measuring the displacement of the `(J−1)γ` level from neighbors, sensitive to structural changes.
- γ-soft/vibrator patterns have negative-even/positive-odd staggering; rigid-triaxial patterns reverse phase; axial rotor gives small nearly constant positive values.
- Experimental chains show transitions and reversals; `S(4)` is useful but not unique, and IBA/Bohr model fits require context.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MC07-1 | `S(J)`/`S(4)` provides a sensitive γ-band energy diagnostic of structural evolution. | observable-framework | direct | PDF Sec.II, Eq.(2), Figs.1–4 | true |
| MC07-2 | Staggering phase/magnitude separates γ-soft/vibrator, axial rotor and rigid-triaxial limiting patterns qualitatively. | model-comparison | mixed | PDF Secs.I–II, Fig.5 | true |
| MC07-3 | Phase reversals in selected Ru/Pd/Er nuclei indicate that no one simple model or backbending explanation is universal. | experimental-systematics | direct | PDF Sec.II, Figs.2–4 | true |

## Summary

McCutchan *et al.* establish `S(J)` as a useful, sensitive—but non-unique—γ-band diagnostic and connect isotope-dependent staggering to transitions among vibrational, γ-soft, axial and triaxial-rigid structures.

## Competing Interpretations and Limitations

Energy-only staggering is affected by band assignments, crossings, γ softness, anharmonicity and quasiparticle coupling; it cannot alone determine a unique shape or phase transition.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| MC07-AR-1 | Observable chain | γ-band energies → S(J) → limiting-model/systematics comparison. | Eq.(2), Figs.1–5 | self-checking |
| MC07-AR-2 | Transfer condition | Requires same band definitions/spin range and companion E2/transition/model evidence. | PDF Secs.II–III | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[gamma-soft-deformation]], [[triaxial-deformation]] and high-spin collective-mode diagnostics.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `MC07-P0-1`: `S(J)`/`S(4)` cannot be used as a unique gamma-rigid/soft classifier without companion evidence.

## Extracted Pages

- Concepts: [[gamma-soft-deformation]], [[triaxial-deformation]]。

## Day20 checkpoint037：交错原件与旧数字归属纠正

本轮定向回读PDF1–5，视觉核PDF2–5的定义、Fig1极限图及Fig2/4；并非新完整十页阅读。原review/flags保留。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MC07-D20-R37-1 | Eq2为归一二阶能量差；Fig1 S4打印vibrator−1.0、axial+.33、γ-soft−2.0、rigidγ30°+1.67，旧013的γ-soft−2.5错误。正S4亦可轴对称、负偶数交错也见振动极限，单符号不唯一确定核形状。 | literal-benchmark-and-inference-boundary | direct-original-and-model | PDF2 Eq2 and discussion; PDF3 Fig1 | true |
| MC07-D20-R37-2 | Figs2/4数据取Ref24，未在这些位置列旧013所用130Ba134Ba130Xe192Os四元精确能量表；本任务未重新取得level inputs或数字化，撤回具体S4实验认证。PDF3说明选定反相核的这种图样在J>5出现，不能倒写192Os S4=.954或全区排他分类。 | input-provenance-and-spin-scope | direct-original-and-boundary | PDF3 first column final paragraph; PDF4 Fig2; PDF5 Fig4/caption | true |


## Day20量化审计：准γ带交错指数S(4)四维基准与三轴刚软辨识（checkpoint135）

> checkpoint146：本节121–145批次的科学认证已撤回。旧文本/输入与指纹保存在本run的history-before-repair-146.json；原始原件与既有review/flags保留。自设数值或flag的passed只验证算术，不识别实际producer、共同Cov、实验CI或唯一模式。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MC07-D20-R135-1 | checkpoint146撤回旧认证；不据此恢复错误表值、跨态强度阶梯、硬阈值或完全闭合。请使用本页较早原件纠错与checkpoint146。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |
