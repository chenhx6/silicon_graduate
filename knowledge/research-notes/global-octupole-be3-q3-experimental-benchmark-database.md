---
type: research-note
title: "全核图直接电八极跃迁 B(E3) 与 Q3 实验基准数据库"
aliases: [global octupole B(E3) Q3 benchmark, direct E3 benchmark database]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
scope: global-even-even-3minus-to-0plus-benchmark
evidence_sources: [Kibedi_Spear_2002, Butler_Nazarewicz_1996, Bucher_2016, Bucher_2017, Gaffney_2013, Butler_2020]
created_from: Day26 global direct E3/Q3 benchmark database study
promotion_target: octupole-and-rare-electromagnetic-decay
tags: [octupole, E3, B(E3), Q3, database, systematics, evidence-boundary]
data_file: "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/global-octupole-db/global_octupole_be3_q3.csv"
analysis_script: "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/global-octupole-db/analyze_global_octupole_be3_q3.py"
---

# 全核图直接电八极跃迁 `B(E3)` 与 `Q3` 实验基准数据库

## Research Trigger

本轮任务要求建立跨质量区的直接电八极跃迁基准，重点比较双幻核、富中子 Ba/Ce、Rn/Ra/Th 轻锕系，并检验三条联系：`B(E3)` 与首个 `3−` 激发能的反比趋势、`Q3–beta2–beta3` 的经验换算，以及静态梨形与软八极振动在多观测量上的区分。

数据库不是把评价表自动当作独立实验全集。当前快照有 14 个核素记录：5 个直接库仑激发记录，6 个旧评价/汇编记录，3 个同时引用 Kibédi–Spear 与 Butler–Nazarewicz 的历史比较记录。数值列保留 `evidence_tier`、`source_lineage`、`local_evidence_locator` 和 `needs_review`，以便后续逐条回到原始寿命或库仑激发论文。

## Grounded Evidence

### 1. 直接库仑激发基准

- `144Ba`：Bucher *et al.* 的垒下 `144Ba+208Pb` 库仑激发给出 `B(E3;3−→0+)=48^{+25}_{−34} W.u.`，并给出拟合 `Q3=1.73^{+0.45}_{−0.62}×10^3 e fm^3`；`beta3=0.17^{+0.04}_{−0.06}` 依赖转子和高阶形变转换。[Bucher 2016 source page, lines 52–56](../sources/bucher-2016-144ba-direct-octupole.md:52)
- `146Ba`：独立的 `659 MeV` 束流库仑激发给出 `B(E3;3−→0+)=48^{+21}_{−29} W.u.`；原件明确将直接 E3 强度与 E1 偶极矩相消分开。[Bucher 2017 source page, lines 52–58](../sources/bucher-2017-146ba-direct-octupole.md:52)
- `220Rn` 与 `224Ra`：Gaffney *et al.* 的 MINIBALL/GOSIA 实验报告最低跃迁矩阵元 `810(50)` 与 `940(30) e fm^3`，以及 `Q3≈2180(130)` 与 `2520(90) e fm^3`。[Gaffney 2013 source page, line 60](../sources/gaffney-2013-pear-shaped-rn-ra.md:60) 由同一轴对称转子换算，数据库记录约 `33` 与 `42 W.u.`；后者是换算值，直接实验量仍以矩阵元和 Q3 列为准。
- `222Ra` 与 `228Ra`：Butler *et al.* 的多步库仑激发给出 `0+→3−` 矩阵元 `1.13(9)` 与 `0.87(15) e b^{3/2}`，每跃迁 `Q3=3030(240)` 与 `2300(400) e fm^3`。[Butler 2020 source page, lines 50–58](../sources/butler-2020-222-228ra-octupole-evolution.md:50) 由矩阵元和 W.u. 定义得到数据库的约 `62` 与 `35 W.u.`，这是派生量；论文另给转子模型聚合 `Q3=3120(190)` 与 `2230(290) e fm^3`。[Butler 2020 source page, line 65](../sources/butler-2020-222-228ra-octupole-evolution.md:65)

### 2. 双幻核与历史汇编基准

`16O (13.5 W.u.; E(3−)=6129 keV)`、`40Ca (27 W.u.; 3737 keV)` 和 `208Pb (34 W.u.; 2615 keV)` 在 CSV 中作为 Kibédi & Spear 评价基准记录。`140Ba (15 W.u.)`、`226Ra (36 W.u.)`、`228Ra (18 W.u.)`、`226Th (35 W.u.)` 和 `228Th (29 W.u.)` 也按用户给出的评价中心值登记；`148Ce` 只保留覆盖占位行，没有在未找到数值 locator 前填入 B(E3)。

Kibédi & Spear 的可核书目信息是：T. Kibédi and R. H. Spear, “Reduced electric-octupole transition probabilities, B(E3; 0_1^+→3_1^−)—an update,” *Atomic Data and Nuclear Data Tables* **80**, 35–82 (2002), DOI [`10.1006/adnd.2001.0871`](https://doi.org/10.1006/adnd.2001.0871)。Crossref/OpenAlex/Semantic Scholar 均可确认身份，但本轮未取得可读的开放原件；因此这些行的 locator 只写到“ADNDT 80, pp.35–82，nuclide entry”，并保持 `needs_review=true`。Butler & Nazarewicz 的 RMP 是反射不对称核的历史框架与来源图，不应被计数为这些旧数值的独立实验。[Butler–Nazarewicz source page, lines 25 and 47](../sources/butler-nazarewicz-1996-intrinsic-reflection-asymmetry.md:25)

### 3. 数据格式和单位审计

CSV 位于 [`global_octupole_be3_q3.csv`](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/global-octupole-db/global_octupole_be3_q3.csv)。`b_e3_down_wu` 固定表示 `B(E3;3−→0+)`；同一约化矩阵元若写成 `B(E3;0+→3−)`，需乘初态简并因子 7，不能被误读成第二个实验值。`q3_direct_efm3` 只记录来源明确给出的 Q3；`q3_derived_from_b_wu_efm3` 使用

`B_W.u.(E3;3−→0+)=R0^6/(16π)`, `R0=1.2 A^(1/3) fm`, `Q3=sqrt(16π B_down)`。

脚本 [`analyze_global_octupole_be3_q3.py`](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/global-octupole-db/analyze_global_octupole_be3_q3.py) 重算 13 个有中心 B(E3) 的条目，CSV 派生 Q3 与公式相差均小于 2%，差异来自四舍五入。该计算是单位和约定审计，不是新的实验拟合。

### 4. 经验 `Q3–beta2–beta3` 标度

采用用户指定的经验式

`Q3 ≈ (3/(4π)) Z e R0^3 beta3 (1+0.8 beta2)`。

`144Ba` 的直接 `Q3≈1.73×10^3 e fm^3`、`beta2=0.18` 和原文摘录的 `beta3≈0.17` **不能在本轮直接代入上述用户式后得到同一数值**：用 `R0=1.2 A^(1/3)` 反演约得 `beta3≈0.455`。这不是被脚本隐藏的算术错误，而是 Q3 算符归一化、形变参数定义或原文半径/密度转换约定尚未对齐的证据边界；在取得 Bucher 原始转换方程前，CSV 同时保留两者但不宣称标度验证通过。对 `220Rn`、`224Ra` 的 Q3 是 Gaffney 的拟合内禀矩；对 `222Ra`、`228Ra` 是 GOSIA/转子约定的逐跃迁转换。不能把这些 Q3 直接当作无模型密度图像或可跨所有质量区共用的静态 `beta3` 标尺。

## Provisional Reasoning

### 1. `B(E3)`–`E(3−)` 反比趋势

对 CSV 中有明确能量的三个双幻核点，脚本拟合 `ln B(E3)` 对 `ln E(3−)` 的描述性斜率为 `−1.104`，`R²=0.965`。这与“较低的八极声子能量对应较强集体性”的直观趋势相容，但样本只有 `16O/40Ca/208Pb`，质量、壳闭合和实验来源同时变化，不能声称全核图普适幂律。Ba、Rn、Ra、Th 的 `E(3−)` 尚未从原始 level-scheme 逐条补齐，故没有把空白能量强行用于回归。

### 2. 静态梨形与软八极振动

单个大的 `B(E3;3−→0+)` 只确立强八极集体跃迁，不能独立选择深双阱静态梨形。Gaffney 原文明确指出，E2/E3 矩阵元与转动分布相容，但不能在“静态四极—八极形状宇称投影”和“四极形状上的八极振动”之间作唯一选择。[Gaffney source page, lines 69–74](../sources/gaffney-2013-pear-shaped-rn-ra.md:69)

更有信息量的是多跃迁图样与宇称能级：Butler 2020 将 `222Ra` 的多个近似恒定 Q3 与 `228Ra` 的 `2+→3−` 近零条目分别解释为稳定梨形和八极振动，但同时保留旋转对齐八极声子等替代解释。[Butler 2020 source page, lines 65–69](../sources/butler-2020-222-228ra-octupole-evolution.md:65) Gaffney 的既有整理给出 `224Ra` 交错宇称位移随自旋下降，而 `220Rn` 仍有较大位移；该判据和 Q3 平坦性应与 E3 共同使用，而非以 B(E3) 单点替代。[Gaffney source page, line 149](../sources/gaffney-2013-pear-shaped-rn-ra.md:149)

### 3. EWSR 耗尽比

本数据库不能计算可信的非能权或能权 E3 和规则耗尽比。当前主要记录首个 `3−` 到基态跃迁，且 Butler 2020 的星号矩阵元由转子关系耦合、并非完全独立。[Butler 2020 source page, lines 75–79](../sources/butler-2020-222-228ra-octupole-evolution.md:75) 因此脚本把 EWSR 标成 `not_computable`；不能把 `B(E3;3−_1→0+)` 除以理论总和后称为实验 EWSR fraction。

## Assumptions

- B(E3) 的方向统一为 `3−→0+`；文献若给 `0+→3−` 矩阵元，先按约化跃迁定义转换。
- W.u. 转 e²fm⁶ 使用 `R0=1.2 A^(1/3) fm` 的标准 Weisskopf E3 约定；派生 Q3 只用于比较和算术回放。
- `Q3–beta3` 经验式按用户给定形式执行；若与原文的 Q3/beta3 数值不符，记录为定义边界，不反向修改任何实验值。
- 直接 Q3、由 B(E3) 派生 Q3、由 Q3 反演的 beta3 是三种不同证据层。
- 评价表中心值可以进入候选基准，但不能与直接实验行合并计算“独立实验平均值”。
- 未取得原始 locator 的历史行保留中心值是为了覆盖审计范围，不表示其已通过本轮原件核查。

## Competing Explanations

- 大 B(E3) 可能来自八极软振动或大幅度零点涨落，而非深静态双阱。
- 多跃迁 Q3 的近似平坦性支持转动型内禀矩，但 GOSIA 转子耦合、相位选择和未观测态仍可能造成拟合相关。
- `E1` 小或变化大不能单独作为八极集体性强弱指标；146Ba 的直接 E3 保持强而 E1 受中子轨道占据和偶极相消影响。[Bucher 2017 source page, lines 64–68](../sources/bucher-2017-146ba-direct-octupole.md:64)
- 壳闭合双幻核的 B(E3) 与轻锕系/富中子 Ba 的 B(E3) 还混入不同半径、配对、壳结构和可达激发态密度效应。
- `Q3` 在不同论文中可能是内禀电多极矩、转子约定转换量或带有球谐归一化因子的约化矩阵元；这些定义未统一前，`Q3–beta3` 的数值比较具有竞争解释。

## Transfer Conditions

跨质量区比较只有在以下条件满足时才可复用：统一跃迁方向、统一 W.u. 定义和半径参数；区分直接矩阵元、转子换算与模型 beta3；同时有 E(3−)、交错宇称能级和至少一条以上独立 E3 链；保留相同的 GOSIA/寿命输入边界及来源谱系。对于 `144/146Ba`、`220/224Rn/Ra` 与 `222/228Ra`，优先比较原始矩阵元和直接 Q3，不把评价中心值用作独立复测。

## Failure Conditions

- Kibédi–Spear 原件或对应 primary lifetime 论文给出不同中心值、方向约定或不确定度时，旧评价行必须回退为待核查。
- 能级混淆、`3−` 非首态、分支漏计、内转换或 feeding 修订会使寿命 B(E3) 失效。
- GOSIA 的目标核矩阵元、先验寿命、相位、星号耦合或系统误差协方差不可取得时，不能把多跃迁 Q3 当作完全独立样本。
- `E(3−)` 缺失或来自不同 level-scheme 版本时，`B(E3)`–`E(3−)` 回归可能是选择效应。
- 若 Bucher 原件的 `Q3`/`beta3` 转换方程与用户式采用不同球谐或半径归一化，直接的 beta3 反演差异不能用实验误差解释，必须更改字段定义或保留不可比状态。
- 用首态 B(E3) 代替完整 EWSR，或用单个 Q3 直接宣称静态深双阱，均属于不可接受的推断越界。

## Falsification or Reverse Tests

1. 为每个评价行获取 primary lifetime/Coulomb-excitation 论文，逐字段核对 `E(3−)`、寿命、分支、B(E3) 方向和不确定度；若任一数值不符，保留旧值并新增 lineage，不静默覆盖。
2. 补齐 `Ba/Rn/Ra/Th` 的首个 `3−` 能量后，按质量区、壳闭合和实验方法分层拟合 `B(E3)`–`E(3−)`；若斜率在分层后消失，撤回“全核图反比律”。
3. 对 `222Ra/228Ra` 复核未带星号与带星号 E3 耦合的协方差；若在独立矩阵元子集上 Q3 不再近似平坦，降低静态梨形解释等级。
4. 获取完整负宇称低能级的 E3 分支并计算 `m0`、`m1` 与 EWSR；若首态只占很小部分，则不能用首态强度代表区域集体性耗尽。
5. 将 parity splitting、E3、E1/E3 和 `Q3` 放入同一来源谱系矩阵；若大 E3 与大宇称劈裂、Q3 随自旋衰减同时出现，应优先保留软振动竞争解释。

## Open Questions

- `148Ce` 的评价 B(E3) 与首个 `3−` 能量究竟对应哪一条独立寿命实验？当前只登记覆盖占位行。
- `140Ba`、`226Ra`、`226Th`、`228Th` 的用户给定中心值需要逐条追溯到 primary experiment，而不是停留在 Kibédi–Spear 评价 entry。
- `144Ba`、`146Ba`、`220Rn`、`224Ra`、`222Ra`、`228Ra` 的 E(3−) 应从原始 level scheme 补录，避免把 Q3–E3 能量趋势建立在空白值上。
- 是否能取得完整 GOSIA likelihood/covariance 和 target matrix-element inputs，从而比较直接 Q3 的统计相关性？
- 哪些额外 `3−_2,5−,7−` E3 分支足以把 EWSR fraction 从“不可计算”推进到“有界估计”？

## Human Review

本页和 CSV 均为 Codex self-audit，`review_status=unreviewed`，没有把 self-audit 写成 human review。优先人工核验：Kibédi–Spear 评价行、`148Ce` 占位、`140Ba` 和 Th/Ra 历史中心值；其次核对 Bucher/Gaffney/Butler 的原始表格、方向约定和 GOSIA 相关性。用户若后续提供 primary PDF 或纠正值，应以具体 record_id 和 locator 触发定向修订。

## Promotion or Rejection History

- 2026-10-29：建立数据库 v1；直接库仑激发与评价汇编分层，未将评价值推广为独立实验。
- 2026-10-29：脚本重算 13 个 B(E3)→Q3 条目；转换差异低于 2%，保留为单位/四舍五入检查。
- 2026-10-29：`B(E3)`–`E(3−)` 斜率仅基于 3 个双幻核点，降级为描述性结果；不晋升为全核图定律。
- 2026-10-29：EWSR fraction 因 final-state coverage 不完整而拒绝计算；静态梨形与软振动只保留条件性比较。
