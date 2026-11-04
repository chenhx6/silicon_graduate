---
type: method
title: "IAEA RIPL-2 能级密度、Ignatyuk 壳阻尼与伽马强度函数方法合同"
aliases: [IAEA-RIPL-contract, RIPL-level-density-contract, GLO-strength-function-contract]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: reaction-data-contract
tags: [ripl, nuclear-data, level-density, ignatyuk-damping, gamma-ray-strength-function, slo-model, glo-model, neutron-resonance-spacing]
topics: [ripl, level-density, photon-strength-functions, optical-model, hauser-feshbach]
sources: [book-iaea-reaction-data-handbook, book-bertulani-nuclear-reactions, book-lin-heavy-ion-reactions]
---

# IAEA RIPL-2 能级密度、Ignatyuk 壳阻尼与伽马强度函数方法合同

## Purpose

本方法合同严格绑定 IAEA《Handbook for Calculations of Nuclear Reaction Data: Reference Input Parameter Library-2 (RIPL-2)》（IAEA-TECDOC-1506, 2006）第 5、6、7 章（物理 PDF pp. 60–151），
系统形式化统计复合核反应计算中能级密度参数 $a(U)$ 的 Ignatyuk 激发能壳阻尼模型（式 6.8）、$s$-波中子共振平均间距 $D_0$ 的反演校准、
标准洛伦兹（SLO）与广义洛伦兹（GLO/EGLO）偶极辐射强度函数（式 7.3–7.8），以及 Koning-Delaroche 全局光学势参数化，
为重离子熔合蒸发截面、统计 $\gamma$ 退激级联、异能态布居与反应道设计提供权威核反应数据参考规范。

## Inputs and Assumptions

1. **复合核有效激发能与反冲位移**：$U = E^* - \Delta$（$\Delta$ 为配对修正回退能，偶偶核 $\Delta > 0$，奇奇核 $\Delta < 0$）；
2. **Ignatyuk 渐近壳阻尼假设**：当激发能 $U$ 升高时，单粒子壳效应被准粒子剧烈两体碰撞热化阻尼，能级密度参数 $a(U)$ 平滑衰减到无壳效应的液滴渐近值 $\widetilde{a}$；
3. **Brink-Axel 偶极巨共振假定**：假设建立在任意激发态上的等矢巨偶极共振（IVGDR）具有与基态相同的共振参数（能量 $E_r$、宽度 $\Gamma_r$ 与峰值截面 $\sigma_r$）；
4. **终端态温度依赖性**：伽马辐射强度函数依赖于终态核温度 $T_f = \sqrt{(U - \epsilon_\gamma)/a}$，确保低能辐射光子发射满足详细平衡原理。

## What It Can Establish

1. **Ignatyuk 能级密度参数能量依赖解析公式（式 6.8）**：
   $$a(U, Z, A) = \widetilde{a}(A) \left[ 1 + \delta W(Z, A) \frac{1 - \exp(-\gamma U)}{U} \right]$$
   - 渐近壳层平滑参数：$\widetilde{a}(A) = 0.073 A + 0.115 A^{2/3}\text{ MeV}^{-1}$；
   - 壳阻尼系数：$\gamma = 0.061\text{ MeV}^{-1}$，表明当激发能 $U \ge 40 - 50\text{ MeV}$ 时，壳效应衰减 $90\%$ 以上，能级密度完全回归均匀费米气体；
2. **从 $s$-波中子共振平均能级间距 $D_0$ 的严格反演方程（式 6.5）**：
   $$D_0^{-1} = \frac{1}{2} \left[ \rho(B_n + \Delta E/2, I_0 + 1/2) + \rho(B_n + \Delta E/2, I_0 - 1/2) \right]$$
   确立了利用热中子与共振中子实验直接提取原子核在结合能 $B_n$ 处绝对能级密度的金标准；
3. **辐射光子透射系数 $T_{XL}$ 与强度函数换算（式 7.3）**：
   $$T_{XL}(\epsilon_\gamma) = 2\pi \epsilon_\gamma^{2L+1} \overleftarrow{f}_{XL}(\epsilon_\gamma)$$
   - 标准洛伦兹（SLO）模型（式 7.4）：$\overleftarrow{f}_{\text{SLO}}(\epsilon_\gamma) = 8.674 \times 10^{-8} \frac{\sigma_r \Gamma_r^2 \epsilon_\gamma}{(\epsilon_\gamma^2 - E_r^2)^2 + (\Gamma_r \epsilon_\gamma)^2}\ (\text{MeV}^{-3})$；
   - 广义洛伦兹（GLO/EGLO）模型：引入温度依赖展宽 $\Gamma(E, T_f) = \Gamma_r \frac{E^2 + 4\pi^2 T_f^2}{E_r^2}$，精确再现低能区（$\epsilon_\gamma < 3\text{ MeV}$）的非零有限辐射吸收强度。

## What It Cannot Establish Alone

1. **低能奇特低能增强（Low-Energy Enhancement, LEE）的微观起源**：RIPL-2 的标准闭式强度函数在 $\epsilon_\gamma \to 0$ 处单调趋平，无法重现奥斯陆方法实验观测到的大质量区轻核与过渡核在 $\epsilon_\gamma < 2\text{ MeV}$ 处的反常上翘增益（LEE），需结合大型壳模型或 QRPA 准粒子自旋翻转；
2. **三轴核等矢巨共振（IVGDR）多模分裂细分**：RIPL 推荐的双峰洛伦兹拟合假设原子核为轴对称长椭球，若原子核具备显著三轴形变（$\gamma \ne 0$），横向模式分裂为长轴与短轴两个相近峰，需借助非弹光散射精细能谱解卷；
3. **极端丰中子滴线核的参数外推风险**：RIPL 参数库主要基于近稳定线靶核中子共振与实验激发函数拟合，直接外推至弱束缚滴线区时，连续态耦合会显著改变能级密度演化。

## Sources

- [[book-iaea-reaction-data-handbook]]：Chapters 5, 6, 7 (PDF pp. 60–151).
- [[book-bertulani-nuclear-reactions]]：Chapter 4 复合核反应与 Hauser-Feshbach 理论.
- [[gilbert-cameron-composite-level-density-and-shell-damping]]：Gilbert-Cameron 能级密度与壳阻尼.
- [[oslo-method-level-density-and-gamma-strength-function]]：奥斯陆方法能级密度与强度函数.
- [[giant-resonances-and-deformation-splitting]]：巨共振动力学与形变分裂.
