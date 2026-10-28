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
- partial_day_indices: [26]
- curriculum_cards_completed: 0
- next_day_index: 26
- hard_deadline: 2026-10-29T15:00:00+08:00
- closeout_window: 2026-10-29 15:00–16:00 Asia/Shanghai
- native_goal: active
- Day27_opened: false

本段继承原runner身份与原始overnight_until。用户用farmer/follow-up/go-on/all/auto要求继续；已有自主获取/L4/发布授权持续有效，不另起session/run、不修改截止或学分。当前只是研学checkpoint，不能把本段来源读完当全时段完成。

### Day25原始状态核对

Day25原run.json为completed、counted_in_substantive_test=true、completed[25]/partial[26]；里程碑累计25/next26。指定card-credit-25.json、final-session-receipt-25.json、task-publication-receipt-25.json缺失。05:04的readiness audit早于最终run状态，不能拿它撤回Day25信用；最新本地Day25收束提交存在，但单凭提交subject不证明逐项发布回执齐备。旧Day21–25学分、人审和撤回边界保留，不补造历史回执。

### Day26卡片进行中审计

|matrix交付|本段实际证据|状态|
|---|---|---|
|回忆并区分直接E3、E1、octupole、MR/AMR|原件后建立证据梯度；尚未做新的盲回忆测验，不追认先读后答为盲测|partial|
|三篇主线原读|BU16 PDF1–5；BU17 PDF1–6；Garg2015 PDF1–8主线与定向references|complete for reading scope|
|三级梯度与单位/误差练习|canonical梯度图；octupole-units-and-sccm-001.py/json|partial: Cd原表待核|
|反证：E1与E3解耦|BU17 Table I/Fig5；新BE16 Eq4/5；E1绝对模型偏差|partial: Ref35与生产核未取得|
|交付图与质量区边界|octupole-mr-amr-evidence-gradient；保留Ba与Pr/Cd数据身份|draft; continue research|

## Candidate pool and selection

|候选问题|当前输入与信息增益|决定|
|---|---|---|
|Pr交叉身份与伪单调轨迹|原Table I与Figs5/7/8可直接否定无来源轨迹|本段优先校正，继续同母态分支重建|
|Ba E1相消的定量程度|实际v²与E1模型/实验幅度差；Ref24新原件可取得|持续主问题：核与对称性，不编分项偶极数|
|E3单位与误差映射|两篇打印M/B与不对称误差完整|已作可复现条件练习；不生成新CI|
|Cd J2/B数列与谱系|旧019输入无locator；综述给不同范围|撤回旧认证，继续查Piiparinen1993/Juutinen1994|
|Garg2019勘误|Crossref/INSPIRE身份已核，正文当前网络失败|保版本边界，换合法仓储路线；不重复无变化失败|
|投影GCM的F图与算符核|新BE16全文、Eqs1–5、Figs1–4、Table I|下一当前高信息路线：区分好宇称态正交与坐标密度相似|

当前问题仍有高价值路线，未进入Day27预习。局部纠错或一次下载失败不构成提前收束。

## Sources and evidence

|来源|实际文件与阅读范围|独立性/限制|
|---|---|---|
|[[bucher-2016-144ba-direct-octupole]]|5页，SHA与既有源一致；重读全文主线/表/拟合方法|独立144Ba实验；E1含既有τ/BR；不是直接拍梨形|
|[[bucher-2017-146ba-direct-octupole]]|6页，SHA一致；重读主线，fresh视觉PDF3–4|146Ba独立实验；有符号D0为模型；内部日期/版本标记分别记录|
|[[garg-2015-135pr-magnetic-rotation]]|9页PDF，主线PDF1–8，fresh视觉PDF7|2015 original；2019勘误未得；τ/absoluteB缺失|
|[[bernard-2016-144ba-sccm-octupole]]|新取得arXiv1604.06706v1，6页，SHA d339bbdde6991e19148ec2d619c79dba4fbb5ca95173084a33ed36a39232b997；全文主线与四图/表|D1S模型，复用BU16实验，不增独立票；未取得生产核/代码|
|[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]|定向PDF26–28、printed488–490及参考文献|综述；Piiparinen RDDS与Clark private DSAM分谱系，不当新原实验|

来源签名/页数/hash与当前session保存在run目录resume-state-001.json。新Bernard已验证后另存raw/papers/gpt/day26-20261028；PDF未列入公开Git。默认请求SI，但当前未确认各目标出版商完整附件清单，不把未检得写成不存在。

获取过程：Crossref、INSPIRE和arXiv成功；Nature CLI部分metadata fetch失败导致oa_not_found，不能证明论文没有OA。Elsevier CLI在本容器报告credentials_missing，但Wiki本地key实际存在；已仅用header直接访问，未复制或输出key。直接API/APS/OpenAlex随后遇到DNS/连接失败，属于运行访问缺口，不冒称publisher拒绝授权。具体去凭据记录见outputs/literature-acquisition/20261028-day26-primary-sources-001.json及run获取记录。

## Theory/analysis exercise

本段producer为run目录octupole-units-and-sccm-001.py，输入为两原表舍入值。

- E3向下B=M²/7，向上B=M²；0.65给向下0.06036 e²b³。b³到fm⁶乘10⁶，不能与E1/E2单位互换。
- 标准Weisskopf单位随A²变化；同打印M得到144/146Ba约49.0/47.7 W.u.，保留作者48的报告中心，不用舍入算术改实验。
- 一阶传播近似打印B误差；平方M端点给另一组区间。无原联合likelihood，不称任一个为重建实验CI，也不由区间相交报显著性。
- BU17 Table I的E1模型/实验幅度比21.26、强度比451.8；0.00474不是0.000474。该差异限制绝对复现措辞，未排除近相消点的微观机制。
- 质心修正的偶极算符说明E1可以因质子/中子质心差相消；具体v²本身不能恢复signed transition kernels。完整模型还须BE16 Eq4/5的norm与相干核。

全部可复用公式、数值与边界已同步canonical研究笔记；JSON是复现工件，不是独立科学来源。

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
- 原生goal已启用并保持active；all/auto执行研究单元，普通优化轮数或收益阈值不覆盖用户原时间窗。farmer仅监督allowlisted暂态失败，不控制学分/Git。
- 本段后续检查与发布以required-checks-001.json、checkpoint-publication-001.json实际结果为准；未签发Day26最终学分或final-session receipt。
- 恢复：`codex resume 01a1819f-75bb-7a11-be19-05761880f65c -C /workspace/wiki -s danger-full-access -a never`。
- 下一当前问题：BE16的norm/奇宇称算符核与F图；Pr同母态branch条件复算；Cd原表合法仓储路线。继续至原研究截止，15:00后才正式收束。
