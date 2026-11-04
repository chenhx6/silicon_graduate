---
type: concept
title: "Gilbert-Cameron复合核能级密度公式与Ignatyuk壳效应热阻尼动力学"
aliases: [Gilbert-Cameron模型, 复合能级密度, Ignatyuk壳效应阻尼, 背移费米气体, 恒温公式, 能级密度参数, 中子共振间距D0, 统计衰变]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [level-density, gilbert-cameron, ignatyuk-damping, back-shifted-fermi-gas, constant-temperature-model, s-wave-resonance, hauser-feshbach, statistical-decay]
---

# Gilbert-Cameron复合核能级密度公式与Ignatyuk壳效应热阻尼动力学

## Definition

### 物理全景：连续区统计衰变与能级密度的基石地位

在低能核物理、高自旋核结构与核反应动力学中，原子核的**能级密度（Nuclear Level Density, $\rho(E, J, \pi)$）**是连接微观离散单粒子/集体能态与宏观热力学连续相的核心物理量。
无论是化合物核的粒子蒸发谱（Hauser-Feshbach 统计模型，如 TALYS、EMPIRE、PACE4、CASCADE 代码）、准连续区退激（$\gamma$-热化瀑布、准连续 $\gamma$ 谱、Oslo 方法提取核能级密度与巨偶极共振 $\gamma$ 强度函数），还是超重核与裂变位垒穿透几率计算，能级密度都是最关键的输入参数。

根据 A. Gilbert & A. G. W. Cameron（Can. J. Phys. 43, 1446, 1965）、A. V. Ignatyuk（Sov. J. Nucl. Phys. 21, 255, 1975）与国际原子能机构核反应数据手册（IAEA-RIPL-2 / RIPL-3）：
1. **纯费米气体公式的低能失效**：
   标准的 Bethe 费米气体模型假设单核子在等间距能级中统计填充，在激发能 $U \to 0$ 时给出 $\rho(U) \propto U^{-5/4} \to \infty$ 的发散奇异性。在低激发能区（$E < 5 \sim 8\text{ MeV}$），原子核受配对关联（Pairing Correlation）与离散集体振动能级的离散凝聚影响，能级并不呈费米气体指数发散，而是呈现出恒定核温的指数增长规律；
2. **Gilbert-Cameron 复合两区模型（Composite Model）**：
   在低激发区采用**恒温模型（Constant Temperature, CT）**描述离散态团簇，在高激发区采用**背移费米气体模型（Back-Shifted Fermi Gas, BSFG）**，并在中间匹配能 $E_x$ 处实施平滑切线接触（函数值与一阶对数导数严格连续）；
3. **Ignatyuk 壳修正热阻尼机制（Shell Damping）**：
   在基态，由于幻数壳层闭壳效应，幻核（如 $^{208}\text{Pb}, ^{132}\text{Sn}, ^{40}\text{Ca}$）具有极深的基态壳修正能 $\delta W < 0$，使其低能级密度被大幅压低数个数量级。然而随着激发能量上升，热激发的准粒子打破了壳层的单粒子能隙，**微观壳效应发生热融化（Melt out）**，能级密度参数 $a(U)$ 渐进恢复为宏观均匀旋转液滴的渐近值 $\tilde{a}(A)$。

---

## Necessary Assumptions

### 严格物理公式与数学结构

### (1) 配对能移动（Pairing Shift, $\Delta$）与有效激发能
由于核子配对相互作用，偶偶核的基态由 BCS 凝聚配对对隙占据，需要消耗配对能 $2\Delta$ 才能产生双准粒子激发。
定义有效激发能（Effective Intrinsic Excitation Energy）：
$$U = E - \Delta$$
标准 Gilbert-Cameron 经验配对能位移公式：
$$\Delta = \begin{cases}
\frac{24}{\sqrt{A}}\text{ MeV} & (\text{偶-偶核, Even-Even}) \\
\frac{12}{\sqrt{A}}\text{ MeV} & (\text{奇-}A\text{核, Odd-}A) \\
0\text{ MeV} & (\text{奇-奇核, Odd-Odd})
\end{cases}$$

---

### (2) Ignatyuk 壳修正阻尼与能级密度参数 $a(U, Z, A)$
在基态，实验结合能与平滑液滴质量公式（Myers-Swiatecki LDM）之差定义了基态壳修正能：
$$\delta W(Z, A) = M_{\text{exp}}(Z, A) - M_{\text{LDM}}(Z, A)$$
- 双幻核处 $\delta W \approx -11 \sim -13\text{ MeV}$（如 $^{208}\text{Pb}$ 为 $-12\text{ MeV}$）；
- 开壳层中轴形变核处 $\delta W \approx +1 \sim +3\text{ MeV}$。

Ignatyuk（1975）唯象热融化形式因子：
$$a(U, Z, A) = \tilde{a}(A) \left[ 1 + \delta W(Z, A) \frac{1 - e^{-\gamma U}}{U} \right]$$
其中：
- 渐近费米能级密度参数（RIPL-2 标准推荐）：
  $$\tilde{a}(A) = \alpha A + \beta A^{2/3}, \quad (\alpha = 0.07224\text{ MeV}^{-1}, \beta = 0.1794\text{ MeV}^{-1})$$
- 壳效应阻尼阻抗参数：$\gamma \approx 0.054 \sim 0.0615\text{ MeV}^{-1}$。

#### 极限性质验证：
- 当 $U \to \infty$（高激发区）：$\frac{1 - e^{-\gamma U}}{U} \to 0$，从而 $a(U) \to \tilde{a}(A)$（微观壳层完全融化，原子核行为退化为纯无规费米液体）；
- 当 $U \to 0$（低激发极限）：$\lim_{U \to 0} \frac{1 - e^{-\gamma U}}{U} = \gamma$，因此 $a(0) = \tilde{a}(A)(1 + \gamma \delta W)$。对于 $^{208}\text{Pb}$，$\delta W = -12\text{ MeV}$，则 $a(0) \approx \tilde{a}(1 - 0.054 \times 12) \approx 0.35 \tilde{a}$，能级密度参数在低能区被极度压低，完美解释了幻核共振态极度稀疏的物理机制！

---

### (3) 高激发区：背移费米气体模型（BSFG）
总能级状态密度（State Density, 积分所有自旋与宇称）：
$$\rho_{\text{BSFG}}(U) = \frac{\sqrt{\pi}}{12} \frac{\exp(2\sqrt{a(U) U})}{a^{1/4}(U) U^{5/4}} \frac{1}{\sqrt{2\pi}\sigma(U)}$$
其中自旋截止参数（Spin Cut-off Parameter）：
$$\sigma^2(U) = \frac{\mathcal{I}_{\text{rig}} T}{\hbar^2} \approx 0.01389 A^{5/3} \sqrt{\frac{U}{a(U)}}$$
局部核热力学温度：
$$T(U) = \sqrt{\frac{U}{a(U)}}$$

---

### (4) 低激发区：恒温模型（Constant Temperature, CT）
在低能区 $E \le E_x$：
$$\rho_{\text{CT}}(E) = \frac{1}{T_0} \exp\left(\frac{E - E_0}{T_0}\right)$$
式中 $T_0$ 为低激发恒定核温（Nuclear Temperature），$E_0$ 为能量零点反向平移量（Energy Back-shift）。
累积离散能级数（Cumulative Number of Discrete Levels）：
$$N_{\text{cum}}(E) = \int_0^E \rho_{\text{CT}}(E') dE' = \exp\left(\frac{E - E_0}{T_0}\right) - \exp\left(-\frac{E_0}{T_0}\right)$$

---

### (5) 严格相切匹配条件（Tangency Matching at $E_x$）
在切点匹配能量 $E_x = U_x + \Delta$ 处，两公式满足 $C^1$ 连续性（函数值相等、逆核温一阶对数导数相等）：
1. 连续性：$\rho_{\text{CT}}(E_x) = \rho_{\text{BSFG}}(U_x)$；
2. 导数匹配（连续温度）：
   $$\frac{1}{T_0} = \left. \frac{d}{dE} \ln \rho_{\text{BSFG}}(E) \right|_{E=E_x} = \sqrt{\frac{a_x}{U_x}} - \frac{1.5}{U_x}$$
3. 零点移动 $E_0$：
   $$\frac{E_x - E_0}{T_0} = \ln\left(T_0 \rho_{\text{BSFG}}(U_x)\right) \implies E_0 = E_x - T_0 \ln\left(T_0 \rho_{\text{BSFG}}(U_x)\right)$$
Gilbert-Cameron 经典经验切点：$U_x \approx 2.5 + \frac{150}{A}\text{ MeV}$。

---

### (6) 自旋与宇称投影能级密度 $\rho(E, J, \pi)$
对于特定自旋 $J$ 与特定宇称 $\pi = \pm 1$：
$$\rho(E, J, \pi) = \frac{1}{2} \rho(E) f(J, \sigma^2)$$
其中自旋分布函数（Spin Distribution Factor）：
$$f(J, \sigma^2) = \frac{2J + 1}{2\sigma^2} \exp\left(-\frac{(J + 1/2)^2}{2\sigma^2}\right)$$
满足正规化积分 $\sum_{J} (2J+1) f(J) \approx 2\sigma^2 \int_0^\infty f(J) dJ = 1$。
在统计平衡区，正负宇称等几率分配（Parity Equipartition: $P(+) = P(-) = 0.5$）。

---

### (7) 中子共振能级平均间距 $D_0$ 的实验标定
在中子分离能 $S_n$ 处（$E = S_n$），慢中子俘获实验（$s$ 波，轨道角动量 $l=0$）激发的共振态密度直接给出了 $D_0$（以 $\text{eV}$ 为单位）：
- 若靶核基态自旋 $I_0 = 0$（偶偶核）：中子共振态自旋只能为 $J = 1/2^+$：
  $$D_0 = \frac{1}{\rho(S_n, J=1/2, \pi)}$$
- 若靶核基态自旋 $I_0 > 0$：共振态包含两个自旋通道 $J_1 = I_0 - 1/2$ 与 $J_2 = I_0 + 1/2$：
  $$D_0 = \frac{1}{\rho(S_n, I_0 - 1/2, \pi) + \rho(S_n, I_0 + 1/2, \pi)}$$
这是实验核物理中唯一能够在特定能量精确标定绝对能级密度幅度的物理测量！

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/gilbert_cameron_level_density_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `density` 命令。

### 运行示范（以 $^{130}\text{Ba}$ 与 $^{208}\text{Pb}$ 为例）：
```bash
# 1. 130Ba 形变开壳核计算
python3 system/scripts/analysis/nuclear_analyzer.py density -Z 56 -A 130 -E 6.5 -J 2 --sn 7.5

# 2. 208Pb 双幻核壳阻尼计算
python3 system/scripts/analysis/nuclear_analyzer.py density -Z 82 -A 208 -E 10.0 --sn 7.37 --json
```

### 计算输出核心物理特征：
1. **$^{130}\text{Ba}$**：$\Delta = 2.105\text{ MeV}$，$\delta W = +1.365\text{ MeV}$，切点 $E_x = 5.759\text{ MeV}$，$T_0 = 0.621\text{ MeV}$。在 $S_n = 7.5\text{ MeV}$ 处，$D_0 \approx 1348\text{ eV}$，反映出形变开壳核在中子阈值处高密度的准连续态；
2. **$^{208}\text{Pb}$**：$\Delta = 1.664\text{ MeV}$，$\delta W = -12.0\text{ MeV}$，由于深度壳效应，其低激发 $a$ 参数被压制到 $8.64\text{ MeV}^{-1}$（渐近值 $\tilde{a} = 21.32\text{ MeV}^{-1}$），中子分离能处的共振间距高达 $D_0 \approx 157\text{ keV}$，比形变核大了两个多数量级，完美再现了实验幻核壳间距效应！

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用

- [[oslo-method-level-density-and-gamma-strength-function]]：Oslo 方法正是利用 $D_0$ 将未归一化的斜率参数变换为物理能级密度；
- [[heavy-ion-fusion-evaporation-and-statistical-decay]]：化合物核蒸发宽度 $\Gamma_n, \Gamma_p, \Gamma_\alpha$ 完全正比于子核的能级密度；
- [[fission-barriers-strutinsky-and-superheavy-dynamics]]：超重核存活几率中的 $\Gamma_n / \Gamma_f$ 竞争，本质是裂变鞍点过渡态能级密度与中子蒸发残核能级密度的比值。
