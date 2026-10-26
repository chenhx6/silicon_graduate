---
type: source
title: "Longitudinal wobbling motion in 187Au"
aliases: [Sensharma 2020 187Au, longitudinal wobbling in 187Au]
created: 2026-07-03
updated: 2026-10-25
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Longitudinal Wobbling Motion in 187Au"
authors: [N. Sensharma, U. Garg, Q. B. Chen, S. Frauendorf, D. P. Burdette, et al.]
journal: Physical Review Letters
year: 2020
volume: 124
pages: 052501
doi: 10.1103/PhysRevLett.124.052501
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevLett.124.052501
zotero_item_key:
citation_key: sensharma_2020_LongitudinalWobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2020_Sensharma et al_Longitudinal Wobbling Motion in Au 187.pdf"
raw_sha256: F348DCE9976AD076FD9B1D5281A728E0923053ACED33B0270F643D770729366A
nuclei: [187au]
reactions: [174yb-f19-6n-187au]
experiments: [atlas-gammasphere-187au-f19-105-115mev]
models: [particle-rotor-model, covariant-density-functional-theory]
observables: [multipole-mixing-ratio, interband-e2-strengths, wobbling-energy]
methods: [gamma-gamma-coincidence]
tags: [a190, 187au, longitudinal-wobbling, signature-partner, gammasphere, prm]
---

# Sensharma 等（2020）：`187Au` longitudinal-wobbling 支持方实验

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

N. Sensharma et al., *Physical Review Letters* **124**, 052501 (2020)，DOI `10.1103/PhysRevLett.124.052501`。题名、作者、年份和 DOI 与只读 BibTeX 条目唯一匹配，使用 citation key `sensharma_2020_LongitudinalWobbling`。

## Scope and Reading Depth

全文精读，并视觉核对 Fig.2 的部分能级纲图、Fig.3 的 angular-distribution fits 与 mixing ratios、Fig.4 的 band energies/`E_wobb`，以及 Fig.5 的实验-PRM transition-ratio 比较。

本页建立 Sensharma 2020 对 `187Au` longitudinal-wobbling 的支持方证据链，不裁决后续低自旋 wobbling 争议。

## Summary

作者利用两次 ATLAS/Gammasphere 实验的合并数据研究 `187Au` 低自旋负宇称带。band (2) 到 yrast 的四条最低 connecting transitions 被 angular-distribution analysis 赋予约 88%-93% E2 admixture；新建 band (3) 到 yrast 的两条 links 几乎为纯 M1。作者将 band (2) 指认为 `n_w=1` longitudinal-wobbling band，将 band (3) 指认为 signature partner，并用随自旋增加的 `E_wobb` 与 PRM 比较支持该解释。

## Experimental or Theoretical Setup

- 富集 `174Yb` 靶为 `13 mg/cm²`，带 `33 mg/cm²` `208Pb` backing；
- 两次 `19F` 束流能量分别为 105 和 115 MeV；
- Gammasphere 分别使用 57 与 73 个 Compton-suppressed Ge detectors；
- 合并获得 `1.08×10^9` 个三重及更高重数 γ 符合事件；
- 以 RADWARE 建立 γ-γ matrices 与 γ-γ-γ cubes，并利用 17 个角度环进行 angular-distribution analysis；
- PRM 描述 `h9/2` proton 与 triaxial rotor 的耦合。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AU20-1 | 两次实验以 105/115 MeV `19F` 轰击带 `208Pb` backing 的富集 `174Yb` 靶；Gammasphere 分别有 57/73 个工作的 Ge detectors，合并得到 `1.08×10^9` 个 fold≥3 γ 符合事件。 | experimental-fact | direct | p.3, left column, experimental setup | false |
| AU20-2 | Fig.2 给出 yrast band (1)、此前被称为 unfavored signature partner 的 band (2)，以及本工作新建、以 `E_x=386.3 keV` 的 `11/2-` state 为带头的 band (3)。 | experimental-fact | direct | p.3, Fig.2 and surrounding text | false |
| AU20-3 | band (2) 通过六条 ΔI=1 transitions 衰变到 yrast；Fig.3(a-d) 分析其中最低的 376.3、461.8、544.3、639.3 keV 四条 links。 | experimental-fact | direct | pp.3-4, Figs.2-3 | false |
| AU20-4 | 四条最低 band (2)→yrast links 的 `δ` 为 `-2.67(7)`、`-2.98(+0.02/-0.03)`、`-3.44(3)`、`-3.72(+0.11/-0.12)`，E2 fractions 分别为 `87.7(+0.5/-0.6)%`、`89.9(1)%`、`92.2(1)%`、`93.3(4)%`。 | experimental-fact | direct | p.4, Fig.3(a-d) | false |
| AU20-5 | band (3) 通过 265.3、436.5 keV ΔI=1 transitions 衰变到 yrast；angular distributions 给出 `δ=-0.06(1)`、`-0.10(1)` 和约 0.4%、1.0% E2 admixture。 | experimental-fact | direct | pp.3-4, Figs.2-3(e,f) | false |
| AU20-6 | 新观察到 429.2 keV ΔI=2 crossover，连接 band (2) 的 `15/2-` level 与 band (3) 的 `11/2-` level；作者结合 in-band stretched-E2 与两条 SP→yrast pure-ΔI=1 links 进行 spin/parity assignment。 | experimental-fact | direct | pp.3-4, Fig.2 and paragraph below Fig.3 | false |
| AU20-7 | 333.8、413.7 keV 两条已知 yrast stretched-E2 transitions 的 angular-distribution fits 给出 `δ=-0.04(1)`、`-0.03(1)`，被用于检查分析方法。 | experimental-fact | direct | p.3 and p.4, Fig.3(g,h) | false |
| AU20-8 | 本文采用的区分判据是：wobbling→yrast ΔI=1 links 应有 collectively enhanced E2 component，而 signature-partner→yrast links 应主要为 M1；LW 的 `E_wobb` 预期随自旋增加。 | experimental-criterion | direct | pp.2-4, Eqs.1-3 and discussion; Figs.1,3-4 | false |
| AU20-9 | 由 Fig.4(d) 中实验 `E_wobb` 随自旋增加，作者把 band (1)/(2) 指认为 `n_w=0/1` longitudinal-wobbling pair。 | author-interpretation | direct | p.4, Fig.4(d) and surrounding text | false |
| AU20-10 | 作者把 band (3) 指认为 yrast 的 unfavored signature partner，依据是 265.3、436.5 keV links 几乎为纯 M1，并结合 band 内 stretched-E2 与 429.2 keV crossover。 | author-interpretation | direct | pp.3-4, Figs.2-3 and surrounding text | false |
| AU20-11 | PRM 使用 `β=0.23, γ=23°`、`Δ=0.88 MeV`、`λ=-1.32 MeV`、`J_0=38.0 ħ²/MeV`，以 single-j `h9/2` proton 为主；加入 `f7/2` 后其波函数 admixture 小于 5%。 | model-result | direct | p.4, right and left columns, PRM setup | false |
| AU20-12 | configuration-fixed CDFT 给出从 `I=9/2` 的 `(β,γ)=(0.28,22°)` 到 `I=29/2` 的 `(0.28,25°)`，作者据此认为 PRM 使用常形变近似合理。 | model-result | direct | p.4, right column, model setup | false |
| AU20-13 | PRM 较好再现三条带的总体能量趋势和增加的 `E_wobb`，但对 `E_wobb` 数值略有低估。 | model-result | direct | pp.4-5, Fig.4 | false |
| AU20-14 | 实验 LW→yrast 的 `B(E2)_out/B(E2)_in` 最大约 0.7，明显大于 SP→yrast；PRM 较好再现 E2 ratios，但高估 LW 的、低估 SP 的 `B(M1)_out/B(E2)_in`。 | model-result | direct | p.5, Fig.5 and surrounding text | false |
| AU20-15 | 论文以 half-filled `h9/2` shell 中准质子趋向沿 medium axis 的分类图景解释 longitudinal geometry；正文未给出逐自旋 angular-momentum-component 图。 | author-interpretation | direct | pp.1-2, Fig.1(c); p.4 PRM setup | false |

## Nuclear Structure Information

- [[187au-yrast-band]]：band (1)，作者作为 `n_w=0` 基带；
- [[187au-longitudinal-wobbling-band]]：band (2)，作者重新指认为 `n_w=1` LW；
- [[187au-signature-partner-band]]：新建 band (3)，作者指认为 unfavored signature partner。

## Authors' Interpretation

- band (1)/(2) 为 `n_w=0/1` longitudinal-wobbling pair；
- band (3) 为 associated signature partner；
- 增加的 `E_wobb`、E2-rich LW links 与 M1-dominated SP links 联合区分两类 excitation；
- `187Au` 被作者称为首个同时识别 associated signature partner 的 longitudinal-wobbling 案例。

以上为作者解释，不是本 Wiki 对低自旋 wobbling 争议的最终裁决。

## Model Results

- PRM 计算能量、`E_wobb`、`B(E2)_out/B(E2)_in` 与 `B(M1)_out/B(E2)_in`；
- CDFT/HFB-D1S 为形变输入提供比较；
- PRM 对 E2 ratios 较好，但对 M1 ratios 存在相反方向偏差；
- angular-momentum geometry 主要以 Fig.1 与 half-filled-shell 分类说明，未展示逐自旋分量。

## Competing Interpretations and Limitations

- 本文是 longitudinal-wobbling 支持方原始实验；后续独立反方[[guo-2022-low-spin-wobbling-187au]]已摄入，见project中的两方对照；
- 完整 coincidence、spin/parity 与系统误差细节被留给 forthcoming publication；
- angular distributions 的效率修正、spin alignment、attenuation coefficients 等完整讨论未在本 PRL 展开；
- 未识别 `n_w≥2` bands；
- PRM 的形变、转动惯量、single-j truncation 与 state mixing 具有模型依赖；
- 本文未报告 connecting-transition linear polarization。

## Extracted Pages

- Nucleus: [[187au]]
- Bands: [[187au-yrast-band]], [[187au-longitudinal-wobbling-band]], [[187au-signature-partner-band]]
- Experiment: [[atlas-gammasphere-187au-f19-105-115mev]]
- Concepts: [[wobbling-motion]], [[longitudinal-wobbling]], [[signature-partner-bands]]
- Observables: [[multipole-mixing-ratio]], [[interband-e2-strengths]], [[wobbling-energy]]
- Method: [[gamma-gamma-coincidence]]
- Models: [[particle-rotor-model]], [[covariant-density-functional-theory]]
- Project: [[187au-longitudinal-wobbling-controversy]]

## Personal Notes

本页只建立 Sensharma 2020 支持方证据链。用户已审核 source 页面及 AU20-1 至 AU20-15，未发现问题；这不构成对后续 `187Au` 争议的裁决。

## Day18 checkpoint052修订：角分布选解、偏振缺口与条件塌缩

原SE20-claims/review保持；旧SE20-D18-1的强断言降为superseded，由D18-2/3分层替代。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SE20-D18-1 | **superseded**：旧关于“盲目采纳制造虚假集体假象”等断言降格，由D18-2/3分别记录作者报告的大根与后续小根对比条件。 | task-correction | superseded-interpretation | 本段D18-2/3；旧guo22-sensharma20-187au-result-022 | true |
| SE20-D18-2 | 本文基于Gammasphere角分布测量（未包含线偏振），在双解中选用大混合比解（delta ~ 2.6-3.0），由此提取出B(E2_out)/B(E2_in)高达~0.70并提出纵向wobbling解释；这是未测偏振条件下的作者派生结果，不是确定性唯一解。 | source-result-and-boundary | direct-and-boundary | PDF pp.3-5 Figs. 3, 5；Table I | true |
| SE20-D18-3 | **superseded at checkpoint094**：旧偏振/δ身份、跨数据强度或排他认证不得沿用；见AU20-D22-R094-1及GU22-D22-R094-1/2。 | task-correction | superseded-interpretation | checkpoint094原件核验 | true |

## Day 21 Checkpoint 019 证据门量化审计：纵向摇摆（LW）大模解偏置与费米面几何约束

依据推断阶梯方法论（[[experimental-claim-boundaries]]）及独立量化程序 day21_checkpoint019_longitudinal_wobbling_187au_audit.py（产物 outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/longitudinal-wobbling-187au-audit-019.json），对 Sensharma 2020 的纵向摇摆主张完成推断阶梯边界核定：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AU20-D21-1 | **superseded at checkpoint094**：旧偏振/δ身份、跨数据强度或排他认证不得沿用；见AU20-D22-R094-1及GU22-D22-R094-1/2。 | task-correction | superseded-interpretation | checkpoint094原件核验 | true |

## Day22 checkpoint094：支持证据与分母、带身份

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AU20-D22-R094-1 | 两次ATLAS/Gammasphere采集合并后作17环角分布；376.3/461.8/544.3/639.3 keV的打印δ=−2.67/−2.98/−3.44/−3.72，E2约87.7–93.3%；无connecting-line polarization。Fig.5给相对B ratios而非新寿命；p.4的1.49 e²b²为Ref39既有187Au 13/2−→9/2−强度，用于PRM形变选择，不能直接给任意out branch绝对定标。作者明确未识别n≥2带；band(3)是signature partner。PRM化学势置h9/2中部，而Guo的多轨道QTR置近底部，属模型输入/结构解释冲突。 | experiment-and-model-input-boundary | direct-original | 052501-3 setup and band paragraph; 052501-4 Fig.3 and PRM paragraph; 052501-5 Fig.5 | true |


## Day23：绝对尺度定标与模型空间的条件

本次定向回读原PDF p.4–5模型输入与结果，原page review和AU20既有flags保持；以下新增needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AU20-D23-1 | p.4先给configuration-fixed CDFT的β=.28、γ由22°到25°，实际PRM改采用HFB-D1S core值β=.23、γ23°，并明说其解释既有187Au13/2→9/2的B(E2)=1.49(eb)²及186Pt2→0的.84(eb)²；这两绝对尺度是引用并参与输入选择，不是本文新增τ测量或独立holdout。PRM single-j h9/2、额外f7/2 admixture<5%，与Guo2022九个负宇称轨道、ε2=.21/γ12°的QTR不是只换带标签的同输入比较。 | model-input-calibration-and-comparison | direct-original-and-cross-source-boundary | printed052501-4, PRM/CDFT input paragraphs | true |

Knowledge Impact and Learning Decision：limits样本内能量/尺度符合度的独立计票；保留原LW/SP支持链和作者PRM比较，并要求[[signature-tip-shears-discrimination-contract]]的configuration-only练习明确哪部分D冻结、哪部分Hamiltonian/算符仍待统一。


## Day23：核芯定标数值与 2021 学位论文对账

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AU20-D23-2 | 本文p4引用186Pt2+→0+的.84(eb)²，thesis printed128引用1.44(eb)²，两个字面数比例1.714且同引Baglin2003；两文实际写出的β输入均.23，不能据引用差断言producer参数改变。现代Pt API cutoff2022-03-01列102W.u.，在单列E2退激/采用αtot/半衰期定义等假设下rate中央重算.645283e²b²；它与表列WU同源、非独立验证，也不证明历史Baglin2003采用值。checkpoint006“严格/完全证实”及七项flag的科学认证撤回；原原子事实/人审flags保持，继续核原评价。 | quoted-reference-version-and-conditional-arithmetic | direct-quotation-and-bounded-task-calculation | printed052501-4; SE21 printed128; currentPtAPI cutoff2022; checkpoint007 correction | true |


### Day23 现代reference导出的读取范围

以下为外部官方字段读数，不归为本文原始实验；完整API快照仍tmp staging/正式raw归档deferred。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AU20-D23-3 | 公开IAEA gammas/levels(186pt)本次返回cutoff1-Mar-2022、Batchelder/Hurst/Basunia，row(start,end,gamma)=(1,0,0)列191.53keV、2+→0+、b_e2=102 W.u.、total CC=.417，初level1半衰期字段240ps；Au187旧cutoff1-Nov-2008的row(10,2,0)列233.4keV、(13/2−)→9/2(−)、188W.u.、total CC=.224、level10半衰期56ps。当前导出每个parent仅列这一条E2，不由RI=100证明全branch闭合。它们来自各自评价，同源τ/α/strength不增加独立证据数，未获得历史Baglin2003正文/完整uncertainty。 | external-evaluated-reference-field-contract | direct-public-api-with-archival-and-model-boundaries | https://www-nds.iaea.org/relnsd/v0/data?fields=gammas&nuclides=186pt row(1,0,0); levels186pt idx1; gammas187au row(10,2,0); levels187au idx10 | true |

guide定义b_e2为W.u.，half_life及half_life_sec为半衰期。本次Pt gammas/levels SHA分别d47db63ca140e07c9a1b435c34d70754b78d3104b9bc33ac31bd1108a3273a75、06cd14997ee06c7315d7f2a82f86cc366893d2e4522014438e1fa5294a8acf2f。条件换算见[[signature-tip-shears-discrimination-contract]]，不能用这些现代字段给旧源“完全证实”或原实验错误认证。

## Day23：原图误差与支持方拟合输入

本次定向实际读原p3方法段、p4 Fig3并fresh四倍局部渲染，原PDF SHA相符；未重读全文。新增Codex self-audit，旧AU20人审范围不扩。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AU20-D23-4 | Fig3(a,b)打印δ分别−2.67(+.07/−.07)、−2.98(+.02/−.02)，对应376.3/461.8keV；不是由中心或E2百分比猜误差。SP的265.3/436.5则为−.06±.01/−.10±.01，后一个436.5的δ与Guo提到旧376的P=−.10(5)是不同线、不同量。333.8/413.7的近纯E2控线δ−.04(1)/−.03(1)亦不能按目标M1/E2坐标读成近纯M1。 | line-resolved-printed-fit-values-and-convention | direct-original-visual | printed052501-4 Fig.3(a,b,e–h); printed052501-3 control-line paragraph | true |
| AU20-D23-5 | 在本任务已声明的历史标称376.3/462.1能量、名义FO K中央固定下，以上两条printedδ端点给αK像[.049200,.050472]/[.028840,.028995]，与四项历史αK各自printed值±误差范围均不相交。这个确定性比较与Guo的旧转换反证方向相同，但没有传播实际响应、共同理论/归一Cov或globalδ域，不能赋排除置信度或最终LW/SP裁决；第二个比较能量不修改本源461.8。 | conditional-endpoint-image-and-countercomparison | original-printed-endpoints-plus-actual-theory-and-task-math | Fig.3(a,b); KB08-D23-001; GU22-D23-013; task input-contract032 | true |

p3确实用17角环和两run合并高统计作AD，并说效率、alignment、attenuation等更多细节待Ref26；Ref26字面为Sensharma et al.(to be published)，不是已明确题名/DOI的公开supplement。[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-D23-6/7给同支持链可读的实际A2/A4、校准选择和分支附近采样步骤，不作为第二次实验。计算前提直接回链[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D23-001及[[guo-2022-low-spin-wobbling-187au]] GU22-D23-013；本轮没有反演或补造新δ。

## Day23：显示拟合曲线的图像形状核验

本次从原PDF p4提取Fig3嵌入raster(xref88、1334×1129)，实际image SHA256 b8d48d938b3dc7a9ef58408a63bc11aeedea08a422bb312b9aac4c6e37a6dcdd，原PDF SHA保持。只取panel(a)红色已拟合曲线，不取黑色实验点/误差棒，不视为原净计数。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AU20-D23-6 | 在明确原图像素轴标定下，对376.3红色显示fit路径以A0(1+A2P2+A4P4)提取形状，约A2=−.672、A4=.389，508个有红线列的纵向RMS残差.44px。3种红色阈值、stride1/2/4与四轴锚点各±1px的声明敏感性给A2约[−.679,−.665]、A4[.383,.395]；这是图像/标定设计范围而非CI，不是原A2/A4实测误差或新实验。 | displayed-fit-curve-geometric-reconstruction | original-raster-plus-explicit-image-analysis | printed052501-4 Fig3(a), imagexref88; task input-contract040 and displayed-curve040 | true |

显示曲线形状与本任务声明Gaussian .2大δ的A2/A4约−.668/.390接近，而不等Table4.4约−.730/.523或Fig4.12初始自由fit的−.6704/.3194；后两量来自[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-D23-8/9/10。这里只把三个实际显示/处理阶段继续分开，不能据形状接近认证原producer完整实现、原nuisance参数/globalχ²或认定其它图表有错。显示强度A0也不能重写成原净峰产额。实际谱/校正链/共同Cov仍缺，新增needs_review:true，旧人审范围不扩。

## Day23：两条定标链的外部原件核阅

此节为明确标识的外部原件，不把它们写成S20新采集。原ENSDF cL T指向1995Wa18的RDM现已沿[NSR真实key查询](https://www.nndc.bnl.gov/nsr/?search-type=keynumber&key=1995Wa18)核身份，并从[Acta公开原刊](https://www.actaphys.uj.edu.pl/fulltext?series=Reg&vol=26&page=279)取得J.C. Walpe et al., *Lifetimes in181Ir and187Au: Enhanced deformation of the πi13/2 Intruder Orbital*, Acta Phys.Pol.B26,279–282(1995)。4页/162661bytes，SHA256 c1c23b63494e18a25b31bb3611cd3434c6b7698902a280c301de7c17b724c9b5，扫描页全部视觉读；OCR只助检索，不代视觉表格。

另取得两派共同所引R. Rodríguez-Guzmán et al., *Mean field study of structural changes in Pt isotopes with the Gogny interaction*, PRC81,024310(2010)，DOI[10.1103/PhysRevC.81.024310](https://doi.org/10.1103/PhysRevC.81.024310)，公开arXiv[1001.4893v1](https://arxiv.org/abs/1001.4893v1)实际18页/1008527bytes，SHA256 7b160fd70bbb8e767b886bbb230186a4d11bda513c25901262596cbf55fc8fae。主线/公式/全部图caption/refs已读，视觉重点PDF4/8/10的Figs2/5/6；没有复现原HFB代码或逐点提取所有曲线。arXiv Jan2010与PDF内Nov2018排版日期分开。两PDF分别暂存tmp/day23-originals/au-reference053-walpe-pdf.pdf与hfb-pt053.pdf，正式raw归档deferred。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WA95-D23-001 | Walpe原实验用ATLAS/NotreDame plunger、12 Compton-suppressed HPGe和50单元BGO multiplicity filter；154Sm(37Cl,4n)187Au为160MeV，另154Sm(31P,4n)181Ir为140MeV。RDM拟合含未观测级联feeding修正。Fig1的示例拟合明确是181Ir，不是187Au原response。 | external-primary-experiment-and-response-scope | directly-read-original-scan | Walpe1995 printed280 experiment and analysis paragraphs; printed281Fig1caption | true |
| WA95-D23-002 | 原TableII的187Au13/2−→9/2−列Eγ233.4keV、meanτ81.3±8.5ps、B(E2)=1.18±.12e²b²、Qt6.08±.31eb；原17/2−→13/2−行字面334.7keV、τ13.7±1.5ps、B1.32±.14，不能默改成后文333.8的精确原值。Qt是跃迁量及其采用几何，不是独立静态Qs或另一测量。 | external-primary-literal-table | directly-read-original-scan | Walpe1995 printed282TableII first and second rows | true |
| WA95-D23-003 | 原TableII的29/2−→25/2−，566.8keV、τ2.8±.3ps带星号；注释说level与feeding寿命未能分离、所列为上限，不作为普通对称Gaussian测量。作者由两带的Qt尺度差解释πi13/2较πh9/2增强形变；这不是对后来的376/462跨带δ或LW/SP归属的直接检验。 | external-primary-limit-and-author-interpretation | directly-read-original-scan | Walpe1995 printed282TableII footnote and conclusion paragraph | true |
| WA95-D23-004 | 仅按定义81.3ln2≈56.35ps，与官方旧Adopted353.66(13/2−)的T1/2=56ps中央对应；评价同列Qt6.08，且header明确T源1995Wa18。此为同RDM谱系的核对，非独立复测或误差完全重现。S20引用B=1.49而本原表B=1.18，中央比1.263；尚未核清历史评价原刊/额外归一的映射，保留差异，不默改S20或据此作模式裁决。 | evaluated-primary-lineage-and-conditional-arithmetic | directly-read-and-derived-with-boundary | Walpe1995 printed282TableII first row; ENSDF187079001cL T andL353.66/G233.4 | true |
| RG10-D23-001 | 原HFB用GognyD1S/D1N/D1M、13 major HO shells及mass quadrupoles：Q20=〈2z²−x²−y²〉/2、Q22=√3〈x²−y²〉/2、Q=(Q20²+Q22²)½、tanγ=Q22/Q20。它们是理论密度形状坐标，不是直接电磁γ或Nilsson potential ε2的自动同义值；原quasiparticle energies与为展示而构造的Routhian SPE也分开定义。 | external-original-model-definition | directly-read-theory | RG2010 PDF5SecII Eqs1–4 and SPEparagraph | true |
| RG10-D23-002 | 原Figs2/5/6在186Pt给近prolate的三轴minimum，γ图读约10–15°，不是精确新测量或CI；D1S/N/M全链趋势相近。Fig5是固定Q在原axial minimum处的γ切片，Fig6是全PES最低点坐标，不互作同一优化路径。S20所写HFB-D1S γ23°与Guo所写同引本源γ12°的数值映射仍须核取值/版本/约定，不能将同引一理论源当两次shape测量，也不能擅自宣称S20实际producer改用12°。 | external-original-model-input-provenance | directly-read-theory-and-explicit-plot-reading | RG2010 PDF4Fig2; PDF8Fig5caption; PDF9–10Fig6 | true |
| RG10-D23-003 | 原文将184–196Pt的三轴区域描述为γ-soft，强调static meanfield不足以定量预测能谱/约化跃迁，需symmetry restoration和β/γfluctuations；原selfconsistent cranking MoI普遍高估实验，作者联系meanfield pairing不足。本原件不提供两篇Au具体PRM/QTR的完整H/operator或新绝对B(E2)，亦不由coreminimum唯一认证oddAu模式。 | external-original-author-limit-and-transfer-boundary | directly-read-theory | RG2010 PDF10Fig6discussion; PDF11–12 beyondmeanfield paragraph; PDF16Conclusions | true |

本次使“原Au寿命source尚未读”缩小为：Walpe短文原表和setup已读，LIFETIME原code/input、逐distance Au spectra、fullfeeding/ICC/branch/errorCov及历史评价到1.49的映射仍未取得。B=1.18的原实验支持既有h9/2带的集体E2尺度；它不是争议激发母态的τ，也不由这一个尺度裁决δ根。对186Pt历史.84/1.44也未以现代API.64替代。新增needs_review:true，旧sourceflags不变。

## Day23：外部5DCH原件与core形状的三个统计对象

沿RG2010原Ref87继续读J.-P.Delaroche et al.，*Structure of even-even nuclei using a mapped collective Hamiltonian and the D1S Gogny interaction*，PRC81,014303(2010)，DOI[10.1103/PhysRevC.81.014303](https://doi.org/10.1103/PhysRevC.81.014303)，[arXiv0910.2940v2](https://arxiv.org/abs/0910.2940v2)。实际PDF为53页（metadata comment写51页），2239596bytes，SHA256 0f83fdd2af1934daad5f9524e87e53e5636d6f14753006724b5c893bb7c7d82d，tmp/day23-originals/delaroche-5dch055.pdf；全主线/公式/图caption/内表/refs文字已读，fresh视觉核PDF6/8/9/11/15/18/48。未复现原HFB/5DCH或声称这是S20实际producer。

原Ref1的CEA入口先返回HTML meta-refresh；真正跟到[作者数据表](https://www-phynu.cea.fr/science_en_ligne/carte_potentiels_microscopiques/tables/HFB-5DCH-table.htm)以及其链接[HFB-5DCH-table-2009.txt](https://www-phynu.cea.fr/science_en_ligne/carte_potentiels_microscopiques/tables/HFB-5DCH-table-2009.txt)，均实际200取得，另核英文tooltip；不是把入口200当数据已得。HTML与text为同一表的两种表示，不是独立计算。原件/表仅tmp公开暂存，正式raw归档deferred。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DL10-D23-001 | 原CHFB+5DCH在GognyD1S的CHFB网格上构建集体Hamiltonian；转动MoI用ω=.002MeV附近的自洽响应，振动mass用cranking近似、缺动态重排，ZPE亦有明列截断。原适用域为even-even低能J≤6、near-zero-frequency参数且无2及更多qp激发；“无额外effectivecharge”不等无functional定标或可直接预测oddAu全部带。 | external-original-model-input-and-domain | directly-read-theory | DL2010 PDF5–6 scope; PDF8–10 Eqs7–14 | true |
| DL10-D23-002 | 原Eq16定义δβ/δγ为sqrt variance，γ均值/二阶矩在0<γ<π/3的sextant上取。HFBminimum、集体波函数mean和该物理分布的RMS宽度为三个对象；宽度不是实验误差或parameterCI。原Eq13/14的EM矩阵元还需完整集体振幅/局部charge矩阵元，不能只由meanβ/γ给出。 | external-original-shape-statistics-and-EM-definition | directly-read-theory | DL2010 PDF10 Eqs13/14; PDF11 Eq16; PDF17–18 Figs3/4discussion | true |
| DL10-D23-003 | 实际CEA表Z=78,N=108列BMIN=.249/GMIN=15°、BET01=.245/GAM01=20°、DELB01=.053/DELG01=11°。HTML与链接text的完整35字段相同；这是该表的模型预测，非186Pt新测shape、误差条或Au实测γ。它既不是RG2010另一个producer的逐点重现，也没有给S20的23°取值映射；不从20±11把23说成实验CI内已验证。 | external-authored-model-table | directly-read-literal-model-data | CEA HFB-5DCH-table-2009 row Z78 N108 columns4/5/11–14 | true |
| DL10-D23-004 | 该CEA行EHFB=−1472.636、EABS=−1477.107、ECORR=−4.471MeV，字面ECORR=EABS−EHFB，与paperEq15的EHFB−E5DCH反号；可明确对应记号，不因表为负就判非物理。B列tooltip字面e²b²而数值为thousands；paperTableI明确e²fm⁴且Sm152第一B为6671，现CEA62/90同列6736.10不精确相同，故unit/版本映射须保留，未自动输出Pt新physicalB或认证table完全重现paper。 | external-table-sign-unit-and-version-boundary | actual-table-and-original-comparison | CEA Z78 N108 columns3/9/10; CEA Z62 N90 column24; DL2010 PDF10Eq15/PDF15TableI | true |
| DL10-D23-005 | 以该表meanγ=20°、RMS宽11°仅作精确打印值的条件信息练习，固定β时三组正分布都可有相同前两矩，却给〈cos3γ〉约.419335/.389904/.515711，不等由mean单独算的cos60°=.5。因此mean/宽度不足以补非线性形状/EM输入；这些是人工概率构造，不是三组真实Pt波函数、同H本征态或configuration解释，也不裁决Au模式。 | Codex-source-motivated-moment-counterexample | declared-conditional-math | DL2010 PDF11Eq16; CEA Z78 N108 GAM01/DELG01; stated two-point construction below | true |

条件构造可直接复算：μ=20、σ=11，取x=μ−a、y=μ+b、ab=σ²，权重p_x=b/(a+b)、p_y=a/(a+b)。a=11给(9°,31°)、(.5,.5)；a=20给(0°,26.05°)、(.23224568,.76775432)；a=121/40给(16.975°,60°)、(.92969204,.07030796)。均落在同sextant、mean20/variance121；对称例的〈cos3γ〉=cos(3μ)cos(3σ)提供独立解析核对。这里未恢复实际P(β,γ)、β³–cos3γ相关或charge tensor，不能把结果填成有效实验γ/CI。

本次supports将staticminimum与动态mean/宽度分别记账，limits“同名Gogny/γ即同输入”的快捷比较。作者原文对非yrast0+与部分跨带E2/E0失败、2qp缺失和inertia改进也明确，不能将全局平均模型符合度用于本Au具体δ的独立证明。新增needs_review:true，原S20 flags与LW/SP争议保留。

## Day23：公开AD数据点中心与误差向量readiness

在AU20-D23-6红色显示fit的几何提取之后，本次另取同一原Fig3(a,b)中的黑色点中心；不是新增采集、原峰计数或重做作者拟合。冻结的既有raw PDF SHA f348dce9976ad076fd9b1d5281a728e0923053aced33b0270f643d770729366a，PDF4 imagexref88实际1334×1129 PNG，SHA b8d48d938b3dc7a9ef58408a63bc11aeedea08a422bb312b9aac4c6e37a6dcdd。system/scripts/day23_au187_plotted_points.py可从原PDF只读重建tmp图像；该重建已实际运行exit0，无raw写入。预先标记局部窗口，取dark connected component，threshold60/100/140；14点叠图经Codex视觉自审，仍needs_review。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AU20-D23-7 | Fig3(a,b)各可提取7个黑色点中心，三个dark threshold的坐标跨度最大约.365px；它们是公开图示Iγ的像素位置，不是原始net counts或17环各自原记录。原图的左右纵轴分别带10³/10⁴，右轴打印label有rounding；由图标尺得到的nominal ordinate不应冒充精确原强度。 | published-observation-plot-digitization | original-raster-plus-declared-image-analysis | printed052501-4 Fig3(a,b), imagexref88 and nativecenters table below | true |
| AU20-D23-8 | 多数点的完整误差条在原native图中与实心marker重叠；376约58°处有可见stem，但black component bbox并不自动等实验σ。两幅约90°的点被frame部分裁切，其dark centroid也不是精确90°探测器角标。因此本提取不生成pointσ、Poisson模型、Cov、weightedχ²、δ或root权重；sourceTable4.4、自由A2/A4、红fit与本黑点中心仍须分阶段比较。 | plotted-vector-error-response-readiness | actual-raster-scope-and-explicit-boundary | printed052501-4 Fig3(a,b) blackmarkers/errorstems and90degreeframe | true |

下表为native像素(x,y)，只保留一位小数方便再定位；精确算法坐标及threshold区间在任务artifact。y向下，图框原点非物理强度0。最后一行frame裁切，不能用x质心偏左自行改真实探测器角度。

| 点序 | 376.3keV native(x,y) | 461.8keV native(x,y) |
|---|---|---|
| 1 | (224.6,243.0) | (781.4,235.6) |
| 2 | (328.0,241.8) | (885.0,234.0) |
| 3 | (420.6,205.4) | (977.3,184.8) |
| 4 | (469.6,147.4) | (1026.5,144.4) |
| 5 | (538.6,95.4) | (1095.4,89.4) |
| 6 | (599.4,61.4) | (1156.2,41.3) |
| 7 | (657.8,42.0) | (1214.8,24.3) |

五项hash/点数/局部定位/threshold稳定/角序控制通过，只核图像提取；没有对这些点做任何拟合。要进入共同实验likelihood仍需原角组净峰面积、误差/Cov、各组efficiency/归一及gate/response。像素敏感性不当实验CI，原条件大δ支持和新HIRFL小δ冲突均不因这一步被覆盖。新增needs_review:true，原审核flags不变。

## Day23：官方历史归档中的实际参考尺度

本节为外部ENSDF历史记录，不归为S20实验新测。由[ENSDF官方入口](https://www.nndc.bnl.gov/ensdf/)实际导航到[ENSDF Archives](https://www.nndc.bnl.gov/ensdfarchivals/)，再读其ui.js与[真实files.json](https://www.nndc.bnl.gov/ensdfarchivals/distributions/files.json)列出的下载路径。旧猜测/ensarch/实际404已剔，未把归档首页静态placeholder文件名/日期当已下载版本。

实际取得[2004March archive](https://www.nndc.bnl.gov/ensdfarchivals/distributions/dist04/ensdf_0403_293.zip)，5162266bytes/SHA c7cf8128b252d1da5f49821696f9cddad036a4e0ffeefaec3c769c4e05306965，选member ENSDF.186 SHA7c17f7e98958cb9f6ae6f865f7c85f101947fd8c027fb92d85401a43ebba7067；[2009October archive](https://www.nndc.bnl.gov/ensdfarchivals/distributions/dist09/ensdf_0910_199.zip)，16442693bytes/SHA c702ed2120cec8ca1f6000764899de6fdd90d8ac19a4129f8bd6805001ee4f26，选ensdf.186 SHA61398f218e2223b7d0ae0bc8be48e42741b776059870182e8ca7ff981b76683e、ensdf.187 SHAa661d56dee52a4c1174328017ed494fa2423fa819367af4fd13df9e1f7d75cae。只定向读186Pt Adopted/186AuEC目标及187Au Adopted参考clock；未称完整质量链/NDS通读。两包仅tmp暂存，不执行内容、不写raw，正式归档deferred。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PT03-D23-001 | 两archive中的186Pt Adopted目标块逐行相同，header明确Coral M.Baglin、NDS99,1(2003)、CUT4-Apr-2003、200306。191.53(4)keV 2+母态T1/2=260(12)ps，191.53(4)γ为E2、αtot=.422、BE2W=94(5)。2004/2009是快照时间，不能当两次测量/两次新评价；现代2022字段240ps/102WU也不能倒写成这一历史版本。 | actual-historical-evaluation-version-and-target-fields | directly-read-official-archive | dist04ENSDF.186 anddist09ensdf.186, 186PTADOPTED H/L191.53/G191.53/BE2W | true |
| PT03-D23-002 | 同版186AuEC(10.7m) dataset的191.53母态明确T来自1972Fi12，multipolarity另由1970Jo02转换subshell及1985Va07取向约束；目标g=.27(3)来自1996St12 transient-field IMPAC、相对192Pt2+的g=.30(1)。clock/EM身份/g的来源不同，不能把g直接填成oddAu的gR或把其参考标尺当独立再次测量。原1972/1996正文未读。 | historical-per-observable-provenance-and-operator-companion | directly-read-evaluated-record-not-primary | dist04ENSDF.186 186AUEC10.7m L191.53 cL T/gcomments | true |
| PT03-D23-003 | 在声明的Weisskopf定义r0=1.2fm、B_W(E2)=(1/4π)(3/5)²R⁴和1b²=10⁴fm⁴下，历史94WU中央仅作单位换算约.59287e²b²。它未闭合S20引用.84或thesis引用1.44的具体映射；不能因找到2003archive就默称那两个数已核实，也不据差异改actualβ或宣布模式错误。无新τ反演/branch假设/CI。 | conditional-unit-crosscheck-and-quoted-scale-nonclosure | declared-unit-arithmetic-on-historical-field | PT03-D23-001 BE2W; S20printed052501-4 referenceBparagraph; SE21printed128 | true |
| AU09-D23-001 | 2009archive的187Au Adopted为Basunia NDS110,999(2009)、CUT1-Nov-2008；L353.66(13/2−)列56(5)ps、Qt6.08(.31)eb，G233.4 E2/αtot.224、BE2W188(17)，header明确T取1995Wa18RDM。按同WU定义188中央约1.19426e²b²，与已读Walpe原TableII1.18(.12)沿同测量谱系，非新独立一致性确认；S20引1.49仍未闭合。2004archive的Au则是1991旧评价，不能以其不含后来的RDMclock判测量不存在。 | historical-Au-clock-and-scale-lineage | directly-read-official-archive-and-primary-comparison | dist09ensdf.187 187AUADOPTED H/cL T/L353.66/G233.4; Walpeprinted282TableII | true |

本次“旧Baglin2003实际字段尚未取得”的缺口已缩小到具体archive记录，仍未读完整NDS原刊或1972/1996primary response。NSR1996ST12已核身份为A.E.Stuchbery et al., *Measured Magnetic Moments and Shape Coexistence in the Neutron-Deficient Nuclei184,186,188Pt*, PRL76,2246(1996)，DOI10.1103/PhysRevLett.76.2246；这里只作下一原件入口，不拿题名推M1/shape终审。历史94WU与现代102WU都是评价派生的强度字段，同源clock/ICC不能另乘一次likelihood，也不恢复任何WU硬门或旧88倍论证。新增needs_review:true，原reviewflags与源引用原字保留。
