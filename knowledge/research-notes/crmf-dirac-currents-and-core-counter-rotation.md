---
type: research-note
title: "CRMF 空间 Dirac 流、核芯反向旋转与磁转动有效 g 因子"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [CRMF spatial Dirac currents, core counter-rotation, relativistic shears currents, CRMF magnetic rotation]
tags: [crmf, dirac-currents, core-counter-rotation, magnetic-rotation, g-factor-quenching]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 L4-authorized CRMF spatial-current and magnetic-rotation proxy study
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, clark-2000-shears-mechanism, garg-2015-135pr-magnetic-rotation]
promotion_target: ""
---

# CRMF 空间 Dirac 流、核芯反向旋转与磁转动有效 g 因子

## Research Trigger

本任务要求把相对论推转平均场（CRMF）中的时间反演破缺、空间矢量场、价准粒子剪刀流、核芯反向流和磁偶极强度放到同一套可复现诊断中，并比较 $^{199}$Pb 与 $^{135}$Pr。指定来源给出了推转 Routhian、磁转动剪刀图像和 $^{135}$Pr 的实验覆盖范围，但没有提供一个可直接重跑的 3-D CRMF 场解或 Dirac 海分辨输出。因此本页把“微观结构方程”与“代理数值结果”分开：前者是 CDFT 的算符和线性响应写法，后者是明确标注的二维代理模型，不能冒充 CRMF 计算或实验反演。

## Grounded Evidence

### 来源与证据层

| claim | claim_kind | evidence_level | locator | 结论边界 |
| --- | --- | --- | --- | --- |
| 推转平均场使用 $H'=H-\boldsymbol\omega\cdot\mathbf J$；自洽解随形变、组态、频率和角动量方向变化 | model-formalism | direct | [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]], PDF pp.467, 469–471, Secs.II–III | 支持 Routhian/取向框架，不直接给 CRMF 空间流数值 |
| 磁转动由高-$j$ 粒子/空穴电流环的剪刀闭合产生较大 M1、较小 E2；横向磁矩随闭合减小 | review-background / author-interpretation | direct | [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]], PDF pp.487–488, Fig.18; [[clark-2000-shears-mechanism]], PDF pp.15–18 | 支持半经典剪刀观测图像，不证明特定核的 Dirac 流拓扑 |
| Clark 用 $^{198,199}$Pb 寿命与剪刀角度拟合得到约 $g_{\rm eff}=0.92$，Schmidt 估计约 1.17 | model-fit | direct | [[clark-2000-shears-mechanism]], PDF pp.15–18 | $0.92/1.17\simeq0.79$ 是配置特定有效差值的尺度提示，不能直接命名为普适 $q_s$ |
| $^{135}$Pr 原实验给出候选磁转动带的相对 $B(M1)/B(E2)$；没有同带绝对寿命，不能分离绝对 $B(M1)$ 和 $B(E2)$ | experimental-report-and-limitation | direct | [[garg-2015-135pr-magnetic-rotation]], PDF pp.7–8, Figs.5–8; note 中 GA15-D26-003/004 | 不可由该实验单独反演 $g_p-g_n$ 或流重整化 |

### CRMF 空间流的算符结构

在常见协变 EDF 的符号约定中，旋转系单粒子方程可写成

$$
 h'\psi_k=\epsilon'_k\psi_k,\qquad
 h'=\boldsymbol\alpha\cdot[-i\boldsymbol\nabla-\mathbf V(\mathbf r)]
 +\beta[m+S(\mathbf r)]+V^0(\mathbf r)-\boldsymbol\omega\cdot\mathbf J .
$$

空间矢量势由 $ω$、$ρ$ 和光子场组成，例如

$$
 \mathbf V=g_\omega\boldsymbol\omega+g_\rho\tau_3\boldsymbol\rho
 +e\frac{1-\tau_3}{2}\mathbf A,
$$

而场方程的空间部分以核子四流为源，抽象地写为

$$
 (-\nabla^2+m_a^2)\,\mathbf a(\mathbf r)=g_a\,\mathbf j_a(\mathbf r),
 \qquad \mathbf j_D(\mathbf r)=\sum_{k\in occ}\bar\psi_k(\mathbf r)\boldsymbol\gamma\psi_k(\mathbf r).
$$

不同文献对 Dirac 哈密顿量中 $α\cdot\mathbf V$ 的正负号、核子电荷投影和度规采用不同约定；物理约束是“空间场与同一四流自洽耦合”，不能只从单一字面符号判定流向。时间反演不变的静态偶偶解中，成对轨道的空间流相消；推转和阻塞破坏该配对相消后，$ω$、$ρ$、$A$ 的空间分量通常不再为零。

这里的“非对称电流环”应精确定义为：在内禀平面内，$ψ(\mathbf r)$ 的高-$j$ 粒子与空穴占据形成不同中心、不同符号或不同权重的环流，导致 $∫ \mathbf r\times\mathbf j_D\,d^3r$ 具有横向分量。它是剪刀几何的微观候选机制；仅有一个非零 $ω$ 或非零 $α\cdot\mathbf V$ 并不能单独证明某条实验带是 MR。

## Provisional Reasoning

### 1. 价流、核芯极化和“Dirac 海”分解

将总空间流按计算可识别的来源写成

$$
 \mathbf j_D=\mathbf j_{\rm val}+\delta\mathbf j_{\rm core}+\delta\mathbf j_{\rm sea}.
$$

价准粒子流由阻塞的高-$j$ 轨道主导；核芯项来自其余占据轨道在自洽矢量场和残余相互作用下的线性响应。对一个稳定的参考解，最小线性响应写成

$$
 \delta\mathbf j_{\rm core}(\mathbf r)
 =-\int d^3r'\,\boldsymbol\chi_{\rm core}(\mathbf r,\mathbf r';\omega)
 \mathbf K_{\rm v}(\mathbf r,\mathbf r';\omega)\mathbf j_{\rm val}(\mathbf r').
$$

若核芯响应核在局域投影上为正，负号表示反向流；在自洽闭合下可用标量示意式

$$
 \delta j_{\rm core}\simeq -\frac{f_{\rm core}\chi}{1+\chi}\,K[j_{\rm val}],
$$

其中分母代表矢量场反馈的饱和/屏蔽。这个负号不是由“相对论”三个字单独推出的定理：它依赖参考态、残余核、阻塞和转轴。可检验的 CRMF 判据是逐频率报告 $∫\mathbf r\times\delta\mathbf j_{\rm core}$ 的符号、大小和对网格/参数的稳定性。

标准 no-sea CDFT 通常把负能 Dirac 海的显式动力学吸收到参数化真空极化中，而不输出逐轨道的 $δ\mathbf j_{\rm sea}$。因此本研究的“Dirac 海反极化”只能写成待检验的敏感性项：若使用带真空极化的正则化计算，应将负能贡献与正能核芯响应分别记账；当前代理代码用一个 6% 的标记残差通道表示这种不确定性，绝不将其解释为已计算的真空贡献。

### 2. 有效 g 因子与 M1 强度

剪刀几何下，取 $θ$ 为两叶片夹角、$θ_p$ 为质子叶片相对总角动量的角，则一体算符的条件表达式为

$$
 \mu_\perp=\mu_N(g_p^{\rm eff}-g_n^{\rm eff})\frac{j_pj_n}{I}\sin\theta,
$$

$$
 B(M1;I\to I-1)=\frac{3}{8\pi}
 \left[(g_p^{\rm eff}-g_n^{\rm eff})\frac{j_pj_n}{I}\sin\theta\right]^2\mu_N^2.
$$

将自由值与介质中有效算符的比写成 $q_g=g_\Delta^{\rm eff}/g_\Delta^{\rm free}$，则

$$
 B(M1)_{\rm eff}=q_g^2B(M1)_{\rm free}.
$$

$q_g$ 是轨道/自旋算符、空穴符号、构型混合、核芯极化和两体电流的合成投影。代理扫描把 $^{199}$Pb 的 $q_g$ 设为 0.836→0.740、$^{135}$Pr 设为 0.880→0.800（$ħ\omega=0.15\to0.75$ MeV）；因此 $B(M1)$ 修正因子为约 0.70→0.55（Pb）和 0.77→0.64（Pr）。这与“0.70–0.85 的有效 g 尺度”有数量级重叠，但不是实验测得的普适区间。

代理运行的积分分解（单位为模型内部的 $ħ$ 归一化）如下：

| 核素 | $ħ\omega$ (MeV) | $J_{\rm val}$ | $J_{\rm core}$ | $J_{\rm sea,proxy}$ | $J_{\rm total}$ | $q_g$ | $B/B_{free}$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $^{199}$Pb | 0.15 | 3.74 | −1.04 | −0.063 | 2.63 | 0.836 | 0.699 |
| $^{199}$Pb | 0.35 | 10.09 | −3.37 | −0.202 | 6.52 | 0.804 | 0.646 |
| $^{199}$Pb | 0.75 | 26.52 | −11.75 | −0.705 | 14.07 | 0.740 | 0.548 |
| $^{135}$Pr | 0.15 | 2.07 | −0.37 | −0.022 | 1.67 | 0.880 | 0.774 |
| $^{135}$Pr | 0.35 | 5.57 | −1.22 | −0.073 | 4.28 | 0.853 | 0.728 |
| $^{135}$Pr | 0.75 | 14.66 | −4.36 | −0.262 | 10.03 | 0.800 | 0.640 |

表中 $J_{\rm core}$ 的负号是代理响应的输入设计，不是 Clark 或 Garg 的实验观测；它应在真实 CRMF 中由占据轨道和矢量场自洽产生。$^{199}$Pb 的 $g_{\rm eff}\simeq0.92$ 与 Schmidt 1.17 的比值约 0.79，可作为该表“有效算符整体尺度”的外部量级校准；$^{135}$Pr 没有绝对寿命，不能作同类经验反演。

### 3. 流场拓扑与终止极限

代理程序在 $x$–$z$ 内禀切片使用无散流函数 $ψ$：

$$
 j_x=\partial_z\psi,\qquad j_z=-\partial_x\psi,
 \qquad \omega_y=\partial_xj_z-\partial_zj_x.
$$

中等频率用两个相反权重的 Gaussian 环流，中心间距 $d\propto\sin\theta$；终止路径令 $θ:70^\circ\to8^\circ$，并把双环流连续混合为 $ψ_{\rm cyl}\propto r^2\exp[-r^2/(2\sigma^2)]$。因此双叶片的横向涡度结构逐渐变成关于转轴的圆柱对称流。程序输出的 `topology_signed_vorticity_index` 只是网格上的符号涡度统计量，不是严格拓扑不变量，也不证明真实 CRMF 解必然经过该连续路径；真实终止应检查 $β_2,γ$、惯量张量、密度对称性和轨道占据是否同时恢复轴对称。

## Assumptions

- 研究对象是无配对或弱配对的阻塞奇奇/奇 A 高自旋构型；数值只保留二维内禀切片。
- Valence current 用两个高-$j$ 局域流环表示；核芯用平滑线性响应表示，响应系数随频率缓慢变化。
- $B(M1)$ 使用半经典高自旋剪刀表达式；量子有限-$I$ CG 系数、投影、构型混合和 M1/E2 混合未求解。
- 计算网格、流函数和 $q_g$ 参数均为可见输入；任何数值结果均为 model-result/our-inference，而非实验事实。
- Dirac 海通道是 6% 的敏感性残差，不是标准 no-sea CRMF 的显式负能级求和。

## Competing Explanations

1. 所谓“核芯反向旋转”可能只是实验室系下价流与集体转动的分解约定；需要独立的局域流场、轨道分辨和转轴依赖来确定。
2. $B(M1)$ 偏低可由叶片角、空穴符号、构型混合、未观测分支、DSAM stopping、M1/E2 混合或 E2 分母变化造成，不必归因于 $g$ 猝灭。
3. 介子交换电流、短程关联和模型空间外极化可改变有效算符；它们不能都压缩为一个与频率无关的 0.79 常数。
4. 终止附近的流场轴对称化可能与能带交叉、配对塌缩或形状分支切换竞争；“涡度变圆柱”是代理模型的连续路径，不是实验判据。
5. $^{135}$Pr 的相对 $B(M1)/B(E2)$ 变化也可能主要由 $B(E2)$ 或分支/门选择变化驱动；缺绝对寿命时不能把它当作 $B(M1)$ 证据。

## Transfer Conditions

结果只有在以下条件同时满足时才可迁移到实际 CRMF/TAC-CDFT：使用同一协变参数化和配对方案；给出阻塞组态、旋转频率、轴排序和空间网格；输出 $ω$、$ρ$、光子空间场以及每个轨道的 $̄\psi\gamma^i\psi$；对无反向流的 frozen-core、全自洽 core 和不同截断做对照；并把计算的绝对 M1/E2 连接到寿命、分支、ICC、DCO/偏振的同一实验合同。跨 Pb–Pr 比较还要固定 $g_l/g_s$、空穴号、角度定义和频率单位。

## Failure Conditions

- 把代理 `J_core_counter_hbar` 或 6% `J_dirac_sea_antipolarization_proxy_hbar` 写成某一 CRMF 参数组的已发表输出。
- 把 $g_{\rm eff}/g_{\rm free}=0.70$–0.85 写成所有 MR 核素的实测、普适或纯自旋淬灭因子。
- 用 $^{135}$Pr 的相对 $B(M1)/B(E2)$ 反演绝对 $g$ 或核心流。
- 把 Frauendorf/Clark 综述示意和具体 $^{199}$Pb 的实验数据混为同一独立来源。
- 由单一切片的视觉涡旋、涡度符号或终止频率直接认证三维拓扑相变。

## Falsification or Reverse Tests

1. 在同一 CRMF 组态下输出全核子、价轨道、深层轨道和负能正则化项的空间流；若核芯角动量不稳定、符号随坐标变换改变或趋近零，则撤回“普遍反向旋转”措辞。
2. 做 frozen-core 与 fully self-consistent 对照。若 $B(M1)$、$J_{\rm core}$ 和 $q_g$ 差异小于数值误差，核心反流不是主要机制。
3. 改变矢量耦合、有效质量、配对和网格盒边界；若 0.70–0.85 区间只由一个参数组给出，则该区间只能保留为模型示例。
4. 对 $^{199}$Pb 同时拟合寿命所得绝对 $B(M1)$、静态 $g$、$B(E2)$ 和配置角度；若单一有效算符无法同时描述这些量，应优先引入构型混合/两体电流而不是继续调 $q_g$。
5. 对 $^{135}$Pr 补测同带绝对寿命和 E2 crossover；若绝对 $B(M1)$ 不随代理 $q_g$ 变化或比值峰由 E2 分母解释，则撤回 Pr 的流重整化推断。
6. 在终止极限检查轴向密度、惯量本征值和所有空间流分量，而不是只检查 `topology_signed_vorticity_index`；若这些量不恢复圆柱对称，则撤回拓扑转变陈述。

## Open Questions

- 现有指定来源没有给出 $^{198,199}$Pb 或 $^{135}$Pr 的公开 CRMF 轨道分辨 $ω$、$ρ$、光子空间场和局域 Dirac 流数据；需定位原始 TAC-CDFT/CRMF 计算或重跑代码。
- no-sea 参数化中真空极化的物理内容如何与显式负能 Dirac 海流分离，尚不能由本代理数值回答。
- Pb 区 0.92 有效差值中轨道项、空穴号、核芯极化和两体电流的独立分解仍不具可识别性。
- Pr 区需要绝对寿命、完整分支和 crossover，以检验相对 $B(M1)/B(E2)$ 的非唯一性。
- 终止附近流场拓扑是否存在定义不依赖坐标、网格和规约的指标，需要 3-D 自洽流的同伦/对称性分析。

## Human Review

本页由 Codex 完成来源回链、公式分层、代理代码和反证设计；`review_status: unreviewed` 保持不变。人工复核重点是空间矢量场符号约定、no-sea 语义、指定核素的实际 CRMF 文献定位，以及是否允许在后续论文中使用“core counter-rotation”这一强措辞。

## Promotion or Rejection History

2026-10-29：建立 provisional research note。`supports` 推转 Routhian、剪刀电流环和 M1/E2 观测层；`limits` 三份指定来源对 CRMF 局域 Dirac 流、负能海分解和 Pr 绝对 $B(M1)$ 的覆盖；`candidate` 二维线性响应代理和可复现积分分解。尚未晋升为 model、observable 或 synthesis 页面。
