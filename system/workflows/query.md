---
type: system-workflow
graph-excluded: true
operation: query
updated: 2026-07-15
---

# QUERY：知识库查询流程

## 1. 定界

- 明确问题对应的核素、能区、能带、观测量、模型和时间范围。
- 区分用户是在问实验事实、文献观点、领域共识，还是要求我们的综合判断。

### 1.1 任务路由

普通 Wiki 问答以直接回答、必要 inline evidence links 和证据边界为目标，不默认执行完整持续学习闭环，不自动追加迁移案例、失效检验、反向检验或研究问题，也不自动创建或默认检索 provisional research reasoning。

路径规则：遵守 [`system/path-contract.md`](../path-contract.md)。问答的长期事实候选只来自 `knowledge/` 及其回链的 `raw/` 原文；`outputs/`、`system/`、`tools/` 和 `tmp/` 中的报告、计划、回执或日志不是长期事实源。若用户要求把输出中的内容用于后续问答或写作，先将可复用内容提炼到 `knowledge/` 并补齐 source/locator。

L0-L4 路由由 `autonomous-research.md` 维护。普通问答保持只读；授权摄入/综合默认进入 L2，高价值问题可进入 L3；L4 必须由用户确认数据后手动启动。不要在本文件复制等级定义。

普通 Q&A 保持 read-only，不因读取或发现旧页面格式而自动写回；可以在回答中报告潜在 migration 需求。需要写入时，必须转入用户已授权的 ingest、reflect、project、synthesis、claim-review-update 或研究写作 workflow，由该 workflow 对实际使用的旧页面做最小 on-touch migration，未触及的历史页面不批量升级。

以下情形才进入研究型路由：文献摄入；reflect；project/synthesis；用户明确要求比较、批判、迁移、研究启发或假设形成；或者问题本身必须依赖这些分析才能可靠回答。研究型路由引用 `ingest.md`、`reflect.md`、`autonomous-research.md` 和 `evidence-policy.md`。ordinary research route 仍由用户控制阅读模式；活跃 L3/L4 可按信息增益自主切换并记录理由、覆盖范围和未覆盖部分。

`knowledge/research-notes/` 位于现有 `nuclear-knowledge` collection，但 ordinary Q&A 的候选过滤必须默认排除该路径或 `type: research-note`。只有 reflect、project、synthesis、用户明确要求研究启发/假设/迁移/暂定认识，或新证据可能修正既有 note 时才主动纳入。纳入后必须显示 `reasoning_status` 和 provisional 身份，并回到 `Grounded Evidence` 所列 source/locator 支撑事实；research note 本身不是正式 evidence。

## 2. 双语术语归一化

1. 识别问题中的中文、英文、缩写、历史写法和实验口语。
2. 使用 `system/vocabulary.md` 的 canonical、aliases、query expansion，以及相关页面 frontmatter 的 `aliases` 双向扩展检索词。
3. 中英文等价词检索同一 canonical concept；原文术语仍保留在来源与回答中。
4. 泛称命中多个模型或方法时，列出候选并询问用户，或按候选分别回答；不得擅自选择一个。
5. `do_not_merge_with` 中的术语不得静默合并。尤其区分 angular distribution / angular correlation、shell model / CSM / PSM / TPSM，以及 wobbling 上位概念与 transverse/longitudinal 下位类型。
6. γ 谱学语境中的 `gate`、`gated by`、“开门”“拉门”“开窗”可扩展到 gating/coincidence gate，但必须保留能量、gate 类型和上下文限定。

若术语扩展改变了检索范围，在最终回答中简要列出使用的 canonical term 和主要扩展词。术语表只负责检索归一化，不构成科学证据。

## 3. 检索顺序
### 3.0 工具使用卫生

查询不得用无过滤递归扫描替代定界检索。禁止 `Get-ChildItem -Recurse` 扫全仓库、`tree`、`ls -R`、`rg "关键词" .`，也不得无目的扫描 `.git/`、`.qmd/`、`.obsidian/`、`tmp/`、`raw/`、`outputs/`、`share_message/`、`__pycache__/` 或 `.pytest_cache/`。默认限定 `knowledge/`、`system/`、`AGENTS.md`、`check.md`、`USER_GUIDE_DETAIL.md`；查 raw PDF 时只查目标文件名或已知候选。

### 3.1 QMD 状态与范围

QMD 已启用为本地候选检索层。project-local 索引位于被 Git 忽略的 `.qmd/`，collection 为 `nuclear-knowledge`，只索引 `knowledge/**/*.md`。从仓库根目录检查：

```powershell
$qmd = Get-Command qmd.cmd -ErrorAction SilentlyContinue
if (-not $qmd) { $qmd = Join-Path $env:APPDATA 'npm\qmd.cmd' }
& $qmd status
```

若 QMD 不可用或索引异常，降级到 `rg`、`knowledge/index.md` 和直接读取，并在回答中说明未使用 QMD。不得把未执行写成已检索。

### 3.2 检索路由

1. 已知路径或候选页面很少：直接读取文件。
2. 精确核素、作者、DOI、citation key、带名和术语：先用 `rg` 或快速 BM25。

   ```powershell
   qmd.cmd search "signature splitting wobbling" -c nuclear-knowledge --format files -n 10
   ```

3. 用户用自然语言描述机制、近义概念或竞争解释，关键词检索覆盖不足：使用语义检索。

   ```powershell
   qmd.cmd vsearch "如何区分低自旋 wobbling 与替代解释" -c nuclear-knowledge --format files -n 10
   ```

4. 高价值跨页综合且执行余量充足：可使用完整 hybrid query。

   ```powershell
   qmd.cmd query "比较低自旋 wobbling、TiP 和 IBFM 替代解释的证据边界" -c nuclear-knowledge --format files -n 10
   ```

   当前 Windows + Intel Iris Xe 环境的首次实测中，BM25 为十秒级、语义检索约两分钟、完整 query 约七分钟。完整 query 不作为简单问答默认路径；超时或收益不足时降级，不得让检索工具阻塞任务。

### 3.3 全文回读与证据追踪

搜索结果只用于建立候选集合。不得从 snippet、score、query expansion 或 reranker 排名直接生成科学结论。对候选页执行：

```powershell
qmd.cmd get "qmd://nuclear-knowledge/synthesis/example.md"
```

然后按以下顺序回读：

1. 相关核素页、带结构页、概念页、模型页和观测量页；
2. 这些页面指向的 `knowledge/sources/` 来源页；
3. 必要时回到 `raw/` 原文核验页码、图表、能级和不确定度。

若 QMD 返回 `knowledge/research-notes/`，ordinary Q&A 在全文回读前将其从候选集合排除；研究型路由使用它时，必须同时读取其 grounded sources。单一 collection 的隔离依赖这一候选过滤与 provenance 回读，不依赖排名分数。

### 3.4 索引维护

`knowledge/` 有实质修改后，QMD refresh 可按任务价值判断。普通单篇摄入不强制 embed；批量摄入、多篇完成、用户明确要求刷新，或大型 project/synthesis 依赖最新检索时运行：

```powershell
qmd.cmd update
qmd.cmd embed -c nuclear-knowledge
qmd.cmd status
```

若本轮 deferred，最终复盘写明 `QMD refresh deferred`、原因和建议补跑时机。增量 `embed` 只处理新建或变化内容。`qmd pull` 仅下载/校验 embedding、generation 和 reranking 模型；正常查询与日常知识更新不需要重复运行。禁止使用 `qmd update --pull`，因为 Git 获取、冲突处理和用户工作树保护必须由显式 Git 工作流负责。

## 4. 回答要求

- Ordinary query scope 包括 ordinary Wiki questions / exploratory synthesis / research discussion / early drafting；它不等同于三种用户摄入模式，也不自动进入严格 paper evidence gate。
- 凡被表述为 Wiki 已收录或 external source 已核验的核心结论，都应追溯到来源页或直接来源；ordinary mode 下的稳定一般专业背景可以使用，但不得伪装成 Wiki 已收录事实。
- 关键数值在已有直接来源时附单位、不确定度和 locator；若精确 locator 暂缺但仍能给出有价值回答，应降低措辞强度并说明限制。
- 术语首次出现时优先使用“中文（English, abbreviation）”；必要时说明 canonical term、用户原词和原文术语的关系。
- 显式标明实验事实、实验判据、作者解释、模型结果、跨来源综合、我们的暂时推断或工作假设。
- 相互冲突的来源并列呈现。
- 库中没有的信息明确写“当前知识库未覆盖”；这表示当前 Wiki 缺少个人化上下文或已整理证据，不自动等于不能回答。ordinary mode 仍可补充稳定的一般专业背景，但必须将其与 Wiki-grounded、human-reviewed 和 externally verified evidence 区分开，不得用模型记忆虚构论文、数据、locator、作者结论或 Wiki 已收录事实。
- 页面或 claim 未完成人工复核时，不得因此隐藏或排除与当前问题相关、可能有信息增益的内容。它仍可用于普通问答、研究分析、探索性综合、文献发现、候选证据发现和问题导航。回答应说明当前 review、source 和 locator 状态，并在内容可能影响判断时主动指出最值得用户核查的位置。涉及精确、争议或论文用途时，应针对具体 claim 回到直接来源核验；页面级 review status 本身既不自动赋予，也不自动取消论文使用资格。
- 已人工审核内容仍可在用户质疑、新证据冲突、精确核查或论文使用时重新检查。不得把 `human-reviewed` 当作永久正确、完整或已充分挖掘的保证。
- synthesis 只能帮助综合和导航，不能替代原始 source/raw。
- source/claim 引用继续以知识页和原始 locator 为准，不得只引用 vocabulary。
- Wiki 直接支持的判断使用 inline evidence link，紧跟在被支持的句子或分句后；anchor text 写明可读的页面/文献名称和已核实的 `line N`。多来源综合用校准措辞并并列最直接的 1-3 个链接；一般背景不机械加链接；重要但 Wiki 缺少直接证据的判断就在原处说明证据缺口和 provenance。普通回答不默认生成末尾重复证据区，只有用户明确要求来源汇总或 strict review 需要时才增加独立来源区；详细格式以 Skill 为准。
- 回答时必须读取目标文件并使用直接承载判断的真实行号，不得猜测或在已有精确位置时只链接文件开头。若客户端不支持 `文件.md:行号`，退化为带可读页面名称和已核实小节/claim 定位的可点击文件链接，并如实说明。不得使用 `[内容页]`、`[打开证据位置]`、`[证据页]` 等无信息 anchor，不得只给裸页面名、slug、反引号包裹的 `[[wikilink]]` 或裸 `[[wikilink]]`；名称或 alias 多候选时列出已解析路径，不得猜测。ordinary mode 不默认显示 citation key、raw PDF、review 状态或完整 locator；该规则只约束 Codex/chat 输出，不要求改写 Wiki 正文中的 Wikilink。
- 纯查询保持 read-only，不运行 EOL 清理脚本。查询一旦转入持久化或文件修改，必须在第一次写入前执行 `check.md` 的 write-entry preflight；后续 commit/push 继续执行对应阶段，不在本 workflow 复制脚本实现。
- 证据不完整时，应校准措辞、说明限制并指出值得补查的方向，而不是无必要地拒绝回答。
- 不得把综合或推断伪装成某一来源直接报告的结论，也不得把“当前尚无直接证据”自动解释为“该判断一定错误”。
- 不得虚构 citation、DOI、页码、图号、表号、locator、原文或数据。

## 5. 持久化判断

只有满足下列任一条件才写入 `outputs/` 或 `knowledge/`：

- 回答解决了反复出现的科研问题；可复用结论写入相应 `knowledge/` 页面，`outputs/` 仅记录本次报告或审计；
- 建立了新的跨来源证据矩阵；
- 形成可用于论文、报告或项目决策的内容；
- 明确暴露了重要证据缺口。

普通问答不机械归档。

普通问答产生的联想、迁移候选或研究问题默认停留在当次输出。只有进入授权研究型任务、通过价值门并遵守暂定推理与晋升边界时，才考虑持久化；即使被检索到，provisional reasoning 也不得作为 source-grounded evidence 使用。

涉及论文或投稿核查、正式引用、直接来源或原文引文、精确 locator、关键科学 claim 确认，或用户明确要求执行 paper evidence review 时，额外遵循 `system/paper-evidence-gate.md`。普通争议讨论本身不自动进入 strict mode。未通过 paper evidence gate 不禁止讨论、谨慎综合或初稿生成；它只表示正式提交前仍需补查直接来源、精确 locator、适用条件、竞争解释和引用风险。当前 Wiki 没有覆盖到的文献不能被推断为“不存在”。

## 6. 收尾

持久化后更新 index、log 和 Active handoff；若产生新问题，追加到 `knowledge/questions.md`。知识层有实质变化时按 3.4 判断是否刷新 QMD；普通单篇摄入可 deferred。
