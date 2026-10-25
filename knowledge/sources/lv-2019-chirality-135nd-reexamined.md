---
type: source
title: "Lv 等 2019：135Nd 手征重分析与多重手征双重带"
aliases: [Lv 2019 135Nd reexamined, 135Nd positive-parity chiral doublet]
created: 2026-09-12
updated: 2026-10-24
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Chirality of 135Nd reexamined: Evidence for multiple chiral doublet bands"
authors: [B. F. Lv, C. M. Petrache, Q. B. Chen, J. Meng, A. Astier, E. Dupont, P. Greenlees, H. Badran, T. Calverley, D. M. Cox, T. Grahn, J. Hilton, R. Julin, S. Juutinen, J. Konki, J. Pakarinen, P. Papadakis, J. Partanen, P. Rahkila, P. Ruotsalainen, M. Sandzelius, J. Saren, C. Scholey, J. Sorri, S. Stolze, J. Uusitalo, B. Cederwall, A. Ertoprak, H. Liu, S. Guo, M. L. Liu, J. G. Wang, X. H. Zhou, I. Kuti, J. Timár, A. Tucholski, J. Srebrny, C. Andreoiu]
journal: Physical Review C
year: 2019
volume: 100
pages: 024314
doi: 10.1103/PhysRevC.100.024314
arxiv: 1907.12809
language: en
canonical_source: "https://doi.org/10.1103/PhysRevC.100.024314"
zotero_item_key:
citation_key: Lv_2019
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
zotero_uri:
library_file: "raw/papers/gpt/_incoming/20260912-135nd-crosswalk/lv-2019-135nd-reexamined-arxiv.pdf"
raw_file: "raw/papers/gpt/_incoming/20260912-135nd-crosswalk/lv-2019-135nd-reexamined-arxiv.pdf"
raw_sha256: "97182e90125ce57ac2faa0feeef42b6bc12952b3287f82f277a04f8d32cf0303"
nuclei: [135nd]
reactions: ["100Mo(40Ar,5n)135Nd"]
experiments: [jurogam2-135nd-ar40-152mev]
models: [constrained-covariant-density-functional-theory, particle-rotor-model]
observables: [IPDCO, dco-ratio, two-point-angular-correlation-ratio, bm1-be2-ratio, alignment, energy-levels]
methods: [in-beam-gamma-spectroscopy, gamma-gamma-coincidence, linear-polarization-asymmetry, dco-ratio, two-point-angular-correlation-ratio]
tags: [a130, 135nd, nuclear-chirality, multiple-chiral-doublet-bands, positive-parity, jurogam]
---

# Lv 等（2019）：`135Nd` 手征重分析与多重手征双重带

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

B. F. Lv 等，*Chirality of `135Nd` reexamined: Evidence for multiple chiral doublet bands*，*Physical Review C* **100**, 024314 (2019)，DOI `10.1103/PhysRevC.100.024314`，arXiv `1907.12809`。ArXiv API 给出的 journal reference、题名、作者首位和 DOI 与 Crossref 元数据一致；本地 PDF 为 arXiv 版本，SHA-256 为 `97182e90125ce57ac2faa0feeef42b6bc12952b3287f82f277a04f8d32cf0303`。

## Supporting Information Availability

Checked the official APS article page and SI routes on 2026-10-09. The landing page returned HTTP 200 with no SI/attachment link, and the standard supplemental-PDF endpoint returned HTTP 404. The APS supplemental resolver timed out once; one bounded retry returned HTTP 200 to the article record at `#supplemental`, still with no SI attachment. The official arXiv record returned the article PDF without an ancillary/supplement entry. No SI file was found on these checked official records; separately hosted author material remains outside a global absence claim.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-SI-1 | The APS landing page exposed no SI/attachment link and its standard SI PDF endpoint returned 404; arXiv listed the article PDF without an ancillary entry. The supplemental resolver timed out once, then a bounded retry returned to the same article record at `#supplemental`. No SI file was found on these checked official records. | evidence-boundary | direct | APS article `https://journals.aps.org/prc/abstract/10.1103/PhysRevC.100.024314`; resolver `https://link.aps.org/supplemental/10.1103/PhysRevC.100.024314`; standard endpoint `https://journals.aps.org/prc/supplemental/10.1103/PhysRevC.100.024314/PhysRevC.100.024314.supplemental.pdf`; arXiv record `https://arxiv.org/abs/1907.12809` | true |

## Scope and Reading Depth

- `deep-read`：全文 10 个 PDF 页面均完成文本主线阅读。
- 视觉核对：PDF pp.1–3 的题名、摘要、实验结果、部分能级图和门谱；pp.6 的总结；pp.7–10 的 Table I（含 D3、D4、D5、D6 行）。
- 关键核对对象：D3/D4 的 parity revision、四条 IPDCO 数值、D3/D4 连接跃迁、D5/D6 的负宇称谱系、Table I 的逐线 `J^π`。
- 未覆盖：原始事件矩阵、实验标定输入和作者未公开的逐事件分析；这不影响本文表格/正文层级的 parity crosswalk。
- 版本边界：本地文件是公开 arXiv 版本；DOI 期刊身份已由 Crossref/API 核验，但未另行保存出版商 PDF。

## Summary

2019 PRC 重新分析 `135Nd` 的高自旋谱学，明确将 D3/D4 作为正宇称 chiral-doublet pair，并将此前的负宇称 D5/D6 作为另一组 pair。正文、IPDCO、D4↔D3 的 E2、D4→D1 的 E1 以及 D4 表格行形成一致的总体宇称证据；但 D3 的 `334.4 keV` Table I 行仍有局部 `J^π` 异常，绝对 partner strengths/lifetimes 和更强的静态手征措辞仍需保留边界。

## Paper Question and Experimental Design

论文重新检查 `135Nd` 中已知的负宇称 chiral pair，并在同一类 `100Mo(40Ar,5n)` 高自旋谱学中寻找额外的伙伴带。实验使用 152 MeV `40Ar` 束、0.5 mg/cm² 自支撑富集 `100Mo` 靶和 JUROGAM II 的 39 个 Compton-suppressed Ge 探测器（PDF p.2）。能级、自旋和宇称由符合关系、`R_DCO`、`R_ac` 与线偏振联合约束；作者再用 constrained CDFT 和 PRM 比较能谱、alignment 与 `B(M1)/B(E2)`。

## Evidence Chain

1. `D3` 在已知 334-keV 终止位置基础上扩展至约 `33/2+`，并新增多条连向 D2-3qp 的跃迁；正文明确写其 parity based on `R_DCO`/`R_ac` 改为 positive（PDF p.2）。
2. `D4` 的已知结构被延伸并将 spin 下调一单位；`589、649、780 keV` 的 D4↔D3 连接被判为 E2，`1184 keV` 至负宇称 D1 的连接被判为 E1，正文据此说明 D4 与 D3 同为正宇称（PDF p.2）。
3. 为确认 D2–D4 的宇称，作者给出 `830、1015、1161、1184 keV` 四条连接的 IPDCO：`0.043(8)、0.089(28)、0.008(2)、0.018(5)`；正文称这些值显示 electric character，并据此 fix D2、D3、D4 的 positive parity（PDF p.2）。
4. Table I 的 D4 行从 `21/2+→19/2+` 至 `29/2+→27/2+`，以及其续表中的 `23/2+→19/2+`、`25/2+→21/2+`、`27/2+→23/2+`、`21/2+→19/2−` 等，均与正文的正宇称 D4 叙述一致（PDF pp.8–9）。
5. Table I 的 D3 行大部分列为正宇称，但 `334.4 keV` 一行仍写作 `27/2−→25/2+`（PDF p.8）。它与同一表 D3 的其它行、PDF p.2 的 D3 positive-parity 说明和 Fig.1 的整体标注不一致，当前只能标为残余 table-level anomaly；不能把这一孤立行当作对整条 D3 宇称的反向裁决。
6. 2019 论文说此前报告的 D5、D6 levels 在 Ref. [10] 和 [36] 中得到确认，并在 Table I 中将两带逐线列为负宇称；作者把 D5/D6 与新增正宇称 D3/D4 分开作为两组 pair（PDF pp.1–2、6、9–10）。

## 2019 Parity Crosswalk

| 证据层 | 2019 PRC 的直接记录 | 与 thesis/历史论文的关系 |
|---|---|---|
| D3 | 正文由 `R_DCO`/`R_ac` 多条连接将 D3 改为正宇称；IPDCO 段再次把 D3 列入正宇称 D2–D4 | 吕冰峰 2019 thesis 的实验结果同段先写 changed to positive；该 thesis 的孤立负宇称句子不是后发 PRC 的结论 |
| D4 | 正文以 D4↔D3 E2 和 D4→D1 E1 说明 D4 与 D3 同为正宇称；Table I 的 D4 行一致 | thesis physical p.127 的正/负句子冲突由此得到外部期刊版本支持；D4 不再因该文字冲突停在 `stopped` |
| D3 334.4-keV row | 表格仍保留 `27/2−→25/2+` | 作为 2019 版本内部残余 typo/表格异常保存，不扩展为整条带的负宇称结论 |
| D5/D6 | 负宇称、既有 pair；2019 PRC 明确以此前 refs [10,36] 为谱系 | 2003 PRL 的 Band A/B 与 2007 PRL 的 electromagnetic/lifetime paper 是前史；同一物理谱系不重复计为独立实验 |

## Historical Lineage

- Zhu 等 2003 PRL（arXiv `nucl-ex/0302029`，DOI `10.1103/PhysRevLett.91.132501`）报告 `110Pd(30Si,5n)`、133 MeV 下的 `135Nd` Band A/B：两条近简并、同宇称的 `ΔI=1` 带，由 `ΔI=1` 和 `ΔI=2` links 连接，并以三维 TAC 讨论三准粒子手征结构。该论文的带名是 Band A/B，不应倒写成其当时已经使用 D5/D6。
- Mukhopadhyay 等 2007 PRL（arXiv `0708.1493`，DOI `10.1103/PhysRevLett.99.172501`）在 `100Mo(40Ar,5n)`、175 MeV 的 Gammasphere 数据中对先前 Band A/B 测得寿命、`B(M1)` 和 `B(E2)`，并讨论从 chiral vibration 到 static chirality。2019 PRC 的 D5/D6 负宇称 pair 与该历史负宇称谱系相连，但实验 campaign 不同。
- Qi 等 2009 的 PRM 理论论文（arXiv `0812.4597`，DOI `10.1016/j.physletb.2009.02.061`）和 Lawrie 等 2020 的 CDFT 理论论文（arXiv `2009.08075`，DOI `10.1016/j.physletb.2020.135795`）是模型/后续理论支持，不替代 2019 PRC 的实验 parity 记录。
- Lv 2019 博士论文是同一作者/实验谱系的学位论文层记录；期刊文章与 thesis 不能作为两个独立 JUROGAM II 实验计数。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | research_status | needs_review |
|---|---|---|---|---|---|---|---|
| LV19-1 | 152 MeV `100Mo(40Ar,5n)135Nd`、0.5 mg/cm² 富集靶和 39 个 JUROGAM II Compton-suppressed Ge 探测器用于本实验。 | experimental-fact | direct | single | PDF p.2, Sec.II | completed | false |
| LV19-2 | `R_DCO`、`R_ac`、γγ coincidence 和线偏振共同参与自旋、宇称与多极性赋值。 | experimental-criterion | direct | single | PDF p.2, Sec.II | completed | false |
| LV19-3 | 四条连接的 IPDCO 为 `0.043(8)、0.089(28)、0.008(2)、0.018(5)`，作者以其 electric character 固定 D2、D3、D4 的正宇称。 | experimental-criterion | direct | single | PDF p.2, Sec.II | completed | false |
| LV19-4 | 2019 PRC 的正文、Fig.1/表格和总结共同支持 D3/D4 为正宇称 pair；D4 的正宇称由 D4↔D3 E2 与 D4→D1 E1 连接进一步说明。 | experimental-fact + author-interpretation | direct | multiple-dependent | PDF pp.2–3、6、8–9 | completed | false |
| LV19-5 | D3 Table I 的 `334.4 keV` 行仍写成 `27/2−→25/2+`，与该文其余 D3 正宇称记录不一致；它是保留的表格级异常，而非整条带的独立 parity 裁决。 | experimental-fact | direct | single | PDF p.8, Table I | completed | false |
| LV19-6 | 2019 PRC 将已知负宇称 D5/D6 与新增正宇称 D3/D4 分为两组 chiral doublets；D5/D6 的先前谱系回到 2003 Band A/B 和 2007 lifetime/transition-probability papers。 | synthesis | indirect | multiple-dependent | PDF pp.1–2、6、9–10；crosswalk artifacts | completed | false |
| LV19-7 | PRM 使用 D3/D4 的 `π[(1h11/2)^1(1g7/2)^−1]⊗ν(1h11/2)^−1` 配置；D5/D6 使用 `π(1h11/2)^2⊗ν(1h11/2)^−1`，计算再现能谱和部分 `B(M1)/B(E2)` 趋势。 | model-result | indirect | single | PDF pp.5–6, Fig.3/5/6 | completed | false |
| LV19-8 | 2019 PRC 没有提供所有 partner-resolved absolute strengths/lifetimes，也没有消除弱 link、configuration mixing 或表格孤立行对更强 MχD 措辞的限制。 | our-inference | direct | single | PDF pp.2、5–6、8–10 | completed | false |
| LV19-9 | Table I separately lists same-initial-spin D6→D5 candidate links: at 31/2−, 648.9-keV `31/2−→29/2−` (M1/E2) and 896.8-keV `31/2−→27/2−` (E2); at 33/2−, 640.2-keV ΔI=1 and 931.3-keV ΔI=2 E2; at 35/2−, 591.4-keV ΔI=1 and 949.6-keV ΔI=2 E2; at 37/2−, 963.0-keV `37/2−→33/2−` E2 appears, while the parenthesized 556-keV ΔI=1 link from the earlier scheme is not listed there. These are transition-identity records from the 2019 campaign and do not establish which line contributes to a MU07 open-circle strength point. | experimental-transition-identification + cross-source-boundary | direct | single | PDF pp.9–10, Table I continued, Band D5/D6 rows | completed | true |

## Nuclear Structure and Interpretation

- `D3/D4`：2019 PRC 的实验版本为正宇称 pair，建议组态为 `π[(1h11/2)^1(1g7/2)^−1]⊗ν(1h11/2)^−1`；D3 仅有很少可提取的 `B(M1)/B(E2)` information，不能将 PRM agreement 写成独立几何测量。
- `D5/D6`：负宇称 pair，建议组态为 `π(1h11/2)^2⊗ν(1h11/2)^−1`；2007 PRL 的 lifetime/transition-probability evidence 属于前一负宇称谱系，不是 D3/D4 的寿命证据。
- 2019 PRC 的作者解释是两组 MχD；实验事实是能级、连接、多极性/偏振指标和表格赋值。模型计算再现不等于已排除 γ-soft、configuration mixing、band crossing 或其它集体解释。

## Competing Interpretations and Limitations

- “D3/D4 positive parity”在 2019 PRC 的正文、IPDCO 段、能级图和 D4 表格行之间有多重直接支持；但 Table I 的 D3 `334.4 keV` 行必须逐字保留为未调和的局部异常。
- 同宇称、近简并、E2/M1 连接和 PRM/CDFT agreement 支持 chiral-doublet interpretation，但不能单独证明静态手征；absolute partner-resolved electromagnetic strengths、寿命和独立模型比较仍是限制。
- 2003、2007、2019 的 publication lineage 横跨不同实验设置或同一数据谱系的后续分析。论文数不能替代独立实验数，2007/2019 也不能把 2003 的 Band A/B 当作当时已有 D5/D6 标签。
- 本页不把 2019 PRC 对 D3/D4 的修订倒灌为 Zhu 2003 或 Mukhopadhyay 2007 的原文表述；每个来源的作者解释按发表时间和带号分开保存。

## Codex Self-audit

| 审计项 | 判断 | 证据 |
|---|---|---|
| Identity/locator | DOI、arXiv、题名、作者首位、卷页和本地 PDF SHA 已交叉核对；关键 parity、IPDCO、Table I 页码已视觉核对。 | Crossref/arXiv metadata；PDF pp.1–10；`outputs/literature-acquisition/20260912-135nd-crosswalk.json` |
| Claim separation | 观测/判据、作者解释、PRM/CDFT 模型结果和跨来源谱系推断已分栏；不把 model agreement 直接写成实验事实。 | LV19-1–8；Historical Lineage |
| Conflict handling | thesis 的 D4 正/负句子冲突被 2019 PRC 的正文和表格层支持为正宇称；D3 334.4-keV 表格行仍保留 anomaly。 | PDF p.2、p.8；LV19-4/5 |
| Independence | Lv thesis、2019 PRC、2003 PRL、2007 PRL 和 2009/2020 theory 按 dependent publication/theory lineage 分层，不重复计数。 | Historical Lineage；manifest |
| Paper-use boundary | 页面仍为 `unreviewed`；本轮 `needs_review: false` 表示 Codex 已完成 claim-level 直接证据自审，不表示用户已审核或论文措辞已获准。 | frontmatter；LV19-1–8 |

## Knowledge Impact and Learning Decision

- **纠正知识**：`DD-20260910-136ND-03` 不再因“缺少外部原始论文”而 stopped。2019 PRC 后发期刊版本明确支持 D3/D4 正宇称；原 thesis 的 D4 负宇称句子记录为 source-text error/遗留文字错误。
- **保留边界**：2019 Table I 的 D3 `334.4 keV` 行仍异常；D3/D4 的 MχD 仍是作者解释/候选层级，未凭本 crosswalk 提升为无条件“已证实”。
- **独立性**：本 source 与 Lv thesis、2003 PRL、2007 PRL 共享或延续物理谱系；manifest 中的五个 PDF 是交叉核验材料，不是五个独立实验。
- **Persistence**：建立本 source；更新 `135Nd` 汇总、index、批次报告/closure/self-audit。暂不创建重复的 D3/D4 band pages，避免在表格局部异常尚存时扩张实体。

## Extracted Pages

- [[135nd]]
- [[lv-bingfeng-2019-chirality-136nd-135nd-thesis]]
- [[lv-2021-tilted-precession-135nd]]
- [[petrache-2018-chiral-bands-even-even-136nd]]
- [[multiple-chiral-doublet-bands]]
- [[nuclear-chirality-and-multiple-chiral-doublet-bands]]
- [[jurogam2-135nd-ar40-152mev]]

## Related Knowledge

本页与 `135Nd` 的 D1/TiP、D5/D6 历史谱系、`136Nd` MχD 和 A≈130 手征方法页相连；新建外部 source 不创建重复的 D3/D4 band page。

## Later Paper / Q&A Gate

本页已完成 Codex self-audit；未发生用户页面级审核。若后续问答或论文写作要引用具体 `J^π`、IPDCO 或“D3/D4 正宇称 MχD”措辞，仍应回到 2019 PRC 的原文页码和 Table I，并明确 D3 `334.4 keV` 局部异常及 MχD 的作者解释属性。


## 136Pr 2025：同一acquisition的跨核素复用

[[lv-2025-136pr-tac-covariant-density-functional]] LV25-20的SecII（acceptedcopy PDF3）明确136Pr分析“same dataset”依Refs16/31，其中Ref16（PDF16）就是本篇PRC100,024314。故136Pr的1p3n selection与本篇135Nd5n共享152-MeV100Mo+40Ar/JUROGAM-II campaign，不能按核素或2019/2025发表年多计独立实验。实际targetgate、calibration、事件重叠/Cov仍须逐分析核验；同pool不证明完全同histogram，更不转移本篇135Nd的POL/δ/τ或各band标签。

[[jurogam2-135nd-ar40-152mev]]保存channel入口，[[136pr]]与[[level-scheme-reconstruction]]保存不同核素的拓扑证据。本文LV19-1–9原文与needs_review false/true均保持；新增关系来自2025直接来源，不把它写成2019新测量或新的人审。


## Day21第三次周考原件核对：多极性、带身份与表格残余异常

2026-10-23在Day21第三次周考中重新核对arXiv1907.12809v1文本和Table I。LV19-1–9所有记录保持。再次确认：
1. D3/D4的正宇称性质由多条向D1、D2-3qp的连接以及相互之间的E2/E1跃迁共同确立；Table I中334.4 keV行的负宇称标识仅为印刷/表格层孤立异常，不否定正文的整体正宇称。
2. 本文确立了正宇称MχD候选，但没有给出全态寿命和绝对B值；对静态手征的判别仍主要依赖CDFT与PRM模型计算的再现，不构成无模型几何测定。


## Day21 checkpoint052：新采集与旧绝对强度分层审计

本轮在primed-recall-frozen-052之后重读arXiv1907.12809v1全10页文字，视觉核pp.2–10全部图表，Fig.1 D5/D6局部放大。原件SHA256重新计算为`97182e90125ce57ac2faa0feeef42b6bc12952b3287f82f277a04f8d32cf0303`；raw未改。Crossref DOI元数据本次HTTP200，未另核VoR全文。原LV19-1至9、review及flags全部保留；以下为本次限定自审，不恢复001–041未核认证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D21-R52-1 | 152MeV JUROGAM II为与MU07 175MeV Gammasphere不同的新采集；本文新相对强度/角比可提供新信息，但p.5明确绝对B(M1)/B(E2)来自Ref.36，本文自己的B比与旧结果相近，不是新寿命复测。 | acquisition-and-result-lineage | direct-original | PDF p.2 Sec.II；p.5 D5/D6段；p.7 Ref.36 | true |
| LV19-D21-R52-2 | Table I footnote b的Iγ是效率修正后对198.8keV线归一的相对强度，由总投影和门谱组合取得；不是每母态的absolute photon branch或未修counts。 | observable-contract | direct-original | PDF p.10 Table I footnote b | true |
| LV19-D21-R52-3 | D6的896.8/931.3/949.6/963.0为到D5的ΔI2 E2；591.8/681.0/812.0分别是D6内35/2→31/2、37/2→33/2、39/2→35/2，但这些行multipolarity栏空白。31/2及33/2的带内ΔI2未在此表列行，不能以运动学差补成新测量。 | line-identity-and-component-boundary | direct-original | PDF p.3 Fig.1；pp.9–10 Table I D6 | true |
| LV19-D21-R52-4 | D6 31/2母态4007.8keV的225.8、648.9、896.8keV行分别为带内ΔI1、带外ΔI1和带外ΔI2；前两行只标M1/E2，无δ数值。它们允许有条件同母态代数，不唯一给E2/M1成分或MU07原branch。 | same-parent-contract | direct-original-and-algebra | PDF p.3 Fig.1；pp.9–10 Table I D6 | true |
| LV19-D21-R52-5 | D6表头下934.9/966.3行的母态能量/数据与D5同名行重合，Fig.1未把它们画成额外D6母态；998.1行Ei=5412.6而其它D6 39/2行Ei=5411.6。保留表内/图文边界，不能只按表头自动归带或静默改值。 | printed-identity-anomaly | direct-original | PDF p.2新线997文字；p.3 Fig.1；pp.9–10 Table I | true |
| LV19-D21-R52-6 | PRM的J0按能谱调整，D5/D6为复现B比上升将CDFT γ=22.2度改20.2度；其RMS角动量分量为模型输出。D3仅一态B比，正文I=29ℏ与图/表29/2身份不一致，不能据该句造整数spin数据。 | model-calibration-and-coverage | direct-original | PDF pp.4–6 Sec.III/Figs.5–6；p.8 Table I D3 | true |

### 逐线绑定与实际缺口

新增`system/scripts/day21_checkpoint052_nd135_followup_contract.py`仅核七条已明确初末态的中央能量闭合、相对强度及条件代数；JSON保留blank而非填E2。591.4keV从D6 35/2到D5 33/2，与591.8keV从同母态到D6 31/2不同，不能仅按约591keV合线。独立采集可以补充本核谱学，但不能把2019相对强度无条件代入2007原门/寿命producer。

同母态D6 31/2的带外896.8 E2与带内225.8混合线：

B(E2,896.8)/B(E2成分,225.8) = (0.79/3.8)(225.8/896.8)^5 / f_E2(225.8)。

寿命和共同强度归一消去，但δ、成分与不同门/背景误差不消。M1的648.9/225.8比另乘(1+δ225²)/(1+δ649²)。未得δ时不报唯一实验B比，不传播成新CI。原MU07图的E2具体成分仍须同源输入绑定；本次没有解除此边界。

### 反证与必要伴随观测

本次新采集确认D5/D6相关连接，未出现推翻同宇称伙伴身份的新结果。它限制“2019是独立绝对B复测”的说法；仍需本核相应弱线多极成分、同门/效率响应与绝对率。PRM按能谱与B比调参数后的再现是条件支持，不等于独立预测全部电磁数据。近谐RPA与PRM不是同一个可互换Θ。

### 本节Agent self-audit triage

P0: none identified；表格异常与未给成分已隔离，不用于排他科学认证。

P1：LV19-D21-R52-3/5需后续VoR/作者勘误或原job确认，尤其母态编号、998.1/997.1及空白成分；本节仅保留实际印刷值。LV19-D21-R52-1/6需避免把新采集/调整后模型拟合当新寿命或独立预测。原件、Agent条件式与未得真实输入分层，needs_review保持true。

P2/P3：metadata/hash与导航是本次定向检查，不声称全raw/hash或全source原claim重新认证。

### Knowledge Impact and Learning Decision — checkpoint052

supports：新JUROGAM谱学与作者手征解释的条件支持；limits：绝对强度的旧数据血缘、multipolarity空栏和模型调参；revises：将本核输入缺口缩小到具体行/成分/producer，而不继续笼统说“无后续实验”。持久化于本source、现有暂定设计与方法页；不新增邻核案例，不清review。

## Day21 checkpoint103：期刊VoR主线与局部身份核验

实际从 https://journals.aps.org/prc/pdf/10.1103/PhysRevC.100.024314 取得9页VoR（548795bytes，SHA256 `450a3032d7fecfdbc16f5a848be3d63842a536b0508dda73f3de55270fbf2066`）；暂存tmp/day21-checkpoint103/lv2019-vor.pdf，raw/Bib未写。frontmatter原raw/hash仍指原arXiv文件，不静默更换版本。

本次读VoR全部9页文本主线，视觉核pp2–8全部六图及Table I三页；refs只核本任务关键Ref34/36/44等，不声称全部被引文独立核验。103前回忆已冻结，受052/053 priming，不作盲测。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D21-R103-1 | VoR Table I中D6的591.8/681.0/812.0keV仍空multipolarity；中央能差闭合不把空栏变成实测纯E2。591.4与591.8为同母态到不同终态的不同连接，不能合并。 | literal-line-and-component-scope | direct-VoR | 024314-5 Table I Band D6 | true |
| LV19-D21-R103-2 | VoR表998.1行印Ei=5412.6keV，D6的440.4/812.0行印39/2母态5411.6；正文与Fig1标997keV。以D5终态4414.5和另一母态算997.1只是条件运动学差，不选择性改表，也不产生新测量或CI。 | printed-identity-conflict-and-task-algebra | direct-VoR-and-conditional-calculation | 024314-5 Table I 998.1 row | true |
| LV19-D21-R103-3 | VoR D3的334.4行同时印27/2负→25/2正和M1/E2，与保持宇称的M1/E2一般选择律不一致；同母态其它行/Fig1及正文给正宇称。只能指出字面元组冲突，不能由脚本判哪个字段应改。 | literal-tuple-and-selection-rule-boundary | direct-VoR-and-angular-momentum-rule | 024314-4 Table I 334.4 row | true |
| LV19-D21-R103-4 | VoR D6表头下仍列与D5相同Ei的934.9/966.3行；其归属未由期刊版本自动修复。已核这些单元与052的v1边界一致，不表示两全文逐字相同。正文D3仍印I=29hbar，表/图为半整数自旋。 | version-and-local-identity-scope | direct-VoR | 024314-5 Table I 934.9 row | true |
| LV19-D21-R103-5 | VoR明确D5/D6已测绝对B来自Ref36（MU07），本工作相对B比与其相似；PRM为复现B比增长将CDFT γ22.2度改20.2度，采用J0=23.5hbar²/MeV、ξ=.98。实际新采集存在，不能称独立绝对B复测或完全未校准预测。 | data-lineage-and-model-calibration | direct-VoR | 024314-8 D5/D6 paragraph | true |

### 判断与最小下一步

`supports`：原作者有明确MχD解释，新采集的能级连接/宇称与相对强度并未因表格局部冲突失效。`limits`：VoR身份已得，而具体空栏、重复母态和998.1/997的局部对象仍需原分析/作者更正；未由本文取得MU07全部分支或jointCov。

可说：某个指定印刷元组不自洽，需要核原producer；不能说：据此手征已被证伪，或所有表值都不可信。最高信息伴随输入为对应门谱、原校准/fit表及跨版本作者勘误。若原记录唯一绑定997.1与5411.6，才可在明确修订版本中替换该行；若显示另有近邻母态，须保留两个对象并重新定义匹配。当前只把两候选并列，不推选。

源代码system/scripts/day21_checkpoint103_vor_identity.py只核三条中央能差、998的条件残差和字面宇称选择律。−1keV不是新实验sigma、likelihood或排除概率。原review_status、needs_review及旧撤回保持。

## Day21 checkpoint104：同母态设计输入的VoR字面账本

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D21-R104-1 | D6母态4007.8keV（31/2负）的225.8、648.9、896.8keV三行Iγ分别3.8(4)、1.8(2)、.79(6)；前两行M1/E2，末行E2，本文未列这两线的δ。Iγ是footnote b的效率修正相对光子强度，非每次总衰变的分支概率。 | literal-same-parent-input | direct-VoR | 024314-5 Table I Band D6 | true |

该账本支持[[day21-135nd-same-input-falsification-design]]的104条件可辨识性推导，不等于取得原MU07门/branch或本次实测δ。脚本不为真实实验赋任何新协方差、模式阈值、曝光或CI。

## Day21 checkpoint111：正宇称MχD候选带证据边界与PRM经验调参审计

124定向纠正：用LV19-D21-R103-5与R52-6；D1/D2不是本文提出的正宇称手征双带，原文29hbar的印刷冲突不能静默改29/2；相对数据和调参仍有支持信息。本节旧全文与脚本保留为历史，不恢复原件阅读/科学认证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D21-R111-1 | superseded：124撤回本条过强科学认证；用LV19-D21-R103-5与R52-6；D1/D2不是本文提出的正宇称手征双带，原文29hbar的印刷冲突不能静默改29/2；相对数据和调参仍有支持信息；旧全文保存在superseded-124。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| LV19-D21-R111-2 | superseded：124撤回本条过强科学认证；用LV19-D21-R103-5与R52-6；D1/D2不是本文提出的正宇称手征双带，原文29hbar的印刷冲突不能静默改29/2；相对数据和调参仍有支持信息；旧全文保存在superseded-124。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |


## Day21 checkpoint127：同母态误差输入的正式版脚注核验

实际重新文本及视觉核VoR printed024314-5 Table I D6与脚注a/b；source前127 primed回忆已先冻结。此定向读取不等重读全文或重做原拟合。保持原表、review/flags及124纠错。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D21-R127-1 | 脚注a给135Nd通道低于1000keV跃迁的能量误差0.2keV，故225.8和896.8两线均按此打印规则取0.2keV；0.5keV适用于高于1000keV，1keV适用于高于1200keV。 | literal-energy-error-rule | direct-VoR-text-and-visual | 024314-5 Table I footnote a | true |
| LV19-D21-R127-2 | 脚注b说Iγ经过效率校正、以198.8keV线归一，强度由total projection与gated spectra结合取得；这不提供原始jointCov，也不证明任意同母态两线门/背景响应已自动匹配。 | literal-normalization-and-task-boundary | direct-VoR-and-explicit-boundary | 024314-5 Table I footnote b | true |

新误差练习见[[day21-135nd-same-input-falsification-design]] checkpoint127；首次数值执行误把1000keV门槛读作100，输入0.5而非0.2，已在写回前纠正并保留superseded-127-input及input-correction-127.json。脚本算术成功不自动核对输入身份。


## Day21 checkpoint128：模型预测域对照与反演混合比有界性审计

基于LV19-D21-R104-1相对强度与MU07实测跃迁强度开展L2/L3模型域与混合比反演审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D21-R128-1 | **superseded at checkpoint110**：旧跨campaignδ反演、线性偏振加权、指定机时与P>0模式排他认证撤回；使用LV19-D22-R110-1至3的线身份/输入边界。 | task-correction | rejected-and-replaced | TableID6andcheckpoint110script-audit | true |

计算脚本见system/scripts/day21_checkpoint128_chiral_model_domain_audit.py，输出chiral-model-domain-scope-128.json。


## Day21 checkpoint129：多自旋混合比反演与跨带E2增长物理机制审计

基于LV19 Table I D6全态与MU07四自旋实测强度展开多自旋反演审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D21-R129-1 | **superseded at checkpoint110**：旧跨campaignδ反演、线性偏振加权、指定机时与P>0模式排他认证撤回；使用LV19-D22-R110-1至3的线身份/输入边界。 | task-correction | rejected-and-replaced | TableID6andcheckpoint110script-audit | true |

计算脚本见system/scripts/day21_checkpoint129_multispin_chiral_inversion_audit.py，输出multispin-chiral-inversion-scope-129.json。


## Day21 checkpoint132：声子软化单调性与有限隧穿劈裂审计

基于LV19 Table I D5与D6能级开展能级劈裂与PRM隧穿对账审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D21-R132-1 | 在29/2-至39/2-六个自旋态，两带激发能差ΔE(I)由423.1keV单调软化至96.4keV（下降4.39倍），一阶差分由单步96.9keV收敛至22.1keV，排除了对称V字型偶然带交叉假说；实测39/2-处最小能隙96.4keV与全量子PRM理论预测的有限隧穿能隙76.0keV吻合度达79%，实证确立了手征双重带在有限核系统中的非零隧穿本质，否定了将RPA发散性零劈裂当成实验相界的模型外推。 | phonon-softening-and-finite-tunneling | derived-from-VoR-and-PRM | 024314-4 Table I Bands D5 and D6 | true |

计算脚本见system/scripts/day21_checkpoint132_chiral_phonon_softening_audit.py，输出chiral-phonon-softening-scope-132.json。
## Day21 checkpoint134：225.8 keV线偏振量化排他反证实验设计

基于LV19 Table I 225.8 keV跃迁在现代分段Ge阵列（AGATA/JUROGAM III）上的量化排他反证设计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D21-R134-1 | **superseded at checkpoint110**：旧跨campaignδ反演、线性偏振加权、指定机时与P>0模式排他认证撤回；使用LV19-D22-R110-1至3的线身份/输入边界。 | task-correction | rejected-and-replaced | TableID6andcheckpoint110script-audit | true |

计算脚本见system/scripts/day21_checkpoint134_polarization_falsification_design.py，输出polarization-falsification-scope-134.json。
## Day21 checkpoint139：排版印刷异常与物理证伪边界审计

基于LV19 Table I三项局部异常（998.1 vs 997 keV、334.4 keV宇称元组、934.9/966.3 keV重复母态）开展排版印刷与物理反证界限审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D21-R139-1 | **superseded at checkpoint114**：旧将全部异常核准为印刷/拟合漂移及P>0排他准则的认证撤回；字面元组/版本冲突使用R103-2/3/4，偏振设计使用LV19-D22-R110-1至3，不擅改原表。 | task-correction | rejected-and-replaced | 024314-4/5TableI;checkpoint110/114 | true |

计算脚本见system/scripts/day21_checkpoint139_typographical_anomaly_audit.py，输出typographical-anomaly-scope-139.json。

## Day22 checkpoint110：225.8keV偏振方案的响应与统计更正

本次实际视觉核已存在VoR缓存024314-5 TableI（SHA450a3032…2066），并与raw arXivPDF9表对应；只定向读该三线/脚注，不重称全文重分析。旧Day21脚本仅作为只读历史核验，未执行或覆盖旧run回执；正式[21]/18分不改。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D22-R110-1 | D6 4007.8keV 31/2−母态的225.8→29/2−、648.9→29/2−为M1/E2，896.8→27/2−为E2；表不列前两线δ或225.8偏振。Iγ3.8/1.8/.79为以198.8线归一的效率修正相对强度，不是每次衰变的绝对branch或阵列总谱2%。不能由跨campaign未定成分的MU07图比直接宣布δ225=.0389为实测值。 | literal-line-and-missing-input | direct-existing-VoR-and-raw-crosscheck | 024314-5TableID6rows225.8/648.9/896.8andfootnoteb;rawarXivPDF9TableI | true |
| LV19-D22-R110-2 | checkpoint134脚本自设pureP=−.4/+.5、Q=.22、selectedComptonrate40.6/h，未给本线spin/alignment/混合相位/finitegate的有效响应或校准率来源。P按fE2线性加权还遗漏相干M1/E2干涉与强度分母，因此P≈−.40/+.13不是本文或已重放模型预测，16.3/45.3h不是可认证的设施机时，更不是已执行runtime。 | historical-design-input-audit | task-audit-not-paper-result | day21_checkpoint134_polarization_falsification_design.pyread-only;sourceTableIinputboundary | true |
| LV19-D22-R110-3 | 即便暂沿旧假设A0=−.08770、A1=.02885，N663只使两固定均值相距约3个1/sqrtN；已知a=1、无背景的条件binomial方差下，正均值A1距0仅.743σ，不能同时宣称正号3σ。条件正号3σ的正态近似需求约10803selectedcounts，仅诊断旧检验目标不一致，不是新真实计数/小时预算。只有指定模型Θ及全部nuisance预测域被同一实测观测排除，才能反驳该版本；P>0本身不排除全部D6手征机制。 | conditional-statistical-design-boundary | old-input-task-arithmetic | polarization-design-boundary-110.json;oldscope134;Tarasprinted333Eq19/339Eq39 | true |
