---
type: source
title: "丁兵 2012 博士论文：过渡区核 127, 128I 高自旋态能级结构研究"
aliases: ["丁兵2012博士论文", "Ding2012Thesis", "High-spin studies of transitional nuclei 127, 128I"]
created: 2026-09-02
updated: 2026-10-16
status: ai-draft
review_status: unreviewed
source_type: thesis
reading_depth: deep-read
title_original: "过渡区核127, 128I 高自旋态能级结构研究"
authors: ["丁兵"]
advisor: ["张玉虎"]
journal: "中国科学院近代物理研究所博士学位论文"
year: 2012
language: zh
canonical_source: "丁兵. 过渡区核127, 128I 高自旋态能级结构研究[D]. 兰州: 中国科学院近代物理研究所, 2012."
citation_key: ""
library_file: "raw/papers/degree dissertation/丁兵 - 博士论文.pdf"
raw_file: "raw/papers/degree dissertation/丁兵 - 博士论文.pdf"
raw_sha256: "ca7765ad962ea0c106791532f5a7d9f359533d25bb0170f03197bfec414be5c7"
nuclei: ["127I", "128I"]
reactions: ["124Sn(7Li, 4n)127I", "124Sn(7Li, 3n)128I"]
experiments: ["tsukuba-127-128i-li7-28-32mev"]
models: ["NPA", "PES", "empirical-shell-model", "Nilsson-model"]
observables: ["energy-levels", "gamma-transitions", "ado-ratio", "multipolarity", "excitation-functions"]
methods: ["in-beam-gamma-spectroscopy", "gamma-gamma-coincidence", "angular-distribution", "parabolic-rule"]
tags: [high-spin, transitional-nuclei, iodine-isotopes, decoupled-band, gamma-soft, shape-coexistence, two-quasiparticle, three-quasiparticle, NPA]
---

# 丁兵 2012 博士论文：过渡区核 $^{127, 128}\text{I}$ 高自旋态能级结构研究

## Bibliographic Record

- 论文题目：过渡区核 $^{127, 128}\text{I}$ 高自旋态能级结构研究
- 英文题目：*High-spin studies of transitional nuclei 127, 128I*
- 作者：丁兵（指导教师：张玉虎 研究员、博士）
- 学位授予单位：中国科学院研究生院 / 中国科学院近代物理研究所
- 答辩与提交日期：2012 年 4 月
- 原始文件：`raw/papers/degree dissertation/丁兵 - 博士论文.pdf` (SHA-256: `ca7765ad962ea0c106791532f5a7d9f359533d25bb0170f03197bfec414be5c7`)

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: 全文 7 章、100 页。覆盖第 1 章引言、第 2 章理论模型（壳模型、Nilsson 模型、两准粒子抛物线经验规律、PES 势能面、NPA 核子配对近似）、第 3-4 章实验与离线数据处理（筑波大学串列、HPGe 阵列、$\gamma$-$\gamma$-t 符合、DCO/ADO 方法）、第 5 章 $^{127}\text{I}$ 能级结构与 PES 讨论、第 6 章 $^{128}\text{I}$ 能级结构与 NPA/经验壳模型计算、第 7 章结论及发表文章目录。
- Not covered: 具体的底层电子学线路硬件排线细节和单道原始脉冲波形。
- Coverage caveats: 学位论文为中文撰写，实验中未测量绝对跃迁几率、寿命或线偏振；两个核素的实际多极性指认主要依据 ADO 系数、符合强度、内转换系数、系统学比较与理论计算。

## Paper Question and Scientific Motivation

- Author-explicit motivation and locator:
  - $A \approx 130$ 过渡区原子核处于球形核向长椭球形变过渡带，费米面紧邻 $h_{11/2}$ 高 $j$ 轨道与 $g_{7/2}, d_{5/2}$ 轨道，具有极软的势能面（$\gamma$-soft 与 $\beta$-soft），是研究集体运动与单粒子激发共存与竞争、形变演化及能带终结的理想场所（pp. 1-5, 82-83）。
  - 在奇 $A$ 碘同位素中，研究高 $j$ $\pi h_{11/2}$ 质子与偶偶 Te 核芯的耦合机制，检验退耦带在最丰中子稳定碘核 $^{127}\text{I}$ 中的延伸，并澄清正宇称低位 $\Delta I=2$ 序列究竟是独立退耦带还是单一强耦合高 $K$ 带的旋称分支（pp. 2-5, 48-65）。
  - 在双奇核 $^{128}\text{I}$ ($N=75$) 中，纠正前人错误的高自旋纲图，建立新的完整能级纲图，研究 $\pi g_{7/2}/\pi d_{5/2} \otimes \nu h_{11/2}$ 与 $\pi h_{11/2} \otimes \nu h_{11/2}$ 组态的激发模式，探索从轻双奇碘核（强转动特征）向重双奇碘核过渡时单粒子运动对集体运动的主导性增强（pp. 3-5, 66-81, 82-83）。

## Method and Design Logic

- Author-explicit design logic and locator:
  - 采用重离子熔合蒸发反应 $^{124}\text{Sn}({}^7\text{Li}, x\text{n})^{127,128}\text{I}$ ($x=4, 3$)。28 MeV 主要布居 $^{128}\text{I}$ 的 3n 道，32 MeV 主要布居 $^{127}\text{I}$ 的 4n 道；$^7\text{Li}$ 束流由日本筑波大学串列加速器提供（PDF p.35，印刷页 27；PDF p.57，印刷页 49）。
  - 探测装置为在束 $\gamma$ 谱仪阵列：9 套带 BGO 反康普顿屏蔽的同轴 HPGe 探测器和 1 套小平面 HPGe 探测器；5 套 HPGe 位于相对束流约 $37^\circ/143^\circ$，其余位于约 $90^\circ$（PDF p.57，印刷页 49）。
  - 测量 $\gamma$ 射线激发函数、X-$\gamma$ 符合和 $\gamma$-$\gamma$-t 快慢符合事件。论文介绍 DCO 与 ADO 两种方法，但明确说明本实验两个核素实际使用 ADO 系数指定多极性；表 5.1、表 6.1 的实验列均为 $R_{\text{ADO}}$（PDF pp.53-55、57，印刷页 45-47、49）。
  - 结合组态限定势能面（PES）方法计算 $^{127}\text{I}$ 的多准粒子形变与激发能；结合经验壳模型（加结合能项与剩余相互作用 $\Delta$）及核子配对近似（NPA）计算 $^{128}\text{I}$ 的低位多重态激发能（pp. 16-21, 62-65, 73-81）。

## Key Evidence and Reasoning Chain

- $\gamma$-$\gamma$ 符合、强度平衡、平行/交叉跃迁和能量加和关系 → 建立 $^{127}\text{I}$、$^{128}\text{I}$ 的能级纲图（Fig.5.2、Fig.6.2；PDF pp.59、77）。
- ADO 系数、已知低能级和内转换系数 → 约束跃迁多极性及高自旋能级的自旋宇称（Tables 5.1、6.1；PDF pp.60-63、78-80）。
- 与偶偶核芯及邻近奇质量/双奇核的能级系统学比较 → 提出 $\pi h_{11/2}$ 退耦带、$\pi g_{7/2}/\pi d_{5/2}$ 高 $K$ 正宇称结构和 $^{128}\text{I}$ 的两准粒子组态。
- PES、NPA 和经验壳模型 → 为组态指认提供模型约束；这些结果不是直接实验观测，且部分能级仍有模型依赖或顺序差异。

## Summary

丁兵 2012 年博士学位论文利用日本筑波大学串列加速器提供的 $^7\text{Li}$ 束流和 $^{124}\text{Sn}$ 重离子熔合蒸发反应，研究了过渡区核 $^{127}\text{I}$ 和 $^{128}\text{I}$ 的高自旋态能级结构。在 $^{127}\text{I}$ 中建立了包含 75 个能级、近 150 条 $\gamma$ 跃迁的新能级纲图，将建立在 $11/2^-$ 态上的 $\pi h_{11/2}$ 退耦结构延伸到约 $(35/2^-)$；将前人认为的两个正宇称 $\Delta I=2$ 序列重解释为同一高 $K$ $\pi g_{7/2}$ 结构的旋称分支，并另行指认为 $\pi d_{5/2}$ 带；同时观察到建立在 $15/2^+$ 和 $23/2^+$ 三准粒子态上的非集体/集体激发共存。对 $^{128}\text{I}$，论文修正了历史纲图，首次给出高自旋态的自旋宇称，并用 NPA、经验壳模型与系统学比较讨论低位两准粒子结构，指出 $N=75$ 处单粒子运动增强。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| D12-1 | 实验利用 32 MeV $^7\text{Li}$ 的 $^{124}\text{Sn}(7\text{Li},4n)^{127}\text{I}$ 反应建立了 75 个能级、近 150 条 $\gamma$ 跃迁的 $^{127}\text{I}$ 能级纲图；表 5.1 给出实验 ADO 系数。 | experimental-fact | direct | PDF p.57-60（印刷页 49-52）、Fig.5.2、Table 5.1 | true |
| D12-2 | $^{127}\text{I}$ 中 $11/2^-$ 至 $27/2^-$ 的序列与偶偶核芯 $^{126}\text{Te}$ 晕带能级间隔相似，作者据此指认为 $\pi h_{11/2}$ 退耦带；序列整体还观测到约 $(35/2^-)$、5242.7 keV 的更高自旋延伸，但 $I>27/2$ 区域出现不规则性，不能无条件视为同一规则退耦段。 | author-interpretation | direct | PDF p.58（印刷页 50）、PDF p.66（印刷页 58）、Fig.5.2 | true |
| D12-3 | 实验观察到连接两个正宇称 $\Delta I=2$ 序列的强带间跃迁；论文讨论了已知的 593.3、549.8 keV 连接线，并报告了新的 850.5、912.4 和 812.3 keV 四极跃迁，从而把前人所谓两条独立退耦序列重解释为同一高 $K$ $\pi g_{7/2}$ 结构的两个旋称分支。 | experimental-fact | direct | PDF p.58（印刷页 50）、PDF p.67（印刷页 59）、Table 5.1 | true |
| D12-4 | 带 B 的强 $\Delta I=1$ 带间跃迁和 ADO 系统性低于纯偶极基准的结果，与负的 $E2/M1$ 混合比相容；作者将其主要组态指认为具有小扁椭形变的高 $K$ $\pi g_{7/2}[404]7/2^+$，带 C 则指认为 $\pi d_{5/2}[402]5/2^+$。 | author-interpretation | direct | PDF pp.67-68（印刷页 59-60）、Fig.5.5 | true |
| D12-5 | 在 $^{127}\text{I}$ 较高自旋区，观测到建立在 $15/2^+$（2068.4 keV）和 $23/2^+$（2901.2 keV）上的非规则非集体结构 E/F 与规则类转动结构 D 在相近激发能区共存。 | experimental-fact | direct | PDF pp.68-70（印刷页 60-62）、Fig.5.6 | true |
| D12-6 | PES 计算给出很浅且对 $\beta/\gamma$ 形变柔软的势能面；表 5.2 中存在与实验 $15/2^+$（2068 keV）和 $23/2^+$（2901 keV）相容的候选组态能量，作者据此支持三准粒子组态及集体/非集体激发共存的解释，但形状参数依赖坐标和模型约定。 | model-result | direct | PDF pp.70-72（印刷页 62-64）、Table 5.2、Fig.5.7 | true |
| D12-7 | 在双奇核 $^{128}\text{I}$ 中以已知 175 ns、$(6^-)$ 同质异能态为锚建立新高自旋纲图，并首次给出高自旋态激发能和作者建议的自旋宇称；当前可核的第六章正文未明确给出全纲图总级数/总跃迁数，具体标签仍受 ADO 歧义和模型辅助限制。 | experimental-fact | direct | PDF pp.76-79（印刷页 68-71）、Fig.6.2、Table 6.1 | true |
| D12-8 | $^{128}\text{I}$ 的低位负宇称多重态中，约 167.4 keV 的 $6^-$ 同质异能态和 183.0 keV 的 $7^-$ 态主要对应 $\pi d_{5/2}\otimes\nu h_{11/2}$；约 226.0 keV、269.6 keV 和 285.2 keV 的结构主要对应 $\pi g_{7/2}\otimes\nu h_{11/2}$。NPA 重现了主要间隔趋势，但部分 $6^-/7^-$ 理论顺序与实验相反，且 $8^-$ 组态还需经验壳模型与系统学支持。 | model-result | direct | PDF pp.82-83（印刷页 74-75）、Fig.6.6、Table 6.1 | true |
| D12-9 | $^{128}\text{I}$ 负宇称结构 B 建立在 285.2 keV $8^-$ 态上，主要路径为 696.2 keV $9^-$、1041.7 keV $10^-$、1454.0 keV $11^-$ 和 1873.5 keV $12^-$；作者将其指认为 $\pi g_{7/2}\otimes\nu h_{11/2}$ 类转动结构，并指出相对于较轻同位素集体特征减弱。 | author-interpretation | direct | PDF pp.84-85（印刷页 76-77）、Fig.6.7、Table 6.1 | true |
| D12-10 | $^{128}\text{I}$ 正宇称 $1460.9\text{ keV} (9^+)$、$1562.2\text{ keV} (10^+)$ 和 $1964.9\text{ keV} (11^+)$ 能级指认为 $\pi h_{11/2}\otimes\nu h_{11/2}$ 两准粒子多重态；经验壳模型计算偏差为 22、44、47 keV，NPA 重现了主要劈裂和 $10^+$ 的绝对激发能，但计算的 $11^+$ 低于实验。 | model-result | direct | PDF pp.85-87（印刷页 77-79）、Fig.6.8 | true |
| D12-11 | 沿双奇碘核同位素链比较，$^{128}\text{I}$ 中的能级间隔呈现无规则化、平行跃迁增多且类转动特征减弱；作者据此认为在 $N=75$ 处单粒子运动增强并在高自旋激发模式中占主导，同时当前数据看不出明确手征双重带迹象。 | author-interpretation | direct | PDF pp.88-91（印刷页 80-83）、Fig.6.9、Table 6.2 | true |

| D12-12 | Figure 3.3 compares CASCADE and PACE calculated excitation functions for the `7Li + 124Sn` reaction and identifies 3n, 4n and 5n as the leading channels; calculated cross-section maxima for `128I` and `127I` are near 26 and 32 MeV. The text warns that these calculations show trends and that experimental excitation-function information is needed to choose beam energies. | model-result | direct | PDF pp.34-35, Fig.3.3 | true |
| D12-13 | The measured total `γ-γ` projection spectra at 32 and 28 MeV show established `127I` lines (490.4, 609.7, 658.8 and 763.3 keV) relatively stronger at 32 MeV, while candidate 102.1- and 411.2-keV lines change in the opposite direction; the cited lines are reported in coincidence with iodine K x rays. | experimental-fact | direct | PDF p.75, Fig.6.1 | true |
| D12-14 | The authors assign the 102.1- and 411.2-keV lines, and correlated 221.0-, 227.1-, 402.7- and 756.7-keV lines, to the `128I` 3n channel using the two-energy intensity pattern, iodine K-x-ray coincidences, known `127I` anchors and `γ-γ` coincidence relationships. This is a source assignment, not an event-by-event isotope tag. | author-interpretation | direct | PDF pp.75-76, Fig.6.1 | true |
| D12-15 | The thesis notes that observed peaks can be doublets or contaminated by evaporation residues `127I`, `126,128Te` and `125Sb` from 4n, 4np, 2np and α2n channels; known level schemes and coincidence analysis were used to identify the `128I` transitions. | experimental-fact | direct | PDF p.76 | true |
| D12-16 | The thesis publication list includes a 2011 paper titled “High-spin states in doubly odd 128I” with Ding and thesis coauthors; Crossref metadata verifies the DOI `10.1360/132010-774`, title, authors and pages. Because the article's acquisition has not been directly checked here, conservatively treat it as a dependent publication and do not count it as an independent dataset. | synthesis | direct | PDF p.99; Crossref DOI 10.1360/132010-774 | true |
| D12-17 | The authors state that the `58.5-keV` transition's `R_ADO=1.66(60)` cannot distinguish a quadrupole `ΔI=2` from a dipole `ΔI=0` transition; its placement is constrained using other transitions and level-scheme evidence. | experimental-criterion | direct | PDF p.79 | true |
| D12-18 | In the ADO method, peak areas for the same gated transition are corrected by the efficiencies of the small- and large-angle detector groups; the gate efficiency cancels in the ratio. The paper's pure-quadrupole and pure-dipole reference values (`1.29` and `0.64`) are specific to this array. | experimental-criterion | direct | PDF pp.54-55, 57 | true |
| D12-19 | The thesis publication list also includes Wang et al. 2010, “A New High-Spin Level Scheme of 128I”; Crossref verifies `Chinese Physics Letters` 27(8), 082701 and DOI `10.1088/0256-307X/27/8/082701`. The publisher access probe on 2026-10-12 returned a restricted status, so this related publication was not read or used to claim level revisions; it is conservatively not counted as an independent acquisition. | synthesis | direct | PDF p.99; Crossref DOI 10.1088/0256-307X/27/8/082701 | true |
| D12-20 | The thesis reports the `127I` experiment as `67×10^6` `γ-γ-t` events with a 100-ns coincidence-time window and `3×10^6` X-γ events; its `128I` chapter states that `127I` and `128I` are different evaporation channels from the same fusion-evaporation experiment and use the same offline analysis method. | experimental-fact | direct | PDF p.57 (printed p.49); PDF pp.75-76 (printed pp.67-68) | true |
| D12-21 | A reproducible text extraction of Table 6.1 yields 61 rows containing a transition-energy and level arrow on PDF pp.78-79. The earlier 20-level/31-transition summary was not located as an explicit total in those chapter pages; whether it denotes a subset or reflects an earlier source-page error remains unresolved. | synthesis | direct | PDF pp.78-79, Table 6.1 | true |
| D12-22 | Table6.1把58.5/255.6/314.3分别列为225.9→167.4、481.8→225.9、481.8→167.4；Iγ为5/4/6、RADO为1.66(60)/.92(20)/.91(15)，Jπ箭头为(6−)→(6−)/(7−)→(6−)/(7−)→(6−)。这些表行与括号标签不能当本任务重拟的新观测。 | literal-transition-and-assignment-crosswalk | direct | PDF78 Table6.1 rows58.5/255.6/314.3; PDF77 Fig6.2 | true |
| D12-23 | PDF79先引用旧167.4(6−)175±15ns、225.6/269.6的(5,6,7)−/M1资料，再明确结合反应布居中spin随激发能增大倾向、ADO与其它线作建议赋值；58.5的ΔI2四极/ΔI0偶极歧义及314/255偶极被一同讨论。旧Sakh/Nati原件本任务未读，不能只将6赋值归因于两个ADO或计独立复核。 | source-reasoning-and-prior-dependency | direct-and-derived | PDF79 printed71 paragraphs below Table6.1 | true |
| D12-24 | 原Table能量误差只给.1–.5keV、强度误差5–30%且866=100；Fig6.2标226.0/481.7，Table为225.9/481.8，正文回述旧225.6。本任务保留这些literal差异；三边Eγ−ΔE为0/−.3/−.1keV，255.6+58.5−314.3=−.2keV，不补每行std/Cov或χ²。 | source-label-and-our-arithmetic-boundary | direct-and-derived | PDF77 Fig6.2; PDF78–79 Table6.1 and footnotes; PDF79 body | true |
| D12-25 | 条件固定source采用的parent7/anchor6并把314/255均当L1时，exacttriangle允许中间J6和J8；加源reactionspintrend或所引用历史(5,6,7)先验才只留6。J8只是本任务的selection-rule反例，不是其被实验支持或重指认；源actualangularresponse/likelihood仍缺。 | our-conditional-constraint-audit | derived | PDF78 Table6.1 three local rows; PDF79 assignment discussion | true |
| D12-26 | Fig6.3为117.8/641.2/239.0 gates且星号为污染，图文例不提供本任务可重放的58.5逐component净峰/Σ。Fig6.5用小平面detector分101.3/102.2并比较756.5/764.7/117.8门，但原横轴印475–550、能量keV与这些低线标签不一致；保留原图、不据该轴直接digitize低线能量或补校准。 | gate-component-and-figure-axis-boundary | direct-and-derived | PDF80 Fig6.3 and text; PDF82 Fig6.5 | true |
| D12-27 | 原175±15ns属于daughter167.4的isomer，当前局部没有225.9/481.8的parentτ；relativeIγ亦非含转换的branch概率。58的absoluteB/δ需parentτ/分支/ICC/响应等实际输入，不能借isomerτ或从ADO表补出。 | parent-identity-and-strength-readiness | direct-and-derived | PDF79 first paragraph; PDF78–79 Table6.1 and footnote b | true |
| D12-28 | Table6.1的101.3是1562.2→1460.9、I146/RADO.70(8)；两个102.2分别为285.2→183.0、I563/R.90(7)，及269.6→167.4、I≥79/R.95(16)。相同gammaenergy不能合row或共享parent、RADO、ICC。 | typed-transition-identity | direct-and-derived | PDF78 Table6.1 rows101.3/two102.2 | true |
| D12-29 | 假定117.8 pureE2，866门下得到退183的102.2之alphaT_exp=.60(7)；866和402.7门得到101.3之.88(21)。理论M1参考为.703(14)/.721(15)，均需带transition/gate/假设；另一102.2的实验ICC未在这些段给出，不能抄同值。 | source-conditional-conversion-input | direct-and-derived | PDF79 finalparagraph; PDF80 openingparagraph | true |
| D12-30 | 作者以Fig6.5/其它符合与energy sums支持101.3→764.7→411.0→102.2的顺序并只用一次411，称旧弱102约总强度10%。本任务选定端点图给chain1379.2keV；若仅固定common-scale photon Istrong563与Iweak≥79，twocomponentfraction≥79/642只是条件算术非真实fraction或CI。 | source-chain-and-conditional-intensity-audit | direct-and-derived | PDF80–81 chain discussion; PDF78 Table6.1 two102.2 rows | true |
| D12-31 | 2010CPL正文现已直接读到，Fig4横轴为Channel且正文弱102说roughly14%，与thesisFig6.5轴标/10%分别保留。2010报告48/72与thesis61表行不是可直接相减的同口径计数；指纹匹配保守按共享/重叠采集，无新独立复测。 | newly-read-dependent-publication-crosswalk | direct-and-derived | PDF81–82; Wang2010 printed082701-1/3 Fig4 | true |
| D12-32 | Fig6.5中756.5/764.7/117.8门的低峰差异有助拆101/102；由source采用端点看，756.5下方285.2的102.2和117.8是竞争分支，另一102.2来自269.6。选定图中某路径不存在不等于完整实验absence或上限，原raw/校准/response/Cov仍缺。 | source-selected-graph-and-negative-evidence-boundary | direct-and-derived | PDF77 Fig6.2; PDF82 Fig6.5; PDF78–79 Table6.1 | true |
| D12-33 | 本文/CPL强102.2为285.2→183.0、ECC=.60(7)随该component；2015选定ENSDF却把102.2/ECC放269.57→167.367并在285.19列15.6。Text/PDF均核，属于sourceobject拓扑/字段冲突，非rounding；未读2012Di14/body/erratum前不裁决哪图正确、不将评价当独立新测量。 | primary-versus-evaluation-conflict-boundary | direct-and-derived | PDF77 Fig6.2; PDF79–80 conversiontext; NNDC128053024 L269.57/G102.2 and renderedPDF2 | true |
| D12-34 | D12-25的6/8→6只限其明示H0/H2集合。本任务扩到M1component-present族后，fixedupper7/anchor6与两genericL1可留6/7，nondecreasingtrend不再唯一；需要独立stretched255或实际角response/spin材料。该scope修订不改本文建议6、也未证明J7匹配RADO。 | conditional-inference-scope-audit | derived | PDF78 Table6.1 three localrows; PDF79 discussion; CPLgeneralwarning; selectedENSDFreactionADOcomments | true |
| D12-35 | 同parent314/255的RADO.91(15)/.92(20)仍可含spinsequence信息；本任务pureL1/commonparentdensity/point37-90/fADO1 baseline给Hx7的a2比例−13/8与异号必要约束，但positivequotedboxwitness存在，实际gate/δ/Σ未核。不因前述kinematic7候选忽略RADO，亦不据打印中心作实验排除。 | our-conditional-angular-consistency-audit | derived | PDF78 Table6.1 rows255.6/314.3; PDF54–55 ADO; PDF57 geometry | true |

### 2026-10-12 reaction-channel evidence addendum

D12-12–D12-21 add the calculated-versus-measured channel-selection distinction, the two-energy isotope-assignment chain, reported contaminant residues, acquisition/time-window facts, related-publication boundaries, a transition-table count audit, and explicit ADO limits. All claims remain `needs_review: true`; page `review_status` remains `unreviewed`.

Related acquisition lineage comparison: [[wang-haixia-2012-173w-128i-high-spin-thesis]] WHX12-5/7/8; this is a same-experiment-source comparison, not an independent `128I` measurement.

## Nuclear Structure Information

- **$^{127}\text{I}$ ($Z=53, N=74$)**：
  - 基态：$5/2^+ [402]5/2$。
  - 带 A（负宇称退耦结构）：带头 $11/2^-$ ($1235.2\text{ keV}$)；表 5.1 中可直接核对的序列跃迁包括 $658.5\text{ keV}$（$15/2^-\rightarrow11/2^-$，$R_{\text{ADO}}=1.22(10)$）、$651.5\text{ keV}$（$19/2^-\rightarrow15/2^-$，$R_{\text{ADO}}=1.17(10)$）和 $431.0\text{ keV}$（$23/2^-\rightarrow19/2^-$，$R_{\text{ADO}}=1.32(13)$）；整体延伸至约 $(35/2^-)$、5242.7 keV，但 $I>27/2$ 区域不规则。
  - 带 B（正宇称高 $K$ 结构）：带头约 $7/2^+$ ($57.4\text{ keV}$)，由两个 $\Delta I=2$ 旋称分支及其强 $\Delta I=1$ 带间跃迁构成，主要组态为 $\pi g_{7/2}[404]7/2^+$。
  - 带 C（正宇称高 $K$ 结构）：由两个 $\Delta I=2$ 序列及其 $\Delta I=1$ 带间跃迁组成，作者指认为 $\pi d_{5/2}[402]5/2^+$。
  - 带 D（类转动集体激发带）：建立在 $23/2^+$ ($2901.2\text{ keV}$) 态上，作者指认为 $\pi g_{7/2} \otimes (\nu h_{11/2})^2$。
  - 结构 E / F（非集体激发）：建立在 $19/2^+$ ($2650.5\text{ keV}$) 和 $15/2^+$ ($2068.4\text{ keV}$) 上，分别对应 $\pi g_{7/2} \otimes (\nu h_{11/2})^2$（具不同三轴形变）和 $(\pi g_{7/2}/d_{5/2})^3$ 三准质子激发及其破对中子耦合态。
- **$^{128}\text{I}$ ($Z=53, N=75$)**：
  - 低位多重态：约 $167.4\,(6^-)$、$183.0\,(7^-)$、$225.9/226.0\,(6^-)$、$269.6\,(7^-)$ 和 $285.2\,(8^-)$ keV；其中 167.4 keV 为 $T_{1/2}=(175\pm15)$ ns 的同质异能态。
  - 带 B（负宇称类转动结构）：建立在 $8^-_1$ ($285.2\text{ keV}$) 态上，主要路径经过 $9^-\,(696.2)$、$10^-\,(1041.7)$、$11^-\,(1454.0)$ 和 $12^-\,(1873.5)$，组态为 $\pi g_{7/2} \otimes \nu h_{11/2}$。
  - 正宇称两准粒子多重态：$9^+ (1460.9), 10^+ (1562.2), 11^+ (1964.9\text{ keV})$，组态为 $\pi h_{11/2} \otimes \nu h_{11/2}$。

## Authors' Interpretation

- 作者指出，传统上将过渡区碘同位素中的能级序列简单划分为长椭球退耦带的图像存在局限：$^{127}\text{I}$ 的正宇称带实际上具有微小的扁椭形变，强带间跃迁和负的 $E2/M1$ 混合比与高 $K$ 轨道解释相容。形变角度的具体数值应按 PES 表格的坐标约定读取，不能脱离约定直接转换为带符号的 $\gamma$。
- 作者强调，$^{127}\text{I}$ 和 $^{128}\text{I}$ 的势能面极为平坦柔软（$\gamma$-soft / $\beta$-soft），这导致集体转动运动与单粒子排列（特别是 $h_{11/2}$ 中子对破对）在相近能量区间发生强烈竞争，在 $^{127}\text{I}$ 中表现为集体带与非集体能级结构的共存，在 $^{128}\text{I}$ 中表现为集体转动特性的退化与单粒子激发的主导。

## Model Results

- **PES (Potential Energy Surface)**：
  - Table 5.2 对 $5/2^+$、$7/2^+$、$15/2^+$ 和 $23/2^+$ 给出多组候选组态的 $E_{\mathrm{cal}}$、$\beta_2$、$|\gamma|$ 和 $\beta_4$；例如 $15/2^+$ 的候选计算能量包括 1979 和 1965 keV，$23/2^+$ 的候选计算能量包括 2846、2726 和 2690 keV，而实验能量分别为 2068 和 2901 keV。
  - PES 图显示相关组态的 $\beta$、$\gamma$ 势能面较软；表格使用 $|\gamma|$ 坐标，不能在没有坐标约定的情况下把它改写成带符号的 $\gamma$。
- **经验壳模型 (Empirical Shell Model)**：
  - 计算 $^{128}\text{I}$ 的 $8^-_1 (\pi g_{7/2} \otimes \nu h_{11/2})$ 激发能为 $272.9\text{ keV}$，与实验值 $285.2\text{ keV}$ 偏差仅 $12.3\text{ keV}$。
  - 计算 $^{128}\text{I}$ 的 $9^+, 10^+, 11^+ (\pi h_{11/2} \otimes \nu h_{11/2})$ 激发能分别为 $1483.0, 1606.3, 2011.6\text{ keV}$，与实验值偏差仅 $22, 44, 47\text{ keV}$。
- **核子配对近似 (NPA)**：
  - NPA 重现了 $^{128}\text{I}$ 低位负宇称态的主要间隔趋势以及正宇称多重态的主要劈裂；但部分 $6^-/7^-$ 理论顺序与实验相反，且实验 $8^-$ 位于两组理论 $8^-$ 态之间，组态指认还依赖经验壳模型和系统学。

## Competing Interpretations and Limitations

- **正宇称 $\Delta I=2$ 序列的物理本质**：早期文献曾将 $^{127}\text{I}$ 中的两条正宇称序列指认为独立退耦带；本工作通过强带间跃迁，将其中两条序列归结为同一高 $K$ 转动结构的旋称分支，另一个 $\pi d_{5/2}$ 结构仍需单独描述。
- **局限性**：实验未进行寿命（DSAM/RDDS）测量和线偏振测量，关于形变参数（$\beta_2, \gamma$）的结论主要依赖理论 PES 和 NPA 计算，缺少直接的跃迁电四极矩 $Q_t$ 或 $B(E2)$ 实验测量值。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-1 | Core reconstruction | 本篇学位论文是 $A \approx 130$ 碘同位素高自旋核结构的重要实验与理论来源。实验通过高灵敏度 $\gamma$-$\gamma$ 符合修正了历史纲图错误，提出 $^{127}\text{I}$ 正宇称结构的旋称分支性质、三准粒子结构共存和 $^{128}\text{I}$ 的单粒子增强特征。 | PDF pp.58-72、76-91（印刷页 50-64、68-83）、Fig.5.2、Fig.6.2 | unreviewed |
| AR-2 | Assumptions and dependencies | 多极性主要由阵列特定的 ADO 系数、强度/能量平衡和部分内转换系数约束；组态、宇称和集体性判断还依赖系统学及 PES/NPA/经验壳模型，不能把 ADO 阈值跨实验复用。 | PDF pp.53-55、57、78-80（印刷页 45-47、49、70-72） | unreviewed |
| AR-3 | Transfer conditions | 能级系统学、ADO 与符合关系联合约束的分析逻辑可迁移；具体 ADO 数值、几何标定、组态判断和 2qp 经验公式参数必须在每个邻近核中重新核验。 | PDF pp.27、53-55、73-87（印刷页 19、45-47、65-79） | unreviewed |
| AR-4 | Failure conditions | 若未来高精度偏振测量发现带间跃迁不含显著 $M1$ 成分，或寿命测量给出反常 $B(M1)/B(E2)$ 比值，高 $K$ 小扁椭形变解释需重新检验。 | 论文第 5.3 节讨论 | unreviewed |
| AR-5 | Reverse/falsification test | 与偶偶核芯 $^{126}\text{Te}$ 比较检验退耦带；利用经验壳模型剩余相互作用公式反算激发能检验多重态指认。 | 论文第 5.3.2 节、第 6.3.1 节 | unreviewed |
| AR-6 | Research-question decision | 为 $N=75$ 奇奇核同中子素链（$^{128}\text{I} \rightarrow {}^{130}\text{Cs} \rightarrow {}^{132}\text{La} \rightarrow {}^{134}\text{Pr}$）的手征与旋称演化提供了轻端基准。 | 论文第 1.2 节、第 7 章 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: 知识库此前重点覆盖了 $N=75$ 奇奇核同中子素中质子数较高核素（$^{130}\text{Cs}, {}^{132}\text{La}, {}^{134}\text{Pr}, {}^{136}\text{Pm}$）的手征双重带与旋称反转，缺少 $Z=53$ 碘同位素的直接实验基准。
- Effect of this source: supports / extends
- Reason: 补充了 $Z=53, N=74, 75$ 的高自旋能级纲图、ADO 数据、$\pi h_{11/2}$ 退耦带基线以及两准粒子/三准粒子共存证据，完善了 $A \approx 130$ 边缘的结构演化图谱。
- Persistence decision: source note created, nucleus pages (`127i`, `128i`), band pages, and experiment page created; index updated.
- Review state: `unreviewed` (source-level correction and Agent self-audit complete; claim-level `needs_review` retained).

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| `foundational-background` | [[134pr]] | 提供 $N=75$ 奇奇核同中子素在低 $Z$ 侧（$^{128}\text{I}$）的 $\pi h_{11/2} \otimes \nu h_{11/2}$ 与 $\pi g_{7/2} \otimes \nu h_{11/2}$ 能级结构对比基准；不构成对 $^{134}\text{Pr}$ 手征解释的直接证据。 |
| `supports` | [[gamma-soft-deformation]] | PES 势能面计算支持 $A \approx 130$ 碘同位素具有平坦极软的势能面，解释了集体与单粒子激发的竞争共存。 |
| `methodological-bridge` | [[high-spin-phenomena]] | 提供熔合蒸发反应、ADO 比值分析、NPA 与经验壳模型计算在过渡区核中的具体应用实例。 |

## Human Review Triage

### P0
P0: none remaining after source-level correction; all source claims still retain `needs_review: true` pending claim-specific use or user confirmation.

### P1
- 核对 $^{127}\text{I}$ 正宇称带 B/C 的完整两分支结构、ADO 数值和负 $E2/M1$ 混合比解释（Fig.5.2、Table 5.1）。
- 核对 $^{128}\text{I}$ 低位负宇称多重态的 NPA 顺序差异、$8^-$ 组态边界，以及正宇称 $9^+,10^+,11^+$ 的经验壳模型偏差与 NPA 劈裂（Fig.6.6、Fig.6.8）。

### P2/P3
- P2: 关注 $^{127}\text{I}$ $15/2^+$ 和 $23/2^+$ 三准粒子态与偶偶核芯 $^{126}\text{Te}$ 破对中子态的激发能匹配关系，以及 Table 5.2 的 $|\gamma|$ 坐标约定。
- P3: 跟踪该学位论文后续发表的期刊论文（如 2011 中国科学、2012 PRC）中是否有微小能级修正。

## Extracted Pages

- Nuclei: [[127i]], [[128i]]
- Bands: [[127i-pi-h11-2-decoupled-band]], [[127i-pi-g7-2-rotational-band]], [[127i-pi-d5-2-band]], [[128i-pi-g7-2-nu-h11-2-structure]], [[128i-pi-h11-2-nu-h11-2-structure]]
- Experiments: [[tsukuba-127-128i-li7-28-32mev]]
- Concepts: [[gamma-soft-deformation]], [[high-spin-phenomena]]
- Methods: [[angular-distribution]], [[gamma-gamma-coincidence]]

## Non-source Notes and Follow-up

- 本学位论文提供了较详尽的实验背景介绍（包含熔合蒸发反应截面、符合线路、DCO/ADO 理论基础）与数据图表；用于方法学或论文写作时，应优先引用实际 ADO 表格和原始能级纲图。

## DAY14三节点局部证据：58.5-keV与spin先验

2026-10-16原DAY14证据迁移练习：来源前primed回忆先保存，再读旧card/核raw SHA256；本轮读PDF74–82对应章引言、placement/assignment与Figures6.2–6.5/Table6.1相关段，并对主要图表视觉核验。不声称100页重新全读，也不以新练习加正式成绩。原raw4045752bytes/SHA`ca7765ad962ea0c106791532f5a7d9f359533d25bb0170f03197bfec414be5c7`不改。

本次增量不同于旧D12-17的“RADO有歧义”：把58.5的具体parent/daughter、共同481.8上层的314.3/255.6三条边与Fig6.2、Table6.1和PDF79论证绑定。原文同时引旧低位资料和reaction-spin增长倾向。若只给exactradiativetriangle条件，7→8的L1即使能量下降也允许，故两伴随偶极本身不唯一选中J6。加入已标明的历史prior或source reactiontrend则保留6，这解释了source采用多项材料的依赖；不提出J8新experimentalassignment。

[[level-scheme-reconstruction]]“128I：58.5-keV局部三边与spin先验”保存16项条件核验、逐边证据/parentstrength边界和falsifier。表/图节点与能量有细微literal差异，未静默修原件；PDF82 Fig6.5的energy-axis标记亦保持，不能拿图上475–550当101/102物理能量作数字拟合。OldSakh/Nati原件、逐门counts/response/Cov未恢复，同一thesis/acquisition与表中spin不计为独立数据。

Agent self-audit：D12-22–27 true，旧1–21/原review保持。初次本任务断言误将314.3−(481.8−167.4)记0，自测捕获后仅修断言为−.1；source/input原值不改。Decision: **supports** 合并能量/placement/角数据/旧anchor的分层链；**limits** selectiontriangle或一个ADO值直接推出唯一Jπ、相对强度/isomerτ推出parentabsoluteB。科学边界可发布，不代表独立重测或正式论文裁决。

## DAY14低能triplet与2010正文的新核验

本轮先冻结primed issue，再回核PDF78–82的三低线/转换/门与版本；现从[出版商公开PDF](https://cpl.iphy.ac.cn/en/article/pdf/preview/10.1088/0256-307X/27/8/082701.pdf)实际取得并完整读取4页[[wang-2010-128i-new-high-spin-level-scheme]]，所以D12-19所记2026-10-12访问受限/未读只代表当时状态。新W10I-1–8保留身份、四页scope和preciselocators；2011入口本次仍只有空SPA，不宣称读其正文。

101.3、102.2a（285.2→183.0）与102.2b（269.6→167.4）的typedrow不同。前者转换.88(21)与a的.60(7)各带原gate/purity合同，b保持未知，不因同energy补同实验值。[[level-scheme-reconstruction]]“128I低能triplet：transition ID、门与转换字段”保存选定图/chain/分支与19项核验，所有路径结论条件于已报告端点，不冒充原事件重新建图。

2010 Fig4原横轴Channel，thesisFig6.5印能量keV却在475–550附近画101/102标签；保留两版，不猜精确rebin/calibration或修原图。本文约10%与2010 roughly14%分别记录；在固定RI中心/下界合同下的79/642≠实测componentfraction，原5–30%范围没有给fullCov/相同归一/门以检验版本一致性。CPL48/72、thesis61表行也不用于计新增。共同装置/束流/事件指纹匹配，保守不计独立重复，未恢复原runIDs/时间窗定义。

Agent self-audit：新D12-28–32 true，旧1–27逐行/flags与review保持；原raw/PLAN/Bib未改。Decision: **supports** 逐rowID/端点/gate/转换的身份合同；**revises** 当前2010primary可读状态；**limits** 同峰合并、混用fraction/branch分母和图坐标、由selectedgraph不连通宣称实验absence。Formal14分数与课程信用不变。


## 选定ENSDF与本thesis的102-keV位置冲突

[[nndc-2015-128i-selected-level-gamma-records]] N128-3–9补直接对象/独立PDF表示，保留更宽的(5,6,7)−标签、15.6/102位置及ECC绑定差别。D12-28/29仍是本thesis实际表/论证，不能将数据库的269.57 parent/ECC反向抄来变成另一102的独立实测ICC；两source版本必须分开。评价者还按RI区间赋error，不能用那些值补本thesis原fitCov。

28项选定记录检查与能量和歧义在[[level-scheme-reconstruction]]新评价节保存。2012Di14精确为PRC86,034302/DOI10.1103/PhysRevC.86.034302，正文未读；source争点不以paper年/compiled标签判决。本段D12-33 true，旧1–32/原review/raw保持，没有新spin、真实σ/δ/absoluteB或模式结论。


## 局部H0/H2与更宽M1族的范围

D12-25原文已经限定fixedparent/anchor与H0/H2；新D12-34把这个限制进一步显式化。[[nndc-2015-128i-selected-level-gamma-records]] N128-13–15与[[wang-2010-128i-new-high-spin-level-scheme]] W10I-4的generalADOambiguity提示，不能把genericdipole自动当stretched，亦不能把条件集合的唯一元素当完整physicaluniqueness。新J7只是kinematiccounterexample，actual58/255的δ、共享parentpopulation、门选择/角响应与Cov仍需数据判断，未作source重指认。

13项集合/证据角色核验和逐前提表在[[level-scheme-reconstruction]]保存。旧1–33逐行/flags/review保持，新34true；本段不提供新的RADO拟合、论文裁决或正式成绩。


## Commonparent的角数据不能被necessarysets替代

[[nndc-2015-128i-selected-level-gamma-records]] N128-16–18用本source实际两个RADO作条件中心/box控制，23项数学检查没有原netcounts/response/δ/Cov。结果补充D12-34的scope：sharedparent在matched条件下可以给比triangle更强的角约束；actual每线gate未给，不能把samelevelID自动视为samepostselecteddensity。完整推导/失效控制在[[level-scheme-reconstruction]]，原sourceJ6与旧1–34行/review/raw保持，新35true。
