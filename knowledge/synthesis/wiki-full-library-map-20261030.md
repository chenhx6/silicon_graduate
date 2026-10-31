---
type: synthesis
title: Wiki 全库知识地图与研究机会索引
aliases: [wiki-full-library-map, 全库知识地图]
created: 2026-10-30
updated: 2026-10-31
status: ai-draft
review_status: unreviewed
scope: wiki-structure-nuclear-structure-research-opportunities
confidence: medium
sources: [chakraborty-2023-131xe-wobbling-origin, banik-2020-131xe-multiple-band-structures, gaffney-2013-pear-shaped-rn-ra, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole]
tags: [wiki-index, nuclear-structure, evidence-map, research-opportunities, workspace-audit]
---

# Wiki 全库知识地图与研究机会索引

本页是 2026-10-31 对 `/workspace/wiki` 的结构、知识图谱和研究主线做出的可复用索引。它服务于温故知新、研究选题和后续论文 prospectus；它不替代 `knowledge/sources/` 的原始证据页，也不把运行输出当作科学事实源。

## Question and Scope

本页回答三个问题：知识库目前覆盖了哪些核结构主题；哪些证据链最适合继续温故知新和发展为论文；如何整理 `outputs/` 与 `raw/papers/` 而不破坏原件身份、来源谱系和可复现回链。索引结论是导航和研究决策，科学主张仍以 source 页、原件和 locator 为准。

## 1. 结构与职责

仓库的长期分层由 `README.md:48-62` 和 `system/path-contract.md:12-47` 定义：

| 层 | 当前职责 | 研究使用方式 |
|---|---|---|
| `knowledge/` | source、核素、能带、实验、方法、模型、project、synthesis、research-note 与问题页 | 日常检索、跨来源综合、论文论证的知识层 |
| `raw/` | 用户提供或获授权归档的原始论文、数据和附件 | 证据身份、哈希、原文 locator 的底座 |
| `outputs/` | 日报、审计、回执、研究运行包和计划书 | 可复现过程与交接，不作为唯一知识源 |
| `system/` | schema、workflow、脚本、检查、handoff 和日志 | 研究治理、证据门和自动化执行 |
| `tmp/` | 下载 staging、OCR、缓存和中间结果 | 可删除，不能承载唯一事实 |

当前 QMD collection 只索引 `knowledge/**/*.md`；因此全库温故知新应先检索知识层，再沿 source 页的 `raw_file`、URL、DOI 和 locator 回到原件。`outputs/` 和 `raw/` 的整理不能改变这一边界。

## Evidence Matrix

| 研究层 | 代表页面 | 可复用证据 | 当前边界 |
|---|---|---|---|
| A≈130 多模式判别 | `131Ce`、`133Ce`、`135Nd` projects | 连接、混合比、偏振、寿命、`B(E2)`/`B(M1)` 和形变比较 | 共同 raw、联合协方差和完整算符常缺 |
| wobbling/partner 分支 | `135Pr`、`187Au`、`131Xe` projects | AD、`R_ac`、偏振、分支和对象身份审计 | RDCO 单独不保证全局唯一；响应与寿命决定可识别性 |
| MR/AMR 与八极 | Day26/Day27 research notes 和 synthesis | `M1/E2`、E1/E3、交替宇称、终止和模型边界 | toy/model 输出不能冒充实验观测 |
| 相邻核科学 | `100Sn`、GT、有限温度、衰变和跨质量区 notes | 可迁移的方法、反例和数据合同 | 需要回到具体核素的 primary 与实验输入 |

## 2. 2026-10-30 规模快照

| 对象 | 数量 | 解释 |
|---|---:|---|
| `knowledge/**/*.md` | 1,032 | 可检索知识页 |
| `knowledge/sources/` | 472 | 文献、数据集、方法或制度来源页 |
| `knowledge/research-notes/` | 245 | 研究中间结论、边界和可复算分析 |
| `knowledge/bands/` | 63 | 能带和局部结构对象 |
| `knowledge/nuclei/` | 62 | 核素对象 |
| `knowledge/concepts/` | 48 | 物理概念与判据 |
| `knowledge/experiments/` | 38 | 实验与装置对象 |
| `knowledge/methods/` | 33 | 分析方法与观测协议 |
| `knowledge/models/` | 15 | 理论模型 |
| `knowledge/observables/` | 20 | 可观测量和派生量 |
| `knowledge/projects/` | 19 | 证据地图、争议项目和研究管线 |
| `knowledge/synthesis/` | 14 | 跨来源综合页（含本页） |
| `outputs/` 全部文件 | 13,150 | 过程产物，最大子树是 `outputs/learning-daily/` |
| `raw/papers/` 全部文件 | 499 | 原始学习资料和用户/外部来源副本 |

知识页之间的 Wiki 链接约 11,118 条、约 1,032 个不同目标；约 456 个 source 页声明了 `raw_file`，约 425 个知识页直接出现 `raw/papers/` 路径，约 362 个知识页引用 `outputs/` 工件。后两项是整理风险指标：任何批量移动都必须先把路径引用、文件哈希和相对链接做成 manifest。

## 3. 研究主线的演化

`system/workflows/continuous-learning.md:17-64` 给出的路线可压缩成四个彼此衔接的能力层：

1. **结构框架**：壳结构、单粒子、配对、平均场、形变、转动、振动、alignment、signature、wobbling、chirality、磁转动和反磁转动。
2. **实验判据**：反应布居、γ 符合与门控、Doppler correction、DCO/ADO、偏振、内转换、混合比、RDDS/DSAM/fast timing、寿命、`B(E2)`、`B(M1)` 和 `Q_t`。
3. **广义核科学**：反应与衰变、质量与 Q 值、GT/Fermi、壳模型、CSM、TRS、TAC、PRM/QTR/TPSM、IBM/IBFM、CDFT、RPA 和可复现分析。
4. **研究判断**：跨来源独立性、反证、必要伴随观测、共享响应/协方差、falsifier、L3 readiness 和 L4 数据边界。

课程日报从 Day 1 的证据合同逐步走到 Day 27 的跨质量区迁移；Day 28 当前收束到 `131Xe` 低自旋对象身份、混合比分支和可识别性。Day 29 的无学分预习把问题转化为最小实验设计：宇称、偏振、角分布、响应、背景和联合协方差必须一起考虑。Day 30 应回读四周 REFLECT 和错题，而不是简单统计读过的论文数。

## 4. 高价值主题簇

### A≈130 三轴性与多模式判别

这是当前最成熟的主轴，包含 `131Ce`、`133Ce`、`134Pr`、`135Nd`、`136Sm` 和相关 `131Xe` 案例。可复用的核心不是“某条带证明了某个模式”，而是把能带连接、混合比、偏振、寿命、`B(E2)`/`B(M1)`、形变和竞争解释放进同一证据矩阵。

- `knowledge/projects/131ce-collective-mode-discrimination.md`：把正常带、候选 wobbling/chirality/shape-coexistence 和寿命约束放在同一判别框架。
- `knowledge/projects/133ce-thesis-analysis-blueprint.md`：提供低自旋到高自旋的三轴性证据链、原始论文和 thesis-only/L4 边界。
- `knowledge/projects/135nd-chiral-partner-resolved-evidence-map.md`：展示静态手征、振动手征、几何退简并和带间观测的分层证据。
- `knowledge/projects/chirality-shape-coexistence-companion-matrix.md`：把手征与形状共存的必要伴随观测和模型依赖放在一起。

**可形成论文的研究问题**：能否用预先冻结的 observable—response—covariance 合同，把“相似能级间距”升级为可证伪的模式比较？现有页面已经有大量边界和 toy algebra，下一步应优先寻找真实逐线数据、公开寿命或共同 raw response，而不是继续增加 synthetic 网格。

### wobbling、tilted precession 与 chiral vibration

`knowledge/projects/low-spin-wobbling-controversies.md`、`knowledge/projects/135pr-wobbling-controversy.md`、`knowledge/projects/187au-longitudinal-wobbling-controversy.md` 和多份 `wobbling-*` research note 形成了争议主线。重复出现的关键教训是：`R_ac`、混合比符号、偏振和带间 `B(E2)` 的解释高度依赖响应、取向、门条件和分支选择；RDCO 单独通常不能全球唯一决定 δ。

**可形成论文的研究问题**：建立跨核素的“模式判别最小观测集”，把 wobbling 与 tilted precession、chirality 和 signature partner 的可混淆区域画成可计算的 decision boundary。现有 `wobbling-dual-root-degeneracy-and-polarization-disambiguation.md`、`wobbling-vs-tilted-precession-hessian-stability.md` 和 `wobbling-mode-transferability-and-moi-hierarchy.md` 可作为理论和方法骨架，但需要真实实验输入才能升级为 L4。

### 磁转动、反磁转动与极限自旋

Day 26 的知识资产已扩展到剪刀模型、AMR/MR、odd-A termination、量子 `M1` 端点、核芯耦合和四极/八极竞争。相关页面包括 `knowledge/research-notes/mr-amr-observable-matrix-boundary.md`、`mr-amr-band-termination-and-extreme-spin-limits.md`、`fixed-j-quantum-shears-m1-boundary.md` 和 `cranked-shears-core-coupling-pb-vs-pr.md`。

**可形成论文的研究问题**：哪些所谓的 `B(M1)` 下降或能量闭合，是几何剪刀信号，哪些其实来自量子有限角动量、核芯四极耦合或组态终止？优先路线是用真实 band energies、相对强度和至少一项独立寿命/磁矩约束做统一拟合；toy 结果只能作为 falsifier 设计。

### 八极集体性、E1/E3 网络与四极—八极耦合

`knowledge/research-notes/global-octupole-be3-q3-experimental-benchmark-database.md`、`octupole-three-tier-evidence-ladder.md`、`octupole-gdr-splitting-and-low-energy-e1-ewsr-boundary.md`、`actinide-alternating-parity-quadrupole-octupole-prm.md` 和 `cranked-qrpa-chiral-octupole-vibrational-phonons.md` 已形成一个可以向跨质量区扩展的主题簇。

**可形成论文的研究问题**：E1/E3 交替宇称、低能 E1 增强、GDR 分裂和八极—三轴耦合如何在同一个证据等级表中区分？下一步应优先补统一单位、跃迁方向、分支比归一和实验/模型独立性，而不是把 synthetic QRPA 或现象学扫描写成核素事实。

### 相邻核科学桥接

`knowledge/projects/100sn-gamow-teller-independent-evidence.md`、`knowledge/research-notes/cdft-time-odd-fields-and-magnetic-moments.md`、`n138-isotonic-octupole-collapse-and-barrier-dissolution.md`、`gdr-thermal-width-expansion-and-tsfm-inapplicability.md`、`gpv-cross-mass-kinematic-and-damping-inapplicability.md` 和 `coriolis-antipairing-and-superdeformed-alignment-transitions.md` 提供从核结构到衰变、有限温度、质量区系统学和微观时奇场的桥。

**边界**：这些页面适合产生假设和补充方法训练；正式论文仍需回到具体原始数据、实验不确定度和可复核 locator。不能因为模型链条完整，就把模型差异写成实验事实。

## 5. 论文候选队列

详细的30天后投稿候选、证据门和下一步顺序见 [[post-30-day-nuclear-structure-paper-prospectus]]。

按当前证据成熟度而不是新颖性排序，短期最可执行的候选是：

| 候选 | 论文核心 | 当前状态 | 最小新增输入 |
|---|---|---|---|
| 131Xe 低自旋对象身份与 δ 分支 | 2020/2023 band crosswalk、宇称版本、RDCO 双根和同母态强度可识别性 | L3，边界已清楚，仍缺原始 AD/偏振/联合协方差 | 1983 AD 原件或逐线 raw/response；794.8-keV 宇称独立判据 |
| wobbling 的跨核素最小判别集 | `R_ac`、偏振、带间 E2、寿命和响应合同的 decision boundary | 方法学骨架较完整，实验汇总未闭合 | 至少两个核素的共同格式数据和独立观测 |
| 131Ce/133Ce 模式竞争矩阵 | 三轴性、signature、wobbling、chirality、shape coexistence 的共同证据表 | L3/L4 candidate | 连接跃迁 mixing ratio、偏振和多带寿命 |
| MR/AMR 终止与核芯耦合 | 剪刀几何、量子端点、四极核芯和 termination 的可证伪分离 | 理论边界充分，实验数据未统一 | 真实能带、强度、寿命或磁矩 |
| 八极 E1/E3 跨质量区数据库 | 统一跃迁方向、`B(E3)`、`Q_3` 和 E1 竞争机制 | 数据库草案，需元数据审计 | 逐条 primary locator、归一化和共同系统误差 |

这些候选都必须经过 `system/paper-evidence-gate.md`：source identity、raw/full-text、locator、claim kind、独立性、反证和人工审阅边界齐全后，才适合变成期刊稿件。

## 6. 温故知新的阅读分层

为了避免把时间消耗在重复打开运行回执上，后续全库复习按三层执行：

1. **深读层**：`knowledge/projects/`、`knowledge/synthesis/`、高争议 `knowledge/research-notes/`，以及对应 `knowledge/sources/` 的原始主线、关键图表和限制。
2. **浏览层**：与当前问题共享核素、观测量或竞争解释的 band、method、model 和 experiment 页面；只在发现矛盾或缺 locator 时回到原件。
3. **索引层**：低相关或仅 metadata 的 source 页、旧运行回执、重复的 scheduler 工件和已被 canonical 页面吸收的过程文件。

每次复习应记录“记住的结构关系、改变的判断、仍缺的观测、下一条高信息路线”。读过数量不作为完成标准；能够写出 falsifier、共享数据边界和必要 companion observable 才算真正复习。

## 7. 工作区整理边界

本次只完成索引和风险识别，尚未移动或删除 `outputs/`、`raw/papers/` 文件。原因是知识页中有大量 `raw_file`、相对路径和输出工件引用，且 raw 目录包含用户原件。下一阶段必须先生成：

- 文件相对路径、大小、SHA-256、扩展名和当前父目录的 manifest；
- 所有知识页和运行记录中的引用反向索引；
- 相同哈希的重复候选及其最早/最强证据路径；
- protected 文件清单，包括用户 PDF、`raw/zotero/wiki-inbox.bib`、runner live state、`PLAN.md` 和已有 dirty 文件；
- 只增不丢的目标目录与 redirect/manifest 方案。

只有某个移动同时满足“哈希不变、引用可更新、原路径可追溯、未覆盖用户原件、可逆回滚”时，才进入小批量整理。否则保留原路径并在 manifest 中标记“乱放但不可安全移动”，这比静默改写证据路径更可靠。

2026-10-31 已执行一次只读安全的 `qmd update`：collection 重新索引 `10` 个新页和
`10` 个更新页，随后完成大部分 embedding 刷新；最后 `index.md` 的 `37` 个 chunks
因 session expiry 仍待嵌入。未运行 `qmd cleanup`，未修改 `raw/`；orphan chunks
仍保留为工具状态，不作为科学证据。

## 8. 当前未决与下一步

- `131Xe`：完成 Day28 最终课程审计前，保持 `completed_day_indices=[]`、`partial_day_indices=[28,29]`；不把 Day29 预习当作学分。
- 全库：先完成 outputs/raw 的 manifest 和引用图，再决定是否只整理新生成的过程工件。
- 论文：从上表选择一个有真实输入的候选，建立 claim-to-source matrix、falsifier 和最小数据合同；不在缺少 raw/response/covariance 时生成代理 L4 结论。
- 质量门：继续保留 `needs_review: true` 和 provisional；不设置 `human-reviewed`，不把 self-audit 升格为人工审阅。

## Synthesis

全库最稳定的共同方法是“先确认对象和来源谱系，再组合互补观测量，最后才讨论模式标签”。近简并、强跃迁、模型极小和相似的 `B(M1)/B(E2)` 都可以由多个机制产生；可发表的增量应来自联合证据、反证和可识别性，而不是继续堆叠相似案例。

## Counter-evidence

- `RDCO`、单条 `B(E3)`、单个形变参数或一张能级图都不能单独排除竞争解释。
- 同一实验的期刊论文、学位论文、评估文件和再分析不能自动计为独立实验。
- 缺少原始 response、事件级计数或联合协方差时，只能形成 L3 证据审计和 L4 readiness boundary。
- `raw/papers/` 中的重复字节文件只说明内容相同，不说明来源独立性或哪个路径应删除。

## Model Dependence

TRS、TAC、PRM/QTR、TPSM、IBFM、CDFT、RPA/QRPA、GOSIA 和 DSAM/RDDS 对输入、算符、校准、feeding 和协方差的依赖不同。模型端点、`β`/`γ`/`β3`、有效电荷、g 因子和淬灭参数必须保持为 model-result，不能在索引中升级为 experimental-fact。

## Limitations and Missing Evidence

本页没有重新拟合任何实验数据，也没有把 1,019 页全部 deep-read；规模数字和链接数量是 2026-10-30 的文件快照。`outputs/literature-acquisition/20261030-workspace-audit/` 的引用扫描是保守的路径形状分析，含空格、相对路径和省略号的条目仍需人工复核。论文候选的最终可行性取决于 primary full text、真实数据、响应和共同不确定度。

## Sources

- [[chakraborty-2023-131xe-wobbling-origin]]：Day28 的对象身份、混合比分支和响应边界。
- [[banik-2020-131xe-multiple-band-structures]]：同采集谱系、795-keV E1 标签和低自旋交叉核验。
- [[gaffney-2013-pear-shaped-rn-ra]]：E2/E3 矩阵元与静态/动态八极解释边界。
- [[bucher-2016-144ba-direct-octupole]]、[[bucher-2017-146ba-direct-octupole]]：直接 E3 与 E1 变化的跨区比较。
- `README.md:48-62`、`system/path-contract.md:12-47`、`system/workflows/continuous-learning.md:17-64`：仓库结构、路径职责和学习路线。
