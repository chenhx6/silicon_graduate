# 学位论文批次 10 小时自主研究计划

**目标:** 在一个明确的 10 小时研究窗口内，先逐篇读取本批次的学位论文和相关 PDF，再围绕证据问题执行 L3/L4 研究，形成可回链的知识增量和批次研究报告。研究可以部分完成；完成判据是问题和证据状态可追溯，而不是读完预定论文数量。

**执行链:** 发现问题 → 读取学位论文和原始 PDF 证据 → 自主 L3/L4 研究 → 形成知识增量 → 提交批次研究报告。

**本轮编辑边界:** 本次只改本计划文件。执行本计划时，允许在任务范围内更新对应 source、核素、能带、实验、方法、概念、模型、project/synthesis 页面和新的批次报告；本次不修改已有批次报告、`system` workflow、`raw` 文件或受保护 BibTeX。

**依据:** `AGENTS.md`、`README.md`、`knowledge/index.md`、`system/workflows/ingest.md`、`system/workflows/reflect.md`、`system/workflows/autonomous-research.md`、`system/paper-evidence-gate.md` 和 `outputs/degree-dissertation-ingest-20260905.md`。

## 持续执行协议（2026-09-12 起）

本任务书由 [2026-09-11 持续研究、温故知新与发布计划](2026-09-11-continue-research.md) 继续驱动。研究由 Codex 完成 source、claim、L3/L4 和批次 self-audit；不主动要求用户审核 source、P0/P1 或研究报告。用户审核只在后续问答需要裁决具体表述，或论文写作需要将具体 claim 纳入 paper evidence gate 时触发。

研究可联网查找原始论文、后续论文、勘误和补充材料。`135Nd` 等能带冲突按正常科研证据演化处理：逐篇比较早期指认、后发修订、能级/跃迁/宇称和作者解释；若后续来源尚未解决，则保留准确的 source conflict 边界。

12 小时是首个软检查点，不是硬上限或产出配额。研究在仍有实质信息增益时继续；到检查点时先完成当前原文、表格或计算单元，再根据证据收益决定继续、暂停或收尾。若有余量，进入温故知新槽，优先复核可能被新论文改变、存在争议或长期未复核的旧知识；不为满足时长机械重读。

科学 `partial`/`stopped` 状态在证据边界、停止原因和下一路线记录完整时允许收尾和发布。来源身份/哈希、raw/权限/凭据、危险文件重叠、无法追溯 locator、检查失败或 Git/远端异常等技术 hard P0 才阻止 final/push。完成 self-audit 后，当前 WIP 应按显式文件范围 amend 为 final，运行发布门，并使用精确非 force refspec push；失败时保留本地 final 并记录 `final-not-pushed`。

## 固定边界

1. 覆盖全量候选 PDF。执行开始时为每个文件建立路径、题名/作者/论文类型、页数、文件大小、SHA-256、可读性、重复关系和 source 映射；不能用文件名或摘要代替实际阅读状态。
2. **学位论文必须逐篇读取。** 至少打开并阅读每篇论文的题名页、摘要、目录、引言/研究动机、方法或实验设计、结果与讨论、结论，以及与问题池相关的章节、图、表和附录。页面图像用于核对能级、组态、跃迁、寿命、参数和图表；文本提取/OCR 只作检索辅助，不能替代页面核对。完整阅读和局部阅读分别记录覆盖范围，未读章节必须写明。
3. 每篇论文按 `deep-read`、`read`、`skimmed`、`source-only`、`duplicate` 或 `needs-human-review` 记录；`skimmed` 只表示真实的有限覆盖，不能伪装成完整阅读。关键来源应达到 `deep-read` 或有明确的局部严格核查范围。
4. 重要事实、数值和引文回链到 `knowledge/sources/` 的原文 locator（页码、图表、公式、能级位置或章节）；实验直接报告、作者解释、模型计算和本任务推断分开记录。
5. 同一实验的期刊论文、学位论文、综述和重复 PDF 显式记录依赖谱系，不重复计为独立实验。raw PDF、OCR 图片、`raw/zotero/wiki-inbox.bib` 和其它受保护用户文件只读，不覆盖、不重命名、不改哈希。
6. 执行过程中不提升 `confidence`，不把 Codex 自审写成 `human-reviewed`。原文歧义、图表不可读、元数据或 locator 缺失时保留 `needs_review: true`；该标记是证据边界，不是本批次的收尾任务。

## 输入与学位论文读取产物

上一批报告 `outputs/degree-dissertation-ingest-20260905.md` 作为初始来源和问题池入口。其来源谱系包括 15 篇学位论文（含丁兵论文和 Alwaleedi 复读记录）以及不计入学位论文数量的 `103Pd` 附加实验报告；manifest 中的原始输入目录为 `raw/papers/degree dissertation/`。执行时仍须以 raw 目录和 manifest 的实际文件为准，逐一打开 PDF 并登记读取状态。已知的论文主题覆盖 `130,131Ba`、`108,112Ru`、`127–131Pr`、`135Pr/187Au`、`170Re/176Ir`、裂变碎片、`100Sn/100In`、`237Pu`、`178Hf`、NEEC 和 `6Li(p,γ)7Be` 等。

每篇学位论文的读取记录至少包含：

- 唯一元数据、raw 相对路径和 SHA-256；
- 实际读取章节、图表、公式和页码范围，以及 `Covered scope` / `Not covered`；
- 研究问题、方法/实验设计逻辑、关键证据链、作者解释、模型结果和本任务推断；
- 与现有 source、核素、能带、实验、方法、概念、模型或 project 的映射；
- 与期刊论文、综述或共享实验的依赖关系；
- 竞争解释、局限、证据缺口、阅读深度、研究状态和下一路线。

学位论文读取与问题研究同步进行：先完成全量 PDF 的最低真实覆盖，再把剩余时间投向能改变 Wiki 判断的章节和图表。只读摘要、只提取文本或只引用已有批次报告，都不算完成该论文的读取。

### 学位论文读取队列

按信息增益动态排序，但不得跳过对低优先级文件的最低真实覆盖。第一轮优先读取与 A≈130、集体运动和争议判据直接相关的学位论文：

- 王守宇：`126Cs` 高自旋态与 A≈130 手征双重带；
- 王海霞：`173W` 与 `128I` 高自旋态；
- 刘晨：`78Br` 手征与反射对称性破缺；
- 吕冰峰：`133Nd/135Nd` 手征；
- 王志刚：`104Ag` 与 `91,92Zr` 高自旋态；
- 李仕成：`184,186Au` 高自旋形变双奇核；
- 王思成：`195Au/195Pt` 高自旋能级结构；
- 郑勇：`145Tb/157Yb` 高自旋态；
- 刘渊：`188Pt` 形状共存；
- 王建国：`103,104Nb/140Pm` 高自旋态。

第二轮读取可迁移的实验和装置方法论文：周厚兵（`101Pd` 在束 γ 谱学与 RDT）、吴鸿毅和《基于数字化的通用获取系统及波形分析算法》、硕士论文《多普勒修正》、岳珂（HIRFL-CSR 外靶 CsI(Tl)）、周旭（磁刚度识别等时性质谱术测量质量）、闫铎（CSR 外靶库仑激发），以及高丙水、黄忠魁、孟令杰关于 CSRm 原子碰撞/储存环的方法论文。

第三轮覆盖理论、反应和跨质量区论文：刘艳鑫（投影壳模型）、刘红娜（`12C` 中子-质子关联与三体力）、孙亚洲（`16C` 单质子敲出）、穆林博士/硕士，以及方永得、张文强、李广顺、李明亮、柳敏良、滑伟、贺创业、郭松、郑宽宽、王凯龙、王世陶、宋立涛。对题名或对象暂不明确的文件，先打开首页和目录确认，再决定深读、source-only 或停止原因；“未建立实体页”不等于“未读取”。

## 统一问题登记与初始问题池

每个唯一问题使用同一条登记记录，字段固定为：

`issue_id`、`priority`（P0/P1）、`source_and_locator`、`core_claim`、`conflict_or_gap`、`competing_explanations`、`l3_l4_route`、`research_status`、`stage_conclusion`、`knowledge_increment`、`remaining_uncertainty`、`next_autonomous_route`。

`source_and_locator` 必须能回到学位论文或相关 PDF 的具体页、图、表、公式或能级位置；`knowledge_increment` 明确写成新知识、纠正知识、总结知识或边界/失败知识之一。登记表可放在批次研究报告中，source 页保留同一 `issue_id` 和精简回链，避免两套编号漂移。

`issue_id` 在本批次内保持稳定（建议格式 `DD-20260910-###`）；优先级或研究状态改变时不重编号。一个 issue 可以引用多个相互独立的 source，但同一 source lineage 的重复 claim 只计一次；L3/L4 研究单元另用 `unit_id`，不把同一单元覆盖的多个 issue 重复计数。

上一批报告当前列出 10 组 P0 和 5 组 P1，执行开始时先按“同一 source lineage + 同一核心 claim/locator + 同一冲突”去重，再统计初始唯一数：

| 初始组 ID | 优先级 | 来源与待研究主张 |
|---|---|---|
| `QY19` | P0 | 强赟华：`130Ba` t-band、`131Ba` 一负两正 MχD、E1/八极关联的带号、组态和措辞。 |
| `CX07` | P0 | 车兴来：`Ru/Ba` 二声子 γ、二准中子、回弯和模型形变参数。 |
| `SM98` | P0 | Smith：`130Pr` SD/ED、TRS 组态和 ED 形变随中子数变化趋势。 |
| `SE21` | P0 | Sensharma：wobbling links、连续声子间距、`187Au` 横/纵向分类和 `135Pr` chiral-wobbler 候选。 |
| `WHL06` | P0 | 王华磊：`170Re` 组态/signature inversion 与 `176Ir` 新能级、长寿命 isomer。 |
| `HK10` | P0 | Hinke：`100Sn` 半衰期、endpoint、B(GT)、`100In` 五条 γ 线和 6+ isomer search。 |
| `LB16` | P0 | Lubos：独立 RIKEN `100Sn` B(GT)/Q-value、50 keV link、`93Ag` proton emitter 和 `90Rh` isomer。 |
| `TM08` | P0 | Morgan：`237Pu` 两个 fission-isomer、149 条 γ 线、54.0(3) keV placement 和四个 Nilsson labels。 |
| `HB05` | P0 | Hayes：两个 Coulomb-excitation 实验、K-mixing trend、hindrance 及 OCR/视觉 locator 边界。 |
| `DP74` | P0 | Dietrich：`103Pd` level count、tentative assignments 与 784 keV `11/2−`、`25±2 ns`。 |
| `RG11` | P1 | Régis：CFD time-walk、MSCD/PRD、benchmark lifetimes、`176W` IBA 和 systematics。 |
| `WE15` | P1 | Wang Enhong：21 核素范围、`147Ce/148Ce/158Sm` 候选解释和裂变数据独立性。 |
| `AP06` | P1 | Pálffy：NEEC relativistic formalism、截面数量级、RR interference 和角分布适用条件。 |
| `CS14` | P1 | 陈思泽：相对归一化、195 keV resonance/`7Be` `3/2+` 候选及独立验证路线。 |
| `SHARED-THESIS` | P1 | 所有学位论文共享的 citation key、source lineage、raw 映射和论文级 locator 缺口。 |

这些组对应上一批报告中的现有 claim ID：`QY19-3/QY19-5/QY19-6`、`CX07-4/CX07-5/CX07-6/CX07-7`、`SM98-3/SM98-6/SM98-7`、`SE21-1/SE21-2/SE21-3/SE21-5/SE21-6/SE21-7`、`WHL06-3/WHL06-5/WHL06-6`、`HK10-2/HK10-4/HK10-5/HK10-7`、`LB16-2/LB16-3/LB16-5/LB16-7`、`TM08-2/TM08-3/TM08-5/TM08-6`、`HB05-1/HB05-2/HB05-3/HB05-4/HB05-7`、`DP74-1/DP74-2/DP74-3`，以及 `RG11-2/RG11-3/RG11-4/RG11-5/RG11-6`、`WE15-1/WE15-4/WE15-5/WE15-7`、`AP06-2/AP06-3/AP06-5/AP06-6`、`CS14-2/CS14-3/CS14-4/CS14-6` 和 shared-thesis metadata claims。去重后为每条唯一问题分配稳定的批次 `issue_id`，并保留这些旧 ID 作为 provenance。

表中组 ID 是初始去重入口，不预先假定最终问题数。执行过程中必须分别报告：

1. 初始问题数：原始 10 组 P0、5 组 P1，以及去重后的初始唯一 P0/P1 数；
2. 本轮新发现问题数：首次由逐篇读取或 L3/L4 研究产生、且不属于初始唯一集合的问题数；
3. 最终唯一 P0/P1 数：去重后的初始问题与新发现问题的并集，按优先级分别计数；
4. 状态数：已研究、部分研究、因时间停止、因来源不足停止，以及仍带有证据边界标记的问题数。

P0/P1 每条记录都必须同时写入所有相关 source 页和批次研究报告；不能把它们写成需要用户逐项确认的任务清单。共享实验或共享 thesis lineage 的问题在各 source 页使用同一个 `issue_id`，并保留来源依赖说明。

## 研究状态、L3/L4 路由和停止规则

`research_status` 使用以下批次登记状态：`discovered`、`queued`、`active-L3`、`candidate-L4`、`completed`、`partially-researched` 和 `stopped`；另设 `stop_reason`（`time`、`source`、`data`、`conflict` 或 `low-gain`）和证据标记 `needs-human-review`。这些是本批次的统计标签，不替代 `autonomous-research.md` 的 L0–L4 状态机。`needs-human-review` 只描述原始证据无法闭合的具体边界；研究报告仍需给出阶段结论、剩余不确定性和下一自主路线，不把它转成用户待办。窗口结束时仍处于研究中的单元必须落到 `partially-researched` 或 `stopped`，并写明原因。

- **L3:** 处理文献冲突、来源依赖、竞争解释、实验判据、旧知识纠正和跨来源综合。每个 L3 单元记录输入来源、问题、检索/阅读范围、阶段结论和证据 locator。
- **L4:** 只有 L3 已提出可检验问题时才启动；只能使用可追溯公开数据或可靠模拟。每个 L4 单元必须有 manifest、参数、代码或计算记录，并完成敏感性或负例/反例检查（至少一项，说明选择理由）；结果标为模型或本任务推断。用户真实数据仍遵守现有手动启动关口。
- 每次研究循环记录启动、完成、部分完成和停止数量；停止原因至少区分时间不足、全文缺失/不可读、数据不可得、证据冲突和信息增益不足。
- 研究按信息增益动态停止：若继续阅读只增加背景而不改变 claim、链接、竞争解释或判断，记录边界后转入下一问题；不能用“读完全部论文”或“耗尽 10 小时”单独宣称完成。

## 10 小时研究安排

| 阶段 | 时间 | 具体动作与产出 |
|---|---:|---|
| 问题池整理 | 0.5 h | 读取上一批报告，建立全量 PDF/学位论文清单，按 source lineage 去重，生成统一问题登记表和初始优先级。 |
| 证据加载与排序 | 1 h | 逐篇打开学位论文和相关 PDF，完成题名页、摘要、目录、引言、结论及关键图表的最低真实覆盖；提取核心 claim、locator、竞争解释和 L3/L4 路线，形成阅读/研究队列。 |
| L3/L4 研究循环 | 6 h | 深读高信息增益学位论文章节和原始图表；执行文献/证据综合，必要时运行有 manifest 的公开数据或可靠模拟；实时更新 issue、source 页和知识回链。 |
| 知识整合 | 1 h | 汇总新知识、纠正知识、跨来源总结和边界/失败知识；检查旧页面的过强措辞、重复实验计数、lineage 和反证。 |
| 报告与检查 | 1 h | 固化问题状态统计、核心结论、未完成原因、下一路线、source/page 回链、raw 哈希、lint 和 `git diff --check` 结果。 |
| 缓冲 | 0.5 h | 处理高价值冲突、不可读页面、L4 敏感性/负例补跑和中断续跑记录。 |

上述时间合计 10 小时。学位论文的逐篇读取贯穿前 3 阶段：1 小时阶段完成最低覆盖和排序，6 小时阶段完成与 P0/P1 相关的正文、图表和附录深读；任何未覆盖章节都写入阅读记录和下一自主路线。

## 证据到 Wiki 的闭环

1. 每个 PDF 先写入阅读台账，再决定 `deep-read`、`read`、`skimmed`、`source-only`、`duplicate` 或 `needs-human-review`；source-only 必须写出不建立实体页的理由。
2. 每个 P0/P1 问题在对应 source 页写入 `issue_id`、核心主张、locator、竞争解释、阶段结论、知识增量和剩余不确定性，并在批次研究报告中保留完整登记记录。
3. 新 source 至少连接到一个已有核素、能带、实验、方法、概念、模型或 project；受影响旧页面至少回链一个新 source。共享实验和 thesis/journal 依赖关系显式标记，不重复创建实体或独立实验计数。
4. 只有跨来源证据真实改变问题地图、竞争解释或证据缺口时才更新 project/synthesis；模型结果、本任务推断和临时假设分别标记，不能升级为实验事实。
5. 每完成 3–8 篇相近论文，执行一次小范围 lint、断链、反向链接和 locator 抽查，再按剩余信息增益重排队列；不等所有 PDF 读完才回链。

## 批次研究报告

最终报告写入 `outputs/degree-dissertation-autonomous-research-20260910.md`，按以下顺序组织，不设置人工逐项确认章节：

1. **执行结果**：实际研究时间、读取的学位论文/PDF 数量、覆盖深度、覆盖来源、初始与新发现 P0/P1 数量、最终唯一 P0/P1 数量。
2. **L3/L4 研究统计**：L3/L4 启动、完成、部分完成和停止的研究单元数；每类停止原因及对应 issue_id。
3. **核心主张与结论**：每个重要问题的核心主张、证据 locator、竞争解释、阶段结论和适用边界；区分实验事实、作者解释、模型结果和本任务推断。
4. **Wiki 知识增量**：
   - **新知识**：原 Wiki 未记录且得到来源支持的事实；
   - **纠正知识**：旧页面被新证据修正的内容，保留修正前后和 locator；
   - **总结知识**：跨来源综合出的机制、判据或比较结论；
   - **边界/失败知识**：未支持、反证、不可复现或暂不能判断的路线。
5. **未完成研究**：按时间不足、全文缺失、数据不可得或证据冲突分类；每条保留已完成范围、停止原因、剩余不确定性和下一自主研究路线。
6. **验证结果**：source/page 回链、raw SHA-256、PDF 覆盖台账、L3/L4 manifest/计算记录（如有）、lint、`git diff --check`、受保护文件状态和研究产物清单。

报告中的统计以 issue_id 和研究单元为唯一计数单位，论文数量只作为覆盖指标。所有 P0/P1 都必须能从报告回到 source 页，再回到学位论文或相关 PDF 的具体 locator。

## 交付与验收

- 明确使用 10 小时预算，允许 `completed`、`partially-researched` 和带 `stop_reason` 的 `stopped` 并存；未完成不伪装成完成，且有下一自主路线。
- 全量 PDF 和学位论文都有真实读取状态、SHA-256、覆盖范围、source 映射或 source-only 理由；重复文件和共享实验 lineage 可追溯。
- P0/P1 的发现、去重、研究、阶段结论和知识增量均可按上述口径统计；10 组 P0、5 组 P1 初始组及本轮新发现问题均有来源依据。
- 所有关键 claim 有 locator；争议主题保留反证、替代解释和适用条件；未闭合证据保留 `needs_review: true`，不提升信心等级。
- 研究报告回答“发现多少问题、启动多少 L3/L4、完成哪些核心结论、Wiki 增加或纠正了什么、哪些问题为何未完成以及下一步是什么”。
- source/page 回链、raw 哈希、manifest、lint、断链/重复实体检查和 `git diff --check` 通过；raw、OCR 图片和受保护 BibTeX 未修改或暂存。
- 本轮计划编辑完成后只复查本文件的定向 diff；不执行实际学位论文研究，不修改 source 页、已有批次报告或 system workflow。
