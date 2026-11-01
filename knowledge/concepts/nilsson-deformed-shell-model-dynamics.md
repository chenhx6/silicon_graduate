---
type: concept
title: "Nilsson变形平均场壳模型、单粒子轨道对角化与能级演化动力学"
aliases: [Nilsson模型, 变形壳模型, 渐近量子数, 下冲轨道, 上冲轨道, 闯入轨道, 四极形变能级, 雅可比对角化, 偶偶核基态形变]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [nilsson-model, deformed-shell-model, single-particle-energies, quadrupole-deformation, asymptotic-quantum-numbers, jacobi-diagonalization, intruder-orbitals]
---

# Nilsson变形平均场壳模型、单粒子轨道对角化与能级演化动力学

## 1. 物理全景：从球形 Mayer-Jensen 壳模型到轴对称变形核能谱

在开壳层原子核中，多个价核子对核芯施加的四极长程相互作用压倒了对能配对倾向，驱使原子核打破空间转动不变性，自发产生宏观四极变形（轴对称长椭、扁椭或三轴形变）。
球形平均场中高度简并的 $j$ 单粒子壳层被彻底撕裂，每个具有特定角动量投影 $\Omega$ 的时间反演克喇默斯（Kramers）双重态 $| \pm \Omega \rangle$ 获得了不同的空间能量移动。

根据 S. G. Nilsson（Dan. Mat. Fys. Medd. 29, no. 16, 1955）、A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II（第 5 章）与卢希庭《原子核物理（修订版）》（第 4 章）：
1. **Nilsson 变形各向异性谐振子势**：
   在球形谐振子势基底上，引入四极形变参数 $\epsilon_2$（$\approx 0.63 \beta_2$）、自旋-轨道耦合项 $C \mathbf{l} \cdot \mathbf{s}$ 以及平滑平顶势修正项 $D (\mathbf{l}^2 - \langle \mathbf{l}^2 \rangle_N)$；
2. **大形变渐近基底与空间取向直觉**：
   当变形很大时，轨道状态由轴对称柱坐标下的**渐近量子数（Asymptotic Quantum Numbers）**完全标定：
   $$\Omega^\pi [N, n_z, \Lambda]$$
   - $\Omega = \Lambda + \Sigma$ 为总角动量在核对称轴 $z$ 上的投影；
   - $N$ 为总谐振子主量子数；
   - $n_z$ 为核子沿对称轴 $z$ 方向的振动量子数；
   - $\Lambda$ 为轨道角动量在对称轴上的投影；
   - $\Sigma = \pm 1/2$ 为内禀自旋在对称轴上的投影；
3. **下冲（Down-sloping）与上冲（Up-sloping）轨道的驱动本质**：
   - 具有大 $n_z$（小 $\Omega$）的单粒子态，其核子波函数波包主要沿对称轴拉长定域，与拉长的长椭球核芯空间重叠最大，吸引势能最低。因此其能量随 $\epsilon_2 > 0$ 增加而剧烈下沉（**下冲轨道，Down-sloping**），对原子核施加极强的**长椭形变稳定驱动力**；
   - 具有小 $n_z$（大 $\Omega$）的单粒子态，其波函数在赤道面聚集，随长椭拉长而势能抬升（**上冲轨道，Up-sloping**），驱动原子核趋向扁椭形变。

---

## 2. 严格数学表象与矩阵对角化

### (1) Nilsson 哈密顿量标准形式
$$H = H_0 + H_\delta - 2 \kappa \hbar \omega_0 \mathbf{l} \cdot \mathbf{s} - \kappa \mu \hbar \omega_0 \left[ \mathbf{l}^2 - \frac{1}{2} N(N + 3) \right]$$
其中：
- 平均振子能量：$\hbar \omega_0 \approx 41.0 A^{-1/3}\text{ MeV}$；
- 四极形变微扰项（在无量纲伸长坐标下）：
  $$H_\delta = - \frac{2}{3} \epsilon_2 \hbar \omega_0 \sqrt{\frac{4\pi}{5}} Y_{20}(\theta, \phi)$$
- $\kappa, \mu$：质子或中子的单粒子标准壳层参数。

---

### (2) 球形基底 $|N, l, j, \Omega\rangle$ 矩阵元推导
在主壳 $N$ 与固定宇称下，由于轴对称性保持了 $j_z = \Omega$ 守恒，哈密顿量在固定 $(N, \Omega)$ 块中呈现有限维实对称方阵结构：
1. **对角能量项**：
   $$E_{\text{diag}}(N, l, j) = \hbar \omega_0 \left( N + \frac{3}{2} \right) - \kappa \hbar \omega_0 \left[ j(j+1) - l(l+1) - \frac{3}{4} \right] - \kappa \mu \hbar \omega_0 \left[ l(l+1) - \frac{1}{2} N(N+3) \right]$$
2. **四极形变非对角耦合项**：
   利用 Wigner-Eckart 定理与 Racah 代数：
   $$\langle N l' j' \Omega | Y_{20} | N l j \Omega \rangle = (-1)^{j' - \Omega} \begin{pmatrix} j' & 2 & j \\ -\Omega & 0 & \Omega \end{pmatrix} \langle N l' j' || Y_2 || N l j \rangle$$
   其中球形谐波约化矩阵元为：
   $$\langle N l' j' || Y_2 || N l j \rangle = (-1)^{j + 1/2} \sqrt{\frac{5 (2j+1)(2j'+1)}{4\pi}} \begin{pmatrix} j' & 2 & j \\ 1/2 & 0 & -1/2 \end{pmatrix} \frac{1 + (-1)^{l + l'}}{2}$$
   只有当 $\Delta l = 0, \pm 2$ 且 $\Delta j = 0, \pm 1, \pm 2$ 时耦合非零。

---

### (3) Jacobi 严格本征值求解
对每个由基态 $|N, l, j, \Omega\rangle$ 张成的对称子块，应用 Jacobi 旋转正交相似变换：
$$\mathbf{A}^{(k+1)} = \mathbf{R}^T \mathbf{A}^{(k)} \mathbf{R}$$
迭代消去非对角元直至收敛至 $10^{-10}$，输出严密的单核子能量本征值 $e_i(\epsilon_2)$。

---

## 3. 高自旋与闯入轨道（Intruder Orbitals）的决定性角色

在每个大壳 $N$ 中，由于极强的自旋-轨道吸引力（$-2\kappa \mathbf{l} \cdot \mathbf{s}$），具有最大角动量的态 $j = l + 1/2$（如 $N=4$ 壳层中的 $1g_{9/2}$，或 $N=5$ 中的 $1h_{11/2}$，以及 $N=6$ 中的 $1i_{13/2}$）被整体压入下方大壳层中，称为**唯一宇称闯入轨道（Intruder Orbitals）**。

在 $A \approx 130$ 区中：
- 质子费米面靠近 $1h_{11/2}$ 底部：产生极深的低 $\Omega$ 下冲轨道（如 $1/2^-[550], 3/2^-[541]$），极力稳定长椭形变并提供巨大内禀角动量；
- 中子费米面靠近 $1h_{11/2}$ 顶部：产生高 $\Omega$ 轨道（如 $9/2^-[514], 11/2^-[505]$），其反冲作用与质子产生三轴正交撕扯，构成了手征三面体（Chiral Trihedron）的根本微观起源！

---

## 4. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/nilsson_model_hamiltonian_diagonalizer.py`
并在 `nuclear_analyzer.py` 中集成为 `nilsson` 命令。

### 运行示范（求解 $A \approx 130$ 区质子 $N=4$ 壳层在 $\epsilon_2 = 0.25$ 下的完整能级）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py nilsson -N 4 -e 0.25 -A 130 --json
```

### 计算输出核心物理特征：
1. **下冲长椭稳定轨**：$\Omega = 1/2$ 处于 $40.24\text{ MeV}$，随形变加大比球形基线大幅下降，确认标定为 `Down-sloping (prolate-stabilizing)`；
2. **上冲赤道排斥轨**：大 $\Omega$ 且低 $n_z$ 的轨道（如 $\Omega = 1/2$ 的第 5 态）升至 $49.20\text{ MeV}$，标定为 `Up-sloping (oblate-stabilizing)`；
3. **单粒子能级劈裂**：$N=4$ 的 15 个独立能量子态全面解算，为宏观-微观 Strutinsky 壳修正计算与 TPSM 准粒子能带投影奠定了第一性原理基准！

---

## 5. 与相关前沿概念的交叉引用
- [[collective-quadrupole-pes-and-gamma-softness]]：微观 Nilsson 单粒子能级求和与液滴势相结合，正是 Strutinsky 构造 5D 四极势能面（PES）的核心输入；
- [[chiral-geometry-tilted-axis-cranking-and-aplanarity]]：手征三面体中短轴与长轴质子-中子矢量的微观来源完全由 Nilsson 轨道 $\Omega$ 决定；
- [[gallagher-moszkowski-rules-and-newby-shifts]]：GM 规则中的 $\Omega [N n_z \Lambda]$ 渐近量子数即为此处解析推导的 Nilsson 表象。
