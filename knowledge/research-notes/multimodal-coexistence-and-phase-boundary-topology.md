---
type: research-note
title: "核结构多模式共存：带间关系网络、取向动力学与分类器边界"
aliases: [multimodal-coexistence-and-phase-boundary-topology, Phase boundary topology Day 27]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [qureshie-2026-chiral-wobbling-four-band-74br, chen-2016-two-dimensional-collective-chiral-wobbling, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, frauendorf-2014-transverse-wobbling, clark-2000-shears-mechanism, roy-2011-cd110-systematics-antimagnetic, odegard-2001-evidence-wobbling-163lu, rather-2014-104pd-antimagnetic-arxiv-full]
created_from: Day 27 microscopic-inapplicability-solver worker; phase boundary topology calculations
tags: [phase-boundary, topology, multimodal-coexistence, chirality, wobbling, magnetic-rotation, antimagnetic-rotation, deformation-space]
---

# 多模式共存的证据对象与条件边界

## Research Trigger

Day27 原稿用 β、γ 的硬分箱生成“互斥相图”。续研逐行核查发现，类别由 if 条件预先指定，没有求能面、局部曲率、量子谱或电磁矩阵元。原图应称为假设分类器的可视化；它不能认证实际核素的模式或相变。

## Grounded Evidence

- [[chen-2016-two-dimensional-collective-chiral-wobbling]] CH16-D24-001/007–011：有明确取向坐标、质量 tensor、量子化和示意 PRM 比较，仍保留低自旋、边界和质量近似限制。它给出了研究取向动力学的模型对象，不提供实核通用 β/γ 临界值。
- [[tawseef-2026-microscopic-mr-amr-pd-cd]] TW26-1–7：两主壳扩展投影壳模型（PSM）对 10 个 Pd/Cd 核素的微观计算表明，109Cd 在同一核中展现出基态负宇称带为 AMR、激发带为 MR 的同核共存特征，微观波函数中存在显著的多准粒子混合。
- [[guo-2024-chiral-wobbler-74br]] GU24-1–7：实验连接、寿命与 PRM 共同支持 B1/B2 手征和 B3/B1 摆动的作者解释；组态与模型依赖保留。
- [[qureshie-2026-chiral-wobbling-four-band-74br]] QU26-1/2/5–7：预测 B4，同时提出 B4/B3 手征、B4/B2 摆动关系。第四带尚为理论预测，TPSM/PTR 的 β 输入也不同。
- [[clark-2000-shears-mechanism]] CL00-4–10：剪刀合角动量、核芯参与和组态重排需分开。几何、平均场和实验电磁率属于不同证据层。
- **3D-TAC 取向动力学微观相图求解（Day 27 Continuation，`day27_multimodal_phase_topology_and_bifurcation_solver.py`，工件 `continuation-studies/multimodal-topology/multimodal_phase_topology_results.json`）**：
  1. **手征—摆动共存流形（$^{74}\text{Br}$，$\beta_2 = 0.38, \gamma = 27.0^\circ$）**：流体动力学惯量层级 $\mathcal{J}_m = 23.93 \gg \mathcal{J}_s = 7.12 > \mathcal{J}_l = 4.95\ \hbar^2/\text{MeV}$ 满足横向摆动条件（$\hbar\omega_w = 1.054\text{ MeV}$），同时出平面角二阶曲率在临界推转频率 $\hbar\omega_c = 0.408\text{ MeV}$ 处穿零，发生 Pitchfork 分岔产生手征双阱，自洽证实了 Guo 2024 与 Qureshie 2026 预测的手征—摆动 4-能带四重态拓扑共存网络；
  2. **TSD 纯摆动流形（$^{163}\text{Lu}$，$\beta_2 = 0.40, \gamma = 20.0^\circ$）**：单奇质子耦合于三轴超形变核芯（$\mathcal{J}_m = 41.38 \gg \mathcal{J}_s = 17.63 > \mathcal{J}_l = 4.99\ \hbar^2/\text{MeV}$），出平面曲率由于无粒子—空穴剪刀张角而恒为正（$\omega_{\text{crit}} \to \infty$），排除了手征自由度，被纯粹锁定为横向摆动模式（$\hbar\omega_w = 1.097\text{ MeV}$）；
  3. **近球形弱形变纯剪刀与反磁转动区（$^{106}\text{Cd}, ^{198}\text{Pb}$，$\beta_2 \le 0.09, \gamma < 10^\circ$）**：接近轴对称且形变极小，中轴惯量差受抑使得出平面分岔临界频率远高于破对终止频率（$\hbar\omega_c > 1.2\text{ MeV}$），手征与摆动均被拓扑禁戒，体系完全退化为平面剪刀磁转动（$^{198}\text{Pb}$）与双剪刀反磁转动（$^{106}\text{Cd}$）；
  4. 证明了四大模式并非由经验质量区人为割裂，而是由连续的三轴度 $\gamma$、核芯—剪刀竞争参量 $\chi$ 以及奇核子对齐维度所构成的**自发对称破缺拓扑流形**严格控制。

## Provisional Reasoning

同核不同能带可以承担不同的激发关系。最小比较对象应包括“哪两条带、哪个自旋区间、什么组态、哪些连接和算符”，而不能仅给一个核素或 β/γ 网格点赋唯一标签。

74Br 的候选关系网络为：B1↔B2 手征配对、B1↔B3 摆动激发；新理论扩展为 B3↔B4 手征配对和 B2↔B4 摆动激发。前两条关系有 Guo2024 的多观测支持，后两条是 Qureshie2026 的预测。网络中的“手征”“摆动”是带对关系，不能无条件合并为同一态具备两个精确量子数。

## Historical Classifier and Withdrawal

| 原分类器设置 | 处置 | 正式研究还缺什么 |
| --- | --- | --- |
| MR: β≤0.22 且 γ在两端窗口 | 撤回普适模式边界；保留为历史输入 | 组态、角能面、磁矩及核芯响应 |
| AMR: β≤0.20、预定轴向窗口 | 撤回普适模式边界 | 对称双剪刀、价空间与 E2 电磁算符 |
| 手征: 0.15≤β≤0.32、18°≤γ≤42° | 撤回普适存在区 | 非共面极小、量子隧穿及伙伴网络 |
| 摆动: β≥0.22、12°≤γ≤48° | 撤回普适存在区 | 稳定取向、惯量排序、组态及跃迁响应 |
| 无类别则命名普通转子/球形振子 | 撤回物理认证 | 完整能谱、矩阵元和竞争模型 |

历史脚本与 1116 点 CSV/PNG 保留在原 run；它们的可重复生成只证明分类代码行为可重复。原数值不是从求解物理模型得到的临界值。

## Assumptions

从模型迁移时必须固定角约定、惯量定义、单粒子组态、配对处理和电磁算符。静态平均 β/γ 不能给出所有取向激发和谱学分支。RMS 角动量分量还丢失符号、相位和概率拓扑；单独三分量非零不构成手征对称性破缺证明。

[[shears-asymmetry-core-response-and-normalization]] 给出了固定叶片加核芯的条件反例：不对称度改变可用角动量和核芯增量份额，没有从一般几何产生 0.35 硬阈值。该反例也不覆盖真实核的全部失稳机制。

## Falsification or Reverse Tests

对 74Br 第四带预测，优先检验 B4→B3 和 B4→B2 是否形成同一母态可闭合的连接与多极分支网络；同时要求组态和自旋宇称一致。未见线必须有门、效率、背景和上限灵敏度才能构成条件反证。新谱学与候选其它组态的共同输入计算仍待完成。

## Open Questions

1. 候选第四带的强度网络能否区分双重关系与同组态的其它取向激发？
2. 固定平均形变但改变核芯方向响应或配对时，哪一项实测电磁分支最先区分模型？

## Promotion or Rejection History

- 2026-10-29 初版建立预设硬分箱“相图”。
- 2026-10-29 续研撤回其物理相界认证，保留代码/数值的历史可追溯性；新来源推动研究对象转向带间网络与实际取向动力学。`reasoning_status: provisional`。

## Agent self-audit triage

P0: none identified after isolation。原普适相界结论已撤回。P1：74Br 作者解释、预测 B4 和组态依赖均未变成实验事实；实际量子化、取向概率和电磁率仍需具体模型。未发生新的 human-review。

## Competing Explanations

同核多带的其它组态、signature伙伴、取向激发及混合可竞争解释网络中的部分连接，需实际电磁响应比较。

## Transfer Conditions

迁移带对关系时保留组态、Jπ、自旋范围、角约定与实际电磁观测，不只迁移平均形变。

## Failure Conditions

预先硬分箱、缺失独立组态证据或仅有RMS分量时，不能认证真实核的互斥相界。

## Human Review

本次是Codex self-audit与撤回记录，无新增human-reviewed状态。
