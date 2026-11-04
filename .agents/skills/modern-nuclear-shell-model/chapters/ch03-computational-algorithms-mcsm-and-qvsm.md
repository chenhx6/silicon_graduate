# 第 3 章：大尺度微观算力突破：MCSM 蒙特卡罗壳模型与 QVSM

**来源专著**：N. Shimizu《The Nuclear Shell Model 70 Years after Its Advent》（MDPI 2023）第 6 篇专论
**对应页码**：印刷 pp. 161–174 / 物理 PDF pp. 172–185

---

## 1. 核心理论推导与组态空间维数灾难

### 1.1 组合维数爆炸与经典 Lanczos 的物理极限
在完全无截断的全组态壳模型中，选定单粒子模型空间维度为 $D_p$ 与 $D_n$，开壳层价核子数为 $N_p, N_n$。
- **Slater 行列式 $M$-表象基底维度**：
  $$D_M = \begin{pmatrix} D_p \\ N_p \end{pmatrix} \times \begin{pmatrix} D_n \\ N_n \end{pmatrix};$$
- **维数爆炸灾难**：在稀土区或中等质量区跨主壳计算（如 $A \sim 130$ 质量区的 $sd-pf-sdg$ 大模型空间），矩阵维度急剧越过 $10^{11} - 10^{15}$，远远超出世界最先进超级计算机直接稀疏 Lanczos 内存容纳上限（$\sim 10^{10}$）。

---

## 2. 蒙特卡罗壳模型 (MCSM) 算法体系

N. Shimizu 与 T. Otsuka 等人发展了革命性的变分重要性基矢生成算法：

### 2.1 变分形变基矢的自适应生成
不再采用天量平凡的球形 Slater 行列式，而是生成由数十到数百个具有不同内禀四极与单极形变参量 $\vec{D}$ 的广义变形基矢：
$$|\phi_i(\vec{D}_i)\rangle = \prod_{\alpha} a_{\alpha}^\dagger(\vec{D}_i) |0\rangle;$$
利用共轭梯度法（Conjugate Gradient）直接对基矢形变参数进行实数能量泛函梯度变分优化，使其自发包围原子核在相空间中最优的四极变形与配对凝聚态。

### 2.2 三维角动量与宇称投影
对每一个优化的变分基矢施加完全的群投影算符：
$$|\Psi_{JM}^\pi\rangle = \sum_{i=1}^{N_{\text{basis}}} c_i \hat{P}_{MK}^J \hat{P}^\pi |\phi_i(\vec{D}_i)\rangle.$$
通过在极小的变分子空间（$N_{\text{basis}} \sim 50 - 200$）对角化广义本征方程 $H \vec{c} = E N \vec{c}$，实现以仅仅百分之一的计算代价精确提取高自旋态波函数。

### 2.3 能量方差外推法 (Energy Variance Extrapolation)
为了完全消除基矢截断误差，引入哈密顿量方差度规：
$$\Delta E^2 \equiv \frac{\langle \Psi | H^2 | \Psi \rangle - \langle \Psi | H | \Psi \rangle^2}{\langle \Psi | H | \Psi \rangle^2}.$$
- 当且仅当试探态是全空间的严格本征态时，方差严格为零：$\Delta E^2 = 0$；
- 微扰理论证明：变分能量 $E(\Delta E^2)$ 随方差满足高度光滑的线性截距关系：
  $$E(\Delta E^2) = E_{\text{exact}} + a_1 \Delta E^2 + a_2 (\Delta E^2)^2.$$
  通过外推至 $\Delta E^2 \to 0$ 截距，获得与全空间对角化完全等价的无偏能量基准。

---

## 3. 准粒子真空壳模型 (QVSM) 创新
针对强配对超流系统，Shimizu 提出了 QVSM 算法：
- 采用 HFB 类型的准粒子相干真空态（Quasi-Particle Vacua）作为基本展开单元；
- 在同一个变分基矢中同时自洽包含长程四极形变与单极超流配对凝聚，使得在处理偶偶核回弯带、三轴超形变与形状共存时，所需基矢数比纯 Slater 行列式进一步减少一个数量级，实现了在微观壳模型中全面复核三轴集体运动特征。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/shimizu-shell-model-mcsm-qvsm-computational-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`tpsm-diagonalization` 子命令)
- **上游来源**：`knowledge/sources/book-nuclear-shell-model-70-years.md`
