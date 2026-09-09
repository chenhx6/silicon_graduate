---
type: source
title: "Lubos 2016 博士论文：100Sn 及邻近核素衰变谱学"
aliases: [Lubos 2016 100Sn thesis, Decay Spectroscopy of 100Sn and Neighboring Nuclei]
created: 2026-09-05
updated: 2026-09-07
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment
reading_depth: deep-read
title_original: "Decay Spectroscopy of 100Sn and Neighboring Nuclei"
authors: [Daniel Georg Lubos]
advisor: [Reiner Krücken, Stefan Schönert]
journal: "Technical University of Munich doctoral dissertation"
year: 2016
volume:
pages: 111
doi:
arxiv:
language: en
canonical_source: "Lubos, Daniel Georg. Decay Spectroscopy of 100Sn and Neighboring Nuclei[D]. Technical University of Munich, 2016."
zotero_item_key:
citation_key: ""
zotero_uri:
library_file: "raw/papers/degree dissertation/Decay Spectroscopy of 100 Sn and Neighboring Nuclei.pdf"
raw_file: "raw/papers/degree dissertation/Decay Spectroscopy of 100 Sn and Neighboring Nuclei.pdf"
raw_sha256: "C9AA0494F29BACC00EC8FB0055A5D6AC201237E3BAD943EA34D350DEEB8550D9"
nuclei: [100sn, 96cd, 98in, 94ag, 90rh, 99sn, 97in, 95cd, 91pd, 93ag, 96in, 94cd, 92ag, 90pd, 98cd]
reactions: ["124Xe projectile fragmentation on 9Be at 345 AMeV"]
experiments: []
models: [large-scale-shell-model, maximum-likelihood-analysis]
observables: [half-life, q-value, gamow-teller-strength, proton-branching-ratio]
methods: [decay-spectroscopy, beta-gamma-coincidence, maximum-likelihood-analysis, positron-calorimetry]
tags: [a100, 100sn, decay-spectroscopy, riken, gamow-teller, proton-dripline, phd-thesis]
---

# Lubos 2016：`100Sn` 及邻近核素衰变谱学

## Bibliographic Record

Daniel Georg Lubos，*Decay Spectroscopy of 100Sn and Neighboring Nuclei*，Technical University of Munich，博士学位论文，2016，111 页。原始 PDF SHA-256 为 `C9AA0494F29BACC00EC8FB0055A5D6AC201237E3BAD943EA34D350DEEB8550D9`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: Abstract、Chapters 1–4、Summary/Prospects；核对 RIKEN BigRIPS、WAS3ABi、EURICA、MLH、Q-value/positron response、`100Sn` BGT、`98In/94Ag/90Rh` isomers、N=Z−1/−2 half-lives 和 proton emission。
- Not covered: 全部引用文献独立复核、补充实验 proposal 的后续结果。
- Coverage caveats: 多核素 half-life/Q-value 表格含不同 decay components 和 model assumptions；需按核素、isomer 和 decay branch 分层。

## Paper Question and Scientific Motivation

论文围绕 `100Sn` 及 N=Z、N=Z−1、N=Z−2 邻近核素，测量 half-lives、Q-values、γ/β branching 和 proton emission，以检验壳模型、GT strength、CVC/rp-process 与质子滴线结构（Abstract；Ch.1）。

## Method and Design Logic

实验在 RIKEN RIBF 用 345 AMeV `124Xe` + `9Be` projectile fragmentation，经 BigRIPS 识别并将 A≈100 cocktail 植入 WAS3ABi；EURICA 记录 decay γ，Si array 同时进行 β/positron calorimetry。MLH、Bateman/decay-correlation、`χ²` Q-value fitting 和 branching analysis 将多核素衰变链分离（Chapters 2–4）。

## Key Evidence and Reasoning Chain

1. BigRIPS PID 和 WAS3ABi implantation/decay correlation 确认 `100Sn` 与邻核。
2. Unbinned MLH/decay-chain models 提取多核素 half-lives。
3. `χ²` positron-energy fit 结合 detector response、bremsstrahlung、annihilation 和 implantation geometry 得到 Q-values。
4. EURICA γ/γγ、β-delayed p branches 和 decay components 约束 `100In/98In/94Ag/90Rh` level/isomer structure。
5. `100Sn` half-life+Q-value 得到 `BGT`，与 large-space shell model 比较。

## Summary

在 RIKEN 实验中识别 2525 个 `100Sn`，得到 `T1/2=1.17±0.10 s`、`Q=3.74±0.14 MeV`、`BGT=5.26(+0.90/-1.06)` 和 `log(ft)=2.86±0.08`。确认 `100In` 既有 level ordering，并提出约 50 keV `5+→6+` link candidate。论文还报告 N=Z−2 核素首次识别/寿命、`93Ag` proton emitter `228±16 ns`、`90Rh` long-lived `5+` isomer candidate，以及 `98In` 9+ isomer/双 decay components。各项结论需按 decay chain 和 branch 的证据强度分开。

## Experimental or Theoretical Setup

- RIKEN BigRIPS、WAS3ABi、EURICA；`124Xe` 345 AMeV + `9Be`。
- MLH/Bateman、implantation-decay correlations、positron calorimetry、Q-value fit、γ/γγ coincidence。
- Large-scale shell model、CVC/rp-process 和 proton-emission interpretation。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| LB16-1 | RIKEN `124Xe+9Be` 345 AMeV、BigRIPS/WAS3ABi/EURICA 实验识别 2525 个 `100Sn` 并同时测邻近 A≈100 核素。 | experimental-fact | direct | single | Abstract；Ch.2；Ch.4 | true |
| LB16-2 | `100Sn` half-life 为 `1.17±0.10 s`，Q-value 为 `3.74±0.14 MeV`，由 `BGT=3811.5/[f(Z,Q)T1/2]` 得到 `BGT=5.26(+0.90/-1.06)`、`log(ft)=2.86±0.08`。 | derived-observable + method-formalism | direct | single | Ch.4.4.1–4.4.2 pp.77–81；Eqs.4.19–4.27；Ch.5.1 p.83 | true |
| LB16-3 | `100Sn` β-delayed γ spectroscopy 支持既有 `100In` level ordering；96/141/436 keV 强度近似相等、1297/2048 keV 为两条分支，并提出约 50 keV `5+→6+` link candidate；LSSM 预言的额外弱分支尚未观测。 | experimental-fact + analytical-boundary | indirect | single | Ch.4.2 pp.70–75；Fig.4.17–4.20；Ch.5.1 pp.83–84 | true |
| LB16-4 | N=Z−2 `96In,94Cd,92Ag,90Pd` 首次识别并测寿命；N=Z−1 核素 half-lives 约 27–33 ms。 | experimental-fact | direct | single | Abstract；Ch.4.1；Table 5.1 | true |
| LB16-5 | `93Ag` 被确认是质子发射体，半衰期 `228±16 ns`；`94Ag` 的已报道 1p/2p emission 在本实验未观察到。 | experimental-fact | direct | single | Abstract；Ch.4.13–4.16；Ch.5.1 | true |
| LB16-6 | `98In` decay curve 含 T=0/T=1 fast/slow components，并支持 9+ isomer 与 `98Cd` 8+/10+ daughter branches；level ordering 仍有讨论。 | experimental-fact + author-interpretation | indirect | single | Ch.4.8–4.10；Ch.5.1 | true |
| LB16-7 | `90Rh` 具有 long-lived isomer candidate，γ spectroscopy 给出 `90Ru` daughter ordering 和新 1163/1316 keV lines，`5+` spin-parity 为 tentative。 | experimental-fact + author-interpretation | indirect | single | Ch.4.12–4.13；Ch.5.1 | true |
| LB16-8 | Q-value fit 使用 600–3000 keV 区间、Geant4 positron-response simulation、24 个 `100In` β+ components，显式计入 19.8% daughter contribution 和 96/141 keV conversion-electron deposition；BGT 的系统误差与 fit-range/response 相关。与 Hinke 2010 是独立 RIKEN/GSI experiments，不能简单平均。 | analytical-boundary | inferred | multiple-independent | Ch.4.4.1–4.4.2 pp.77–81；Figs.4.22–4.24 | true |

## Nuclear Structure Information

- `100Sn`：GT decay、Q-value、`100In` low-energy γ scheme。
- `98In/94Ag/90Rh`：odd-odd N=Z isomers、Fermi/GT components、γ/particle branches。
- N=Z−1/−2 核素：half-life、proton emission 和 dripline identification。

## Raw Locator Audit (2026-09-07)

- The corrected Q chain is explicit: raw fit `Q=3.81` with fit-range systematic discussion (p.77), average conversion-electron contribution ≈63 keV from 96/141 keV lines, and corrected `Qcorr=3.74±0.14 MeV` (p.78; Eqs.4.19–4.20).
- The Q spectrum includes 24 simulated `100In` β+ components, 19.8% daughter contribution in the 3 s window, and a statistically useful comparison range of 600–3000 keV (pp.77–78; Fig.4.23).
- `BGT` is calculated from the half-life and Q via Eq.4.25; the thesis attributes the lower value relative to the extreme single-particle 17.78 to large-space/model-space treatment and higher `1+` states, not to a new direct strength observable (pp.80–81; Fig.4.24).

## Authors' Interpretation

作者把 `100Sn` BGT 与 large-space shell model 比较，并把 `93Ag` proton emission、`98In`/`90Rh` isomer 解释放入 N=Z 线和核天体物理背景；对 level ordering、isomer spin 和 missing transitions 保留不确定性。

## Model Results

- MLH/Bateman/response simulation：half-life、Q-value 和 branching extraction。
- LSSM：`100In` level ordering/BGT comparison；CVC/rp-process 用于物理意义讨论。

## Competing Interpretations and Limitations

- Hinke 2010 与 Lubos 2016 的 `100Sn` BGT 不同，来自不同统计、Q-value、response and analysis；差异不能直接写成物理矛盾。
- `100In` 50 keV link、`98In` level ordering、`90Rh` 5+ 和 `94Ag` proton branches 仍需原始谱图/后续 experiment。
- 多核素 half-life table 不等于每个核素拥有相同 detector/branch sensitivity。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-LB16-1 | Core reconstruction | 该论文把 `100Sn` GT/Q-value 与邻近滴线核素 decay spectroscopy 置于同一可复现 MLH/response framework。 | LB16-1–8 | unreviewed |
| AR-LB16-2 | Assumptions and dependencies | Q-value/BGT、isomer half-life 和 branch assignment 依赖 detector response、decay chain 和 branch assumptions。 | Chs.3–4 | unreviewed |
| AR-LB16-3 | Transfer conditions | 可与 Hinke 2010 形成 independent `100Sn` comparison，也可作为 A≈100 decay-spectroscopy 方法基线。 | LB16-2/8 | unreviewed |
| AR-LB16-4 | Failure conditions | 更高统计 γγ/total absorption 或新的 mass/Q measurements 改变 `100In` ordering/BGT 时需修订。 | LB16-3/8 | unreviewed |
| AR-LB16-5 | Reverse/falsification test | 逐核素回查 decay component、Q fit residual、γγ closure、proton branch 和 daughter level ordering。 | Ch.4 tables/figures | unreviewed |
| AR-LB16-6 | Research-question decision | 建立 `100Sn` independent-experiment evidence map，并保留 N=Z dripline 方法桥接。 | LB16-2–8 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: 本轮 Hinke 2010 刚建立 GSI `100Sn` baseline；Lubos 提供独立 RIKEN 高统计更新和邻核扩展。
- Effect of this source: supports and refines；为 `100Sn` BGT/Q-value 和 `100In` level ordering 提供独立实验链，同时引入多核素边界。
- Reason: 两个实验可做独立比较，不应合并统计或视为同一数据集。
- Persistence decision: 新建 source；更新 `100sn` nucleus；不批量建立全部邻核页面。
- Review state: 页面 `unreviewed`；LB16-2–8 保留 claim-level review。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[100sn]] | 提供 RIKEN 独立高统计 `100Sn` decay baseline。 |
| competing-interpretation | [[gamow-teller-strength]] | `BGT` 受 Q-value/response/analysis 条件影响。 |
| methodological-bridge | [[lifetime]] | 多核素 MLH/decay-correlation lifetime extraction。 |

## Human Review Triage

### P0

- LB16-2/LB16-3：核对 `100Sn` T1/2、Q、BGT、log ft、50 keV link 和未观测分支边界。
- LB16-5/LB16-7：核对 `93Ag` proton emitter、`90Rh` 5+ isomer 和新 γ lines 的 assignment 强度。

### P1

- LB16-1/LB16-4：核对 2525 `100Sn`、N=Z−1/−2 sample 和 half-life table。
- LB16-6/LB16-8：与 Hinke 2010 做 independent experiment、response and branch audit。

### P2/P3

- 后续按实际研究问题建立 `98In`/`94Ag`/`90Rh` 页面。

## Extracted Pages

- Nuclei: [[100sn]]。
- Methods: [[lifetime]]、[[gamma-gamma-coincidence]]。

## Non-source Notes and Follow-up

该论文与 Hinke 2010 的 GSI 实验不是同一数据集；两者应作为 `multiple-independent` 证据并列。
