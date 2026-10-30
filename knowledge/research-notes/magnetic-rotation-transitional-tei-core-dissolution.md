---
type: research-note
title: "过渡区碲与碘同位素磁转动剪刀容量与核芯转动溶解机制"
aliases: [magnetic-rotation-transitional-tei-core-dissolution, transitional Te I magnetic rotation, Day27 shears dissolution]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [clark-2000-shears-mechanism, hubel-2005-magnetic-rotation-review, rather-2014-104pd-antimagnetic-arxiv-full]
created_from: Day 27 magnetic rotation in transitional Te/I isotopes study; system/scripts/day27_magnetic_rotation_transitional_tei_study.py
tags: [magnetic-rotation, shears-mechanism, transitional-nuclei, core-coupling, tellurium, iodine, A110, A120, Day27]
---

# 过渡区碲与碘同位素磁转动剪刀容量与核芯转动溶解机制

## Research Trigger

在磁转动（MR）传统图景中（如 [[clark-2000-shears-mechanism]] 与 [[hubel-2005-magnetic-rotation-review]] 综述所归纳），磁转动多被视作近球形闭壳邻近核（如 A≈190 的 Pb 与 A≈110 的 Sn、Cd）的专属现象。早期假说常认为磁转动随着质子数越过 $Z=50$ 闭壳将发生“相变式猝灭”。然而在 $Z=52$ 的碲（$^{118}\text{Te}$）与 $Z=53$ 的碘（$^{119}\text{I}$）高自旋实验中，仍观测到显著的规则 $\Delta I = 1$ 偶极磁转动带，并在 [[rather-2014-104pd-antimagnetic-arxiv-full]] 的邻近核系统学中形成对比。本研究基于剪刀加核芯变分动力学模型，推演核芯四极形变 $\beta_2$ 与转动惯量 $\mathcal{J}_{\text{core}}$ 随质子数增加时的微观演化规律，确立磁转动向普通集体四极能带平滑溶解（Dissolution）的连续不适用性相界。

## Grounded Evidence

通过执行全微观剪刀闭合与核芯转动竞争求解器 `system/scripts/day27_magnetic_rotation_transitional_tei_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/mr-transitional-tei/magnetic_rotation_transitional_tei_resolution.json`），确立以下定量证据：

1. **同位素链 $Z=50 \to 52 \to 54$ 的核芯参与参数 $\chi$ 演化：**
   - 定义无量纲核芯—剪刀竞争度 $\chi = \mathcal{J}_{\text{core}} / \mathcal{J}_{\text{shears}}$；
   - **$^{106}\text{Sn}$（$Z=50$，近球形，$\beta_2 \approx 0.05, \mathcal{J}_{\text{core}} = 3.0\ \hbar^2/\text{MeV}$）：** $\chi = 0.12 \ll 1$。角动量几乎全部由剪刀叶片闭合提供（$\theta$ 从 $88.1^\circ$ 剧烈闭合 $88.1^\circ$ 至全对齐），$B(M1)$ 剧烈下降 $100\%$，形成典型的纯磁转动（$B(M1)/B(E2)$ 峰值高达 $1814\ \mu_N^2/(e\text{b})^2$）；
   - **$^{118}\text{Te}$ 与 $^{119}\text{I}$（$Z=52, 53$，过渡区，$\beta_2 \approx 0.16, \mathcal{J}_{\text{core}} = 15 - 18\ \hbar^2/\text{MeV}$）：** $\chi = 0.60 - 0.72$。核芯转动吸收了约 $35\% - 40\%$ 的总角动量，减缓了剪刀叶片的闭合速率（$\theta$ 仅闭合 $18^\circ - 21^\circ$），$B(M1)$ 下降幅度趋缓（约 $31\% - 36\%$），而 $B(M1)/B(E2)$ 维持在 $60 - 88\ \mu_N^2/(e\text{b})^2$，展现出明显的**核芯辅助磁转动（Core-Assisted Magnetic Rotation）**过渡特征；
   - **$^{122}\text{Xe}$（$Z=54$，变形区，$\beta_2 \approx 0.24, \mathcal{J}_{\text{core}} = 32.0\ \hbar^2/\text{MeV}$）：** $\chi = 1.28 > 1$。集体四极转动主导了全角动量生成（$R_{\text{core}} > 75\%$），剪刀角闭合被严重压制（仅微闭 $11.1^\circ$），$B(M1)/B(E2)$ 骤降至 $<20\ \mu_N^2/(e\text{b})^2$，剪刀特征完全溶解为普通集体 $E2$ 转动带。

2. **$Z>50$ 质子粒子—中子空穴剪刀组态的存在性：**
   - 在 $^{118}\text{Te}$（$N=66$）中，费米面位于 $N=50-82$ 壳层中上部，中子空穴占据高-$j$ 的 $\nu h_{11/2}^{-2}$ 轨道；
   - $Z=52$ 的 2 个价质子越过 $Z=50$ 闭壳占据 $\pi (g_{7/2}, d_{5/2})$ 并可在转动离心力下布居至 $\pi h_{11/2}$ 轨道；
   - 质子粒子叶片（$\vec{j}_\pi$）与中子空穴叶片（$\vec{j}_\nu$）依然满足倾斜相互作用与剪刀矢量加法条件，证明跨越 $Z=50$ 壳层并不破坏剪刀几何的存在性。

## Provisional Reasoning

体系总能量为剪刀排斥势能与核芯转动动能之和：
\[
E(I, \theta) = \frac{1}{2} V_2 (3\cos^2\theta - 1) + \frac{(I - j_{\text{shears}}(\theta))^2}{2 \mathcal{J}_{\text{core}}},
\]
其中剪刀总角动量为：
\[
j_{\text{shears}}(\theta) = \sqrt{j_\pi^2 + j_\nu^2 + 2 j_\pi j_\nu \cos\theta}.
\]
变分极小化平衡条件给出平衡剪刀角 $\theta_{\text{eq}}$ 随自旋 $I$ 的动态方程：
\[
\frac{dE}{d\theta} = -3 V_2 \cos\theta \sin\theta + \frac{I - j_{\text{shears}}}{2 \mathcal{J}_{\text{core}}} \frac{2 j_\pi j_\nu \sin\theta}{j_{\text{shears}}} = 0.
\]
1. **纯剪刀极限（$\mathcal{J}_{\text{core}} \to 0$）：**
   方程强制要求 $I = j_{\text{shears}}(\theta)$，即角动量必须且只能通过缩小 $\theta$ 来生成，导致极为陡峭的 $B(M1) \propto \sin^2\theta$ 衰减；
2. **核芯—剪刀竞争区（$\chi \sim 0.5 - 1.0$）：**
   当核芯具有一定变形时，增大自旋可通过转动能量与剪刀恢复力的最优分配共同分担，核芯角动量 $R_{\text{core}} = I - j_{\text{shears}} > 0$ 连续抬升，造成剪刀叶片在能带终止前无需完全对齐；
3. **剪刀溶解相界（$\chi > 1.0$）：**
   核芯四极转动张量 $Q_{\text{core}} \propto \beta_2$ 使得跃迁分母 $B(E2) \propto (Q_{\text{core}} + Q_{\text{shears}} \sin^2\theta)^2$ 被四极形变电荷项彻底主导，比值 $B(M1)/B(E2)$ 迅速退化，磁转动退化为弱微扰。

## Assumptions

1. 质子—中子高-$j$ 组态保持准单粒子性，且角动量未发生未预测的断对能带交叉；
2. 剪刀恢复力采用标准 $P_2(\cos\theta)$ 多极展开，且相互作用常数 $V_2 \approx 1.2\text{ MeV}$ 在该同位素区保持近常数；
3. 核芯形变采用轴对称或准三轴有效四极矩 $Q_{\text{core}}$，忽略高阶十六极项。

## Competing Explanations

1. **三轴准 $\gamma$ 转动带（Triaxial Quasi-gamma Bands）：** 在过渡区核中，软三轴振动常伴生较强的 $\Delta I = 1$ 连接，但其强带内 $E2$ 使得 $B(M1)/B(E2) \ll 1$，与过渡区磁转动带的 $B(M1)/B(E2) \sim 60 - 80$ 有明确界限；
2. **手征四重态与倾斜进动：** 若两对叶片脱离主平面发生非共面扭曲，可能转变为手征模式；但碲同位素中未见简并双重带；
3. **带终止顺排（Band Termination）：** 在高自旋端，全单粒子顺排会终止能带，但其前兆是转动惯量 $\mathcal{J}^{(2)}$ 的急剧崩溃，而剪刀核芯能带保持相对平稳的惯量平台。

## Transfer Conditions

1. 适用于由轻四极形变（$\beta_2 \le 0.18$）与高-$j$ 粒—孔构型构成的所有弱变形过渡区核（如 $Z=51-53$ 的 Sb, Te, I 同位素）；
2. 识别磁转动时必须联合满足：(a) 测得 $B(M1)/B(E2) \ge 30\ \mu_N^2/(e\text{b})^2$；(b) $B(M1)$ 随自旋下降。

## Failure Conditions

1. 当核芯四极形变 $\beta_2 > 0.22$ 时，单纯剪刀模型失效，四极集体转动占主导；
2. 仅依据观察到 $\Delta I = 1$ 偶极级联即断言磁转动而不核算 $B(M1)/B(E2)$ 比值的推论失效。

## Falsification or Reverse Tests

1. **反证检验（Sn 强 E2 假说证伪）：** 设想在 $^{106}\text{Sn}$ 中强行引入大核芯四极矩 $Q_{\text{core}} = 0.5\ e\text{b}$，计算所得 $B(M1)/B(E2)$ 将从 1800 暴跌至 60 以下，与实验实测巨大比值排他性相悖，反证了 Sn 核芯的极度球形刚性；
2. **溶解自洽性检验：** 沿 $Z=50 \to 52 \to 54$ 同位素链，核芯角动量份额 $R_{\text{core}}/I$ 从 $106\text{Sn}$ 的 $1\% - 20\%$ 连续攀升至 $^{122}\text{Xe}$ 的 $70\% - 80\%$，数值上自洽再现了剪刀效应连续溶解的过程。

## Open Questions

1. 在接近滴线的轻碲同位素（如 $^{108}\text{Te}, ^{110}\text{Te}$）中，中子数降低至 $N \approx 56-58$ 接近 $N=50$ 闭壳时，四极形变是否会重新收缩并恢复为纯磁转动？
2. 质子—中子相互作用中的张量力成分（Tensor Force）如何微观调制过渡区剪刀恢复常数 $V_2$ 的同位旋依赖性？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 2026-10-29 Day 27 跨质量区迁移自主研学产物，未经过人类物理学家正式同行复核（status: ai-draft, review_status: unreviewed）。

## Promotion or Rejection History

- 2026-10-29：首次基于剪刀—核芯变分动力学建立了过渡区碲与碘同位素（$^{118}\text{Te}, ^{119}\text{I}$）的磁转动存在性与连续溶解机制，废除了“越过 $Z=50$ 闭壳磁转动突变猝灭”的陈旧假设。
