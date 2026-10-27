---
type: source
title: "Meyer-ter-Vehn1975(II)：奇A独特宇称谱与三轴芯的实验比较"
aliases: [Meyer ter Vehn1975 PartII, MTV75 odd-A unique parity comparison]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: theoretical-paper-with-experimental-comparison
reading_depth: deep-read
title_original: "Collective model description of transitional odd-A nuclei (II). Comparison with unique parity states of nuclei in the A = 135 and A = 190 mass regions"
authors: [J. Meyer-ter-Vehn]
year: 1975
journal: Nuclear Physics A
volume: 249
pages: 141–165
doi: 10.1016/0375-9474(75)90096-2
canonical_source: https://doi.org/10.1016/0375-9474(75)90096-2
citation_key: ""
raw_file: raw/papers/1975_MeyerTerVehn_CollectiveOddANuclei_PartII.pdf
raw_sha256: fd1ba7f9280e8bafd86bbec06ec18e8a7089f93e84306829a4be897d9dd8439d
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-meyer1975-partii-entry-057/attachment-object-response.pdf
nuclei: [133Ce, 135Nd, 137Nd, 131Ba, 129La, 131La, 135Pr, 187Ir, 195Au, 193Hg, 199Tl, 190Os, 124Xe]
models: [single-j-shell, triaxial-rotor-plus-quasiparticle, BCS, rigid-triaxial-core]
methods: [level-scheme-comparison, standard-parameter-calibration, electromagnetic-branching]
observables: [energy-spectrum, B(E2), B(M1), mixing-ratio, spectroscopic-moment]
tags: [133Ce-method-blueprint, model-calibration, gamma-softness, source-lineage]
---

# 谱对三轴芯有偏好，不等于直接测得刚性

## Bibliographic Record

J. Meyer-ter-Vehn，NPA249(1975)141–165，DOI10.1016/0375-9474(75)90096-2。这是[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] Ref52，Ref51为[[meyer-ter-vehn-1975-triaxial-rotor-particle-model]]。physical页+140=印刷页。

057以Crossref/出版商FULL XML和首页确认身份，从实际MAIN attachment取得真25页、1368683bytes、上述SHA的完整正文；普通下载器一页preview与真body分开。SI入口默认检查，ALTIMG/thumbnail不当科学补充材料。PDF/XML/OCR/整页渲染暂在tmp，未归档raw，也不进入本run公开manifest。

## Scope and Reading Depth

060连续读PDF1–13的一般取参和A190、全部该段图表；059负责PDF14–19的A135/Tables4–5/Figs7–9；061连续读PDF20–25讨论/结论/参考，另核必要context1–2/18–19。root连续文本读1–24及25参考，视觉另核PDF4/9/13/14/17/19/21/22的关键取参、原表、Ce图与PES论证。合并主线含Figs1–10/Tables1–7；单个worker不冒独立全25页。没有原读全部44篇引用、复现作者job或重提实验强度。

## Summary

本篇将同一个1qp/独特宇称j壳模型与已有odd-A谱比较，得到有条件的三轴偏好。参数主要由邻偶核取，但γ的prolate/oblate侧、壳内λ及若干β例外仍利用目标谱；“essentially parameter-free”不等于完全独立预测。133Ce的9/2态是作者明确保留的失败。作者也明确说不能照字面取rigid shape，尚无定量PES结论。

## Key Results

所有新行needs_review:true；原实验、继承数据、模型、作者解释和任务算术分开。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MTVII75-D24-001 | 固定βγ为近似；1qp unique-parity低激发约2Δ以下，遗漏形状涨落、Coriolis attenuation、odd polarization、pair blocking、其它j与≥3qp。非unique-parity系统mixed-j比较未做。 | explicit-model-domain | direct-original | PDF1–2 Introduction | true |
| MTVII75-D24-002 | γ取邻偶核能量比，particle用A−1、hole用A+1；γ与60−γ的哪侧另依odd-A谱。β却用两邻第一2+平均，作者承认经验折衷，不能把所用邻偶核再算独立holdout。 | parameter-source-and-dependence | direct-original | PDF3–4 §2/Table1 | true |
| MTVII75-D24-003 | 壳内λ近似fit第一(j−1)目标态；图2–9的tildeλ是相对单壳端点/间隔的无量纲坐标，不是WK22 MeV λ或negative-parity actual输入。 | explicit-target-calibration-and-units | direct-original | PDF4 §2 final paragraphs | true |
| MTVII75-D24-004 | 199Tl β标准.13改.15，195Au β.141改.144；195Au模型衰变率和187Ir δ使用已知实测Eγ。它们保有模型比较价值，也不是所有观测独立于数据的预测。 | actual-calibration-and-EM-input | direct-original | PDF7–9 Figs2–3; PDF13 Table3b footnote | true |
| MTVII75-D24-005 | 193Hg decoupled yrast序被γ38/β.13与γ60/β.11两例都再现；第二19/2态提供额外三轴线索但实验宇称不定。仅yrast序不唯一测γ。 | actual-alternative-model-and-companion | direct-original | PDF9–10 §3.1.3/Fig4 | true |
| MTVII75-D24-006 | Table2第二11/2态β.141的原印率%为4,25,11,40，总80；不补24或归一。Table3b五条理论δ仅两条在原实验字面范围内；不把该成员检查改成统计显著性。 | original-table-crosscheck-and-boundary | direct-original-plus-arithmetic | PDF9 Table2; PDF13 Table3b | true |
| MTVII75-D24-007 | 187Ir的h9/2/h11/2用不同邻芯，K/Ω分类近似且带间泄漏明显；约.3(e b)^2实测B(E2)来自189Ir，不是187Ir同态测量。187Ir stagger及部分branch未再现，不能只摘“good agreement”。 | state-lineage-and-model-residual | direct-original | PDF10–14 §3.1.4–3.1.5/Figs5–6/Tables3a–b | true |
| MTVII75-D24-008 | Table5 La129/131的两条favored E2绝对强度来自Ref29，而b由邻偶核B(E2)均值定标；理论误差来自所取γ不确定度。相邻跃迁强度接近是该案例对弱耦合的约束，不移成Ce实测或普适模式门。 | measured-EM-and-model-calibration | direct-original | PDF16–17 §3.2.2/Table5 | true |
| MTVII75-D24-009 | N75同中子素为135Nd/133Ce/131Ba，非131Ce。Fig9 exp以11/2−为0、9/2−为−170；triaxial列9/2为+18、axial为+37。最低9/2未降够，作者未加ad hoc attenuation。 | historical-Ce-spectrum-and-explicit-failure | direct-original | PDF18–19 §3.2.4/Fig9 | true |
| MTVII75-D24-010 | Fig9比较β.22/γ23与β.19/γ0，同tildeλ1/Δ1MeV；并非只变γ的单参数检验。历史相对零点及高态不能凭近能差整体移为现代band。 | comparison-input-and-cross-version-boundary | direct-original-and-task-scope | PDF19 Fig9 | true |
| MTVII75-D24-011 | 137Nd部分附加态不能同时配上h11/2能量与衰变网络，作者提出f7/2或h9/2替代并要更多数据；不是测定组态，也不代135Nd高spin三qp解释。 | counter-evidence-and-assignment-limits | direct-original | PDF17–18 §3.2.3/Fig8 | true |
| MTVII75-D24-012 | Fig10是schematic PES；摘要coexistence指ΔI1和ΔI2 band structures，不等观测到两shape。作者说rigid shape照字面理解naive。 | direct-terminology-and-inference-boundary | direct-original | PDF1 Abstract; PDF19–20 §4/Fig10 | true |
| MTVII75-D24-013 | Table6对比完全γ独立Wilets–Jean极限与一个rigid点，实验既不达complete soft也不达rigid。不能由排一个极限推出无一般γ软度、σγ或唯一PES。 | conditional-softness-test | direct-original | PDF21 Table6 and following paragraph | true |
| MTVII75-D24-014 | Table7引用dynamic rms与本篇effective fitγ是不同量；右侧原header为196Pt计算与196Hg standard，不擅修。结论约±2°是指定谱模型敏感性，不是实验CI或波函数宽度；作者明确无定量PES结论。 | observable-definition-and-precision-boundary | direct-original | PDF22 Table7; PDF23–24 Conclusion | true |
| MTVII75-D24-015 | 作者提出odd particle+γ动态芯定量对照但尚无结果；Refs33–35无明显triaxmin的概括保Ref36 N76/Z56–66例外。本篇复用所引实验和邻核取参，不是新独立采集。 | alternative-readiness-and-source-lineage | direct-original | PDF21 footnote; PDF22 final paragraph; PDF24–25 References | true |

## Theory and Actual Table Checks

标准取参是γ先由偶核比值、β=[1224X(γ)/(A^(7/3)Ebar2+)]^(1/2)，Ebar单位MeV。particle tildeλ=(λ−e1)/(e2−e1)，hole tildeλ=(e_(j+1/2)−λ)/(e_(j+1/2)−e_(j−1/2))。它们不提供任意多轨道GAMPN/ASYMO header、共同绝对E0或负宇称λ。

Table2第二11/2的实验列52/3/11/34与β.144列57/8/15/20各总100，β.141列4/25/11/40总80。原图fresh放大确认4，保归一/排印缺口，不改原件。第三11/2实验blank不是零。Table3a四个B(E2)比在宽/单侧范围内，第一项1.7(+∞,−1.4)对理论7.07不能称精密符合。

|Table3b Eγ keV|实验原范围|模型δ|字面成员检查|
|---|---|---|---|
|200|0<δ<.25|.04|内|
|330|.25<δ<.40|.18|外|
|389|.15<δ<.25|.19|内|
|395|.28<δ|.21|外|
|385|−.40<δ<−.15|−.14|外|

模型使用实测Eγ，误差/区间coverage未建立。2/5是原表算术，不能换成p值、完整拟合优劣或迁移实际Ce δ符号。

Table5原La数据：129La B(15/2→11/2)=.42(2)、B(19/2→15/2)=.38(6)，131La为.34(2)/.33(3)，单位e²b²；相应γ269/475和336/533keV。理论γexp行.37(2)/.42(2)、.32(2)/.37(2)，轴向行.50/.52、.45/.47。b6.8/6.4来自邻偶核B(E2)均值，勿将带外定标与同一数据派生量重新计独立证据。

## Ce Reference and Modern Migration

Fig9以exp11/2=0，13/2=385、15/2=620、17/2=1136、19/2=1380、21/2=2027、23/2=2336keV；9/2为−170。现代[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-36所列Ex207.4等不能直接同零点。先平移后逐态和全links验证，高态差异不因同spin标签消失。原caption未解释994虚线/1164注；本轮后续Ref26原件已给出数值出处，见下节。最高模型态spin印字仍保扫描歧义，不猜拓扑。

N75三核相似谱是历史系统学线索，非三个新独立campaign；原Ref26/27实验身份和可追溯边需要原件，不能只引本篇理论比较。图中Q/μ为calculated basic-state moments，理论箭头含model B及已知实验Eγ；不是新测静态矩、寿命或δ。fixed1qp<2Δ的较高I态不自动对应现代3qp crossing。

## Competing Interpretations and Limitations

Table6定义r1=E(2₂)/E(4₁)、r2=[E(4₂)−E(2₂)]/[E(3₁)−E(2₂)]：complete γ-independent理论(1,1)，rigidγ22.2°(1,2.73)，190Os(1.02,2.01)，124Xe(.96,1.47)。两个比共享E2₂，无joint error；不能按离两个端点的距离反演γ分布宽度。作者保finite spread解释而非“完全刚性”。

Table7 Ref33的186Os γrms为23.2/21.1/19.6/33.4，196Pt为36.2/38.9/40.5/31.2，顺序0₁/2₁/4₁/2₂；本篇standard186Osγ16、196Hgγ37。原header和量定义保留，不将不同核/不同统计量相减成实测波动。作者更偏好Hg较不软，对Os/Pt/A135证据说较弱，并要求尚未完成的γ动态odd-A计算。

本轮decision：supports逐谱联合E/EM与邻芯的条件三轴线索；limits把模型有效γ、强度比、近简并或支带个数当直接刚性/手征/两shape测量。actual133Ce三程序输入、signed输出与582分母仍独立缺；本文也不提供135Nd partner的g向量或替代模型胜负。

## Extracted Pages

- [[133ce-thesis-analysis-blueprint]]：历史负谱、参数坐标与模型失效的跨源合同。
- [[135nd-chiral-partner-resolved-evidence-map]]：奇A低1qp系统学不能代高spin三qp伙伴证据。
- [[chirality-shape-coexistence-companion-matrix]]：拒绝complete softness不等测出rigidity。


## Ref26原实验续核：数字出处闭合，现代整带身份未闭合

[[gizon-1974-deformed-states-cerium-neodymium]] GZ74-D24-009–012取得真22页原实验后，可明确Fig9的旧数值：primary以历史9/2=0，11/2=170、支态1163.6；故支态改参考为1163.6−170=993.6≈994，而1163.6≈1164。原caption未解释这两个数的事实不变，现在其出处不再仅猜测。

同原primary没有本篇图顶21/2/23/2的同spin主支，19/2原值1552.3−170=1382.3也不等本图1380，不用粗rounding或一个offset强合所有节点。primary当年ground/isomer顺序未定，现代37.2为WK22能差派生，暂定平移只支持低node/一条608.7边候选，不是整Band4或signedEM认证。本文及后来的理论复用这一primary，不能重复计新独立采集。


Day24 primary link: [[butler-1975-la129-la131-rd-lifetimes]]


Day24 evaluation link: [[nndc-2011-133ce-low-level-reference-records]]
