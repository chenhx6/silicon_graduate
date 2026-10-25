# Day22：wobbling 几何、声子与观测量

## Run state

- run_id: `2026-10-24-day-22-01`
- day_index: 22
- session_id: `01a16ccb-2ecb-7501-ae47-fb2d58c270da`
- timezone: Asia/Shanghai
- overnight_until: `2026-10-25T15:00:00+08:00`
- closeout_window_ends_at: `2026-10-25T16:00:00+08:00`
- completed_day_indices: [22]
- partial_day_indices: [23]
- next_day_index: 23
- Day 22 card audit: complete
- closeout_event_id: `closeout`
- closeout_started_at: `2026-10-25T15:01:36.242476+08:00`
- research_status: closeout-only

本卡的结果是可追溯的几何、声子与实验判据，并纠正继承的过强排他结论。相近能谱、强 E2、相近 alignment 各有检验力；模式指认仍需逐线身份、混合比选解、强度归一和模型适用域共同约束。新增内容保持 `needs_review: true`，没有新增人工审核。

### Day 22 card completion audit

| Day-matrix deliverable | Evidence locator / artifact | Status |
|---|---|---|
| 回忆：TW/LW、phonon、带外 E2 与 M1/E2 比值 | [判据卡](../../knowledge/methods/wobbling-criteria-card.md)；[读源后理解校核](20261024-DAY22-wobbling-geometry-phonon-observables-run-01/understanding-check-123.md)；下文 Theory/analysis exercise | complete |
| 主线：wobbling-motion、F14、H03 | [概念页](../../knowledge/concepts/wobbling-motion.md)；[同 SHA 主线及视觉复核](20261024-DAY22-wobbling-geometry-phonon-observables-run-01/source-mainline-recheck-121.json) | complete |
| 练习：候选带四列证据 | [四列观测合同](../../knowledge/methods/wobbling-geometry-phonon-observable-contract.md)；下文实验矩阵 | complete |
| 反证：135Pr 检验“近简并＋强 E2”充分性 | [135Pr 争议项目](../../knowledge/projects/135pr-wobbling-controversy.md)；L22-D22-R095-1 | complete |
| 交付：必要检验、支持条件和反证的判据卡 | [wobbling criteria card](../../knowledge/methods/wobbling-criteria-card.md) | complete |

Day23 只覆盖无学分预习，本轮不授分；未打开 Day24。实际状态转移和发布结果分别以本 run 的 card-credit-22、run.json 和任务发布回执为准，不由历史 checkpoint 的“全绿”字样代替。

## Candidate pool and selection

| 已选择的问题 | 本轮解决的范围 | 仍需的输入 |
|---|---|---|
| 几何、谐近似与非谐拓扑 | 主轴映射、冻结 j 的非零 M1、小角域、有限矩阵控制、不同 wobbling 定义 | 完整 QTR/多体 producer 和实际跨自旋跃迁算符未重跑 |
| Lu 实验与声子阶梯 | 逐带/逐线身份、两混合比根、共同母态分母和两次采集谱系 | 476 keV 偏振及逐带绝对寿命；Schmitz/Görgen 原文路径尚未闭合 |
| 135Pr/187Au 支持与反证 | 修复 P/δ 混线、错误绝对尺度和独立性；保留双方实际证据 | 原计数、响应、取向与共同协方差/似然 |
| 当前计数与 g/orientation 分析 | matched-null 条件检验/区间；三重积均值、RMS 和 Gram 代理的区别 | 实际校准/背景/计数率；GR18 Ref14 正文与算符约定 |
| Day23 已有预习 | SP/TiP/MR 逐量比较与独立寿命对照 | 留待 Day23 正式 run 审计，不预授学分 |

13:30 门后未取得新科学来源、开启新课程卡或增加新研究路线；只完成已经打开的分析、核心原文回读和一致性检查。研究按原定 15:00 截止收束，不把局部饱和解释成全局科学问题已解决。

## Sources and evidence

| 直接来源入口（单一原子 locator） | 实际覆盖及作用 | 独立性/使用边界 |
|---|---|---|
| [F14](../../knowledge/sources/frauendorf-2014-transverse-wobbling.md) · F14-D22-R091-1 | 同 SHA 十二页主线文本回读；视觉核 p6 Eqs11–24 | 理论 HFA/完整 QTR，不是新增采集；Pr 实验值为 Matta 发表前通信 |
| [H03](../../knowledge/sources/hamamoto-2003-quantized-wobbling-excitations-alignments.md) · H03-D22-R091-1 | 同 SHA 五页主线文本回读；视觉核 p3–4 Eq14/Figs2–4 | 对已有 Lu 实验的模型比较，保留能谱与非谐限制 |
| [OD01](../../knowledge/sources/odegard-2001-evidence-wobbling-163lu.md) · OD01-D22-R092-1 | 四页全文文本回读及 p5869 视觉核；电性质选解、相对 B | 152 MeV/2.4×10⁹ 采集；未打印数值 P、未新测 TSD2 寿命 |
| [JE02](../../knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md) · JE02-D22-R092-2 | 四页全文文本回读及 p2–4 视觉核；TSD3 网络/双根 | 157 MeV/6×10⁹ 新采集；一声子解释及 δ 基准仍依赖旧文 |
| [Lv 135Pr](../../knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md) · L22-D22-R095-1 | 主文与关键 SI/逐线表、实际 P–Rac 对照 | 与 Matta 不同采集；不同源 A/P 不能直接混用 |
| [SH26](../../knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md) · SH26-D22-R095-1 | 定向 PDF14–15/Fig12 条件 χ² 与 QTR 回应 | 旧数据重分析不算新独立实验；非完整 nuisance profile |
| [105Pd](../../knowledge/sources/timar-2019-transverse-wobbling-105pd.md) · TI19-D22-R103-1 | 六页主线及关键 DCO/P/TableI 核验 | 独立支持案例保留；参数定标点与额外检验点分开 |
| [136Nd](../../knowledge/sources/lv-2022-transverse-wobbling-136nd.md) · LV22-D22-R091-1 | 主线及 Figs3–5/唯一可分析线 | 相对 B 与单点定标；没有旧任务所称的该带对 DSAM 塌缩 |

详细 SHA、SI 范围、其它比较来源和未覆盖内容见各 source 页及 source-mainline-recheck-121/122；公开获得的 FD2015 accepted 稿仍为只读 staging，未冒称正式新 source/raw 摄入。书目命中不提供未读的寿命数值。

## Theory/analysis exercise

TW/LW 首先是在所用粒子–转子约定下，准粒子 j 垂直/平行最大惯量轴的几何分类；跨文献须映射主轴和惯量排序。harmonic phonon 还涉及局部稳定、小角量子化与能量/矩阵元阶梯，不能由两带相近就给声子数。完整非谐拓扑与 Lawrie 的谐声子定义存在术语/适用域差异，实际 δ 冲突仍需实验检验。

同一条 M1/E2 混合线的 E2 光子份额为 δ²/(1+δ²)；同母态两条退激的 rE2 则还含光子分支和 Eγ⁵，二者不同。共同寿命在相对比中抵消，但缺寿命时不产生绝对 B 或 W.u.；rM1 的单位是 μN²/(e²b²)。能谱参考扣除的 i_x 与角分布的 σ/I 也是两类 alignment，均不直接测得进动锥。

[F14](../../knowledge/sources/frauendorf-2014-transverse-wobbling.md) · F14-D22-R091-1 的 Eq21 明确在冻结内禀 j 时仍有非零 M1。不能据 M1 占优唯一判剪刀，也不能设跨核统一 δ、W.u. 或小角阈值。有限自旋控制是明示 Hamiltonian 的数学结果，不是原 QTR 程序或实测核态。

### Four-column evidence exercise

| 候选带 / 原子出处 | Band energy | In/out strengths | Alignment | Polarization |
|---|---|---|---|---|
| 163Lu TSD2/TSD1 · OD01-D22-001 | 分离约250–300 keV、随spin下降 | 平均δ=−3.10(+.36/−.44)，90.6(1.3)% E2；43/2支路λ=.36(.04)，相对B | i_x/J(2)相近；σ/I另列为磁子态宽度 | electric性质排小根；未打印可引用的P正负/数值 |
| 163Lu TSD3/TSD2 · JE02-D22-002 | 四条ΔI=1；另八条到TSD1的ΔI=2 | 476/627同母态；rE2=.51(.13)或.019(+.024/−.017) | TSD2/3相对i_x差约.1ℏ，支持family | 476偏振未测成；大根还依赖family/PRM |
| 135Pr side/yrast · L22-D22-R095-1 | 下降曲线保留，TW2网络有重新分组 | 813 rE2由Matta .843(.032)到Lv .12(.08)，是跨实验中央比 | QTR重取向为模型结果 | 747 P+.04配δ−.47；813 P−.03配δ−.37，勿混线 |
| 136Nd L3/L1 · LV22-D22-R091-1 | 作者报告下降Ewob | 751 δ−.48、rE2=.36(.17)、rM1=.61(.29)，无本篇新τ | 刚性j=10为模型输入 | 仅751可联合分析，另三条弱/污染 |
| 187Au bands2/1 · GU22-D22-R094-1 | 上升Ewobb可有不同解释 | 新δ约−.26/−.28；数W.u.依赖外部带内尺度 | PRM/QTR费米位置和输入不同 | 新P–Rac与旧AD大根冲突；完整共同似然未得 |
| 105Pd B/A · TI19-D22-R103-1 | Ewob降至29/2；高spin组态变化另列 | 三线rE2=.66/.60/.34，均相对量 | CDFT/惯量是模型及拟合输入 | 负P联合DCO支持大正δ；g_eff×.36有定标点 |

表中伴随输入的原子出处（summary/note）：OD01-D22-002；JE02-D22-001；L22-D22-R095-2；M15-D22-R095-1；LV22-D22-R091-2；GU22-D22-R094-2；TI19-D22-R103-2；TI19-D22-R103-3。

矩阵的其它输入和确切逐线出处保存在[四列观测合同](../../knowledge/methods/wobbling-geometry-phonon-observable-contract.md)和各 source；表内来源分别沿上述唯一原子 ID 回查，不把多个派生量当多次独立采集。

### Quantitative controls and limits

| 控制 | 实际结果 | 只允许得出的结论 |
|---|---|---|
| JE02打印中心重建 | rE2≈.5154/.01934；同母态out/out约.035/.94 | 两个δ解释的敏感性，不是实测强度塌缩；.51/.21另含不同带内尺度 |
| 临界冻结j人工族 | HFA曲率零时有限隙仍正；指定标度趋四次振子隙2.73931 | 近似与完整有限矩阵的条件差别，非真实核的临界拟合 |
| matched-null四计数 | chosen表给P=.3、单侧p≈.03463；central95区间[−.02326,.62077] | 仅shared response、独立raw cells和knownQ模型；非实际机时/实验CI |
| 三矢量operator控制 | chosen伸展态signedχ/RMS均0而Gram代理≈.33235 | 平均几何代理与真实算符矩不能互换；非GR18 producer识别/论文错误裁决 |

Lu重建和临界族的原子出处（summary/note）为JE02-D22-R092-3、F14-D22-R106-1；模型限制另见F14-D22-R106-2。

计数和算符的原子推导分别见 [Miller source](../../knowledge/sources/miller-2007-sega-polarization.md) · MI07-D22-R118-1、[GR18 source](../../knowledge/sources/grodner-2018-128cs-chiral-g-factor.md) · GR18-D22-R119-1。所有人工计数、参数、packet及有限矩阵明确不当作新实验。

## Counter-evidence and missing companion observables

135Pr 是本卡的主要反向检验：早期 E2-rich/下降能差支持 TW；独立 P–Rac 数据提出小δ及 TiP 解释，SH26 又保留固定取向 AD 的大根偏好。近能量＋强E2不能独立给唯一声子标签；也不能由支持链受挑战就断言 TiP 唯一成立。需要共同门/背景、a/Q、取向与δ候选的联合检验，以及未被该点定标的模型预测或伙伴态寿命。

[OD01](../../knowledge/sources/odegard-2001-evidence-wobbling-163lu.md) · OD01-D22-R122-1 的交替低能支路没有有效上限，不能补为零。[JE02](../../knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md) · JE02-D22-R122-1 的rM1上限.012属于选大δ后的比较；不是独立选根证据或绝对B上限。

继承的135Nd“.9356±.0102”是五个sqrtB中央比的均值/散布，不是Qt置信区间；37/2→39/2两带中央E2降幅约2.46/2.64，不能恢复旧严格排他认证。见[MU07](../../knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md) · MU07-D22-R102-1。225.8 keV的P正号与16.3/45.3h认证已撤回，实际响应/率/核模型尚不足，见[LV19](../../knowledge/sources/lv-2019-chirality-135nd-reexamined.md) · LV19-D22-R110-3。Day21正式[21]与18/24保留，课程信用不替科学证明。

## Knowledge Impact and Learning Decision

本轮将几何定义、谐近似、完整模型、逐线实验和任务数学重建分别写入 canonical knowledge。保留真实支持与反证，撤回未核的普适数值硬门、全核区唯一、缺测等于零和跨带/跨核寿命移植。091/097的隔离账本及114个旧producer脚本归档保留失败历史；恢复基线不等于对所有继承科学文字重新认证。

新的必要伴随观测集中在两处：原始响应与共同似然能否区分δ候选；未用于定标的寿命/电磁/磁矩观测能否检验模型。GR18的原算符约定仍开放，不用任务数学强行替原作者改式。所有新增科学条目保持needs_review，不设置human-reviewed。

## Durable knowledge delta

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
      "anchor": "| F14-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/hamamoto-2003-quantized-wobbling-excitations-alignments.md",
      "anchor": "| H03-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/hamamoto-2003-quantized-wobbling-excitations-alignments.md",
          "locator": "H03-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
      "anchor": "| OD01-D22-R092-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
      "anchor": "| JE02-D22-R092-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2022-transverse-wobbling-136nd.md",
      "anchor": "| LV22-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-transverse-wobbling-136nd.md",
          "locator": "LV22-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chen-2019-transverse-wobbling-even-even.md",
      "anchor": "| CH19-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2019-transverse-wobbling-even-even.md",
          "locator": "CH19-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zamfir-casten-1991-gamma-softness-triaxiality.md",
      "anchor": "| ZC91-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/zamfir-casten-1991-gamma-softness-triaxiality.md",
          "locator": "ZC91-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/guo-2024-chiral-wobbler-74br.md",
      "anchor": "| GU24-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2024-chiral-wobbler-74br.md",
          "locator": "GU24-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-criteria-card.md",
      "anchor": "## 必要检验、支持条件与反证",
      "summary": "按模型定义/小角域/实验支持分层，撤回跨核统一数值门。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        },
        {
          "path": "knowledge/sources/chen-2019-transverse-wobbling-even-even.md",
          "locator": "CH19-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/minimal-wobbling-identification-protocol.md",
      "anchor": "## 逐项程序",
      "summary": "将原子身份、选解、相对强度、模型/声子有效域分别检验。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        },
        {
          "path": "knowledge/sources/lv-2022-transverse-wobbling-136nd.md",
          "locator": "LV22-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## HFA局部重建与失效域",
      "summary": "保留有原件的曲率与小角公式，不把有限模型对照当核素实验。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## checkpoint091 可复核的算符与参考抵消",
      "summary": "FA仍有非零M1；公共Harris参考等频抵消，不虚报核素漂移。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        },
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## checkpoint092 163Lu直接观测边界",
      "summary": "修正OD01偏振/寿命范围及JE02跨两声子退激。",
      "sources": [
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-R092-1"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/interband-e2-strengths.md",
      "anchor": "## Day22相对比值、绝对强度与声子归一（checkpoint092）",
      "summary": "重建相对B，揭示r21/r10不同带内分母；不推绝对W.u.。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-3"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/wobbling-motion.md",
      "anchor": "## Day22偶偶核追加裁决撤回（checkpoint092）",
      "summary": "撤回M1占优必否证及未绑定寿命表改判。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-transverse-wobbling-136nd.md",
          "locator": "LV22-D22-R091-1"
        },
        {
          "path": "knowledge/sources/chen-2019-transverse-wobbling-even-even.md",
          "locator": "CH19-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/transverse-wobbling.md",
      "anchor": "## Day22横向几何与声子有效域校准（checkpoint092）",
      "summary": "修正唯一基准、能量单调及HFA等同完整QTR的量词。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-003"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/longitudinal-wobbling.md",
      "anchor": "## Day22 checkpoint094：分类与可迁移边界",
      "summary": "不把特定费米面模型条件泛化为全部低spin核严格禁戒。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/wobbling-energy.md",
      "anchor": "## Day22能量解释边界校准（checkpoint092）",
      "summary": "保持派生能量对象和模型域，不由斜率唯一分类。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/experimental-wobbling-evidence-strength-map.md",
      "anchor": "| WOB-EXP-11 |",
      "summary": "重新校准高spin实验的多声子支持和偏振缺口，不作全区穷尽结论。",
      "sources": [
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-R092-1"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
      "anchor": "| F14-D22-R092-1 |",
      "summary": "定向原件核Fig.19所指Ref.25的字面身份疑点；不判数据错误或静默替换原引用。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R092-1"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "JT01-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
      "anchor": "| JT01-D22-R092-1 |",
      "summary": "首页/摘要身份核：165Tm的DSAM论文不直接提供163Lu TSD寿命，本轮不是全文重读。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "JT01-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lawrie-2020-tilted-precession-wobbling.md",
      "anchor": "| LAW20-D22-R093-1 |",
      "summary": "定向核作者冻结j、谐n规则和典型参数域，保留解释范围。",
      "sources": [
        {
          "path": "knowledge/sources/lawrie-2020-tilted-precession-wobbling.md",
          "locator": "LAW20-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
      "anchor": "| CF22-D22-R093-1 |",
      "summary": "定向核Sec4.6对Lawrie的定义回应；非谐拓扑并非新独立实验。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2024-wobbling-review.md",
      "anchor": "| F24-D22-R093-1 |",
      "summary": "核SSS真实有限Fourier定义，区别于Bogoliubov本征态压缩。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## checkpoint093 定义、有效域与模型比较合同",
      "summary": "分开定义、谐近似有效域和完整模型观测预测，列出条件AMGM下界。",
      "sources": [
        {
          "path": "knowledge/sources/lawrie-2020-tilted-precession-wobbling.md",
          "locator": "LAW20-D22-R093-1"
        },
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/spin-squeezed-state-map.md",
      "anchor": "## Day22 SSS定义纠错（checkpoint093）",
      "summary": "修正旧045定义并给密度矩阵角表示归一核控制，非核素测量。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/spin-coherent-state-map.md",
      "anchor": "## Day22 SCS相位、测度与模式边界（checkpoint093）",
      "summary": "区分体固符号与概率测度，撤回通用电磁硬门和模型图像实测化。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R093-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/wobbling-motion.md",
      "anchor": "## Day22 模式与谐近似的定义分歧（checkpoint093）",
      "summary": "并列两派定义，不把近似域判决直接替代实验模式裁决。",
      "sources": [
        {
          "path": "knowledge/sources/lawrie-2020-tilted-precession-wobbling.md",
          "locator": "LAW20-D22-R093-1"
        },
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/low-spin-wobbling-gamma-soft-deformation-and-alternative-interpretations.md",
      "anchor": "## Day22 thematic REFLECT：争议定义与观测合同校准（checkpoint093）",
      "summary": "三来源定义/有效域比较的专题反思；撤回旧全区终审并保留实验δ冲突与独立预测问题。",
      "sources": [
        {
          "path": "knowledge/sources/lawrie-2020-tilted-precession-wobbling.md",
          "locator": "LAW20-D22-R093-1"
        },
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
      "anchor": "| GU22-D22-R094-1 |",
      "summary": "新混合比、旧P身份、误差范围与继承错误校正。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-1"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-2"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md",
      "anchor": "| AU20-D22-R094-1 |",
      "summary": "支持实验的相对比、伴随SP身份与PRM输入范围。",
      "sources": [
        {
          "path": "knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md",
          "locator": "AU20-D22-R094-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/187au-longitudinal-wobbling-controversy.md",
      "anchor": "## Day22 checkpoint094：恢复开放争议与逐量对照",
      "summary": "撤回88倍/4σ及终审，保留源间独立性与共同响应缺口。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-2"
        },
        {
          "path": "knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md",
          "locator": "AU20-D22-R094-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/longitudinal-wobbling.md",
      "anchor": "## Day22 checkpoint094：分类与可迁移边界",
      "summary": "撤回普适费米面禁戒，回到具体模型及观测冲突。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-3"
        },
        {
          "path": "knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md",
          "locator": "AU20-D22-R094-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/experimental-wobbling-evidence-strength-map.md",
      "anchor": "## Checkpoint094：187Au独立性与强度纠错",
      "summary": "纠正P/δ、conversion与二声子身份依赖错误。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-1"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "- [ ] `187Au` 的376/462",
      "summary": "恢复真实未解决问题，撤回88倍与新4σ认证。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-1"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
      "anchor": "| M15-D22-R095-1 |",
      "summary": "逐线A/δ与实验/模型列身份、完整QTR重取向边界。",
      "sources": [
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-D22-R095-1"
        },
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-D22-R095-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
      "anchor": "| L22-D22-R095-1 |",
      "summary": "逐线P/δ与同母态比值重建，不擅报3σ或物理塌缩。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-1"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-2"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
      "anchor": "| SH26-D22-R095-1 |",
      "summary": "保留固定σ/I条件χ²证据，撤回浮动必等深与最终TiP认证。",
      "sources": [
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/135pr-wobbling-controversy.md",
      "anchor": "## Day22 checkpoint095：撤回最终TiP裁决，恢复逐线争议",
      "summary": "重开实际response与模型差异问题。",
      "sources": [
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-D22-R095-2"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-1"
        },
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/signature-tip-shears-discrimination-contract.md",
      "anchor": "## 逐项比较程序",
      "summary": "撤回跨核硬门，预习改为逐量竞争解释比较。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-3"
        },
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/wobbling-vs-signature-partner.md",
      "anchor": "## Day22 checkpoint095：机制比较的适用边界",
      "summary": "撤回M1百分比到模式的唯一映射。",
      "sources": [
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-D22-R095-1"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "- [ ] `135Pr` 的独立P–Rac",
      "summary": "量身份和源间冲突保持开放，未形式终审。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-1"
        },
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
      "anchor": "| YA67-D22-R096-1 |",
      "summary": "A4条件识别推导及非负有限J布居歧义见证；非实测拟合。",
      "sources": [
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-1"
        },
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/multipole-mixing-ratio.md",
      "anchor": "## Day22 checkpoint096：A4能否选根取决于取向和响应",
      "summary": "撤回普适双根、偏振正号和精度硬门，给出有条件反演。",
      "sources": [
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-1"
        },
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/high-spin-angular-polarization-mixing-ratio.md",
      "anchor": "## Day22 checkpoint096：A4能否选根取决于取向和响应",
      "summary": "已知取向和自由张量模型分开，保留SH26条件证据。",
      "sources": [
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-2"
        },
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "anchor": "## Day22 checkpoint096：A4能否选根取决于取向和响应",
      "summary": "为实数两成分单γ模型提供反演条件与正布居反例。",
      "sources": [
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-1"
        },
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "- [ ] `A2/A4`、偏振及取向/响应",
      "summary": "收缩不可辨识性的量词，实际响应/Cov缺口仍开放。",
      "sources": [
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-1"
        },
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "#### 偏振和角分布的条件选解",
      "summary": "清除旧跨阵列精确吻合和普适正偏振定理，回到逐线与条件A4证据。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-1"
        },
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
      "anchor": "| AG07-D22-R098-1 |",
      "summary": "比值先升后降；43/2原打印强度与比值未闭合，模型/实验分层。",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-D22-R098-1"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-D22-R098-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
      "anchor": "| CHI01-D22-R098-1 |",
      "summary": "核实际寿命态与alignment上扬，撤回错spin轨迹。",
      "sources": [
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-D22-R098-1"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-D22-R098-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/signature-tip-shears-discrimination-contract.md",
      "anchor": "## Day22 checkpoint098：Day23无学分预习的独立磁转动对照",
      "summary": "独立ratio/absolute链对照，不迁寿命或固定硬门。",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-D22-R098-1"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-D22-R098-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/wobbling-vs-signature-partner.md",
      "anchor": "## Day22 checkpoint098：Day23无学分预习的独立磁转动对照",
      "summary": "保留MR组态变化处非单调与逐门输入缺口。",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-D22-R098-2"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-D22-R098-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
      "anchor": "| DO99-D22-R099-1 |",
      "summary": "Qt寿命谱系、SD–ND对象与未分辨线/新旧campaign边界。",
      "sources": [
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-1"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-2"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/interband-e2-strengths.md",
      "anchor": "## Day22 checkpoint099：163Lu的SD–ND E2对照",
      "summary": "同核相对E2/两态混合控制，避免外标Qt迁为SD2τ。",
      "sources": [
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-1"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-2"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## Day22 checkpoint099：163Lu的SD–ND E2对照",
      "summary": "为近能量与强E2非充分性增加有对象映射的SD–ND例。",
      "sources": [
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-1"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-2"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
      "anchor": "| JE02-D22-R100-1 |",
      "summary": "逐线共母态/分母映射与双带外E2比、依赖边界。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R100-1"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R100-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/interband-e2-strengths.md",
      "anchor": "## Day22 checkpoint100：同母态out/out能消去什么",
      "summary": "区分同母态消尺度和跨带不同归一的声子比较。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R100-1"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R100-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
      "anchor": "| CF22-D22-R101-1 |",
      "summary": "实际勘误图与RMS不重建SCS的正性条件控制。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R101-1"
        },
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R101-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/spin-coherent-state-map.md",
      "anchor": "## Day22 checkpoint101：相同RMS可以对应不同SCS图",
      "summary": "三RMS/完整密度、测度与实验解释边界。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R101-1"
        },
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R101-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "| MU07-D22-R102-1 |",
      "summary": "继承统计量/图号/手征对称性与模型临界边界纠正。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D22-R102-1"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D22-R102-2"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D22-R102-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
      "anchor": "| LV21-D22-R102-1 |",
      "summary": "低spinTiP带族与三准粒子手征pair、campaign依赖分层。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
          "locator": "LV21-D22-R102-1"
        },
        {
          "path": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
          "locator": "LV21-D22-R102-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "## Day22 checkpoint102：135Nd模式判别先绑定带族与统计量",
      "summary": "原支持解释保留，撤回Qt精密排他和同核跨组态否证。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D22-R102-1"
        },
        {
          "path": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
          "locator": "LV21-D22-R102-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
      "anchor": "| TI19-D22-R103-1 |",
      "summary": "独立DCO/P支持、大δ/负P、相对强度与g_eff定标范围。",
      "sources": [
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-1"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-2"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/experimental-wobbling-evidence-strength-map.md",
      "anchor": "## Day22 checkpoint103：保留105Pd的独立支持链",
      "summary": "保留正常形变实质支持和C带/组态/定标限制。",
      "sources": [
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-1"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-2"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-criteria-card.md",
      "anchor": "## 模型定标与独立检验点：105Pd控制",
      "summary": "区分g_eff幅度定标与额外可检验观测，不预先否决有调节模型。",
      "sources": [
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-1"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-2"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
      "anchor": "| NOM22-D22-R104-1 |",
      "summary": "保留IBFM实质预测、127Xe例外与二手表误差/校准边界。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-1"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-2"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/low-spin-wobbling-gamma-soft-deformation-and-alternative-interpretations.md",
      "anchor": "## Day22 checkpoint104：竞争模型比较需保留完整观测向量",
      "summary": "整M1算符标度不修复E2向量；反方不作最终实验裁决。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-1"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-2"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/multipole-mixing-ratio.md",
      "anchor": "## Day22 checkpoint104：竞争模型比较需保留完整观测向量",
      "summary": "δ比例、绝对强度与算符/数据版本校准分层。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-1"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-2"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2024-wobbling-review.md",
      "anchor": "| F24-D22-R105-1 |",
      "summary": "Fig35绝对量/比值标签、LL模型与邻核转述限定。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-2"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-criteria-card.md",
      "anchor": "## Day22 checkpoint105：wobbling–scissors耦合不同于磁转动分类",
      "summary": "isovector scissors与valence shears分层，不把M1淬火作唯一模式证明。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-2"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/low-spin-wobbling-gamma-soft-deformation-and-alternative-interpretations.md",
      "anchor": "## Day22 checkpoint105：wobbling–scissors耦合不同于磁转动分类",
      "summary": "保留QRPA的E2缺陷、校准和转述差异，公开伴随未正式raw/source摄入。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-2"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
      "anchor": "| F14-D22-R106-1 |",
      "summary": "人工临界族的四次回复项/有限spin隙与渐近域，非核实验。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## checkpoint106：HFA软化的有限spin四次势控制",
      "summary": "区分局部谐近似软化与完整有限谱、固定I与实测Ewob。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/wobbling-energy.md",
      "anchor": "## Day22 checkpoint106：谐频零不等于有限谱隙零",
      "summary": "五限定控制及完整模型/真实观测边界。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
      "anchor": "| SHJ24-D22-R107-1 |",
      "summary": "扩展Lu/Ta实读，绝对B/归一比、K与等价γ扇区分层。",
      "sources": [
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-D22-R107-1"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-D22-R107-2"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-D22-R107-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2024-wobbling-review.md",
      "anchor": "| F24-D22-R107-1 |",
      "summary": "TPSM的suppressed须说明比较量，不误读为缺测/零。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R107-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## checkpoint107：K标签与等价γ扇区不是新物理模式",
      "summary": "轴置换不变量与完整输入一致变换，不把K/坐标当物理模式。",
      "sources": [
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-D22-R107-2"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-D22-R107-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
      "anchor": "| NOM22-D22-R108-1 |",
      "summary": "v²只是模型输入；exchange与PES不可识别Majorana方向分开。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R108-1"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R108-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2024-wobbling-review.md",
      "anchor": "| F24-D22-R108-1 |",
      "summary": "softcore/TPSM作者比较不变成普适softness禁戒或无Pauli断言。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R108-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/gamma-soft-vs-gamma-rigid-diagnostics.md",
      "anchor": "## Day22 checkpoint108：γ-soft不是模式禁止条件，PES不定标全部M1",
      "summary": "core交错、basis参数、PES约束与动态磁性残余项分层。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R108-2"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R108-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-criteria-card.md",
      "anchor": "## Day22 checkpoint108：γ-soft不是模式禁止条件，PES不定标全部M1",
      "summary": "补充参数识别/交换处理边界，不用统一阈值裁模式。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R108-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R108-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/wobbling-motion.md",
      "anchor": "## Day22 checkpoint109：声子代数是局部近似，基占据不等声子标签",
      "summary": "明确finite-spin局部代数、nK/nw与真实E2阶梯的区别；任务条件练习。",
      "sources": [
        {
          "path": "knowledge/sources/hamamoto-2003-quantized-wobbling-excitations-alignments.md",
          "locator": "H03-D22-002"
        },
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## Day22 checkpoint109：声子代数是局部近似，基占据不等声子标签",
      "summary": "明确finite-spin局部代数、nK/nw与真实E2阶梯的区别；任务条件练习。",
      "sources": [
        {
          "path": "knowledge/sources/hamamoto-2003-quantized-wobbling-excitations-alignments.md",
          "locator": "H03-D22-002"
        },
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
      "anchor": "| LV19-D22-R110-1 |",
      "summary": "核三线实际身份/缺δ，撤回未校准机时与Psign模式排他。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-2"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/taras-1971-phase-defined-polarization-formulas.md",
      "anchor": "| T71-D22-R110-1 |",
      "summary": "混合线Stokes/强度含干涉，源p与现代P不可混。",
      "sources": [
        {
          "path": "knowledge/sources/taras-1971-phase-defined-polarization-formulas.md",
          "locator": "T71-D22-R110-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day21-135nd-same-input-falsification-design.md",
      "anchor": "## Day22 checkpoint110：撤回旧排他机时方案，保留可执行的输入清单",
      "summary": "provisional设计恢复共母态/响应/Θ/功效输入要求，旧128–141认证移历史。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-3"
        },
        {
          "path": "knowledge/sources/taras-1971-phase-defined-polarization-formulas.md",
          "locator": "T71-D22-R110-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/high-spin-angular-polarization-mixing-ratio.md",
      "anchor": "## Day22 checkpoint110：225.8keV设计不能由P正号直接裁模式",
      "summary": "区分假设分离和正号检验，不造新设施预算。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-2"
        },
        {
          "path": "knowledge/sources/taras-1971-phase-defined-polarization-formulas.md",
          "locator": "T71-D22-R110-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/miller-2007-sega-polarization.md",
      "anchor": "| MI07-D22-R111-1 |",
      "summary": "计数层/倒数a约定与已知校准方差、未知a识别边界。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/compton-polarimetry.md",
      "anchor": "## Day22 checkpoint111：同一计数预算先区分样本与校准",
      "summary": "全Jacobian/Σ与target-only校准退化，不造实际阵列σ。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day21-135nd-same-input-falsification-design.md",
      "anchor": "## Day22 checkpoint111：pilot与双bin统计合同",
      "summary": "provisional设计把raw/selected/background/a/Q/Θ分层。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## Day22 checkpoint112：静态g的独立标量约束与几何边界",
      "summary": "本任务定义的一j磁矩模型代数/CG控制，不是源论文新g数据或模式唯一反演。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-3"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D19-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-criteria-card.md",
      "anchor": "## Day22 checkpoint112：静态g的独立标量约束与几何边界",
      "summary": "本任务定义的一j磁矩模型代数/CG控制，不是源论文新g数据或模式唯一反演。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-3"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/compton-polarimetry.md",
      "anchor": "## Day22 checkpoint113：效应分离度不等检验功效",
      "summary": "旧未验证均值下的exactbinomial目标诊断，z/α/功效分开，不作核/设施预算。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-3"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day21-135nd-same-input-falsification-design.md",
      "anchor": "## Day22 checkpoint113：效应分离度不等检验功效",
      "summary": "旧未验证均值下的exactbinomial目标诊断，z/α/功效分开，不作核/设施预算。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-3"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
      "anchor": "| GR18-D22-R114-1 |",
      "summary": "signedχ/RMS/Gram定义问题明确为条件待核，不改实验g或原式。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-1"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "## Day22 checkpoint114：g与三矢量几何需说明order parameter",
      "summary": "标量g/期望/方差/代理分开，条件packet不作核band证明。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-1"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "## Day22 checkpoint114：三矢量orientation定义待核",
      "summary": "Ref14metadata已核、body/producer未得，保留定向问题而非结案。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-1"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/miller-2007-sega-polarization.md",
      "anchor": "| MI07-D22-R115-1 |",
      "summary": "shareda/独立raw cells条件下的matched-null检验，非实际实验。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/compton-polarimetry.md",
      "anchor": "## Day22 checkpoint115：独立matched-null四计数的条件检验",
      "summary": "四计数/校准匹配/条件统计边界，不作真实预算。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day21-135nd-same-input-falsification-design.md",
      "anchor": "## Day22 checkpoint115：独立matched-null四计数的条件检验",
      "summary": "四计数/校准匹配/条件统计边界，不作真实预算。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
      "anchor": "| GR18-D22-R116-1 |",
      "summary": "完全伸展态signed/RMS零但Gram代理非零；保留作者定义问题。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R116-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "## Day22 checkpoint116：伸展态中的算符与代理差别",
      "summary": "非线性期望顺序不能互换；非核态/原论文算法认证。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R116-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/miller-2007-sega-polarization.md",
      "anchor": "| MI07-D22-R118-1 |",
      "summary": "同一chosen四cell模型的exact conditional区间/单侧与双侧标准，不作实际CI。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R118-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/compton-polarimetry.md",
      "anchor": "## Day22 checkpoint118：检验方向与区间尾部一致",
      "summary": "同一chosen四cell模型的exact conditional区间/单侧与双侧标准，不作实际CI。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R118-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day21-135nd-same-input-falsification-design.md",
      "anchor": "## Day22 checkpoint118：检验方向与区间尾部一致",
      "summary": "同一chosen四cell模型的exact conditional区间/单侧与双侧标准，不作实际CI。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R118-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
      "anchor": "| GR18-D22-R119-1 |",
      "summary": "独立lab自旋平方三重积的任务精确关联式/定义边界，非原producer识别。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R119-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "## Day22 checkpoint119：平均几何量遗漏哪些关联",
      "summary": "独立lab自旋平方三重积的任务精确关联式/定义边界，非原producer识别。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R119-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/antimagnetic-rotation.md",
      "anchor": "## checkpoint081追加认证撤回（checkpoint091）",
      "summary": "撤回缺原表和普适阈值的旧任务认证，108In只作实测强度来源边界对照。",
      "sources": [
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-D22-R098-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/flip-mode.md",
      "anchor": "## checkpoint077追加认证撤回（checkpoint091）",
      "summary": "撤回任意FM数值分区和未证物理认证，保留局部近似域。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "## Day22几何、声子与观测合同",
      "summary": "Day22已存在知识/来源导航，非新增科学证据。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2018-comment-wobbling-stability.md",
      "anchor": "| FC18-1 |",
      "summary": "本run已读评论的理论范围/惯量排序与近似边界，非新实验。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2018-comment-wobbling-stability.md",
          "locator": "FC18-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/tanabe-2018-reply-wobbling-stability.md",
      "anchor": "| TR18-1 |",
      "summary": "本run已读回复的理论判据/近似边界，非对2020/2022实验的回复。",
      "sources": [
        {
          "path": "knowledge/sources/tanabe-2018-reply-wobbling-stability.md",
          "locator": "TR18-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
      "anchor": "| OD01-D22-R122-1 |",
      "summary": "既有原件限定缺测、选根条件上限和真实响应输入，不作新数据/排他认证。",
      "sources": [
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-R122-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
      "anchor": "| JE02-D22-R122-1 |",
      "summary": "既有原件限定缺测、选根条件上限和真实响应输入，不作新数据/排他认证。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R122-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/minimal-wobbling-identification-protocol.md",
      "anchor": "## Day22 checkpoint122：缺测、条件上限和实际响应",
      "summary": "既有原件限定缺测、选根条件上限和真实响应输入，不作新数据/排他认证。",
      "sources": [
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-R122-1"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R122-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/overview.md",
      "anchor": "## Current Snapshot: 2026-10-25 Day22 evidence audit",
      "summary": "同步本次实际治理计数、来源使用边界和QMD deferred；统计来自lint，不是实验或全库科学认证。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        }
      ]
    }
  ]
}
```


## Open questions and belief revision

1. 135Pr/187Au的共同数据处理和响应域未复现，争议保持开放。
2. Lu逐带绝对寿命谱系未闭合；F14 Ref25字面书目对象与Lu数据引用存在身份疑点，不能由此判数据虚假或补造τ。
3. 137Pr 43/2打印分支重建不闭合；不调输入强配。108In独立寿命不能移植到137Pr。
4. matched-null校准若响应不匹配，零偏振可模拟目标对比；真实Q、背景、selected rate和物理null仍缺。
5. GR18 Ref14正文/producer约定未得；signedχ、RMS、Gram代理不同，实验g不因此改写。
6. Day23预习留待正式run重新审计；未打开Day24。

开放问题的canonical入口为[questions](../../knowledge/questions.md)。源页未读范围和模型/实验边界继续保留。

## L0–L4 state

L1/L2完成本卡主线、原件定位和判据校准；L3形成共同观测与反证问题；L4限于打印输入重建及明示假设的数学/统计控制。没有原始event refit、实验CI重标或原多体producer复现。科学partial不被写成问题闭环。

Agent self-audit：未隔离技术hard P0为none identified；P1为source lineage、δ/response/取向/协方差、绝对尺度与operator约定；P2/P3包括source citation-key缺口、导航和格式。不存在新增human-reviewed promotion，原有人工审核范围不因本次正文更新扩张。

## Verification and continuation

原runner使用本run baseline验证全部变更知识页、唯一writeback、固定标题与课程覆盖；此前辅助检查遗漏的标题/backlink/映射问题已在120修补，原失败回执保留。正式检查与最新两个已改控制脚本的实际结果见required-checks-closeout.json及run.json的checks，结构通过不认证全库科学真值。

protected Bib/PLAN哈希与启动基线相同。QMD refresh/embed/cleanup明确deferred：安装wrapper固定到项目外旧缓存，当前使用rg/direct read；未改外部缓存或全局配置。overview只同步本次实际治理计数。

原clock monitor曾停于manual-attention-required；不把旧PID/心跳算作持续研究证明。当前同一thread实际执行，硬截止仍取原receipt。收束事件只允许在真实15:00后向既有thread单次queue并留实际回执，不重启daemon或创建session。

发布稳定指针：`main` · `Day22: calibrate wobbling evidence and close learning card`；精确hash及远端结果只写任务发布回执。显式manifest排除raw/PDF、受保护Bib、PLAN、继承Day20修改和本地冗余历史日志。下一任务只有Day23准备入口，新的执行身份/截止须由其自身runner新原始receipt给出。
