---
type: concept
title: "原子核电磁跃迁几率、Weisskopf单粒子估计与形变核Alaga分支规则法典"
aliases: [电磁跃迁几率, Weisskopf单位, 单粒子估计, Wu, Alaga规则, 分支比, 混合比delta, gK-gR提取]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [electromagnetic-transitions, weisskopf-units, alaga-rules, reduced-transition-probability, branching-ratios, mixing-ratios, deformed-rotors]
---

# 原子核电磁跃迁几率、Weisskopf单粒子估计与形变核Alaga分支规则法典

## 1. 物理全景：核态寿命、电磁跃迁多极性与微观波函数重叠

原子核激发态通过发射 $\gamma$ 光子或内转换电子退激的跃迁速率，直接由初末态波函数在电磁多极算符作用下的空间重叠积分决定：
$$T(\sigma \lambda) = \frac{8\pi (\lambda+1)}{\lambda [(2\lambda+1)!!]^2} \frac{1}{\hbar} \left(\frac{E_\gamma}{\hbar c}\right)^{2\lambda+1} B(\sigma \lambda; I_i \to I_f)$$
其中 $\sigma \lambda$ 代表电多极（$E\lambda$）或磁多极（$M\lambda$）跃迁，$B(\sigma \lambda)$ 为减缩跃迁几率（Reduced Transition Probability）。

根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. I（第 3 章）与 Vol. II（第 4 章）、K. Heyde《Basic Ideas in Nuclear Physics》、W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》（第 1–2 章）与卢希庭《原子核物理（修订版）》（第 3 章）：
1. **核集体性度规——Weisskopf 单粒子单位（Weisskopf Units, W.u.）**：
   通过假定单质子在具有刚性表面半径 $R = 1.2 A^{1/3}\text{ fm}$ 的球形势阱中从轨道 $j_i = \lambda + 1/2$ 跃迁至 $j_f = 1/2$，Victor Weisskopf 导出了模型无关的单粒子基准跃迁几率 $B_{\text{sp}}(\sigma \lambda)$：
   - 若实测 $B(E2) \sim 1\text{ W.u.}$：对应纯单核子单粒子跃迁；
   - 若实测 $B(E2) \sim 50 \sim 500\text{ W.u.}$：标志着数十乃至数百个核子参与宏观相干形变转动的**超强集体增强（Collective Enhancement）**；
   - 若实测 $B(E1) \sim 10^{-4} \sim 10^{-7}\text{ W.u.}$：表现为同位旋对称性或 $K$ 禁戒引起的剧烈阻碍；
2. **形变核几何分支法则——Alaga 规则（G. Alaga et al. 1955）**：
   在具有轴对称变形（好量子数 $K$）的刚性转子中，同一初态向同一转动带不同末态跃迁的减缩跃迁几率之比，完全由空间几何耦合的 Clebsch-Gordan 矢量相加系数严格决定！

---

## 2. Weisskopf 单粒子估计显式计算公式

在核物理标准单位（$E_\gamma$ 以 MeV 为单位，$B(E\lambda)$ 以 $e^2\text{fm}^{2\lambda}$ 为单位，$B(M\lambda)$ 以 $\mu_N^2\text{fm}^{2\lambda-2}$ 为单位）下：

### (1) 单粒子减缩跃迁几率定义式
$$B_{\text{sp}}(E\lambda) = \frac{(1.2)^{2\lambda}}{4\pi} \left(\frac{3}{\lambda+3}\right)^2 A^{2\lambda/3}\ [e^2\text{fm}^{2\lambda}]$$
$$B_{\text{sp}}(M\lambda) = \frac{10}{\pi} (1.2)^{2\lambda-2} \left(\frac{3}{\lambda+2}\right)^2 A^{(2\lambda-2)/3} \left(\frac{\hbar}{2 m_p c}\right)^2\ [\mu_N^2\text{fm}^{2\lambda-2}]$$

数值基准表：
- **$B(E1)_{\text{sp}} = 0.06446 \cdot A^{2/3}\ e^2\text{fm}^2$**
- **$B(E2)_{\text{sp}} = 0.05940 \cdot A^{4/3}\ e^2\text{fm}^4$**
- **$B(E3)_{\text{sp}} = 0.05940 \cdot A^2\ e^2\text{fm}^6$**
- **$B(M1)_{\text{sp}} = 1.7905\ \mu_N^2$**
- **$B(M2)_{\text{sp}} = 1.6501 \cdot A^{2/3}\ \mu_N^2\text{fm}^2$**

### (2) 跃迁速率与单粒子跃迁几率关系
- $T(E1) = 1.587 \times 10^{15} \cdot E_\gamma^3 \cdot B(E1)\ \text{s}^{-1}$
- $T(E2) = 1.225 \times 10^9 \cdot E_\gamma^5 \cdot B(E2)\ \text{s}^{-1}$
- $T(E3) = 5.709 \times 10^2 \cdot E_\gamma^7 \cdot B(E3)\ \text{s}^{-1}$
- $T(M1) = 1.758 \times 10^{13} \cdot E_\gamma^3 \cdot B(M1)\ \text{s}^{-1}$
- $T(M2) = 1.350 \times 10^7 \cdot E_\gamma^5 \cdot B(M2)\ \text{s}^{-1}$

---

## 3. 轴对称刚性转子 Alaga 分支规则法典

对于轴对称内禀形变核，核态波函数具有分离形式 $|I M K\rangle = \sqrt{\frac{2I+1}{8\pi^2}} D_{MK}^I(\theta_i) \chi_K$。

### (1) Alaga 分支比通用定理（Alaga 1955）
对于同一初态向同一带内两不同末态发射多极性为 $\lambda$ 的电磁辐射：
$$\frac{B(\lambda; I_i K_i \to I_{f1} K_f)}{B(\lambda; I_i K_i \to I_{f2} K_f)} = \frac{\langle I_i K_i \lambda (K_f - K_i) | I_{f1} K_f \rangle^2}{\langle I_i K_i \lambda (K_f - K_i) | I_{f2} K_f \rangle^2}$$

### (2) 偶偶核基态带经典 Alaga 比率基准
在 $K=0$ 的偶偶核基态带中，带内级联 $E2$ 跃迁减缩几率满足：
$$\frac{B(E2; I \to I-2)}{B(E2; 2^+ \to 0^+)} = \frac{\langle I 0 2 0 | I-2 0 \rangle^2}{\langle 2 0 2 0 | 0 0 \rangle^2} = \frac{15}{2} \frac{I (I - 1)}{(2I - 1)(2I + 1)}$$
特别地：
- **$B(E2; 4^+ \to 2^+) / B(E2; 2^+ \to 0^+) = 10/7 \approx 1.42857$**
- **$B(E2; 6^+ \to 4^+) / B(E2; 2^+ \to 0^+) = 1.5746$**
- **$B(E2; 8^+ \to 6^+) / B(E2; 2^+ \to 0^+) = 1.6495$**

若实验测得 $B(4^+ \to 2^+) / B(2^+ \to 0^+) \approx 2.0$（如非形变简谐振子比值），则判定体系处于球形谐振子声子态；若比值收敛至 $1.43$，则判定体系进入坚固的刚性轴对称转动相；若偏离 Alaga 比率，则直接反映了三轴非对称性（$\gamma$ 软度或 Davydov-Filipov 刚性三轴形变）！

---

## 4. 在束转动能带 $B(M1)/B(E2)$ 实验比值与 $|g_K - g_R|/Q_0$ 反演

在高自旋在束 $\gamma$ 谱学实验中，转动能带中高自旋态 $I$ 通常具有两条竞争退激路径：
1. **$\Delta I = 1$ 级联跃迁（$I \to I-1$）**：为 $M1 + E2$ 混合跃迁，光子能量为 $E_{\gamma 1}$，分支强度为 $I_{\gamma 1}$，多极混合比为 $\delta(E2/M1)$；
2. **$\Delta I = 2$ 跨级跨越跃迁（$I \to I-2$）**：为纯 $E2$ 跃迁，光子能量为 $E_{\gamma 2}$，分支强度为 $I_{\gamma 2}$。

### (1) 实验强度比向减缩跃迁比反演公式
根据多极辐射速率与探测光子强度关系：
$$\frac{B(M1; I \to I-1)}{B(E2; I \to I-2)} = 0.697 \cdot \frac{E_{\gamma 2}^5}{E_{\gamma 1}^3} \cdot \frac{I_{\gamma 1}}{I_{\gamma 2}} \cdot \frac{1}{1 + \delta^2} \quad \left[ \frac{\mu_N^2}{e^2\text{b}^2} \right]$$
（式中 $E_\gamma$ 单位为 MeV，强度 $I_\gamma$ 为相对探测计数率）。

### (2) 刚性变形核转子模型解析反演
根据强耦合粒子-转子模型（PRM），带内跃迁强度解析式为：
$$B(E2; I \to I-2) = \frac{5}{16\pi} e^2 Q_0^2 \langle I K 2 0 | I-2 K \rangle^2$$
$$B(M1; I \to I-1) = \frac{3}{4\pi} (g_K - g_R)^2 K^2 \langle I K 1 0 | I-1 K \rangle^2$$
由此导出国际通用的**理论比值几何方程**：
$$\frac{B(M1; I \to I-1)}{B(E2; I \to I-2)} = \frac{12}{5} \frac{(g_K - g_R)^2}{Q_0^2} \frac{K^2}{I^2 - 1}$$
通过沿自旋 $I$ 拟合实测比值，可**直接绝对提取核心物理量 $|g_K - g_R| / Q_0$**，从而在未知绝对寿命的情况下，高精度鉴别单粒子准粒子轨道归属与核芯内禀电四极矩 $Q_0$！

---

## 5. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/electromagnetic_transition_alaga_calculator.py` 中实现了完整的电磁跃迁分析器：
1. **Weisskopf 单粒子基准转换器**：输入任意质量数 $A$，自动输出 $E1, E2, E3, M1, M2$ 的单粒子值与物理寿命转换因子；
2. **寿命 $\tau \leftrightarrow B(E2)$ 互演器**：从测得的皮秒寿命精确反演 $B(E2)$（$e^2\text{b}^2$ 与 W.u.）及内禀电四极矩 $Q_0$；
3. **Alaga 规则自洽性检验器**：输入自旋与 $K$ 量子数，计算 Clebsch-Gordan 理论预测比，并与实测矩阵元比值执行相容性检验；
4. **束内级联 $B(M1)/B(E2)$ 反演器**：输入 $E_{\gamma 1}, E_{\gamma 2}, I_{\gamma 1}, I_{\gamma 2}$ 与混合比 $\delta$，计算绝对比值并反演 $|g_K - g_R| / Q_0$。

---

## 6. 权威文献与理论溯源

1. **Alaga, G., Alder, K., Bohr, A., & Mottelson, B. R.** (1955). Intensity rules for beta and gamma transitions to nuclear rotational states. *K. Dan. Vidensk. Selsk. Mat. Fys. Medd.*, 29(9), 1-22.
2. **Weisskopf, V. F.** (1951). Radiative transition probabilities in nuclei. *Phys. Rev.*, 83(5), 1073.
3. **Hamilton, W. D.** (1975). *The Electromagnetic Interaction in Nuclear Spectroscopy*, Chapters 1, 2, 7. North-Holland.
4. **Bohr, A. & Mottelson, B. R.** (1975). *Nuclear Structure*, Vol. II, Chapter 4 (Electromagnetic Transitions). Benjamin, New York.
5. **卢希庭、江栋兴、叶沿林** (2000). 《原子核物理（修订版）》第 3 章：原子核电磁跃迁. 原子能出版社.
