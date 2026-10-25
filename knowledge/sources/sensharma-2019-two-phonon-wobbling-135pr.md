---
type: source
title: "Two-phonon wobbling in 135Pr"
aliases: [Sensharma 2019 135Pr, two-phonon wobbling in 135Pr]
created: 2026-07-03
updated: 2026-10-25
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Two-phonon Wobbling in 135Pr"
authors: [N. Sensharma, U. Garg, S. Zhu, A. D. Ayangeakaa, S. Frauendorf, et al.]
journal: Physics Letters B
year: 2019
volume: 792
pages: 170-174
doi: 10.1016/j.physletb.2019.03.038
arxiv:
language: en
canonical_source: doi:10.1016/j.physletb.2019.03.038
zotero_item_key:
citation_key: sensharma_2019_Twophononwobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2019_Sensharma et al_Two-phonon wobbling in 135Pr.pdf"
raw_sha256: 54F06038943DE5F980DC731266844DCFA1980F1775E47A943F77D31C256C741F
nuclei: [135pr]
reactions: [123sb-o16-4n-135pr]
experiments: [atlas-digital-gammasphere-135pr-o16-80mev]
models: [triaxial-particle-rotor-model, triaxial-projected-shell-model]
observables: [multipole-mixing-ratio, interband-e2-strengths, wobbling-energy]
methods: [gamma-gamma-coincidence, dco-ratio]
tags: [a130, 135pr, two-phonon-wobbling, gammasphere, qtr, tpsm]
---

# Sensharma 等（2019）：`135Pr` 二声子 wobbling 支持方实验

## Bibliographic Record

N. Sensharma et al., *Physics Letters B* **792**, 170-174 (2019)，DOI `10.1016/j.physletb.2019.03.038`。题名、作者、年份和 DOI 与只读 BibTeX 条目唯一匹配，使用用户指定 citation key `sensharma_2019_Twophononwobbling`。

## Scope and Reading Depth

全文精读，并视觉核对 Fig.1 的部分能级纲图、Fig.2 的三组角分布与 mixing ratio、Fig.3 的相对 E2 强度比和 Fig.4 的 QTR/TPSM 能量比较。

本页按 `experiment-ingest + project-ingest` 建立 Sensharma 2019 对 `135Pr` two-phonon wobbling 解释的支持方证据链。它不裁决后续争议，也不把 `n_w=0/1/2` 指认写成裸观测。

## Summary

作者利用更高统计量的 digital Gammasphere 数据扩展 `135Pr` 的负宇称能级结构，建立一条新序列及其到既有 TW1 候选带的 450.2、550.5、517.1、571.7 keV 四条连接跃迁。前三条最低能连接跃迁的角分布给出较大的 E2/M1 mixing ratio 和约 78%-92% 的 E2 成分。作者把新序列指认为 `n_w=2` 带，并把其 wobbling energy、自旋演化及相对 E2 强度与 QTR、TPSM 计算比较。该解释明确继承 Matta 2015 对 yrast/TW1 的 `n_w=0/1` transverse-wobbling 指认。

## Experimental or Theoretical Setup

- 80 MeV `16O` 束流轰击 `634 μg/cm²` 的 `123Sb` 靶，靶前有 `15 μg/cm²` Al 层；
- digital Gammasphere 有 83 个正常工作的 Compton-suppressed Ge 探测器，分布于 17 个角度环；
- 收集 `1.45×10^10` 个三重及更高重数 γ 符合事件，以 RADWARE 建立 γ-γ 矩阵和 γ-γ-γ 立方体；
- 角分布数据归并为覆盖 `0°-90°` 的 7 个角度环，并分别做效率修正；
- QTR 计算沿用 Matta 2015 参数；TPSM 使用独立的三轴形变输入并进行角动量投影。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| S19-1 | 实验使用 80 MeV `16O` 束流、`634 μg/cm²` 的 `123Sb` 靶和 83 个工作的 Compton-suppressed Ge 探测器；DGS 收集 `1.45×10^10` 个 fold≥3 γ 符合事件。 | experimental-fact | direct | p.171, right column, experimental setup | false |
| S19-2 | Fig.1 在既有 yrast、TW1、signature-partner 和 dipole sequences 之外建立一条新序列；该序列通过 450.2、550.5、517.1、571.7 keV 四条 ΔI=1 transitions 连接 TW1。 | experimental-fact | direct | pp.171-172, Fig.1 and surrounding text | false |
| S19-3 | Table 1 给出 450.2、550.5、517.1 keV 三条 TW2→TW1 连接跃迁的 DCO-like ratios 分别为 `0.55(3)`、`0.49(10)`、`0.37(20)`。 | experimental-fact | direct | p.171, Table 1 | false |
| S19-4 | Fig.2 对 450.2、550.5、517.1 keV 跃迁给出 `δ=-1.91(+0.04/-0.05)`、`-2.26(+0.20/-0.21)`、`-3.48(+0.31/-0.36)`，相应 E2 成分为 `78.5(+0.9/-0.7)%`、`83.6(+2.5/-2.4)%`、`92.4(+1.3/-1.5)%`。 | experimental-fact | direct | p.172, Fig.2 | false |
| S19-5 | 作者由强度与角分布所得 mixing ratio 提取 `B(E2)_out/B(E2)_in`；本文不能测量绝对跃迁概率，因此 Fig.3 给出的是相对强度比而非绝对 `B(E2)`。 | experimental-fact | direct | p.172, text below Figs.2-3 | false |
| S19-6 | 以 yrast 作为 `n_w=0` 参考时，Fig.4 中实验 TW2 wobbling energy 随自旋增加而下降。 | experimental-fact | direct | pp.172-173, Fig.4 and first paragraph below it | false |
| S19-7 | 本文采用的主要实验判据是：相邻候选 wobbling bands 由 ΔI=1、以 E2 为主的连接跃迁相连，并结合相对 interband E2 strength 与 wobbling-energy 演化判断。 | experimental-criterion | direct | pp.170-173, introduction; Figs.2-4 | false |
| S19-8 | 作者把新序列指认为 `n_w=2` two-phonon wobbling band，并把既有 yrast/TW1 分别作为 `n_w=0/1`；这是作者解释，不是能级和 γ 线存在本身。 | author-interpretation | direct | pp.170-174, Abstract, Fig.1, Conclusions | false |
| S19-9 | `n_w=2` 指认明确依赖 Matta 2015 已提出的 `n_w=1` TW1：本文以新带到 TW1 的连接跃迁及相对 yrast/TW1 的能量关系建立 phonon hierarchy。 | author-interpretation | direct | pp.170-171, final introduction paragraph; Fig.1 | false |
| S19-10 | QTR 沿用 Matta 2015 的 `ε=0.16, γ=26°`、`J_m,J_s,J_l=7.4,5.6,1.8 ħ²/MeV` 和转动惯量尺度因子 `1+0.116I`。 | model-result | direct | p.173, left column, model setup | false |
| S19-11 | QTR 给出的逐级 wobbling-phonon energy 明显非谐：在相应自旋标记下，第一声子增量约为第二声子增量的两倍，即 `E_TW1(I+1)-E_yrast(I) ≈ 2[E_TW2(I+2)-E_TW1(I+1)]`；QTR 还再现较小的 TW2→TW1 与 TW2→yrast 相对 E2 比。 | model-result | direct | pp.173-174, Figs.3-4 | false |
| S19-12 | TPSM 使用 `ε=0.17, ε'=0.12`（对应 `γ=35°`）；它比 QTR 更高估 one-phonon energy，却给出相近的相对 E2 比，并更好再现 signature-partner band energy。 | model-result | direct | p.173, model setup and right column; Figs.3-4 | false |
| S19-13 | 论文说明 TPSM 尚未完成角动量几何分析；其较大的 SP→yrast E2 比被作者解释为 one-phonon wobbling 与 signature-partner states 之间可能存在耦合，细节留待后续理论工作。 | model-result | direct | p.173, right column, final paragraphs | false |

## Nuclear Structure Information

- [[135pr-yrast-band]]：本文沿用 `n_w=0` 指认；
- [[135pr-side-band]]：本文称为 TW1，并沿用 Matta 2015 的 `n_w=1` 指认；
- [[135pr-second-side-band]]：新建立的序列，作者指认为 TW2/`n_w=2`；
- [[135pr-signature-partner-band]]：作为主要 dipole 连接的对照序列；
- [[135pr-dipole-band]]：Fig.1 中继续显示并扩展的强 dipole sequence。

## Authors' Interpretation

- 新序列为 `n_w=2` two-phonon wobbling band；
- TW2→TW1 的 ΔI=1、E2-dominated connections 和下降的 `E_wob(TW2)` 支持 transverse-wobbling 分类；
- TW1/TW2 能量与相对 E2 比偏离 harmonic limit，表明强 anharmonicity；
- 该案例被作者称为 A≈130 区首个 two-phonon wobbling 观察。

以上均为 Sensharma 2019 的支持方解释，不是本 Wiki 对 `135Pr` 争议的裁决。

## Model Results

- QTR 沿用 Matta 2015 的形变、转动惯量和自旋依赖参数，比较 TW1/TW2、yrast 与 signature-partner 能量及相对 E2 比；
- TPSM 从三轴准粒子基底投影，计算能量和 E2 ratios，但本文尚未分析其角动量几何；
- 两种模型都给出强 anharmonicity 图景，但对 one-phonon energy 和 signature-partner band 的再现程度不同。

## Competing Interpretations and Limitations

- 本文是 two-phonon wobbling 支持方原始实验；后续反对或替代解释尚未在本页摄入；
- TW2 指认不是独立于 Matta 2015 的证据链：若 TW1 的 one-phonon assignment 改变，TW2→TW1 的 phonon-order 解释也需重新评估；
- 本文没有报告 linear-polarization measurement；
- 只有三条最低能 TW2→TW1 links 给出完整角分布/mixing ratio，第四条连接跃迁未给出同等定量约束；
- 相对 E2 比由强度与 mixing ratio 推导，缺少本文独立寿命测量，不能替代绝对 `B(E2)`；
- QTR 参数沿用既有拟合，TPSM 角动量几何尚未分析，二者均不能作为独立实验事实。

## Extracted Pages

- Nucleus: [[135pr]]
- Bands: [[135pr-yrast-band]], [[135pr-side-band]], [[135pr-second-side-band]], [[135pr-signature-partner-band]], [[135pr-dipole-band]]
- Experiment: [[atlas-digital-gammasphere-135pr-o16-80mev]]
- Concepts: [[wobbling-motion]], [[transverse-wobbling]]
- Observables: [[multipole-mixing-ratio]], [[interband-e2-strengths]], [[wobbling-energy]]
- Methods: [[gamma-gamma-coincidence]], [[dco-ratio]]
- Models: [[triaxial-particle-rotor-model]], [[triaxial-projected-shell-model]]
- Project: [[135pr-wobbling-controversy]]

## Personal Notes

本页只建立 Sensharma 2019 的支持方证据链。用户已完成 source 页面和 S19-1 至 S19-13 的原文核对，未发现问题；这不构成对 `135Pr` wobbling 争议的裁决。


## Day23：新增采集、复用观测与非谐定义分别记录

本次完整回读5页主线、关键图注/输入/局限，视觉核printed171实验段及Table1、printed172 Fig1–3；raw SHA保持。原S19-1–13/人审flags不动，新条目全needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| S19-D23-1 | 本文83探测器DGS、634μg/cm²靶及1.45×10^10事件，正文明确digital升级使相近beam time取得近4倍Ref10(Matta2015)数据。这支持相对旧Matta采集的新增DGS数据，不能因共享反应/靶厚/解释链就称逐事件同一采集；具体run IDs/重叠仍缺event ledger。SH26 SecII另明确把本文数据与其新run合并，故不能将S19和SH26两整份样本当完全独立。 | acquisition-and-partial-overlap-boundary | direct-original-and-cross-source | printed171, experiment paragraph; SH26 PDF2 Sec.II | true |
| S19-D23-2 | Fig3图注明确TW1→Yrast实验值取自Ref10(Matta2015)，而本文新增TW2等比值由本次intensity/AD δ派生；新DGS acquisition并不让图上每一量都成为新测。主文还明确无absolute transition probability。须逐observable区分继承点、同源派生和新增观测，不按paper篇数或图中点数增加独立性。 | observable-reuse-and-derived-strengths | direct-original | printed172, Fig.3 caption and adjacent text | true |
| S19-D23-3 | printed171称QTR解只要保留与harmonic limit相同topology，即使定量非谐仍可用phonon标签；printed173把TW2→TW1比值小于TW1→Y的现象与strong anharmonicity联系，两个分母分别是各自band origin的in-band E2。此作者定义不等于要求exact factor2，也不凭relative ratio自动证明完整拓扑/实测声子。 | author-definition-and-normalizer-boundary | direct-original | printed171, topology paragraph; printed173, Fig.3 discussion | true |

Knowledge Impact and Learning Decision：supports保留真实新增DGS支持链，limits对全部观测独立性的二元计票和把harmonic比例当唯一模式定义。[[low-spin-wobbling-controversies]]与[[135pr-wobbling-controversy]]按run/observable/模型依赖分别组织，不作最终归属。


### Day23：旋称分类与激发带身份

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| S19-D23-4 | printed171分别定义odd-n_w wobbling序列的opposite signature与另一个unfavoured SP；后者可存在于轴对称/三轴情形，wobbling候选在三轴时额外出现。两者可共享相对yrast相反的α，故α分类本身不唯一指定ordinary SP或wobbling，也不等于pseudospin。 | author-classification-and-identification-boundary | direct-original-and-bounded-inference | printed171, spin-sequence and unfavoured-signature paragraphs | true |
