---
type: concept
title: "形变奇奇核Gallagher-Moszkowski（GM）耦合定则、剩余p-n相互作用裂分与Newby奇偶位移法典"
aliases: [Gallagher-Moszkowski定则, GM定则, 残余质子中子相互作用, 自旋平行优势, 双重态裂分, Newby位移, K=0转动带, 奇奇核基态]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [gallagher-moszkowski, gm-rules, odd-odd-nuclei, nilsson-model, pn-residual-interaction, newby-shift, k-zero-bands, ground-state-spins]
---

# 形变奇奇核Gallagher-Moszkowski（GM）耦合定则、剩余p-n相互作用裂分与Newby奇偶位移法典

## 1. 物理全景：轴对称形变场中的价核子自旋对齐法则

在轴对称变形核（Deformed Nuclei）中，单核子在平均 Nilsson 势场中运动，其空间波函数由渐近量子数 $\Omega [N n_z \Lambda]$ 完全标定。
对于奇奇核（Odd-Odd Nuclei），奇质子与奇中子分别占据一个未配对的准粒子轨道：
- 奇质子：$\Omega_p [N_p, n_{z, p}, \Lambda_p]$，其内禀自旋在对称轴上的投影为 $\Sigma_p = \Omega_p - \Lambda_p = \pm 1/2$；
- 奇中子：$\Omega_n [N_n, n_{z, n}, \Lambda_n]$，其内禀自旋在对称轴上的投影为 $\Sigma_n = \Omega_n - \Lambda_n = \pm 1/2$。

由于变形势场的轴对称性，总角动量在核对称轴上的投影量子数 $K$ 可以有两种矢算耦合方式：
$$K_+ = \Omega_p + \Omega_n$$
$$K_- = |\Omega_p - \Omega_n|$$
在纯单粒子图像下，$K_+$ 与 $K_-$ 态是严格简并的。然而实验表明，两者之间存在高达 $100 \sim 350\text{ keV}$ 的显著能量裂分，且其中必有一个构型优先成为奇奇核的基态带头！

根据 C. J. Gallagher & S. A. Moszkowski（Phys. Rev. 111, 1282, 1958）、N. D. Newby（Phys. Rev. 125, 2063, 1962）以及 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II（第 5 章）：
1. **短程吸引核力中的自旋交换优势**：
   质子与中子之间的有效剩余两体相互作用具有极强的自旋-自旋吸引项 $-V_{\sigma\sigma} \vec{\sigma}_p \cdot \vec{\sigma}_n$（在自旋单态 $S=0$ 与自旋三重态 $S=1$ 之间产生剧烈不对称）。该吸引力在**两核子的内禀自旋 $\vec{s}_p$ 与 $\vec{s}_n$ 互相平行时势能最低**；
2. **Gallagher-Moszkowski（GM）耦合定则**：
   **凡是使得质子与中子的内禀自旋投影具有相同符号（$\Sigma_p \cdot \Sigma_n > 0$，即内在自旋彼此平行）的那个 $K$ 值状态，其能量必然低于反平行状态，构成该准粒子组态的基态带头！**
3. **$K=0$ 能带的 Newby 奇偶位移（Newby Shift, $a_N$）**：
   当奇质子与奇中子恰好具有相同的 $\Omega$ 值时（$\Omega_p = \Omega_n$），$K_- = 0$。该带包含全套单自旋序列 $I = 0, 1, 2, 3, \dots$。由于核芯与两体短程相互作用的宇称反演对易性，转动能谱发生剧烈的奇偶交错阶跃（Newby Staggering），导致偶自旋与奇自旋序列产生宏观能量相对位移！

---

## 2. 严格物理推导与数学判据

### (1) Gallagher-Moszkowski 定则判定判据
已知质子与中子的 Nilsson 渐近参数，首先计算内禀自旋符号：
$$\Sigma_p = \Omega_p - \Lambda_p = \pm \frac{1}{2}, \qquad \Sigma_n = \Omega_n - \Lambda_n = \pm \frac{1}{2}$$

- **规则一：同号平行规则（$\Sigma_p \cdot \Sigma_n > 0$）**：
  若 $\Sigma_p$ 与 $\Sigma_n$ 符号相同（同为 $+1/2$ 或同为 $-1/2$）：
  此时两个自旋沿对称轴同向排列，相加态 $K_+$ 具有平行的内禀自旋：
  $$K_{\text{GM}} = K_+ = \Omega_p + \Omega_n \quad (\text{低能基态})$$
  $$K_{\text{unfav}} = K_- = |\Omega_p - \Omega_n| \quad (\text{激发态})$$

- **规则二：异号反向规则（$\Sigma_p \cdot \Sigma_n < 0$）**：
  若 $\Sigma_p$ 与 $\Sigma_n$ 符号相反（一个 $+1/2$，一个 $-1/2$）：
  此时两核子自旋在相减态 $K_-$ 中反而获得互相平行的空间排列：
  $$K_{\text{GM}} = K_- = |\Omega_p - \Omega_n| \quad (\text{低能基态})$$
  $$K_{\text{unfav}} = K_+ = \Omega_p + \Omega_n \quad (\text{激发态})$$

---

### (2) 剩余 $p-n$ 相互作用能裂分 $\Delta E_{\text{GM}}$
双重态之间的能级差由自旋相关势的矩阵元决定：
$$\Delta E_{\text{GM}} = E(K_{\text{unfav}}) - E(K_{\text{GM}}) = 2 |V_{\sigma\sigma}| \int \rho_p(\vec{r}) \rho_n(\vec{r}) d^3r$$
在微观 $\delta$ 力近似下，重叠积分可参数化为：
$$\Delta E_{\text{GM}} \approx \frac{2500}{A} \sqrt{\Omega_p \Omega_n}\text{ [keV]}$$
典型变形核中的裂分在 $150 \sim 300\text{ keV}$ 之间，这构成了奇奇核纲图中同质异能态或低激发能级精细排布的根本原因。

---

### (3) $K = 0$ 能带的 Newby 奇偶位移（Newby Shift）
对于 $\Omega_p = \Omega_n$ 的特殊情形，$K_- = 0$。根据量子力学，对称性要求哈密顿量中包含直接对合算符 $(-1)^{I+1}$：
$$E(I, K=0) = \frac{\hbar^2}{2\mathcal{J}} \left[ I(I + 1) + a_N (-1)^{I+1} \right]$$
其中 $a_N$ 为无量纲的 **Newby 解耦参数（Newby Shift Parameter）**，其物理量纲对应能量位移 $E_N = A_{\text{rot}} a_N$。
- **偶自旋序列（$I = 0, 2, 4, 6$）**：
  $$(-1)^{I+1} = -1 \implies E_{\text{even}}(I) = A_{\text{rot}} [I(I+1) - a_N]$$
  若 $a_N > 0$，所有偶自旋能级被整体下推！
- **奇自旋序列（$I = 1, 3, 5, 7$）**：
  $$(-1)^{I+1} = +1 \implies E_{\text{odd}}(I) = A_{\text{rot}} [I(I+1) + a_N]$$
  若 $a_N > 0$，所有奇自旋能级被整体上抬！
这种现象在 $^{166}\text{Ho}, ^{170}\text{Tm}$ 以及 $A \approx 130$ 区中被实验高度证实，若忽视 Newby 位移，实验自旋赋值将产生完全错位。

---

## 3. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/gallagher_moszkowski_coupling_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `gm` 命令。

### 运行示范（以典型形变奇奇核 $K=0$ 带为例）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py gm \
  --omega-p 2.5 --lambda-p 2 --omega-n 2.5 --lambda-n 3 \
  --A 130 --A-rot 20.0 --newby-shift 35.0 --json
```

### 计算输出核心物理特征：
1. **轨道解析与自旋对齐判定**：
   - 质子轨道 $\Omega_p = 5/2, \Lambda_p = 2 \implies \Sigma_p = +0.5$；
   - 中子轨道 $\Omega_n = 5/2, \Lambda_n = 3 \implies \Sigma_n = -0.5$；
   - 符号相反（$\Sigma_p \Sigma_n < 0$），自旋平行态为相减态；
2. **基态与激发态带头预言**：
   - **GM 规则优势基态带头：$K = |2.5 - 2.5| = 0.0$**；
   - 激发带头：$K = 2.5 + 2.5 = 5.0$；
   - 预言双重态能量裂分 $\Delta E_{\text{GM}} = 48.1\text{ keV}$；
3. **$K=0$ 能带 Newby 锯齿位移能谱**：
   - $I=0$ 基态受 $-35\text{ keV}$ 位移降至 $-35.0\text{ keV}$；
   - $I=1$ 态受 $+35\text{ keV}$ 位移升至 $75.0\text{ keV}$；
   - $I=2$ 态（转动能 $120\text{ keV}$）受 $-35\text{ keV}$ 位移降至 $85.0\text{ keV}$；
   - 偶奇交错清晰重现，彻底排除了平滑转动假设带来的谱线归属错误！

---

## 4. 与相关前沿概念的交叉引用
- [[chiral-geometry-tilted-axis-cranking-and-aplanarity]]：奇奇核中高 $j$ 质子粒子与中子空穴的相互取向正是手征几何的母体；
- [[nuclear-k-isomers-and-hindrance-systematics]]：利用 GM 定则预言的高 $K$ 构型（如 $K_+$）往往构成核素图中的长寿命 $K$-同质异能素；
- [[signature-inversion-and-triaxial-pn-interaction]]：当三轴形变增强时，单核子波函数的 Nilsson 表象与推转角动量对齐发生强非线性纠缠。
