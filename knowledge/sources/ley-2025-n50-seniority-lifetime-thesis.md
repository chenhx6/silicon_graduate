---
type: source
title: "Ley 2025 - Investigation of Seniority Conservation in the N = 50 Isotones using Lifetime Measurements"
title_original: "Investigation of Seniority Conservation in the N = 50 Isotones using Lifetime Measurements"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Mario Ley"]
year: 2025
institution: "Universität zu Köln"
url: https://kups.ub.uni-koeln.de/79393/
canonical_source: "Mario Ley, accepted doctoral dissertation, Universität zu Köln, 2025"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/PhD_thesis_Ley.pdf
raw_sha256: 63aaf3cf93bc4509fae22923a28ecb1d50759135cc277e479106244027a05136
raw_storage_status: archived-local
archive_required: true
nuclei: ["91Nb", "92Mo", "93Tc", "94Ru", "95Rh", "95Ru"]
tags: [seniority, fast-timing, transition-strength, shell-model, thesis]
---

# Ley 2025：N=50 同中子素的寿命与 seniority

## Bibliographic Record

Mario Ley，Universität zu Köln 博士论文。PDF 1 记载 2025 年获接收。
PDF 23–33 和 37–44 分别是两篇附印 PRC 出版正文（`10.1103/PhysRevC.108.064313`、
`10.1103/PhysRevC.110.034320`）。PDF 47–56 是 2025 年 6 月 27 日的附印稿。
Crossref 元数据显示同题论文于 2026 年 11 月 9 日发表（`10.1103/6fdh-yk8k`）。
下述 Rh/Ru 数值定位到实际可核的学位论文附印稿，期刊全文和稿版差异尚待核查。

## Scope and Reading Depth

原件 PDF 1–84，含虚页、引言和方法、三项附文、汇总、展望与书目。
Gemini 分单元主读，Codex 核对附文身份、关键表和定时条件。
PDF 34 在缓存回执中未读，已在原 PDF 上验证为无印刷内容的分隔页。

## Summary

三组实验用混合 LaBr₃ 与 HPGe 探测器和 γ–γ 快定时测量能级平均寿命。
对比同中子素的 E2 归一强度后，有些跃迁符合单一 \(g_{9/2}\) 轨道的
seniority 趋势，个别跃迁则需要检验组态混合、模型空间和已有数据的分歧。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| LEY-1 | 定时谱以 prompt 响应和指数衰减卷积表示。寿命短时需校准质心位移的能量依赖和本底，寿命可分辨时可拟合指数尾。附印文章按不同门和峰/本底条件选用方法。 | analysis-method | direct-original-pages | PDF 16–19, 39–42 |
| LEY-2 | $^{92}$Mo 的 $4_1^+$ 采用平均寿命为 22.5(11) ps，对应 $B(E2;4_1^+\to2_1^+)=132^{+7}_{-6}$ $e^2\,\mathrm{fm}^4$。附印文以这组核的跃迁数据约束态相关有效电荷，再预测较多价质子核，不构成预测核的独立验证。 | measurement-and-model-input | direct-original-pages | PDF 27 Table I, 28–31 |
| LEY-3 | $^{94}$Ru 的 $4_1^+$ 采用平均寿命为 66(2) ps，$B(E2)=50(2)$ $e^2\,\mathrm{fm}^4$。表中保留两个文献强度 38(3) 与 103(24)，单一、态相关有效电荷计算分别给 12 与 7.8(7)。同篇 Fig. 6 的两个极小值显示，仅用该组强度不足以唯一确定混合参数。 | measurement-and-competing-models | direct-original-pages | PDF 40–43 Tables I–II, Fig. 6 |
| LEY-4 | $^{93}$Tc 的 1516 keV 跃迁列 M1+E2，所采用的 $\delta=-16.6^{+21}_{-29}$ 来自该附印文的 Ref. [39]，用于换算下限。本文的实测约束是寿命，未用 γ 线偏振和角量反演该 $\delta$。 | adopted-multipole-input | direct-original-pages | PDF 40–41, Table II note d |
| LEY-5 | $^{95}$Rh 附印稿的 $17/2_1^+\to13/2_1^+$ 717 keV 跃迁给出 $B(E2)=32(1)$ $e^2\,\mathrm{fm}^4$，与同栏文献下限 $\ge167$ 不相容。$^{95}$Ru 两条 255 keV 线重叠，作者用不同馈入门及联合拟合检验平均寿命，并保留同一批数据的依赖。 | manuscript-measurement-and-source-conflict | direct-original-pages | PDF 50–55, Table II |
| LEY-6 | 论文用纯单 \(j\) 壳的预期趋势检验 seniority。多数强度仍呈现局部趋势，偏离的 $^{94}$Ru、$^{95}$Rh 结果可由部分 seniority 混合或外轨道成分讨论，且不同模型仍有失配。 | cross-nuclide-interpretation | direct-original-pages | PDF 57–61, Fig. 8 |

## Competing Interpretations and Limitations

- 论文不同章及正文汇总复用了同一组寿命。附印文章只计各自的实验来源。
  $^{95}$Ru 的 255 keV 双线有公共级联和响应条件，不把两种提取法当作独立实验。
- \(B(E2)\) 依赖多极性、分支和转换系数。表中的下限、拟合采用值、外来
  文献值和模型预测需按列读取。PDF 44 的 Ref. [39] 对应 Brown 等，
  *Nuclear Physics A* 306, 242–258 (1978)，DOI `10.1016/0375-9474(78)90326-3`。
  本地 NSR 书目记录报告该研究测过延迟 γ 的线偏振和角分布。1516 keV 的
  $\delta$ 如何取得、线偏振是否进入该支路求解以及是否报告 $\sigma/I$，须回
  Brown 原表或正文。这里仅登记候选与所采用的二手数值。
- 跨壳激发、态相关有效电荷和 seniority 混合均是物理建模输入。
  $^{94}$Ru 的相互不兼容测量及双极小需要在比较模型时一并保留。

## Extracted Pages

- PDF 1–22：书证、seniority、快定时与实验设计。
- PDF 23–44：两篇附印出版论文及其分隔页。
- PDF 45–56：$^{95}$Rh/$^{95}$Ru 附印稿及章页。
- PDF 57–84：总结、展望、文献、图目、贡献声明。
