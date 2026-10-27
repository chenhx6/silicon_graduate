---
type: source
title: "Chen2018：四single-j壳PRM与136Nd逐伙伴输出边界"
aliases: [Chen2018 four-j shell PRM 136Nd]
created: 2026-10-26
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: theoretical-paper
reading_depth: deep-read
title_original: "Multiple chiral doublets in four-j shells particle rotor model: Five possible chiral doublets in 136Nd"
authors: [Q. B. Chen, B. F. Lv, C. M. Petrache, J. Meng]
year: 2018
journal: Physics Letters B
volume: 782
pages: 744–749
doi: 10.1016/j.physletb.2018.06.030
arxiv: 1805.06162v1
canonical_source: https://doi.org/10.1016/j.physletb.2018.06.030
full_text_url: https://arxiv.org/pdf/1805.06162v1
citation_key: ""
raw_file: raw/papers/2018_Chen_FourJShellPRM136Nd_arxiv180506162v1.pdf
raw_sha256: cba4fa62433207c06b8673dc484d8a2d0ecdd7db51c27eafb2329726190bee91
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-nd136-prm-holdout-031/chen2018-fourj-prm.pdf
nuclei: [136nd]
models: [particle-rotor-model, four-single-j-shells]
observables: [energy-splitting, B(M1)/B(E2), angular-momentum-components]
methods: [strong-coupling-basis, configuration-energy-truncation]
tags: [chirality, model-output-contract, partner-resolved-evidence]
---

# 四壳量子PRM支持D5，目标两E2预测仍未交付

## Bibliographic Record

Q. B. Chen、B. F. Lv、C. M. Petrache和J. Meng，*Physics Letters B* **782**, 744–749 (2018)，DOI `10.1016/j.physletb.2018.06.030`，Crossref核身份。实际body为官方arXiv1805.06162v1，384518bytes、15页，SHA见frontmatter；官方v1日期2018-05-16，PDF1另印June26,2021 typeset date，二者不混成新科学版本。第二条有明确线索的Kyoto bitstream为HTTP200 HTML壳、非PDF；VoR未核，不继续猜地址。raw仅保留归档槽，实际原件在tmp，未改用户raw。

## Scope and Reading Depth

Day24内Day25无学分预习的一项模型比较。worker完整读15页、6图、TableI和Eqs1–9，并视觉核PDF3–11；root独立读全部文本主线及参考，视觉核PDF6/TableI和Fig1、PDF8/Fig3、PDF10/Fig5。没有作者producer、数值对角化或曲线数字化，未声称独立复现PRM。以下locator属于该v1。

## Summary

good-I量子PRM可保留初末态振幅的相干EM计算，文章实际发表的EM比较是带内B(M1)/B(E2)，不是[[lv-bingfeng-2019-chirality-136nd-135nd-thesis]]中D5-C20+两条E2的out/in预测。能谱、带内比和模型几何支持保留，不能据总体“EM agreement”补出缺失的跨带E2矩阵元。

## Experimental or Theoretical Setup

Eqs1–4以四个single-j壳内多particle/hole的Hintr耦合三轴转子，Hcoll=Σ(Ik−Jk)²/(2𝒥k)，𝒥k=𝒥0 sin²(γ−2kπ/3)。Eqs5–9构造内禀态及time-reversal伙伴，在D2对称strong-coupling基中对角化，总I为好量子数。它不是[[wu-2018-two-dimensional-collective-electromagnetic-transitions]]的单密度平均局部TAC率；框架可算仍须实际态系数、EM核和数值输出。

## Key Results

所有新增claim为`needs_review:true`，区分原模型、发表输出与任务设计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CQ18-D25P-001 | 四single-j壳PRM采用D2对称strong-coupling good-I态，展开保K/内禀振幅。给定完整张量核原则上可相干求态间EM；正文仅说获得波函数后可计算B，未印完整EM核/phase字典或交付actualproducer。 | direct-state-space-and-derived-capability | direct-original-plus-explicit-task-inference | PDF3–5 Eqs1–9及EM计算段 | true |
| CQ18-D25P-002 | D5为正六qp πh11/2²g7/2^−2⊗νh11/2^−1f7/2¹，β=.26、γ23°、𝒥0=40ℏ²/MeV、ξ=.93；是PE18 C宽轨道配置的具体single-j选择，不是各轨道occupation的直接测量。 | model-input-and-cross-source-mapping | direct-original-and-labelled-comparison | PDF6 TableI; PDF5 inputparagraph | true |
| CQ18-D25P-003 | 𝒥0/ξ按能谱趋势调整，EM用经验Q0、gR=Z/A和gs=.6gsfree等处方。按配置能量截断到约5000–10000维、energyuncertainty≤.1%的声明不自动成为小interbandEM同精度证书，完整拟合/截断记录未给。 | calibration-and-convergence-boundary | direct-original-plus-error-object-distinction | PDF5 truncation/inputparagraphs | true |
| CQ18-D25P-004 | 全文实际EM图仅Fig3带内B(M1)/B(E2)，无D5-C20+→D5/D5-C18+两路E2的逐线B、RME或out/in输出，不能认证thesis条件比.21979已被此稿模型检验；范围限本次实际v1，不断言作者从未计算过。 | published-output-verified-negative | complete-original-output-audit | PDF6–11 Figs1–6/TableI; PDF8 Fig3 | true |
| CQ18-D25P-005 | D5能谱/带内EM/RMS支持真实存在；I17–21的g7/2 holes重排、D2劈裂低估、D3 B比不佳、D4低spin配置失配和其它四pair缺双方实测比同时保留。I20目标不能借高spinRMS近合代填EM。 | model-support-and-adverse-results | direct-original | PDF5–10 results; Figs1/3/5 | true |
| CQ18-D25P-006 | 目标同parent两E2的R=abs(Rout)²/abs(Rin)²消共同2Ii+1及一致全局Q0尺度；仍需冻结输入/端点、交付两E2输出和EM收敛及其是否参与调参。此为任务提出的有限holdout合同，非本文已发表结果。 | explicit-task-design-and-boundary | derived-from-good-I-premise-and-actual-thesis-branches | PDF4 Eqs8–9; PDF8 Fig3 outputscope; TH19-D25P-005 | true |

## Model and Observable Chain

D5的六qp分布于四壳。[[petrache-2018-chiral-bands-even-even-136nd]]的C把质子空穴写为(d5/2g7/2)^−2、中子粒子为(f7/2h9/2)¹；本文选g7/2与f7/2，不等完整多轨道混合的同一Hamiltonian。𝒥0/ξ有能谱定标，不能因目标比未画就认证严格out-of-sample，完整fit输入未得。

Fig1为扣0.008I(I+1)参考的能谱，Fig2的S(I)由相同能量派生，不是新独立采集。Fig3实际带内B(M1)/B(E2)无跨带E2分子；两个partner的M1分子又是不同矩阵元，不能把图中比值相除恢复缺失的E2out/in。Figs4–6为RMS分量，不能给signedRME/phase。D5 Fig5中I≥21时几何更相似，低spin两g7/2 holes对齐过程不同是作者解释，仍为模型几何。

目标thesis两路均Ii20、If18，若完整EM输出可得，共同Wigner–Eckart分母消去；同一算符的全局Q0也可消，但γ、态混合、截断及端点身份不消。须给20+_D5C、18+_D5C、18+_D5与实验Ei/link的明确对应，不用邻近spin或普通带内比替换。实验比的τ/globalreference可消，不因此要求先测τ；它的gate/响应/Cov边界另在thesis源页，不生成CI。

## Competing Interpretations and Limitations

实验点复用PE18 Ref20，不是新采集；thesis为同campaign更细账本而非第三份独立证据。作者强调仅D5双方有实测比、其它四组需进一步实验，摘要整体成功不能覆盖局部失败。v1 TableI把D6 parity印为+，与另一source的assignment差别保留，未静默改表或据此否定D5；VoR尚未核。未取得每I实际cutoff、全部带符号波函数和两个E2输出，目标模型prediction仍`not supplied`。

## Extracted Pages

- [[chirality-shape-coexistence-companion-matrix]]：136Nd D5同parent E2设计与已发表模型输出的区别。
- [[135nd-chiral-partner-resolved-evidence-map]]：不同核/模型的相干EM能力与实际输出应逐项区分。
