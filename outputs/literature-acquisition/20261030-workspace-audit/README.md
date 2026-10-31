---
type: output
graph-excluded: true
created: 2026-10-30
updated: 2026-10-30
---

# 2026-10-30 工作区整理审计

本目录保存工作区整理的只读基线，不保存新的科学事实，也不改变已有原件路径。

## 文件

- `audit-summary.json`：审计策略、文件数、总字节数和引用扫描分类。
- `raw-papers-manifest.tsv`：`raw/papers/` 下每个文件的相对路径、大小、SHA-256 和扩展名。
- `raw-duplicate-hashes.tsv`：相同 SHA-256 的重复字节候选；重复不等于独立实验，也不自动触发删除。
- `outputs-manifest.tsv`：`outputs/` 下每个文件的相对路径、大小、输出根和扩展名。
- `knowledge-artifact-references.tsv`：知识页中检测到的 raw/output 路径形状引用。
- `source-raw-reconciliation.tsv`：`knowledge/sources/` 的 `raw_file` 与 raw manifest 对账；区分哈希匹配、路径缺失、未声明哈希和未设置 raw slot。
- `outputs-cleanup-candidates.tsv`：728个只读候选（45个 `.pyc`、677个零字节过程文件、6个名称含 `copy` 的人工复核候选）；候选不等于可删除对象。

## 保护边界

本轮没有改名、移动、复制、删除或覆盖 `raw/papers/` 文件，也没有修改
`raw/zotero/wiki-inbox.bib`、`PLAN.md`、runner live state 或继承的 dirty 文件。
任何后续整理都必须先核对路径、哈希、来源页 `raw_file`/`raw_sha256` 和相对链接，
并使用可回滚的新增 manifest 或逻辑事件。

`knowledge-artifact-references.tsv` 是保守的路径形状扫描：含省略号、长 inline
示例、含空格的自然语言路径和相对路径会被标为 `unresolved-placeholder` 或
`needs-manual-review`。这些状态不是已经确认的断链，不能据此批量修复或删除文件。

## 下一步

先人工复核 9 组重复 SHA-256 的对象身份和 source lineage，再决定是否只为新接收
材料建立 `raw/papers/gpt/_incoming/<run-id>/` 到 archive 的新增副本。既有原件保持
原路径；manifest 版本采用追加方式，回滚通过状态事件完成。

独立 YAML/frontmatter parser 的 source 对账结果为：393 个声明路径和 SHA-256
匹配，57 个声明路径在 raw manifest 中未找到，10 个页面有路径但未声明
`raw_sha256`，6 个路径存在但 hash 无法由当前 manifest 验证，16 个页面没有
`raw_file`；另有1个 source 页存在 frontmatter 解析错误。`source-raw-reconciliation.tsv`
是这一版本的准确回链清单。这些数字是元数据治理结果，不等于论文缺失或实验
独立性判断；含 staging、历史路径和未归档的真实来源仍需逐项复核。

输出中的 `failed`、`reopened`、`history-before-repair`、`verification-*` 和其它
版本化文件默认属于 provenance，不能按文件名或“final”字样清理。零字节 stderr/stdout
也只能在确认运行器、事件日志和下游引用后标记为可回收；本轮不删除、不移动。
