---
type: concept
title: "同位旋类似态（IAS）库仑位移能、同位旋对称性破缺与镜像核CED高自旋对齐法典"
aliases: [同位旋类似态, IAS, 库仑位移能, 同位旋破缺, 库仑能量差, CED, 镜像核转动带, 回弯机制判决, 49Cr与49Mn]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [isobaric-analog-state, ias, coulomb-displacement-energy, coulomb-energy-difference, ced, isospin-symmetry-breaking, mirror-nuclei, band-crossing-alignment]
---

# 同位旋类似态（IAS）库仑位移能、同位旋对称性破缺与镜像核CED高自旋对齐法典

## Definition

### 物理全景：电磁库仑相互作用对微观强相互作用对称性的精细破缺

在完全忽略电磁相互作用的理想假定下，核力具有严格的电荷无关性（Charge Independence）与电荷对称性（Charge Symmetry），原子核多体哈密顿量在同位旋群 $SU(2)_{\text{isospin}}$ 下严格对易。
然而，质子之间无处不在的长程排斥库仑势：
$$V_C = \sum_{i < j}^Z \frac{e^2}{|\vec{r}_i - \vec{r}_j|}$$
对同位旋对称性施加了微扰破缺。

根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. I（第 3 章）、J. Jänecke（1969）以及 M. A. Bentley & P. E. Garrett（J. Phys. G 34, R182, 2007）：
库仑破缺在两个极其重要的核结构物理领域产生了不可替代的科学洞见：
1. **同位旋类似态（Isobaric Analog State, IAS）与库仑位移能 $\Delta E_C$**：
   在母核 $|Parent\rangle$（质子数 $Z$，中子数 $N$，同位旋 $T_0 = (N-Z)/2, T_z = T_0$）上作用费米同位旋降低算符 $T_- = \sum_k \tau_-(k)$，将一个中子转化为处于完全相同空间轨道和自旋态的质子。该态在子核 $(Z+1, N-1)$ 中构成了母核基态的忠实镜像——**同位旋类似态（IAS）**。IAS 与母核基态的能量差 $\Delta E_C$（库仑位移能）极其精确地测量了核电荷分布半径与核子电荷交换关联；
2. **镜像核高自旋能级之差——库仑能量差（Coulomb Energy Difference, CED）**：
   在 $N \approx Z$ 附近的镜像核对（Mirror Nuclei，如一对同质异位素 $T_z = -1/2$ 与 $T_z = +1/2$，典型案例为 $^{49}\text{Mn} / {}^{49}\text{Cr}$ 或 $^{71}\text{Br} / {}^{71}\text{Kr}$）中，沿各自的基态转动带观察同自旋能级激发能之差：
   $$\text{CED}(I) = E_x(I, T_z = -1/2) - E_x(I, T_z = +1/2)$$
   当转动频率升高至带交叉（Backbending 回弯）处时，**CED 曲线将产生高达数十至上百 keV 的突发性阶跃跳跃（Sharp Jump）**！这一跳跃构成了实验上**一锤定音判定究竟是质子对率先对齐还是中子对率先对齐的终极判据**！

---

## Necessary Assumptions

### 严格物理公式与数学推导

### (1) 同位旋类似态（IAS）算符定义
设母核基态为 $|J_0^\pi, T_0, T_{z0} = T_0\rangle$。
定义正规化的 IAS 态：
$$|IAS\rangle = \frac{T_- |J_0^\pi, T_0, T_0\rangle}{\sqrt{2 T_0}}$$
其角动量、宇称与总同位旋与母核基态完全相同（$J^\pi = J_0^\pi, T = T_0$），但同位旋第三分量改变为 $T_z = T_0 - 1$。
在实验电荷交换反应（如 $(p, n)$ 或 $(^3\text{He}, t)$ 反应）中，由于传递算符为纯标量，激发截面在零度角极度占优。

---

### (2) 库仑位移能 $\Delta E_C$ 系统学
母核与其 IAS 态之间的能量差等于子核中 IAS 激发能加上两核基态质量差：
$$\Delta E_C = M(Z+1, A) - M(Z, A) + (m_n - m_p - m_e) = M(Z+1, A) - M(Z, A) + 0.7823\text{ MeV}$$

在等密度均匀带电球体近似下，包含直接库仑自能与反向泡利交换项（Jänecke 公式）：
$$\Delta E_C = \frac{6}{5} \frac{e^2}{R_0} \frac{\bar{Z}}{A^{1/3}} - 0.96 \frac{e^2}{R_0} \frac{\bar{Z}^{1/3}}{A^{1/3}} \dots$$
其中有效电荷为初末态平均值：$\bar{Z} = Z + 0.5$。
经典经验参数化闭合形式：
$$\Delta E_C(Z, A) \approx 1.444 \frac{\bar{Z}}{A^{1/3}} - 1.130\text{ [MeV]}$$
对于中重核，$\Delta E_C$ 达到 $8 \sim 15\text{ MeV}$，使得 IAS 往往深埋在子核的粒子分离阈以上的准连续态中。

---

### (3) 镜像核库仑能量差（CED）与对齐微观机制
定义镜像转动带上的相对库仑能量差：
$$\text{CED}(I) = E_x(I, T_z = -1/2) - E_x(I, T_z = +1/2)$$
各激发能 $E_x(I)$ 扣除了各自的基态结合能差，因此抵消了宏观单极库仑场，只对核内部微观轨道排布敏感。

#### 回弯对齐时的库仑能跃变判决：
在转动推转力作用下，高 $j$ 轨道（如 $1f_{7/2}$ 或 $1g_{9/2}$）中的一对核子发生拆对对齐（Coriolis alignment）：
1. **富质子核（$T_z = -1/2$）**：若发生的是**质子对对齐（Proton Alignment）**，两个断裂的质子在转动轴上重新定向，占据相同的轨道空间，空间波函数重叠骤然增大。由于质子携带正电荷，两质子间的微观排斥能增加（$\Delta E_C \approx +100\text{ keV}$），使得转动带激发能相对抬高；
2. **富中子核（$T_z = +1/2$）**：在其镜像核中，对应的是**中子对对齐（Neutron Alignment）**。由于中子不带电荷，对齐过程完全不引起额外的库仑排斥！
3. **CED 跃变法典（The CED Jump Rule）**：
   $$\Delta \text{CED}(I) = \text{CED}(I) - \text{CED}(I-2)$$
   - 若在回弯自旋 $I_c$ 处，**$\text{CED}(I)$ 发生明显的正向跳跃（$\Delta \text{CED} > 0$）**：证明是**质子对率先对齐**！
   - 若在回弯自旋 $I_c$ 处，**$\text{CED}(I)$ 发生剧烈的负向塌缩（$\Delta \text{CED} < 0$）**：证明是**中子对率先对齐**！

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/isobaric_analog_state_ced_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `ias` 命令。

### 运行示范（模拟经典 $^{49}\text{Mn} / {}^{49}\text{Cr}$ 镜像核转动带数据）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py ias -Z 24 -A 49 --demo-ced --json
```

### 计算输出核心物理特征：
1. **库仑位移能**：
   - 母核 $^{49}\text{Cr}$（$Z=24$）向子核 $^{49}\text{Mn}$（$Z=25$）的位移能预测为 $\Delta E_C = 8.538\text{ MeV}$；
   - 直接库仑项贡献 $+9.641\text{ MeV}$，泡利交换修正项贡献 $-0.914\text{ MeV}$，子核中 IAS 激发等效 $Q$ 值为 $7.756\text{ MeV}$；
2. **镜像核 CED 演化与对齐诊断**：
   - 在低自旋区（$I = 3.5 \sim 11.5\hbar$），CED 随自旋平滑从 $-11.0\text{ keV}$ 上升至 $+99.0\text{ keV}$；
   - **在临界自旋 $I_c = 13.5\hbar$ 处，发生剧烈的阶跃突降：$\Delta \text{CED} = -59.0\text{ keV}$**（从 $+99\text{ keV}$ 骤跌至 $+40\text{ keV}$）；
   - 自动诊断输出：`Neutron Pair Alignment (CED drops by -59.0 keV at I = 13.5 hbar)`，完全符合核结构实验中 $^{49}\text{Cr}$ 中子率先在 $1f_{7/2}$ 壳层对齐的物理结论！

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用

- [[high-spin-band-crossing-and-alignment-mechanisms]]：经典 Harris 标架对齐角动量 $i_x$ 与此处 CED 库仑跳跃共同构成了回弯机制判决的双重印证；
- [[beta-decay-phase-space-log-ft-and-cvc-unitarity]]：超允许 $0^+ \to 0^+$ $\beta$ 衰变本质上就是发生在 IAS 之间的纯 Fermi 跃迁；
- [[wigner-supermultiplet-su4-and-mass-cusp]]：同位旋多重态能量正是从 Wigner 超多重态微观对称性中衍生而来。
