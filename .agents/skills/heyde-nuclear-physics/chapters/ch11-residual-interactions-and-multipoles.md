# 第 11 章：核子两体有效残余相互作用、多极展开与四极力驱动形变机制

**来源专著**：Kris L. G. Heyde《Basic Ideas and Concepts in Nuclear Physics》（IOP 1999）第 10、11 章
**对应页码**：印刷 pp. 310–360 / 物理 PDF pp. 330–380

---

## 1. 核心理论推导与残余相互作用表象

### 1.1 平均场与两体残余相互作用的微观分解
在核多体薛定谔方程中，核子之间通过现实两体力 $V_{ij}$ 发生相互作用。通过引入自洽平均单体势场 $U(i)$（如含自旋-轨道耦合的 Woods-Saxon 势或谐振子势），总哈密顿量严格分解为：
$$H = \sum_{i=1}^A \left[ -\frac{\hbar^2}{2m} \nabla_i^2 + U(i) \right] + \left[ \sum_{i<j}^A V_{ij} - \sum_{i=1}^A U(i) \right] \equiv H_0 + V_{\text{res}}.$$
- $H_0$ 为独立粒子模型哈密顿量，给出球形单粒子能级 $\epsilon_j$ 与幻数结构；
- $V_{\text{res}}$ 为**两体残余相互作用 (Two-Body Residual Interaction)**，负责引起组态混合（Configuration Mixing）、消除单粒子态简并并驱动集体效应。

### 1.2 残余相互作用的多极展开与物理分量
将空间局域的两体残余力 $V(\vec{r}_1 - \vec{r}_2)$ 按两粒子相对距离与球谐函数多极展开：
$$V(\vec{r}_1, \vec{r}_2) = \sum_{k=0}^\infty v_k(r_1, r_2) P_k(\cos\theta_{12}) = \sum_{k=0}^\infty \frac{4\pi}{2k+1} v_k(r_1, r_2) \sum_{m=-k}^k Y_{km}^*(\hat{r}_1) Y_{km}(\hat{r}_2).$$
1. **单极分量 ($k=0$)**：
   改变核中心单体势的平均深度，驱动单粒子能量随质子/中子数填充的微观壳演化（Monopole Shift）；
2. **短程配对分量 ($\delta$ 相互作用极限，包含全部 $k$)**：
   作用于时间反演共轭轨道核子对（$|j, m\rangle$ 与 $|j, -m\rangle$），在全角动量 $J=0^+$ 态产生极深的吸引能降（$\Delta E(0^+) = -\frac{2j+1}{2} G$），维系偶偶核的超流基态能隙；
3. **长程四极分量 ($k=2$, 四极-四极吸引力 $Q \cdot Q$)**：
   $$H_{QQ} = -\chi \sum_{m=-2}^2 \hat{Q}_{2m}^*(1) \hat{Q}_{2m}(2) \equiv -\chi \hat{Q}_1 \cdot \hat{Q}_2.$$

---

## 2. 质中四极吸引 $H_{QQ}$ 与原子核宏观形变相变

### 2.1 配对力与四极力的微观竞争
- **同类核子 ($pp, nn$) 配对力**：倾向于使核子两两成对耦合为球形 $J=0^+$，偏好维持球形封闭构型；
- **质子-中子 ($pn$) 四极吸引力**：由于同位旋对称性与非全同核子泡利原理不受阻挡，质子与中子之间的四极张量力 $H_{QQ}^{\pi\nu} = -\chi_{\pi\nu} \hat{Q}_\pi \cdot \hat{Q}_\nu$ 强度极大；
- **四极相干形变相变临界条件**：
  当开壳层的价质子数 $N_\pi$ 与价中子数 $N_\nu$ 较小时，配对能与壳隙占优，原子核呈现球形振动；
  随着远离闭壳层，$N_\pi \cdot N_\nu$ 迅速增加，长程 $pn$ 四极吸引相干能按 $N_\pi N_\nu$ 剧烈增长并最终超过配对力与壳隙单粒子分离能：
  $$E_{\text{def}} \approx -\chi_{\pi\nu} \langle \hat{Q}_\pi \rangle \cdot \langle \hat{Q}_\nu \rangle \propto -\chi_{\pi\nu} \cdot \beta_\pi \beta_\nu.$$
  原子核在基态自发破坏球对称性，经历向**轴对称长椭球形变或三轴形变**的宏观量子相变！

---

## 3. 在束核谱学应用：两粒子组态裂距与 Pandya 交叉定理
对于开壳层两个价核子在同一单粒子轨道 $j$ 中的两粒子态 $|j^2; J\rangle$：
$$\langle j^2; J | V_{\text{res}} | j^2; J \rangle = - V_0 \frac{(2j+1)^2}{2J+1} \begin{pmatrix} j & j & J \\ 1/2 & -1/2 & 0 \end{pmatrix}^2.$$
由角动量 $3j$ 符号与两粒子-两空穴变换直接导出 **Pandya 交叉定理 (Pandya Transformation)**：
粒子-粒子多重态矩阵元与粒子-空穴多重态矩阵元满足代数反演变换，为在束核谱学依据邻近偶偶核、奇奇核激发态反推微观有效残余相互作用矩阵元提供了严密的代数反演引擎。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/heyde-collective-modes-and-exotic-nuclei-contract.md`
- **代码实现**：`system/scripts/analysis/surface_delta_interaction_pandya_calculator.py`
- **上游来源**：`knowledge/sources/book-heyde-nuclear-physics-concepts.md`
