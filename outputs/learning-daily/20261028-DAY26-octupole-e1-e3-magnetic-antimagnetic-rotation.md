---
type: daily-learning
graph-excluded: true
created: 2026-10-28
updated: 2026-10-28
---

# Day26：八极关联、E1/E3与磁／反磁转动

## Run state

- run_id: 2026-10-28-day-26-01
- session_id: 01a1819f-75bb-7a11-be19-05761880f65c
- day_index: 26
- schedule_id: wiki-daily-learning
- status: running
- completed_day_indices: []
- partial_day_indices: [26, 27]
- curriculum_cards_completed: 0
- next_day_index: 26
- hard_deadline: 2026-10-29T15:00:00+08:00
- closeout_window: 2026-10-29 15:00–16:00 Asia/Shanghai
- native_goal: active
- Day27_opened: false (only bounded no-credit preview; original run receipt lists partial[26], next_day_index remains 26)

本段继承原runner身份与原始overnight_until。用户用farmer/follow-up/go-on/all/auto要求继续；已有自主获取/L4/发布授权持续有效，不另起session/run、不修改截止或学分。当前只是研学checkpoint，不能把本段来源读完当全时段完成。

### Day25原始状态核对

Day25原run.json为completed、counted_in_substantive_test=true、completed[25]/partial[26]；里程碑累计25/next26。指定card-credit-25.json、final-session-receipt-25.json、task-publication-receipt-25.json缺失。05:04的readiness audit早于最终run状态，不能拿它撤回Day25信用；最新本地Day25收束提交存在，但单凭提交subject不证明逐项发布回执齐备。旧Day21–25学分、人审和撤回边界保留，不补造历史回执。

### Day26卡片进行中审计

| matrix交付 | 当前证据与缺口 | 状态 |
| --- | --- | --- |
| 回忆与区分E3、E1、octupole、MR/AMR | evidence-gradient三层图已建立；017/019纠正对称性和“充要”硬门 | 内容已写回，正式授分前复核 |
| 三篇主线原读 | BU16 5页、BU17 6页、Garg2015 9页；保Pr2019勘误缺口 | 原读范围已记录 |
| 单位、不确定度与证据梯度 | 001和019重算方向因子7；022对齐Cd频率中心并保留负有限差分 | 条件练习完成，不冒实验重拟合 |
| E1强度能否独立变化 | BU17 TableI/Fig5支持占据驱动近相消；生产有符号核未取得，撤回自设90%/97.1%分解 | 有界反证已写回，精确机制仍开放 |
| 交付图与质量区边界 | evidence-gradient与跨质量区预习页修正原硬门，Day27仅无学分preview | 页面已写回，Day26保持running |

## Candidate pool and selection

|候选问题|当前输入与信息增益|决定|
|---|---|---|
|Pr交叉身份与伪单调轨迹|原Table I与Figs5/7/8可直接否定无来源轨迹|本段优先校正，继续同母态分支重建|
|Ba E1相消的定量程度|实际v²与E1模型/实验幅度差；Ref24新原件可取得|持续主问题：核与对称性，不编分项偶极数|
|E3单位与误差映射|两篇打印M/B与不对称误差完整|已作可复现条件练习；不生成新CI|
|Cd J2/B数列与谱系|旧019输入无locator；综述给不同范围|撤回旧认证，继续查Piiparinen1993/Juutinen1994|
|Garg2019勘误|Crossref/INSPIRE身份已核，正文当前网络失败|保版本边界，换合法仓储路线；不重复无变化失败|
|投影GCM的F图与算符核|新BE16全文、Eqs1–5、Figs1–4、Table I|下一当前高信息路线：区分好宇称态正交与坐标密度相似|

当前问题仍有高价值路线；Day27跨质量区页已作有界预习且不计学分。局部纠错或一次下载失败不构成提前收束。

## Sources and evidence

|来源|实际文件与阅读范围|独立性/限制|
|---|---|---|
|[[bucher-2016-144ba-direct-octupole]]|5页，SHA与既有源一致；重读全文主线/表/拟合方法|独立144Ba实验；E1含既有τ/BR；不是直接拍梨形|
|[[bucher-2017-146ba-direct-octupole]]|6页，SHA一致；重读主线，fresh视觉PDF3–4|146Ba独立实验；有符号D0为模型；内部日期/版本标记分别记录|
|[[garg-2015-135pr-magnetic-rotation]]|9页PDF，主线PDF1–8，fresh视觉PDF7|2015 original；2019勘误未得；τ/absoluteB缺失|
|[[bernard-2016-144ba-sccm-octupole]]|新取得arXiv1604.06706v1，6页，SHA d339bbdde6991e19148ec2d619c79dba4fbb5ca95173084a33ed36a39232b997；全文主线与四图/表|D1S模型，复用BU16实验，不增独立票；未取得生产核/代码|
|[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]|定向PDF26–28、printed488–490及参考文献|综述；Piiparinen RDDS与Clark private DSAM分谱系，不当新原实验|
|[[roy-2011-cd110-systematics-antimagnetic]]|5页PDF（PLB 694, 322），SHA 2a090a6f66d7c908419dd6c1bdc67b4f617101d8e3a4fd8d02d6da9be06d1d0a；精读Table 1 DSAM寿命与Eqs 1–6经典粒子转子模型|独立110Cd INGA实验；B(E2)缓降（0.14->0.06），core耦合为作者模型解释，28+不归AMR|
|[[nomura-2018-odd-ba-octupole]]|11页PDF（PRC 97, 024317 / arXiv 1711.09587v2），SHA 4df5fce3696da1d019ea07111e064fe9704376f2f6c8b6bb33826cb61fa953be；精读Tables I-IX与激发能谱/B(E3)|微观约束sdf-IBFM模型；奇粒子轨道分量与f玻色子成分不能独立给普适Pauli阻塞因果认证|
|[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]]|8页PDF（PRC 76, 024321）；继承已核Table I与Fig7的source记录|137Pr独立实验；作者报告相对比值62.1(12.0)到17.2(2.9)，保留δ假设和TAC偏差|

|[[butler-2020-222-228ra-octupole-evolution]]|发布版6页与arXiv附加页7–16均读；发布版raw SHA c0f864…；多跃迁E3但星号受耦合约束|独立Ra CoulEx；未闭合总和|
|[[nndc-2009-ra225-adopted-parity-doublet]] / [[nndc-2022-ac225-adopted-parity-doublet]]|官方ENSDF评价原文归档；225Ra/225Ac的E1和伙伴记录|评价对象；原实验未逐篇重读|
来源签名/页数/hash与当前session保存在run目录resume-state-001.json。新Bernard已验证后另存raw/papers/gpt/day26-20261028；PDF未列入公开Git。默认请求SI，但当前未确认各目标出版商完整附件清单，不把未检得写成不存在。

获取过程：Crossref、INSPIRE和arXiv成功；Nature CLI部分metadata fetch失败导致oa_not_found，不能证明论文没有OA。Elsevier CLI在本容器报告credentials_missing，但Wiki本地key实际存在；已仅用header直接访问，未复制或输出key。直接API/APS/OpenAlex随后遇到DNS/连接失败，属于运行访问缺口，不冒称publisher拒绝授权。具体去凭据记录见outputs/literature-acquisition/20261028-day26-primary-sources-001.json及run获取记录。

## Theory/analysis exercise

### checkpoint019 科学纠错

旧日报把17项工件统称“完全独立验证”，其中007–015含未定位实验表、自设参数与错误定理，不能保留该科学认证。已对九对Python/JSON加科学状态标记；旧Python默认停止，显式历史replay才允许执行。原始材料未改，旧代码字节由Git历史保留。规范通过不等于原文支持或实验复现。

- **直接原件记录**：BU16向下E3为48(−34/+25)，BU17为48(−29/+21) W.u.，旧015把两组误差互换。BU17的146Ba E1幅度实验0.000223与SCCM0.00474相差21.26倍，不认证“绝对精确复现”；计算有符号D0不是实测符号。
- **017 条件推转与流场**：构造明确对称性的示意流场与冻结陀螺模型，临界频率0.514639 MeV/ℏ是该输入的结果。纠正AMR时间反演不破缺、总磁矩处处零、β=.20硬门和J2/B≥100排他判据；不是实际核密度泛函生产计算。
- **018 点团簇反向例**：在固定未极化点团簇假设内，20Ne E1严格相消但E3可非零；146Ba同一单通道不能同时拟合所用E1/E3中心。不是团簇存在或GDR相消的实验测量。
- **019 准粒子算符与宇称位移反例**：正交3qp/5qp态的单体矩阵元可为0.96q；理想转子简单平均位移为−12keV，自旋加权插值为0；AMR横向零而纵向磁矩可非零。未给Pr的真实E2矩阵元。
- **022 Cd打印表复算**：Roy Table1完整逐点输入；邻接差149、99、−9、44keV给J2=26.85、40.40、−444.44、90.91 ħ²/MeV。频率与强度中心明列，负值不隐藏。纯E2单位分支寿命换算与表列B有约7%–13%差别，记录待补的转换/分支条件，不静默改表。
- **奇A专题016**：独立source审计与条件模型保留奇粒子阻塞的模型范围，不以无显著f玻色子含量普遍证明无双重态或完全抑制八极。

可复用纠错归入 [[day26-quantitative-claim-corrections]]；原表定位归入Roy、Bucher与Nomura来源页；所有新页面保持unreviewed，不更改旧人工审核。完整模型输入/输出在相应017–019、022工件。016的独立代理定向审查、全库结构检查与本checkpoint发布状态以后续实际回执为准。

### Checkpoint 019–028：证据重建与可复用反例

- **016 奇 A 锕系/镧系**：`parity-doublet-actinide-lanthanide-016.py/json` 与 `odd-a-parity-doublet-blocking-audit.md` 将 225Ra ENSDF 评价层（31.50-keV E1，B(E1)=0.00081(20) W.u.）与奇 Ba 的 sdf-IBFM 模型层分开；评价记录并不自动证明所有奇 A 核都有或没有静态八极双重态。
- **017 三维流场/TAC**：`tac-currents-shears-chiral-phase-017.py/json` 与 `n75-3d-tac-source-contrast-day26.md` 把局部玩具流场、冻结陀螺临界频率0.514639 MeV/ℏ、132La实验双带位移和Olbratowski模型分支分层；这些不是核密度泛函生产结果或普适MR/AMR相界。
- **018–019 反向检验**：点团簇模型确认荷质比相等时E1几何零点，但同一E1/E3通道的联立解需核尺度局域约束；BCS代数例给出单体算符连接3qp/5qp的非零矩阵元0.96q，撤回“单体E2必为零”。
- **020 原件审计**：BU16/BU17 E3误差、BU17 E1表列0.000223/0.00474及Gaffney 940±30（E3约化矩阵元）/2520±90（Q3）经独立目视复核；Egido–Robledo1990正文未取得，未把元数据当全文。
- **022–023 Cd归一化**：Roy Table1五个寿命与B(E2)保留；ENSDF半衰期除以ln2重现平均寿命，内转换约10^-3不足以解释7–11%中心差，22+的1100-keV评价支线与Roy未确认的门条件不能混算。条件误差尺度不是正式统计检验。
- **027 多跃迁E3完整性**：Butler 2020 的 222Ra 多条E3矩阵元/近恒定Q3图样与 228Ra 近零耦合线，为静态梨形—八极振动区分提供比单个E3更强但仍模型依赖的证据；星号矩阵元受转子耦合约束，未闭合总和。
- **028 225Ac评价层**：ENSDF给3/2−基态、40.10-keV 3/2+和40.09-keV E1 B=0.00171(15) W.u.；A–D多带使同自旋劈裂不唯一，D0=0.1688±0.0074 e fm仅为K=3/2转子条件反演。
- **029 E3账本**：逐项核对BU16/BU17/Gaffney/Butler的单位、Q3转换、初态简并因子和星号耦合；027平方和混合不同Ji，不能叫0+闭合m0。
- **032–035 E3方向审计**：Butler的E1/E2/E3幅度比保留量纲；228Ra的2+→3−区间跨零，222Ra Q3近常数仅定性；所有B(E3)方向转换使用实际Ji，0+ closure只取Ji=0行。
- **041 Pr勘误闭合**：公开APS勘误原件两页已取得并核读；813.3-keV偏振不对称从−0.20(8)改为+0.04(3)，747.5-keV从−0.05(3)改为+0.03(3)，两条均为M1+E2。它修正当前多极性入口，但不提供绝对寿命/B(M1)，也不改变作者总体解释边界。
- **042 Egido正文获取审计**：新增 reader/ScienceDirect 公开入口探测；分别得到 TLS handshake failure 与 HTTP 403，仍无正文/页图/文本。仅更新访问边界，不把元数据或失败响应写成科学证据。
- **043 Day26 requirement audit**：逐项标出 R1–R4 已证实、R5 正式学分/closeout 待硬截止、R6 Day25 回执缺失、R7 Day27 bounded preview；该审计不是最终 receipt。
- **044 110Cd HI,XNG 输入契约**：完整读取 NNDC 110048022 固定栏对象；确认 18+–24+ 半衰期、E2分支和22+的1100-keV保留支线。它补齐分支身份，但不提供 Roy 的 LINESHAPE feeding 协方差或绝对 B(E2) 重放输入。
- **045 110Cd 分支归一化审计**：评价字段给出22⁺的1314.1-keV份额 2.7/(2.7+1.0)=0.7297；18⁺、20⁺、24⁺所读块无第二评价分支。该情景不能覆盖全部7–11%中心差，也不能直接修正 Roy 未确认1100-keV线。
- **046–047 并行复核**：Ba 证据层再次确认 E1 中心差异不是精确模型验证，SCCM F 图不能替代非对角算符核；Cd HI,XNG 的 RI 仍是相对量，评价表头不等于逐线绝对 B(M1)/B(E2)。
- **048 closeout readiness**：逐项审计标出 R1–R8 已证实或弱证据，R9 正式学分/最终 receipt 继续 pending；报告 preview 与原 run.json 的 partial 字段差异留待 closeout reconciliation。
- **049 live closeout refresh**：00:20 Asia/Shanghai重新核对 farmer PID、`HEAD=origin/main` 和原 run.json；正式学分/最终 receipt继续pending，15:00–16:00必须重新跑门禁并完成 reconciliation。
- **043 续接与次日准备**：已生成可复制 resume 命令、未决路线和 Day27 无学分预览；不推进 next_day_index，不打开 Day28，正式 Day27 仍等待自己的原始 runner receipt。
- **036 奇A能量窗**：225Ra/225Ac同自旋异宇称候选计数随50/100/200-keV窗扩大，最近能级可误导；A–D带标签与分支连接缺失时不选定宇称伙伴。
- **037–040 收敛审计**：MR/AMR十项观测矩阵、E3跨来源一致性、奇A跨来源一致性和离散电流边界均完成；Roy Table 1已核为归档PDF印刷p.324，p.323仅为前页线形段；Ra E1 provenance更正为229Th α-decay链，Ac才是225Ra β− L-subshell ratios。
- **030 奇A配对**：225Ra仅1/2配对唯一、225Ac仅3/2配对唯一；其余A–D带同自旋组合多解，条件D0不能直接比较。
- **031 TAC单位敏感性**：冻结陀螺示例的ωc=0.514639046 MeV/ℏ、Icrit=15.9538ℏ；Jm对±10%最敏感，Starosta带位移、Olbratowski HF起点和玩具阈值不是同一实验量。
- **024–026 量子边界**：132La/N=75的3D-TAC与实验输入、固定双角动量M1的Racah/矩阵残差1.78×10^-15、非正交HWG自然基底诊断均是有界模型/代码练习；026显示旧015全维零模会取到f†Nf≈0的伪低态，不能从其0.0 JSON恢复物理E1/E3。

## Counter-evidence and missing companion observables

1. Pr：27/2−是低端态，作者交叉约33/2−；交叉后未见crossover，不能认证“27/2反弹”或post-crossing强度轨迹。
2. Cd：旧744/907/1042/1180 keV与误差输入缺原表，撤回245–414认证。综述的计算平台、RDDS与private DSAM分开；无普适J2/B阈值或所有M1恒零。
3. Ba：强E3加小E1支持解耦，不测得有符号D0。两个宽区间相容不证明刚性；软PES与投影混合是可解析替代图像。
4. 理想AMR横向相消不排除总磁矩、跨带M1或其它symmetry-breaking项；ΔI2间M1的选择规则也不是AMR专属判据。

## Knowledge Impact and Learning Decision

本段`revises` Day25原件未支撑的Pr/Cd数列与过强认证，`supports` 按observable→derived strength→model分层，`limits` 用相似F图、均场minimum或占据数代替投影跃迁核。新SCCM源使当前问题可以继续深入，来源访问失败不把研究任务转给用户。

## Durable knowledge delta

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/research-notes/octupole-mr-amr-evidence-gradient.md",
      "anchor": "## Grounded Evidence",
      "summary": "三类模式的测量—强度—模型证据图与输入/符号/误差边界。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
      "anchor": "## Key Results",
      "summary": "新取得并精读六页SCCM原件；good-J/宇称与相干核、软PES和模型缺项。",
      "sources": [
        {
          "path": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
          "locator": "BE16-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
      "anchor": "## Day26：E3方向、误差与形状推断",
      "summary": "向上/向下B、相位灵敏度与宽误差的推断边界。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
          "locator": "BU16-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
      "anchor": "## Day26：实际占据、E1定量偏差与投影算符核",
      "summary": "E1幅度/强度的模型偏差、具体v²及有符号核的缺口。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
      "anchor": "## Day26原件复核：带头、交叉与强度比的数据覆盖",
      "summary": "27/2带低端与33/2交叉区分；撤回伪低spin轨迹。",
      "sources": [
        {
          "path": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
          "locator": "GA15-D26-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md",
      "anchor": "## Day26：110Cd数值与实验谱系复核",
      "summary": "PAC平台、RDDS与private DSAM分开，综述比值100–200。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md",
          "locator": "F01-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/magnetic-rotation.md",
      "anchor": "## Day26：纠正Day25高自旋轨迹与寿命硬门",
      "summary": "替换17/2–27/2伪轨迹与固定绝对B确证硬门。",
      "sources": [
        {
          "path": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
          "locator": "GA15-D26-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/antimagnetic-rotation.md",
      "anchor": "## Day26：撤回Day25无原表的110Cd数列认证",
      "summary": "撤回无locator的Cd逐点输入与245–414认证，限制所有M1恒零。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md",
          "locator": "F01-D26-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "## Day26：八极与磁转动证据梯度",
      "summary": "加入新证据梯度与SCCM方法源入口。",
      "sources": [
        {
          "path": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
          "locator": "BE16-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/overview.md",
      "anchor": "## Current Snapshot: 2026-10-28 Day26 checkpoint001",
      "summary": "实际目录计数与本段研学/结构检查边界。",
      "sources": [
        {
          "path": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
          "locator": "BE16-D26-004"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/cross-mass-region-collective-mode-transfer-boundaries.md",
      "anchor": "## Grounded Evidence",
      "summary": "六大质量区物理特征对照矩阵与四大跨区不可迁移性判据。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
          "locator": "BU16-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day26-quantitative-claim-corrections.md",
      "anchor": "## Grounded Evidence",
      "summary": "本轮定向原件核对与条件推导；未升级人审。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/octupole-cluster-dipole-dynamics-conditional-equivalence.md",
      "anchor": "## Grounded Evidence",
      "summary": "本轮定向原件核对与条件推导；未升级人审。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/odd-a-parity-doublet-blocking-audit.md",
      "anchor": "## Grounded Evidence",
      "summary": "本轮定向原件核对与条件推导；未升级人审。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2009-ra225-adopted-parity-doublet.md",
          "locator": "Key Results"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md",
      "anchor": "## Day26 原件重读与派生量复核",
      "summary": "本轮定向原件核对与条件推导；未升级人审。",
      "sources": [
        {
          "path": "knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md",
          "locator": "RO11-D26C-003"
        }
      ]
    }
  ]
}
```


索引已加入两张新知识页；数值更正直接替换MR/AMR当前末节，同时保留旧历史与旧review flags。未把outputs当长期事实源。

## Open questions and belief revision

- 相消点附近，E1绝对误差能否来自较小的占据/配对/形变变化？需要有符号核与参数敏感性，不能从21倍幅度差直接断言机制失败或成功。
- 哪些更高阶E3/电荷形状观测能在给定不确定度下区分局域形状与软相关？现有一个强度不能独立裁决。
- Cd逐点J2的中心自旋如何与B(E2)初态对齐，RDDS/DSAM的feeding、BR与系统误差如何处理？原表未得前不画认证曲线。
- Pr原Table I是否能在明确multipolarity条件下重现Figs5/7的相对比，且保持erratum边界？继续做版本分层的复算。

## L0–L4 state

L1/L2原件阅读与互链、L3竞争解释和输入合同在进行；L4限打印电磁矩阵元的可复现单位/误差敏感性练习。尚未重放GOSIA或SCCM生产计算，不伪造真实数据/实验响应/新CI。新内容不升级human-reviewed。

## Verification and continuation

- 入口EOL清理exit0，preflight/boundary通过，受保护Zotero Bib哈希匹配；farmer PID3193监督本session，未挂起重试。
- 继承1143条Git状态入口和未跟踪历史；并发出现的system/scripts/run_daily_learning.py修改属protected external scope，本研学不编辑或stage。
- 原生goal继承并保持active；all/auto执行研究单元，普通优化轮数或收益阈值不覆盖用户原时间窗。farmer仅监督allowlisted暂态失败，不控制学分/Git。
- 本段后续检查与发布以required-checks-001.json、checkpoint-publication-001.json实际结果为准；未签发Day26最终学分或final-session receipt。
- 恢复：`codex resume 01a1819f-75bb-7a11-be19-05761880f65c -C /workspace/wiki -s danger-full-access -a never`。
- 下一当前问题：BE16的norm/奇宇称算符核与F图；Pr同母态branch条件复算；Cd原表合法仓储路线。继续至原研究截止，15:00后才正式收束。
