---
type: research-note
title: "四极—八极势能面拓扑的适用边界：轨道近简并、配对与八极响应"
aliases: [beta2 beta3 octupole topology boundary, quadrupole octupole PES topology]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [rodriguez-guzman-2012-sm-gd-quadrupole-octupole, bernard-2016-144ba-sccm-octupole, nomura-2020-ra-th-gogny-d1m-octupole]
created_from: Day26 microscopic follow-up on quadrupole-octupole topology
promotion_target: octupole-mr-amr-evidence-gradient
tags: [octupole, quadrupole-octupole-coupling, beta2, beta3, Gogny, RMF, BCP, pairing, single-particle-structure, model-boundary]
---

# 四极—八极势能面拓扑的适用边界

## Research Trigger

本笔记核验“八极关联严格集中于 $\beta_2\simeq0.15$–$0.20$”这一唯象假说，并把二维 $(\beta_2,\beta_3)$ 势能面、费米面附近异宇称轨道、配对和偶极矩的相消放到同一微观框架中。结论是：$\beta_2\simeq0.15$–$0.20$ 是部分 Ba、Sm/Gd 计算中常见的软化窗口，但不是普适硬阈值，也不能把静态极小、动态八极关联和强 $E3$ 直接等同。

## Grounded Evidence

八极响应是局部单粒子谱、占据、配对和自洽场共同决定的函数。对给定四极约束 $\beta_2$，静态八极坐标的局部势能可写成

\[
 V(\beta_2,\beta_3)=V_0(\beta_2)+\frac12 C_3(\beta_2)\beta_3^2+\frac14 D_3(\beta_2)\beta_3^4+\cdots .
\]

在自洽 HFB/QRPA 语言下，$C_3$ 的软化与静态响应 $\chi_3$ 相关，但二者不是只由一个形变参数给出的常数。一个用于识别控制项的示意准粒子表达式是

\[
 \chi_3(\beta_2)\sim 2\sum_{\mu<\nu}
 \frac{|Q^{(3)}_{\mu\nu}(\beta_2)|^2
 (u_\mu v_\nu+v_\mu u_\nu)^2}{E_\mu(\beta_2)+E_\nu(\beta_2)}.
\]

这里 $Q^{(3)}_{\mu\nu}$ 是约束四极场下的八极矩阵元，$u,v$ 是占据振幅，$E_\mu$ 是准粒子能量。

### 微观势能面与形变对照表

| 体系与模型 | 二维或约束结果 | 微观线索 | 对“固定 $\beta_2$ 窗口”的含义 | locator |
|---|---|---|---|---|
| $^{146-156}$Sm、$^{148-158}$Gd，Gogny-D1M（与D1S作比较） | $N=86,88$ 一带沿 $\beta_3$ 较软；$N=88$ 可有浅的非零 $\beta_3$ 极小；$N\ge90$ 后沿 $\beta_3$ 变陡。图示最低点从约 $\beta_2\sim0.1$ 向 $0.25$–$0.35$ 演化。 | 壳层演化与 $\pi d_{5/2}$–$h_{11/2}$、$\nu f_{7/2}$–$i_{13/2}$ 异宇称近邻结构共同改变，且软势需要动态处理。 | 148Sm 的约 $0.1$ 与150Sm的约 $0.15$ 已落在固定区间外缘；重 Sm/Gd 的四极形变增大后并不产生一个可跨核素复用的硬阈值。 | `tmp/1504.03243.pdf`, PDF pp.4–5, Fig.1; `rodriguez-guzman-2012-sm-gd-quadrupole-octupole.md`, PDF p.4, pp.12,14–15 |
| $^{148,150}$Ba，反射不对称RMF/PK1 | $^{148}$Ba: $\beta_2\approx0.26,\beta_3\approx0.17$；$^{150}$Ba: $\beta_2\approx0.28,\beta_3\approx0.17$。 | $\nu f_{7/2}\leftrightarrow i_{13/2}$、$\pi d_{5/2}\leftrightarrow h_{11/2}$；在八极极小附近出现 $N=88$、$N=94$ 和 $Z=56$ 费米面能隙。 | 直接给出 $\beta_2>0.20$ 仍有强静态八极极小的反例；轨道重排能在较大四极形变下重新打开八极增益。 | `tmp/1008.1888.pdf`, PDF p.4 Table 1, pp.4–6, Figs.2–3 |
| $^{144}$Ba，Gogny-D1S投影GCM/SCCM | 最低点约 $(\beta_2,\beta_3)=(0.2,\pm0.1)$，但 $\beta_3\in[-0.2,0.2]$ 区域较软；对称性恢复与组态混合同时改变谱和跃迁。 | 实验大 $E3$ 与投影集体波函数相容；有限基底、轴对称和缺少推转响应限制静态形状反演。 | $\beta_3$ 非零最低点不能单独证明刚性梨形；$\beta_2\approx0.2$ 是一个实例，不是普适定位器。 | `bernard-2016-144ba-sccm-octupole.md`, PDF pp.2–4, Fig.1, Table I |
| $^{146}$Sm、$^{148,150}$Sm，Gogny-D1S/D1M | $^{146}$Sm 两泛函均 $Q_{30}=0$；$^{148,150}$Sm出现有限八极极小。$^{150}$Sm的平均场八极关联能仅约204 keV(D1S)、105 keV(D1M)。 | $\pi d_{5/2}$–$h_{11/2}$ 与 $\nu f_{7/2}$–$i_{13/2}$ 在费米面附近形成关键结构；浅能量增益意味着软动态关联。 | 同一质量区内相邻核素可从球形到软八极极小，不能由 $\beta_2$ 一维阈值代替粒子数和轨道占据。 | `rodriguez-guzman-2012-sm-gd-quadrupole-octupole.md`, PDF p.4 Table I, p.12, pp.14–15 |
| $^{220-240}$U，Gogny-D1S/D1N/D1M 与BCP1 | 所有核都有深长椭四极最低点；$^{222-230}$U出现非零 $Q_3$ 极小，深度不超过约1.5 MeV；其余核在 $Q_3=0$ 近似抛物。 | 出现八极极小与中子配对能较低、费米面单粒子密度较低相联系；$D_0$ 由费米面附近特定高-$K$ 轨道占据决定。BCP1配对相关和惯性可明显不同。 | 强长椭背景不构成“八极必被淬灭”的定律；四极—八极耦合弱可能是该模型族的近似，而不是跨区域公理。 | `tmp/day26-octupole-doublewell/1209.0927.pdf`, PDF pp.3,7–9, Fig.1–3 |
| $^{218-238}$Ra、$^{220-240}$Th，Gogny-D1M HFB映射sdf-IBM | 二维Gogny-D1M PES映射到sdf-IBM后，$^{224}$Ra、$^{226}$Th附近八极集体性最显著；不是整条链均具有同样深双阱。 | 映射保留全局最低点附近拓扑，但谱和跃迁还受玻色空间、惯性和映射参数影响。 | “八极区域”是核素与自由度共同决定的局部区域；不能把某一质量区的 $\beta_2$ 经验范围外推到所有Ra/Th/U。 | `nomura-2020-ra-th-gogny-d1m-octupole.md`, source summary and cited Gogny-D1M PES |

---

## Provisional Reasoning

### 1. 轨道排列与费米面相干

反射不对称场的主要驱动来自相同 $\Omega$、相反宇称且 $\Delta l=\Delta j=3$ 的近邻轨道，例如 Ba/Sm 区的 $\nu f_{7/2}$–$i_{13/2}$ 和 $\pi d_{5/2}$–$h_{11/2}$。四极约束先把球壳层分裂成 Nilsson 分支；随后八极场通过这些分支间的矩阵元降低能量。能否降低总能量取决于分支是否同时靠近费米面、占据是否允许成对混合以及自洽密度重排，不能只看球形轨道标签。

### 2. 费米面能隙与配对动力学

局部能隙通常降低费米面态密度和配对相关能；在HFB势能面上，这可使形变极小更清楚，但同时会增大某些准粒子分母并抑制线性响应。两种效应方向并不相同：低配对可使集体惯性增大，局部静态极小更深，而跃迁强度和动态波函数仍由惯性、零点能和投影共同决定。1209.0927明确把八极极小与较低配对能、低费米面能级密度联系起来，却没有给出“低配对即强八极”的普遍充分条件。

### 3. 偶极相消与八极强度的微观解耦

内禀偶极矩可写成质子和中子质心偏移的差：
$$D_0(Q_3)=e\frac{NZ}{A}(\bar{z}_p - \bar{z}_n)$$
因此 $D_0$ 或 $B(E1)$ 小可以来自质子—中子过渡密度相消，即使八极形变或 $B(E3)$ 很大。1209.0927在 $^{236}$U展示了特定轨道占据造成的 $D_0$ 近零区间；Day26的 $^{146}$Ba机制研究同样表明，E1相消必须检查完整投影/过渡密度，不能由 $E3$ 强度或单个 $\beta_3$ 推出。

---

## Assumptions

假定微观平均场计算满足自洽 HFB 约束最小化；假定四极与八极形变坐标具有明确的勒让德多极展开定义；假定单粒子能阶满足特定能量密度泛函（Gogny D1S/D1M 或 RMF/PK1）。

## Competing Explanations

1. 固定四极窗口假说：认为八极关联严格局限于 $\beta_2 \in [0.15, 0.20]$，强四极形变（$\beta_2 > 0.25$）必然淬灭八极（已被 $^{148,150}\text{Ba}$ 和 $^{222-230}\text{U}$ 反例证伪）；
2. 轨道自洽共振假说：认为只要费米面附近存在合适的 Nilsson 分支近简并，即使在较大四极形变下也能出现稳定的八极深极小。

## Transfer Conditions

可迁移的是双对易子与准粒子响应分解式；不同质量区（稀土区与锕系）的极小值位置、势垒深度与配对演化必须基于各自自洽势能面独立核定，严禁直接移植常数阈值。

## Failure Conditions

若在 $\beta_2 < 0.10$ 的纯球形区发现深达 $2\text{ MeV}$ 的刚性静态梨形双阱极小，或在强四极长椭变形区（$\beta_2 > 0.35$）证实八极软振动完全消失且无任何八极集体度，则本微观拓扑框架需重新修正。

## Falsification or Reverse Tests

1. 固定窗口反例：RMF 给出 $^{148,150}\text{Ba}$ 的 $\beta_2\approx0.26$–$0.28$ 与 $\beta_3\approx0.17$；若把 $0.20$ 当作普适上限，该结果直接否证；
2. 强四极淬灭反例：U 链在深长椭四极背景下仍有 $^{222-230}\text{U}$ 八极极小；因此“$\beta_2>0.28$ 必然淬灭 $\chi_3$”不能作为普适断言。

## Open Questions

在固定粒子数、配对强度和坐标归一化后，D1S/D1M/BCP/RMF 四大泛函对 $(\beta_2, \beta_3)$ 局部曲率与准粒子响应的具体分项偏差有多大？

## Human Review

本笔记由 Codex source self-audit 驱动，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 创建独立研究笔记，明确四极—八极势能面拓扑的微观适用边界。
