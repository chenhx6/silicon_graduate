---
type: research-note
title: "A≈130 三轴形变研究的模型、代码与运行时路线审计"
aliases: [A130 model route audit, triaxial model code route 20261105]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [a130-model-runtime-and-public-code-audit-20261105, a130-model-choice-card, a130-single-point-paper-133ce-response-aware-identifiability]
created_from: "Full-library audit, public-code acquisition and delegated runtime checks"
scope: a130/model-selection/code-reproducibility/paper-route
nuclei: [133ce, 135pr, 132la, 130ba, 163lu]
tags: [a130, triaxiality, wobbling, model-selection, reproducibility, code-audit]
---

# A≈130 三轴形变研究的模型、代码与运行时路线审计

## Research Trigger

全库审计显示，旧 A≈130 论文包把模型名称、预设曲线、实验观测和图件缓存
混在一起；用户要求把公开核结构模型、壳模型、Geant4 等工具全部纳入重新
评估，并寻找可以收束为一篇单点论文的创新。

## Grounded Evidence

核心 source 页为 [[a130-model-runtime-and-public-code-audit-20261105]]，公开材料
清单位于 `raw/papers/gpt/query/20261105-model-runtime-audit/manifest.json`。
运行结果和资源约束见
`outputs/l4/20261105-a130-model-runtime-audit/report.md`。既有 A≈130 物理边界
来自 [[a130-model-choice-card]]、[[131ce-133ce-mode-identifiability-boundary]]
和 [[pado-alignment-response-dependence-paper]]。

## Model inventory and evidence status

| Route | Current status | What it can support | What it cannot support yet |
|---|---|---|---|
| PTRM/QTR scaffold | 可运行的本地简化模型 | 参数鲁棒性、极限、wobbling energy 形状 | 完整 QTR、全电磁矩阵元和实验模式确认 |
| HFODD v2.73y | 公开 benchmark 已运行 | 自洽 Skyrme-HFB 旋转形变、配对和 alignment 的局部演化 | 目标奇核无对称性 TAC-CDFT、partner splitting 唯一解释 |
| DIRHB | 公开论文和代码路线，当前单元未编译 | 静态偶偶 RHB/三轴势面候选 | 已复现目标核素数值、奇核高自旋 TAC |
| TPSM scaffold | 本地简化投影程序可运行 | 角动量投影公式、基底混合和极限检查 | 完整非正交核/Pfaffian/算符验证和发表级 TPSM |
| BIGSTICK | 公开串行 sd-shell benchmark 已运行 | 壳模型工作流、Lanczos 输出和受限交叉检查 | A≈130 SN100 高自旋完整空间和有效算符闭合 |
| IBM/ArbModel | 源码路线受 Eigen 依赖阻塞 | 未来偶偶 core 系统学 | 当前可复现第三方 IBM 结果 |
| CSM/TRS | 公开老代码路线，当前未编译 | Routhian、alignment、回弯和组态交叉 | 绝对 E2/M1、partner-band 量子分裂 |
| Geant4 + ROOT | smoke test 已通过 | 指定几何和响应下的 DCO/偏振/效率敏感性 | 没有真实阵列参数时的实验修正 |
| NPTool | 历史对象 source 已审计，当前不可执行 | 代码对象/单位/调用合同 | 当前生产分析或新实验响应 |

## Innovation Search After the Audit

### Candidate A: P-ADO alignment-response and coverage paper

这是当前最成熟的单点创新。它不声称发现新的 A≈130 能级，而是把
“跨反应条件转移同一 `sigma/J` alignment nuisance”变成一个可检验的
profile/coverage 问题。公开 `^{67}Ga` 表格提供可复现基准，A≈130 物理意义
来自 mixing-ratio 分支会被用于 wobbling、chirality 和 TiP 判别这一事实。

当前工作包已经包含 shared/family/energy/mixture 模型、共同协方差敏感性、
maximum-row coverage grid 和 claim ledger。目标期刊首选 EPJA Regular Article；
现阶段仍是 `partial/not-ready`，因为原文没有事件级计数、row covariance、
detector response，且 P0/P1 论文用 claim 尚未完成用户定向审核。

### Candidate B: `133Ce` response-aware collective-mode identifiability

这是核结构价值更高、但数据风险更大的路线。核心不是重新宣称 W1 是 wobbling，
而是把 wobbling、signature partner/TiP、γ-soft particle-core 和
crossing/configuration mixing 放进同一 forward likelihood，显式保留 gate、
alignment、response、feeding 和 covariance，并以未参与拟合的 gate family
或 transition block 做 holdout。

当前 South Africa 数据仍缺 event list、完整 polarization input、absolute
lifetime、producer-level covariance 和独立 holdout，因此只能保持
partial-L4/local-only-unpublished。若这些输入闭合，首投 EPJA，结果足够强且
竞争模型排序在 holdout 上稳定时再考虑 PRC。

### Candidate C: HFODD-constrained rotating-shape paper

HFODD 路线可形成一个较窄的理论文章：固定泛函、配对方案、基组和 blocking，
只追踪一个 A≈130 核的少量旋转频率点，报告 \(\beta_2,\gamma\)、配对和
alignment 的自洽演化。它的创新只能是“自洽形变演化对某个观测量的约束”，
不能把平均场输出直接写成 wobbling 或 chirality 的唯一证据。

当前还没有完成目标核素输入、阻塞态连续追踪、基组收敛和实验 companion
observable；因此它是下一条理论路线而不是本轮文章。

### Candidate D: Geant4/ROOT response-bias paper

若取得真实阵列几何、阈值、死层、能量分辨和校准数据，可以只选一个 A≈130
级联，计算有限立体角、Compton scattering 和分辨率对 `P(theta)` 或
`R_DCO` 的偏差。这会是一个清晰的方法学单点，但当前没有完整几何和响应
协方差，不能把示意模拟写成实验校正。

## Decision

当前主线按信息增益排序：

1. 继续完成 P-ADO 的 source/coverage/feeding claim self-audit，保持 EPJA
   Regular Article draft；
2. 继续维护 `133Ce` 为 secondary nuclear-structure candidate，等待响应、
   producer 和 holdout closure；
3. 将 HFODD 和 Geant4 作为针对性独立验证工具，不把它们堆入当前 P-ADO 文章；
4. 只有在单一物理问题和独立观测量明确后，才启动完整 TPSM、TAC 或 SN100
   shell-model 计算。

## Competing Explanations

能级、signature splitting 或单一 mixing-ratio 结果都可能由多个机制解释；模型
间的优劣必须通过独立的 E2/M1、偏振、寿命、响应控制或 holdout 来比较。
代码的运行成功只证明软件路径可执行，不构成对物理模式的实验证明。

## Failure Conditions

- 目标核素输入或 blocking/configuration identity 无法固定；
- 模型输出没有独立实验 observable 可检验；
- response、feeding、有效电荷或 covariance 只能靠未声明的默认值填补；
- 结果只在一个手工参数点成立；
- 文章需要把 private unpublished data 或 synthetic event sample 写成公开实验事实。

## Knowledge Impact

本笔记把模型路线从“工具清单”压缩为带有可运行性和证据边界的决策层，并支持
当前两篇候选文章分流：公开表格方法文章先收束，`133Ce` 核结构文章等数据闭合。
它不改变 `PLAN.md`，不提升任何页面到 `human-reviewed`，也不改变 private data
的发布权限。

## Human Review

本页是 Codex self-audit；尚未发生论文级用户 claim review。

## Provisional Reasoning

对当前文章队列，信息增益主要来自可复现的证据边界和独立验证，而不是继续
堆叠没有输入合同的模型名称。P-ADO 的 table-level profile/coverage 已有
可运行分析，故先收束；`133Ce` 的核结构创新只有在 response、producer 和
holdout 闭合后才有足够的可证伪性。

## Assumptions

运行时版本和公开 benchmark 的身份以本轮回执和归档 manifest 为准；本地简化
脚本不自动等同于外部完整模型。邻近偶偶核 PES 只作先验，不能替代 `133Ce`
奇核直接计算。

## Transfer Conditions

模型路线只有在版本、输入空间、有效算符、blocking/configuration 和实验
companion observable 重新固定后，才可从 benchmark 或邻近核迁移到目标核素。

## Falsification or Reverse Tests

对 HFODD 运行目标核素时改变基组、初始态和频率步长，检查连续构型是否保持；
对 BIGSTICK 改变可辩护的空间截断和有效算符，检查主要结果是否稳定；对
Geant4 用已知源和不同随机种子检查响应闭合；对 P-ADO 和 `133Ce` 使用未参与
拟合的 transition/gate holdout。若模型排序只在单一默认设置下成立，则撤回
强主张。

## Open Questions

- HFODD v2.73y 的完整 source package 能否从官方 Mendeley 数据集稳定取得并
  固定哈希？
- 是否能在当前资源约束下完成一个 A≈130 奇核的 blocking continuation？
- `133Ce` 是否能取得 producer-level response covariance 和独立 holdout？
- P-ADO 论文在完成用户 P0/P1 定向核查后是否达到 EPJA Regular Article 门槛？

## Promotion or Rejection History

2026-11-05：模型/代码路线从临时运行结果提升为 source/knowledge 记录；P-ADO
继续作为公开数据主线，`133Ce` 保留为等待 response/holdout 闭合的 secondary。
