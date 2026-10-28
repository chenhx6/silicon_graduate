---
type: research-note
title: "E3能量加权和规则、低能/高能八极共振与跃迁密度边界"
aliases: [e3-ewsr-transition-density-boundary]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra, butler-2020-222-228ra-octupole-evolution]
created_from: Day26 delegated E3-EWSR and transition-density investigation
promotion_target: octupole-correlation
tags: [E3, EWSR, transition-density, RPA, Tassie-model, LEOR, HEOR]
---

# E3能量加权和规则、低能/高能八极共振与跃迁密度边界

## Research Trigger

本轮核验五个核的首个$3^-$态占据E3能量加权总和规则(EWSR)的比例，并把集体表面跃迁密度与微观RPA跃迁密度分开。用户给出的$35/(8\pi)$系数与标准电磁$E3$双重对易子推导不一致，因此同时保留“用户归一化”与“标准尖锐均匀球归一化”两列，避免把系数争议隐藏成数值结果。

## Grounded Evidence

| 核素 | 首个$3^-$输入 | $B(E3;0^+\to3^-)$输入 | 来源与边界 |
|---|---:|---:|---|
| $^{144}$Ba | $E\simeq0.839$ MeV，条件读图/能级链 | $(0.65)^2=0.4225\ e^2b^3$ | BU16 PDF3的$3^-\to2^+$为639.0 keV、Table I给$0^+\to3^-$矩阵元；首态能量需稳定能级locator，保留needs_review |
| $^{146}$Ba | 0.82110(83) MeV | $(0.65)^2=0.4225\ e^2b^3$ | BU17 Table I；ENSDF 146056001记录821.10(83) keV |
| $^{224}$Ra | 0.290352(21) MeV | $(0.940)^2=0.8836\ e^2b^3$ | Gaffney Table 1给$M(E3)=940(30)\ e\mathrm{fm}^3$；ENSDF 224088001给290.352(21) keV |
| $^{226}$Ra | 0.32154(6) MeV | $1.10(11)\ e^2b^3$ | ENSDF 226088001 `BE3=1.10(11)`，固定栏评价字段；不可与矩阵元再平方 |
| $^{208}$Pb | 2.614522(10) MeV | 0.611(9) $e^2b^3$ | ENSDF 208082001；同时给$B(E3)W=33.8(6)$ |

## Provisional Reasoning

### 公式审计

令

$$\hat M_{3\mu}(E3)=e\sum_{p=1}^{Z}r_p^3Y_{3\mu}(\hat r_p).$$

对无自旋相关、动能为$\hat T=\sum_i p_i^2/(2m_N)$的局域哈密顿量，非能权基态双对易子为

$$m_1(E3)=\sum_{\mu=-3}^{3}\sum_n(E_n-E_0)|\langle n|M_{3\mu}|0\rangle|^2
=\frac12\sum_\mu\langle0|[M_{3\mu}^{\dagger},[H,M_{3\mu}]]|0\rangle.$$

局域势与两体坐标势对该交换子不贡献，梯度恒等式给

$$\sum_\mu|\nabla(r^3Y_{3\mu})|^2=\frac{21}{4\pi}r^4.$$

于是

$$m_1(E3)=\frac{21\hbar^2e^2}{8\pi m_N}Z\langle r^4\rangle_p.$$

若把质子分布近似为半径$R_0$的均匀球，$\langle r^4\rangle=3R_0^4/7$，则

$$m_1^{\rm sharp}=\frac{9}{8\pi}\frac{\hbar^2e^2}{m_N}ZR_0^4.$$

因此题目给的$35/(8\pi)$在同一标准下高出$35/9=3.8889$倍。它只有在另行定义了$R_0$或E3算符归一化时才能使用；本回执仍按该系数给出一列，称为“用户公式归一化”，不称标准TRK-E3。

### 首态耗尽百分比

采用$\hbar^2/m_N=41.471$ MeV fm$^2$、$R_0=1.2A^{1/3}$ fm、$1\ b^3=10^6$ fm$^6$。首态贡献为$E_{3^-}B(E3;0\to3^-)$。结果如下：

| 核素 | 首态贡献(MeV $e^2$fm$^6$) | 题目$35/(8\pi)$列 | 标准尖锐球$9/(8\pi)$列 |
|---|---:|---:|---:|
| $^{144}$Ba | 354477.50 | 7.00%* | 27.23%* |
| $^{146}$Ba | 346914.75 | 6.73% | 26.17% |
| $^{224}$Ra | 256555.03 | 0.179% | 0.696% |
| $^{226}$Ra | 353694.00 | 0.244% | 0.948% |
| $^{208}$Pb | 1597472.94 | 1.320% | 5.133% |

*144Ba使用约0.839-MeV首态能量，需后续固定能级原件；其E3矩阵元误差会使用户公式百分比约2.92–11.15%，标准列约11.37–43.34%。146Ba矩阵元误差给用户列约3.23–9.94%，标准列约12.54–38.65%。224Ra取$M=0.940(30)$，标准列约0.652–0.741%；226Ra的BE3=1.10(11)直接作为B，标准列约0.853–1.043%；208Pb标准列约5.058–5.209%。这些只是首态的部分和，不是完整E3 EWSR耗尽。

### LEOR/HEOR与相干性

低能八极态的强度集中来自近费米面异宇称粒子–空穴对的相干叠加，集体RPA的$(X_{ph}+Y_{ph})$同相使表面过渡密度增强；残余相互作用把这部分强度移至低能区域。高能八极共振由更宽的多粒子–空穴空间、速度相关项和残余相互作用共同形成，承载大量能量加权强度。对于电磁$E3$，单个低能态的百分比只能是该算符、该基态和已观测态的部分和；alpha散射常讨论的等标量LEOR/HEOR EWSR不等于质子电磁E3 EWSR，不能直接混用百分比。

### Tassie/Bohr-Mottelson与RPA跃迁密度

表面位移模型令$\delta R(\theta)=\alpha_{3\mu}R_0Y_{3\mu}(\theta)$，得

$$\delta\rho_{\rm Tassie}(r,\Omega)=-\alpha_{3\mu}R_0\frac{d\rho_0(r)}{dr}Y_{3\mu}(\Omega).$$

对尖锐球，$d\rho_0/dr$是表面δ函数；因此E3矩阵元几乎全部位于表面，且径向形状无内部节点。Bohr–Mottelson的集体表面位移与Tassie形式在一阶小振幅下等价；差别来自有限表面扩散、压缩性和高阶形变。

微观RPA写成

$$\delta\rho_{3\nu}(r)=\sum_{ph}\left(X_{ph}^{\nu}+Y_{ph}^{\nu}\right)\langle p\Vert Y_3\Vert h\rangle R_p(r)R_h(r),$$

并分别保留质子/中子分量。它可有内部节点、表面峰位移动、质子–中子异相以及非集体粒子–空穴尾部。与Tassie相符的证据是径向无节点表面集中、多个主导$ph$分量同相及大E3；偏离则表现为节点、内区权重、等标量/等矢量混合或不同自旋态的形状不一致。仅用一条B(E3)不能判定二者吻合；需要径向transition-density、相位与多态E3核。

## Assumptions

EWSR推导采用局域动能、质子点电荷和完整$\mu=-3...3$求和；动量依赖/交换电流、有限核子质量、中心质心修正和两体电流会修正精确值。百分比把每个输入解释为$B(E3;0\to3^-)$；226Ra和208Pb直接使用ENSDF的BE3字段，未再平方。144Ba首态能量是条件输入。

## Competing Explanations

强低能E3可来自静态梨形、软八极振动或对齐八极声子；高能EWSR剩余部分可能在LEOR/HEOR及非集体连续谱中分布。静态/动态区分需要多态E3相对图样、宇称能级、PES/惯性和模型竞争，不能由首态EWSR百分比单独裁定。

## Transfer Conditions

可迁移的是双对易子、Tassie表面形式、RPA过渡密度和部分和下界；不可迁移的是等标量alpha散射EWSR、完整高能共振分数、闭合谱或不同B(E3)方向约定。

## Failure Conditions

若误把$B(E3;3\to0)$当作$B(E3;0\to3)$，会漏乘7；若把226Ra ENSDF的BE3字段当矩阵元再平方，会重复平方；若把用户$35/(8\pi)$当无条件标准TRK系数，所有百分比被系统压低3.889倍。

## Falsification or Reverse Tests

下一步应取得144Ba固定的ENSDF/能级图原件，复核首态能量；对五核构建所有已测$3^-$态的$\sum E B(E3)$部分和，并与同一算符的RPA/QRPA强度分布比较。对至少一核取得径向RPA transition-density，计算其与Tassie模板的加权重叠及节点数，而不是以总B(E3)代替形状比较。

## Open Questions

在自洽微观 QRPA 连续谱计算中，粒子-空穴剩余相互作用的速度依赖与交换项对 E3 EWSR 的同位旋修正因子精确值为多少？Tassie 表面跃迁密度在轻锕系与稀土区核中的微观修正节点分布如何？

## Human Review

Codex source self-audit；未经过用户审核，保持unreviewed。

## Promotion or Rejection History

2026-10-29：纠正任务给出的$35/(8\pi)$系数边界；分开用户归一化和标准尖锐球公式。记录EWSR百分比为单首态部分和，不宣称LEOR/HEOR完整耗尽。

## Next Actions

补足144Ba能级原件、取得直接RPA径向密度和等标量/电磁算符的同约定对账，再更新数值；本轮不推进额外课程学分。
