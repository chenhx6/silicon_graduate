---
type: source
title: "Wang 2017：109Ag 的 TAC-CDFT 可分离配对方法"
aliases: [Wang 2017 109Ag separable pairing, TAC-CDFT separable pairing 2017]
created: 2026-10-15
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
source_type: journal-article-theory-and-method
reading_depth: deep-read
title_original: "Yrast band of 109Ag described by tilted axis cranking covariant density functional theory with a separable pairing force"
authors: [Y. K. Wang]
journal: Physical Review C
year: 2017
volume: 96
pages: 054324
doi: 10.1103/PhysRevC.96.054324
arxiv: 1708.06117v2
language: en
canonical_source: "https://doi.org/10.1103/PhysRevC.96.054324"
citation_key: ""
raw_file: "raw/papers/2017-Wang-109Ag-TAC-separable-pairing.pdf"
raw_sha256: 15e901a4f5d8ad1b5cf4bffe61e050d8eb6a3c89b0f9f62dea84e5d56c335d87
nuclei: [109Ag]
reactions: []
models: [tilted-axis-cranking, covariant-density-functional-theory, relativistic-Hartree-Bogoliubov]
observables: [excitation-energy, angular-momentum, B(M1), B(E2)]
methods: [separable-pairing, quasiparticle-blocking]
tags: [pairing, tac-cdft, blocking, number-projection, model-input]
---

# Wang（2017）：109Ag 的 TAC-CDFT 可分离配对方法

## Bibliographic Record

Y. K. Wang, Physical Review C **96**, 054324 (2017)，DOI [10.1103/PhysRevC.96.054324](https://doi.org/10.1103/PhysRevC.96.054324)。Crossref 给出2017-11-27；arXiv 元数据给出 Yakun Wang、相同题名和精确 DOI，对应 [1708.06117v2](https://arxiv.org/abs/1708.06117v2)。所读为[公开预印本 PDF](https://arxiv.org/pdf/1708.06117v2)，9页，边栏印“6 Dec 2017”，首页另印“Dated: May 29, 2022”。保留这处版本日期差异，不据排版日期改写发表年。

本次按 daily-learning 授权建立可追溯来源记录；**未完成 raw 归档摄入**。`raw_file` 是尚未填入的保留槽，不是实际现存文件。实际只读输入为 `tmp/day14-20261014/tac2017/PDFs/Yrast_band_of_109Ag_described_by_tilted_axis_cranking_covariant_density_functional_theory_with_a_separable_pairing_force.pdf`，525900 bytes，SHA256 如 frontmatter；下载器 manifest、独立 PDF/hash/首页核验与阅读回执位于 DAY14 run-02。未改 raw 或 BibTeX，citation key 未在本地 BibTeX 匹配，故留空。以下页码均为这份预印本的 PDF 页，未核正式排版或 erratum。

## Scope and Reading Depth

- **Covered scope**：沿全文9页主线读 Introduction、理论框架、数值实现、结果和 Summary；视觉核 Figs.1–8、影响判断的 Eqs.(4)、(10)–(12)、(19)–(28)，以及 Appendix A 的基底、选择条件和矩阵元结构。本文没有独立 table；Fig.7 的 canonical-basis 贡献也核过。
- **Not covered**：未复跑作者 RHB 程序；没有实际 occupied/blocked 清单、轨道追踪日志、收敛路径、数目投影输出或计算协方差。Ref.[31] 的 blocking 算法和 Ref.[36] 的原始实验只是已识别上游文献，尚未据本页冒充直接读取。未请求 SI。
- 入口回忆已受136Pr TableII及既有 HFB 概念 priming；正文前回忆已先保存。页级 `unreviewed`、全部 claim `needs_review: true`；没有用户审核。

## Summary

论文把有限程可分离 Gogny 型配对引入 TAC-CDFT/RHB，用109Ag 的1qp和3qp yrast结构检验能量、角动量与电磁量。配对改善部分比较，但回弯区未收敛；作者明示粒子数未恢复，磁矩 Dirac 项还需近似缩放。它提供方法输入和失效边界，不能补全136Pr 的真实阻塞清单，也不提供该核的新实验事实。

## Problem, Motivation and Method

与零程 monopole 配对相比，作者用有限程 form factor 避免紫外截断问题；与完整有限程 Gogny 力相比，可分离形式减少矩阵元计算。旋转系采用 `ω=(ω cosθω,0,ω sinθω)`，RHB 方程含 `hD−λ−ω·J`、配对场 `Δ` 与由 U/V 构造的密度和 pairing tensor。正常场与配对场自洽求解；Appendix A 说明倾斜推转破坏的空间对称性使更多配对矩阵元非零。这些是模型设计，不能从某个组态简称重建全部数值输入。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| W17-1 | TAC-RHB 方程以 `hD−λ`、推转项和Δ为块；配对场由两体矩阵元与κ构造，κ由准粒子U/V给出。 | theoretical-method | direct | PDF p.2 Eq.(4) | true |
| W17-2 | 可分离力含 `G δ(R−R′)P(r)P(r′)(1−Pσ)/2`，P为归一高斯形式；数值采用G=−738 MeV fm³、a=0.636 fm。spin projector只说明S=0，不能单由该式读出实际isospin/pn实现。 | theoretical-method-and-scope | direct-and-derived | PDF p.2 Eq.(11) | true |
| W17-3 | 109Ag低/高自旋段分别用πg9/2^-1与πg9/2^-1⊗νh11/2²；迭代不同λ/ω时追踪并阻塞准粒子轨道以维持组态，细法回指Ref.[31]。本文不提供136Pr的阻塞输入。 | model-input-and-boundary | direct | PDF p.3 Sec.III | true |
| W17-4 | J由内禀期望值分量求得，并通过`⟨J⟩·⟨J⟩=I(I+1)`作半经典对应；time reversal与signature被破坏，作者称parity为保留的好量子数。这不是good-I投影态。 | theoretical-method | direct | PDF p.3 Eq.(19) | true |
| W17-5 | 作者明示Bogoliubov变换下粒子数不守恒，讨论数目恢复可能改善1qp/3qp带头能差，未在本工作实施；单粒子能误差也是作者保留的替代原因。 | author-stated-limitation | direct | PDF p.4 Sec.IV | true |
| W17-6 | PC-PK1配合12主壳；在ℏω=.35 MeV的12→14壳比较中，总能量和总角动量变化分别在.021%和.020%内。这个局部数值检查不认证全部频率、分支或电磁量误差。 | numerical-method-and-scope | direct-and-derived | PDF p.3 Sec.III | true |
| W17-7 | 约I=7.5ℏ至11.5ℏ回弯区未取得收敛解；该区以外配对使固定频率下的计算角动量降低，更接近所比较数据。 | model-result-and-failure | direct | PDF p.4 Fig.3 discussion | true |
| W17-8 | Figs.4–7给出1qp的l–i平面与3qp的l–s平面转轴及质子/中子角动量组成，配对对1qp取向和低j中子对齐作用较大；这些方向和canonical分量均为模型结果。 | model-result | direct | PDF p.5 Fig.4 | true |
| W17-9 | Fig.8同时比较有/无配对和额外Dirac磁矩项缩放；正文用.58因子近似处理该项的有效质量/回流效应。它不是把全部B(M1)统一乘.58²，也不能只凭减小的B(M1)唯一识别配对。 | model-result-and-operator-boundary | direct-and-derived | PDF p.7 Fig.8 | true |
| W17-10 | 所读v2 Eq.(25)中段为`3μ⊥²/(8π)`，最后一项却印`3(μx sinθJ−μz cosθJ)/(8π)`而无平方。按该分量为μ⊥的读法，两端维度/缩放不一致；这是版本字面边界，不判作者实际代码。 | literal-formula-and-our-audit | derived | PDF p.3 Eq.(25) | true |
| W17-11 | v2 A18印`n=Nμ−nγμ−nδμ`，A19的Kronecker条件为`nγμ+nδμ=n+Nμ`；按同一非负相对谐振子量子数解释，对非零n不能普遍兼容。保留两式，不当已核官方勘误。 | literal-formula-and-our-audit | derived | PDF p.8 Eq.(A18) | true |
| W17-12 | p.7以0.87 MeV与1.26 MeV比较中子配对隙并称“20% smaller”；按后者作分母直接算为约30.95%。当前只保留数值/百分数字面不一致，不修作者结果。 | literal-numerical-and-our-audit | derived | PDF p.7 neutron-gap paragraph | true |
| W17-13 | 文中实验比较点回引Datta等PRC78,021306(2008)，方法回引Zhao等PRC92,034319(2015)。本页是109Ag方法论文而非136Pr新采集；Lv2025共用方法作者也不增加该核独立实验数。 | source-lineage-and-boundary | direct-and-contextual | PDF p.9 Ref.[36] | true |

## Competing Interpretations and Limitations

支持“配对改善比较”的是同一模型中开/关配对的控制；限制来自带头仍有差异、回弯区未收敛，以及Fig.8中磁矩算符选择的额外影响。不能把“能量、B(E2)、B(M1)部分接近”合成唯一组态证明。

## Counter-Evidence and Missing Companion Observables

所需伴随输入包括完整阻塞轨道、reference/spectator定义、准粒子态追踪准则及日志、不同频率和基空间的收敛检查；若据电磁量区分机制，还需明确磁矩算符、寿命/分支导出的量与其误差及协方差。本页没有这些136Pr输入。Eq.(11)的S=0 spin projector也不替代对实际配对species通道的说明。

## Analytical Reconstruction

[[configuration-occupation-audit]] 中“配对方法companion不能补全实际阻塞输入”给出可复现练习：用源a归一Eq.(12)，检验S=0 projector，并以声明的有限Fock空间区分数目期望、number parity与blocking；另以声明磁矩分量说明只缩放Dirac项不等于整体缩放B。这些构造不是作者波函数，不修136Pr的任何组态列。

Eq.(25)、A18/A19及百分数字面问题均已视觉回查。计算只检验所读版本的内部一致性；未取得代码或正式版本前，不把任何一项升级为模型输出错误或实验事实。

## Related Knowledge and Project Relations

- `methodological-bridge` → [[configuration-occupation-audit]]：把组态简称、配对/阻塞定义与完整可重放输入分开。
- `limits` → [[tilted-axis-cranking]]：保留半经典I、数目未恢复、局部收敛和算符依赖。
- `not-direct-evidence` → [[a130-model-choice-card]]：可借鉴方法输入契约，但不提供136Pr实际blocked/spectator或新PSM/TPSM覆盖。
- [[lv-2025-136pr-tac-covariant-density-functional]] 的Ref.[44]是本方法；两者核素、基空间与实际组态不同。

## Knowledge Impact and Learning Decision

Decision: **supports** 配对与阻塞是独立必要输入；**limits** 从拟合曲线或“unpaired”简称恢复完整模型态。持久化到本source、已有occupation方法页、TAC模型页和model-choice卡，不新建109Ag核素/研究note。原136Pr Q1/Q1*缺口仍开放；原PSM/TPSM覆盖2/7不变。overview update deferred：当前为一条方法证据链的校准，没有需要另建全库地图的变化。

## Agent self-audit triage

- **P0: none identified**。输入身份、公开来源和hash已核；raw未归档是显式边界。
- **P1 / W17-3、W17-5**：Sec.III与p.4给出blocking/未恢复数目，但未给实际清单；不能替136Pr填reference或spectator。最高信息下一步是Ref.[31]的实际追踪定义或136Pr公开输入。
- **P1 / W17-9**：Fig.8与Eq.(28)的缩放仅作用于Dirac项；按整个B统一乘因子会改变模型比较含义。
- **P1 / W17-10、W17-11、W17-12**：保留上述精确locator和版本，暂不用于实际RHB复现公式；正式排版/勘误尚未核，不制造已确认代码错误。
- **P2**：空citation key和raw保留槽随lint显式报告；不修改Bib或凭据。

## Extracted Pages

- Methods: [[configuration-occupation-audit]]
- Models: [[tilted-axis-cranking]]
- Projects: [[a130-model-choice-card]]

## 上游阻塞方法的后续核验

后续已直接读取本页Ref.[31]的[[zhao-2015-pairing-spin-orientation-tac]]；ZT15-3、ZT15-4给出分开最大化O1/O2和继承/反转blocked标记。[[configuration-occupation-audit]]固化其43-check实canonical/BdG控制与phase/tie/zero-norm/reference重放缺口。这个后续来源缩小方法定义缺口，不改本页既有claims/review，也不补Pr136实际轨道或增加独立实验。

## Provenance

- [Crossref](https://api.crossref.org/works/10.1103/PhysRevC.96.054324)：精确DOI、作者、题名、卷/文章号和发表日期。
- [arXiv v2 PDF](https://arxiv.org/pdf/1708.06117v2)：本页全部科学locator；SHA256如frontmatter。
- [阅读核验回执](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac2017-reading-audit.json)与[50-check练习](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac-pairing-contract.json)。
