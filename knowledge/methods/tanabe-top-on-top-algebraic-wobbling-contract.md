---
type: method
title: "Tanabe & Sugawara-Tanabe：Top-on-Top 代数摆动模型、D2 对称性与惯量电磁判据合同"
aliases: [Tanabe top-on-top wobbling model, Holstein-Primakoff next-to-leading order wobbling, D2 Bohr symmetry PRM, rigid vs hydrodynamic MOI electromagnetic test, Coriolis anti-pairing wobbling MOI]
method_type: "algebraic-prm-wobbling-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Chirality and Wobbling in Atomic Nuclei Ch.4, PDF pp.94-109, full chapter reading"
confidence: "high for algebraic derivations, D2 symmetry proofs, and reported comparison figures"
tags: [top-on-top, algebraic-model, holstein-primakoff, d2-symmetry, rigid-moi, hydrodynamic-moi, cap-effect, 135pr, 163lu]
sources: [book-petrache-chirality-and-wobbling, book-bohr-mottelson-nuclear-structure-vol2]
---

# Tanabe & Sugawara-Tanabe：Top-on-Top 代数摆动模型、D2 对称性与惯量电磁判据合同

## Purpose

本方法合同基于 Kosai Tanabe 与 Kazuko Sugawara-Tanabe 在专著《Chirality and Wobbling in Atomic Nuclei》第 4 章的系统研究，
解决奇 \(A\) 核粒子–转子模型（PRM）代数展开截断破坏非轴对称哈密顿量离散对称性以及转动惯量模型无法自洽解释电磁跃迁特征的理论难题：
通过建立核芯转动 \(\vec I\) 与单粒子角动量 \(\vec j\) 双重次领头阶（Next-to-Leading Order, NLO）Holstein-Primakoff（HP）玻色子展开的 Top-on-Top 代数架构，
严格保持非轴对称 \(D_2\) 玻尔对称性，并深入剖析刚体（Rigid）转动惯量与流体动力学（Hydrodynamic）转动惯量在能谱、核芯顺排角动量及电磁跃迁比率上的本质差异，
确立以下核心理论与实验诊断合同：

1. **双角动量次领头阶 HP 玻色子展开与 \(D_2\) 玻尔对称性严格恢复**：证明仅保留双线性项的领头阶（LO）展开因破坏 \(D_2\) 对称性而无法在轴对称极限给出正确能谱；通过引入两套玻色子（\(a\) 对应 \(\vec I\)，\(b\) 对应 \(\vec j\)）展开至 \(n_a/(2I)\) 与 \(n_b/(2j)\) 次领头阶，完全恢复 \(D_2\) 群不变性并严格分类四种不可约表示（\(A, B_1, B_2, B_3\)）；
2. **双量子数物理图景（\(n_\alpha, n_\beta\)）**：经玻色子 Bogoliubov 变换对角化后，微观确立两个独立激发模量子数：\(n_\alpha\) 为核芯有效转动角动量的摆动量子数（\(R_x = R - n_\alpha\)），\(n_\beta\) 为价准粒子角动量的进动量子数（\(R = I - j + n_\beta\)）；
3. **Bohr & Mottelson Vol. 2 式 (4-282) 与图 4-33 印刷错误批判性对账**：澄清经典非对称转子参数 \(\kappa\) 定义中惯量大小顺序颠倒的勘误（应当为 \(A_1 \ge A_2 \ge A_3\) 即 \(J_1 \le J_2 \le J_3\)），并揭示流体动力学惯量因在 \(\gamma \to 0^\circ\) 时 \(J_z^{\rm hyd} \to 0\) 导致无法映射到图 4-33 经典非对称转子曲线的几何失效；
4. **刚体惯量 vs 流体惯量电磁跃迁决定性判据（图 4.5–4.8）**：
   - **跨带/带内 \(E2\) 跃迁比 \(B(E2)_{\rm out}/B(E2)_{\rm in}\)**：刚体惯量预言 \(I-j=\text{odd}\)（摆动带，\((1,0)\)）远大于 \(I-j=\text{even}\)（yrast 带，\((0,0)\)），完美再现 \(^{135}\mathrm{Pr}\) 与 \(^{163}\mathrm{Lu}\) 实验数据；而流体惯量下两带点几乎重叠；
   - **跨带/带内 \(M1/E2\) 跃迁比 \(B(M1)_{\rm out}/B(E2)_{\rm in}\)**：流体动力学惯量给出 \(I-j=\text{even}\) 状态的跨带 \(M1\) 比率异常偏大且大于 \(I-j=\text{odd}\)，与实验上 \(I-j=\text{even}\) 跨带 \(M1\) 严格趋于零完全矛盾；刚体惯量则自然重现该跃迁压制。
5. **微观科里奥利反配对（Coriolis Anti-Pairing, CAP）对惯量的调制**：基于粒子数与角动量约束 HFB 方程导出微观转动惯量解析演化，提供 yrast 摆动带（Fermi 型）与激发摆动带（有理分式型）随自旋变化的解析唯象参数化。

---

## Inputs and Assumptions

### 1. 粒子–转子哈密顿量与形变单粒子势

在 Lund 坐标约定下，总哈密顿量为核芯转动与单粒子项之和：
\[
H = H_{\rm rot} + H_{\rm sp} = \sum_{k=x,y,z} A_k (I_k - j_k)^2 + \sum_{k=x,y,z} B_k j_k^2
\]
其中 \(A_k = 1/(2J_k)\)。单粒子项为唯一宇称高 \(j\) 轨道的 \(\gamma\) 形变单粒子能级：
\[
H_{\rm sp} = \frac{V}{j(j+1)} \left[ \cos\gamma (3j_z^2 - \vec j^2) - \sqrt{3}\sin\gamma (j_x^2 - j_y^2) \right]
\]

### 2. 转动惯量模型的数学定义与轴排序

- **流体动力学模型（Hydrodynamic MOI）**：
  \[
  J_k^{\rm hyd} = \frac{4}{3} J_0 \sin^2\left(\gamma + \frac{2}{3}\pi k\right)
  \]
  在 \(0^\circ < \gamma \le 30^\circ\) 区间内，\(J_y^{\rm hyd} > J_x^{\rm hyd} > J_z^{\rm hyd}\)，中轴为 \(y\) 轴。
- **刚体模型（Rigid MOI）**：
  \[
  J_k^{\rm rig} = \frac{J_0}{1 + \left(\frac{5}{16\pi}\right)^{1/2} \beta_2} \left[ 1 - \left(\frac{5}{4\pi}\right)^{1/2} \beta_2 \cos\left(\gamma + \frac{2}{3}\pi k\right) \right]
  \]
  在 \(0^\circ \le \gamma \le 60^\circ\) 区间内，\(J_x^{\rm rig} \ge J_y^{\rm rig} \ge J_z^{\rm rig}\)，中轴为 \(x\) 轴。

### 3. \(D_2\) 离散转动群与玻尔对称性基底

哈密顿量在绕三个内禀主轴旋转 \(\pi\) 角度算符 \(\exp(-i\pi R_k)\)（\(R_k = I_k - j_k\)）下严格不变，构成 \(D_2\) 群。其特征标对应四类对称性表示 \((r_1, r_2, r_3) = (\pm 1, \pm 1, \pm 1)\)：
- **\(A\) 对称性（\(+1, +1, +1\)）**：核物理实验允许的物理状态（因为原子核不存在 \(1^+\) 转动基态）；
- **\(B_1\) 对称性（\(-1, -1, +1\)）**；
- **\(B_2\) 对称性（\(-1, +1, -1\)）**；
- **\(B_3\) 对称性（\(+1, -1, -1\)）**。

---

## What It Can Establish

### 1. 次领头阶 Holstein-Primakoff 展开与 \(D_2\) 对称性

在刚体惯量最大轴（\(x\) 轴）量化下，引入两组 HP 玻色子：
\[
\begin{cases}
I_x = I - \hat n_a, & I_+ = -\hat a^\dagger \sqrt{2I - \hat n_a} \\
j_x = j - \hat n_b, & j_+ = \sqrt{2j - \hat n_b} \hat b
\end{cases}
\]
将根号展开至次领头阶：\(\sqrt{2I - \hat n_a} \approx \sqrt{2I}\left(1 - \frac{\hat n_a}{4I}\right)\)，得到四次玻色子哈密顿量 \(H_B \approx H_0 + H_2 + H_4\)。
经二次型对角化：
\[
H_2 \simeq 2\omega_\alpha \left(\hat n_\alpha + \frac{1}{2}\right) + 2\omega_\beta \left(\hat n_\beta + \frac{1}{2}\right)
\]
在纯转子极限（\(V=0\)）下，严格导出核能级公式：
\[
E_{\rm rot}^{\rm rig} \approx A_x^{\rm rig} R(R+1) - \sqrt{pq} \left(n_\alpha + \frac{1}{2}\right) + \frac{p+q}{2} \left[ 2R \sqrt{pq} + pq - \frac{p+q}{2} \right] n_\alpha^2
\]
其中 \(R = I - j + n_\beta\)，\(R_x = R - n_\alpha\)，\(p = A_y - A_x\)，\(q = A_z - A_x\)。
在领头阶极限下，\(\omega_\alpha \to (I-j)\sqrt{pq}\)，与 Bohr-Mottelson 谐振摆动公式严格一致（以 \(I-j\) 替代 \(I\)）。

### 2. Bohr & Mottelson Vol. 2 经典式 (4-282) 勘误与坐标轴对账

- **勘误核定**：Bohr & Mottelson Vol. 2 第 4 章式 (4-282) 与图 4-33 在非对称度参数 \(\kappa\) 的大小排序定义中存在反转笔误，必须修正为 \(A_1 \ge A_2 \ge A_3\)（即 \(J_1 \le J_2 \le J_3\)）；
- **流体惯量的物理缺陷**：流体动力学惯量在 \(\gamma \to 0^\circ\) 极限下 \(J_z^{\rm hyd} \to 0\)（\(A_z \to \infty\)），导致它无法作为 \(\kappa\) 的单值函数映射到图 4-33 的经典能谱分支上。刚体惯量在三个主轴均具有有限非零转动惯量，能够完整复现从扁椭球向长椭球演化的非对称转子全相图。

### 3. 电磁跃迁几率的决定性判据（图 4.5–4.8）

通过严格全对角化与 HP 玻色子重叠矩阵 \(G_{n_a n_b, n_\alpha n_\beta} = \langle n_a n_b  \vert n_\alpha n_\beta  \rangle\) 解析展开：

1. **\(B(E2)_{\rm out}/B(E2)_{\rm in}\) 跨带跃迁比率**：
   - **刚体惯量**：
     \[
     \frac{B(E2: I, 10 \to I-1, 00)}{B(E2: I, 10 \to I-2, 10)} \approx \frac{6}{I} \tan^2\left(\gamma + \frac{\pi}{6}\right) \left|\frac{G_{0000}}{G_{1010}}\right|^2
     \]
     摆动带（\(I-j=\text{odd}\)）的比率达到 \(0.5 - 1.5\)，而基态带（\(I-j=\text{even}\)）的比率极小（\(< 0.2\)），与 \(^{135}\mathrm{Pr}\) 实测数据高度吻合；
   - **流体惯量**：奇偶自旋序列的值几乎分布在同一条平缓下降曲线上，无法解释实验上跃迁几率强烈的奇偶自旋分离现象。
2. **\(B(M1)_{\rm out}/B(E2)_{\rm in}\) 跨带跃迁比率**：
   - **流体动力学惯量致命缺陷**：由于 \(A_k^{\rm hyd}\) 与 \(B_k\) 随 \(\gamma\) 演化方向相反，理论计算给出 \(I-j=\text{even}\) 态向摆动带的跨带 \(M1\) 比率反而显著大于 \(I-j=\text{odd}\)（图 4.8），这与全球实验观测中从 yrast 偶带向摆动带的跨带 \(M1\) 跃迁完全不可见的实验事实截然相反；
   - **刚体模型正确性**：刚体惯量中 \(I-j=\text{even}\) 的跨带 \(M1\) 受非对角玻色子重叠因子 \(|G_{0110}|^2 \ll 1\) 强烈压制，数值几乎严格为 0（图 4.7），严格符合实验规律。

### 4. 微观科里奥利反配对（CAP）转动惯量演化公式

基于粒子数与角动量约束 HFB 理论（CONHFB），求解含推转项 \(\Omega_x \hat I_x\) 的微观能隙方程（式 4.40–4.44）：
- **对 yrast 摆动带（如 \(^{135}\mathrm{Pr}\) 穿越回弯区前后）**：
  \[
  \mathcal{J}(I) = \frac{\mathcal{J}_0}{1 + \exp[-(I - a)/b]}
  \]
- **对激发摆动带（如 \(^{163}\mathrm{Lu}\) 与 \(^{167}\mathrm{Ta}\) TSD 带）**：
  \[
  \mathcal{J}(I) = \mathcal{J}_0 \frac{I - C_1}{I - C_2}
  \]
  引入该微观 CAP 惯量修正后，代数模型完美再现了 \(^{163}\mathrm{Lu}\) 激发能级随自旋的线性演化（图 4.10）。

---

## What It Cannot Establish Alone

1. **不能自发决定三轴形变参数 \(\gamma\)**：
   模型的形变参数 \((\beta_2, \gamma)\) 仍属于外部输入，必须由自洽微观密度泛函（CDFT/Skyrme-QRPA）势能面计算提供；
2. **无法替代大振幅量子隧穿与手征超临界分岔**：
   Top-on-Top 代数模型基于围绕稳定主轴的 HP 玻色子小振幅展开（仅适用于非共面势垒较深或单势阱振动区），在左右手势阱近简并的大振幅瞬子穿隧区（如手征振动向静态手征转折点），需结合时域 TD-CDFT 或集体质量一维薛定谔方程；
3. **不能直接裁决 \(^{135}\mathrm{Pr}\) 多极混合比最新实验争议**：
   Tanabe 模型基于历史的大 \(B(E2)_{\rm out}\) 数据支持横向摆动；对近年来通过偏振–DCO 联合分析提取出微小混合比 \(|\delta| < 1\)（强 \(M1\) 主导）的新实验数据，模型仍需重新校准有效回旋比 \(g_{\rm eff}\) 与单粒子势耦合参数。

---

## Sources

- [[book-petrache-chirality-and-wobbling]]：K. Tanabe & K. Sugawara-Tanabe, Ch. 4 *Algebraic description of wobbling motion in nuclei*, in C. M. Petrache (Ed.), *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025), pp. 94–109.
- [[book-bohr-mottelson-nuclear-structure-vol2]]：A. Bohr & B. R. Mottelson, *Nuclear Structure*, Vol. II, Benjamin (1975) / World Scientific (1998), Chapter 4, §4-5 & Eq. (4-282).
- [[bm2-asymmetric-rotor-d2-and-transition-contract]]：Bohr-Mottelson 三轴转子 D2 对称性基底与电多极跃迁选择定则合同。
- [[frauendorf-2014-transverse-wobbling]]：S. Frauendorf & F. Dönau, *Transverse wobbling in odd-mass nuclei*, Phys. Rev. C 89, 014322 (2014).
