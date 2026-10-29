---
type: research-note
title: "MR、手征与超形变三维多极小 Routhian 分岔和隧穿"
aliases: [MR chirality SD multivalley, magnetic rotation to chirality and superdeformation, 三维多极小隧穿]
created: 2026-10-29
updated: 2026-10-29
category: research-notes
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
promotion_target: ""
created_from: "Day26 高阶前沿研学：MR 向手征与 SD 分岔的三维能量超曲面"
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, frauendorf-meng-1997-tilted-rotation-chirality, clark-2000-shears-mechanism-review, mr-amr-to-chiral-topological-transition-mechanisms, mr-amr-to-superdeformation-bifurcation-phase-diagram]
tags: [magnetic-rotation, nuclear-chirality, superdeformation, routhian, bifurcation, tunneling, WKB, high-spin]
---

# MR、手征与超形变三维多极小 Routhian 分岔和隧穿

## Research Trigger

Day26 任务要求把平面剪刀极小（MR，`phi=0`）、非共面手征极小（`phi!=0`）和高自旋超形变极小（`beta2≈0.6`）放入统一三维能量超曲面，并随转动频率计算势垒、半经典作用量和跃迁分支比。已有笔记分别讨论了 MR→手征几何分岔与 MR→SD 双阱交叉；本页把二者耦合成同一可运行诊断。

## Grounded Evidence

| 主张 | 类型/证据级别 | 定位与边界 |
|---|---|---|
| 平面 TAC/MR 与非共面 TAC 可由出平面角区分，左右手解在实验室恢复后可形成同宇称近简并带 | author-interpretation；indirect；medium | Frauendorf 2001, pp.475–476, 484–485；Frauendorf–Meng 1997, pp.8–13。模型分类不等于某核素静态手征确证。 |
| 高-j 粒子/空穴剪刀闭合给出 MR 的强 M1、弱 E2 机制；核芯转动和组态交叉可改变趋势 | author-interpretation；indirect；medium | Clark 2000, pp.11–18, 30–34；Frauendorf 2001, pp.487–488。 |
| SD 分支具有大形变和大转动惯量，可在高自旋降低 Routhian 斜率并与弱形变分支竞争 | experimental-fact/contextual；medium | 既有笔记 `mr-amr-to-superdeformation-bifurcation-phase-diagram.md` 的 Pb 区证据摘要；具体数值仍需回到对应原始 source locator。 |
| 本扫描中 `a_phi` 变号导致 MR→±phi 手征分岔，SD 旋转增益造成高频率竞争 | model-result；direct（工件）；medium | `outputs/.../workers/mr-chiral-sd-multivalley/mr_chiral_sd_multivalley.py` 与同目录 `scan.csv/json`。 |

## Provisional Reasoning

采用生成坐标 `q=(beta2,theta,phi)`，其中 `theta` 为剪刀张角，`phi` 为出平面角。示例 Routhian 为

`R = V_shape(beta2;omega) + V_shear(theta;omega) + a_phi(beta2,omega) phi^2 + b_phi phi^4 + V_coupling`。

`V_shape` 是在 `beta2≈0.12` 与 `0.60` 间保留亚稳井的平滑双阱；SD 井加入 `-1/2 DeltaJ omega^2` 旋转增益。`a_phi=0.105-0.46 omega^2+1.55(beta2-0.12)^2`，所以低频率平面解稳定，频率提高后 ND 井先出现 `±phi` 镜像极小，SD 井仍被形变项压回 `phi=0`。这把“手征分岔”和“SD 竞争”区分成两个耦合但不同的序参量。

计算在 `omega=0.10–0.72 MeV/hbar` 上扫描。每个频率对代表性井固定 `beta2`、放松角坐标；随后在 31³ 网格上用 minimax 路径求两个极小之间的瓶颈。WKB 代理为 `S/hbar=1.25 sqrt(2 M) B^(3/2)`，`M=18 hbar²/MeV`。低频率仅有 MR 与 SD 分支；约 `0.45–0.50 MeV/hbar` 后 MR 平面极小失稳并由手征镜像取代；SD 分支随频率降低能量并在约 `0.3–0.4 MeV/hbar` 进入竞争区。作用量随手征分岔和 SD 交叉下降，分支比用 `w_i=exp(-2S_i/hbar)` 归一化，仅表示模型内相对权重。

## Assumptions

- `beta2, theta, phi` 是经典生成坐标；未作 good-I 投影、TAC 自洽求解、RPA 或真实集体质量计算。
- 惯量、势能系数和 WKB 质量参数是示例量，未拟合 `106Ag`、`106Cd`、`194Pb` 或任何具体核素。
- SD 形变用 `beta2≈0.60` 代理，未显式引入 `gamma`、配对、八极自由度和多准粒子组态。
- minimax 网格路径和 `B^(3/2)` 作用量是可复现的最低瓶颈近似；不能直接转换为寿命。

## Competing Explanations

- 近简并双带可能来自不同准粒子组态、signature partner、形状软化或带混合，而非左右手隧穿；已有 `mr-amr-to-chiral-topological-transition-mechanisms.md` 对 `106Ag` 的寿命反证必须保留。
- MR→SD 的能量交叉可能是 diabatic/avoided crossing、配对塌缩或核芯极化效应，未必是真正的形状相变。
- `phi` 的 Landau 分岔可被三轴软度和量子涨落抹平，几何极小不保证实验上出现可分辨 partner bands。

## Transfer Conditions

迁移到具体核素前至少需要：已核验组态与宇称、频率依赖惯量、`B(M1)`/`B(E2)` 和带间矩阵元、寿命与 feeding 协方差、连接跃迁，以及同一组态空间的 TAC/PRM 或 CDFT 计算。只有这些量能共同约束 `a_phi`、SD 井偏移、集体质量和路径，模型分支比才有核素解释价值。

## Failure Conditions

- 把扫描临界频率或归一化分支比写成实验事实。
- 把非零 `phi`、近简并或平滑 `S(I)` 单独当作手征充分判据。
- 把 SD 井的示例 `beta2` 与具体 Pb 区 `Q0` 数值混为一谈。
- 在瓶颈低于端点、路径不收敛或局部井消失时仍报告有限隧穿概率；工件中的空值表示分支未识别或已失稳。

## Falsification or Reverse Tests

1. 改变 `M`、网格和路径算法；若作用量不稳定，结论只能保留为势垒拓扑而不能保留 WKB 数值。
2. 将 `DeltaJ`、`a_phi` 和形变井深度分别置零；应分别消除 SD 旋转竞争、手征分岔和双阱共存。
3. 用自洽 TAC/PRM 计算检查 `phi` 曲率是否在相同频率变号；若不一致，优先撤回“临界频率”解释。
4. 对候选双带比较绝对带内/带间 `B(M1), B(E2)`；显著不匹配或不同组态可复现实验时，降低隧穿手征解释权重。
5. 检查高自旋 SD linking transitions、`J^(2)` 和寿命；若没有连接或 SD 井不稳定，应把 MR→SD 解释改为普通带交叉。

## Open Questions

- 由配对、三轴软度和多准粒子组态导出的真实集体质量，是否会使 MR→手征与 MR→SD 的作用量出现相反排序？
- 能否在同一投影框架中同时描述 `106Ag` 的 MR/手征候选和 Pb 区 MR/SD 共存，而不共享不可检验的示例参数？
- 手征双带与 SD 带之间是否存在可测的跨井 M1/E2 linking network，还是两类极小由近似选择规则隔离？
- 八极坐标与 `phi` 的耦合是否会产生手征—反射不对称的四维分岔？

## Human Review

本页为 Codex self-audit 的 `ai-draft`，`review_status: unreviewed`。源页中的历史审核状态不自动继承到本页；模型参数、WKB 质量和分支比尚未由用户逐项审核。

## Promotion or Rejection History

- 2026-10-29：建立本页，整合已有 MR→手征和 MR→SD 笔记，新增三维 Routhian、minimax 瓶颈和相对 WKB 分支扫描。
- 2026-10-29：保留为 `reasoning_status: provisional`；未晋升为正式 model/concept，原因是缺少核素特定自洽计算和实验 linking evidence。
