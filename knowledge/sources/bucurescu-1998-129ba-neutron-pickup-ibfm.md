---
type: source
title: "Bucurescu 1998：129Ba 中子拾取强度与多壳层 IBFM"
aliases: [Bucurescu1998 Ba129 transfer, 129Ba polarized deuteron transfer]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-model-comparison
reading_depth: read
title_original: "Single particle excitations in 129Ba from a (d, t) reaction study"
authors: [D. Bucurescu, J. Ott, W. Schauer, T. von Egidy, A. Gollwitzer, R. Hertenberger, A. Metz, G. Graw, B. D. Valnion, R. Meunier, D. Le Du]
journal: Nuclear Physics A
year: 1998
volume: 630
pages: 643-660
doi: 10.1016/S0375-9474(98)00804-5
canonical_source: https://doi.org/10.1016/S0375-9474(98)00804-5
citation_key: Bucurescu1998Ba129
citation_key_origin: task-bibliography-in-ba129-model-readiness
raw_file: raw/papers/gpt/query/20261105-ba129-model-readiness/bucurescu1998-main.pdf
raw_sha256: 13461f44e44bf7ff224c260e0bce83c3180d1864cc56e382778248b819f7ee8d
archive_required: true
nuclei: [129ba, 130ba]
models: [interacting-boson-fermion-model]
methods: [polarized-neutron-pickup, dwba]
observables: [spectroscopic-strength, spin-parity, electromagnetic-branching]
tags: [a130, transfer, gamma-softness, multiorbital, holdout]
---

# 129Ba 转移强度提供不同于能谱的波函数约束

## Summary

偏振(d,t)实验与多壳层IBFM比较提供独立于重离子γ谱采集的低能态组分信息。
强度为相对归一，原文没有逐点误差；有效转移算符和γ衰变探测不同组分，
不能把两类观测量或两套表格归一当成重复的独立证据。

## Bibliographic Record

出版商 FULL XML、TUM 机构题录和18页PDF的题名、作者及卷页相符。
正文由 XML 明列 MAIN attachment 的授权接口取得。完整获取清单为
`raw/papers/gpt/query/20261105-ba129-model-readiness/manifest.json`。

## Scope and Reading Depth

已读18页全文主线；核实验方法、Tables 1–3、IBFM模型/算符来源、正负宇称
讨论及结论。视觉核printed pp.647、653的关键表格及p.657–659讨论；
未重新提取全部角分布点、未复现CHUCK或ODDA/PBEM/SPEC。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BU98-1 | 25-MeV偏振氘束、130Ba靶、Q3D测量了低能态转移角分布和分析本领；它是与重离子γ谱不同的实验观测。 | experiment | direct-original | pp.645–646 §2 | true |
| BU98-2 | 靶厚不确定，转移强度只给相对标度。Table1以1/2+基态为1；Table2另以7/2+首态为1，两归一不能当独立测量。 | normalization | direct-original | pp.647–648 Table1/正文；p.653 Table2 | true |
| BU98-3 | Table2的9/2−与11/2−实验强度为0.07、1.33，IBFM列为0.006、1.77；没有该表逐值误差或协方差。作者总体评价模型较好，不能省略这一局部残差。 | reported-data-and-model | direct-original-visually-checked | p.653 Table2；p.659结论 | true |
| BU98-4 | 转移计算沿用1991年模型参数，transfer operator来自映射；作者称部分具有预测性，并非所有波函数、选带和EM参数都仅由本任务能量拟合独立确定。 | calibration-lineage | direct-original | p.652 §3.2；p.659 | true |
| BU98-5 | 原负宇称空间含h11/2、f7/2、h9/2；附加计算因ODDA最多五壳限制使用另一个含f5/2、p3/2、p1/2的空间。不是同时包含全部负宇称轨道的一次计算。 | model-space | direct-original | p.652 §3.2 | true |
| BU98-6 | 拾取强度探测与130Ba基态相连的组分；γ衰变还探测耦合核芯激发态的较大组分。作者同时保留能量与强度分布的偏差。 | observable-complementarity | direct-original | pp.654–659 | true |

## Competing Interpretations and Limitations

由Table2中心值直接相除，实验 \(G_{9/2}/G_{11/2}=0.05263\)，模型
为0.003390。两者相差约15.5倍是**打印数值的比较**，不是显著性、
原始截面比或h9/2混合概率。DWBA、归一、占据因子和有效转移算符不可略去。

严格单j空间配合裸单粒子转移算符有角动量选择限制；多步反应和核芯辅助的
有效转移算符可能改变该限制。因此此表不能直接排除所有h11/2主导描述，
也不能仅凭比值把某个wobbling候选改判为其它模式。

## Knowledge Impact and Learning Decision

`revises`：对129Ba增加γ-soft IBFM或复现能谱本身不构成新方向，已有直接先例。
`motivates`：研究可检验问题应收紧为转移约束与电磁预测能否由同一态对应及算符
同时描述。不能把用于校准的转移量再作为holdout；现代摆动候选的高自旋态亦
不能按相近能量与本低自旋转移峰直接对应。

## Extracted Pages

- [[ba129-model-input-and-holdout-contract]]
- [[ba129-rank4-identifiability]]
- [[129ba]]

## Human Review

以上为直接原件核查和本任务推断；没有human review或最终paper admission。
