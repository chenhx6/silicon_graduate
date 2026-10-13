---
type: learning-daily
graph-excluded: true
created: 2026-10-13
updated: 2026-10-13
---

# Day 13 — Doppler correction、反冲与速度信息

## Run state

- run_id: `2026-10-13-day-13-01`
- run_date: `2026-10-13`；timezone: `Asia/Shanghai`；day_index: `13`
- phase: `gamma-spectroscopy-and-level-schemes`；schedule_id: `wiki-daily-learning`
- completed_day_indices: [13]
- partial_day_indices: [14]
- Day 13 card audit: complete
- 入口状态：`next_day_index=13 / completed_day_count=12`，与矩阵一致；Day 11/12 不重跑。
- session_id: `01a13489-64ba-7930-9a2c-291375d95ad0`（本次新 session，与上轮不同）。
- resume_command: `codex resume 01a13489-64ba-7930-9a2c-291375d95ad0 -C /workspace/wiki -s danger-full-access -a never`
- 研究硬截止：`2026-10-14T15:00:00+08:00`；下一调度：`2026-10-14T16:00:00+08:00`。
- 执行路线：用户在同一 interactive session 中明确继续；未观察到 foreground daily runner，故以真实人工续接/检查回执对账，不伪造 runner exit code。
- 使用技能：`farmer`、`go-on`、`all`、`auto`；`debug`仅用于method schema错误修复。保留原任务、模型与文件现场；farmer 的 ensure 启动成功，dry-run 无恢复 action。auto 的原生 goal 创建成功；不增加未请求的 token budget。
- 本次课程交付完整；实验重拟合仍 not-ready，见下面的数据边界。Day 14 只有知识预习，没有该卡 completion audit、正式周考学分或课程跨越。

### Day 13 card completion audit

| Day-matrix deliverable | Evidence locator / artifact | Status |
|---|---|---|
| 来源前回忆：shift、velocity、angle、stopping、event correction | [recall-record.md](20261013-DAY13-doppler-correction-recoil-velocity-run-01/recall-record.md)，保存于本轮原文读取前；明确标作上轮预习后的 primed recall。 | complete |
| Doppler 方法、Mavela thesis 与一个 in-beam source 主线核验 | [Doppler method](../../knowledge/methods/doppler-correction.md)；[Mavela](../../knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md) DD-20261013-32S-27/28，Eqs.(4.5)/(4.6)、Fig.4.17；[Klemme](../../knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md) KL99-2/4/18，十页主线及 Fig.1/Table I–II。 | complete |
| 给定能量、β、角度的重算及速度误差传播 | [复算代码](../../system/scripts/day13_doppler_diagnostics.py)、[结果 JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/doppler-exercise.json)；exact inversion、Jacobian、covariance、有限差分和固定 seed MC。 | complete |
| 区分真实宽化、未完全校正、停止与近邻跃迁，含反证和必要伴随观测 | [诊断表](../../knowledge/methods/doppler-correction.md)；KL99-18 同跃迁的距离相关两分量；[Herzáň](../../knowledge/sources/herzan-2015-193bi-spectroscopy.md) HE15-5 的四线峰；低速 width-only rank-2 反例明确标为任务推导。 | complete |
| 一页 Doppler correction 诊断表，保留 locator | [Doppler correction 诊断表：峰位、峰宽与停止](../../knowledge/methods/doppler-correction.md)，八行症状/伴随检查/反证/locator；同步 [A≈130 thesis matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md) 的 Doppler-to-level/strength contract。 | complete |

## Candidate pool and selection

本轮延续问题为“校正后的峰能否验证速度/方向，并分开停止和多条跃迁”；主来源是必读的 Mavela `32S` thesis。独立 in-beam 对照选择 Klemme `134Nd` coincidence-RDDS：它将速度历史保留为寿命信息，直接检验“校正之后就不需 stopping”的说法。Longfellow 的已审核 GRETINA 方法仅作 first-interaction/角度与能量转换分离的支持性核验。唯一下一日预习选择 Herzáň `193Bi`，用原图和表把谱峰身份接到能级放置。

| 候选 | 本轮处理及信息增益 | 剩余判别输入 |
|---|---|---|
| Mavela β20/24、9%/7%与 S3 printed transform | 复核 printed input 和精确式；修正 `196Pt` 冲突句的 locator；不把排印列表等同执行版。 | production sorter hash、target/coordinate metadata、ring/sector spectra。 |
| β/角度/response 的峰宽识别 | 精确协方差传播及低速 rank-2 多解，改变对 angle-width diagnostics 的充分性判断。 | 至少一项独立 calibration，实际 joint covariance 和 response。 |
| Klemme stopping 与近邻线 | 全文主线、Fig.1和 Table I/II 回读；相同跃迁随 stopper distance 改变分量。 | 原始 distance/feeding/response 包才能重拟合。 |
| GRETINA frame/first-point | raw Eq.(18) 支持能量反演；最高能量点的排序是本装置的方法选择。 | 不移植阵列 response 或 sorting performance。 |
| Day 14 唯一知识预习 | Fig.2/Table I 三层重建、共用门和 quadruplet 反例；Table II 的 X/linking 与弱线缺失边界。 | 正式 Day 14 自己的来源前回忆、周考、weekly REFLECT 与逐卡验收。 |

开始快照为17:12、距原截止1307分钟；17:33刷新后1286分钟，按 AGENTS/continuous-learning 的新规则只预习 Day14，不按旧 advance wording 给学分。最终研究候选池在17:51:03刷新，剩1268.94分钟，见 [research-closeout.json](20261013-DAY13-doppler-correction-recoil-velocity-run-01/research-closeout.json)。

这次提前收束不是因为两个来源读完：已重新检查生产数据、独立 calibration、stopping 对照、tracking frame、下一张卡与具体可复算路径。当前诊断问题和唯一预习的可得证据已固化；仍会改变判断的输入是缺失的 acquisition/code/response 包，官方库新核验也没有这些附件。其它一般来源不能代替本次执行身份。未打开 Day15 的科学来源或课程；未解决输入列为 readiness boundary，不列成用户待办。

## Sources and evidence

| 来源与指纹 | 本轮实际覆盖 / locator | 独立性与证据层 |
|---|---|---|
| Mavela 2019；local raw SHA-256 `4c656a983a0502eaef7c551dfaf6e13539ce472f8e76aea6299ad09cfc112ccf`，94页 | 摘要/动机、CE/reorientation 理论主线、setup、calibration/gates、Doppler/GOSIA、discussion/conclusion；关键图式和代码视觉核验 PDF file pp.41,51,53,56,70,74。DD-20261013-32S-27/28；DD-20261013-32S-25 locator 改为 PDF p.41 / printed p.32。 | 一个实验；PDF、本文知识页和 UWC copy不是独立复测。Q_S/GOSIA extraction、作者 intrinsic-shape interpretation 与本任务 diagnostics 分层。 |
| Klemme 1999；SHA-256 `2a6dfcdac12de9dbf61b2a63c274aed8e286249a3dd28d1a2c6c5a46f1c00604`，10页 | introduction lifetime conflict→GASP/plunger/DDCM→finite stopping→Tables I–IV/IBM/TRS/ASYR limits→conclusion；视觉 Fig.1/2、Table I；KL99-18 补足 same-line distance反例。 | 独立于 Mavela；多 rings/gates/邻核仍属同次 acquisition，Table II branching 为另一次薄靶数据依赖；模型几何不是直接实测。 |
| Longfellow 2026；SHA-256 `fb3b4f5e4dce6a436bb569b64af1914c6b673561374d7867a3d906aef7090df1` | 支持性 raw p.3 Eq.(18)、first-interaction/ordering 段、p.7 summary；L26-8。 | 独立方法实验；原 human-reviewed/claim flags 保持不变，本轮未改 source。 |
| Herzáň 2015；SHA-256 `f727485ad0f52269a66b27272dac75d34d9e67aaf8b073631cfeac5fe81d3aea`，20页 | 仅本次 Day14 预习：reaction/tagging→bands/isomers/SD→interpretation/conclusion 主线；重点视觉 Table I p.3、Fig.2 p.8、Fig.5 p.10，及 Table II p.15 / negative evidence p.19；HE15-4–7。 | 独立 A≈190 实验；图、表、同门投影不是多份独立实验。Jπ/multipolarity 为联合赋值，configuration/SD 是受约束解释。 |

外部核验：Crossref `10.1103/PhysRevC.60.034301` 的作者/题名/年/期刊与 raw 一致，属于身份核验。UWC [item API](https://uwcscholar.uwc.ac.za/server/api/core/items/459d5ba1-daee-4bc9-b3f7-974e342e8e9a) 与 [bundle inventory](https://uwcscholar.uwc.ac.za/server/api/core/items/459d5ba1-daee-4bc9-b3f7-974e342e8e9a/bundles?size=100) 本次均HTTP200，分别列 thesis PDF、LICENSE、TEXT、THUMBNAIL，没有独立执行 sorter、event/yield/ring spectrum/calibration 附件。没有将 metadata 或搜索结果当作物理证据，也没有下载或改动 raw。

Mavela 的 Eq.(4.5)/(4.6) 与 inverse/Jacobian相容，Fig.4.17的2230.57-keV peak聚拢是真实图示；它未给角分辨centroids、完整 covariance 或执行版列表。Sec.4.4从 uncorrected target 与 projectile-corrected spectra取不同 yield，不证明 target β=0。printed β20 异常、β24候选、S3 transform 和9%/7%文本边界均保留。

## Theory/analysis exercise

设 θ 为 lab photon direction 对发射核速度的夹角，`E_lab=E0/[γ(1−β cosθ)]`，`E0=E_lab γ(1−β cosθ)`。对 x=(E_lab,β,θ) 用 `σ²=JΣJᵀ`；θ以 rad 输入，σβ与σθ若相关必须保留cross term。精确 Jacobian 和推导保存在 [Doppler method](../../knowledge/methods/doppler-correction.md)；来源基式是 Mavela Eq.(4.6)，传播结果是本任务推导。

自设 `E0=1000 keV, β=0.07, σE_lab=1 keV, σβ=0.002, σθ=2°`：

| θ | E_lab (keV) | independent σE0 (keV) |
|---:|---:|---:|
| 35° | 1058.226372 | 2.377966 |
| 90° | 997.546991 | 2.644848 |
| 145° | 943.449018 | 2.395211 |

三行精确反演均为1000 keV。90°的 β 一阶低速项消失，但 exact derivative 仍有相对论项，角度项较大。忽略 γ 会共同偏低2.453009 keV。35°相同 marginal σ 下，把ρβθ从−0.8改到+0.8使σ由3.0748变为1.3620 keV；未给 covariance 不能声称完整误差预算。

代码实测：forward/inverse最大误差 `1.14×10⁻13 keV`，有限差分相对误差 `2.44×10⁻9`，九种 covariance 的固定seed MC σ与一阶式最大差 `0.171%`；程序退出0。新模拟只验证方法与假设，不构成实验重拟合。

低速反例为 `V(θ)=A+B cos²θ+C sin²θ`。由于cos²+sin²=1，设计矩阵rank2；`(A,B,C)=(1,4,5.9705014)` 和 `(2,3,4.9705014) keV²` 给七个角度完全相同 variance。这直接限制“仅多角度峰宽就能唯一分解response/β/angle”的说法。独立calibration才能解除至少一项歧义。

停止toy用自设指数 slowing/emission law，无feeding、β_i=0.016、τ=t_s=1.1ps。固定初始β校正后的exact MC mean residual在35°/90°/145°为−6.502/+0.085/+6.615keV。Klemme只报告约1.1ps Au stopping time，没有报告本toy law或τ；两者不能等同。

### Day 14 uncredited knowledge preview

[来源前回忆](20261013-DAY13-doppler-correction-recoil-velocity-run-01/day14-preview-recall.md) 明确为已读source概要后的 primed recall，raw图/表在之后打开。正式Day14仍要重新做回忆和周考。

[Level-scheme method](../../knowledge/methods/level-scheme-reconstruction.md)保存Herzáň Fig.2/Table I的1228(17/2+)→929(15/2+)→605(13/2+)子图。299.2、323.4列M1，直接622.4分支列E2；`299.2+323.4−622.4=0.2 keV`。拟合误差独立时σ=0.1732keV；再假设caption的0.3keV增量各线独立时σ=0.5477keV。没有joint covariance，后者只是练习。三整数level energies为圆整值。

622.4分支与299.2+323.4级联互斥；共用下方门又未必能拆出同带299.8/299.2近邻。HE15-5的323-keV quadruplet是直接反例。HE15-6保留SD带的X与tentative link，HE15-7保留未见低能线及conversion/x-ray解释，不补写“已测”跃迁。

| 预习自检维度（0–4；primed，非正式周考） | 分数 | 本次证据与仍需练习 |
|---|---:|---|
| 理论/公式 | 3 | exact transform/Jacobian与energy closure已复算；不能替代完整响应积分。 |
| 谱/纲图/门 | 3 | 三层branch和四线峰已核；未持有真实多门矩阵重拟合。 |
| 误差/feeding/background | 3 | covariance与rank反例；实际feeding/response未知。 |
| 事实/解释/模型分层 | 4 | 图表、assignment、X/linking与模型解释明确分开。 |
| 竞争解释/反证 | 3 | stopping、quadruplet与未见低能γ的反例；灵敏度未重算。 |
| 研究问题/最小设计 | 3 | β/geometry/calibration和互斥branch controls已提出；事件包未取得。 |

本轮自检19/24，不是Day14正式成绩。预习REFLECT：峰、跃迁、能级和configuration不能合并成一个证据对象；energy closure与多投影会共享事件/标定；negative evidence必须带detection/branch/ICC条件。正式Day14宜优先检验这些边界并形成自己的weekly产物，而不是照抄预习分数。

## Counter-evidence and missing companion observables

1. Klemme Fig.1同一line有距离相关shifted/unshifted分量，反驳“两个峰必是两条跃迁”；Table I的6g+从1.38到corrected1.63ps增加18.1%，显示finite stopping影响寿命。
2. Herzáň Fig.5(a)的quadruplet反驳“一个谱峰必是一条γ”；低能非观测的解释不能自动填成已测线。
3. rank-2是推导层反例，反驳width-only decomposition的充分性；它不声称Mavela真实nuisance就是这组值。
4. 必需packet：executed sorter/geometry/β inputs、ring/sector与γ-crystal切片、matched gates、energy calibration/response、joint covariance、stopping/feeding metadata。缺这些不能比较β20/24的实际影响或修订GOSIA/Q_S。

## Knowledge Impact and Learning Decision

`supports`：exact correction、逐emitter谱/yield身份、stopping与谱峰/跃迁区分。

`revises`：多角度width可诊断输入，却在已声明低速模型中不能独自分解三个nuisance；应先取得独立calibration。

`limits`：总谱窄峰、shared gate、energy closure、relative Iγ与模型曲线的结构推断。A≈130 chirality/wobbling/signature/configuration解释排序不变，未获得新绝对B矩阵。

## Durable knowledge delta

可复用知识的canonical落点是八个 `knowledge/` 页面：Doppler诊断/推导、level-scheme方法、三份source、A≈130 evidence contract、开放问题locator及index。`outputs/`的JSON/回忆/评分/候选池只作执行与验收记录，不能取代这些证据页。新科学claims仍为unreviewed/needs_review；未升级为human-reviewed。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Doppler correction 诊断表：峰位、峰宽与停止",
      "summary": "固定症状、伴随检查、反证与locator；分开emitter、angle/velocity、stopping和多线。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        },
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-28"
        },
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-18"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "精确 Jacobian 与协方差练习",
      "summary": "新增自设三角度重算、相关误差、有限差分和MC验证；非实验测值。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "低速峰宽多解：角覆盖本身不足以分离三个 nuisance",
      "summary": "写回rank2反例和独立calibration解除歧义的条件。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "停止历史 toy 的边界与符号检验",
      "summary": "以明确自设的law显示初始β校正后残差；不把1.1ps尺度当实测停止曲线。",
      "sources": [
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-4"
        },
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
      "anchor": "DD-20261013-32S-27",
      "summary": "补exact transform和emitter-specific counts事实并修正196Pt句的实际p41/p32 locator。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        },
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-28"
        },
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-25"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
      "anchor": "KL99-18",
      "summary": "补同跃迁距离相关两分量和TableI/TableII finite-stopping区别。",
      "sources": [
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
      "anchor": "HE15-4",
      "summary": "固化三线属性、复合峰、tentative SD X/link和低能非观测的作者解释。",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-4"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-5"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-6"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "193Bi Band 1 三层实例",
      "summary": "新增图表子图、逐线证据层、energy closure/covariance和同母态branch边界。",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-4"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "门条件、反证与可以重排纲图的观察",
      "summary": "保留复合峰、弱线缺失、未知X和可证伪的重排条件。",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-5"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-6"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "anchor": "Doppler-to-level/strength evidence contract",
      "summary": "连接Doppler/line identity到A130强度与模式证据门，不改变模式排序。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        },
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-18"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "PDF p.41/印刷 p.32",
      "summary": "修正target-conflict问题定位，保留production数据缺口。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-25"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[level-scheme-reconstruction]]",
      "summary": "登记新方法页和Doppler诊断入口。",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-4"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

- Mavela实际执行β表/坐标与打印列表是否相同？新的bundle库存仍不含执行与逐环数据；继续保留开放问题，未更改PDF或猜测正确数值。
- independent calibration能约束width分解中的哪项？rank2限制的是已写明的低速/小独立误差模型，真实角度相关response与non-Gaussian tails要另建响应。
- level identity何时需要拆峰或重排？对子图的closure、coincidence、spin/parity或同母态branch条件出现可靠冲突时重审；先排除随机/feeding/response问题。
- 本次 belief revision和最小数据设计均已写回方法页；没有把输入缺口转成人工审核清单。

## L0–L4 state

| 等级 | 状态 / readiness |
|---|---|
| L0 | raw identity/locator/原图核验完成；保留所有权限、文本与执行版边界。 |
| L1 | source↔method、thesis contract、index反链完成；不同实验/不同emitter的适用条件保留。 |
| L2 | exact formula、covariance、rank2和stopping toy为可复算低成本验证；未冒充测量。 |
| L3 | 诊断问题的竞争机制、反证、falsifier、数据包与停止条件完成；真实Mavela执行影响仍partial。 |
| L4 | experimental refit `not-ready`：缺事件、production code、ring spectra、response/covariance和feeding；模拟练习不作为新实验L4或absolute-strength研究。 |

## Verification and continuation

最终检查：boundary exit0（无error/warning）；Wiki lint最终 exit0，0 errors /92 warnings /1558 info。Warnings为89项既有citation-key缺失和3项reaction-parser边界；未猜测BibTeX key。第一次lint的4个错误仅为新method缺少Purpose/Inputs/Can/Cannot四小节，按模板/config补齐后同命令回归通过；失败记录保留。

report headings、唯一writeback（12items/8changed pages/0locator errors）、Day13 coverage与Day14 partial、PLAN/Bib保护检查均通过；git diff --check exit0。具体代码/MC结果和preflight记录可回到run-dir audit。提交前仍核对显式stage、cached diff、fresh fetch/ancestry/dry-run和非force push；真实结果只写run receipt，不把计划写成发布成功。

first-write boundary/preflight/EOL checks均成功，index初始为空。继承的Day6–9 run artifacts、system/log旧差异和daemon修改排除；raw/PLAN/受保护Bib只读，源PDF哈希一致。overview/QMD update按本次局部方法增量deferred；只读collection boundary已通过。

研究收束时间为2026-10-13 17:51:03+08:00，早于原硬截止1268.94分钟；原deadline不改。原因、全候选池与Day14检查保存在research-closeout.json；它保留缺失输入和重复核验无新增判别能力的具体边界。只在取得新primary packet或用户定向新问题后重开该诊断；讨论仍可用本页resume_command。

本轮续接文件：[continuation-prompt.md](20261013-DAY13-doppler-correction-recoil-velocity-run-01/continuation-prompt.md)。Formal Day14须新session，保持本次预习不计学分；最终发布和课程状态转换记录于run.json与scheduler event，精确hash只写任务回执。
