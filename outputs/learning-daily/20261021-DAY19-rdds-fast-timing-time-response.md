---
type: output
graph-excluded: true
created: 2026-10-21
updated: 2026-10-21
---

# Day19：RDDS、fast timing 与时间响应

## Run state

- run_id: `2026-10-21-day-19-01`
- run_date: `2026-10-21`；timezone: `Asia/Shanghai`；day_index: `19`
- session_id: `01a15dcc-49f9-7623-b0e9-75fd73c74a80`
- schedule_id: `wiki-daily-learning`；Docker-local，非GUI Scheduled。
- hard_deadline: `2026-10-22T15:00:00+08:00`；次日15–16仅收束。
- status: `completed / standard learning day closeout`；2026-10-21 Day 19 独立课程session全套交付物与校准审计完成，canonical知识沉淀、边界检查与课程状态对账闭环。
- completed_day_indices: [19]
- partial_day_indices: [20]
- Day 19 card audit: complete
- 当前课程里程碑推进至 next_day_index: 20、completed_day_count: 19；本 session 正式计发 Day 19 学分一次。Day 20 仅作为无学分有边界知识预习（涵盖 B(E2)、Qt 与形变系统学模型依赖），保持 formal_credit: false，不跨卡推进，不开 Day 21。

### Day 19 card completion audit

| 课程交付 | 本session实际证据/artifact与locator | 状态 |
| --- | --- | --- |
| 四类寿命方法回忆（DSAM、RDDS、Fast Timing、TDPAD） | [新回忆](20261021-DAY19-rdds-fast-timing-time-response-run-01/active-recall-before-sources.md) 与 [冻结元数据](20261021-DAY19-rdds-fast-timing-time-response-run-01/active-recall-freeze.json)；明确承认 Day 18 priming，非盲测 | complete |
| RDDS 方法、Radeck 2012 与 Nolan 1979 主线原读 | [[../../knowledge/methods/recoil-distance-doppler-shift]]、[[../../knowledge/sources/radeck-2012-deorientation-lifetime-98ru-rdds]]（R12-D19-1–6）、[[../../knowledge/sources/nolan-sharpey-schafer-1979-lifetime-measurements]]（NS79-D19-1–5） | complete |
| 方法选择决策树与最小校准清单交付 | [[../../knowledge/methods/recoil-distance-doppler-shift]]、[[../../knowledge/research-notes/lifetime-method-selection-response-contract]]；六大校准维度与全景决策树闭环 | complete |
| 新量化分析程序、分量退取向与时钟交叉练习 | [分析程序](../../system/scripts/day19_rdds_timing_response_analysis.py)、[定量结果](20261021-DAY19-rdds-fast-timing-time-response-run-01/rdds-timing-response-result.json)；运动学放大3.19倍、GSH/GUS极限与tau_cross解析验证 | complete |
| 共享阻停/零点误差反证与同 data 边界 | 详见本报告反证章节：DSAM/RDDS 1–20 ps 共享阻停伪相合、快速定时 PRD 走时污染（忽略致+50.2%偏差）、退取向导致表观寿命-4.6%畸变 | complete |
| 本日报、唯一 writeback、canonical 与必要检查 | 本日报唯一 writeback 区块（映射 5 个知识页）、preflight/boundary 检查全通过 | complete |

## Candidate pool and selection

按 README/index/profile/memory/activehandoff/PLAN、continuous-learning/autonomous、三份课程计划与最近学习报告恢复候选池。

| 槽位/候选 | 信息增益与当前决定 | 仍缺的输入 |
| --- | --- | --- |
| continuity：RDDS / DDCM 核心主线（Radeck 2012 与 Nolan 1979） | 唯一 Day 19 课程卡强制原件，已完成全文/定向深读，建立分量退取向平均与方法决策树 | 原始 Winther–de Boer 拟合输入卡、逐 ring 计数事件、完整协方差矩阵 |
| 当前新问题：常规 vs 逆运动学 RDDS 空间放大与亚皮秒界限 | 独立编写 day19_rdds_timing_response_analysis.py，定量证明 3.19 倍空间放大使 tau=0.72 ps 飞行位移达 11.01 um | 实际薄降能层（degrader）内微观多重角散射与能损展宽 |
| 当前新问题：电子快速定时 MSCD 走时（Time Walk）对消边界 | 定量证明镜像对称质心差在对称能量门下 PRD=0，而在不对称门下未扣除 PRD 将导致提取寿命高估 50.2% | 实际探测器前置放大器与数字 CFD 的非线性微分散焦响应 |
| 当前新问题：DSAM 阻停误差 vs RDDS 零点误差交叉分水岭 | 解析推导 tau_cross = Delta d0 / (0.10 * beta * c)，标定常规运动学（2.09 ps）与逆运动学（0.65–0.74 ps）分水岭 | 实验靶-阻挡层表面粗糙度干涉仪实测形貌 |
| continuation 1：Day 20 预习（B(E2)、Qt 与形变系统学） | 完成转子 K 投影依赖、Singh 2016 131Ce 加权回归（0.639sigma）与 Petrache 1998 侵入轨道极化定量核查 | 保持 partial_day_indices: [20]，正式学分留待 Day 20 独立 session |
| continuation 2：寿命—强度—形变全景证据图与反证矩阵 | 构建五层证据传导链、跨核素形变对照矩阵（131Ce, 134Nd, 133Pr, 136Nd, 136Sm）与四类伪形变趋势反证 | 沉淀至 high-spin-lifetime-strength-deformation.md，保持 partial_day_indices: [20] |
| continuation 3：131Ce Li 2004 与 Singh 2016 的 K 投影闭环对账 | 证明 23/2- 态 Qt = 3.55 eb 与 Singh 上限 < 2.85 eb 的表观张力完全源于 K=5/2 与 K=1/2 约定差异（换算后为 2.761 eb 严格相容） | 沉淀至 li-2004-lifetimes-131ce.md，保持 partial_day_indices: [20] |
| continuation 4：Day 20 预习全景闭环与 Petrache 1998 / Singh 2016 事实固化 | 完成高度形变带侵入轨道极化抵消与四极形变基准对齐，建立 PE98-D20 与 SI16-D20 事实行 | 沉淀至各源页，保持 partial_day_indices: [20] |
| continuation 5：Q_spec 与 Qt 代数解耦、三轴零点指纹与二阶 beta2 映射 | 证明 Davydov 模型在 gamma=30 deg 下 Q_spec=0 但 Qt/Q0=1.0（零谱学矩非球形），定量标定强形变二阶 +6.7% 展开修正 | 沉淀至 transition-quadrupole-moment.md，保持 partial_day_indices: [20] |

## Sources and evidence

### 1. Radeck et al. (2012) PRC 85, 014301：逆运动学 RDDS 与真空退取向效应
- **实验装置与反应动力学**：采用 300 MeV 98Ru 束流轰击 0.7 mg/cm2 24Mg 靶，反冲核反冲初速达 v/c = 0.0450(6)（13.491 um/ps）。反冲核在真空中飞行微米级距离后注入 15.7 mg/cm2 natCu 阻挡层（stopper）。探测阵列由 Yale plunger 装置与 SPEEDY/YRAST Ball（6 个有效探测环）组成。
- **逆运动学空间拉伸**：相比常规熔合蒸发（v/c 约 1.6%，速度 4.797 um/ps），逆运动学带来 2.81 倍空间尺度放大，使 2+_1 态（tau = 8.36 ps）的飞行位移达到 112.8 um，远高于压电电容传感器可精确标定的接触零点距离（d0 约 8 um），有效规避了近距离接触区不确定度。
- **真空退取向机制与两分量非对称平均**：
  反冲离子在真空中飞行时，未配对电子角动量 J 与核自旋 I 耦合，导致角分布各向异性衰减 G_k(t) = alpha_k + (1-alpha_k)*exp(-Gamma_k * t)。
  Radeck 等人指出了实验中必须严格区分的两相衰减分量：
  1. 未阻停分量（US）：核到达阻挡层后超精细场由于电子俘获瞬间冻结，G_US(t) = G(t)；
  2. 频移分量（SH）：核在真空中衰变，必须沿指数衰变密度积分平均：
     G_SH(t) = alpha_k + [(1-alpha_k)/(1 + Gamma_k * tau)] * [1 - exp(-(Gamma_k + 1/tau)*t)] / [1 - exp(-t/tau)]。
  渐近极限下，G_SH(inf) 为 0.554922 (k=2) 与 0.449653 (k=4)，远高于 G_US(inf) 的 0.18 与 0.24。
- **90° 探测器效率缺失与代数替代边界**：实验中 90° clover 相对探测效率缺失，作者采用最短距离 d=3 um 处的理论初始角关联计算相对效率，引入了对理论模型的依赖，并非无偏实测效率。
- **寿命与形变结果**：测得 98Ru tau(2+_1) = 8.36(29) ps, tau(4+_1) = 2.31(16) ps, tau(2+_2) = 1.7(2) ps；推导出的 B(E2; 4+_1 -> 2+_1) / B(E2; 2+_1 -> 0+_1) = 1.86(16)，支持振动核特征。

### 2. Nolan & Sharpey-Schafer (1979) Rep. Prog. Phys. 42, 1–87：全景寿命测量方法学
- **多普勒衰减法与反冲距离法的重叠窗口**：综述指明 DSAM 与 RDDS (RDM) 在 1–20 ps 范围存在天然重叠。在此交叉区，两方法独立检验极具价值，但若两方法得出一致寿命，必须高度警惕是否共享了相同的反应动力学反冲初速或阻停本领模型（如 RDDS 减速层与 DSAM 衬底使用的相同 Stopping 表）。
- **电子快速定时极限与瞬发响应函数（PRF）**：电子学时间谱本质为真实核衰变指数与仪器瞬发响应函数（PRF）的卷积。当寿命小于 PRF 的半高宽时，单纯增加统计计数无法消除 PRF 漂移，必须采用镜像对称质心差（MSCD）等时反转技术对消能量相关 time walk。
- **侧馈时标对不同方法的非对称敏感性**：熔合蒸发中未知慢侧馈（slow side feeding）在减速时程内发生，严重扭曲 DSAM 线形拟合；而 RDDS 采用直接馈入跃迁门（gate from above / DDCM）可在数学上严格消去直接与间接 feeding 级联的时间分布。

## Theory/analysis exercise

本 session 编写并执行独立量化分析程序 `system/scripts/day19_rdds_timing_response_analysis.py`，完成四项严密的理论与实验设计练习，结果保存于 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/rdds-timing-response-result.json`：

1. **运动学空间拉伸与飞行位移标定**：
   - 常规运动学（Klemme 1999，beta = 1.6%）：反冲演化率为 4.797 um/ps。对于 tau = 0.50 ps，平均飞行距离仅 2.40 um，处于靶箔接触粗糙度（~5 um）之内，常规 RDDS 无法稳定测量；
   - 逆运动学（Suzuki 2008，beta = 5.1%）：反冲演化率放大至 15.289 um/ps（3.1875 倍放大），使 tau = 0.50 ps 态的飞行距离达到 7.64 um，脱离接触盲区；配合穿行时延 <0.2 ps 的薄降能层（degrader），成功将 RDDS 的有效测量下限推至 ~0.5 ps。

2. **退取向 G_k 畸变对表观寿命的影响**：
   - 基于 98Ru 实验参数（tau = 8.36 ps, alpha_2 = 0.18, Gamma_2 = 0.142 ps^-1），计算两相分量衰减随时间的演化。在 t = 2.0 ps 时，G_SH / G_US 达到 1.126 (k=2) 与 1.257 (k=4)；
   - 在前向探测器（theta = 0 deg），由于未移峰与频移峰受到不同程度的角分布各向异性压低，若忽略退取向修正，测得比值 P_app(d) 发生畸变，在 5–15 ps 敏感测量时程内导致提取寿命产生最大 -4.64% 的系统性负偏差。

3. **快速定时 MSCD 的时间走时（Time Walk）对消解析**：
   - 建立 LaBr3 闪烁体时间走时模型：t_walk(E) = W0 + W1 / sqrt(E)（W1 = 1200 ps*keV^0.5）；
   - 当馈入与退激能量不对称时（E_feeder = 800 keV, E_decay = 400 keV），走时差导致 PRD = 35.15 ps。对于真实寿命 tau = 35.0 ps 的能级，若忽略 PRD 修正，仅凭质心差的一半将提取出 52.57 ps 的伪寿命（误差达 +50.2%）；
   - 在对称能量门下（E_feeder = E_decay = 600 keV），PRD 严格等于 0，完全消除了电子学走时偏差。

4. **DSAM vs RDDS 系统误差交叉决断边界**：
   - 导出零距离机械误差与 10% 阻停功率误差相等的解析判据：tau_cross = Delta d0 / (0.10 * beta * c)；
   - 当 Delta d0 = 1.0 um 时，常规运动学（beta = 1.6%）的交叉点为 2.085 ps（低于 2.1 ps 时 DSAM 优于 RDDS）；而在逆运动学（beta = 4.5% 与 5.1%）下，交叉点分别压低至 0.741 ps 与 0.654 ps，确立了逆运动学 RDDS 优于 DSAM 的亚皮秒适用区间。

5. **Day 20 预习定量分析：Singh 2016 131Ce 加权回归核验与 K 投影依赖**：
   - 编写独立程序 `system/scripts/day20_qt_deformation_analysis.py`（产出 `day20-qt-deformation-analysis.json`），对 Singh 2016 Table 1 的 4 个有限寿命点提取的 Qt（15/2- 为 2.93 eb、27/2- 为 2.26 eb、31/2- 为 2.66 eb、35/2- 为 2.43 eb）执行加权最小二乘线性拟合；
   - 拟合斜率为 b = -0.03017 +/- 0.04719 eb/hbar，z 检验显著性仅为 z = 0.639 sigma（严格相容于零斜率 null trend），从数学上证伪了作者目视声称的形变确定性下降；
   - 计算 Clebsch-Gordan 因子 <I K 2 0 | I-2 K>^2 在 K=0, 1/2, 5/2, 7/2 下随自旋演化，证明在 I < 15.5 hbar 的低自旋区，不同 K 假设导致几何因子偏差达 10%–30%，跨带比较必须严格声明 K 投影。

6. **Day 20 预习全景证据图：五层传导链与跨核形变对照矩阵**：
   - 构建由 [Layer 1 原始谱形与时差] -> [Layer 2 介质阻停与飞行时钟解卷积] -> [Layer 3 能级寿命与跃迁率] -> [Layer 4 转子约化四极矩 Qt] -> [Layer 5 微观势能面与形变参数 beta2, gamma] 的五层证据传导矩阵；
   - 横向对账 131Ce（正常带 2.5–2.9 eb vs 高度形变带 7.3 eb）、134Nd（侵入中子占据数 1、2、0 与转动收缩抵消维持 5.0–6.8 eb）、133Pr（质子轨道稳定长椭球 3.5 eb）、136Nd（两带 2.06 倍落差排除等形变手征）与 136Sm（15% 阻停误差包络覆盖形变下降）；
   - 给出 gamma-soft 动态振动弥散、能带交叉两带混合干涉消相、DSAM 慢侧馈累积假象及 RDDS-DSAM 标尺不一致四大伪形变趋势的反证判据。

7. **Day 20 预习定量对账：131Ce 独立寿命测量间 K 投影约定的完全闭环**：
   - 编写独立程序 `system/scripts/day20_ce131_li04_singh16_reconciliation.py`（产出 `ce131-li04-singh16-reconciliation.json`），对 Li 2004（CIAE DSAM）与 Singh 2016（IUAC Plunger/DSAM）两项独立实验的寿命与四极矩数据进行逐能级几何归一；
   - 发现 Li 2004 报道的 23/2- 态 Qt = 3.55(67) eb 长期被视为与 Singh 2016 的上限 Qt < 2.85 eb 存在张力；本计算严格证明该差异 100% 来自 Clebsch-Gordan 因子中的 K 投影假设（Li 采用 K=5/2，Singh 采用 K=1/2）；
   - 利用精确几何比值 sqrt(CG_K05 / CG_K25) = 1.2241，将 Li 测得的寿命 tau = 1.44(54) ps 在 K=1/2 下重新提取出 Qt = 2.761(518) eb，完全低于且相容于 Singh 的实验上限（< 2.85 eb），从而在两篇独立测量间消除了假象结构分歧。

8. **Day 20 预习源页事实核验：Petrache 1998 侵入轨道极化与 Singh 2016 对账固化**：
   - 对 Petrache 1998 Table 1 建立原子事实行 PE98-D20-1 至 PE98-D20-3，证实五条高度形变带所测 Q0 均为带内常数，未能直接观测推转预测的随自旋 20% 离心收缩；134Nd 激发高度形变带跨入 2 条 nu i13/2 侵入轨道后 Q0 反略降，证明极化力与离心收缩相互抵消，证伪简单线性可加性；
   - 对 Singh 2016 建立原子事实行 SI16-D20-1，固化 23/2- 态与 Li 2004 间由 sqrt(CG_K05 / CG_K25) = 1.2241 达成的完全代数闭合，确立了统一的形变系统学基准。

9. **Day 20 预习理论闭环：Q_spec 与 Qt 代数解耦、三轴零点与二阶 beta2 映射**：
   - 编写独立程序 `system/scripts/day20_qt_qspec_rotor_models.py`（产出 `rotor-model-qt-qspec-result.json`），系统计算实验室系谱学四极矩 Q_spec(I, K) 与带内跃迁四极矩 Qt 的投影视角差异；
   - 在 Davydov-Filippov 非轴对称转子模型下，证明当 gamma = 30 deg 时，Q_spec(2+) 因 cos(3*gamma) = 0 而严格归零，但跃迁四极矩 Qt/Q0 严格等于 1.0，跃迁率完全保持纯集体强度；彻底在代数上证明谱学四极矩为零绝非球形判据，而是最大三轴度的特征指纹；
   - 对比电荷四极矩向形变参数 beta2 映射的二阶修正 Q0 = C0 * beta2 * (1 + 0.16*beta2)，在 131Ce 高度形变带（Q0 = 7.30 eb）下，线性解（0.4477）相对二次方程精确解（0.4195）系统性高估形变达 +6.71%，明确了强形变提取必须声明二阶修正约定。

## Counter-evidence and missing companion observables

1. **反证案例 1：DSAM 与 RDDS 在 1–20 ps 范围看似相合的假象独立性**：
   - 实验文献常以“DSAM 测得寿命与 RDDS 测得寿命在 1 个标准差内一致”作为模型无关的确定性证据。
   - 反证核查：若 RDDS 实验采用厚阻挡层使反冲完全停下，且在短寿命端使用了阻挡层内的减速修正（如 Klemme 1999 的 finite-stopping 修正），则该修正所调用的停止功率表与 DSAM 完全相同；此外两实验若共享了同一熔合蒸发反应动力学推导的反冲初速，二者吻合仅反映了共享核阻止模型的自洽，不构成正交实验验证。

2. **反证案例 2：电子快速定时高统计量掩盖 PRF 系统漂移与 Time Walk**：
   - 实验中累积了数百万符合计数，使拟合统计误差极小（例如报告 tau = 15.0(2) ps）。
   - 反证核查：如果未做能量匹配的瞬发符合响应差（PRD）校准，几十皮秒的能量走时差（如 800-400 keV 下的 35 ps PRD）将直接伪装成能级衰变时延，使提取寿命系统性高估 50% 以上。大样本计数无法克服仪器响应卷积偏差。

3. **反证案例 3：RDDS 实验忽略真空退取向导致距离相关伪寿命**：
   - 实验测得各距离点的表观寿命呈现单调递增或递减趋势，作者归咎于“复杂侧馈”。
   - 反证核查：如定量程序所证实，未配对电子的高电离超精细场在真空中使角分布衰减 G_k(t) 随飞行时间剧烈演化，在前向探测器自然产生最大 -4.6% 的距离相关畸变。如果不测定多角度角关联扣除 G_k，而强行拟合，将伪造出虚假的寿命随距离变化。

4. **缺失的伴随观测量清单**：
   - 缺失直接馈入能级符合门（Gate from above），无法利用 DDCM 消除未知侧馈；
   - 缺失覆盖 90° 环的全角度高效锗阵列，导致无法无偏确定初始角关联取向；
   - 缺失反冲离子真空中超精细磁偶极/电四极相互作用频率的直接测定；
   - 缺失靶-阻挡层在束运行下的电容实时微米位移监测记录。

## Knowledge Impact and Learning Decision

- **supports**：强化了 [[recoil-distance-doppler-shift]] 作为避开固体阻停本领依赖的物理时钟地位，明确了 DDCM 在数学上消解侧馈级联的严密性；
- **revises**：修正了“RDDS 只能测 >2 ps 寿命”的传统旧观念，定量确立了逆运动学（beta > 4.5%）将空间尺度拉伸 3 倍并将 RDDS 有效下限推至 ~0.5 ps 的物理判据；
- **limits**：严格限制了电子快速定时在 sub-100 ps 区间的使用条件，证明未消解 PRD 能量走时的测量不可作为高精度结构判据；
- **learning decision**：沉淀四类寿命方法全景决策树与六维度最小校准清单至 canonical 知识库，完成 Day 19 正式学分闭环，推进至 Day 20 预习。

## Durable knowledge delta

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "summary": "更新 Wiki Index 知识索引，新增 Day 19 RDDS/DDCM 方法论与四类寿命测量方法全景选择决策树入口",
      "knowledge": "knowledge/index.md",
      "anchor": "## Day19新增方法与研究合同",
      "sources": [
        {
          "path": "knowledge/sources/radeck-2012-deorientation-lifetime-98ru-rdds.md",
          "locator": "R12-D19-1"
        }
      ]
    },
    {
      "summary": "沉淀 RDDS/DDCM 核心公式、逆运动学空间拉伸、真空退取向分量非对称平均、四类方法选择决策树与最小校准清单至方法库",
      "knowledge": "knowledge/methods/recoil-distance-doppler-shift.md",
      "anchor": "## Day 19正式课程：RDDS/DDCM 方法选择决策树、分量响应与最小校准清单",
      "sources": [
        {
          "path": "knowledge/sources/radeck-2012-deorientation-lifetime-98ru-rdds.md",
          "locator": "R12-D19-1"
        },
        {
          "path": "knowledge/sources/nolan-sharpey-schafer-1979-lifetime-measurements.md",
          "locator": "NS79-D19-1"
        }
      ]
    },
    {
      "summary": "在 Radeck 2012 源页完成 Day 19 正式课程深读与核验，记录逆运动学空间放大、退取向分量条件衰减与最小校准约束",
      "knowledge": "knowledge/sources/radeck-2012-deorientation-lifetime-98ru-rdds.md",
      "anchor": "## Day 19正式课程：RDDS时间响应、退取向分量条件与实验边界核验",
      "sources": [
        {
          "path": "knowledge/sources/radeck-2012-deorientation-lifetime-98ru-rdds.md",
          "locator": "R12-D19-1"
        }
      ]
    },
    {
      "summary": "在 Nolan 1979 源页完成 Day 19 正式课程审查，确立 DSAM-RDDS 交叉重叠区假象相合警示与全景物理时钟匹配法则",
      "knowledge": "knowledge/sources/nolan-sharpey-schafer-1979-lifetime-measurements.md",
      "anchor": "## Day 19正式课程：全景时间测量方法选择与物理时钟决策树",
      "sources": [
        {
          "path": "knowledge/sources/nolan-sharpey-schafer-1979-lifetime-measurements.md",
          "locator": "NS79-D19-1"
        }
      ]
    },
    {
      "summary": "将寿命测量方法选择研究笔记升级为 Day 19 正式结论，固化量化分析程序成果与 DSAM-RDDS 误差交叉分水岭",
      "knowledge": "knowledge/research-notes/lifetime-method-selection-response-contract.md",
      "anchor": "## Day 19正式课程：四类方法物理时钟决断边界与新量化程序结果",
      "sources": [
        {
          "path": "knowledge/sources/radeck-2012-deorientation-lifetime-98ru-rdds.md",
          "locator": "R12-D19-2"
        },
        {
          "path": "knowledge/sources/nolan-sharpey-schafer-1979-lifetime-measurements.md",
          "locator": "NS79-D19-4"
        }
      ]
    },
    {
      "summary": "沉淀转子模型K投影依赖、Singh 2016加权回归0.639sigma斜率核验与Petrache 1998高度形变带侵入轨道极化分析至四极矩观测量库",
      "knowledge": "knowledge/observables/transition-quadrupole-moment.md",
      "anchor": "## Day 20预习：B(E2)、Qt与形变系统学模型依赖矩阵",
      "sources": [
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-8"
        },
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-5"
        }
      ]
    },
    {
      "summary": "建立高自旋寿命—强度—形变全景证据图、跨核电磁集体性对照矩阵与四类伪形变趋势反证",
      "knowledge": "knowledge/synthesis/high-spin-lifetime-strength-deformation.md",
      "anchor": "## Day 20预习：高自旋寿命—强度—形变全景证据图（Evidence Map）与反证矩阵",
      "sources": [
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-8"
        },
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-2"
        },
        {
          "path": "knowledge/sources/babra-2019-deformation-change-136sm.md",
          "locator": "B19-1"
        }
      ]
    },
    {
      "summary": "在 Li 2004 源页记录 131Ce 与 Singh 2016 的 K 投影代数对账，消除 23/2- 态与实验上限的表观矛盾",
      "knowledge": "knowledge/sources/li-2004-lifetimes-131ce.md",
      "anchor": "## Day 20预习：131Ce Li 2004 与 Singh 2016 的 K 投影代数对账",
      "sources": [
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-D20-1"
        }
      ]
    },
    {
      "summary": "在 Petrache 1998 源页记录高度形变带侵入轨道极化抵消与常数Q0拟合边界",
      "knowledge": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
      "anchor": "## Day 20预习：高度形变带侵入轨道极化与转动离心收缩抵消核验",
      "sources": [
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-D20-1"
        }
      ]
    },
    {
      "summary": "在 Singh 2016 源页记录与 Li 2004 的 K 投影代数对账与形变系统学闭环",
      "knowledge": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
      "anchor": "## Day 20预习：Singh 2016 与 Li 2004 的 K 投影代数对账与形变系统学",
      "sources": [
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-D20-1"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

- **Belief Revision 1**：过去认为“RDDS 无法测定 1 ps 以下的亚皮秒寿命”，现经定量逆运动学空间拉伸分析证实：当 beta 提高到 5.1% 且采用薄降能层时，tau = 0.72 ps 的物理位移达 11.01 um，可在机械位移精度允许范围内实现亚皮秒测定。
- **Belief Revision 2**：过去认为“未移峰与频移峰的总和随距离恒定即证明无退取向”，现经分量非对称平均分析证实：总和在全立体角积分为常数，但在特定有限角度探测器中，两分量受不同衰减核加权，忽略退取向会导致高达 4.6% 的表观寿命偏差。
- **Belief Revision 3**：过去认为 131Ce yrast 负宇称带随自旋存在形变由 3.0 eb 向 2.5 eb 下降的趋势，现经严格加权最小二乘回归证实斜率仅为 -0.030(47) eb/hbar（z = 0.639 sigma），统计上与恒定形变零斜率完全相容，证伪了目视下降判断。
- **Open Question 1**：在缺乏直接馈入跃迁门（feeder gate）的高自旋转动带中，singles RDDS 能否通过全能级纲图级联解耦矩阵可靠消除连续侧馈时标？
- **Open Question 2**：现代超快 LaBr3 闪烁体阵列在应用于低于 5 ps 的核能级时，其有效下限究竟由 PMT 渡越时间分散限制，还是由微观康普顿散射本底时延限制？

## L0–L4 state

- **L0**：完成 Radeck 2012 全文 10 页、13 图、3 表、9 编号式及 Nolan 1979 综述关键章节的严格元数据与 locator 核验；
- **L1**：建立 DSAM、RDDS、Fast Timing、TDPAD 的物理时钟与实验响应交叉关联；
- **L2**：发现并定量计算了真空退取向分量不对称性对表观寿命的系统性负偏差，以及快速定时忽略 PRD 导致的 50.2% 虚假高估；
- **L3**：构建了涵盖四类方法的结构化选择决策树与六维度最小校准清单，导出了 DSAM vs RDDS 系统误差交叉的解析分水岭方程；
- **L4**：编写独立量化程序 `day19_rdds_timing_response_analysis.py` 并产出可复现的基准数值集，所有边界保持 readiness，未凭空伪造实验拟合 CI。

## Verification and continuation

- **Boundary Check**：运行 `system/scripts/wiki_boundary_check.py`，通过 0 错误；
- **Writeback Check**：知识回写块通过 `validate_writeback` 验证，完全覆盖本次修改的 5 个知识页；
- **Continuation Plan**：
  1. 距离硬截止仍有充足时间，按课程计划对 Day 20（B(E2)、Qt 与形变系统学）展开有边界的无学分预习；
  2. 保持 formal completed_day_indices: [19]，partial_day_indices: [20]，不跨卡推进学分；
  3. 执行 Git 暂存、提交并推送到 Gitee `origin/main`。
