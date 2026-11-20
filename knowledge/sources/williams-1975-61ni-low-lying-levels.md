---
type: source
title: "Williams et al. 1975 - Low-lying levels in 61Ni"
aliases: [Williams 1975 61Ni levels]
created: 2026-09-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-shell-model
reading_depth: deep-read
title_original: "A study of the low-lying levels in 61Ni"
authors: [J. R. Williams, C. R. Gould, R. O. Nelson, D. R. Tilley, D. G. Rickel, N. R. Roberson]
journal: "Nuclear Physics A"
year: 1975
citation_key: "williams_1975_61ni-lying-levels"
volume: 253
pages: "365-379"
pii: "0375-9474(75)90487-X"
canonical_source: "Williams et al., Nucl. Phys. A 253, 365-379 (1975)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/1975_Williams et al_A study of the low-lying levels in 61Ni.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/1975_Williams et al_A study of the low-lying levels in 61Ni.pdf"
raw_sha256: "bfdcc111891a0f88c3ab01df131c438337497fc0d456e8ca3fa6a09912f0a02e"
nuclei: [61Ni, 61Cu]
reactions: [58Fe-alpha-n-gamma, 60Ni-deuteron-p-gamma]
experiments: [GeLi, DSAM, angular-correlation, linear-polarization]
models: [sd-pf-shell-model, Glaudemans-shell-model]
observables: [lifetime, mixing-ratio, linear-polarization, angular-distribution, M1, E2]
methods: [Doppler-shift-attenuation, gamma-gamma-angular-correlation, Compton-polarimetry]
tags: [61Ni, level-scheme, DSAM, mixing-ratio, polarization, shell-model]
---

# Low-lying levels in `61Ni`

## 2026-11-19 targeted polarization extraction audit

The later targeted note for this same PDF is merged here rather than registered
as a second source. That audit covered printed pp.370-371 (Table 1), p.373
(Fig.4 and text), and the polarization passages for the 1016, 1611 and 2020-keV
states; it was not a fresh full-paper or shell-model review.

For 909 to ground, p.373 reports P=-0.15 +/- 0.04 and
delta=+0.20(+0.16,-0.03). The generated -0.08 extraction was rejected.
For 909 to 67 keV, the same page reports P=0.01 +/- 0.11 and the delta
interval [-1.19,-0.36], not an invented central value. The inspected methods
constrain magnetic-substate populations; not finding one Gaussian sigma/I
is not evidence that the final analysis fixed an assumed Gaussian sigma/I.
No new PDM fit or covariance reconstruction was performed.

## Bibliographic Record

- J. R. Williams *et al.*, *Nucl. Phys. A* **253**, 365–379 (1975), PII `0375-9474(75)90487-X`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/1975_Williams et al_A study of the low-lying levels in 61Ni.pdf`。

## Scope and Reading Depth

- PDF pp.365–379 fully read: `58Fe(α,nγ)` and `60Ni(d,pγ)` methods, DSAM, angular correlations, linear polarization, level scheme below 2.2 MeV, Table 1 strengths/lifetimes and shell-model comparison.
- Not covered: raw spectra and later re-evaluated `61Ni` levels.

## Key Results

- Seventeen `61Ni` states below 2.2 MeV were studied with DSAM, γ angular correlations, linear polarization and particle–γ coincidences. New `Jπ` assignments include levels at 1016, 1611, 2020 and 2123 keV (PDF pp.365–369, Fig.2).
- DSAM \(F(\theta)\) 与 FTAU 停止模型给出的平均寿命见表 1。909、1132、1457、1611 keV 依次为 \(450^{+330}_{-150}\)、\(400^{+200}_{-100}\)、\(480^{+340}_{-160}\)、\(365^{+160}_{-90}\) fs。表 1 的 2125 keV 为 \(45(8)\) fs，§3.6 正文为 \(48(8)\) fs，且表 1 的基态分支 \(>95\%\) 与正文叙述的仅到基态各按原处保留。
- Angular correlations and a Ge(Li) Compton polarimeter determine multipolarities and mixing ratios under the Rose–Brink convention. The paper reports M1/E2 strengths and compares transition rates with the Glaudemans shell model (PDF pp.367–374, Table 1).
- 原刊摘要、图和表给 1016、1611、2020、2123 keV 态依次指认 \(7/2^-,5/2^-,7/2^-,9/2^+\)。2123→1016 的结果属于 E1/M2 范围，不能作为 E2/M1 条目。

### 线偏振、混合比与取向条件

| 跃迁 \(E_i\to E_f\) (keV) | \(P\) | 原文 \(\delta\) | 结论依据 |
| --- | --- | --- | --- |
| 909→0 | \(-0.15(4)\) | \(+0.20^{+0.16}_{-0.03}\) | 角分布、n–γ 角关联与 \(P\) 选支，图 3–4 |
| 909→67 | \(+0.01(11)\) | \([-1.19,-0.36]\) | 角分布与 \(P\) 限定，图 4 |
| 1016→0 | \(+0.45(10)\) | \(-0.03^{+0.12}_{-0.22}\) | 寿命排除纯高阶分支，\(P\) 与主 E2 相容，图 5、§3.3 |
| 1016→67 | \(-0.22(5)\) | \(-2.5(5)\) | 大 E2 混合与 \(P\) 判宇称，图 5、§3.3 |
| 1611→0 | \(+0.05(20)\) | \([+0.18,+2.75]\) | 角分布偏好 \(5/2\) 但拟合水平低，\(P\) 与该区间相容，图 6、§3.4 |
| 1611→67 | \(+0.49(19)\) | \([-0.18,+0.18]\) | \(P\) 留两个 \(J^\pi\) 候选，结合寿命/强度排除 \(3/2^+\)，图 6、§3.4 |
| 2020→67 | \(-0.65(27)\) | \(+0.03(16)\) | \(P\) 选 \(7/2^-\)，角分布给 \(\delta\)，图 7、§3.5 |

§2.2 的 n–γ 角关联拟合只布居 \(m=\pm1/2\)。§2.3 的同时采集 singles 角分布与偏振采用另一处理：以统计模型、ABACUS-II 透射系数和 Perey–Buck 参数限制磁子态布居，再用拟合后的勒让德系数预测 \(P\)。两条分析有各自的取向前提。全文没有一个高斯 \(\sigma/I\) 数值，不能把前者的约束套到后者。极化器由两圆柱 Ge 晶体构成，位于束轴 \(90^\circ\)，两个方位各四小时。细部标定见文中 Ref. 13。印刷 367–369 页。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WI75-1 | Multimethod spectroscopy establishes the low-lying `61Ni` scheme and revised `Jπ` assignments. | experiment-result | direct | PDF pp.365–369, Fig.2 | true |
| WI75-2 | DSAM lifetimes and M1/E2 strengths constrain single-particle/shell-model configurations. | lifetime-result | direct | PDF pp.366–374, Table 1 | true |
| WI75-3 | Mixing-ratio and polarization signs use an explicit Rose–Brink convention. | convention-boundary | direct | PDF pp.367–370 | false |

## Summary

Williams *et al.* provide a foundational `61Ni` multimethod data set that complements Meyer 1978, Wadsworth 1977 and Samanta 2019. Its strength is the joint lifetime, angular-correlation and polarization evidence; DSAM stopping/feeding, weak branches and shell-model mapping remain explicit limitations.

## Competing Interpretations and Limitations

- DSAM lifetimes depend on stopping powers, feeding assumptions and line-shape corrections; several values are upper/lower limits.
- Mixing ratios and `Jπ` assignments depend on reference spins, angular distributions, detector response and Rose–Brink phase conventions.
- Shell-model comparison is a model test, not a direct measurement of configuration purity or deformation.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| WI75-AR-1 | Scheme chain | Particle–γ/γ–γ coincidences → angular distribution/polarization → multipolarity/Jπ → level placement. | PDF pp.366–370 | self-checking |
| WI75-AR-2 | Lifetime chain | Doppler shift factors + stopping model → τ → M1/E2 strengths → shell-model comparison. | PDF pp.366–374, Table 1 | self-checking |
| WI75-AR-3 | Transfer condition | Keep low-energy `61Ni` data separate from later `61Ni` remeasurements and high-spin interpretations; reconcile lineages explicitly. | PDF pp.365–379 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[wadsworth-1977-61ni-levels]], [[meyer-1978-multiparticle-configurations-61ni-67zn]], [[samanta-2019-single-particle-configurations-61ni]], [[doppler-shift-attenuation-method]], [[multipole-mixing-ratio]].
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `WI75-P0-1`: Preserve DSAM and Rose–Brink boundaries when reconciling the `61Ni` source lineage; do not merge strengths without transition crosswalks.

## Extracted Pages

- Sources/methods: [[doppler-shift-attenuation-method]], [[multipole-mixing-ratio]], [[wadsworth-1977-61ni-levels]]。
