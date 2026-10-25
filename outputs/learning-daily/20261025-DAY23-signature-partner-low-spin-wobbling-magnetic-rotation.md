---
type: learning-daily
graph-excluded: true
created: 2026-10-25
updated: 2026-10-25
---

# Day23：旋称伙伴、低自旋wobbling与磁转动（持续研究checkpoint002）

## Run state

- run_id: 2026-10-25-day-23-01
- day_index: 23
- session_id: 01a172fd-cbfb-7a13-b715-cfa0c479e08e
- schedule_id: wiki-daily-learning
- status: active-checkpoint
- completed_day_indices: []
- partial_day_indices: [23]
- original_deadline: 2026-10-26T15:00:00+08:00
- closeout_window: 2026-10-26 15:00–16:00 Asia/Shanghai
- checked_at: 2026-10-25T20:48:53.170388+08:00

当前仍在原始研究窗口，继续研究，未授Day23学分、未打开Day24。原始身份取本run `events.jsonl` 的thread.started，与原生goal线程一致；截止取既有 `run.json`，未由准备prompt创建新session或改deadline。可复制恢复命令：`codex resume 01a172fd-cbfb-7a13-b715-cfa0c479e08e -C /workspace/wiki -s danger-full-access -a never`。

Day22四份回执交叉核对：final-session与card-credit均只授[22]，partial[23]、累计22、next23；run completed，task-publication标published，H3的18项命令退出码全0，postcommit reconciliation passed。该核验不重加学分。精确旧hash只见Day22任务回执。Farmer原PID2698持续运行，dry-run/status/ensure已执行，无重启；不把本轮用户续接当瞬时故障自动恢复事件。

### Day 23 card progress audit（未完成授分）

| matrix交付 | 本checkpoint状态 | 证据与下一缺口 |
|---|---|---|
| 五机制区分 | partial | 下述暴露后回忆；需结合MR/AMR原件检验，不能假称盲测 |
| 两篇主线 | in-progress | Guo主文/SI与Lv主线/SI实际回读；剩余支持方定标/response深入核验 |
| 支持—反证—依赖矩阵 | in-progress | canonical项目新表/图；需继续查外部Q与cross-campaign ledger |
| 只改configuration | in-progress | canonical方法页冻结D的Au轨道替代与holdout；固定producer和可分预测未取得 |
| 谱系图/可证伪问题 | in-progress | 已写图及问题框架；待伴随观测和真实输入进一步约束 |

## Candidate pool and selection

| 槽/候选 | 信息增益与可得性 | 决策 |
|---|---|---|
| A：Pr/Au逐线P、A、Rac、δ与共享响应 | 已有raw可核；同源量和校准谱系可能改变比较的权重 | active；本轮找到Au376上误差误记及同源强度约束 |
| B：冻结计数/能级的configuration重指派 | 有原QTR轨道内容，缺统一producer与未定标预测 | active；完成冻结范围和检验量设计，继续寻找输入 |
| MR/AMR的独立寿命/组态对照 | 137Pr打印比不闭合、108In有DSAM；不能沿旧黄金阈值 | current-card候选，尚未新读其全文 |
| Day24手征伙伴逐态证据 | 只在本卡两槽局部饱和后按时窗预习 | 尚未打开；预习也不给正式学分 |

已有README/index/profile/memory/active handoff、PLAN、continuous-learning、三计划/matrix与近期Day22回执均已读取；PLAN中的旧审批/时钟文字不覆盖当前用户明确授权。当前路径门与H1预检通过，已有未跟踪Day20/Day22材料保留；不运行隔离的114个producer。

## Sources and evidence

checkpoint002实际选读Zheng2013 printed044328-4/5与Herzáň2015 PDF2/7/10并视觉核两篇校准图，哈希均匹配；未重算已在Z13-9/10/13记录的原表误差/1368问题。新增HE15-D23-1区分JUROGAM-II polarimeter的75.5°/104.5°和Rexp角组；AU20-D23-1核定Au PRM使用既有绝对E2选择β，故不把这两尺度再当独立holdout。精确阅读范围见reading-scope-002.json。

阅读账本为本run `reading-scope-001.json`；五主PDF与两SI哈希均匹配来源记录。Guo主文6页和SI6页全文主线已回读，Lv主文物理正文pp1–5和SI7页已读，主文p6参考表只抽取；支持方另按实际选读范围记录，不冒称所有来源本次重新通读。新视觉：Guo p3 Fig3/4、两个4倍误差图例，Lv p3 Table1/Fig2、SH26 p14 Fig12。

- [[../../knowledge/sources/guo-2022-low-spin-wobbling-187au|Guo2022]] GU22-D23-001：原Fig3(a)为δ−.26(+.11/−.15)，定向修正Day22继承+.16；Fig3(b)为−.28(+.23/−.69)。旧−.10(5)仍为P，非δ。
- 同源GU22-D23-002/003：自测a、借用Zheng2013 Q；462的上/中/下界来自同一次实验不同门，非独立采集；5%为Rac效率/有限张角预算，不是完整polarization prior。
- [[../../knowledge/sources/lv-2022-evidence-against-wobbling-135pr|Lv2022]] L22-D22-R095-1：747 P+.04/δ−.47、813 P−.03/δ−.37逐线保留。L22-17/19与SI Eq2：P/Ap同源、Q外借、旧AD再分析和新P-Rac须分列。
- [[../../knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr|SH26]] SH26-D22-R095-1、SH26-11/15：Fig12的σ/I=.2条件大根支持确实存在；新报告DB连接仍在共享/合并实验谱系，不拿新observable冒充完全独立新采集；逐图event ledger缺口保留。
- [[../../knowledge/sources/sensharma-2020-longitudinal-wobbling-187au|Au支持方]] AU20-1/4/5、p3–4：两次Gammasphere采集合并，17环AD和associated SP支持链保留。p4明确β=.23的尺度选择用既有B(E2)，不能再作为独立留出验证。

联网核验实际返回：arXiv2011.14354 landing 200、两篇PLB Crossref DOI均200，题名/年份匹配；详见`network-verification-001.json`。元数据验证不代替原文物理证据。

## Theory/analysis exercise

checkpoint002：按照两原校准的印刷p0/p1，来源曲线在Au376/462给Q=.314472/.292257，在Pr450.2/747.3/813.2给.236763/.148787/.134271。共同参数导致跨线Cov；若只知道两参数marginal σ，未知ρ下可给一阶σQ范围，不能指定成真实target CI。Q376/Q462=1.076013、Q747.3/Q813.2=1.108109，其校准形状误差与绝对归一不同；未知transfer κ(E)仍未覆盖。8项全两参数有限差分/PSD/rank/共同尺度控制实际通过，来源与公式均在canonical方法页“Day23 外借Q的能量共同误差与迁移边界”；代码day23_polarization_calibration_transfer.py、结果calibration-transfer-002.json。没有由印刷Q误差恢复原共同likelihood或排除分支。

暴露后回忆（primed，已见准备提示/继承页面，非盲测评分）：signature partner是同组态的旋称分支关系，不是pseudospin；wobbling要区分几何、局部harmonic声子与完整量子拓扑；TiP在相应QTR术语中是3D进动/重定向的模型解释；MR需粒子/空穴叶片几何及绝对M1随spin的证据；AMR的理想双剪刀横向磁矩相消需其对称条件，弱E2/无M1不是无条件唯一判据。基础校准见[[../../knowledge/concepts/signature-partner-bands|旋称伙伴]]、[[../../knowledge/concepts/magnetic-rotation|MR]]、[[../../knowledge/concepts/antimagnetic-rotation|AMR]]，本段未新认证这些页全部历史数值。

本轮定量练习的全部定义、公式、限制保存在[[../../knowledge/methods/signature-tip-shears-discrimination-contract|canonical方法页]]“同源派生强度的秩约束”。输入为Lv813.2/726.0同母态、光子比6.4/3.7、δ−.37。纯E2分母与MeV系数.697下，rE2=.11812877、rM1=.39772213；三个汇总量(δ,rE2,rM1)由两个输入(δ,K)决定，Jacobian rank2，约束为c rE2−δ²rM1=0。六项有限差分/极限/变号/缩放/秩控制实际通过。这不是实验Cov、CI或原producer复现。

首次JSON导出因numpy布尔类型失败，改成builtin bool后重跑成功；失败及修正记入reading ledger，不把失败的首轮当通过。脚本`system/scripts/day23_strength_dependency_rank.py`，结果`strength-dependency-001.json`。

## Counter-evidence and missing companion observables

checkpoint002进一步限定：Q校准完成不使P成为不依取向的核态属性；两实验还须各自population/feeding/gate响应才能比较同一δ。现有Au PRM与QTR的shape/MoI/model space也不同，作者之间的比较不是只改configuration的受控实验。严格隔离该作用仍需固定H、算符和拟合集合。

为取得独立于Q/取向的historical conversion输入，已查Rupnik1998 DOI10.1103/PhysRevC.58.771：publisher候选PDF未认证，直接link403、harvest401；OpenAlex200给LSU repository页，Scholar超时、api.osti域名解析失败，均如实记rupnik-access-002.json。访问状态不等于没有原文或原数据。尚未将αK升格为本次直接原件核验，LSU200但明确无正文下载，其摘要写Hg而Guo原PDF经3倍图核仍印187Ag；Ag→Au不符单步β电荷改变。该身份文字疑点新增GU22-D23-004，馆藏公式缺失/未得原文，不补母核完整Jπ、αK或非观察灵敏度，也不据此否定Rupnik实验。下一沿机构/作者可访问原件及Bourgeois1978调查，不用Guo的δ换算点伪装新conversion采集。

只改configuration的练习冻结D：计数、门/背景、response、能级、自旋宇称和连接不变。Au Band2从同πh9/2组态的nω=1候选换成QTR #21主导轨道，Band1为#19主导；来自G22-20。这不包含把SP序列改归188Pt，也不把独立实验的δ偷换为另一实验值。

可证伪问题：固定候选Hamiltonian/算符与已用定标点后，两种组态归属对未参与定标的同母态退激向量及绝对E2/M1尺度能否给出共同响应下可分离的预测？必要伴随观测为逐态τ、完整分支/δ/ICC与feeding/响应/Σ，辅以候选模型确实给出差别的g/Qs或轨道选择敏感观测。单j g可能完全相同，不能承诺其单项排他。未取得预测区间/producer就不能给差值、功效、计数或机时。

同源派生rE2/rM1不会自动增加独立检验；模型拟合用过的能量/绝对尺度不再是holdout。形式上可写的轨道替代尚无同等拟合/预测证据，不能等同可信度。Lu、两qp Ba/Nd及105Pd原支持链保持独立，不能因Pr/Au冲突一概否决。

## Knowledge Impact and Learning Decision

checkpoint002 supports/limits：明确源曲线与target transfer分层、共同校准误差及P的取向依赖；进一步把Au观测层不变的重解释与同Hamiltonian的configuration数值对照区分开。模型/实验排序尚无充分共同输入裁决，继续当前A/B问题。

revises：一处Au误差抄写；limits：主/SI、δ/强度和不同门的重复计票；supports：使用原件、带身份和响应合同比较对立解释。保持Pr固定取向大根条件支持和反方新测量；尚无共同likelihood或最终模式归属裁决。

## Durable knowledge delta

可复用事实更正、方法推导、组态替代设计、证据依赖矩阵和争议谱系图都已写入knowledge，不以本报告或旧认证为科学源。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
      "summary": "原图修正376keV上误差为+.11；分开自有a/外部Q及462选门依赖。 补Rupnik母核原文Ag字面与馆藏Hg摘要的身份边界。",
      "anchor": "Day23 原件复核：误差上标与新增观测的依赖",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D23-001"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D23-002"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D23-003"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D23-004"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/signature-tip-shears-discrimination-contract.md",
      "summary": "逐线响应合同、同源强度Jacobian秩2及保持计数的轨道重指派/留出检验。 补外借Q共享能量误差/迁移κ与固定H检验边界。",
      "anchor": "Day23 同线观测向量与响应合同",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-002"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "G22-20"
        },
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-15"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-2"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-D23-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/low-spin-wobbling-controversies.md",
      "summary": "支持/反证/采集依赖矩阵与争议Mermaid图；新报告DB观测不自动算新采集，跨核campaign仍缺ledger。",
      "anchor": "Day23 活跃比较入口",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-005"
        },
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-11"
        },
        {
          "path": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
          "locator": "LV21-D22-R102-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "summary": "纠正Au开放问题的376keV上误差，仍保留响应、SP身份和共同模型输入缺口。",
      "anchor": "Guo Fig3打印δ=−.26(+.11/−.15)",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D23-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
      "summary": "核定被Lv采用的Q曲线实际极化角/选样与Rexp角组不同，保留transfer/参数Cov缺口。",
      "anchor": "Day23：被Lv2022采用的Q曲线与实际选择对象",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-D23-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md",
      "summary": "确认PRM输入shape已参考旧绝对E2；和QTR的模型空间/shape差异不是纯重标带名。",
      "anchor": "Day23：绝对尺度定标与模型空间的条件",
      "sources": [
        {
          "path": "knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md",
          "locator": "AU20-D23-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/187au-longitudinal-wobbling-controversy.md",
      "summary": "隔离Guo引用母核文字疑点，明确Rupnik仅元数据/摘要可访问，历史αK仍非本次直接核阅。",
      "anchor": "Day23：历史conversion的直接证据缺口与母核文字",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D23-004"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

- Au376上误差已由原图改正，中央值与争议排序不变；不从图例直接报显著性。
- 同型Clover外借Q的实际参数、门选择与响应适用性怎样影响两核比较？已有source中的原Q论文优先核查。
- 两候选模型是否能在不复用定标量的情况下产生可分预测？缺固定producer与模型误差，继续做输入readiness。
- Pr/Nd跨核campaign事件同一性、SH26逐图run组成仍需ledger；同reaction和总events不证明逐event一致。

## L0–L4 state

L1/L2实际原件/哈希/联网核验完成本checkpoint；L3证据图、依赖推导和可证伪设计active。L4真实实验共同response/Cov/计数与固定producer不齐，not-ready；本轮数值只为声明输入的代数控制。新claims均needs_review:true，无human-reviewed升级；课程及Day21/22既有学分不变。

## Verification and continuation

checkpoint002实际boundary=0、lint=0、diff=0、calibration=0，8项限定控制通过；真实runner报告/累计7个已改知识页writeback均valid。lint0error/220warning，新增claims仍needs_review:true。required-checks-002.json保存退出码/尾部与映射；原始baseline-001保持不变。

checkpoint001实际boundary=0、lint=0、git diff --check=0、strength_dependency=0；6项限定数值控制通过。真实runner validate_report和validate_durable_knowledge均valid，首批4个已改知识页均在唯一writeback区块映射。lint为0 errors、220 warnings，source_missing_citation_key=182为继承覆盖债务，新claim_missing_locator/kind均0；needs_review信息不冒称人审。详细退出码见`required-checks-001.json`与`runner-contract-check-001.json`。下一提示`next-continuation-002.md`保持本session和原15:00截止；本报告是checkpoint，不是当天完成或提前收束。checkpoint002发布稳定指针为main · Day23: trace polarization calibration and parent identity；实际H3结果/精确hash只记本run `task-publication-receipt-002.json`，正式授分仅到截止收束门处理。原生goal active持续推进，Farmer仅负责allowlisted瞬时失败。
