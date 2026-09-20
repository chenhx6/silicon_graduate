---
type: source
title: "General properties of the πh9/2[541]1/2− configuration and level scheme of 165Tm"
aliases: ["Jensen 2001 165Tm", "NPA695 Jensen 165Tm", "HS-006 HS-007 canonical duplicate group"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "General properties of the πh9/2[541]1/2− configuration and level scheme of 165Tm"
authors: ["H. J. Jensen", "R. A. Bark", "P. O. Tjøm", "G. B. Hagemann", "I. G. Bearden", "H. Carlsson", "S. Leoni", "T. Lönnroth", "W. Reviol", "L. L. Riedinger", "H. Schnack-Petersen", "T. Shizuma", "X. Z. Wang", "J. Wrzesinski"]
journal: "Nuclear Physics A"
year: 2001
volume: 695
issue: "1-4"
pages: "3-50"
doi: "10.1016/S0375-9474(01)01111-3"
language: en
canonical_source: "Jensen, H. J. et al. General properties of the πh9/2[541]1/2− configuration and level scheme of 165Tm. Nucl. Phys. A 695, 3-50 (2001)."
library_file: "raw/papers/gpt/high-spin-20260920/NPA695-Jensen-2001-3.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/NPA695-Jensen-2001-3.pdf"
raw_sha256: "0fde4a838d94fdc23dcd4d4034a945073cb569c47c153e9e3b90676c44838770"
duplicate_ids: ["HS-006", "HS-007"]
nuclei: ["165Tm", "164Tm", "164Er", "166Yb"]
reactions: ["150Nd(19F,4n)165Tm", "154Sm(15N,4n)165Tm"]
experiments: ["nordball-165tm-f19-85mev", "nordball-165tm-n15-70mev"]
models: ["cranked-shell-model", "cranked-nilsson-strutinsky-model", "potential-energy-surface", "two-band-mixing"]
observables: ["level-scheme", "dco-ratio", "mixing-ratio", "transition-quadrupole-moment", "lifetime", "alignment", "crossing-frequency", "B(M1)/B(E2)", "B(E1)/B(E2)"]
methods: ["gamma-gamma-coincidence", "dco-ratio", "doppler-shift-attenuation-method", "band-mixing"]
tags: [165Tm, h9-2, delayed-alignment, i13-2-alignment, gamma-vibration, DSAM, quadrupole-moment, rare-earth]
---

# General properties of the πh9/2[541]1/2− configuration and level scheme of 165Tm

## Bibliographic Record

- 作者：H. J. Jensen 等；*Nuclear Physics A* 695(1-4), 3-50 (2001)。DOI：`10.1016/S0375-9474(01)01111-3`。
- 规范来源：HS-006 `NPA695-Jensen-2001-3.pdf`。HS-007 是同一 SHA-256 的第二个外部路径副本，已完成逐条 duplicate audit，不重新摄入。
- 规范 raw 文件：`raw/papers/gpt/high-spin-20260920/NPA695-Jensen-2001-3.pdf`；SHA-256：`0fde4a838d94fdc23dcd4d4034a945073cb569c47c153e9e3b90676c44838770`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: 48 页全文；引言、两次熔合蒸发实验、Nordball γγ/γγγ 与 DCO 分析、完整 `165Tm` 能级图、四条新带、DSAM lineshape/lifetime/Qt、band mixing、B(M1)/B(E2)、CSM/Ultimate Cranker 形变和 crossing-frequency 系统学、E1 概率与总结均已阅读。Fig.2-3、5-8、9-19 和 Tables 1-8 的关键图表视觉核对。
- Not covered: 原始事件树、DSAM stopping-power Monte Carlo code、Ultimate Cranker code/input 和引用来源全文。
- Coverage caveats: 大量 Table 1 逐线数据保留在 source 原文；本页只固化改变组态、形变、alignment 和竞争解释排序的结果。部分新带自旋/组态仍为作者建议或多解 DCO 解释。

## Paper Question and Scientific Motivation

- 论文研究稀土 `165Tm` 中 `πh9/2[541]1/2−` 的形变、`i13/2` 中子延迟 alignment 和 crossing-frequency shift，并扩展高自旋能级纲图（PDF pp.3-4）。
- 主要问题是：变形改变、质子-中子相互作用和 pairing/Cor iolis effects 各自能解释多少 `πh9/2` 带相对于邻近 even-even 核的 delayed alignment；同时建立四条新带及其 γ-vibrational/3qp 性质。

## Method and Design Logic

- 两次实验：`150Nd(19F,4n)`，`85 MeV`；`154Sm(15N,4n)`，`70 MeV`。Nordball 使用 20 个 Compton-suppressed HPGe 和 60 元 BaF2 inner ball；最高统计达 `1.4×109` 和 `0.8×109` coincidence events（PDF pp.4-6）。
- `Eγ-Eγ` 矩阵和 `Eγ-Eγ-Eγ` cube 建立 level scheme；四环探测器角度约 `37.4°/79.2°/100.8°/142.6°`。DCO 用 `W(37×79)/W(79×37)`，dealignment 用 `W(37×37)/W(79×79)`；测得 `σ/I=0.26(4)`（PDF pp.6-7）。
- DSAM 用电子/核 stopping、Monte Carlo recoil velocities、Bateman feeding 和 lineshape least-squares 拟合；每个 backing 的四角谱用于 lifetime/Qs/Qt（PDF pp.23-27）。
- 相对形变用 two-band mixing；crossing frequencies、aligned angular momenta 和 `B(M1)/B(E2)` 约束新带组态；Ultimate Cranker diabatic PES/CSM 计算比较形变与 alignment（PDF pp.27-43）。

## Key Evidence and Reasoning Chain

1. Level scheme 扩展到 `71/2−`，新建四条带：两条 `K=17/2` 三准粒子候选带，另两条归为与 h9/2 质子耦合的 γ-vibrational bands（摘要；PDF pp.3, 19-23）。
2. `[541]1/2−` favoured signature 延伸至 `53/2−`，unfavoured signature 至约 `39/2−/43/2−`；`[411]1/2+` 和 `[404]7/2+` 分别扩展至 `67/2+`、`53/2+`（PDF pp.19-23）。
3. Bands 3/4 的 in-band DCO 多数支持 stretched E2，band 3 到 `[541]1/2−` 的平均 DCO `0.36(5)` 给出两个 δ 分支；band 4 的自旋/负宇称仍需结合 signature-partner、B(E2) 和邻核 γ band 系统学（PDF pp.22-23，Fig.5）。
4. DSAM 给出 `[541]1/2−` 加权 `Qt=8.3(5) eb`、`β2≈0.33`；`[411]1/2+` 为 `Qt=7.4(5) eb`、`β2≈0.30`。相对两带 mixing 进一步给 `[404]7/2+≈7.1(6) eb`、`[523]7/2−≈7.2(7) eb`，说明 h9/2 `[541]1/2−` 带形变约高 `12-15%`（PDF pp.25, 33-35，Tables 2,5,6）。
5. `[541]1/2−` 的 AB crossing 约 `355 keV`，显著高于 `[523]7/2−`、`[404]7/2+`、`[411]1/2+` 和邻近 even-even bands 的约 `247-281 keV`；CSM/PES 只解释部分 shift，剩余部分需要 pairing、configuration effects 或 residual proton-neutron interaction（PDF pp.36-43，Tables 3,8，Figs.17-18）。
6. `[411]1/2+↔[541]1/2−` interband E1 transitions 的强度比单粒子估计增强约 3-5 个数量级；加入 core octupole-vibrational coupling 后定性改善，但 spin/signature dependence 仍未完全解释（PDF pp.44-46，Fig.19）。

## Summary

Jensen 等人的 `165Tm` 工作把高统计 γγ/γγγ 谱学、DCO、DSAM 寿命、band mixing、alignment 和 diabatic CSM/PES 系统学结合起来。实验扩展了能级图并发现四条新带；DSAM 直接支持 `πh9/2[541]1/2−` 带比其它近邻带有更大形变。模型能解释部分 delayed `i13/2` crossing shift，但系统性低估 `[541]1/2−` 的 shift，提示形变之外还需残余质子-中子相互作用等机制。E1 增强指向八极振动耦合，但仍保留模型依赖。

## Experimental or Theoretical Setup

- `150Nd(19F,4n)` at 85 MeV and `154Sm(15N,4n)` at 70 MeV；Nordball 20 HPGe + 60 BaF2。
- DCO geometry: 37.4°, 79.2°, 100.8°, 142.6°；`σ/I=0.26(4)` from known stretched cascades。
- DSAM: thin/backed targets, Au/Pb stopping, four angular spectra, cascade side-feeding model with fixed `J(2)=65.0 ħ²/MeV`。
- Theory: two-band mixing, Ultimate Cranker diabatic PES/CSM, semiclassical B(M1)/B(E2), particle-rotor/octupole-coupling E1 estimates。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| J01-1 | `165Tm` level scheme extends to `71/2−` and adds four bands: two K=17/2 3qp candidates and two γ-vibrational bands coupled to h9/2 proton. | experimental-result/author-interpretation | direct | PDF pp.3,19-23，Figs.2-5 | true |
| J01-2 | DSAM gives weighted `Qt=8.3(5) eb` for `[541]1/2−` and `7.4(5) eb` for `[411]1/2+`; relative mixing gives `[404]7/2+≈7.1(6) eb`, `[523]7/2−≈7.2(7) eb`. | experimental-result | direct | PDF pp.25,33-35，Tables 2,5,6 | false |
| J01-3 | `[541]1/2−` AB crossing is near `355 keV`, delayed relative to comparable bands and even-even neighbours near `247-281 keV`. | experimental-result | direct | PDF pp.36-43，Tables 3,8，Figs.17-18 | false |
| J01-4 | CSM/PES explains only part of the delayed crossing; residual proton-neutron interactions are proposed as an additional contribution. | author-interpretation/model-result | direct | PDF pp.36-43 | true |
| J01-5 | E1 strengths between `[411]1/2+` and `[541]1/2−` are enhanced by orders of magnitude over single-particle estimates; octupole-vibrational coupling improves qualitative agreement. | experimental-result/model-result | direct | PDF pp.44-46，Fig.19 | true |

## Nuclear Structure Information

- `165Tm` bands: `[523]7/2−`, `[541]1/2−`, `[411]1/2+`, `[404]7/2+`, `[402]5/2+`, new bands 1-4, and candidate `[514]9/2−`, `[411]3/2+`.
- New-band assignments: band 1 `π[523]7/2−⊗ν[642]5/2+⊗ν[523]5/2−`, Kπ=17/2+; band 2 `π[404]7/2+⊗ν[642]5/2+⊗ν[523]5/2−`, Kπ=17/2−; bands 3/4 likely γ bands coupled to h9/2 proton.
- `[541]1/2−` shape polarization and delayed alignment are the main structure results; E1 links to `[411]1/2+` connect opposite-parity configurations.

## Authors' Interpretation

- The h9/2 `[541]1/2−` proton drives a larger deformation and delayed i13/2 neutron alignment, but deformation changes alone cannot explain the full crossing shift.
- Bands 3/4 are interpreted as γ-vibrational structures because of low excitation, alignment behavior, and B(E2)out/B(E2)in comparisons with `164Er`; their detailed spins and δ branches remain less secure.

## Model Results

- Ultimate Cranker diabatic PES/CSM predicts relative deformations and crossing frequencies across rare-earth nuclei. For `165Tm`, calculated Q values are generally 1-8% below measured; relative deformation ratios agree better.
- Two-band mixing gives `Vint=5.0(5) keV`, `Q([404]7/2+)/Q([411]1/2+)=0.96(5)`; `[541]1/2−/[523]7/2−` mixing gives `Vint=1.75(18) keV`, `Q` ratio `1.16(9)`.
- Octupole-vibrational E1 operator improves qualitative trends but does not fully reproduce signature/spin dependence.

## Competing Interpretations and Limitations

- Bands 3/4: γ-vibration, 3qp bandheads, or mixed configurations are not completely separable with present weak links; band 4 signature-partner assignment is suggested but lacks direct 3↔4 linking transitions.
- CSM/PES underestimates `[541]1/2−` crossing shift by up to ~100 keV; pairing, deformation, p-n interaction and model assumptions compete.
- DSAM side-feeding is modeled with a three-transition cascade and fixed moment of inertia; stopping-power systematics receive an added 5% uncertainty, and statistics prevent gating above all transitions of interest.
- B(M1)/B(E2) calculations set δ=0 for many bands; ratios can be overestimated by up to ~10% where δ is not measured.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-J01-1 | Core reconstruction | The source is a rare complete chain from level scheme to DSAM Q moments and crossing systematics; the h9/2 deformation and delayed alignment are supported by independent observable classes. | PDF pp.19-46 | self-checking |
| AR-J01-2 | Assumptions and dependencies | Qt depends on stopping powers, side-feeding model and rotational formula; crossing interpretation depends on CSM/PES and reference moments of inertia. | PDF pp.23-43 | self-checking |
| AR-J01-3 | Transfer conditions | The method/physics transfers to other rare-earth h9/2 bands only with matched DSAM, band-mixing and crossing reference; numerical Qt/crossing values do not transfer. | PDF pp.25-43 | provisional |
| AR-J01-4 | Failure conditions | If new lifetimes, side-feeding or p-n interaction calculations change Q ratios or crossing shifts, the deformation-only explanation is insufficient and the configuration ranking changes. | PDF pp.36-43 | active-L3 |
| AR-J01-5 | Reverse/falsification test | Compare another h9/2 odd-Z chain with direct Qt, AB crossing and E1 strength; vary stopping powers/side feeding and add residual p-n interaction to CSM. | PDF pp.36-46 | candidate-L3 |
| AR-J01-6 | Research-question decision | This is a high-value comparative source for h9/2 shape polarization, delayed alignment and DSAM/systematics; no L4 is opened without raw lineshapes or executable CSM inputs. | PDF pp.23-46 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki already contains DSAM, high-spin alignment, shape and rare-earth references, but this source adds a full `165Tm` lifetime/Qt/crossing/E1 chain and explicit deformation-versus-p-n-interaction failure boundary.
- Effect of this source: `supports`, `limits` and `methodological-bridge`。
- Reason: It links direct lifetimes and branching to model interpretation while keeping CSM/PES and E1 octupole explanations separate from measured quantities.
- Persistence decision: source page and existing DSAM/alignment method links; no new `165Tm` band pages in this first pass beyond source-level mapping.
- Review state: `unreviewed`; claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[doppler-shift-attenuation-method]] | Detailed DSAM lineshape, side-feeding and stopping-power uncertainty example. |
| supports | [[angular-momentum-alignment]] | AB crossing and aligned angular momentum systematics connect band structure to neutron alignment. |
| limits | [[triaxial-deformation]] | Measured deformation supports core polarization, but deformation alone fails to explain the full crossing delay. |
| foundational-background | [[high-spin-phenomena]] | Extended level scheme, DCO, band mixing and rare-earth crossing history. |

## Human Review Triage

### P0

- J01-P0-1：`Qt`、`β2` 和 crossing-frequency values depend on DSAM stopping/feeding and reference-model assumptions; paper use must preserve those conditions.

### P1

- J01-P1-1：Bands 3/4 γ-vibrational and band 4 signature-partner assignments remain interpretation-level, with weak/missing links and multiple DCO δ branches.
- J01-P1-2：CSM/PES residual p-n interaction claim is a model gap/interpretation, not a direct measurement.

### P2/P3

- HS-006 and HS-007 are exact byte duplicates; HS-007 has an explicit row-level audit event and no second source page.

## Extracted Pages

- Nuclei: `165Tm` source-level entry only; no independent nucleus page created in this batch unit.
- Bands: `[541]1/2−`, `[523]7/2−`, `[411]1/2+`, `[404]7/2+`, Bands 1-4 retained inside source; independent pages deferred until cross-source map.
- Concepts: delayed alignment, shape polarization, γ-vibrational bands, band mixing, octupole-enhanced E1.
- Methods: [[doppler-shift-attenuation-method]], [[dco-ratio]], [[angular-momentum-alignment]].

## Non-source Notes and Follow-up

- HS-006 is the canonical copy; HS-007 is duplicate and must be marked `audited-reused` in the execution ledger.
- Later direct sources can test whether the h9/2 deformation/crossing pattern is universal across the rare-earth region or specific to this lineage.
