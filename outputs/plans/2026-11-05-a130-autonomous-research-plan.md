---
type: task-plan
title: "A≈130 三轴形变与集体激发：全库审计、创新筛选与论文交付"
created: 2026-11-05
updated: 2026-11-05
status: active
goal_thread: "01a1a756-e768-7320-bc92-6bff2607f122"
---

# A≈130 三轴形变与集体激发：全库审计、创新筛选与论文交付

## 任务定义

在 `/workspace/wiki` 内完成三条相互耦合的工作线：

1. 对 `raw/`、`knowledge/`、`system/` 和已有写作包进行全库审计与温故知新，优先修正能够由直接来源、原始数据或确定性脚本核实的错误；
2. 围绕 A≈130 三轴形变、wobbling、chirality、signature partner、γ-soft/γ-rigid 和 shape coexistence 建立竞争解释，主动搜索 motivation、反证和可检验的单点创新；
3. 将证据闭环的一个核心创新点写成可复现的 EPJA/PRC/PLB 候选稿件，所有文章相关文件落在 `raw/writing/gpt/<topic>/`。

## 当前候选主线

### Primary: P-ADO alignment response dependence

当前最先推进的投稿候选是一个公开数据方法学论文：

> 对同一个 `^{67}Ga` 纯 E2 参考跃迁，跨 projectile、beam energy 和
> direct/cascade feeding 条件共享一个 `sigma/J` alignment nuisance 是否
> 会被公开表格数据反证？

单一创新点是：用 condition-specific/feeding-aware alignment profile
替代默认 shared `sigma/J`，并把未知 `alpha2-alpha4` covariance、projectile
family 和 pseudo-experiment coverage 纳入统计合同。这个问题直接服务
A≈130 wobbling/chirality/TiP 的 mixing-ratio 证据链；P-ADO 结果本身不冒充
A≈130 核素的新实验测量。目标期刊暂定 EPJA。

文章工作包：`raw/writing/gpt/pado-alignment-response-dependence/`。

### Secondary: `133Ce` response-aware identifiability

`133Ce` iThemba/AFRODITE 数据仍是核结构价值更高的第二候选：

- 用门匹配的 ADO/DCO/偏振矩阵和 workbook 计数重建观测量；
- 将 `sigma/J`、有限几何、效率、偏振灵敏度、背景和门选择作为显式 nuisance；
- 比较单声子 wobbling、signature-partner/TiP、γ-soft particle-core 和 crossing/configuration-mixing；
- 只有在独立 holdout、响应校准和数据身份闭合后，才把结论升级为论文主张。

当前数据缺少原始 list-mode、完整 `polarization.xlsx`、绝对寿命和完整 response
covariance，仍停在 partial-L4；项目页为
`knowledge/projects/a130-single-point-paper-133ce-response-aware-identifiability.md`。

两条路线不合并为 omnibus paper；每篇文章只保留一个中心命题。

## 阶段与验收

### 阶段 A：全库盘点与证据边界

- 建立 raw/knowledge/source/model/method/analysis inventory；
- 读取 A≈130 相关 project、synthesis、research-note 和直接 source；
- 对已有 `a130-triaxial` 稿件做材料复用与过度主张审计；
- 记录 source lineage、独立实验计数、缺失 locator、数据权限和 archive gate 状态；
- 将可复用的新事实写回 `knowledge/`，过程报告只放 `outputs/`。

验收：形成 A≈130 候选问题矩阵、证据依赖表和停止条件。

### 阶段 B：motivation 与新颖性反向检索

- 检索近年 A≈130 相关实验、理论和方法论文；
- 对每个候选做“已有人做过吗”的反方搜索；
- 比较 EPJA、PRC、PLB 的创新强度与篇幅要求；
- 将外部原件和可用 supporting material 归档到 `raw/papers/gpt/query/20261105-*`；
- 不以文献数量替代信息增益，不将摘要或 URL 当全文证据。

验收：保留 1–3 个有明确 falsifier 的候选，淘汰重复或输入不可得的路线。

### 阶段 C：可复现数据与模型验证

- 审计 `raw/data/SouthAfrica/133Ce*` 的 workbook、ROOT/m4b、校准、sorter 和矩阵谱系；
- 先重算 workbook 公式，再从门匹配矩阵恢复可比较的计数；
- 检查 prompt/unprompt 分支、背景窗口、效率和偏振校准；
- 对 P-ADO primary 先重建 `^{67}Ga` 十行公开表、shared/family/energy-dependent
  alignment models 和 pseudo-experiment coverage；
- 使用精确 F 系数、alignment 模型和公开模型作条件预测；
- 建立 negative control、gate/response sensitivity 和 independent holdout；
- 数据不足时输出 partial-L4 readiness，不生成代理实验后验。

验收：有脚本、输入 manifest、参数、随机种子/版本、失败检查和可复算图表。

### 阶段 D：单点论文包

- 选定一个核心 claim 和一个主要竞争解释；
- 写入 `raw/writing/gpt/<topic>/`：LaTeX、BibTeX、`data/`、图、绘图脚本、运行记录和数据溯源；
- 文章正文把实验事实、作者解释、模型结果和本任务推断分开；
- 对所有论文主张建立 claim-to-source/locator 表；
- 选择合适模板，先编译和自审，再做 paper evidence gate 的定向用户审核清单；
- 未经用户确认的关键 claim 保持 calibrated wording，不写成最终确定结论。

验收：稿件可编译、图表可重建、数据和代码路径完整、证据边界显式、未发表数据权限未越界。

## 全局停止条件

- 关键数据或响应身份无法闭合；
- 外部来源只能获得摘要/元数据，且缺失内容会改变主要判断；
- 所有候选都被已有工作覆盖，或创新只剩重画图/机械复现；
- 独立 holdout 无法保留；
- 继续检索不再改变候选排序；
- 论文只能依赖未授权的私有数据公开。

停止时保留 partial/stopped 结果、失败原因、下一步和可复制恢复入口。

## 当前风险

- `raw/writing/gpt/a130-triaxial/` 包含多条物理线，不能直接作为新稿结构或结论源；
- South Africa 数据是本地未发表用户数据；留档不等于公开发布授权；
- workbook 中的 `delta`、`B(E2)` 比值和“wobbling frequency”是派生结果，不能当作独立实验观测；
- prompt 与非 prompt 矩阵分支已经被内容审计识别，未经门匹配不能联合；
- Wiki 中存在大量 `needs_review` claims 和至少一个既有 archive gate 缺档，需要按当前研究所触及的 claim 定向修正。
