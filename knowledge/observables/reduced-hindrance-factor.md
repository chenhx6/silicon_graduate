---
type: observable
title: 折合阻碍因子（f_nu）
aliases: [reduced hindrance factor, f_nu, K-isomer hindrance]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: unreviewed
observable_kind: transition-hindrance-metric
symbol: f_\nu
units: dimensionless
tags: [isomers, k-isomer, forbidden-transition, triaxiality, k-mixing]
---

# 折合阻碍因子（Reduced Hindrance Factor, $f_\nu$）

## Definition

用于定量评估**高 $K$ 同核异能态（$K$-Isomers）**跃迁禁戒程度的物理观测量。在轴对称形变核中，总角动量在对称轴上的投影 $K$ 是一个良好量子数。若跃迁初末态之间的角动量投影改变 $\Delta K = |K_i - K_f|$ 大于跃迁多极阶数 $\lambda$，该跃迁按照几何选择定则是严格禁戒的。此时跃迁禁戒度定义为：
$$\nu = \Delta K - \lambda$$
折合阻碍因子 $f_\nu$ 表征平均每个禁戒度 $\nu$ 对跃迁半衰期造成的压低倍数。

## Formula and Conventions

首先定义实验测量的单支跃迁分半衰期 $T_{1/2}^\gamma$ 与 Weisskopf 单粒子半衰期估计 $T_{1/2}^W$ 之比为总阻碍因子（Hindrance Factor, $F_W$）：
$$F_W = \frac{T_{1/2}^\gamma}{T_{1/2}^W} = \frac{1}{\text{Branching Ratio}} \cdot \frac{T_{1/2}^{\text{total}}}{T_{1/2}^W}$$

对于 $\nu$-重禁戒跃迁，折合阻碍因子按禁戒阶数归一化为：
$$f_\nu = (F_W)^{1/\nu} = \left( \frac{T_{1/2}^\gamma}{T_{1/2}^W} \right)^{1/(\Delta K - \lambda)}$$

## Physical Interpretation and Benchmarks

- **经验基准规律（Empirical Rule）**：在重变形稀土区和锕系核（如 $^{178}\text{Hf}$），严格轴对称且具有较硬势能面的核中，$f_\nu$ 通常稳定在 **$100 \sim 300$**（即每增加一重禁戒，跃迁几率下降 2 到 3 个数量级）；
- **三轴形变诱导 $K$-混合（$K$-Mixing via Triaxiality）**：
  - 当原子核具有显著的非轴对称三轴形变（$\gamma \ne 0$）或 $\gamma$-软性时，内禀轴失去轴对称旋转不变性，$K$ 量子数强烈破缺；
  - 波函数发生多重 $K$ 分量杂化：$| \Psi_M^I \rangle = \sum_K c_K | I K M \rangle$；
  - 这导致原本严重禁戒的跃迁阻碍因子急剧崩塌，**$f_\nu$ 骤降至 $5 \sim 30$**；
  - 测量 $f_\nu$ 的异常变小是诊断原子核微观三轴形变程度的独立实验指纹。

## Boundary and Limitations

- **科里奥利力混合干扰**：高自旋下强烈的 Coriolis 相互作用会诱发动力学高阶 Coriolis mixing，即使轴对称核也可能出现 $f_\nu$ 的反常下降，分析时必须扣除 Coriolis 顺磁去耦效应；
- **多极混合比影响**：若跃迁包含混合多极性（如 $M1+E2$），计算 $F_W$ 时必须根据实测混合比 $\delta$ 分别分解 $M1$ 与 $E2$ 的分阻碍因子，不可直接使用全跃迁强度。
