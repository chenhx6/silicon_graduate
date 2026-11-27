---
type: source
title: "Engel–Menéndez 2017：0νββ 核矩阵元、闭合与有效流"
aliases: [Engel Menendez 2017 NME review]
created: 2026-11-08
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: review-article
reading_depth: read
title_original: "Status and future of nuclear matrix elements for neutrinoless double-beta decay: a review"
authors: [Jonathan Engel, Javier Menéndez]
journal: Reports on Progress in Physics
year: 2017
volume: "80"
pages: "046301"
doi: "10.1088/1361-6633/aa5bc5"
arxiv: "1610.06548"
citation_key:
canonical_source: "doi:10.1088/1361-6633/aa5bc5"
raw_file: "raw/papers/gpt/query/20261108-r3-g48-weak-operators/engel-menendez-2017-rpp-0nubb-nme.pdf"
raw_sha256: "813111c10bab58d8d0f19ca91833383a8a521a33c0434b276eacd4fead195417"
archive_required: true
nuclei: [136xe]
tags: [doctoral-foundations, double-beta, effective-operators, closure]
---

# 从单 β 的有效强度到双 β 的不同动量核

## Bibliographic Record

35物理页预印本；书目由官方Crossref核定，记录见R3 bibliography-audit集合。
本地文件不冒称期刊排版版，以下页码均为实际PDF页。

## Scope and Reading Depth

G48定向学习，T07与总控独立核PDF4、17–18；前者检查
Eqs.(6)–(10)的中间态和单核子流，后者检查淬灭、两体流及Figs.11–12。
不是对全综述逐式重推，也不是2017以后全部进展的盘点。

## Summary

该综述比较0ν核矩阵元方法、闭合与有效流。本轮仅以已核页说明不同弱过程的动量和空间条件。

## Key Results

| claim | claim_kind | evidence_level | locator | boundary |
|---|---|---|---|---|
| 闭合用代表性能差替换中间态分母，再利用完备性 | review-theory | located-review | PDF4, Eqs.(6)–(10) | 大动量给近似动机，不是误差为零 |
| CVC给自由核子流所用的gV(0)=1 | review-theory | located-review | PDF4, Eq.(8) | 不推出有限空间每个矢量算符均无修正 |
| 单β淬灭的来源及高动量两体流修正具有方法依赖 | review-synthesis | located-review | PDF17–18, Figs.11–12 | 文中若干20%/30%计算例子不作普适定值 |

## Competing Interpretations and Limitations

有限空间、态相关、有效算符和两体流须共同记账，不能把一个标量q无条件乘到所有过程。
该综述不是新测量；其引用的计算与后续讨论存在来源依赖。
0ν过程的轻Majorana交换范围与其他轻子数破坏机制分开。

## Extracted Pages

- [[doctoral-r3-weak-operators-and-delayed-particles-20261108]]

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理页1–8，题页、I 引言及 II 双β衰变的意义，含轻中微子交换、闭合、其他机制及实验对核矩阵元的依赖。
- 物理页8–15，III 核矩阵元计算现状，含壳模型、QRPA、EDF/GCM、IBM、其他方法及方法间比较。
- 物理页15–18，IV 轴矢耦合淬灭，含单β与双β、荷交换证据、遗漏的多体关联和两核子流。
- 物理页19–26，V 改进现有模型、从头算与有效算符、误差评估，以及 VI 总结展望和致谢。
- 物理页27–35，参考文献 [1]–[311]。
- 本次获取的具体覆盖：通读物理页1–35的带页标抽取文本，覆盖正文、致谢和参考文献表。图的证据来自可读图注和正文，图像与公式版式均未经目视核验。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A22-1 | 轻马约拉纳中微子交换推导以约100 MeV的典型动量解释闭合近似。将分母中的中间态能量换成与态无关的平均值后，可用完备性求和。所引检验在适当选取平均能量时给出约10%以内的差异，检验未覆盖高于数十 MeV 的中间态。冲量近似中，自由单核子矢量流依矢量流守恒取 gV(0)=1。 | 理论推导与所引计算检验 | source-reported | 物理页4，II B 1，式(6)–(7)及闭合段、式(8)后正文，文献 [45]–[49]。公式符号与版式待核物理页4。 | true |
| A22-2 | 综述转述的荷交换实验中，约50 MeV以下提取的 GT⁻ 积分强度通常约为 Ikeda 和规则右端 3(N−Z) 的一半。更高激发能处的自旋–同位旋强度仍难与背景区分。 | 所引实验观察 | source-reported | 物理页15–16，IV A，式(20)及其后荷交换讨论，文献 [207]、[209]、[214]–[215]。 | true |
| A22-3 | ¹³⁶Xe 的壳模型与 QRPA 单体流计算给出相近的 GT 动量分布，QRPA 分布偏向较高动量。综述举例称，加入两核子流后，壳模型与 QRPA 的 0νββ 核矩阵元分别降低约30%和20%。QRPA 的例子还重新拟合了等标量配对强度，以维持对 2νββ 的描述。 | 所引模型结果 | source-reported | 物理页17，IV B，图11及图12，曲线、阴影与图元待核该页。物理页18，IV B，两核子流计算讨论，文献 [217]–[218]。 | true |
| A22-4 | 综述用未淬灭 gA 的多种模型比较说明当时 0νββ 核矩阵元约有两至三倍的差异。作者指出，各方法可能共同遗漏重要物理，模型间散布因此不足以给出定量不确定区间。 | 综述比较与作者解释 | source-reported | 物理页8，III 开头正文及图5图注。物理页25，V D 开头的误差讨论。 | true |

闭合误差来自综述引述的闭合与非闭合比较。图11汇编文献 [217] 的壳模型和 [218] 的 QRPA 结果，两核子流降幅也取自这两项工作。荷交换强度来自综述转述的实验。引用链仅核到本稿参考文献表。

- 在 Wiki 增记本地版本 arXiv:1610.06548v2，分列页边版本日期、题页署期和期刊年份。046301 记作期刊文章号，35 记作本地 PDF 物理页数。
- 将闭合机制的宽泛定位式(6)–(10)收紧为物理页4式(6)–(7)及闭合段。将 gV(0)=1 定位到式(8)后正文，保留自由单核子流的限定。
- 将图11、图12都精确定位到物理页17，约30%和20%的降幅定位到物理页18正文。图11的两体流阴影仅对应壳模型，图12给出 χEFT 两核子流的示意。
- 物理页3式(5)的绝对值线在抽取中脱落，正文明确要求取模。物理页5式(11)的平均能量记号和张量项自旋下标可疑，式(12)的归一化须连同式(10)–(11)回页核对。物理页22的耦合簇展开与式(23)的系数、上下标和算符字符也应回页后再转录。
- 物理页6将约138 MeV与约1.4 fm⁻¹并列，换算存疑，暂仅保留约138 MeV。物理页10图6及物理页16图10的抽取混入被引原图的编号和图注片段，采用综述图号，拟合数值与指数待回页。物理页24图14的抽取标签出现 ²²O、²³O、²⁴O，图注却称两个同位素，回页核对后再写数量。
