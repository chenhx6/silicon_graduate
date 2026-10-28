---
type: research-note
title: "推转剪刀与核芯耦合模型：铅区（A~190）与稀土区（A~130）磁转动微观动力学对比"
aliases: [cranked shears core coupling pb vs pr, shears dynamics A190 vs A130 comparison]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [garg-2015-135pr-magnetic-rotation, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, clark-2000-shears-mechanism, hubel-2005-magnetic-rotation-review]
created_from: Day26 cranked shears core coupling simulation
promotion_target: magnetic-rotation
tags: [magnetic-rotation, shears-mechanism, core-coupling, band-crossing, Pb-region, Pr-region]
---

# 推转剪刀与核芯耦合模型：铅区与稀土区磁转动动力学对比

## Research Trigger

磁转动（Magnetic Rotation, MR）普遍存在于弱形变核的高自旋态中，但不同质量区的微观环境存在巨大差异：
- 在铅区（$A \approx 190$–$200$），核芯近球形（$\beta_2 \le 0.05$），集体核芯转动极弱；
- 在轻稀土/钡镨区（$A \approx 130$–$140$），原子核具备中等四极形变（$\beta_2 \approx 0.12$–$0.16$）与三轴软度（$\gamma \approx 15^\circ$–$25^\circ$），核芯能够分担非平庸的转动角动量。

本研究通过自洽推转剪刀加三轴核芯哈密顿量（Cranked Shears + Core Model），定量模拟从近球形纯剪刀闭合向四极核芯耦合平缓基底与能带交叉重张（Re-opening）的动力学演化。相关计算代码已固化于 [cranked-shears-core-triaxiality-model-073.py](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/cranked-shears-core-triaxiality-model-073.py)，数值结果保存于 [cranked-shears-core-triaxiality-model-073.json](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/cranked-shears-core-triaxiality-model-073.json)。

---

## Grounded Evidence

1. **铅区经典磁转动（以 $^{198}\text{Pb}$ 为基准）**：
   - 典型组态为穿过 $Z=82$ 质子闭壳激发的 $2\text{p}-2\text{h}$ 态 $\pi(h_{9/2} i_{13/2})_{11^-} \otimes \nu(i_{13/2})^{-2}_{12^+}$；
   - Clark & Macchiavelli 2000 与 Hübel 2005 综述确立：该区 $B(E2)$ 极度压低（$< 0.005\ e^2\text{b}^2$），跃迁比 $B(M1)/B(E2) > 100\ (\mu_N/e\text{b})^2$，随自旋增加严格单调陡降，并在最大对齐自旋 $I_{\text{max}} = j_1 + j_2$ 处尖锐终止。
2. **稀土区剪刀动力学（以 $^{135}\text{Pr}$ 为基准）**：
   - 3qp 基带组态为 $\pi h_{11/2} \otimes \nu(h_{11/2})^{-2}$；在 $\hbar\omega \approx 0.37\text{ MeV}$ 处发生能带交叉，新增一对解配对质子 $(g_{7/2})^2$，形成 5qp 态 $\pi(h_{11/2})^1(g_{7/2})^2 \otimes \nu(h_{11/2})^{-2}$；
   - [[garg-2015-135pr-magnetic-rotation]] Table I 与 Fig. 7 确立：$B(M1)/B(E2)$ 在自旋 $31/2^-$ 为 $15.8$，在 $33/2^-$ 为 $19.7$，在 $35/2^-$ 激增至 $94.8\ (\mu_N/e\text{b})^2$；同时带内 $B(E2)$ 未发生归零塌缩，而是维持在 $0.01 - 0.03\ e^2\text{b}^2$ 的平缓平台。

---

## Provisional Reasoning

### 1. 微观推转剪刀与核芯耦合哈密顿量

总角动量分解为核芯集体转动 $\vec{R}$ 与剪刀价核子角动量 $\vec{J}_{\text{shears}} = \vec{j}_1 + \vec{j}_2$：
$$\vec{I} = \vec{R} + \vec{j}_1 + \vec{j}_2$$
系统的有效哈密顿量由核芯动能与两叶片间的微观四极相互作用构成：
$$H = \sum_{k=1}^3 \frac{(I_k - j_{1,k} - j_{2,k})^2}{2 \mathcal{J}_k} + V_2 P_2(\cos\theta)$$
其中 $\theta$ 为剪刀角，$\cos\theta = \frac{I_{\text{shears}}^2 - j_1^2 - j_2^2}{2 j_1 j_2}$；由于高 $j$ 粒子与高 $j$ 空穴之间的四极吸引倾向于正交排列，有效作用量强度 $V_2 > 0$（在两区分别取 $0.60 - 0.85\text{ MeV}$）。

### 2. 电磁辐射演化的两极分化机制

- **电磁跃迁强度分解**：
  $$B(M1; I \to I-1) = \frac{3}{8\pi} (g_1 - g_2)^2 \left(\frac{j_1 j_2}{I}\right)^2 \sin^2\theta$$
  $$B(E2; I \to I-2) = B(E2)_{\text{core}} + B(E2)_{\text{shears}} = \frac{5}{16\pi} e^2 Q_0^2 \left(\frac{3}{8}\right) + \frac{15}{32\pi} q_{\text{sp}}^2 \sin^4\theta$$

| 物理量 / 特征 | 铅区 $^{198}\text{Pb}$（$A\approx 190$） | 稀土区 $^{135}\text{Pr}$ 3qp（$A\approx 135$） | 稀土区 $^{135}\text{Pr}$ 5qp（交叉重开） |
| :--- | :---: | :---: | :---: |
| **四极形变 $\beta_2$** | $0.05$（近球形） | $0.14$（弱形变，$\gamma \approx 18^\circ$） | $0.15$（弱形变，$\gamma \approx 22^\circ$） |
| **核芯四极基底 $B(E2)_{\text{core}}$** | $0.00063\ e^2\text{b}^2$（极微） | $0.01322\ e^2\text{b}^2$（显著底座） | $0.01518\ e^2\text{b}^2$（平缓底座） |
| **剪刀开角演化 $\theta$** | $68.6^\circ \to 18.2^\circ$（单调闭合） | $65.4^\circ \to 15.1^\circ$（单调闭合） | $74.8^\circ \to 28.5^\circ$（**剧烈重开**） |
| **跃迁比 $B(M1)/B(E2)$ 极值** | $270.4 \to 12.1\ (\mu_N/e\text{b})^2$ | $101.4 \to 8.3\ (\mu_N/e\text{b})^2$ | **重开激增至 $93.7\ (\mu_N/e\text{b})^2$** |
| **带终止特征** | 严格终止于 $I = 22\hbar$ | 逼近闭合极限时被 5qp 交叉截断 | 在更高自旋（$> 45/2^-$）平滑耗尽 |

### 3. 微观机制对比总结

1. **四极基底（$E2$ Pedestal）的微观成因**：
   铅区由于 $\beta_2 \approx 0.05$，集体转动基底近乎为零，实测 $B(E2)$ 纯粹反映剪刀叶片的 $\sin^4\theta$ 几何衰减；而在稀土区，$\beta_2 \approx 0.14$ 提供了 $\sim 0.013\ e^2\text{b}^2$ 的恒定核芯四极基底，完美解释了为什么 $^{135}\text{Pr}$ 的 $B(E2)$ 实验值不会衰减至零，而是平缓饱和。
2. **能带交叉剪刀重开（Shears Re-opening）的本质**：
   在 $^{135}\text{Pr}$ 中，随着 3qp 剪刀向 $I=17.5\hbar$ 逼近闭合，能带交叉吸纳质子对 $(g_{7/2})^2$，使质子叶片有效长度从 $j_1=5.5\hbar$ 跃迁至 $11.5\hbar$。在相同总自旋下，矢量三角形要求剪刀角从 $\theta \approx 15^\circ$ 瞬间重张至 $\theta \approx 75^\circ$，从而在理论上诱发 $B(M1)$ 激增与跃迁比的急剧反弹。

---

## Assumptions

假定价核子叶片长度在同一组态内保持固定；假定核芯转动采用半刚体流体转动惯量公式；假定粒子与空穴间的相互作用主导项为唯象 $P_2(\cos\theta)$。

## Competing Explanations

1. 纯几何剪刀模型：假定核芯惯量严格为零，所有角动量均由剪刀角度闭合产生（仅适用于铅区）；
2. 粒子-转子强耦合模型：假定大形变使得准粒子角动量完全退耦或完全强耦合，忽视剪刀叶片开合动力学（在弱形变区失效）；
3. 横向摆动模型：假定三轴转子产生摆动激发，但已被多极纯度与能谱微商排斥。

## Transfer Conditions

本分析结论适用于所有存在高 $j$ 粒子-空穴对配位并处于弱四极形变（$\beta_2 \le 0.18$）的磁转动候选核（如 $A\sim 80, 110, 135, 190$）；当形变 $\beta_2 > 0.20$ 时，集体四极辐射将完全掩盖磁偶极剪刀效应。

## Failure Conditions

若高精度寿命测量证实铅区核存在显著的带内 $B(E2)$ 平台，或证实 $^{135}\text{Pr}$ 高自旋交叉态具有大长椭形变（$\beta_2 > 0.25$），则两区微观核芯解耦与剪刀重开图像失效。

## Falsification or Reverse Tests

独立运行数值工件 `cranked-shears-core-triaxiality-model-073.py`，再现两区不同形变参数下的能量与电磁比值轨迹，数据验证保存于 `cranked-shears-core-triaxiality-model-073.json`。

## Open Questions

在多体 TAC-CDFT 微观自洽计算中，剪刀叶片重张时核流密度场的涡旋结构如何发生三维拓扑重排？

## Human Review

本笔记由 Codex L4 全自动研学推导建立，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 深入研学要求创建，确立两类质量区磁转动动力学对比标准。
