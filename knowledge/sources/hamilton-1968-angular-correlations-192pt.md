---
type: source
title: "Hamilton & Davies 1968 - Angular correlation measurements in 192Pt"
aliases: [Hamilton 1968 192Pt mixing ratios]
created: 2026-09-20
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-method
reading_depth: deep-read
title_original: "Angular correlation measurements in 192Pt"
authors: [W. D. Hamilton, K. E. Davies]
journal: "Nuclear Physics A"
year: 1968
citation_key: "hamilton_1968_192pt-angular-correlation"
volume: 122
pages: "165-176"
pii: "0375-9474(68)90710-0"
doi: "10.1016/0375-9474(68)90710-0"
canonical_source: "Hamilton & Davies, Nucl. Phys. A 122, 165-176 (1968)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/mixing ratio/1968_Hamilton et al_Angular correlation measurements in 192Pt.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/mixing ratio/1968_Hamilton et al_Angular correlation measurements in 192Pt.pdf"
raw_sha256: "5a08c45e80c6793456ad892f68e97bf471c86b4ec69f57fe0920d179ec477f77"
nuclei: [192Pt, 192Ir]
reactions: [192Ir-beta-decay]
experiments: [sussex-Ge-NaI-angular-correlation]
models: [angular-correlation-formalism]
observables: [angular-correlation-coefficients, linear-polarization, E2-M1-mixing-ratio]
methods: [gamma-gamma-angular-correlation, linear-polarization-asymmetry]
tags: [192Pt, mixing-ratio, angular-correlation, polarization, historical-method]
---

# Angular correlation measurements in 192Pt

## Bibliographic Record

- W. D. Hamilton and K. E. Davies, *Nuclear Physics A* **122**, 165–176 (1968), DOI `10.1016/0375-9474(68)90710-0`，与出版 PDF 的 PII 及出版商 Crossref 登记一致。
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/mixing ratio/1968_Hamilton et al_Angular correlation measurements in 192Pt.pdf`。
- 12-page historical experiment; Ge+NaI cascade separation and summing polarimeter checked.

## Scope and Reading Depth

- PDF 1–12（印刷 165–176 页）：¹⁹²Ir 的级联，300/600 keV 复合峰，角关联分解，随机扣除，线偏振，表 1–2，图 1–6 和书目。复核表 2、图 4–6 和出版版结论。
- Not covered: raw coincidence matrices, full detector-response files and later `192Pt` evaluations.

## Key Evidence and Reasoning Chain

- A Ge detector resolves individual lines while NaI selects the 300-keV complex; linear equations disentangle three overlapping cascades and remove the 588-316 contribution.
- Angular coefficients `A22/A44` are corrected for centering, finite source size and solid angle; a summing polarimeter at 90° correlation angle measures `W(γ=0/90)` and polarization.
- Reported E2:M1 mixing ratios are `δ(296)=−9.0 to −11.0`, `δ(308)=−6.5 to −8.3`, `δ(604)=+1.9 to +2.4`, with polarization selecting branches and confirming accepted spins.
- The method is designed to address poor Ge resolution/complex cascades and to inform possible E0 conversion-electron interpretations of the `2+→2+` transition.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HD68-1 | Ge+NaI composite angular correlations separate overlapping 296/308/316 and 588/604-keV cascade contributions. | method-result | direct | PDF pp.165–171, Figs.1–3 | true |
| HD68-2 | 在级联角 \(90^\circ\) 的双 NaI 极化装置给出的是复合相关。300–300 keV 组测 \(P=-0.020\pm0.024\)，含六种有次序的极化贡献。600–300 keV 组分析 600 keV 侧，给 \(P=-0.129\pm0.042\)。利用级联权重、未观测线的退取向及标定求各线约束。 | method-result | direct | 168、173、175 页，图 4–6 | true |
| HD68-3 | 合并依据后的 \(\delta(296)\in[-11,-9]\)、\(\delta(308)\in[-8.3,-6.5]\)、\(\delta(604)\in[1.9,2.4]\)。单独的极化分解给 296 keV 的 \(-(6.2^{+\infty}_{-1.7})\) 与 604 keV 的 \(2.4^{+6}_{-1.6}\)。308 keV 的主要定量约束来自 308–612 keV 的方向关联，表 2 给 \(-(7.3^{+1.0}_{-0.8})\)。 | experimental-result | direct | 165、172、175 页，表 2 | true |
| HD68-4 | 604–316 keV 的 \(A_{22}=-0.480(16)\)，而 \(A_{44}=+0.34\pm2.23\)。构造 588→296→316 的污染修正需要从测得的级联组合做除法，小的四阶输入使传播误差放大。对 296–316，作者讨论 \(A_{44}\) 偏小和约两倍标准差容差。 | experimental-and-uncertainty | direct | 167、171–172 页，表 1–2 | true |

## Summary

Hamilton & Davies demonstrate a practical resolution of complex low-resolution γγ cascades using a Ge/NaI hybrid and a summing polarimeter, yielding consistent E2/M1 mixing ratios for `192Pt`.

## Competing Interpretations and Limitations

Results depend on intensity/branching weights, internal-conversion coefficients, solid-angle/centering corrections and polarization sensitivity. Historical line-shape subtraction and convention mapping are required before modern quantitative reuse.

- 方向系数的峰面积/峰高检验使用同一数据，原文不因此降低误差。极化分解采用未观测 296 keV 的 \(\lvert\delta\rvert=10\) 计算 \(A_2U_2=0.12\)、\(A_4U_4=-0.291\)。这处固定条件属于污染级联建模。
- 表 2 注明，296 keV 在线序反转后换号。末节给出 Biedenharn 定义，并指出对这三条线，最终所列符号与 Rose–Brink 一致。关于 [[rikovska-1983-irfe-pt192-polarization]] 所列反号与幅度差，尚需从其完整方法原文核实对应相位，不能以符号映射消除幅度差。
- 方向角关联和线偏振的分析角、门与探测器各有定义。极化装置和标定见 [[davies-hamilton-1968-gamma-gamma-polarimeter-calibration]]。本文使用衰变级联的角关联，未报告在束 \(\sigma/I\)。

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| HD68-AR-1 | Cascade chain | Composite coefficients → cascade separation → A22/A44 → polarization branch selection → δ. | PDF pp.166–172 | self-checking |
| HD68-AR-2 | Convention | δ signs and temporal order follow the paper's convention; cross-source Rose–Brink mapping required. | Table 2 notes | self-checking |
| HD68-AR-3 | Failure condition | Overlap subtraction/solid-angle/random corrections can bias small coefficients and δ. | PDF pp.167–172 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-correlation]], [[linear-polarization-asymmetry]] and [[multipole-mixing-ratio]].
- Persistence: historical method source; no new project-level scientific claim.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `HD68-P0-1`: preserve convention, cascade weights and detector corrections before comparing δ across sources.

## Extracted Pages

- Methods: [[angular-correlation]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]]。
