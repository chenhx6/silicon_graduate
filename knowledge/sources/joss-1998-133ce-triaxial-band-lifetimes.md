---
type: source
title: "Joss1998：133Ce高自旋三轴带寿命与Qt"
aliases: [Joss 1998 133Ce triaxial band, 133Ce high-spin DSAM]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: experimental-lifetime-paper
reading_depth: deep-read
title_original: Lifetime measurements of a triaxial band in 133Ce
authors: [D. T. Joss, E. S. Paul, R. M. Clark, I. Y. Lee, S. J. Asztalos, J. A. Becker, L. Bernstein, B. Cederwall, M. A. Deleplanque, R. M. Diamond, P. Fallon, L. P. Farris, K. Hauschild, I. M. Hibbert, W. H. Kelly, A. O. Macchiavelli, P. J. Nolan, N. J. O’Brien, A. T. Semple, F. S. Stephens, R. Wadsworth]
year: 1998
journal: Physical Review C
volume: 58
issue: 6
pages: 3219–3222
doi: 10.1103/PhysRevC.58.3219
canonical_source: https://doi.org/10.1103/PhysRevC.58.3219
citation_key: ""
raw_file: raw/papers/1998_Joss_133Ce_Triaxial_Band_Lifetimes.pdf
raw_sha256: 81b6ace5d9ee867220c5425e7f3d9ae4f5074d9484f7063fd04fd137b0deea0a
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-joss1998-133ce-triaxial-lifetime-078/publisher-pdf.pdf
nuclei: [133Ce, 132Ce, 131Ce]
reactions: [100Mo-36S-xn-133Ce]
experiments: [gammasphere-dsam-133Ce-1998]
models: [triaxial-rotor-plus-quasiparticle, total-routhian-surface, IBFM]
methods: [DSAM, doppler-broadened-line-shape, Monte-Carlo-stopping]
observables: [mean-lifetime, Qt, T(E2), level-scheme]
tags: [133Ce-analysis-blueprint, high-spin-lifetime, triaxial-model, sidefeeding]
---

# 高自旋带的寿命和Qt提供独立时钟，也保留阻停与组态边界

## Bibliographic Record

D.T.Joss等，*Physical Review C*58(6)(1998)3219–3222，DOI10.1103/PhysRevC.58.3219。078取得APS正式4页、120604bytes、SHA见frontmatter。它是Gammasphere+DSAM/DBLS primary，与[[emediato-1997-133ce-rdds-lifetimes]]低自旋RDDS不同，二者不能按νh11/2标签合并。

## Scope and Reading Depth

全文4页、Fig1–4、TablesI–II和方法/讨论均读及视觉核；未运行LINESHAPE/TRS、未取得raw counts/阻停核/fullCov/producer，SI入口未识别补充材料。原文中的模型参数和组态标记保作条件结果。

## Summary

本文在100Mo(36S,xn) A≈132反应中测133Ce高自旋三轴带的四条DBLS寿命：1.11(.13)、.33(.04)、.20(.02)、.21(.02)ps，对应Qt 1.94(.10)、2.65(.16)、2.66(.21)、2.15(.15)eb，作者加权给Qt≈2.2(.1)eb。它是具体高自旋带/阻停合同的实验结果，不是全核寿命调查或直接静态γ测量。

## Experimental and Fit Contract

约9×10^8 fold>5 events、5天；相对通道产额为 132Ce:131Ce:133Ce = 5:4:1，按422/488/643/888keV门分选，前向31.7–37.4°、90°、后向142.6–148.3°。LINESHAPE以Currie Monte Carlo每步5000 histories、0.001ps步长，Ziegler+MC阻停；sidefeeding用固定惯量48 ħ²/MeV五态带且强度先由数据固定。Qt/QSF/污染峰/背景和归一化共同拟合，未提供raw/完整Cov/逐线系统核。

## Key Results

全部新claims needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JO98-D24-001 | 133Ce high-spin DBLS四条线来自Gammasphere；DSAM线形依赖阻停、feeding与sidefeeding，不是response-independent τ。 | direct-method-and-scope | direct-original | PDF1–2/3219–20 | true |
| JO98-D24-002 | 四条平均τ/Q_t为887.4 1.11(.13)/1.94(.10)、999.3 .33(.04)/2.65(.16)、1097.6 .20(.02)/2.66(.21)、1188.1 .21(.02)/2.15(.15)；加权Qt≈2.2(.1)。 | high-spin-lifetime-and-Qt | direct-original | Table I PDF2/3220 | true |
| JO98-D24-003 | 表内Qt逆方差加权算术为2.199(.070)，支持2.2中心核算；作者正文讨论指出绝对Qt另含约10–15%阻停系统学，不能仅由表内误差重建。 | table-crosscheck-and-systematics | task-arithmetic-plus-original | Table I; discussion PDF4 | true |
| JO98-D24-004 | 5000-history/0.001ps阻停、前/90/后角和固定五态sidefeeding是拟合输入；没有raw kernel/fullCov/producer。 | response-and-readiness-boundary | direct-original | PDF1–2 | true |
| JO98-D24-005 | TRS给单νh11/2 β≈.19, γ≈−30°，(νh11/2)^3 γ≈−73°，高自旋图有γ≈−83°与β≈.4 SD极小值；这些是模型PES结果，不是静态γ测量。 | model-result-boundary | direct-original | PDF3–4/Fig3 | true |
| JO98-D24-006 | 以γ−83°、无hexadecapole假设由Qt推β2=.186(.007)，是模型转换，不能当独立形变观测。 | model-derived-shape | direct-original | PDF3 | true |
| JO98-D24-007 | 作者估计带内T(E2)≈35W.u.，低于132Ce SD约490和正常带约100；这是寿命/模型约定的集体性比较。 | derived-collectivity | direct-original | PDF4 | true |
| JO98-D24-008 | 高spin标签多为括号估计，缺连到已知低能带的link；ENSDF band letter/现代BandF不是独立组态实测。 | identity-and-crosswalk-boundary | direct-original | PDF3–4 | true |
| JO98-D24-009 | Emediato1997 low-spin T(E2)≈50W.u.被引用为独立RDDS路线；不把低自旋时钟迁移到本篇高spin四条线。 | source-lineage-and-clock-boundary | direct-original | PDF4 | true |
| JO98-D24-010 | 本文没有partner-band EM network、signed phase、tunneling或静态手征直接证据；高spin triaxial interpretation仍是联合模型解释。 | chirality-boundary | interpretation-boundary | PDF4 conclusion | true |

## Table I Lifetime Ledger

|Eγ keV|τ ps|Qt eb|side-feed τSF ps|
|---:|---:|---:|---:|
|887.4|1.11(.13)|1.94(.10)|.48(.11)|
|999.3|.33(.04)|2.65(.16)|.49(.01)|
|1097.6|.20(.02)|2.66(.21)|.37(.04)|
|1188.1|.21(.02)|2.15(.15)|.34(.04)|

## Competing Interpretations and Limitations

共同132Ce SD1比较可作相对collectivity线索，但绝对Qt仍受阻停系统学；四点不等四个独立模型无关时钟。Emediato低spin和Joss高spin是不同实验/方法，不能按同νh11/2组态合并。未有完整linking transitions、partner EM、signedRME或隧穿证据，不能由Qt/γ模型结果判定chiral vibration/static chirality。

## Extracted Pages

- [[133ce-thesis-analysis-blueprint]]
- [[emediato-1997-133ce-rdds-lifetimes]]
- [[nndc-2011-133ce-low-level-reference-records]]


Day24 high-spin link: [[joss-1998-133ce-triaxial-band-lifetimes]]
