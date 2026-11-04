---
type: method
title: "Bohr & Mottelson Vol. II：Nilsson 变形单粒子能级、转移反应指纹与 Coriolis 顺排合同"
aliases: [BM2 Nilsson model, BM2 Chapter 5 single particle, Nilsson asymptotic quantum numbers, one-particle transfer fingerprints, Coriolis decoupling and attenuation, Stephens rotation alignment]
method_type: "deformed-single-particle-and-coriolis-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Bohr & Mottelson Nuclear Structure Vol. II, Chapter 5 Section 5-1 (printed pp.211-238 / PDF pp.233-260) and Section 5-3 (printed pp.243-255 / PDF pp.265-277)"
confidence: "high for analytical Hamiltonian derivations, asymptotic formulas, transfer fingerprint relations, and Coriolis attenuation physics"
tags: [bohr-mottelson, vol2, nilsson-model, asymptotic-quantum-numbers, transfer-fingerprints, coriolis-coupling, decoupling-parameter, rotation-alignment, avoided-crossings]
sources: [book-bohr-mottelson-nuclear-structure-vol2]
---

# Bohr & Mottelson Vol. II：Nilsson 变形单粒子能级、转移反应指纹与 Coriolis 顺排合同

## Purpose

本方法合同基于 Aage Bohr 与 Ben R. Mottelson 的巨著《Nuclear Structure》第二卷第 5 章 §5-1 与 §5-3 的系统研究，
解决轴对称与非轴对称形变核中单核子能级结构、渐近量子数分类、单核子转移反应谱学因子以及转动科里奥利相互作用引起能级畸变与顺排对齐的理论与实验对账难题：
通过在轴对称形变谐振子场中引入自旋–轨道耦合（\(\vec l \cdot \vec s\)）与平顶离心轨道平移项（\(\vec l^2 - \langle \vec l^2\rangle_N\)），
建立微观 Nilsson 模型本征值问题与圆柱坐标系大形变渐近基底 \([N n_3 \Lambda \Omega]\)，
严格推导单核子剥离与拾取反应截面特征“指纹谱”（Fingerprint patterns），
量化 \(K=1/2\) 奇 \(A\) 带的 Coriolis 解耦参数 \(a\)、二阶 Coriolis 转动惯量重整化（含 BCS 准粒子因子）及高自旋 Stephens 转动对齐（Rotation-Alignment, RAL）机制：

1. **Nilsson 变形壳模型哈密顿量与微观渐近能级（式 5-10、5-15）**：在椭球形变参数 \(\delta_{\rm osc}\) 下建立包含修正项的单核子哈密顿量，推导大形变极限下渐近量子数 \([N n_3 \Lambda \Omega]\) 的解析能级趋势与独宇称侵入轨道（Unique-parity intruders，如 \(h_{11/2}, i_{13/2}\)）的陡倾下潜机理；
2. **回避交叉（Avoided Crossings）与基底展开**：解析证明相同宇称 \(\pi = (-1)^N\) 与相同 \(\Omega\) 的单粒子轨道在形变演化中发生能级排斥，导出在球形基底 \( \vert j \Omega\rangle\) 中的展开系数 \(c_j \equiv \langle j \Omega  \vert \nu  \rangle\)；
3. **单核子转移反应截面与指纹法则（§5-3a）**：建立剥离反应 \(\frac{d\sigma}{d\Omega} \propto c_j^2 u_\nu^2\) 与拾取反应 \(\frac{d\sigma}{d\Omega} \propto c_j^2 v_\nu^2\) 的谱学因子理论，利用各转动成员相对截面比率唯一锁定 Nilsson 轨道身份；
4. **Coriolis 解耦参数与签名分裂（式 5-46）**：严格推导 \(K=1/2\) 带对角 Coriolis 矩阵元导出的解耦参数 \(a = - \langle \nu, 1/2  \vert j_+  \vert \nu, \overline{1/2} \rangle\)，解释特征能量交错 \(\Delta E_{1/2}(I) = A_{\rm rot} a (-1)^{I+1/2}(I+1/2)\)；
5. **二阶 Coriolis 惯量重整化与衰减机理（式 5-47）**：解析证明二阶 Coriolis 矩阵元含非对角配对因子 \((u_\nu u_{\nu'} + v_\nu v_{\nu'})^2\)（与 \(M1\) 跃迁相同），并阐明微观理论系统高估矩阵元导致经验衰减因子（\(\rho_{\rm att} \a0.6 \sim 0.8\)）的物理根源；
6. **高自旋 Stephens 转动对齐（RAL）与解耦能带形成（§5-3d）**：阐述 Coriolis 推转力矩 \(-\omega j_x\) 克服形变势场四极固定力矩（\(-D j_z^2\)）使得角动量沿转轴顺排的过程，导出解耦带能量间距紧跟偶偶核芯 \(E_{\rm core}(R)\) 的物理图像。

---

## Inputs and Assumptions

### 1. 轴对称形变谐振子势能与参数化

空间主轴频率满足体积守恒约束 \(\omega_1 \omega_2 \omega_3 = \omega_0^3 = \text{const}\)：
\[
\omega_3 = \omega_0 \left(1 - \frac{2}{3}\delta_{\rm osc}\right), \quad \omega_\perp = \omega_0 \left(1 + \frac{1}{3}\delta_{\rm osc}\right)
\]
形变四极参量 \(\delta_{\rm osc} \a0.95 \beta_2\)。

### 2. Nilsson 哈密顿量参数标定（表 5-1）

哈密顿量为（式 5-10）：
\[
H_{\rm Nil} = \frac{p^2}{2M} + \frac{1}{2}M\left[\omega_\perp^2 (x_1^2 + x_2^2) + \omega_3^2 x_3^2\right] + v_{ll}\hbar\omega_0 \left(\vec l^2 - \langle\vec l^2\rangle_N\right) + v_{ls}\hbar\omega_0 (\vec l \cdot \vec s)
\]
其中 \(\langle\vec l^2 \rangle_N = \frac{1}{2}N(N+3)\)。在稀土区（\(50 < Z < 82, 82 < N < 126\)），典型参数为 \(v_{ls} \approx -0.127\)，\(v_{ll} \approx -0.038\)（质子）与 \(-0.027\)（中子）。

---

## What It Can Establish

### 1. 渐近量子数分类与能级演化（式 5-15、图 5-1–5-5）

在圆柱坐标系中，单核子状态由渐近量子数严格标记：
\[
[N n_3 \Lambda \Omega]
\]
- \(N\)：主谐振子量子数；
- \(n_3\)：沿长轴（对称轴 \(z\)）的振动量子数；
- \(\Lambda\)：轨道角动量在对称轴上的投影（\(\Lambda = 0, 1, \dots, N-n_3\) 且 \(N-n_3-\Lambda\) 为偶数）；
- \(\Omega = \Lambda \pm 1/2\)：单核子总角动量在对称轴上的投影（好量子数）。

在大形变（长椭球 \(\delta_{\rm osc} > 0\)）极限下，单粒子能级解析近似为：
\[
\varepsilon(N n_3 \Lambda \Omega) \approx \hbar\omega_0 \left[ N + \frac{3}{2} - \frac{1}{3}\delta_{\rm osc} (3n_3 - N) - v_{ll} (\Lambda^2 - \langle\vec l^2\rangle_N) + v_{ls} \Lambda \Sigma \right]
\]
**下倾（Down-sloping）轨道与上倾（Up-sloping）轨道物理法则**：
- 当 \(n_3\) 较大时（波函数空间分布沿长轴延伸），能量随长椭形变 \(\delta_{\rm osc} > 0\) 迅速下潜（如 \([505\ 11/2^-]\) 下潜轨道，构成 \(A\approx130\) 区手征与摆动的关键入侵轨道）；
- 当 \(n_3 = 0\) 时，波函数集中于赤道平面，能量随长椭形变剧烈抬升（在扁椭形变下下沉）。

### 2. 单核子转移反应“指纹法则”（§5-3a、图 5-10）

将 Nilsson 本征态展开为球形基底 \(|\nu \Omega\rangle = \sum_{j} c_j |j \Omega\rangle\)（其中 \(c_j = \sum_l c_{lj\Omega}\)）：
- **单核子剥离反应（Stripping，如 \((d, p), (\alpha, t)\)）**：
  \[
  \frac{d\sigma}{d\Omega}(I) = 2 c_{j=I}^2 u_\nu^2 \sigma_{\rm DWBA}(\theta, l, j)
  \]
- **单核子拾取反应（Pickup，如 \((p, d), (d, t)\)）**：
  \[
  \frac{d\sigma}{d\Omega}(I) = 2 c_{j=I}^2 v_\nu^2 \sigma_{\rm DWBA}(\theta, l, j)
  \]
同一转动能带内各成员能级的截面相对比值仅取决于膨胀系数平方 \(c_j^2\)，与自旋和轨道角动量高度特异性绑定，构成了实验上指认形变核能带单粒子母体轨道（Parentage）的不可替代的“指纹谱”。

### 3. Coriolis 解耦参数与二阶惯量重整化（式 5-46、5-47）

- **\(K=1/2\) 带解耦参数 \(a\)**：
  \[
  a = - \langle \nu, \Omega=1/2  \vert j_+  \vert \nu, \overline{\Omega=1/2}  \rangle = (-1)^N \sum_l \left[ c_{l, 0, 1/2}^2 + 2\sqrt{l(l+1)} c_{l, 0, 1/2} c_{l, 1, -1/2} \right]
  \]
  使得能级产生交错分裂 \(\Delta E = A_{\rm rot} a (-1)^{I+1/2}(I+1/2)\)；
- **二阶 Coriolis 惯量重整化**：
  \[
  \delta A(\nu) = - (A_{\rm rot}^{(0)})^2 \sum_{\nu'}  \vert \langle \nu'  \vert j_+  \vert \nu   \rangle|^2 \left[ \frac{(u_\nu u_{\nu'} + v_\nu v_{\nu'})^2}{E(\nu') - E(\nu)} - \frac{(u_\nu v_{\nu'} - v_\nu u_{\nu'})^2}{E(\nu) + E(\nu')} \right]
  \]
  明确揭示单准粒子诱发的转动惯量增加项受配对因子 \((u_\nu u_{\nu'} + v_\nu v_{\nu'})^2\) 控制。

### 4. Coriolis 经验衰减机理与 Stephens 转动顺排（§5-3d）

1. **Coriolis 衰减因子（\(\rho_{\rm att} \a0.6 \sim 0.8\)）微观起源**：
   纯单粒子波函数预测的 Coriolis 混合矩阵元系统性偏大约 1.5–2 倍。该衰减来自于：
   - 准粒子与高能微观粒子–振动声子的相干耦合；
   - 配对反冲（Pairing recoil）与阻塞效应引起的配对势能面微观重整；
   - 自旋极化（Spin-polarization / Arima-Horie 机制）对有效核磁与动量算符的屏蔽。
2. **Stephens 转动顺排（Rotation-Alignment, RAL）**：
   在高自旋区，推转项 \(-\omega j_x\) 超过内禀四极对齐能，将高 \(j\) 轨道（如 \(h_{11/2}, i_{13/2}\)）的核子自旋强制对齐到转动轴（\(x\) 轴），导致能带退耦（Decoupled bands），其能级跃迁能量全同于偶偶核芯基带（\(\Delta E(I \to I-2) \approx E_{\rm core}(R \to R-2)\)）。

---

## What It Cannot Establish Alone

1. **轴对称 Nilsson 模型不包含三轴度 \(\gamma\) 自由度**：
   标准 Nilsson 势假定核芯为轴对称长椭球或扁椭球。对于三轴形变过渡核（\(A\approx130\)），必须采用三轴 Nilsson 势（引入 \(\sqrt{3}\sin\gamma (x_1^2 - x_2^2)\)）或三轴微观自洽平均场；
2. **不能自洽处理高自旋回弯中的动态多对拆对**：
   单粒子模型假定单一未配对准粒子，在高自旋带交叉点（Backbending），多个高 \(j\) 核子对同时发生退对对齐，需借由推转壳模型（CSM）或自洽推转 HFB（CRHFB）进行全微观重构；
3. **单粒子转移截面受光学势参数影响**：
   指纹法则给出的是相对比例 \(c_j^2\)；绝对截面的抽取受限于 DWBA 光学模型势深度及出射道库仑相互作用的不确定度。

---

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]：A. Bohr & B. R. Mottelson, *Nuclear Structure*, Vol. II: *Nuclear Deformations*, Chapter 5 §5-1 (pp. 211–238) & §5-3 (pp. 243–255), Tables 5-1 to 5-17.
- [[nilsson-deformed-shell-model-dynamics]]：Nilsson 变形壳模型哈密顿量对角化与单粒子轨道动力学。
- [[bm2-particle-rotor-adiabatic-coriolis-contract]]：BM-II 附录 4A 轴对称粒子–转子绝热基与非绝热 Coriolis 耦合合同。
- [[book-casten-nuclear-structure-simple-perspective]]：R. F. Casten, *Nuclear Structure from a Simple Perspective*, Chapter 7 (Nilsson Model) & Chapter 8 (Coriolis Coupling).
