---
type: source
title: "Lv et al. 2025 - Configuration-dependent shapes and rotations in 136Pr"
aliases: [Lv 2025 136Pr TAC-CDFT study]
created: 2026-09-30
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Configuration dependent shapes and types of rotations in the gamma-soft 136Pr nucleus revealed by detailed calculations with tilted axis cranking covariant density functional theory"
authors: [B. F. Lv, C. M. Petrache, Y. K. Wang, P. W. Zhao, J. Meng, J. G. Li, et al.]
journal: Physical Review C
year: 2025
volume: 111
pages: 014321
doi: 10.1103/PhysRevC.111.014321
arxiv:
language: en
canonical_source: "https://doi.org/10.1103/PhysRevC.111.014321"
zotero_item_key: ""
citation_key: ""
zotero_uri: ""
library_file: ""
raw_file: "raw/papers/gpt/day3-mean-field-20260929/136pr-2025-tac-cdfTAC/PDFs/Configuration_dependent_shapes_and_types_of_rotations_in_the_gamma-soft_Pr-136_nucleus_revealed_by_detailed_calculations_with_tilted_axis_cr.pdf"
raw_sha256: c8e14461975a7606d7e38325d6e83b500e75d232027b118743e1f1ff754537d6
nuclei: [136Pr]
reactions: ["100Mo(40Ar,1p3n)136Pr"]
experiments: [JUROGAM-II-136Pr-2025]
models: [tilted-axis-cranking, covariant-density-functional-theory, shell-model]
observables: [level-scheme, RDCO, Rac, B(M1)/B(E2), angular-momentum-alignment]
methods: [gamma-gamma-coincidence, directional-correlation, two-point-angular-correlation]
tags: [a130, 136pr, gamma-softness, tac-cdft, high-spin, configuration-assignment]
---

# Lv 等（2025）：136Pr 高自旋谱学与 TAC-CDFT 组态比较

## Bibliographic Record

Lv et al., Physical Review C 111, 014321 (2025), DOI [10.1103/PhysRevC.111.014321](https://doi.org/10.1103/PhysRevC.111.014321). 本地文件是 Jyväskylä 大学仓储的作者接收稿，来自 [该校开放仓储 PDF](https://jyx.jyu.fi/bitstreams/c9c701b4-dab3-4b19-8a3f-2aa95d467942/download)。Crossref DOI 元数据与接收稿首页题名、作者、卷和文章号一致。接收稿说明其分页与排版可能不同于正式出版版；以下定位均注明为本地 PDF 页。

## Scope and Reading Depth

- 已读正文主线，并核查 Fig. 1 能级纲图、Table I 的跃迁/强度/角关联数据、TAC-CDFT Figs. 6–16、Table II 组态与形变、摘要和结论。
- 覆盖重点：136Pr 新 JUROGAM II 高自旋谱、各带的角动量对齐与组态比较、pairing collapse、模型与数据不一致处、作者提出的竞争解释。
- 未覆盖：重新分析事件数据、重跑 TAC-CDFT/壳模型代码、与原始事件级数据或计算输入协方差做独立比较。
- 本次只获取主文。相关方法、数据表和图均在主文；目前没有发现依赖 SI 才能判读的关键输入或结果。
- 主张均保留 needs_review: true，本页仍为 unreviewed；模型输出不作实验事实。

## Summary

The paper combines a new high-statistics JUROGAM II 136Pr level scheme with PC-PK1 tilted-axis-cranking covariant density functional theory and a large-scale SN100PN shell-model discussion. It offers a direct modern model application to the same Hara Table 5 candidate, but it is not a projected-shell-model calculation and its configuration, deformation and mode assignments remain model-mediated.

## Active Recall Before Opening the Full Text

开全文前的记忆是：136Pr 为 Z=59,N=77 奇奇核；Hara–Sun Table 5 的星号是轴对称 PSM 拟合失败后的三轴候选。TAC-CDFT 应给旋转系下的角动量、组态和形变响应，但不能恢复总角动量好量子数。未知点包括 2025 计算是否真的使用角动量投影、D4/D6 是否是同一形变、对实验跃迁强度的拟合是否一致，以及弱连线是否独立确定宇称。原文核对后确认：这是同一核素的自洽 TAC-CDFT/壳模型研究，不是角动量投影；D4/D6 仍保留替代解释，Q1 宇称依赖模型推断。

## Experimental or Theoretical Setup

- 实验直接报告：100Mo(40Ar,1p3n)136Pr，40Ar 束流能量 152 MeV，JUROGAM II；作者报告采集 5.1×10^10 个三重及更高折符合事件，当前 136Pr 数据统计约为此前一项该核实验的 240 倍（摘要、Sec. II，本地 PDF pp. 2–3）。
- 自旋宇称判据：强跃迁使用方向相关比 RDCO；弱跃迁使用两个角度组的 Rac。Table I 给出 γ 线能量、相对强度、RDCO/Rac、多极性和能级指派（Table I，本地 PDF pp. 6–9）。
- TAC-CDFT：使用 PC-PK1，三维谐振子基底 10 个主壳，Bogoliubov 变换与有限程可分离配对力；若带头配对关联为零，作者对该带后续态关闭 Bogoliubov 配对。作者称 calculation 没有额外调参。正文明确讨论了粒子数投影可能避免 pairing-collapse jump，但未在本工作中实现（Sec. III.A，Fig. 6，本地 PDF pp. 9–10）。
- 另用 SN100PN 有效相互作用进行大空间壳模型计算，重点理解 D5 及其衰变到的正宇称低能态；作者指出实验与计算态之间难建立唯一对应（Sec. III.B，本地 PDF p. 13）。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV25-1 | 新 JUROGAM II 数据确认并扩展 136Pr 高自旋谱；论文图 1 给出 595-keV、Iπ=6+ 异能态以上的 D1–D6、Q1–Q4 能级纲图。 | experimental-fact | direct | Abstract; Sec. II; Fig. 1, PDF pp. 2–4 | true |
| LV25-2 | Table I 报告跃迁能量、初态能量、相对γ强度、RDCO、Rac、多极性和自旋宇称指派；相对强度以 209.5-keV 7+→6+ 跃迁归一。 | experimental-fact | direct | Table I, PDF pp. 6–9 | true |
| LV25-3 | Q1 的 875.6(4)-keV 连接跃迁测得 RDCO=0.47(8)，与拉伸偶极跃迁的标定值相符；其相对强度 2.9(2)，偏振分析因低计数和污染未能确定宇称。 | experimental-criterion | direct | Sec. II, PDF p. 3; Table I Q1 row875.6, PDF p.8; footnote e, PDF p.9 | true |
| LV25-4 | TAC-CDFT 使用 PC-PK1、10 个谐振子主壳及 Bogoliubov 配对；本工作不实施角动量或粒子数投影。 | synthesis | direct | Sec. III.A, PDF p. 9 | true |
| LV25-5 | Table II 的组态和 (β,γ) 是 TAC-CDFT 模型输出；D1/D2/D3/D4/D6 与 Q1/Q2/Q3/Q4 的带头形变约跨 β=0.16–0.24、γ=17°–39°。 | model-result | direct | Table II; Fig. 16, PDF p. 15 | true |
| LV25-6 | D1 的计算能量趋势接近实验，但计算 B(M1)/B(E2) 高于从所报告分支比得到的实验派生值。 | model-result | direct | Fig. 6; Sec. III.A, PDF pp. 9–10 | true |
| LV25-7 | D2 的计算 B(M1)/B(E2) 显著低于实验派生值；D3 的预测比值远高于 D1/D2。 | model-result | direct | Figs. 7–8; Sec. III.A, PDF pp. 10–11 | true |
| LV25-8 | TAC-CDFT 没有找到可描述 D5 的组态；作者随后使用 SN100PN 大空间壳模型讨论 D5 及其衰变到的部分低能态。 | model-result | direct | Sec. III.A–B, PDF pp. 11–13 | true |
| LV25-9 | 作者未在目标数据中识别手征转动、wobbling 或 oblate rotation；D4/D6 被讨论为可能磁转动，或作为另一种 D4 偏 prolate、D6 偏 oblate 的形状共存方案，二者是竞争解释。 | author-interpretation | direct | Sec. III.A–C; Figs. 9–11; Summary, PDF pp. 10–15 | true |
| LV25-10 | 2025 年模型计算与实验谱来自同一篇论文的同一 JUROGAM II 数据集，因而模型拟合不是独立实验确认；作者称新数据统计约为此前该核实验的 240 倍。 | synthesis | direct | Sec. II; Figs. 6–16; PDF pp. 2–15 | true |
| LV25-11 | 本次 arXiv、Crossref、OpenAlex、Semantic Scholar 和 INSPIRE 的限定检索未找到 136Pr/137Pr 的直接三轴 PSM/TPSM 全文；检索到并获取的 136Pr 2025 研究是 TAC-CDFT/壳模型，不是角动量投影。Google Scholar HTML 路由卡住并终止，故该路由未验证，检索不构成“文献不存在”的证明。 | our-inference | contextual | Day 3 bounded search record, 2026-09-30 | true |
| LV25-12 | 作者依据 TAC-CDFT 构型为 Q1 提出正宇称；该正宇称并未由本次偏振测量确定。 | author-interpretation | indirect | Sec. II, PDF p. 3 | true |
| LV25-13 | D1 的 TAC-CDFT 总角动量曲线在旋转频率约 0.35 MeV 附近因配对塌缩出现突跳；粒子数投影虽被提及可避免此非物理塌缩，但本研究未实施。 | model-result | direct | Fig. 6; Sec. III.A, PDF p. 10 | true |
| LV25-14 | D3 的带内交叉 E2 跃迁未观测到，因此该带实验 B(M1)/B(E2) 只能给出下限。 | experimental-fact | direct | Fig. 8; Sec. III.A, PDF p. 11 | true |
| LV25-15 | 作者把 D5 未找到 TAC-CDFT 组态视为近球形形变的间接线索，同时提醒 TAC-CDFT 在该形状区可能不适用。 | author-interpretation | direct | Sec. III.A–B, PDF pp. 11–13 | true |
| LV25-16 | 作者将Q1的876-keV link由先前14+终点改接Q2的18+，依据546/876双门谱仍见661/689；按stretched-dipole assignment带头自旋提高4ℏ到19(+)。正宇称仍为模型提议，非新偏振结果。 | experimental-placement-and-author-assignment | direct | PDF p.3 Sec.II; PDF p.4 Figs.1–2; PDF p.8 TableI Q1/Q2 rows | true |
| LV25-17 | 本文DCO不是一个全局阈值：TableI d为dipole gates、e为stretched-quadrupole gates。Q1列689/850门，D5列263，D6列231/354；caption给Q-gate下dipole≈.46/Q≈1，D-gate下dipole≈1/Q≈2.1。逐target实际gate组合及Cov仍未提供。 | experimental-gate-criterion | direct | PDF p.6 TableI caption; PDF p.9 TableI footnotes b/d/e | true |
| LV25-18 | TableI的4530.8-keV17+态有241.2、357.0、320.4到不同16+态；这些16+再经611.1、495.4、532.1到3678.4-keV15+。320.4和532.1的R/M栏为空，不能沿图自动补成已测pureM1。 | experimental-transition-crosswalk | direct | PDF p.7 TableI D4/D5; PDF p.8 TableI D6; Fig.1 | true |
| LV25-19 | 作者明确把旧band3分为D5/D6依据不同configuration（转Sec.III）；新544-keV E2与低端branch支持D5正宇称，先前D5负宇称是理论性tentative建议。分带不是只由新coincidence唯一证明的model-free划分。 | author-partition-and-experimental-boundary | direct | PDF p.6 Sec.II D5/D6 paragraphs; PDF p.8 TableI544.0 | true |
| LV25-20 | Sec.II明示本工作与Refs16/31使用same dataset；Ref16是135Nd PRC100,024314(2019)，Ref31是PRC98,044304(2018)。5.1×10^10为全采集fold≥3事件；136Pr约10% totalcrosssection不等于其selectedevent fraction。2025为发表年，不能据此定为新独立2025采集。 | acquisition-lineage-and-counting-boundary | direct | PDF p.3 Sec.II; PDF p.16 Ref16; PDF p.17 Ref31 | true |
| LV25-21 | Fig.4明确263/405峰来自136Pr D5，因为制作D3合并谱的230/334门也接收D5。TableI的D3与D5分别有打印334.4的条目；相同打印中心值不证明物理能量精确简并。 | experimental-shared-gate-counter-evidence | direct | PDF p.5 Fig.4 caption; PDF p.7 TableI D3/D5 rows334.4 | true |
| LV25-22 | Fig.5(a)星号为136Nd污染；Fig.5(b)的265峰因719门混入强lowlying722-keV line出现。共同门谱中的峰不能全自动作为同一目标路径成员。 | experimental-contamination-counter-evidence | direct | PDF p.5 Fig.5 caption | true |
| LV25-23 | Fig.10(c) D6使用向上箭头式点，TableI D6没有给出inbandE2 crossover。按单侧/限值边界保留这些点，原文未提供D6逐点limit构造或CL，不能当普通双侧误差ratio点给拟合χ²。 | display-fact-and-our-inference-boundary | mixed | PDF p.11 Fig.10(c); PDF p.8 TableI D6 | true |
| LV25-24 | 此accepted copy的Fig.10caption写D6的gd^4 unpaired形式，而TableII ConfigD6写gd^2且含sd^-4 neutronholes，具体配置列示不一致。PublisherPDF请求403，未核正式排版或erratum；保留版本内locator冲突，不断言计算代码用错配置。 | versioned-model-input-boundary | direct | PDF p.11 Fig.10 caption; PDF p.15 TableII ConfigD6 | true |
| LV25-25 | TableI脚注a称以209.5-keV7+→6+强度为reference，D1表列209.4(1)的I=64(4)，未声明reference必须100。本任务保留原标度，不凭常规习惯改I、补missingbranch或反推counts。 | normalization-boundary | direct | PDF p.9 TableI footnote a; PDF p.6 TableI D1 row209.4 | true |
| LV25-26 | 本接受稿TableI D5为3678.4-keV15+经405.1(1)到3273.3-keV14+，再263.1(2)到3010.2-keV13+；两者表列M1+E2。它与2018评价的263/405先后不同，原文这组表行不给出该差异原因。 | experimental-transition-record-and-boundary | direct | PDF p.7 TableI D5 rows405.1/263.1 | true |
| LV25-27 | D5的263.1(2)行在3273.3(10)母态，Iγ18.8(7)、R_DCO1.02(9)；405.1(1)行在3678.4(10)母态，Iγ14.9(7)、R_DCO.86(13)，二者M1+E2。此为相对γ强度，不是totaldecay流或completebranch保证。495.4(2)为4173.8→3678.4入口，可作母态tag候选，但逐门净计数未给。 | experimental-relative-intensity-and-parent-identity | direct | PDF p.7 TableI D5 rows263.1/405.1/495.4 | true |
| LV25-28 | 本acceptedcopy TableI PDF6–9可提取156条Eγ/Ei table rows，D1的1552.2 (3)母态含空格使strict-token规则漏一行。156是本任务表行提取数，不是作者报道的新γ/独立跃迁或完整levelscheme总数；同表重复334.4/200.0/近611/900的身份需逐parent核。 | our-table-extraction-and-identity-boundary | derived | PDF pp.6–9 TableI; D1 row366.7 PDF6; D3/D5 rows334.4 PDF7 | true |
| LV25-29 | D3的5086.3-keV18+母态经334.4/650.5到不同17+、经987.0到D2 16+；987的R_DCO2.07(14)d支持quadrupole，TableI列E2。SecII明确inband与若干link的E2 assignment含假设；表未给987独立POL列，π须按作者全图/已知锚与该假设的joint assignment记录。 | reported-angular-ratio-and-assignment-conditions | direct | PDF p.7 TableI D3 rows334.4/650.5/987.0; PDF p.3 SecII assignmentparagraph | true |
| LV25-30 | D3的660.4(4)来自4254.6 15+→D2 15+，R_DCO.82(24)d、M1+E2；653.0(4)的TableI M/R栏为空。前者不是purestretchedΔJ=1默认模型，后者不能由归带直接补实测M。 | experimental-transition-record-and-model-domain | direct | PDF p.7 TableI D3 rows660.4/653.0 | true |
| LV25-31 | TableI D4可逐同parent配16–23的dipole/crossoverγ对，Fig9(c)有8个对应spin的log-scale B(M1)/B(E2)点，单位μN²/(e²b²)。481、370.8、587.4、1117.9的table M栏为空（481正文称quadrupole）；重算需声明component/purity而非补写逐线已测pureM。文中未为该组给完整δ/Cov/逐点算法。 | reported-table-figure-and-input-boundary | direct | PDF p.7 TableI D4; PDF p.5 SecII D4; PDF p.11 Fig9(c) | true |
| LV25-32 | AcceptedTableII的valence十行相对Z50/N82给净9p/−5n；Q1/Q1*的unpaired neutron列仅列h11/2^-1与intruder^1，sd未列。若该列被当evenpairedreference上的完整pair-reduced inventory，listed(up,un)=(3,0)留下(6,−5)差，总差1为奇数，不能仅以任何two-fermion pairs补全；若active标签/未列spectator则解释不同。此为本任务条件审计，不证明程序错误。 | our-inference-from-literal-model-input | derived | PDF p.15 TableII ConfigQ1/ConfigQ1*; PDF p.11 Figs9/10captions | true |
| LV25-33 | TableII报D4(.17,35°)、D6(.19,39°)，Fig16仅展示γ0–60°扇区；PDF12另称D4γ<0绕medium axis、D6γ>0绕short axis为alternative shape-coexistence场景，并使用irrotational-flow假设。本文未给该alternative与表/图之间的逐态signedγ/轴映射，不能自行给D4改号或把两场景合为实验共存事实。 | reported-model-and-alternative-frame-boundary | direct-and-derived | PDF p.12 alternate D4/D6 paragraph; PDF p.15 TableII; PDF p.15 Fig16 | true |
| LV25-34 | D4的3937.2-keV15+母态经207.8(5)/265.0(4)到不同14+支路，Fig1将较高14+经208线接15+；481.0 crossover须沿该层级链核对。相同band标签、母态和ΔI不保证同一daughter/path。 | experimental-graph-and-input-boundary | direct-and-derived | PDF p.7 TableI D4 rows207.8/265.0/481.0; PDF p.4 Fig1 D4 | true |
| LV25-35 | D4中5934.5-keV20+、6444.8-keV21+母态的reported ΔI1 γ分别为503.6(2)、510.3(2)keV，中心能量差6.7keV；用它们构造任何曲率估计仍需声明stencil、频率位置及误差相关性，原文未给这些线的共同Σ。 | reported-energy-difference-and-boundary | direct-and-derived | PDF p.7 TableI D4 rows503.6/510.3 | true |

## Nuclear Structure Information

实验报告以 595-keV、Iπ=6+、T1/2=90 ns 异能态为基准的复杂高自旋结构。Fig. 1 显示 D1–D6 偶极带和 Q1–Q4 四极带；D3 为新观测带，原先一条高自旋带在本次分析中分为 D5、D6。Table I 的多极性由 RDCO/Rac 等约束，但若干高自旋指派仍带括号。

## Model Results and Authors' Interpretation

- TAC-CDFT 给出每条带的旋转系能量、总角动量、对齐、构型和形变；Table II 与 Figs. 6–16 是模型结果，不是直接测量的 β、γ 或轨道占据。
- D4/D6 的自洽最佳组态分别含不同 h11/2 质子 Ω；作者另保留磁转动与 prolate/oblate 三轴形状共存两种解释。
- Q1 正宇称没有由偏振测量确立，而由模型帮助选择；不得把模型给出的宇称或构型标签并入实验事实。
- 文章讨论的是本次 136Pr 谱学和 TAC-CDFT/壳模型，不是 projected-shell-model 重算，也不恢复良好总角动量。

## Competing Interpretations and Limitations

- The authors leave D4/D6 as either possible magnetic rotation or a prolate/oblate triaxial shape-coexistence scenario; neither alternative is independently established by the calculated deformation table.
- D1 calculated B(M1)/B(E2) values are above the experimental derived values, D2 values are below them, and TAC-CDFT does not find a configuration for D5. These model-data limits prevent treating the overall reasonable energy fit as a unique configuration proof.
- Q1 positive parity is proposed with TAC-CDFT support after polarization analysis of the weak 875.6-keV link was inconclusive.
- Pairing collapse, omitted particle-number projection and absence of total-angular-momentum restoration limit the mean-field comparison.

## Counter-Evidence and Missing Companion Observables

- 对唯一解释的反证来自模型自身：D1 与 D2 的 B(M1)/B(E2) 偏差方向相反，D5 没有匹配 TAC 组态；pairing collapse 与未做粒子数投影也限制高自旋解。
- Q1 的 875.6-keV 跃迁只支持偶极性质，偏振因低计数与污染不能确定宇称；需更高统计且可控污染的线偏振/角关联测量。
- D4/D6 的模型竞争需要 partner-resolved lifetime、绝对 B(E2)/B(M1) 或 Qt，以及独立形状敏感观测来区分磁转动与形状共存。
- Table II 中形变与 Fig. 16 采用的坐标表示和正文“γ<0°/γ>0°”替代方案还需按作者具体轴约定作进一步复核；当前不将两种解释合并。

## Related Knowledge and Project Relations

- [[136pr]]：核素级实验能级、观测判据和竞争解释汇总。
- [[hara-sun-1995-projected-shell-model-high-spin]]：HS10-4 将 136Pr (N=77) 列为 “presumably triaxial” 候选；它是旧轴对称 PSM 的模型推断。
- [[a130-model-choice-card]]：区分 136Pr TAC-CDFT/SM 应用和 TPSM 投影覆盖计数。
- [[tilted-axis-cranking]] 与 [[covariant-density-functional-theory]]：TAC-CDFT 方法输入、输出与 projection 边界。

## Knowledge Impact and Learning Decision

Decision: revises. 136Pr 从“后续投影覆盖待查”更新为“已有 2025 直接核素 TAC-CDFT/SM 与新实验谱学；尚非 PSM/TPSM 投影复算”。它加强了模型对这一候选核的可比较性，但不能把模型形变或模式解释升级为实验形状事实。

## Human Review Triage

- P1：核对 Q1 宇称是否在后续实验中得到独立验证；保持 LV25-3 的实验事实与模型指派分层。
- P1：复查 Table II、Fig. 16 和 D4/D6 替代形状方案的 γ 轴/转轴约定，不能把二者写成已决形状共存。
- P2：粒子数投影未实施；D5 的模型归类仍依赖较不唯一的大空间壳模型对应。

## Extracted Pages

- Nuclei: [[136pr]]
- Models: [[tilted-axis-cranking]], [[covariant-density-functional-theory]], [[cranked-shell-model]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]]
- Projects: [[a130-model-choice-card]]


## Day14接受稿复核：连接终点、门与版本边界

本次核SHA与Crossref HTTP200、题名/首作者/PRC111/014321/2025-01-16一致。当前raw是Jyväskylä self-archived **Accepted version (Final draft)**，共17 PDF页，其中第1页为cover，印刷页=PDF页−1；不是已核正式publisher排版。沿PDF2–15全部正文主线、16–17 references，视觉复核Figs1–16及TableI关键rows/全部gating脚注和TableII；红色修订文字也属这份版本，不视为额外实验。PublisherPDF单次403 HTML，未绕认证/挑战，不将本版caption冲突写成officialerratum。

新增LV25-16–25保留源图/表细节：Q1实际endpoint重排与π边界、D6三条并行支路及weakline空栏、sharedgates的真实反例、D5/D6模型辅助分组和one-sided显示、sharedacquisition与versioned配置冲突。旧LV25-1–15的needs_review true保持；LV25-3的表行locator修到PDF8（gating脚注在PDF9）。旧12–15因表中空行未被claimparser读取，现合回同表，内容/flags未升级；这不是四条新实验或新人审。

[37-check crosswalk](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-scheme-crosswalk.json)直接核immutablePDF行，并以声明independentquotedσ给两cycle残差−.1/−.2keV及相关矩阵；source真实jointΣ仍unknown。可复用逐边表、Q1重排和限制在[[level-scheme-reconstruction]]“136Pr：双门重排、共享门峰与模型分带”，核素入口[[136pr]]，[[a130-thesis-evidence-matrix]]新增实际A130 row。

[[lv-2019-chirality-135nd-reexamined]]是本文Ref16，并非因核素/发表年不同就有独立acquisition。[[jurogam2-135nd-ar40-152mev]]保持135Nd channel视角并记录samepool的136Pr branch；actualselection、calibration、gateΣ仍逐分析待核。没有把135Nd偏振或τ移给136Pr。决定supports source-level Q1连接重排与正宇称边界，revises“新发表=新采集”/“band标签=模型无关”/“所有点均双侧测量”；D4/D6磁转动和形状共存仍竞争，β/γ是模型，不裁决新模式。


### 截止前已读的旧评价比较

[[nndc-2018-136pr-selected-level-gamma-records]] N136-3/4保存旧Q1 endpoint与263/405次序，N136-8保存1996全文未取得边界。LV25-26是本接受稿的直接表行，不将差异原因预填为作者改排或评价者错误；详细比照见[[level-scheme-reconstruction]]“136Pr：2018评价与2025接受稿的顺序冲突”。本段在硬截止后仅收束既有摘录，没有开新研究。


### Relative I与顺序的条件流量设计

LV25-27与[[nndc-2018-136pr-selected-level-gamma-records]] N136-9为两次不同采集/标度的RI，不能混成一组强度。[[level-scheme-reconstruction]]“136Pr：相对强度、缺失分支与独立母态标签”用真实表行的zeroIC声明control检验哪些条件能定序；fraction不是本实验branchlimit，不转成新absoluteB或顺序裁决。


### TableI的逐行候选图

LV25-28的156行由[day14_pr136_transition_candidates.py](../../system/scripts/day14_pr136_transition_candidates.py)核actualPDF SHA/四页表行、weaklimit与空栏，44项checks完成。与[[nndc-2018-136pr-selected-level-gamma-records]]旧135条placedγ建立discovery graph，所有keV窗口自选非σ阈值。[[level-scheme-reconstruction]]“136Pr：逐线候选图与energy-nearest的失败”保存完整范围/反例；候选唯一不等身份唯一，零候选不等新发现，不以算法配对覆盖sourcegraph。


### D3的new-band与旧level候选分层

LV25-29/30与[[nndc-2018-136pr-selected-level-gamma-records]] N136-10给出同约5086-keV母态/650γ的旧新候选关联；源只把D3叫newband，不凭此将所有levels/lines认证为首次发现。[[level-scheme-reconstruction]]“136Pr D3：新带、旧态候选与宇称handle”保存小图、13项row/assumption自审和条件边界。作者的E2/positiveπ标签保持为原reportedassignment，不把R2.07当独立测到electric character，也不反向改成作者赋值错误。


### 同parent强度比的条件表图复核

LV25-31的16条literalrow按8个parent配对。[[bm1-be2-ratio]]“同母态radiative比值的抵消条件”与[[level-scheme-reconstruction]]“136Pr D4：同母态比值重算与绝对强度的区别”保存SIrate→κ、δ/纯度和共分母抵消；71checks给δ0/purecrossover控制数与Fig9(c)在图精度下一致。该一致只为同acquisition的内部校核，不证明作者实际δ=0、原Cov模型或纯度，不增加新强度测量。四个M空栏、tentative23与D6单侧点保持；没有重估absoluteB或裁决MR/shapecoexistence。


### TableII列示与完整模型输入

LV25-32与[[configuration-occupation-audit]]的62-check限定了**完整unpaired列解释**；所有valence列Z/N实际记账通过，没有识别到实际程序粒子数不守恒。未列spectator/参考态与blocking定义没有提供，不能修入一个νsd hole或根据literal5项断言真实state属半整数I。[[a130-model-choice-card]]和[[136pr]]保存scope，Hara直接投影覆盖仍2/7。Goodπ标签乘积不补Q1实验POL缺口，源的positiveπ proposal及β/γ/modelinterpretation状态不升级。

## γ、模型形状与替代转轴场景的定向复核

LV25-33将PDF12的alternative段与PDF15的TableII/Fig16分开。Fig11的ConfigD6还显示同时非零的Jx/Jz，正文以此说明tilted nature；不能把替代场景中的principal-axis描述倒填为所有实际TAC态的唯一转轴。当前没有原始quadrupole tensor、逐态signed axis map或alternative的独立数值解。

[[triaxial-deformation]]“形状张量、轴置换与signedγ分开”用声明的无量纲quadrupole normal form证明±γ可只是proper axis permutation，配合假设irrotational law展示固定转轴与同步换轴的差别。50项检查读取本表十行rounded模型参数，但几何形式、惯量标度和控制±20°均明确非作者实际frame/实验量。证明只涉及四极张量，不认证完整密度/波函数相同，也不以cos3γ裁决作者prolate/oblate措辞或重排D4γ号。

因此原P1的几何必要条件和场景分层已推进，实际作者轴映射仍开放；D4/D6 MR与shape-coexistence继续竞争，缺失E2/POL/寿命不能由几何补。原claims/review保持，实际程序未重跑。

### Ref48的实际证据层级

后续直接核读[[petrache-2015-nd-exotic-rotations-triaxiality]]全文及Fig1/Table1。PT15-5把calculated负/正γ与中间/短轴联系，PT15-6仍要求寿命检验轴变化，PT15-4说明J^(2)选带/均值/图示删点。它补的是本段alternative的Nd系统学语境，没有136Pr逐态轴映射，也没有完整展开D4/D6特定lowΩ/highΩ极化输入。故Ref48引用本身不补actual frame/共存实证，原LV25-33及review状态保持。

### D4有序能量练习

LV25-34/35回到实际TableI/Fig1，支撑[[level-scheme-reconstruction]]“136Pr：动力学惯量需要有序路径”与[[moments-of-inertia]]的71-check练习。这里的相邻/跨两条/偶奇crossover曲率是本任务明确stencil与位置的派生值，不是作者新增J2数据；四个M空和I23tentative保持。Closure的非零小残差未强制修平，共同Σ缺失；声明筛选敏感性不等于重算Nd51/23或给Pr定γ/轴。原claims/review保留。

## Day19量化审计：136Pr微观组态形变谱、三轴形状共存与N=77手征终止分水岭

**checkpoint088：撤回旧科学认证；原标题保留为历史anchor。**

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LV25-D19-1 | checkpoint086撤回形状共存/手征终止认证：TableII十行beta/gamma是不同组态的TAC-CDFT输出，均值差18.3度不是实测形状劈裂或共存观测。PDF13 SecIII.C说未观察到chiral/wobbling/oblate rotation，D4/D6的possible MR与oblate-prolate coexistence是替代场景。不能推136Pr绝不手征或N=77严格终止。未找到D5对应TAC构型不证明无任何变形极小或唯一球形结构。Q1+4hbar归作者的连接/拉伸指派，positive parity仍未由POL确定；同采集谱系和ConfigD6版本差异仍保留。 | source-and-analysis-correction | direct-where-reread-otherwise-withdrawn | checkpoint088 source scope and rejection registry | true |

## checkpoint088：未观察到与排除不可能分开

本轮定向重读接受稿PDF13 SecIII.B/C、PDF15 TableII与summary的文本；本轮未新视觉核全套TAC图，不声称独立计算。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LV25-D19-2 | 原文did not observe chiral rotation/wobbling/oblate rotation，是本研究结果范围；possible magnetic rotation或oblate-prolate coexistence是D4/D6的两替代解释。TableII beta/gamma是模型参数，不能用平均gamma差认证共存观测或发明N=77手征终止线。D5壳模型的多state对应亦非唯一；保持Q1宇称、D6版本、缺τ/δ/E2及同acquisition边界。 | author-wording-and-model-boundary | direct-original-and-boundary | accepted PDF13 SecIII.B/C; PDF15 TableII/Summary | true |
## Day20量化审计：136Pr磁转动剪刀机制、TAC-CDFT微观形变与N=77边界去普适化（checkpoint031）

> checkpoint032：本节旧认证已撤回；程序通过只曾检自设输入。以下R32为本次定向原读纠正。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LV25-D20-1 | checkpoint032：旧科学认证撤回，原因：Fabricated ratio array contradicted Fig9c; imposed angle closure not measured; correlation of invented values not evidence; possible MR/shape coexistence alternatives turned into observed/exclusive facts.；当前可用陈述见下方R32原读纠正。 | withdrawn-task-certification | rejected-and-replaced | checkpoint032; LV25-D20-R32-1 | true |

## checkpoint032：原件定位与科学认证纠正

本次Codex self-audit，原review状态与全部已有claim flags保持；不是新增独立实验或全文阅读认证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV25-D20-R32-1 | PDF11 Fig9c原D4点非旧7.8到.8严格单调数组；旧9.75倍、剪刀角/r认证均撤回。TableI同parent八组比只可在明示δ/purity下重算中央值；四条M空、I23tentative保持。PDF12/13仍possible MR与oblate-prolate coexistence两方案；TableII形变为模型而非实测塌缩。 | plot-and-interpretation-correction | direct-original-and-visual | PDF7 TableI D4; PDF11 Fig9c; PDF12 alternative paragraph; PDF13 SecIII.C; PDF15 TableII | true |


## Day20量化审计：磁转动剪刀机制对决手征双重带、平面倾斜旋转与N=77边界去普适化（checkpoint134）

> checkpoint146：本节121–145批次的科学认证已撤回。旧文本/输入与指纹保存在本run的history-before-repair-146.json；原始原件与既有review/flags保留。自设数值或flag的passed只验证算术，不识别实际producer、共同Cov、实验CI或唯一模式。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LV25-D20-R134-1 | checkpoint146撤回旧认证；不据此恢复错误表值、跨态强度阶梯、硬阈值或完全闭合。请使用本页较早原件纠错与checkpoint146。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |
