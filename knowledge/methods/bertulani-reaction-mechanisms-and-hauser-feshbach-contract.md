---
type: method
title: "Bertulani-Danielewicz 复合核统计理论与直接反应方法合同"
aliases: [Bertulani-reaction-contract, Hauser-Feshbach-contract, DWBA-transfer-contract]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: reaction-theory-contract
tags: [bertulani, nuclear-reactions, hauser-feshbach, compound-nucleus, dwba, transfer-reactions, transmission-coefficients]
topics: [nuclear-reactions, hauser-feshbach, compound-nucleus, dwba, transfer-reactions]
sources: [book-bertulani-nuclear-reactions, book-lin-heavy-ion-reactions, book-lu-nuclear-physics-chinese]
---

# Bertulani-Danielewicz 复合核统计理论与直接反应方法合同

## Purpose

本方法合同严格绑定 Carlos A. Bertulani & Pawel Danielewicz《Introduction to Nuclear Reactions》（CRC Press 2021 第二版）第 4、5、6 章（印刷 pp. 109–254 / 物理 PDF pp. 120–265），
系统形式化复合核统计衰变中的 Hauser-Feshbach 微积分方程（式 4.180–4.189）、透射系数 $T_l$ 宇称选择定则、重离子近垒熔合动力学，以及扭曲波玻恩近似（DWBA）单核子转移反应与动量转移分析，
为在束重离子反应出射道预测、蒸发剩余核截面计算与转移反应单粒子光谱因子反演提供权威物理规范。

## Inputs and Assumptions

1. **Bohr 独立性假设与连续能量平均**：复合核在充分弛豫的热平衡态下衰变，从初态通道 $c$ 到终态通道 $c'$ 的截面在能量平均下可分解为形成截面与衰变分支比的乘积（式 4.181）：
   $$\sigma_{cc'}^{J\pi} = \sigma_{\text{CN}}^{J\pi}(c) \cdot \frac{\Gamma_{c'}^{J\pi}}{\Gamma^{J\pi}}$$
2. **光学模型透射系数（Transmission Coefficients）**：出射与入射分波穿透系数由复光学模型势求解通道薛定谔方程严格确定：$T_l = 1 - |\langle S_l \rangle|^2$；
3. **角动量与宇称完全守恒**：总角动量 $\vec{J} = \vec{l} + \vec{s}$（通道自旋 $\vec{s} = \vec{i} + \vec{I}$）与宇称 $\pi = \pi_{\text{proj}} \cdot \pi_{\text{targ}} \cdot (-1)^l$ 严格守恒；
4. **DWBA 一阶微扰假设**：直接转移反应发生于掠射碰撞外围（Grazing collision），相互作用势在入射与出射扭曲波通道之间按一阶矩阵元展开。

## What It Can Establish

1. **角动量与宇称相关的 Hauser-Feshbach 统计截面公式（式 4.189）**：
   $$\sigma_{cc'} = \frac{\pi}{k^2} \sum_J \frac{2J + 1}{(2i_c + 1)(2I_c + 1)} \frac{\sum_{s, l} T_l(c) \cdot \sum_{s', l'} T_{l'}(c')}{\sum_c \sum_{s, l} T_l(c)}$$
   - 严格给出了考虑自旋宇称守恒下，各轻粒子蒸发通道（$xn, yp, z\alpha$）与剩余核能级密度的耦合跃迁截面；
   - 证明库仑势垒使得低能中子发射（$xn$ 道，$V_C=0$）在稳定线及中高质量区熔合反应中占据压倒性优势；
2. **宇称守恒对出射角动量的强选择定则**：
   - 正宇称复合核状态（$\pi_{\text{CN}} = +$）退激到正宇称残核仅允许偶数分波 $l = 0, 2, 4, \dots$；
   - 退激到负宇称残核仅允许奇数分波 $l = 1, 3, 5, \dots$，为特征 $\gamma$ 射线角分布的 Legendre 展开系数奇偶性提供根基；
3. **DWBA 转移反应角分布形状与轨道角动量 $\Delta l$ 测定**：
   - 微分截面主峰角位 $\theta_{\text{peak}}$ 严格由动量转移关系 $q = |\vec{p}_a - \vec{p}_b| \approx l/R$ 决定；
   - 实验测量角分布前向峰位置可无歧义反演被转移核子的轨道角动量 $l$（如 $s, p, d, f, g, h$ 轨道），并提取绝对光谱因子 $S_{lj}$。

## What It Cannot Establish Alone

1. **预平衡发射（Pre-equilibrium Emission）的截面贡献**：在入射动能显著高于库仑势垒（$E_{\text{lab}} > 10\text{ MeV/u}$）时，部分激元在达到统计平衡前快速逃逸，纯 Hauser-Feshbach 会低估前向高能轻核产额；
2. **高角动量下的液滴裂变截断**：当复合核自旋超过转动液滴模型裂变极限 $\ell_{\text{fiss}} \approx 70\hbar$ 时，裂变道宽度急剧压倒粒子蒸发，需耦合动力学裂变摩擦模型；
3. **未测共振间距对绝对能级密度的依赖**：Hauser-Feshbach 出射道分母求和强烈依赖残核能级密度参数 $a$，需结合独立测量的低激发分立能级与中子共振间距 $D_0$ 严格定标。

## Sources

- [[book-bertulani-nuclear-reactions]]：Chapters 4, 5, 6 (印刷 pp. 109–254 / PDF pp. 120–265).
- [[book-lin-heavy-ion-reactions]]：第 6 章 熔合反应与 Hauser-Feshbach 统计模型.
- [[book-lu-nuclear-physics-chinese]]：第 9 章 核反应机制与光学模型.
- [[compound-nucleus-statistical-decay-and-level-density]]：复合核统计衰变与能级密度参数化.
- [[excitation-functions-target-integration-and-cross-sections]]：激发函数与截面反演指南.
