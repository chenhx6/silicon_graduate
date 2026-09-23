---
type: system-governance
graph-excluded: true
created: 2026-09-23
updated: 2026-09-23
---

# Wiki 路径契约

这是仓库唯一的内容落点契约。`AGENTS.md`、摄入/反思/查询/自治研究工作流、每日学习 prompt 和自动化预检都引用本页；如果其它说明与本页冲突，以用户当前指令和本页为准。契约只规定仓库内的路径，不扩大科学研究范围，也不改变 raw 证据的保护规则。

## 六类持久化边界

| 路径 | 唯一职责 | 可以写入 | 不得写入 |
|---|---|---|---|
| `raw/` | 用户原始论文、手稿、数据、图片、笔记和其它原始材料 | 用户明确提供的原件；已授权的 `raw/papers/gpt/_incoming/`、`raw/papers/gpt/` 和 `raw/zotero/gpt.bib` 入口 | 知识页、日报、计划、审计、临时缓存；不得覆盖、改写、重命名或批量整理用户原件；`raw/zotero/wiki-inbox.bib` 始终只读 |
| `knowledge/` | 长期知识大脑，供 Q&A、研究和论文写作检索 | 可复用的 source、nucleus、band、experiment、method、model、observable、concept、project、synthesis、question、受控 research-note、证据矩阵和经过证据回链的知识增量 | 仅一次性的运行回执、调度日志、日报正文、临时草稿；重要事实必须能回到 `knowledge/sources/` 和 `raw/` locator |
| `outputs/` | 交代性输出与过程状态 | 日报、周报、审计、paper card、L3/L4 readiness/report、run receipt、scheduler state、literature-acquisition manifest、`outputs/plans/` 任务计划书和其它过程报告 | 只在这里保存长期知识正文、project/synthesis/evidence matrix 的唯一副本；输出中产生的可复用知识必须同步提炼到 `knowledge/` |
| `system/` | 治理与执行层 | `AGENTS`/规则、workflow、schema、prompt、template、memory、handoff、log、queue、脚本和测试 | 科学来源正文、日报/周报、原始材料、运行缓存 |
| `tools/` | 外部工具和服务适配层 | MCP、下载器、服务代码、工具专属配置和缓存（按各工具规则） | Wiki 长期知识、原始论文、日报和治理规则 |
| `tmp/` | 临时运行数据 | 下载 staging、OCR/图像 scratch、缓存、锁、临时工作树和可删除中间产物 | 任何唯一知识、证据、计划、报告或必须跨会话恢复的状态 |

### 输出知识回写规则

`outputs/` 是交付记录，不是第二个知识库。每次日报、周报、审计、L3/L4 报告或计划书出现可复用的事实、方法、证据矩阵行、竞争解释、开放问题或研究设计时，任务必须：

1. 在 `knowledge/` 创建或更新相应 canonical 页面；
2. 在输出中列出具体 `knowledge/...` 页面链接和来源 locator；
3. 明确区分实验直接报告、作者解释、模型结果和本任务推断；
4. 若没有可持久化的新知，写出 `verified no-op` 及原因，不把日报本身冒充知识增量。

每日学习的硬验收是 `Durable knowledge delta`；它必须指向 `knowledge/` 页面、知识矩阵/问题修订、可复核计算资产，或明确的带证据 `verified no-op`。仅写一份 `outputs/learning-daily/` 日报不能使当天学习通过。

## 计划书和支持性路径

- `outputs/plans/` 是任务计划书的 canonical 路径。旧的 `docs/plans/` 已清理；不得重新创建 `docs/plans/`，新计划不得写到 `docs/`。
- 根目录 `PLAN.md` 是用户维护的宏观方向和阶段计划，保留在根目录，不迁入 `outputs/` 或 `knowledge/`。
- `.qmd/`、`.obsidian/`、`.agents/` 是本地索引、编辑器和 skill 配置/缓存；它们不属于知识层，也不作为长期事实源。
- `script/` 是历史/兼容启动器；新脚本统一放 `system/scripts/`。`share_message/`、`testdir/` 和其它本地兼容目录不承载长期知识。
- 现有历史文件可以保留在其原路径以便追溯；本契约禁止新增漂移。临时新文件统一写入 `tmp/`，不在根目录或 `outputs/` 外另建 scratch 目录。

## 检索和晋升边界

- QMD collection `nuclear-knowledge` 只能覆盖 `knowledge/**/*.md`；不得把 `raw/`、`outputs/`、`system/`、`tools/` 或 `tmp/` 加入 collection。
- ordinary Q&A 默认从 `knowledge/` 检索；`knowledge/research-notes/` 仍须按 query workflow 的 provisional 规则过滤并回到 grounded source。
- 输出、计划、run receipt 和 scheduler state 可以引用知识页，但不能成为 Q&A 或论文写作的长期事实来源。
- 论文级主张仍必须回到 `knowledge/sources/`、`raw/` 原文、locator、适用条件和竞争解释；路径晋升不等于科学审核或 `human-reviewed`。

## 自动化执行约束

`system/scripts/wiki_boundary_check.py` 是本契约的只读机器检查，`wiki_automation_preflight.py` 默认调用它。边界失败时，文献摄入和每日学习在写入前 safe-suspend；检查只读取路径和必要元数据，不读取、修改或哈希扫描 `raw/` 内容。通过边界检查后仍须运行 Wiki lint、证据自审和相应 Git 发布门。
