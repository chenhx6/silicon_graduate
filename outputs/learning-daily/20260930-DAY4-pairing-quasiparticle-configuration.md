---
type: learning-daily
graph-excluded: true
run_id: prompt-2026-09-30-day-04
runner_run_id: 2026-09-30-day-04-04
parent_run_id: 2026-09-30-day-04-01
run_date: 2026-09-30
timezone: Asia/Shanghai
day_index: 4
phase: nuclear-structure-framework
cycle: 2026-09-30-day-substantive
schedule_id: wiki-daily-learning
schedule_name: Wiki 30-day substantive daily learning
run_kind: substantive
acceptance_only: false
review_status: ai-draft
session_id: 01a0f1e5-98fb-7453-aa16-e987dcbd633d
session_mode: resumed-existing-session
---

# 2026-09-30 Day 4：配对、准粒子与组态变化

## Run state

- 本日报覆盖日程任务 `prompt-2026-09-30-day-04`，最终回执位于 [run-04 receipt](20260930-DAY4-pairing-quasiparticle-configuration-run-04/run.json)。同一 Codex session 为 `01a0f1e5-98fb-7453-aa16-e987dcbd633d`；可恢复命令：`codex resume 01a0f1e5-98fb-7453-aa16-e987dcbd633d -C /workspace/wiki -s danger-full-access -a never`。
- 本日报覆盖日程任务 `prompt-2026-09-30-day-04`，最终回执位于 [run-04 receipt](20260930-DAY4-pairing-quasiparticle-configuration-run-04/run.json)。同一 Codex session 为 `01a0f1e5-98fb-7453-aa16-e987dcbd633d`；可恢复命令：`codex resume 01a0f1e5-98fb-7453-aa16-e987dcbd633d -C /workspace/wiki -s danger-full-access -a never`。
- 计划截止时间为 `2026-10-01 15:00 Asia/Shanghai`；行政收束时间为 `2026-09-30 22:10 Asia/Shanghai`。本轮提前收束，理由是 Day 4 两个选定问题已分别完成原文/定量核查，下一步最有价值的 Masiteng 2013/2014 原文路线在可公开来源处受访问阻挡；已停止重复尝试被挡端点。后续只有出现新的合法全文副本或目标带数据时才重开该问题。
- 执行时 fast 配置为 `global_rounds_max=3`、`optimization_gain_stop=<25%`、`quality_ratio_min=0.60`、`effective_format=Markdown`。没有无 fast 的同环境对照，提速倍数与质量比例未实测。
- 并行只读审查共派 6 个子代理：Ma 1990、Nomura 2021、194Tl 访问路线、AME2020 Ba 质量差分、Pai 2012 原文、候选池与研究设计；六项均已返回。Wiki farmer `ensure` 成功且 watcher 在运行；`once` exit `0`、`actions=[]`。没有 allowlisted 瞬时失败需要重试；原 runner 在用户中断后由当前 session 明确续接。
- 起始 tracked 工作树干净；继承的 Day 2 / Day 3 / Day 4-run-01 目录与 Day 2 / Day 3 raw 文件均未改写。新增 Pai PDF 保存于本轮专属 `raw/papers/gpt/day4-20260930/194tl-pai-2012/`，作为原始公开来源保留且不纳入 Git；公式核查渲染留在 `tmp/`。未改 `PLAN.md`、Zotero inbox 或任何 `human-reviewed` 标记。

## Candidate pool and selection

从 [当前开放问题](../../knowledge/questions.md)、[A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)、Day 2 的壳隙/`131Ce` 来源指纹和 Day 3 的模型选择/`131Ce` 设计记录重建候选池。最近几日已反复读取 `Ding 2021`、`Li/Singh 131Ce`、`Agarwal 137Pr` 与投影模型来源；本日避免将它们重复算作新增实验。

| 槽位 | 问题 | 选择理由与范围 |
|---|---|---|
| 连续性 | `131Ba` 高自旋 `h11/2` crossing 能说明什么 pairing / quasiparticle 结构变化？ | 选用 Ma 1990 原始能带与 alignment 数据；它连接 Day 2 已有的 `N=75` signature/轨道讨论，也能把直接 γ 能级、派生 alignment、模型组态分开。注意 `Ma 1990` 的 `νh11/2` 高自旋序列与 Ding 2021 的 `νg7/2` band 2 是不同能带。 |
| 新颖性 | `194Tl` 的 `2qp→4qp` crossing 与 crossing 后 partner 候选是否为同一证据？ | 选用不同质量区的 Pai 2012 INGA 原始数据；它证明 crossing 本身已在早期独立实验中报道。Masiteng/iThemba 后续四准粒子近简并结果目前只有 Bark 2024 综述和出版商摘要可读，不能升格为本轮直接复核的 partner 证据。 |
| 理论锚点 | Nomura 2021 的配对涨落可否解释奇 A 高自旋 band crossing？ | 按 Day 4 卡指定读取。该论文针对 `128,130Xe` 偶偶核低能谱，为区分 pairing vibration 与高自旋 blocked quasiparticle 提供模型边界。 |

**开原始 PDF 前的主动回忆：** BCS 准粒子能量含有单粒子能级相对化学势的偏移与 pairing gap；转动参考系中 `E′=E−ωI_x` 会改变不同 alignment 配置的相对能量。奇核基态有 blocked quasiparticle，再增加一对准粒子后，组态粒子数奇偶数增加 2。质量的奇偶 staggering 可作为基态配对相关量，但跨越自旋区间的 pairing gap、准粒子组态指认与观测到的能级 crossing 仍是不同层次的问题。开文献前不确定 crossing 的频率是否直接测量，以及 Harris reference 对 alignment 曲线的影响。

## Sources and evidence

| 来源与精确定位 | 证据类别 | 本轮可支持的内容与边界 |
|---|---|---|
| [Nomura et al. 2021 Wiki source](../../knowledge/sources/nomura-2021-pairing-triaxial-vibrations-gamma-soft.md)：`NOM21-1/2` Fig.1 PDF p.2；`NOM21-3` Eqs.(1)–(5) pp.2–3；`NOM21-4/5` Fig.2 p.4；`NOM21-6/7` Fig.3 p.4；`NOM21-8/9` Fig.4 p.5。DOI [`10.1103/PhysRevC.103.054322`](https://doi.org/10.1103/PhysRevC.103.054322)，Crossref 核对题名、作者、PRC 103(5)、文章号 054322 和出版日。 | 模型结果；图中的实验点是既有输入 | `PC-PK1 RMF+BCS (α,β,γ) PES → IBM n0−1/n0/n0+1 boson spaces` 描述偶偶 `128,130Xe` 的低能配对/三轴涨落。Fig.2 显示动态自由度改变激发 `0+` 能量；子空间混合阻止逐态唯一拆分配对与形变贡献。Fig.3 中 `E2γ` 与 `R3γ` 趋向不同几何参考；Fig.4 的非 yrast `B(E2)` 不确定度较大。模型不含本任务中的奇 A 高自旋 qp alignment，且省略约 3 MeV 以上的 2qp/4qp 空间。Wiki PDF SHA-256 `cf500a8c…810102c4`，arXiv v1 是同文预印本，不是独立来源。 |
| [Ma et al. 1990 Wiki source](../../knowledge/sources/ma-1990-131ba-competing-alignments.md)：`MA90-1` PDF p.717 摘要 / p.725 Fig.5 / p.726 Fig.6(a)；`MA90-2` PDF pp.725–728, Figs.5–7, Table II；`MA90-3` PDF pp.725–727, Figs.1,6；`MA90-4` PDF pp.719–725, Table I, Figs.3–4；`MA90-5` PDF p.725 Eq.(2), Fig.5。DOI [`10.1103/PhysRevC.41.717`](https://doi.org/10.1103/PhysRevC.41.717)，本地原文 SHA-256 `a0dbdd4957d1d11af570b5daffc9c44609d9ef5ed570dc3ad32a67388dad90de`。 | γ-ray 能级/符合/角数据为直接实验报告；`i_x` 与 crossing frequency 为能级派生量；形状和 qp 指认是作者解释 | 十条带的能级图、部分角分布/DCO/混合比来自 `119Sn(12C,4n)` 五 Ge 实验。质子 signature crossing 为 `0.445(3)` 与 `0.415(3) MeV`；band 7/8 中子对齐为不同的候选 crossing (`0.44` 与 `0.36 MeV`)。CSM/TRS 将质子和中子 alignment 分别解释为不同的形状驱动力。`i_x` 使用 Harris reference，参数由 band 5 拟合；alignment 不是 pairing gap 的直接读数。 |
| [AME2020 Wiki source](../../knowledge/sources/ame2020-sn132-mass-curvature.md)：`AME20-130BA-1` 行 1656；`AME20-131BA-1` 行 1674；`AME20-132BA-1` 行 1691；推导项 `AME20-ODD3-BA-1`。本地表与 [IAEA mass_1 官方数据](https://www-nds.iaea.org/amdc/ame2020/mass_1.mas20.txt) SHA-256 均为 `e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307`。 | 评价基态质量；三点差分是本轮派生量 | 给出 `130–132Ba` 相邻 `N=74,75,76` 的 AME2020 mass excess。`131Ba` 行的 `-n` 原样保留，意义未推断。质量由同一次 least-squares evaluation 汇总；不作为三次独立实验。 |
| [Pai et al. 2012 Wiki source](../../knowledge/sources/pai-2012-high-spin-bands-194tl.md)：`PAI12-1` PDF pp.1–2；`PAI12-2` pp.4–6, Fig.5；`PAI12-3` p.8, Fig.7；`PAI12-4` p.8/p.10 Fig.13；`PAI12-5` p.6；`PAI12-6` p.9；`PAI12-7` p.5, Table I。DOI [`10.1103/PhysRevC.85.064313`](https://doi.org/10.1103/PhysRevC.85.064313)，[arXiv:1201.6596v2](https://arxiv.org/abs/1201.6596v2) 原始 PDF SHA-256 `633b068625691c4aeb6200867a9cd8820e6528b9fc19ae1c6ca2a3928fcf7553`。 | 直接 γ-ray 实验；derived alignment；作者 qp解释 | INGA Re+C 独立数据报告约 `0.34 MeV` alignment gain。作者把它解释为第二对 `νi13/2` neutron alignment、B1 从 2qp 延续到 post-crossing 4qp。B2 宇称/组态不确定，原文明确需要 `18−` lifetime。该 crossing 早于且独立于后续 iThemba acquisition。 |
| [Bark et al. 2024 topical review](../../knowledge/sources/bark-2024-investigations-nuclear-chirality-ithembalabs.md)：`BK24-12/13` PDF pp.16–20, Figs.20–27；Masiteng 2013 DOI `10.1016/j.physletb.2013.01.006`、2014 DOI `10.1140/epja/i2014-14119-5` 的出版商/机构路由已查。 | 二级综述；原始 Masiteng full text 本轮不可读 | 仅保留后续 4qp near-degeneracy、三条观测带与四条计算带配对歧义为二级线索；2013 ScienceDirect 为 HTTP 403，2014 Springer PDF URL 返回订阅 HTML。摘要/综述未用于声称本轮直接核实了后续寿命或逐条转移。 |

## Theory/analysis exercise

**分层：** 一般 BCS 背景下 `E_k=√[(ε_k−λ)^2+Δ^2]`；准粒子 pair 的相对 Routhian 还受 `−ω I_x` 项影响。此式说明配对与转动可共同改变配置排序，不直接给本核某条能带的 `Δ`。Nomura 的 `α` 是映射到 IBM 相邻 boson-number 子空间的 pairing-vibration 坐标；Ma 的 `i_x` 则由自旋、频率和 Harris reference 导出，两种量不互换。

**AME2020 三点 odd-even 质量指标：** 明确定义正号约定

`δ₃,n^odd(Z=56,N=75) = [2 ME(131Ba) − ME(130Ba) − ME(132Ba)] / 2`

代入 `ME(130Ba)=−87256.776(287) keV`、`ME(131Ba)=−86678.958(415) keV`、`ME(132Ba)=−88434.903(1053) keV`，得 `1166.8815 keV`。在误差独立假设下，`σ=0.5√[4(0.415)^2+(0.287)^2+(1.053)^2]=0.685580 keV`。AME未提供拟合质量协方差；所以数值的中心值可复算，`±0.6856 keV` 仅是条件误差传播。这是基态 mass staggering 指标，含质量面平滑曲率成分。

**Harris 对齐参考练习：** Ma Eq.(2) 使用 `J0=11.90 ℏ² MeV⁻¹`、`J1=21.1 ℏ⁴ MeV⁻³`，`I_ref=ω(J0+J1ω²)`。在 `ℏω=0.43 MeV`，`I_ref/ℏ=J0(ℏω)+J1(ℏω)^3=6.7946ℏ`（约 `6.79ℏ`）。因此 crossing 位置来自实验能级/Routhian 与 alignment 曲线的派生分析；Harris term 改变曲线基线，不能被解释成配对隙或独立观测量。

## Counter-evidence and missing companion observables

- Ma 报告的质子对齐附近有两条 signature crossing 值；中子 band 7 和 band 8 的候选 crossing 也不同。两类 alignment 被解释为 near-prolate / near-oblate 的相反形状驱动力，保留了形变变化对能级演化的作用。中子 bands 7/8 的组态仍是候选，不能把 `0.44` 与 `0.36 MeV` 合并为唯一 crossing。
- 另一个机制检查来自 Ding 2021：`131Ba` 的 `νg7/2` band 2 signature splitting 可由 triaxiality 与邻近 `νs1/2` Coriolis mixing 共同影响 (`D21-4/5/6`)。该能带/数据集不同于 Ma 的 `νh11/2` crossing，只提供“signature splitting 不唯一反演 γ”的机制对照。
- Feeding 会改变门控布居和强度比，也会影响寿命/`B(E2)` 提取；它本身不会移动由能级能量构造的 Routhian crossing。Ma 的 bands 7–10 有复杂衰变路径，configuration mixing 对 crossing 附近的谱线也未由多带寿命矩阵定量排除。
- 要判定 crossing 前后集体性和 pair configuration，需要跨带/带内 lifetime、绝对 `B(E2)`、`B(M1)` 或 `Q_t`，并用 linking transitions、g-factor 或 transfer 对组态敏感。AME 基态 `δ₃` 为辅助质量尺度，不能填补高自旋转移矩阵。
- `194Tl` 的 Pai INGA 数据与 iThemba/AFRODITE acquisition 使用不同反应和装置；Pai 支持较早 crossing，Masiteng/Bark 讨论后续 crossing 后 pair。Bark 为综述，不算独立的第三项实验；后续 Masiteng full text 缺失是当前 novelty 路线的停止边界。

## Knowledge Impact and Learning Decision

**Decision: `revises`.** 本轮把“pairing gap—quasiparticle crossing—shape/collectivity”拆成三条可追踪量：AME ground-state odd-even mass staggering；Ma/Pai 由 γ 能级派生的 crossing/alignment；CSM/TRS/作者对 blocked configurations 与形状演化的解释。Crossing 支持准粒子 pair alignment 的作者解释，但不单独给出数值 pairing gap，也不唯一指认形变。Nomura 模型说明低能 pairing vibration 能改排偶偶 `0+` collective states，同时限定了它不能直接指认奇 A 高自旋 crossing。

## Durable knowledge delta

- [Ma 1990 source](../../knowledge/sources/ma-1990-131ba-competing-alignments.md)：修订 `MA90-1/2` 的实验/派生/模型层，新增 `MA90-5` Harris alignment 方程与参数 locator；page status 仍为 `unreviewed`，claims `needs_review` 未清除。
- [AME2020 mass source](../../knowledge/sources/ame2020-sn132-mass-curvature.md)：新增 `130–132Ba` mass rows 与带协方差边界的奇数 `N=75` 三点 indicator `AME20-ODD3-BA-1`。
- [131Ba nucleus page](../../knowledge/nuclei/131ba.md)：持久记录 Ma 的 signature-specific crossing、band 7/8 uncertainty、`AME2020 δ₃` 辅助量及其不能代表高自旋 gap 的限制，并打开 companion-observable 问题。
- [Pai 2012 primary source](../../knowledge/sources/pai-2012-high-spin-bands-194tl.md) 与 [194Tl nucleus page](../../knowledge/nuclei/194tl.md)：新增独立 INGA crossing source 与 B2 lifetime/parity evidence boundary；后续 iThemba pair 仍标为 secondary。
- [Wiki Index](../../knowledge/index.md)：更新 Ma/AME 摘要并新增 Pai source 入口。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/ma-1990-131ba-competing-alignments.md",
      "summary": "Separated 131Ba signature-specific crossing values and added the Harris-reference-derived alignment method while preserving the source's unreviewed state.",
      "anchor": "MA90-2",
      "sources": [
        {"path": "knowledge/sources/ma-1990-131ba-competing-alignments.md", "locator": "MA90-2"},
        {"path": "knowledge/sources/ma-1990-131ba-competing-alignments.md", "locator": "MA90-5"}
      ]
    },
    {
      "knowledge": "knowledge/sources/ame2020-sn132-mass-curvature.md",
      "summary": "Added checked 130-132Ba AME2020 mass rows and the explicitly defined N=75 odd-neutron three-point staggering with conditional error propagation.",
      "anchor": "AME20-ODD3-BA-1",
      "sources": [
        {"path": "knowledge/sources/ame2020-sn132-mass-curvature.md", "locator": "AME20-130BA-1"},
        {"path": "knowledge/sources/ame2020-sn132-mass-curvature.md", "locator": "AME20-131BA-1"},
        {"path": "knowledge/sources/ame2020-sn132-mass-curvature.md", "locator": "AME20-132BA-1"},
        {"path": "knowledge/sources/ame2020-sn132-mass-curvature.md", "locator": "AME20-ODD3-BA-1"}
      ]
    },
    {
      "knowledge": "knowledge/nuclei/131ba.md",
      "summary": "Linked the high-spin Ma alignment evidence with the independent evaluated ground-state odd-even indicator and its open lifetime/absolute-strength test.",
      "anchor": "Pair Alignment and Ground-State Odd-Even Mass Indicator",
      "sources": [
        {"path": "knowledge/sources/ma-1990-131ba-competing-alignments.md", "locator": "MA90-1"},
        {"path": "knowledge/sources/ma-1990-131ba-competing-alignments.md", "locator": "MA90-2"},
        {"path": "knowledge/sources/ma-1990-131ba-competing-alignments.md", "locator": "MA90-3"},
        {"path": "knowledge/sources/ma-1990-131ba-competing-alignments.md", "locator": "MA90-5"},
        {"path": "knowledge/sources/ame2020-sn132-mass-curvature.md", "locator": "AME20-ODD3-BA-1"}
      ]
    },
    {
      "knowledge": "knowledge/sources/pai-2012-high-spin-bands-194tl.md",
      "summary": "Added the direct Pai INGA crossing evidence, its 2qp-to-4qp author interpretation, and the B2 lifetime/parity boundary.",
      "anchor": "PAI12-3",
      "sources": [
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-1"},
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-2"},
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-3"},
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-4"},
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-5"},
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-6"}
      ]
    },
    {
      "knowledge": "knowledge/nuclei/194tl.md",
      "summary": "Connected the independent early INGA crossing to later, still-secondary iThemba near-degeneracy evidence without merging their acquisitions.",
      "anchor": "Early INGA Crossing Evidence",
      "sources": [
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-2"},
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-3"},
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-4"},
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-5"},
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-6"},
        {"path": "knowledge/sources/bark-2024-investigations-nuclear-chirality-ithembalabs.md", "locator": "BK24-12"},
        {"path": "knowledge/sources/bark-2024-investigations-nuclear-chirality-ithembalabs.md", "locator": "BK24-13"}
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Updated the AME source summary and indexed the direct Pai 2012 194Tl source.",
      "anchor": "[[pai-2012-high-spin-bands-194tl]]",
      "sources": [
        {"path": "knowledge/sources/pai-2012-high-spin-bands-194tl.md", "locator": "PAI12-1"}
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Extended the indexed AME2020 source description to include its Ba N=75 mass-staggering row and covariance boundary.",
      "anchor": "[[ame2020-sn132-mass-curvature]]",
      "sources": [
        {"path": "knowledge/sources/ame2020-sn132-mass-curvature.md", "locator": "AME20-ODD3-BA-1"}
      ]
    }
  ]
}
```

## Open questions and belief revision

- `131Ba` 的 `δ₃,n^odd` 约 `1.167 MeV` 如何与转动频率上升时的 pairing suppression、`h11/2` proton/neutron pair alignment 和 triaxial shape drive 联系？分辨这些因果项需要 band-resolved lifetime/absolute `B(E2)`,`B(M1)`/`Q_t`、跨带 link，并对 feeding 与 Harris reference 作敏感性检查。
- `194Tl` 的早期 INGA 数据已确立约 `0.34 MeV` 派生 crossing；iThemba 后续 near-degenerate 4qp pair 与三观测带/四计算带的配对仍缺 Masiteng 2013/2014 可读全文来核查 exact level/transition/lifetime locators。
- **Belief revision:** 开篇预期 crossing 可作为 pair-breaking handle；原文核对后把它限定为能级导出的 alignment 及作者的配置解释。AME `δ₃` 是基态奇偶质量指标，Nomura 是偶偶低能 pairing-vibration 模型，Ma/Pai 是不同核区的旋转准粒子 band；三者互为比较坐标，尚无一个量能代替另一个。

## L0–L4 state

- **L0：bounded direct-source review complete。** Nomura PRC PDF/Eqs.(1)–(5)/Figs.1–4；Ma PDF alignment and crossing pages/Figs.5–7/Table II；Pai arXiv PDF pp.1–2,4–10,12/Table I/Figs.5,7,13；AME2020 official `mass_1` values and online SHA were verified. Masiteng 2013/2014 remained inaccessible as full text, so related pair claims remain secondary.
- **L1：updated.** Updated Ma source locators, AME Ba data, `131Ba` and `194Tl` nucleus pages, added Pai primary source and refreshed index. All changed pages retain `unreviewed`; every new/expanded source claim has `needs_review: true`; no `human-reviewed` was added.
- **L2：complete.** Completed BCS/Routhian separation, three-layer crossing evidence map, odd-N mass-staggering calculation with uncertainty assumption, Harris-reference numerical exercise, competing-shape/feeding/band-mixing checks and dataset-lineage audit.
- **L3：bounded candidate.** `131Ba` pairing versus shape/band-mixing remains open; `194Tl` is a cross-mass comparison with a primary early crossing and secondary-only later partner route. Stop reason: selected routes reached their evidence boundary and the only direct iThemba full-text route was access-blocked.
- **L4：not-ready.** No user event-by-event γ data, response/covariance, calibrated lifetime/strength data package or executable model input for `131Ba`/`194Tl`; no proxy analysis was produced.

## Verification and continuation

- Write-boundary checks before source/knowledge writing and after all current edits: `python3 system/scripts/wiki_boundary_check.py --root .` — exit `0`, no errors/warnings both times.
- `python3 system/scripts/wiki_automation_preflight.py --root .` — exit `0`; protected `raw/zotero/wiki-inbox.bib` hash matched `037EA133DE204270AD36961CA66B3AB36C0913B7D472B45F8FD013C8293BE5BE`. `python3 system/scripts/clean_knowledge_eol_dirty.py` — exit `1` because it retained 5 substantive tracked knowledge edits; `restored=0`, `unsafe/mixed=0`.
- AME online stream hash: `curl … mass_1.mas20.txt | sha256sum` — exit `0`; matches local file and AME source page. Pai arXiv PDF: HTTP `200`, `application/pdf`, 441074 bytes, SHA-256 matches the downloaded source and raw manifest. Nomura/Ma PDF hashes match existing source pages.
- Masiteng access routes: 2013 ScienceDirect HTTP `403`; 2014 Springer PDF request returned subscription HTML, not a PDF. No credentials or access control were bypassed; a repeated endpoint attempt has no expected information gain.
- Required `python3 system/scripts/wiki_lint.py --fail-on error`: final exit `0`, `0 errors / 92 warnings / 1294 info`. Remaining warnings: `CITATION_KEY_MISSING=88`, `REACTION_PARSE=3`, `RAW_GIT_CHANGE=1`; the raw warning aggregates local-only source files, which are excluded from the publish stage. An earlier lint run caught the new Pai source page's three missing standard sections; those sections were added before this final pass.
- `git diff --check`: exit `0`. Report validation: all 10 required headings present; 22 relative Markdown links checked, 0 broken. `wiki_knowledge_writeback.py` structural validation: `valid=true`, mode `updated`, anchor/source-locator checks pass. The resumed manual segment had no persisted byte-for-byte pre-turn snapshot; an initial HEAD-byte comparison flagged EOL-normalized pages, so no snapshot-pass is claimed. The initial tracked status was clean; the current `git diff --name-status` shows five tracked knowledge edits, while `git status` reports one new Pai source page. Together these six task-owned knowledge changes are all mapped in the block.
- Knowledge review states remain unchanged: source/nucleus pages remain `unreviewed` (Nomura source remains `human-reviewed` at its existing status); new and expanded claims retain `needs_review: true`. No tests were added or run.
- Run-04 continuation prompt: [continuation-prompt.md](20260930-DAY4-pairing-quasiparticle-configuration-run-04/continuation-prompt.md). Next-day Day 5 prompt: [prompt preview](prompts/20261001-DAY5-beta-gamma-octupole-shape-coexistence.md). The receipt carries the session/resume command, checks and evidence-saturation stop reason; final branch, subject and push outcome are reported in the closeout recap.
