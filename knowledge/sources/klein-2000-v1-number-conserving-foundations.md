---
type: source
title: "Klein 2000 v1：数守恒框架与附录迭代式边界"
aliases: [Klein2000 particle rotor foundations v1]
created: 2026-11-06
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: theory-preprint
reading_depth: read
title_original: "Foundations of self-consistent particle-rotor models and of self-consistent cranking models"
authors: [Abraham Klein]
year: 2000
arxiv: nucl-th/0004051v1
canonical_source: https://arxiv.org/abs/nucl-th/0004051v1
citation_key: Klein2000FoundationsV1
citation_key_origin: task-primary-source-audit
raw_file: raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-v1.pdf
raw_sha256: 8dc1b32a948f542dee9ed6488a17015dd27b01bd2c8b6bb3ad79c2c6aa688461
archive_required: true
models: [core-particle-coupling, particle-rotor-model]
tags: [pairing, particle-number, cfp, source-consistency, iteration]
---

# 约束框架不等于固定矩阵的态选择器

## Bibliographic Record

所读为2000-04-23的arXiv v1，共29页；原TeX亦已归档。
对应PRC63,014316(2001)的最终版未核读，以下问题不外推到最终版。

## Scope and Reading Depth

定向读§II及AppendixA；视觉核PDF25–27，比较TeX原式。未复现全文模型。

## Summary

CFP连接同一奇核与A±1偶核，包含数目、归一和自洽约束；
不能以任意Nambu坐标扇区权重替代。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KL-1 | V/U分别为到两邻偶核的移除/添加振幅；数目和轨道分辨归一是额外约束。 | formalism | direct-original | pp.4–7，Eqs2.9–2.10、2.24–2.28 | true |
| KL-2 | 按v1字面定义，A13乘√Λ把A12的范数变成Λ²Ω；未完成所称归一。 | source-consistency | original-plus-task-algebra | p.25，A12–A13 | true |
| KL-3 | A18/A21不能一般推出A22；A23及A25–A26的更新不满足所述投影切空间条件。 | source-consistency | original-plus-exact-counterexamples | pp.26–27，A18–A28 | true |

## Competing Interpretations and Limitations

30项有理数矩阵检查支持上述局部反例；不是对整个KK框架的否定。
没有验证勘误或最终期刊版，不把该迭代直接写入求解器。
详见[[ba129-core-and-pairing-validity]]；检查回执位于本轮`klein-review/`。

## Extracted Pages

- [[ba129-core-and-pairing-validity]]
- [[paired-single-j-positive-bcs-rotor]]

## Human Review

Codex选段与数学self-audit，非human-reviewed。

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1–3页，题名页、摘要、§I 引言
- 物理第4–7页，§II 运动方程与变分原理
- 物理第7–13页，§III 轴对称强耦合粒子–转子模型
- 物理第13–17页，§IV 轴对称替代推导与推转极限
- 物理第17–22页，§V 三轴转子与推转极限
- 物理第22–24页，§VI 总结与讨论
- 物理第24–27页，附录 A 与迭代方案
- 物理第28–29页，参考文献 [1]–[40]
- 本次获取的具体覆盖：逐页读取物理第1–29页的抽取文本，覆盖正文、附录 A 和参考文献。公式核算集中在附录的归一化与投影更新。给定文本无编号图表或图表题注，公式版面待核。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A19-1 | CFP 的 V 对应从较重偶核移除粒子，U 对应向较轻偶核添加粒子，两者连到同一奇核。变分框架包含邻偶核粒子数约束，以及总归一化和逐轨道归一化。 | 理论框架 | source-reported | 物理第4–7页，式（2.9）–（2.13）、（2.18）–（2.20）、（2.24）–（2.30）。第4页的邻核横线及第5、7页的模方符号须核对原页后逐字转录。 | true |
| A19-2 | 轴对称替代推导取单粒子与集体角动量之比的最低阶，所得粒子–转子近似仍保角动量。再以推转振幅和角频率作替换时舍弃严格角动量守恒，保留粒子数守恒。作者给出的轴对称倾轴情形关联非零 K，三轴模型允许三维推转。 | 模型推导 | source-reported | 物理第15–17页，式（4.19）–（4.33）及相邻正文；第21–23页，式（5.37）–（5.45）及 §VI。 | true |
| A19-3 | 按抽取文本中 A12 的定义，A13 乘以 √Λₐ 后，逐轨道范数由 ΛₐΩₐ 变为 Λₐ²Ωₐ。若 Λₐ>0，使该范数等于 Ωₐ 的缩放因子为 1/√Λₐ；Λₐ=0 时单纯缩放无法补回范数。 | 原式一致性核算 | source-reported | 物理第25页，式（A12）–（A14）；须核对 A13 根号下的因子和 A14 的势重标度。 | true |
| A19-4 | 令 P=R/Ω、Q=1−P，则 A18 给出 H=Ω(PΘP−QΘQ)，可推出 A15 和 A21 的对易关系。A22 仍需额外条件。A25 的残差 Y=QHQ−PHP 一般有对角块，而 A27 要求 PδRP=QδRQ=0，因此 A26 一般无法保持一阶幂等性。 | 原式一致性核算 | source-reported | 物理第24页式（A8），第26页式（A15）、（A18），第27页式（A21）–（A28）。第26页核对 A18 的符号，第27页核对反对易号及 Ω 因子。 | true |

既有笔记与本次归档原件的版本和散列一致。建议接受其 §II 与附录 A 的同版定向覆盖，其余章节的文本覆盖以本回执为据。附录公式逐字入库前应核对所列原页。既有笔记所述 TeX 对照、视觉检查和三十项矩阵检查属于此前工作。

- KL-2 保留对 v1 字面归一化的判定，并补写 Λₐ>0 时的倒根号缩放。若第25页原式确认，A14 中该势的相应双线性因子应为 1/√(ΛᵦΛ_d)。
- KL-3 分开写两处问题。第26–27页的 A18/A21 到 A22 缺少条件，A23 属于由此得到的方程。第27页 A25–A26 才定义残差更新，须用 A27 的两个对角块条件检验；A28 只检查其中一块。
- 物理第2页 [17–21,?] 的问号保留为待查引文。第28页 [18] 的 Fauendorf 拼写及 [22]、[24] 中出现的 bf 须对原页辨明后再录入。
