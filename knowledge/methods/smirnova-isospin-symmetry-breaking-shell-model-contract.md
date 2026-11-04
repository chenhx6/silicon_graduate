---
type: method
title: "Smirnova：同位旋对称性破缺、INC 壳模型与弱电修正合同"
aliases: [Smirnova isospin-symmetry breaking, INC shell model, IMME MED TED isospin mixing, delta_C superallowed Fermi decay]
method_type: "isospin-symmetry-breaking-and-weak-interaction-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Nuclear Shell Model 70 Years article 12, full main-text reading"
confidence: "high for formalisms and review comparisons; conditional for specific model parameters"
tags: [shell-model, isospin-symmetry-breaking, inc-hamiltonian, imme, med, ted, superallowed-fermi, cvc, vud, isospin-mixing]
sources: [book-nuclear-shell-model-70-years]
---

# Smirnova：同位旋对称性破缺、INC 壳模型与弱电修正合同

## Purpose

这篇综述解决的是低能核物理中一个跨越强相互作用、电弱统一检验与核天体物理的核心课题：
核多体系统中的微小同位旋对称性破缺（Isospin-Symmetry Breaking, ISB）如何通过壳模型
有效相互作用（Isospin-Nonconserving, INC Hamiltonians）得到定量描述，并在以下关键问题中
建立可检验的分析基准：

1. 等位旋多重态质量方程（IMME）的系数结构与配对交错效应；
2. 镜像能级差（MED）与三重态能级差（TED）对对齐机制、核半径（中子皮）与 Thomas–Ehrman 位移的约束；
3. 等位旋禁戒衰变（如 IAS 质子、\(\alpha\)、两质子衰变）与同位旋杂质矩阵元反演；
4. 超允许 \(0^+\to0^+\) Fermi \(\beta\) 衰变的同位旋对称性破缺修正项 \(\delta_C=\delta_{C1}+\delta_{C2}\)，用于检验 CVC 假说与提取 CKM 矩阵元 \(|V_{ud}|\)；
5. 恒星爆发生核过程中天体物理质子捕获反应率与共振强度的壳模型修正。

文章把同位旋破缺的物理来源分层为：长程库仑势、微观核起源电荷相关力（CD 与 CSB）、
模型空间截断与径向波函数不匹配。它为低能谱学、弱衰变与镜像核结构提供了微观分析合同。

## Inputs and Assumptions

### Isospin algebra and tensor decomposition

将核子视为 \(t=1/2\) 的费米子，在同位旋空间由两分量旋量表示，中子与质子对应 \(m_t=\pm1/2\)。
对于 \(A\) 核子系统，总同位旋算符 \(\vec T=\sum_k \vec t(k)\)，其第三分量 \(T_z=(N-Z)/2\)。

由于电磁相互作用和核力中的电荷非对称成分，核哈密顿量在同位旋空间可分解为不可约球张量：

\[
\hat H = \hat H^{(0)} + \hat H^{(1)} + \hat H^{(2)} ,
\]

其中包含等标（标量 \(\lambda=0\)）、等矢（矢量 \(\lambda=1\)）和等张（张量 \(\lambda=2\)）三部分。
在微观双核子相互作用层面，Henley–Miller 将两核子力严格分为四类：

- **Class I**：电荷无关相互作用（\(\{1, \vec t(1)\cdot\vec t(2)\}\)）；
- **Class II**：破缺电荷无关性（Charge Independence Breaking, CIB），但保留电荷对称性（\(\{t_3(1)t_3(2)\}\)）；
- **Class III**：破缺电荷对称性（Charge Symmetry Breaking, CSB），在 \(n-p\) 系统中消失（\(\{t_3(1)+t_3(2)\}\)）；
- **Class IV**：不守恒两核子总同位旋的相互作用（\(\{\vec t(1)\times\vec t(2), t_3(1)-t_3(2)\}\)）。

两体库仑相互作用同时包含 Class I、II、III 分量。在手征有效场论（\(\chi\text{EFT}\)）中，
两核子力强度遵循分层：\(V_I \gg V_{II} > V_{III} > V_{IV}\)。

### INC shell-model Hamiltonian

在价空间壳模型中，INC 哈密顿量构建为基准电荷无关相互作用加上 INC 修正：

\[
\hat H_{\rm INC} = \hat H_0 + \hat V_{\rm INC} , \quad
\hat V_{\rm INC} = \hat V_{\rm Coul} + \hat V_{\rm CD} + \sum_a \tilde\epsilon(a) ,
\]

其中 \(\hat V_{\rm CD}\) 包含微观短程核电荷相关力，\(\tilde\epsilon(a)=\epsilon_p(a)-\epsilon_n(a)\) 为核芯库仑极化产生的等矢单粒子能。
在低阶微扰下，等位旋多重态能级满足二次 IMME：

\[
E(A, T, T_z) = a(A, T) + b(A, T) T_z + c(A, T) T_z^2 .
\]

对于 \(T\ge3/2\) 的四重态与五重态，若出现更高级的三体电荷相关力或强同位旋态混合，可能产生三次项 \(d T_z^3\) 和四次项 \(e T_z^4\)。

## What It Can Establish

### 1. IMME 系数 \(b\) 与 \(c\) 的微观机制与配对交错

文章指出，经验电荷相关壳模型相互作用（如 sd 壳参数化与 pf 壳 GX1Acd）能够高精度再现实验 IMME 系数：

- sd 壳 \(b\) 系数理论与实验 rms 偏差仅约 \(30\) keV，\(c\) 系数约 \(9\) keV；
- pf 壳 \(b\) 系数 rms 偏差约 \(95\) keV（排除上壳区 \(A=59,61,63\) 后为 \(55\) keV），\(c\) 系数约 \(25\) keV；
- **配对交错（Pairing staggering）**：\(c\) 系数在 \(A=4n+2\) 多重态中系统性高于 \(A=4n\)；\(b\) 系数在 \(A=4n+1\) 与 \(A=4n+3\) 中呈现反相振荡；
- 图 2 与图 3 证明：这种交错源于质子–质子与中子–中子平均配对能的库仑贡献差，且交错振幅随激发能增加而明显衰减，反映了高激发态下两体配对关联的逐步减弱。

### 2. MED 与 TED 对核结构微观机制的高灵敏度

对于 \(T=1\) 多重态，同位旋能级差与 IMME 系数直接相关：

\[
\text{MED}(J) = -2[b(J)-b_0] , \quad
\text{TED}(J) = 2[c(J)-c_0] .
\]

它们沿激发带的演化能够灵敏揭示：

- **核子对转动对齐（Pair alignment）**：当高 \(j\) 质子对或中子对发生科里奥利反冲对齐时，空间波函数重叠改变引起局部库仑能跌落，在 MED/TED 曲线中形成特征弯折；
- **单粒子轨道效应与中子皮**：MED 与质子/中子物质半径差（中子皮）呈线性相关；
- **Thomas–Ehrman 位移**：低角动量轨道（特别是 \(s_{1/2}\)）因缺乏离心势垒，波函数在质子滴线附近向外大幅延展，导致含高 \(s_{1/2}\) 占据的质子富集态能级产生反常压低。

### 3. 等位旋禁戒衰变与 IAS 态混合概率

当母核发生 \(\beta\) 衰变到达子核的等位旋类似态（IAS）时，由于同位旋选择规则，
从 IAS 发射质子（\(\Delta T=1/2\)）、\(\alpha\) 粒子（\(\Delta T=0\)）属于等位旋禁戒过程。

实验观测到此类禁戒发射直接证明了 IAS 态中存在非类似态的同位旋杂质混合。在二态混合近似下：

\[
|{\rm IAS}\rangle \approx \sqrt{1-x^2}\vert T\rangle + x\vert T-1\rangle , \quad
x \sim \frac{\langle T \vert \hat V_{\rm INC} \vert T-1\rangle}{\Delta E} .
\]

测得的质子或 \(\alpha\) 部分衰变宽度允许反演同位旋混合矩阵元 \(\langle V_{\rm INC} \rangle\)。
然而，理论能级间距 \(\Delta E\) 的几百 keV 不确定度会对混合几率 \(x^2\) 产生巨大扰动，因此提取实验混合强度时必须严格结合直接测量的能级差。

### 4. 超允许 \(0^+\to0^+\) 衰变修正 \(\delta_C = \delta_{C1} + \delta_{C2}\)

在超允许 Fermi 衰变中，实验 \(ft\) 值通过辐射修正与同位旋破缺修正转化为普适的 \(\mathcal{F}t\) 值：

\[
\mathcal{F}t = ft(1+\delta_R')(1+\delta_{\rm NS}-\delta_C) = \frac{K}{2G_V^2(1+\Delta_R)} .
\]

壳模型将同位旋破缺修正分解为两个严格的独立微观贡献：

\[
\delta_C \approx \delta_{C1} + \delta_{C2} :
\]

1. **\(\delta_{C1}\)（构型混合项）**：由于价空间内 INC 哈密顿量引起的 IAS 与同自旋宇称非类似态的组态混合，导致 Fermi 跃迁强度从 IAS 态向外耗散；
2. **\(\delta_{C2}\)（径向重叠不匹配项）**：由于质子与中子单粒子径向波函数在真实自洽平均场（Woods–Saxon 或自洽 Hartree–Fock）中受库仑势与分离能影响而不再完全重合：
   \[
   \delta_{C2} = \frac{2}{|M_F^0|^2}\sum_{\alpha,\pi} \langle f \vert c^\dagger_{\alpha n} \vert \pi \rangle_0 \langle \pi \vert c_{\alpha p} \vert i\rangle_0 (1-\Omega_{\alpha}^\pi) ,
   \]
   其中 \(\Omega_\alpha^\pi = \int_0^\infty R_{\alpha n}^\pi(r) R_{\alpha p}^\pi(r) r^2 dr\) 为依赖于中间态能级的径向重叠积分。

文章在图 5 中总结对比了 SM-WS、SM-HF、RHF-RPA、RH-RPA、DFT 等各类理论计算。
目前只有通过实验单核子分离能和核电荷半径精密校准势参数的 Woods–Saxon 壳模型（SM-WS）能够提供与 CVC 假说自洽且置信度最高的 \(\delta_C\) 值；
DFT 与微观 HF 模型往往给出系统偏小的修正值，提示超出平均场近似的多体关联对径向波函数修正不可或缺。

### 5. 天体物理 \(rp\) 过程质子捕获共振强度

在 X 射线暴和新星核合成的爆发生氢燃烧中，\((p,\gamma)\) 反应率由质子发射阈之上的孤立共振主导：

\[
N_A\langle\sigma v \rangle_{(p,\gamma)} \propto \omega\gamma \exp\left(-\frac{11.605 E_r}{T_9}\right) , \quad
\omega\gamma = \frac{2J_f+1}{2(2J_i+1)}\frac{\Gamma_p\Gamma_\gamma}{\Gamma_{\rm tot}} .
\]

INC 壳模型能够利用测得的中子富集镜像核能级，通过精确的理论 IMME \(b\) 和 \(c\) 系数反演质子滴线核中未知的共振能量 \(E_r\)；
同时，Thomas–Ehrman 效应对弱束缚 \(s_{1/2}\) 质子共振谱因子的剧烈重整化，构成了高精度天体物理反应率评估的关键输入。

## Experimental and Weak-Interaction Analysis Contract

将同位旋破缺壳模型用于实验谱学与弱衰变分析时，必须保持以下证据分层与方法合同：

1. **区分同位旋动力学破缺与态混合**：不能把库仑位移能（能量差）与同位旋态混合（波函数杂质）混淆；
2. **IMME 拟合透明度**：使用二次 IMME 预测未知核质量或共振能时，必须明确标明采用的 \(b\) 或 \(c\) 来源、拟合模型空间及其在已知同中子/同位素多重态中的残差；
3. **MED/TED 机制分离**：不能将 MED 曲线的全部变化简单归结为形变；必须同时考虑单粒子等矢位移、对齐阻塞和库仑多极单极项；
4. **超允许衰变修正的势场依赖性**：计算 \(\delta_C\) 时，必须明确说明是基于实验电荷半径与分离能约束的 Woods–Saxon 势，还是自洽微观场；报告 \(\delta_{C1}\) 与 \(\delta_{C2}\) 的独立分量，不得仅给出一个整体数字；
5. **天体物理共振提取限制**：利用镜像对称性平移谱因子时，必须对弱束缚低 \(\ell\) 轨道（尤其是 \(s_{1/2}\)）施加 Thomas–Ehrman 修正，保留波函数延展导致的展宽或压低。

## What It Cannot Establish Alone

- 单个镜像能级对的能量差不能独立分离出短程核电荷相关力（Class II/III）与经典长程库仑力；
- 纯壳模型模型空间对角化给出的等位旋纯态无法涵盖超出主壳层的径向解耦；\(\delta_{C2}\) 必须外接微观/唯象径向势场；
- 实验上观测到很小的禁戒衰变分支，若缺乏精确的初末态能级差 \(\Delta E\)，不能直接换算为可靠的哈密顿量混合矩阵元；
- 现有各类理论对 \(\delta_C\) 的计算值仍存在显著分散（图 5），不能声称超允许衰变中的同位旋破缺理论不确定度已经完全闭合；
- 本文涉及的轻核与中重核同位旋破缺结论不能直接套用到 A≈130 质量区重核的三轴手征性或摆动运动，但其中的电荷对称性破缺与同位旋多极展开提供了处理非轴对称核芯电磁算符的严格参考。

## Knowledge Impact and Learning Decision

Smirnova 的文章为 Wiki 补齐了壳模型在“同位旋守恒与破缺”方向上的现代标准处理流程：
它将 Bentley 的 MED/TED 高自旋经验分析、Nolen–Schiffer 反常的微观起源、\(\beta\) 衰变的 CVC 检验与 CKM \(V_{ud}\) 提取，
以及天体物理氢燃烧共振统一在同一个哈密顿量球张量分解框架下。

本单元完成 Smirnova 综述主文本与关键图表的核读。其引用的具体 ab initio 计算细节与生产级代码不单独计入。

## Evidence and Locators

- Article pp.352–356 / physical PDF pp.272–276：同位旋代数、不可约球张量展开、弱相互作用与电磁选择规则式 (10)–(12)；
- Article pp.356–358 / physical PDF pp.276–278：Henley–Miller 四类核力、Nolen–Schiffer 反常、\(\chi\text{EFT}\) 层次与微观有效相互作用；
- Article pp.358–363 / physical PDF pp.278–283：INC 相互作用拟合、IMME 二次式、\(b\) 与 \(c\) 系数图 1、配对交错图 2–3、MED/TED 与 Thomas–Ehrman 位移；
- Article pp.363–367 / physical PDF pp.283–287：库仑位移法预测质量、扩展 IMME 式 (19)、IAS 等位旋禁戒衰变图 4 与二态混合；
- Article pp.367–374 / physical PDF pp.287–294：超允许 Fermi 衰变 \(\mathcal{F}t\) 式 (29)、\(\delta_C=\delta_{C1}+\delta_{C2}\)、图 5 各模型发散对比、图 6 径向重叠积分、镜像核 GT 衰变不对称性；
- Article pp.374–376 / physical PDF pp.294–296：天体物理 \(rp\) 过程质子捕获共振强度式 (35)–(36) 与 Thomas–Ehrman 影响；
- 已渲染核对 PDF pp.272、274、277、280、281、286、289、291、294。

## Sources

- [[book-nuclear-shell-model-70-years]]
- [[isobaric-multiplet-med-ted-highspin-contract]]
- [[nolen-schiffer-anomaly-and-charge-symmetry-breaking]]
- [[beta-decay-phase-space-log-ft-and-cvc-unitarity]]
- [[brown-shell-model-dripline-continuum-outposts-contract]]
- [[utsuno-shell-evolution-force-decomposition-contract]]
