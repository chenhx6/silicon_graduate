---
type: system-prompt
graph-excluded: true
created: 2026-10-08
updated: 2026-10-08
---

# DAY9 — B(E2)、B(M1)、约化矩阵元与强度比

## Run context

- run_id: {{RUN_ID}}
- run_date: 2026-10-08
- day_index: 9
- timezone: Asia/Shanghai
- schedule_id: wiki-daily-learning
- expected_start: 2026-10-08T16:00:00+08:00
- overnight_until: 2026-10-09T15:00:00+08:00
- output_dir: {{OUTPUT_DIR}}
- report_file: /workspace/wiki/outputs/learning-daily/20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths.md
- state_file: /workspace/wiki/outputs/learning-milestones/2026-09-one-month-state.json

RUN_ID/OUTPUT_DIR占位由正常runner绑定到实际run；不得把prompt seed当真实session ID。每次正式调用创建新的Codex session，run receipt保存session_id和可复制resume_command，不复用Day8 session。最新Runtime snapshot的时刻/剩余分钟优先于旧静态时间；snapshot中的通用advance/complete-next-card措辞不授予Day10学分，课程不变量是onlyDay9credit/Day10partial。

## 正式卡与预习边界

Day8 session已预习本题知识和有条件算术，但仅Day8计卡。正式Day9必须重新建立自己的recall/evidence record、输入链练习、反证和card audit；不继承预习为已完成。先读Day8日报或知识页后回忆，应标primed recall；已有记忆也不冒称blind。

在/workspace/wiki依次读README、knowledge/index、profile/activehandoff、PLAN、Day8日报、[本计划](/workspace/wiki/outputs/plans/2026-10-08-DAY9-be2-bm1-reduced-matrix-elements-strengths.md)、daily-task-matrix的Day9卡和autonomous-research/continuous-learning workflows。写前boundary与gitstatus；保留继承dirty文件、raw、PLAN、review flags。课程state只通过normalrunner/state contract推进，不设置human-reviewed或清除needs_review。

## Day9 card

1. 回忆：查Day9来源正文前，独立说明partial lifetime、branching、mixing fractions与B/RME的关系，写mean lifetime/half-life和单位区别；标明priming，之后核对差异。
2. 主线：读knowledge/synthesis/high-spin-lifetime-strength-deformation.md与knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md。率/核算符归一回到LKH82 p.121 Eqs.2.2–2.3；表格回到MU08 printed034311-3/TableI与034311-4/TableII。
3. 练习：选MU08 Band1 I18、Ex6711.4组，独立核原表三枝401.2/757.4/389.6-keV及tau0.56(8)ps，重算一条有条件B(E2)或B(M1)输入链，逐项列数值、单位、分支basis、radiativefractions、IC/E0和误差。不能从quotedB倒推alpha/delta/covariance再验证自己。
4. 反证：检查漏枝、feeding、stopping、IC、branch uncertainty以及同数据派生输出的依赖。未知branch定义保留至少两种forward解释；15%stopping不自动作独立1sigma或跨带共模。精确归一化/quotedSD的不相容只排除额外joint解释，不判作者错误。
5. 交付：一页输入—公式—输出—误差表；每个判断回source locator，不能把视觉强度当B。绝对B、RME、reverseB、Qt或same-parentratio若共享输入，不重复计独立证据。

## 来源与候选优先级

- 第一优先是branch/lifetime/ICC/单位/不确定度闭合；先用已有source与immutableDay8 receipts核实，而非增加无关核素或文献数量。
- MU08 p.3说提取过程参照Chiara etal.[16]；p.6列C.J.Chiara etal.,Phys.Rev.C64,054314(2001)。若定义缺口仍改变判断，可在正式Day9验证该候选身份/合法全文再精读；当前未给其题名/DOI或方法作为事实。
- 现代BrIcc FO/NH inputs只是条件理论输入，不能证明MU08实际采用哪种处理；N6/shellcoverage、atomicradius、penetration/current域与模型相关性保留。
- 独立事件、line-shape、response、stopping/feeding代码与covariance缺失时不计L4；本日前述预习只L2。可靠模拟也不能冒充实验事实。

## 时间与课程

保持day_index=9。>=120分钟继续高信息当前题；局部饱和后重建候选池，只可预习恰好Day10知识，无学分、partial10，不把next_day_index越过10，不打开Day11。90–119分钟有界继续；<90分钟不打开新source/card，finishcurrent；2026-10-09 15:00停止研究，15:00–16:00收束。卡内容完成不单独结束窗口；等待/心跳不计研究时长。

日报使用标准十heading。Runstate只一行completed_day_indices和一行partial_day_indices；只有Day9全部deliverables完成才写completed=[9]与`Day 9 card audit: complete`，有至少4行completionaudit表。Day10只能partial，旧模板任何整卡前移计学分措辞在本运行禁用。Durable知识同步knowledge并保留唯一合法knowledge-writeback JSON，updated须真实改页，否则groundedverified-no-op。

Closeout执行boundary、wiki_lint --fail-on error、gitdiff --check及originalbaseline report/writeback/card验证；显式stage本runownedmanifest。Gitee freshfetch→ancestor→HEAD:main dryrun→同refspec非forcepush/H3。正常runner state最多credit9，生成下一未完成卡plan/prompt；hash仅run receipt，canonical指针branch+subject。
