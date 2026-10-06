---
type: learning-daily
run_id: 2026-09-27-day-01-01
prompt_run_id: prompt-2026-09-27-day-01
run_date: 2026-09-27
timezone: Asia/Shanghai
day_index: 1
phase: baseline-and-research-contract
cycle: 2026-09-30-day-substantive
schedule_id: wiki-daily-learning
schedule_name: Wiki 30-day substantive daily learning
run_kind: substantive
acceptance_only: false
review_status: ai-draft
session_id: 01a0e1e1-812e-7eb3-a140-cedd5fe10111
---

# 2026-09-27 Day 1：基线考试与研究契约

## Run state

- 本轮执行正式 30 天实质周期的 Day 1，主题是“基线考试与研究契约”。本次注入的 prompt 标识为 `prompt-2026-09-27-day-01`，运行目录为 `outputs/learning-daily/20260927-DAY1-baseline-research-contract-run-01/`；状态文件在开始时仍为 `next_day_index: 1`。
- 启动前按约读取了 [README](../../README.md)、[Wiki index](../../knowledge/index.md)、[profile](../../profile.md)、[active handoff](../../system/handoff.md)、[PLAN](../../PLAN.md)、近期日报、[一个月 CLI 训练计划](../../outputs/plans/2026-09-22-one-month-codex-cli-apprenticeship.md)、[Day 1 任务矩阵](../../outputs/plans/2026-09-22-one-month-daily-task-matrix.md)、[A≈130 三轴论文管线](../../outputs/plans/2026-09-22-a130-triaxial-thesis-pipeline.md)、[continuous-learning workflow](../../system/workflows/continuous-learning.md) 和 [scheduled-continuation workflow](../../system/workflows/scheduled-continuation.md)。
- 写入前执行 `python3 system/scripts/wiki_boundary_check.py --root .`，exit `0`；继承的 dirty baseline 被保留，未修改 `raw/`、`PLAN.md` 或 `raw/zotero/wiki-inbox.bib`。
- 本轮 Codex session 为 `01a0e1e1-812e-7eb3-a140-cedd5fe10111`，可恢复命令为 `codex resume 01a0e1e1-812e-7eb3-a140-cedd5fe10111 -C /workspace/wiki -s danger-full-access -a never`。该 ID 来自本次运行的 `events.jsonl` 的 `thread.started` 记录；runner 的最终 receipt 仍负责写入其正式 session 字段。
- 原排程窗口于 `2026-09-28 10:00 Asia/Shanghai` 结束；原 runner 因 Matta 来源 backlink 缺失及 Continuation 14 usage-limit exit `1` 留下 `failed-verification`。用户随后明确授权完成恢复验收。本次已修复来源链接、重验报告和写回，并按 runner 的字段完成恢复：receipt 状态为 `completed`、Day 1 已计数，原始失败状态、exit code 和原因保留在 recovery audit 字段中。

## Candidate pool and selection

候选池由 [knowledge/questions.md](../../knowledge/questions.md)、[A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)、最近三次 Day 1 记录、[131Ce collective-mode project](../../knowledge/projects/131ce-collective-mode-discrimination.md) 以及最近的 source fingerprints 重建。候选按 Day 1 卡片要求覆盖核素/质量区、竞争机制、实验 observable、证据层级和 source-independence 风险。

- **连续性槽位：Ding 2012 的 127,128I 基线契约复核。** 这是当前矩阵的直接锚点；需要检查“能级放置—ADO/符合 assignment handle—作者解释—模型输出—Codex 推断”是否仍分层，避免重复把已有矩阵行写成新证据。主来源为 [Ding 2012 source page](../../knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md)，原始文件哈希与 PDF locator 在该页保留。
- **新颖性槽位：144Ba/146Ba 的直接 E3 对照。** [Bucher 2016](../../knowledge/sources/bucher-2016-144ba-direct-octupole.md) 和 [Bucher 2017](../../knowledge/sources/bucher-2017-146ba-direct-octupole.md) 与 A≈130 的 127,128I 基线不重叠，但能检验“直接跃迁强度”和“由模型转换的形变参数”应如何分层。两篇论文是相邻同位素的独立实验，不把共同的 CHICO2/GRETINA/GOSIA 方法谱系当作完全独立装置复现。

**打开来源前的主动回忆与纠错：**

1. `J^π` 是状态的自旋与宇称标签；单条 `E_γ` 或规则间隔不能独立给出它。
2. 激发能 `E_x` 相对参考态定义；能级纲图连接的是“态—跃迁”，不是 PES 图。
3. `γ` 能量、符合、强度平衡和 `R_ADO` 是直接或派生观测；claim 还需要 claim kind、locator、evidence level 和 source lineage。
4. 作者的 band/configuration 标签是 interpretation；PES/NPA/壳模型的 `β、γ`、能量和波函数是 model result；缺失 companion observable 的判断是 Codex inference。
5. `R_ADO` 依赖阵列角度、alignment、feeding、效率和约定，不能把一个实验的经验阈值移植到另一个阵列。
6. 直接 `B(E3)` 比相对 E1 或 parity-doublet 印象更接近跃迁强度证据，但把 `B(E3)` 转成静态 `β3` 仍依赖形状模型和高阶多极项。

基线错误日志保留四类高频错误：把 assignment 当成 measurement；把能量闭合当成唯一 `J^π` 或模式判据；把阵列特定 ADO 当通用阈值；把模型 `β/γ/β3` 当实验形状测量。今天的主线复核这些错误，而不是再添加同一 Ding 实验谱系的重复行。

## Sources and evidence

### 连续性来源：Ding 2012

- [Ding 2012 source page](../../knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md) 的 `status: ai-draft`、`review_status: unreviewed` 和各 claim 的 `needs_review: true` 原样保留。原始 PDF 为 `raw/papers/degree dissertation/丁兵 - 博士论文.pdf`，SHA-256 为 `ca7765ad962ea0c106791532f5a7d9f359533d25bb0170f03197bfec414be5c7`。
- **实验直接事实：** `^{124}Sn(^{7}Li,4n)^{127}I` 的新纲图、γ 线和 ADO 表属于 D12-1；`^{128}I` 的 20 个能级、31 条跃迁和 Fig.6.2/Table 6.1 属于 D12-7。PDF 逐页复核还显示作者用开窗符合、强度平衡、交叉跃迁和能量闭合建立 128I 纲图；这些是 placement evidence，不自动升级为唯一结构解释。
- **最小级联：** D12-9 给出 285.2 keV 的 `8^-` 起始结构、696.2、1041.7、1454.0 和 1873.5 keV 的后续能级，以及 411.0、345.4、412.3、419.5 keV 的表中 γ 线。表内 345.4 keV 与由四舍五入能级相减得到的 345.5 keV 差异是 0.1 keV rounding residual。
- **作者解释：** D12-2、D12-4 和 D12-9 的退耦带、高 K 组态、`\pi g_{7/2}\otimes\nu h_{11/2}` 类转动结构和负 `E2/M1` 混合比是 author interpretation；不能写成某条 γ 线直接测得的组态或形变。
- **模型结果与反证：** D12-6 的 PES 柔软势面、D12-8 的 NPA/经验壳模型组态和 D12-10 的两准粒子多重态计算属于 model result。D12-8 明确保留部分 `6^-/7^-` 理论顺序与实验相反、实验 `8^-` 落在理论候选之间的限制。
- **证据契约：** AR-2 明确 ADO 的阵列和分析条件依赖；AR-4 将未来偏振、寿命和 `B(M1)/B(E2)` 异常列为对高 K 小扁椭解释的 falsifier。方法页 [Spin/parity assignment](../../knowledge/methods/spin-parity-assignment.md) 也要求至少一个 transition-property handle，不能只靠规则能级间隔。

### 新颖性对照：144Ba/146Ba

- [Bucher 2016 source page](../../knowledge/sources/bucher-2016-144ba-direct-octupole.md) 的 BU16-1 报告 `B(E3;3^-\rightarrow0^+)=48^{+25}_{-34}\,W.u.`（PDF pp.3–4、Table I）；BU16-3 记录 CHICO2/GRETINA 粒子门、Doppler-corrected γ yields 和 `^{134}Xe` control。BU16-2 和 BU16-AR-2 同时保留 `Q_3/β_3` 转换的 rigid-rotor、高阶多极和 E1/E3 sign 边界。
- [Bucher 2017 source page](../../knowledge/sources/bucher-2017-146ba-direct-octupole.md) 的 EXT146-1 报告相邻 `^{146}Ba` 的 `B(E3;3^-\rightarrow0^+)=48^{+21}_{-29}\,W.u.`（PDF pp.2–3、Table I）；EXT146-2/3 区分了持续的 E3 强度、变化的 E1 dipole moment 和 SCCM/GCM 的 occupancy explanation。该页保留 raw event matrices、完整 GOSIA covariance 和 SCCM code 不可得的边界。
- Crossref DOI 复核返回 Bucher 2016 的 PRL 116, 112503（online 2016-03-17）和 Bucher 2017 的 PRL 118, 152504（online 2017-04-12）；检索结果只用于身份核验，不替代 PDF locator。

四层归类为：D12-1/D12-7/D12-9 与 BU16-1/EXT146-1 的能级、产额、`R_ADO`、`B(E3)` 是实验事实；D12-2/D12-4/D12-9 与 octupole-shape wording 是作者解释；D12-6/D12-8/D12-10 与 BU16-2/EXT146-3 是模型或模型链接结果；“需要 mixing ratio、偏振、寿命、绝对强度或独立 linking”是本任务推断。

## Theory/analysis exercise

### 1. 128I 最小能级纲图与表格交叉核算

从 D12-9 和 Fig.6.2/Table 6.1 重建结构 B：

`8^-_1(285.2) ←[411.0] 9^-(696.2) ←[345.4] 10^-(1041.7) ←[412.3] 11^-(1454.0) ←[419.5] 12^-(1873.5) keV`。

用表内能级相减复核 γ 线，得到 `411.0`、`345.5`、`412.3` 和 `419.5 keV`。相对表值的残差为 `0.0, +0.1, 0.0, 0.0 keV`，与一位小数显示精度一致。这个算术只验证 placement closure；它不能独立验证 `J^π`、`\pi g_{7/2}\otimes\nu h_{11/2}` 组态或集体模式。

### 2. 直接 E3 的不对称误差比较

把两篇相邻同位素的中心值相减，`ΔB(E3)=48-48=0 W.u.`。若只作近似独立误差传播，正向合成误差为 `sqrt(25^2+21^2)=32.6 W.u.`，负向合成误差为 `sqrt(34^2+29^2)=44.7 W.u.`。因此两次测量的中心值一致；可迁移的结论是“E3 强度在两个同位素中都很大”，不是“静态 `β3` 已被无模型地测得”。共同的实验方法和分析框架还要求保留 source-lineage caveat。

### 3. 十二条基线陈述的口试分类

| 编号 | 陈述类型 | 本轮判定 |
|---|---|---|
| B1 | 表 6.1 的 411.0 keV 线连接 696.2 与 285.2 keV | 实验直接事实（D12-7、D12-9） |
| B2 | 101.3/102.2/411.0 keV 路径由符合和能量平衡支持 | 实验事实，仍受门条件和污染控制约束 |
| B3 | `696.2−285.2=411.0 keV` | 由来源派生的可复核算术 |
| B4 | `R_ADO(411.0)=0.65(5)` | 本阵列的直接报告量 |
| B5 | 411.0 keV 因而必然是唯一 M1 | 过强推断；被 AR-2 限制 |
| B6 | 285.2 keV 态被作者建议为 `8^-` | 作者解释/assignment |
| B7 | `\pi g_{7/2}\otimes\nu h_{11/2}` 是直接测得组态 | 过强推断；依赖 D12-8/D12-9 的模型和系统学 |
| B8 | NPA 重现部分低位多重态间隔趋势 | 模型结果 |
| B9 | NPA 的部分 `6^-/7^-` 顺序与实验相反 | 模型—实验边界事实（反证） |
| B10 | 1460.9/1562.2/1964.9 keV 正宇称多重态与组态标签相容 | 作者解释加模型比较，不是单线测量 |
| B11 | PES 的浅 `β/γ` 势能面就是实验三轴形变 | 过强推断；模型结果不能替代 `Q_t/B(E2)` |
| B12 | 缺少寿命、偏振、绝对强度和独立 linking 会限制模式判别 | 实验方法事实加 Codex 证据推断 |

## Counter-evidence and missing companion observables

- **Ding 的反证：** D12-8 的理论 `6^-/7^-` 顺序反转和候选 `8^-` 夹在不同计算态之间，说明能量相容不能唯一锁定组态。AR-2 还禁止把 `R_ADO` 作为跨阵列通用阈值。
- **Ding 的必要 companion：** `J^π`/多极性需要 transition-level mixing ratio、线偏振和必要的转换系数；集体性需要寿命、绝对 `B(E2)/B(M1)` 或 `Q_t`；组态和模式竞争需要带间 linking、转移/反应选择性，必要时需要 g-factor。若未来偏振或寿命给出 AR-4 所列反常结果，应下调高 K/小扁椭解释。
- **Bucher 的反证：** BU16-2/BU16-AR-2 和 EXT146-3 都把直接 `B(E3)` 与模型转换的 `β3` 分开；146Ba 的 E1 变小不能单独推出 E3 变弱。GOSIA 相关协方差、原始事件矩阵和 SCCM 代码不可得，因此不能执行 L4 重拟合。
- **source independence：** Ding 的实验事实、作者解释和模型比较属于一个学位论文实验谱系；Bucher 2016 与 2017 是不同同位素的独立 Coulomb-excitation 实验，但共享实验技术和部分作者网络。它们足以做相邻同位素比较，不足以被写成完全无共同系统误差的重复实验。
- **L4 readiness boundary：** 本轮只有可定位的 PDF/知识页和表格数字，没有事件级 spectra、探测器 response、校准协方差、GOSIA/sorting code 或失败模板；因此只做能级闭合和误差传播，不生成 proxy fit。

## Continuation 1: model-to-observable identifiability

### 选择与主动回忆

上一块的 Ding/144Ba 复核已经达到“事实—解释—模型—推断”基线；本 continuation 选择 handoff 指定的模型选择路线。打开来源前先回忆：static mean-field/HFB 给 intrinsic density 与 pairing；cranked mean-field/CSM 给 rotating-frame Routhian、alignment 和 crossing；angular-momentum projection/PSM/TPSM 把 intrinsic basis 投影到良好 `I` 并混合配置；三者都不能仅凭计算的 `β/γ`、能级或波函数权重证明实验形状或模式。

### 新来源证据链

- [Åberg–Flocard–Nazarewicz 1990](../../knowledge/sources/aberg-flocard-nazarewicz-1990-mean-field-shapes.md) 的 AFN90-1/AFN90-4 把 mean-field minima 定义为 intrinsic model output，并提醒 `β₂/γ` 与 rotation-axis sector 依赖约定；AFN90-3 要求 octupole/coexistence 另找 companion observables。
- [Hara–Sun 1995](../../knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md) 的 HS10-1/HS10-3 给出 Nilsson+BCS → angular-momentum projection → projected configuration mixing → energy/electromagnetic observables 的方法链；HS10-4 明确早期 A≈130 axial-PSM 与实验不符只能提出三轴候选，不能直接证明三轴形变；HS10-5 保留 particle-number projection 与截断空间的 spurious-state 风险。
- [Ding et al. 2021](../../knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md) 的 D21-1 是 `131Ba/133Ce` level/strong-coupling 直接证据，D21-4/D21-5/D21-6 显示 CSM/QTR 中 `γ`、低-j `s1/2` Coriolis mixing 和 attenuation 可共同改变 `S(I)`；D21-7 的 PES `β₂,γ` 仍是模型极小值。

### 理论/设计练习：四层可识别性表

| 模型层 | 能生成/比较的量 | 可以被什么实验量约束 | 不能越过的结论 |
|---|---|---|---|
| static mean-field/HFB | intrinsic density、pairing、候选 `β₂/γ/β₃` minima | masses、`E(2+)`、寿命/`Q_t`、transfer 或 Coulomb-excitation observables | 单一 minimum 不是 laboratory band identity 或 rigid shape 的直接测量 |
| CSM/QTR | Routhian、alignment、`J^(2)`、crossing、`S(I)` 与参数敏感性 | transition-level `δ`/偏振、`R_ADO`/DCO、绝对 `B(E2)/B(M1)`、partner linking | `S(I)` 或拟合 `γ` 不能单值反演非轴性；低-j mixing/attenuation 是竞争解释 |
| PSM/TPSM/projected mixing | good-`I` bands、configuration weights、signature、`B(E2)/B(M1)`、g-factors | partner-resolved strengths、g-factor、δ/偏振、寿命和同一数据集的 common-input comparison | axial mismatch、投影能级或 wave-function weight 不能单独证明三轴、wobbling 或 chirality |
| beyond-mean-field fluctuation/mixing | competing minima、collective wave functions、shape-mixing trend | `Q_t`、E0/E2 links、invariants、寿命、transfer/Coulomb excitation | 只有模型极小值而无实验连接时，shape coexistence 仍是候选解释 |

将表格应用于 `131Ce` 的最小实验设计：A 阶段先固定 band/transition identity；B 阶段测连接跃迁的 `δ` 与线偏振；C 阶段取得 partner-resolved lifetime、absolute `B(E2)/B(M1)` 或 `Q_t`；D 阶段才在相同带和相同 observables 上比较 CSM/QTR、projected mixing 与 γ-soft alternative。该顺序是设计规则，不是对 `131Ce` 缺失数据的代理拟合。

### Continuation 1 反证与判定

- AFN90-1/AFN90-4 的 intrinsic/model boundary 反驳“计算 `γ` 就是实验形变”；HS10-4 反驳“axial PSM 失败就证明三轴”。
- D21-6 是直接机制反证：在 Coriolis attenuation 改变时，类似 `S(I)` staggering 可在不同 `γ` 区间消失或恢复；因此 `S(I)→γ` 不是唯一映射。
- HS10-5 的截断/particle-number caveat 说明 projected agreement 也需要 basis and operator sensitivity；没有 response、covariance 和 code，本轮不进入 L4。

**Continuation 1 decision: revises + limits。** 模型选择卡现在有可定位的模型—观测 crosswalk：CSM/QTR 用于机制敏感性，PSM/TPSM 用于良好角动量和跃迁比较，mean-field/HFB 用于 intrinsic 候选；三者都必须由 transition properties 和绝对强度检验。该结果修订“先选最复杂模型即可解决模式争议”的倾向，但不改变 `131Ce` 当前 signature/configuration coupling 优先、γ-soft background provisional、wobbling/chirality unsupported 的项目排序。

## Continuation 2: `131Ce` electromagnetic-manifest audit

### 候选选择与外部检索边界

本 continuation 从 project 的下一决定性问题中选择 `131Ce` Bands 1–7 的 measured `δ`、偏振、partner-resolved lifetime、absolute strength 和 linking manifest；模型 crosswalk 已经完成，继续扩展模型不会增加同等信息。候选来源按“目标核直接性—observable 完整度—source independence—locator 可得性”排序：Alwaleedi 2013 目标核纲图、Singh 2016 与 Li 2004 寿命、Petrache 1998 HD 控制，以及历史 Gizon 1977 能带论文的外部身份核验。

Crossref 给出 Gizon 等论文题名 *The h11/2 and g7/2 band structures in 131Ce and 129Ce*、*Nuclear Physics A* **290**(1), 272–284 (1977)，DOI `10.1016/0375-9474(77)90679-0`；Semantic Scholar 只返回相同身份和 `openAccessPdf: CLOSED`。没有本地 PDF、raw 哈希或可引用页码，因此它是 blocked discovery route，不是本轮科学 evidence。这个边界防止把历史题名或搜索元数据误写成 measured mixing ratio/polarization。

### 已有来源的 manifest 分类

| manifest 字段 | 现有可用证据 | 状态与边界 |
|---|---|---|
| band/level identity | Alwaleedi AW13-1–AW13-8 的 Bands 1–7、连接和组态图 | `available-provisional`；Band 2 parity conflict 与 Band 5 duplicate label 仍按原文隔离 |
| measured transition `δ` | 无；AW13-9 从 branching ratio 明确假设 `δ=0` | `missing-direct`；不能把 `R(0)` 当 measured mixing ratio |
| linear polarization | 本轮公开 source pages 未找到 Bands 1–7 的 target-specific polarization matrix | `missing-direct` |
| partner-resolved lifetime/absolute strength | SI16-1 和 LI04-1/LI04-3 给 yrast/parity-specific lifetimes；PE98-7 给独立 HD `Q0` | `partial-but-nonpartner`；覆盖不同带或不同形变扇区，不能填补 thesis Bands 1–7 partner matrix |
| interband linking and common transition matrix | AW13-1/AW13-2 有谱学连接，但没有和 measured `δ`、偏振、partner-resolved strengths 同时闭合 | `partial-identity-only` |
| model shape/γ | AW13-6/7、SI16-6/7 和 PE98-9 是 Woods–Saxon/TRS 或 cranked-Strutinsky model/interpretation | `model-only`；不作为直接形变观测 |

### 定量/设计练习：δ 假设的可见影响

Alwaleedi 的 AW13-9 给出 `R(δ)=R(0)/(1+δ²)`。因此 `|δ|=0.5` 时 `R(δ)=0.8R(0)`：把 `δ=0` 当真值会相对真实值高估 25%，相对 `R(0)` 的差为 20%。这能量化 `δ` 缺失对派生 `B(M1)/B(E2)` 的影响，但不能产生 `δ` 的符号、偏振相位或 partner assignment。

用四层 manifest 作为最小实验设计：

1. 先以 AW13-1/AW13-2 固定同一 transition/level identity；任何 parity 或 duplicate mapping 冲突先隔离。
2. 对连接 `ΔI=1` 跃迁同时测 mixing ratio 的幅值/分支和线偏振，才能把 M1/E2 竞争从 `δ=0` 假设中释放出来。
3. 在相同 band manifest 上取得多带寿命、absolute `B(E2)/B(M1)` 或 `Q_t`；SI16-1、LI04-1/3 的不同带寿命只能作为 E2 collectivity controls。
4. 将新增 interband links 和 absolute strengths 输入同一套 CSM/QTR/projected/γ-soft comparison；若没有 common response/covariance，仍停在 L3 readiness。

### 反证、独立性与判定

- AW13-11 直接列出本数据集没有寿命、绝对 `B(E2)`、偏振或直接 γ-rigidity measurement；AW13-9 的 `δ=0` 派生比值不能关闭这些缺口。
- SI16-1/SI16-5 的 yrast lifetime/`Q_t` 趋势约束 E2 collectivity，但 SI16-7 的具体 `γ` 来自 TRS/作者解释；LI04-1/LI04-3 的正负宇称序列同样不是 same-parity partner evidence。
- PE98-7 的 HD `Q0=7.3(4) eb` 是同核独立强形变扇区；PE98-13 明确没有把 HD 带映射到 normal-deformed Bands 1–7 或 chirality，因此它提高 shape-coexistence 可行性而不建立共存。
- Gizon 1977 的闭合全文和 locator 缺失是 source blocker，而非反证；没有把 Crossref/Semantic Scholar 元数据计作实验测量。

**Continuation 2 decision: no material change to mode ranking, but strengthens the readiness boundary.** 现有证据仍支持 signature/configuration coupling 作为 band-identity 首选，寿命作为 E2/core-response 正交约束；γ-soft 维持 model-assisted background，wobbling/chirality 维持 `unsupported`/`unestablished`。本轮把“缺 δ/偏振/partner strengths”从开放描述转成可执行 manifest 状态，没有生成 proxy fit 或读取用户数据。

## Continuation 3: blocked-source acquisition audit

### 获取路线与证据边界

本 continuation 只处理 Gizon 1977 的合法全文获取，不把访问元数据当核结构证据。逐一检查了以下公开路线：

- [OpenAlex work record](https://api.openalex.org/works/https://doi.org/10.1016/0375-9474(77)90679-0)：身份为 *The h11/2 and g7/2 band structures in 131Ce and 129Ce*，`is_oa=false`、`pdf_url=null`、`any_repository_has_fulltext=false`。
- [Unpaywall record](https://api.unpaywall.org/v2/10.1016/0375-9474(77)90679-0?email=research@example.org)：`oa_status=closed`、`best_oa_location=null`、`oa_locations=[]`、`has_repository_copy=false`。
- [Semantic Scholar record](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/0375-9474(77)90679-0?fields=title,abstract,openAccessPdf,externalIds,url,venue,year)：`openAccessPdf.status=CLOSED`，abstract 被 publisher elision，不能提供 locator。
- ScienceDirect landing page 与 CORE DOI search 的公开请求分别返回 HTTP 403；Google Scholar 请求超时。本轮没有循环请求、绕过控制或把 HTML/元数据当 PDF。

### Readiness exercise：全文获取四项门

| 门 | Gizon 1977 当前状态 | 影响 |
|---|---|---|
| bibliographic identity | `available`（Crossref/OpenAlex/Unpaywall/Semantic Scholar 一致） | 可记录题名、作者、期刊、DOI |
| lawful full text | `blocked`（无 OA/repository copy；publisher/CORE 受限） | 没有页码、图表、公式或 level-scheme locator |
| raw hash / reproducible artifact | `missing` | 不能建立本地 source page 或 hash-backed claim table |
| measured `δ`/polarization/partner strengths | `unknown`, not `absent` | 不能据题名推断其是否存在；保持 open acquisition question |

这项练习的停止条件是：没有全文和 locator 就不建立 source claim、不更新 `131Ce` 模式排序。下一次合法路线是机构订阅/图书馆馆际获取或作者/仓储提供的可授权副本；在此之前只保留 blocked status。

### Continuation 3 decision

**Decision: no material scientific change; source-acquisition blocker confirmed.** Gizon 1977 不能补齐 `131Ce` measured `δ`、偏振或 partner-resolved strength manifest。当前 signature/configuration coupling 首选、γ-soft model-assisted background、wobbling/chirality unsupported/unestablished 的排序不变；本 continuation 只提高了来源获取状态的可复现性。

## Continuation 4: next-measurement information-gain design

### 设计问题与主动回忆

Gizon 1977 进入 blocked-needs-source 后，继续重复检索的预期信息增益下降。下一高价值问题改为：在不读取用户独立数据的条件下，哪一项新测量最可能改变 `131Ce` 五种竞争解释的排序？设计原则先后是 band identity、transition character、absolute strength、统一模型比较；任何“高分”都是 ordinal design score，不是实验显著性。

### 可复核设计表

对每项测量包定义 `priority = discrimination + gap + feasibility`，每一项取 1–3 级：

| 优先级 | 测量包 | 分数（判别/缺口/可行性） | 主要能改变的判断 |
|---|---|---|---|
| 1 | `ΔI=1` connecting transitions 的 measured `δ` + 线偏振 | `3/3/2 = 8` | 释放 AW13 `δ=0` 假设，区分普通 signature/configuration links 与 wobbling/chirality 的 M1/E2 pattern |
| 2 | 同一 Bands 1–7 manifest 的 partner-resolved lifetimes + absolute `B(E2)/B(M1)`/`Q_t` | `3/3/2 = 8` | 把 SI16/LI04 非 partner E2 controls 变成同带 collective-strength test，检验 out-of-band E2 与 core response |
| 3 | 完整 interband linking、band identity 和 common transition matrix | `3/3/2 = 8` | 先排除 pairing/crossing/HD–ND 误配，再谈 wobbling phonon 或 chiral partner |
| 4 | quadrupole invariants/Coulomb excitation 或统一 soft-vs-rigid comparison | `2/3/1 = 6` | 约束 γ-soft、shape coexistence 和 HD–ND 关系，但响应/协方差和装置成本更高 |
| 5 | g-factor、转移/反应选择性等 configuration-sensitive probes | `2/2/1 = 5` | 降低 orbital/configuration ambiguity，不能单独建立 partner electromagnetic symmetry |

这三个 8 分项并列时，identity/linking 是前置条件；最小可执行组合是 3 → 1 → 2，然后才进入 4 的形变问题。分数没有使用实验数据或模型拟合，只是将已有 locator 的“缺口—判别预测—可行性”显式化。

### 反证与判定

- AW13-11/AR-4 说明当前数据缺少寿命、绝对强度、偏振和直接形变测量；因此 priority 1–3 的高分来自 missingness 和 model-ranking sensitivity，而非已有信号强度。
- SI16-1、LI04-1/3 的寿命属于不同带/宇称范围，不能把它们直接当作 priority 2 已完成；PE98-7/PE98-13 的 HD `Q0` 也不能替代 HD–ND linking。
- 如果未来 measured `δ`/偏振仍支持普通 M1-dominant links，wobbling/chirality 权重应继续下降；如果 partner-resolved out-of-band E2 与 absolute strengths 显著增强，现有排序需 revision。若 linking 失败，则所有 partner-mode 分数都应降级为 identity-blocked。

**Continuation 4 decision: supports the experiment-design contract, no change to current scientific ranking.** 设计资产把开放问题转成可执行的最小测量组合，但没有新增实验事实、代理数据或 L4 拟合。

## Continuation 5: `131Ce` band/transition manifest contract

### 模板字段与主动回忆

上一块的 ordinal ranking 只有在字段、谱系和失败检查可复现时才有用。本 continuation 将其转成 manifest contract：每条 transition 必须同时携带 source lineage、band/level identity、`Eγ`/强度、multipolarity、measured 或假设的 `δ`、偏振、寿命/`Q_t`、linking、response/covariance 和模型输入。空字段保持 `missing`；模型 `γ`、邻核 proxy 或视觉印象不能填空。

### 设计交叉核验

| 字段 | 当前状态 | 可复用失败检查 |
|---|---|---|
| source lineage | AW13、SI16、LI04、PE98 可分开；Gizon blocked | DOI/raw hash/反应/阵列不全就停在 discovery；转载不重复计数 |
| band/level identity | AW13-1/AW13-2 provisional | parity conflict、duplicate configuration 或缺 linking 标为 `identity-uncertain` |
| transition observable | AW13-9 只有 `δ=0` 派生比值，direct `δ`/偏振 missing | 未释放 δ 假设或 polarization sign 未标定不得比较 |
| strength/lifetime | SI16/LI04 是非 partner controls，PE98-7 是 HD 扇区 | limits/effective/finite points 分开；不同 band/几何不合并 |
| linking/response/model | linking 部分存在，完整 common transition matrix、response/covariance/code 缺失 | 缺 identity 或 response 时禁止 mode label/L4 proxy fit |

最低可执行组合是 `source_lineage + band_level_identity + transition_observable + strength_lifetime + linking_identity`；`response_covariance` 缺失时最多进入 L3 readiness。这个模板把设计约束写成字段和失败条件，不声称已有数据满足这些字段。

### 反证与判定

- AW13-11、SI16-1/7、LI04-1/3 和 PE98-7/13 共同说明：现有数据能支撑谱学身份和 E2 collectivity controls，但不能组成同一 Bands 1–7 的 partner electromagnetic matrix。
- 如果未来 identity/linking 不闭合，priority 1–3 的信息增益同时降级；如果 δ/偏振闭合但 absolute strengths 缺失，只能更新 multipolarity/transition-character 层，不能宣称 wobbling/chirality。
- 如果 response/covariance/code 不可得，任何 L4 结果都必须停在 readiness boundary；不使用 proxy data 填补。

**Continuation 5 decision: supports the manifest contract, no new experimental claim.** `131Ce` 当前 mode ranking 不变；新增的是可直接交给未来数据或全文获取任务使用的字段 schema 和失败检查。

## Continuation 6: public-source manifest seed rows

### 选择与主动回忆

本 continuation 不再扩展缺失的 Gizon source，而是把已有公开 locator 映射为四条 manifest seed rows。每行只回答“来源已经知道什么、哪一列可填、哪一列仍 missing”；它不是 transition-level 数据表，也不替代未来事件级分析。

### Seed-row mapping

| seed row | 可填字段 | 明确缺失字段 | source lineage |
|---|---|---|---|
| `AW13-Bands1-7` | provisional band identity/linking（AW13-1/AW13-2）、`δ=0` 派生比值（AW13-9）、组态/模型标签 | measured `δ`、偏振、寿命、absolute strengths、response/covariance | `100Mo(36S,5n)` Gammasphere thesis；单一目标核谱系 |
| `SI16-131Ce-yrast` | 4 个有限寿命和 3 个限值（SI16-1）、部分 `Q_t`（SI16-2） | partner-resolved identity、direct `δ`/偏振、完整 interband matrix；TRS γ 是模型/解释（SI16-7） | 119Sn(16O,4n) 独立 yrast lifetime experiment；与 Li 行依赖关系显式保留 |
| `LI04-131Ce-parity-controls` | 正负宇称序列有限/限值寿命和 `Q_t`（LI04-1/LI04-3） | same-parity partner、direct δ/偏振；LI04-11 明确不是 chiral-doublet evidence | 116Sn(19F,p3n) 独立 DSAM；限值和 finite points 分开 |
| `PE98-131Ce-HD` | HD `Q0=7.3(4) eb`（PE98-7）和 separate-band scope（PE98-13） | HD–ND linking、共存混合、thesis Bands 1–7 partner mapping | 110Pd(28Si,α3n) GASP+ISIS；独立 HD 扇区 |

### Seed-row consistency checks

1. `AW13-Bands1-7` 的 `B(M1)/B(E2)` 不能与 `SI16`/`LI04` `Q_t` 直接拼接为同一 transition matrix；它们的 band、observable 和分析假设不同。
2. `SI16` Table 1 中转载 Li 的比较行仍属于 Li 谱系；seed rows 只保留原始实验独立性。
3. `PE98-131Ce-HD` 只提供形变尺度 control，不把 HD 带硬映射为 normal-deformed Bands 1–7。
4. 任何未来 row 若缺 response/covariance 或 transition-level locator，只能标记 `L3-ready`/`blocked-needs-source`，不能生成 L4 proxy。

**Continuation 6 decision: supports manifest usability, no scientific ranking change.** 四条 seed rows 让现有 locator 可直接转成未来数据输入，但所有决定性 companion columns 仍显式为空。

## Continuation 7: AW13 public-table transition rows

### 原始表格核验

对 Alwaleedi 原始 PDF 的 Tables 4.1–4.4 做了 Poppler text extraction，并核对表头、assignment 和相邻章节叙述。四条代表性表格行进入 source page 的 claims `AW13-14`–`AW13-17`，均保持 `needs_review: true`；它们提供 `Eγ`、相对强度和角强度比 `R`，不提供 measured `δ`、偏振或寿命。后续 DAY7 原文校正另把 Figure 4.5 的 505-keV link 加入 manifest 为 AW13-19；它不属于 Table 4.1–4.4 的这四条行。

| manifest row | `Eγ` / `Iγ` / `R` | source assignment | 缺失字段 |
|---|---|---|---|
| `AW13-B1-E2-507.9` | `507.9 keV / 100 / 0.94±0.02` | `15/2−→11/2−`, E2 | δ、偏振、寿命/absolute strength |
| `AW13-B1-M1E2-137.4` | `137.4 keV / 68.3±3.2 / 0.50±0.04` | `11/2−→9/2−`, M1/E2 | δ branch/sign、偏振、寿命/absolute strength |
| `AW13-B4-intraband-611.1` | `611.1 keV / 25.2±1.1 / 0.56±0.02` | Band 4 `17/2−→15/2−`, M1/E2 intraband transition | direct δ/偏振、lifetime/absolute strength |
| `AW13-B1-B4-link-505` | `505 keV`, identified in Figure 4.5 | Band 1–Band 4 link; endpoint spins/parities and multipolarity are not specified at this locator | endpoint mapping, `Iγ`/`R`, direct δ/偏振、partner matrix、response/covariance |
| `AW13-B7-E2-950.3` | `950.3 keV / 24.3±1.4 / 1.01±0.03` | `29/2−→25/2−`, E2 | measured δ/偏振、寿命/absolute strength |

### 交叉检查与边界

- Table 4.1/4.2 的 `R` 是 source-reported angular intensity ratio，在 manifest 中保留为观测字段；它不是跨阵列通用 multipolarity threshold，也不释放 AW13 的 `δ=0` 假设。
- Table 4.4 的 611.1-keV row 是 Band 4 偶内跃迁，不是带间 link；Figure 4.5 标示的 505-keV line 才是 Band 1–Band 4 连接，见 AW13-16/AW13-19。
- **2026-10-06 后续原文校正：** Day1 当时的 manifest 把 AW13-16 误当成带间 link。DAY7 按 Table 4.4（thesis p.66 / PDF p.70）与 Figure 4.5（thesis p.59 / PDF p.63）回核后已在 source/project 页修正；505-keV link 的多极性和端点自旋宇称仍未知。
- 这些 rows 仍使用 global relative intensities；不能把它们当作 Figure 5.5 gated branching inputs。`response_covariance` 和 event-level sorting code 仍 missing。

**Continuation 7 decision: supports manifest concreteness, limits interpretation.** 四条真实 PDF table rows 让 manifest 能开始接收公开数据，但没有新增 measured `δ`/偏振/寿命，不能改变当前 mode ranking，也不进入 L4。

## Continuation 8: AW13 angular-ratio subset cross-check

### 定量练习

从 AW13 Table 4.1/4.2 的前四条 Band 1 rows 计算 inverse-variance weighted means：

- E2 subset `R={0.94±0.02, 1.06±0.04, 1.30±0.09, 0.97±0.06}` 给出 `R_E2=0.976±0.017`，`χ²≈20.6`（3 d.o.f.）。
- M1/E2 subset `R={0.50±0.04, 0.50±0.04, 0.45±0.06, 0.61±0.05}` 给出 `R_M1/E2=0.516±0.023`，`χ²≈5.1`（3 d.o.f.）。
- 仅按表内统计误差的均值差为 `0.461±0.028`（约 16σ nominal）。这个 nominal significance 不能当实验结论：E2 子集自身的 dispersion、feeding、阵列几何、共同校准和未公开协方差没有进入计算。

### 判定边界

该交叉核算支持“AW13 表中 quadrupole 与 dipole-like assignment handles 在这组 rows 上明显分开”，但不提供跨阵列 `R` threshold、不释放 `δ=0`、也不独立证明每条 assignment 的 multipolarity。它适合作为 manifest 的 sanity check；若未来 transition-level δ/偏振与表中 `R` 冲突，应优先检查 gate、feeding、response 和 source assignment，而不是强行重写阈值。

**Continuation 8 decision: supports table-level sanity check, limits interpretation.** 没有新增 source claim 之外的实验事实、没有更新模式排序，也没有进入 L4；可复用计算和系统误差边界已写入 project。

## Continuation 9: table-level evidence saturation

AW13 Tables 4.1–4.6 的公开表格已经提供了当前可得的 assignment-handle 层；继续在相同 PDF 中寻找更多 `R` rows 不会补齐 measured `δ`、偏振、寿命或 response/covariance。现阶段的高信息增益只来自新的 transition-property 数据或新的合法原始来源。

**Continuation 9 decision: verified-no-op / evidence saturation at current source boundary.** 本块没有新增 canonical knowledge；既有 AW13 claims `AW13-14`–`AW13-17`、manifest rows 和 R sanity check 足以支撑表级边界，模式排序不变。下一轮若没有新 locator，应保持 verified-no-op，不重复扩展同一表格。

## Continuation 10: `131Xe` mechanism-control transfer boundary

### 邻核来源证据

[Chakraborty 2023 `131Xe`](../../knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md) 是与 `131Ce` 不重叠的机制控制来源。C23-2 报告连接跃迁的 `δ≈0.03(3)`, `0.09(8)` 和 `≈0`，C23-3 将小 E2 admixture/M1-dominant links 解释为 unfavoured signature partner，C23-7 明确本工作没有发现 wobbling 实验信号。TPRM/TPSM 的三轴参数是模型结果，不是直接 shape measurement。

### 可迁移 falsifier 与边界

- **可迁移：** 在候选带中，若连接跃迁稳定呈 M1-dominant 且 E2 admixture 很小，wobbling 的 E2-enhancement 判据应降权；这可作为 `131Ce` manifest 的 falsifier field。
- **不可迁移：** `131Xe` 的 δ、反应、阵列、band identity 和 model parameters 不能填入 `131Ce` rows；它只能说明方法判据的可行性。
- **当前目标核：** AW13 的 direct δ/偏振缺失仍未被 C23 替代；`131Ce` 的 ranking 继续保持 configuration/signature 首选、wobbling unsupported。

**Continuation 10 decision: supports transferable falsifier, limits cross-nucleus transfer.** C23 增强了 manifest 的 competing-prediction 字段，但没有新增 `131Ce` 实验事实或改变模式排序。

## Continuation 11: `131Xe`–`131Ce` manifest contrast

C23 与 AW13 的字段对照显示：`131Xe` 已有 target-specific δ/polarization/multipolarity evidence，可作为 falsifier protocol；`131Ce` 仍只有 δ=0 派生比值、provisional linking 和缺失 direct δ/polarization。可迁移的是测试条件（M1-dominant links 会削弱 wobbling assignment），不可迁移的是 C23 数值、反应、阵列、band identity 和 TPRM `γ`。

**Continuation 11 decision: supports protocol transfer, limits evidence transfer.** 对照增强了 `131Ce` manifest 的 competing-prediction 字段，但未新增目标核事实或改变模式排序。

## Continuation 12: `135Pr` branch-degeneracy method control

### 争议来源对照

- Matta M15-4/M15-5 报告 747/813/755-keV wobbling links 的大 `|δ|`、E2 fractions 和正 polarization asymmetry。
- Lv L22-3/L22-4/L22-5 显示 angular-distribution `χ²` 可保留大/小 `|δ|` 双解，联合 `P-R_ac` 选择小 `|δ|`、M1-dominant branch，并给出约 82–91% magnetic character。
- Guo GU21-2/GU21-3 进一步指出已报告 polarization sign 不能单独排除小 `|δ|`，且缺 calibration sensitivity/逐跃迁 `σ/I` 会削弱唯一解声明。

### 可迁移规则与边界

迁移到 `131Ce` 的只是方法规则：manifest 必须同时记录 angular-distribution branch、polarization magnitude/sign、`R_ac`、alignment/`σ/I`、detector response 和 branch covariance；单一拟合分支不能作为 wobbling/chirality 裁决。Matta/Lv/Guo 的 `135Pr` 数值、band identities、反应和阵列不得填入 `131Ce` rows。

**Continuation 12 decision: supports branch-degeneracy falsifier, no target-nucleus evidence change.** 该方法控制强化 `131Ce` δ/偏振 manifest 的失败检查，但不改变当前 `131Ce` mode ranking。

## Continuation 13: `135Pr` branch-degeneracy quantitative control

### 定量对照

- Matta M15-4/M15-5 报告 747/813/755-keV wobbling links 的大 `|δ|`、E2 fractions 和正 polarization asymmetry。
- Lv L22-3/L22-4/L22-5 显示 angular-distribution `χ²` 可保留大/小 `|δ|` 双解，联合 `P-R_ac` 选择小 `|δ|`、M1-dominant branch，并给出约 82–91% magnetic character。
- Guo GU21-2/GU21-3 指出 polarization sign 不能单独排除小 `|δ|`，缺 calibration sensitivity/逐跃迁 `σ/I` 会削弱唯一解声明。

这些数字不能直接合并为一个实验平均：Matta/Lv 使用不同反应、阵列和分析路线。可迁移的是 branch-aware manifest 规则：同时记录 angular-distribution branch、polarization magnitude/sign、`R_ac`、alignment/`σ/I`、response 和 covariance；未被联合观测选择的分支标为 `δ-ambiguous`。

**Continuation 13 decision: supports branch-aware manifest design, no target-nucleus evidence change.** `135Pr` 定量控制强化了失败字段，但未新增 `131Ce` 测量或改变现有排序。

## Continuation 14: `135Pr` branch-sensitive E2 fraction check

### 定量计算

按 source convention `δ=E2/M1`，用 `f_E2=δ²/(1+δ²)` 把报告的 mixing-ratio branches 转成 E2 fractions：

| 数据集 / 跃迁 | `δ` branch | `f_E2` | 来源与边界 |
|---|---:|---:|---|
| Matta 747.0 keV | `−1.24(13)` | `60.6(5.1)%` | M15-4 直接报告 |
| Lv 747.3 keV | `−0.47(+0.09/−0.22)` | central `18.1%`; endpoints `12.6–32.3%` | 由 L22-4/L22-5 small branch 计算；独立 JUROGAM II run |
| Matta 812.8 keV | `−1.54(9)` | `70.3(2.4)%` | M15-4 直接报告 |
| Lv 813.2 keV | `−0.37(+0.10/−0.14)` | central `12.0%`; endpoints `6.8–20.6%` | 由 L22-4/L22-5 small branch 计算 |
| Matta 754.6 keV | `−2.38(37)` | `85.0(4.0)%` | M15-4 直接报告；此处不配对 Lv 的 450-keV transition |
| Lv 450.2 keV | `−0.31(+0.10/−0.13)` | central `8.8%`; endpoints `4.2–16.2%` | 由 L22-4/L22-5 计算，是另一条连接跃迁 |

对 747/813-keV 近匹配跃迁，Matta 大 branch 与 Lv 小 branch 的 E2 fraction point estimates 明显不同。但两者来自不同 reaction/array/gating/analysis pipeline，不能合并成显著性检验或同一实验的误差比较；Guo GU21 comment 依赖 Matta 报告，不是第三个独立实验。结论是 branch choice 能显著改变 wobbling E2-link 判据，判别需要共同响应、polarization magnitude、`R_ac` 和 branch covariance。

### `131Ce` 迁移边界与决定

这项计算只把 branch-sensitivity 规则写入 `131Ce` manifest 设计：保留多个 δ branches，记录 polarization/`R_ac`/response 以便 future discrimination。不得将 `135Pr` δ、E2 fractions 或 band identities 填进 `131Ce` rows。

**Continuation 14 decision: supports branch-aware falsifier design, no `131Ce` evidence or ranking change.**

Matta M15-4 与 Lv L22-4/L22-5 的原子 locator、以及 Guo GU21-2/GU21-3 的双解/偏振边界已逐项对照各自 source page。Matta 的 747/813 keV 较大分支与 Lv 的近匹配小分支换算后得到明显不同的 E2 fraction；因为实验响应和分析流程不同，这只说明 branch choice 会改变判据，不能据此给出跨实验显著性或归因。`754.6 keV` 与 `450.2 keV` 未作为匹配跃迁比较。

## Knowledge Impact and Learning Decision

**Decision: supports + limits + revises。**

- **Supports：** Ding 2012 的实验直接事实、assignment handle、作者解释、模型结果和推断边界仍能组成 Day 1 的可复核四层契约；表 6.1 的能级—γ 线闭合也通过了逐项核算。
- **Limits：** ADO、能量简并、PES/NPA 相容和相邻带规则性都不能单独固定 `J^π`、组态、三轴形变、wobbling 或手征模式；必要 companion observables 仍是论文门槛。
- **Revises：** 144Ba/146Ba 对照把“直接矩阵元—相对 E1—模型 `β3`”的证据梯度具体化：E3 强度可持续而 E1 偶极矩变化，故不能用单一 E1 或 PES 印象替代绝对跃迁强度。
- **Governance repair：** 检查发现继承的 Day 2 模型选择卡已存在但未进入 `knowledge/index.md`；本轮只补了索引入口，没有改写模型卡内容或其 review 状态。
- **Continuation 1：** 为 [A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md) 增加了 `Model-to-observable locator crosswalk`，把 AFN90、HS10 和 D21 的原子 locator 与可测 observable、falsifier 和 L4 边界连起来；保持 `review_status: unreviewed`。
- **Continuation 2：** 为 [131Ce collective-mode project](../../knowledge/projects/131ce-collective-mode-discrimination.md) 增加 `131Ce electromagnetic-manifest audit (2026-09-27)`，将 AW13/SI16/LI04/PE98 的直接、派生、模型和缺失字段分层；Gizon 1977 仅记录为 blocked discovery route。
- **Continuation 3：** 复核 OpenAlex、Unpaywall、Semantic Scholar、ScienceDirect 和 CORE 获取状态；未取得全文，不新增科学 locator，继续保持 `blocked-needs-source`。
- **Continuation 4：** 为 [131Ce collective-mode project](../../knowledge/projects/131ce-collective-mode-discrimination.md) 增加 design-only 的 `next-measurement information-gain ranking`，保留 ordinal score 与实验事实的边界。
- **Continuation 10：** 为同一 project 增加 `131Xe mechanism-control transfer boundary (design-only)`，保留 C23-2/C23-3/C23-7 作为邻核 falsifier 逻辑，不迁移为 `131Ce` 目标核证据。
- **Continuation 11：** 为同一 project 增加 `131Xe–131Ce manifest contrast (design-only)`，明确测试条件可以迁移，数值和 band identity 不能跨核迁移。
- **Continuation 12：** 为同一 project 增加 `135Pr branch-degeneracy method control (design-only)`，保留 Matta/Lv/Guo 的双解与响应边界，不迁移 `135Pr` 数值。
- **Continuation 13：** 在同一 project 记录 `135Pr` E2-rich/M1-dominant branch contrast 与 branch-aware manifest fields，保持目标核证据边界。
- **Continuation 14：** 在同一 project 增加 `135Pr` branch-to-E2 fraction quantitative check；补齐 Matta/Lv/Guo source backlinks，区分近匹配 747/813-keV links 与不同的 450/754.6-keV transitions，不合并跨实验误差。
- **验收恢复（2026-09-28）：** 统一 `131Ce` project 中重复的 Matta/Lv/Guo `Sources` 行，仅保留一个来源入口并保留三个 source 链接；未新增科学结论，也未改变 review 状态。经用户明确授权，修复后报告/知识校验通过，Day 1 receipt 和 milestone state 恢复为完成/已计数；原始 usage-limit 与 backlink 失败均保留在恢复审计字段。
- **Continuation 5：** 为同一 project 增加 `131Ce band/transition manifest contract (design-only)`，把 identity、δ/偏振、寿命/强度、linking、response/covariance 和模型输入的空缺与失败条件固定下来。
- **Continuation 6：** 为同一 project 增加四条 public-source manifest seed rows，分别标记 AW13、SI16、LI04 和 PE98 可填字段及仍缺的 direct/partner/response 数据。
- **Continuation 7：** 在 AW13 source page 增加 `AW13-14`–`AW13-17` 四条原始表格 claims，并将对应 `Eγ/Iγ/R/assignment` 映射为四个 manifest transition seed rows；所有新 claims 保持 `needs_review: true`。
- **Continuation 8：** 对 AW13-14/AW13-15 的代表性 `R` 子集完成统计加权 sanity check，保留高 χ²、feeding、几何和协方差边界；未将 nominal 16σ 差异提升为实验 multipolarity结论。
- 复核没有设置 `human-reviewed`、没有清除任何 `needs_review`，也没有把模型结果写成实验事实。现有矩阵已覆盖 Ding 基线行；新颖性对照已有独立 source/synthesis 资产，向 A≈130 thesis matrix 重复写入不会增加信息增益。

## Durable knowledge delta

本轮的可复用训练产物是日报中的 `baseline-error-log`、128I 最小能级闭合、144Ba/146Ba 不对称误差练习、模型—观测可识别性设计表、`131Ce` electromagnetic manifest readiness audit、Gizon 1977 合法获取 blocker audit、next-measurement information-gain ranking、band/transition manifest contract、四条 public-source seed rows、四条 AW13 public-table transition rows、`R` 子集 sanity check、`131Xe` mechanism-control transfer boundary、`131Xe–131Ce manifest contrast`、`135Pr` branch-degeneracy method control 和 Matta/Lv branch-to-E2 fraction cross-check。它们指向的长期矩阵资产是 [knowledge/projects/a130-thesis-evidence-matrix.md](../../knowledge/projects/a130-thesis-evidence-matrix.md) 的精确 anchor **`Day 1 evidence contract (transferable baseline)`**、[A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md) 的 **`Model-to-observable locator crosswalk`**，以及 [131Ce collective-mode project](../../knowledge/projects/131ce-collective-mode-discrimination.md) 的 **`131Ce electromagnetic-manifest audit (2026-09-27)`**、**`131Ce` next-measurement information-gain ranking (design-only)**、**`131Ce` band/transition manifest contract (design-only)**、四条 seed-row mapping、AW13 table-row mapping、AW13 angular-ratio subset cross-check、`131Xe mechanism-control transfer boundary (design-only)`、`131Xe–131Ce manifest contrast (design-only)`、`135Pr` branch-degeneracy method control (design-only)、`135Pr` branch-to-E2 fraction cross-check 和 branch-aware quantitative control。矩阵行没有重复写入；模型卡和 `131Ce` project 分别保存模型 crosswalk、direct/derived/missing manifest、source-acquisition boundary、measurement priority、manifest schema、公开 seed rows、真实 PDF table rows、统计/系统误差边界以及邻核 branch/falsifier/contrast boundaries。

截止后对 canonical page [131Ce collective-mode project](../../knowledge/projects/131ce-collective-mode-discrimination.md) 的具体修订位于 `Branch-to-E2 fraction cross-check (design-only)`：删去重复的 `Sources` 行，保留 project 到 Matta、Lv、Guo source page 各一个链接和已核算的分支比例。对应原子 locator 为 Matta `M15-4`、Lv `L22-4`/`L22-5`、Guo `GU21-2`/`GU21-3`；没有把 Guo 对 Matta 的评论计为独立实验，也没有把 `135Pr` 数值迁移进 `131Ce` 数据行。

```knowledge-writeback
{
  "status": "updated",
  "reason": "The canonical Day 1 evidence-contract row and its atomic Ding locators were rechecked against the raw-backed source page. Continuations 1–13 added model/manifest design assets and neighboring controls; Continuation 14 repaired source backlinks and added an E2-fraction transformation for the reported Matta/Lv branches without pooling cross-experiment uncertainties or transferring values to 131Ce.",
  "items": [
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "Verified the existing Day 1 evidence contract: direct 127I/128I level and gamma observables remain separated from ADO-specific assignment, author interpretation, model results, and missing companion observables; the matrix remains unreviewed.",
      "anchor": "Day 1 evidence contract (transferable baseline)",
      "sources": [
        {
          "path": "knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md",
          "locator": "D12-1"
        },
        {
          "path": "knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md",
          "locator": "D12-7"
        },
        {
          "path": "knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md",
          "locator": "D12-9"
        },
        {
          "path": "knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md",
          "locator": "AR-2"
        },
        {
          "path": "knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md",
          "locator": "AR-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added the missing exact Projects index entry for the already-existing A≈130 high-spin model-choice card; no scientific page or review status was changed.",
      "anchor": "[[a130-model-choice-card]]",
      "sources": [
        {
          "path": "knowledge/sources/aberg-flocard-nazarewicz-1990-mean-field-shapes.md",
          "locator": "AFN90-1"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "Added a source-grounded model-to-observable locator crosswalk for mean-field/HFB, CSM/QTR and projected-shell-model routes, including discriminating observables and falsifier boundaries for 131Ce/A≈130 questions.",
      "anchor": "Model-to-observable locator crosswalk",
      "sources": [
        {
          "path": "knowledge/sources/aberg-flocard-nazarewicz-1990-mean-field-shapes.md",
          "locator": "AFN90-1"
        },
        {
          "path": "knowledge/sources/aberg-flocard-nazarewicz-1990-mean-field-shapes.md",
          "locator": "AFN90-4"
        },
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-1"
        },
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-4"
        },
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-5"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-1"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-4"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Added the 131Ce electromagnetic-manifest audit: AW13 delta-zero derived ratios, independent but non-partner lifetime/Q_t controls, the separate HD Q0 sector, and the blocked Gizon 1977 discovery route.",
      "anchor": "`131Ce` electromagnetic-manifest audit (2026-09-27)",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-9"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-11"
        },
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-1"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-1"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-11"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-7"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Added a design-only next-measurement information-gain ranking; ordinal scores prioritize identity/linking, measured delta plus polarization, and partner-resolved absolute strengths without treating the scores as experimental results.",
      "anchor": "`131Ce` next-measurement information-gain ranking (design-only)",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-9"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-11"
        },
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-1"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-1"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-3"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Added a design-only band/transition manifest contract with required identity, delta/polarization, lifetime/strength, linking, response/covariance and model fields plus failure checks.",
      "anchor": "`131Ce` band/transition manifest contract (design-only)",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-1"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-9"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-11"
        },
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-1"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-1"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Added four public-source manifest seed rows for AW13 Bands 1–7, Singh 131Ce yrast, Li parity-specific lifetime controls and Petrache HD, explicitly retaining missing direct delta/polarization/partner/response fields.",
      "anchor": "AW13-Bands1-7",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-1"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-9"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-11"
        },
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-1"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-1"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
      "summary": "Added four raw-PDF table claims AW13-14 through AW13-17 for representative Band 1, Band 4 link, Band 6/7 transition rows; each remains needs_review and keeps delta, polarization and lifetime gaps.",
      "anchor": "AW13-14",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Mapped four AW13 public-table transition seed rows into the manifest while retaining source-assignment and missing-companion boundaries.",
      "anchor": "AW13-B1-E2-507.9",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-14"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-15"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-16"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Added the AW13 angular-ratio subset sanity check with statistical-only weighted means and explicit high-chi-square, geometry, feeding and covariance limits.",
      "anchor": "AW13 angular-ratio subset cross-check (design-only)",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-14"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Added the 131Xe mechanism-control transfer boundary: C23 low-E2/M1-dominant links and no-wobbling conclusion are retained as a neighboring falsifier, not transferred to 131Ce evidence.",
      "anchor": "`131Xe` mechanism-control transfer boundary (design-only)",
      "sources": [
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-2"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-3"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Added a design-only 131Xe–131Ce manifest contrast that transfers falsifier conditions but keeps C23 values, band identities and model parameters nucleus-specific.",
      "anchor": "`131Xe`–`131Ce` manifest contrast (design-only)",
      "sources": [
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-1"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-2"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-7"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-1"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-9"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Added the 135Pr branch-degeneracy method control, preserving Matta/Lv/Guo double-solution and response boundaries without transferring 135Pr values to 131Ce.",
      "anchor": "`135Pr` branch-degeneracy method control (design-only)",
      "sources": [
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-4"
        },
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-5"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-3"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-4"
        },
        {
          "path": "knowledge/sources/guo-2021-comment-transverse-wobbling-135pr.md",
          "locator": "GU21-2"
        },
        {
          "path": "knowledge/sources/guo-2021-comment-transverse-wobbling-135pr.md",
          "locator": "GU21-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Removed the repeated Sources line while retaining the Matta/Lv/Guo backlinks and the branch-specific E2-fraction calculation; cross-experiment values remain unpooled.",
      "anchor": "Branch-to-E2 fraction cross-check (design-only)",
      "sources": [
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-4"
        },
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-5"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-4"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-5"
        },
        {
          "path": "knowledge/sources/guo-2021-comment-transverse-wobbling-135pr.md",
          "locator": "GU21-2"
        },
        {
          "path": "knowledge/sources/guo-2021-comment-transverse-wobbling-135pr.md",
          "locator": "GU21-3"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

- 对 `131Ce` Bands 1–7，最小可判别链是否必须同时包含能级放置、transition-level `δ`/偏振、partner-resolved lifetime/absolute `B(E2)` 与 `B(M1)`、带间 linking，以及在适用时的 g-factor 或转移选择性？若只有 `S(I)`、alignment 或 derived `B(M1)/B(E2)`，模式排序仍应保持 provisional。
- 对 `128I`，若未来寿命给出与高 K 小扁椭带不相容的 `B(M1)/B(E2)`，或偏振改变关键跃迁多极性，当前组态/集体解释应按 AR-4 触发 revision，而不以旧的能量闭合保护它。
- 对 `144Ba/146Ba`，直接 E3 与 E1 变化已支持“E1 不等于 E3”的修订；仍需在 parity splitting、寿命/绝对强度、可比的响应协方差和模型空间敏感性上区分静态八极形状、软八极关联与高自旋对齐解释。
- Gizon 1977 `131Ce/129Ce` 论文的 OpenAlex、Unpaywall、Semantic Scholar 和 publisher/repository 路线均已审计：身份可核验，但 OA/repository copy、abstract 和 locator 均不可得；若后续机构或作者提供合法全文，优先检查 angular-distribution、mixing-ratio 或 polarization 数据，否则保持 blocked discovery，不改变当前 manifest。
- [开放问题池](../../knowledge/questions.md) 已记录 Matta/Lv 对 747、813 keV 分支差异的未决问题。此处 E2 fraction 换算显示 branch choice 会明显改变电/磁成分的解释，但没有解释两数据集间差异来自何种响应、`σ/I`、angular-correlation 或 gate 条件。下一次实质研究应先对照原文的 transition identity、`P`、`R_ac` 定义和逐跃迁假设，并保留共同响应/协方差缺失边界。
- 本轮没有改变 A≈130 论文矩阵的行数或 review 状态；知识页变化是 `knowledge/index.md` 的缺失入口修复、模型选择卡的 locator crosswalk、`131Ce` project 的 manifest/design assets，以及 AW13 source page 的四条 raw-PDF table claims。它们都保留原有 `unreviewed` 边界，不把日报文字冒充成新的科学 claim。

## L0–L4 state

- **L0：** 运行身份、Day 1 卡片、路径契约、dirty baseline、raw/PLAN/BibTeX 保护边界和 DOI 身份核验完成。
- **L1：** 完成 `J^π`、`E_x`、γ 跃迁、level scheme、claim/locator/evidence level/source independence 的主动回忆和十二条错误分类。
- **L2：** 完成 Ding 2012 关键章节/图表主线复核、128I 能级闭合与两篇 Bucher 直接 E3 的不对称误差传播；实验事实、作者解释、模型结果和推断已分栏。
- **L3：** 形成 Ding 基线与 144Ba/146Ba 的跨质量区 evidence-contract 对照，用 AFN90/HS10/D21 建立模型—观测可识别性 crosswalk，完成 `131Ce` direct/derived/missing electromagnetic manifest、design-only measurement ranking、field-level manifest contract、四条 public-source seed rows、四条 AW13 raw-table transition rows、R sanity check、`131Xe` neighbor falsifier boundary、nucleus-specific manifest contrast、`135Pr` branch-degeneracy method control 和 branch-aware quantitative control，并确认 Gizon 1977 的 blocked-needs-source 状态；没有创建新的 A≈130 竞争模式结论。
- **L4：** `not-ready`。除现有 `131Ce` 寿命/派生结果外，仍缺同带事件级 transition-property matrix、探测器 response、校准协方差、可运行 sorting/GOSIA/SCCM code；不启动代理拟合。

## Verification and continuation

- 写入前与恢复后的 `python3 system/scripts/wiki_boundary_check.py --root .` 均 exit `0`；automation preflight exit `0`。
- 报告：[Day 1 日报](outputs/learning-daily/20260927-DAY1-baseline-research-contract.md)。唯一 `knowledge-writeback` block 为 `status: updated`；修复前恢复快照检查 valid，changed path 仅为 `knowledge/projects/131ce-collective-mode-discrimination.md`。project 中 Matta、Lv、Guo 三个来源页各保留一个链接，原子 locator 为 `M15-4`、`L22-4`、`L22-5`、`GU21-2`、`GU21-3`。
- `python3 system/scripts/wiki_lint.py --fail-on error` exit `0`：`SUMMARY pages=534 wikilinks=4857 hashes=246 errors=0 warnings=81 info=1124`。剩余 warning 类别：`CITATION_KEY_MISSING=76`、`REACTION_PARSE=3`、`ORPHAN_PAGE=1`、继承工作树产生的 `RAW_GIT_CHANGE=1`；raw 未修改。runner 同口径 `--no-git` lint exit `0`。
- `git diff --check` exit `0`。日报所有必需标题齐全；新增 AW13 source claims 仍为 `needs_review: true`，没有设置 `human-reviewed`。
- 用户明确授权恢复后，原 receipt 从 `failed-verification` 改为 `completed` 并计入 Day 1；原始 Continuation 14 exit `1` 和 usage-limit 原因未删除，而是保存在 `original_*`/`recovery` 字段中。`2026-09-one-month-state.json` 的 `next_day_index` 更新为 `2`。scheduler JSONL 追加了 `runner-recovered` 事件，原始 `runner-finished/failed` 事件保留。
- runner 已用正式 helper 生成 [Day 2 prompt](prompts/20260928-DAY2-shell-gap-single-particle.md)；本 run 的 [continuation prompt](20260927-DAY1-baseline-research-contract-run-01/continuation-prompt.md) 记录恢复路径。Day 1 基线考试、证据矩阵和设计/反证练习均已交付；`135Pr` 分支差异与 Gizon 1977 全文仍是研究开放问题，可从 question pool 后续推进。
- 未暂存、未提交、未推送；未修改 raw、PLAN、受保护 BibTeX 或既有 review 状态。
