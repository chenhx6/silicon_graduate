---
type: method
title: "Budaca：基于准粒子对齐三轴核自旋动力学与半经典相空间量化合同"
aliases: [Budaca spin dynamics, semiclassical triaxial rotor with alignments, SU(2) coherent state PRM mapping, coordinate-dependent mass wobbling, tilted-axis wobbling model]
method_type: "semiclassical-spin-dynamics-prm-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Chirality and Wobbling in Atomic Nuclei Ch.13, PDF pp.275-291, full chapter reading"
confidence: "high for analytical derivations, phase space equations, and reported experimental fits"
tags: [prm, semiclassical-dynamics, su2-coherent-state, coordinate-dependent-mass, tilted-axis-wobbling, chiral-geometry, 130ba, 105pd, 133la, 134pr, 138pm]
sources: [book-petrache-chirality-and-wobbling]
---

# Budaca：基于准粒子对齐三轴核自旋动力学与半经典相空间量化合同

## Purpose

本方法合同基于 Radu Budaca 在专著《Chirality and Wobbling in Atomic Nuclei》第 13 章的系统研究，
解决粒子–转子模型（PRM）中多体相互作用导致的代数对角化维度膨胀与微观物理图景模糊的理论难题：
通过将包含冻结准粒子对齐（Frozen Alignment, FA）的量子 PRM 哈密顿量借助 \(SU(2)\) 自旋相干态映射到单位球面上，
构造正则共轭的经典相空间变量（投影变量 \(x = I\cos\theta\) 与方位角 \(\phi\)），
并进一步沿极小能量路径执行简谐展开与坐标依赖质量的一维薛定谔方程严格量化，
确立以下核心理论与唯象分析合同：

1. **\(SU(2)\) 自旋相干态半经典映射理论**：利用全角动量代数的超完备相干态基底，严格推导经典能量函数 \(H(x, \phi)\) 与标准正则泊松括号运动方程 \(\{H, x\} = \dot x\)、\(\{H, \phi\} = \dot \phi\)；
2. **三维自旋空间驻点拓扑与分岔相变**：求解能量泛函在不同形变 \(\gamma\) 与准粒子倾角 \(\alpha, \alpha'\) 下的驻点轨迹，揭示随自旋升高从共面单极小向非共面双阱超临界分岔的临界自旋 \(I_{\rm crit}\) 条件；
3. **坐标依赖质量量子化哈密顿量**：在方位角 \(\phi\) 上沿极小能量路径 \(\phi_0(x)\) 展开，利用广义微分对应原理严格推导含有效质量 \(B(x)\) 的一维集体薛定谔方程，以方阱基底展开严格求解波函数与跃迁几率；
4. **倾斜轴摆动（Tilted-Axis Wobbling）新物理图像**：在 \(^{133}\mathrm{La}\) 中定量证明微小倾角使摆动激发能极小点下移，成功调和了纵向摆动（LW）与横向摆动（TW）的表面矛盾；
5. **偶偶核与奇奇核全系统实验检验**：在 \(^{130}\mathrm{Ba}\)（两准粒子摆动）、\(^{105}\mathrm{Pd}\)（中子横向摆动）、\(^{134}\mathrm{Pr}\)（小倾角静态手征）及 \(^{138}\mathrm{Pm}\)（非对称倾角手征振动–转动相变）中完美复现实验能隙与电磁跃迁比。

---

## Inputs and Assumptions

### 1. 广义粒子–转子模型（PRM）与冻结对齐哈密顿量

对于具有三轴形变核芯并耦合两个准粒子（自旋分别为 \(\vec j\) 与 \(\vec j'\)）的原子核系统，总角动量为 \(\vec I = \vec R + \vec j + \vec j'\)。
核芯转子哈密顿量为：
\[
H_R = \sum_{k=1,2,3} A_k (\hat I_k - \hat j_k - \hat j'_k)^2 , \quad A_k = \frac{1}{2\mathcal{J}_k}
\]
在流体动力学模型惯量约定下：
\[
\mathcal{J}_k = \frac{4}{3} \mathcal{J}_0 \sin^2\left(\gamma - \frac{2}{3}k\pi\right)
\]
当选定 \(\gamma \in (60^\circ, 120^\circ)\) 时，核芯半轴满足 \(R_2 < R_3 < R_1\)，即第 1、2、3 主轴分别对应长轴（\(l\)）、短轴（\(s\)）和中轴（\(m\)）。
该形变区间确保中轴具有最大转动惯量（\(\mathcal{J}_3 = \mathcal{J}_m = \max\)），核芯倾向于绕中轴转动。

在冻结对齐（Frozen Alignment, FA）近似下，准粒子角动量算符被其沿主平面的取向期望值取代：
\[
\begin{cases}
\hat j_1 = j \cos\alpha, & \hat j'_1 = 0 \\
\hat j_2 = 0, & \hat j'_2 = j' \cos\alpha' \\
\hat j_3 = j \sin\alpha, & \hat j'_3 = j' \sin\alpha'
\end{cases}
\]
其中 \(\alpha\) 与 \(\alpha'\) 分别量化中子空穴偏离长轴及质子粒子偏离短轴的倾斜角（Tilting angles）。
由此，有效量子哈密顿量简化为含顺排推转项的三轴转子算符：
\[
\hat H_{\rm align} = A_1 \hat I_1^2 + A_2 \hat I_2^2 + A_3 \hat I_3^2 - 2A_1 j \hat I_1 \cos\alpha - 2A_2 j' \hat I_2 \cos\alpha' - 2A_3 (j\sin\alpha + j'\sin\alpha') \hat I_3
\]

### 2. \(SU(2)\) 自旋相干态基底

选取第 3 轴（中轴）为量子化轴，自旋相干态由球极坐标的方位角 \(\phi\) 与投影变量 \(x = I\cos\theta\) 立体投影参数化：
\[
|\psi_{IM}(x, \phi)\rangle = \sum_{K=-I}^I \frac{1}{(2I)^I} \sqrt{\frac{(2I)!}{(I-K)!(I+K)!}} (I+x)^{\frac{I-K}{2}} (I-x)^{\frac{I+K}{2}} e^{i\phi(I+K)} \vert IMK\rangle
\]
相干态对角动量算符的期望值满足严格几何关系：
\[
\langle \hat I_1 \rangle = \sqrt{I^2 - x^2}\cos\phi, \quad \langle \hat I_2 \rangle = \sqrt{I^2 - x^2}\sin\phi, \quad \langle \hat I_3 \rangle = x
\]
平方算符的期望值包含有限自旋测不准重整化因子：
\[
\langle \hat I_k^2 \rangle = \frac{I}{2} + \frac{2I-1}{2I} \langle \hat I_k \rangle^2 , \quad (k=1,2,3)
\]
满足 \(\sum_k \langle \hat I_k^2 \rangle = I(I+1)\)，保证态矢是 \(\hat I^2\) 的严格本征态。

---

## What It Can Establish

### 1. 经典相空间能量函数与正则泊松括号运动方程

应用含时变分原理 \(\delta \int \langle\psi \vert H_{\rm align} - i\partial_t  \vert \psi \rangle dt = 0\)，导出球面上的经典能量函数：
\[
\begin{aligned}
H(x, \phi) = & \frac{(2I-1)(I^2-x^2)}{2I} (A_1\cos^2\phi + A_2\sin^2\phi - A_3) \\
& - 2\sqrt{I^2-x^2} (A_1 j \cos\alpha\cos\phi + A_2 j' \cos\alpha'\sin\phi) \\
& - 2A_3 x (j\sin\alpha + j'\sin\alpha') + \frac{I}{2}(A_1+A_2) + A_3 I^2
\end{aligned}
\]
运动方程严格满足正则哈密顿形式：
\[
\dot x = \{H, x\} = -\frac{\partial H}{\partial \phi}, \quad \dot\phi = \{H, \phi\} = \frac{\partial H}{\partial x}
\]
其中 \(\{\phi, x\} = 1\)，由此确立 \(\phi\) 为广义坐标，\(x\) 为广义动量。

### 2. 驻点相图、超临界分岔与静态手征转变（图 13.1–13.3）

- **单准粒子情况（如纯质子 \(j'=11/2, j=0\)）**：
  极小点方位角被锁定在对称面上（空穴 \(\phi=0\)，粒子 \(\phi=\pi/2\)）。
  当自旋达到临界值 \(I_{\rm crit}\) 时，中轴附近的单一能量极小点分裂为两个对称分布在 \(x_{\min} > 0\) 与 \(x_{\min} < 0\) 的极小能谷（图 13.1）。
- **两相互垂直准粒子情况（手征构型 \(j=j'=11/2\)）**：
  在理想轴对齐（\(\alpha=\alpha'=0^\circ\)）且 \(\gamma=90^\circ\) 时，方位角驻点恒为 \(\phi_{\min}=45^\circ\)。
  当 \(\gamma \ne 90^\circ\) 时，系统随自旋发生明确的**平面进动向非共面立体转动相变**：
  低自旋区角动量矢量在两准粒子主平面内移动；跨过临界自旋 \(I_{\rm crit}\) 后分裂为两个立体极小，进入静态手征区。
- **倾角引入后的平滑机制**：
  非零倾角 \(\alpha, \alpha' > 0\) 打破了两个极小的能量对称性，使跃迁区平滑化，并在较高自旋区导致双带能隙随自旋重新增大（图 13.2、13.3）。

### 3. 坐标依赖质量一维薛定谔集体运动方程（式 13.14–13.24）

经典能量函数沿极小能量路径 \(\phi_0(x)\)（满足 \(\partial H/\partial\phi = 0\)）进行简谐展开：
\[
\tilde H(x, \phi) \approx H(x, \phi_0(x)) + \frac{1}{2} \left.\frac{\partial^2 H}{\partial\phi^2}\right|_{\phi_0(x)} [\phi - \phi_0(x)]^2
\]
其中 \(\phi_0(x)\) 由严格超越方程确定：
\[
\frac{(2I-1)\sqrt{I^2-x^2}}{2I} (A_2 - A_1) \sin 2\phi_0(x) = 2 \left[ A_2 j' \cos\alpha'\cos\phi_0(x) - A_1 j \cos\alpha\sin\phi_0(x) \right]
\]
定义有效质量函数：
\[
B(x) = \left[ \left.\frac{\partial^2 H(x, \phi)}{\partial\phi^2}\right|_{\phi_0(x)} \right]^{-1}
\]
采用量子对应原理 \(\phi = i \frac{d}{dx}\) 并执行酉波函数变换 \(f(x) = [B(x)]^{-1/4} F(x) \exp\left[i\int \phi_0(x)dx\right]\)，
导出标准的一维定态薛定谔方程：
\[
-\frac{1}{2} \frac{1}{\sqrt{B(x)}} \frac{d}{dx} \frac{1}{\sqrt{B(x)}} \frac{d}{dx} f(x) + V(x) f(x) = E f(x)
\]
其中有效势能严格由经典极小路径与质量函数的高阶导数确定：
\[
V(x) = H(x, \phi_0(x)) + \frac{B''(x)}{8 [B(x)]^2} - \frac{9 [B'(x)]^2}{32 [B(x)]^3}
\]
在边界条件 \(F_I(\pm I) = 0\) 下，采用一维无穷深方阱基底 \(\{\cos\frac{(2n-1)\pi x}{2I}, \sin\frac{2n\pi x}{2I}\}\) 展开对角化，
直接得到本征能量 \(E_{I, s}\) 与波函数投影展开系数 \(\Lambda_{IK}^s\)。

### 4. 电磁跃迁几率与混合比提取公式（式 13.25–13.30）

- **\(E2\) 跃迁算符（含二阶四极张量修正）**：
  \[
  T_{2\mu}(E2) = t_1 q_{2\mu} + t_2 [q \times q]_{2\mu}
  \]
  跃迁几率由有效四极矩 \(\tilde Q_0, \tilde Q_2\) 与波函数展开系数紧密关联（式 13.27–13.28）。
- **\(M1\) 跃迁算符**：
  考虑冻结对齐下的球张量算符近似（式 13.29），
  微观给出带内与跨带磁偶极跃迁几率 \(B(M1; I_s \to I'_{s'})\)（式 13.30），
  由有效回旋比 \(g_j - g_R\) 与 \(g_{j'} - g_R\) 控制。

### 5. 重点核区实验再现与动力学机制裁决

| 核素 | 物理模式 | 关键参数拟合 | 理论计算与实验吻合特征 |
|---|---|---|---|
| **\(^{130}\mathrm{Ba}\)** | 偶偶核两准粒子横向摆动 | \(\pi h_{11/2}^2\) (\(j=10\hbar\)), \(\gamma=90^\circ, \alpha=\alpha'=0^\circ\) | 完美再现摆动激发能 \(\Delta E(I)\) 随自旋下降及 \(B(M1)_{\rm out}/B(E2)_{\rm in}\) 的抛物线演化（图 13.5a,d） |
| **\(^{105}\mathrm{Pd}\)** | 奇中子核横向摆动 | \(\nu h_{11/2}\), 轴对齐 \(\alpha'=0^\circ\) | 再现 \(\Delta E(I)\) 随自旋下降趋势与带间/带内电磁比（图 13.5b,e） |
| **\(^{133}\mathrm{La}\)** | 倾斜轴摆动（Tilted-Axis Wobbling） | \(\pi h_{11/2}\), 显著倾角 \(\alpha' \a10^\circ\)–\(30^\circ\) | 阐明微小倾角使摆动能极小下移至低自旋，使高自旋区展现 \(\Delta E(I)\) 上升表象，统一了 LW 与 TW（图 13.5c,f） |
| **\(^{134}\mathrm{Pr}\)** | 近简并静态手征双重带 | \(\pi h_{11/2} \nu h_{11/2}^{-1}\), \(\alpha=\alpha'=3^\circ\) | 在 \(I=13\hbar\) 处准确重现能隙极小（< 280 keV）及从手征振动向静态手征转动的相变（图 13.4b） |
| **\(^{138}\mathrm{Pm}\)** | 非对称倾角手征相变 | \(\pi h_{11/2} \nu h_{11/2}^{-1}\), \(\alpha'=8^\circ, \alpha=0^\circ\) | 精确再现能级差 \(\Delta E(I)\) 的先降后升反弹曲线及带内 \(B(M1)/B(E2)\) 比率（图 13.6a,b） |

---

## What It Cannot Establish Alone

1. **不能直接微观预言转动惯量与形变参数**：
   三轴度 \(\gamma\)、惯量比例尺度 \(\mathcal{J}_0\) 以及倾斜角 \(\alpha, \alpha'\) 是唯象可调参数或借由流体动力学公式预设，模型本身不包含微观自洽的自旋–同位旋残余相互作用与平均场自洽反作用；
2. **不能描述大振幅配对动力学与带交叉反转**：
   哈密顿量基于冻结对齐（FA）与固定的单/双准粒子角动量标量，无法自发处理转动诱发的准粒子配对拆对（Pair breaking）、回弯（Backbending）及高自旋下核心能带交叉；
3. **不能替代全对角化粒子转子模型（PRM）中的有限矩阵元微观细节**：
   简谐近似展开假定在方位角 \(\phi_0(x)\) 附近振幅较小，在极高非简谐区或近球形极软势场下，连续质量薛定谔方程与离散全组态 PRM 存在阶数截断差异；
4. **不能仅由能级拟合唯一锁定倾斜角 \(\alpha, \alpha'\)**：
   由于三轴度与倾斜角在能级拟合中存在一定程度的代数相关性，必须联合高精度的带间电磁跃迁绝对分支比、多极混合比 \(\delta(E2/M1)\) 与寿命测量方能解除参数简并。

---

## Cross-References and Ecosystem Integration

- **微观推转与势能面支撑**：
  - [[chen-cdft-prm-wobbling-and-fermi-surface-contract]]：微观 CDFT 势能面约束导出 \((\beta, \gamma)\) 及费米面演化定律；
  - [[zhao-tdcdft-chiral-precession-and-tunneling-contract]]：时域 TD-CDFT 验证了微观相空间手征进动椭圆闭合轨道；
- **全代数对角化与三维投影对比**：
  - [[sheikh-tpsm-wobbling-and-triaxial-projection-contract]]：TPSM 投影壳模型微观恢复实验室好对称性；
  - [[wang-tpsm-even-even-chiral-wobbling-contract]]：偶偶核多准粒子 TPSM 与 \(^{130}\mathrm{Ba}\) 摆动波函数节点拓扑对照；
- **核芯柔性与 \(\gamma\) 振动竞争**：
  - [[zhang-gamma-vibrational-collective-model-contract]]：Bohr 玻尔哈密顿量核芯 \(\gamma\) 振动耦合与 M\(\chi\)D 多重机制；
  - [[davydov-filippov-triaxial-rotor-and-wobbling-dynamics]]：经典三轴刚体转子 Davydov–Filippov 能量基准；
  - [[chiral-vibrational-tunneling-and-double-well-splitting]]：手征双阱瞬子隧穿作用量与能隙分裂微观理论。


## Sources

- [[book-petrache-chirality-and-wobbling]]：R. Budaca, Ch. 13 *Spin dynamics of triaxial nuclei with quasiparticle alignments*, in C. M. Petrache (Ed.), *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025), pp. 275–291.
- [[book-bohr-mottelson-nuclear-structure-vol2]]：A. Bohr & B. R. Mottelson, *Nuclear Structure*, Vol. II, World Scientific (1998), Chapter 4 & Appendix 4A.
- [[frauendorf-2014-transverse-wobbling]]：S. Frauendorf & F. Dönau, *Transverse wobbling in odd-mass nuclei*, Phys. Rev. C 89, 014322 (2014).
