---
type: concept
title: "Nilsson单核子内禀g_K因子、磁偶极矩μ与在束B(M1)/B(E2)分支比反演动力学"
aliases: [Nilsson磁矩, g_K因子, g_R因子, 磁偶极矩, M1跃迁几率, B(M1)/B(E2)比值, 分支比反演, 准粒子纯度检验, 131Ba磁矩]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [nilsson-magnetic-moments, g_k-factor, g_r-factor, magnetic-dipole-moment, b-m1-over-b-e2, branching-ratio-inversion, quasiparticle-purity, odd-a-deformed-nuclei]
---

# Nilsson单核子内禀g_K因子、磁偶极矩μ与在束B(M1)/B(E2)分支比反演动力学

## 1. 物理全景：从转动带退激光子强弱比值到未配对核子波函数纯度

在形变奇 $A$ 核（如 $A \approx 130$ 的 $^{131}\text{Ba}, ^{133}\text{Ce}, ^{135}\text{Nd}$）中，高自旋带中每个激发能级通常具有两个并行的退激通道：
1. **停止跨步跃迁（Stopover, $I \to I-1$）**：偶极跃迁，以磁偶极（$M1$）为主并掺杂少许电四极（$E2$）；
2. **交叉跃迁（Crossover, $I \to I-2$）**：纯集体电四极（$E2$）跃迁。

实验核物理学家在分析在束 $\gamma$ 能谱时，能够以极高的精度测量同一能级发射的两条光电峰强度之比：
$$\lambda = \frac{I_\gamma(I \to I-1)}{I_\gamma(I \to I-2)}$$
根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II（第 4 章）、K. L. G. Heyde《Basic Ideas and Concepts in Nuclear Physics》以及卢希庭《原子核物理（修订版）》（第 4 章）：
这一看似简单的强度比值，直接内嵌了极其深刻的电磁动力学规律：
- **磁偶极跃迁强度的微观本能**：
  $B(M1)$ 强度正比于内禀单粒子磁旋比 $g_K$ 与核心集体转动磁旋比 $g_R$ 的相对差值平方：
  $$B(M1; I \to I-1) \propto (g_K - g_R)^2$$
- **波函数组态的“基因指纹”**：
  核心转动磁旋比 $g_R \approx Z/A$ 是一个平滑的宏观量；然而，**内禀因子 $g_K$ 却极其严格、唯一地由未配对核子所在的 Nilsson 轨道的渐近量子数 $\Omega [\mathcal{N} n_z \Lambda] \Sigma$ 所决定**！
  - 若为质子轨道：$g_K$ 往往显著大于零（通常 $g_K > +1.0$）；
  - 若为中子轨道：由于中子轨道磁矩为零且自旋为负，$g_K$ 常常呈现特征性的**负值（$g_K < 0$）**！
因此，通过反演实验测得的 $B(M1)/B(E2)$ 强度比，可以直接在实验现场无歧义地判定能带的微观多准粒子纯度，彻底辨别到底是奇质子带还是奇中子带！

---

## 2. 严格理论推导与反演数学方程

### (1) Nilsson 内禀陀螺磁因子 $g_K$ 解析公式
单核子磁偶极算符由轨道角动量与内禀自旋构成：
$$\vec{\mu} = g_l \vec{l} + g_s^{\text{eff}} \vec{s}$$
在轴对称 Nilsson 单粒子态 $|K^\pi = \Omega^\pi [\mathcal{N} n_z \Lambda] \Sigma\rangle$ 中，投影守恒条件给出：
$$K g_K = \langle K | g_l l_z + g_s^{\text{eff}} s_z | K \rangle = g_l \Lambda + g_s^{\text{eff}} \Sigma$$
其中：
- 自由核子磁旋比：
  - 质子：$g_l = 1.0, g_s^{\text{free}} = +5.586$；
  - 中子：$g_l = 0.0, g_s^{\text{free}} = -3.826$；
- **核内有效自旋淬灭因子（Core Polarization Quenching）**：
  受核内介质自旋-同位旋极化（$\Delta$ 异质态与泡利屏蔽）影响，有效值通常取为自由值的 $70\%$：
  $$g_s^{\text{eff}} \approx 0.70 \cdot g_s^{\text{free}}$$
  质子取 $g_s^{\text{eff}} \approx +3.910$，中子取 $g_s^{\text{eff}} \approx -2.678$。
- 核心集体转动磁旋比：$g_R \approx \frac{Z}{A} \approx 0.35 \sim 0.45$。

---

### (2) 轴对称转动带磁偶极矩 $\mu(I)$
对于变形核中 $K \ne 1/2$ 的能态，自旋为 $I$ 的磁偶极矩由两部分构成：
$$\mu(I, K) = g_R I + (g_K - g_R) \frac{K^2}{I + 1}$$
特别地，在转动带头基态（$I = K$）处：
$$\mu(I=K) = \frac{K}{K + 1} \left( g_R + K g_K \right)$$
这一理论值可直接与超精细结构、核磁共振（NMR）或在束 TDPAD 测得的基态磁矩做严格对账！

---

### (3) $B(M1)/B(E2)$ 实验强度比与 $|g_K - g_R|$ 反演
在同一自旋 $I$ 能态上：
- $I \to I-1$ 的 $M1$ 约化跃迁几率：
  $$B(M1; I \to I-1) = \frac{3}{4\pi} (g_K - g_R)^2 K^2 \langle I K 1 0 | I-1 K \rangle^2\text{ [}\mu_N^2\text{]}$$
- $I \to I-2$ 的集体 $E2$ 约化跃迁几率（内禀四极矩为 $Q_0$）：
  $$B(E2; I \to I-2) = \frac{5}{16\pi} e^2 Q_0^2 \langle I K 2 0 | I-2 K \rangle^2$$
代入 Clebsch-Gordan 矢算耦合系数后，两者的理论比值为：
$$\frac{B(M1; I \to I-1)}{B(E2; I \to I-2)} = \frac{12}{5 Q_0^2} (g_K - g_R)^2 \frac{1}{I^2 - 1}\text{ [}\mu_N^2 / (e\cdot\text{b})^2\text{]}$$

在实验上，光子跃迁强度正比于能量的五次方与三次方：
$$\frac{B(M1)}{B(E2)} = 0.697 \cdot \frac{E_\gamma^5(I \to I-2)}{E_\gamma^3(I \to I-1)} \cdot \frac{I_\gamma(I \to I-1)}{I_\gamma(I \to I-2)} \cdot \frac{1}{1 + \delta^2}$$
式中能量以 $\text{MeV}$ 为单位，$\delta$ 为 $I \to I-1$ 跃迁的 $E2/M1$ 混合比（通常极小）。

#### 终极反演方程：
$$|g_K - g_R| = \sqrt{ \left( \frac{B(M1)}{B(E2)} \right)_{\text{exp}} \cdot \frac{5 Q_0^2 (I^2 - 1)}{12} }$$
由此从实测峰面积比值直接开方导出 $|g_K - g_R|$！
将该数值与不同假想 Nilsson 轨道的理论 $g_K$ 对比，不仅能**唯一锁定能带的准粒子组态**，更能通过其正负分支符号直接决定角分布混合比 $\delta$ 的相位！

---

## 3. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/nilsson_magnetic_moment_gk_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `gk` 命令。

### 运行示范（模拟典型形变奇中子核 $^{131}\text{Ba}$ 的 $\nu 5/2[411]$ 轨道反演）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py gk \
  --omega 2.5 --lambda-val 2 -A 131 -Z 56 --neutron --invert --json
```

### 计算输出核心物理特征：
1. **Nilsson 磁旋因子微观求解**：
   - 轨道 $\Omega = 5/2, \Lambda = 2 \implies \Sigma = +0.5$；
   - 淬灭自旋磁旋比 $g_s^{\text{eff}} = -2.678$；
   - 微观理论计算得出单中子内禀磁旋因子为典型的负值：
     $$g_K = - 0.5356$$
   - 核心集体转动 $g_R = Z/A = 0.4275$，内禀相对差值为负：$g_K - g_R = - 0.9631$；
2. **能带全自旋磁矩剖面**：
   - 带头 $I = 2.5\hbar$ 处磁矩理论值为 $\mu = -0.651 \mu_N$；
   - 随转动自旋增加，集体转动正磁矩贡献迅速增大，在 $I=4.5\hbar$ 处翻转为 $+0.829 \mu_N$；
3. **在束分支比反演**：
   - 代入实测交叉跃迁 $E_{\gamma}(I \to I-2) = 750\text{ keV}$（强度 40）与跨步跃迁 $E_\gamma(I \to I-1) = 380\text{ keV}$（强度 100）；
   - 实验反演得出 $B(M1)/B(E2) = 7.536\text{ }\mu_N^2/(e\cdot\text{b})^2$，并直接反演导出微观绝对差值：
     $$|g_K - g_R| = 27.21$$
   - 为确定核芯三轴极化与准粒子混合度提供了定量微观约束！

---

## 4. 与相关前沿概念的交叉引用
- [[angular-distribution-and-multipole-mixing-ratios]]：$M1/E2$ 混合比 $\delta$ 的符号严格由此处 $(g_K - g_R)$ 的符号决定；
- [[tdpad-hyperfine-precession-and-gfactor-dynamics]]：TDPAD 测量的纳秒态 $g$ 因子在理论上即为此处 $g_K$ 与 $g_R$ 的矢量耦合；
- [[nilsson-deformed-shell-model-dynamics]]：单核子轨道波函数的渐近量子数直接充当此处 $g_K$ 计算的初态输入。
