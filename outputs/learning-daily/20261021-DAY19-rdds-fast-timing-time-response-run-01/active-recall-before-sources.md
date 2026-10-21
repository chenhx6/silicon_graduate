# Day19 来源前主动回忆（primed，非盲测）

- frozen_at: 2026-10-21T17:37:09.821350+08:00
- session_id: 01a15dcc-49f9-7623-b0e9-75fd73c74a80
- run_id: 2026-10-21-day-19-01
- 本 session 尚未打开 Day19 source 原件正文（Radeck 2012、Nolan 1979、recoil-distance-doppler 方法页新读范围）、raw 原文或新 analysis 脚本。README/index/运行交接/课程计划及用户准备 prompt 已读，索引已暴露相关摘要。以下内容为受 priming 的主动回忆，不作盲测分数。

## 已暴露的 priming 与已知上下文

用户准备 prompt、Day 18 运行交接、checkpoint 060 及 checkpoint 068 已经明确说明：
1. 四类寿命/时间测量方法（DSAM、RDDS、Fast Timing、TDPAD）的时钟机制与时间窗口差异。
2. Radeck 2012 (98Ru): 真空中反冲核超精细相互作用导致的去取向（deorientation）效应；分量衰减因子 G_US 与 G_SH 的条件平均；90° 探测器效率缺失时的理论几何归一；两步 tau 迭代流程；探测器距离 d/d0 的机械坐标零点界限。
3. Nolan & Sharpey-Schafer 1979 经典综述：DSAM 与 RDDS (RDM) 在 1–20 ps 范围存在重叠；两方法若得出相合寿命，可能共享了相同的反冲初速或阻停本底系统误差（而非真正独立检验）；电子快速定时必须建立精确 prompt response function (PRF)、zero-time 零时间基准与能量门匹配，大样本统计量无法消除 PRF 漂移或卷积系统偏差。
4. 逆运动学 Degrader-RDDS 空间尺度放大（Suzuki 2008 beta=5.1% 相对 Klemme 1999 beta=1.6% 带来 3.19 倍空间拉伸，将 tau=0.72 ps 的位移从 3.45 um 放大到 11.01 um，薄降能层穿行时间 <0.2 ps 将 RDDS 测量下限延伸至 ~0.5 ps）。
5. 现代快速定时方法（Régis 2011 博士论文 LaBr3/MSCD，镜像对称能量门对消 time-walk，零交叉点 Delta C = 2*tau + PRD(Delta E)）与 TDPAD（Grodner 2018 128Cs 手征异构态 g 因子测定与拉莫尔进动；Ionescu-Bujor 1998 129,131Ce 电四极矩进动）。
6. Schwalm 1977 (Nucl. Phys. A 293, 425) 与 Hermans 1977 (Nucl. Phys. A 284, 307) 当前仅有元数据，原 body 尚未获得，不得虚构为已读 primary。

## 四类寿命/时间测量方法的时间窗口与物理响应比较

| 方法 | 典型有效时间窗口 | 物理时钟与标尺 | 主要响应与观测量 | 核心误差来源与限制 |
| --- | --- | --- | --- | --- |
| **DSAM** | ~10 fs – 1–2 ps | 固体阻停介质减速历程 v(t)，时钟由材料阻停时间 ~0.5–2 ps 决定 | 前/后向探测器中连续多普勒展宽谱形或频移因子 F(tau) | 阻停本领系统误差 (10–15%)、未知侧馈时标、反冲角散射卷积 |
| **RDDS** | ~1 ps – 数 ns (逆运动学可至 ~0.5 ps) | 机械真空飞行距离 d 与反冲初速 v0 (t = d / v0) | 飞行频移峰 Is 与减速/阻停峰 Iu 强度比 | 箔片平整度与接触零点 d0、真空退取向衰减 Gk(t)、上游复杂 feeding |
| **Fast Timing** | ~10 ps – 数十 ns (MSCD 可至 ~5–50 ps) | 电子学高精度时钟 (TAC / 数字 CFD) | 相对瞬发响应函数 (PRF) 的指数斜率或质心位移差 (MSCD) | PRF 标定、能量依赖的时间游走 (time walk)、康普顿散射本底 |
| **TDPAD** | ~ns – 数十 us | 恒定外磁场拉莫尔进动周期或晶格电场梯度四极进动周期 | 定向角分布各向异性调制比 R(t) 随时间的振荡衰减 | 顺磁放大/Knight 移位、核自旋弛豫、晶格缺陷与四极杂散场 |

## 方法选择决策树要素

1. **反冲速度与运动学**：常规熔合蒸发 (beta ~ 1–2%) 在 tau < 2 ps 时 RDDS 位移仅数微米，受限于平整度与 d0，DSAM 主导；逆运动学 (beta > 4–5%) 空间尺度拉伸数倍，RDDS 成为 sub-ps 首选。
2. **Feeding 拓扑**：慢侧馈严重扭曲 DSAM 拟合；RDDS 结合符合门与 DDCM 可数学消去直接/间接 feeding；快速定时要求衰变路径明确。
3. **退取向与探测几何**：RDDS 真空飞行超精细场引起 Gk(t) 衰减，需多角阵列或精确模型扣除。

## 本 session 拟推进的新量化设计与交付

1. 原件深读：Radeck 2012、Nolan 1979 与 recoil-distance-doppler 方法页。
2. 决策树与最小校准清单。
3. 本 session 新量化练习：设计退取向敏感性与运动学空间拉伸模拟，给出明确 readiness 边界。
4. 规范日报、唯一知识写回与卡交付自审。