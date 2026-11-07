---
type: source
title: 'Wang & Chen 2024: 协变密度泛函五维集体哈密顿量探索偶偶核三轴摆动与自旋相干态图'
aliases: [Wang Chen 2024 PLB, 5DCH even-even wobbling, 10.1016/j.physletb.2024.139131]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: Exploring wobbling motion in triaxial even-even nuclei
authors: [Y. M. Wang, Q. B. Chen]
journal: Physics Letters B
year: 2024
volume: 859
pages: '139131'
doi: 10.1016/j.physletb.2024.139131
canonical_source: https://doi.org/10.1016/j.physletb.2024.139131
citation_key: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G29/wang-2024-exploring-wobbling-even-even.pdf
raw_sha256: 77d21f7239346ea03ef356309c877d96add3aa4d6ec485696b4e5117b5f57b21
raw_storage_status: archived-local
archive_required: true
learning_candidate: true
nuclei: [112Ru, 114Pd, 150Nd, 188Os]
models: [5dch-rdft, covariant-density-functional, spin-coherent-state-map]
observables: [rotational-energy, b(e2), cos3delta, scs-probability-density]
methods: [multidimensional-collective-hamiltonian, azimuthal-projection, wavefunction-average]
tags: [even-even-wobbling, 5dch, triaxiality, scs-map, gamma-softness, longitudinal-wobbling]
---

# Wang & Chen2024：五维集体波函数中的取向动力学

## Bibliographic Record

Y.M. Wang、Q.B. Chen，*Exploring wobbling motion in triaxial even-even nuclei*，PLB859,139131(2024)，
DOI `10.1016/j.physletb.2024.139131`。实际六物理页出版PDF，CC BY；路径与哈希见frontmatter。

## Scope and Reading Depth

G29读取；总控独立回PDF1–5主文，核SCS定义、EDF/配对输入、惯量校准、Fig1–6与作者结论边界。
未运行5DCH代码，未获得波函数数表；References中的实验并未因此全部原读。
130Ba/136Nd只在引言中作为已有两准粒子案例提及，不是本文5DCH算例。

## Summary

作者将形状与转动自由度共同量子化，用SCS边缘分布解释112Ru等核的模型摆动特征，
并与150Nd比较。文末明确要求完整带间E2实验来检验预言，不能写成新实验已经确证。
该模型保留形状涨落，因而反对“所有软核都不能有取向模式”的笼统判断。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WC24-1 | 5DCH波函数按K展开；对β/γ求迹得到ρ_K′K，再由ρ构造归一SCS分布 | model-method | direct-original | PDF2 Eqs.1–6 | false |
| WC24-2 | PC-PK1与δ配对输入；为补未包含的Thouless–Valatin修正，将惯量增强到匹配实验2₁能量；讨论I≤10ℏ | model-input-and-calibration | direct-original | PDF2末、PDF3 Fig2前 | false |
| WC24-3 | 模型给112Ru/114Pd/188Os不同程度三轴分布，150Nd更近轴；q₃型平均量与完整分布一起比较 | model-result | direct-original | PDF2–4 Figs.1/4/5 | false |
| WC24-4 | 112Ru的SCS在基带m轴附近峰、γ带相应处谷/环，被作者解释为非谐摆动；150Nd没有同样图样 | author-model-interpretation | direct-original | PDF4–5 Fig6及讨论 | false |
| WC24-5 | 文末要求带间B(E2)实验检验理论预测；文中也承认Ru/Pdγ带绝对能量偏高 | explicit-limitation | direct-original | PDF3 Fig2后、PDF5结论末 | false |

Eq.4所用测度与系数采用作者规范；不能把该表达式未经转换当所有5DCH量子化的通用测度。
SCS是波函数分析而非探测器直接拍摄。q₃平均量接近零不独立给γ刚性或全分布。

## Competing Interpretations and Limitations

形状振动与取向量子动力学可耦合；平均形变、SCS边缘分布和单个交错不能独立唯一反演机制。
B(E2)对同一对态的正反方向严格受2I+1因子联系，Fig3的不同ΔI分支不是违反详细平衡。
不以能谱校准后同一能级的吻合当留出验证，不将本文变成130Ba破对态计算。

## Extracted Pages

见[[doctoral-r1-g29-a130-core-orientation-20261108]]的跨模型比较及候选问题。

## Agent Self-audit Triage

P0：原件身份、正文和关键公式已核，旧稿“平均量严格定量刚性/112Ru实验证实”已撤回。
P1：没有波函数/代码重放、完整实验网络和Cov，支持范围为作者模型解释。
