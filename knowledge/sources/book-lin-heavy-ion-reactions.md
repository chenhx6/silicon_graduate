---
type: source
title: "林承键 2017 - 重离子核反应"
aliases: [林承键重离子核反应, Lin 2017 Heavy Ion Reactions, 重离子核反应专著]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "重离子核反应"
authors: [林承键]
publisher: "科学出版社"
year: 2017
pages: "223"
isbn: "9787030537232"
canonical_source: "林承键, 《重离子核反应》, 科学出版社 (2017)"
library_file: "raw/books/重离子核反应 (林承键) (Z-Library).pdf"
raw_file: "raw/books/重离子核反应 (林承键) (Z-Library).pdf"
raw_sha256: "792bfe7f7807623b7e1439b32eddb7320ab3ec6bf6be7e3894b436c1c9f65b2e"
nuclei: []
reactions: [heavy-ion-fusion, elastic-scattering, deep-inelastic, transfer-reactions, fusion-evaporation]
experiments: []
models: [optical-model, proximity-potential, bass-model, compound-nucleus-decay]
topics: [heavy-ion-reactions, fusion-cross-section, critical-angular-momentum, reaction-kinematics]
---

# 林承键 2017 - 重离子核反应

## 专著概况与定位

本书由中国原子能科学研究院（CIAE）重离子核物理专家林承键研究员所著，是国内第一部全面系统论述重离子核反应动力学、机制与唯象理论模型的权威著作。对于低能核结构实验而言，重离子熔合蒸发反应是布居高自旋态的最核心途径。本书为设计束流能量、估算入射临界角动量 $\ell_{\text{crit}}$、选择靶-弹体系组合以及计算反应截面提供了直接物理与工程判据。

## 核心章节精要与物理内容

### 第 2 章：重离子相互作用势（pp. 28–46）
- **总相互作用势构成**：$V(r) = V_C(r) + V_N(r) + \frac{\hbar^2 l(l+1)}{2\mu r^2}$
  - 库仑势 $V_C(r)$（均匀带电球体外为 $Z_1 Z_2 e^2 / r$）；
  - 核相互作用势 $V_N(r)$：唯象 Woods-Saxon 势、双折积势（Double-folding potential）以及著名的接近势（Proximity potential）；
  - 离心势能项（Centrifugal barrier），导致有效势垒高度与位置随角动量 $l$ 显著变化。
- **库仑势垒（Bass 势垒与相互作用距离）**：定义标称库仑势垒高度 $V_B$ 与接触半径 $R_B \approx 1.07 (A_1^{1/3} + A_2^{1/3}) + 2.72\text{ fm}$。

### 第 6 章：熔合反应动力学与蒸发道（pp. 147–188）
- **完全熔合的经典截面与极限**：
  - 经典临界角动量截面公式：$\sigma_{\text{fus}} = \frac{\pi}{k^2} \sum_{l=0}^{\ell_{\text{crit}}} (2l+1) T_l = \frac{\pi R_B^2}{E_{\text{cm}}} [E_{\text{cm}} - V_B]$；
  - 入射能量较高时，熔合截面受到临界角动量 $\ell_{\text{crit}}$ 或复合核裂变势垒消失的强烈限制，截面转为与 $1/E_{\text{cm}}$ 成线性反比下降。
- **熔合蒸发道竞争（Fusion-Evaporation vs Fission）**：
  - 激发复合核的退激途径：中子发射（$xn$ 蒸发）、带电粒子发射（$yp, z\alpha$）与竞争裂变；
  - 旋转复合核的高角动量输入使得中子蒸发残核继承了高达 $30\hbar\sim 50\hbar$ 的角动量，从而在熔合蒸发后沿 yrast 线的 $\gamma$ 级联辐射中展现高自旋三轴转动、手征和摆动带。

## 对本 Wiki 研究的核心指导价值

1. **实验 Proposal 设计核算**：用于在提出实验申请（如北京 HI-13 串列、兰州 HIRFL 或南非 iThemba 束流申请）时，严格计算弹靶组合的质心能量 $E_{\text{cm}}$、库仑势垒穿透率以及最佳 $xn$ 蒸发窗口。
2. **反应运动学校正**：提供反冲核初始速度分布 $v/c = \beta$ 与角分布分散的理论输入，用于多普勒频移校正（Doppler shift correction）与薄靶/厚靶反冲停阻（DSAM）分析。
