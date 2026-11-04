---
name: nuclear-experimental-methods
description: "吴治华《原子核物理实验方法》（第三版）与在束实验设计指南：死时间双根判据、HPGe效率拟合、真符合求和、符合矩阵本底扣除、RDM/DSAM寿命测量、重离子实验机时预算及与《粒子探测技术》视界解冲突手册。"
---

<!-- argument-hint: [topic, method, detector, or chapter number] -->

# 原子核物理实验方法与在束实验设计指南（吴治华，第三版）

**著者**：吴治华（复旦大学现代物理研究所） | **出版社**：原子能出版社 (2005) | **页数**：483 页
**本地原件**：`raw/books/原子核物理实验方法--第三版 (吴治华) (Z-Library).pdf` (SHA-256 `e23f010ff8d3b4737405235c4aba920533f44e89409ebb7e2cb076b7ab4ee591`)

本技能将吴治华《原子核物理实验方法》这一国内实验核物理领域的标准权威专著转化为可反复调用的智能体技能，为在束 $\gamma$ 谱学实验设计、探测器阵列搭建、死时间校正、探测效率标定、寿命测量及与高能探测教材（汪晓莲《粒子探测技术》）的视界解冲突提供完备的方法论与实操工具箱。

## How to Use This Skill

- **实验设计咨询**：询问 `如何设计在束实验`、`机时预算计算`、`靶厚度与衬底选取`、`反冲初速度 v/c`、`束流发热与冷却`；
- **数据分析校正**：询问 `死时间双根判决`、`脉冲发生器活时间标定`、`HPGe效率拟合`、`真符合求和校正`、`二维符合矩阵扣本底`；
- **能态寿命反演**：询问 `RDM 活塞反冲距离法`、`DDCM 差分衰变曲线法`、`DSAM 多普勒频移衰减法`、`ZBL 阻止本领`；
- **教材视界解冲突**：询问 `吴治华与汪晓莲的区别`、`死时间模型冲突`、`成形时间冲突`、`走动与晃动定时冲突`、`中子辐射损伤补偿`；
- **按章节查阅**：调用 `ch01`（统计与死时间）、`ch05`（半导体探测器）、`ch10`（$\gamma$ 能量与效率）、`ch11`（带电粒子鉴别）、`ch15`（核寿命测量）或 `reconciliation`（解冲突手册）。

---

## Core Frameworks and Mental Models

1. **放射性统计与高计数率死时间双根判决（第 1 章 §1.5）**：
   - **非扩展型（Non-paralyzable）**：真实输入率 $m = n / (1 - n \tau_N)$；
   - **扩展型（Paralyzable）**：记录率 $n = m e^{-m \tau_P}$，在 $m = 1/\tau_P$ 处达到最大记录率 $n_m_{\max} = 1/(e \tau_P)$；
   - **高计数率双根危险**：当 $n < n_m_{\max}$ 时，方程存在两个实数根 $m_1 < 1/\tau_P$（物理正常分支）与 $m_2 > 1/\tau_P$（严重阻塞瘫痪分支）。绝不能脱离计数率连续监测盲目套用公式；必须采用**周期性脉冲发生器（Pulser injection）**注入前放测试端，通过实测活时间分数 $f_{\text{live}} = N_{\text{meas}} / N_{\text{injected}}$ 实现模型无关的绝对计数恢复。

2. **HPGe 探测器微观物理与高精度效率标定（第 5、10 章）**：
   - **能量分辨率三要素**：$(\text{FWHM})^2 = (2.355 \sqrt{F \epsilon E_\gamma})^2 + (\text{FWHM})_{\text{noise}}^2 + (\text{FWHM})_{\text{drift}}^2$，其中 Fano 因子 $F \a0.10$，有效电离能 $\epsilon_{\text{Ge}} = 2.96\text{ eV}$；
   - **全能峰效率曲线拟合**：采用对数高阶多项式 $\ln\epsilon = \sum_{k=0}^N a_k (\ln E_\gamma)^k$（低能区 $100 - 500\text{ keV}$ 与高能区 $500 - 3000\text{ keV}$ 分段拟合或统一五阶拟合）；
   - **真符合求和（True Coincidence Summing, TCS）校正**：级联 $\gamma$ 射线在紧凑立体角下同时被同一晶体吸收，导致单峰计数损失（Summing-out）或全能虚假加和峰（Summing-in），必须在近距离标定时进行几何立体角立体修正。

3. **在束 $\gamma-\gamma$ 符合矩阵与 Radford 本底扣除（第 10 章）**：
   - 建立能量-能量二维符合矩阵 $M(E_1, E_2)$；
   - **Radford 算法**：总符合矩阵扣除展宽连续谱与偶然符合本底：
     $$N_{ij}^{\text{net}} = M_{ij} - \frac{B_i T_j + B_j T_i}{T_{\text{tot}}} + \frac{B_i B_j}{T_{\text{tot}}},$$
     其中 $T_i$ 为一维投影谱总计数，$B_i$ 为平滑连续谱本底；现代分析配合 2D SNIP（Sensitive Nonlinear Iterative Peak clipping）自动扣除二维康普顿散射脊。

4. **核激发态短寿命反演方法学（第 15 章）**：
   - **反冲距离法（RDM / Plunger，$\sim 1\text{ ps} - 1\text{ ns}$）**：靶与阻挡箔之间设置微米级可调距离 $d$。由移动峰 $I_u$ 与停止峰 $I_s$ 的强度比随距离变化：
     $$R(d) = \frac{I_u(d)}{I_u(d) + I_s(d)} = \exp\left(-\frac{d}{v \tau}\right).$$
     现代数据处理采用差分衰变曲线法（DDCM），直接对 $d I_s / dd$ 微分求斜率，彻底消除未知级联侧馈（side-feeding）延迟影响；
   - **多普勒频移衰减法（DSAM，$\sim 10\text{ fs} - 2\text{ ps}$）**：反冲核在厚靶或高 $Z$ 衬底中放慢减速（减速时间 $t_{\text{stop}} \sim 1\text{ ps}$）。$\gamma$ 跃迁在运动中发射产生连续多普勒线形（Doppler lineshape），通过输入 ZBL 核阻止截面与电子阻止截面进行 Monte Carlo 放慢积分反演寿命 $\tau$。

5. **重离子在束核反应实验设计全流程**：
   - **出射道与能量优化**：利用 Bass 库仑势垒模型与统计蒸发代码（PACE4）计算出射道激发函数，确定最佳束流能量 $E_{\text{lab}}$ 使目标蒸发道截面 $\sigma_{\text{target}}$ 最大化；
   - **靶设计**：角分布/偏振测量采用薄靶加高 $Z$ 金衬底（Au backer，厚度 $\ge 15\text{ mg/cm}^2$），使反冲核在 $\sim 1\text{ ps}$ 内完全阻停于立方晶格金点阵中，完全消除超精细场真空退取向效应（$G_k \to 1.0$）；测寿命则采用自支撑超薄箔；
   - **束流发热与机时预算**：评估束流功率沉积 $P = I_p \cdot \Delta E_{\text{target}}$，加装静电摇摆器扩大束斑防止烧靶；基于目标弱线分支比计算有效双符合事件数与纯物理曝光机时。

6. **吴治华 vs 汪晓莲教材视界解冲突体系**：
   - 明确低能核谱学（追求极端能量分辨率 $\Delta E/E \sim 10^{-3}$，成形时间微秒级，HPGe+BGO，CFD 零交叉消除走动）与中高能粒子物理（追求极高计数率 MHz、空间位置精度微米级，纳秒级短成形防堆积，MIP Landau 展宽，硅微条/气体室，首光子极低阈定时）的任务边界。

---

## Chapter Index

| # | 章节主题 | 核心实操内容 |
|---|---|---|
| [ch01](chapters/ch01-statistics-and-deadtime.md) | 放射性测量统计与死时间 | 非扩展型/扩展型死时间方程、双根退化、双源法、Pulser 活时间标定 |
| [ch05](chapters/ch05-hpge-detectors-and-signal.md) | 半导体探测器与电荷收集 | HPGe 同轴电极结构、载流子饱和漂移速度、前置放大器、电荷灵敏回路 |
| [ch10](chapters/ch10-gamma-energy-and-efficiency.md) | $\gamma$ 射线能量与效率测量 | 全能峰效率拟合、真符合求和（TCS）校正、Radford 扣本底法、内转换系数 |
| [ch11](chapters/ch11-charged-particle-pid.md) | 荷电粒子鉴别技术 | $\Delta E - E$ 望远镜、Bethe-Bloch 阻止本领、粒子双曲线轮廓分离 |
| [ch15](chapters/ch15-lifetime-measurements-rdm-dsam.md) | 核激发态寿命测量 | 快定时符合法、RDM 活塞反冲距离法、DDCM 微分法、DSAM 多普勒线形分析 |
| [reconciliation](chapters/wu-vs-wang-reconciliation.md) | 吴治华 vs 汪晓莲解冲突手册 | 能量分辨率极限、成形时间常数、气体室取舍、死时间模型、定时走动/晃动、中子辐射损伤 |

## Supporting Reference Files

- [glossary.md](glossary.md) — 实验核谱学专用术语与公式符号规范对照。
- [patterns.md](patterns.md) — 5 大实验设计与数据分析高阶实操范式。
- [cheatsheet.md](cheatsheet.md) — 实验物理常数、靶衬底参数、活时间与机时预算速查表。

---

## Scope & Limits

本技能提供低能实验核物理、高纯锗谱学、在束测量与实验方案设计的方法学指导。对于量子核结构基础理论推导，配合 `bohr-mottelson-nuclear-structure`；对于集体转子与相互作用玻色子模型，配合 `casten-nuclear-structure`；对于三轴形变手征几何与摆动运动前沿，配合 `chirality-and-wobbling-atomic-nuclei`。
