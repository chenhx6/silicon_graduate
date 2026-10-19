---
type: output
graph-excluded: true
created: 2026-10-19
updated: 2026-10-19
---

# Day17：线偏振、P/A/Q与Compton响应

## Run state

- run_id: `2026-10-19-day-17-01`
- run_date: `2026-10-19`；timezone: `Asia/Shanghai`；day_index: `17`
- session_id: `01a1532e-0f21-7903-9bf6-8a9cc9ee9e17`
- phase: `angular-correlation-polarization-and-mixing-ratio`
- schedule_id: `wiki-daily-learning`；Docker-local，非GUI Scheduled对象。
- hard_deadline: `2026-10-20T15:00:00+08:00`；15:00–16:00仅收束。
- status: `running / substantive checkpoint`；原生goal为active，未提前关闭研究窗口。
- completed_day_indices: []
- partial_day_indices: [17]
- Day 17 card audit: partial
- 当前课程文件仍为next17/count16；Day16预习、旧程序检查与旧分数不兑换正式17。本session只允许正式17，最多无学分partial18，不开19；目前未开18。

实际runner回执位于[run.json](20261019-DAY17-linear-polarization-paq-compton-run-01/run.json)，其run-01/session与原deadline覆盖准备prompt的run-17/output_dir示例。`events.jsonl`实际thread.started与CODEX_THREAD_ID相符。用户打断后明确要求farmer/go-on/all/auto继续；后来暂停并恢复goal，仍是同一session，不新建daemon/session或调度。当前未观察原runner正常exit，不把它写成已发生。

### Day 17 card completion audit

| 课程交付 | 本session实际证据/artifact与locator | 状态 |
| --- | --- | --- |
| 来源前主动回忆及priming声明 | [active-recall-before-sources.md](20261019-DAY17-linear-polarization-paq-compton-run-01/active-recall-before-sources.md)与[freeze](20261019-DAY17-linear-polarization-paq-compton-run-01/active-recall-freeze.json)，2026-10-19 16:04:24上海、session/hash；不是盲测 | complete |
| ST99原件主线与关键图/表/式 | [[../../knowledge/sources/starosta-1999-pdco-experimental-test]]末段actualreadscope；printed16–26、Figs1–7、Table1–4、Eq1–7及脚注；ST99-14 | complete |
| SG98原件主线与关键图/表/式 | [[../../knowledge/sources/schmid-1998-gammasphere-polarization]]末段actualreadscope；printed95–110、Figs1–15、Tables1–3、Eq1–19；SG98-13/14 | complete |
| P/A/Q分层与新计数/误差练习 | [[../../knowledge/research-notes/polarimetry-shared-calibration-count-design]]“P/A/Q分层与原件输入”及“声明设计的计数与定量结果”；[newresult](20261019-DAY17-linear-polarization-paq-compton-run-01/paq-shared-calibration-result.json) | complete |
| 反证、必要companion和独立校准输入 | ST99-2/7/13/14；SG98-5/8/9/12/13/14；新note中holdout支路、共同Σ和改分母反例 | complete |
| 本日报、唯一writeback与checks | 六页canonical已变更；首轮模板缺项已修、lint-001 exit0/0errors190warnings；报告/映射/发布的完整验收尚待检查点记录 | partial |

这是研究中检查点的实况表，未预填formal17完成或提前计卡。最终完成时再按所有门更新completed[17]及逐卡审计。

## Candidate pool and selection

按README/index/profile/memory/activehandoff/PLAN、三份课程计划、continuous-learning/autonomous/reflect规则和最近八次日报的候选部分重建；见[candidate-pool-001.json](20261019-DAY17-linear-polarization-paq-compton-run-01/candidate-pool-001.json)。日报只提供运行历史，不作为新的科学事实源。

| 槽位/候选 | 信息增益、覆盖与当前决定 |
| --- | --- |
| continuity：两原件的P/A/Q、共享a/η与Q依赖 | 当前课程强制主线；实际计数定义和cross-Cov可改变P幅度/误差，先核原件再作新联合设计，已产生canonical增量 |
| 同一问题下一步：detector合并权重 | ST99以18台合并a≈1、SG98以12台合并C/S；reference/target的不同权重是否破坏迁移仍有高信息增益，继续研究 |
| 实际P/δ重拟合 | 原events、producer、matching response、fit/calibrationΣ未得；不以更多toy替输入 |
| SG98 294-keV printingclosure | 旧边界仍在，无新producer/unrounded输入；不调η、不复跑旧JSON计新交付 |
| non-overlapping novelty | 当前未强行占槽；Day16强priming来源不自动算novelty，不以篇数判饱和 |
| Day18 | 当前continuity仍有有价值路线，未打开；如后续按时间门局部饱和才看恰好下一卡，无学分 |

Day8–16近期覆盖含选律/相位、寿命与分支、双带电磁、反应与符合、Doppler、谱学身份、ADO/DCO和大量偏振预习。按课程重读ST99/SG98属于有记录的课程重叠，不声称来源未暴露或实验独立。

## Sources and evidence

| 来源与identity | 本session实际覆盖/locator | 证据分层与独立性 |
| --- | --- | --- |
| [[../../knowledge/sources/starosta-1999-pdco-experimental-test]]；DOI10.1016/S0168-9002(98)01220-0 | 原11页printed16–26主线与全部图像；printed17 Eq1/2、footnote1，printed18 Eq3/4，printed19 Eq5/6/Table1，printed21 integrated，printed23–25三表，printed26 ακ | 原164Yb采集与NORDBALL单clovercalibration分开；reference P来自上游AD/GOSIA，四组P/integrated/RDCO不是独立实验；旧10⁻5/脚注纠正不作新发现 |
| [[../../knowledge/sources/schmid-1998-gammasphere-polarization]]；DOI10.1016/S0168-9002(98)00624-X | 原16页printed95–110主线与全部图像；Eq13–18、Fig8 zero、Fig9/10 threshold、Fig12 level scheme、Table3与Fig13–15 | 三reference的A/P/Q同链派生；197Pb是另一应用数据；44页alternate本session未打开，原same-study版本不计独立实验 |
| 两DOI的Crossref exact请求 | 本次实际HTTP200，分别11/12作者、1999/1998、423/417和16–26/95–110；[progress-001](20261019-DAY17-linear-polarization-paq-compton-run-01/progress-001.json) | 仅校身份，非物理正文/独立实验 |

两原件实际SHA-256分别为`883fdd7b08831efefe25f5df610e84b95bb1acbcd7b8e7f684b1a1b31bf8030b`、`66502edb2f0ff2d09321d3b388767ea98736b83865b90f128fdd1e46921b2a2c`，与source元数据一致。raw只读；启动boundary/preflight均exit0，受保护Bib基线matched。

本轮新增ST99-14是source定义与共享校准依赖的有条件推导；SG98-13是改分母的代数反例、SG98-14是原N/ε措辞字典。新claims全needs_review，原25条ST99/SG98 claim行和flags逐字核相同，未设human-reviewed。

## Theory/analysis exercise

完整公式、假设与数据在[[../../knowledge/research-notes/polarimetry-shared-calibration-count-design]]；可运行[day17_paq_shared_calibration.py](../../system/scripts/day17_paq_shared_calibration.py)，输入[paq-design-input.json](20261019-DAY17-linear-polarization-paq-compton-run-01/paq-design-input.json)，结果[newresult](20261019-DAY17-linear-polarization-paq-compton-run-01/paq-shared-calibration-result.json)。这是新声明的设计计数，不是ST99/SG98实测数据。

clover用A=(aN⊥−N∥)/(aN⊥+N∥)；SG98用A=(ηC−S)/(√η(C+S))且C含sideADCzero。各推自己的Jacobian，联合primitive六counts和独立P_ref传播P_t=P_ref A_t/A_ref，保留Cov(A_t,Q)。另一路条件binomial Fisher和各120000次Poisson设计MC验证同一统计模型，不计独立实验。

| 新设计 | U；reference；target（各两类别均值） | A_t；Q；P_t±localσ | 若错当A_t/Q独立的σ |
| --- | --- | --- | --- |
| clover | 500000/500000；55000/45000、P_ref=.5±.01；53000/47000 | .06；.2；.300±.0194486 | .0201951 |
| SG98 | 1000000/160000；101600/14400、P_ref=.8±.012；100600/15400 | .015；.05；.300±.0627474 | .0646613 |

共同η不自动完全消去；比值中只取消√η，剩余敏感性为C_t/(ηC_t−S_t)−C_r/(ηC_r−S_r)的局部log导数。若改成B=(ηC−S)/(ηC+S)，则B=(1+η)QP/[2√η+(η−1)QP]，一般非线性；此设计沿旧Q得到P=.441961，即使以同一参考重标一点也仅.291999而非真值.300000。符号、数值和适用条件都在canonical，未修改source实验结果。

脚本首次用两个interpreter均缺SymPy（actualexit1），保留[first-execution-failure.json](20261019-DAY17-linear-polarization-paq-compton-run-01/first-execution-failure.json)；随后用已有repo内依赖缓存的per-command PYTHONPATH执行exit0。未安装全局包、未改系统配置；新代码/input/hash、依赖版本与首次成功/补充代数核验结果均保留，不称首次即成功。freeze的时间说明如实区分来源前回忆与执行后查看结果前封存的inputhash。

## Counter-evidence and missing companion observables

- ST99-2：490-keV的P/RDCO仍保留E2与ΔI0 M1/E2；正号不保证唯一δ/Jπ。ST99-12的ακ是作者理论预测而非已测ICC，不能拿它闭合分支。
- SG98-5/8：zerochannel是另一侧confined，Fig9 130keV与Fig10/Pb 60keV不能混用。源Table3误差来自DAMM拟峰，不能覆盖为√面积。
- SG98-9/12：432线正A和带内负A是直接观测层；E1/M1/negativeparity是作者附条件解释，shears为结构解释。高背景散布/AD companion限制精确P提取；约36%只属于原条件，不是通用P界。
- SG98-10：294打印中央值未闭合仍保留；actualη在quoted误差内，不是实验矛盾，不调η强配。
- 必要独立校准输入：未参与Q拟合、已知P且energy/threshold/gate/arrayweights可核验的holdout支路；另需U/r/t真实峰与background/event-overlap Σ。用同reference回代自己不是独立验证。
- SG98-14：Eq13称N为source发射数，而Eq18称Ni为incident；要有接受角/曝光归一字典。photopeak/coincidence、本征/绝对/relativeNaI/条件效率不能混为同一ε；高背景下裸F不是可靠仪器排名。

## Knowledge Impact and Learning Decision

`supports`直接从原始计数表达P/A/Q、共同校准和可复算Σ；`revises`“改分母再标一条线即可继续用线性Q”的预期；`limits`从同参考回代、偏振号或裸F取得独立验证。没有新增实验P/Q/δ/Jπ/模式，也没有解释原294印刷差或490剩余分支。

本session的数学交叉核验为同一design的内部证据；两原件不同采集可以比较合同，但不能组合成一个新的实际计数实验。任何真实反演仍需matchingresponse/完整Σ。

## Durable knowledge delta

本轮六个knowledge页面实际变更。新canonical [[../../knowledge/research-notes/polarimetry-shared-calibration-count-design]]保存P/A/Q表、两Jacobian、共同校准比值/误差、新计数/Fisher/MC、非线性反例和holdout设计；ST99-14及SG98-13/14给精确source锚点。两method页新增使用门、index提供入口；outputs不是唯一知识副本。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {"knowledge": "knowledge/research-notes/polarimetry-shared-calibration-count-design.md", "summary": "保存Day17新P/A/Q分层、联合计数/误差设计、改分母非线性与效率归一边界；均为附条件推导。", "anchor": "共同校准如何进入参考比值", "sources": [{"path": "knowledge/sources/starosta-1999-pdco-experimental-test.md", "locator": "ST99-14"}, {"path": "knowledge/sources/schmid-1998-gammasphere-polarization.md", "locator": "SG98-13"}, {"path": "knowledge/sources/schmid-1998-gammasphere-polarization.md", "locator": "SG98-14"}]},
    {"knowledge": "knowledge/sources/starosta-1999-pdco-experimental-test.md", "summary": "本session完整主线/图表原件复核及共享a/reference/target依赖边界，原claim flags保持。", "anchor": "2026-10-19 Day17独立session的实际复核", "sources": [{"path": "knowledge/sources/starosta-1999-pdco-experimental-test.md", "locator": "ST99-14"}]},
    {"knowledge": "knowledge/sources/schmid-1998-gammasphere-polarization.md", "summary": "本session完整原件复核，新增改分母非线性与发射/入射效率字典；原294等边界保持。", "anchor": "2026-10-19 Day17独立session的实际复核", "sources": [{"path": "knowledge/sources/schmid-1998-gammasphere-polarization.md", "locator": "SG98-13"}, {"path": "knowledge/sources/schmid-1998-gammasphere-polarization.md", "locator": "SG98-14"}]},
    {"knowledge": "knowledge/methods/linear-polarization-asymmetry.md", "summary": "新增共享校准传播与reference独立验证门。", "anchor": "同参考校准的计数与误差门", "sources": [{"path": "knowledge/sources/starosta-1999-pdco-experimental-test.md", "locator": "ST99-14"}, {"path": "knowledge/sources/schmid-1998-gammasphere-polarization.md", "locator": "SG98-13"}]},
    {"knowledge": "knowledge/methods/compton-polarimetry.md", "summary": "新增primitive计数/响应归一与效率分母使用边界。", "anchor": "共同校准与估计量归一的联合设计", "sources": [{"path": "knowledge/sources/starosta-1999-pdco-experimental-test.md", "locator": "ST99-14"}, {"path": "knowledge/sources/schmid-1998-gammasphere-polarization.md", "locator": "SG98-14"}]},
    {"knowledge": "knowledge/index.md", "summary": "加入Day17新研究笔记导航；这里只是治理入口，物理主张仍回source/note。", "anchor": "polarimetry-shared-calibration-count-design", "sources": [{"path": "knowledge/sources/starosta-1999-pdco-experimental-test.md", "locator": "ST99-14"}]}
  ]
}
```

## Open questions and belief revision

下一高信息问题是：逐detector的a/η与Q不同时，合并参考和target的权重差能否引入伪P或改变其符号/幅度？原ST99 Fig2合并a≈1并不单独证明任意target selection匹配；SG98 Eq13也要求总photopeak yield对两pure偏振相同。先冻结预期、明确forward contract，再查原件允许的条件或真实公开输入；不把自由权重toy当原实验偏差证明。

完整U/r/t/fit-Cov、P_ref的AD/GOSIA不确定度、逐门响应/producer仍缺。若取得matched holdout失败或target-weight不同的实测ledger，将触发Q迁移和δ幅度判断修订；当前没有这样的观测，不裁决原实验。

## L0–L4 state

L1原件学习、L2源与方法写回已实质推进；当前L3为校准/response可识别性与最小独立检查设计。声明MC只是数理验证，不是actual experimental L4 fit；真实events/response/Σ未齐，实验重分析not-ready。日计划授权保持有效，不将缺口自动转为用户待办或额外启动请求。

## Verification and continuation

启动boundary和automationpreflight actualexit0；首次lint因新研究笔记缺11个必需heading为exit1，随后补齐并以JSON格式重跑的[lint-001](20261019-DAY17-linear-polarization-paq-compton-run-01/lint-001.json)为exit0、0errors190warnings（137citationkey/50rawslot/3reactionparser）。source旧25claim行/flags实际逐字核相同，raw/PLAN/Bib和继承dirty保留。`git diff --check`当前actualexit0。[verification-002](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-002.json)已实际核report/coverage/唯一writeback六页、boundary/lint/diff均通过，PLAN/Bib/recall与原25claim保护通过；H3与实际push另记本runpublication，未把内容检查当远端发布成功。

原研究窗口仍持续；当前[continuation-current.md](20261019-DAY17-linear-polarization-paq-compton-run-01/continuation-current.md)继续同一session的array-weight问题，不以本检查点终止整日。原生goal仅在原窗口收束与所有交付/验证/发布完成后才标complete；Farmer PID42019确认存活，无pending恢复事件，不承担学习调度或Git。

Resume：`codex resume 01a1532e-0f21-7903-9bf6-8a9cc9ee9e17 -C /workspace/wiki -s danger-full-access -a never`。本轮正文/候选/续接尽量中文；QMD/overview批量刷新deferred。
