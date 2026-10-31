---
type: source
title: "Wang2019 RAT-PRM：78Br八极软性输入、反射不对称模型与手征解释范围"
aliases: [Wang2019 RAT-PRM 78Br, arxiv1902.00191]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
source_type: preprint-theory
reading_depth: read
title_original: "Multiple chiral doublet bands with octupole correlations in reflection-asymmetric triaxial particle rotor model"
authors: [Y. Y. Wang, S. Q. Zhang, P. W. Zhao, J. Meng]
year: 2019
journal: Physics Letters B
volume: "792"
pages: "454-460"
doi: "10.1016/j.physletb.2019.04.014"
arxiv: "1902.00191v1"
citation_key: wang_2019_RATPRM78Br
canonical_source: "https://arxiv.org/abs/1902.00191"
source_url: "https://arxiv.org/pdf/1902.00191v1"
raw_file: "raw/papers/gpt/learning-daily/20261029-DAY27-cross-mass-region-transferability/wang-2019-rat-prm-78br-arxiv1902.00191v1.pdf"
raw_sha256: "cefe9aeb1fcf8be56c6808825faf95f486246254c231893320ee62f9a9907aae"
raw_storage_status: reserved-unpopulated-preprint-staging-only
public_staging_manifest: "outputs/literature-acquisition/20261030-day27-wang2019-rat78br.json"
analysis_status: versioned-arxiv-read-with-independent-worker-audit
nuclei: [78Br]
reactions: []
experiments: []
models: [reflection-asymmetric-triaxial-particle-rotor-model, covariant-density-functional-theory, Nilsson-BCS]
observables: [energy-spectrum, bm1-be2-ratio, be1-be2-ratio, effective-angle]
methods: [parity-projection, particle-rotor-diagonalization]
tags: [chirality, octupole-correlations, RAT-PRM, source-boundary, Day27]
---

# 78Br反射不对称粒子—转子模型的实际输入与结论

## Bibliographic Record

实际读取官方arXiv **1902.00191v1**：17页、340748字节、PDF指纹见frontmatter。arXiv提交日期2019-02-01，PDF内部日期2019-02-04；未据此发明v2。精确Crossref DOI核对关联期刊为Physics Letters B **792**, 454–460（2019），但本轮没有逐字比较最终期刊排版版本；下列locator均按v1的PDF页。

文件实际在 `tmp/day27-rat2019-audit/arxiv-1902.00191v1.pdf`；raw_file是未填归档槽，raw未写。独立worker获取、阅读、图像及报告在同一tmp目录；父代理核对指纹并读取关键参数/算符/解释段。一次v2请求404已保留，未用不一致的无版本预览作证据。

## Scope and Reading Depth

独立子代理实际读取17页：正文主线1–14、参考文献14–17；视觉检查Figs.1–5、关键公式。父代理另外读取PDF6/7/12/13文字并视觉核PDF6的算符和参数段；不声称父代理独立重算RAT-PRM谱或通读所有参考原件。输入/结果的范围检查与数值复现是两回事。

## Paper Question and Scientific Motivation

作者构建带准质子、准中子、反射不对称三轴转子的模型，联合讨论78Br正负宇称双带、带间E1及角动量几何。目标是扩展对八极关联的描述，并非给全部核素一条β3禁戒手征阈值。

## Method and Design Logic

Nilsson单粒子场、配对和转子耦合 → 构造好总角动量与总宇称的基 → 对角化能谱及波函数 → 用M1/E2/E1算符求跃迁 → 与既有78Br数据比较 → 从量子角动量分量及effective angles解释几何。形变和有效角度为模型量，不是直接测得的经典矢量。

## Summary

本RAT-PRM应用用非零八极输入模拟软势中的关联，计算正负宇称带和E1连接，并对负宇称带讨论手征几何。它没有测量静态梨形，也没有报告β3>0.1的扫描或提出普适β3排除线；其特殊理想极限的额外quartet选择定则也未在这篇应用文中建立。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| W19-D27-R047-1 | MDC-CDFT给β2=0.28、γ=16.3°及β3=0；因势能面对β3软，RAT-PRM采用β3=0.02表征八极关联。这是固定模型输入，不是实测静态β3。本文未提供β3>0.1的解或阈值扫描，不能称其证明或反驳0.1数值排除线。 | model-input-and-coverage-boundary | direct-v1-and-visual | PDF6, Sec.III first paragraph; mainline PDF1–14 | true |
| W19-D27-R047-2 | J0=14 ħ²/MeV及核芯宇称分裂E(0−)=3 MeV按实验能谱调整；配对gap取12/√A。图中实验数据来自Ref.11即Liu2016，不是本篇新实验，不能重复计独立谱学证据。 | fitted-model-parameters-and-independence | direct-v1 | PDF7 Sec.III and Fig.1 caption; PDF14 Ref.11 | true |
| W19-D27-R047-3 | 基底包含总宇称投影和角动量耦合；Eq.(18)给M1有效g因子，E2主要取核芯项，而E1不能略去价核子项，并采用质心反冲修正有效电荷。不能凭“D2×PT”简写替代具体哈密顿量、基底及算符，进而无条件保证跨带严格零值。 | model-construction-and-task-boundary | direct-v1-plus-explicit-inference | PDF5 Eqs.(13)–(17); PDF6 Eqs.(18)–(20) | true |
| W19-D27-R047-4 | Eq.(21)用角动量期望值定义effective angles；带头近90°也可出现在chiral vibration，因为转子角动量较小。角度或RMS分量不独立证明静态左右局域化。 | geometric-diagnostic-limitation | direct-v1 | PDF12 Eq.(21) and last paragraph | true |
| W19-D27-R047-5 | 正宇称带的总角动量接近i–s平面；负宇称带几何被作者解释为手征。非零固定反射不对称输入与该模型手征解释可共存，但不因此确证真实核素静态八极或理想四重近简并。 | author-model-interpretation-and-boundary | direct-v1 | PDF9–11 Figs.3–4; PDF13–14 Summary | true |
| W19-D27-R047-6 | 计算B(E1)/B(E2)通常低估数据，γ从约16°改至21°会增强E1。负宇称主组态改为πg9/2⊗νf5/2，与先前πf5/2⊗νg9/2解释不同；作者要求微观计算或g因子测量进一步支持。 | competing-configuration-and-model-limitation | direct-v1 | PDF9 Fig.2/discussion; PDF13 configuration and Summary | true |

## Competing Interpretations and Limitations

这一模型不是理想chirality–parity对称极限的普适选择定则论文。它的相反宇称谱、有限核芯宇称分裂、可变组态和E1算符贡献需一起评估；量子基底中的好宇称与内禀非对称输入并不矛盾。β3=0.02的结果不能回答β3>0.1是否在其它条件下兼容手征；缺少大β3计算是覆盖缺口，不是反证。

## Knowledge Impact and Learning Decision

`limits` [[chiral-octupole-tac-coupling-and-planar-restoration]] 的跨核阈值、真实角度/势垒与quadruplet认证；`supports` [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] 对八极软性和模型解释的分层；`competing-interpretation`为负宇称组态重排及其可检验g因子路线。保留source及现有研究note纠错，不生成新的全核区相图。QMD/overview在本主题纠错完成后批量处理，不把该理论与原实验重复计数。

## Extracted Pages

- [[chiral-octupole-tac-coupling-and-planar-restoration]]：角度势代数与真实TAC/PRM输入合同分开。
- [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]]：同一实验数据的后续模型解释，保留source依赖。

## Human Review Triage

保持unreviewed，本轮为agent self-audit。文件身份、哈希、读图和locators已核；没有复现模型数值。P1：未核最终期刊版、β3大值未扫描、负宇称组态与其它模型不同、E1/E2拟合残差和几何定位边界。任何更强的精确transition zero规则须另找真实理想极限推导，不借此文补写。
