---
type: method
title: "Zhao 等：含时协变密度泛函理论（TD-CDFT）手征进动与微观隧穿动力学合同"
aliases: [Zhao TDCDFT chiral dynamics, TDCDFT chiral precession, 135Nd microscopic chiral tunneling, 3D Kohn-Sham-Dirac time evolution, Fourier chiral excitation spectrum]
method_type: "microscopic-tdcdft-chiral-dynamics-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Chirality and Wobbling in Atomic Nuclei Ch.9, PDF pp.204-221, full chapter reading"
confidence: "high for formalisms, calculated curves, and reported data; conditional for model parameter choices"
tags: [td-cdft, 3dtac-cdft, chiral-precession, quantum-tunneling, 135nd, pc-pk1, mchid, fourier-spectral-analysis]
sources: [book-petrache-chirality-and-wobbling]
---

# Zhao 等：含时协变密度泛函理论（TD-CDFT）手征进动与微观隧穿动力学合同

## Purpose

本方法合同基于李博、赵鹏巍在专著《Chirality and Wobbling in Atomic Nuclei》第 9 章的系统研究，
解决低能核结构中微观平均场模型无法直接描述核手征性大振幅量子振动与左右手势阱间微观穿隧的理论难题：
通过建立全三维真实空间含时协变密度泛函理论（TD-CDFT）与静态三维倾斜轴推转协变密度泛函理论（3DTAC-CDFT）的自洽结合，
完全摆脱半经典唯象势能面拟合与冻结核芯假设，在无需引入任何超出相对论能量密度泛函（PC-PK1）的自由参数条件下，
追踪总角动量矢量在内禀主轴坐标系下的全动力学实时间演化轨迹，确立以下关键微观合同：

1. **全微观手征进动（Chiral Precession）图景**：在内禀惯量主轴系中，角动量矢量 \(\vec J(t)\) 绕 \((s-l)\) 平面内的倾斜轴做微观闭合进动；极角 \(\theta_J(t)\) 与方位角 \(\varphi_J(t)\) 的轨道在能量曲面上构成闭合椭圆轨迹；
2. **手征激发能的傅里叶谱分析提取法（图 9.1–9.6）**：通过对实时间演化轨迹进行高精度傅里叶谱分析，在谐振进动极限下，谱功率主峰中心值严格对应手征伴随带的微观激发能量 \(E^*(I)\)；
3. **从简谐手征振动向静态手征微观穿隧相变（图 9.7）**：揭示低自旋区（单势阱、谐振进动、单峰谱）随着自旋升高能面沿方位角 \(\varphi_J\) 急剧变软、非简谐效应加剧，并在临界自旋（如 \(^{135}\mathrm{Nd}\) 正宇称带 \(I=31/2\hbar\)）处发生超临界分岔，形成由 \(\varphi_J=0^\circ\) 势垒阻隔的对称双阱；展现势垒下方局域（静态手征）与跨势垒非简谐贯穿（量子穿隧）的动力学相空间图景；
4. **\(^{135}\mathrm{Nd}\) 偶奇核多重手征双重带（M\(\chi\)D）全微观能谱再现（图 9.8–9.16）**：针对正宇称三准粒子构型 \(\pi[h_{11/2}(gd)^1] \otimes \nu h_{11/2}^{-1}\) 与负宇称构型 \(\pi h_{11/2}^2 \otimes \nu h_{11/2}^{-1}\)，全微观无参数再现两对手征双重带能级谱。

## Inputs and Assumptions

### Relativistic point-coupling Lagrangian and 3DTAC-CDFT

微观能量密度泛函基于相对论点耦合相互作用拉格朗日量（PC-PK1，式 9.1–9.2），包含自由核子动能项、标量/矢量四费米子接触项、介质极化高阶项、有限力程梯度导数项及电磁相互作用。
通过自洽求解旋转参考系下的狄拉克方程式 (9.4)：

\[
\left[ \vec\alpha \cdot (\hat{\vec p} - \vec V) + V_0 + \beta(m_N + S) - \vec\omega \cdot \hat{\vec J} \right] \psi_k(\vec r) = \epsilon_k \psi_k(\vec r) ,
\]

其中转动频率 \(\vec\omega\) 的大小与总自旋通过半经典量子化条件 \(\langle\hat{\vec J}\rangle \cdot \langle\hat{\vec J}\rangle = I(I+1)\) 约束，方向由最小化总 Routhian 自洽确定。

### Real-time TD-CDFT evolution in 3D coordinate space

初始微观 Slater 行列式由偏离平衡态的约束 3DTAC-CDFT 给出。波函数实时间动力学由含时非线性狄拉克方程控制：

\[
i\hbar \frac{\partial}{\partial t}\psi_k(\vec r, t) = \hat h(\vec r, t) \psi_k(\vec r, t) ,
\]

其中时间依赖的标量势 \(S(\vec r, t)\) 与四维矢量势 \(V^\mu(\vec r, t)\) 由核子时空密度 \(\rho_S\) 与四维流 \(j^\mu\)（式 9.9–9.10）自洽生成。

**数值实现规范**：
- 空间网格步长取为 \(0.8\text{ fm}\)，三维立方计算盒尺寸为 \(24\times24\times24\text{ fm}^3\)；
- 采用预估–校正（Predictor-corrector）步进算法，时间步长取为 \(\Delta t = 0.1\text{ fm}/c\)；
- 总角动量在空间固定系严格守恒，通过在每一个时间步长实时计算核物质惯性主轴张量，将角动量矢量投影到瞬时内禀坐标主轴（短轴 \(s\)、中间轴 \(m\)、长轴 \(l\)），获得极角 \(\theta_J(t)\) 与方位角 \(\varphi_J(t)\) 的动态动力学轨迹。

## What It Can Establish

### 1. 手征进动（Chiral Precession）与动力学对称性

由 TD-CDFT 导出的相空间轨迹展现出深层规律：

- 角动量在内禀空间的轨迹呈现关于平衡极小点的闭合椭圆（图 9.1）；
- 在方位角 \(\varphi_J\) 方向的摆动振幅系统性大于极角 \(\theta_J\) 方向，这是因为势能面在中间轴方向呈现相对松弛的扁椭形状；
- \(\varphi_J(t)\) 轨迹同时跨越正值与负值区间，微观反映了系统在左手参考系与右手参考系之间的动力学进动遍历；该现象被命名为**手征进动（Chiral Precession）**。

### 2. 傅里叶谱功率与手征双重带激发能 \(E^*(I)\)

对时间序列 \(\theta_J(t)\) 与 \(\varphi_J(t)\) 执行傅里叶频域分析：

- 在低自旋区（如 \(^{135}\mathrm{Nd}\) 的 \(I = 19/2, 21/2, 23/2, 25/2\hbar\)），不同初始偏离角（如 \(\varphi_J=10^\circ, 20^\circ\)）激发的进动轨迹表现出严格全同的基频与谱峰中心值（图 9.1–9.4）；
- 谱峰能量中心值对应手征激发的微观量子能量：\(E^* = 0.29\text{ MeV}\)（\(19/2\hbar\)）、\(0.26\text{ MeV}\)（\(21/2\hbar\)）、\(0.24\text{ MeV}\)（\(23/2\hbar\)）、\(0.20\text{ MeV}\)（\(25/2\hbar\)），呈现单调下降趋势；
- 伴随带能级由静态基态 Routhian 加上傅里叶激发能 \(E^*(I)\) 直接重构，消除了唯象转子惯量参数调整。

### 3. 超临界分岔与微观势垒穿隧相变（图 9.7）

随着自旋升高向临界自旋演化：

- **能面变软与非简谐加剧（\(I=27/2, 29/2\hbar\)）**：势能面在方位角 \(\varphi_J\) 方向极度软化，轨迹被压扁，不同初始偏离激发出的谱峰中心出现 \(0.01\)–\(0.03\text{ MeV}\) 的频移，标志着微观进动开始偏离简谐假定；
- **双阱对称自发破缺与势垒穿隧（\(I=31/2\hbar\)）**：
  - 势能面在 \((\theta_J, \varphi_J) = (59^\circ, \pm 25^\circ)\) 处自发形成两个能量严格简并的深极小，中间由位于 \(\varphi_J = 0^\circ\)（共面）的能量势垒阻隔；
  - 初始能量低于势垒的轨迹被严格局域在左手或右手极小附近的闭合轨道中，代表**静态手征转动**；
  - 初始能量高于势垒的轨迹则横跨左右两个非共面势阱，展现大振幅**量子势垒穿隧**；
  - 进动周期与振幅发生显著畸变，微观上展现了从软手征振动向静态手征双阱隧穿相变的相空间全景。

### 4. \(^{135}\mathrm{Nd}\) 多重手征带 M\(\chi\)D 微观再现（图 9.8–9.16）

针对负宇称 3 准粒子态 \(\pi h_{11/2}^2 \otimes \nu h_{11/2}^{-1}\)（涵盖 \(I = 27/2\hbar\) 至 \(41/2\hbar\)）：

- 轨迹显示全区平衡点均处于 \(\varphi_J=0^\circ\)，手征进动激发能由 \(0.29\text{ MeV}\) 逐渐降至 \(0.20\text{ MeV}\)；
- 结合正宇称态与负宇称态，图 9.16 证明 TD-CDFT 与 3DTAC-CDFT 联合给出的双重带能级不仅精准再现了实验测定的双带能隙与斜率，而且完全基于微观相对论核力 PC-PK1，无任何人造有效质量或带头平移参数。

## Experimental and Dynamical Analysis Contract

将含时密度泛函理论用于指导或解释手征实验数据时，应遵循以下合同准则：

1. **区分时域进动描述符与量子本征态**：
   TD-CDFT 给出的是波包均值的半经典实时间轨迹，其傅里叶谱峰中心是跃迁能量的直接对应，但不能直接替代全正交手征基底上的严格量子几率波函数（如 GCM 或投影态）；
2. **识别势能面软化导致的频移不确定度**：
   在接近手征分岔临界点时，由于非简谐势能导致频域主峰展宽并产生初始振幅依赖（\(\sim 20\)–\(30\text{ keV}\) 不确定度），必须在报告中声明该动态非简谐误差；
3. **势垒隧穿与静态手征判定**：
   只有在能面上出现明确的 \(\pm\varphi_J\) 对称双极小且势垒高度大于零点能振幅时，才能判定进入静态手征转动相；在单一平底势阱中发生的左右横扫属于手征进动振动；
4. **全质子/全中子流自洽演化**：
   计算必须包含全部空间流分布 \(j^\mu(\vec r, t)\)，不能使用刚体核芯转动惯量替代流分布随自旋的自洽响应。

## What It Cannot Establish Alone

- 单纯 TD-CDFT 轨迹演化属于单行列式含时演化，无法直接求解左右手波函数线性杂化后的严格微观奇偶本征态（需要进行时域 GCM 或路径重量子化）；
- 傅里叶能量提取法适用于定常进动，无法直接处理伴随剧烈粒子发射或阻尼退激的瞬态耗散过程；
- 泛函未包含超出平均场的动态对振动，在极低自旋（\(I \le 15/2\hbar\)）受对起伏影响可能存在系统性偏差。

## Knowledge Impact and Learning Decision

赵鹏巍等人的第 9 章将核手征性的微观理论从静态自洽场推进到实时间空间动力学时代：
它首次在无参数相对论泛函高度统一了手征进动概念、相空间椭圆轨道、傅里叶谱能量提取、超临界双阱分岔与势垒穿隧，
全微观再现了 \(^{135}\mathrm{Nd}\) 的两对多重手征能带，
为 Wiki 奠定了从时域非线性动力学连接频域离散谱学实验的最高层全微观理论合同。

本单元完成第 9 章全文、微观公式推导及图 9.1–9.16 的全面精读与核验。

## Evidence and Locators

- Ch.9 pp.185–187 / physical PDF pp.204–206：核手征性背景、全球实验概况、手征振动与静态手征转变概念；
- Ch.9 pp.187–189 / physical PDF pp.206–208：PC-PK1 点耦合拉格朗日量式 (9.1)–(9.2)、局域密度与流式 (9.3)、3DTAC-CDFT 旋转狄拉克方程式 (9.4)–(9.5)、含时 TD-CDFT 狄拉克时域演化式 (9.6)–(9.10)；
- Ch.9 pp.189–194 / physical PDF pp.208–213：\(^{135}\mathrm{Nd}\) 正宇称带手征进动轨迹（图 9.1–9.6）、傅里叶谱功率单峰、激发能 \(E^*\) 提取；
- Ch.9 pp.192–194 / physical PDF pp.211–213：\(I=31/2\hbar\) 超临界分岔、双阱势垒、左右构型微观势垒穿隧动力学（图 9.7）；
- Ch.9 pp.194–200 / physical PDF pp.213–219：\(^{135}\mathrm{Nd}\) 负宇称带进动轨迹与谱分析（图 9.8–9.15）、两对手征双带微观能谱再现与实验对账（图 9.16）；
- Ch.9 pp.200–201 / physical PDF pp.219–220：总结与重量子化前沿展望；
- 已渲染核对 PDF pp.208、211、213、214、219、220。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[chen-cdft-prm-wobbling-and-fermi-surface-contract]]
- [[chiral-vibrational-tunneling-and-double-well-splitting]]
- [[chiral-geometry-tilted-axis-cranking-and-aplanarity]]
- [[multiple-chiral-doublets-and-chiral-parity-quartets]]
- [[odd-odd-chiral-mep-instanton-tunneling]]
