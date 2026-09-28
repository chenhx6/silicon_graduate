---
type: learning-daily
run_id: 2026-09-25-day-01-01
run_date: 2026-09-25
day_index: 1
phase: baseline-and-research-contract
cycle: 2026-09-30-day-substantive
schedule_id: wiki-daily-learning
schedule_name: Wiki 30-day substantive daily learning
run_kind: substantive
acceptance_only: false
review_status: ai-draft
session_id: 01a0d794-6454-7563-bac1-3b5ad970edda
---

# 2026-09-25 Day 1：基线考试与研究契约

## Run state

- 本轮执行正式 30 天周期的 Day 1，主题为“基线考试与研究契约”。开始时状态文件仍为 next_day_index: 1；是否计数由 runner 的最终报告、写回、lint 和 diff 门统一决定。
- 启动时保留了继承的 dirty baseline：knowledge/projects/a130-thesis-evidence-matrix.md、system/handoff.md 以及其它用户/上一轮文件没有被覆盖；raw/、PLAN.md 和受保护的 raw/zotero/wiki-inbox.bib 未修改。
- 写入前执行 python3 system/scripts/wiki_boundary_check.py --root .，退出码为 0，路径契约无 error/warning。
- 当前 CLI session：01a0d794-6454-7563-bac1-3b5ad970edda。可恢复命令：codex resume 01a0d794-6454-7563-bac1-3b5ad970edda -C /workspace/wiki -s danger-full-access -a never。

## Candidate pool and selection

候选池由 [knowledge/questions.md](../../knowledge/questions.md)、现有 [A≈130 论文证据矩阵](../../knowledge/projects/a130-thesis-evidence-matrix.md)、最近的 [2026-09-24 acceptance-only 记录](2026-09-24.md)、[Day 1 任务卡](../../outputs/plans/2026-09-22-one-month-daily-task-matrix.md#day-1--基线考试与研究契约)、[一个月 CLI 训练计划](../../outputs/plans/2026-09-22-one-month-codex-cli-apprenticeship.md) 和 [A≈130 三轴论文管线](../../outputs/plans/2026-09-22-a130-triaxial-thesis-pipeline.md) 重建。

- **连续性槽位：** 131Ce 的集体模式判别契约。当前 Wiki 仍缺少能把 signature/configuration coupling、γ-soft response、wobbling、chirality 和 shape coexistence 分开的完整 companion-observable 链。
- **新颖性槽位：** Ding 2012 的 127,128I 高自旋实验作为可迁移的证据分层锚点。它同时包含符合、能量闭合、ADO、自旋宇称指认和 PES/NPA/经验壳模型比较，能检验“观测—assignment—解释—模型—推断”链条。
- 选择 Ding 作为 Day 1 训练锚点的理由是信息增益集中在研究契约，而不是再凑论文数。该来源是一个学位论文实验谱系；同一论文中的模型和实验不计作独立复制，不能把重复引用当成独立证据。

主动回忆（重新打开来源前）：

1. J^π 是自旋与宇称的状态标签，不能由一条能量或规则间隔自动推出。
2. 激发能 E_x 是相对参考态的能量；能级纲图是“态—跃迁”的图，而不是模型势能面。
3. γ 能量、符合关系、强度/能量平衡和 ADO 是观测或派生观测；claim 还必须有 claim kind、locator、evidence level 和 source-independence。
4. 作者的 band/configuration 标签、PES/NPA 输出与 Codex 对缺失 companion observable 的判断必须分开。
5. 本次回忆中最初把 ADO 当成跨实验通用的多极性阈值，复核 AR-2 后更正为阵列、角度、alignment、feeding 和标定依赖的局部判据。

## Sources and evidence

### 主来源与定位

- [Ding 2012：127,128I 高自旋能级结构](../../knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md)。原始文件为 raw/papers/degree dissertation/丁兵 - 博士论文.pdf，SHA-256 为 ca7765ad962ea0c106791532f5a7d9f359533d25bb0170f03197bfec414be5c7；source 页保持 status: ai-draft、review_status: unreviewed，所有 claim 的 needs_review: true 不变。
- 我沿 PDF 主线复核了实验反应/阵列与 ADO 设定（PDF pp.57–60，打印 pp.49–52）、127I Fig.5.2/Table 5.1（PDF pp.59–63）、128I Fig.6.2/Table 6.1（PDF pp.69–71）、NPA 与经验壳模型比较 Fig.6.6/Table 6.1（PDF pp.74–76）以及带系统学和模型边界（PDF pp.76–91）。图 6.2 的原始能级连接、箭头强度和 A/B/C 分区与表 6.1 的数值相互核对。
- **实验直接事实：** 32 MeV 124Sn(7Li,4n)127I 建立 75 个能级、近 150 条 γ 跃迁并给出 ADO（D12-1）；128I 建立 20 个能级、31 条跃迁的新高自旋纲图（D12-7）；表 6.1 记录每条线的 Eγ、相对强度、R_ADO 和初末能级。
- **作者解释：** 127I 正宇称序列的高-K/旋称分支和 128I 285.2 keV 8− 带头的 πg7/2⊗νh11/2 指认，分别由序列、连接跃迁和邻核系统学支持（D12-2、D12-3、D12-9）。这些是作者的结构解释，不是单个 γ 能量的直接测量。
- **模型结果：** PES 的浅而 β/γ 柔软势能面及三准粒子候选（D12-6）、NPA 对 6−/7− 顺序和 8− 组态的比较（D12-8）、正宇称两准粒子多重态能量偏差（D12-10）都保留为 model-result，不能写成实验直接测得的形变或组态。
- **证据边界：** ADO、符合和内转换可以约束部分多极性与放置，但依赖阵列和分析条件（AR-2）；原实验没有寿命和线偏振，也没有直接 Q_t 或 B(E2)（AR-4 及 source 页 coverage caveat）。[Spin/Parity Assignment 方法页](../../knowledge/methods/spin-parity-assignment.md)也明确要求把序列逻辑与角分布、DCO、偏振、转换或寿命等至少一个 transition-property handle 分开记录。

### 12 条基线陈述分类（baseline-error-log）

| 编号 | 陈述 | 分类 | 证据层/定位 | 纠错要点 |
|---|---|---|---|---|
| B1 | 表 6.1 记录 411.0 keV γ 线从 696.2 到 285.2 keV。 | 实验直接事实 | direct；D12-7、Table 6.1 | 能量和初末态可直接读表；不是多极性结论。 |
| B2 | 101.3→764.7→411.0→102.2 keV 是一条被符合与能量加和支持的级联。 | 实验直接事实 | direct；D12-7（PDF pp.72–73） | 级联次序来自符合/加和，仍需保留污染和门条件。 |
| B3 | E_x(9−)-E_x(8−)=696.2-285.2=411.0 keV。 | Codex 可复核计算 | derived from D12-9、Table 6.1 | 算术只验证放置闭合，不独立测量 J^π 或组态。 |
| B4 | R_ADO(411.0)=0.65(5)。 | 实验直接事实 | direct；D12-7、Table 6.1 | 这是本阵列的比值，不能直接移植成通用阈值。 |
| B5 | 411.0 keV 因而必然是唯一的 M1 跃迁。 | 过强推断（错误） | D12-7、AR-2 | ADO 还受 ΔI=0/2、alignment、feeding 和几何影响，不能单独给唯一答案。 |
| B6 | 285.2 keV 态被作者建议为 8−。 | 作者解释/assignment | direct-supported；D12-9 | “建议为”要保留 source wording，不能写成无条件实验事实。 |
| B7 | 285.2 keV 8− 的 πg7/2⊗νh11/2 是直接测得的组态。 | 过强推断（错误） | D12-8、D12-9 | 组态由 NPA、经验壳模型和系统学共同约束；模型输出不是直接观测。 |
| B8 | NPA 重现了部分低位多重态间隔趋势。 | 模型结果 | model-result；D12-8 | 可以支持模型相容性，不能取代独立组态观测。 |
| B9 | NPA 的部分 6−/7− 顺序与实验相反，8− 落在两个理论候选之间。 | 模型—实验边界事实 | direct comparison；D12-8 | 这是反证/限制，提醒不要把“能量相近”当唯一指认。 |
| B10 | 2901.2 keV 态的 23/2+ 指认包含 E1/M2 强度量级排除负宇称的作者论证。 | 作者解释 | direct-supported；D12-4 | 论证依赖跃迁极性、强度和选择定则，仍非一项单独测量。 |
| B11 | PES 给出的浅 β/γ 势能面就是实验测得的三轴形变。 | 过强推断（错误） | D12-6、AR-2 | PES 是模型输出；需寿命、绝对强度、Q_t 等 companion observables。 |
| B12 | 这项实验没有寿命/线偏振/直接 Q_t 或 B(E2)，因此集体模式结论存在缺口。 | 实验方法事实 + Codex 证据推断 | AR-4、source coverage caveat | 缺口本身是事实；“因此哪些模式仍不可区分”是本任务推断。 |

这 12 条形成个人 baseline-error-log：主要错误是把 assignment 当 measurement、把模型输出当观测、把阵列特定 ADO 当普适阈值，以及把能量闭合误当作模式判别。

## Theory/analysis exercise

### 最小 128I level scheme 与重算

用 [Ding source 页的 D12-9 与 Fig.6.2/Table 6.1](../../knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md) 重建带 B 的最小级联：

\[
8^-_1(285.2)
\xleftarrow[411.0]{\gamma}
9^-(696.2)
\xleftarrow[345.4]{\gamma}
10^-(1041.7)
\xleftarrow[412.3]{\gamma}
11^-(1454.0)
\xleftarrow[419.5]{\gamma}
12^-(1873.5)\ \mathrm{keV}.
\]

逐项核算（表内四舍五入造成 0.1 keV 差异）：

- 696.2-285.2=411.0 keV；
- 1041.7-696.2=345.5 keV ≈ 345.4 keV；
- 1454.0-1041.7=412.3 keV；
- 1873.5-1454.0=419.5 keV。

这验证了能量放置的闭合和图表的一致性；它没有独立验证自旋宇称、组态或转动/三轴模式。表 6.1 的同一阵列还给出 R_ADO=0.65(5)（411.0 keV）、0.73(5)（412.3 keV）和 0.81(6)（419.5 keV）。论文正文明确提醒，ADO 不能在某些情形区分四极 ΔI=2 与偶极 ΔI=0；因此这些数值只能作为本实验条件下的 assignment handle。

### 四层证据表

| 层级 | 本轮可复核对象 | 可以说什么 | 不能说什么 |
|---|---|---|---|
| 实验直接事实 | γ 能量、符合、相对强度、能量和、R_ADO、内转换系数 | 线存在、路径和放置受数据支持 | 不能单独给唯一 J^π、组态或形变 |
| 作者解释 | 高-K、退耦/旋称分支、πg7/2⊗νh11/2 | 记录作者如何把多项观测组合成 assignment | 不能改写为无条件事实 |
| 模型结果 | PES、NPA、经验壳模型能量与势能面 | 检验模型与能级/系统学是否相容 | 不能把 β、γ 或组态当直接测量 |
| Codex 推断 | 缺少 mixing ratio、偏振、寿命、绝对强度和独立链接 | 明确下一项最有信息量的观测 | 不能补造数据或清除 needs_review |

## Counter-evidence and missing companion observables

1. **模型反证：** D12-8 记录 NPA 的部分 6−/7− 顺序与实验相反；实验 8− 位于两个理论 8− 候选之间。一次计算能量接近不能唯一锁定组态。
2. **观测判据反证：** AR-2 说明 ADO 是阵列和分析条件特定的量；D12-7 表 6.1 中相近能量线的 ADO 与符合路径并不等于唯一多极性。
3. **必要 companion observables：** 对 J^π/多极性应补 transition-level mixing ratio、线偏振和必要的转换系数；对集体性应补寿命、绝对 B(E2)/B(M1) 或 Q_t；对组态和模式竞争应补独立带间 linking、转移/反应选择性，必要时补 g-factor。
4. **共享谱系边界：** Ding thesis 的实验事实、作者解释和模型比较来自同一论文/同一实验线；[Spin/Parity Assignment 方法页](../../knowledge/methods/spin-parity-assignment.md)是 Wiki 方法归纳，不是独立复现实验。不能把它们计为多个独立来源。
5. **L4 边界：** 当前没有事件级数据、探测器响应、协方差、校准和可运行分析代码；因此只做能级和算术复核，没有生成 proxy fit 或伪结果。

## Knowledge Impact and Learning Decision

**Decision: supports and limits.**

- **Supports：** 现有证据矩阵的四层契约得到一条可复核的 128I 级联、ADO 约束和模型/实验边界支持。
- **Limits：** 本轮没有独立的新实验谱系，也没有足以判定 131Ce 集体模式的 companion observables；不改变既有模式排序。
- 矩阵已有 Day 1 行，source 页和 review 状态也完整；在不重复写入同一行的前提下，本轮把 12 条错误类型、能量重算和表/图复核保留在日报，并将知识页写回判定为 grounded verified-no-op。未设置 human-reviewed，未清除任何 needs_review。

- **Continuation 1 decision: revises and limits.** Liu 的系统学支持“修订 I0 后可得到一致的 inversion pattern”，但 odd-ΔI crosswalk 和未决 Cs 参考说明 signature/γ-shape 解释仍依赖自旋锚点。

- **Continuation 2 decision: supports and limits.** Ma 的直接角分布/DCO/δ 与 Table II 系统学支持 alignment 是可检验的 shape-driving 机制；TRS γ 极小值、未决带和缺少寿命/绝对强度限制了固定形变或集体模式结论。

- **Continuation 3 decision: supports and limits.** Alwaleedi 的 crossing 和 branching-derived B(M1)/B(E2) 支持组态相容性练习；δ=0、g/alignment/Q0 输入和绝对强度缺失限制其对集体模式的判别力。

## Durable knowledge delta

本 continuation 新增 131Ce 的派生强度/δ=0 evidence bridge，并保留 Liu 与 Ma 两行。canonical page 为 [knowledge/projects/a130-thesis-evidence-matrix.md](../../knowledge/projects/a130-thesis-evidence-matrix.md)：

- anchor **A≈130 πh11/2⊗νh11/2 signature-inversion crosswalk**：spin-anchor conditional。
- anchor **131Ba competing-alignment evidence bridge**：Table I/II 的 alignment、角分布、DCO、δ 和 crossing/splitting 边界。
- 新 anchor **131Ce derived-strength and delta-zero evidence bridge**：Equation 5.6–5.7、Table 5.4 的派生输入、δ=0 敏感性和缺失绝对强度/寿命。
- 三个 anchor 均保持矩阵 page review_status: unreviewed；source 的既有 review 状态未被提升或清除。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "Retained the Liu signature-inversion crosswalk as conditional on independent spin anchors.",
      "anchor": "A≈130 πh11/2⊗νh11/2 signature-inversion crosswalk",
      "sources": [
        {
          "path": "knowledge/sources/liu-1996-signature-inversion-a130.md",
          "locator": "LU96-1"
        },
        {
          "path": "knowledge/sources/liu-1996-signature-inversion-a130.md",
          "locator": "LU96-2"
        },
        {
          "path": "knowledge/sources/liu-1996-signature-inversion-a130.md",
          "locator": "LU96-3"
        },
        {
          "path": "knowledge/sources/liu-1996-signature-inversion-a130.md",
          "locator": "LU96-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "Retained the 131Ba competing-alignment bridge with source-specific angular, DCO, mixing and N=75 systematics boundaries.",
      "anchor": "131Ba competing-alignment evidence bridge",
      "sources": [
        {
          "path": "knowledge/sources/ma-1990-131ba-competing-alignments.md",
          "locator": "MA90-1"
        },
        {
          "path": "knowledge/sources/ma-1990-131ba-competing-alignments.md",
          "locator": "MA90-2"
        },
        {
          "path": "knowledge/sources/ma-1990-131ba-competing-alignments.md",
          "locator": "MA90-3"
        },
        {
          "path": "knowledge/sources/ma-1990-131ba-competing-alignments.md",
          "locator": "MA90-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "Added the 131Ce derived-strength and delta-zero bridge with the Equation 5.6–5.7 input chain, Table 5.4 model inputs and missing absolute-strength boundary.",
      "anchor": "131Ce derived-strength and delta-zero evidence bridge",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-5"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-9"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-10"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-11"
        }
      ]
    }
  ]
}
```



## Open questions and belief revision

- 对 131Ce 或相邻 A≈130 候选带，最小可判别链是否必须同时包含：能级放置、transition multipolarity/mixing ratio、偏振、寿命、绝对强度和带间 linking？
- Liu 1996 新增一个前置问题：若候选带的 I0 只来自平滑系统学，什么独立观测能防止奇数 ΔI 重排把 signature 或 γ-shape 解释整体翻转？
- Ma 1990 新增 alignment 设计问题：在同一 reference convention 下，能否用 crossing、signature、已定 multipolarity 的 linking 与 lifetime/absolute strength 区分 proton/neutron alignment、γ-soft mixing 和普通 signature partner？
- Alwaleedi 2013 新增派生量问题：在 δ、lifetime 和 Q0 均不闭合时，B(M1)/B(E2) 曲线的哪一部分仍能改变 131Ce 模式排序？
- 哪一个单独缺失的 companion observable 最可能改变 γ-soft 与 wobbling/chirality 的相对排序？当前没有数据支持先验指定。
- Belief revision：Ding 的 placement/ADO 契约得到支持；Liu 使 signature/γ-shape 判断变为 spin-anchor conditional；Ma 支持 alignment 作为可检验机制；Alwaleedi 说明 derived B(M1)/B(E2) 只有在 δ=0、g/alignment/Q0 和 band mapping 边界同时显式保留时才可用于组态相容性，不能独立裁决集体模式。
- 最高信息增益的后续路线：以 [Ding et al. 2021 131Ba/133Ce signature splitting](../../knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md) 检查低-j Coriolis mixing 与 γ 非轴性的竞争解释，避免把 Ma/Alwaleedi 的 splitting 单变量解释当成定论。

## Continuation 1 — A≈130 signature-inversion crosswalk

### Candidate update and active recall

Day 2 的 HJS49/RS78 壳隙桥已经有 canonical page [[a130-shell-gap-orbital-observable]]，重复同一闭壳层容量算术不会增加信息。本 continuation 改选 A≈130 的独立系统学来源 Liu et al. 1996，问题是：当 bandhead 自旋 I0 只由能量系统学间接约束时，signature inversion 和 γ 形变解释能否被视为稳健观测？

主动回忆结果：

- signature splitting 需要先固定同一组态的自旋序列，再比较相邻自旋的能量差；I0 改变奇数 ΔI 会重标记 favored/unfavored signature。
- 由能量曲线得到的 inversion spin 是系统学量，不等于直接测得的 γ 角或三轴形状。
- particle–triaxial-rotor 与数据趋势相容只能说明模型在给定 I0、残余相互作用和参数下可行；不能替代独立自旋、mixing ratio、寿命或绝对强度。

### Source and evidence

- 主来源是 [Liu et al. 1996 signature-inversion source page](../../knowledge/sources/liu-1996-signature-inversion-a130.md)，DOI [10.1103/PhysRevC.54.719](https://doi.org/10.1103/PhysRevC.54.719)，原始 PDF 为 raw/papers/gpt/high-spin-20260920/旋称/1996_Liu et al_Systematic study of spin assignments and signature inversion of π h 1 1 - 2 ⊗ν.pdf，SHA-256 ca3e1c1bc834158112dee525fa4c42c3d44596975a506f3a2a1da023580a346f。source 页仍为 review_status: unreviewed，claim-level needs_review 保留。
- 这是 compiled literature systematics，不是一次新的独立谱学实验；原始 La/Pr/Pm/Eu/Cs 实验是依赖输入。论文明确把“平滑激发能曲线 → 修订 I0 → signature inversion”作为方法先验（LU96-1），并把 particle–triaxial-rotor 比较放在修订后的 spin crosswalk 之后（LU96-3）。
- 视觉复核了 PDF p.720 的 Table I、p.728 的 Fig. 15 和 p.729 的讨论。Fig. 15 的纵轴是 [E(I)-E(I-1)]/(2I)，单位为 keV/ℏ；实心/空心点分别表示作者定义的 favored/unfavored signatures，箭头标出 inversion point。PDF p.723–725 的 Table II/逐条讨论保留 Cs 的多个参考 I0 方案（LU96-4）。

### Quantitative reconstruction

我把 Table I 的 14 行 La/Pr/Pm/Eu 记录转成显式计数：

- 14 个核素行中，13 行已有 previous I0；其中 11 行的 present I0 与 previous I0 相差奇数 ΔI（126La: 4→7、130La: 6→9、132La: 8→9、134La: 8→9、130Pr: 8→7、132Pr: 8→9、134Pr: 8→9、136Pr: 8→9、136Pm: 8→9、138Pm: 8→9、138Eu: 8→9），其余两行保持不变。
- Table I 的 present 列把这 14 行都列为 low-spin signature inverted；因此“全体反转”依赖 revised I0，而不是 14 个独立的直接自旋测量。
- 我用 Fig. 15 的归一化定义做了透明算术检查：若相邻能级为 E(10)=500.0、E(11)=512.0、E(12)=526.0 keV，则 [E(11)-E(10)]/(2×11)=0.545 keV/ℏ，[E(12)-E(11)]/(2×12)=0.583 keV/ℏ。这只是公式和单位的 sanity check，不是 Liu 数据的新拟合。
- Table I 中能同时给出实验与 Tajima inversion spin 的少数条目并不逐点相等（例如 126La present 21.5 对计算 13.5，128La ≥23.5 对 15.0，134Pr 17.5 对 18.5）；因此可保留的支持是 inversion 的定性模式和随中子数变化的趋势，不能宣称精确数值验证。
- Cs 的 Table II 更直接显示识别边界：以 124Cs I0=7、130Cs I0=9 或 130Cs I0=11 为参考会给出不同全链自旋；论文结论是这些参考选择不能同时正确（LU96-4），不是一个已解决的 spin assignment。

### Evidence-layer interpretation

| 层级 | Liu 1996 能支持的内容 | 不能支持的内容 |
|---|---|---|
| 资料/系统学事实 | 既有能级资料、Table I/II 的 previous/present I0、Fig.15 的归一化曲线和 inversion 标记 | 把 compiled values 当成一次新实验的原始观测 |
| 作者方法与解释 | 平滑激发能系统学可作为修订 I0 的工作准则；修订后低自旋 signature inversion 更系统 | 把平滑性先验当作独立自旋测量 |
| 模型比较 | particle–triaxial-rotor 在给定 spin crosswalk 后可重现实验趋势（LU96-3） | 唯一 γ、三轴刚性或集体模式的直接证明 |
| 本任务推断 | 自旋锚点是 A≈130 signature/形变判断的前置 companion observable | 不能把 signature inversion 单独升级为 wobbling、chirality 或固定 γ 形变证据 |

## Counter-evidence and missing companion observables

- **最强反证是自旋依赖性：** 论文自己指出，bandhead 自旋错一个奇数会反转 signature order，并可能改变此前 γ-deformation 的符号讨论；这使能量系统学解释具有结构性脆弱点，而不是小的统计误差。
- **Cs 未决边界：** 124Cs I0=7 与 130Cs I0=9/11 的交叉参照不能同时满足平滑曲线（LU96-4）。在新的自旋锚点出现之前，Cs 的 inversion trend 不能作为已闭合证据。
- **缺失的必要观测：** 需要 nucleus-specific 的已定自旋/宇称锚点、transition multipolarity/mixing ratio、线偏振或寿命、绝对 B(E2)/B(M1)/Q_t，以及能把候选带身份锁定的 linking transitions。Liu 论文没有直接 δ/lifetime 数据，source 页也明确禁止把 γ-shape inference 转移给 131Ba/131Ce（LU96-AR-3）。
- **源独立性：** Liu 的表格汇编、原始谱学论文和 particle–triaxial-rotor 计算构成依赖链；即使 Table I 有 14 个核素，也不能计为 14 个独立实验复现。
- **与 Day 1 契约的关系：** 这项结果把“assignment handle 不是 measurement”的规则推进一步：即使能级曲线很平滑，先验本身也可能重排 signature 和 γ 解释；因此对 131Ce 必须先闭合 spin/multipolarity，再谈模式。



## Continuation 2 — 131Ba alignment, signature and transition observables

### Candidate selection and active recall

本 continuation 选择 Ma et al. 1990 的 131Ba 原始实验，因为它与 Liu 的 compiled spin crosswalk 不重叠，直接提供 alignment、角分布、DCO 和 mixing ratio。问题是：**proton/neutron alignment 是否能把 signature splitting 的变化与固定三轴形变区分开？**

主动回忆：

- alignment 是准粒子角动量沿转轴的响应；crossing frequency 依赖旋转参考、配对和轨道占据。
- A₂/A₀、A₄/A₀ 和 DCO 是实验分析量；混合比 δ 还依赖 alignment、有限探测器修正和 phase convention。
- TRS/CSM 的 β、γ 极小值是模型输出；只有与 crossing、signature、multipolarity 和必要电磁强度一起使用时，才可作为结构解释的候选。

### Source and evidence

- 主来源为 [Ma et al. 1990 131Ba source page](../../knowledge/sources/ma-1990-131ba-competing-alignments.md)，DOI [10.1103/PhysRevC.41.717](https://doi.org/10.1103/PhysRevC.41.717)，原始 PDF 为 raw/papers/gpt/high-spin-20260920/形变/1990_Ma et al_Competing proton and neutron rotational alignments.pdf，SHA-256 a0dbdd4957d1d11af570b5daffc9c44609d9ef5ed570dc3ad32a67388dad90de。source 页仍是 review_status: unreviewed。
- 实验直接事实：119Sn(12C,4n) 反应，57 MeV，五个 Compton-suppressed Ge，约 60 million coincidence events；Fig.1 建立十条带，1–6 为 ΔI=1 双 signature 序列，7–10 为 decoupled ΔI=2 结构（MA90-1；PDF pp.718–725）。
- PDF p.719 给出角分布拟合式 W(θ)=A₀+A₂P₂(cosθ)+A₄P₄(cosθ)，带 1 的平均 alignment 参数为 a₂=0.59(7)、a₄=0.20(2)，其它带为 a₂=0.75(6)、a₄=0.40(2)。这些是分析输入，不是形变角。
- Table I（PDF pp.720–722）直接列能量、相对强度、A₂/A₀、A₄/A₀、DCO 和 assignment/mixing。560.0 keV 的 band-6 ΔI=1 线为 A₂/A₀=−0.73(4)、A₄/A₀=0.06(6)、DCO=0.26(1)、M1/E2，δ=−0.42(9)；784 keV 的 stretched E2 与它的强各向异性对照（MA90-4 的 detector/alignment boundary）。
- Table II（PDF p.727）给出 N=75 的 crossing 和 signature splitting。131Ba 的两个 proton signature crossing 为 0.445(3) 与 0.415(3) MeV，νh11/2 低自旋 splitting 为 0.160(5) MeV，proton-aligned configuration 的 post-crossing splitting 为 −0.005(5) MeV。133Ce、135Nd、137Sm、139Gd 的 crossing 和 splitting 也在同表中。
- Fig.6（PDF p.726）是 TRS 模型输出：在约 0.41 MeV，νh11/2⊗[πh11/2]² 与 [νh11/2]³ 的两个 minima 分别位于约 γ=+26° 和 γ=−82°；这支持 opposite shape-driving 的模型图像，但不是直接 γ 测量。Fig.7（PDF p.727）显示 N=75 链中 proton crossing 随 Z 增大下降。

### Quantitative reconstruction and design check

我从 Table II 逐行重算了两个 signature crossing 的平均值和差值；误差只传播表中独立的 ±0.003 MeV 数字误差，未包含可能的共同系统误差：

| Nucleus | mean crossing (MeV) | α−−α+ (MeV) | low-spin splitting (MeV) | post-crossing splitting (MeV) |
|---|---:|---:|---:|---:|
| 131Ba | 0.4300±0.0021 | 0.030±0.004 | 0.160±0.005 | −0.005±0.005 |
| 133Ce | 0.3685±0.0021 | 0.019±0.004 | 0.120±0.005 | 0.000±0.005 |
| 135Nd | 0.3270±0.0021 | 0.018±0.004 | 0.115±0.005 | 0.000±0.005 |
| 137Sm | 0.2900±0.0021 | 0.012±0.004 | 0.110±0.005 | 0.015±0.005 |
| 139Gd | 0.2890±0.0021 | 0.008±0.004 | 0.095±0.005 | 0.015±0.005 |

由此得到三个可复核结果：

1. 131Ba→139Gd 的平均 proton crossing 下降约 0.141 MeV，低自旋 νh11/2 splitting 下降 0.065 MeV；post-crossing splitting 从 −0.005 增至 +0.015 MeV。这支持沿 N=75 链 shape-driving 背景发生变化的实验趋势，但不是唯一的 γ 轨迹。
2. 131Ba 的 α−−α+ = 0.030±0.004 MeV，而 139Gd 为 0.008±0.004 MeV；该差值在表内误差下明显减小，但共同校准/参考误差未给出，不能把简单显著性当作完整协方差检验。
3. 一个最小 131Ce 设计应同时记录：同一 Harris/reference convention 下的 crossing frequency、相邻 signature splitting、至少一条已定 multipolarity 的 linking transition、DCO/偏振或 δ，以及 lifetime/absolute strength。单独看到 splitting 变小不能决定是 proton alignment、γ-soft mixing 还是其它 band mixing。

### Continuation 2 counter-evidence and missing observables

- **模型竞争：** MA90-1/MA90-2 的“γ≈−30°、alignment 后 γ≈0°或−40°到−80°”是 CSM/TRS interpretation；MA90-AR-2 明确依赖 Harris reference、配对和 cranking 参数。configuration mixing 或 alignment blocking 也可产生大 signature splitting（MA90-4）。
- **谱学边界：** bands 3/4 的 linking 弱或未解析，band 10 的 parity 不唯一；band 7/8 的近 bandhead 和不同 crossing frequency 保留 neutron-aligned configuration alternatives（MA90-3）。
- **跃迁边界：** 560 keV 的 δ=−0.42(9) 仍是由 alignment coefficients、有限探测器修正和 phase convention 得到的 source-specific quantity；没有寿命、绝对 B(E2)/B(M1) 或 polarization 就不能把它升级为集体模式裁决。
- **源独立性：** Ma 是独立的 131Ba 五晶体实验，但 N=75 Table II 与 Liu 的系统学问题在文献层面可能有依赖；本行只计 Ma 这一次实验，Liu 仍单列为 compiled systematics。


## Continuation 3 — 131Ce derived strengths and the δ=0 boundary

### Candidate selection and active recall

本 continuation 选择 Alwaleedi 2013 的 131Ce source，因为它把 crossing/alignment、angular-intensity ratios 和 branching-derived B(M1)/B(E2) 放在同一条证据链上，正好检验 Ma 1990 的 alignment bridge 能否闭合到 131Ce。问题是：**当 B(M1)/B(E2) 依赖 δ=0、模型 g factors、alignment 和 Q0 时，它能支持到什么程度的组态或集体模式判断？**

主动回忆：

- B(M1)/B(E2) 是由能量、分支强度、mixing ratio 和模型参数派生的比值，不是绝对 B(M1) 或 B(E2)。
- δ=0 是一个计算假设；它不是“没有混合”的实验事实。
- crossing frequency 可以帮助组态识别，但跨核素比较必须保持相同 reference convention、组态和 alignment 定义。
- 与半经典理论曲线相符只能支持组态相容性，不能单独建立 wobbling、chirality 或 γ-rigid shape。

### Source and evidence

- 主来源是 [Alwaleedi 2013 131Ce source page](../../knowledge/sources/alwaleedi-2013-band-structures-131ce.md)，DOI [10.17638/00015073](https://doi.org/10.17638/00015073)，raw PDF SHA-256 B50C22877418DE560F06002588BB46D34F5BA670C6880E30A89D1509C79AD8C1。source 页为 review_status: unreviewed，AW13-12/AW13-13 是既有 claim-level review，不把整页升级为 human-reviewed。
- 实验直接事实包括 100Mo(36S,5nγ)131Ce、165 MeV、Gammasphere 101 个 Compton-suppressed HPGe 和约 3×10^9 个 fold≥7 prompt coincidences（source setup；AW13-1/AW13-3）。
- Table 5.1 的 crossing frequency 为 Band 1 两个 signature 0.329、0.367 MeV/ℏ，Band 2 两个 signature 均为 0.316 MeV/ℏ（AW13-5）。这些数值是 alignment/crossing handles，不是 γ 的直接测量。
- Equation 5.6–5.7 和 Table 5.4（PDF pp.86）给出 B(M1)/B(E2) 的输入链：能量五次方/三次方、分支比 λ、显式 1/(1+δ²)、单粒子 g factors 和平均 alignment（AW13-9）。Table 5.4 的 g/ix 输入包括 neutron [404]7/2+ 0.255/0.5、[514]9/2− −0.209/2.5、[541]1/2− 0.209/1.5，以及 proton [413]5/2+ 0.73/1.5、[550]1/2− 1.214/4.5。
- Figure 5.5 的经验比值在 Band 1 低自旋约 1、backbend 后约 3.5；Band 2 约 0.25 到 4；Band 7 约 3.75 (μN/eb)²。作者把实验/半经典曲线相符解释为组态支持（AW13-10），但 source 明确没有寿命、绝对 B(E2)、线偏振或直接形变测量（AW13-11）。
- 131Ce Band 1 的低自旋 signature splitting、约 0.3 MeV/ℏ 的 backbend 和约 9ℏ alignment gain 与 νh11/2、πh11/2² crossing 的解释来自作者的 alignment/model chain；Ma 131Ba 的平均 proton crossing 约 0.430 MeV 只能作为方法参照，不能把数值跨核素转移。

### Quantitative δ-sensitivity exercise

由 Equation 5.6，若把 δ=0 得到的比值记为 R0，则有 R(δ)=R0/(1+δ²)。用 Ma 560 keV transition 的 δ=−0.42(9) 只作一个**敏感性情景**，不是 131Ce 的 δ 测量：

| R0 from δ=0 | R(δ=0.30) | R(δ=0.42) | R(δ=0.50) |
|---:|---:|---:|---:|
| 1.00 | 0.917 | 0.850 | 0.800 |
| 3.50 | 3.211 | 2.975 | 2.800 |
| 0.25 | 0.229 | 0.213 | 0.200 |
| 4.00 | 3.670 | 3.400 | 3.200 |
| 3.75 | 3.440 | 3.188 | 3.000 |

因此在 |δ|≈0.42 的情景下，δ=0 会把真实比值高估约 17.6%（相对真实值），或使修正值约为 δ=0 数值的 85.0%。这项传播只处理 δ，尚未包含分支强度、能量、g factor、alignment 和 Q0 的不确定度，也没有可用 covariance。

同样的 reference audit 也不能把 crossing 数值直接类比：Ma 131Ba 的 proton crossing 均值约 0.430 MeV，而 131Ce Band 1 两 signature 是 0.329/0.367 MeV；不同核素、组态、Harris 参数和带定义使其只能作为设计对照。对 131Ce 真正有区分力的设计应同时取得独立 δ/偏振、寿命或绝对强度，再比较 crossing 后的 B(M1)/B(E2) 是否保持。

### Continuation 3 counter-evidence and missing observables

- **δ=0 反证：** 只要真实 δ 不为零，Equation 5.6 的 derived ratio 就系统偏离；Ma 的 δ=−0.42(9) 证明同类高自旋 M1/E2 线可以有显著混合，但该值不能转移到 131Ce。
- **模型输入边界：** Table 5.4 的 g factors、平均 alignment 和 TRS-derived Q0 是计算输入；它们不是 131Ce 的直接电磁测量。AW13-10 的“曲线相符”因此是 model-assisted support。
- **组态边界：** AW13-3/AW13-8 的 band/configuration labels 仍依赖 crossing、Routhian 和 source 内部 parity/band-5 mapping；AW13-12/AW13-13 的原文冲突必须继续隔离。
- **缺失 companion observables：** 没有 lifetime、绝对 B(E2)/B(M1)、线偏振、直接 Q_t 或可靠 δ，就不能用比值曲线裁决 wobbling、chirality、shape coexistence 或 γ-soft/γ-rigid。
- **源独立性：** Alwaleedi 是一条 131Ce thesis 实验线；Ma 是独立 131Ba 实验。两者提供方法互补，不构成同一核素的重复验证。



## L0–L4 state

- **L0：** complete。已核对 Alwaleedi source identity、DOI、raw hash、实验设置、Table 5.1/5.4、Equations 5.6–5.7、Figure 5.5 和 AW13 atomic locators。
- **L1：** complete。新增“crossing/alignment → branching-derived ratio → δ/g/alignment/Q0 inputs → configuration boundary → missing absolute observables”链，并与 Ma/Liu/Ding 证据契约相连。
- **L2：** complete/extended。完成主动回忆、原始公式和表格视觉复核、δ 敏感性传播、跨核素 reference audit 和反证审计。
- **L3：** candidate only。131Ce/131Ba 的竞争问题更清楚，但仍未建立含完整独立数据和停止条件的 L3 unit。
- **L4：** not ready。没有事件级数据、response、covariance、校准和分析代码；未生成 proxy 结果。

## Verification and continuation

- 本 continuation 写入前的 python3 system/scripts/wiki_boundary_check.py --root . → exit 0；六类目录、outputs 分类和 QMD 边界通过。
- 报告仍是 [20260925-DAY1-baseline-research-contract.md](20260925-DAY1-baseline-research-contract.md)，run receipt 为 [run.json](20260925-DAY1-baseline-research-contract-run-01/run.json)，同一 session 为 01a0d794-6454-7563-bac1-3b5ad970edda。
- 由于本 continuation 新增 131Ce matrix row，唯一机器块保留 status: updated；runner 的 knowledge snapshot 应检测到 knowledge/projects/a130-thesis-evidence-matrix.md 的变化。
- 收尾检查：python3 system/scripts/wiki_lint.py --fail-on error → exit 0（errors=0，warnings=80，info=1106；summary pages=531, wikilinks=4829, hashes=244）；git diff --check → exit 0；writeback validator → valid=true，mode=updated，changed_paths=[knowledge/projects/a130-thesis-evidence-matrix.md]，三个 anchor 与 LU96-1…LU96-4、MA90-1…MA90-4、AW13-5/AW13-9/AW13-10/AW13-11 原子 locator 均通过。
- 下一 continuation prompt：继续同一 Day 1 session，以 [[ding-2021-131ba-133ce-signature-splitting]] 对照低-j Coriolis mixing、γ 非轴性和 N=75 signature systematics，检查其是否提供独立的竞争解释或只是依赖已有带数据。
