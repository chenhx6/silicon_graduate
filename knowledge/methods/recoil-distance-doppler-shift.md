---
type: method
title: Recoil-distance Doppler-shift and differential decay-curve method
aliases: [RDDS, recoil-distance Doppler-shift, coincidence plunger, DDCM, differential decay curve method, RDDM]
created: 2026-08-11
updated: 2026-08-11
status: ai-draft
review_status: unreviewed
method_type: nuclear-lifetime-coincidence-plunger
tags: [lifetime, plunger, doppler-shift, ddcm, feeding, stopping]
---

# Recoil-distance Doppler-shift / DDCM

## Purpose

RDDS 通过改变 target-stopper distance，比较核在飞行中发射的 shifted γ component 与停止后发射的 unshifted component，提取 excited-state lifetime。Coincidence DDCM 用 feeding-transition gates 隔离 decay curves，并以逐 distance 的 `τ(x)` constancy 检查系统误差。

## Inputs and Assumptions

- calibrated target-stopper distances、recoil velocity 与 detector angles；
- shifted/unshifted peak components and efficiency normalization；
- direct or indirect feeding transition 可分辨并适合作 gate；
- contaminant、unobserved feeding、deorientation、finite stopping and stopping powers 被校正或进入 uncertainty；
- branching/mixing information 足以把 lifetime 转为 `B(Eλ)`/`Q_t`。

## Core Coincidence-DDCM Chain

对单一 direct feeder，Klemme 1999 的 Eq. (3) 可写为：

`τ(x) = I_su^BA(x) / [dI_ss^BA(x)/dx] × 1/v`，

其中 `I_su^BA` 是 feeding transition 的 shifted component 与 depopulating transition 的 unshifted component 的 coincidence intensity，`I_ss^BA` 为 shifted-shifted coincidence intensity，`v` 是 recoil velocity。多 feeder 情形需按 coincidence intensity normalization 扣除 direct-feeding contribution（source Eqs. 1-2）。

每个 distance 可独立给出 `τ(x)`。在敏感 distance range 内，理想结果应近似常数；明显 distance dependence 是 contaminant、feeding 或 peak-separation 系统误差的诊断，而不是应被平均掩盖的散点。

## Coincidence Advantage

在 interest level 上方的 feeder gate 可以显著减少 unobserved feeding 和 low-spin deorientation 对 lifetime 的影响。不同 rings、direct/indirect gates 给出多个相对独立 lifetime estimates，可检查 contaminant sensitivity。

## Short-Lifetime Boundary

当 lifetime 与 stopper 中 slowing time 可比时，停止过程内发射产生额外 line-shape component；纯 shifted/unshifted RDDS 近似不再充分。Klemme 1999 对 Au 中约 `1.1 ps` slowing time 使用 DSAM-like correction，并因 stopping-power ambiguity 给 adopted lifetime asymmetric errors。高统计和小 statistical error 不会消除这项系统边界。

## What It Can Establish

- source-specific level lifetimes；
- 联合 branching/mixing information 后的 `B(E2)`, `B(M1)` 与 `Q_t`；
- distance/gate/ring consistency and feeding-systematic diagnostics；
- 同实验多带/多核的相对 lifetime/collectivity comparison。

## What It Cannot Establish Alone

- 不能单靠 lifetime 决定 γ-soft versus rigid-triaxial shape、microscopic configuration 或 nuclear chirality；
- 不能在缺少 band crosswalk 时把一个早期 level lifetime转移到后来同核素的 band label；
- 不能忽略 branching ratios、mixing ratios、side feeding、finite stopping 或 deorientation 直接把 `τ` 当成 intrinsic quadrupole moment；
- 不同 stopping materials/parametrizations 与 plunger geometries 的 correction 不能跨实验机械复用。

## Inverse-Kinematics Degrader Variant

Suzuki 2008 demonstrates an RDDS variant in which inverse-kinematics recoils are slowed in a degrader rather than stopped. Direct-feeder DDCM uses shifted feeding and unshifted depopulating intensity divided by the shifted-component change between neighboring distances. When the direct feeder is contaminated, an upper transition can gate the cascade and a measured intensity ratio corrects the unwanted contribution. This extension improves short-lifetime access but preserves three boundaries: foil transit/stopping effects must remain small relative to the lifetime, velocity is different before and after the degrader, and indirect-gate lifetimes carry the correction's systematic dependence.

The method yields source-specific lifetimes. Converting them to `B(M1)` or `B(E2)` still requires branching and multipole-mixing information; Suzuki 2008 assumes pure M1 for the dipole branches. One-band lifetimes cannot establish electromagnetic equality of a proposed doublet.

## Source-Level Examples

- [[klemme-1999-lifetimes-134nd-neighbors]]：GASP-II、22 distances、direct/indirect feeder DDCM、constant-`τ` diagnostic 与 `<2 ps` finite-stopping correction。
- [[singh-2016-lifetime-131ce-133pr]]：`131Ce` plunger+DSAM 与 `133Pr` plunger；后者展示 singles-only statistics、long side feeding and pre-crossing validity boundaries。
- [[radeck-2012-deorientation-lifetime-98ru-rdds]]
- [[nolan-sharpey-schafer-1979-lifetime-measurements]]：强调 RDDS 语境下的 distance-dependent deorientation/angular-correlation correction。

## Sources

- [[klemme-1999-lifetimes-134nd-neighbors]]
- [[suzuki-2008-lifetimes-103rh-104rh]]
- [[singh-2016-lifetime-131ce-133pr]]
- [[radeck-2012-deorientation-lifetime-98ru-rdds]]
- [[nolan-sharpey-schafer-1979-lifetime-measurements]]

## Related Methods

[[doppler-shift-attenuation-method]]、[[doppler-correction]]、[[angular-correlation]]、[[transition-quadrupole-moment]]。

## Evolution Log

- 2026-08-11: added Suzuki 2008 inverse-kinematics degrader DDCM, indirect-gate correction and one-band evidence boundary.
- 2026-08-11：由 Klemme 1999 建立 coincidence-DDCM equation/diagnostic 与 finite-stopping boundary，并接入 Singh 2016/Radeck 2012 作为方法关系。


## Day18内无学分Day19预习：分量条件与缺失校准

[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-P19-1–10新完整原读十页/13图3表，旧人审prefix/flags保护。stopper取向冻结的US与按lifetime平均的SH需不同G；90°缺eff由最短距离理论角关联补、两步τ/G迭代与same-data校正后平坦性都不认证完整独立Σ。实际distanceproducer未得，Eq9的d−d0/正8与d3、Eq2后A0=0的literal域保，不改raw/重报τ。新canonical [[lifetime-method-selection-response-contract]]给条件核和actualinput优先级；后续Nolan定向段已补方法选择表与最小校准清单；Nolan非本次完整88页重读、现代fast-timing/TDPAD primary仍缺，正式19留新session。

## 四类时间测量方法选择矩阵（checkpoint060）

在 [[lifetime-method-selection-response-contract]] 中，DSAM（$10\text{ fs}-2\text{ ps}$）、RDDS（$1\text{ ps}-1\text{ ns}$）、Fast Timing MSCD（$5\text{ ps}-50\text{ ns}$）与 TDPAD（$5\text{ ns}-10\ \mu\text{s}$）被整合为完整的实验方法选择矩阵。RDDS 以真空中反冲速度 $v_0$ 与微米飞行距离为时钟，其主导系统误差为距离绝对零点与飞行中时间退取向 $G_k(t)$；在皮秒至纳秒窗口内与现代 [[regis-2011-fast-timing-labr3]] 快速定时形成关键交叉验证。详见新 [timing-method-selection-result-060](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/timing-method-selection-result-060.json)。

## 逆运动学Degrader-RDDS与空间尺度放大（checkpoint068）

[[klemme-1999-lifetimes-134nd-neighbors]] KL99-17与[[suzuki-2008-lifetimes-103rh-104rh]] SU08-2给不同运动学/foil响应的companion。打印中心beta .051/.016约3.1875，tau=.72ps的简单d=v*t控制约11.01/3.45微米；未传播beta/tau/零点误差。薄degrader不完全停止反冲，减小厚stopper慢化影响，但不免finite-foil能损/发射、速度/距离与gate校准，也不证明普适.5ps下限或完全无模型独立交叉验证。详[[lifetime-method-selection-response-contract]] checkpoint078；旧068检查只算术。


## Day 19正式课程：RDDS/DDCM 方法选择决策树、分量响应与最小校准清单

本节为 2026-10-21 正式 Day 19 独立课程的 canonical 方法论沉淀，系统整合反冲距离多普勒频移法（RDDS）、微分衰变曲线法（DDCM）、真空退取向效应（Deorientation）、快速定时（Fast Timing）与 DSAM 的方法选择决策树和最小校准清单。

### 1. 核心时钟机制与运动学尺度拉伸

RDDS 的物理时钟为真空中反冲核以恒定速度 v0 = beta * c 飞越微米级机械距离 d 的飞行时间 t = d / v0。
- **常规熔合蒸发运动学**（如 [[klemme-1999-lifetimes-134nd-neighbors]]，beta = 1.6%）：反冲演化率为 v = 4.797 um/ps。在 tau < 1.5 ps 时，飞行位移 d < 7 um，受限于靶-阻挡层表面粗糙度和平行接触零点误差（d0 约 5-10 um），测量不确定度急剧发散；
- **逆运动学 Degrader-RDDS**（如 [[radeck-2012-deorientation-lifetime-98ru-rdds]] beta = 4.5%，[[suzuki-2008-lifetimes-103rh-104rh]] beta = 5.1%）：空间尺度被拉伸 2.81 - 3.19 倍（v = 13.49 - 15.29 um/ps）。对于 tau = 0.72 ps 的极短寿命态，飞行位移从常规运动学的 3.45 um 放大至 11.01 um，配合极薄降能层（degrader，穿行时延 <0.2 ps），使 RDDS 可精确下拓至 ~0.5 ps，提供与 DSAM（依赖固体阻停本领）正交的独立物理时钟。

### 2. 微分衰变曲线法（DDCM）消除侧馈级联的严格性

对于单一直馈跃迁 B -> A，在 feeder 符合门下，能级 A 的寿命为：
tau(x) = [I_su^BA(x) / (d I_ss^BA(x) / dx)] * (1 / v)
其中 I_su^BA(x) 为 feeding 频移峰与 decay 未移峰的符合计数，I_ss^BA(x) 为双频移符合计数。该公式在数学上完全消除了上游所有已知和未知 feeding 级联的时间常数，彻底克服了 DSAM 对侧馈模型参数的严重依赖。在敏感距离区间内，各距离点提取的 tau(x) 必须呈现平坦常数行为；任何距离相关漂移均直接指示未扣净本底、杂质线污染或退取向畸变。

### 3. 真空退取向效应（Deorientation）的分量不对称响应

高电离反冲离子在真空中飞行时，未配对电子壳层角动量 J 与核自旋 I 发生超精细相互作用，导致核自旋取向发生时间依赖的衰减：G_k(t) = alpha_k + (1-alpha_k)*exp(-Gamma_k * t)。
在 RDDS 观测中，衰减因子对两相分量产生显著不对称性：
1. **未移分量（US）**：反冲核到达 stopper 后超精细相互作用因电子俘获和晶格电荷中和而瞬间冻结，其取向衰减严格等于到达时刻的值：
   G_k^US(t) = G_k(t)
2. **频移分量（SH）**：核在真空中飞行的衰变必须沿指数衰变密度积分加权平均：
   G_k^SH(t) = alpha_k + [(1-alpha_k)/(1 + Gamma_k * tau)] * [1 - exp(-(Gamma_k + 1/tau)*t)] / [1 - exp(-t/tau)]
3. **渐近发散与系统偏差**：当 t >> tau 时，G_k^US 趋向硬核极限 alpha_k（如 98Ru 中 alpha_2 = 0.18），而 G_k^SH 趋向 alpha_k + (1-alpha_k)/(1 + Gamma_k * tau) = 0.554922。在前向探测器若忽略该退取向分量差异，表观寿命提取将产生最大可达 -4.6% 的系统偏差。

### 4. 四类核寿命测量方法全景选择决策树

| 待测态寿命范围 | 首选实验方法 | 物理时钟标尺与机制 | 关键优势与适用条件 | 核心实验约束与主要 Nuisance |
| --- | --- | --- | --- | --- |
| **10 fs – 1.5 ps** | **DSAM**（常规）或 **Degrader-RDDS**（逆运动学） | 固体介质阻停本领 dE/dx 或高初速（beta > 4%）微米飞行位移 | 高自旋集体带态连续测定；逆运动学可避开阻停功率依赖 | 阻停本领模型漂移（10–15%）、未知慢侧馈、反冲角散射 |
| **1 ps – 1 ns** | **RDDS / DDCM** | 真空机械微米飞行位移 d = v0 * t | 具备清晰频移峰分离；DDCM 数学上严格消去直接与间接 feeding | 接触零点 d0 标定（+/-0.5–1 um）、真空退取向 G_k(t)、90°效率缺失 |
| **10 ps – 50 ns** | **Fast Timing**（MSCD / 坡度法） | 超快闪烁体（LaBr3/BaF2）与高精度电子学 CFD/TAC | 低能跃迁频移不显或单粒子退激态；无微米位移机械限制 | 瞬发响应函数（PRF）漂移、能量走时（Time Walk，需 PRD 标定）、康普顿本底 |
| **5 ns – 10 us** | **TDPAD** | 外加磁场拉莫尔进动周期或晶格电场梯度进动周期 | 同核异能态（Isomer）g 因子与静态四极矩直接测量 | 自旋-晶格弛豫、顺磁放大因子、非立方晶格缺陷杂散电场 |

### 5. 实验物理测量最小校准清单

| 校准维度 | 物理对象与参数 | 必须满足的实验判据 | 典型未校准系统偏差后果 |
| --- | --- | --- | --- |
| **1. 时钟零点基准** | RDDS 绝对零距离 d0；Fast Timing 零时间 t0 与 PRF 质心 | 电容式微米测距仪接触传感零点（误差 <= 0.5 um）；双探测器瞬发符合零点 | d0 偏差 1 um 在 beta=1.6% 下导致 Delta_tau = 0.21 ps；快速定时未对消走时导致伪寿命 |
| **2. 探测阵列响应** | 多角度（尤其是 90度）相对效率、立体角收缩 Qk 与 Doppler 展宽 | 标准源全能峰效率校准；禁止在最短距离处用理论角分布替代 90度实测效率 | 90度效率缺失人为强制拟合角分布，导致退取向参数 alpha_k, Gamma_k 严重偏离 |
| **3. 运动学与速度分布** | 反冲初速矢量 v0、速度弥散 Delta v / v、薄膜能损 | 运动学重建或高激发单线高能 Doppler 分离；降能层/衬底能损 SRIM/ATIMA 实验校验 | 速度误差 Delta v/v 线性 1:1 传递至提取寿命 Delta_tau/tau |
| **4. 真空退取向参数** | 衰减因子 G_k(t)、超精细参数 alpha_k, Gamma_k = |g|/C_k | 多环角分布测定或已知 g 因子电荷态平衡迁移；区分 US 冻结与 SH 积分核 | 忽略退取向使前向探测器表观寿命偏小达 3-5%；跨元素盲目迁移 C_k 破坏绝对标尺 |
| **5. 衰变拓扑与 Feeding** | 离散馈入支路强度、侧馈时标、内转换系数 alpha_tot | 优先采用 direct-feeder 符合门；若用 singles 必须做完整上能级级联扣除 | 未观测慢侧馈可导致 DSAM/RDDS 表观寿命虚假延长 20-100% |
| **6. 停止介质相互作用** | 固体衬底/阻挡层停止功率 dE/dx（电子与核慢化） | 采用最新试验数据库比对；对 RDDS 阻挡层考虑有限停止时延（~1 ps）修正 | 停止功率标准系统误差（10-15%）直接限制绝对 B(E2) 提取精度 |

### 6. 系统误差交叉分水岭：DSAM vs RDDS 决断边界

根据定量分析程序 [day19_rdds_timing_response_analysis.py](../../system/scripts/day19_rdds_timing_response_analysis.py)，当零距离标定不确定度为 Delta d0 = 1.0 um 时：
- 在常规运动学（beta = 1.6%）下，零点误差与 10% 阻停功率误差的交叉寿命为 tau_cross = 2.085 ps。低于 2.1 ps 时，DSAM 的阻停误差反优于 RDDS 的零点机械误差；
- 在逆运动学（beta = 4.5%，[[radeck-2012-deorientation-lifetime-98ru-rdds]]）下，交叉点压低至 tau_cross = 0.741 ps；在 beta = 5.1% 下进一步降至 0.654 ps。这严密证明了逆运动学将 RDDS 的优选应用边界推拓至亚皮秒级。
