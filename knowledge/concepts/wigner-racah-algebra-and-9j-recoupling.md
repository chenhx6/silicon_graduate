---
type: concept
title: "Wigner-Racah角动量代数、9j符号严格代数求解与L-S到j-j重耦合系数法典"
aliases: [Wigner-Racah代数, 9j符号, 6j符号收缩, L-S到j-j变换, 角动量重耦合, 壳模型双粒子矩阵元, Edmonds公式, 张量算符代数]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [wigner-racah-algebra, 9j-symbol, 6j-symbol, ls-to-jj-coupling, angular-momentum-recoupling, shell-model, tensor-algebra]
---

# Wigner-Racah角动量代数、9j符号严格代数求解与L-S到j-j重耦合系数法典

## Definition

### 物理全景：核壳模型与跃迁矩阵元的底层代数基石

在量子力学与微观核结构多体理论中，角动量耦合不仅是标定核能级量子数（$J^\pi$）的工具，更是计算微观两体剩余相互作用矩阵元（如中心力、张量力、自旋-轨道力）与电磁跃迁几率的底层数学中枢。
当体系涉及三个角动量耦合时，变换由 Racah $W$ 系数或 Wigner $6j$ 符号完全解决；
**而当体系涉及四个角动量（如两个核子的轨道角动量与内禀自旋 $(l_1, s_1, l_2, s_2)$）以不同拓扑次序相加时，必须引入 Wigner $9j$ 符号（9j Symbol）！**

根据 A. R. Edmonds《Angular Momentum in Quantum Mechanics》、D. A. Varshalovich 等《Quantum Theory of Angular Momentum》以及 J. Suhonen《From Nucleons to Nucleus》：
Wigner $9j$ 符号描述了**两对互不相同子系统耦合后再次相加的幺正重整化变换（Unitary Recoupling Transformation）**：
$$| ((j_1 j_2) j_{12}, (j_3 j_4) j_{34}) J \rangle \longleftrightarrow | ((j_1 j_3) j_{13}, (j_2 j_4) j_{24}) J \rangle$$
其最伟大的物理应用是**建立核物理中 $L-S$ 耦合表象与 $j-j$ 耦合表象之间的精确双向桥梁**！
现代从头计算核理论、壳模型两体矩阵元解析展开（如 Moshinsky 括号变换）以及转移反应谱因子（Spectroscopic Factors）计算，全部严格建立在 $9j$ 符号的代数收缩之上。

---

## Necessary Assumptions

### 严格数学展开与 Racah 三重 $6j$ 收缩方程

### (1) Wigner $9j$ 符号的定义与对称性
$9j$ 符号由 $3 \times 3$ 矩阵的 9 个角动量构成，满足行三角定则与列三角定则：
$$\begin{Bmatrix} j_1 & j_2 & j_{12} \\ j_3 & j_4 & j_{34} \\ j_{13} & j_{24} & J \end{Bmatrix}$$
每一行 $(j_1, j_2, j_{12}), (j_3, j_4, j_{34}), (j_{13}, j_{24}, J)$ 以及每一列 $(j_1, j_3, j_{13}), (j_2, j_4, j_{24}), (j_{12}, j_{34}, J)$ 必须分别满足三角不等式（例如 $|j_1 - j_2| \le j_{12} \le j_1 + j_2$）。

#### 刚性对称律（Permutation Symmetries）：
- 沿主对角线或副对角线实施**转置变换**，数值严格不变；
- 实施任意行或列的**偶置换**，数值严格不变；
- 实施任意行或列的**奇置换**（如调换第 1 行与第 2 行），获得全角动量代数求和的奇偶相位因子：
  $$\begin{Bmatrix} j_3 & j_4 & j_{34} \\ j_1 & j_2 & j_{12} \\ j_{13} & j_{24} & J \end{Bmatrix} = (-1)^\Sigma \begin{Bmatrix} j_1 & j_2 & j_{12} \\ j_3 & j_4 & j_{34} \\ j_{13} & j_{24} & J \end{Bmatrix}, \quad \Sigma = \sum_{\text{all } 9} j$$

---

### (2) 基于三重 Wigner $6j$ 符号的闭合 Racah 收缩公式
根据 Edmonds 标准代数展开，$9j$ 符号可解析求和展开为三个 $6j$ 符号的标量积：
$$\begin{Bmatrix} j_1 & j_2 & j_{12} \\ j_3 & j_4 & j_{34} \\ j_{13} & j_{24} & J \end{Bmatrix} = \sum_{k} (-1)^{2k} (2k + 1) \begin{Bmatrix} j_1 & j_2 & j_{12} \\ j_{34} & J & k \end{Bmatrix} \begin{Bmatrix} j_3 & j_4 & j_{34} \\ j_2 & k & j_{24} \end{Bmatrix} \begin{Bmatrix} j_{13} & j_{24} & J \\ k & j_1 & j_3 \end{Bmatrix}$$
式中求和变量 $k$ 遍历所有同时满足三个 $6j$ 符号三角关系的整数或半整数。

---

### (3) 单零项极限退化（Reduction to 6j Symbol）
当 $9j$ 符号中包含一个零角动量时（例如总自旋 $J = 0$ 且 $j_{13} = j_{24}$）：
矩阵元退化为一个单重 $6j$ 符号与规范因子的乘积：
$$\begin{Bmatrix} j_1 & j_2 & j_{12} \\ j_3 & j_4 & j_{34} \\ j_{13} & j_{13} & 0 \end{Bmatrix} = \delta_{j_{12}, j_{34}} \frac{(-1)^{j_2 + j_3 + j_{12} + j_{13}}}{\sqrt{(2j_{12} + 1)(2j_{13} + 1)}} \begin{Bmatrix} j_1 & j_2 & j_{12} \\ j_4 & j_3 & j_{13} \end{Bmatrix}$$
这一恒等式构成了核多体物理中检验高阶代数库编写正确性的绝对数值锚点！

---

### (4) $L-S$ 到 $j-j$ 表象重整化变换支架
在原子核壳模型中，两核子体系既可用轨道与自旋分别耦合的宏观 $L-S$ 基底 $|(l_1 l_2)L, (s_1 s_2)S; J\rangle$ 描述，也可用各自先完成自旋-轨道耦合的微观 $j-j$ 基底 $|(l_1 s_1)j_1, (l_2 s_2)j_2; J\rangle$ 描述。
两套完全正交基底之间的重耦合幺正变换矩阵元为：
$$\langle (l_1 s_1)j_1, (l_2 s_2)j_2; J | (l_1 l_2)L, (s_1 s_2)S; J \rangle = \sqrt{(2j_1 + 1)(2j_2 + 1)(2L + 1)(2S + 1)} \begin{Bmatrix} l_1 & s_1 & j_1 \\ l_2 & s_2 & j_2 \\ L & S & J \end{Bmatrix}$$
该矩阵满足完全的正交归一性：
$$\sum_{j_1, j_2} |\langle jj | LS; J \rangle|^2 = 1, \qquad \sum_{L, S} |\langle jj | LS; J \rangle|^2 = 1$$

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/wigner_racah_algebra_9j_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `w9j` 命令。

### 运行示范（以经典 $(p_{3/2})^2$ 两核子态变换为 $L=2, S=0, J=2$ 为例）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py w9j --recouple-demo --json
```

### 计算输出核心物理特征：
1. **$9j$ 符号严格求解**：
   - 输入阵列：Row 1: $[1, 1/2, 3/2]$，Row 2: $[1, 1/2, 3/2]$，Row 3: $[2, 0, 2]$；
   - 包含 $S=0$ 零项收缩，严格解得 $9j$ 符号数值为 $0.064550$；
2. **$L-S$ 到 $j-j$ 重耦合系数解析吻合**：
   - 乘以维度因子 $\sqrt{4 \times 4 \times 5 \times 1} = \sqrt{80}$ 后，解析得出重耦合系数为：
     $$\langle (p_{3/2})^2; J=2 | (p^2) L=2, S=0; J=2 \rangle = \frac{1}{\sqrt{3}} \approx + 0.577350$$
   - 跃迁概率权重为：$|\langle jj | LS \rangle|^2 = 1/3 = 33.33\%$；
   - 严格重现了 Suhonen 壳模型经典教科书的解析解，证明纯 Python 算法无外依赖实现了高精度代数计算！

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用

- [[two-body-residual-interaction-surface-delta-and-pandya]]：表面 $\delta$ 相互作用在进行粒子-空穴变换时依赖此类 Racah 代数重整；
- [[wigner-supermultiplet-su4-and-mass-cusp]]：Wigner 超多重态在从非相对论 $L-S$ 表象投影至现实自旋-轨道势场中时，必须通过该 $9j$ 矩阵进行对角化。
