---
type: source
title: "Vogt 等（2017）：137Ba 的 tentative 15/2− 指认、上游 isomer 寿命与独立 E2 检验范围"
aliases: [Vogt2017PRC95_024316, 137Ba post-ENSDF 15/2 assignment]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-theory
reading_depth: skimmed
title_original: "Isomers and high-spin structures in the N=81 isotones 135Xe and 137Ba"
authors: [A. Vogt, B. Birkenbach, P. Reiter, A. Blazhev, M. Siciliano, K. Hadyńska-Klęk, J. J. Valiente-Dobón, C. Wheldon, E. Teruya, N. Yoshinaga]
authors_abbreviated: true
author_count: 89
journal: Physical Review C
year: 2017
volume: 95
issue: 2
pages: "024316"
article_number: "024316"
publication_date: 2017-02-15
doi: "10.1103/PhysRevC.95.024316"
canonical_source: "doi:10.1103/PhysRevC.95.024316"
citation_key: Vogt2017PRC95_024316
citation_key_origin: "Unique DOI-based local citation key; full author list supplied in the sidecar BibTeX."
raw_file: "raw/papers/gpt/query/20261106-vogt2017-ba137-rstat/manifest.json"
raw_sha256: "3e777f4bae5e9e2ca7b4a6bd773436d1282bdd64678b117250d512c886f5854f"
raw_storage_status: archived-local
archive_required: true
nuclei: [137ba, 135xe, 133te]
reactions: [136Xe-238U-MNT, 136Xe-208Pb-MNT, 136Xe-198Pt-MNT, 130Te-11B-p3n]
models: [shell-model, PQM130, SN100PN]
observables: [level-energy, spin-parity-assignment, half-life, relative-gamma-intensity, reduced-E2-transition-probability]
methods: [gamma-gamma-coincidence, delayed-coincidence, decay-curve-fitting, source-lineage-audit]
tags: [a130, n81, isomer, E2, post-ensdf, calibration-dependence]
---

# Vogt2017：目标指认已出现，所需绝对 E2 分母仍缺

## Bibliographic Record

A. Vogt **et al.**（89 位作者），*Isomers and high-spin structures in the N=81 isotones 135Xe and 137Ba*，**Physical Review C 95(2), 024316 (2017)**，DOI `10.1103/PhysRevC.95.024316`。正式发表日期为 **2017-02-15**，由 OSTI/CHORUS 封面及归档 Crossref DOI 记录的 `published-online`/`published` 共同核定。仓储页面的下载、收录或更新日期不作为文章年份。

引用键：`Vogt2017PRC95_024316`。[完整 BibTeX](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/vogt2017-citation.bib)保留 89 位作者；[元数据 JSON](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/vogt2017-metadata.json)列出完整作者顺序和日期依据。完整作者顺序采用 DOI 元数据并与稿件作者页核对，本页 frontmatter 仅列前十位。

本地 [manifest](/workspace/wiki/raw/papers/gpt/query/20261106-vogt2017-ba137-rstat/manifest.json) 的 SHA-256 为 `3e777f4bae5e9e2ca7b4a6bd773436d1282bdd64678b117250d512c886f5854f`，记录下载原址、实际取得时间、原始 PDF、Crossref JSON及本地阅读派生物。

| 本地文件（均在该 raw 集合） | SHA-256 | 版本边界 |
|---|---|---|
| `vogt2017-osti.pdf` | `1cd82bd29db800728593c181bf8e720576ec5fc113d1e354dc7d4c388e0f6c1c` | OSTI/CHORUS accepted manuscript；正文标注 January 17, 2017 |
| `vogt2017-accepted.pdf` | `5a17b3fdd5c08c4e27284bc59f1d3e6e7ef9821746069057caf8b2745a12680b` | Birmingham peer-reviewed version；正文标注 January 25, 2017，不能由 URL 中的 January 21 推断正文日期 |

两份 PDF 均为 18 页，即封面加 17 页稿件。下文以 Birmingham 稿件为阅读主件：**PDF 页码 = 稿件印刷页码 + 1**；不声称这些页码就是期刊排印版页码。关键能级、Table II/III 数值在两份稿件中一致。完整 PDF、提取文本和视觉核查页图仅留在本地 raw，**不进入论文包**。

## Scope and Reading Depth

**Covered scope:** 实际读取作者页/封面、实验方法相关段、137Ba 的 Section III B、Fig.6/7、Table II，Section IV 的 E2/有效电荷及态排序讨论、Table III，相关结论和 references [26]/[69]。视觉核查 Fig.6、Fig.7/Table II、Table III；检查目标表格的空强度格及跨稿件对应数值。

**Not covered:** 未重新分析实验事件或重做衰变曲线拟合；未逐条验证所有高自旋新 γ 的放置；未重算 PQM130/SN100PN，也未计算新的 IBFM 高自旋预测；没有继续搜寻本文以外的新实验或原参考文献全文。因此按有界精读位置记录 `skimmed`，不标全文 deep-read。

## Summary

本文已经在 **2229.8 keV** 标出 tentative **\((15/2^-)\)**，通过约 **1568-keV** γ 衰变到 **661.7-keV \(11/2^-\)** isomer。因此，“137Ba 没有已指认 \(15/2^-\) 目标”只能作为此前 **2007 ENSDF 对象**的历史检查结果，不能继续充当当前文献结论。

但本文没有给出该 **2229.8-keV 态的独立寿命或绝对 \(B(E2;15/2^-\to11/2^-)\)**。经 1568-keV γ 加门得到的 **589(20) ns 是上游 2349.9-keV \((19/2^-)\) 态的半衰期**。本文给出的 **0.46(3) W.u.** 属于 **\((19/2^-)\to(15/2^-)\)**，可以另列为 EM 检验，不能替代 \(R_{\rm stat}^{(1)}\) 的分母，也不直接进入初态 \(J=11/2\) 的三阶电荷矩。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | confidence | locator | needs_review |
|---|---|---|---|---|---|---|---|
| V17-MAP | 作者按 N=81 同中子素系统学将 2229.8、2349.9 keV 分别标为 \((15/2^-)\)、\((19/2^-)\)，括号保留；这不同于旧 ENSDF 的 \((13/2^-)\)、\((17/2^-)\) 标注。 | author-interpretation | direct | single | high | Fig.6，PDF p.8/稿件 p.7；Table II，PDF p.9/稿件 p.8；Sec.IV，PDF p.13 | true |
| V17-GAMMA | Table II 给出 2229.8→661.7 keV 的 γ 为 1568.2 keV，γ 能量统一误差 ±0.5 keV；Fig.6 则标 1568.1 keV。两处原值分别保留。 | experimental-fact | direct | single | high | Table II 与 Fig.6 | false |
| V17-INT | Table II 的 120.1、1568.2-keV 行均未填 \(I_\gamma\)；有 \(\equiv100\) 的是上方 274.5-keV 行，不能转移给目标跃迁。 | experimental-fact | direct | single | high | Table II，PDF p.9；已视觉及表格坐标核查 | false |
| V17-T | GAMMASPHERE 的 1568-keV 加门时间谱，经六个 100–700 ns 拟合区间的加权均值给出 **2349.9-keV 母态** \(T_{1/2}=589(20)\) ns。 | experimental-fact | direct | single | high | Fig.7(c) 与 Sec.III B，PDF p.9/稿件 p.8 | false |
| V17-B | 作者按该 E2 衰变解释并作内转换校正，报告 \(B(E2;(19/2^-)\to(15/2^-))=0.46(3)\) W.u.；它与同一半衰期提取相关，不是额外独立寿命观测。 | experimental-fact | direct | multiple-dependent | high | Sec.IV，PDF p.13/稿件 p.12；Table III，PDF p.14/稿件 p.13；ref.[69] | false |
| V17-DEN | 本文提供了 tentative 目标对应，却未确定 \(B(E2;15/2^-_1\to11/2^-_1)\) 或 \(R_{\rm stat}^{(1)}\) 的实验值；不能把 589 ns 赋给下方 \(15/2^-\) 态。 | our-inference | direct | multiple-dependent | high | Fig.6/7、Table II/III、Sec.III B 的联合核查 | false |
| V17-SM | 对 137Ba 的 \(19/2^-_{1,2}\to15/2^-_1\)，PQM130 列 0.31/0.41 W.u.，SN100PN 列 0.01/1.19 W.u.；这些是作者理论值。 | model-result | direct | single | high | Table III；Sec.IV 关于两个理论 \(19/2^-\) 态排序的讨论 | false |
| V17-SCOPE | \(19/2^-\to15/2^-\) 是另一个 EM benchmark；初态 11/2 的 rank-2 三阶闭合链不能直接含 19/2 中间态。 | our-inference | direct | single | high | 本页选择定则推导；固定 scalar 模块的 RME 闭合约定 | false |

**级联和时间归属。**
\[
2349.9\;(19/2^-)
\xrightarrow{120.1}
2229.8\;(15/2^-)
\xrightarrow{1568.2\ {\rm(Table\ II)}}
661.7\;11/2^- .
\]
用下游 γ 触发时间谱可以测量上游 isomer 的延迟；γ 门能量本身不指定被测寿命的母态。正文明确归属 2349.9 keV。原文关于未见进一步 few-ns 寿命的陈述限定于 **2349.9 keV 以上**，不能改写成下方 2229.8-keV 态的定量寿命界。

**内转换及强度边界。** Table III 明确说明实验 \(B(E2)\) 已按 ref.[69] 的 BrIcc 处理内转换，但正文/表格未给出这里所需的数值 \(\alpha\)。因此不把缺失系数置零，也不对已校正的 0.46(3) W.u. 再套一次 ICC。目标 1568-keV 行既没有独立寿命，也没有可直接用于重新提取绝对强度的完整数值分支；能级图只画一条箭头不等于独立测得单位总支路。

**Table III 的其它核素必须分开。**

| 核素与跃迁 | 表列 \(T_{1/2}\) | 表列实验 \(B(E2)\) | 依赖/用途 |
|---|---:|---:|---|
| \(^{133}\)Te \(19/2^-_1\to15/2^-_1\) | 100(5) ns | 2.58(29) W.u. | 前人结果；本文以它调整 SN100PN 的质子有效电荷，不能把相符当作该模型的独立验证 |
| \(^{135}\)Xe \((19/2^-)_1\to(15/2^-)_1\) | 9.0(9) ns | 0.52(6) W.u. | 本文测量/提取；**不是 135Ba**，不能补入 135Ba 的 682.3-keV 分母 |
| \(^{137}\)Ba \((19/2^-)_1\to(15/2^-)_1\) | 589(20) ns | 0.46(3) W.u. | 本文测量/提取；可另列为固定模型的额外 EM 检验 |

**与 \(R_{\rm stat}^{(1)}\) 和三阶矩的关系。**
\[
R_{\rm stat}^{(1)}
=\frac{|\langle11/2^-_1\|T(E2)\|11/2^-_1\rangle|^2/12}
{B(E2;11/2^-_1\to15/2^-_1)} ,
\quad
B(11/2\to15/2)=\frac{16}{12}B(15/2\to11/2).
\]
需要的是第二步跃迁的绝对强度，第一步的 0.46(3) W.u. 不能替代。对初态 \(i=11/2\) 的三阶矩，闭合链为 \(R_{ia}R_{ab}R_{bi}\)；两个中间自旋都必须可由一个 rank-2 算符连接初态，故
\[
J_a,J_b\in\{7/2,9/2,11/2,13/2,15/2\}.
\]
\(|19/2-11/2|=4>2\)，所以 \(19/2\to15/2\) 的矩阵元不直接进入该链。它可以检验模型在其它态上的 E2 描述，但不能宣称直接验证初态 11/2 的 \(q_3\)。

## Competing Interpretations and Limitations

- 新文献消除了“没有 \(15/2^-\) 候选指认”的当前知识缺口，未消除绝对分母缺口。指认括号和系统学/理论辅助性质保留，不升级为完备谱中的无歧义最低态。
- 1568.2-keV Table II 数值与 Fig.6 的 1568.1 keV 相差 0.1 keV，在表列 ±0.5 keV γ 能量误差内；不平均、不修补原件。
- 589(20) ns 与 0.46(3) W.u. 是同一上游衰变的关联结果。只照抄作者 quoted margins，不补充置信水平或模型误差。
- 独立的 \(19/2\to15/2\) 模型比较需先固定态对应及 E2 约定。作者讨论 PQM130 两个相近理论 \(19/2^-\) 态可能交换对应，不构成事后挑选 IBFM ordinal 以贴合强度的许可。本任务没有进行该比较或重新拟合。
- 两份归档物是 accepted manuscripts；审查的关键条目一致，不声称已核对期刊排印版的每个字。物理文章年份为 2017，不能采用仓储下载/搜索更新时间作为发表年。
- 本文没有给出新的 137Ba 静态矩，也没有重放 Nomura 的 EM 或形状不变量图。既有静态-v1 结果和哈希保持不变，旧 ENSDF 检查保留为有版本界限的历史证据。

## Extracted Pages

- 相关集合 source：[[nndc-ba135-ba137-static-e2-constraints]]，已在其当前摘要中链接本次 post-ENSDF 修订。
- [Vogt2017 readiness JSON](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/vogt2017-readiness.json)与 [constraint CSV](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/vogt2017-constraints.csv)区分目标分母、其它跃迁、其它核素和作者理论结果。
- [元数据](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/vogt2017-metadata.json)、[BibTeX](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/vogt2017-citation.bib)、[有界检查脚本](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/audit_vogt2017.py)供父任务引用与复核；不把原件 PDF 或源页图复制到 article/data。
