# 第 7 章：复合核统计衰变、Hauser-Feshbach 理论与蒸发自旋窗

**来源专著**：林承键《重离子核反应》（科学出版社 2017）第 6、7 章 & Bertulani《Introduction to Nuclear Reactions》（2021）第 4 章
**对应页码**：林书印刷 pp. 143–155, 177–195 / 物理 PDF pp. 153–165, 187–205；Bertulani PDF pp. 120–171

---

## 1. 核心理论推导与统计衰变体系

### 1.1 Bohr 独立性假设与完全平衡
重离子完全熔合后，初生体系在 $\sim 10^{-20}\text{ s}$ 内经历巨量核子双体碰撞，所有动能转化为核子无规热运动，形成热力学与统计平衡的复合核（Compound Nucleus, CN）：
- **Bohr 独立性原理**：复合核在给定总能量 $E^*$、总自旋 $J$ 与总宇称 $\pi$ 下的衰变几率与形成它的初始反应道完全无关：
  $$\sigma(a, b) = \sigma_{\text{form}}^{\text{CN}}(a; E^*, J^\pi) \cdot \frac{\Gamma_b(E^*, J^\pi)}{\sum_c \Gamma_c(E^*, J^\pi)}.$$

### 1.2 Hauser-Feshbach 统计截面微积分方程
严格考虑角动量与宇称完全守恒的统计截面公式（Bertulani 式 4.189）：
$$\sigma_{\alpha \beta}(E) = \frac{\pi}{k_\alpha^2} \sum_{J^\pi} \frac{2J + 1}{(2I_p + 1)(2I_t + 1)} \frac{\sum_{l, s} T_l^\alpha(E) \cdot \sum_{l', s'} T_{l'}^\beta(E')}{\sum_{\gamma} \sum_{l'', s''} T_{l''}^\gamma(E'')},$$
其中：
- $T_l(E)$ 为出射/入射通道的光学模型分波透射系数；
- 分母求和遍历所有开放的物理出射通道（$n, p, \alpha, d, t, \gamma$ 及裂变 $f$），包括各通道的离散已知能级求和与高激发能区连续能级密度积分：
  $$\sum_{\gamma} \int_0^{E^* - S_\gamma} \rho_{\gamma}(E^* - S_\gamma - \epsilon, J') \sum_{l''} T_{l''}^\gamma(\epsilon) d\epsilon.$$

---

## 2. 核能级密度与 Ignatyuk 能量依赖壳阻尼

### 2.1 Bethe 费米气体能级密度
在单粒子等间距费米气体模型中，激发能为 $U = E^* - \Delta_{\text{pair}}$ 时的总能级密度：
$$\rho(U, J) = \frac{2J + 1}{24 \sqrt{2} \sigma^3 a^{1/4} U^{5/4}} \exp\left( 2\sqrt{a U} - \frac{(J+1/2)^2}{2\sigma^2} \right),$$
其中自旋截止因子 $\sigma^2 = \frac{\mathcal{J}_{\text{rig}} T}{\hbar^2}$，核温 $T = \sqrt{U/a}$。

### 2.2 Ignatyuk 壳效应能量阻尼模型
真实的单粒子能级存在壳层修正能 $\delta W$（幻数闭壳处结合能额外增加数 $\text{MeV}$）。随着激发能上升，单粒子态热展宽逐渐抹平壳缝：
$$a(U) = \widetilde{a} \left[ 1 + \delta W \frac{1 - \exp(-\gamma U)}{U} \right],$$
参数：渐近费米能级密度参数 $\widetilde{a} \a0.073 A + 0.115 A^{2/3}\text{ MeV}^{-1}$，阻尼阻抗常数 $\gamma \a0.054\text{ MeV}^{-1}$。
- 当 $U < 10\text{ MeV}$ 时，微观壳效应剧烈影响能级密度；
- 当 $U > 40 - 50\text{ MeV}$ 时，指数因子 $e^{-\gamma U} \to 0$，能级密度参数平滑过渡为均匀无壳的渐近宏观值 $\widetilde{a}$。

---

## 3. 粒子蒸发与在束高自旋入口态自旋窗

### 3.1 蒸发通道选择性竞争规律
1. **中子发射（$xn$ 道）**：中子不带电荷，库仑势垒严格为零（$V_C = 0$）。因此在稳定线及中等质量核中，一旦激发能超过中子分离能（$E^* > S_n$），中子发射几率占绝对主导地位（分支比 $> 90\%$）；
2. **质子与 $\alpha$ 粒子发射**：受到强库仑势垒（$V_C \sim 6 - 15\text{ MeV}$）阻断，仅在质子滴线附近极度缺中子区（此时 $S_p \ll S_n$）或极高自旋离心势能极度过剩时才有可观竞争；
3. **裂变截断**：转动液滴模型预言裂变势垒随角动量升高急剧下降：$B_f(J) \approx B_f(0) - \Delta E_{\text{rot}}$。当复合核角动量超过临界裂变极限量 $\ell_{\text{fiss}} \sim 65 - 75\hbar$ 时，裂变宽度 $\Gamma_f \gg \Gamma_n$，复合核直接发生双体对称或非对称裂变，完全阻断蒸发残核形成。

### 3.2 入口态自旋窗与高自旋退激级联
- 初始复合核自旋分布覆盖 $0 \le J \le \ell_{\text{fiss}}$；
- 每个中子蒸发以 $s$ 波和 $p$ 波为主，平均带走约 $B_n + 2T \sim 10.5 - 11.5\text{ MeV}$ 能量，但仅带走约 $1\hbar$ 角动量；
- 连续蒸发 $4 - 5$ 个中子后，激发能降至粒子发射阈值以下（$E^* < S_n \approx 8\text{ MeV}$），体系进入**高自旋入口态区域（Entry States）**；
- 此时残核具有极高的剩余自旋（$I \approx 20 - 45\hbar$），随后纯粹通过快速统计偶极 $\gamma$ 射线（冷却能量）与带内集体四极跃迁（带走大量角动量）级联退激，高效率灌注并布居三轴形变手征带与高自旋摆动能带！

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/bertulani-reaction-mechanisms-and-hauser-feshbach-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`evaporation-channels` 子命令)
- **上游来源**：`knowledge/sources/book-bertulani-nuclear-reactions.md`
