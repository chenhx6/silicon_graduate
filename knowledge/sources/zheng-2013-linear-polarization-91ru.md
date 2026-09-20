---
type: source
title: "γ-ray linear polarization measurement and (g9/2)−3 neutron alignment in 91Ru"
aliases: ["Zheng 2013 91Ru polarization", "91Ru EXOGAM linear polarization"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "γ-ray linear polarization measurements and (g9/2)−3 neutron alignment in 91Ru"
authors: ["Y. Zheng", "G. de France", "E. Clément", "A. Dijon", "B. Cederwall", "R. Wadsworth", "T. Bäck", "F. Ghazi Moradi", "G. Jaworski", "B. M. Nyakó", "J. Nyberg", "M. Palacz", "H. Al-Azri", "G. de Angelis", "A. Atac", "Ö. Aktaş", "S. Bhattacharyya", "T. Brock", "P. J. Davies", "A. Di Nitto", "Zs. Dombrádi", "A. Gadea", "J. Gál", "P. Joshi", "K. Juhász", "R. Julin", "A. Jungclaus", "G. Kalinka", "J. Kownacki", "G. La Rana", "S. M. Lenzi", "J. Molnár", "R. Moro", "D. R. Napoli", "B. S. Nara Singh", "A. Persson", "F. Recchia", "M. Sandzelius", "J.-N. Scheurer", "G. Sletten", "D. Sohler", "P.-A. Söderström", "M. J. Taylor", "J. Timár", "J. J. Valiente-Dobon", "E. Vardaci"]
journal: "Physical Review C"
year: 2013
volume: 87
issue: 4
pages: "044328"
doi: "10.1103/PhysRevC.87.044328"
language: en
canonical_source: "Zheng, Y. et al. Gamma-ray linear polarization measurement and (g9/2)−3 neutron alignment in 91Ru. Phys. Rev. C 87, 044328 (2013)."
library_file: "raw/papers/gpt/high-spin-20260920/纲图/2013_Zheng et al_γ -ray linear polarization measurements and ( g 9 - 2 ) − 3 neutron alignment.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/2013_Zheng et al_γ -ray linear polarization measurements and ( g 9 - 2 ) − 3 neutron alignment.pdf"
raw_sha256: "0688633ba372e7f3f60b2e9fd69e556d28070b2f5bde62d13d01d1bd9a5483ef"
nuclei: ["91Ru", "91Tc", "90Mo", "88Mo"]
reactions: ["58Ni(36Ar,2p1n)91Ru"]
experiments: ["ganil-exogam-91ru-ar36-111mev"]
models: ["semiempirical-shell-model"]
observables: ["linear-polarization", "polarization-asymmetry", "dco-ratio", "angular-distribution", "gamma-ray-intensity", "alignment"]
methods: ["gamma-gamma-coincidence", "compton-polarimetry", "linear-polarization-asymmetry", "dco-ratio", "angular-distribution"]
tags: [91Ru, 91Tc, EXOGAM, clover-polarimeter, linear-polarization, neutron-alignment, g9-2]
---

# γ-ray linear polarization measurements and (g9/2)−3 neutron alignment in 91Ru

## Bibliographic Record

- 作者：Y. Zheng 等；Physical Review C 87, 044328 (2013)。DOI：`10.1103/PhysRevC.87.044328`。
- 论文电子重印包含原文前置信息和 Physical Review C 正文；正文物理页码为 044328-1 至 044328-10。
- 原始文件：`raw/papers/gpt/high-spin-20260920/纲图/2013_Zheng et al_γ -ray linear polarization measurements and ( g 9 - 2 ) − 3 neutron alignment.pdf`；SHA-256：`0688633ba372e7f3f60b2e9fd69e556d28070b2f5bde62d13d01d1bd9a5483ef`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: 电子重印与正文 11 页全部阅读；反应、EXOGAM/Neutron Wall/DIAMANT 装置、DCO 公式、Compton polarimeter 定义与校准、Tables I-II、Figs.1-8、91Ru 能级图、半经验壳模型和总结均已核对。关键谱图、偏振校准图、`A-R_DCO` 图、能级图和 shell-model energy comparison 视觉核对。
- Not covered: 事件级 γγ 矩阵、EXOGAM response 文件、原始 shell-model 输入代码和引用论文全文。
- Coverage caveats: `91Ru` 基态 `Jπ=(9/2+)` 是作者采用的假设；因此除 `(31/2+)` 外的许多绝对自旋宇称赋值在该基态假设下成立。作者总结也明确保留这一边界。

## Paper Question and Scientific Motivation

- 论文用线偏振、角分布和 DCO 联合确定 `91Ru` 高自旋跃迁的电磁性质、自旋差和宇称，解决早期只靠系统学/DCO 的大不确定性（PDF pp.1-2）。
- 物理问题是 `N=47`、`g9/2` 中子空穴与质子激发之间的竞争：`ν(g9/2)−3` 可产生至 `21/2+` 的中子全顺排结构，而 `π(g9/2)2ν(g9/2)−1` 可延伸至 `25/2+`；非 yrast `(21/2+)`、`(17/2+)` 是否为 seniority-three `ν(g9/2)−3` 相关结构是主要结构问题（PDF pp.1-2, 8-10）。

## Method and Design Logic

- 反应为 `58Ni(36Ar,2p1n)91Ru`，束流 `111 MeV`、约 `10 pnA`；`EXOGAM` 使用 11 个 clover（7 个 `90°`、4 个 `135°`），Neutron Wall 50 个液闪单元，DIAMANT 80 个 CsI，触发要求至少一个中子和一个 γ；共记录约 `4×109` events（PDF p.2）。
- DCO 以 `90°/135°` 非对称 γγ 矩阵构造，定义
  \[
  R_{DCO}=\frac{I(\gamma_1\;135^\circ;\,\gamma_2\;90^\circ)}{I(\gamma_1\;90^\circ;\,\gamma_2\;135^\circ)}.
  \]
  `90°` 与 `135°` 效率行为相同，实验证得 `R_eff=1.79±0.05`，因此无需额外能量效率修正（PDF pp.2-3，式 (1)）。
- EXOGAM clover 作为 Compton polarimeter：在 `90°` clover 中选相邻晶体的水平/垂直散射，定义
  `A=([a(Eγ)N⊥]−N∥)/([a(Eγ)N⊥]+N∥)`，并用无偏振 `152Eu` 源得到 `a(Eγ)=a0+a1Eγ`，其中 `a0=1.05(3)`、`a1=3.9(9)×10−5 keV−1`（PDF pp.4-5，式 (2)-(4)）。
- 物理偏振与实验不对称满足 `A=QP`；点状 polarimeter 的 Klein-Nishina sensitivity 结合有限晶体响应给出 `Q=Qpoint(p0+p1Eγ)`。用已知纯 E2 线的角分布求 `P`，拟合得到 `p0=0.39(2)`、`p1=0.00006(3)`（PDF pp.4-5，式 (5)-(7)，Table I，Fig.5）。

## Key Evidence and Reasoning Chain

1. 已知 stretched quadrupole 的 `R_DCO≈1`、纯 stretched dipole 的 `R_DCO≈0.6`（四极门）用于初步多极性标定；DCO 对混合跃迁和非 stretched 跃迁有多解边界（PDF pp.2-3）。
2. 线偏振不对称的符号区分 stretched electric 与 magnetic character；与 DCO 联合可以区分 E1/M1/E2 和 nonstretched E1 的歧义（PDF pp.3-5，Fig.6）。
3. 在 `91Ru` 中，强正宇称序列 `974, 898, 497, 823, 959, 957 keV` 具有四极 DCO 与正偏振，支持其 stretched E2 性质；328、919 keV 连接线为 nonstretched E1，负宇称结构由偏振和 DCO 共同约束（PDF pp.6-8，Table II，Fig.7）。
4. 新观察到 436、491、1127 keV 等跃迁；491 和 436 keV 级联把第二个 `(17/2+)` 与 `(21/2+)` 状态放在 `2363`、`2799 keV`，但除 `(31/2+)` 外的绝对赋值依赖 `(9/2+)` 基态假设（PDF pp.6-8）。
5. 半经验壳模型把 yrast `(21/2+),(17/2+)` 与 `π(g9/2)2ν(g9/2)−2ν(g9/2)−1` 类多粒子-空穴结构联系起来，并把非 yrast `(21/2+),(17/2+)` 与 `π(g9/2)4ν(g9/2)−3` 的 `Jmax/Jmax−2` seniority-three 结构联系起来；计算能量与观察值接近（PDF pp.8-10，Fig.8）。

## Summary

这项 `91Ru` 熔合蒸发实验用 EXOGAM clover 的 Compton 线偏振、DCO 和角分布联合约束高自旋能级的电磁性质与宇称。论文通过已知 E2 线校准 `Q(Eγ)`，并以 `A=QP` 把探测器不对称转成物理偏振。该联合证据扩展了 `91Ru` 能级图、发现非 yrast `(17/2+)` 和 `(21/2+)` 状态，并提出其与 `g9/2` 中子空穴 seniority-three 结构的对应。由于基态宇称/自旋是假设，论文将绝对赋值保留为相应条件下的结果。

## Experimental or Theoretical Setup

- 反应：`58Ni(36Ar,2p1n)91Ru`，`111 MeV`，平均 `10 pnA`。
- 阵列：EXOGAM 11 clovers；Neutron Wall；DIAMANT；约 `4×109` triggered events。
- 分析：γγ coincidence、DCO、角分布、clover Compton polarization；Shell-model semiempirical energy estimates。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| Z13-1 | EXOGAM `90°` clover 的 polarization calibration 覆盖约 `0.3-1.3 MeV`；`Q(Eγ)` 用已知纯 E2 线和角分布确定。 | experimental-result | direct | PDF pp.4-5，Table I，Fig.5 | false |
| Z13-2 | `A=QP`，`a(Eγ)=1.05(3)+3.9(9)×10−5 Eγ`；拟合 `p0=0.39(2)`、`p1=0.00006(3)`。 | method-calibration | direct | PDF pp.4-5，式 (2)-(7)，Fig.4-5 | false |
| Z13-3 | 328、919 keV 为 nonstretched E1；812、721、253 keV 等负宇称带跃迁具有 stretched M1/E1 约束，具体逐线赋值见 Table II/Fig.7。 | experimental-fact/criterion | direct | PDF pp.6-8，Table II，Fig.6-7 | false |
| Z13-4 | 新的 `(17/2+_2)`、`(21/2+_2)` 状态位于约 `2363`、`2799 keV`，由 491/436 keV 级联建立。 | experimental-result | direct | PDF pp.6-8，Fig.7 | false |
| Z13-5 | 非 yrast `(21/2+_2)`、`(17/2+_2)` 可由 `π(g9/2)4ν(g9/2)−3` seniority-three `Jmax/Jmax−2` 结构解释。 | model-result/author-interpretation | direct | PDF pp.8-10，Fig.8，shell-model section | true |

## Nuclear Structure Information

- `91Ru` 采用 `(9/2+)` 基态假设；正宇称 yrast 序列由 974、898、497、823、959、957 keV 等跃迁连接。
- 新增/确认非 yrast 正宇称结构：`17/2+_2`（2363 keV）和 `21/2+_2`（2799 keV）；两者之间由 436/491 keV 级联约束。
- 负宇称结构含 `13/2−`、`17/2−`、`19/2−`、`21/2−`、`25/2−` 等候选，偏振为 parity 约束关键。

## Authors' Interpretation

- 作者把线偏振和 DCO 的联合测量视为从“系统学/间接证据”走向较强自旋宇称赋值的关键。
- 作者把非 yrast 正宇称状态解释为 `g9/2` 质子/中子空穴的 seniority-three 多粒子结构，但承认基态 `Jπ` 未被直接测量，因而绝对 assignments 仍有条件。

## Model Results

- 半经验 shell model 使用邻核已知构型能量、单粒子能量和两体相互作用估计复杂多粒子-空穴组态。
- 对 yrast `(21/2+_1,17/2+_1)` 计算约 `2399/2024 keV`，观察值约 `2369/1872 keV`；对非 yrast `(21/2+_2,17/2+_2)` 计算约 `2774/2092 keV`，观察值约 `2799/2363 keV`。这些接近支持构型解释，但不提供唯一波函数分解。

## Competing Interpretations and Limitations

- DCO 单独对混合跃迁、非 stretched 跃迁有多解；偏振联合测量减少但不自动消除所有分支歧义。
- `91Ru` 基态自旋宇称未直接测量；因此许多 level assignments 是 conditional/tentative，`31/2+` 仍特别保留不确定性。
- 论文未对左侧负宇称结构全部做线偏振测量；部分 assignments 仍依赖先前工作和局部连接关系。
- Shell-model 构型能量来自半经验邻核输入，属于模型结果而非直接观测。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-Z13-1 | Core reconstruction | 本文的主要增量是“偏振+角分布+DCO”联合证据链，而非单一偏振符号判定。 | PDF pp.2-8 | self-checking |
| AR-Z13-2 | Assumptions and dependencies | 依赖 clover `a(Eγ)`、`Q(Eγ)` 校准、已知 E2 参考线、角分布系数和 gate purity。 | PDF pp.4-5，Table I | self-checking |
| AR-Z13-3 | Transfer conditions | `A=QP` 和 Compton calibration 可迁移为方法框架；`Q(Eγ)`、符号约定、统计和阵列几何必须逐阵列重标定。 | PDF pp.4-5 | provisional |
| AR-Z13-4 | Failure conditions | 弱峰、门控污染、未知基态 `Jπ`、未测偏振的结构和混合跃迁会使绝对 assignments 不唯一。 | PDF pp.6-8，Summary | active-L3 |
| AR-Z13-5 | Reverse/falsification test | 用独立基态自旋/宇称、更多 polarization lines、branching/寿命或邻核 g-factor 数据检验 `g9/2` seniority-three assignments。 | PDF pp.1,8-10 | candidate-L3 |
| AR-Z13-6 | Research-question decision | 该来源适合作为线偏振—DCO—自旋宇称联合判据和 `g9/2` alignment 案例，不启动独立 L4。 | PDF pp.2-8 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有线偏振、Compton `P/A/Q`、DCO 和 `91Ru` 之外的高自旋 assignments 方法页；本来源补充 EXOGAM clover 的实际校准和一个 `g9/2` seniority-three 案例。
- Effect of this source: `supports` and `methodological-bridge`。
- Reason: 直接实验展示了 `A=QP`、`Q(Eγ)`、DCO 与线偏振如何联合约束 parity/multipolarity，并明确记录基态假设造成的 evidence boundary。
- Persistence decision: update [[linear-polarization-asymmetry]], [[compton-polarimetry]] and [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] as a source-level example; no independent 91Ru nucleus page yet。
- Review state: `unreviewed`; source claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[linear-polarization-asymmetry]] | EXOGAM clover `A/Q/P` calibration、符号和 DCO 联合使用案例。 |
| methodological-bridge | [[compton-polarimetry]] | 具体展示 clover 相邻晶体 Compton 散射、`Q(Eγ)` 和 figure of merit。 |
| supports | [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] | 提供物理偏振、实验 asymmetry、响应校准和自旋宇称判据之间的完整实验链。 |

## Human Review Triage

### P0

- Z13-P0-1：`91Ru` 的绝对自旋宇称 assignments 依赖 `(9/2+)` 基态假设；论文级使用时必须保留该条件，不能把 Table II 的括号 assignments 写成无条件事实。

### P1

- Z13-P1-1：`g9/2` seniority-three 构型是半经验 shell-model 解释，需与邻核 g-factor、独立谱学或后续 shell-model 结果区分。

### P2/P3

- EXOGAM 的 `Q(Eγ)` 和 `a(Eγ)` 仅作为该装置校准记录；后续跨阵列比较需要各自 response source。

## Extracted Pages

- Nuclei: 暂不建立独立 `91Ru` 页；source 级记录核素与反应。
- Bands: `91Ru` level scheme 保留在 source，不创建未有稳定名称的 band 页。
- Concepts: 关联 `g9/2` neutron alignment、seniority-three、linear polarization。
- Methods: 更新 [[linear-polarization-asymmetry]]、[[compton-polarimetry]]。

## Non-source Notes and Follow-up

- 下一步：将 EXOGAM `A/Q/P` 校准、`F=1.51×10−5` 和基态假设边界加入方法页；后续处理 HS-005 等方法/纲图来源时比较独立性。
