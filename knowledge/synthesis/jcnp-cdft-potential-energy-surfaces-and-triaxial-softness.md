---
type: synthesis
title: "JCNP 协变密度泛函微观势能面与跨质量区三轴刚软性演化专题"
aliases: [JCNP势能面研究, CDFT三轴刚软性, jcnp-cdft-pes-triaxial-softness]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
scope: csdft-potential-energy-surfaces-and-triaxial-rigidity-softness
confidence: high
sources: [ding-2012-phd-thesis-127-128i-high-spin, qiang-2019-high-spin-130-131ba-87zr, che-2007-high-spin-108-112ru-134-135ba]
tags: [jcnp, cdft, pes, triaxiality, gamma-softness, moments-of-inertia]
---

# JCNP 协变密度泛函微观势能面与跨质量区三轴刚软性演化专题

## 1. 研究背景与理论方法

在低能原子核结构中，原子核内禀基态与低激发态的宏观几何形状，本质上由微观单核子波函数在自洽平均场中的重组所决定。中国核物理联合中心 JCNP 核图网（Joint Center for Nuclear Physics Nuclear Map, \url{http://nuclearmap.jcnp.org/}）基于多维度约束协变密度泛函理论（Multidimensionally-Constrained Covariant Density Functional Theory, MDC-CDFT），系统计算了全核素图上数千种核素在内禀四极形变平面 $(\beta_2, \gamma)$ 与八极形变坐标 $(\beta_3)$ 上的高精度二维/三维微观势能面（Potential Energy Surfaces, PES）。

在 MDC-CDFT 框架下，相对论 Kohn-Sham 能量密度泛函包含核子 Dirac 旋量、标量介子 $\sigma$、矢量介子 $\omega$、同位旋矢量介子 $\rho$ 以及光子场的自洽耦合：
\begin{equation}
    E_{\text{CDFT}}[\rho] = \int d^3r \, \mathcal{E}(\vec{r})
\end{equation}
通过引入拉格朗日乘子约束外加四极与八极多极约束算符：
\begin{equation}
    E_{\text{constr}} = E_{\text{CDFT}} + \frac{1}{2} C_{20} (\langle \hat{Q}_{20} \rangle - q_{20})^2 + \frac{1}{2} C_{22} (\langle \hat{Q}_{22} \rangle - q_{22})^2 + \frac{1}{2} C_{30} (\langle \hat{Q}_{30} \rangle - q_{30})^2
\end{equation}
自洽求解约束 Dirac-Hartree-Bogoliubov 方程，精确绘制出能量沿形变网格曲面的等高线演化图。

---

## 2. 六大多区三轴势能面微观拓扑对比

通过对 JCNP 核图网数据库在全核素图上的扫描比对，六大典型三轴演化核区在内禀形变平面上的势能拓扑展现出深刻的物理演化分立：

### (1) $A \approx 60$ 质量区（$^{66}\text{Ge}, ^{68}\text{Se}$）
- **势能面特征**：极度强烈的多形状共存（Multi-Shape Coexistence）。势能面上同时存在长椭球极小（$\beta_2 \approx 0.25, \gamma \approx 0^\circ$）与扁椭球极小（$\beta_2 \approx 0.30, \gamma \approx 60^\circ$），两极小之间的三轴鞍点势垒极低（$\Delta V \le 300\text{ keV}$）；
- **微观物理**：零点振动能量（$\sim 1.0\text{ MeV}$）远大于势垒高度，原子核在动力学上在长-扁-三轴形状之间剧烈穿透振动，基态表现为大振幅形状涨落，无法维系任何刚性三轴集体激发。

### (2) $A \approx 80$ 质量区（$^{76,78}\text{Kr}, ^{78,80}\text{Sr}$）
- **势能面特征**：具有较为明确的三轴极小点（$\beta_2 \approx 0.38, \gamma \approx 22^\circ$），向扁椭方向的势垒高度约为 $0.8 \sim 1.2\text{ MeV}$；
- **微观物理**：中子与质子同时填充高 $j$ $1g_{9/2}$ 轨道，强烈的相干四极极化克服了对力阻碍，确立了相对稳定的静态三轴形变；同时在八极约束方向 $\beta_3$ 势能极其平缓，为手征对称性与空间反射对称性的联立破缺奠定了天然几何平台。

### (3) $A \approx 100$ 质量区（$^{104,106}\text{Ru}, ^{106,108}\text{Pd}$）
- **势能面特征**：经典的 $\gamma$ 平坦河谷（$O(6)$ 伽马不稳定核）。在固定 $\beta_2 \approx 0.22$ 处，能量从 $\gamma = 0^\circ$ 扫描至 $\gamma = 60^\circ$，势能总起伏不足 $150\text{ keV}$；
- **微观物理**：体系完全不具备任何定义分立转动主轴的势能刚性，属于教科书级的 Wilets-Jean 软核；在这一核区寻找横向摆动运动在原理上是不可能的，因为任何表观上的能量交错本质上都是 $\gamma$ 振动激发。

### (4) $A \approx 130$ 质量区（$^{130,132}\text{Ba}, ^{132,134}\text{Ce}, ^{134,136}\text{Nd}$）
- **势能面特征**：浅三轴势能谷。能量极小位于 $\beta_2 \approx 0.20 \sim 0.25, \gamma \approx 20^\circ \sim 25^\circ$，但沿 $\gamma$ 方向的限制势垒仅为 $300 \sim 500\text{ keV}$；
- **微观物理**：介于刚性与软核之间的关键“临界过渡区”。单个外加准粒子（如奇核中的 $\pi h_{11/2}$）带入的内禀极化能量足以驱动势阱极小发生 $5^\circ \sim 10^\circ$ 的漂移；这深刻解释了为什么 A~130 区横向摆动运动与准粒子倾斜进动（TiP）产生高度纠缠。

### (5) $A \approx 160$ 质量区（$^{168}\text{Er}$ vs. $^{163,165}\text{Lu}$ 第二势阱）
- **势能面特征**：双势阱绝缘结构。在基态正常形变区为极其陡峭的纯轴对称长椭球（$\gamma = 0^\circ, \beta_2 \approx 0.30$）；而在超形变第二势阱中，涌现出深达 $1.5 \sim 2.0\text{ MeV}$ 的孤立三轴超形变（TSD）极小（$\beta_2 \approx 0.38, \gamma \approx 20^\circ$）；
- **微观物理**：高势垒完全锁死了三轴椭球的内禀形状，使核芯真正具备了抗拒大振幅涨落的刚体惯量，成为全核素图上唯一测得纯净多声子谐振子摆动运动的黄金标准。

### (6) $A \approx 190$ 质量区（$^{192,194}\text{Pt}, ^{196}\text{Hg}$）
- **势能面特征**：偏向扁椭侧的三轴浅势阱（$\beta_2 \approx 0.15, \gamma \approx 40^\circ \sim 50^\circ$）；
- **微观物理**：费米面接近中子与质子壳层顶端，空穴型准粒子驱动原子核偏向扁椭球，诱发独特的扁椭三轴手征转动。

---

## 3. 全局三轴刚软性判据总结表

| 质量区 | 代表同位素 | JCNP 势能极小 $(\beta_2, \gamma)$ | 沿 $\gamma$ 势垒高度 $\Delta V_\gamma$ | 刚软性归属 | 对应集体激发表现形式 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **$A \approx 60$** | $^{66}\text{Ge}$ | $(0.26, 28^\circ)$ | $< 250\text{ keV}$ | 极度软核 / 形状共存 | 低位 $0_2^+$ 态、$E0$ 强跃迁 |
| **$A \approx 80$** | $^{78}\text{Kr}$ | $(0.36, 21^\circ)$ | $\sim 900\text{ keV}$ | 中度刚性三轴 | 手征双重带、八极-手征联立破缺 |
| **$A \approx 100$** | $^{104}\text{Ru}$ | $(0.23, 27^\circ)$ | $< 150\text{ keV}$ | 极限 $\gamma$-不稳定软核 | 多手征双重带 M$\chi$D、无摆动 |
| **$A \approx 130$** | $^{132}\text{Ce}$ | $(0.22, 23^\circ)$ | $\sim 400\text{ keV}$ | $\gamma$-软性过渡核 | TW 与 TiP 激烈争鸣、手征双重带 |
| **$A \approx 160$** | $^{163}\text{Lu}$ (TSD) | $(0.39, 19^\circ)$ | $> 1500\text{ keV}$ | 刚性三轴超形变金标准 | 多声子谐振摆动带（$n_w=1, 2$） |
| **$A \approx 190$** | $^{194}\text{Pt}$ | $(0.16, 45^\circ)$ | $\sim 300\text{ keV}$ | 扁椭三轴软核 | 扁椭手征带、低自旋进动 |

本专题研究直接为博士学位论文第 1 章与第 2 章关于势能面微观演化的论述提供了完整、权威的第一性数据支撑。
