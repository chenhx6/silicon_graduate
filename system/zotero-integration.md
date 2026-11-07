---
type: system-integration
graph-excluded: true
updated: 2026-11-07
---

# Zotero 轻量连接约定

## 职责

- Zotero：书目、Collection、附件关系和人工标注的主库。
- `raw/papers/`：当前准备摄入的精选 PDF。
- `knowledge/sources/`：经过核验并可被 Wiki 引用的来源页。
- [本地文献馆藏](workflows/local-literature-archive.md)：智能体内部发现原件、核对版本与
  附件，只读关联 source 与 citation key；目录登记不表示阅读或书目已导出。

## 为什么不直接操作 zotero.sqlite

运行中的数据库会被 Zotero 锁定；SQLite 内部 schema 不是本项目的稳定接口。Agent 不解除锁、不写数据库，也不以数据库备份替代 Zotero 本身。

## 当前书目入口

`raw/zotero/wiki-auto-generated.bib` 是现有source的自动导出入口，
由下面的脚本流程维护，可供用户按自己的Zotero工作方式导入或引用。
摄入时通过DOI、题名、作者年份和已有citation key核对身份；存在真实Zotero item
key时再关联，不把Zotero登记设为学习前提。

旧 `raw/zotero/wiki-inbox.bib` 入口已废弃，不重建；如本地仍有用户维护的历史
inbox/JSON或其它导出，只读核对，不覆盖、不迁移。Agent不直接操作Zotero数据库或私有附件。

## 当前状态

- 2026-07-01 曾记录 `Wiki Inbox`、旧inbox导出和一条样例记录；这些是历史配置，
  不代表当前入口或馆藏数量。
- 来源未在Zotero登记时仍可从PDF摄入；缺少Zotero身份时不编造 `zotero_item_key`
  或 `zotero_uri`。`citation_key` 可由既有 Wiki 脚本生成，不以存在 Zotero 条目为前提。

## 自动书目衔接

`system/scripts/wiki_citation_key.py export --root .` 从已有 citation key 的 source
生成 `raw/zotero/wiki-auto-generated.bib`；需要填补缺失 key 时，`sync` 会先修改
source 再导出，须属于当前获准的 source/书目维护范围。不要手改生成文件，不因
馆藏清点自动运行全库 `sync`。inbox、Zotero 身份与自动生成书目保持各自职责；
本地目录只关联这些记录，不批量创建 source，也不把导出条目当作全文可用证明。

## 来源页映射

| Zotero/Better BibTeX | Source frontmatter |
|---|---|
| item key | `zotero_item_key` |
| citation key | `citation_key` |
| select link | `zotero_uri` |
| attachment path | `library_file` |
| DOI | `doi` |

## 标注

第一版不自动同步 1260 条历史标注。后续先选一篇论文试验“Zotero 标注 → Markdown 摘录 → source 页定位”，验证不会丢页码、颜色语义和批注作者后再扩大。
