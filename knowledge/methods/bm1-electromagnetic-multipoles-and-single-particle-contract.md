---
type: method
title: "Bohr & Mottelson Vol. I：电磁多极辐射场展开、单核子极化与 Weisskopf 单粒子基准合同"
aliases: [BM1 electromagnetic multipoles, Bohr Mottelson Weisskopf units, Schmidt limits single particle, E2 core polarization effective charge, BM1 Appendix 3C radiative transitions]
method_type: "electromagnetic-transition-theory-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Bohr & Mottelson Nuclear Structure Vol. I, Section 3-3 (printed pp.332-345 / PDF pp.351-364) and Appendix 3C (printed pp.379-391 / PDF pp.398-410)"
confidence: "high for analytical formulas, Wigner-Eckart reduced matrix elements, and Weisskopf conversion constants"
tags: [bohr-mottelson, vol1, electromagnetic-transitions, weisskopf-units, schmidt-limits, core-polarization, effective-charge, reduced-transition-probability]
sources: [book-bohr-mottelson-nuclear-structure]
---

# Bohr & Mottelson Vol. I：电磁多极辐射场展开、单核子极化与 Weisskopf 单粒子基准合同

## Purpose

本方法合同基于 Aage Bohr 与 Ben R. Mottelson 的巨著《Nuclear Structure》第一卷第 3 章 §3-3 与附录 3C 的系统研究，
解决原子核在束 \(\gamma\) 谱学与核衰变分析中单粒子与集体电磁跃迁几率的基准标定、多极辐射场展开以及单核子电磁矩微观修正的理论难题：
通过建立电多极（\(E\lambda\)）与磁多极（\(M\lambda\)）算符在长波近似下的标准球张量展开，
严格推导约化跃迁几率 \(B(\sigma\lambda)\) 与实测光子辐射跃迁速率 \(T(\sigma\lambda)\) 的绝对转换因子，
确立 Weisskopf 单粒子单位的模型无关定义、核芯四极极化有效电荷机制（\(e_{\rm eff}\)）与单粒子磁矩施密特极限（Schmidt limits），
为低能核结构与在束谱学建立坚不可摧的电磁观测量理论基石：

1. **电磁辐射多极场展开与跃迁几率解析表达（附录 3C-2）**：在长波极限 \(qr \ll 1\) 下，将麦克斯韦方程辐射场展开为定宇称球谐张量算符，严格给出跃迁速率 \(T(E\lambda), T(M\lambda)\) 与约化跃迁几率 \(B(E\lambda), B(M\lambda)\) 的显式系数；
2. **Weisskopf 单粒子单位基准定义（附录 3C-5）**：推导均匀电荷球模型半径 \(R = 1.2 A^{1/3}\text{ fm}\) 下任意阶 \(E\lambda\) 与 \(M\lambda\) 单粒子跃迁几率 \(B_W(\sigma\lambda)\) 的通用解析标度律；
3. **单核子四极矩与粒子–空穴反转（§3-3a）**：给出轨道 \((nl)j\) 单核子内禀四极矩 \(Q_{\rm sp} = -\frac{2j-1}{2(j+1)} \langle r^2 \rangle\) 的解析公式，证明粒子–空穴共轭导致的严格正负变号 \(Q_{\rm hole} = -Q_{\rm sp}\)；
4. **闭壳核芯四极极化与宏观有效电荷（§3-3a）**：解析证明价核子与 \(2\hbar\omega_0\) 巨四极共振（GQR）的虚耦合驱动核芯质子相干变形，导出有效电荷 \(e_{\rm eff} = e_{\rm bare} + e_{\rm pol}\)（中子 \(e_{\rm eff} \a0.5e\)，质子 \(e_{\rm eff} \a1.5e\)）；
5. **磁偶极矩算符与施密特极限（§3-3b）**：严格推导单核子两分支施密特线 \(\mu_{\rm sp}(j = l \pm 1/2)\)，确立单粒子磁偶极 \(M1\) 跃迁的 \(\Delta l=0\) 严格禁戒定则。

---

## Inputs and Assumptions

### 1. 长波近似（Long-Wavelength Approximation）

对于典型的核跃迁，光子能量 \(E_\gamma \le 5\text{ MeV}\)，对应波数 \(q = E_\gamma/(\hbar c) \le 0.025\text{ fm}^{-1}\)。
核半径 \(R \a1.2 A^{1/3}\text{ fm} \sim 7\text{ fm}\)，满足极小乘积条件：
\[
qr \ll 1
\]
在此极限下，球贝塞尔函数可展开为其领先项 \(j_\lambda(qr) \approx \frac{(qr)^\lambda}{(2\lambda+1)!!}\)，
多极电荷与电流密度算符约化为静态电多极矩与磁多极矩。

### 2. 多极算符球张量表示

- **电多极算符（Electric Multipole Operator）**：
  \[
  \mathcal{M}(E\lambda, \mu) = \sum_{k} e_k r_k^\lambda Y_{\lambda\mu}(\theta_k, \phi_k)
  \]
  宇称变化为 \(\Delta \pi = (-1)^\lambda\)。
- **磁多极算符（Magnetic Multipole Operator）**：
  \[
  \mathcal{M}(M\lambda, \mu) = \frac{\mu_N}{\hbar} \sum_k \left[ \frac{2}{\lambda+1} g_l^{(k)} \vec l_k + g_s^{(k)} \vec s_k \right] \cdot \vec\nabla (r_k^\lambda Y_{\lambda\mu})
  \]
  宇称变化为 \(\Delta \pi = (-1)^{\lambda+1}\)。
  自由核子回旋比设定为：\(g_l^p = 1\), \(g_l^n = 0\), \(g_s^p = +5.586\), \(g_s^n = -3.826\)。

---

## What It Can Establish

### 1. 辐射跃迁速率与减缩跃迁几率换算方程（式 3C-16–3C-18）

光子自发辐射跃迁几率定义为：
\[
T(\sigma\lambda; I_1 \to I_2) = \frac{8\pi(\lambda+1)}{\hbar \lambda [(2\lambda+1)!!]^2} \left(\frac{E_\gamma}{\hbar c}\right)^{2\lambda+1} B(\sigma\lambda; I_1 \to I_2)
\]
其中约化跃迁几率由初末态角动量归一化矩阵元给出：
\[
B(\sigma\lambda; I_1 \to I_2) = \frac{1}{2I_1 + 1} |\langle  I_2 \vert| \mathcal{M}(\sigma\lambda) |\vert  I_1 \rangle|^2
\]
对于常用前几阶跃迁，在标准实用单位（\(E_\gamma\) 单位为 MeV，\(B(E\lambda)\) 单位为 \(e^2\text{fm}^{2\lambda}\)，\(B(M\lambda)\) 单位为 \(\mu_N^2\text{fm}^{2\lambda-2}\)）下，跃迁速率为：
\[
\begin{aligned}
T(E1) &= 1.587 \times 10^{15} E_\gamma^3 B(E1) \quad [\text{s}^{-1}] \\
T(E2) &= 1.225 \times 10^9 E_\gamma^5 B(E2) \quad [\text{s}^{-1}] \\
T(E3) &= 5.709 \times 10^2 E_\gamma^7 B(E3) \quad [\text{s}^{-1}] \\
T(M1) &= 1.758 \times 10^{13} E_\gamma^3 B(M1) \quad [\text{s}^{-1}] \\
T(M2) &= 1.350 \times 10^7 E_\gamma^5 B(M2) \quad [\text{s}^{-1}]
\end{aligned}
\]

### 2. Weisskopf 单粒子单位解析定义（式 3C-38）

假定一个核子从 \(j_i = \lambda + 1/2\) 跃迁至 \(j_f = 1/2\)，径向波函数在半径 \(R = 1.2 A^{1/3}\text{ fm}\) 的硬球内常数分布：\(\langle r^\lambda \rangle = \frac{3}{\lambda+3} R^\lambda\)。
由此导出标准 Weisskopf 单粒子跃迁几率：
\[
B_W(E\lambda) = \frac{(1.2)^{2\lambda}}{4\pi} \left(\frac{3}{\lambda+3}\right)^2 A^{2\lambda/3} \quad [e^2\text{fm}^{2\lambda}]
\]
\[
B_W(M\lambda) = \frac{10}{\pi} \left(\frac{\hbar}{Mc}\right)^2 (1.2)^{2\lambda-2} \left(\frac{3}{\lambda+3}\right)^2 A^{(2\lambda-2)/3} \quad [\mu_N^2\text{fm}^{2\lambda-2}]
\]
常用基准标度数值：
- \(B_W(E1) = 0.06446 A^{2/3} \ e^2\text{fm}^2\)
- \(B_W(E2) = 0.05940 A^{4/3} \ e^2\text{fm}^4 = 5.940 \times 10^{-6} A^{4/3} \ e^2\text{b}^2\)
- \(B_W(E3) = 0.05940 A^2 \ e^2\text{fm}^6\)
- \(B_W(M1) = 1.7905 \ \mu_N^2\)（严格与质量数 \(A\) 无关！）
- \(B_W(M2) = 1.6501 A^{2/3} \ \mu_N^2\text{fm}^2\)

### 3. 单核子四极矩与粒子–空穴几何（式 3-25–3-28）

单个质子处于状态 \( \vert j, m=j\rangle\) 的内禀四极矩为：
\[
Q_{\rm sp} = \langle j, m=j  \vert r^2(3\cos^2\theta - 1)  \vert j, m=j \rangle = -\frac{2j-1}{2(j+1)} \langle r^2 \rangle
\]
负号物理本质：在最高取向 \(m=j\) 状态下，核子轨道运动几率集中分布于赤道平面，形成扁椭分布。
对于单质子空穴态，由于闭壳层缺失一个 \(m=-j\) 轨道，空穴在时间反演与粒子–空穴共轭下相因子为 \(-1\)，四极矩反号变为正值：
\[
Q_{\rm hole} = -Q_{\rm sp} = +\frac{2j-1}{2(j+1)} \langle r^2   \rangle
\]
单中子自身不带电荷，无极化单粒子四极矩为 0。

### 4. 核芯极化与微观有效电荷（式 3-32 邻文）

实测偶奇核单核子四极矩与单中子跃迁 \(B(E2)\) 显示强烈非零值。物理机制在于价核子四极场极化了闭壳核芯：
价核子与频率为 \(\Delta E \approx 2\hbar\omega_0 \a80 A^{-1/3}\text{ MeV}\) 的高能等标巨四极共振（ISGQR）产生微扰耦合虚激发，
驱动闭壳层全部 \(Z\) 个质子产生同相四极形变，从而引入极化电荷：
\[
e_{\rm pol} \approx \frac{Z}{A} e
\]
使单质子有效电荷重整化为 \(e_{\rm eff}(p) \a1.5e\)，单中子获得感生有效电荷 \(e_{\rm eff}(n) \a0.5e\)。

### 5. 磁偶极矩施密特极限（式 3-35–3-38）

单核子磁矩 \(\vec \mu = g_l \vec l + g_s \vec s\) 在 \(|j, m=j\rangle\) 态的期望值为解析施密特值：
\[
\mu_{\rm sp} = \begin{cases}
j \left[ g_l + \frac{g_s - g_l}{2l+1} \right], & j = l + 1/2 \\
j \left[ g_l - \frac{g_s - g_l}{2l+1} \right], & j = l - 1/2
\end{cases}
\]
单粒子 \(M1\) 跃迁矩阵元严格服从选择定则：\(\Delta n = 0\), \(\Delta l = 0\), \(\Delta j = 0, \pm 1\)。
由于磁偶极算符不包含径向坐标且为一阶自旋算符，不同主壳或不同轨道角动量 \(l\) 之间的单粒子跃迁严格禁戒（\(l\)-forbidden），
单粒子 \(M1\) 跃迁只能在同轨道自旋–轨道分裂伙伴 \(j = l + 1/2 \leftrightarrow j = l - 1/2\) 之间发生。

---

## What It Cannot Establish Alone

1. **Weisskopf 单位仅为量纲标尺而非真实结构预言**：
   Weisskopf 估计忽略了径向波函数的节点结构、结合能随轨道的变化、多核子配对关联与形变相干增强。实际测得 \(B(E2) \gg 1\text{ W.u.}\)（如 \(50\sim300\text{ W.u.}\)）是集体四极转动增强的确凿证据，而不能由单粒子模型描述；
2. **有效电荷存在局域壳层与同位旋依赖性**：
   简单的 \(e_{\rm pol} \a\a\approx pprox Z/A\) 是一阶平均场近似。在紧邻中子滴线或中子过剩核中，弱束缚中子晕轨道及等矢量四极极化会导致中子有效电荷发生显著漂移（\(e_{\rm eff}(n) \sim 0.2 - 0.7 e\)）；
3. **施密特极限未考虑介子交换流与高阶组态混合**：
   绝大多数真实单粒子态磁矩均位于两条施密特线围成的区域内部（施密特线淬灭）。这种衰减必须借由微观张量力核芯极化（Arima–Horie 机制）与 \(\Delta\)-同位旋激发交换流方能完全消除偏差。

---

## Sources

- [[book-bohr-mottelson-nuclear-structure]]：A. Bohr & B. R. Mottelson, *Nuclear Structure*, Vol. I: *Single-Particle Motion*, W. A. Benjamin (1969) / World Scientific (1998), Chapter 3 §3-3 (pp. 332–345) & Appendix 3C (pp. 379–391).
- [[microscopic-electromagnetic-transition-matrix-elements]]：微观核物理代数与电磁跃迁矩阵元推导全指南（Suhonen 与 Rose 相位约定）。
- [[electromagnetic-transition-rates-weisskopf-and-alaga-rules]]：原子核电磁跃迁几率、Weisskopf 单粒子估计与形变核 Alaga 分支规则法典。
- [[book-hamilton-electromagnetic-interaction]]：W. D. Hamilton, *The Electromagnetic Interaction in Nuclear Spectroscopy*, North-Holland (1975), Chapters 1–2.
