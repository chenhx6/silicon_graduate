---
type: research-note
title: "壳模型下Gamow-Teller与首禁戒不同Rank弱算符协同衰变机制与淬灭非普适性研究"
aliases: ["GT and first-forbidden common operator note", "doctoral-r1-g34-weak-decay", "Zhi 2013 weak-operator analysis"]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: ["knowledge/sources/doctoral-r1-g34-zhi-2013-prc-shell-model-half-lives.md", "knowledge/sources/continuation-g19-dunlop-2016-cd-halflives.md", "knowledge/sources/continuation-g19-saito-2020-129cd-spectroscopy.md", "knowledge/sources/continuation-g19-cd-in-common-weak-operator-20261107.md", "knowledge/research-notes/doctoral-r1-t04-first-forbidden-operator-audit-20261108.md"]
created_from: project
promotion_target:
tags: ["beta-decay", "gamow-teller", "first-forbidden", "weak-interaction", "quenching-factor", "shape-factor", "shell-model", "r-process-waiting-point", "doctoral-foundations"]
---

# 壳模型下Gamow-Teller与首禁戒不同Rank弱算符协同衰变机制与淬灭非普适性研究

## Research Trigger

在天体物理快速中子俘获过程（$r$-process）等待点核（特别是 $N=50, 82, 126$ 幻数区）以及 $A \approx 130$ 丰中子核（如 $^{128-130}\text{Cd}$、$^{129}\text{In}$）的弱衰变谱学研究中，传统的唯象处理常将衰变率简化为纯 Gamow-Teller（GT）允许跃迁，或粗糙地假设一阶禁戒（FF）跃迁可以按统一的轴矢量淬灭因子 $g_A^{\text{eff}}$ 直接标度。然而，实验测得的核半衰期与馈送分支比不仅由末态能级密度决定，更由初末态波函数在允许与不同 rank 禁戒弱算符下的跃迁振幅相干叠加所决定。

本研究聚焦以下关键理论机制缺口：
1. 给定母态自旋宇称、母子核 $Q_\beta$ 能窗以及大尺度壳模型波函数时，允许 GT 与首禁戒不同 rank 算符（$0^-, 1^-, 2^-$）如何通过相空间积分与能量依赖形状因子 $C(W)$ 协同产生总 $\beta$ 衰变率；
2. 哪些理论输入和淬灭因子是通过母核周围已知实验跃迁进行后验拟合获得的，哪些等待点半衰期是作为理论计算结果；
3. 为什么在弱相互作用物理本质上不能使用一个通用的 $g_A$（或单个经验淬灭因子 $q$）统一度量或重标所有首禁戒算符，以及矢量流与轴矢量流之间的量子相干干涉如何在禁戒形状因子中体现。

## Grounded Evidence

本研究基于对基础理论原件 Zhi et al., Phys. Rev. C 87, 025803 (2013)（同源预印本 arXiv:1301.5225v1，经独立审计确认为 14 物理页，正文与图表延续至第 14 页）的直接核验，结合 Dunlop et al., Phys. Rev. C 93, 062801(R) (2016) 与 Saito et al., Phys. Rev. C 102, 024337 (2020) 的实验谱学证据链，并对照总控与 Terra 独立完成的原件审计结果（[[doctoral-r1-t04-first-forbidden-operator-audit-20261108]]）展开：

### 1. 弱衰变相空间与运动学严格定义

在 Behrens-Bühring 理论框架下（Zhi 2013 Sec. II, Eqs. 1–3），跃迁到特定末态的偏半衰期 $t$ 与相空间因子 $f$ 满足积分关系：
\begin{equation}
f t = K = 6146\,\text{s}
\end{equation}
偏衰变常数 $\lambda_k = \ln 2 / t_k$。总衰变率是所有能量可达末态的偏衰变率之和：$\lambda_{\text{total}} = \sum_k \lambda_k = \ln 2 / T_{1/2}$。末态分支比为 $b_k = \lambda_k / \lambda_{\text{total}}$。
相空间积分的形式定义为：
\begin{equation}
f = \int_1^{W_0} C(W) F(Z, W) (W^2 - 1)^{1/2} W (W_0 - W)^2 dW
\end{equation}
各物理量的严格定义与无量纲化单位如下（按 Zhi 2013 原文约定）：
- $W$ 为发射电子的总相对论能量，以电子静质量 $m_e$ 为自然单位（采用 $c=1$），即 $W = E_e / (m_e c^2) = 1 + T_e / (m_e c^2)$，下限为静止阈值 $W=1$。
- $W_0$ 为特定初末态跃迁的最大可能电子能量（端点能），原文直接基于始末**核态质量差**定义：
  \begin{equation}
  W_0 = \frac{Q}{m_e c^2} = \frac{M_i^{\text{nuc}} - M_f^{\text{nuc}}}{m_e}
  \end{equation}
  若使用中性原子质量差 $Q_\beta^{\text{atom}} = [M_{\text{atom}}(A, Z_i) - M_{\text{atom}}(A, Z_i+1)]c^2$ 换算，在忽略微小原子结合能变化的前提下，端点能满足：
  \begin{equation}
  W_0 \approx 1 + \frac{Q_\beta^{\text{atom}} - E_x}{m_e c^2}
  \end{equation}
  不能漏加电子静能单位 $1$。
- $F(Z, W)$ 为相对论费米函数，用于修正子核有限电荷分布对发射电子波函数近核库仑畸变效应。
- $C(W)$ 为核跃迁形状因子（shape factor），体现轻子波函数展开与核跃迁矩阵元的耦合。
- **与常规比较半衰期定义的重要区别**：在常规实验谱学中，比较半衰期采用纯费米积分 $f_0 = \int_1^{W_0} F(Z, W)(W^2 - 1)^{1/2} W (W_0 - W)^2 dW$，定义 $\log f_0 t$。而在 Zhi 2013 的 $ft = K$ 中，相空间因子 $f$ 显式吸收了形状因子 $C(W)$。为了与常规量进行对比，原文定义了平均形状因子（Eq. 14）：
  \begin{equation}
  \overline{C(W)} = \frac{f}{f_0}
  \end{equation}
  使得常规比较半衰期满足 $f_0 t = K / \overline{C(W)}$。

### 2. 允许 GT 与首禁戒算符的矩阵元与形状因子

对于允许 Gamow-Teller 跃迁（$\Delta J = 0, \pm 1, \Delta \pi = \text{no}$，且排除 $0^+ \to 0^+$），形状因子与电子能量无关（Zhi 2013 Eq. 4）：
\begin{equation}
C(W) = B(GT) = \left(\frac{g_A}{g_V}\right)^2 \frac{|\langle f || \sum_k \bm{\sigma}^k \bm{t}_-^k || i \rangle|^2}{2J_i + 1}
\end{equation}
其中约定 $\bm{t}_- n = p$，核子求和对全部价核子进行，裸耦合常数比取自由核子值 $(g_A/g_V) = -1.2701(25)$。此时相空间积分退化为 $f = B(GT) f_0$。原文定义的 $B(GT)$ 已内含弱耦合比平方 $(g_A/g_V)^2$。

对于首禁戒（First-Forbidden, FF）跃迁（宇称改变 $\Delta \pi = \text{yes}$，$\Delta J = 0, 1, 2$），轻子流展开包含 $p$-波分量或相对论小分量，导致形状因子呈现特征能量依赖（Zhi 2013 Eq. 6）：
\begin{equation}
C(W) = k + ka\, W + \frac{kb}{W} + kc\, W^2
\end{equation}
展开系数 $k, ka, kb, kc$ 由核矩阵元、端点能 $W_0$、原子序数以及无量纲库仑参量 $\xi = \alpha Z / (2R)$ 决定（$R \approx 1.2 A^{1/3}\,\text{fm}$ 为均质带电球半径）：
\begin{eqnarray}
k & = & \left[\zeta_0^2 + \frac{1}{9}w^2\right]^{(0)} + \left[\zeta_1^2 + \frac{1}{9}(x+u)^2 - \frac{4}{9}\mu_1\gamma_1 u(x+u) + \frac{1}{18}W_0^2(2x+u)^2 - \frac{1}{18}\lambda_2(2x-u)^2\right]^{(1)} \nonumber \\
& & + \left[\frac{1}{12}z^2(W_0^2 - \lambda_2)\right]^{(2)} \\
ka & = & \left[-\frac{4}{3}u Y - \frac{1}{9}W_0(4x^2 + 5u^2)\right]^{(1)} - \left[\frac{1}{6}z^2 W_0\right]^{(2)} \\
kb & = & \frac{2}{3}\mu_1\gamma_1 \left\{-\left[\zeta_0 w\right]^{(0)} + \left[\zeta_1(x+u)\right]^{(1)}\right\} \\
kc & = & \frac{1}{18}\left[8u^2 + (2x+u)^2 + \lambda_2(2x-u)^2\right]^{(1)} + \frac{1}{12}\left[z^2(1+\lambda_2)\right]^{(2)}
\end{eqnarray}
其中参量定义为：
\begin{equation}
\begin{aligned}
V & = \xi^\prime v + \xi w^\prime, \quad & \zeta_0 & = V + \frac{1}{3} w W_0 \\
Y & = \xi^\prime y - \xi(u^\prime + x^\prime), \quad & \zeta_1 & = Y + \frac{1}{3}(u - x) W_0
\end{aligned}
\end{equation}
方括号上标 $(0), (1), (2)$ 显式标记算符的张量阶数（rank）。库仑参数取近似 $\mu_1 \approx 1, \lambda_2 \approx 1, \gamma_1 = \sqrt{1 - (\alpha Z)^2}$。

### 3. 首禁戒算符的多极分类与 CVC 约束

经过非相对论约化后，算符与球张量球谐函数 $\bm{C}_{1m} = \sqrt{4\pi/3}\,\bm{Y}_{1m}$ 的耦合关系为（Zhi 2013 Eq. 8）：
- **Rank 0（$0^-$ 跃迁）**：
  - 时样相对论轴矢量算符（$\gamma_5$ 约化）：
    \begin{equation}
    \xi^\prime v = \frac{g_A \sqrt{3}}{M} \frac{\langle f || \sum_k [\bm{\sigma}^k \times \bm{\nabla}^k]^0 \bm{t}_-^k || i \rangle}{\sqrt{2J_i + 1}}
    \end{equation}
  - 轴矢相关量算符：
    \begin{equation}
    w = -g_A \sqrt{3} \frac{\langle f || \sum_k r_k [\bm{C}_1^k \times \bm{\sigma}^k]^0 \bm{t}_-^k || i \rangle}{\sqrt{2J_i + 1}}
    \end{equation}
- **Rank 1（$1^-$ 跃迁）**：
  - 矢量算符（极偶极，不含自旋）：
    \begin{equation}
    x = - \frac{\langle f || \sum_k r_k \bm{C}_1^k \bm{t}_-^k || i \rangle}{\sqrt{2J_i + 1}}
    \end{equation}
  - 时样相对论矢量算符：
    \begin{equation}
    \xi^\prime y = - \frac{1}{M} \frac{\langle f || \sum_k \bm{\nabla}^k \bm{t}_-^k || i \rangle}{\sqrt{2J_i + 1}}
    \end{equation}
    **在矢量流守恒（CVC）及同位旋良好对称性假设下**，约束矢量速度相关算符与空样矢量算符的代数比例关系（Ahrens-Feenberg 展开）：
    \begin{equation}
    \xi^\prime y = E_\gamma x
    \end{equation}
    其中 $E_\gamma = E_{\text{IAS}(i)} - E_f = Q + \Delta E_C - (m_n - m_p)c^2$，$\Delta E_C \approx 1.4136 \bar{Z}/A^{1/3} - 0.9134\,\text{MeV}$ 为同位旋模拟态的库仑位移能。
  - 空样赝矢量轴矢量算符（自旋偶极 rank 1）：
    \begin{equation}
    u = -g_A \sqrt{2} \frac{\langle f || \sum_k r_k [\bm{C}_1^k \times \bm{\sigma}^k]^1 \bm{t}_-^k || i \rangle}{\sqrt{2J_i + 1}}
    \end{equation}
- **Rank 2（$2^-$ 独特一阶禁戒跃迁，Unique First-Forbidden）**：
  - 空样对称张量轴矢量算符（自旋偶极 rank 2）：
    \begin{equation}
    z = 2 g_A \frac{\langle f || \sum_k r_k [\bm{C}_1^k \times \bm{\sigma}^k]^2 \bm{t}_-^k || i \rangle}{\sqrt{2J_i + 1}}
    \end{equation}

## Provisional Reasoning

### 1. 允许与首禁戒算符共同产生衰变率的微观机制

总衰变常数分解为允许与禁戒之和：$\lambda_{\text{total}} = \lambda_{GT} + \lambda_{FF}$。
在核结构波函数确定时，允许 GT 与首禁戒跃迁呈现出完全不同的相空间权重与核跃迁能谱分布：
1. **能级位置与相空间竞争**：在丰中子核中，由于自旋-轨道劈裂与主壳间隙，允许 GT 跃迁往往连接到子核较高激发态（例如在 $^{130}\text{Cd}$ 中 $\nu 0g_{7/2} \to \pi 0g_{9/2}$ 跃迁集中在 $E_x \sim 2-5\,\text{MeV}$）。这导致其有效端点能 $W_0$ 减小。相空间对允许跃迁的经验定标行为近似为 $f \sim Q_\beta^5$。
2. **禁戒跃迁的相空间补偿**：首禁戒算符连接相反宇称轨道（例如 $\Delta l = 1$，$\nu 0h_{11/2} \to \pi 0g_{9/2}$ 或 $\nu 1d_{3/2} \to \pi 1p_{1/2}$）。这些末态往往是子核的低激发态乃至基态（如 $^{129}\text{In}$ 的 $9/2^+, 11/2^+, 13/2^+$）。虽然首禁戒内禀矩阵元带有无量纲压低因子 $k_e R \approx R/\lambdabar_c \sim 10^{-2}$，但较低的激发能赋予其显著更大的端点能 $W_0$。在 $Q_\beta$ 较小的核中，相空间因子的放大能够部分或完全抵消矩阵元的压低。
3. **Rank 2 独特禁戒的能量依赖**：对于 rank 2 独特禁戒跃迁，当 $\lambda_2 \approx 1$ 时，其形状因子化简为：
   \begin{equation}
   C(W) \approx \frac{1}{12} z^2 \left[(W_0 - W)^2 + (W^2 - 1)\right] = \frac{1}{12} z^2 (q_\nu^2 + p_e^2)
   \end{equation}
   动量平方因子进入相空间积分后，使得其衰变率随有效能窗的依赖强度攀升至 $\sim Q_\beta^7$。

### 2. 拟合输入与留出预测的严格划分

在 Zhi et al. 2013 的理论架构中，存在明确的经验拟合参数与纯理论留出预测的界限：
- **后验拟合参数（Fitted Inputs）**：
  1. *首禁戒淬灭因子*：作者基于铅区与铟区（包括 $^{131m}\text{In}, ^{129m}\text{In}, ^{205,206}\text{Hg}, ^{206,207}\text{Tl}, ^{205}\text{Au}$）已知的 20 项纯一阶禁戒衰变跃迁行（Table I），执行最小二乘拟合确定了 5 个淬灭参数：
     \begin{equation}
     q(\xi^\prime v) = 1.266, \quad q(w) = q(w^\prime) = 0.66, \quad q(x) = q(x^\prime) = 0.51, \quad q(u) = q(u^\prime) = 0.38, \quad q(z) = 0.42
     \end{equation}
     原文未披露详细的目标函数权重、协方差矩阵或数据挑选判据；$^{131m}\text{In}(1/2^-)$ 与 $^{129m}\text{In}(1/2^-)$ 是首禁戒拟合集的一部分，不能当作盲验证。
  2. *GT 淬灭因子 $q_{GT}$*：在固定上述首禁戒淬灭后，利用当时已知的 $^{130}\text{Cd}$ 实验半衰期（Kratz 2000 报告的 $162(7)\,\text{ms}$）作为输入，反调得到 $q_{GT} = 0.66$（计算值 $164.29\,\text{ms}$，首禁戒占 $13\%$）。$^{130}\text{Cd}$ 属于 GT 校准样本，绝非留出预测。
- **留出预测（Holdout Predictions）**：
  1. $N=50$ 等待点核链：$^{82}\text{Ge}, ^{81}\text{Ga}, ^{80}\text{Zn}, ^{79}\text{Cu}, ^{78}\text{Ni}, ^{77}\text{Co}, ^{76}\text{Fe}, ^{75}\text{Mn}, ^{74}\text{Cr}$ 的总半衰期 $T_{1/2}$（Table II）及中子发射几率 $P_n$（Fig. 7）。
  2. $N=82$ 等待点核链：$^{131}\text{In}(9/2^+), ^{129}\text{Ag}, ^{128}\text{Pd}, ^{127}\text{Rh}, ^{126}\text{Ru}, ^{125}\text{Tc}, ^{124}\text{Mo}$ 的总半衰期 $T_{1/2}$（Table III）及 $P_n$。
  3. $N=126$ 等待点核链：$^{199}\text{Ta}, ^{198}\text{Hf}, ^{197}\text{Lu}, ^{196}\text{Yb}, ^{195}\text{Tm}, ^{194}\text{Er}, ^{193}\text{Ho}, ^{192}\text{Dy}$ 的理论寿命预言（Table IV）。
  4. 首禁戒对各同中子素链总寿命的百分比贡献趋势（Figs. 5, 10, 15）。

**外部谱学标定演进（Dunlop 2016 关联）**：
Zhi 2013 原文所使用的标定输入是 Kratz 2000 的 $^{130}\text{Cd}$ 旧实验值 $162(7)\,\text{ms}$。后续 TRIUMF-GRIFFIN（Dunlop 2016 PRC 93, 062801(R)，详见 [[continuation-g19-dunlop-2016-cd-halflives]]）与 EURICA（Lorusso 2015）精确测定 $^{130}\text{Cd}$ 真实半衰期为 $126(4)\,\text{ms}$。为了匹配这一显著更短的新寿命，后续大尺度壳模型研究将 $q_{GT}$ 重新标定为 $0.75$。这一演进明确表明，等待点计算中的 $q_{GT}$ 属于与特定参考核素寿命联立的唯象调整参数，不可当作第一性物理常数。

### 3. 为什么不能用一个通用 $g_A$ 重标所有首禁戒算符

在物理微观机制上，将全部一阶禁戒跃迁矩阵元统一乘以单一的 $(g_A^{\text{eff}})^2$ 或单一淬灭因子 $q_{FF}^2$ 在理论上是不成立的：

1. **矢量流与轴矢量流的对称性与有效算符重整化差异**：
   - 弱相互作用包含矢量流 $V_\mu$ 与轴矢量流 $A_\mu$。极矢量算符 $x$ 属于矢量流。根据 CVC 假设，在同位旋完好对称极限下，弱矢量荷不发生微观淬灭（即裸耦合 $g_V = 1$）。但在截断的价空间壳模型中，有效矢量算符仍会受到有限基底截断、组态相互作用和相对论修正的重整化，表现出唯象拟合值 $q(x) = 0.51$。这说明不能断言其“完全源于芯极化”，但更不能将其粗暴地按轴矢量 $g_A$ 的淬灭规则处理。
   - 轴矢量算符（$w, u, z, \xi^\prime v$）属于轴矢量流，在介质中天然受到核子核内激发及关联的重整化。
2. **时样轴矢量荷的表观增强与软介子流解释**：
   - Rank 0 的时样相对论轴矢算符 $\xi^\prime v \sim \frac{\bm{\sigma} \cdot \bm{\nabla}}{M}$ 对应单粒子狄拉克方程中的 $\gamma_5$ 项。
   - 拟合所得的 $q(\xi^\prime v) = 1.266 > 1.0$ 展现出明显的表观增强。Warburton 等人的微观分析将其解释为软 $\pi$ 介子交换流（MEC）的相长干涉。但在本壳模型框架中，该数值依然属于有限模型空间下的唯象拟合参数，未在本文中由微观 MEC 自洽推导，不能声称“已唯一由 MEC 解释”。不过，这一表观增强与空样算符的普遍压低（$q < 1$）形成了明确的物理反差，直接排除了采用统一 $g_A < 1$ 缩放所有算符的做法。
3. **不同角动量 Rank 的自旋-空间多极各向异性**：
   - 空样算符 $w$（rank 0）、$u$（rank 1）和 $z$（rank 2）具有不同的自旋-轨道张量结构 $[\bm{C}_1 \times \bm{\sigma}]^J$。
   - 自旋偶极（SD）在 $J^\pi = 0^-, 1^-, 2^-$ 各多极通道具有不同的激发能分布与碎裂结构，导致有效粒子-空穴相互作用在不同 $J$ 激发通道表现出不同的屏蔽程度，唯象拟合直接反映了这一通道分化：$q(w) = 0.66 \neq q(u) = 0.38 \neq q(z) = 0.42$。
4. **Rank 1 中矢量与轴矢量的相干量子干涉**：
   - 在非独特首禁戒跃迁（$\Delta J = 1^-$）中，矢量算符 $x$ 与轴矢量算符 $u$ 同时贡献于同一末态，并在形状因子展开系数中构成交叉干涉项，如 $(x+u)^2$、$(2x+u)^2$、$(2x-u)^2$、$-4\mu_1\gamma_1 u(x+u)$ 以及 $u Y$。
   - 拟合显示矢量与轴矢算符的有效因子相差明显（$q(x)=0.51$ vs $q(u)=0.38$）。若强行采用单一因子重标，将人为扭曲 $x$ 与 $u$ 之间的相对振幅比，破坏真实的干涉相消或相长，导致不仅总衰变常数发生系统偏差，甚至会改变电子能谱形状因子 $C(W)$ 的斜率与曲率。

### 4. 两个具体核素案例的深入核查

#### 案例一：$^{130}\text{Cd}$（$N=82$ 等待点核，基态 $0^+$）
- **衰变机制**：母态具有满中子壳 $N=82$ 与 2 个质子空穴（$Z=48$）。衰变主要由允许 GT 跃迁 $\nu 0g_{7/2} \to \pi 0g_{9/2}$ 驱动，连接子核 $^{130}\text{In}$ 的低激发 $1^+$ 态。
- **计算与实验数值**：Zhi 2013 计算得到总半衰期 $T_{1/2} = 164.29\,\text{ms}$，首禁戒贡献约为 $13\%$。FF 跃迁主要由 $\nu 0h_{11/2} \to \pi 0g_{9/2}$（rank 1 算符）连接负宇称态（如 $1^-$）。
- **定位与边界**：该计算采用 $q_{GT} = 0.66$ 系对当时 $162(7)\,\text{ms}$ 数据的反调，属于拟合输入；后续更新属于 Dunlop 2016 来源，不可混淆。

#### 案例二：$^{78}\text{Ni}$（$N=50$ 双幻等待点核，基态 $0^+$）
- **衰变机制**：在简单独立粒子模型（IPM）中，质子 $0f_{7/2}$ 轨道完全填满（$Z=28$）。中子 $0g_{9/2} \to \pi 0f_{7/2}$ 的首禁戒跃迁遭遇严格的泡利阻挡（Pauli blocking）；同时，中子 $0f_{5/2} \to \pi 0f_{7/2}$ 的 GT 跃迁同样被完全阻挡。传统平均场或 QRPA 模型通常预测 $^{78}\text{Ni}$ 具有极长的半衰期（数秒之久）。
- **计算与实验数值**：Hosmer et al. 2005 测得 $^{78}\text{Ni}$ 半衰期为 $0.11^{+0.10}_{-0.06}\,\text{s}$（$110\,\text{ms}$）。Zhi et al. 2013 壳模型成功计算出 $T_{1/2} = 0.15\,\text{s}$（$150\,\text{ms}$），与实验高度吻合（Table II）。
- **微观破阻挡机制**：在包含跨壳激发的大尺度壳模型中，$Z=28$ 质子壳和 $N=50$ 中子壳由于强对关联与粒子-空穴剩余相互作用发生组态混合，部分解除了质子 $0f_{7/2}$ 的占据饱和度（产生质子空穴并占据 $1p_{3/2}, 0f_{5/2}$），从而打开了低激发的 GT 与首禁戒跃迁通道。

### 5. Table I 内部自洽性疑点记录（对照 T04 独立审计）

根据总控与 Terra 独立完成的原件审计（见 [[doctoral-r1-t04-first-forbidden-operator-audit-20261108]]），在 Zhi 2013 Table I 中发现两行理论列数值存在内部对应疑点：
- Table I 中给出的换算关系为 $\log_{10}(f_0 t / \text{s}) = \log_{10}[6146 (\lambda_e / \sqrt{\overline{C}})^2]$（$\lambda_e \approx 386.159\,\text{fm}$）。
- 对于 $^{205}\text{Hg} \to {^{205}\text{Tl}}(3/2^+_1)$：原表理论列 $\sqrt{\overline{C}} = 18.9\,\text{fm}$ 反算出的 $\log f_0 t$ 约为 $6.41$，但原表所列理论 $\log f_0 t$ 为 $7.26$；
- 对于 $^{205}\text{Hg} \to {^{205}\text{Tl}}(3/2^+_2)$：原表理论列 $\sqrt{\overline{C}} = 10.3\,\text{fm}$ 反算出的 $\log f_0 t$ 约为 $6.94$，但原表所列理论 $\log f_0 t$ 为 $6.32$；
- 二者理论 $\log f_0 t$ 与 $\sqrt{\overline{C}}$ 未满足该文声明的换算关系。该疑点在 PDF 和 `rp.tex` 源码中均完全一致。本笔记在此如实记录该审计发现，不作擅自篡改，亦不宣称独立发现。

### 6. 关于 Ikeda 求和规则与能窗强度的边界辨析

必须强调理论边界：**不得把能窗内的实测强度当作 Ikeda 全和**。
Ikeda 求和规则指出：
\begin{equation}
S_{\beta^-} - S_{\beta^+} = \sum_f B(GT, i \to f)_{\beta^-} - \sum_{f'} B(GT, i \to f')_{\beta^+} = 3(N - Z)
\end{equation}
这里的裸求和强度不含 $(g_A/g_V)^2$；若采用本文含耦合常数的 $B(GT)$ 定义，必须同步处理该因子。有限价空间与有效算符不自动满足相同裸和。

该求和规则是在完备希尔伯特空间中通过流代数对易子 $[I_+, I_-] = 2 I_3$ 推导出的与模型无关的严格算符恒等式。然而，在实际 $\beta$ 衰变中，受限于核质量差 $Q_\beta$，实验只能探测到激发能 $E_x < Q_\beta$ 能窗之内的跃迁强度。能窗外可有未测的GT强度及巨共振贡献，其相对份额应逐核计算，不能预设统一百分比。在价空间壳模型或实验衰变谱学中，不能把能窗内的有限累积强度亏损当成全空间算符总和的内在淬灭。

### 7. Brainstorming Candidates

#### 候选设想一：利用连续 $\beta$ 能谱形状因子 $C(W)$ 的微分测量解缠 $A \approx 130$ 丰中子核首禁戒多极 Rank 分解（Shape-Factor Sensitive Disambiguation of FF Multipole Decomposition in $A \approx 130$ Waiting-Point Betas）
- **Idea（核心构想）**：
  在奇 $A$ 镉同位素（如 $^{129}\text{Cd} \to {^{129}\text{In}}$）的弱衰变中，直接测量通向各独立低激发态符合的连续电子能谱，通过微分展开拟合形状因子 $C(W) = k + ka W + kb/W + kc W^2$ 的斜率与曲率，从而在实验上区分 rank 1 非独特禁戒与 rank 2 独特禁戒的相对贡献，减少对总半衰期积分值的唯象依赖。
- **Assumption（物理假设）**：
  高纯锗探测器配合薄窗硅探测器望远镜具备足够的能量分辨，能通过模拟反卷积电子在探测器中的反散射与本底；子核低能激发态（如 $995\,\text{keV}$ 与 $1354\,\text{keV}$）的 $\gamma$ 门能够有效隔离单一初末态跃迁。
- **Prediction（可检验预测）**：
  若 rank 1 跃迁由 $x$ 与 $u$ 的相干干涉主导且 $q(x) \neq q(u)$，则其 $ka/k$ 系数将呈现特定的线性斜率特征；若 rank 2 轴矢量张量 $z$ 占比较高，则能谱在两端将展现向上二次抛物线上翘曲率。
- **Evidence（现有支撑证据）**：
  Saito 2020 PRC Table II 报告了 $^{129}\text{Cd}$ 通向 $^{129}\text{In}$ 的 $9/2^+$ 基态、$11/2^+$（$995\,\text{keV}$）和 $13/2^+$（$1354\,\text{keV}$）的禁戒馈送，但仅给出了总分支比和表观 $\log ft$，未获得微分能谱形状。
- **Competing Explanations（最强竞争解释）**：
  母态异能态混合污染；未观测到的高能弱 $\gamma$ 馈送导致的级联虚假污染；探测器反散射几何导致的低能电子堆积伪造斜率。
- **Discriminating Observables & Failure/Pivot Criteria（可区分观测与失败/转向条件）**：
  以 $995\,\text{keV}$ 纯门符合下的电子连续谱为可区分观测量。若实测 $C(W)$ 在统计误差内与常数无偏（$ka \approx 0, kc \approx 0$），则表明 rank 1 干涉与 rank 2 强度在当前通道恰好抵消或 rank 2 占比极低，此时应转向有效单粒子组态波函数的理论重构。

#### 候选设想二：利用 $^{129}\text{Cd}$ 双母态衰变率联立检验有效弱耦合常数（Independent Weak Coupling Evaluation via Paired Decay of $^{129}\text{Cd}$ Isomers）
- **Idea（核心构想）**：
  利用 $^{129}\text{Cd}$ 中两个长寿命母态（自旋宇称指认为 $11/2^-$ 与 $3/2^+$，存在基态能序争议），建立联立衰变率关系式：一个母态主要由单跃迁强 GT 加上低能 FF 构成，另一个由高度碎裂的 GT 加上负宇称 FF 构成。在 CVC 约束矢量算符的前线下，检验能否用自洽的 $q_{GT}$ 与轴矢淬灭因子同时描述两者，从而减少依赖单一 $^{130}\text{Cd}$ 寿命标定的局限。
- **Assumption（物理假设）**：
  壳模型相互作用（如 NA-14 或 Cuenca 2007）能以相近精度描述同一核素中两个母态的单粒子组态结构；两母态的能级间隔与各自的 $Q_\beta$ 具有可信输入（本任务未获得 2026 最新逐态输入）。
- **Prediction（可检验预测）**：
  两母态相近的总半衰期并非来自相同的内禀矩阵元，而是相空间与碎裂度的偶然补偿；自洽提取将要求允许与禁戒算符采用不同的有效淬灭幅度。
- **Evidence（现有支撑证据）**：
  Dunlop 2016 测得的双母态半衰期（$147(3)\,\text{ms}$ 与 $157(8)\,\text{ms}$）；Saito 2020 测得的逐能级馈送分布；Manea 2020 PRL 报告的能级差。
- **Competing Explanations（最强竞争解释）**：
  母态能序争议（$11/2^-$ 与 $3/2^+$ 谁为基态尚未完全排除）；缓发中子发射几率 $P_n$ 在两母态之间存在不对称发射（本任务未获得独立逐态输入）。
- **Discriminating Observables & Failure/Pivot Criteria（可区分观测与失败/转向条件）**：
  获取纯净激光电离分离下的独立 $P_n$ 与高精度质量差。若联立方程在物理可信区间内无解，或两母态要求的等效淬灭因子偏差过大（$>30\%$），则判定壳模型有限价空间（如缺少质子完整主壳）存在波函数系统偏差，方案转向扩展组态空间或微观第一性原理计算。

## Assumptions

1. 弱相互作用有效哈密顿量采用 $V-A$ 点接触流-流相互作用假设，轻子流按狄拉克库仑偏波函数进行多极展开（Behrens-Bühring 冲激近似）。
2. 核电荷分布近似为半径 $R = 1.2 A^{1/3}\,\text{fm}$ 的均匀带电球体，用于计算有限大小库仑修正因子 $I(1,1,1,1,r)$ 与 $\xi = \alpha Z / (2R)$。
3. 矢量流守恒（CVC）与同位旋对称性在球形幻数核及其邻近同位素中近似成立，约束矢量速度相关算符 $\xi^\prime y = E_\gamma x$。
4. 唯象淬灭因子假定跨所研究的球形等待点核区保持近似常数，由铅区与铟区 20 个实验跃迁行拟合标定。
5. 大尺度壳模型对角化采用 Lanczos 算法（截断至 100 步迭代），其低能态收敛对应物理态，高能非物理态对积分相空间的影响在有限不确定度内平滑。

## Competing Explanations

1. **$Q_\beta$ 能窗与质量评估不确定性**：
   - 半衰期对端点能具有极高敏感度（相空间按 $Q^5-Q^7$ 增长）。若质量评估（如 AME 不同版本或最新 Penning 阱测量）存在几十至上百 keV 偏差，将直接导致理论寿命产生显著浮动。
2. **同核异能态倒转与母态混合污染**：
   - 在奇 $A$ 核（如 $^{129}\text{Cd}$ 的 $11/2^-$ 与 $3/2^+$，存在基态能序争议）中，母态提取若未完全纯化，衰变曲线解缠误差会导致馈送分支比 $I_\beta$ 出现交叉污染，影响提取的 $\log ft$。
3. **Pandemonium 效应导致的馈送低估**：
   - HPGe 探测器对高能 $\gamma$ 射线效率较低，容易漏测来自高能区微弱级联，从而高估低能馈送强度并漏计高能 GT 强度。总吸收 $\gamma$ 谱学（TAGS）是检验该偏差的重要手段。
4. **模型空间截断与有效相互作用单极漂移**：
   - 壳模型仅包含有限价空间（如 $N=82$ 计算采用 $^{88}\text{Sr}$ 芯），被省略的组态被吸收到有效两体矩阵元中。QRPA 与密度泛函（如 DF3+CQRPA）给出的不同寿命常反映了平均场对称性破缺与多粒子关联的差异。

## Transfer Conditions

1. **向中重变形核区迁移**：
   - 本研究所验证的淬灭方案基于球形幻数等待点核。向大变形区迁移时，初末态必须在形变内禀坐标系下按角动量投影进行展开。此时，$K$-禁戒度与三轴非对称性将改变多极矩阵元的几何选择定则。
2. **向双 $\beta$ 衰变（$0\nu\beta\beta$）迁移**：
   - 普通 $\beta$ 衰变的动量转移极低（$q \sim \text{few MeV}/c$），而无中微子双 $\beta$ 衰变动量转移高达 $q \sim 100\,\text{MeV}/c$。在如此高的动量尺度下，核短程关联与两体交换流产生完全不同的动量依赖截断。因此，**绝对不可将本研究中单 $\beta$ 衰变拟合得到的淬灭因子直接套用于 $0\nu\beta\beta$ 核矩阵元**。

## Failure Conditions

1. **实验能谱形状因子出现反常曲率**：
   - 若利用高精度 $\beta$ 能谱探测器测得的非独特首禁戒跃迁连续能谱形状因子 $C(W)$ 无法拟合为四项形式，或系数比值与 rank 1 矢量/轴矢干涉预言产生统计显著的符号相反，则当前的冲激近似展开及其多极淬灭方案宣告失效。
2. **Ab initio 包含手征两体弱流后淬灭参数失效**：
   - 若基于手征有效场论的微观第一性原理多体计算在自洽包含两体弱流后，初末态跃迁率显示出强烈的态依赖与轨道依赖（无法用跨核素恒定的 rank 因子概括），则表明常数淬灭仅为有限价空间下的一种唯象吸收。

## Falsification or Reverse Tests

### 逆向测试一：通用淬灭因子强行套用测试（Universal Quenching Falsification）
- **操作方案**：在 Zhi 2013 Table I 的 20 个已知一阶禁戒衰变跃迁行中，强行令所有算符采用统一的淬灭因子：$q(\xi^\prime v) = q(w) = q(x) = q(u) = q(z) = q_{GT} = 0.70$。
- **检验判据**：重新计算 20 项跃迁的 $\log f_0 t$ 与平均形状因子平方根 $(\overline{C(W)})^{1/2}$，对比实验测量。
- **证伪表现**：对于纯 rank 0 跃迁（如 $^{206}\text{Tl}(0^-) \to {^{206}\text{Pb}}(0_1^+)$），由于压低了时样轴矢算符 $\xi^\prime v$ 的表观增强，计算的跃迁几率将被低估数倍，残差显著激增；在 rank 1 跃迁中，改变 $x$ 与 $u$ 的比例导致干涉项失真。

### 逆向测试二：相空间五次方拟合与真实形状因子积分差异测试
- **操作方案**：在典型等待点核中，对比采用完整四项形状因子数值相空间积分得到的偏衰变率 $\lambda_{\text{exact}}$，与采用允许相空间乘以平均常数形状因子近似 $\lambda_{\text{approx}} = \overline{C} \cdot f_0$。
- **检验判据**：检查二者的相对偏差。若偏差在高能端或大自旋变化跃迁中显著放大，则证明基于简化 $\log ft$ 处理禁戒衰变将引入相空间偏置。

## Open Questions

1. 随着手征有效场论在丰中子核结构中的发展，如何从微观核力自洽导出包含两体弱流的一阶禁戒有效算符，从而逐步减少对经验常数淬灭参数的依赖？
2. 在中子数 $N=126$ 极丰中子核中，中子分离能极低时的连续谱耦合如何定量影响首禁戒强度的相空间积分分布？
3. $^{129}\text{Cd}$ 两个长寿命母态各自的纯中子发射几率 $P_n$ 真实数值是多少，本任务未获得相应逐态输入。

## Human Review

本笔记由 Agent 根据 Zhi et al. 2013 PRC（arXiv:1301.5225v1，14页）、Dunlop et al. 2016 PRC、Saito et al. 2020 PRC 以及 T04 独立原件审计（[[doctoral-r1-t04-first-forbidden-operator-audit-20261108]]）完成研读、推演与交叉复核。本轮任务未发生用户逐项审核事件，记录的是自主研学自审结果，未标记为 human-reviewed。所有的推断与分析性假说均保留 provisional 状态。

## Promotion or Rejection History

- **2026-11-08**：初始创建并经物理审核与 T04 独立原件审计修订（任务 G34，阶段 1 弱相互作用翼实质研学）。核正了预印本实际 14 页码与 Table I 实际 20 跃迁行的结构边界；厘清了始末核质量端点能与中性原子能量零点、积分相空间吸收形状因子与传统 $\log f_0 t$ 的数学区别；如实记录了 T04 对 Table I 内部理论列自洽性的审计疑点；严格明确了 $^{131m}\text{In}$ 与 $^{130}\text{Cd}$ 的校准样本属性，保持 provisional 状态。
