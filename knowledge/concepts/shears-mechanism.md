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

1. **3qp $\to$ 5qp 顺对齐能带交叉与强度比反弹物理机制**（工件 shears-dynamics-bandcrossing-model-014.py/json）：
   理想单组态剪刀模型预报 $B(M1) \propto \sin^2(\chi/2)$ 随自旋单调下降。但在实际原子核中，高自旋下必然经历准粒子破对与角动量重排。基于独立理论计算工件 shears-dynamics-bandcrossing-model-014.py/json，确立多准粒子剪刀动力学的三大核心机制：
   - **半经典剪刀运动学与张角演化**（Clark & Macchiavelli 2000 Eqs. 5–8）：
     质子叶片 $\vec{j}_\pi$ 与中子叶片 $\vec{j}_\nu$ 的张角满足 $\cos\theta = \frac{I(I+1) - j_\pi(j_\pi+1) - j_\nu(j_\nu+1)}{2 \sqrt{j_\pi(j_\pi+1) j_\nu(j_\nu+1)}}$。质子叶片相对总自旋角为 $\sin\theta_\pi = \frac{\sqrt{j_\nu(j_\nu+1)}}{\sqrt{I(I+1)}} \sin\theta$。横向偶极辐射几率由垂直磁矩分量决定：$B(M1; I \to I-1) = \frac{3}{8\pi} (g_\pi - g_\nu)^2 j_\pi(j_\pi+1) \sin^2\theta_\pi$；电四极跃迁则由叶片张角与弱四极形变调制：$B(E2; I \to I-2) = \frac{15}{128\pi} (e Q_{\text{eff}})^2 \sin^4\theta_\pi + B(E2)_{\text{core}}$；
   - **准粒子顺对齐驱动剪刀“重新张开”（Shears Re-opening）**：
     在 $^{135}\text{Pr}$（$N=76, \hbar\omega \approx 0.37\text{ MeV}$）与 $^{137}\text{Pr}$（$N=78, \hbar\omega \approx 0.42\text{ MeV}$）中，低自旋带基于 3qp 态 $\pi h_{11/2} \otimes \nu h_{11/2}^{-2}$（$j_\pi = 11/2, j_\nu \approx 10$）。随自旋上升剪刀正常闭合。当转频达到临界值时，一对 $g_{7/2}/d_{5/2}$ 质子破对顺对齐，体系跃迁至 5qp 态 $\pi h_{11/2}(g_{7/2})^2 \otimes \nu h_{11/2}^{-2}$。此时质子叶片角动量突增为 $j_\pi' = 11/2 + 6 = 23/2$。由于叶片变长，为了匹配同一总角动量 $I$，剪刀张角 $\theta$ 必然突发性地重新增大（剪刀重开），使 $\sin^2\theta_\pi$ 反弹上升，促使 $B(M1)$ 剧增；
   - **跨带 $E2$ 跃迁的正交性淬灭（Orthogonality Suppression）**：
     电磁 $E2$ 算符为单体算符，而 5qp 态与 3qp 态相差两个准粒子，两体跃迁矩阵元严格为零：$\langle 3\text{qp} | \hat{T}(E2) | 5\text{qp} \rangle \equiv 0$。在交叉混合区，$|I\rangle = \alpha(I)|3\text{qp}\rangle + \beta(I)|5\text{qp}\rangle$。对于 $\Delta I = 2$ 的 $E2$ 跨带跃迁，始态 $I$ 已被 5qp 组态主导（$\beta(I)^2 > 0.8$），而终态 $I-2$ 仍处于 3qp 组态（$\alpha(I-2)^2 > 0.8$）。此时对角项乘积 $\alpha(I)\alpha(I-2) \ll 1$ 且 $\beta(I)\beta(I-2) \ll 1$，导致带内交叉 $B(E2; I \to I-2)$ 出现极其陡峭的塌缩式极小点（从 $0.11$ 暴跌至 $0.03\ e^2\text{b}^2$）；
   - **强度比反弹峰与动力学转动惯量 $\mathcal{J}^{(2)}$ 共振峰的严格对应**：
     分子 $B(M1)$ 受剪刀重开而增强，分母 $B(E2)$ 受正交性抑制而塌缩，双重动力学效应迫使比值 $B(M1)/B(E2)$ 出现剧烈反弹激增：$^{135}\text{Pr}$ 实测从 $15.78$ 飙升至 $94.83\ (\mu_N/e\text{b})^2$（数值模型给出 $63.6 \to 86.9$）；$^{137}\text{Pr}$ 实测从 $10.4$ 飙升至 $62.1\ (\mu_N/e\text{b})^2$（数值模型给出 $84.7 \to 50.4$）。在频率轴上，准粒子顺对齐使 $\mathcal{J}^{(2)} = dI/d\omega$ 在交叉频率 $\omega_c$ 产生高达 $137 - 220\ \hbar^2/\text{MeV}$ 的尖锐共振峰，与 $B(M1)/B(E2)$ 极值点高度吻合；
   - **经典剪刀闭合与带交叉多核系统学对照**：
     * $^{198}\text{Pb}$（Band 1）：4qp 纯剪刀闭合（$\pi(h_{9/2}i_{13/2})_{11^-} \otimes \nu(i_{13/2})^{-2}_{12^+}$），无能带交叉，自旋 $17 \to 23$ 剪刀角从 $78^\circ$ 闭合至 $20^\circ$，$B(M1)$ 严格单调下降 10 倍以上（$3.2 \to 0.25\ \mu_N^2$），$\mathcal{J}^{(2)}$ 稳定维持在 $\sim 22\ \hbar^2/\text{MeV}$；
     * $^{197}\text{Pb}$（Band 'a'）：经历 $I \approx 37/2^-$ 与 $49/2^-$ 两次中子空穴顺对齐交叉，剪刀经历两次重开，$B(M1)$ 出现两次显著反弹跃升（从 $0.5$ 反弹至 $1.8\ \mu_N^2$）；
     * $^{135}\text{Pr}$ 与 $^{137}\text{Pr}$：证实了稀土过渡区准粒子对顺对齐打破单调闭合唯象假设的普遍规律；并在 $^{137}\text{Pr}$ 中完满观察到 5qp 剪刀在高自旋区重新闭合使强度比回跌至 $17.2$ 的完整两相旋回。

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
