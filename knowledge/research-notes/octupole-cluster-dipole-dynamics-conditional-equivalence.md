---
type: research-note
title: "八极集体坐标与 α 团簇相对运动：偶极相消和可证伪边界"
aliases: [octupole cluster dipole conditional equivalence, Day26 cluster E1 E3 geometry]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra, bernard-2016-144ba-sccm-octupole]
created_from: Day26 analytic point-cluster and parity/GDR mixing study
promotion_target: octupole-and-rare-electromagnetic-decay
tags: [octupole, alpha-clustering, E1, E3, parity-doublet, IVGDR, evidence-boundary]
---

# 八极集体坐标与 α 团簇相对运动的条件对应

## Research Trigger

本笔记保留一个跨质量区可复算的反向检验：同样大的电八极跃迁可以伴随严格为零或很小的电偶极跃迁，但不能据此认定 α 团簇、静态梨形或 GDR 干涉。数值与输入在 [解析基准脚本](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/octupole-vs-cluster-dipole-dynamics-018.py) 和 [结构化结果](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/octupole-vs-cluster-dipole-dynamics-018.json)。这是解析点团簇与二能级示例，不是反对称化微观计算或实验拟合。

## Grounded Evidence

实验锚点分开保留：[[bucher-2016-144ba-direct-octupole]] Table I 给 $^{144}$Ba 的 $0^+\leftrightarrow3^-$ 矩阵元 $0.65^{+0.17}_{-0.23}\ e\mathrm{b}^{3/2}$ 和向下 $B(E3)=48^{+25}_{-34}$ W.u.；[[bucher-2017-146ba-direct-octupole]] PDF p.3 Table I 给 $^{146}$Ba 对应 E3 中心 $0.65\ e\mathrm{b}^{3/2}$、$B(E3)=48^{+21}_{-29}$ W.u. 及 $0^+\leftrightarrow1^-$ E1 幅度 $0.000223\ e\mathrm{b}^{1/2}$。后者的 E1 主要受先前寿命和分支约束，且该论文的 SCCM E1 计算幅度 $0.00474\ e\mathrm{b}^{1/2}$ 与实验打印中心相差约 21 倍，不能说绝对 E1 已精确复现。[[gaffney-2013-pear-shaped-rn-ra]] Table 1 给 $^{224}$Ra 的 $0^+\to3^-$ E3 矩阵元 $940(30)\ e\mathrm{fm}^3$；其 Fig.5 的模型比较并不支持把所有 Rn/Ra 八极趋势自动归给单一团簇模型。[[bernard-2016-144ba-sccm-octupole]] 的投影与坐标混合是模型证据，不是另一组独立测量。

## Provisional Reasoning

### 质心几何的严格部分

令两子团簇质量数、质子数为 $(A_1,Z_1)$ 和 $(A_2,Z_2)$，$A=A_1+A_2$，$\mathbf R=\mathbf r_1-\mathbf r_2$。在质心系 $A_1\mathbf r_1+A_2\mathbf r_2=0$，所以 $\mathbf r_1=A_2\mathbf R/A$、$\mathbf r_2=-A_1\mathbf R/A$。沿相对轴的内禀偶极为

$$D_0^{\rm cluster}=e(Z_1r_1+Z_2r_2)=e\frac{Z_1A_2-Z_2A_1}{A}R.$$

若 $Z_1/A_1=Z_2/A_2$，分子严格为零，故在**固定电荷与质量质心、两点团簇且未加入内部极化**的模型中 $D_0^{\rm cluster}\equiv0$，与 $R$ 大小无关。$^{16}$O+$\alpha$ 的两个 $Z/A$ 均为 $1/2$，因此 $^{20}$Ne 是严格零偶极但非零八极的解析反例；它不等于真实核的全部 E1 跃迁均为零。有限尺寸、内部同位旋极化、交换与反对称化会打破点团簇近似。

同一质心约定下，完整核算符 $D_z=e(N/A)\sum_p z_p-e(Z/A)\sum_n z_n=eNZ(R_{p,z}-R_{n,z})/A$。把核密度恰好分成上述两个固定荷质比团簇时，该式与点团簇公式代数等价；在平均场中，轨道占据和极化通过 $R_p-R_n$ 改变同一 E1 算符的矩阵元。**相消的算符条件相同，产生质心位移的动力学过程并未因此相同**。BU17 PDF pp.4–5 的中子轨道占据解释属于 SCCM 模型层，三个 $v^2$ 值不足以恢复逐轨道有符号贡献或相消百分数。

对轴上点团簇，$\mathcal M(E3,0)=e\sqrt{7/(4\pi)}c_3R^3$，$c_3=Z_1(A_2/A)^3-Z_2(A_1/A)^3$。采用 $K=0$ 转子约定 $Q_3=\sqrt{16\pi/7}\mathcal M(E3,0)=2ec_3R^3$，于是 $B(E3;0^+\to3^-)=7Q_3^2/(16\pi)$。这是同一实验室多极算符的条件匹配，不表示两模型的态空间、惯量或势能面相等。

| 假定两点分解 | $c_1=D_0/(eR)$ | $c_3=Q_3/(2eR^3)$ | 结论 |
| --- | ---: | ---: | --- |
| $^{20}$Ne $=^{16}$O+$\alpha$ | 0 | −0.9600 | 点团簇 E1 恒零而 E3 可非零 |
| $^{144}$Ba $=^{140}$Xe+$\alpha$ | −0.4444 | −1.8368 | 系数只是几何，不是团簇存在证据 |
| $^{146}$Ba $=^{142}$Xe+$\alpha$ | −0.4658 | −1.8390 | 若孤立点团簇独占 E1/E3，会预言较大的偶极 |
| $^{224}$Ra $=^{220}$Rn+$\alpha$ | −0.4286 | −1.8943 | Gaffney E3 可作几何条件对照 |
| $^{226}$Ra $=^{222}$Rn+$\alpha$ | −0.4425 | −1.8952 | 本轮没有直接源支持其 E1/E3 数值比较 |

把 BU17 的两个**向上**矩阵元按 $1\mathrm b^{1/2}=10$ fm、$1\mathrm b^{3/2}=1000$ fm³换算，$B(E1;0\to1)=4.973\times10^{-6}\ e^2\mathrm{fm}^2$，$B(E3;0\to3)=4.225\times10^5\ e^2\mathrm{fm}^6$；其比为 $1.177\times10^{-11}\ \mathrm{fm}^{-4}$。比值带量纲，也依赖跃迁方向与初态自旋，不能直接当普适形变指标。$K=0$ 转子换算给 $|D_0|=0.00456\ e\mathrm{fm}$、$|Q_3|=1742\ e\mathrm{fm}^3$；前者无符号信息。

若**另外强加**“所有 E3 来自一个权重为 1 的点团簇跃迁通道”以拟合 $^{146}$Ba 中心 E3，则 $R=7.795$ fm，预言 $|D_0^{\rm point}|=3.630\ e\mathrm{fm}$。在这个**已固定 $R$** 的条件下，用一个共同跃迁重叠权重 $w$ 消去 E1，得到 $w=0.001257$；相同的 $w$ 会使 E3 强度比观察中心小约 $6.33\times10^5$ 倍。因此，在核尺度局域距离和相同单通道权重的额外条件下，这个点团簇版本不能同时解释两中心值。

若 $R$ 与 $w$ 都自由，则 $D_{\rm obs}=w e|c_1|R$、$Q_{3,\rm obs}=2we|c_3|R^3$ **确有代数共同解**：$R=219.84$ fm、$w=4.46\times10^{-5}$。采用示意核接触尺度 $1.2(142^{1/3}+4^{1/3})=8.17$ fm，所需距离约为其 $26.9$ 倍，脱离局域核内团簇运动的模型域。这不是全模型无解定理：非局域连续谱、内部极化或额外构型的振幅改变前提。这里的 $w$ 只是假设 E1 与 E3 共用的**跃迁矩阵元重叠权重**；它不等于下文定义的归一化通道概率 $S_\alpha$，也不是可直接测量的反应谱因子。对 $^{224}$Ra，单以 Gaffney Table 1 E3 匹配得到 $R\approx8.73$ fm 和点团簇 $|D_0|\approx3.74\ e\mathrm{fm}$；本轮不将此几何值当实测偶极。

## 宇称谱与动力学映射的范围

对自旋为零的两个团簇，相对轨道 $L$ 给 $J=L$、宇称 $(-1)^L$；Pauli 允许的径向通道和势阱决定 $0^+,1^-,2^+,3^-,\ldots$ 是否真的出现及能距。取两个局域反射伙伴阱，隧穿形成宇称本征态；最小示例 $E_+(I)=aI(I+1)$、$E_-(I)=aI(I+1)+\epsilon$。奇自旋能级相对于相邻偶自旋平均的位移为 $\delta E(I)=\epsilon-a$。脚本用 $a=12$ keV、$\epsilon=300$ keV 得到 $288$ keV，纯属示例；常数位移本身不能证明双阱，真实 $I$ 依赖的惯量与隧穿需独立拟合。

平均场的 $\beta_3$ 集体哈密顿量与团簇 $R$ 动力学只有在坐标映射 $\beta_3=f(R)$、量子度规/惯量、势、边界条件、宇称投影和 E1/E3 **跃迁核**均匹配时才可称为同一有效一维理论。相同的 $B(E1)$ 或 $B(E3)$ 是少数矩阵元相同，不能推出该映射。单阱谐振八极声子的 $3^-$ 激发及多声子结构也不能直接与交错宇称转子逐态等同；分子团簇通道还受 Pauli 禁止态、反对称化、内部激发和连续谱约束。平均场中近费米面的相反宇称 $\Delta l=\Delta j=3$ 轨道相干可增强八极响应，但它既非局域 $\alpha$ 形成的充分条件，也不排斥其混合。

若 $S_\alpha$ 被**定义为归一化态投影到明确正交化 α 通道的概率**，则 $0\le S_\alpha\le1$。这是本轮能为 $^{20}$Ne、$^{144,146}$Ba 和 $^{224,226}$Ra 共同给出的物理上界；本轮来源没有同一约定下这些核的实测 $S_\alpha$。反应模型提取的 spectroscopic factor、α 衰变预形成因子和这个投影概率并非天然同一量。仅凭 E1/E3，其他通道的有符号振幅可相消或相长，不能给 $S_\alpha$ 的非平凡上下界。

## IVGDR 低能拖尾的反向检验

只有当低能态和 IVGDR 组态**相干混合成同一个末态**时，低能 E1 幅度才可以写成 $D_{\rm low}'=D_{\rm low}\cos\theta-D_{\rm GDR}\sin\theta$，其中 $\tan2\theta=2v/(E_{\rm GDR}-E_{\rm low})$。脚本中的 $1/13$ MeV、$D_{\rm low}/D_{\rm GDR}=0.1$、$v=1.212$ MeV 构造出严格零点，只证明相消在数学上可能；它们不是 Ba/Ra/Ne 的实测参数。IVGDR 强度函数低能尾部的**非相干外推**不能直接从某个离散跃迁的 $B(E1)$ 中相减。能量加权和规则约束总强度，不能确定某个低能态的相对相位。

| 判据层 | 可据此陈述 | 仍需的证伪量 |
| --- | --- | --- |
| 1. 实验观测 | 同一核的能级宇称、寿命/分支、同方向 $B(E1)$ 与直接 $B(E3)$，记录误差和拟合相关；BU16/BU17 的大 E3 与 BU17 小 E1 已构成此层对照 | 精确 E1 符号、独立强度约束与同自旋序列 |
| 2. 有效动力学 | 同时比较 $\delta E(I)$、转动惯量、多条 E1/E3/E2 跃迁及核反应/α 通道信息；检验点团簇与 $\beta_3$ 模型是否可在**同一参数集**解释 | 若模型需在不同跃迁逐条重设 $R$、$S_\alpha$ 或算符，则该版本失败 |
| 3. 微观机制 | 反对称化 α 通道范数及反应/衰变约束，对照 SCCM 占据与有符号投影跃迁核；IVGDR 假说另需混合与相位证据 | 若无可匹配的混合态或相对相位，GDR 相消解释不成立；若完整 α 通道计算与反应观测冲突，团簇主导解释不成立 |

依据独立验证工件 `octupole-ivgdr-mixing-cancellation-071.py/json`：
以 $^{146}\text{Ba}$ 为例（$E_{\text{GDR}} \approx 14.81\text{ MeV}$, $E_{\text{oct}} = 1.05\text{ MeV}$），由于同位旋矢量巨偶极共振耗尽了 TRK 能量加权总和规则，其本征偶极跃迁矩阵元高达 $D_{\text{GDR}} \approx 6.44\ e\text{ fm}$。
在低激发八极态与 IVGDR 的相干双态混合模型中：
- 仅需微小的两态耦合矩阵元 $V_{\text{mix}} \approx 0.14\text{ MeV}$（对应 IVGDR 态的概率混杂仅 $P_{\text{GDR}} \approx 0.01\%$，即万分之一量级）；
- 所诱发的破坏性干涉偶极位移即可达到 $-0.065\ e\text{ fm}$，完全抵消低能单粒子壳极化矩，使净内禀偶极矩塌缩至接近零；
- 这在微观巨共振耦合图像上证明了极小的概率混杂足以借助巨共振的巨大矩阵元杠杆抹去低能偶极辐射，从而与中子轨道反向极化机制形成微观等价互补。

## Self-audit 与待解决问题

- 来源直接报告：BU16/BU17 的 Ba E3、BU17 的 E1 表列幅度、GA13 的 Ra E3。它们属于不同实验谱系；BE16 SCCM 与 BU17 解释共享模型链，不能算第二次实验。
- 解析恒等式：质心 E1 零点、点团簇 E3 系数、转子约定和二态混合零点。它们只在列明模型内成立。
- 条件推断：以 E3 匹配点团簇距离后的 E1 不相容、$S_\alpha$ 不可辨识、GDR 相位需求。未把任何示例参数标成实验值。
- 下一步需要同约定的 α 通道范数/反应数据、可核验的同核 E1 符号或干涉信息、以及同一理论计算的 E1/E3/能谱联合协方差；在此之前保留团簇、平均场及混合解释的竞争性。

## Assumptions

点团簇携带整数 $A_i,Z_i$、内部电荷与质量中心重合；两态混合例中的能量、偶极幅度与耦合常数均为自设参数。$D_0,Q_3$ 从实验跃迁矩阵元的换算另假定轴对称 $K=0$ 转子约定。

## Competing Explanations

强 E3 可以来自软八极相关、局域反射不对称、α 通道与非团簇构型的混合；小 E1 可以来自荷质比相等、质子/中子密度相消或特定末态相干混合。现有数值不对这些机制作排他排序。

## Transfer Conditions

跨核只能迁移算符恒等式与单位约定。若迁移 $R$、$S_\alpha$、GDR 混合或能级位移，必须重新给出同核、同跃迁方向、同模型空间的输入和误差。

## Failure Conditions

当内部极化、反对称化、非正交通道或多组态幅度不可忽略时，两点电荷模型失效；当低能态与 IVGDR 无同末态相干混合证据时，二态相消示例不能用于实验解释。

## Falsification or Reverse Tests

用同一参数组联合预言 E1、E3、宇称谱与反应/α 通道观测。若在预先声明的核尺度 $R$ 范围和共同跃迁权重下无法同时再现 E1/E3，孤立未极化点团簇的该版本失败；若加入额外有符号幅度，须由独立测量约束其大小和相位。

## Open Questions

是否可取得同一约定下的归一化 α 通道投影或转移反应约束，以及能识别 E1 相位的观测？对 Ba/Ra 的完整投影算符核是否能同时解释绝对 E1 与 E3？

## Human Review

本轮为 Codex 解析推导与已列原件的 self-audit；`review_status: unreviewed`，无用户人工审核记录。

## Promotion or Rejection History

2026-10-28：建立 provisional 笔记。待微观通道和同核联合证据出现后再评估晋升；目前未晋升、未拒绝。
