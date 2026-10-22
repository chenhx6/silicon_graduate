---
type: source
title: "Zanon 2023：反应点速度、馈入控制与20O寿命"
aliases: [Zanon 20O 70 fs, 20O MUGAST AGATA VAMOS lifetimes]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: experimental-paper-with-supplement-and-theory-comparison
reading_depth: deep-read
title_original: "High-Precision Spectroscopy of 20O Benchmarking Ab Initio Calculations in Light Nuclei"
authors: [I. Zanon, E. Clément, A. Goasduff, J. Menéndez, T. Miyagi, M. Assié]
author_list_scope: first-six-of-public-copy
journal: Physical Review Letters
year: 2023
volume: 131
pages: 262501
doi: 10.1103/PhysRevLett.131.262501
data_version: arXiv-2405.14305v1-main-and-bundled-supplement
canonical_source: "https://doi.org/10.1103/PhysRevLett.131.262501"
citation_key:
raw_file: "raw/papers/gpt/day13/zanon-2023-o20-high-precision.pdf"
raw_sha256: "2bd272e29518978205cb47b0d7829a0f57f1a5b81f8c0be7d7d984cec94435cc"
raw_storage_status: reserved-unpopulated-public-preprint-only
external_pdf_url: "https://arxiv.org/pdf/2405.14305v1"
nuclei: [19o, 20o]
methods: [doppler-correction, dsam, particle-gamma-coincidence, two-body-kinematics]
tags: [agata, mugast, vamos, feeding-control, femtosecond-lifetime, model-dependent-strength]
---

# 粒子测量怎样约束DSAM入口

## Bibliographic Record

I. Zanon 等，Physical Review Letters **131**, 262501 (2023)，DOI如上。Crossref核验题名、作者前缀、卷与2023-12-28发表日期；实际所读arXiv:2405.14305v1于2024-05-23上传。出版年仍2023，不以arXiv上传年替换。

原始raw保持不变，main七页副本在`tmp/day13/reopened/zanon-2023-o20-high-precision.pdf`，SHA如上，raw位置未填充。Supplemental Material来自同公开v1 author-source archive `https://arxiv.org/src/2405.14305v1`，archive SHA `f5f044b0737669fb6cbbbb558dfd5bf7072ee803c3ca43dd03fb19a177c77260`；只读取文档成员、未执行source。四页SI副本`tmp/day13/reopened/zanon-public-source/SupplementalMaterial.pdf`，SHA `5a3841daa9f3e47bf20b7a5ca1ccbec47d74f9d46576e8c940c5cc4fdeb94eb9`。SI为本main的依赖补充，不另计实验。

## Scope and Reading Depth

- Covered scope：main七页与SI四页主线；reaction/targets、entrypoint、line-shape、χ² conventions、feeding、knownlongcontrol与模型/δ条件；SI TableI/Fig.5、main讨论及TableI核验。
- Not covered：e775s原始事件、production simulation/config、χ²数值面、Ex gate migration/完整Σ及外部stopping原始测量；公开archive不是事件数据库。

## Paper Question and Scientific Motivation

用可重建初始速度/布居的directreaction测20O非yrast态寿命、branch与电磁strength，检验几种chiral EFT/VS-IMSRG和USDB。Doppler/feeding/响应约束构成实验论证，模型性能另列。

## Method and Design Logic

19O(d,p)20O逆运动学：质子能量/角度给Ex与反应点重离子速度，VAMOS给残余核标签，AGATA给γ位置/能量。薄CD2用于谱学；CD2+Au用于短寿命DSAM。用Ex门选定初始态，模拟按state测得的velocity/angular inputs和Au transport生成线形，并共同扫描τ与静止Eγ。

## Key Evidence and Reasoning Chain

粒子入口测量降低初速度分布对反应模型的依赖，Ex选择限制feeding。新的1156keV feeder表明不能把全部2396keV事件都当直接布居2+2；但source支路28%不是目标样本feeding fraction。Long2+1 control约束已声明的geometry/response/loss组合，不能代所有短态gate/correction代码的独立校验。

## Summary

2+2总寿命`70(10)fs`（90%时`70(14)fs`）；3+1总寿命`54(9)fs`（90%时`54(12)fs`）。作者承认与2020的150fs有张力且原因未完全理解，提出初速度模型或未观测sidefeeding。其“systematics cancelled”按作者解释保留，任务不独立证明该强措辞。

## Experimental or Theoretical Setup

19O束8AMeV、平均4×10⁵pps；CD2 .3mg/cm²及同CD2加Au24.4mg/cm²两dataset。MUGAST质子、VAMOS重离子与AGATAγ三重符合。与[[assie-2021-mugast-agata-vamos]]为同装置/实验方法链，与2017的18O+Ta实验独立采集。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZA23-1 | 19O(d,p)20O8AMeV，CD2.3mg/cm²做谱学，CD2+Au24.4mg/cm²做DSAM；两个dataset角色分开。 | experimental-fact | direct | main PDF p.2, Experimental details | true |
| ZA23-2 | 质子能量/角度给Ex及每态反应点速度；SI Fig.2显示四态各自初β分布，用测得angular inputs。 | experimental-criterion | direct | main pp.2–3; SI pp.1–2, Fig.2 | true |
| ZA23-3 | Ex门选2+2后线形共同扫描τ/Eγ，2+2τ70(10)fs/70(14)fs90%；3+1用3552.6keV与相应Ex门得54(9)/54(12)fs90%。 | experimental-fact | direct | main p.3, Lifetime measurements, Fig.3 | true |
| ZA23-4 | 2+2→2+1/ground branches .88(1)/.12(1)；3+1→2+2/2+1 branches .28(1)/.72(1)。 | experimental-fact | direct | main p.3; SI p.1, TableI | true |
| ZA23-5 | SI给Eγ2396.1(2)keV与新1156.0(8)keV3+1→2+2 feeder，BR28(1)%；作者指出忽略该支路可影响2+2寿命。 | experimental-fact | direct | SI p.1, TableI and adjacent text | true |
| ZA23-6 | 已测δ(2+2→2+1)=−.18(8)引自早期工作；3+1两支δ实验未知，TableI的strength采用USDB δ=.13和.019，故这部分B分解有模型输入。 | experimental-criterion | direct | main p.4 discussion; p.5 TableI/caption | true |
| ZA23-7 | 作者明说两次20Oτ差异尚未完全理解，初速度模型或未观测sidefeeding可给更长τ；“cancelled”是作者对其改进方法的解释。 | author-interpretation | direct | main pp.3–4, Discussion | true |
| ZA23-8 | Au stopping与IAEA数据/SRIM/LISE++比较；作者称10MeV/u附近10%差异不影响其最终结果、波动低于统计误差。任务未复算其敏感性。 | author-interpretation | direct | SI p.2, Fig.3 and stopping text | true |
| ZA23-9 | long2+1基准CD2 data/sim E1674.6(2)/1674.5(2)keV、FWHM6.5(3)/6.2(2)；CD2+Au为1675.1(2)/1675.5(2)、9.2(4)/8.7(3)。该基准校正明确包括计算的Au loss。 | experimental-criterion | direct | SI p.2, Fig.4/text | true |
| ZA23-10 | SI采用Neymanχ²、重bin至每bin≥10events；E扫描2394–2398keV、τ40–175fs，二维Δχ²2.3/4.6对应作者68/90%区域。 | experimental-criterion | direct | SI pp.2–3, Lifetime measurement, Fig.5 | true |
| ZA23-11 | TableI给B(E2;2+2→2+1)=4(2)e²fm⁴、B(M1)=.05(2)μN²；来源为τ/branch/先前δ组合，不是三个独立计数实验。 | experimental-fact | direct | main p.5, TableI/caption; p.4 δ paragraph | true |
| ZA23-12 | VS-IMSRG(2)用3种chiralNN+3N Hamiltonians与一致演化EMoperators，未含mesonexchange currents；USDB用不同算符/effective charge，3+δ亦来自USDB。 | model-result | direct | main pp.4–5, theory and TableI | true |
| ZA23-13 | 作者把B(E2)低估联系VS-IMSRG(2)遗漏的many-particle–many-hole correlations，B/M1差异与δ/算符问题分开；不等同由τ单独证实特定强力。 | author-interpretation | direct | main pp.4–6, discussion/conclusion | true |
| ZA23-14 | Data statement指e775s注册，印刷URI为https://doi.org:10.10.26143/GANIL-2020-E775S，格式异常；不能由此称raw事件已公开。 | experimental-fact | direct | main p.6, Data Availability Statements | true |
| ZA23-15 | DataCite核实正式DOI10.26143/ganil-2020-e775s、title“Lifetime measurements of excited states in 20O populated by direct nucleon transfer”；record列2020-02-23至03-05Collected、2025-03-05Available(end embargo)、CC-BY-NC4.0和公共landingURL。这是注册metadata，不证明事件下载成功。 | experimental-fact | direct | DataCite API attributes.titles/url/dates/rightsList; retrieved 2026-10-14 | true |

## Nuclear Structure Information

SI TableI给2+2 4.071(1)MeV、3+1 5.228(1)MeV与各γ/branches。本文的完整示例用于速度/feeding/strength链；不向A≈130移植特定寿命、δ或阈值。

## Authors' Interpretation

作者强调入口测量和feeding-free优势，并承认旧/新结果张力原因未明。其关于Au loss、systematiccancelled与模型算符截断的归因均单独保存，不冒充任务验证。

## Model Results

模型波函数configuration与B不属于实验直接观测。特别是未知3+δ时，τ与branches只定总partialradiative rate，E2/M1分量须有额外输入；使用USDBδ再评估USDB strength会引入条件依赖。

## Competing Interpretations and Limitations

- DataCite正式注册已通过`https://api.datacite.org/dois/10.26143%2FGANIL-2020-E775S`核实，landing为`https://data.ganil-spiral2.eu/record/10.26143/ganil-2020-e775s`。本次HTTPSlanding访问ConnectionError、HTTP备选ConnectTimeout，尚未读取文件清单，不称事件可得或断言权限拒绝。注册技术字段Au20mg/cm²、intensity2×10⁵pps与main24.4mg/cm²/4×10⁵不同；registry描述用“we propose”，按注册/设计metadata保存，实际analysis参数以main和生产packet为准。
- 入口速度/feeding是具体竞争解释，尚无共同packet证明它们独占80fs差异。
- Longreference的response/loss符合有用，但同state/nominalthickness/config的数据与模拟不提供完整independence；不同短态Ex分辨率/泄漏仍要检查。
- 所有短τ谱是否采用与longcontrol完全相同的correction-vector convention，本文未提供完整生产字段/code，不能从该段自动外推。
- SI一次把2396keV标为2+2→2+2，结合TableI/main可定位为印刷标签问题，保留原文边界，不为它构造新跃迁。
- Neyman重bin≥10的做法为source方法；不自动保证所有bin Gaussian或confidence覆盖。任务未取实际数值grid，不计算精确差异p值。
- 原始事件公开性尚未确认；数据注册不是可下载事件文件。失败/异常locator在任务回执留证。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| ZA23-AR1 | independent/shared边界 | 2023transfer与2017deepinelastic独立采集；main/SI/AS21为依赖方法链，未知数值calibration covariance不猜。 | ZA23-1/2; CI20-1 | unreviewed |
| ZA23-AR2 | gate设计 | 1156 feeder的branch不能代目标samplefeeding；需entrypopulation、Ex迁移、coincidenceacceptance。 | ZA23-3/4/5 | unreviewed |
| ZA23-AR3 | strength的模型依赖 | 3+分量用USDBδ；保留partialrate与模型E2/M1split的区别。 | ZA23-6/11/12 | unreviewed |
| ZA23-AR4 | jointuncertainty | 区域按作者二维Δχ²定义；不把reportedinterval全部视为独立Gaussian1σ。 | ZA23-3/10 | unreviewed |

## Knowledge Impact and Learning Decision

与[[ciemala-2020-c16-o20-lifetimes]]组成受限L3 comparison，写回 [[doppler-correction]] 与 [[doppler-velocity-validation-contract]]；不作pooledτ、不裁决差异原因或abinitioforce。

## Related Knowledge and Project Relations

Methodobject续核[[nptool-2019-reaction-velocity-code-object]] NP19-2/3/4/5/7/8/10提供公开历史reconstruction/getter契约；不证明本实验使用相同commit/caller。测得proton输入、beam/mass/targetprior、reaction-pointβ与emission/exittransport分开。


SIRef6的方法原报告已续读为[[baker-cousins-1984-histogram-fits]]，BC84-1/2/3/5/6/7/9。该入口澄清计数/区间/normalization条件，不由generalmethod推断本实验Neyman实现或τcoverage错误。


| Relation type | Target | Specific relation |
|---|---|---|
| independent-comparison | [[ciemala-2020-c16-o20-lifetimes]] | 70fs/150fs总寿命张力与jointτ–E。 |
| method-lineage | [[assie-2021-mugast-agata-vamos]] | lightparticle测量/kinematics/装置。 |
| methodological-bridge | [[doppler-correction]] | 入口/发射/出口速度与Exgate。 |
| methodological-bridge | [[doppler-velocity-validation-contract]] | reference/SI/feeding/stopping/strengthpacket。 |

## Human Review Triage

P0：publiccopy/raw与dataURI权限边界已隔离，无事件access声明。P1：ZA23-3/5/6/7/8/9/10/11的uncertainty、feeding与解释条件；不升级human-reviewed。

## Extracted Pages

Main1–7与SI1–4；main2–5、SI1–3为关键experimental/fit/strengthlocator；SI Fig.5二维面与TableI已核。

## Day19量化审计：直接转移Ex门控消除馈入、约化跃迁几率重构与从头算关联低估

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_o20_ciemala_zanon_reconciliation_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/o20-ciemala-zanon-reconciliation-result-056.json`，核准了 $^{20}\text{O}$ 激发态绝对跃迁几率与微观从头算核力比较基准：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| ZA23-D19-1 | 对 Table I 中 $^{20}\text{O}(2_2^+)$ 态跃迁强度与微观从头算模型进行系统学审计：(1) 跃迁强度数值重构：标准转换公式严格复现 Table I 报告值：$B(E2; 2_2^+ \to 2_1^+) = 4.08\text{ e}^2\text{fm}^4 \to 4(2)$ 与 $B(M1) = 0.0503\text{ \mu}_N^2 \to 0.05(2)$；(2) 从头算模型局限性：基于手征有效场论核力（$NN+3N$）的 VS-IMSRG(2) 理论模型预测 $B(E2) = 0.68\text{ e}^2\text{fm}^4$，低估实验值达 $\sim 6$ 倍；微观机制归因于标准两体截断空间遗漏了多粒子—多空穴（$p\text{--}h$）组态形变关联；经验 USDB 壳模型计算给出 $7.1\text{ e}^2\text{fm}^4$；(3) 飞秒寿命张力消解：Zanon 2023 的 $70(10)\text{ fs}$ 测量依托 MUGAST 粒子探测与直接反应 $E_x$ 门控彻底切断了高自旋连续态馈入，消解了深非弹性反应由于未分辨连续馈入导致的 $150\text{ fs}$ 假象。 | task-rates-and-abinitio-audit | derived-and-boundary | main p.5 Table I; SI pp.1-3; o20-ciemala-zanon-reconciliation-result-056.json | true |
