---
type: source
title: "99Rh官方记录：1117同母态支路与取向参考的边界"
aliases: [NNDC99Rh sameparent reference audit, Rh99 2017 ENSDF selected records]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-objects
reading_depth: skimmed
title_original: "Nuclear Data Sheets for A = 99; 99RH Adopted and (HI,XNG) selected objects"
authors: [E. Browne, J. K. Tuli]
journal: Nuclear Data Sheets
year: 2017
volume: 145
pages: "25-340"
doi: "10.1016/j.nds.2017.09.002"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "NNDC99045001/99045019, accessed2026-10-19"
source_url: "https://www.nndc.bnl.gov/ensdf/"
raw_file: "raw/data/gpt/day16-20261018/rh99-hi2017-2cb933aafd59.ens"
raw_sha256: "2cb933aafd59b7df0eefdd6c78798d4543726c819b39c1a256c8d7ed672b914a"
raw_storage_status: official-staging-verified-raw-archive-deferred
nuclei: [99Rh]
reactions: []
observables: [multipole-mixing-ratio, DCO, polarization, angular-distribution]
methods: [ENSDF-fixed-column, reference-matching, source-independence]
tags: [a100, high-spin, alignment, conditional-design, provenance]
---

# 同母态不自动等于已知取向参考

## Bibliographic Record

Browne/Tuli，*Nuclear Data Sheets*145,25–340(2017)，DOI[10.1016/j.nds.2017.09.002](https://doi.org/10.1016/j.nds.2017.09.002)。Crossref核作者、卷页；两个NNDC对象header均给cut1-Jul-2017、base201707/201709。

## Scope and Reading Depth

实际读取HI对象758行主线/注释/能级表；Adopted1102行只定向核header、3711.1母态及相邻能级。HI格式PDF21页，重点视觉核pp2/5/7/9/12/18/21中的母态、目标γ、图式和band角色；不称通读A99全部评价或九篇primary。

| 对象 | 实际staging路径 | SHA-256 |
| --- | --- | --- |
| 99045001,99RH Adopted | `tmp/day16-rh99-structure/adopted2017.ens` | f51058dfe9df8c3921f8f2f711cd923fc47f13dcb59166b9de2808bf76afaafb |
| 99045019,99RH HI | `tmp/day16-rh99-structure/HI2017.ens` | 2cb933aafd59b7df0eefdd6c78798d4543726c819b39c1a256c8d7ed672b914a |

原始对象由官方form精确POST选取，未把search页面当ENSDF。PDF、原文及元数据在repo内tmp，raw/Bib未修改，公开归档槽仍deferred。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N099-1 | HI对象声明数据来自2014Ku20，扩展2013Su15/2000Si05；2017是评价版本，不是新测量。 | lineage-and-version | direct-object | 99045019 header c-lines5–34 | true |
| N099-2 | HI列3710.6(11)、23/2−、band(e)，其六个出射γ为163.1、277.1、561.3、597.4、820.4、1117.5keV。 | sameparent-identity | direct-fixed-column-and-diagram | 99045019 L3710.6；PDFp18 | true |
| N099-3 | 1117.5列DCO=.47(.04)、IPDCO=+.02(.01)，820.4列DCO=.51(.05)。这些是2014原谱系的编译观测，不能重命名为P00的P或a2。 | observable-object-boundary | direct-object | 99045019 L3710.6/G1117.5；PDFp12 | true |
| N099-4 | 近能1114.1 E2来自4264.0的27/2+；1104.3 M1来自3698.1的23/2+、同到2593.2。两者都不是3710.6同母态参考。 | identity-failure-control | direct-object-and-diagram | 99045019 L4264/G1114.1；L3698.1/G1104.3 | true |
| N099-5 | 所选六支在HI仅标M1或E1，无pureE2支路；这只说明该对象未列这种同母态参考，不证明所有可能弱支均不存在。 | reference-readiness | direct-selected-records | 99045019 L3710.6 sixG | true |
| N099-6 | 六支MR字段均空。header为计算CC而在未给MR时假设某些δ；其默认.10/1.00不是这些γ的实测混合比，CC也不是新测ICC。 | missing-field-and-theory-boundary | direct-header-and-fields | 99045019 cGMR；L3710.6/G1117.5 MRblank | true |
| N099-7 | 所选母态记录没有a2/a4、u2、实际取向密度或Q/Cov。multipole标签和DCO/IPDCO不能独立补足P00-15要求的同条件u2符号。 | missing-companion | direct-record-readiness | 99045019 L3710.6 record block | true |
| N099-8 | 六支HI中央RI按1117.5的33.8归一到100，与Adopted六个印刷RI半舍入格均相容；它们不是六项独立强度重测。 | normalization-crosscheck | actual-arithmetic | 99045001 L3711.1；99045019 L3710.6 RI | true |
| N099-9 | Adopted母态3711.1与HI3710.6属于各自least-squares能量版本；原γ能量残差不必逐项为零，不能把其差当新状态或独立能量冲突。 | fitted-level-version | direct-note-and-calculation | 99045001 cLE；99045019 cLE | true |
| N099-10 | 2014Ku20用75As+28Si/120MeV、18clovers；P00用74Ge+31P/110MeV（P00-16），1994Ra07才用89Y+16O。不同采集可提供新观测，但编译、primary及同次DCO/derivedlabel不各计独立实验；2014实际response尚未恢复。 | independence-and-response | direct-header-with-P00-crosswalk | 99045019 2014Ku20 paragraph | true |
| N099-11 | HI注释指出1975Ki13曾把相关γ归99Pd并采用其spin序列，故那一分析不直接适用于99Rh；复用偏振必须先校核spin/核素身份。 | historical-counter-evidence | evaluator-attribution | 99045019 1978Lu02/1975Ki13 paragraph | true |
| N099-12 | 1994Ra07是P00Ref8的High-spin states in99Rh，DOI10.1088/0954-3899/20/3/005，441–450；已核metadata/官方引用，未取得原正文，不能补gate或AD。 | original-source-readiness | metadata-and-access-boundary | official HIreferences 1994RA07 | true |
| N099-13 | Codex条件设计：相同density下pureΔJ0/ΔJ1 dipole的a2满足a2(0)=−44a2(1)/25；未知相邻高多极振幅时，有相位无关的充分纯度条件，分别约|δ|<.86021与.141913才保证F2符号不翻。不是这些支路的实测界。 | reference-design-model | exact-kernel-and-CG6j | 本页参考纯度设计；rh99-reference-purity-result | true |
| N099-14 | 编译feeding包含3988.8的25/2−经278.5M1到3710.6，以及4579.6的27/2−经867.8E2到3710.6。仅给spin路径与源标签，不把它们的2014强度/取向移回P00或证明pure。 | actual-feeding-identity | direct-table-and-diagram | 99045019 L3988.8/G278.5；L4579.6/G867.8；PDFpp5/9/21 | true |

## Same-parent branch crosswalk

| γ/keV | HI终态/keV及Jπ | HI标签 | HI RI | Adopted RI（1117=100） |
| --- | --- | --- | --- | --- |
| 163.1 |3547.4，21/2− |M1 |.30(.06) |.89(.18) |
| 277.1 |3433.5，21/2− |M1 |.11(.02) |.33(.06) |
| 561.3 |3149.9，23/2+ |E1 |.50(.08) |1.48(.24) |
| 597.4 |3113.2，21/2− |M1 |.23(.04) |.68(.12) |
| 820.4 |2890.2，21/2+ |E1 |9.9(.6) |29.3(1.8) |
| 1117.5 |2593.2，21/2+ |E1 |33.8(2.0) |100(6) |

同一母态的photon RI与总跃迁率仍不同，不能跳过ICC/selection。a2/a4/P与该RI没有已知共同Σ。六个能量闭合残差为+.1、0、−.6、0、0、−.1keV；程序逐项保留原母态/γ/终态的quoted误差，不用任意零残差阈值裁决。

## 参考纯度设计：先识别符号，再估计宽度

以下是[[rh99-1117-population-feasibility]]延续的Codex条件模型，不是2017评价或2014作者给出的公式。定义u2为该note的pure23/2→21/2 dipole二阶系数。对相同density、point或已正确修正的响应：

`a2(ΔJ=1) = u2 F1(δ)/(1+δ²)`，

`a2(ΔJ=0) = −(44/25)u2 F0(δ)/(1+δ²)`。

独立CG/6j与12个physical pair核逐项相合：F22/F11分别13/35和−100/143，crossratio平方分别63/5和45/572。考虑两种δ相位，`F(d) ≥ 1−2|crossratio|d+(F22/F11)d²`，d=|δ|。其第一个正零给保证F>0的充分条件：

| 同母态参考路径 | 相位无关的充分幅度上界d | 相应高多极photon份额上界 | 与u2≤0相符的a2符号 |
| --- | --- | --- | --- |
| ΔJ=1，如820.4 |.1419127 |.0197416 |a2≤0 |
| ΔJ=0，如561.3 |.8602067 |.4252727 |a2≥0 |

严格小于上界时才保证符号；F=0会失去rank2取向信息。这是充分条件，不是完整可行域，也不是原δphase转换。EMduality使I相同，因此设计本身无需先选E/M宇称；仍必须独立知道参考的阶次混合与density匹配。

561.3的ΔJ0符号在这个模型中较不易受未知混合翻转，但其photon RI仅约target的1.48%；820.4约29.3%，却需要更严的混合幅度约束。这个取舍来自实际记录与条件核，不替真实背景、响应和统计功效计算。两支都没有已取得的参考a2或纯度界。

`a4≈0`不能独立证明pure dipole：例如各m等布居时所有混合都有rank4零，而不是只有δ=0。纯限恒等式也只在实际density/trigger/gate/feeding匹配时可用，不能从不同母态或不同反应借入。

## Competing Interpretations and Limitations

原P00正P与AD选择E1仍是其作者结论；此记录不反推新的δ或宇称。所列labels含源分析与评价，不升级为独立purity测量。u2≤0仍expected-but-not-established；不同反应的2014 DCO/IPDCO不能无模型移回P00。

2014Ku20 primary DOI10.1088/0954-3899/41/10/105110已核。当前IOP返回bot页面，Lund记录只有metadata/摘要、OpenAlex指出bronze但未取得body。不能由这些记录补完整角组、gate、a(E)/Q、Cov或phase。1994与2014两个primary缺口分开保存，不联系作者或绕过访问控制。

## Summary

官方记录确认1117.5的母态及六个出射支路，未提供独立取向参考所需的混合纯度和同条件AD。ΔJ0/1的条件设计给出可补测对象与代价，当前不把取向符号或竞争分支判决写成已测。

## Knowledge Impact and Learning Decision

`supports`目标与同母态六支身份；`limits`“找到了sameparent就测得alignment”的承诺；`revises`参考选择为“已知阶次混合+匹配取向/响应+实际AD”。新增有统计代价的ΔJ0与ΔJ1选择，不授实验L4或Day17学分。

## Reproducibility and Self-audit

[fixed-column程序](../../system/scripts/day16_rh99_official_reference_audit.py)、[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/rh99-official-reference-result.json)与[纯度设计程序](../../system/scripts/day16_rh99_reference_purity_design.py)、[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/rh99-reference-purity-result.json)实际exit0。首个.2keV阈值失败、纯度程序首个PYTHONPATH缺SymPy失败及修正均保留，未改source/冻结合同或安装环境。

P0：未识别未隔离的来源身份/路径/权限问题。P1：模型纯度阈值、同density与source标签不可升级；实际body/Σ缺口仍在。所有claims needs_review，不写human-reviewed。

## Extracted Pages

[[99rh]]、[[palit-2000-rh99-clover-polarimetry]]、[[rh99-1117-population-feasibility]]、[[multipole-mixing-ratio]]、[[linear-polarization-asymmetry]]、[[high-spin-angular-polarization-mixing-ratio]]。


这两条spin路径的完整未观测转移条件见[[unobserved-feeding-alignment-sign]]；高spin低L保号不代实际reaction/粒子j/方向门核验。
