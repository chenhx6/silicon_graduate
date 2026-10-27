---
type: source
title: "Emediato1997：133Ce RDDS寿命、B值与三准粒子带"
aliases: [Emediato 1997 133Ce lifetimes, 133Ce RDDS 1997]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: experimental-lifetime-paper
reading_depth: deep-read
title_original: Lifetime Measurements in 133Ce
authors: [L. G. R. Emediato, M. N. Rao, N. H. Medina, W. A. Seale, S. Botelho, R. V. Ribas, J. R. B. Oliveira, E. W. Cybulska, F. R. Espinoza-Quinones, V. Guimaraes, M. A. Rizzutto, J. C. Acquadro]
year: 1997
journal: Physical Review C
volume: 55
issue: 4
pages: 2105–2108
doi: 10.1103/PhysRevC.55.2105
canonical_source: https://doi.org/10.1103/PhysRevC.55.2105
citation_key: ""
raw_file: raw/papers/1997_Emediato_133Ce_Lifetime_Measurements.pdf
raw_sha256: 39f6d6a7bb4e2da109504aaab2c22c52fa8b1465b860c1dfd58937bc404869df
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-emediato1997-ce133-rdds-072/publisher-direct-pdf.pdf
nuclei: [133Ce]
reactions: [120Sn-16O-3n-133Ce]
experiments: [recoil-distance-lifetime-133Ce-1997]
models: [particle-plus-triaxial-rotor, Donau-Frauendorf-geometry, IBFM]
methods: [recoil-distance, simultaneous-shifted-unshifted-fit, lifetime-to-transition-probability]
observables: [mean-lifetime, B(M1), B(E2), B(E1), level-scheme]
tags: [133Ce-analysis-blueprint, lifetime-network, rd-ds, three-quasiparticle]
---

# 133Ce寿命网络中的时钟、跃迁和模型边界

## Bibliographic Record

L.G.R.Emediato等，*Physical Review C*55(4)(1997)2105–2108，DOI10.1103/PhysRevC.55.2105。072经APS正式PDF入口取得4页、102259bytes、SHA见frontmatter；本文为120Sn(16O,3n) 70MeV的RDDS寿命primary，不是ENSDF数值转录。SI入口未识别补充材料，原件暂tmp，raw未归档。

## Scope and Reading Depth

全文4页、全部Table II/III、Fig1–2和方法/讨论已读及视觉核。未取得raw counts、逐线响应核、完整Cov、ICC表或作者producer，未运行新拟合。原文primed recall与access receipt在run workers目录。

## Summary

本文报告平均寿命τ：11/2−→9/2−为76(3) ps；现代ENSDF的52.7(2.1) ps是乘ln2后的半衰期。其余负带低态给7.9(.5)、3.8(.8)、≤1 ps，正宇称三准粒子态给5.3(.6)、4.5(.5)、5.3(.6) ps；不能把≤1当精确中心或把同核所有态都覆盖。B(M1)提取使用纯M1假设，双重放置/ICC/协方差缺口需保留。

## Experimental Setup and RDDS Contract

反应120Sn(16O,3n) 70MeV；HPGe+NaI、约1.0mg/cm² Sn靶、薄Au背衬、约20mg/cm² Pb stopper、13个20–250μm距离、d0=22.5(1.0)μm。Au279keV线作距离归一；LIFETIME同时拟合14条跃迁的shifted/unshifted衰变与生长曲线，含固角、alignment、slowing和一步sidefeeding修正。340点、22参数、reducedχ²2.1；无原始计数/完整Cov/逐线ICC/producer，不能重建新CI或B。

## Key Results

全部新claims needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EM97-D24-001 | 本文为120Sn(16O,3n) 70MeV的RDDS，给13个距离和d0=22.5(1.0)μm；不是DSAM/DDCM无feeding。 | direct-experiment-and-method | direct-original | PDF1–2/2105–06; Fig1 | true |
| EM97-D24-002 | 14条跃迁衰变/生长曲线共340点/22参数共同fit，含shift/unshift、固角、取向、slowing和sidefeeding；fullCov/rawkernel未交。 | fit-readiness-boundary | direct-original | PDF2/2106; PDF3/2107 | true |
| EM97-D24-003 | Table II原报meanτ：170keV 11/2−→9/2− 76(3)ps；ENSDF52.7(2.1)ps为ln2转换的T1/2，不能反写原τ。 | clock-definition-and-evaluation-crosswalk | direct-original-plus-evaluation | PDF3 TableII; [[nndc-2011-133ce-low-level-reference-records]] N133CE11-D24-004 | true |
| EM97-D24-004 | 13/2−τ7.9(.5)、15/2−τ3.8(.8)、17/2−/19/2≤1ps；双重放置385/235，B(M1)按纯M1假设。 | negative-band-lifetime-and-B-boundary | direct-original | PDF3 TableII | true |
| EM97-D24-005 | 正宇称17/2+、19/2+、21/2+τ分别5.3(.6)、4.5(.5)、5.3(.6)ps；15/2+头未得，负三qp仅<1ps。 | three-quasiparticle-clock-ledger | direct-original | PDF3 TableIII | true |
| EM97-D24-006 | PTR/geometry/IBFM比较同时有E2支持和M1偏差；PTR小γ≈−5°、signature约−30°是本1997模型输入/解释，不是现代producer或γrigidity。 | model-result-and-boundary | direct-original | PDF2–4 TablesII–III/Fig2 | true |
| EM97-D24-007 | 几何图用νh11/2[541]9/2−字面，不能擅改现代[514]；PTR λ50.6MeV等是本文模型卡，不能迁WK22实际input。 | literal-model-input-boundary | direct-original | PDF2–3 model paragraph | true |
| EM97-D24-008 | TableIII的两个E1 23/42μW.u.在正文第2107页（PDF3）讨论中顺序与表相反，保两种literal版本，不静默选。 | source-internal-order-conflict | direct-original | PDF3 TableIII; PDF3 discussion | true |
| EM97-D24-009 | 133Ce不应写成“全核无τ”：本文仅覆盖列出态，modern832/1409.8/1809.1母态不能按近能/Jπ自动套用这些寿命。 | scope-and-migration-boundary | direct-original-plus-task | PDF3 TableII/III; PDF4 discussion | true |

## Lifetime and Transition Ledger

|transition|Eγ keV|mean τ ps|reported probability|
|---|---:|---:|---|
|11/2−→9/2−|170|76(3)|B(M1)=65(2)mW.u.|
|13/2−→9/2−|555|7.9(.5)|B(E2)=17(3)W.u.|
|13/2−→11/2−|385|7.9(.5)|B(M1)=45(4)mW.u.|
|15/2−→11/2−|619|3.8(.8)|B(E2)=52(15)W.u.|
|15/2−→13/2−|235|3.8(.8)|B(M1)=56(15)mW.u.|
|17/2−→13/2−|752|≤1|B(E2)≥65W.u.|
|17/2−→15/2−|517|≤1|B(M1)≥40mW.u.|
|19/2−→15/2−|763|≤1|B(E2)≥65W.u.|

## Positive-Parity 3qp Ledger

TableIII reports 17/2+→15/2− 1269keV τ5.3(.6)ps/B(E1)23μW.u.; 19/2+→17/2− 954keV τ4.5(.5)ps/B(E1)42μW.u.; 19/2+→17/2+ 201keV B(M1).5W.u.; 21/2+→19/2+ 159keV τ5.3(.6)ps/B(M1)1.1W.u. The 15/2+ head is too weak for τ. E1 23/42 order conflicts between table and prose; both preserved. These assignments reuse prior configuration work and do not independently prove a 3qp identity.

## Competing Interpretations and Limitations

This primary closes a real 133Ce low/high-spin lifetime route and the τ-to-evaluation conversion, but not all bands, branch fractions, ICC, signed matrix elements, or covariance. It supports retaining measured clocks by exact Ei/Jπ/branch and method; it limits transfer from the 11/2− clock to modern 582/817 candidate edges or high-spin bands. No direct chirality verdict follows from these lifetimes alone.

## Extracted Pages

- [[133ce-thesis-analysis-blueprint]]
- [[gizon-1974-deformed-states-cerium-neodymium]]
- [[nndc-2011-133ce-low-level-reference-records]]


Day24 source link: [[emediato-1997-133ce-rdds-lifetimes]]

## Day25 checkpoint005：原方法对化学势禁令的直接反例

独立代理定向回读4页，父代理fresh文字/视觉核PDF2；SHA39f6d6a7bb4e2da109504aaab2c22c52fa8b1465b860c1dfd58937bc404869df相符。本次新读为原有body的参数反例，不是新增实验或2022代码复现。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EM97-D25-A005-01 | 作者为负宇称νh11/2 yrast PTR比较用λ50.6MeV、Δ.92MeV、ħω0=8.41MeV，并含N4/5壳；这直接反驳不同宇称必须相差一个经验ħω或负宇称禁用50.6的普适规则，不恢复WK22 actual参数。 | direct-model-input-counterexample | direct-original-and-visual | PDF2 printed2106 PTR parameter paragraph | true |
| EM97-D25-A005-02 | 本工作为São Paulo本实验室建造plunger的RDDS，不是Köln采集；几何与效率不能由其它plunger名转移。 | direct-experimental-identity | direct-original | PDF1 printed2105 experimental paragraph | true |

此修订与[[133ce-thesis-analysis-blueprint]] actual输入边界联动；全signed核、BR/ICC/Cov仍按原页缺口保留。
