---
type: learning-daily-index
graph-excluded: true
updated: 2026-09-05
---

# Daily learning records

每日独立学习任务将记录写在本目录，文件名建议为 `YYYY-MM-DD.md`；同日续跑可使用 `YYYY-MM-DD-<run>.md`。每份实质记录至少包含：

- 运行时间、时区、运行类型和当前 90 天阶段；
- 候选池与选择理由、来源指纹/重复关系/近期重叠和 checkpoint；
- source/claim/locator、证据层级、source independence、支持/反证/竞争解释；
- 新增 source↔knowledge 双向链接和 Knowledge Impact and Learning Decision；
- 开放问题、L0–L4 状态、停止或 continuation 理由；
- Git/权限结果（包括 `content-complete / final-not-pushed`），不记录 token 或宿主凭据。

没有实质变化时只写 verified no-op receipt，不制造空 commit。

日报是运行交代，不是长期知识库。每次日报产生可复用的事实、方法、证据矩阵行、竞争解释、开放问题或研究设计，必须在同一任务中写入 `knowledge/` 的 canonical 页面，并在日报中列出页面路径和 source locator；只有带证据的 `verified no-op` 才可以没有新的知识页。

自动 runner 还要求日报的 `## Durable knowledge delta` 含唯一 `knowledge-writeback` JSON 区块：`updated` 必须对应本次运行实际改变的知识页，`verified-no-op` 必须列出现有知识页、source locator 和无变化理由。区块中的页面、锚点和 locator 会在推进 day state 前逐项解析。
