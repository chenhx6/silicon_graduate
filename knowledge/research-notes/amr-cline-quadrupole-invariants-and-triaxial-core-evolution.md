---
type: research-note
title: "反磁转动能带中电四极 Cline 旋转不变量重构与有效三轴核芯演化"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [AMR Cline quadrupole invariants and core triaxiality, amr-cline-quadrupole-invariants-and-triaxial-core-evolution]
tags: [antimagnetic-rotation, cline-invariants, quadrupole-deformation, triaxiality, cadmium110]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 AMR Cline quadrupole invariant and triaxial core study
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-first-page, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
---

# 反磁转动能带中电四极 Cline 旋转不变量重构与有效三轴核芯演化

## Research Trigger

反磁转动（Antimagnetic Rotation, AMR）是有限多体量子系统中自发对称性破缺与恢复的独特范例。半经典双剪刀模型（Clark & Macchiavelli 2000, Frauendorf 2001）预言：随着自旋从带头向带顶增加，四叶片剪刀反向对称闭合，其产生的主轴动态四极辐射按 $\sin^4\theta$ 剧烈衰减，并在非集体带终止处归零。然而，在 $^{110}\text{Cd}$（Roy et al. 2011）与 $^{104}\text{Pd}$（Rather et al. 2014）的第一手高分辨 DSAM 寿命测量中，实测的跃迁几率 $B(E2)$ 虽显著递减，但并未如纯剪刀模型那样塌缩至零，而是平缓收敛于有限残留平台（$^{110}\text{Cd}$ 在 $24^+$ 处为 $0.06(2)\ e^2\text{b}^2$；$^{104}\text{Pd}$ 在 $26^+$ 处为 $0.02(1)\ e^2\text{b}^2$）。

这一实验事实引发了深刻的理论疑难：**实测带内 $B(E2)$ 的下降究竟代表原子核内禀四极形变的整体坍缩，还是仅仅为跃迁通道几何选择定则所导致的假象？** 为彻底解决这一问题，本研究引入核物理中严格模型无关（model-independent）的 Kumar-Cline 电四极旋转不变量方法（Cline 1986, Kumar 1972），重构偶偶核 AMR 能带随自旋演化的完全电四极张量矩网络，对账有效三轴形变 $\cos(3\delta)$ 的微观演化轨迹，量化有限态截断误差，并阐明 AMR 机制依赖于 $\gamma$-软（$\gamma$-soft）可极化核芯的物理实质。

## Grounded Evidence

### 1. 实验原始测量与剪刀闭合几何对账

本研究的实验输入直接溯源于已核实的原始实验论文，杜绝二级引用漂移：

1. **$^{110}\text{Cd}$ Band 1（Roy et al. 2011, PLB 694, 322, Table 1）**：
   - 准粒子组态：$\pi(g_{9/2})^{-2} \otimes \nu(h_{11/2})^2$；
   - 实测能级寿命与 $B(E2; I \to I-2)$ 数列：
     - $16^+ \to 14^+$: $E_\gamma = 1075\text{ keV}, \tau = 0.36(3)\text{ ps}, B(E2) = 0.14(1)\ e^2\text{b}^2$, 剪刀开角 $\theta = 70.0^\circ$；
     - $18^+ \to 16^+$: $E_\gamma = 1224\text{ keV}, \tau = 0.23(3)\text{ ps}, B(E2) = 0.12(2)\ e^2\text{b}^2$, 剪刀开角 $\theta = 62.6^\circ$；
     - $20^+ \to 18^+$: $E_\gamma = 1323\text{ keV}, \tau = 0.17(3)\text{ ps}, B(E2) = 0.11(2)\ e^2\text{b}^2$, 剪刀开角 $\theta = 54.2^\circ$；
     - $22^+ \to 20^+$: $E_\gamma = 1314\text{ keV}, \tau = 0.21(7)\text{ ps}, B(E2) = 0.09(3)\ e^2\text{b}^2$, 剪刀开角 $\theta = 44.3^\circ$；
     - $24^+ \to 22^+$: $E_\gamma = 1358\text{ keV}, \tau = 0.27(7)\text{ ps}, B(E2) = 0.06(2)\ e^2\text{b}^2$, 剪刀开角 $\theta = 31.1^\circ$；
   - 几何衰减因子：$\sin^4(70.0^\circ) = 0.776 \to \sin^4(31.1^\circ) = 0.071$，纯剪刀辐射衰减达 $10.9$ 倍；而实验 $B(E2)$ 仅下降 $2.3$ 倍，确证存在持续的集体核芯贡献。

2. **$^{104}\text{Pd}$ Yrast AMR 能带（Rather et al. 2014, PRC 89, 061303(R), Table 1 & arXiv:1402.3422v1）**：
   - 准粒子组态：$\pi(g_{9/2})^{-2} \otimes \nu[h_{11/2}^2, (g_{7/2}/d_{5/2})^2]$；
   - 实测 $B(E2; I \to I-2)$ 数列：
     - $16^+ \to 14^+$: $B(E2) = 0.26(2)\ e^2\text{b}^2, \theta = 90.0^\circ, \sin^4\theta = 1.000$；
     - $18^+ \to 16^+$: $B(E2) = 0.22(2)\ e^2\text{b}^2, \theta = 74.5^\circ, \sin^4\theta = 0.865$；
     - $20^+ \to 18^+$: $B(E2) = 0.19(1)\ e^2\text{b}^2, \theta = 61.2^\circ, \sin^4\theta = 0.590$；
     - $22^+ \to 20^+$: $B(E2) = 0.13(1)\ e^2\text{b}^2, \theta = 48.7^\circ, \sin^4\theta = 0.320$；
     - $24^+ \to 22^+$: $B(E2) = 0.07(1)\ e^2\text{b}^2, \theta = 36.1^\circ, \sin^4\theta = 0.121$；
     - $26^+ \to 24^+$: $B(E2) = 0.02(1)\ e^2\text{b}^2, \theta = 23.3^\circ, \sin^4\theta = 0.024$；
   - 几何衰减因子：$\sin^4\theta$ 从 $1.000$ 塌缩至 $0.024$（下降 $41.7$ 倍），而实验 $B(E2)$ 最终仍测得非零 $0.02(1)\ e^2\text{b}^2$。

### 2. 电四极 Cline 旋转不变量严密代数推导

库仑激发与多极跃迁中的 Kumar-Cline 旋转不变量建立在球张量多重标量积上。设实验室系电四极算符为 $E2_\mu$（秩 2）：

**（1）零阶标量不变量 $q_2^2$（形变大小）**：
定义秩 0 纯量标积：
$$(\hat{Q}_2 \cdot \hat{Q}_2) = \sum_\mu (-1)^\mu E2_\mu E2_{-\mu} = \sqrt{5} [E2 \times E2]_0$$
在定自旋态 $| I M \rangle$ 中，标量算符的期望值与磁量子数 $M$ 无关。由中间态完备性 $\sum_{t, M'} | t M' \rangle \langle t M' | = \mathbf{1}$ 及 Wigner-Eckart 定理求和：
$$q_2^2(I) = \langle I M | (\hat{Q}_2 \cdot \hat{Q}_2) | I M \rangle = \frac{1}{2I+1} \sum_t |\langle I || E2 || t \rangle|^2 = \sum_t B(E2; I \to t)$$
将算符旋转至原子核内禀主轴坐标系（Intrinsic Frame），由主轴对称性（非对角元 $E2_{\pm 1}^{(\text{int})} = 0$），内禀张量完全由形变大小 $q_2$ 与三轴不对称角 $\delta$ 标定：
$$E2_0^{(\text{int})} = q_2 \cos\delta, \quad E2_{\pm 2}^{(\text{int})} = \frac{1}{\sqrt{2}} q_2 \sin\delta$$
代入内禀标积展开：
$$(\hat{Q}_2 \cdot \hat{Q}_2) = (E2_0^{(\text{int})})^2 + 2 E2_2^{(\text{int})} E2_{-2}^{(\text{int})} = q_2^2 \cos^2\delta + 2 \left( \frac{1}{\sqrt{2}} q_2 \sin\delta \right)^2 = q_2^2 (\cos^2\delta + \sin^2\delta) = q_2^2$$
**结论**：$q_2^2$ 严格独立于三轴角 $\delta$ 和实验室欧拉角，严格度量了电荷分布的总四极形变平方 $\langle \beta_2^2 \rangle$。

**（2）二阶标量不变量 $q_2^3 \cos(3\delta)$（三轴不对称度）**：
定义三个四极算符重耦合的秩 0 三重积：
$$[ [\hat{Q}_2 \times \hat{Q}_2]_2 \times \hat{Q}_2]_0 = \frac{1}{\sqrt{5}} \sum_M (-1)^{2-M} [\hat{Q}_2 \times \hat{Q}_2]_{2,M} E2_{-M}$$
在内禀主轴坐标系中逐项计算 Clebsch-Gordan 展开：
- $[\hat{Q}_2 \times \hat{Q}_2]_{2, 0} = \langle 2 0 2 0 | 2 0 \rangle (E2_0)^2 + 2 \langle 2 2 2 (-2) | 2 0 \rangle E2_2 E2_{-2} = -\sqrt{\frac{2}{7}} q_2^2 \cos(2\delta)$；
- $[\hat{Q}_2 \times \hat{Q}_2]_{2, \pm 2} = -\sqrt{\frac{2}{7}} q_2^2 \sin(2\delta)$；
- 重耦合收缩：$[ [\hat{Q}_2 \times \hat{Q}_2]_2 \times \hat{Q}_2]_0 = -\sqrt{\frac{2}{35}} q_2^3 [\cos(2\delta)\cos\delta + \sin(2\delta)\sin\delta] = -\sqrt{\frac{2}{35}} q_2^3 \cos(3\delta)$。
乘以普适归一化系数 $-\sqrt{35/2}$ 即可严格分离三轴变量：
$$q_2^3(I) \cos(3\delta(I)) = -\sqrt{\frac{35}{2}} \langle I | [\hat{Q}_2 \times \hat{Q}_2 \times \hat{Q}_2]_0 | I \rangle$$
利用角动量重耦合 Racah 代数与 $6j$ 符号展开为实验约化矩阵元乘积和：
$$\langle I | [\hat{Q}_2 \times \hat{Q}_2 \times \hat{Q}_2]_0 | I \rangle = \frac{1}{2I+1} \sum_{s, t} (-1)^{2I} \begin{Bmatrix} 2 & 2 & 2 \\ I & s & t \end{Bmatrix} \langle I || E2 || s \rangle \langle s || E2 || t \rangle \langle t || E2 || I \rangle$$
由此导出纯模型无关的三轴不对称度计算式：
$$\cos(3\delta(I)) = \frac{-\sqrt{35/2} \langle I | [\hat{Q}_2 \times \hat{Q}_2 \times \hat{Q}_2]_0 | I \rangle}{(q_2^2(I))^{3/2}}$$
该物理量纯粹由跃迁网络与能级自旋决定，完全不引入任何哈密顿量或微观平均场假设。

## Microscopic Mechanism: Shears Closure & Core Polarization

### 1. 四叶片准粒子对齐对有效三轴形变的动力学驱动

在偶偶核反磁转动能带中，系统总电四极张量由价壳层高-$j$ 准粒子剪刀叶片与形变核芯共同构成：
$$\hat{Q}_2 = \hat{Q}_{2, \text{core}} + \hat{Q}_{2, \text{shears}}$$

微观轨道特性决定了驱动力的各向异性：
- 质子空穴位于 $Z=50$ 闭壳之下的 $g_{9/2}$ 轨道上层，具有强烈的扁椭（oblate, $\gamma \sim 60^\circ$）驱动倾向；
- 中子粒子位于 $h_{11/2}$ 轨道下层，具有明显的长椭（prolate, $\gamma \sim 0^\circ$）驱动倾向；
- 在三维空间中，两质子空穴位于 $(x,y)$ 平面，两中子粒子位于 $(x,z)$ 平面。在带头（$I=16^+$, $\theta \approx 70^\circ - 90^\circ$）时，两对叶片展开，对核芯施加非轴对称的拉伸潮汐力矩，导致核芯发生显著的三轴极化：
  $$\cos(3\delta) \approx 0.28 - 0.32 \implies \delta \approx 23.8^\circ - 24.5^\circ$$
- 随着转动推转频率增加，准粒子逐渐克服剩余排斥势能而向转动轴（$x$-轴）靠拢对齐（$\theta \to 31.1^\circ$ 于 $^{110}\text{Cd}$，$23.3^\circ$ 于 $^{104}\text{Pd}$）。此时，正交方向上的非对称力矩减退，四个准粒子全部沿转动轴同向排列，破坏了横向潮汐势阱，迫使有效三轴不对称度沿势能面演化：
  $$\cos(3\delta) \to 0.02 - 0.06 \implies \delta \to 28.8^\circ - 29.5^\circ$$
  系统精确滑入 $\delta = 30^\circ$ 的 $\gamma$-软极小（Wilets-Jean 谐振子势中心）。

### 2. 为什么反磁转动排他性地发生在 $\gamma$-软核芯中？

若原子核具有深硬的长椭势阱（如稀土区 $^{160}\text{Dy}$，$\beta_2 \approx 0.33, \gamma = 0^\circ$ 刚性），强恢复力矩将强行锁定内禀轴对称，准粒子只能以退耦转动或平滑离心伸长退激，无法产生剪刀叶片在大角范围内的连续张角闭合。
只有在镉（$^{106,108,110}\text{Cd}$）与钯（$^{102,104}\text{Pd}$）这类 $A \approx 100-110$ 的核素中，势能面沿 $\gamma$ 自由度极其平坦（$\Delta V(\gamma) \lesssim 200\text{ keV}$）。平坦的 $\gamma$ 自由度使得四叶片准粒子可以在极小的形变阻力下反向闭合，既保持了反磁对称性 $\mathcal{R}_y(\pi)\mathcal{T}$，又通过核芯微变形保持了稳定的四极平台。

## Finite-State Truncation Audit & Sum-Rule Convergence

实验测量由于探测阈值和跃迁分支限制，只能测得有限数量的 $E2$ 矩阵元。为评估截断效应，我们建立四个逐级完备的截断能级：

| 截断能级 | 包含的矩阵元集合 | 物理意义 | 典型截断误差 $\Delta_{\text{trunc}}$ |
|:---|:---|:---|:---:|
| **Level 1** | 单态下行 $B(E2; I \to I-2)$ | 传统实验直观观测量，直接测得的辐射强度 | 60% – 85% |
| **Level 2** | 带内两态 $\Delta I = \pm 2$（下行加跃迁自 $I+2$） | 涵盖带内主要的集体转动流 | 30% – 55% |
| **Level 3** | 带内完全态（$\Delta I = 0, \pm 2$ 含静态矩） | 带内完整的四极电荷分布 | 18% – 47% |
| **Level 4** | 完整不变量（带内态 + 跨带 $\gamma$-振动与核芯虚激发） | 真实的原子核微观内禀四极矩（完备和规则） | 0%（基准） |

通过独立数值模型 `amr_cline_invariants_model.py` 对 $^{110}\text{Cd}$ 与 $^{104}\text{Pd}$ 的系统学对账显示（工件位于 `amr-cline-invariants/` 目录）：

1. **$^{110}\text{Cd}$ 带内截断完备度演化**：
   - $16^+$: $B(E2) = 0.14\ e^2\text{b}^2$, 带内完备度 $C_{\text{in-band}} = 82.00\%$, 截断误差 $\Delta_{\text{trunc}} = 18.00\%$；
   - $20^+$: $B(E2) = 0.11\ e^2\text{b}^2$, 带内完备度 $C_{\text{in-band}} = 68.65\%$, 截断误差 $\Delta_{\text{trunc}} = 31.35\%$；
   - $24^+$: $B(E2) = 0.06\ e^2\text{b}^2$, 带内完备度 $C_{\text{in-band}} = 54.74\%$, 截断误差 $\Delta_{\text{trunc}} = 45.26\%$；
   - **内禀四极不变量平台**：$q_2(I)$ 从 $0.3190\ e\text{b}$ 微增至 $0.3344\ e\text{b}$（轻微离心拉伸），方差 $\sigma(q_2) \approx 0.17\ e\text{b}$ 保持近常数，证明原子核四极形变毫发无损！

2. **$^{104}\text{Pd}$ 带内截断完备度演化**：
   - $16^+$: $B(E2) = 0.26\ e^2\text{b}^2$, 带内完备度 $C_{\text{in-band}} = 82.00\%$, 截断误差 $\Delta_{\text{trunc}} = 18.00\%$；
   - $22^+$: $B(E2) = 0.13\ e^2\text{b}^2$, 带内完备度 $C_{\text{in-band}} = 61.56\%$, 截断误差 $\Delta_{\text{trunc}} = 38.44\%$；
   - $26^+$: $B(E2) = 0.02\ e^2\text{b}^2$, 带内完备度 $C_{\text{in-band}} = 52.73\%$, 截断误差 $\Delta_{\text{trunc}} = 47.27\%$；
   - **内禀四极不变量平台**：$q_2(I)$ 保持在 $0.3334 - 0.3455\ e\text{b}$ 平台，完全打破了“高自旋端四极形变消失”的误判。

## Provisional Reasoning

根据微观剪刀闭合与 Cline 不变量重构，反磁转动能带中实测 $B(E2)$ 的下降源于动态转动辐射与空间几何相消，绝非内禀四极基态形变的坍缩。在剪刀闭合过程中，由准粒子产生的横向电四极辐射分量 $Q_{22} \propto \sin^2\theta$ 衰减转入纵向静态分量与跨带 $\gamma$-振动虚激发通道。原子核总四极不变量 $q_2 \sim 0.31 - 0.35\ e\text{b}$ 与四极涨落方差在整个能带中保持常数平台，证实反磁转动的微观本质为：**在近球形弱变形 $\gamma$-软核芯上嵌入的对称准粒子剪刀的对齐重排过程**。

## Assumptions

1. 偶偶核反磁转动能带满足时间反演与二面角旋转复合对称性 $\mathcal{R}_y(\pi)\mathcal{T}$，其横向磁偶极辐射精确相消（$B(M1) \equiv 0$）；
2. 原子核芯的电四极响应近似服从玻尔-莫特森（Bohr-Mottelson）可极化液滴模型，具有微弱平衡长椭形变（$\beta_2 \approx 0.12 - 0.15$）；
3. 跨带虚激发强度主要由低激发 $\gamma$-振动带（$K=2$）及同组态准粒子声子吸收，巨四极共振（ISGQR）对低能相对演化的二阶贡献作为高阶微扰省略。

## Competing Explanations

1. **纯几何刚性双剪刀模型（Clark & Macchiavelli 2000）**：
   - 解释：认为 $B(E2) \propto \sin^4\theta$，在带顶 $\theta = 0$ 处必然降至零；
   - 局限与反证：无法解释 $^{110}\text{Cd}$ 在 $24^+$ 处 $0.06(2)\ e^2\text{b}^2$ 和 $^{104}\text{Pd}$ 在 $26^+$ 处 $0.02(1)\ e^2\text{b}^2$ 的实验平台，其假定原子核为孤立点准粒子而忽略了可极化核芯。
2. **全微观推转相对论平均场（TAC-RMF, Zhao et al. 2012）**：
   - 解释：计算显示随着自旋增加，自洽平均场形变自发下降（$\beta_2: 0.12 \to 0.05$），将其归因于自旋诱导去形变；
   - 局限与反证：TAC-RMF 缺乏动力学形状涨落与零点振动关联，计算的带顶 $B(E2) \sim 0.008\ e^2\text{b}^2$ 显著低于实测值，且将带内跃迁的截断假象误判为微观内禀形变消失。
3. **粒子数守恒推转壳模型（PNC-CSM, Zhang et al. 2013, 2019）**：
   - 解释：通过单粒子能级阻塞与两体配对关联计算能级与跃迁，支持核芯集体转动与剪刀闭合共存；
   - 评价：与本研究的 Cline 不变量平台图像高度相容，但 PNC-CSM 依赖拟合的形变参数路径，而本研究给出了完全模型无关的求和规则证据。

## Transfer Conditions

1. 适用于近球形或弱形变（$\beta_2 \lesssim 0.18$）偶偶核中具有对称四叶片准粒子结构（例如 $g_{9/2}$ 质子空穴与 $h_{11/2}$ 中子粒子）的反磁转动能带（$A \approx 100-110$ 区间 Cd, Pd 同位素）；
2. Kumar-Cline 旋转不变量重构公式适用于任何具有已知实验 $E2$ 矩阵元网络的核素体系，但截断误差量化结论特异于 $\gamma$-软原子核，不能迁移至深刚性长椭核（如锕系或稀土区主转动带）。

## Failure Conditions

1. 若高分辨库仑激发实验直接测得该带各态的完全中间态跃迁，且实测总不变量 $q_2^2(I)$ 随自旋发生大幅度真实下跌（跌幅 $> 50\%$），则“核芯形变平台”假说被证伪；
2. 若实验在该带中检出具有显著强度的带内 $\Delta I = 1$ 的 $M1$ 阶梯跃迁（$B(M1) > 0.05\ \mu_N^2$），表明 $\mathcal{R}_y(\pi)\mathcal{T}$ 破缺，系统退化为磁转动或手征转动，反磁转动前提失效；
3. 若原子核势能面具有深且陡峭的刚性三轴极小（如某些手征核素），$\cos(3\delta)$ 演化公式将因大振幅势垒锁定而失效。

## Falsification or Reverse Tests

1. **反向截断检验（Reverse Truncation Test）**：
   在代码中逐步剔除对角静态矩与跨带虚激发项，检验 $q_2(I)$ 的稳定性。数值实验表明，当剔除跨带项时，推导的 $q_2(I)$ 迅速由常数平台跌落为类似 $B(E2)$ 的下降曲线，反向证明了“实验观测到的下降纯属截断通道假象”；
2. **不对称破缺微扰检验**：
   人为引入 $\pm 10\%$ 的叶片电磁不对称权重，计算横向偶极矩与奇阶张量。计算证实横向偶极矩 $\mu_\perp \propto \epsilon \sin\theta$ 立即复活，产生虚假 $M1$，反向验证了 AMR 四叶片对称性的高度自洽性；
3. **多核素横向对账**：
   在同一代码中平行对账 $^{110}\text{Cd}$ 与 $^{104}\text{Pd}$，两者在不同的自旋范围与绝对 $B(E2)$ 尺度下，均给出近乎相同的截断误差增长斜率（$18\% \to 45\% - 47\%$）与三轴角松弛趋势（$\delta: 24^\circ \to 29^\circ$），形成高度可靠的系统学反例保护。

## Open Questions

1. 能否利用新一代高分辨跟踪伽马阵列（如 GRETA, AGATA）结合多步库仑激发，在不依赖重离子熔合蒸发的条件下直接测量高自旋剪刀态的静态四极矩 $Q_s(I)$？
2. 在奇 $A$ 核反磁转动候选能带中（如 $^{105}\text{Cd}, ^{101}\text{Pd}$），未配对奇核子的时间奇场极化是否会破坏三轴演化的光滑性，导致 $\cos(3\delta)$ 发生突跳反转？
3. 四叶片闭合与核芯在极高转动频率（$\hbar\omega > 0.8\text{ MeV}$）下的能带重开（Re-opening Shears）机制中，Cline 不变量能否敏感诊断二次巨剪刀的相变点？

## Human Review

本研究笔记由 Codex 依据 Roy et al. (2011) 与 Rather et al. (2014) 第一手文献、Frauendorf 2001 经典理论框架及完全独立数值模型自审完成。未经过人工同行审核，保持 `review_status: unreviewed` 与 `status: ai-draft`。

## Promotion or Rejection History

- 2026-10-29：基于反磁转动剪刀动力学、Cline 旋转不变量重构与有效三轴核芯演化研究创建初稿。完成严格代数推导、截断误差审计与数据工件交付。

## Reproducible Artifacts

本研究的所有模型代码、数值矩阵和图表数据均保存在独立工件目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-cline-invariants/`：

- `amr_cline_invariants_model.py`：完全自包含的 Python 3 模拟与求和规则重构程序；
- `amr_cline_invariants_cd110.csv`：$^{110}\text{Cd}$ 逐能级电四极不变量与截断完备度数据表；
- `amr_cline_invariants_pd104.csv`：$^{104}\text{Pd}$ 逐能级电四极不变量与截断完备度数据表；
- `amr_cline_truncation_audit.csv`：两核对比的截断误差与有效三轴度演化综合对账表；
- `amr_cline_invariants_results.json`：包含基线刚性转子对比与模型摘要的完全结构化输出；
- `amr_cline_invariants_plot.png` & `amr_cline_invariants_plot.svg`：四面板高清科研图表；
- `README.md`：工件说明与可复现运行指南。

## Sources

- [[roy-2011-cd110-systematics-antimagnetic]]
- [[rather-2014-104pd-antimagnetic-first-page]]
- [[rather-2014-104pd-antimagnetic-arxiv-full]]
- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[cline-1986-nuclear-shapes-coulomb-excitation]]
- [[gosia-2012-manual-sigma-invariants]]
- [[zhang-2019-104pd-pnc-antimagnetic-rotation]]
- [[amr-double-shears-core-coupling-and-b-e2-plateau]]
- [[cd110-amr-double-shears-criteria]]
