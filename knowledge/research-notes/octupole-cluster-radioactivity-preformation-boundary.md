---
type: research-note
title: "八极关联与重核团簇放射性：预形成、颈缩与最小作用量的微观联系及边界"
aliases: [octupole cluster radioactivity preformation boundary, beta3 beta5 beta7 cluster emission]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [nndc-ra-th-cluster-decay-adopted, warda-2011-actinide-cluster-radioactivity-gogny, denisov-2013-multidimensional-cluster-radioactivity, bernard-2016-144ba-sccm-octupole, bucher-2017-146ba-direct-octupole]
created_from: Day26 cluster-radioactivity microscopic follow-up
promotion_target: octupole-mr-amr-evidence-gradient
tags: [octupole, cluster-radioactivity, preformation, beta3, beta5, beta7, neck, GCM, WKB, E1-cancellation, actinides]
---

# 八极关联与重核团簇放射性

## Research Trigger

八极形变与团簇放射性共享**质量不对称、表面局域化和颈缩**这些集体坐标。反射不对称的多维路径可使原子核较容易演化到轻团簇—重子核组态，动态形变也可降低部分势垒。但是，低能大 $B(E3)$、基态非零 $\beta_3$ 或小 $D_0$ 都不直接测得团簇预形成概率 $P_{\rm cluster}$；$\beta_5,\beta_7$ 的作用还受符号、耦合、配对、壳效应及惯性支配，不存在已由本轮原文证实的普适“促进百分数”。

题设中的两个Th基准必须区分：已取得来源支持 $^{228}$Th$\to{}^{208}$Pb+$^{20}$O 的实测团簇分支；$^{226}$Th在Warda–Robledo原文的实验比较则是 **$^{18}$O+$^{208}$Pb的部分半衰期下限**，不是已正测的 $^{20}$O+$^{206}$Pb。该论文Table I列 $\log_{10}[T_{1/2}(^{18}{\rm O})/{\rm s}]>16.76$，计算为17.31。本轮取得的NNDC $^{226}$Th Adopted表也没有给出 $^{20}$O 的正测分支，故不能为题设补写一个实验中心值。来源：[[nndc-ra-th-cluster-decay-adopted]]、[[warda-2011-actinide-cluster-radioactivity-gogny]]。

## Grounded Evidence

若评价给出百分数 $\%c$，无量纲分支为 $b_c=(\%c)/100$，团簇部分半衰期为

\[
 T_{1/2}^{(c)}=\frac{T_{1/2}^{\rm total}}{b_c}.
\]

下面用NNDC各核Adopted基态字段，年份转换声明为1 y=365.25 d。括号误差保留来源打印值；表中部分半衰期为中心值的算术派生，并非重新测量。

| 通道 | 总 $T_{1/2}$ | 评价团簇百分比 | 无量纲 $b_c$ | 派生 $T_{1/2}^{(c)}$ / s | locator |
|---|---:|---:|---:|---:|---|
| $^{222}$Ra$\to{}^{208}$Pb+$^{14}$C | 33.6(4) s | $3.0(10)\times10^{-8}\%$ | $3.0(10)\times10^{-10}$ | $1.120\times10^{11}$ | NNDC222Ra PDF2, ground state |
| $^{224}$Ra$\to{}^{210}$Pb+$^{14}$C | 3.6316(23) d | $4.0(10)\times10^{-9}\%$ | $4.0(10)\times10^{-11}$ | $7.844\times10^{15}$ | NNDC224Ra PDF1, ground state |
| $^{226}$Ra$\to{}^{212}$Pb+$^{14}$C | 1600(7) y | $3.2(16)\times10^{-9}\%$ | $3.2(16)\times10^{-11}$ | $1.578\times10^{21}$ | NNDC226Ra PDF1, ground state |
| $^{228}$Th$\to{}^{208}$Pb+$^{20}$O | 1.9116(16) y | $1.13(22)\times10^{-11}\%$ | $1.13(22)\times10^{-13}$ | $5.339\times10^{20}$ | NNDC228Th PDF1, ground state |
| $^{226}$Th$\to{}^{208}$Pb+$^{18}$O | — | 本轮未取得正测分支 | — | $>5.754\times10^{16}$ | Warda2011 PDF13 Table I；原实验引用链 |
| $^{226}$Th$\to{}^{206}$Pb+$^{20}$O | — | 本轮未建立正测基准 | — | 不填造值 | acquired-data boundary |

三个Ra同位素的14C部分半衰期跨越约10个数量级，而224Ra、226Ra分支的中心相近；不能只依据某个核有更强低能八极关联来排列其团簇寿命。对子核的壳闭合、衰变Q值、质子/中子转移、配对和作用量必须同时考虑。这些数据有共同实验谱系，不能把NNDC、Warda和后续综述的转引当成三次独立测量。评价版本和来源NSR码见 [[nndc-ra-th-cluster-decay-adopted]]。

## Provisional Reasoning

常见预形成模型写成

\[
 \lambda_c=\nu_c P_0 P_{\rm out},\qquad
 P_{\rm out}\simeq e^{-2S_{\rm out}},\qquad
 S=\frac1\hbar\int ds\sqrt{2B_{\rm eff}(s)[V(s)-E]}.
\]

$\nu_c$是撞击频率，$P_0$是给定模型的内部形成因子，$P_{\rm out}$是从指定匹配面出发的势垒穿透率。一次半衰期测量只约束乘积 $\nu_cP_0P_{\rm out}$，不能独立求出三个因子。若把全路径作用量划分为 $S=S_{\rm in}+S_{\rm out}$，内部代价可以被写作 $P_0\sim e^{-2S_{\rm in}}$；改变匹配面或势垒定义就会重新分配所谓“预形成”与“穿透”代价。

Denisov2013写 $T_{1/2}=\ln2/[\nu S T(Q)]$，但在其采用的密度ansatz中**设 $S=1$**，通过形变、壳修正及多维惯性描述内部重排与外部隧穿。Warda2011则沿Gogny-HFB超非对称裂变路径计算全作用量，没有独立输出一个实验测得的 $P_0$。两者可在不同参数化中描述同一衰变率；不能把它们的“1”和其他模型的“小 $P_0$”当成直接物理矛盾。来源：[[denisov-2013-multidimensional-cluster-radioactivity]] Eqs21–31；[[warda-2011-actinide-cluster-radioactivity-gogny]] Eqs2–7。

在微观通道语言下，需要构造反对称化片段态的重叠

\[
 \mathcal F_c(r)\sim\left\langle
 \mathcal A\{\Phi_d\Phi_cY_\ell(\hat r)\}\middle|\Psi_P\right\rangle,
\]

并处理Pauli交换的norm kernel、通道正交化和边界条件。只有定义清楚的通道投影/形成振幅才能与“团簇概率”联系；非正交GCM中 $|f(q)|^2$ 不能直接作 $P_0$。R-matrix形式 $\Gamma_c=2P_\ell(a)\gamma_c^2(a)$同样依赖匹配半径 $a$；具有物理可比性的是一致处理后宽度，单独的 $P_0$ 或约化宽度不是无约定的实验观测。

## 3. 八极与高阶奇形变如何参与局域化和颈缩

### 3.1 从软梨形到超非对称裂变不是同一个小振幅问题

Warda2011的224Ra基态给出 $\beta_2\simeq0.18$、$\beta_3\simeq0.14$、$Q_{20}=8.3$ b、$Q_{30}=4.2$ b$^{3/2}$。其团簇通道在更大 $Q_{30}$ 发展出14C样小片段和Pb样大片段，并在 $Q_{30}\simeq28$ b$^{3/2}$ 的颈缩区域连续连接单体与双片段解；比较的颈密度约0.09 fm$^{-3}$，约4.9个核子从颈重分配到片段。这里的“片段在颈裂前已出现”属于自洽密度分析，不是对基态中一个现成14C实体的独立探测。Pb样闭壳结构还必须与实际片段粒子数区分：224Ra发出14C后的子核是210Pb，只有222Ra的14C通道严格得到208Pb。

大 $Q_{30}$ 可用作碎片质量不对称的有效坐标，但不能把其值按小振幅表面展开的同一个固定 $\beta_3$ 理解。二维 $(\beta_2,\beta_3)$ 的低能SCCM基底若没有显式延伸到颈缩和碎片通道，就不具备直接预测团簇衰变宽度的态空间。来源：[[warda-2011-actinide-cluster-radioactivity-gogny]] PDF5、12–13；低能SCCM对照见 [[bernard-2016-144ba-sccm-octupole]]。

### 3.2 为什么 $\beta_5,\beta_7$ 会有用，但不能宣布普适促进

轴向表面可写作

\[
 R(\theta)=cR_0\left[1+\sum_\lambda\beta_\lambda Y_{\lambda0}(\theta)\right].
\]

$\beta_3$控制大尺度反射不对称，$\beta_5,\beta_7$提供更局域的极端和颈部曲率自由度，使同一个大尺度质量不对称可以有不同的颈厚、尖端半径和局域密度。高阶奇形变还与 $\beta_3$ 允许反射偶的交叉项，例如 $C_{35}\beta_3\beta_5$ 和 $C_{37}\beta_3\beta_7$；它们可以改变最低谷方向，而不是只给既有梨形统一增加一个比例因子。

一个严格但局部的变分结论是：若 $\mathbf q_h=(\beta_5,\beta_7)$ 的稳定曲率矩阵 $C_h$ 正定，展开

\[
 V=\frac12C_{33}\beta_3^2+\beta_3\mathbf c^T\mathbf q_h
   +\frac12\mathbf q_h^TC_h\mathbf q_h
\]

并允许高阶自由度松弛，就有

\[
 \mathbf q_h^*=-C_h^{-1}\mathbf c\,\beta_3,
 \qquad C_{33}^{\rm eff}=C_{33}-\mathbf c^TC_h^{-1}\mathbf c\le C_{33}.
\]

这说明**在同一模型、同一约束和稳定局部展开下，增加可变形状自由度不会使最低势能更高**。然而衰变由作用量决定：松弛可能改变 $B_{\rm eff}$、路径长度、壳占据和零点能，最低能量路径未必等于最低作用量路径，故不能推出总半衰期必以固定比例缩短。这一推导是本任务的机制推断，不是所读文献已测出 $\beta_5$ 或 $\beta_7$ 的数值。

两个点状质量片段也展示了为何高阶奇矩天然伴随团簇几何。若轻、重片段质量为 $A_c,A_d$，$A=A_c+A_d$，分离 $R$，则质心系质量多极矩的轴向几何部分为

\[
 q_\lambda(R)\propto
 \left[A_c\left(\frac{A_d}{A}\right)^\lambda
 +(-1)^\lambda A_d\left(\frac{A_c}{A}\right)^\lambda\right]R^\lambda.
\]

$\lambda=1$恰为零，而不对称片段的 $\lambda=3,5,7$一般非零。它说明片段化几何不只含一个八极坐标；却不意味着真实重叠核的所有高阶矩可从两个点片段精确恢复。在靠近颈裂的巨大形变下，应直接检查密度、颈算符和片段粒子数，而不依赖截断球谐表面展开。

### 3.3 穿透率的促进机制与量纲

尖端朝向的伸长可以增大接触距离、降低部分Coulomb/核势垒；子核壳闭合可降低相关片段谷的能量。对给定有效路径，小扰动满足

\[
 \delta S=\frac1\hbar\int ds\,
 \frac{\delta[B_{\rm eff}(V-E)]}{\sqrt{2B_{\rm eff}(V-E)}},
 \qquad \delta\ln T_{1/2}\simeq2\,\delta S,
\]

另需处理路径和转折点的变化。这里 $S$无量纲，势能下降和惯性下降都可缩短寿命，但符号相反的变化可能抵消。配对通常同时改变轨道占据和惯性，因此“形变降低势垒”与“预形成概率增加”不应被当成同一个已测机制。

Denisov2013在动态片段形变的多维模型中得到228Th20O计算 $5.0\times10^{20}$ s，接近其引用实验 $(5.29\pm1.01)\times10^{20}$ s；但模型使用惯性增强系数，且设形成因子 $S=1$。Warda2011的对应log10计算为19.53，相对本轮评价换算20.727短约1.20个数量级；222Ra、224Ra、226Ra的对应计算比评价中心分别短约2.15、0.83、2.22个数量级。成功描述尺度和偏差都应记录，不能借单个半衰期拟合认证唯一微观路径。

## 4. 团簇模型与SCCM/GCM在E1相消上的交集

在质心系，把轻、重片段暂视为固定荷质比的非重叠点团簇，有

\[
 D_0^{\rm rel}=e\frac{Z_cA_d-Z_dA_c}{A}R
 =e\left(Z_c-\frac{Z A_c}{A}\right)R.
\]

这个几何有效电荷可以因为轻、重片段 $Z/A$接近而很小，虽然 $Q_{30},Q_{50},Q_{70}$仍很大。按下列约定，$R$从重片段指向轻片段：

| 几何分解 | $D_0/(eR)$ | 物理含义 |
|---|---:|---|
| 222Ra=208Pb+14C | +0.45045 | 有限相对运动偶极有效电荷 |
| 224Ra=210Pb+14C | +0.50000 | 系数随子核同位素改变 |
| 226Ra=212Pb+14C | +0.54867 | 不能仅用相同14C标签假定相同E1 |
| 228Th=208Pb+20O | +0.10526 | 荷质比接近，几何E1有效电荷较小而高奇矩非零 |
| 226Th=206Pb+20O（仅几何比较） | +0.03540 | 更小的有效电荷不构成该衰变已被测到或P0较大的证据 |
| 226Th=208Pb+18O（下限通道） | +0.83186 | 与20O通道的几何E1完全不同 |

完整核的质心修正E1算符则为

\[
 \hat D_z=e\frac{N}{A}\sum_pz_p-e\frac{Z}{A}\sum_nz_n
 =e\frac{NZ}{A}(R_{p,z}-R_{n,z}).
\]

**共同点是同一个质心修正电偶极算符**：片段语言把它写成相对坐标的有效电荷，自洽平均场把它写成质子—中子密度与轨道极化。真正的SCCM跃迁需两套宇称/角动量投影态之间的非对角过渡密度和有符号核；单个内禀密度的 $D_0$ 不是完整的实验E1矩阵元，几个$v^2$占据也不能重构全部相位。224Ra或Ba的强E3和小E1不自动测得团簇含量。跨表示的质心几何推导见 [[octupole-cluster-dipole-dynamics-conditional-equivalence]]；146Ba的相消证据与模型边界见 [[bucher-2017-146ba-direct-octupole]]。

**不同点是态空间和动力学**：固定14C/Pb片段模型预选了通道；普通HFB/GCM不预设片段，但其有限坐标网格、投影和非正交norm kernel也不自动给出通道形成振幅。要建立两者的定量联系，需要在相同EDF、粒子数投影、Pauli处理和渐近通道边界下，直接计算片段化基底与集体GCM态的重叠及衰变通量。

## Falsification or Reverse Tests

1. 对222/224/226Ra和226/228Th建立一致的 $(Q_{20},Q_{30},Q_{50},Q_{70},q_N)$ 约束网格，$q_N$为颈算符；同时保存质子/中子局域密度、片段粒子数和配对张量。
2. 分别冻结和放开 $Q_{50},Q_{70}$，比较同一 $Q_{20},Q_{30}$ 处的能量、完整惯性张量和最小作用量，避免把最低能量谷误当成最小作用量路线。
3. 用相同匹配半径和Pauli规范构建14C/Pb、18O/Pb、20O/Pb通道形成振幅，检验“高阶奇形变促进P0”是否在不同核、不同片段和不同EDF中保持符号。
4. 对E1做质子/中子过渡密度分解，同时给E3与片段投影重叠；若E1相消而通道重叠不增大，应拒绝“相消是团簇预形成增强的必要标志”。
5. 用真实总半衰期、百分比分支和各channel Q值传播实验与模型不确定度；未取得226Th20O正测前保留限值/待检，不给造出的中心值。

## 证据边界与获取记录

本轮取得NNDC五核Adopted PDF及两篇理论预印本，实际签名、页数、哈希和阅读覆盖载于对应JSON。7份原件已逐文件核验后新增归档至raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/，未覆盖既有文件；未重读每条罕见分支的原始实验论文，未取得生产HFB/GCM代码、通道norm kernels或完整惯性网格。Sawhney–Sharma–Gupta2011的higher-multipole论文仅核验Crossref书目信息，出版社下载403、APS harvest401，不能用未读正文支持beta5/beta7定量增强。**本轮没有实验beta5/beta7值，也没有独立微观P0数值**；这些缺口是研究边界，不转写成确定结论。

## Assumptions

分支换算只采用指数衰变和同一评价对象的总半衰期；年度换算明确为365.25 d。局部高阶形变松弛推导要求给定EDF、同一约束、稳定正定高阶曲率；两点片段几何假定非重叠片段和固定荷质比。WKB仅适用于指定势垒/惯性/边界条件的半经典通道。

## Competing Explanations

同一半衰期可以由较小P0与较大外部穿透率，或S=1且较大内部作用量描述；已有数据不独立区分。低能E3增强可来自软振动/形状混合，团簇路径可来自更大伸长的自洽碎片化；子核闭壳与Q值也可主导同位素寿命趋势。E1小既可来自相对运动的荷质比相消，也可来自内部质子—中子极化，不能优先认定某一个图像。

## Transfer Conditions

跨核素比较需要一致的团簇通道、Q值来源、匹配面、形变归一化、配对处方和惯性定义。将低能SCCM结论迁移到团簇衰变，必须延伸到颈/片段坐标并处理通道norm kernel和渐近边界；局部beta3不能替代完整路径。

## Failure Conditions

若仅通过开放beta5/beta7降低局部势能而没有惯性/路径变化，不能宣称半衰期被定量增强。若罕见分支未正测或只有限值，不得形成实验中心值。若跨模型的P0使用不同的匹配面与Pauli规范，则其数值直接比较失效。

## Open Questions

最有价值的缺口是统一EDF与配对下Q30/Q50/Q70/颈约束的最小作用量、反对称化片段通道形成振幅，以及226Th的18O限值来源和20O实验检索的进一步原始文献核验。当前数据不能给出独立的beta5/beta7增强倍数。

## Human Review

Codex source self-audit；所有新增主张保留needs_review边界，不标为human-reviewed。研究笔记承载长期知识；算术脚本和JSON承载可复算审计。本任务不创建run身份/截止，不推进课程学分。

## Promotion or Rejection History

2026-10-29：建立本受控research-note，纠正226Th20O正测基准的预设，保留beta5/beta7与P0的未决状态；没有将模型解释升级为实验事实。
