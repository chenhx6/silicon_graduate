---
type: research-note
title: "225Ac 奇 A 宇称伙伴：评价能级、E1 与阻塞推断边界"
aliases: [Ac225 parity doublet evidence audit, 225Ac octupole parity partners]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [nndc-2022-ac225-adopted-parity-doublet, nndc-2009-ra225-adopted-parity-doublet, nomura-2018-odd-mass-ba-octupole, butler-nazarewicz-1996-intrinsic-reflection-asymmetry]
created_from: Day26 unit028 official ENSDF acquisition
promotion_target: octupole-correlation
tags: [octupole, parity-doublet, odd-A, actinium, E1, evidence-boundary]
---

# $^{225}$Ac 奇 A 宇称伙伴：评价能级、E1 与阻塞推断边界

## Research Trigger

验证奇 A 锕系核是否存在可复核的低能同自旋宇称伙伴，并检查 E1 强度是否足以给出内禀偶极矩。官方 NNDC ENSDF `225089001,225AC` 是本单元唯一新取得的对象。

## Grounded Evidence

评价表给出 $^{225}$Ac 基态 $(3/2^-)$、$40.10(4)$ keV 的 $(3/2^+)$ 态及 $40.09(5)$ keV E1 到基态，$B(E1)=0.00171(15)$ W.u.。同一评价还给出多个 $5/2^\pm$、$7/2^\pm$ 和 $9/2^\pm$ 态，但它们分属 A–D 带，且大多 Jπ 带括号。故可稳妥写成低能评价伙伴与 E1 记录；不能把整个表压缩成单一交替宇称转动带。完整字段和 raw/hash 见 [[nndc-2022-ac225-adopted-parity-doublet]]。

邻近 $^{225}$Ra 评价对象也有低能 A/B 状态和 $B(E1;3/2^-\to1/2^+)=0.00081(20)$ W.u.，但两核的 K、组态和分支结构不同；不能以数值相近直接认证同一微观机制。

## Provisional Reasoning

### 同自旋劈裂

对 $^{225}$Ac 的最低 $3/2^-$–$3/2^+$ 组合，评价中心差按 $E_- - E_+$ 定义为 $-40.10$ keV。其他候选因重复自旋而不唯一：$5/2^-_{A}-5/2^+_{B}=-34.78$ keV、$5/2^-_{C}-5/2^+_{B}=+56.12$ keV；$7/2^-_{A}-7/2^+_{B}=-27.88$ keV、$7/2^-_{C}-7/2^+_{B}=+65.74$ keV。符号交替和组态重复要求先锁定带成员，再谈 $\Delta E(I)$。

### 条件 $D_0$

采用 $R=1.2A^{1/3}$ fm 的 E1 Weisskopf 单位、$B(E1)=0.00171(15)$ W.u. 和轴向强耦合 $K=3/2$。对 $I_i=I_f=3/2$ 的 E1，$|\langle IK,1,0|IK\rangle|^2=K^2/[I(I+1)]=0.6$，由

$$B(E1)=\frac{3}{4\pi}D_0^2\,|\langle IK,1,0|IK\rangle|^2$$

得到 $D_0=0.1688\pm0.0074\ e\,\mathrm{fm}$。这是从评价 B(E1) 做的条件转子反演；它不等于评价直接给出的 $D_0$，也没有确定正负号。若 K 混合、带混合或分支归一变化，结果会改变。

### 阻塞命题

Nomura 2018 的奇 Ba 计算显示低能态 $f$ 玻色子成分与八极态激发能具有状态依赖性，但没有给出可直接迁移到 $^{225}$Ac 的阻塞率。$^{225}$Ac 的单一评价 E1 和多带能级不能单独证明八极准粒子响应被完全阻塞。需要同一 EDF/配对约定下的偶/奇自洽阻塞 QRPA 或 GCM 响应差分。

## Assumptions

评价 Jπ、带标签和 E1 字段按 ENSDF 固定栏读取；原始实验未重读。$D_0$ 推导采用轴向 K=3/2、无额外分支、$R=1.2A^{1/3}$ fm 和标准约化矩阵元约定。

## Competing Explanations

40-keV 伙伴可能来自静态反射不对称、八极振动、粒子–芯耦合或偶然能级靠近。多个相同自旋状态和括号 Jπ 也可能反映组态混合或评价不确定性。E1 增强受质子–中子偶极相消、K 混合和波函数重叠共同影响。

## Transfer Conditions

可迁移的是宇称投影和转子矩阵元公式；$K$、配对隙、$Q_3$、Coriolis 解耦因子及 E1 分支不可从 $^{225}$Ra 或 Ba 直接移植。

## Failure Conditions

若把评价表中的括号 Jπ 当作确定实验指认，或把同自旋不同带的多个差值合并为一条宇称双重带，结论失效。若把条件 $D_0$ 当作直接观测，或把评价 E1 当作新实验，来源层级也失效。

## Falsification or Reverse Tests

获得 $^{225}$Ac 原始寿命、转换电子和分支协方差后，检查 40.09-keV E1 是否由同一 $K=3/2$ 带内波函数描述；再以与偶偶邻核相同的阻塞 EDF/QRPA 计算比较 E1、E3 和同自旋位移。若响应不下降或另一带解释更好，则“完全阻塞”假说被限制。

## Open Questions

原始 1985Is03 $^{225}$Ra β− 数据中的 E1 转换电子归一、$^{225}$Ac 多带波函数和同源八极矩阵元尚未重建；需要先解决评价字段与原实验之间的依赖关系。

## Human Review

本页为 Codex source self-audit，保持 unreviewed；未把 ENSDF 评价提升为 human-reviewed 或论文级原件认证。

## Promotion or Rejection History

2026-10-28：官方取得 $^{225}$Ac Adopted 对象；确认低能 40-keV $3/2^\pm$ 伙伴和 E1 字段，同时撤回“唯一交替宇称带”与“完全阻塞”式过强措辞。

## Next Actions

获取 1985Is03 与 $^{225}$Ac 原始谱学来源，建立带成员、寿命、转换系数和分支协方差表；再做同约定的阻塞响应计算。

## Sources

- [[nndc-2022-ac225-adopted-parity-doublet]]
- [[nndc-2009-ra225-adopted-parity-doublet]]
- [[nomura-2018-odd-mass-ba-octupole]]
