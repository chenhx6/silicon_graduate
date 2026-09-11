---
type: source
title: "Sensharma 等 2026：135Pr 中从横向摇摆到手征的演化"
aliases: [Sensharma 2026 135Pr chirality, evolution of chirality from transverse wobbling 135Pr]
created: 2026-09-13
updated: 2026-09-13
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
citation_key:
zotero_uri:
library_file: "raw/papers/gpt/_incoming/20260912-135pr-refresh/sensharma-2026-135pr-chirality-wobbling.pdf"
raw_file: "raw/papers/gpt/_incoming/20260912-135pr-refresh/sensharma-2026-135pr-chirality-wobbling.pdf"
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
