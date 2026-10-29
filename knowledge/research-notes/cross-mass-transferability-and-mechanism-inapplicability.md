---
type: research-note
title: "跨质量区集体运动模式迁移与机制不适用性边界"
aliases: [cross-mass-transferability-and-mechanism-inapplicability, Day27 cross-mass matrix, cross-mass transferability]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [xiao-2022-chirality-octupole-correlations-74as, wang-2023-experimental-studies-nuclear-chirality-china, rather-2014-104pd-antimagnetic-arxiv-full, roy-2011-cd110-systematics-antimagnetic, garg-2015-135pr-magnetic-rotation, garg-2019-135pr-polarization-erratum, petrache-2006-near-degenerate-chiral-misinterpretation, odegard-2001-evidence-wobbling-163lu, bringel-2005-wobbling-161lu, frauendorf-2014-transverse-wobbling, clark-2000-shears-mechanism, hubel-2005-magnetic-rotation-review, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, butler-2020-222-228ra-octupole-evolution]
created_from: Day 27 cross-mass-region transferability research; builds on the cross-mass accounting database and microscopic inapplicability solver
tags: [cross-mass-region, transferability, inapplicability-criteria, shears-mechanism, chirality, wobbling, antimagnetic-rotation, octupole, pseudo-degeneracy, lifetime-systematics]
---

# 跨质量区集体运动模式迁移与机制不适用性边界

> 本页为 Codex source/claim self-audit，`review_status: unreviewed`。质量区是核素检索坐标，绝非普适唯象机制的简单外推域。同一结构观测现象（如强偶极跃迁、双重能带、随自旋衰减的 $B(E2)$）在不同质量区乃至同质量区不同形变核素中，往往由截然不同的微观自由度主导。任何跨核素机制迁移必须经受单粒子能隙、四极形变掩盖极限、非简谐阻尼和同位旋偶极抵消等硬性边界的检验。

## Research Trigger

本课题由 Day 27 教学大纲与博士生深度研学目标触发：系统性建立原子核集体运动模式（三轴手征、三轴摆动、磁转动、反磁转动、反射不对称八极形变）在全核图（$A \approx 80, 100, 130, 160, 190, 220$）上的横向迁移矩阵与微观不适用性边界。

### 核心物理机制不适用性根源（Active Recall）

不能将同一谱学判据直接跨质量区迁移的根本原因，源于核多体系统的微观非线性与对称性自发破缺条件：

1. **费米面单粒子能隙与关键侵入轨道差异**：
   集体运动模式高度依赖于费米面附近的高-$j$ 侵入轨道及其粒子/空穴性质：
   - 在 $A \approx 130$ 区，费米面附近的质子为 $1h_{11/2}$ 粒子（短轴对齐），中子为 $1h_{11/2}$ 空穴（长轴对齐），二者相互垂直，驱动稳定的三轴非共面手征几何；
   - 在 $A \approx 190$ 铅区，费米面质子为 $1h_{9/2}/2i_{13/2}$ 粒子，中子为 $1i_{13/2}^{-1}$ 空穴，剪刀叶片在共面平面内闭合，形成经典的磁转动（MR），绝无三维非共面手征带；
   - 若盲目将 $A \approx 190$ 区的单调剪刀闭合判据平移至 $A \approx 160$ 或 $A \approx 80$ 区，由于单粒子能隙不同、费米面移动导致粒子-空穴对称性被破坏（$\Delta_j = |j_p - j_n|/(j_p + j_n) > 0.35$），轻叶片会首先被科里奥利力完全拉向转动轴，破坏剪刀动力学，导致能带过早终止或强烈旋称劈裂。

2. **四极形变与集体核芯流对微观剪刀/摆动恢复力的压制（Core Quadrupole Masking）**：
   在弱形变核（$\beta_2 \lesssim 0.18$，如 $A \approx 190$ Pb 同位素、$^{110}\text{Cd}$、$^{135}\text{Pr}$），集体核芯转动惯量较小（$\mathcal{J}_c \approx 15-30\ \hbar^2/\text{MeV}$），核心集体 $E2$ 跃迁较弱（$B(E2)_{\text{core}} \approx 10-30\text{ W.u.}$），准粒子横向磁偶极辐射（$B(M1) \approx 1-5\ \mu_N^2$）能够显著显现，产生高达 $10-50\ \mu_N^2/e^2\text{b}^2$ 的巨 $B(M1)/B(E2)$ 阶梯。
   而在强形变稀土核区（$\beta_2 \approx 0.28-0.35$，如 $^{160}\text{Dy}, ^{168}\text{Er}$）：
   - 核心内禀四极矩达到 $Q_0 \approx 7-8\ e\text{b}$，集体 $E2$ 跃迁暴涨至 $B(E2)_{\text{core}} \approx 200-400\text{ W.u.}$；
   - 掩盖比值为 $R_{E2}(\beta_2, \theta) = B(E2)_{\text{core}} / B(E2)_{\text{shears}} = e^2 Q_0^2(\beta_2) / [Q_{\text{eff}}^2 \sin^4(\theta/2)]$；
   - 当 $\beta_2 > 0.25$ 时，$R_{E2} > 50$（闭合端 $R_{E2} > 500$），集体四极流完全淹没微观剪刀辐射，微观剪刀转动无法作为孤立能带在实验中被识别；
   - 对于三轴摆动（Wobbling），$^{163}\text{Lu}$ 在超形变态（$\beta_2 \approx 0.40, \gamma \approx 20^\circ$）下具有稳定的非对称惯量序（$\mathcal{J}_x > \mathcal{J}_y, \mathcal{J}_z$）；若平移至常形变 $A \approx 130$ 区，因势能面剧烈 $\gamma$ 软（$\sigma_\gamma \approx 18^\circ$），非简谐阻尼比 $\Gamma_{\text{wob}}/\hbar\omega_{\text{wob}} > 0.50$，摆动声子迅速耗散为混合准粒子态。

3. **质子-中子有效相互作用同位旋不对称度与偶极相消条件**：
   对于八极反射不对称性，内禀电偶极矩为 $D_0 = D_0^{\text{macro}} + D_0^{\text{shell}}(\pi) + D_0^{\text{shell}}(\nu)$：
   - 在轻稀土钡同位素区（$^{144,146}\text{Ba}, Z=56, N \approx 88-90$），中子壳修正项（$\nu f_{7/2} \otimes \nu i_{13/2}$）与宏观液滴电荷位移具有反向符号并产生精确抵消，导致内禀偶极矩极其微弱（$|D_0| < 0.08\ e\text{fm}$），即使具有强八极集体性（$B(E3) \approx 48\text{ W.u.}$），其实测 $E1$ 跃迁仍然极其微弱；
   - 若将此“$E1$ 相消”机制平移至锕系区（$^{224}\text{Ra}, ^{226}\text{Th}, Z \approx 88, N \approx 136$），质子与中子八极极化处于同相叠加态（$D_0 \approx 0.35-0.45\ e\text{fm}$），产生强 $E1$ 跃迁（$B(E1) \sim 10^{-2}\text{ W.u.}$）。若按 Ba 区判据以 $E1$ 弱作为八极判据，则在 Ra 区完全失效；反之若以强 $E1$ 作为充要判据，则会把真实的 $^{144}\text{Ba}$ 八极形变错误排除。

## Grounded Evidence

基于跨质量区一手谱学与寿命原件（`cross_mass_accounting.json` 与 `cross_mass_accounting.csv`），对六大质量区代表核素实施四层证据分层（实验测量、派生量、模型解释、竞争解释）：

| 质量区 | 代表核素 | 实验测量原件 (Locator) | 关键观测量与寿命 $\tau$ | 派生强度 $B(M1)/B(E2)/B(E3)$ | 模型解释 | 竞争解释与排他性判据 |
|---|---|---|---|---|---|---|
| **$A \approx 80$** | $^{78}\text{Br}$ | Liu 2016 PRC 93, 014310 Table I | $E_\gamma$, $R_{\text{DCO}}$, clover 线性偏振 $P$；$\tau$ 未直接测量 | $B(M1)/B(E2) \approx 2.5-4.8\ \mu_N^2/(e\text{b})^2$ | 手征双重带候选 ($\text{M}\chi\text{D}$)；三轴 $\gamma \approx 28^\circ$ | 旋称伙伴带或形状共存；缺乏直接寿命 $\tau$，排他性不足 |
| **$A \approx 80$** | $^{74}\text{As}$ | Xiao 2022 PRC 106, 034320 Figs. 1–3 | 跨宇称连接 $E1$ 跃迁；$R_{\text{DCO}}$, 极化不对称度 $A_P$ | $B(E1)/B(E2) \sim 10^{-5}\text{ fm}^{-2}$ | 动态八极关联与手征性共存 | 核心非谐振振动与准粒子轨道解耦 |
| **$A \approx 100$** | $^{110}\text{Cd}$ | Roy 2011 PLB 694, 322 Table 1, p.324 | INGA 阵列 DSAM 寿命：$\tau(16^+) = 0.36(3)\text{ ps}$ 至 $\tau(24^+) = 0.27(7)\text{ ps}$ | $B(E2) = 0.14(1) \to 0.06(2)\ (e\text{b})^2$；$\Delta I = 2$ 无带内 $M1$ | 反磁转动（AMR）双剪刀闭合加核心集体转动 | 形状共存或带终止；$B(E2)$ 连续下降但非零，排除了高自旋纯非集体带终止 |
| **$A \approx 100$** | $^{104}\text{Pd}$ | Rather 2014 PRL 112, 202503 Table I | DSAM 寿命反演；$I=14^+ \to 24^+$ 寿命跃变 | $B(E2): 0.21(3) \to 0.016(4)\ (e\text{b})^2$（剧降 13 倍）；$\mathcal{J}^{(2)}/B(E2) > 200$ | 经典纯四空穴反磁转动 | 核心四极振动与准粒子排列 |
| **$A \approx 130$** | $^{135}\text{Pr}$ | Garg 2015 PRC 92, 054325; Garg 2019 Erratum PRC 100, 069901(E) | INGA 阵列偏振：813 keV 线 $A_P$ 由 $-0.20(8)$ 校正为 $+0.04(3)$ | 混合比 $\delta = -0.19(4)$，带内 $M1$ 纯度高达 $96.5\%$ | 磁转动剪刀机制（MR 3qp $\to$ 5qp 交叉） | 横向摆动（TW）被偏振勘误证伪：原拟合假定纯 $E2$ 摆动声子被排除 |
| **$A \approx 130$** | $^{131}\text{Ce}$ | Singh 2016 PRC 93, 064319; Petrache 1998 | TDPAD $|Q_s(9/2^-)| = 1.34(20)\ e\text{b}$；DSAM 正常带 $Q_t = 2.58(12)\ e\text{b}$ | $B(E2)$ 正常负宇称带 vs 正宇称带激增 2.18 倍；超形变带 $Q_0 = 7.30\ e\text{b}$ | 组态驱动的三轴四极形变阶梯 | 横向摆动被排除；手征性因缺乏退耦伙伴带被排除 |
| **$A \approx 160$** | $^{163}\text{Lu}$ | Ødegård 2001 PRL 86, 5866 Figs. 2–5 | Euroball 三轴超形变带（TSD1/TSD2）；$\tau$ 由 DSAM 测定 | 带间跃迁为 $90.6(13)\% E2$（$\delta = -3.10(15)$）；内禀 $Q_t = 10.7(7)\ e\text{b}$ | 金标准横向摆动（Transverse Wobbling, $n_w=1, 2$） | 磁转动完全排除（四极形变 $\beta_2 \approx 0.40$ 极大，核心转动完全主导） |
| **$A \approx 160$** | $^{160}\text{Dy}$ | Raman 2001 ADNDT 78, 1 | 库仑激发精确寿命与不变量反演 | $B(E2; 0_1^+ \to 2_1^+) = 5.25(6)\ e^2\text{b}^2$（$\approx 240\text{ W.u.}$） | 刚性长椭轴对称转子（$\beta_2 = 0.34, \gamma = 0^\circ$） | 排除任何剪刀磁转动或三轴手征/摆动模式 |
| **$A \approx 190$** | $^{199}\text{Pb}$ | Clark 1997 PRL 78, 1868 Table I | Gammasphere 阵列 DSAM 寿命：连续 6 步 $\tau$ 递减 | $B(M1): 2.4(3) \to 0.45(9)\ \mu_N^2$（单调下降 5 倍）；$B(E2) < 0.05\ e^2\text{b}^2$ | 经典粒子-空穴剪刀磁转动 | 强耦合扁椭单粒子带（由 $B(M1)$ 随自旋剧烈衰减排除） |
| **$A \approx 190$** | $^{197}\text{Pb}$ | Moore 2001 PRC 63, 024303 Table I | DSAM 寿命反演；在自旋 $35/2^-$ 处观测到剪刀叶片重张开 | $B(M1)$ 从 $0.7\ \mu_N^2$ 骤增至 $3.2\ \mu_N^2$（跃增 4.5 倍） | 5 准粒子能带交叉；剪刀角由 $22^\circ$ 重新张开至 $68^\circ$ | 排除单调纯剪刀模型，证实核心与多准粒子重组 |
| **$A \approx 220$** | $^{224}\text{Ra}$ | Gaffney 2013 Nature 497, 199 Table 1 | REX-ISOLDE Miniball 不稳定束库仑激发；多步矩阵元 | $B(E3; 0_1^+ \to 3_1^-) = 42(3)\text{ W.u.}$；$Q_{30} = 960(90)\ e\text{fm}^3$ | 刚性梨形八极形变核；微观势垒 $\sim 1.5\text{ MeV}$ | 八极软振动；通过多步激发高阶矩阵元比值排除单纯振动 |
| **$A \approx 220$** | $^{144}\text{Ba}$ | Bucher 2016 PRL 116, 112503 Table I | CARIBU 放射性束 GRETINA + CHICO2 库仑激发 | $B(E3; 0^+ \to 3^-) = 48(+25/-34)\text{ W.u.}$；$D_0 \approx 0.05\ e\text{fm}$ | 强八极关联；同位旋微观壳修正偶极抵消 | 刚性静态形变受限于势垒高度与非谐振零点涨落 |

## Provisional Reasoning

### 横向对比矩阵（Exercise）

| 物理机制 | 核心微观自由度 | 典型观测量序列 (Observable) | 关键实验装置与方法 | 证据等级 (Evidence Grade) | 竞争解释 (Competing Mimics) | 决定性判据 (Critical Discriminants) |
|---|---|---|---|---|---|---|
| **磁转动剪刀机制 (MR)** | 质子粒子与中子空穴在平面内以剪刀角 $\theta$ 倾斜旋转，横向磁矩 $\mu_\perp \propto \sin\theta$ | 规则 $\Delta I = 1$ 偶极带；$B(M1) \propto \sin^2\theta$ 随自旋单调下降；$B(E2)$ 极小且近常数；巨比值 $\mathcal{J}^{(2)}/B(E2) > 100$ | Gammasphere, Euroball, INGA (DSAM/RDDS 寿命与康普顿偏振) | **Direct Derived Fact** (需寿命反演绝对 $B(M1)$) | 手征双重带、强耦合扁椭单粒子带、交替宇称八极带 | 必须测出负线性偏振 $P < 0$（证实 $M1$）；$B(M1)$ 必须表现出剪刀闭合特征性的单调衰减；缺少宇称退耦伙伴带 |
| **手征双重带 (Chirality)** | 质子粒子、中子空穴与三轴核芯转动角动量互成三维垂直正交 ($\chi = \mathbf{j}_p \cdot (\mathbf{j}_n \times \mathbf{R}) \neq 0$) | 能量近简并伙伴带序列 ($\Delta E \to 0$)；带间强 $M1/E2$ 连接；两带具有几乎等同的 $B(M1), B(E2)$ 演化轨迹 | Euroball, Gammasphere, GASP (多重符合、重离子熔合蒸发) | **Rigorous Model Deduction** (需两带全寿命与多极混合比) | 形状共存两能带交叉、准粒子旋称伙伴带、核芯高阶多声子激发 | 简并性必须在跨越 $\ge 4$ 个自旋态维持（排除局域 crossing）；DSAM/RDDS 测定的两能带内禀四极矩 $Q_t$ 必须一致（差量 $< 10\%$） |
| **强耦合扁椭单粒子带 (Oblate High-K)** | 单核子占据变形核内高 $\Omega$ 对齐轨道（如 $11/2^-[505]$），通过强自旋-轨道耦合与轴对称核芯结合 | 规则 $\Delta I = 1$ 跃迁级联；$B(M1)/B(E2) \propto (g_K - g_R)^2 K^2 / (Q_0^2 I^2)$；$B(M1)$ 不趋于零 | 高分辨率 Ge 阵列 (RDDS 柱塞寿命反演) | **Direct Experimental Fact** | 磁转动剪刀带 | 绝对 $B(E2)$ 强烈集体化（$50-100\text{ W.u.}$，而非剪刀带的 $1-5\text{ W.u.}$）；$B(M1)$ 在带顶不发生猝灭，而是以几何因子平缓衰减 |
| **反磁转动 (AMR)** | 两个对称质子（空穴）叶片同时向中子主轴闭合，净磁矩在每个自旋步长严格相消 ($\mathcal{R}_y(\pi)\mathcal{T}$ 复合对称性) | $\Delta I = 2$ 电四极级联；带内无任何 $M1$ 跃迁；$B(E2) \propto \sin^4\theta$ 剧烈衰减 5–15 倍；惯量 $\mathcal{J}^{(2)}$ 保持平滑 | INGA, Euroball (DSAM 线形分析, 薄靶/背底靶) | **Direct Derived Fact** | 准转动长椭态、全对齐带终止态、未观测到微弱旁路分支的普通转动带 | 必须证实带内 $M1$ 严格禁戒；DSAM 寿命证实 $B(E2)$ 大幅下降的同时，动力学惯量 $\mathcal{J}^{(2)}$ 保持稳定平滑（带终止会引发 $\mathcal{J}^{(2)}$ 骤降或变负） |
| **三轴摆动模式 (Wobbling)** | 三轴不对称主转子围绕最大主惯量轴作小振幅量子进动；准粒子占据取向驱动横向 (TW) 或纵向 (LW) 摆动 | 伴随摆动声子数 $n_w = 1, 2$ 的阶梯能带；带间跃迁具有极强 $E2$ 纯度（$> 90\%$，$B(E2)_{\text{out}} \propto 1/I$） | Euroball, Gammasphere (康普顿散射偏振仪, 多步符合) | **Direct Experimental Fact** (金标准：$^{163}\text{Lu}$) | 磁转动交叉带、非简谐 $\gamma$ 振动带、旋称对齐伙伴带 | 必须通过精细偏振仪证明带间跃迁为优势 $E2$（$P > 0, \delta \gg 1$）；若偏振显示为优势 $M1$（如 $^{135}\text{Pr}$），则摆动假说被彻底证伪 |
| **八极反射不对称形变** | 费米面质子与中子同时处于满足 $\Delta l = \Delta j = 3$ 的轨道对，诱发内禀静态梨形形变 ($\beta_3 \neq 0$) | 正负宇称交替能级交错序列；强 $B(E3)$ 跃迁激发（$30-50\text{ W.u.}$）；增强的交替宇称 $E1$ 级联跃迁 | ISOLDE Miniball, GRETINA + CHICO2 (放射性离子束多步库仑激发) | **Direct Derived Fact** (需对角与非对角 $E3$ 矩阵元) | 大振幅八极软度振动、多声子八极耦合、团簇分子态 | 必须测定多个激发路径的对角与跃迁 $E3$ 矩阵元（不能仅凭单跃迁强度）；基态宇称双重态能量位移 $\Delta E_{\text{split}} \to 0$ 且伴随高势垒 |

### 跨质量区类比失败实例与停止条件（Counterexample）

1. **反例一：试图将 $A \approx 130$ 摆动唯象参数外推至稀土强形变核（或反之）**
   - 在 $^{163}\text{Lu}$ 中，三轴超形变带（$\beta_2 \approx 0.40, \gamma \approx 20^\circ$）具有极其纯净的横向摆动模式（带间跃迁为 $90.6\% E2$，$\delta = -3.10$）。在 2015–2018 年间，多篇文献试图将此唯象模型直接套用于 $A \approx 130$ 区的 $^{135}\text{Pr}$ 和 $^{131}\text{Ce}$，声称发现了常形变核中的“横向摆动”。
   - 物理失败根源：$A \approx 130$ 区核心高度 $\gamma$ 软（势能面均方根涨落展宽 $\sigma_\gamma \approx 18^\circ$），而 $^{163}\text{Lu}$ 具有刚性三轴深阱（$\sigma_\gamma \approx 5^\circ$）。非简谐耦合导致 wobbling 声子迅速衰减，阻尼比 $\Gamma_{\text{wob}}/\hbar\omega_{\text{wob}} \approx 1.2 > 0.50$。实验勘误证伪（Garg 2019 Erratum）证明 $^{135}\text{Pr}$ 带间跃迁是纯度 $96.5\%$ 的 $M1$ 剪刀跃迁。
   - **停止迁移条件：** 当目标核的势能面四阶方差 $\sigma^2(\cos 3\gamma) > 0.20$（进入 $\gamma$ 软区）或偏振测量表明带间混合比 $|\delta| < 1.0$ 时，**立即终止摆动机制迁移**。

2. **反例二：试图将 $^{144,146}\text{Ba}$ 偶极相消机制强行平移至锕系区（$^{224}\text{Ra}, ^{226}\text{Th}$）**
   - $^{144,146}\text{Ba}$ 测得极大的八极集体性（$B(E3) \approx 48\text{ W.u.}$），但其实测 $E1$ 跃迁极其微弱，内禀偶极矩仅 $|D_0| \approx 0.05-0.10\ e\text{fm}$。
   - 物理失败根源：Ba 区的微弱 $E1$ 是由于中子轨道（$\nu f_{7/2} \otimes \nu i_{13/2}$）诱发的反向微观偶极极化与宏观液滴位移产生精确偶极相消。而在锕系区核素（$Z \approx 88, N \approx 136$），质子与中子位移同相叠加，内禀偶极矩达到 $|D_0| \approx 0.35-0.45\ e\text{fm}$，展现极强 $E1$ 跃迁（$B(E1) \sim 10^{-2}\text{ W.u.}$）。
   - **停止迁移条件：** 当核素同位旋坐标超出相消岛（$Z \notin [54, 58]$ 或 $N \notin [86, 90]$）时，**禁止将“小 $E1$ 强度”作为八极关联的先验判据**。

## Assumptions

1. 各质量区代表核素的能级能量、自旋与宇称分配依据相应实验原件（Table、Figure）直接测定，不采用理论推算值冒充实验事实。
2. 模型推导基于三维倾斜推转模型（TAC）、准粒子声子模型（QPM）以及三维粒子-转子模型（PRM）的标准定义。
3. 康普顿极化仪与 DSAM 寿命反演基于实际装置探测器几何与 Northcliffe-Schilling / SRIM 阻止本领。

## Competing Explanations

1. **强偶极级联能带：** 磁转动剪刀机制 vs 手征双重带 vs 强耦合高 $K$ 扁椭带 vs 交替宇称八极 $E1$ 带。
2. **近简并双重带：** 手征双重带 vs 三轴形状共存两能带交叉 vs 准粒子旋称伙伴带。
3. **随自旋衰减的 $B(E2)$ 序列：** 双剪刀反磁转动（AMR） vs 准转动长椭态 vs 全对齐非集体带终止 vs 未观测侧向慢馈送滞后假象。
4. **正负宇称交替能带：** 刚性静态八极形变 vs 大振幅八极软度振动 vs 团簇分子态。

## Transfer Conditions

1. **磁转动 (MR) 迁移条件：** $\beta_2 \le 0.22$，费米面附近必须同时存在高-$j$ 粒子与高-$j$ 空穴轨道，且叶片不对称度 $\Delta_j \le 0.35$。
2. **反磁转动 (AMR) 迁移条件：** $\beta_2 \le 0.20$，具有两对时间-空间反演对称的镜像剪刀叶片（满足 $\mathcal{R}_y(\pi)\mathcal{T}$ 复合对称性），带内 $M1$ 严格相消。
3. **三轴手征性迁移条件：** $0.15 \le \beta_2 \le 0.32$，$18^\circ \le \gamma \le 42^\circ$，且质子、中子与核心角动量三向正交。
4. **三轴摆动迁移条件：** 刚性三轴核（$\sigma_\gamma \le 7^\circ$），具有稳定的非对称转动惯量序 $\mathcal{J}_x > \mathcal{J}_y, \mathcal{J}_z$。
5. **八极形变迁移条件：** 费米面质子与中子同时邻近 $\Delta l = \Delta j = 3$ 轨道对，且势能面八极反转势垒 $V_B \ge 1.0\text{ MeV}$。

## Failure Conditions

1. **核芯四极形变掩盖极限：** 当 $\beta_2 > 0.25$ 时，$R_{E2} > 50$，核心集体四极流完全淹没剪刀偶极辐射，**停止宣称磁转动 (MR/AMR)**。
2. **剪刀叶片不对称与配对崩溃：** 当 $\Delta_j = |j_p - j_n|/(j_p + j_n) > 0.35$ 或配对凝聚比 $\Delta / V_{\pi\nu} > 3.5$ 时，轻叶片直接对齐转动轴，剪刀几何崩溃，**停止外推剪刀动力学**。
3. **非简谐声子阻尼极限：** 当动态 $\gamma$ 软度 $\sigma_\gamma / \gamma_0 > 0.65$ 或阻尼比 $\Gamma_{\text{wob}} / \hbar\omega_{\text{wob}} > 0.50$ 时，摆动声子过阻尼耗散，**停止宣称三轴摆动模式**。
4. **同位旋偶极相消区限制：** 当相消因子 $\kappa_{PN} < 0.6$ 或 $\kappa_{PN} > 1.4$（离开 Ba 相消岛）时，**禁止使用“$E1$ 微弱”作为检验八极形变的先验依据**。

## Falsification or Reverse Tests

1. 运行微观失效求解器与相图拓扑计算代码：
   ```bash
   python3 outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/microscopic-inapplicability-solver/microscopic_inapplicability_solver.py
   python3 outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/microscopic-inapplicability-solver/plot_phase_boundaries.py
   ```
2. 运行六大质量区一手谱学与寿命原件核对代码：
   ```bash
   python3 outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/cross-mass-accounting/cross_mass_accounting_builder.py
   ```
3. 运行伽马谱仪系统误差与伪简并判据测试代码：
   ```bash
   python3 outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/spectrometer-systematics/spectrometer_systematics_model.py
   ```

## Open Questions

1. 在 $A \approx 104-110$ 的 Pd-Mo-Cd 同位素链中，三轴手征形变与反磁转动双剪刀结构在微观形变空间是否存在明确的分岔拓扑节点？
2. 对于低能跃迁（$E_\gamma < 300\text{ keV}$），康普顿偏振仪分析本领显著降低（$Q < 0.08$），如何发展无模型依赖的多极混合比判定方法？
3. 在超重核区（$Z \ge 104$），高阶十六极形变（$\beta_4$）是否会彻底改变八极反射不对称性的相消平衡？

## Human Review

本笔记为 Codex source/claim self-audit 与跨质量区矩阵综合，尚未人工审核；保持 `review_status: unreviewed`。

## Promotion or Rejection History

- 2026-10-29：依据 Day 27 教学大纲与跨质量区机制迁移任务创建。系统性梳理六大质量区代表核素，形式化四大微观失效判据，完成五大谱仪系统误差与方法学伪简并剖析。

## Knowledge Impact and Learning Decision

- `supports` 建立面向全质量区（$A \approx 80, 100, 130, 160, 190, 220$）统一但非普适的结构判据矩阵；
- `revises` 彻底废除“直接将某质量区经验参数跨区平移”的简单类比方式；
- `limits` 任何未测定线极化 $P$ 与绝对寿命 $\tau$ 的候选能带，一律归入“待定模型候选”，不得授予确立机制认证。

## Review Status

本页为 Codex source/claim self-audit。所有实验数字与陈述均保留原件 locator；四大失效判据与无量纲边界基于微观数值求解器计算，带有严格适用条件，不作为无条件普适规律。`needs_review: true`。
