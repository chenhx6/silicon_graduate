---
type: learning-daily
graph-excluded: true
run_id: 2026-09-26-day-01-01
run_date: 2026-09-26
timezone: Asia/Shanghai
day_index: 1
phase: baseline-and-research-contract
schedule_id: wiki-daily-learning
status: in-progress
---

# 2026-09-26 Day 1：基线考试与研究契约

## Run state

- 本轮执行正式 30 天实质周期的 Day 1，主题为“基线考试与研究契约”。状态文件在本轮开始时仍为 `next_day_index: 1`；只有 runner 在报告、知识写回、lint、diff 和 continuation prompt 全部通过后才计数。
- 启动前已读取 [README](../../README.md)、[Wiki index](../../knowledge/index.md)、[profile](../../profile.md)、[active handoff](../../system/handoff.md)、[PLAN](../../PLAN.md)、最近学习记录、[一个月 CLI 训练计划](../../outputs/plans/2026-09-22-one-month-codex-cli-apprenticeship.md)、[Day 1 任务矩阵](../../outputs/plans/2026-09-22-one-month-daily-task-matrix.md)、[A≈130 三轴论文管线](../../outputs/plans/2026-09-22-a130-triaxial-thesis-pipeline.md) 以及 [continuous-learning workflow](../../system/workflows/continuous-learning.md) 和 [scheduled-continuation workflow](../../system/workflows/scheduled-continuation.md)。
- 写入前 [wiki boundary check](../../system/scripts/wiki_boundary_check.py) 已返回 exit `0`；继承的工作树和受保护文件未覆盖，`raw/`、`PLAN.md` 和 `raw/zotero/wiki-inbox.bib` 未写入。

## Candidate pool and selection

候选池由 [knowledge/questions.md](../../knowledge/questions.md)、现有 [A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)、最近的 [2026-09-25 Day 1 record](20260925-DAY1-baseline-research-contract.md)、[Ding 2021 source page](../../knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md)、以及近期已检查的 `135Pr`、`137Ba` 和 angular-polarization source fingerprints 重建。9 月 25 日已经写入 Liu、Ma 和 Alwaleedi 三条 A≈130 行；重复同一行不会增加信息增益。

- **连续性槽位：** `131Ba/133Ce` 的 `νg7/2[404]7/2+` signature splitting 是否可以被当作 γ 形变的单一观测？选择 [Ding et al. 2021](../../knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md)，因为它把 level energies、`R_ac`、alignment、`J^(2)`、CSM、QTR 和 PES 放在同一证据链中，能直接检验“观测—assignment—模型”的分层。
- **新颖性槽位：** `137mBa` competitive double-γ decay 中，哪一个 companion observable 改变虚跃迁多极性解释？选择 [Walz 2015](../../knowledge/sources/walz-2015-competitive-double-gamma-137ba.md) 与独立 [Söderström 2020](../../knowledge/sources/soderstrom-2020-137ba-competitive-gamma.md) 的 source pages，质量区和机制均与 A≈130 signature splitting 不重叠；这项对照用于训练可迁移的证据契约，不把它当作论文矩阵的 A≈130 行。

**主动回忆（打开来源前）：**

1. `J^π` 是状态的自旋与宇称标签；一条能量间隔不能独立给出它。
2. `S(I)`、alignment 和 `J^(2)` 都是由能级或跃迁数据构造的判别量，不等同于直接测得的 γ 角或形状。
3. `R_ac`/ADO 依赖探测器角度、alignment、feeding、效率和分析约定，不能把一个阵列的阈值移植到所有实验。
4. 作者的组态标签是 interpretation；CSM/QTR/PES 的 `γ`、`β₂` 和波函数分量是 model results；Codex 对缺失观测的判断是 inference。
5. `137mBa` 的能量和角度信息可以显示 rare branch，但 angular-only fit 可能有多解；energy-sharing 是我在回忆中列出的必要 companion observable。
6. 同一论文的不同图、学位论文和期刊版本不能自动计成独立实验；必须记录反应、阵列和 shared-dataset lineage。

## Sources and evidence

### 主来源：Ding 2021

- [Ding et al. 2021 source page](../../knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md)，DOI [`10.1103/PhysRevC.104.064304`](https://doi.org/10.1103/PhysRevC.104.064304)，原始 PDF 为 `raw/papers/2021_Ding et al_Signature splitting of the g 7 - 2 [ 404 ] 7 - 2 + bands in Ba 131 and Ce 133.pdf`，本轮复核 SHA-256 为 `752d3c5da690c20ec7e188dcc043f9da2a7f062deefc371dd8a497a190b66c37`。
- **实验直接事实：** `122Sn(13C,4n)131Ba` 与 `125Te(12C,4n)133Ce` 两条反应分别使用 GALILEO 与 AFRODITE；Fig.1–3 和 Tables I–II 给出新带的能级、γ 线、相对强度、`R_ac` 与 assignment handles（D21-1；PDF pp.3–9）。这是两次不同反应/阵列的直接实验谱系，但共享同一篇论文的分析框架。
- **作者解释：** 两核新带 2 以强耦合 `7/2+` 带头和 M1+E2 级联为依据，被指认为 `νg7/2[404]7/2+`（D21-2；PDF pp.6–9）。这是 author-interpretation，不是单一跃迁测量。
- **上下文系统学：** Fig.4 的 `i_x`、`J^(2)` 和 Routhian 图把 `131Ba/133Ce` 与 `129Ba/131Ce/133Nd` 比较；后面三核数据来自 refs.46–48 的旧工作（D21-8；PDF pp.5–6、9、14–15），因此不能作为 Ding 2021 的新独立实验。
- **模型结果：** CSM 在低频、γ=0° 时几乎不给 splitting，γ 约 10° 后 splitting 出现并随 γ 增强（D21-4；PDF p.11、Fig.7）；QTR 用 `γ=10°` 描述 `133Ce`、`γ=15°` 描述 `131Ba`，并含近邻 `s1/2[400]1/2+` 分量（D21-5；PDF pp.11–12、Figs.8–9）。衰减 Coriolis 作用后，γ≤15° 的 staggering 可消失而 γ>15° 又出现（D21-6；PDF p.12、Figs.8–9），说明同一 `S(I)` 模式不是 γ 的唯一反演。
- **PES 边界：** Table III 给出模型的 `β₂,γ,β₄`，如 `131Ba` `β₂=0.180, γ=9.1°` 和 `133Ce` `β₂=0.195, γ=-10.5°`（D21-7；PDF p.13、Table III）；这些是 model-result，不能写成实验直接形变。

### 新颖性对照：`137mBa` competitive double-γ

- [Walz 2015 source page](../../knowledge/sources/walz-2015-competitive-double-gamma-137ba.md)，DOI [`10.1038/nature15543`](https://doi.org/10.1038/nature15543)，PDF pp.406–409、Figs.1–4、Table 1；本轮核对原始 PDF SHA-256 `4177a89672ef1362d9dc35ff1292c7550c2db477fe34b61abaec4c72475b9c45`。直接结果是 `Γγγ/Γγ=(2.05±0.37)×10⁻⁶`（W15-1），并用 timing、random subtraction、energy-sum 与 72°/144° angular correlation 排除主要背景路径（W15-2）。
- [Söderström 2020 source page](../../knowledge/sources/soderstrom-2020-137ba-competitive-gamma.md)，DOI [`10.1038/s41467-020-16787-4`](https://doi.org/10.1038/s41467-020-16787-4)，PDF pp.3–6、Figs.3–5、Table 1；本轮核对原始 PDF SHA-256 `fb8bd159bae6e5f1e2b9827e1bf2bce7cd98c126c7fef00f1bd41526154ec12a`。独立的 11-CeBr3 五角度测量给出 `2.62(30)×10⁻⁶`，并显示 angular-only fit 的多解；energy-sharing 数据偏向较大的 E3M1 和较小的 M2E2 分量（SO20-1、SO20-2、SO20-3）。
- 这两篇是同核素的两次实验，不是重复 PDF；总分支比可以比较，但 `α` 系数的符号/路径约定和模型输入必须回到各自 Eq./Table。原始 response、协方差和 sorting code 未公开，不能开展独立 L4 重拟合。

## Theory/analysis exercise

### `S(I)` 的 level-scheme 重算

对 Ding Tables I–II 的 Band 2 能级使用论文定义

`S(I) = E(I) − E(I−1) − 1/2[(E(I+1)−E(I)) + (E(I−1)−E(I−2))]`。

用 `131Ba` 的 `E(7/2,9/2,11/2,13/2,15/2,17/2) = (526.3, 882.5, 1210.7, 1624.1, 1988.4, 2450.2) keV`，得到：

- `S(11/2) = −56.6 keV`；
- `S(13/2) = +67.1 keV`；
- `S(15/2) = −73.3 keV`。

用 `133Ce` 的 `(340.3, 678.4, 1033.1, 1459.9, 1852.5, 2304.3) keV`，得到 `S(11/2) = −27.8 keV`、`S(13/2) = +53.2 keV`、`S(15/2) = −46.7 keV`。交替符号与几十 keV 的幅度说明 `S(I)` 确实携带 signature staggering；它没有把 `γ`、Coriolis attenuation 或 `s1/2` 混合逐项分离出来。计算只重算了 published level energies，没有重新拟合模型。

### 两次 `137mBa` 分支比的误差传播

把两次实验的总分支比差写成 `Δ = 2.62−2.05 = 0.57×10⁻⁶`，若暂按独立统计误差传播，`σ_Δ = √(0.37²+0.30²) = 0.476×10⁻⁶`，标准化差为 `Δ/σ_Δ = 1.20`。因此总分支比在这个简化比较下相容；真正改变解释排序的是 Söderström 的 energy-sharing companion observable，而不是总分支比本身。这个算术不是新的实验拟合。

### 基线四层映射

| 层级 | 本轮例子 | 可支持的说法 | 不能越过的边界 |
|---|---|---|---|
| 实验直接事实 | Ding 的能级/γ 线/`R_ac`/`i_x`/`J^(2)`；Walz/Söderström 的计数、时间、能量和角度 | 线、级联、比值和 signal/background chain 被报告或由表格重算 | 不能单独给唯一组态、固定 γ 或虚中间态矩阵元 |
| 作者解释 | `νg7/2[404]7/2+`、signature-splitting mechanism、Walz 的 dominant `Aqq` | 复述作者如何组合观测 | 不能把标签改写成 direct measurement |
| 模型结果 | CSM/QTR/PES；EDF+QPM/MCSM | 检验模型与数据相容性及竞争机制 | 不能把 `β₂,γ` 或 α path 变成实验事实 |
| Codex 推断 | `S(I)` 与 energy-sharing 是判别 handles；缺少 lifetime/δ/polarization 时不可识别 | 明确下一项最高信息量观测 | 不能补造响应、协方差或 proxy fit |

## Counter-evidence and missing companion observables

- **Ding 的反证：** 131Ba/133Ce 的 `S(I)` 可由两类机制共同产生。QTR 在衰减 Coriolis、γ≤15° 时可使 staggering 消失，而在 γ>15° 又恢复（D21-6）；因此“splitting 大 ⇒ 固定三轴 γ 大”不是唯一解释。
- **近简并边界：** 131Ba 两个 `7/2+` 态只差约 18 keV，133Ce 的对应 `13/2+` 也有近邻混合条件（D21-1、D21-8 的正文讨论）；组态混合会改变能级差，却不能从能级本身直接量出混合矩阵元。
- **多极性与形变的必要 companion：** 需要 transition-level mixing ratio、线偏振和必要转换系数来巩固 `J^π`/multipolarity；需要寿命、绝对 `B(E2)/B(M1)` 或 `Q_t` 来检验集体性；需要独立 linking、转移选择性或 g-factor 才能降低 configuration/mode ambiguity。
- **137Ba 的反证：** Walz 的 angular-correlation 拟合给出 dominant `Aqq`（W15-3），而 Söderström 显示 angular-only 有两个 χ² 极小值，并由 energy-sharing 支持 E3M1（SO20-2、SO20-3）。同一总分支比的一致性不能关闭虚路径分解争议。
- **来源独立性：** Ding 的 N=73 `129Ba/131Ce/133Nd` 曲线依赖 refs.46–48；Walz 与 Söderström 才是 `137mBa` 的两个不同实验谱系。任何后续综合必须把这些依赖关系留在 source lineage 中。
- **L4 缺口：** 本轮没有事件级 spectra、detector response、calibration covariance、sorting/fit code 或公开 Mendeley snapshot；因此只做能级算术和分支比误差传播，不生成 L4 proxy result。

## Knowledge Impact and Learning Decision

**Decision: revises（同时 supports placement、limits mode inference）。**

- `Ding 2021` 支持两个 N=75 新带的 placement/assignment chain，但修订了“signature splitting 可直接量 γ”的朴素信念：低 `j` `s1/2` Coriolis mixing 与 non-axiality 必须并列作为竞争机制。
- `137mBa` 对照支持 Day 1 的 companion-observable 契约：总分支可在独立实验中相容，而 energy-sharing 才改变 virtual-path interpretation。
- 本轮没有设置 `human-reviewed`、没有清除任何 `needs_review`，也没有把模型输出或 source-page self-audit 写成实验事实。

## Durable knowledge delta

已检查矩阵中已有的 Ding 2012、Liu、Ma 和 Alwaleedi 行，确认没有把同一 claim 重复写入；本轮在 [A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md) 新增 anchor **`131Ba/133Ce νg7/2 signature-splitting mechanism bridge`**。该行固定了两条反应/阵列的直接证据、`S(I)`/`R_ac` assignment handles、CSM/QTR/PES 的模型边界、N=73 依赖谱系和所需的 mixing-ratio/polarization/lifetime/absolute-strength companions。Ding source 页原有 `review_status: human-reviewed` 被保留；矩阵页仍为 `review_status: unreviewed`。`137Ba` 两个 source 页已有相应 durable records，本轮只做交叉核对，不重复创建 source/project 页。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "Added the 131Ba/133Ce signature-splitting mechanism bridge, separating direct level and angular observables from author assignments, CSM/QTR/PES model results, dependent N=73 context, and required companion observables.",
      "anchor": "131Ba/133Ce νg7/2 signature-splitting mechanism bridge",
      "sources": [
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-1"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-2"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-4"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-5"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-6"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-7"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Added the N=73 original-source audit: Palacz 1991 directly verifies the 131Ce high-spin source behind refs.47, Bazzacco 1998 verifies the 133Nd GASP/DCO source behind refs.48, and Byrne 1992 remains a full-text boundary.",
      "anchor": "N=73 original-source audit (Palacz 1991/Bazzacco 1998)",
      "sources": [
        {
          "path": "knowledge/sources/palacz-1991-high-spin-131ce.md",
          "locator": "PAL91-1"
        },
        {
          "path": "knowledge/sources/palacz-1991-high-spin-131ce.md",
          "locator": "PAL91-2"
        },
        {
          "path": "knowledge/sources/palacz-1991-high-spin-131ce.md",
          "locator": "PAL91-4"
        },
        {
          "path": "knowledge/sources/palacz-1991-high-spin-131ce.md",
          "locator": "PAL91-6"
        },
        {
          "path": "knowledge/sources/bazzacco-1998-rotational-bands-133nd.md",
          "locator": "BAZ98-1"
        },
        {
          "path": "knowledge/sources/bazzacco-1998-rotational-bands-133nd.md",
          "locator": "BAZ98-2"
        },
        {
          "path": "knowledge/sources/bazzacco-1998-rotational-bands-133nd.md",
          "locator": "BAZ98-5"
        },
        {
          "path": "knowledge/sources/bazzacco-1998-rotational-bands-133nd.md",
          "locator": "BAZ98-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/palacz-1991-high-spin-131ce.md",
      "summary": "Created the source page and claim table for the public Palacz 1991 131Ce high-spin PDF, preserving incomplete-link and assignment boundaries.",
      "anchor": "PAL91-1",
      "sources": [
        {
          "path": "knowledge/sources/palacz-1991-high-spin-131ce.md",
          "locator": "PAL91-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bazzacco-1998-rotational-bands-133nd.md",
      "summary": "Created the source page and claim table for the public Bazzacco 1998 133Nd GASP/DCO PDF, preserving DCO, imported-Q0 and cross-nucleus boundaries.",
      "anchor": "BAZ98-1",
      "sources": [
        {
          "path": "knowledge/sources/bazzacco-1998-rotational-bands-133nd.md",
          "locator": "BAZ98-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added exact index entries for the two newly created N=73 source pages so the source graph and lint index boundary remain complete.",
      "anchor": "[[palacz-1991-high-spin-131ce]]",
      "sources": [
        {
          "path": "knowledge/sources/palacz-1991-high-spin-131ce.md",
          "locator": "PAL91-1"
        },
        {
          "path": "knowledge/sources/bazzacco-1998-rotational-bands-133nd.md",
          "locator": "BAZ98-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/haxel-jensen-suess-1949-magic-numbers.md",
      "summary": "Corrected the source-local historical magic-number attribution: HJS Table I/text explicitly list 14,28,50,82,126, while the modern 2,8,20 context belongs to later/background knowledge and is not attributed wholesale to this letter.",
      "anchor": "HJS49-1",
      "sources": [
        {
          "path": "knowledge/sources/haxel-jensen-suess-1949-magic-numbers.md",
          "locator": "HJS49-1"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

- 对 `131Ba/133Ce`，同一 `S(I)` 序列中低 `j` Coriolis mixing 与 non-axiality 的最小可识别 observable 组合是什么？仅增加更高自旋能级不能解决这个问题；优先级应给 `δ`、线偏振、寿命和绝对强度。
- `131Ce` 的现有 `B(M1)/B(E2)` 派生链能否接入类似的 alignment/`S(I)` crosswalk，同时保持 `δ=0`、`g` factors、`Q0` 和 source lineage 的边界？
- `137mBa` 中，若重新获得 response/covariance/code，能否在同一 likelihood 中联合 energy-sharing、五个 angular points 和 detector-response nuisance parameters，以检验 E3M1/M2E2 分解？当前数据 DOI 端点不可用，问题保持 `not-ready`。
- **信念修订：** A≈130 signature splitting 现在应被视为“结构机制的联合判据”，而非 γ 角的单变量 proxy；rare-decay 对照进一步说明必要 companion observable 可能比更高统计量的同一 observable 更有信息增益。

## L0–L4 state

- **L0：complete。** 任务卡、source identity、DOI、raw PDF hash、PDF locator 和 matrix anchor 已核对；Continuation 1 又完成了 refs.47/48 的原始全文身份核验，并记录了 ref.46 的 closed boundary。
- **L1：complete。** 已把 level/transition facts、assignment handles、interpretation limits 和 source lineage 互链；Palacz/Bazzacco source pages 与 `131Ce` project/index 已反链。
- **L2：complete for this bounded Day 1 exercise。** 完成一次跨 source 的反证、独立性和 companion-observable 检查，并把结果写回矩阵与 N=73 project audit；没有把重复引用当独立证据。
- **L3：candidate-L3。** `131Ba/133Ce` mechanism bridge 可作为后续 A≈130 evidence map 单元，但本轮没有启动完整的多来源课题、falsifier 搜索或 prospectus。
- **L4：not-ready。** Ding 没有事件级/响应/协方差/代码包；`137Ba` 现有论文也缺少可复现 response/code snapshot。只保留 readiness boundary，不生成代理数据结果。


### Continuation 1：N=73 原始来源核验

- **Palacz 1991 (`131Ce`, refs.47)：** Springer PDF 全文可得。PDF p.467 的摘要/实验段给出 `117Sn(18O,4n)131Ce`、NORD-BALL、约 `10^8` 事件和延伸至 `51/2`；Fig.1/2 与 PDF pp.467–468 显示五带纲图、正负宇称带、alignment/routhian 以及不完整 linking。其 `g7/2` 与 `K=7/2` 是作者/模型层（PAL91-1–6）。
- **Bazzacco 1998 (`133Nd`, refs.48)：** APS harvest PDF 全文可得。PDF p.2003 的 DCO 约定明确给出 stretched-quadrupole gate 下 E2≈1、纯 dipole≈0.5，混合跃迁依赖 `δ`（BAZ98-2）；PDF pp.2011–2017、Fig.7/10 与 band-9 讨论给出 `ν[404]7/2` 的 alignment/无 splitting contextual anchor（BAZ98-4–7）。
- **Byrne 1992 (`129Ba`, refs.46)：** Crossref/DOI identity 已确认，但 Elsevier TDM 返回 `400 INVALID_INPUT`/unauthorized，OpenAlex 与 Semantic Scholar 标记 closed；没有把 Ding 图注数值当作原始证据。
- **判断：** refs.47/48 现在从“仅有 Ding caption 归属”升级为两个可回链的 source pages；N=73 comparison 仍是 contextual support，未增加 `131Ce` target-nucleus electromagnetic evidence，也未改变现有模式排序。


### Continuation 2：Day 2 壳隙—轨道—可观测量验证

**主动回忆（打开 source 前）：**

1. spherical closure、deformation-dependent shell gap、orbital/configuration label 和 shape/collectivity 是不同证据层。
2. 轨道简并度可做 occupancy arithmetic，但不能由粒子数差直接得到 gap 的 MeV 数值。
3. `β₂/γ`、Nilsson label、Strutinsky correction 和高自旋 Routhian 都可能是 model outputs；需要质量/分离能、`E(2+)`、alignment、寿命和绝对强度等 companion observables。
4. 现代常用 magic-number 序列与历史 HJS 信件的 Table I 必须分开引用；RS78 是后来的 review synthesis。

**主来源核验：**

- [Haxel–Jensen–Suess 1949](../../knowledge/sources/haxel-jensen-suess-1949-magic-numbers.md) 的原始扫描页视觉复核确认：正文写的是“magic numbers 14, 28, 50, 82, 126”，Table I 的 magic-number column 也标出 14、28、50、82、126（HJS49-1；PDF p.1766）。因此现有 source 页的现代序列归属过宽，已修正为 source-local wording。
- [Ragnarsson–Nilsson–Sheline 1978](../../knowledge/sources/ragnarsson-nilsson-sheline-1978-shell-structure.md) review 明确把现代球形序列 `2,8,20,28,50,82,126`、modified-oscillator/realistic potential、Strutinsky shell correction 和形变/高自旋实验比较分成不同层（RS78-1、RS78-2、RS78-3；PDF pp.3–26、42–82）。

**定量与设计练习：**

- 用现代示意性轨道容量 `2+4+2+6+2+4+8+4+6+2+10=50` 复核一个 `N=50` occupancy closure；这验证粒子数记账，不估计能隙，也不等于 HJS Table I 的历史标记序列。
- 将“壳隙变大/变小”映射到最小观测组合：质量/两核子分离能的局部曲率、低能 `E(2+)`/集体性、配置敏感的 transfer 或 decay、alignment/crossing 和 calibrated `B(E2)`/`Q_t`。单个高 `E(2+)` 或一条模型图不足以闭合 shell-gap claim。
- 对 A≈130 高自旋 band，最小模型输入还需 `β₂,γ` 参数化、pairing、扩散度、平滑方案、旋转频率网格和 occupied Nilsson branches；现有 Wiki 没有统一数值表/协方差，因此不启动 proxy gap fit。

**反证与决定：**

- pairing、diffuseness、smoothing、γ-soft potential 和 configuration mixing 都能改变计算 gap 或谱线排序；RS78-3 要求把实验 shell-effect signatures 与 model shape labels 分开。
- 本 continuation 的 durable change 是 HJS49-1 的 attribution correction；已有 `knowledge/projects/a130-shell-gap-orbital-observable.md` 的 closure arithmetic 和 boundary 已覆盖其余 Day 2 桥接，无需重复新增行。
- **Decision: revises (source attribution), no material change to A≈130 mode ranking.** HJS source page 现保持 `review_status: unreviewed`；未设置 `human-reviewed`，未把历史模型变成现代实验事实。

**L0–L4 continuation state：** L0/L1 source identity and layer separation complete；L2 bounded shell-gap exercise complete；L3 remains candidate only；L4 not-ready because no target-nucleus shell-gap table with response/covariance/code exists。

## Verification and continuation

- 本轮写入前 boundary check exit `0`；矩阵写回仅涉及 `knowledge/projects/a130-thesis-evidence-matrix.md`，未改 raw、PLAN、protected BibTeX 或既有 source review 状态。
- 已核对 Ding 2021、Walz 2015、Söderström 2020 三个 raw PDF 的 SHA-256；原始 PDF 版本与 source-page metadata 一致。
- Continuation 1 新增了两个公开全文 source page：`knowledge/sources/palacz-1991-high-spin-131ce.md`（SHA-256 `e230b4a7…ef7b`）和 `knowledge/sources/bazzacco-1998-rotational-bands-133nd.md`（SHA-256 `0beaa99e…a22b`），并在 project page 固化 refs.47/48 的 source lineage。公开 PDF 只进入 `raw/papers/gpt/_incoming/20260926-day1-n73/`，没有覆盖既有 raw。
- Byrne 1992 `129Ba` 的 DOI/题名已由 Crossref/OpenAlex/Semantic Scholar 交叉确认，但全文获取返回 closed/400；该缺口记录为 source boundary，未用搜索摘要补 claim。
- Continuation 2 再次运行 `python3 system/scripts/wiki_lint.py --fail-on error`：exit `0`，`errors=0`、`warnings=80`、`info=1120`；`git diff --check`：exit `0`。HJS source correction 及 Day 2 验证没有引入 lint error；剩余 warnings 属于既有基线（citation-key 缺口、三个未自动解析反应和继承的 raw 工作树提示等），不是本轮新增科学错误。
- 结构化 `knowledge-writeback` 解析器在不带运行前快照的独立复核中返回 `valid: true, mode: updated`；runner 将用启动时快照确认该矩阵页确实发生了 durable change。
- 下一条正式 continuation prompt：`继续 Day 2 壳隙—轨道—可观测量映射：先不看资料回忆球形壳层、形变壳隙与单粒子组态的区别，再用 Haxel–Jensen–Suess 1949 与 Ragnarsson–Nilsson–Sheline 1978 做一个最小 shell-gap/observable 对照；保持模型结果、实验事实和反证边界。`
- 预期的下一日 prompt 路径为 `outputs/learning-daily/prompts/20260927-DAY2-shell-gap-orbital.md`；runner 在本日最终门通过后生成该文件。当前 run receipt 由 runner 负责补写 `session_id`、`resume_command`、continuation count、实际检查结果和 substantive state。
