# 2026-11-07 核结构规模化研学：所有 worker 的共同合同

你在 `/workspace/wiki`，是受父代理明确授权的研究 worker。用户要求以 Gemini 3.8 Flash Tiered/high 承担大多数工作，复杂问题由 Terra/xhigh 处理；目标是可追溯的低能核结构研究，不是堆论文或使用额度。你不再派发子代理，不提交/推送，不修改调度器、技能、治理、用户 PLAN/BibTeX、原始 PDF 或其它 worker 文件。共享文件单一写者；父代理统一整合。

## 科学任务

核心：三轴形变与集体动力学；交叉：八极/反射不对称，同核异能态、弱衰变与壳演化。六区 A≈60/80/100/130/160/190 是比较坐标，不是硬边界。

本轮已找到并核验三篇出版正文：

- `raw/papers/⁹⁸Mo A possible candidate for octupole collectivity in A ≈ 100 region.pdf`，8物理页，DOI 10.1016/j.nuclphysa.2025.123265。
- `raw/papers/Low-Energy Dipole Strength Distribution in ¹⁰²Ru Coexistence of Scissors and Octupole Resonances.pdf`，7物理页，DOI 10.1103/rcb1-gntj。
- `raw/papers/Exploring chiral rotation in A ≈ 60 nuclei  Role of residual interactions.pdf`，9物理页（下载封面1页），DOI 10.1088/1674-1137/adc3fd。

只由指定的 G01/G02/G03 修改其 canonical source。其余 worker 可以只读这些 PDF，自身关注指定核区，不写这三个 source。

## 必读与流程

按本轮需要读 README、knowledge/index 相关段落、profile、system/handoff 最新两条、system/schema、system/workflows/ingest-strategies、system/evidence-policy。派发消息若指定现有知识入口，先读它们，避免重复已闭合工作。

文献：读取 `.agents/skills/local-literature-archive/SKILL.md`、`.agents/skills/get-paper/SKILL.md`、`.agents/skills/research-archive/SKILL.md`。先本地检查；索引不足可用 `rg --files --hidden --no-ignore raw/papers raw/theses raw/books` 定向回退。外部研究必须实际调用可用 web/search 工具核验题名、日期与 DOI；不能凭记忆给“最新”“全球首次”“从未发现”。技术内容只依赖原论文/机构/正式数据库等 primary sources。

确需新材料时，限于直接能改变本任务判断的候选，先取得与读透1–3份，不泛滥下载。只能新增到自己任务的 `raw/papers/gpt/query/20261107-campaign-Gxx/`，不覆盖任何文件。`manifest.json` 必须是 research-archive-v1，时区化实际获取时间，每条 path/URL或source/size/SHA256/archive_required:true；learning_candidate、learning_topic、collection_reason、acquisition_context 记录实际用途。实际只拿到摘要就按摘要记录，不把网页/XML/一页预览称作全文。

新 canonical source 只用 `knowledge/sources/campaign-gxx-*.md` 前缀（G01–G03指定的既有source除外）。先确认无既有同身份 source；若已有，引用它，在回执提出必要改动，不去改别人的source。

## 硬边界与常见错误

1. 实验能级/多极性/寿命是事实，手征/摆动/静态八极通常仍有模型解释。每条关键 claim 给 claim_kind、locator、单位、误差、适用条件和竞争解释。定位必须指向实际本地版本的物理页与图表/公式；只读摘要不能补正文细节。
2. Thesis、期刊与综述复述同一采集不是独立证据；不要将 cited source 的内容当成本论文直接测量。
3. 质量数、γ软性标签、某个轴对称计算、局部带终点都不能推出整个核区机制不可能。未覆盖/未观察/有反证分别说清。
4. E1增强不能唯一认证静态β3；E3线的存在/多极性与绝对增强B(E3)不同。NRF E1/M1响应与高自旋交替宇称带不可以直接当同一模式。
5. 混合比 δ 要保留多个分支、相位/几何；E2辐射份额不等于E2集体大小；同母态误差存在Cov。半衰期与平均寿命不同，转换不能重复校正。
6. 单j半满壳节点已经作过精确两体/三体PH模型，不重跑同义toy。136Sn多轨道有效两体结果不能据单j定理排除。裸Ikeda恒等式不等于普适gA淬灭。
7. 不创造统一数值阈值、没有来源的精确能量/强度、事件数/显著性或全球新颖性。直接阅读不能恢复未发表原始数据/协方差。
8. 公开产物不得复制大段有版权正文/摘要、原图或下载封面的个人信息。原件只本地留档。
9. `review_status`/`needs_review` 只历史元数据，不作核验优先级、科学强度或人工许可门。不得写human-reviewed。

## 输出合同

每人只改派发消息列出的独占路径；scratch写 `tmp/runs/20261107-large-nuclear-research/Gxx/`。允许独占的 raw/source 路径如上。所有可复用结论必须写入自己 `knowledge/` 页；outputs只是回执。

知识页 frontmatter 的数组全部写在同一行。source 使用 schema 所需字段、真实 raw_file/sha256/archive_required:true、reading_depth，以及正文 Covered scope / Not covered；无真实 citation_key 就留空。research-note 必须 type:research-note、status:active、review_status:unreviewed、reasoning_status:provisional、evidence_sources:[已存在source]、created_from:project、promotion_target:空，以及科学问题/证据矩阵/竞争解释/本任务推断/可证伪预测/失败与停止条件/下一步/历史等必要结构。不要凭空引用尚不存在的其他worker页。

你应交付：

- 指定的 canonical 知识页；
- 独占回执 `outputs/l3/20261107-nuclear-structure-campaign/workers/Gxx-receipt.json`（不要将outputs文件命名manifest.json）；
- 回执含 task_id、实际model/effort若可见、真实read_paths与read_scope、changed_paths、主张定位、命令退出码/核验结果、获得物与SHA、未完成项、最有信息增益的下一步、source_independence。

验收：逐一回查最重要的数字/推断、运行自己source/raw显式归档门、有界diff检查；完整全库lint/Git/QMD由父代理统一执行，不要每人扫描一遍全库。终答给具体路径和3–6条最重要的结果/边界。遇到正文缺失继续可解析的分支，不能把普通研究决策交给用户。
