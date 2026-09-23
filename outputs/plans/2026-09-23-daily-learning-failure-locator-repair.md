# 日报首日失败：knowledge locator 验收修复计划

**目标:** 找出并修复 2026-09-23 Day 1 日报未通过 `knowledge-writeback` 的确定性原因，使后续日报能够在保留证据边界的前提下完成 canonical knowledge 回写验收。

**当前结论（只读分析）:**

- CLI 进程退出码为 0，日报十个必需标题、Wiki 边界预检、Wiki lint 和 `git diff --check` 均通过；失败点唯一落在 durable knowledge validator。
- 日报的 `knowledge-writeback` 块把三个独立 source claim ID 和页码合成了一个 locator 字符串：`D12-1, D12-7, AR-2 (PDF pp.53-60, 76-80)`。
- [`system/scripts/wiki_knowledge_writeback.py`](../../system/scripts/wiki_knowledge_writeback.py) 逐项要求 `sources[].locator` 原样出现在 source 页；Ding source 页分别存在 `D12-1`、`D12-7` 和 `AR-2`，不存在上述合并字符串，因此在第一个 locator 检查处确定性失败。
- `knowledge/projects/a130-thesis-evidence-matrix.md` 已留下 Day 1 行的未提交改动，但 validator 在完成 `changed_paths` 对账前就因 locator 异常返回，所以 receipt 中显示空的 `changed_paths`。该部分必须在修复时单独对账，不能把失败运行直接计为成功。

**范围与约束:** 本计划只处理 writeback contract 和已有失败回执；不修改 raw、PLAN、受保护 BibTeX，不清除 `needs_review`，不把失败运行改写成成功。所有改动完成前，正式 Day 1 状态保持未计数。

## 文件结构与职责

- `system/prompts/daily-learning.md`：规定模型生成 writeback JSON 的最小结构和 locator 原子性。
- `system/scripts/wiki_knowledge_writeback.py`：执行路径、anchor、source link、exact locator 和 changed-path 验收。
- `system/scripts/run_daily_learning.py`：组合最终成功门；只在所有检查通过后推进 `day_index`。
- `system/tests/test_wiki_knowledge_writeback.py`：覆盖单 locator、复合 locator、changed-path 和 no-op 行为。
- `system/tests/test_daily_learning_runner.py`：覆盖日报验收与状态推进边界。
- `outputs/learning-daily/2026-09-23.md`：已有失败报告，修复时只改 writeback 块和与其直接相关的状态说明。
- `outputs/learning-daily/2026-09-23-run-01/run.json`：已有失败回执，保留失败身份；通过新验收后再由 runner 产生新的成功回执，不覆盖原始失败记录。

## 任务分解（执行门：用户后续明确继续后才执行）

### Task 1：冻结失败证据并建立可复现 fixture

**Consumes:** 当前 receipt、日报 writeback 块、Ding source 页和现有 validator。

**Produces:** 一个最小测试 fixture，明确证明复合 locator 被拒绝、三个独立 locator 可通过；不修改生产文件。

- [ ] 写测试 `test_composite_locator_is_rejected_with_actionable_error`：`locator` 使用当前失败字符串，预期 `valid=False`，错误同时指出必须使用 source 页中的 exact locator。
- [ ] 写测试 `test_multiple_atomic_locators_are_accepted`：同一 source path 使用三个 item 或三个 source references，每个 locator 分别为 `D12-1`、`D12-7`、`AR-2`，并在 fixture knowledge page 中提供 anchor/link。
- [ ] 运行 `python3 -m unittest system.tests.test_wiki_knowledge_writeback -v`，预期新增测试先失败而既有测试保持通过。
- [ ] 记录失败运行的 knowledge snapshot、当前 matrix diff 和 receipt 状态；不恢复、删除或覆盖这些文件。

### Task 2：固化原子 locator contract

**Files:** `system/prompts/daily-learning.md`、`system/scripts/wiki_knowledge_writeback.py`、对应测试文件。

**Interface:**

- `sources[]` 中每个对象的 `locator` 必须是 source 页中可直接匹配的单一 claim ID、页码、图表号或能级位置。
- 页码范围、多个 claim ID 和解释性文字放入新的 `note` 字段（若需要），不得拼接进 `locator`；validator 只对 `locator` 做 exact containment 检查。

- [ ] 在 prompt 的 JSON 示例中给出 `D12-1`、`D12-7`、`AR-2` 的分条示例，并明确禁止逗号拼接、页码说明和多个 claim ID 混入一个 `locator`。
- [ ] 在 validator 中保留 exact containment 规则，改进错误信息，返回 source path、非法 locator 和“拆成多个 atomic references”的修复提示；不要自动拆分模型字符串，以免猜测 claim 边界。
- [ ] 运行 Task 1 的两个测试，确认复合 locator 仍失败、原子 locator 通过。
- [ ] 补充 runner 测试：durable validator 失败时 `status=failed-verification`、`counted_in_substantive_test=false`、`next_day_index` 不变；通过时才推进状态。

### Task 3：修复已有 Day 1 报告的 writeback 块并核对部分写回

**Consumes:** Task 2 的 contract；已有 `outputs/learning-daily/2026-09-23.md` 和 matrix diff。

**Produces:** 一个可验证的修复候选；原始失败回执仍保留，修复候选只有在完整验收通过后才允许进入正式 Day 1 计数。

- [ ] 将 writeback 的 `sources` 改为可逐项匹配的 `D12-1`、`D12-7`、`AR-2`；页码范围作为 note/summary 文字保留，不作为 locator。
- [ ] 检查 matrix 的 Day 1 行是否与报告声明一致，确认 canonical page link 和 source link 均存在；若发现行内容超出报告证据，先标记为待裁决，不扩大科学结论。
- [ ] 用 `validate_durable_knowledge(report, root, knowledge_before)` 对运行前 snapshot 做离线验收；预期 `valid=True`、mapped changed path 只包含 matrix page。
- [ ] 运行日报验证、Wiki lint 和 `git diff --check`；在用户批准前不推进 `next_day_index`，不把旧 receipt 改成 completed。

### Task 4：建立正式重跑与发布门

- [ ] 选择“修复现有报告并形成补偿 receipt”或“保留失败记录、重新执行 Day 1”中的一种，并在状态文件中记录选择理由；不得同时计数两次。
- [ ] 新运行必须产生新的 session、新的 `run.json` 和唯一 writeback 块；成功条件仍为 process、preflight、报告、durable knowledge、lint、diff 全部通过。
- [ ] 运行 `python3 -m unittest discover -s system/tests -p 'test_*.py'`、`wiki_boundary_check.py`、`wiki_automation_preflight.py`、`wiki_lint.py --fail-on error --no-git` 和 `git diff --check`。
- [ ] 只显式暂存本计划相关文件；提交前核对 staged 文件，不带入现有 knowledge 矩阵之外的用户改动、raw 或事件日志。

**验收标准:** 复合 locator 会给出可操作失败；原子 locator 可完成 writeback；失败日不推进状态；正式成功日产生完整回执并把 `next_day_index` 只增加一次。

**当前未执行项:** 本计划写入时未修改 validator、prompt、日报、knowledge matrix、state 或 runner，也未重跑日报。
