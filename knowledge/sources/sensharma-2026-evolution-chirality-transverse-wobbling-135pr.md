---
type: source
title: "Sensharma 等 2026：135Pr 中从横向摇摆到手征的演化"
aliases: [Sensharma 2026 135Pr chirality, evolution of chirality from transverse wobbling 135Pr]
created: 2026-09-13
updated: 2026-10-25
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Evolution of chirality from transverse wobbling in 135Pr"
authors: [N. Sensharma, U. Garg, Q. B. Chen, S. Frauendorf, S. Zhu, J. Arroyo, A. D. Ayangeakaa, D. P. Burdette, M. P. Carpenter, P. Copp, J. L. Cozzi, S. S. Ghugre, D. J. Hartley, K. B. Howard, R. V. F. Janssens, F. G. Kondev, T. Lauritsen, J. Li, R. Palit, A. Saracino, D. Seweryniak, S. Weyhmiller, J. Wu]
journal: Physical Review C
year: 2026
volume: 113
pages: 024313
doi: 10.1103/3g4p-ncjn
arxiv: 2403.10749
language: en
canonical_source: "https://doi.org/10.1103/3g4p-ncjn"
zotero_item_key:
citation_key: Sensharma_2026
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
zotero_uri:
library_file: "raw/papers/gpt/learning-daily/20260912-PREPLAN-135pr-refresh/sensharma-2026-135pr-chirality-wobbling.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260912-PREPLAN-135pr-refresh/sensharma-2026-135pr-chirality-wobbling.pdf"
raw_sha256: "294f791a230a12005ef43a237afb25b9bf731f8f520a1a65d6b32d0386ef91b3"
nuclei: [135pr]
reactions: ["123Sb(16O,4n)135Pr"]
experiments: [atlas-digital-gammasphere-135pr-o16-80mev]
models: [quasiparticle-triaxial-rotor-model, triaxial-projected-shell-model, constrained-relativistic-density-functional-theory]
observables: [energy-levels, angular-distribution, multipole-mixing-ratio, interband-e2-strengths, bm1-be2-ratio, wobbling-energy]
methods: [gamma-gamma-coincidence, angular-distribution, dco-ratio, multipole-mixing-ratio]
tags: [a130, 135pr, chirality, transverse-wobbling, chiral-vibration, gammasphere, qtr, tpsm]
---

# Sensharma 等（2026）：`135Pr` 中从横向摇摆到手征的演化

## Bibliographic Record

N. Sensharma 等，*Evolution of chirality from transverse wobbling in `135Pr`*，*Physical Review C* **113**, 024313 (2026)，DOI `10.1103/3g4p-ncjn`，arXiv `2403.10749`。Crossref 给出 2026-02-09、卷 113、期 2、article 024313；arXiv v2 题名、作者首位、摘要和 journal reference 与该元数据一致。本地 arXiv PDF 为 17 页、6330099 bytes，SHA-256 为 `294f791a230a12005ef43a237afb25b9bf731f8f520a1a65d6b32d0386ef91b3`。

## Scope and Reading Depth

- `deep-read`：全文 17 页完成文本主线阅读。
- 视觉核对：PDF p.1 题名/摘要；pp.2–6 实验、Fig.2–5 和 Table I；pp.8–13 QTR、SCS/transition-probability 比较；pp.14–15 对 Lv 等批评的 χ² 复核、Fig.12–13 和结论。
- 重点检查：DB1/DB2 的新连接跃迁、MCMC angular-distribution mixing ratios、当前实验是否有 polarization、QTR/TPSM 输入、DB1/DB2 energy crossing、对 Lv 2022 的回应以及绝对强度限制。
- 未覆盖：原始 Gammasphere event tree、逐环效率文件、角分布原始计数和未公开的完整计算输入；论文自身也没有给出新实验的 polarization measurement 或绝对 lifetime。
- 版本边界：本地是 arXiv v2；期刊 DOI、article number 和作者信息由 Crossref 核验。文章所称“refute”是作者对相关批评的解释，不等于本 Wiki 已完成统一重分析。

## Summary

论文把 `135Pr` 中两个已知 dipole bands（DB1、DB2）作为同一高统计 `123Sb(16O,4n)` Gammasphere 数据谱系中的新研究对象，新增五条 DB2→DB1 的 `ΔI=1` 连接，并对三条最低能连接做 angular-distribution/MCMC mixing-ratio 提取。三条新测连接得到小 `|δ|`，作者据此称其为主要 dipole，并结合近简并、QTR 几何和相对跃迁概率，把 DB1/DB2 解释为手征伙伴；文章同时沿用先前工作把相关序列解释为 transverse wobbling，并专门回应 Lv 2022 对 747、813 和 754 keV 旧连接的双解批评。当前结论应分为“新增 DB1/DB2 连接的实验事实”“作者的 chiral interpretation”“对既有 wobbling 判据的作者反驳”三层。

## Experimental and Analysis Chain

80 MeV `16O` 束流轰击 `697 μg/cm²` 富集 `123Sb` 靶，前有 `15 μg/cm²` Al 层；本次 Gammasphere 可用 63 个 Compton-suppressed HPGe，采用 triple-coincidence acquisition，并把本次数据与此前 run 合并为约 `2.5×10^10` 个三重及以上 γ coincidence events（PDF pp.2–4）。RADWARE 用于 γγ 矩阵和 γγγ cube。由于不同 run 的探测器数目不同，作者按每次 run 建立总效率文件并逐环修正角分布。

对 642.2、572.9 和 476.9 keV 三条最低能 DB2→DB1 连接，作者以 MCMC 采样 `a_2/a_4`，解 angular-distribution 中关于 mixing ratio `δ` 的二次方程，并选取 χ² 较低的物理解。当前实验未能做 polarization measurement，因此 Fig.2 的能级图中 DB1/DB2 的 parity 仍标为 tentative；角分布可以牢固约束这些连接的 multipolarity，但不单独完成宇称测定（PDF pp.4–6）。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | research_status | needs_review |
|---|---|---|---|---|---|---|---|
| SH26-1 | 实验使用 80 MeV `123Sb(16O,4n)135Pr`、`697 μg/cm²` `123Sb` 靶、`15 μg/cm²` Al front layer 和 63 个可用 Gammasphere Compton-suppressed HPGe；合并数据约有 `2.5×10^10` 个 fold≥3 γ coincidence events。 | experimental-fact | direct | multiple-dependent | PDF pp.2–4, Sec.II | completed | false |
| SH26-2 | DB1、DB2 两条 dipole bands 的既有放置得到确认，并新增五条 DB2→DB1 `ΔI=1` 连接；三条最低能连接为 642.2、572.9、476.9 keV。 | experimental-fact | direct | multiple-dependent | PDF pp.2–4, Fig.2–4, Table I | completed | false |
| SH26-3 | 三条最低能新连接的 angular-distribution/MCMC mixing ratios 分别为 `δ=-0.10(6)`、`-0.15(3)`、`-0.11(2)`；作者据小 `|δ|` 将其判为主要 dipole（M1+E2）。 | experimental-criterion + experimental-fact | direct | multiple-dependent | PDF pp.4–6, Fig.5, Table I | completed | false |
| SH26-4 | 当前新实验没有 polarization measurement，故 DB1/DB2 中能级的 parity assignment 在 Fig.2 中保留为 tentative；angular distributions 约束 multipolarity，不等同于独立的 parity measurement。 | our-inference | direct | single | PDF p.5, paragraph before Table I | completed | false |
| SH26-5 | DB1/DB2 在 `I=41/2` 附近最小能量差约 `17 keV`；在相同 `ω` 下 DB2 约多 `2ℏ` alignment，作者用 QTR 的角动量分布把高自旋区域联系到 chiral-rotation geometry。 | experimental-fact + model-result | indirect | multiple-dependent | PDF pp.5、8–10, Figs.6–9 | completed | false |
| SH26-6 | 论文从 mixing ratios 和相对强度得到 DB1/DB2 的相对 `B(E2)`、`B(M1)` 比值；QTR 对能量与部分 ratios 只有 fair/qualitative agreement，实验没有提供 partner-resolved absolute strengths。 | model-result + our-inference | direct | multiple-dependent | PDF pp.5、12–13, Figs.6、10–11 | completed | false |
| SH26-7 | QTR 使用 constrained relativistic DFT 给出的 `β=0.19, γ=22°`、`J0=25 ℏ²/MeV`、irrotational-flow inertia、约 `1.0 MeV` BCS gaps 及 `π(1h11/2)^1⊗ν(1h11/2)^−2` 配置；这些是模型输入/结果而非直接形变测量。 | model-result | direct | single | PDF pp.8–10, QTR setup and Figs.6–9 | completed | false |
| SH26-8 | 论文用 Fig.12 对旧的 746、812 和 754 keV angular distributions 计算 χ²，报告 `|δ|>1` 分支比 `|δ|<1` 分支有更低的 χ²，并据此反驳 Lv 对既有 wobbling links 双解的质疑。 | author-interpretation + model-result | direct | multiple-dependent | PDF pp.14–15, Fig.12 | completed | false |
| SH26-9 | 对 Lv 关于偏振的批评，作者称 Matta 2015 的正 asymmetry 只是对大 E2 admixture 的补充确认而非独立的 mixing-ratio extraction，并将当前结论建立在旧 angular-distribution data 的 χ² 选择上。 | author-interpretation | direct | multiple-dependent | PDF p.15, discussion after Fig.12 | completed | false |
| SH26-10 | 论文指出 QTR 与实验 ratios 的差异可能与约 `100 keV` 的未包含非对角矩阵元、DB1/DB2 状态混合有关；作者明确说 lifetime measurements 对获得 absolute reduced transition probabilities 和消除当前 ambiguity 很重要。 | our-inference + author-interpretation | direct | multiple-dependent | PDF pp.12–14, discussion before Fig.12 | completed | false |
| SH26-11 | 2026 论文与 Matta 2015、Sensharma 2019 共享/延续 `123Sb(16O,4n)` 80 MeV Gammasphere 数据谱系；合并数据、后续重分析和理论回应不能作为三个 independent experiments 计数。 | cross-source-synthesis | indirect | multiple-dependent | PDF pp.2、14–15；[[matta-2015-transverse-wobbling-135pr]]；[[sensharma-2019-two-phonon-wobbling-135pr]] | completed | false |
| SH26-12 | 本v2 TableI对旧side-to-yrast连接给746.3(9)、811.6(10)、754.2(7)keV，Ji→Jf分别17/2−→15/2−、21/2−→19/2−、25/2−→23/2−；delta为−1.40(+.14/−.12)、−1.63(+.02/−.03)、−2.16(+.06/−.05)。图12的另一delta标为−.59、−.52、−.40，未附这些另一根的误差。TableI图注明确all errors purely statistical。 | reported-data-and-error-boundary | direct | multiple-dependent | arXivv2 PDF5 TableI；PDF14 Fig12 | targeted-self-audit | true |
| SH26-13 | Fig12图注明确采用sigma/I=.2；纵轴标签log10(chi²)，不是Delta chi²或reducedchi²。正文承认两possible local minima并以较低者选分支；“one true minimum”须按作者global preference理解，不能把固定sigma切片自动当全部nuisance的profile或全部候选不存在。 | likelihood-display-and-condition | direct-and-self-audit | multiple-dependent | arXivv2 PDF14 Fig12/III.B；PDF15续段 | targeted-self-audit | true |
| SH26-14 | 官方arXivv2公开源码归档有29个regular members：26PDF、TeX、BibTeX、README；完整文件清单及26PDF的embedded-file检查未发现event、原始角度/效率表、Cov或fit program。TeX与绘图PDF是已发表表示，不能等同完整replay输入。文件名chiral_wobb_prc_V3.tex的V3不是arXiv版本号，实际归档v2日期2026-01-15。 | reproducibility-readiness-boundary | public-object-self-audit | single | https://arxiv.org/src/2403.10749v2；00README.json；chiral_wobb_prc_V3.tex | targeted-self-audit | true |
| SH26-15 | 正文SecII称角分布使用合并data并按两run的detector/live-time修ring efficiency；Fig12图注又引用早期Refs15/16。未给逐图event/run ledger，故可确认shared lineage，不能仅由caption证明Fig12与2015图逐event/逐角计数完全相同，也不能当新独立第三次确认。 | event-identity-boundary | direct-and-self-audit | multiple-dependent | arXivv2 PDF2 SecII；PDF3–4 angle correction；PDF14 Fig12；TeX164/435 | targeted-self-audit | true |
| SH26-16 | p4–5称先把a2/a4作independent parameters采样、解a2的二次式、用较低chi²选根并在附近继续采样。此文字不提供实验a2/a4的完整Cov、所有分支posterior权重或原fit code；proposal参数独立不等于观测/拟合结果独立。 | inference-readiness-boundary | direct-and-self-audit | multiple-dependent | arXivv2 PDF4–5 MCMC方法段；PDF17 Ref54/70 | targeted-self-audit | true |

## Chiral and Wobbling Interpretation

作者把 DB1/DB2 的近简并、same-spin band crossing、相对 `B(E2)`/`B(M1)` 行为、QTR 角动量分布和新 DB2→DB1 连接综合为 `π(1h11/2)^1⊗ν(1h11/2)^−2` 配置的 chiral-partner bands；在其叙事中，低/中自旋的 transverse chiral vibration 随自旋演化为 chiral rotation。该段是作者解释和模型结果，不是 parity-independent 的直接观测。

对于 transverse wobbling，作者继续依赖 Matta 2015/Sensharma 2019 的既有 E2-rich links、wobbling-energy systematics 和 phonon hierarchy，并以 Fig.12 的旧角分布 χ² 重分析回应 Lv 2022。2026 新增的三条 DB2→DB1 links 本身主要是 dipole character；它们增强了 DB1/DB2 的 chiral-band 讨论，但不能单独把“chirality”和“transverse wobbling”两个解释同时升级为无争议事实。

## Competing Interpretations and Limitations

- Guo 2021 comment 指出 Matta 2015 角分布可能同时允许 `|δ|>1` 与 `|δ|<1`，且正 polarization asymmetry 不能单独排除小 `|δ|`；Lv 2022 则用独立 JUROGAM `P-R_ac` 数据得到小 `|δ|`。2026 论文的回应是重新计算既有 Gammasphere data 的 χ²，而不是一套统一的三方 raw-data reanalysis。
- 当前 2026 run 没有 polarization，因此 DB1/DB2 parity 仍 tentative；角分布的 dipole/electric character与宇称证据必须分开。
- 新论文只有相对 transition-probability ratios，没有 partner-resolved lifetime、absolute `B(E2)`/`B(M1)`；其自身还指出约 100 keV 状态混合可能重分配 in-band/out-of-band ratios。
- 合并三重符合事件中的 726 keV 峰有额外未解释贡献，作者认为可能来自弱衰变路径或其它 reaction channel，并称其不影响主要 level placement；这是 source-level residual contamination boundary。
- DB1/DB2 的支持方文章与本论文存在 shared Gammasphere lineage；Lv 2022 是不同 reaction/facility 的 counter chain。论文数量不能替代独立实验数量。
- QTR/TPSM/DFT 对 `β,γ`、惯量、pairing、chemical potentials 和 configuration 的选择会影响几何与能量比较；模型 agreement 不能替代 direct electromagnetic measurements。

## Codex Self-audit

| 审计项 | 判断 | 证据 |
|---|---|---|
| Identity/locator | DOI、article number、arXiv、页数、bytes、SHA 和关键页已交叉核对；Table I、Fig.5、Fig.12–13 已视觉检查。 | Crossref/arXiv metadata；PDF pp.1、5–6、12–15；manifest |
| Claim separation | 新连接和 δ 是实验层；chiral/wobbling 归类是作者解释；QTR/TPSM/DFT 是模型结果；对既有争议的“反驳”保留作者归属。 | SH26-1–11 |
| Independence | 本论文与 Matta/Sensharma 支持链按同一 Gammasphere campaign/后续 analysis lineage 归并；Lv 2022 作为独立 counter experiment 保留。 | SH26-11；`135Pr` project |
| Negative evidence | 明确记录无新 polarization、无 absolute lifetime/strength、726-keV contamination 和约 100 keV mixing limitation；不以模型图替代缺失数据。 | SH26-4、SH26-6、SH26-10；Competing Interpretations |
| Review state | 页面 `unreviewed`；SH26 claims 的 `needs_review: false` 仅表示 Codex direct-source self-audit，不表示用户审核或论文措辞准入。 | frontmatter；SH26-1–11 |

## Knowledge Impact and Learning Decision

- **新增知识**：补入 2026 PRC 的 DB1/DB2 五条新连接、三条 MCMC mixing ratios、17-keV minimum splitting 和 QTR/SCS transition-probability comparison。
- **纠正/限制知识**：2026 论文为支持方对 Lv 2022 双解批评提供了更具体的旧数据 χ² 论证，但没有消除 Guo/Lv 的方法差异、当前实验无 polarization 和 absolute-strength gap，因此 `135Pr` project 仍保持争议状态。
- **谱系判断**：Matta 2015、Sensharma 2019、Sensharma 2026 视为同一 80-MeV Gammasphere campaign 的延续/重分析；Lv 2022 是独立 JUROGAM counter chain；Guo 2021 是对 Matta 报告的 methodological comment，不是新实验。
- **Persistence**：建立本 source，更新 `135pr`、`135pr-wobbling-controversy`、low-spin synthesis、index 和批次 report；不创建重复 band pages，不启动 L4。

## Extracted Pages

- Nucleus: [[135pr]]
- Bands: [[135pr-yrast-band]]、[[135pr-side-band]]、[[135pr-second-side-band]]、[[135pr-dipole-band]]
- Experiments: [[atlas-digital-gammasphere-135pr-o16-80mev]]、[[atlas-gammasphere-135pr-o16-80mev]]、[[tifr-inga-135pr-o16-80mev]]
- Concepts/observables: [[transverse-wobbling]]、[[nuclear-chirality]]、[[chiral-vibration]]、[[multipole-mixing-ratio]]、[[interband-e2-strengths]]、[[wobbling-energy]]
- Methods/models: [[angular-distribution]]、[[dco-ratio]]、[[linear-polarization-asymmetry]]、[[triaxial-particle-rotor-model]]、[[triaxial-projected-shell-model]]
- Project: [[135pr-wobbling-controversy]]

## Related Knowledge

- [[matta-2015-transverse-wobbling-135pr]]
- [[sensharma-2019-two-phonon-wobbling-135pr]]
- [[lv-2022-evidence-against-wobbling-135pr]]
- [[guo-2021-comment-transverse-wobbling-135pr]]
- [[lawrie-2020-tilted-precession-wobbling]]
- [[135pr-wobbling-controversy]]

## Later Paper / Q&A Gate

若后续问答或论文写作需要使用 2026 论文的“first observation of chirality”、某条 `δ`、Fig.12 χ² 或“refute Lv”表述，必须同时回到本页对应原文页码，并明确：当前论文无 polarization/absolute lifetime，旧数据 χ² 争议未做统一三方 raw reanalysis，相关 chiral/wobbling 结论仍是作者解释与候选层。

## 2026-10-17固定取向、输入身份与公开源码审计

本次先冻结primed定向回忆，再核main raw原SHA，读PDF2–5、14–15及17相关引用，视觉核TableI和Fig12；不是新通读17页。旧SH26-1–11及unreviewed状态保持，新12–16均needs_review:true；旧false仅历史Codex self-audit，不扩为人审。Crossref重核正式DOI10.1103/3g4p-ncjn；publisher public abstract返回403，未得VoR正文/其DAS，不把本v2当已核VoR。

公开arXivv2 landing200，submission history定v2为2026-01-15；其TeX Source链接合法取得归档，5825886bytes，SHA-256 cdda3eceff0876c3774b253d91e1e41441941a3a2dbd9d358f64f2b785312278。本地仅新增raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/sh26-arxiv-2403.10749v2-source.tar，不覆盖main raw、不执行其中内容、不stage archive。29项inventory与26PDF零embedded files保留，TeX实际164/435行和三张原始chi2 PDF已定向检查。作者文件名V3与arXivv2分开；原件中的注释不是独立正式科学结论。

SH26-8/9/11的作者偏好与shared-lineage判断仍保留；新SH26-13/15把固定sigma切片、不同数据summary、未知event-level overlap说清。[[135pr-mixing-branch-input-contract]]保存三方delta/input角色表和后续profile设计，未从log10图估计Delta chi²、dof、reject significance或证明任意geometry/feeding下唯一解。当前public package没有足够input独立重放本分支选择，但并不声称作者从未提供过其它渠道。

## Day22 checkpoint095：保留条件卡方证据和双方模型差异

本轮只定向回读既有arXivv2原件PDF14–15，并视觉核Fig.12；未重称新通读或已取得正式VoR。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SH26-D22-R095-1 | Fig.12在σ/I=.2下的三条角分布χ²曲线偏好大δ，正文认为多角度能分开A2/A4而区分局部极小；这是真实的条件支持证据，不应因其为切片而抹掉，也不自动等于对全部nuisance已profile。旧任务声称σ/I自由后两谷必等深无本轮重拟合依据；仍不能从log10χ²图擅报排除σ数。p.15明确完整QTR允许j重取向，差别主要归于MoI比（约4对调定约2），这与Matta p.5相符；不把旧冻结批评当实现事实。作者以正A作补充确认的理由保留为观点，新实验未测polarization，不构成推翻Lv新P–Rac的共同响应重分析。 | conditional-evidence-and-model-reply | direct-original-and-cross-source-boundary | arXivv2 PDF14 Fig12/III.B; PDF15 continued response | true |


## Day23：两run合并与旧连接图的证据权重

本次定向回读/视觉核PDF2 SecII，并读PDF3–4逐run效率及angular distributions段；原review/SH26既有flags保持，新增needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SH26-D23-1 | SecII明说本次63Ge、697μg/cm²靶的run与Ref16（Sensharma2019的83Ge DGS）数据相加，合计2.5×10^10 events；PDF3–4又明说angular distributions用combined dataset，并按各run detector configuration/live time构造合并效率。这既包含新增采集成分，也与S19部分重叠；不把整篇当第三次完全独立重复，亦不抹掉新增run的信息。 | merged-acquisition-and-response | direct-original | arXivv2 PDF2 Sec.II; PDF3–4 angular-distribution paragraph | true |
| SH26-D23-2 | Fig12仍引Refs15/16且固定σ/I=.2，SecII则给combined-data的全局分析程序；未有逐图event/run ledger，不能确认该图每个角度究竟用哪一组事件或声明它逐点等于2015计数。原SH26-D22-R095-1的条件大根偏好保留；“旧AD谱系回应”表示研究/观测继承，不是已证明排除了新增事件贡献。 | per-observable-sample-identity-boundary | direct-and-bounded-inference | arXivv2 PDF14 Fig.12; PDF2–4 Sec.II | true |

Knowledge Impact and Learning Decision：revises“论文整体独立/重复”的二元标签；本任务不重建raw joint likelihood，source/readiness与新增run和复用点的图见[[low-spin-wobbling-controversies]]。


### Day23：与2021学位论文的合并样本摘要对账

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SH26-D23-3 | 本v2 SecII的63Ge/697μg靶、合并Ref16 DGS与[[sensharma-2021-wobbling-motion-135pr-187au]] printed71 Run4描述相匹配，但学位论文合并数1.52×10^10、本v2为2.5×10^10。该采集成分已在2021来源中出现，不能把“相对S19的新run”误说成确认于2026才采集；也不能缺event ledger便认定两版本完整事件集相同或哪版印错。固定σ/I=.2条件χ²支持保持，未由总数差重估显著性。 | cross-version-event-summary-boundary | direct-original-and-cross-source | PDF2 Sec.II; SE21-D23-1 | true |

## Day23：Fig12矢量图示输入与原χ²目标分开核验

本次只定向核既有同hash arXivv2 PDF14 Fig12/III.B，fresh原页与747 inset放大视觉核，不重复称新17页通读。原raw SHA294f791a230a12005ef43a237afb25b9bf731f8f520a1a65d6b32d0386ef91b3。该页无embedded bitmap而有vector paths，故与Au栅格提点不同：system/scripts/day23_sh26_published_vectors.py直接读取黑色circle、其下的vertical stem与两端horizontal caps，以及红/蓝和主图黑曲线的polyline。PDF只读，未执行源包代码或隔离producer。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SH26-D23-4 | Fig12三inset各有7个黑色circle，可在vector图元中分别配到vertical errorstem和两条cap，共21点/42caps；marker与stem中点最大差约4.6×10⁻5 PDFpoint。该结果恢复的是公开图示位置/半误差线长度，非原ring峰面积/协方差或真实统计coverage。图示能量按原件746.3/811.6/754.2keV保留，不能默改成其它来源747.3/813.2的精确能量。 | published-vector-observation-and-errorbar-geometry | original-vector-primitives-and-declared-extraction | arXivv2 PDF14 Fig12 threeinsets | true |
| SH26-D23-5 | 按主图Arctanδ及log10χ²的刻度对黑profile作几何读数，在打印红/蓝δ处，746.3约χ²2.3/6.6、811.6约47/423、754.2约5.8/375。它们是作者图在σ/I=.2下的显示读数，不是本任务重新拟合或新统计量；保留大根条件偏好，不推全部nuisance自由后的唯一性，也不预判两谷必等深。无dof/CI/p-value/排除σ数。 | published-author-profile-geometric-readout | direct-original-vector-readout-with-conditional-scope | arXivv2 PDF14 Fig12 mainprofiles andcaption sigma/I=.2 | true |
| SH26-D23-6 | 本任务另定义D=Σ[(图示点−同x处显示曲线)/图示halfbar]²，附加“halfbar当独立1σ”的条件、保持显示归一、不refit。直接polyline给红/蓝D约140/456、138/1114、42/820，方向均偏红，但数值未重现主图χ²读数。D与作者目标不应混称；原objective/归一/误差与样本处理链仍缺，不能把非闭合直接判paper错误或相反强行认证共同likelihood已复现。 | Codex-conditional-plot-diagnostic-and-nonclosure | declared-conditional-analysis-not-original-fit | arXivv2 PDF14 Fig12 main/inset comparison; explicit Ddefinition below | true |

| 图示能量keV | 打印δ红/蓝 | 主图χ²标签的近似读数红/蓝 | 本任务D红/蓝（附加对角halfbar条件） |
|---|---|---|---|
| 746.3 | −1.40 / −.59 | 2.3 / 6.6 | 140 / 456 |
| 811.6 | −1.63 / −.52 | 47 / 423 | 138 / 1114 |
| 754.2 | −2.16 / −.40 | 5.8 / 375 | 42 / 820 |

D在PDF纵向坐标直接计算，轴的共同平移/尺度不影响它，实际affine控制差≤5.1×10⁻12。最终用literal polyline插值，不依赖将曲线再拟成P2/P4；探索性P2/P4重构及单一归一probe亦未闭合，未将它们冒充作者程序或用于改数据。源χ²是原图名义标签，D是任务声明的另一诊断；图示halfbar的coverage、完整Cov和objective正常数未恢复，故本页没有Δχ²置信检验。

七项几何/hash/cap/中点/正半长/affine/非闭合保留控制实际通过，仅验证本提取。公开曲线与误差图元可读比“只能看近似形状”前进了一步，却仍不提供共同response与原producer。SH26-D23-1/2/3的部分run重叠及逐图ledger缺口原样保留；本图不是一次新偏振或独立采集。新增needs_review:true，旧source self-audit flags不变。

## Day23：MCMC所引方法原件与AD迁移边界

本次沿原PDF17Ref54取得K.B.Howard，*Structure effects on the giant monopole resonance and determinations of the nuclear incompressibility*，arXiv[2004.02362v2](https://arxiv.org/abs/2004.02362v2)，PDF封面明确v2/Aug2020，189页/12245878bytes/SHA256 4e137af925c309e1486a9b5eb6f078eac22d9f02163970c942b9ca31f28c9fa7。**只定向读PDF94–105、printed79–90的MDA/MCMC方法、题名/目录与相关refs，不称189页通读**；关键PDF95/97/98/99/100/104已render，98/100实际视觉核。原文的GMR测量与不可压缩系数不作为本Day23新核物理结果。

再沿其Ref31取得Foreman-Mackey/Hogg/Lang/Goodman，*emcee: The MCMC Hammer*，PASP125,306(2013)，DOI[10.1086/670067](https://doi.org/10.1086/670067)，公开[arXiv1202.3665v4](https://arxiv.org/abs/1202.3665v4)，15页/183607bytes/SHA256 d9db50484bd46ddc29e966a69f3775061cb240dc7c10111d7d3505c711ad56b6。全主线/算法/公式/refs/附录已文字读，PDF9/10fresh视觉；没有安装或执行附录命令，也未称当前package或原AD代码版本已核。两PDF只在tmp/day23-originals/公开暂存，正式raw归档deferred。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HW20-D23-001 | Howard原Eq4.5为α散射DWBA多极分解，Aλ是各Ex bin的EWSR份额，λmax8/10；Eq4.9给[0,1] uniform prior。这里A0/A2/A4不是γ AD的强度归一与Legendre系数，非负EWSR先验不能直接移给可为负的AD A2/A4，更不是δ的先验。 | external-cited-method-parameter-identity | directly-read-original-method | HowardPDF95Eq4.5; PDF99–100Eq4.9 | true |
| HW20-D23-002 | 所读方法Eq4.6是Σ[(yj−f)/δyj]²，Eq4.7取exp(−χ²/2)，Eq4.8/4.9另定义prior；该段给通用固定误差形式，未给本Pr/Au AD的原输入/Cov/取向/归一或具体目标函数版本。因此引用Howard不能完成Fig12共同响应重放，也不授权本任务补一个未知noise参数去强行闭合057。 | external-cited-likelihood-and-transfer-readiness | directly-read-method-not-AD-producer | HowardPDF99Eqs4.6–4.8; PDF100Eq4.9 | true |
| FM13-D23-001 | emcee原Sec3明确独立样本数受integrated autocorrelation time约束，Eq12为τf=1+2ΣCf(T)/Cf(0)，并依赖所估函数f；Markov只规定给定当前态后的条件依赖，不等连续每步iid。HowardPDF97的口头“essentially independent”不能当一般定理，亦不能由MCMC名/步数认证实际Pr/Au的ESS或误差。 | external-primary-method-and-precision-boundary | directly-read-primary-plus-bounded-inference | emceePDF5 M–Hdiscussion; PDF9Eqs11–13; HowardPDF97paragraph | true |
| FM13-D23-002 | 原Sec4明确谷内autocorrelation可短而跨谷migration很慢，短链可能看不见长时间尺度；分谷独立采样还需“properly”合并，不由局部样本数直接给global权重。此方法限制不意味着本Pr/Au两谷等深；真实固定σ条件偏好保留，actualtarget/prior/chain跨谷记录仍需。 | external-primary-multimode-limit | directly-read-primary-and-scope | emceePDF10–12Sec4 multimodaldiscussion | true |
| FM13-D23-003 | 原emceeEq3/9及Algorithms2/3的affine invariance涉及参数重参数化/伸缩move和正确acceptance，并非删除原数据Cov、无条件完成marginalization或保证跨谷。HowardPDF100 footnote对affine“保角”的一般化不成立：剪切T=((1,1),(0,1))的明确矩阵例见下，能保parallel而改夹角。此为数学术语校准，不判原emcee或核数据实际实现错误。 | primary-sampler-definition-and-Codex-math-boundary | directly-read-method-and-declared-counterexample | emceePDF4Eq3; PDF6Eq9; PDF7Algorithm3; HowardPDF100footnote5 | true |
| FM13-D23-004 | 声明的stationary AR(1)控制ρ=.9给corr1=.9、渐近τint19；选数学链N19000，有限N的mean-ESS约1000.50。另取disjoint A/B的πp=p fA+(1−p)fB，则π(x∣A)=fA与p无关，局部样本不能单独恢复global谷权重。这些是条件信息反例，不是实际Pr/Au链诊断、γevents、CI或束流率。 | Codex-conditional-sampling-information-exercise | declared-math-with-source-definition | emceePDF9Eq12; stated AR1 anddisjointmixture below | true |

矩阵例明确采用T=((1,1),(0,1))，将两条正交unitaxes变成(1,0)与(1,1)，夹角45°，parallel仍保持；不把它与057的观测纵轴共同单位变换D不变混为同一性质。AR控制为Xt+1=.9Xt+sqrt(1−.9²)εt，stationary variance1，直接有限Cov求和与几何级数闭式相合；这里ESS只针对sample mean。局部例用p=.2/.8、fA=(.3,.7)、fB=(.6,.4)，两组conditional A均(.3,.7)，从未给实际δ根赋这些权重。

HowardAlgorithm1是示意pseudocode而实际方法选emcee；具体缓存更新、proposal条件、伸缩因子与版本不能靠示意替代执行代码。本次不据其简写判GMR/AD代码有错。对SH26正文“先选较低χ²再附近采样”的应用，应分别取得global目标与先验、参数约束、各链跨谷/mixing证据以及未定标检验；局部MCMC不能替代这些，也不因此抹条件大根优势。五限定数学控制通过，只核反例；新增needs_review:true，原review状态不变。


## 2026-10-29 Day27 continuation context

[[chen-2026-bayesian-inertia-wobbling-135pr]] provides context on recent theoretical Bayesian inertia inference in 135Pr; see that metadata-only note for details on energies-only conditioning and fixed EM inputs.
