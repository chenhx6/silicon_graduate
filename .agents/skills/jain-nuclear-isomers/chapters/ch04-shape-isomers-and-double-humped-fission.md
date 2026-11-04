# 第 4 章：形状异能态、双峰裂变势垒与超形变微观动力学

**来源专著**：Ashok Kumar Jain 等《Nuclear Isomers: A Primer》（Springer 2021）第 4 章
**对应页码**：印刷 pp. 53–70 / 物理 PDF pp. 65–82

---

## 1. 核心理论推导与双峰裂变势垒

### 1.1 Strutinsky 宏观-微观壳修正与第二极小
S. M. Polikanov 等人（1962）在前苏联杜布纳（Dubna）首次发现了寿命长达毫秒级的自发裂变同核异能态 $^{242m}\text{Am}$。
V. M. Strutinsky (1967) 建立了著名的壳修正理论：
总势能面为宏观转动液滴能与微观单粒子壳修正能之和：
$$V(\beta) = V_{\text{LDM}}(\beta) + \delta U_{\text{shell}}(\beta) + \delta P_{\text{pair}}(\beta).$$
1. **宏观液滴能**：随形变单调升高，在裂变鞍点处形成极宽的单峰极值；
2. **微观壳修正能的周期振荡**：
   - 当原子核处于正常形变（$\beta_2 \a0.25$，主轴比 $1.3:1$）时，产生第一势能极小（基态势阱）；
   - 随着核体进一步极度拉伸至**两主轴比达到严格的 $2:1$（超形变 Superdeformation, $\beta_2 \a0.60$）**时，由于单粒子谐振子频率呈现有理数简并（$\omega_\perp : \omega_z = 2 : 1$），微观单粒子态再次形成巨大的壳层闭壳间隙；
   - 这一巨大的负壳修正能叠加在宏观势垒顶峰，强行将单一势垒下压切裂出第二个局域极小深阱，形成著名的**双峰裂变势垒 (Double-Humped Fission Barrier)**！

---

## 2. 形状异能态 (Shape Isomers) 退激与 WKB 穿透

被俘获在第二极小深阱内的量子态称为**裂变形状异能态**（通常激发能 $E_{\text{II}} \approx 2 - 3\text{ MeV}$）：
- **两条退激路径的量子穿隧竞争**：
  1. **穿透外势垒（Outer Barrier $V_B$）**：直接发生自发裂变（Spontaneous Fission, SF）；
  2. **穿透内势垒（Inner Barrier $V_A$）**：退激回第一势阱基态，发射高能延迟 $\gamma$ 射线或延迟内转换电子；
- **WKB 准经典穿隧半衰期公式**：
  $$T_{1/2} = \frac{\ln 2}{\nu_0} \exp\left( \frac{2}{\hbar} \int_{s_1}^{s_2} \sqrt{2 B(s) [V(s) - E_0]} \, ds \right),$$
  其中惯量质量参数 $B(s)$ 随四极拉伸空间演化。极宽的势垒厚度使穿隧几率压低数十个数量级，产生纳秒至毫秒的宏观亚稳时标。

---

## 3. 标杆实验实验证实：第二极小内的超形变转动带
H. J. Specht 等人（1972）在 $^{240m}\text{Pu}$（$T_{1/2} = 3.8\text{ ns}$）的第二极小深阱内测得了一组极低能量的微弱转换电子序列，重构出超形变转动带：
- **转动惯量常数对比**：
  - 正常形变基态（第一极小）：$A_{\text{norm}} = \frac{\hbar^2}{2\mathcal{J}} \approx 7.2\text{ keV}$；
  - 形状异能态（第二极小）：$A_{\text{SD}} = \frac{\hbar^2}{2\mathcal{J}_{\text{SD}}} \approx 3.33\text{ keV}$！
- **终极几何判决**：转动惯量增加了整整 **$2.2$ 倍**，严格与主轴比 $2:1$ 的刚体长椭旋转相吻合，无可争议地直接证实了宏观形状异能态的存在。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/sources/book-jain-nuclear-isomers.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`fission-isomer` 子命令)
- **上游来源**：`knowledge/sources/book-jain-nuclear-isomers.md`
