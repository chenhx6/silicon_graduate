---
type: research-note
title: "反磁转动四叶片剪刀临界闭合角速度的全核区同位素定标律与壳效应调制"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [amr-shears-critical-frequency-isotopic-scaling-and-shell-modulation, AMR critical frequency isotope scaling, AMR shell modulation]
tags: [antimagnetic-rotation, critical-frequency, scaling-laws, shell-effects, cadmium-palladium]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 delegated investigation of AMR four-blade shears critical-frequency isotope scaling"
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-first-page, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
---

# 反磁转动四叶片剪刀临界闭合角速度的全核区同位素定标律与壳效应调制

## Research Trigger

本研究追问三个问题：双剪刀/四叶片反磁转动的闭合频率如何从有效粒子–空穴相互作用得到；同位素改变 (A)、((N-Z)/A)、费米面轨道和核芯惯量后，理论闭合点如何迁移；以及为什么实验上最清楚的 Cd/Pd 反磁转动集中在 (Napprox56	ext{--}66) 的窄窗口。

任务给定的

\[
\cos\theta=\frac{\omega}{\omega_c},\qquad
\hbar\omega_c=\frac{3V_{\pi\nu}}{2j_\pi}
\]

可以在最小 (P_2) 角势中严格推出，但它是内禀剪刀频率，不能自动等同于由实验 (E_\gamma) 反推出的实验频率。(j_\nu) 和 (mathcal J_{\rm core}) 主要改变总自旋映射与闭合自旋。本文因此同时记录内禀 (omega_c)、

\[
I_c=j_\nu+2j_\pi+\mathcal J_{\rm core}\omega_c,
\]

以及实验最高跃迁能量的条件代理。

## Grounded Evidence

### 直接实验与模型输入

| 核素 | 直接来源与定位 | 可用实验量 | 组态/模型边界 |
|---|---|---|---|
| (^{106}\mathrm{Cd}) | Roy et al. 2011, printed p.324 Table 1及Cd比较 | 带区间 (18^+\text{--}24^+)；表中最高列出的带内 (E_\gamma=1675.5\) keV；(B(E2)) 从约 0.15 降至 0.05 (e^2b^2) | 作者的两粒子加转子比较，采用 (V_{\pi\nu}=1.2) MeV；不是裸两体矩阵元 |
| (^{108}\mathrm{Cd}) | Roy et al. 2011, printed p.324 Table 1及Cd比较 | (16^+\text{--}24^+)；最高列出 (E_\gamma=1469) keV；末端有效寿命标签需保留 | 纯反磁转动比较，(V_{\pi\nu}=1.2) MeV；中子有效角动量和占据随构型给定 |
| (^{110}\mathrm{Cd}) | Roy et al. 2011, p.324 Table 1; pp.325–326 Fig.4与讨论 | (16^+\text{--}24^+) 的 (B(E2)=0.14(1),0.12(2),0.11(2),0.09(3),0.06(2)\ e^2b^2)；最高表列 (E_\gamma=1358) keV；作者认为更高顶端受重叠/有效喂入影响 | (V_{\pi\nu}=1.2) MeV，(mathcal J_{\rm core}=19.5\,\hbar^2/\mathrm{MeV})；AMR 与核芯转动耦合 |
| (^{104}\mathrm{Pd}) | Rather et al. 2014, arXiv全文 p.10 Table 1及 pp.4–5 Eqs.4–9 | (16^+\text{--}26^+)；(B(E2)=0.26(2)\to0.02(1)\ e^2b^2)；本轮未从图表逐线重建最高 (E_\gamma) | 有效 (pi g_{9/2}^{-2}\otimes\nu[h_{11/2}^2(g_{7/2},d_{5/2})^2])，(V_{\pi\nu}=1.2) MeV、(mathcal J=5\,\hbar^2/\mathrm{MeV})；PNC 四空穴是另一模型空间 |
| (^{108,110}\mathrm{In}) | Chiara et al. 2001, DSAM/寿命与剪刀带来源 | 有剪刀带寿命与 (B(M1),B(E2)) 提取链；本轮没有把未逐表核验的带头、终止自旋和最高跃迁填入 | 剪刀带来源不等价于偶偶 Cd 双剪刀的同一几何参数 |

Roy 的三种 Cd 模型均固定 (V_{\pi\nu}\approx1.2) MeV；随 (N) 变化的显式模型输入还包括 (j_\nu)、占据数 (n) 和核芯响应。该事实支持“模型中的中子数效应不等于 (V_{\pi\nu}) 已被实验测出单调变化”。Rather 2014 将 (V_{\pi\nu}=1.2) MeV 从邻近 Cd 系统学迁移到 (^{104}\mathrm{Pd})，所以它是有效参数的模型迁移，不是独立的四空穴相互作用测量。

### 最小四叶片角势推导

取两支镜像质子空穴叶片的有效角动量为 (j_\pi)，中子刃沿转轴方向，令 (c=\cos\theta)。在固定旋转系频率的最小有效哈密顿量中，角相关部分写为

\[
E(c,\omega)=V_{\pi\nu}P_2(c)-2\hbar\omega j_\pi c,
\qquad P_2(c)=\frac{3c^2-1}{2}.
\]

驻值条件为

\[
\frac{\partial E}{\partial c}=3V_{\pi\nu}c-2\hbar\omega j_\pi=0,
\]

故

\[
\boxed{c=\cos\theta=\frac{\omega}{\omega_c}},
\qquad
\boxed{\hbar\omega_c=\frac{3V_{\pi\nu}}{2j_\pi}}.
\]

在这个约定下，(omega=0) 对应最大张角，(omega=\omega_c) 对应经典闭合。四叶片的 (\mathcal R_y(\pi)\mathcal T) 对称性可使横向磁矩在镜像叶片之间相消；电四极振幅带有 (\sin^2\theta)，从而最小几何模型给出 (B(E2)\propto\sin^4\theta)。有限核的反对称化、配对、(P_4(c)) 项、形变收缩和带交叉会使这一幂律成为有限窗口近似。

### 体积–同位旋有效标度

在同一有效模型空间中，令核半径 (R=r_0A^{1/3})。若粒子–空穴角势的径向重叠和归一化因子在有限范围内近似给出 (R^{-1}) 的主导尺度，则

\[
V_{\pi\nu}(A,\delta)=V_0A^{-1/3}f(\delta),
\qquad \delta=\frac{N-Z}{A}.
\]

电荷对称性要求最低阶同位旋修正为偶函数；截断到 (delta^2) 得

\[
\boxed{V_{\pi\nu}(A)=V_0A^{-1/3}\left[1-\kappa\left(\frac{N-Z}{A}\right)^2\right]}.
\]

这不是从三篇来源唯一证明的裸核力定律，而是一个有明确半径尺度、同位旋偶性和参数约定的有效标度 ansatz。工件用 Roy 2011 的 (^{110}\mathrm{Cd}), (V_{\pi\nu}=1.2) MeV、(kappa=1) 做归一，得到 (V_0approx5.85) MeV。(V_0)、(kappa) 必须在固定 PNC/HFB/EDF 空间重新拟合，不能跨模型直接比较。

### 实验代理的定义

当来源给出最高带内跃迁能量时，工件报告

\[
\hbar\omega_{\gamma\text{-proxy}}=E_\gamma^{\max}/2.
\]

它只把 (E_\gamma\simeq2\hbar\omega) 作为转动能标的近似，不替代作者的 (I(\omega)) 曲线，也不处理有效寿命、内转换、支线分支和喂入协方差。缺少直接定位的 (I_0)、(I_{\rm term}) 或 (E_\gamma^{\max}) 在 CSV/JSON 中保留为空值。

## Provisional Reasoning

### 同位素窗口与 (h_{11/2}) 费米面

在 (N\sim56\text{--}66) 的中等质量区，(g_{7/2}/d_{5/2}) 与 (h_{11/2}) 的相对占据、配对和旋转对齐共同决定中子刃的有效长度。随着中子数增加，费米面可能从 (h_{11/2}) 下沿向中层移动，使可用的高-(j) 对齐和四极转动密度改变；这会同时改变 (j_\nu)、(mathcal J_{\rm core}) 和角势曲率。模型证据支持“构型重排比裸 (V_{\pi\nu}) 单调变化更直接”，但不能仅凭 (N) 证明单调趋势。

为把该窗口放入相图，工件定义一个独立壳代理

\[
n_{h11/2}=\mathrm{clip}\left(\frac{N-56}{10},0,1\right),
\qquad
f_{\rm shell}=1+0.12\sin(\pi n_{h11/2}).
\]

于是 (V_{\pi\nu}^{\rm shell}=f_{\rm shell}V_{\pi\nu})。它在 (N=61) 附近达到最大，仅表示中层费米面极化的工作假设；不是从 Cd/Pd 数据拟合出的普适函数。若加入配对阻塞、形变自洽和 PNC 占据，窗口边界可能移动。

### 26 个候选核素的结果摘要

`amr_isotope_systematics.csv` 包含 101–110Pd、106–110Cd、108–111In、142–146Gd 和 100–101Ru 控制行，共 26 个对象。直接 AMR 实验字段只对 104Pd、106Cd、108Cd、110Cd 填入。其余核素的理论值是统一公式下的候选扫描，`evidence_status` 明确标为 `review-candidate`、`lifetime-source-candidate` 或 `cross-mass-probe-no-AMR-closure`。

代表性直接对账如下（数值来自工件的统一计算）：

| 核素 | (V_{\pi\nu}^{\rm base}) (MeV) | (hbar\omega_c^{\rm shell}) (MeV) | (I_{\rm term}^{\rm obs}) | (I_c^{\rm shell}) |
|---|---:|---:|---:|---:|
| (^{104}\mathrm{Pd}) | 1.226 | 0.438 | 26 | 27.2 |
| (^{106}\mathrm{Cd}) | 1.224 | 0.437 | 24 | 27.0 |
| (^{108}\mathrm{Cd}) | 1.212 | 0.450 | 24 | 25.0 |
| (^{110}\mathrm{Cd}) | 1.200 | 0.446 | 24 | 27.7 |

这里的 (I_c) 是把来源的有效 (j_\nu) 和 (mathcal J_{\rm core}) 代入最小公式得到的闭合自旋估计，不能当作逐级谱线拟合。(^{110}\mathrm{Cd}) 的核芯惯量把闭合自旋向高处推移，与其 (B(E2)) 平台和 AMR+core 解释方向一致；(^{104}\mathrm{Pd}) 的 (B(E2)) 快速下降则说明相同 (V_{\pi\nu}) 迁移并不保证相同核芯平台。

## Assumptions

- 两支质子叶片镜像、等权，(c=\cos\theta) 是内禀几何变量。
- (V_{\pi\nu}) 是已经吸收轨道矩阵元、活跃粒子数、配对和归一化约定的有效角势参数。
- (j_\pi)、(j_\nu) 是模型有效角动量，不自动等于单个 Nilsson 轨道的 (j)。
- (mathcal J_{\rm core}) 使用静态粒子–转子惯量；频率依赖惯量、跨带交叉和自洽形变没有纳入最小闭合公式。
- (E_\gamma^{\max}/2) 只是旋转频率的条件代理。
- 壳因子 (f_{\rm shell}) 是敏感性扫描输入，不是实验拟合，也不是直接来源结论。

## Competing Explanations

- (B(E2)) 下降可由剪刀闭合、频率依赖形变收缩、配对/占据重排、带交叉、侧馈或停止本领系统误差共同产生。
- (N=56\text{--}66) 的集中可能反映高-(j) 轨道可用性与弱形变窗口的重叠，而不是单一 (V_{\pi\nu}) 标度。
- (^{110}\mathrm{Cd}) 的平缓 (B(E2)) 可能包含核芯集体转动、形变软化或未分辨组态混合；不能只由四叶片几何幂律判定。
- Gd 条目在本地证据集中是跨质量区探针，不应被模型输出升级为已观测 AMR。

## Transfer Conditions

可迁移的是最小 (P_2) 驻值推导、(A^{-1/3}) 与偶同位旋修正的参数化形式、以及 (I_c=j_\nu+2j_\pi+\mathcal J_{\rm core}\omega_c) 的变量分工。迁移到奇 A、四质子空穴、In 或 Gd 时必须重新计算叶片权重、signature、配对阻塞、费米面占据和核芯惯量。(V_0=5.85) MeV、(kappa=1)、壳振幅 0.12 只属于本工件的敏感性基线。

## Failure Conditions

- 将 (V_{\pi\nu}=V_0A^{-1/3}[1-\kappa\delta^2]) 写成已由实验普遍证明的裸相互作用定律。
- 将 (hbar\omega_c=3V_{\pi\nu}/(2j_\pi)) 与实验 (E_\gamma/2) 视为同一直接观测量。
- 把 (j_\nu) 或 (mathcal J_{\rm core}) 无条件塞进内禀 (omega_c) 公式，混淆频率与总自旋映射。
- 用邻近 Cd/Pd 的参数补造 101–111In 或 142–146Gd 的带头、终止或最高跃迁。
- 把示意壳因子、相图和 SVG 曲线称为微观 PNC/HFB/EDF 预测。

## Falsification or Reverse Tests

1. 在同一 PNC/HFB 空间固定 (V_{\pi\nu}) 改变 (mathcal J_{\rm core})，检验内禀 (omega_c) 是否稳定而 (I_c) 迁移；若直接频率也漂移，说明需要频率依赖角势。
2. 用实际 (h_{11/2},g_{7/2},d_{5/2}) 单粒子能级、配对隙和四极矩替换壳代理，拟合 (V_2,V_4)，检查 (cos\theta) 线性区间。
3. 对 101–105Pd、106–110Cd 和 108–111In 取得同一实验协议下的寿命、完整支线和喂入协方差，比较 (B(E2)) 斜率与模型闭合点。
4. 对 (N=56\text{--}66) 之外的同组态候选核寻找高-(j) 费米面和弱形变条件；若同样的 (B(E2)) 下降和绝对寿命出现，窄窗口解释需要修正。
5. 若高分辨数据显示 (E_\gamma^{\max}/2) 与自洽 (omega_c) 系统偏离，优先检查频率定义、核芯惯量和带交叉，而不是调大壳因子。

## Open Questions

- 能否从 Roy 2011 Fig.3–4 和 Rather 2014 Fig.3 对所有级联逐点数字化 (I(\omega))、(B(E2)) 与拟合协方差？
- (V_0,kappa) 是否能用同一 PNC-CSM 或 projected-HFB 空间而不是四个现象学点重新估计？
- 108–111In 的 Chiara 2001 剪刀带是否存在可与 Cd/Pd 同定义的 (j_\pi,j_\nu) 和终止判据？
- 142–146Gd 是否有直接 AMR 候选带，还是核芯集体转动已压过剪刀信号？
- (N=56) 和 (N=66) 的窗口边界由 (h_{11/2}) 占据、配对阻塞、形变或实验可观测性中的哪一项主导？

## Human Review

尚未进行人工审核。`review_status: unreviewed`、`reasoning_status: provisional` 保持不变。人工复核重点是：Roy/Rather 参数的模型层级、(E_\gamma/2) 代理的频率约定、四叶片与四空穴有效角动量的对应关系、以及 In/Gd 候选池是否需要补入直接来源。

## Promotion or Rejection History

2026-10-29：新建研究笔记。保留最小 (P_2) 闭合频率推导，加入有限范围 (A,N) 的统一候选扫描；将 104Pd、106/108/110Cd 的实验字段与其来源定位分开；In、Gd 和 Pd 未核验条目仅作为候选/控制行。尚未晋升为正式 synthesis，未记录 human-reviewed 事件。

## Reproducible Artifacts

脚本与工件位于 [`amr-scaling-laws` worker](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-scaling-laws/)。运行 `python3 amr_scaling_laws.py` 可重建 26 核素 CSV、JSON、1626 点 (A)–(N) 相图数据和 SVG 示意图。工件内的 `evidence_status` 是事实边界的一部分，不应删除后再解释数值。
