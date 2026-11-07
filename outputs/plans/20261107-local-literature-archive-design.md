# local-literature-archive 设计与实施计划

日期：2026-11-07。状态：规划完成，尚未实现。

## 目标与已确认规格

用户要求新建本地文献 skill，参考图书馆目录管理，解决已有原件不可发现、重复下载、外部访问失败遮蔽本地全文的问题，并与 source 学习记录和自动 BibTeX 衔接。

- 同一论文设置一个主文献条目；arXiv 与出版版归于该条目，出版版为底本。
- arXiv 原件保留；补充材料、勘误保留并关联主文献，不删除。
- 出版版与正式勘误共同形成当前使用依据；不把修正前后的冲突抹去，不把 arXiv 特有结果静默归于出版版。
- 目录登记不代表阅读，不自动批量建立 source，不改变阅读深度。
- 默认在找文献、使用原件和准备获取时执行本地预查；按主题发现可以包含未学习材料。
- 保护原件路径、已有修改、私有材料；本项目不修改 get-paper 安装或代码。

## 现状与数量口径

2026-11-07 的有界盘点在 raw 下排除名为 data、personal、.git、node_modules、__pycache__、.venv 的目录，统计 PDF/EPUB/DJVU 共 678 个文件，其中 papers 518、books 39、theses 60、notes 10、reports 1、writing 50。文件数不是独立文献数，也不是完整馆藏结论。

knowledge/sources 顶层有 534 个 Markdown 文件。标准 YAML 读取成功 533 个；1 个解析失败，未修改该页。成功读取者中，508 个 raw_file 指向非 JSON 路径，25 个指向 JSON 清单。source 类型还包括软件、评价数据、元数据和投稿指南，故不能与文献格式文件数相减推算未读论文。

当前没有观察到两个可解析页面使用完全相同的 raw_file 字符串；这不能证明原件内容或文献身份无重复。54 个 raw_file 按记录字符串执行存在性检查未找到，尚未完成路径归一、迁移或替代件查找，不能据此宣称54份原件丢失。

当前书目工具 system/scripts/wiki_citation_key.py 从带 citation_key 的 source 导出 raw/zotero/wiki-auto-generated.bib。它不清点未摄入原件，也不证明导出条目存在可用全文。

## 图书馆式数据结构

采用“文献主条目—载体与附件—学习记录”三层关联；查询默认呈现一篇论文一条结果。

| 对象 | 标识和字段 | 职责 |
| --- | --- | --- |
| 文献主条目 | 稳定本地 accession_id、题名/别名、作者、年份、类型、DOI/arXiv、学科词、核素词、身份依据 | 表示一项文献作品；标识不因补齐 DOI 或题名而变化 |
| 原件/载体 | artifact_id、相对路径、角色、版本标签、格式、大小、mtime_ns、SHA-256、可读性、页数、发现/验证时间、元数据出处 | 表示实际文件；允许多个路径对应相同字节 |
| 附加关系 | supplement_of、corrects、translation_of、published_as、duplicate_bytes | 保留附件、纠错和版本关系；勘误自己的 DOI 与书目身份独立保存 |
| 学习关联 | source 路径、citation_key、reading_depth、Covered scope 原位置 | 读取既有记录，不从目录登记推断阅读完成 |

册号采用稳定的本地编号，不将分类号或路径编码进主键。主题分类采用多标签与别名，避免把跨学科论文锁入单一类别。图书卷册分别管理；同一实验的不同论文保持独立作品关联，不因题名接近而合并。

主条目分别保存 canonical_edition（应采用的底本）和 available_local_artifact（实际可读原件）。已知出版但本地只有 arXiv 时，明确报告“出版版为底本，本地暂存预印本”；本次任务可依据预印本继续有界阅读，涉及关键数据/引用定位须说明实际使用版本，不强制停止研究。

出版版到位后更改首选读取目标，不自动重写已有 source 的版本、页码和哈希；形成需要核对的版本差异记录。纠错按适用部分覆盖原结论，不把整篇原文标作无效。无法确认纠错归属时保留待核关系。

## 目录和索引位置

- 新建 `.agents/skills/local-literature-archive/SKILL.md`：触发场景、查询行为、底本规则、结果格式、衔接边界。
- 新建 `.agents/skills/local-literature-archive/AGENTS.md`：包内维护说明。
- 新建 `system/workflows/local-literature-archive.md`：规范和数据 schema。
- 新建 `system/scripts/local_literature_archive.py`：清点、归一、匹配、增量索引、查询。
- 新建 `system/tests/test_local_literature_archive.py`：离线人工构造样本，不依赖全库原件。
- 新建 `.agents/local-literature/` 下的本地目录 JSON 和 SQLite/FTS 查询库；目录不跟踪，不发布。首次实现显式加入精确忽略规则。
- `tmp/local-literature/` 保存提取 scratch；可恢复目录仅存路径、身份、关系和人工消歧，不依赖 scratch 作为唯一副本。
- `outputs/literature-acquisition/` 保存按次盘点/核对回执；不作为论文事实或科学知识来源。

JSON 保存可恢复的登记、身份与消歧关系；SQLite/FTS 从登记和原件重建。学习记录仍以 source 为准，不在目录创建第二套阅读状态。所有目录均不改变 QMD 的 knowledge-only 范围。

第一版扫描 papers/books/theses/reports/notes 与已有 source/manifest 的相关路径。writing 下 manuscript、template、figure 等默认不纳入外部文献主目录；用户指定的文献文件可加入。排除 personal、实验 data、凭据、工具依赖、临时目录和仓库外链接。源页面指针越界时只报告，不自动跟随。扫描根可配置且写入每次统计。

## 查询与增量工作流

以下是计划接口，当前尚不可执行：

```text
python3 system/scripts/local_literature_archive.py inventory --root .
python3 system/scripts/local_literature_archive.py refresh --root .
python3 system/scripts/local_literature_archive.py find --root . --query "题名、DOI或主题" --json
python3 system/scripts/local_literature_archive.py check-local --root . --doi "10.xxxx/example" --json
python3 system/scripts/local_literature_archive.py stats --root . --json
```

1. inventory 首次清点配置范围，登记文件、manifest 和 source 关联。复用已有哈希作为已登记值；不把未重算者标成已验证。
2. refresh 用路径、大小、mtime_ns 筛选变化项，仅重提取变化文件。mtime/大小是性能提示，不能替代使用前的原件哈希验证；文件变化时保留旧登记，标记待核，不自动改写 source 哈希。
3. 提取优先 PDF 元数据、首页与题名信息。全文 FTS 为可重建本地索引，按需要处理候选；第一版不做全库 OCR 或 embedding。
4. DOI/arXiv 精确身份优先；标准化题名加作者年份产生匹配候选。正文参考文献里的 DOI 不直接认作文件身份。题名相似不自动合并，正文命中不等于题名命中。
5. check-local 返回 found-usable、candidate-needs-identification、metadata-only、missing、unreadable 或 index-incomplete，并附检索范围。索引缺失/过期时执行有界刷新或文件名回退，不能把无命中说成全库不存在。
6. 外部检索可发现新论文；下载前再次匹配返回的 DOI/题名。同一任务内失败后只在有新线索、范围遗漏或本地更新时重查，避免重复空扫描。
7. 并发读允许；写目录采用锁与原子替换，查询读上次完整快照。锁冲突给出明确状态，不覆盖半成品。
8. 实际阅读前核验选中原件可读性和归档身份，显示底本/实际版本、附件/勘误、source 与阅读范围。

stats 分别报告独立文献、底本可用、仅预印本、附件、原件副本、已有关联 source、身份待核、路径异常和扫描范围。各统计维度允许交叉，不把总文件数称作文献数或阅读完成率。

## 与既有入口衔接

在 system/workflows/query.md、literature-access.md、research-archive.md 增加简短本地预查路由；在 AGENTS.md、check.md 及用户指南登记新入口。既有其他修改先比对，不替换整段用户内容。skill 清单按实际目录格式增加条目。

不修改 get-paper 的实现、安装、下载边界或测试。通过上游 Wiki 路由先查本地，再调用现有获取器。

原件获取完成后遵循既有归档规则并刷新目录。学习完成后关联既有 source；需要生成书目时调用现有 wiki_citation_key.py export/sync 的合适动作，不手改生成文件，不因清点而批量生成 citation_key。

system/zotero-integration.md 当前仍含旧 wiki-inbox 和只读约束，与现行自动书目流程不一致；实施时仅核对并修正这部分入口说明，保留用户 Zotero 私有数据边界。

## 分步实施与验收

1. **身份与底本规则**：实现登记 schema、稳定主键和匹配函数。离线样本验证出版版/arXiv 同一条目、出版版为首选、两个同名不同作者论文保持分离、勘误独立 DOI 关联原文。测试失败后再实现相应行为。
2. **本地清点与安全范围**：实现 inventory/refresh。临时样本目录验证原件字节不变、排除私有目录和仓库外链接、文件移失显示异常、坏 PDF 与坏 YAML 不阻断其他文件、重复执行无新增重复条目。
3. **检索与可用性**：实现 find/check-local/stats。样本验证参考文献 DOI 不误匹配、仅摘要不报全文、索引空缺与真实缺件分开、出版版缺失时明确报告实际预印本、补充/纠错始终随主条目可发现。
4. **学习与书目衔接**：只读关联 source/manifest 与 citation_key。样本验证一个 manifest 多原件、source 指向缺失路径但候选副本存在、已有学习范围不被目录登记升级、不覆盖既有 BibTeX。相同字节多路径不删除任何路径。
5. **skill 与路由**：编写轻量 skill 与规范，加入查询工作流路由。用“找某 DOI”“外网403但本地已有”“主题查未学习原件”“同时有出版版与勘误”四个场景人工检查指令是否可执行、返回是否带原件路径和实际版本。
6. **真实库有界试运行**：先在有限目录运行，再经范围确认清点默认目录。报告实际范围、耗时、身份待核与旧路径问题，不自动改修 source 或原件。通过离线测试、任务差异检查和仓库边界检查后交付。

计划验收命令（实现后运行）：

```bash
python3 -m unittest discover -s system/tests -p 'test_local_literature_archive.py'
python3 system/scripts/wiki_boundary_check.py --root .
git diff --check
```

## 本轮交付边界

本轮只创建此规划文件，未创建可运行 skill/索引，未修改原件、get-paper 或其他会话文件。本计划记录的是软件目录设计与执行状态，没有新增科学结论；无需为本次盘点创建科学 source 或把规划复制进 knowledge。实际实施中若生成可复用科学认识，仍按既有规则回写 knowledge。
