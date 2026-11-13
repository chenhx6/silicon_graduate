---
type: source
title: "Dewald et al. 2012 - Developing the Recoil Distance Doppler-Shift technique"
aliases: [Dewald 2012 RDDS DDCM review, DDCM review]
created: 2026-11-13
updated: 2026-11-13
status: active
review_status: unreviewed
source_type: journal-article-review
reading_depth: skimmed
title_original: "Developing the Recoil Distance Doppler-Shift technique towards a versatile tool for lifetime measurements of excited nuclear states"
authors: [A. Dewald, O. Möller, P. Petkov]
journal: "Progress in Particle and Nuclear Physics"
year: 2012
volume: "67"
issue: "3"
pages: "786–839"
doi: "10.1016/j.ppnp.2012.03.003"
canonical_source: "https://doi.org/10.1016/j.ppnp.2012.03.003"
citation_key: "dewald-2012-ddcm-recoil-distance"
raw_file: "raw/papers/2012_Dewald et al_Developing the Recoil Distance Doppler-Shift technique towards a versatile tool for lifetime measure.pdf"
raw_sha256: "5c17814e531c70f151b8d183206f902b7c8f7168e977cb2118da9df05668db20"
raw_storage_status: archived-local
archive_required: true
actual_read_pages: [1, 3, 4, 5, 6, 7, 37, 38, 39, 40]
actual_read_scope: "总控定向核PDF1身份、3–7页基本方法相关段、37–40页DDCM；PDF38/39作页面图像核查，PDF40核直接与间接门的Eqs30–34。不表示54页全文通读，旧伪引文已撤回。"
nuclei: []
reactions: [fusion-evaporation, deep-inelastic, coulomb-excitation]
experiments: [plunger, gammasphere, gassp, euroball]
models: [rdds, ddcm, doppler-shift]
observables: [lifetime, reduced-transition-probability, b-e2, b-m1]
methods: [differential-decay-curve-method, recoil-distance-method, gating-from-above]
tags: [RDDS, DDCM, plunger, lifetime, DSAM, Doppler-shift, nuclear-structure]
---

# RDDS与DDCM：先规定计数、门和距离，再谈寿命

## Bibliographic Record

A. Dewald、O. Möller、P. Petkov，Progress in Particle and Nuclear Physics 67 (2012) 786–839，
DOI 10.1016/j.ppnp.2012.03.003。所存出版PDF共54物理页、4,713,767字节，
实际路径与SHA见frontmatter；总控核了PDF首页身份与原件哈希。

## Scope and Reading Depth

本轮为定向选读：PDF3–7的基本RDDS相关段、PDF37–40的数据分析。
总控视觉核PDF38–39／印刷823–824，并在PDF40／印刷825核Eqs.(30)–(34)。
未重算装置模拟、全部去取向处理或全部测量案例。旧稿将直接移位馈送门公式
定位到PDF38–39并给出不实引文，现予撤回；不改变历史用户审核记录。

## Summary

RDDS把反冲核运动与核态退激时间联系起来。DDCM使用随距离变化的峰强度与导数，
在选定的馈送和归一条件下提取寿命。其优势来自可测的局域衰变曲线关系，
不是任意上方门都能自动消除全部实验系统误差。

## Key Results

| ID | 原件报告或方法关系 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| C-DEWALD-01 | 单谱中，作者的N_i(t)是t之后的累计退激数，不是瞬时布居n_i(t)。Eq.(19)给tau_i=[−N_i+sum b_ki N_k]/N_i'。换成实际gamma衰变曲线R_i时，Eq.(20)还含各线的相对响应因子alpha_ki，Eq.(21)给其角分布和效率关系。 | formal-method | direct-original | PDF38／印刷823，Eqs.(19)–(21) | false |
| C-DEWALD-02 | 对紧邻馈送B的移位分量B_s设门，在所定义的同级联强度下，tau_i={B_s,A_u}/[v d{B_s,A_s}/dx]。这不是任意上方间接门均可无修正使用的公式。 | formal-method | direct-original | PDF40／印刷825，Eqs.(32)、(34) | false |
| C-DEWALD-03 | 较上方的间接门C_s还需扣除后续直接馈送的相应项，并处理响应归一；不能把直接B_s公式搬给所有上门。 | formal-method-and-boundary | direct-original | PDF40，Eqs.(30)、(33)；PDF39，Eq.(29) | false |
| C-DEWALD-04 | 两光子强度的时间区间与先后次序属于定义的一部分。总符合强度固定时的导数恒等式，不等于移位门事件总数随距离固定。 | definition-and-task-boundary | direct-original-plus-inference | PDF39，Eqs.(24)–(29)；PDF40的直接门推导 | false |
| C-DEWALD-05 | DDCM理想关系可只依赖相对距离；常数零点偏移不改变同一点对应的强度/导数比。实际仍需相对距离精度、速度、峰分解及响应修正。 | explicit-method-advantage-and-boundary | direct-original-plus-inference | PDF37／印刷822，Sec.7.1；PDF40，Eq.(34) | false |

## Method and Notation Mapping

为与论文正文统一，若把能级i的所有出口在停止时刻之后的累计发射数记为U_i，
之前记为S_i，并用相同布居归一，则作者式(19)可改写为

$$
\tau_i=\frac{U_i-\sum_kb_{ki}U_k}{v\,dS_i/dx}.
$$

这是定义转换后的关系，不是把原文的R_i直接当作未经修正的任意光子峰面积。
不同出口的分支、效率与角响应应先处理；见原式(20)–(21)。

对直接馈送的移位门，令I_ss={B_s,A_s}、I_su={B_s,A_u}，原式(34)为

$$
\tau_i=\frac{I_{su}(x)}{v\,dI_{ss}(x)/dx}.
$$

I_ss+I_su一般随x改变。若改用每距离门峰面积作归一，求导时必须保留归一因子随x的变化。
即使在另一个固定总yield定义下有dS/dx=−dU/dx，带馈送时仍不能因此省去寿命公式的馈送项。
本任务的速率方程重构和两态例子见
[[a130-rewrite-forward-observables-and-cascade-consistency-20261113]]第7项。

## Competing Interpretations and Limitations

上门必须足够纯净，并选择论文假设的馈送路径；双峰重叠、未解析旁路、有限速度分布、
箔内退激及角响应都会影响实际提取。直接门和间接门的公式与修正不同。
“只需相对距离”是所述DDCM关系的性质，不应扩展成所有RDDS分析均不关心距离校准。

## Extracted Pages

- PDF1：文章身份；PDF3–7：基本RDDS定义与相关实例的定向段落。
- PDF37：DDCM优势及敏感区讨论。
- PDF38：单谱Eqs.(19)–(21)、Fig.41与门选说明。
- PDF39：时间区间定义和一般符合式。
- PDF40：直接/间接移位门Eqs.(30)–(34)，以及导数拟合讨论。

## Parent Source Reconciliation

2026-11-13：依据原PDF更正页码、计数定义、响应归一和直接门公式；撤回旧稿的
非逐字引文与“彻底消除所有侧馈偏差”“国际金标准”式无条件判断。
这是智能体的直接证据自审，不是新增human-reviewed事件。
