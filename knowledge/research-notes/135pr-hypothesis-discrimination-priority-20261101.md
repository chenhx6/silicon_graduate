---
type: research-note
title: "`135Pr` 竞争假设的可区分预测与测量优先级"
aliases: [135Pr hypothesis discrimination priority, 135Pr measurement value of information]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [matta-2015-transverse-wobbling-135pr, lv-2022-evidence-against-wobbling-135pr, sensharma-2019-two-phonon-wobbling-135pr, sensharma-2026-evolution-chirality-transverse-wobbling-135pr, guo-2021-comment-transverse-wobbling-135pr]
created_from: "2026-11-01 Day29 continuation: hypothesis-discrimination design"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: 135pr/competing-hypotheses/measurement-design/value-of-information
nuclei: [135pr]
observables: [angular-distribution, polarization, rac, mixing-ratio, lifetime, b-e2, b-m1, transition-identity]
tags: [135pr, wobbling, tilted-precession, signature-partner, configuration-mixing, chiral, falsifier, l3, l4-readiness]
---

# `135Pr` 竞争假设的可区分预测与测量优先级

## Research Trigger

`135Pr` 的公开结果已经把争议压缩到少数几条连接线，但“支持哪一方”仍容易被
论文数量、单线 `δ` 或作者模型名称带偏。本页把大胆假设保留下来，同时把每个假设
翻译成可被同一响应合同检验的预测，并按预期 belief revision 排列下一次测量。

这不是对任何模式的最终裁决。它是一个 L3 研究设计：允许在输入尚不完整时提出
高价值假设、预测和 falsifier，但不把条件支持升级为实验事实或 L4 结果。

## Grounded Evidence

| Evidence layer | Atomic locator | What it establishes | Boundary |
|---|---|---|---|
| Matta support chain | [[matta-2015-transverse-wobbling-135pr]] `M15-4`, `M15-5`, `M15-9` | 747/813-keV links 的大 `\(\lvert\delta\rvert\)`、正 asymmetry 记录及 `E_wob` 能量趋势是 transverse-wobbling 解释的输入 | angular-distribution branch、alignment、`A` 与其它实验的 `P`/`R_ac` 不能直接合并 |
| Lv counter chain | [[lv-2022-evidence-against-wobbling-135pr]] `L22-4`, `L22-5`, `L22-7`, `L22-14`, `L22-15` | 独立 JUROGAM `P-R_ac` 给出小 `\(\lvert\delta\rvert\)` 分支，补充材料记录门污染控制和 realignment 模型 | response、逐门 counts、完整联合协方差和 absolute strengths 仍缺 |
| Sensharma continuation | [[sensharma-2019-two-phonon-wobbling-135pr]] `S19-4`, `S19-5`, `S19-6`; [[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]] `SH26-3`, `SH26-8`, `SH26-10`, `SH26-11` | two-phonon/DB 连接和固定 `\(\sigma/I=.2\)` 下的条件分支偏好；作者也指出 lifetime 对绝对几率和歧义消除的重要性 | 共享 Gammasphere 谱系；无新 polarization/absolute lifetime，不能作为独立第三次实验 |
| Methodological counterpoint | [[guo-2021-comment-transverse-wobbling-135pr]] `GU21-2`, `GU21-3` | 旧角分布可能保留大、小分支，单一正 polarization asymmetry 不能独立选根 | 依赖 Matta 报告，不是新的 event pool |

## Competing Hypotheses

| Hypothesis | Conditional prediction | Necessary companion observable | Falsifier |
|---|---|---|---|
| `H_TW`: low-spin transverse wobbling | 在共同 alignment/feeding/response profile 下，核心连接线保持 E2-rich 大根，并与声明的 `E_wob` 自旋趋势相容 | 同一 transition identity 下的 count-level AD、polarization/`R_ac` 和至少一条 partner-resolved lifetime/absolute `B(E2)` | 三条核心线的联合 profiled prediction set 稳定落在小根或与绝对 E2 strength 不相容，且结果对 calibration/Cov 不敏感 |
| `H_TiP`: tilted precession / realignment | 小 `\(\lvert\delta\rvert\)`、M1-dominated 连接与逐带 single-particle/total-angular-momentum realignment 可以在同一门条件下共同解释 | `P-R_ac` 原始 counts、取向/feeding nuisance 和一个不参与 branch 选择的 absolute EM holdout | 在同一 response contract 下小根的联合预测被排除，且 realignment 模型不能覆盖能量和 EM holdout |
| `H_SP/CM`: signature partner or configuration mixing | 能级近简并和相对强度可以出现，但不要求统一的 wobbling phonon order；line-dependent branch、交叉或带内/带间绝对强度不对称是可检验信号 | partner-resolved lifetime、绝对 `B(E2)`/`B(M1)`、g-factor 或 configuration-sensitive linking | 在固定 state identity 后，所有允许的 partner/mixing 预测均无法覆盖共同 EM 与能级数据 |
| `H_CH`: high-spin DB1/DB2 chiral interpretation | 高自旋近简并 dipole bands 和小根连接可支持作者的 chiral reading，但不能自动重写低自旋 TW/TiP 争议 | parity、partner-resolved absolute strengths、寿命和独立连接线；必须保留与低自旋带的 state lineage | 若独立 partner-resolved observables 与 chiral geometry 不相容，则下调该高自旋解释；不能用低自旋结果直接替代 |

表中 `H_CH` 是同一核素内的高自旋竞争层，不是把 2026 论文的作者解释转成
低自旋事实。四个假设都允许在新证据出现前保持活跃；它们的权重只能由预先声明
的观测和 falsifier 改变。

## Highest-information Measurement

设计推断上，最有信息增益的单次测量不是再取得一条相似的中心 `δ`，而是把一个
核心连接线做成同一事件/响应体系中的三联观测：

1. 以 `747` 线为主线，同时保留真实角组的净峰 counts、sideband 和 random；
2. 在相同 state/gate lineage 下取得 polarization 或 `R_ac` 的原始计数；
3. 对同一母态的竞争退激取得 partner-resolved lifetime 或绝对分支归一；
4. 将 `813` 线预先冻结为 holdout，`450` 线作为敏感性检查，不把三条线算成三次独立实验；
5. 在 acquisition 层保存 detector response、效率、deadtime、feeding/alignment 和
   共享 calibration covariance。

这项设计同时攻击两层不确定性：第一层判断大、小 `\(\delta\)` 是否只是 response
或 branch-selection 差异，第二层判断即使 branch 被选定，wobbling 是否仍能区别于
tilted precession 或 configuration mixing。若只能追加一种观测，partner-resolved
absolute EM/lifetime 的机制信息通常高于再做一条同类角分布；这是研究设计推断，
不是已测得的统计功效或实验排序。

## Minimum identifiability audit

The `135Pr` contract has three non-interchangeable layers:

1. **Object layer:** freeze the mother state, daughter state, gate ancestry and
   acquisition lineage for `747`, `813` and `450`. If this layer fails, a common
   likelihood is not defined.
2. **Branch layer:** use an interference-sensitive combination such as AD plus
   polarization/`R_ac` to select or profile the large/small `δ` roots. Matta's
   `747`/`813` polarization asymmetries and Lv's `P–R_ac` values are not a single
   event pool; they cannot be subtracted or pooled as if they shared one response.
3. **Mechanism layer:** use a partner-resolved lifetime or absolute `B(E2)`/`B(M1)`
   observable to test collectivity after the branch has been profiled. Relative
   mixing ratios alone do not supply this layer.

The source ledger makes the missing bridge explicit. Matta's Table I gives no
experimental `rE2/rM1` pair for `747` and reports no new absolute lifetime, while
the `813` relative ratios depend on an in-band denominator and are not an absolute
matrix-element measurement (`M15-D22-002`, `M15-D22-R095-1`). Lv supplies a
three-line `P–R_ac` branch result and a derived `B(E2)` ratio, but the source still
does not provide the event-level response, full joint covariance or a
partner-resolved absolute-strength block (`L22-D22-R095-1`, `L22-D20-R41-2`,
`L22-18`). Therefore the practical minimum is a matched `747` branch block plus
the same-parent `526.2-keV` companion lifetime/absolute normalization, with `813`
frozen as a leave-EM-out check and `450` retained as sensitivity line.

This gives a direct reverse test: if a model changes rank only after relative ratios
are converted with an assumed pure-E2 denominator, the change is an input-convention
effect rather than a mechanism result. A mode claim can advance only when the rank
survives the object, branch and mechanism layers together.

## Belief Revision Rules

| Joint outcome | Revision | What remains forbidden |
|---|---|---|
| 三条核心线在共同 profile 中稳定偏向大根，且独立 absolute EM holdout 与 E2-rich 预报相容 | 上调 `H_TW`；降低“纯响应差异”解释的权重 | 仍不能写成 wobbling 已被唯一证明，除非 partner identity、寿命和独立 holdout 均闭合 |
| 三条线稳定偏向小根，且 realignment/TiP 模型覆盖能级和 EM holdout | 下调 `H_TW`，上调 `H_TiP` 或 `H_SP/CM` | 不能把小根直接等同于 TiP，也不能把模型拟合当独立实验事实 |
| 747、813、450 的分支随 gate/阵列改变，或共同 Cov 使两根重叠 | 优先修订 response、feeding、transition identity 或 event lineage | 不能用论文投票、单线中心值或局部 `\(\chi^2\)` 选模式 |
| branch 已闭合但 absolute EM 显示 line-dependent collectivity/crossing | 下调统一 phonon-order 叙事，转向 partner/configuration mixing 分析 | 不能用 `E_wob` 单变量恢复统一模式 |

## Readiness and Stop Rule

当前可做的是公开 evidence audit、假设排序和测量设计。没有逐角/逐 gate counts、
真实 response、event/run overlap、联合协方差和独立 holdout 时，研究停在 L3。
不得生成 Bayes factor、全局 `\(\delta\)` CI、排除 sigma、统一显著性或“已排除”
竞争机制。

若某个新来源只增加书目、摘要、同谱系再分析或已知 supplementary locator，而不
增加新的 observable/response/Cov/holdout，则记录 `verified-no-op` 并转向下一候选。
若取得真实输入但缺少独立 holdout，最多进入 candidate-L4/readiness，不自动形成
机制终局结论。

## Provisional Reasoning

把 `747`、`813` 和 `450` 组织成“主线—holdout—敏感性线”会比按论文或按中心
值投票更容易发现 branch 与 mechanism 是否混淆。这个排序依赖一个设计假设：三条
线的 transition identity 可在新采集或逐事件 ledger 中冻结；如果该假设失败，优先级
应退回 state/lineage 审计。这里的“最高信息增益”是定性判断，不是由现有数据估计的
Fisher 信息、统计功效或机时最优解。

## Assumptions

- `H_TW`、`H_TiP`、`H_SP/CM` 和 `H_CH` 是候选解释标签，不是观测量。
- future response、feeding、alignment、deadtime、background 和 covariance 可以
  被逐 acquisition 记录；当前并没有把它们当作已经存在的输入。
- `813` 可作为预先冻结的外部检查，前提是它没有参与 branch 选择或模型调参。
- absolute EM/lifetime 的测量目标、门条件和归一化必须在实验前定义；不能用公开图像
  读数补成新寿命或绝对强度。

## Competing Explanations

branch 差异可能来自真实多极性、有限 alignment、feeding、门污染、响应/校准、
transition misidentification 或同一谱系的不同重分析。即使共同 response 选出某个
`δ` 分支，能级和相对强度仍可能由 wobbling、tilted precession、signature partner
或 configuration mixing 共同解释。高自旋 DB1/DB2 的 chiral reading 还可能只属于
另一自旋/构型区间。

## Transfer Conditions

这套主线—holdout—敏感性线结构可迁移到其它低自旋 wobbling 争议，但必须重新核对
transition identity、同事件关系、响应矩阵、独立性和 holdout。四个假设表中的具体
能量、分支和优先级不能直接迁移到其它核素。

## Failure Conditions

若 `747` 的母态/末态、门条件或 acquisition lineage 不能冻结，停止“branch +
absolute EM”联合设计并先做 identity audit。若真实数据只有 summary central values，
不能把它们扩展为 event-level likelihood。若所有新增来源只是同谱系复述，则该路线
记录 verified-no-op，不重复计权。

## Falsification or Reverse Tests

对每个候选假设预先生成 response-folded prediction set；分别改变 alignment、feeding、
background、calibration covariance 和 gate selection，检查结论是否保持。若只有在
固定 nuisance 切片上出现分支排序，反向结论是“当前输入不足以区分”，而不是某个
模式被排除。若 branch 与 absolute EM 同时闭合，再用 `813` holdout 检查是否仍能
预测未参与选择的连接线。

## Open Questions

- 是否存在可合法取得的 `135Pr` event/run ledger、逐角净峰、polarization counts、
  response 或原始 covariance？
- `747` 的 partner-resolved lifetime 哪一条退激支最能减少 branch 与 mechanism 的
  混淆，而又不复用训练观测？
- 高自旋 DB1/DB2 与低自旋 bands 的 state/configuration lineage 能否逐线闭合？
- 若真实输入仍不可得，能否把该设计迁移到一个有公开多观测量数据的邻近核素？

## Knowledge Impact and Learning Decision

`supports`: `135Pr` 已从“哪篇论文更可信”的叙事问题推进为四假设、三核心线和
一项高信息测量的可证伪设计。

`limits`: 当前没有新的 event-level 数据、响应文件、联合协方差、寿命或 absolute
strength；本页没有重拟合公开图像，也没有改变现有实验模式判断。

`revises`: 后续分析优先级从“再找一条相似 `δ`”改为“同一连接线的 branch + absolute
EM + 独立 holdout”，并把高自旋 chiral reading 与低自旋争议严格分层。

## Human Review

本页是 Codex self-audit，`review_status: unreviewed`、`reasoning_status: provisional`。
它允许提出大胆假设和可检验预测，但不替代用户审核、primary raw 或论文级 evidence gate。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-01 | Day29 continuation hypothesis-discrimination design | none | provisional L3 design | Existing source claims support a branch conflict and competing explanations; a matched branch-plus-absolute-EM design adds a durable research decision without inventing missing data | [[post-30-day-nuclear-structure-paper-prospectus]] |
