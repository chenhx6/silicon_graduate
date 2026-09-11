---
type: system-policy
graph-excluded: true
updated: 2026-07-10
---

# 科学证据与置信度政策

## 为什么不按来源数量机械定级

五篇相互转引的论文可能只有一份原始实验；一篇包含完整角关联、偏振和寿命测量的工作，反而可能提供更直接的证据。因此置信度同时考虑证据直接性、来源独立性、模型依赖和核查质量。Codex 在授权研究任务中完成 self-audit；用户审核保留给后续问答裁决和论文写作中的具体 claim。

## 六类陈述

| 类型 | 推荐措辞 |
|---|---|
| 实验事实 | “测得”“观察到”“给出” |
| 实验判据 | “该判据要求”“该观测量可区分”，并注明适用前提 |
| 作者解释 | “作者解释为”“文献指认为” |
| 模型结果 | “该模型计算得到”“在参数……下再现” |
| 我们的推断 | “我们推测”“工作假设是” |
| 综合判断 | “综合现有来源”“当前证据支持”，并保留限制和竞争解释 |

不得把后三类改写成无主语的确定事实。

## 置信度

- `low`：单一来源、间接证据、定位信息缺失，或存在显著竞争解释。
- `medium`：来源和定位明确，证据链基本完整，但仍有模型依赖或未解决反证。
- `high`：直接且可定位的证据、多项相互独立的约束、竞争解释已认真评估，并通过 Codex self-audit；它不等同于用户审核或论文准入。

Agent 可以依据证据和 self-audit 设置 `low`、`medium` 或 `high`；论文写作中的最终 claim 和措辞仍须按 paper evidence gate 由用户确认。

## Codex self-audit 与后续人工审阅

- 页面级 `review_status` 表示整页处理状态。`human-reviewed` 只说明用户看过该页并完成页面层复核，不等于每条 claim 均已确认。
- `human-reviewed` 不表示页面永久正确、完整或已穷尽所有可提取知识。用户质疑、发现冲突、新来源出现或具体 claim 用于论文时，仍可重新核验。
- claim-level `needs_review: true` 表示具体陈述仍保留证据成熟度或后续用途核验标记。Codex 完成直接来源、locator、claim kind、适用条件和竞争解释的 self-audit 后，可以更新对应 claim 状态；不得把该动作记录为 `human-reviewed`。
- 用户明确确认具体 claim 或明确圈定的一组 claims 后，才可记录真实 Human review，并据此处理论文用途的最终措辞。未发生用户审核不阻止 Codex 研究、普通问答、探索性综合或常规发布。
- 未完成 Codex self-audit 的内容可以用于研究导航，但必须标出当前核查程度；相关且可能有信息增益的内容不得仅因 `unreviewed` 而隐藏。Review status 是核查元数据，不是内容价值或可见性标签。论文使用仍须针对具体 claim 核查直接来源、locator、适用条件、数据一致性和竞争解释。

每次摄入或整理完成后，最终复盘必须列出 Codex self-audit 的 P0/P1 项和后续问答/写作核验入口。正式审计至少分别报告：页面级 unreviewed 数、source 页 unreviewed 数、claim-level `needs_review: true` 数、缺失 locator 的 claim 数、缺失 claim kind 的 claim 数，以及缺失 source/citation key 的来源项数。

## 核结构解释的最低要求

涉及 wobbling、chiral doublet、γ-soft 或 γ-rigid 的综合页，至少包含：

1. 支持该解释的观测量；
2. 关键判据适用的模型前提；
3. 替代解释；
4. 当前证据缺口；
5. 能改变结论的未来测量或计算。

## 引用定位

优先级依次为：

1. 原始数据表、图、能级方案或补充材料；
2. 原文页码与段落；
3. DOI/期刊元数据；
4. 二手综述。

若只能使用二手来源，必须显式标记，后续应寻找原始来源。

论文级使用还必须满足 `system/paper-evidence-gate.md`。Wiki 未收录某类文献只能说明当前库未覆盖，不能据此写“没有相关工作”或“一篇不漏”。

## 分析性重建、暂定推理与知识晋升

可追溯性限制的是未经审核的知识晋升，不限制 Agent 在授权研究任务中进行深入推理、跨来源比较、条件化迁移、竞争解释分析、反向检验或研究问题形成。

- `source-grounded evidence` 只承载来源直接支持且可定位的内容。
- 作者明确说明的动机、设计逻辑、推理链和限制可以进入 source，并保留 locator。
- Agent 对上述内容的分析性重建必须与作者明示内容分开，标为 `Analytical reconstruction` 或 provisional interpretation，并列出证据、locator、推断步骤和不确定性。
- 暂定研究推理可以被保留和审核，但不得冒充论文事实、作者结论、正式 synthesis、用户已采用的 project 判断、稳定 memory 或普通 log。
- 晋升到 project、synthesis、method、concept 或其它正式知识前，必须由 Codex 确认 provenance、适用条件、竞争解释和 self-audit 结果；只有后续问答或论文写作需要用户裁决时再记录 Human review。被新证据修正、拒绝或取代时保留处置依据，不静默删除认识变化。

普通问答中的低价值联想、重复摘要或无充分依据的问题不持久化。高价值暂定推理的具体字段由 `system/schema.md` 定义，创建、持久化、晋升和处置由 `system/workflows/reflect.md` 管理；research-note 仍不得伪装成正式知识或替代 source evidence。
