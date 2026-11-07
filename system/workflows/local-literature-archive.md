---
type: system-workflow
graph-excluded: true
operation: local-literature-archive
updated: 2026-11-07
---

# 智能体本地文献馆藏

内部入口为 [local-literature-archive skill](../../.agents/skills/local-literature-archive/SKILL.md)。
智能体在找文献、使用原件、查证具体主张或准备获取时先核对本地馆藏，自行处理结构化
候选。普通交流无需清点。目录服务于原件发现；科学依据仍回到实际原文及
`knowledge/sources/` 的 locator，不以目录或运行回执代替证据。

## 内部接口与存储

执行入口为 `system/scripts/local_literature_archive.py`；命令均输出 JSON，
供智能体内部调用。参数包括 `--root`、`--query`、`--doi`、`--arxiv`、
`--scan-root`（可重复）和 `--limit`；`--help` 可查看实际接口。

| 命令 | 用途 |
| --- | --- |
| `inventory` | 清点指定本地范围，关联原件、source 与 manifest |
| `refresh` | 增量刷新变化项，报告缺件、解析失败和范围 |
| `find` | 按身份、题名作者或主题返回聚合候选，包含未学习馆藏 |
| `check-local` | 下载或使用前核对具体文献的本地身份与可用性 |
| `stats` | 分别统计作品、原件副本、版本、附件、source 关联与异常 |
| `index-text --path`（可选） | 只为指定原件建立全文文本索引 |

默认提取本地元数据与 PDF 前几页。无全文索引不妨碍元数据发现；扫描件、提取失败
或只提取首页要保留覆盖边界。不自动 OCR，不建全库 embedding，也不联网补齐身份。
身份或附件关系经原件核实后，可在本地 `.agents/local-literature/overrides.json`
写入路径级消歧。字段 `basis` 记录原件、页码和确认理由，缺少依据的条目被忽略并报告。
例如下面是结构示例，不代表已核实任何真实文献：

```json
{
  "artifacts": {
    "raw/papers/example-supplement.pdf": {
      "role": "supplement",
      "parent_work_key": "doi:10.1234/example",
      "basis": "原件p.1明确给出对应主文题名和DOI"
    }
  }
}
```

可用字段还包括 `work_key`、`doi`、`arxiv`、`title` 和 `edition`
（`published`、`accepted`、`manuscript`、`preprint` 或 `unknown`）。
勘误用 `role: erratum` 和 `parent_work_key` 建立纠错关联，同时保留其独立source/DOI。
只有确认同一作品才使用共同 `work_key`；不能用模糊相似度覆盖身份冲突。

- `.agents/local-literature/catalog.json` 与 `index.sqlite` 是本地、Git 忽略、可重建的
  目录与查询缓存；不得提交、发布或成为身份消歧的唯一凭据。重建须保留可重放的
  override 依据与稳定身份映射，不静默丢弃人工消歧。忽略规则由主实现集成维护。
- `tmp/local-literature/` 可存提取 scratch；不保存唯一原件或学习记录。
- 默认范围是 `raw/papers/`、`raw/books/`、`raw/theses/`、`raw/reports/`、
  `raw/notes/`，以及既有 source/manifest 明确指向且位于允许范围的原件。
  `raw/writing/` 的手稿、模板、图片默认不作为外部文献入库；明确指定的文献可另行纳入。
- 排除 personal、实验 data、凭据、依赖、临时目录和仓库外链接；source 指针不能
  绕过排除项或符号链接边界。记录实际扫描根、排除项、时间和失败项。
- 目录写入用锁和原子替换，查询只读完整快照；锁冲突/不完整扫描明确报告。
  大小与 mtime 只用于增量筛选；使用前仍核验原件哈希，不能把旧 manifest 哈希
  标作本轮已重算。文件变化保留旧身份，不自动改 source 哈希。

## 身份、底本与学习

实现可调整字段名和高级关系表示，但须保留这些语义：

| 对象 | 最小语义 |
| --- | --- |
| 文献作品 | 稳定本地身份、题名/别名、作者年份、DOI/arXiv、匹配依据及身份待核边界 |
| 原件载体 | 路径、角色/版本、大小、哈希与验证状态、可读性和提取覆盖范围 |
| 版本与附件关系 | 同一作品的出版版/arXiv、补充材料、独立勘误、翻译及相同字节副本 |
| 学习关联 | 已有 source 路径、citation_key、reading_depth 和 Covered scope 的只读指针 |

只有已验证属于文献自身的 DOI 才能作为 DOI 身份匹配依据；PDF 中任意 DOI 命中
特别是参考文献 DOI 不构成身份。题名/作者/年份可产生候选，不能仅凭题名相似合并。
同一实验的不同论文、书籍不同卷册分别保留作品身份；相同字节的多个路径只关联副本，
不删除或移动文件。确认身份后出版版与 arXiv 聚为同一作品，稳定身份不随路径、
题名补齐或 DOI 补齐变化。

出版版是首选底本，实际可读原件单独标明。已知出版但本地仅有预印本时，可以继续
有界阅读并注明实际版本；关键数据/引用定位不冒充出版版。出版版到位只更新首选读取
目标，不自动重写既有 source 的版本、哈希或页码，也不把 arXiv 特有结果归给出版版。
补充材料与勘误随主条目可发现；勘误保留独立 DOI/书目身份，通过 `corrects` 等关系
关联，按适用部分修正，保留修正前后差异。归属不明时只记录待核关系。

登记、下载或索引全文不表示阅读，不批量建 source、生成 citation key 或提高
reading_depth。学习状态以既有 source 为准；`review_status`、`needs_review` 和
人工审核历史不参与排序或知识使用判断。统计维度允许交叉，文件数不当作文献数，
source 关联数不当作已读数。

## 查询与获取路由

1. 已知文件/source 先直接核验；其余按 DOI/arXiv、题名作者或主题查询。候选保留
   匹配依据、实际路径、底本与实际版本、可用性、附件/勘误和已有阅读范围。
2. 区分可用原件、身份待核候选、仅元数据、缺件、不可读与索引不完整。
   实现的状态名可不同，但不能把摘要/首页或旧下载成功记录当成已验证全文。
3. 索引不存在、过期或范围遗漏时做有界刷新或路径/文件名回退；脚本未就绪时
   如实报告并直接检查相关 source/manifest。无命中须带范围，不宣称全库无原件。
   普通问答只允许本地可重建缓存刷新，不因此写 raw、source 或交接。
4. 外部发现候选后、下载前再次核对身份。403 或旧访问失败不能遮蔽现存全文；
   同一任务仅在出现新身份线索、本地更新或范围遗漏时重查，避免重复空扫描。
5. 本地不足时转 [literature-access](literature-access.md)，保持既有获取器接口和权限，
   不修改 get-paper。取得材料后按 [research-archive](research-archive.md) 留档，
   校验原件与 manifest，再刷新目录。附件完整性另核，主文件存在不代表 SI 齐备。
6. 学习/写入转既有 ingest 流程；书目需求转 [Zotero 约定](../zotero-integration.md)。
   不手改自动 BibTeX，不写 inbox，不以目录登记触发全库 `sync`。

最终回答按研究问题组织，仅展示有用的证据链接与版本/访问边界，不向用户要求
馆藏命令、固定查询格式或界面操作。QMD 继续只索引 `knowledge/**/*.md`。

## 首次迁移的 source 修复依据

批准设计和 [2026-11-07 路径审计回执](../../outputs/literature-acquisition/20261107-local-literature-path-audit.json)
记录了全部 534 个 source 中的 55 个 `raw_file` 未命中项：1 项在 raw 已有同哈希原件，
53 项在明确来源的暂存区或历史输出有同哈希候选，共 54 项可恢复；另 1 项是历史手稿
版本缺口。候选含评价数据、软件和校准文件，不全是论文。许多旧页面的 raw 路径
原本就是待填充归档槽，所以路径未命中不能写成“原件曾丢失”。这些是当日有界盘点，
不是全库附件完整性审计。实施结果见
[恢复回执](../../outputs/literature-acquisition/20261107-local-literature-recovery-receipt.json)、
[定向归档检查](../../outputs/literature-acquisition/20261107-local-literature-archive-check.json)：
54项已完成原件恢复/指针对齐，并保留暂存文件；逐source及恢复manifest的检查通过。

修复的目的在于让 source 指向可验证、持久的原件。仅在另行授权的迁移范围内，
逐文件重算候选哈希：raw 已有同哈希则复用；否则复制到不存在的目标，保留旧文件，
遇不同哈希目标保留冲突/另立版本，不覆盖。manifest 保留来源与历史获取时间，
未知时间明确记未知，本次恢复时间单列 `recovered_at`；不伪造重新下载。
随后最小更新 source 路径、归档状态和 provenance，保留阅读范围、结论与 citation key，
对对应 source/manifest 逐项运行归档门，最后对账 54 项实际结果及残余缺口。
日常查询只报告异常，不自动执行该批恢复。

独立保留 `chen-2026-pdm-probability-density-mapping.md` 所指历史 15 页手稿
`raw/writing/pado/20260722.pdf` 的版本缺口，旧 SHA-256 为
`f19b52b872432f6d615dae9350eef42d12cff27cfb621a041f09720699f74421`。
当日该目录 21 个 PDF 未命中只说明已查范围；其他可用版本可支持其适用范围内的工作，
不得覆盖旧哈希、借用旧页码或标成已找回，也不公开检索私人未发表版本。
用户随后指定 `raw/writing/pado/20260929_submitted_v1/nst_sample.pdf`；
题名、四位作者、PDM方法和八条基准跃迁核对确认它属于同一文献的11页修订稿。
source现指向该可用原件，旧15页稿的哈希与历史阅读定位仍保留，未冒充字节一致。
新稿仅完成有界版本核对，未沿用旧稿的全文阅读完成状态。详见
[版本对账](../../outputs/literature-acquisition/20261107-pdm-version-reconciliation.json)。
该source的LaTeX题名YAML转义已修复；标准YAML解析和现有归档检查通过。

## 集成检查

主实现以离线样本核查四条路径：精确 DOI 命中、外网 403 但本地有原件、主题发现
未学习材料、出版版与勘误同时可发现。另核参考文献 DOI 不误合并、仅元数据不报全文、
索引不完整与缺件分开、预印本实际版本明确、原件字节与学习记录不变。
脚本行为、忽略规则和历史恢复的实际完成情况由各自执行回执报告；文档检查不能
替代这些检查，也不以本页新增字段要求扩大主实现。
