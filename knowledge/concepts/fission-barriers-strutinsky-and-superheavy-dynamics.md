---
type: concept
title: "双峰裂变势垒、Strutinsky壳修正动力学与超重核合成存活几率"
aliases: [双峰裂变势垒, 裂变异构体, Strutinsky壳修正, 裂变性参数, 超重核合成, 存活几率, 准裂变]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [nuclear-fission, fission-barrier, strutinsky-method, superheavy-elements, quasi-fission, survival-probability, liquid-drop-model]
---

# 双峰裂变势垒、Strutinsky壳修正动力学与超重核合成存活几率

## 1. 物理全景：经典液滴裂变性与量子壳效应的微观宏观统一

重核与超重核的大振幅裂变分裂（Fission）是微观核多体系统中结合能释放最大（$\sim 200\text{ MeV}$）、形变自由度最剧烈的相变动力学过程。

根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II（第 6 章）、C. A. Bertulani《Introduction to Nuclear Reactions》（第 5 章）、W. Greiner《Nuclear Models》、林承键《重离子核反应》与卢希庭《原子核物理（修订版）》（第 9 章）：
1. **宏观液滴模型（LDM）与裂变性参数（Fissility Parameter）**：
   在纯经典均匀液滴模型中，原子核的稳定性由表面张力势能（抵抗形变）与质子间库仑排斥能（促进裂变）的竞争决定：
   $$x \equiv \frac{E_C^{(0)}}{2 E_S^{(0)}} = \frac{Z^2 / A}{(Z^2 / A)_{\text{crit}}}, \quad (Z^2 / A)_{\text{crit}} \approx 50.883 \left[ 1 - 1.7826 \left(\frac{N - Z}{A}\right)^2 \right]$$
   - 当 $x < 1$ 时，存在有限的宏观裂变势垒 $B_f^{\text{LDM}}$；
   - 当 $x \ge 1$ 时（通常 $Z \ge 104$ 超重核区），宏观液滴裂变势垒彻底坍缩为零（$B_f^{\text{LDM}} = 0$），经典液滴在库仑斥力下将自发飞散！
2. **超重“稳定岛”的微观物理起源**：
   超重核为何能在实验中存活并被合成？其唯一物理根源在于**微观单粒子壳修正（Shell Correction Energy, $\Delta E_{\text{shell}}$）**！在满壳或准闭壳核区（如超重预言幻数 $Z=114, 120, 126$，$N=184$），基态单粒子能级密度极其稀疏，产生高达 $-5 \sim -8\text{ MeV}$ 的负壳修正，凭空构筑出高达数个 MeV 的微观诱导裂变势垒（$B_f \approx -\Delta E_{\text{shell}}$），赋予超重核可观测的宏观寿命。

---

## 2. Strutinsky 壳修正方法与双峰裂变势垒（Double-Humped Barrier）

### (1) Strutinsky 能量平滑法典（V. M. Strutinsky 1967）
宏观-微观结合模型（Macroscopic-Microscopic Method）将原子核总势能面分解为宏观平滑背景与量子微观修正之和：
$$E(Z, A, \text{def}) = E_{\text{macro}}(Z, A, \text{def}) + \Delta E_{\text{shell}}(Z, A, \text{def}) + \Delta E_{\text{pair}}(Z, A, \text{def})$$

微观壳修正通过对离散单粒子能级 $\varepsilon_i$ 进行非均匀高斯展开平滑获得：
$$\Delta E_{\text{shell}} = \sum_{i=1}^A \varepsilon_i - \int_{-\infty}^{\tilde{\lambda}} \varepsilon \tilde{g}(\varepsilon) d\varepsilon$$
其中平滑能级密度为：
$$\tilde{g}(\varepsilon) = \frac{1}{\gamma \sqrt{\pi}} \sum_i f_{\text{corr}}\left(\frac{\varepsilon - \varepsilon_i}{\gamma}\right) \exp\left[ -\left(\frac{\varepsilon - \varepsilon_i}{\gamma}\right)^2 \right]$$
通过选择平滑参数 $\gamma \approx 1.2 \hbar\omega_0 \approx 8 \sim 10\text{ MeV}$ 与 $p$ 阶修正多项式，使平滑能量严格满足平稳高原条件（Plateau Condition）。

### (2) 双峰裂变势垒与裂变同质异能素（Shape Isomers）
当原子核沿伸长形变方向（$\beta_2$）拉长时：
1. **第一势阱（Ground-state Well, $\beta_2 \sim 0.25$）**：对应原子核基态正常变形；
2. **第一鞍点（Inner Barrier $V_A$, $\beta_2 \sim 0.4$）**：三轴非轴对称形变（$\gamma \approx 20^\circ$）在此处显著降低势垒高度；
3. **第二势阱（Superdeformed Second Well, $\beta_2 \sim 0.6 \sim 0.7$）**：
   当长短轴之比达到 $2:1$ 时，单粒子轨道发生强烈的二次壳层闭壳简并（与超形变带物理机制同源），形成深达 $2 \sim 4\text{ MeV}$ 的亚稳第二势阱——即 **裂变同质异能素（Fission Isomer / Shape Isomer，Polikanov 1962 发现）**，其自发裂变半衰期比基态缩短数十个数量级（纳秒至毫秒级）；
4. **第二鞍点（Outer Barrier $V_B$, $\beta_2 \sim 0.8 \sim 0.9$）**：
   体系在此处强烈破坏空间反射对称性（产生八极梨形形变 $\beta_3 \ne 0$ 与质量不对称颈缩），直接决定了锕系核（$^{235}\text{U}, {}^{239}\text{Pu}$）裂变碎块呈现标志性的**不对称双峰质量分布（Asymmetric Mass Distribution）**！

---

## 3. 裂变穿透与统计衰变竞争：Hill-Wheeler 与 $\Gamma_n / \Gamma_f$

### (1) Hill-Wheeler 抛物线势垒穿透概率
对于高度为 $V$、曲率倒数频率为 $\hbar\omega$ 的反向抛物线势垒，能量为 $E$ 的复合核量子力学穿透几率由著名的 Hill-Wheeler 公式给出：
$$P_{\text{HW}}(E) = \frac{1}{1 + \exp\left[ \frac{2\pi (V - E)}{\hbar\omega} \right]}$$
当 $E \ll V$ 时，退化为经典 WKB 势垒贯穿因子：$P \propto \exp[-2\pi(V - E)/\hbar\omega]$。

### (2) Vandenbosch-Huizenga 中子蒸发与裂变分支比
在激发能 $E^*$ 下，复合核的退激主要由单中子蒸发（中子发射宽度 $\Gamma_n$）与裂变（裂变宽度 $\Gamma_f$）主导：
$$\frac{\Gamma_n}{\Gamma_f}(E^*) = \frac{2 m_n R^2 g_n}{\hbar^2} \frac{T^{1/2}}{2\sqrt{\pi} a_f^{1/2}} \exp\left[ 2\sqrt{a_n(E^* - B_n)} - 2\sqrt{a_f(E^* - B_f)} \right]$$
其中 $B_n$ 为中子分离能，$B_f$ 为有效裂变势垒，$a_n$ 与 $a_f$ 分别为中子发射与裂变鞍点的能级密度参数（通常取 $a_f / a_n \approx 1.05 \sim 1.15$）。

### (3) 壳修正的热阻尼退相干（Thermal Damping of Shell Effects）
随着复合核激发能（核温度 $T = \sqrt{E^*/a}$）升高，准粒子热占据抹平了费米面附近的壳间隙，**微观壳修正能呈指数阻尼衰减**：
$$\Delta E_{\text{shell}}(T) = \Delta E_{\text{shell}}(0) \cdot \exp\left( -\frac{T^2}{T_0^2} \right) = \Delta E_{\text{shell}}(0) \cdot \exp\left( -\frac{E^*}{E_D} \right)$$
其中特征阻尼能通常取 $E_D \approx 18 \sim 20\text{ MeV}$（阻尼温度 $T_0 \approx 1.2\text{ MeV}$）。这一热阻尼效应使得高激发超重核的裂变势垒急剧丧失，$\Gamma_n / \Gamma_f$ 迅速跌破 $10^{-2} \sim 10^{-3}$！

---

## 4. 超重核合成动力学：三步反应模型与截面微观反演

超重核残留截面（Evaporation Residue Cross Section, $\sigma_{\text{ER}}$）可严格因式分解为三阶段相乘：
$$\sigma_{\text{ER}}(E_{\text{c.m.}}) = \sum_{J=0}^{J_{\text{max}}} \sigma_{\text{cap}}(E_{\text{c.m.}}, J) \cdot P_{\text{CN}}(E_{\text{c.m.}}, J) \cdot P_{\text{surv}}(E^*, J)$$

1. **第一步：库仑俘获截面 $\sigma_{\text{cap}}$**：
   弹核克服入通道库仑势垒形成接触双核系统（DNS）的截面：
   $$\sigma_{\text{cap}} = \frac{\pi}{k^2} \sum_{J=0}^{J_{\text{max}}} (2J+1) T_J(E_{\text{c.m.}})$$
2. **第二步：复合核熔合几率 $P_{\text{CN}}$ 与准裂变竞争**：
   双核系统从接触形变演化跨越内部鞍点（Inner Saddle）融合成单一球形复合核的动力学几率。对于重核系统，强库仑力促使系统未跨越鞍点前直接沿对称质量轴分裂解体，发生**准裂变（Quasi-fission）**，导致 $P_{\text{CN}} \sim 10^{-3} \sim 10^{-5}$ 甚至更低；
3. **第三步：中子蒸发存活几率 $P_{\text{surv}}$**：
   形成复合核后通过连续发射 $x$ 个中子回到基态冷核并逃脱裂变淘汰的总几率：
   $$P_{\text{surv}}(E^*) = \prod_{i=1}^x \left( \frac{\Gamma_n}{\Gamma_n + \Gamma_f} \right)_i \approx \prod_{i=1}^x \left( \frac{\Gamma_n}{\Gamma_f} \right)_i$$

### (4) 冷熔合（Cold Fusion）vs 热熔合（Hot Fusion）对比法典
- **冷熔合路线（Cold Fusion，德国 GSI 主导）**：
  - 反应：$^{208}\text{Pb} / {}^{209}\text{Bi}$ 双幻硬球靶 + 稳定同位素弹核（如 $^{70}\text{Zn} + {}^{208}\text{Pb} \to {}^{277}\text{Cn} + 1n$）；
  - 优劣：复核极冷（$E^* \sim 12 \sim 15\text{ MeV}$），仅需发射 $1n$，$P_{\text{surv}}$ 相对极高；但弹靶库仑斥力极其巨大（$Z_1 Z_2 > 2000$），接触后极难克服内势垒发生熔合，$P_{\text{CN}}$ 急剧指数坍塌，导致 $Z \ge 113$ 时截面跌破 $1\text{ pb}$ 难以推进；
- **热熔合路线（Hot Fusion，俄罗斯杜布纳 JINR 主导）**：
  - 反应：富中子双幻弹核 $^{48}\text{Ca}$（$Z=20, N=28$）轰击富中子锕系靶（$^{244}\text{Pu}, {}^{248}\text{Cm}, {}^{249}\text{Cf}$）；
  - 优劣：弹靶质量不对称度大（$Z_1 Z_2 \sim 1900$），准裂变被显著抑制，$P_{\text{CN}}$ 提升数个数量级；虽然复核较热（$E^* \sim 35 \sim 45\text{ MeV}$），需蒸发 $3n \sim 4n$ 粒子，存活几率经受多次裂变削减，但最终合成截面仍维持在亚皮靶至数皮靶区间（$0.5 \sim 5\text{ pb}$），成功合成 $Z=114 \sim 118$（Fl, Mc, Lv, Ts, Og）全套超重元素！

---

## 5. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/fission_barrier_superheavy_calculator.py` 中实现了完整的裂变势垒与超重核合成计算器：
1. **液滴裂变性与势垒计算**：根据 Myers-Swiatecki 经典公式计算裂变参数 $x$ 与无壳修正时的宏观势垒 $B_f^{\text{LDM}}$；
2. **Strutinsky 双峰势垒轮廓建模**：重构第一势阱、第一鞍点 $V_A$、异构体极小 $E_{\text{iso}}$ 与第二鞍点 $V_B$ 的平滑势能曲线；
3. **Hill-Wheeler 量子穿透几率计算**：评估任意激发能下的裂变势垒透射系数；
4. **Vandenbosch-Huizenga 中子/裂变竞争比**：引入能级密度参数比与壳修正热阻尼阻尼因子，计算 $\Gamma_n / \Gamma_f$；
5. **超重核全链条截面预测器**：输入俘获截面、熔合几率与中子链参数，精确预言 $1n \sim 4n$ 通道超重残核合成截面 $\sigma_{\text{ER}}$（自动输出 pb/fb/nb）。

---

## 6. 权威文献与理论溯源

1. **Bohr, N. & Wheeler, J. A.** (1939). The mechanism of nuclear fission. *Phys. Rev.*, 56(5), 426-450.
2. **Strutinsky, V. M.** (1967). Intermediate states in fission. *Nucl. Phys. A*, 95(2), 420-442.
3. **Vandenbosch, R. & Huizenga, J. R.** (1973). *Nuclear Fission*. Academic Press, New York.
4. **Oganessian, Yu. Ts. & Utyonkov, V. K.** (2015). Super-heavy element research. *Rep. Prog. Phys.*, 78(3), 036301.
5. **Bertulani, C. A. & Danielewicz, P.** (2004). *Introduction to Nuclear Reactions*, Chapter 5 (Fusion and Fission). CRC Press.
6. **卢希庭、江栋兴、叶沿林** (2000). 《原子核物理（修订版）》第 9 章：核裂变与超重核. 原子能出版社.
7. **林承键** (2013). 《重离子核反应》第 4 章：完全熔合与准裂变竞争. 原子能出版社.
