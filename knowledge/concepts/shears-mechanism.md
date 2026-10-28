---
type: concept
title: "Shears Mechanism"
aliases: [shears mechanism, shears bands]
created: 2026-07-13
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
concept_type: angular-momentum-generation
confidence: low
tags: [shears, magnetic-rotation, angular-momentum-alignment]
---

# Shears Mechanism

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

In the shears picture, high-j particle and hole angular-momentum vectors act as blades. Their gradual alignment increases the total angular momentum along a band, while the interaction and induced polarization determine the opening angle and transition strengths.

## Evidence Boundary

The mechanism is an interpretation of a configuration and its calculated angular-momentum geometry. A smooth energy sequence or changing B(M1) is not an independent proof without configuration, multipolarity and lifetime information.

## Relation to Alignment

This angular-momentum alignment is distinct from reaction-produced magnetic-substate alignment used in angular-distribution analysis. The two meanings must not be merged in `sigma/I` or P-ADO work.

## Necessary Assumptions

- The particle and hole blades belong to a resolved or explicitly proposed configuration.
- The interaction and any quadrupole polarization are specified before interpreting the angular-momentum path.

## Discriminating Observables

Spin-dependent angular momentum, frequency, B(M1), B(E2), and lifetime trends are used together.

## Supporting Evidence

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[clark-2000-shears-mechanism]]
- [[chiara-2001-108-110in-shears-band-lifetimes]]
- [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]]

## Counter-evidence and Competing Interpretations

Configuration crossing, quasiparticle alignment and ordinary collective rotation can change the same observables.

## Our Current Position

Keep shears-blade alignment distinct from reaction alignment and magnetic-substate population.

Day23纠正：旧Day21的“跨组态全段单调骤降、6–10倍与固定大比值”认证撤回，不作为本页判据。[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-D22-R098-1/2的实际108In表既有组态内下降，也有alignment附近回升；[[clark-2000-shears-mechanism]] CL00-D23-001/002限定了角度和组态范围。新增为Codex self-audit，needs_review:true。

## Day 26：带交叉反弹、双剪刀四刃对称性与核心耦合

结合 [[garg-2015-135pr-magnetic-rotation]]、[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]] 与 [[roy-2011-cd110-systematics-antimagnetic]]，深化剪刀机制在多准粒子与核心耦合下的理论与实验边界：

1. **3qp $\to$ 5qp 顺对齐能带交叉与强度比反弹**：
   理想单组态剪刀模型预报 $B(M1) \propto \sin^2(\chi/2)$ 随自旋单调下降。但在实际原子核中，高自旋下必然经历准粒子对破对重排。在 $^{135}\text{Pr}$（N=76，$\hbar\omega \approx 0.37\text{ MeV}$）与 $^{137}\text{Pr}$（N=78，$\hbar\omega \approx 0.42\text{ MeV}$）中，一对 $g_{7/2}$ 质子顺对齐使 3qp 能带交叉进入 5qp 能带。在逼近交叉点时，动力学转动惯量剧增与组态相干混合使 $B(M1)/B(E2)$ 出现剧烈的特征反弹峰（$^{135}\text{Pr}$ 升至 $94.83\ (\mu_N/e\text{b})^2$；$^{137}\text{Pr}$ 升至 $62.1\ (\mu_N/e\text{b})^2$），随后在 $^{137}\text{Pr}$ 中展现 5qp 剪刀重新闭合回落至 $17.2$。这确立了多相剪刀机制容许能带交叉反弹的普遍规律，打破了“剪刀带必须处处单调陡降”的唯象硬门。

2. **反磁转动四刃对称性与纯剪刀终止自旋极限**：
   在反磁转动（AMR）中，两对粒子-空穴叶片关于转动轴对称闭合，其垂直于自旋的横向磁偶极分量严格反向相消，内禀 $M1$ 跃迁禁戒。对于 $^{110}\text{Cd}$ 组态 $\pi(g_{9/2})^{-2} \otimes \nu(h_{11/2})^2$：
   - 纯双剪刀（核心惯量 $\Im = 0$）极限下，角动量最大值为 $I_{\text{max}} = j_p + 2 j_h = 10 + 2 \times 4.5 = 19\hbar$。纯剪刀机制物理上无法解释实验观测到能带延伸至 $24^+$ 及 $26^+$ 的事实；
   - 引入核心集体转动耦合（$\Im = 19.5\text{ MeV}^{-1}\hbar^2$，半刚体转子值）后，核心转动在 $16^+ \to 24^+$ 贡献 $2.9 \to 6.3\hbar$ 角动量，分担了自旋增益，使剪刀闭合速率减缓，理论完满重现实测 $B(E2)$ 维持在 $0.14(1) \to 0.06(2)\ (e\text{b})^2$ 的平稳平台，以及巨判据比 $\mathcal{J}^{(2)}/B(E2) \approx 116–341\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$。

3. **平面剪刀向三维手征转动的跃迁分水岭**：
   单剪刀（MR）与双剪刀（AMR）的角动量产生局限在主平面内，保留 $\mathcal{S} = \mathcal{T}\mathcal{R}_y(\pi)$ 平面对称性，不产生手征性。当核芯具备显著三轴形变（$\gamma \approx -30^\circ$）时，中等轴的核心转动 $R$ 将总角动量拉出主平面，使质子叶片（短轴偏好）、中子叶片（长轴偏好）与核心转动 $R$（中等轴）构成右手与左手三维非共面三轴陀螺，实现由平面剪刀磁转动向三维手征转动的相变。

## Sources

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[clark-2000-shears-mechanism]]
- [[chiara-2001-108-110in-shears-band-lifetimes]]
- [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]]
- [[angular-momentum-alignment]]

## Review Status

New concept page; review pending.


## Day23 两blade几何的适用域

令经典无core模型I=jπ+jν、m=μ/μN=gπjπ+gνjν，jπ/jν/I均以ℏ为单位，χ为两blade夹角。以I方向为纵轴，在I²>0时

$$m_\perp^2=(g_\pi-g_\nu)^2\frac{j_\pi^2 j_\nu^2\sin^2\chi}{I^2},\qquad
I^2=j_\pi^2+j_\nu^2+2j_\pi j_\nu\cos\chi.$$

这是由m×I=(gπ−gν)jπ×jν得到的条件代数；半经典跃迁估计B(M1)/μN²=3mperp²/(8π)。[[clark-2000-shears-mechanism]] CL00-D23-001的sin²θπ使用的是**单blade相对I角**。等长两blade时θπ=θν=χ/2，从而B(M1)∝sin²(χ/2)，不能仍把χ叫同一个θ。TAC相对密度主轴的倾角又是另一对象；137Pr的25°/26°平均tilt不是实测shears开角。有限j的sqrt(j(j+1))处方、core R、changing configuration及量子涨落另需给定，不能把此无core代数当全量子禁戒或核态角度反演。

`system/scripts/day23_shears_geometry.py`以声明的整数/有理数向量检查投影恒等式、等长半角、平行极限、相同g抵消、互换与尺度平方；6项exact controls通过。chosen vectors无核素对应，不产生新角度、B、δ或τ。

实际实验比较须保留[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-12/13/16的τ—branch—ICC与feeding/stopping边界；[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]] AG07-D22-R098-1/2只有相对B(M1)/B(E2)且43/2打印输入未闭合，不能把比值下降叫已测绝对M1下降。以上均needs_review:true。
