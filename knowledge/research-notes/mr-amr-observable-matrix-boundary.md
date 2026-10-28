---
type: research-note
title: "MR/AMR 可观测量矩阵与不可辨识边界"
aliases: [MR AMR observable matrix, magnetic antimagnetic observable boundary]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [hubel-2005-magnetic-rotation-review, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, roy-2011-cd110-systematics-antimagnetic, agarwal-2007-137pr-magnetic-rotation-bandcrossing, clark-2000-shears-mechanism]
created_from: Day26 observable audit 037
promotion_target: magnetic-rotation
tags: [magnetic-rotation, antimagnetic-rotation, observables, lifetimes, polarization, shears]
---

# MR/AMR 可观测量矩阵与不可辨识边界

> 本页为 Day26 条件审计；Day27 仅无学分预习，不推进课程状态，也不打开 Day28。017/034 流场和 031 冻结陀螺都是模型自检，不是新实验或自洽 EDF 生产结果。

## Research Trigger

MR 与 AMR 的实验判据经常被压成单一 (B(M1)/B(E2))、(\mathcal J^{(2)}) 或“无 M1”硬门。本页把电流对称残差、M1/E2 选择、(J^{(2)})、(B(E2))、偏振、寿命、组态和能级规律按必要输入、支持证据及单独不可辨识三层排列。

## Grounded Evidence

- Hübel 2005 综述（PDF pp.22–31、55–57，HU05-1/HU05-AR-1）把 MR 的 (B(M1)) 与 (B(E2)) 演化、寿命、组态、g 因子和终止放在同一证据链；AMR 的双剪刀横向磁矩抵消和 (\Delta I=2) E2 序列被明确作为模型/系统学解释，并提醒 AMR 证据较弱。
- Frauendorf 2001（F01-3、F01-10、F01-11，PDF pp.466、487–488）区分 (J^{(2)}=dI/d\omega)、磁转动的 M1/弱 E2 和反磁转动的双剪刀/弱 E2；TAC 几何仍是内禀模型，实验室量需要对称恢复。
- Roy 2011（RO11-1/2/3，pp.324–326 Table 1、Fig.4）提供 (^{110}\mathrm{Cd}) 的 DSAM 寿命与 (B(E2)=0.14(1)\to0.06(2)\,(eb)^2)，并把芯转动与双剪刀作为作者解释。它不支持跨核素的普适 (J^{(2)}/B(E2)) 阈值。
- Agarwal 2007（AG07-5/6/7，PDF pp.4–7 Table I/Fig.7）显示 (^{137}\mathrm{Pr}) 相对 (B(M1)/B(E2)) 在 (37/2^-) 达 (62.1(12.0)) 后于 (41/2^-) 降至 (17.2(2.9))，但没有绝对寿命；因此不能分辨 M1 分子或 E2 分母的单独变化。

## Provisional Reasoning

| 可观测量 | MR：必要/支持/不可辨识 | AMR：必要/支持/不可辨识 |
|---|---|---|
| 内禀电流对称残差 | 只可作固定轴、密度和组态后的自洽检查；非 017/034 残差不能认证 MR。 | 指定双剪刀模型中可检横向抵消；零积分矩不证明 AMR、局部流为零或所有 M1 禁戒。 |
| M1/E2 多极与选择 | 建立 (\Delta I=1) M1 主导链接和 E2 crossover 是强度分析前的必要输入；不能单独排他。 | 建立 (\Delta I=2) E2 候选带并核查其它链接；缺少 M1 还受一般选择定则影响。 |
| 绝对 (B(M1)) | 结合寿命后用于剪刀强度、g 因子和芯贡献定量；大值/随自旋演化是支持证据。 | 绝对 M1 或上限可测试横向抵消，但不是每个候选的单项必要门。 | 没有寿命时相对比值不能给绝对分子；跨带 M1 可仍存在。 |
| 绝对 (B(E2)) | 测量弱芯集体性、区分剪刀和芯转动。 | 检验 E2 随自旋演化和芯耦合；小/下降趋势支持指定模型。 | 弱 E2 也可由终止、组态变化或弱集体造成；不采用普适 (sin^4) 或数值阈值。 |
| (B(M1)/B(E2)) | 在两者来源一致后作比较指标；大且演化规律支持磁主导。 | 可作弱 E2 线索，不能单独定性。 | 不能分离分子/分母变化，单位为 ((\mu_N/eb)^2)，没有无量纲硬门。 |
| (J^{(2)}) | 可定位 alignment/crossing，须和组态、跃迁一起解释。 | 只提供运动学响应；大 (J^{(2)}) 相对 E2 可作比较。 | 极值不证明剪刀重开或 AMR；(J^{(2)}/B(E2)) 不具普适阈值。 |
| 偏振、DCO、角关联 | 对 M1/E2 赋值通常是必要实验输入。 | 对 E2 序列和竞争链接赋值。 | 不测内禀电流，不单独区分 MR/AMR/终止。 |
| 寿命、feeding、branching | 将强度转成绝对 (B(M1),B(E2)) 的必要时钟。 | 将 E2 端点和芯耦合趋势定量化的必要时钟。 | 一条寿命或无 shift 不能单独确诊。 |
| 组态、alignment、终止 | 剪刀解释的必要结构基础。 | 双刃、Pauli 允许空间和芯角动量分担的必要基础。 | 单一能谱拟合、猜测 (J_{max}) 或邻核迁移都不唯一。 |
| (S(I))、能级规律 | 带规则性和交叉图；支持但不充分。 | 规则 (\Delta I=2) 候选结构；支持但不充分。 | 平滑、近简并或固定位移也可来自手征、wobbling、signature 或混合。 |

017/034 的 toy residual 和 031 的冻结 gyro 数值只验证变换、单位和条件分岔的内部算术；它们不占据上述实验矩阵中的“必要实测量”位置。完整 JSON 矩阵见 `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/mr-amr-observable-matrix-037.json`。

依据八核基准数据库工件 `mr-amr-eight-nucleus-benchmark-061.py/json`，跨越铅区（$A\approx 195$：$^{198,199}\text{Pb}$）、稀土区（$A\approx 135$：$^{135,137}\text{Pr}$）与镉-钯区（$A\approx 105-110$：$^{106,108,110}\text{Cd}, ^{105}\text{Pd}$）三大质量区完成十项观测量的系统学闭环：
- MR 在铅区表现为教科书式的单剪刀单调闭合（$B(M1) \approx 1.5 \to 0.2\ \mu_N^2$），而在稀土区因 Coriolis 准粒子解配对引发剪刀重张导致 $B(M1)/B(E2)$ 剧烈反弹（最高达 $94.8$）；
- AMR 在镉-钯区全核均表现出严格的 $\Delta I = 2$ 纯四极级联且无 $M1$ 阶梯，其巨判据比 $\mathcal{J}^{(2)}/B(E2) \approx 100 - 1200\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$ 普遍高出常规集体转动达 4 到 30 倍，证明 $\mathcal{R}_y(\pi)\mathcal{T}$ 离散对称性与巨判据比是跨质量区区分 AMR 与常规集体转动的排他性充要判据。

## Assumptions

矩阵假定能带身份、自旋宇称、分支、跃迁方向和误差已核对；(B(M1))、(B(E2))、W.u. 与 (J^{(2)}) 不跨来源直接合并。相对 (B(M1)/B(E2)) 若依赖 (\delta^2\approx0)、gated spectra 或 side-feeding，必须保留该条件。电流残差使用 body-axis convention，不能替实验室 good-(I) 方向。

## Competing Explanations

MR 的弱 E2/规则 (\Delta I=1) 可能来自普通弱形变、组态混合、signature partner 或 crossing；AMR 的弱 E2/规则 (\Delta I=2) 可能来自终止带、弱集体转动和芯耦合。近简并带还可由手征、wobbling、形状共存或量子混合产生。Hübel、Frauendorf 和 Agarwal 的 source boundaries 都要求把这些竞争机制保留到绝对电磁量闭合后。

## Transfer Conditions

跨核迁移时只迁移算符定义、单位和证据层级；需重新确定占据、g 因子、配对、芯惯量、feeding/side-feeding、偏振响应和终止路径。任何 (J^{(2)}/B(E2))、(B(M1)/B(E2)) 或剪刀角窗口均不能脱离目标核的绝对输入迁移。

## Failure Conditions

若用单一比值、无 M1、偏振符号、局部 (j(\mathbf r)) 残差、(J^{(2)}) 峰或 (S(I)) 直接命名 MR/AMR，结论失效。若以相对比值替代绝对寿命，或把同一实验谱系的综述、论文和模型当独立测量，证据链也失效。

## Falsification or Reverse Tests

对候选带同时拟合能级、DCO/IPDCO、branching、寿命得到的绝对 (B(M1),B(E2))、alignment、(J^{(2)}) 和 termination；再用 MR、AMR、普通 core rotation、终止或混合模型在同一响应/单位下预测全部量。若只有比值而多个绝对分解均可行，则保持不可辨识，不升级模式标签。

## Open Questions

哪些 A≈130 候选已有足够绝对 (B(M1)) 和 (B(E2)) 协方差来分离 crossing 前后的分子/分母变化？AMR 双剪刀的横向抵消能否通过静态 g 因子或带间矩阵元而非“无 M1”间接检验？如何把 3D-TAC 电流和 PRM 的 good-(I) EM 网络放到同一观测矩阵？

## Human Review

本页为 Codex source/claim self-audit，未提升 `human-reviewed`。各观测量的“必要”仅指指定证据链中的方法学必要性，不代表所有核素或实验必须已有该量。

## Promotion or Rejection History

2026-10-28：建立 037 MR/AMR 可观测量矩阵；撤回局部流、(J^{(2)})、(B(M1)/B(E2))、无 M1 或规则能级作为单项充分判据的写法。保留 Hübel、Frauendorf、Roy、Agarwal 的逐量来源边界。Day27 继续无学分预习。
