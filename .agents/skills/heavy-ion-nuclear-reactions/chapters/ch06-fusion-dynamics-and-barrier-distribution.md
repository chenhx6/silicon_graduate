# 第 6 章：重离子熔合动力学、Wong 穿透公式与 Rowley 势垒分布

**来源专著**：林承键《重离子核反应》（科学出版社 2017）第 6 章 & Bertulani《Introduction to Nuclear Reactions》（2021）第 5 章
**对应页码**：林书印刷 pp. 134–176 / 物理 PDF pp. 144–186；Bertulani PDF pp. 172–213

---

## 1. 核心理论推导与熔合穿透模型

### 1.1 经典锐截止模型 (Sharp Cutoff Model)
假定凡是轨道角动量小于临界角动量 $\ell_n_{\text{crit}}$ 的分波全部发生熔合，而 $l > \ell_n_{\text{crit}}$ 的分波完全不熔合：
$$\sigma_{\text{fus}} = \frac{\pi}{k^2} \sum_{l=0}^{\ell_n_{\text{crit}}} (2l+1) = \frac{\pi}{k^2} (\ell_n_{\text{crit}} + 1)^2 \approx \frac{\pi}{k^2} \ell_n_{\text{crit}}^2.$$
由掠碰能量守恒条件 $E_{\text{c.m.}} = V_B + \frac{\hbar^2 \ell_n_{\text{crit}}^2}{2 \mu R_B^2}$，导出经典熔合截面解析式：
$$\sigma_{\text{fus}}(E_{\text{c.m.}}) = \pi R_B^2 \left( 1 - \frac{V_B}{E_{\text{c.m.}}} \right).$$
该公式预言：截面随 $1/E_{\text{c.m.}}$ 呈线性关系；当 $E_{\text{c.m.}} \le V_B$ 时截面严格为零。

### 1.2 Hill-Wheeler 量子穿透概率与 Wong 公式
真实的原子核具有量子波动性，在近垒与次垒能区具有显著的量子隧穿几率。
- **Hill-Wheeler 反转简谐势垒穿透因子**：
  $$T_l(E) = \frac{1}{1 + \exp\left( \frac{2\pi (V_l - E)}{\hbar\omega_l} \right)};$$
- **Wong 熔合截面积分解**（将分波求和化为关于角动量平滑积分）：
  $$\sigma_{\text{fus}}(E_{\text{c.m.}}) = \frac{\pi}{k^2} \int_0^\infty 2l \, dl \, T_l(E_{\text{c.m.}}) = \frac{\hbar\omega_B R_B^2}{2 E_{\text{c.m.}}} \ln\left[ 1 + \exp\left( \frac{2\pi (E_{\text{c.m.}} - V_B)}{\hbar\omega_B} \right) \right].$$
Wong 公式不仅在高能区渐近还原为经典公式，更在深次垒区平滑过渡为指数穿透：
$$\sigma_{\text{fus}}(E_{\text{c.m.}} \ll V_B) \propto \exp\left( \frac{2\pi (E_{\text{c.m.}} - V_B)}{\hbar\omega_B} \right).$$

---

## 2. 次垒熔合增强与耦合道效应 (Coupled-Channels)

### 2.1 实验观测与一维单势垒模型的破缺
20 世纪 80 年代的大量精密实验发现：在中重核次垒熔合中，**实测截面比单势垒 Wong 预言高出整整 2 到 3 个数量级**！
**物理机制**：弹核与靶核在相互接近过程中，不是两块刚体球；它们具有内禀表面低频振动（$2^+, 3^-$ 声子）及基态静态形变（$\beta_2, \beta_4$）。这种内禀自由度与相对轨道运动发生强烈的**非绝热强耦合（Coupled-Channels）**。

### 2.2 Rowley 熔合势垒分布二阶导数反演定理
Rowley、Satchler 与 Stelson (1991) 提出了著名的势垒分布反演定理：
将能量乘截面 $E_{\text{c.m.}} \sigma_{\text{fus}}$ 对质心能量求二阶导数：
$$D_{\text{fus}}(E_{\text{c.m.}}) \equiv \frac{d^2(E_{\text{c.m.}} \sigma_{\text{fus}})}{d E_{\text{c.m.}}^2}.$$
- **单势垒标准峰形**：
  $$D_{\text{fus}}(E) = \pi R_B^2 \frac{2\pi}{\hbar\omega_B} \frac{\exp\left(\frac{2\pi(E-V_B)}{\hbar\omega_B}\right)}{\left[ 1 + \exp\left(\frac{2\pi(E-V_B)}{\hbar\omega_B}\right) \right]^2}, \quad \text{FWHM} = 0.56 \hbar\omega_B;$$
- **多重势垒流分裂（形变效应直接成像）**：
  对于具有轴对称四极形变 $\beta_2$ 的靶核，由于碰撞取向角 $\theta$ 的随机性，势垒高度依赖于空间取向：
  $$V_B(\theta) \approx V_B^{(0)} \left[ 1 - \sqrt{\frac{5}{4\pi}} \beta_2 P_2(\cos\theta) \right].$$
  - **对头碰撞（Tip-to-Tip）**：接触半径最大，库仑势垒显著降低（可降低数 $\text{MeV}$），使得次垒熔合截面发生爆发式指数增强；
  - **侧向碰撞（Side-by-Side）**：接触半径变小，库仑势垒升高。
  二阶导数 $D_{\text{fus}}(E)$ 呈现出结构分立的双峰或多峰，其实验分裂间距 $\Delta V_B$ 直接测定原子核的真实基态形变度 $\beta_2$。

---

## 3. 在束谱学应用：自旋分布拓扑与高自旋带布居
复合核形成的初态自旋分布直接决定了后续高自旋带的产额：
$$\sigma(l) = \frac{\pi}{k^2} (2l+1) T_l(E_{\text{c.m.}}).$$
- 在单势垒模型下，自旋分布在低能下被严格限制在低分波；
- **形变耦合道效应的自旋扩展**：耦合道效应显著将自旋分布尾部向更高角动量方向拓宽，甚至在次垒能量下也能布居到高达 $30 - 40\hbar$ 的高自旋态，为在束 $\gamma$ 谱学寻找三轴高声子摆动态和第二/第三手征带提供了前所未有的自旋充盈度。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/lin-heavy-ion-fusion-and-barrier-distribution-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`barrier-distribution` 子命令)
- **上游来源**：`knowledge/sources/book-lin-heavy-ion-reactions.md`
