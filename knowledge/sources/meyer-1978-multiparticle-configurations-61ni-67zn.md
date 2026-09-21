---
type: source
title: "Multiparticle configurations in the odd-neutron nuclei 61Ni and 67Zn populated by decay of 61Cu, 67Cu, and 67Ga"
aliases: ["Meyer 1978 61Ni 67Zn decay spectroscopy", "Multiparticle configurations 61Ni 67Zn"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "Multiparticle configurations in the odd-neutron nuclei 61Ni and 67Zn populated by decay of 61Cu, 67Cu, and 67Ga"
authors: ["R. A. Meyer", "A. L. Prindle", "William A. Myers", "P. K. Hopke", "D. Dieterly", "J. E. Koops"]
journal: "Physical Review C"
year: 1978
volume: 17
issue: 5
pages: "1822-1830"
doi: "10.1103/PhysRevC.17.1822"
citation_key: Meyer_1978
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
language: en
canonical_source: "Meyer, R. A. et al. Multiparticle configurations in the odd-neutron nuclei 61Ni and 67Zn populated by decay of 61Cu, 67Cu, and 67Ga. Phys. Rev. C 17, 1822-1830 (1978)."
library_file: "raw/papers/gpt/high-spin-20260920/纲图/1978_Meyer et al_Multiparticle configurations in the odd-neutron nuclei Ni 61 and Zn 67.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/1978_Meyer et al_Multiparticle configurations in the odd-neutron nuclei Ni 61 and Zn 67.pdf"
raw_sha256: "0e3aeebca53776e3f99ac058563cb40b272425136bd2035ceb778b2aea218b36"
nuclei: ["61Ni", "67Zn", "61Cu", "67Cu", "67Ga"]
models: ["shell-model", "modified-surface-delta-interaction", "adjusted-surface-delta-interaction", "cluster-model"]
observables: ["beta-decay", "gamma-ray-energy", "gamma-ray-intensity", "half-life", "logft", "transition-probability", "mixing-ratio"]
methods: ["decay-spectroscopy", "gamma-ray-spectroscopy", "compton-suppression", "chemical-separation"]
tags: [61Ni, 67Zn, decay-spectroscopy, multiparticle-configuration, shell-model, odd-neutron-nuclei]
---

# Multiparticle configurations in the odd-neutron nuclei 61Ni and 67Zn

## Bibliographic Record

- 作者：R. A. Meyer 等。
- 期刊：*Physical Review C* 17(5), 1822-1830 (1978)。DOI：`10.1103/PhysRevC.17.1822`。
- 原始文件：`raw/papers/gpt/high-spin-20260920/纲图/1978_Meyer et al_Multiparticle configurations in the odd-neutron nuclei Ni 61 and Zn 67.pdf`；SHA-256：`0e3aeebca53776f3f99ac058563cb40b272425136bd2035ceb778b2aea218b36`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: 正文 10 页全部阅读；摘要、引言、`61Cu/67Cu/67Ga` 化学分离与 γ 谱测量、Tables I-IV、`61Ni/67Zn` 衰变纲图、MSDI/ASDI shell-model 计算、cluster-model 比较、Figs.1-7 和总结均已核对。Fig.5/6/7 及关键衰变纲图视觉核对。
- Not covered: 原始探测器事件、完整化学分离日志、引用论文全文和可执行 shell-model 输入。
- Coverage caveats: 论文结合 1970 年代衰变数据和模型；部分自旋宇称、β 分支和低强度 γ 线保留当时的测量/系统学边界。

## Paper Question and Scientific Motivation

- 论文研究 `61Ni` 与 `67Zn` 奇中子核的多粒子组态、能级和 γ 衰变，使用 `61Cu`、`67Cu`、`67Ga` 衰变作为布居来源（摘要；PDF pp.1-2）。
- 作者关注 `g9/2` intruder、三粒子聚簇和 p-f 壳模型在中质量奇质量核中的作用，并以低能级密度、γ 强度、β 分支和转移概率检验 multiparticle configurations（PDF p.1）。

## Method and Design Logic

- `61Cu`、`67Cu` 和 `67Ga` 通过核反应和化学分离制备，使用 LEPS、大体积 Ge(Li) 和 Compton-suppression γ 谱仪测量；`67Ga` 的绝对强度使用离子室与标准样品归一化（PDF pp.2-4）。
- `67Ga` 半衰期由长期交替计数测得；作者报告精确 `T1/2=3.261(1) d`。`67Cu`、`61Cu` 的衰变 γ 线用于建立 `61Ni/67Zn` 能级和分支。
- `61Ni` 的 transition probabilities 用闭壳 `56Ni` 核、`2p3/2,1f5/2,2p1/2` 价空间和 MSDI/ASDI 两种表面 δ 相互作用计算；`67Zn` 同时比较 shell-model 与三中子空穴 cluster/Alaga 模型（PDF pp.7-9）。

## Key Evidence and Reasoning Chain

1. `67Ga` 绝对 γ 强度和 `T1/2=3.261(1) d` 校正了既有衰变数据；Table II/III 给出 91.3、93.3、184.6、208.9、300.2、393.5 keV 等主要线的强度（PDF pp.3-5）。
2. `67Zn` 衰变纲图汇总了低于约 `1.3 MeV` 的能级、β 分支、γ branching 和 `log ft`；814.7 keV 线仅以极低强度 `~2×10−7`/decay 的观察记录出现，若按 β 直接布居会导致很大的 `log ft`，因此作者保留路径解释边界（PDF pp.5-6，Fig.4/7）。
3. `61Cu` 衰变纲图（Fig.5）与先前 `61Ni` 反应谱学结合，确认多个低能级和分支；作者没有观察到此前提出的 1019 keV level，但确认了约 1014 keV level 的 population（PDF pp.6-7）。
4. `61Ni` shell-model 计算比较 MSDI/ASDI 的能级、branching、mixing ratio、lifetimes 和 transition probabilities；两模型对 2.2 MeV 以下能级总体可用，但特定分支和 1132/1186 keV lifetimes 有显著偏差（PDF pp.8-9，Fig.6）。
5. `67Zn` 的 cluster model 可描述部分低能级和衰变性质，但 `B(E2)`、M1 单粒子矩阵元和 β-decay strengths 仍有明显模型依赖（PDF p.9，Fig.7）。

## Summary

论文以 `61Cu/67Cu/67Ga` 衰变谱学建立和修订 `61Ni/67Zn` 能级、γ 强度和 β 分支信息，并用 shell-model、cluster-model 比较多粒子组态。最直接的实验增量是 `67Ga` 半衰期与绝对 γ 强度、`61Ni` 衰变纲图和多个低能级/分支约束；模型层面则显示 MSDI/ASDI 对 `61Ni` 主要低能结构有一定描述力，但特定 branching/lifetime 和 `67Zn` 的 M1/β 强度仍受有效算符与组态空间限制。

## Experimental or Theoretical Setup

- 衰变源：化学分离 `61Cu`、`67Cu`、`67Ga`；`67Ga` 通过 `67Cu(α,2n)` 制备并以高纯样品计数。
- 探测：LEPS、Ge(Li)、大体积 Ge(Li) 和 Compton-suppression spectrometer；`67Ga` 绝对强度结合标准源/离子室。
- 理论：`61Ni` MSDI/ASDI shell model；`67Zn` shell/cluster model；有效中子电荷约 `1.67e` (MSDI) / `1.40e` (ASDI)，`p3/2→f5/2` M1 单粒子矩阵元约 `0.58 μN`。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| M78-1 | `67Ga` 半衰期为 `3.261(1) d`。 | experimental-result | direct | PDF pp.3-4，摘要 | false |
| M78-2 | 论文给出 `67Ga` 主要 γ 线的绝对强度，包括 91.3、93.3、184.6、208.9、300.2、393.5 keV 等。 | experimental-result | direct | PDF pp.3-5，Tables II-III | false |
| M78-3 | `61Cu` 衰变研究确认多个 `61Ni` 能级/γ 分支，未观察此前提出的约 1019 keV level，并观察到约 1014 keV level population。 | experimental-result | direct | PDF pp.6-7，Fig.5 | true |
| M78-4 | MSDI/ASDI 对 `61Ni` 低能级和主要 γ 衰变性质总体可描述，但部分 branching/lifetimes 偏差明显。 | model-result | direct | PDF pp.8-9，Fig.6 | false |
| M78-5 | `67Zn` cluster/shell calculations 可描述部分低能级，但 M1、B(E2) 和 β-strength 仍受模型空间与有效算符影响。 | model-result | direct | PDF p.9，Fig.7 | true |

## Nuclear Structure Information

- `61Ni`：闭 `Z=28` 核附近的奇中子结构，低能级涉及 `2p3/2,1f5/2,2p1/2` 价空间；作者讨论了 multiparticle states 和可能的 intruder influence。
- `67Zn`：奇中子核，低能级谱与 `g9/2` intruder、三中子空穴 cluster 及 p-f 单粒子 M1 转移有关。
- 该来源不建立新的高自旋 band 页；它提供衰变谱学和模型边界背景。

## Authors' Interpretation

- `61Ni` 低能级可视为相对受限 p-f 价空间中的 shell-model states，但 branching/lifetime discrepancies 说明有效相互作用/算符仍有限。
- `67Zn` 的三中子空穴 cluster model 能解释部分能级和衰变，但 β 强度和 B(E2) 的偏差不支持无条件的单一 cluster 描述。

## Model Results

- MSDI/ASDI 计算使用 `56Ni` core 和 `2p3/2,1f5/2,2p1/2` 空间；ASDI 通过拟合 Ni/Cu binding 和 excitation energies 调整矩阵元。
- `61Ni` 两模型对能级到约 2.2 MeV 及若干高自旋状态总体合理；MSDI 与 ASDI 对特定分支各有优劣，1132/1186 keV 的 lifetime 计算明显过长。
- `67Zn` cluster model 使用约 10 个参数重现实验低能级，因此其可解释性和独立预测能力有限。

## Competing Interpretations and Limitations

- 衰变强度和低强度线可能受未观测分支、效率、转换电子或级联喂养影响；早期 NDS 赋值与本工作有差异时需回原始实验。
- `67Zn` 的 cluster、shell-model 和 phonon-core interpretations 并非互斥，但本文没有事件级数据来唯一拆分组态。
- 模型有效电荷、单粒子 M1 矩阵元和有限价空间会改变 transition probabilities；不能把计算 branching 当作直接观测。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-M78-1 | Core reconstruction | 该来源的长期价值是把衰变谱学、绝对强度和早期 shell/cluster 模型放在同一证据链中，而不是只提供一张静态能级图。 | PDF pp.3-9 | self-checking |
| AR-M78-2 | Assumptions and dependencies | 依赖化学分离纯度、效率曲线、β/γ 强度归一化、级联平衡和 NDS/邻核输入。 | PDF pp.2-6 | provisional |
| AR-M78-3 | Transfer conditions | `61Ni/67Zn` 不能直接作为 A≈130 组态证据；可迁移的是衰变强度/模型边界和 source-to-level bookkeeping 方法。 | PDF pp.1,7-9 | self-checking |
| AR-M78-4 | Failure conditions | 若新测量改变低强度线、branching、转换或 level Jπ，旧 shell/cluster 比较需重做；文中部分 discrepancy 已显示该风险。 | PDF pp.5-9 | active-L3 |
| AR-M78-5 | Reverse/falsification test | 用独立 β/γ、conversion、寿命或 transfer-reaction数据复核 disputed levels/branches，比较 MSDI、ASDI 和 cluster predictions。 | PDF pp.6-9 | candidate-L3 |
| AR-M78-6 | Research-question decision | 作为历史衰变谱学、有效算符和多粒子组态的比较来源保留；不单独启动 L4。 | PDF pp.1-9 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 当前高自旋方法页较少覆盖 1970 年代化学分离衰变、绝对 γ 强度和有效算符模型比较。
- Effect of this source: `foundational-background` and `methodological-bridge`。
- Reason: 来源提供低能核素衰变谱学的完整实验—模型链及其有效算符/组态空间边界，但与 A≈130 当前主线没有直接同位素对应。
- Persistence decision: source-only with links to decay-spectroscopy, spin-parity and shell-model context; no new `61Ni/67Zn` entity pages yet。
- Review state: `unreviewed`; source claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[high-spin-phenomena]] | 提供早期高自旋/多粒子组态研究的衰变谱学背景。 |
| methodological-bridge | [[spin-parity-assignment]] | 连接 β/γ branching、log ft、γ 能量和模型比较，但不单独闭合 Jπ。 |
| not-direct-evidence | A≈130 high-spin projects | 质量区和实验类型不同，只用于方法、有效算符与证据边界比较。 |

## Human Review Triage

### P0

- M78-P0-1：低强度 γ 线、`1014/1019 keV` level、`67Zn` 814.7 keV branch 和 Table III 绝对强度若用于论文，需回到表格/纲图并检查后续 NDS 修订。

### P1

- M78-P1-1：MSDI/ASDI/cluster 模型的有效电荷、M1 单粒子矩阵元和参数自由度，不能与直接实验强度混写。

### P2/P3

- DOI、卷期、页码和扫描 PDF 身份已核对；无需在本轮创建核素实体页。

## Extracted Pages

- Nuclei: 暂不创建 `61Ni`、`67Zn`、`61Cu`、`67Cu`、`67Ga` 独立页面。
- Bands: 不创建。
- Concepts: 关联多粒子组态、shell-model effective operator、衰变谱学。
- Methods: 关联 decay-spectroscopy / gamma-ray-spectroscopy 概念。

## Non-source Notes and Follow-up

- 下一步：处理 HS-006/HS-007 Jensen 2001 重复组时，建立一个 canonical source 并对两条路径逐条做 duplicate audit。
