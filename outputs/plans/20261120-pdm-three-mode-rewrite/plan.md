---
title: "multipolePDM：两组几何、GUI与正式发布的合并执行合同"
date: "2026-11-20"
updated: "2026-11-25"
status: in_progress
phase: geometry26_software_release
report_update_authorized: true
goal_id: "01a212d0-2f83-7582-9e2a-2d9c51511377"
---

# PDM 当前执行与验收合同

本文件与 tasks.json 为本轮唯一现行方案。用户已确认23段合并任务，授权必要源码、测试、示例、分析、绘图、报告修订、新版本正式PyPI发布及正常Git提交推送。过去报告阶段的“不改GUI／不发布”、两套生成器计数及旧几何默认设置均被本合同替代。旧完成事实及冻结回执继续有效，不改写历史数据。

## 1. 恢复现场与历史成果

工作树开始时干净，分支main。既有E01–E03、U00–U09、R00–R05和N01–N03均为历史完成项，不代表本轮验收。旧报告90页，30注入、30文献二维声明模型（15条不同跃迁）及9纯项前向控制；旧30注入及其二维数组、统计与图片复用，不再次PDM反演。独立9j实现、历史校验、随机记录保留后台，均不另计主要案例。当前源码的delta命名消歧与v3导出尚未进入PyPI 0.1.1，本轮一并发布。

历史回执：delivery/report-revision-20261124.json、delivery/statistics-naming-20261125.json、delivery/0.1.1/acceptance.json。plan.pdf仅为20261120历史阅读快照，不更新或另建计划PDF。修订前main.tex/main.pdf、报告正文及原计划已版本留档，不覆盖唯一历史证据。

## 2. 写域与并行所有权

- GUI worker：GUI控件、contracts/grid/common默认及专用测试。
- JSON worker：io/input、必要CLI、包内examples、软件README及专用测试。
- 计算worker：analysis/scripts/benchmark_geometry_26.py与新的geometry26_20261125结果集合。
- 幻灯片worker：revise_slide_figure已有程序、δ=+10三模式Notebook和单图；135Pr及旧图先留档，不重构。
- 主代理：本计划与账本、秘书main.tex/inject_test.tex/main.pdf、figures新数据图表与比较、版本/构建/发布、知识与交接、最终验证和Git。

不改原实验数据、汇总xlsx、根PLAN或无关工程。临时编译、日志、预览、隔离安装均放tmp/pdm-20261125。禁止多个写者同时改同文件。工作源码正常跟踪，结果与原件依原Git边界本地保留。

## 3. 物理与注入合同

三模式内部P_ADO/P_DCO/PDCO，显示P-ADO/P-DCO/PDCO：依次为单线P+ADO、无方向门单线P+DCO、保留方向门P+DCO。目标5→4 M1/E2，DCO目标先、下游4→2纯E2门；单一共同Gaussian源I=5，sigma/I=0.30即sigma=1.5。下游传播不重新生成Gaussian，不更改已验证相位/模型。

每模式delta为[-10,-5,-1,-0.5,-0.1,+0.1,+0.5,+1,+5,+10]。直接正式响应生成P/R，再给误差，中心不随机，独立进行一次PDM映射和统计；同模式/几何/网格复用正式响应缓存。独立9j不是运行前提、不增加GUI生成器。

| 集合 | 案例 | ratio组A/B | P角 | PDCO偏振方向门 | 角扫描域及步长 |
| --- | --- | --- | --- | --- | --- |
| 旧，冻结复用 | 30 | 125°/90° | 90° | 125° | ±89.9°，0.1° |
| 新，本轮计算 | 30 | 26°/90° | 90° | 90° | ±89°，0.1° |

DCO分子C(target A,gate B)，分母C(target B,gate A)，不可两项门都改90°；ADO为W(A)/W(B)。每组权重1，缺省phi用环强度平均；多探测器先合并强度后比值，mean/sum明确。新输入实际26°，不替换154°。新旧sigma域均[0.15,5]（sigma/I[0.03,1]）、步长0.025（sigma/I .005）；末格、节点和真实边界保留。比较须同时声明角域及PDCO门变化，不能只归因于小角。

误差DeltaP=max(0.1075,0.8|P|)，DeltaR=0.1|R|，左右正幅度分别保存。0.1075由冻结实验P左右误差样本的跨线中位数支持，仅为合成工作点；不调参、不用epsilon代替实验误差。原文献几何与输入完全保留，纯前向不造二维PDF。

## 4. 统计与命名

全部HDI/ETI为68%，在arctan(delta)边缘PDF评估，ETI16/50/84；所有HDI连通段分别保留端点、局部mode、mass及mass_fraction=mass/各段mass之和。mass和为.68，fraction和为1；角与sigma边缘各自归一、不可配对分支。积分用真实坐标与权重。

显示delta由角中心/端点直接tan，不重新排序delta PDF的HDI。命名明确tan{mode[arctan(delta)]}、tan{HDI68%[arctan(delta)]}、tan{mean[arctan(delta)]}。tan角均值不是delta算术均值，tan(mean±std)只是转换端点。真delta PDF含1/(1+delta²)因子，旧接口只保留读取兼容，不改快照。

内部完整精度，先tan后舍入；报告角用rad、默认小数点后两位，小非零用科学计数法。mean/std从所画PDF加权积分。

## 5. 报告与图片

新建inject_test.tex并由main.tex的\input{inject_test}引入，集中全部注入正文，两个主体章节为旧125/90与新26/90，分别三模式各10行输入—输出表及30张四联图。主文不重复保留旧注入。每行含ID/图、模式、自旋、delta/角真值、sigma/I、P/R左右误差、所有角HDI/mode及tan表示、ETI角/tan、恢复sigma/I。邻近共同设置表明确角组、权重、门线/次序与phi。仅宽长表页A4横向，优先一模式一页、可读字号；其它正文/短表/图竖向。

60注入+30文献二维模型各一套四联图，文献30模型/15跃迁/9前向分开计数。A完整有限观测响应域，横R纵P及左右误差棒，viridis色值明示；B横角纵sigma/I二维密度及真值；C角边缘有pi分数刻度，D宽度边缘，两者HDI仅填PDF下并标所有分支mode/fraction和阈值线，橙ETI与灰mean±std，真值线。边缘标题Full Range Marginalization; Constant Weight并说明实际域。

Python实际数据绘图，沿用Nature绘图QA：布局对齐、字形和碰撞检查、面板视觉核对。幻灯片当前δ+10换新数据，135Pr及旧资产哈希可追溯，不重复计算δ+10。

分模式给两组注入—恢复比较图与详细表，重点|delta|=5/10，区分角峰偏移、每HDI分支包含、ETI中心/端点、多解/折叠、实测Jacobian与跨sigma积分作用。保留失败，不预设26/90无偏。正文不展示重复生成器、随机重复、Clopper–Pearson或包含频率主线，无新随机或卡方。

## 6. GUI、JSON和新版本

所有数值框含聚焦/表格禁止滚轮改值，保留键盘/方向键/明确按钮，尽量让外页面滚动。共用控件层修复并回归。

推荐网格默认锁定，取消可手动并提示范围/精度/耗时；重勾按当前共同源自旋恢复。默认角域±89°内部rad；sigma下限保留整数.15/半整数.20，上限源I，单位切换仅改变表示。旧JSON非推荐域保留并手动，显式CLI网格可用。GUI/CLI/示例共享默认，测试锁/解锁/恢复、自旋、单位、导入与往返。

严格JSON支持指定顶层_help（单任务/批量/导出），不影响物理，其他未知字段仍报错。说明覆盖模式、目标/门/上下游、观测误差、方向/权重/方位环平均、角单位、内部sigma与显示sigma/I、源态换算、推荐/手动；区分待反演delta、已知门delta、合成标签。新几何示例重生成P/R，帮助有无结果一致，旧文件兼容。

执行前PyPI最新为0.1.1，本轮已选择未占用的0.1.2并正式发布、从PyPI安装精确版本复核；纳入尚未发行的delta命名订正。运行单元/GUI/CLI/例子及build/twine checks，tmp隔离安装wheel验证入口/包数据/依赖；使用既有安全凭据正式上传，不改全局认证/SSL、不输出token。发布后从PyPI安装精确版本复核。缺凭据或网络失败如实未发布。

## 7. 本轮验收清单

| ID | 状态 | 验收证据 |
| --- | --- | --- |
| G00 现场与计划 | completed | 启动规则、干净状态、旧数据计数/哈希、历史保存及现行合同 |
| G01 新30注入 | completed | 30真跑、正式缓存、完整输入/数组/统计、误差依据 |
| G02 GUI控件与网格 | completed | 全数值滚轮、锁/单位/自旋/旧导入回归 |
| G03 JSON示例 | completed | _help严格校验、三模式新P/R、导出/批量/结果等价 |
| G04 报告与比较 | completed | inject_test两章、60+30图、六张主表、真实大delta诊断 |
| G05 幻灯片资产 | completed | 旧图/135Pr哈希、新δ+10三模式图/Notebook |
| G06 构建与正式发布 | completed | 全测试、隔离wheel/PyPI读回、新版安装命令 |
| G07 全页与归档 | completed | main.pdf逐页视觉/编译、机器数值/图表/68%/fraction一致 |
| G08 知识与Git | in_progress | 新source/knowledge、归档门、handoff、显式commit非force push |

完成必须有本轮实际验证，历史测试/旧报告不代替。有限域的确定性注入不证明普遍无偏或频率覆盖，文献依赖/声明几何与不兼容保留。研究证据不足时记录缺口、停止原因与下一步。
