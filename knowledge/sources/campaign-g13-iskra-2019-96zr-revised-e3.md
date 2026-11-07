---
type: source
title: "Iskra等2019：96Zr 3-态B(E3)跃迁几率修订与MCSM微观结构（PLB）"
aliases: ["Iskra 2019 PLB 96Zr revised B(E3)", "PLB 788 396", "10.1016/j.physletb.2018.10.069"]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Revised B(E3) transition rate and structure of the 3− level in 96Zr"
authors: ["Ł. W. Iskra", "R. Broda", "R. V. F. Janssens", "M. P. Carpenter", "B. Fornal", "T. Lauritsen", "T. Otsuka", "T. Togashi", "Y. Tsunoda", "W. B. Walters", "S. Zhu"]
journal: Physics Letters B
year: 2019
volume: 788
pages: 396–400
doi: "10.1016/j.physletb.2018.10.069"
canonical_source: "https://doi.org/10.1016/j.physletb.2018.10.069"
citation_key: ""
raw_file: raw/papers/gpt/query/20261107-campaign-G13/iskra-2019-96zr-revised-e3.pdf
raw_sha256: 59c772991a381100f31f1edca6aefc72bef0c95cd8ef2cb2ea7bf37f9e429cca
archive_required: true
nuclei: ["96zr", "90zr", "92zr", "94zr"]
tags: ["octupole", "e3-transition", "gammasphere", "coincidence-branching", "mcsm", "zr96"]
---

# Iskra等：96Zr E3修订与多轨道集体性

## Bibliographic Record

Ł. W. Iskra et al., PLB788(2019)396–400，DOI10.1016/j.physletb.2018.10.069。
实际5页CC-BY出版原件，2018-11-30在线，卷年2019；不以DOI年替代卷年。

## Scope and Reading Depth

### Covered scope

全文5页、Tables1–2、Figs1–2；总控另回读寿命/分支段、Table1脚注、MCSM讨论和结论。

### Not covered

未重新分析六套事件或取得MCSM波函数/作者代码；Horen1993等历史文献的详细方法
在本页只按Iskra转述，不能声称已重做或证实其所有系统误差。

## Key Results

| ID | 原件支持内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| IS19-1 | 本文采用Horen1993的T1/2=67.8(43)ps；并报告历史加权值66.2(40)ps在误差内相容，不是本次新测寿命 | experimental-fact, adopted-input | direct-report + secondary-lifetime | printed397/PDF2 | false |
| IS19-2 | 六套Gammasphere资料，用3−上方级联门比较1897.2与1750.4keV；归一后先13.0(3)、求和修正后12.8(3) | experimental-fact | direct | PDF2–3 Fig1/Table1 | false |
| IS19-3 | 12.8(3)相对1750.4-keV线=100，不是占全部退激12.8%；按作者处理得到E3部分半衰期.60(4)ns | experimental-fact | direct | PDF3 Table1与右栏 | false |
| IS19-4 | 报告向下B(E3;3−→0+)=23(2)×10³ e²fm⁶及42(3)W.u.；仍为强集体，但低于当时汇编 | experimental-fact, derived-strength | direct | PDF3 | false |
| IS19-5 | 本文MCSM给B(E3)=46.6W.u.；大空间中质子/中子多种跃迁共同贡献，原文说各轨道矩阵元同相 | model-result | direct | PDF4–5 Table2 | false |
| IS19-6 | 作者据新结果认为96Zr不再具有先前“异常强度”地位，并提出90Zr值得进一步测量 | author-interpretation | direct | PDF1摘要、PDF5结论 | false |

## Experimental Method and Dependence

六种反应资料与Mach1990的β快定时采集不同；本工作测分支，并采用另一论文寿命。
Table1三列门方案部分共享计数，作者明确在误差中考虑相关，不能当18份独立数据。
比较两个高能线可减轻跨大能区效率/定时问题，利用后续1750-keV级联间接包含
146.6-keV E1转换通道。门控与求和改进不表示一切本底/feeding系统误差被数学上消灭。

## Units and Interpretation Boundaries

普通A=96 Weisskopf参考1.2^6 A²/(16π)约547.47 e²fm⁶，
23×10³对应中心约42.01W.u.。从已舍入的±2×10³传播会得约3.65W.u.，
不能声称它“严格舍入”为作者报告的±3；两个原文打印误差分别保留，
未取得未舍入拟合量时不制造更精确的一致性认证。
反向0+→3−的绝对B为向下的7倍；比较W.u.须明确所用参考约定，
不默换方向相关归一以声称数值必相同。

## Summary

本次以真实出版原文把N=56比较推进到2019修订E3。42(3)W.u.仍为强集体，
历史参照的改变不独立裁决静态/动态形状或所有模型。

## Competing Interpretations and Limitations

MCSM的轨道贡献是作者模型分解，不是占据概率或独立实验测得的质子/中子强度。
大空间相干支持该计算的振动集体解释，但一个强度接近不能唯一排除所有内禀形变模型。
Mach1990是历史直接报告，不能把其PES解释写成被一项新B完全否定的静态形变确证。
早期寿命的差异没有在此逐一追定原因，不将讨论低能γ测量的time-walk泛化为
已证明Mach寿命因延迟馈送偏小。

## Knowledge Impact and Learning Decision

`revises + provisional research-note`：[[campaign-g13-zr96-revised-e3-20261107]]。
本轮N=56比较改用这份已核2019报告42(3)W.u.作为更新参照，并保留历史65(10)。
没有认证2026 NNDC现时采用值或穷尽此后全部测量。

## Agent Self-audit Triage

P0: none identified in source identity/hash。P1：总控纠正相对强度/总分支、
历史寿命因果、误差舍入和静态形状排他推断。没有由本论文生成无计算的90Zr≤18W.u.预报。

## Extracted Pages

5页出版PDF，关键直接证据printed397–400。
