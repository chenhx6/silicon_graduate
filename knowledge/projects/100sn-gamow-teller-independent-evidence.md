---
type: project
title: "100Sn Gamow-Teller independent evidence map"
aliases: [100Sn BGT comparison, 100Sn decay spectroscopy evidence map]
created: 2026-09-06
updated: 2026-09-07
status: ai-draft
review_status: unreviewed
project_stage: competing-evidence-matrix
confidentiality: private
nuclei: [100sn]
tags: [a100, 100sn, gamow-teller, beta-decay, evidence-map, project]
---

# `100Sn` Gamow–Teller 独立证据地图

## Project Purpose

本项目比较 GSI 与 RIKEN 两条 `100Sn` 衰变谱学实验链，追踪 `B(GT)`、Q/endpoint、衰变分支和 `100In` 能级方案之间的依赖关系。它不把数值差异裁决为物理矛盾，也不替代两份 source 的 claim-level 人工复核。

## Research Question

`B(GT)=9.1(+4.8/-2.3)`（GSI）与 `5.26(+0.90/-1.06)`（RIKEN）的差异，能否由 Q/endpoint、统计量、single-state 或 branching 假设、探测器响应和模型约定解释？哪些 companion observables 才能把分析差异与真实 GT 结构差异区分开？

## Current Hypotheses

- H1：主要差异来自 Q/endpoint、branching、response 或 phase-space 输入，而非真实 GT 矩阵元变化。
- H2：`100In` 未闭合的低能分支/能级方案使 single-state 或 branching 假设不一致，从而传播到 B(GT)。
- H3：即使统一实验输入，shell-model space/quenching convention 仍可能造成残余差异；该假设需要共同模型重算。

## Source Roles and Independence

| Source | Facility / lineage | Project role | Evidence independence |
|---|---|---|---|
| [[hinke-2010-100sn-decay-spectroscopy]] | GSI FRS + SIMBA/RISING；`124Xe` projectile fragmentation at 1 GeV/u | historical low-statistics `100Sn` half-life/endpoint/BGT baseline | single within source; independent of RIKEN chain |
| [[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]] | RIKEN RIBF BigRIPS/WAS3ABi/EURICA；345 AMeV `124Xe+9Be` | higher-statistics Q-value, BGT and neighboring-nuclei decay chain | single within source; independent of GSI chain |

两条链标为 `multiple-independent`：不同 facility、植入/响应系统和 analysis chain。它们不是同一实验的重复出版，但数值仍不能在统一输入和误差模型前合并。

## Evidence Available

Raw-PDF reread completed for Hinke Ch.5.1–5.4 and Ch.6.2/7.1, and Lubos Ch.4.2/4.4 and Ch.5.1. The crosswalk below separates measured inputs, analysis corrections, derived observables and model comparisons.

## Evidence Matrix

| Claim / observable | GSI support | RIKEN support | Main dependency or limitation | Current status |
|---|---|---|---|---|
| `100Sn` half-life | `1.16±0.20 s` from MLH mother/daughter/granddaughter/background fit; about 70 mother decays（HK10-2；Ch.5.1 pp.57–59；Table 5.1） | `1.17±0.10 s`; β-gated check used `N=204` correlations（LB16-2；Ch.4.4.2 p.83；Ch.5.1） | Different event samples and likelihood selections; values are numerically compatible within quoted uncertainty | reported, needs review |
| Endpoint / Q-value | Raw endpoint `3.15±0.20 MeV`; `+200 keV` bremsstrahlung/annihilation and `−59 keV` conversion correction → `Eβ0=3.29±0.20 MeV`; 87% β+ / 13% EC（HK10-3；Ch.5.3 pp.63–66） | Raw `Q=3.81` from `χ²` fit; ≈63 keV conversion-electron correction → `Q=3.74±0.14 MeV`; Q fit uses 600–3000 keV and Geant4 response（LB16-2/LB16-8；Ch.4.4.1 pp.77–78；Eqs.4.19–4.20） | Different endpoint/Q conventions and correction chains; Hinke’s single-state fit excludes low-energy region, Lubos includes daughter/response components | reported, needs review |
| `B(GT)` / `log(ft)` | `BGT=9.1(+4.8/-2.3)` from single-channel formula; Hinke calls it Super GT and notes large statistical uncertainty（HK10-5/HK10-8；Ch.6.2 pp.76–79；Eq.A.8；Ch.7.1） | `BGT=5.26(+0.90/-1.06)`, `log(ft)=2.86±0.08` from Eq.4.25 with `T1/2=1.17 s`, `Q=3.74 MeV`; fit-range/systematic dependence noted（LB16-2/LB16-8；Ch.4.4.2 pp.80–81；Eqs.4.25–4.27） | Phase-space/Q input, branching, response and shell-model convention; no silent average | central unresolved comparison |
| `100In` level scheme / branching | Five γ lines: 96, 141, 436, 1297, 2048 keV; Table 5.2 intensities are low-statistics and γγ shows only a 3-count 96–436 keV hint（HK10-4/HK10-6；Ch.5.2 pp.59–62；Table 5.2；Fig.5.7） | 96/141/436 keV intensities are approximately equal while 1297/2048 keV form two branches; ≈50 keV `5+→6+` link candidate; extra fragmented LSSM branches absent（LB16-3；Ch.4.2 pp.70–75；Figs.4.17–4.20；Ch.5.1 pp.83–84） | γγ closure, multipolarity and low-energy efficiency are decisive; candidate is not confirmation | complementary, not yet closed |
| `100Sn` 6+ isomer | Four counts near 3004 keV in first 25 ns; timing probability requires `Eγ<100 keV`, `B(E2)≈40 W.u.`, while realistic `≈1 W.u.` favors later bins（HK10-7；Ch.5.4 pp.66–68；Fig.5.9） | No independent confirmation in the thesis summary; missing weak branches remain a stated limit（LB16-3） | Delayed timing, detector response and higher-statistics γγ/total-absorption data required | unresolved |

## Interpretations and Alternatives

- `B(GT)` 数值差异首先应作为 analysis/input difference 的候选，而不是 GT quenching 的直接反证；两份 source 都把 response、branching 或 level-scheme assumptions 置于解释链中（HK10-8；LB16-8）。
- Hinke 的 “Super Gamow–Teller / no obvious quenching” 与 Lubos 的 large-space shell-model comparison 都是作者解释或模型比较，不是独立实验事实。
- Model-space crosswalk: Hinke discusses a dominant isolated `1+` final state and reports no obvious quenching within large statistical errors; Lubos contrasts extreme single-particle `BGT=17.78`, `g_A` renormalization (`≈10`) and LSSM sums (`8.19` all final states, `7.82` within QEC window, first excited `1+` contribution `5.7`). These are model outputs/interpretations, not directly measured observables (Hinke Ch.1 pp.5–8; Lubos Ch.4.4.2 pp.80–81).
- `100In` 的低能 level ordering、约 50 keV link 和 `6+` isomer 仍可由 missing weak branches、multipolarity ambiguity 或统计限制解释；“未观测”在当前灵敏度下只写为 conditional limitation。

## Risks and Blockers

- 两份 source 的 claim-level `needs_review` 尚未完成；当前 project 不适合作为论文级数值引用。
- 原始 PDF 的逐页 crosswalk、共同 Q/phase-space 定义和 response 参数仍缺失；不能用摘要数字替代。
- 受保护 BibTeX 和 Git 发布能力不属于本项目科学证据，当前 `.git` probe 失败也不改变内容判断。

## Next Actions

1. 将本轮已核对的 HK10/LB16 页码、图表和公式输入写入 source-level audit；保留 claim-level `needs_review`。
2. 建立统一表格：half-life、endpoint/Q、β+/EC branching、response correction、phase-space、B(GT)、model-space。
3. 仅在 companion observables 闭合后，决定是否更新 `100sn`/`gamow-teller-strength` 的 synthesis wording。

## Necessary Companion Observables

要把两条 `B(GT)` 链放入同一比较，至少需要：

1. 明确 endpoint/Q-value 定义、质量输入、β+/EC 分支和 phase-space convention；
2. 回查 Hinke 的 70-event MLH/single-state fit 与 `+200−59 keV` correction，及 Lubos 的 1070-event Q spectrum、24 daughter components、19.8% daughter fraction、600–3000 keV fit range 和 ≈63 keV conversion correction；
3. 逐条核对 `100In` γ branching、γγ closure、multipolarity 和低能探测效率；
4. 对 `6+` isomer 候选给出 delayed-time distribution、响应模型和统计灵敏度；
5. 用相同 shell-model space、矩阵元和 quenching convention 重算 comparison，而不是比较不同 model-space 的单个数字。

## Knowledge Impact and Learning Decision

- **此前认识**：Wiki 已有两个 source 和 `100sn`/`gamow-teller-strength` 页面，但差异主要以“不可直接平均”一句话保存。
- **本轮修正**：把差异拆成 half-life、endpoint/Q、BGT、level scheme 和 isomer 五个可审计维度；当前最关键 gap 是 Q/endpoint 与 branching/response 的逐输入 crosswalk。
- **证据边界**：两条实验链是 `multiple-independent`，但每条 source 内的数值和解释仍为 `needs_review: true`；本项目不提升任何 review_status 或 confidence。
- **持续化决定**：保留本 project 作为后续 claim-specific review 的 owning page；不新建 `100In`、`6+` isomer 等页面，直到有独立结构信息和可复核 locator。

## Open Questions and Falsifiers

- 若统一 Q/phase-space、branching 和 response 后两值仍显著不一致，需要检查 source-level event selection、未观测分支或模型矩阵元，而不能直接归因于 quenching。
- 若新的 γγ/total-absorption 数据关闭 `100In` 弱分支或否定约 50 keV link，当前 level-scheme interpretation 必须修订。
- 若更高统计 delayed timing 明确 `6+` isomer，Hinke 的“insufficient counts”边界可被更新；反之仍应保持 conditional non-confirmation。

## Human Review Triage

### P0

- 核对 HK10-2/HK10-5 与 LB16-2 的 half-life、endpoint/Q、BGT、`log(ft)` 数值和 locator，确认 phase-space、single-state、branching 与误差传播没有被混写。
- 核对 HK10-4/HK10-6 与 LB16-3 的 `100In` 五条 γ 线、约 50 keV candidate、multipolarity/level-ordering 边界，避免把 candidate 写成 established link。
- 审核 evidence matrix 中“multiple-independent”是否仅表示不同实验链，不把两个 thesis 的模型比较当成独立物理证据。

### P1

- 回 source/raw 核对 MLH、positron-response、annihilation/conversion 和背景/子体处理，建立统一输入 crosswalk。
- 核对 shell-model model-space、quenching convention 及 `6+` delayed-γ 灵敏度；判断哪些比较可迁移到其它 A≈100 N=Z 核素。

### P2/P3

- 后续仅在有可靠原始谱图和 locator 时建立 `100In`/`90Rh` 等邻核页面。
