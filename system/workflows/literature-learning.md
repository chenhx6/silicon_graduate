---
type: system-workflow
graph-excluded: true
---

# 文献检索、补读与筛选回放

使用 `system/scripts/literature_learning.py`，从具体科学问题和实际原件范围出发。它在本地处理文件。原件选取先过[馆藏身份核对](local-literature-archive.md)，查到的页再按[摄入](ingest.md)或[反向检验](reflect.md)的证据规则阅读。多个版次对应同一实验时，保留其谱系关系。

## 按问题定位原页

给出少量已核对身份的 PDF 和与原文匹配的术语。搜索结果包括原件 SHA-256、物理 PDF 页、抽取片段和匹配词。物理页与书面页码的映射由原件核实。结果来自关键词排序，同页优先显示一个片段；公式、图表、扫描页和多栏顺序需要回原件确认。清单报告没有可检索文字的页面。提取依赖 Poppler 的 `pdftotext`，缓存按原件哈希留在 `tmp/literature-learning/`。QMD 的知识页索引依然提供语义导航。

```bash
mkdir -p tmp/literature-learning
python3 system/scripts/literature_learning.py evidence \
  raw/theses/PAPER.pdf \
  --query 'Doppler shift centroid attenuation stopping power' \
  > tmp/literature-learning/round-1.json
```

需要核对多栏、表格位置或图注时，可对候选原页运行 `layout`。它给出物理页、页面尺寸和各文本块的边界坐标，量纲为点，原点在页面左上角。用页面图像核对实际列顺序、单元格与脚注。扫描图像或公式的核对仍依赖相应的原页图像。

```bash
python3 system/scripts/literature_learning.py layout raw/theses/PAPER.pdf --page 120
```

## 按证据缺口补读

读过首批命中页后，把能改变判断的缺口写成一个问题。用不同术语定位方法、误差传播、反例或灵敏度前提。复用上一轮原件与分轮清单，可追加另一件已归档原件。收据保留父回执哈希，标明哪些页以前出现过。以前出现过的页仍可含有同一问题的另一条决定性证据。发现版本变化时，按新底本重建检索记录。

```bash
python3 system/scripts/literature_learning.py followup \
  tmp/literature-learning/round-1.json \
  --gap '最终估计如何传播 stopping-power 不确定度？' \
  --query 'systematic uncertainty stopping powers propagated covariance' \
  > tmp/literature-learning/round-2.json
```

以实际回读的页、图、表、公式和适用条件判断证据。歧义、竞争解释和空结果应进入原有证据矩阵。片段检索的覆盖范围是回执列出的候选原页。整篇阅读按原有覆盖验收。

## 让已筛结果重新排列候选

`screen` 接受 `get-paper` 的 `search-manifest.json`，也接受由 `id`、`title`、可选 `abstract` 和 `label` 组成的 JSON 列表。候选 ID 按显式 `id`、DOI、arXiv ID、URL、标题回退。可另外用 `--labels` 提供 ID 到 `relevant` 或 `irrelevant` 的映射。标签反映当前问题的筛选决定。相关和不相关样本各有可用术语后，用标题和摘要训练一个轻量词项模型来调整下一批阅读顺序。原始记录与排序仍可对照。

```bash
python3 system/scripts/literature_learning.py screen \
  tmp/runs/get-paper/CASE/search-manifest.json \
  --labels tmp/literature-learning/screen-labels.json
```

模型分数用于排序。低排位候选仍保留，独立证据与反常结果值得在筛选中定向抽查。`replay` 使用完整标注的旧候选池，先指定正负种子，再比较自适应与原顺序在同一留出池上找回相关文献的进度。自适应排序每次只能看到先前已选记录的标签。输出保留输入清单哈希。比较的是这批已标注候选的回放效果。

```bash
python3 system/scripts/literature_learning.py replay \
  tmp/literature-learning/labeled-pool.json --seed POSITIVE_ID --seed NEGATIVE_ID
```

## 来源与适配

以下来源均按固定版本静态核读。本地实现使用相同工作原理并采用 Wiki 的原件、证据和路径约定。

| 来源 | 吸收的机制 | 核查文件 SHA-256 |
| --- | --- | --- |
| [PaperQA2 `c692d0d`，Apache-2.0](https://github.com/Future-House/paper-qa/blob/c692d0dfeac4a0296599f7fe21a253a58b7ac12a/src/paperqa/docs.py) | 针对问题从文献原文取证据片段 | `d14055c94afd811e4307a1ef3f7d05ebdeaf57ddf188f8b394f81bfeedce83d5` |
| [OpenScholar `0e9b8fb`，Apache-2.0](https://github.com/AkariAsai/OpenScholar/blob/0e9b8fb912273d3dae39e593da86e4f6d3bf8de1/src/open_scholar.py) | 用当前回答暴露出的证据缺口发起补查 | `873d2e84c3519a435475a17286e3805412c3fe25ba83967af52cf81b66776dd0` |
| [ASReview `79d5682`，Apache-2.0](https://github.com/asreview/asreview/blob/79d568212b2b0a78f9fd7be3c5117dfb890489f9/asreview/simulation/simulate.py) | 用筛选反馈更新顺序，并用可靠旧标签回放 | `02a1d1d910900b668b52889c60253581582ffb292ffd3030beca28a86951a0fb` |
