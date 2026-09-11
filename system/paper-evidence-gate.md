---
type: system-policy
graph-excluded: true
updated: 2026-07-10
---

# 论文级证据门

本规则用于判断 Wiki 内容能否进入论文级证据池。它不是论文写作模板，也不表示当前 Wiki 已完整覆盖文献。

The paper evidence gate is a conditional manuscript-readiness check. It is not the default operating mode for ordinary Wiki questions, exploratory synthesis, research discussion, or early drafting.

Failure to pass the paper evidence gate does not prohibit discussion, provisional synthesis, or draft generation. It requires calibrated wording, traceable supporting material when available, and a clear indication of what should be checked before final submission.

中文边界：未通过 paper evidence gate，不等于不能讨论、不能写草稿或不能提出合理推断；只表示正式投稿、正式引用核查或关键主张确认前，还需要进一步检查直接来源、精确 locator、适用条件、数据一致性、竞争解释和引用风险。

## Candidate evidence and claim admission

1. **Knowledge discovery / candidate evidence**：高度相关且有信息增益的材料，无论页面或 claim 的 review status，均可用于普通问答、研究讨论、探索性综合、早期草稿、文献发现和 candidate manuscript evidence discovery。Review status 影响不确定性说明和核验优先级，不决定相关内容是否可被检索或主动呈现。
2. **Claim-specific verification**：当材料可能进入论文、正式引用或关键主张时，针对当前准备使用的具体 claim 和准确措辞，核查原始 source、必要 raw、作者原意、精确 locator、数据与不确定度、适用条件、claim kind、source attribution、竞争解释及当前使用语境；无需先全面审核整页。
3. **Paper admission**：Codex 可以执行并报告具体核验、建议可支持的措辞强度；最终准入和措辞必须由用户明确确认。确认只适用于已核验 claim 和当前语境，不自动改变页面级 `review_status`、其它 claims 的 `needs_review`，也不扩大为整页审核完成。

A page may remain `unreviewed` while a specific claim is directly verified and admitted for a specific manuscript use. A `human-reviewed` page does not by itself qualify a specific claim when precision, controversy, new evidence, or wording risk requires claim-specific verification.

## 科学主张准入条件

论文正文使用 Wiki 支撑科学主张时，至少满足：

1. 当前准备写入论文的具体 claim 已完成 claim-specific verification：回到原始 source 和必要 raw 原文，核对作者原意、精确 locator、数据与不确定度、适用条件、claim kind、source attribution 和竞争解释，并由用户确认该 claim 及拟采用措辞可用于当前论文语境。页面级 `human-reviewed` 只记录既往页面复核，不能单独替代当前关键 claim 的核验；页面整体也无需先完成全面人工审核；
2. claim 有精确 locator，例如页码、图号、表号、能级、跃迁或数据位置；
3. 明确区分 experimental fact、experimental criterion、author interpretation、model result、Codex/我们的暂时推断和 cross-source synthesis；
4. 关键解释已经检查竞争解释或完成反向检验；
5. 回到原始 source 和必要的 raw 原文，不能用 synthesis 代替原始文献；
6. citation key 已存在；缺失时只能列为待补，不得编造；
7. 尚未完成 claim-specific verification 或用户确认的内容，不得写成最终确定的论文结论，也不得描述为已经通过 paper evidence gate；但相关且可能有用的内容必须作为 candidate evidence 向用户呈现，并说明 review、source、locator、适用条件和缺口，以及最值得核查的位置，不得仅因 `unreviewed` 而隐藏。它仍可用于研究讨论、探索性综合和带明确限制的早期草稿。

Wiki 未收录某类文献，只能写“当前知识库未覆盖”。不得据此声称“没有相关工作”“文献已经完整覆盖”或“一篇不漏”。

## Paper-use Human review triage gate

任何准备进入 paper evidence gate 的 claim、project statement、synthesis-supporting statement 或 data-analysis-derived statement，默认必须列为 P0 或 P1 审核对象。P0/P1 是当前关键 claim、证据项或高风险位置的核验优先级；focused review 可以满足当前 claim 的审核需求，不要求全面审核整页或整篇文献，除非该 claim 依赖更广上下文。其它 claims 保持原状态。

P0/P1 focused review 和用户确认未完成时，不得描述为“可直接用于论文”“可直接作为论文结论”“已经进入 paper evidence gate”或“无需回原文引用”，但仍须呈现 candidate evidence、风险和最值得核查的位置。完成当前 claim 的 focused review 和用户确认后，可以判断该 claim 对当前论文措辞的支持能力，不自动将整个页面或文献标记为已审核。这个用户确认门只在实际论文写作、正式引用或用户要求的严格 claim 核查中触发，不阻止普通研究、Codex self-audit 或常规知识发布。

Synthesis 可以组织跨来源思路，project 可以推进证据链，但两者都不能替代 source 和原文 locator。论文写作仍须回到原始来源，并满足本文件的全部准入条件。普通研究中的 P0/P1 由 Codex self-audit 处置；只有准备进入论文用途时，才需要本节规定的 focused review 和用户确认。

进入 paper evidence gate 的最终复盘必须完整列出全部 P0；P0 可以分批展示，但不得聚合隐藏、降级或省略。P1 可以按主题或页面分组，但仍须展示实际判断、证据、Agent inference 和审核目的。每个 P0/P1 必须保留文件、claim/section、locator、审核事项和风险；P2/P3 可以聚合。

## 投稿前漏引检查

投稿前至少检查：

1. 已精读 Wiki 中的相关 source 和 synthesis；
2. 更大的本地全文语料或文献库；
3. 必要时在线学术检索；
4. 记录检索式、检索日期、数据库或语料范围及覆盖限制。

本检查完成前，不得把 Wiki 的来源集合描述为领域完整书目。

## 未来写作 Skill 接口

当前阶段只预留接口，不创建写作 Skill。

未来写作 Skill 可辅助 literature review、introduction/background、创新点候选梳理、claim-to-paragraph、related-work 比较和 evidence-table-to-paragraph。它应优先读取：

- `README.md`、`AGENTS.md`；
- `system/evidence-policy.md`、本文件和 `USER_GUIDE.md`；
- 相关 source、synthesis、concept、observable、nucleus 和 band 页面；
- `.bib` citation key 信息；
- 用户提供的数据处理结果和人工确认结论。

生成论文级文字前必须检查 source、locator、claim kind、citation key、人工复核状态、竞争解释/反向证据，并确认没有把 synthesis 当作原始文献。

A writing skill may surface reviewed or unreviewed candidate evidence with explicit review/source/locator status and verification tasks. It may use unverified candidates for exploratory drafting with calibrated wording, but final manuscript claims require claim-specific verification and explicit user confirmation. Whole-page review is not a prerequisite, and admitted claims must remain clearly separated from unverified candidates.

允许输出草稿段落、证据表、创新点候选、related-work 对比、引用候选及缺失证据/待人工确认清单。不得自动：

- 宣称文献完整覆盖；
- 把未复核 claim 写成确定结论；
- 把 synthesis 当作原始文献引用；
- 编造 citation key 或实验数据；
- 替用户决定最终创新性；
- 修改论文正文或提交 Git，除非用户明确要求。

满足以下条件后再考虑创建写作 Skill：

- source/synthesis 层已经较稳定；
- citation key 基本补齐；
- 本证据门已经实际执行；
- 至少存在一个真实 project 或 synthesis 闭环案例；
- 用户已有数据处理结果或明确写作目标。

候选名称仅作接口记录：`wiki-paper-draft`、`wiki-literature-review`、`wiki-innovation-map`、`wiki-claim-to-paragraph`。
