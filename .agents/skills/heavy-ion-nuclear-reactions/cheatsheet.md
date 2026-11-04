# Cheatsheet: 重离子核反应动力学与实验设计速查卡

碰撞运动学、Bass 熔合势垒、Wong 穿透公式、反冲多普勒频移与实验参数速查卡。

---

## 1. 重离子碰撞运动学核心公式卡

| 物理量 | 符号与表达式 | 实用计算单位与典型取值 |
|---|---|---|
| 质心系有效能量 | $E_{\text{c.m.}} = \frac{A_t}{A_p + A_t} E_{\text{lab}}$ | $[\text{MeV}]$ |
| 相对运动约化质量 | $\mu = \frac{A_p A_t}{A_p + A_t} u$ | $u = 931.494\text{ MeV}/c^2$ |
| 质心系波数 | $k = \frac{\sqrt{2\mu E_{\text{c.m.}}}}{\hbar} = 0.2187 \sqrt{\frac{A_p A_t}{A_p + A_t} E_{\text{c.m.}} [\text{MeV}]}$ | $[\text{fm}^{-1}]$ |
| Sommerfeld 库仑参数 | $\eta = 0.1574 Z_p Z_t \sqrt{\frac{A_p A_t}{(A_p + A_t) E_{\text{c.m.}} [\text{MeV}]}}$ | 无量纲，重离子通常 $\eta \gg 1$ |
| 复合核反冲初动能 | $E_{\text{recoil}} = \frac{A_p}{A_p + A_t} E_{\text{c.m.}} = \frac{A_p A_t}{(A_p + A_t)^2} E_{\text{lab}}$ | $[\text{MeV}]$ |
| 反冲初速比率 | $\beta = \frac{v_{\text{recoil}}}{c} \a0.04635 \frac{\sqrt{A_p E_{\text{lab}} [\text{MeV}]}}{A_p + A_t}$ | 无量纲，通常在束反应 $\beta \sim 1\% - 3\%$ |
| 多普勒频移公式 | $E_\gamma(\theta) \approx E_{\gamma 0} (1 + \beta \cos\theta_{\text{det}})$ | 探测角为 $\theta_{\text{det}}$ |

---

## 2. 常用重离子在束实验弹-靶组合 Bass 势垒与几何参数速查

| 反应系统 (弹核 + 靶核) | 质心系能量比 $\frac{A_t}{A_p+A_t}$ | 势垒半径 $R_B\ [\text{fm}]$ | Bass 势垒 $V_B\ [\text{MeV}]$ | 对应实验室束能 $E_{\text{lab}}^{\text{th}}\ [\text{MeV}]$ | 典型应用能区与物理目标 |
|---|---|---|---|---|---|
| $^{12}\text{C} + {}^{116}\text{Cd}$ | $0.906$ | $10.15$ | $35.4$ | $39.1$ | $^{124}\text{Te}$ 高自旋集体带与八极态 |
| $^{13}\text{C} + {}^{124}\text{Sn}$ | $0.905$ | $10.32$ | $36.2$ | $40.0$ | $^{133,134}\text{Ba}$ 形状共存与剪刀振动 |
| $^{16}\text{O} + {}^{122}\text{Sn}$ | $0.884$ | $10.42$ | $47.6$ | $53.8$ | $^{134}\text{Ce}$ ($4n$), $^{133}\text{Ce}$ ($5n$) 三轴/摆动候选 |
| $^{16}\text{O} + {}^{120}\text{Sn}$ | $0.882$ | $10.38$ | $47.8$ | $54.2$ | $^{131,132}\text{Ce}$ ($5n/4n$) 关键手征双重带 |
| $^{18}\text{O} + {}^{124}\text{Sn}$ | $0.873$ | $10.51$ | $47.2$ | $54.1$ | $^{138}\text{Ba}$ 与中子过剩富中子核 |
| $^{30}\text{Si} + {}^{110}\text{Pd}$ | $0.786$ | $10.78$ | $74.2$ | $94.4$ | $^{136}\text{Nd}$ ($4n$) 手征与超形变带 |
| $^{34}\text{S} + {}^{104}\text{Pd}$ | $0.754$ | $10.85$ | $85.6$ | $113.5$ | $^{134}\text{Nd}$ ($4n$) 三轴形变转动带 |
| $^{40}\text{Ar} + {}^{100}\text{Mo}$ | $0.714$ | $10.92$ | $98.4$ | $137.8$ | $^{136}\text{Ce}$ ($4n$) 高自旋超形变研究 |

---

## 3. Wong 熔合截面与势垒分布计算卡

$$V_B \approx \frac{1.44 Z_1 Z_2}{R_B} - \frac{R_1 R_2}{R_1 + R_2} \frac{d_B}{a_B} \exp\left(-\frac{R_B - R_1 - R_2}{d_B}\right)$$

1. **Wong 单抛物线解析穿透公式**：
   $$\sigma_{\text{fus}}(E_{\text{c.m.}}) = \frac{\hbar\omega_B R_B^2}{2 E_{\text{c.m.}}} \ln\left[ 1 + \exp\left( \frac{2\pi (E_{\text{c.m.}} - V_B)}{\hbar\omega_B} \right) \right]$$
   - 极高能渐近线 ($E_{\text{c.m.}} \gg V_B$)：$\sigma_{\text{fus}} \approx \pi R_B^2 \left(1 - \frac{V_B}{E_{\text{c.m.}}}\right)$；
   - 深次垒渐近线 ($E_{\text{c.m.}} \ll V_B$)：$\sigma_{\text{fus}} \approx \frac{\hbar\omega_B R_B^2}{2 E_{\text{c.m.}}} \exp\left( \frac{2\pi (E_{\text{c.m.}} - V_B)}{\hbar\omega_B} \right)$；
2. **Rowley 熔合势垒分布二阶导数反演公式**：
   $$D_{\text{fus}}(E_{\text{c.m.}}) \equiv \frac{d^2(E_{\text{c.m.}} \sigma_{\text{fus}})}{d E_{\text{c.m.}}^2} = \pi R_B^2 \frac{2\pi}{\hbar\omega_B} \frac{\exp\left(\frac{2\pi(E_{\text{c.m.}}-V_B)}{\hbar\omega_B}\right)}{\left[1 + \exp\left(\frac{2\pi(E_{\text{c.m.}}-V_B)}{\hbar\omega_B}\right)\right]^2}$$
   - 单一势垒下的半高全宽：$\text{FWHM} = \frac{\ln(3 + 2\sqrt{2})}{\pi} \hbar\omega_B \a0.56 \cdot \hbar\omega_B$。

---

## 4. 复合核蒸发退激能耗与通道经验估算卡

| 出射粒子类别 | 库仑势垒阻挡 $V_C$ | 平均单粒子能量消耗 $\Delta E^*$ | 平均带走角动量 $\Delta l$ | 主导质量区与能区特征 |
|---|---|---|---|---|
| **中子 ($n$)** | $0\text{ MeV}$ (无库仑势垒) | $S_n + 2T \a10.5 - 11.5\text{ MeV}$ | $\sim 1\hbar$ ($s, p$ 波主导) | 稳定线及中重核区熔合蒸发主导通道 |
| **质子 ($p$)** | $V_C \sim 5 - 8\text{ MeV}$ | $S_p + V_C + 2T \a14 - 17\text{ MeV}$ | $\sim 1 - 2\hbar$ | 极缺中子区（接近质子滴线）剧烈竞争 |
| **$\alpha$ 粒子** | $V_C \sim 10 - 15\text{ MeV}$ | $S_\alpha + V_C + 2T \approx 20 - 25\text{ MeV}$ | $\sim 2 - 4\hbar$ | 轻核区及极高自旋离心势能过剩区 |
| **裂变 ($f$)** | 转动液滴势垒 $B_f(J)$ | 释放巨大动能 ($\sim 100 - 150\text{ MeV}$) | 损耗全部角动量 | 当复合核自旋超过 $\ell_{\text{fiss}} \sim 65 - 75\hbar$ 时阻断蒸发 |

---

## 5. 在束重离子反应实验机时与计数率速算公式

$$Y_{\text{peak}} = I_{\text{beam}} \cdot \left(\frac{N_A \cdot \rho t}{M_{\text{target}}}\right) \cdot \sigma_{\text{fus}} \cdot b_{xn} \cdot \epsilon_{\gamma} \cdot B_\gamma \cdot \epsilon_{\text{live}}$$

| 参数项 | 典型实验取值 | 换算系数与实用关系 |
|---|---|---|
| 束流强度 $I_{\text{beam}}$ | $1.0 - 2.0\text{ pnA}$ ($10^9 - 10^{10}\text{ pps}$) | $1\text{ pnA} = 6.24 \times 10^9\text{ ions/s}$ |
| 靶原子面密度 $N_{\text{target}}$ | $\rho t = 1.0\text{ mg/cm}^2, M = 120$ | $N_{\text{targ}} = \frac{10^{-3} \times 6.022 \times 10^{23}}{120} = 5.02 \times 10^{18}\text{ atoms/cm}^2$ |
| 反应总截面 $\sigma_{\text{fus}}$ | $500 - 1000\text{ mb}$ | $1\text{ b} = 10^{-24}\text{ cm}^2 \implies 1\text{ b} \times N_{\text{targ}} \approx 5.02 \times 10^{-6}$ |
| 目标残核通道分支比 $b_{xn}$ | $4n$ 或 $5n$ 峰位处 $\sim 40\% - 65\%$ | $0.40 - 0.65$ |
| HPGe 全能峰绝对效率 $\epsilon_\gamma$ | 大阵列单探测器 $\sim 0.1\% - 0.2\%$，总阵列 $\sim 5\% - 10\%$ | $1.33\text{ MeV}$ 处总阵列效率 $\sim 8\%$ |
| 符合二重事件产额比 | $Y_{\gamma\gamma} \approx Y_0 \cdot \epsilon_\gamma^2$ | 二重符合计数率约为总触发率的 $0.6\%$ |
