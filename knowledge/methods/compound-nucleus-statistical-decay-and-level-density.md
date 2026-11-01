---
type: method
title: "复合核统计衰变、能级密度参数化与蒸发道竞争计算手册"
aliases: [复合核统计衰变, 能级密度计算, Hauser-Feshbach模型, 蒸发道截面评估, RIPL-2参数手册]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
topics: [compound-nucleus, hauser-feshbach, level-density, transmission-coefficients, evaporation-channels]
---

# 复合核统计衰变、能级密度参数化与蒸发道竞争计算手册

## 1. 物理框架：Bohr 独立性假设与 Hauser-Feshbach 统计理论

在重离子熔合反应中，当入射弹核与靶核克服库仑势垒发生完全熔合后，弹核的宏观动能通过核子间的剧烈多次两体碰撞完全热化，形成处于高激发能 $E^*$ 和高角动量 $J$ 的热平衡中间态——**复合核（Compound Nucleus, CN）**。

根据 Niels Bohr 经典独立性假定，复合核的退激衰变方式仅取决于其总能量、总自旋和宇称，与其形成的方式无关。
依据 Carlos Bertulani《Introduction to Nuclear Reactions》（第 6 章）与 IAEA RIPL-2（IAEA-TECDOC-1506），复合核向开通道 $\beta$（出射轻粒子如中子 $n$、质子 $p$、$\alpha$ 粒子或裂变通道）的衰变微分截面由**Hauser-Feshbach 统计公式**严格控制：

$$\sigma_{\alpha \beta}(E_{\text{inc}}) = \frac{\pi}{k_\alpha^2} \sum_{J^\pi} \frac{2J + 1}{(2I_p + 1)(2I_t + 1)} \cdot \frac{T_l^\alpha(E) \cdot \sum_{l', s'} T_{l'}^\beta(E')}{\sum_c T_c(E)}$$

其中分母是对所有在能量上允许的开放退激通道（中子、带电粒子、统计巨共振 $\gamma$ 射线发射及裂变）的总透射几率求和。

---

## 2. 能级密度（Nuclear Level Density）参数化理论

当复合核激发能高于核子分离能时，分立能级演化为致密的准连续区，粒子衰变速率强烈正比于残核的能级密度 $\rho(E^*, J^\pi)$。

### (1) 反冲费米气体模型（Back-Shifted Fermi Gas Model, BSFG）
IAEA RIPL-2 推荐的标准能级密度模型为 BSFG 公式：
$$\rho(U, J) = \frac{\sqrt{\pi}}{12} \frac{\exp(2\sqrt{a U})}{a^{1/4} U^{5/4}} \cdot \frac{2J + 1}{2\sqrt{2\pi} \sigma^3} \exp\left(-\frac{(J + 1/2)^2}{2\sigma^2}\right)$$
- **有效内禀激发能**：$U = E^* - \Delta_{\text{pair}}$（$\Delta_{\text{pair}}$ 为配对修正能，偶偶核 $\Delta > 0$，奇 $A$ 核 $\Delta \approx 0$，奇奇核 $\Delta < 0$）；
- **能级密度参数 $a$**：
  $$a \approx \frac{\pi^2}{6} g(\epsilon_F) \approx \frac{A}{8.5} \text{ MeV}^{-1}$$
  在闭壳附近，受壳效应影响 $a$ 值显著降低；在变形开壳区，$a$ 随质量数平滑增长。
- **自旋截止因子（Spin Cutoff Parameter）$\sigma^2$**：
  $$\sigma^2 = \frac{\mathcal{J}_{\text{rigid}}}{\hbar^2} \sqrt{\frac{U}{a}} \approx 0.0146 \cdot A^{5/3} \cdot \sqrt{\frac{U}{a}}$$
  它描述了激发核能级在不同自旋 $J$ 上的高斯展宽。高自旋下 $\rho(U, J)$ 迅速被截断，使得复合核优先通过蒸发轻粒子释放能量，最终降落至 yrast 转动带上沿。

---

## 3. 出射通道穿透系数与蒸发道竞争物理法则

### (1) 中子 vs 带电粒子蒸发竞争
- **中子蒸发通道（$xn$ 道）**：
  中子呈电中性，无库仑势垒，仅受离心势垒 $\frac{\hbar^2 l(l+1)}{2\mu r^2}$ 阻碍。只要残核激发能高于中子分离能 $S_n$（通常 $7 \sim 8\text{ MeV}$），中子穿透系数 $T_l^n \approx 1$。因此，**在富中子和近稳定线重离子熔合反应中，中子蒸发截面占据绝对主导（$>90\%$）**。
- **带电粒子蒸发通道（$yp, z\alpha$ 道）**：
  出射质子与 $\alpha$ 粒子必须克服残核的库仑势垒：
  $$V_C(p) \approx 1.44 \frac{(Z_{\text{CN}}-1)}{R_0 A^{1/3}} \approx 8 \sim 12\text{ MeV}$$
  $$V_C(\alpha) \approx 2.88 \frac{(Z_{\text{CN}}-2)}{R_0 A^{1/3}} \approx 16 \sim 22\text{ MeV}$$
  只有在质子滴线极缺中子核区（中子分离能极高，质子分离能极低甚至为负）或极高自旋离心力显著降低质子势垒时，带电粒子蒸发道才能与中子蒸发有效竞争。

### (2) 经验 $xn$ 蒸发道能量窗口速算准则
在设计熔合实验束流能量时，可利用以下经验解析法则快速定位最优截面峰位：
$$E^*_{\text{opt}}(x n) \approx \sum_{i=1}^x S_n(i) + x \cdot \langle E_{\text{kin}}^n \rangle$$
其中每个中子带走的平均动能为：
$$\langle E_{\text{kin}}^n \rangle \approx 2 T = 2 \sqrt{\frac{E^*}{a}} \approx 2.5 \sim 3.5\text{ MeV}$$

**典型 $A\approx 130$ 质量区蒸发窗口对照**：
- $3n$ 最佳复合核激发能：$E^* \approx 35 \sim 42\text{ MeV}$；
- $4n$ 最佳复合核激发能：$E^* \approx 45 \sim 55\text{ MeV}$；
- $5n$ 最佳复合核激发能：$E^* \approx 58 \sim 68\text{ MeV}$。

这套理论模型为利用 Python 编写精准截面预测与分析算法提供了严格的数学函数基准。
