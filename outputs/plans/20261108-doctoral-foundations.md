# 博士论文前置研学执行计划

用户要求先完成充分的核结构进阶研究，再进入新论文设计。
本计划执行普通专题L3与有界L4，不修改`PLAN.md`或daily状态。
长期科学内容和覆盖/就绪矩阵以
`knowledge/projects/doctoral-nuclear-structure-foundations.md`为准。

## 目标与授权

原生goal已于本会话创建：六区集体与核芯形变、一核两翼和实验电子学的深入理解、
可追溯比较、候选问题与就绪判断。无用户指定token预算，不虚报真实消耗或余额。
采用auto推进；用户指令已明确研究、写回与持续发布授权，不重复请求普通批准。
brainstorm用于科学问题探索，不扩展为无关软件架构项目。

当前保留`raw/writing/gpt/A130/`，基线为
`outputs/l3/20261108-doctoral-foundations-r1/a130-preserved-baseline.json`。
用户允许准备充分后清空精确目录并重写；当前条件未到达。
论文设计与Gemini正文写作均未开始。

## 工作波次

1. G26–G30：A60/80/100/130/160原始证据；T03：形状高阶矩与动力学。
2. G31：A190低自旋形状与混合；G32：吴鸿毅数字电子学；
   G33：异能态热耦合网络；G34：实际GT+FF理论；
   G35：形变/配对与0νββ；G36：逐分波形成/存活。
   RAT-PRM原件在既有source已有充分读取，不重复下载/另立同源证据。
3. G37：科学发散后新增的核心路线——γ振动/摆动耦合历史与偶偶核微观描述；
   T04独立核G34原文方程与校准，未先看G34草稿。
4. 总控：Kumar/Cline历史与形变推断、跨区整合、独立检查；
   worker先独立提出候选，总控在看齐结果后作反方评议。
5. 回查字节、locator、表格与算符，重放有界计算，写回knowledge。
6. 执行局部归档/结构/链接、lint增量、Git与发布门；显式暂存、非force推送；
   post-commit reconciliation。批次发布不等于原生goal完成。

## 并行合同

研究worker无Git操作、无继续派发权限，仅写分配前缀。
当前运行器共享树；路径划分是protocol-only，不是假称独立工作树或沙箱。
source与note各前缀唯一写者；README/index/共享综合/memory/handoff由总控写。
raw新资料只新增不覆盖，`manifest.json`使用非空`files`列表；
数值provenance使用`run-provenance.json`，CSV统一LF。

Gemini：`antigravity/gemini-3.8-flash-tiered`，high；
复杂理论：`codex/gpt-6.1-terra`，xhigh。
不能从请求路由推断供应商底层实现、成本或真实token用量。

## 验证与停止判据

各worker必须交代已读范围、原件/版本/哈希、locator、依赖、反例与失败条件，
不能把文本提取、题录或同一采集的多篇文献算作独立深读。
总控复核关键式、数值和至少关键图表；模型结果单独标明。
局部饱和只关闭该子问题，有价值问题继续推进。
阶段1只有达到项目页的解释/证据条件才可完成；不得因批次结束、页数或旧标签提前转写论文。
