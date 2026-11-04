# 第 2 章：重离子相互作用势、接近势与 Bass 熔合势垒

**来源专著**：林承键《重离子核反应》（科学出版社 2017）第 2 章 & Bertulani《Introduction to Nuclear Reactions》（2021）第 3、5 章
**对应页码**：林书印刷 pp. 18–36 / 物理 PDF pp. 28–46；Bertulani PDF pp. 80–119, 172–213

---

## 1. 核心理论推导与相互作用势体系

### 1.1 重离子总径向相互作用势的构成
在处理重离子碰撞与熔合时，弹核与靶核中心距离为 $r$ 时的总有效相互作用势为三大基本分量之和：
$$V_l(r) = V_C(r) + V_N(r) + V_{\text{cent}}(r) = V_C(r) + V_N(r) + \frac{\hbar^2 l(l+1)}{2 \mu r^2}.$$
1. **长程库仑势 $V_C(r)$**：
   在核外为纯点电荷库仑斥力：$V_C(r) = \frac{Z_1 Z_2 e^2}{r}$；当进入核重叠区（$r < R_C$）时，按两带电均匀球体电荷密度重叠积分平滑软化；
2. **短程强相互作用核吸引势 $V_N(r)$**：
   由核力在核表面引入的强吸引势场，随距离呈指数形式衰减；
3. **离心势垒 $V_{\text{cent}}(r)$**：
   由相对轨道角动量 $l$ 引入的反比于 $r^2$ 的动动量守恒斥力势。

### 1.2 接近势 (Proximity Potential) 定理
Błocki 与 Świątecki (1977) 基于液滴模型提出了著名的**接近力定理 (Proximity Force Theorem)**：
两个曲面接近时单位面积的相互吸引势能仅由两个平面之间的单位接触面积表面势能函数乘以曲率因子决定：
$$V_N(r) = 4 \pi \gamma \frac{R_1 R_2}{R_1 + R_2} b \cdot \Phi(\zeta),$$
其中：
- 核表面张力常数 $\gamma \a0.9517 [1 - 1.7826 ((N-Z)/A)^2]\text{ MeV/fm}^2$；
- 核弥散度表层厚度 $b \a1.0\text{ fm}$；
- 无量纲相对表面间距 $\zeta = \frac{r - R_1 - R_2}{b}$；
- 普适无量纲接近势函数：
  $$\Phi(\zeta) \approx \begin{cases} -\frac{1}{2}(\zeta - 2.54)^2 - 0.0852(\zeta - 2.54)^3, & \zeta \le 1.2511 \\ -3.437 \exp(-\zeta/0.75), & \zeta > 1.2511 \end{cases}.$$

---

## 2. Bass 经验熔合势垒模型

Bass (1974, 1977) 通过综合海量重离子实验熔合数据，建立了实验核物理中最具实用精度的熔合势垒参数化公式：
$$V_B = \frac{1.44 Z_1 Z_2}{R_B} - \frac{R_1 R_2}{R_1 + R_2} \frac{d_B}{a_B} \exp\left(-\frac{R_B - R_1 - R_2}{d_B}\right),$$
参数取值：
- 单核等效作用半径：$R_i = 1.16 A_i^{1/3} - 1.39 A_i^{-1/3}\text{ fm}$；
- 经验接触间距参数：$d_B = 1.35\text{ fm}$，$a_B = 0.033\text{ MeV}^{-1}\text{fm}^{-1}$；
- 势垒半径 $R_B$ 由势能一阶导数置零方程 $\left.\frac{dV_0(r)}{dr}\right|_{r=R_B} = 0$ 自洽求根确定：
  $$R_B \approx R_1 + R_2 + 2.0\text{ fm}.$$
Bass 势垒是重离子熔合反应规划中判断是否能够发生完全熔合的经典黄金准则。

---

## 3. 势能口袋条件与临界角动量极限

当相互作用势随 $r$ 具有极大值（势垒峰）与更小距离下的极小值（势能口袋 Pocket）时，体系才能形成暂态束缚系统并发生完全熔合：
1. **口袋充要条件**：
   $$\left.\frac{dV_l}{dr}\right|_{r = R_{\text{pocket}}} = 0, \quad \left.\frac{d^2 V_l}{dr^2}\right|_{r = R_{\text{pocket}}} > 0;$$
2. **离心势垒对口袋的压制与填平**：
   随轨道角动量 $l$ 持续增大，离心斥力 $\propto l(l+1)/r^2$ 迅速抬升，使得局部极小深谷逐步变浅；
3. **口袋消失临界角动量 ($\ell_{\text{pocket}}$)**：
   当 $\frac{d^2 V_l}{dr^2} = 0$ 且 $\frac{dV_l}{dr} = 0$ 发生在同一点（拐点接触）时，口袋彻底消失。当 $l > \ell_{\text{pocket}}$ 时，体系无法发生熔合，只能发生深部非弹性散射或快裂变。

---

## 4. 实验设计案例：在束熔合反应势垒计算
在实验设计 $^{16}\text{O} + {}^{120}\text{Sn} \to {}^{136}\text{Ce}^*$ 反应中：
- $R_1 = 1.16 \times 16^{1/3} - 1.39 \times 16^{-1/3} = 2.923 - 0.552 = 2.37\text{ fm}$；
- $R_2 = 1.16 \times 120^{1/3} - 1.39 \times 120^{-1/3} = 5.722 - 0.282 = 5.44\text{ fm}$；
- 势垒半径：$R_B \approx 2.37 + 5.44 + 2.00 = 9.81\text{ fm}$；
- 静电库仑项：$V_C(R_B) = \frac{1.44 \times 8 \times 50}{9.81} = 58.72\text{ MeV}$；
- 核吸引修正项：$\Delta V_N \approx -10.92\text{ MeV}$；
- 理论 Bass 势垒：$V_B \approx 47.8\text{ MeV}$；
- 换算到实验室系轰击阈能：$E_{\text{lab}}^{\text{th}} = \frac{16 + 120}{120} \times 47.8 = 54.17\text{ MeV} \approx 54.2\text{ MeV}$。
实验选定束能 $E_{\text{lab}} = 75 - 82\text{ MeV}$，显著越过熔合势垒，保证高自旋态的高效布居。

---

## 5. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/lin-heavy-ion-fusion-and-barrier-distribution-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`bass-barrier` 子命令)
- **上游来源**：`knowledge/sources/book-lin-heavy-ion-reactions.md`
