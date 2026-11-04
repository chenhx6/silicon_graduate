# 第 2 章：滴线弱束缚、Berggren 复基底与 Gamow 连续谱壳模型

**来源专著**：B. A. Brown & J. G. Li 等《The Nuclear Shell Model 70 Years after Its Advent》（MDPI 2023）第 4、5 篇专论
**对应页码**：印刷 pp. 115–160 / 物理 PDF pp. 126–171

---

## 1. 核心理论推导与滴线结合能微积分

### 1.1 结合能双差分与有效壳隙指标
B. A. Brown 提出利用原子结合能（Binding Energy）的离散双差分，作为诊断远离稳定线壳隙硬度与配对演化的无模型依赖观测量：
$$D^{(q)} \equiv (-1)^q [2 \text{BE}(q) - \text{BE}(q+1) - \text{BE}(q-1)],$$
其中 $q$ 可以取中子数 $N$ 或质子数 $Z$。
- **物理意义**：消除了宏观液滴能的平滑体积与表面项，直接提取微观壳层闭合与奇偶配对隙；
- **弱束缚核的波函数展宽**：当核子分离能 $S_n \to 0$ 时，传统谐振子势的高斯紧束缚假定彻底失效；单核子渐近波函数展示极其缓慢的单向空间出射长尾，促使单粒子能谱发生剧烈拓扑重组。

---

## 2. Berggren 复动量完备性定理与开放多体量子体系

### 2.1 复动量平面与 Siegert 出射波边界条件
在散射理论中，复动量 $k = k_r + i k_i$ 平面上的单粒子薛定谔方程本征态满足：
1. **束缚态（Bound States）**：位于正虚轴上（$k_r = 0, k_i > 0$），具有实负能量，空间指数衰减平方可积；
2. **非束缚共振极点（Resonant Poles）**：位于第四象限（$k_r > 0, k_i < 0$），满足纯向外出射波边界条件：$\psi(r) \propto e^{i k r} = e^{i k_r r} e^{|k_i| r}$；
   复本征能量严格解析给出极点能量与衰变宽度：
   $$E = \frac{\hbar^2 k^2}{2\mu} = E_r - i \frac{\Gamma}{2}.$$

### 2.2 Berggren 复围道完备性代数
T. Berggren (1968) 证明：通过选取一条绕过所有共振极点的下半平面复围道 $L^+$，离散态与非束缚连续散射态构成严格的正交完备广义度规基底：
$$\sum_{b \in \text{Bound}} |u_b\rangle \langle \tilde{u}_b| + \sum_{r \in \text{Resonance}} |u_r\rangle \langle \tilde{u}_r| + \int_{L^+} |u(k)\rangle \langle \tilde{u}(k)| dk = \hat{1}.$$
对偶内积定义为**无复共轭的复正规化标量积**：
$$\langle \tilde{\phi}_i | \phi_j \rangle = \int_0^\infty \phi_i(r) \phi_j(r) dr = \delta_{ij}.$$

---

## 3. Gamow 壳模型 (GSM) 多体方程与滴线外核结构应用

### 3.1 复对称哈密顿矩阵对角化
在由 Berggren 基底直接构成的多体 Slater 行列式上展开两体现实有效相互作用（如复软芯 CD-Bonn 势）：
- 总多体哈密顿矩阵为复对称矩阵（$H = H^T \ne H^\dagger$）；
- 采用复 Lanczos 或复 Arnoldi 算法求解复特征值，直接在第一性原理层级自洽包含：
  1. 多核子组态混合；
  2. 束缚态与连续散射谱的虚激发相干耦合；
  3. 真实的粒子自发破裂发射衰变宽度 $\Gamma$。

### 3.2 极端滴线前沿应用：$^{28}\text{O}$ 四中子非束缚发射
利用 GSM 精确计算证明：
- $^{28}\text{O}$（$Z=8, N=20$）处于强相互作用滴线外，共振能量位于连续谱中 $E_r \a0.5 - 1.2\text{ MeV}$；
- 其衰变宽度 $\Gamma$ 深刻揭示了两个双中子对（$2n-2n$ 关联）在出射势垒处的关联连续喷射，彻底终结了国际上关于氧滴线是否能够延展至 $N=20$ 的长期学术争论。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/gamow-shell-model-dripline-continuum-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`drip-line-cluster` 子命令)
- **上游来源**：`knowledge/sources/book-nuclear-shell-model-70-years.md`
